"""
Fix Wikipedia links whose page titles were mangled during the scrape.

fix_links.py restored the domain of Wikipedia links, but the titles are still
lowercased and hyphenated:
  https://en.wikipedia.org/wiki/alan-kay
Wikipedia only normalizes the first letter, so most of these 404. The real
title is:
  https://en.wikipedia.org/wiki/Alan_Kay

For each link, this script builds candidate titles (from the slug and the link
text) and checks them against the Wikipedia API, preferring real articles over
disambiguation pages. Links whose slug already resolves are left alone.

Usage:
  python fix_wikipedia_titles.py [--dry-run] [--report report.tsv]
"""

import argparse
import glob
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request

DOCS_DIR = "docs"
CACHE_FILE = ".wikipedia_title_cache.json"
USER_AGENT = "quicksilver-wiki-linkfix/0.1 (https://github.com/nathanbraun/quicksilver-wiki)"

LINK_RE = re.compile(r'\[((?:[^\[\]\\]|\\.)*)\]\((https?://[^)\s]+)\)')

# (url regex, site the title lives on)
URL_PATTERNS = [
    (re.compile(r'https?://(?:en|en2|www)\.wikipedia\.org/wiki/([^#]+)(#.*)?$'), 'en.wikipedia.org'),
    (re.compile(r'https?://(?:www\.)?wikipedia\.org/wiki[-/]([^#]+)(#.*)?$'), 'en.wikipedia.org'),
    (re.compile(r'https?://simple\.wikipedia\.org/wiki/([^#]+)(#.*)?$'), 'simple.wikipedia.org'),
    (re.compile(r'https?://de\.wikipedia\.org/wiki/([^#]+)(#.*)?$'), 'de.wikipedia.org'),
    (re.compile(r'https?://quote\.wikipedia\.org/wiki/([^#]+)(#.*)?$'), 'en.wikiquote.org'),
    (re.compile(r'https?://meta\.wiki[pm]edia\.org/wiki/([^#]+)(#.*)?$'), 'meta.wikimedia.org'),
]

# Link text that is itself a Wikipedia URL is the most reliable source
TEXT_URL_RE = re.compile(r'https?://(?:en\.)?wikipedia\.org/wiki/(\S+)$')

SMALL_WORDS = {'a', 'an', 'and', 'at', 'by', 'de', 'des', 'du', 'for', 'in',
               'la', 'le', 'of', 'on', 'or', 'the', 'to', 'van', 'von'}
ACRONYMS = {'uss', 'hms', 'hmas', 'hmcs', 'sms', 'rms', 'cia', 'nasa', 'fbi', 'us',
            'uk', 'usa', 'ussr', 'dna', 'ibm', 'nsa', 'mit', 'bbc', 'ii', 'iii', 'iv'}
NAMESPACES = {'category', 'user', 'talk', 'template', 'image', 'wikipedia', 'help'}


def parse_wikipedia_url(url):
    for pattern, site in URL_PATTERNS:
        m = pattern.match(url)
        if m:
            return site, urllib.parse.unquote(m.group(1)), m.group(2) or ''
    return None


def title_case(words):
    return ' '.join(w.upper() if w in ACRONYMS
                    else w if (i and w in SMALL_WORDS)
                    else w[:1].upper() + w[1:]
                    for i, w in enumerate(words))


def tokens(s):
    return set(re.findall(r'[a-z0-9]+', s.lower()))


def fold(s):
    """Lowercase, strip accents and punctuation: "Qur'an" -> "qur an"."""
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode()
    return ' '.join(re.findall(r'[a-z0-9]+', s.lower()))


def similar(title, slug):
    """True if a title and a slug share most of their words, both ways."""
    a, b = tokens(title), tokens(slug)
    common = len(a & b)
    return bool(a and b) and common / len(a) >= 0.5 and common / len(b) >= 0.5


def slug_candidates(slug):
    """Candidate titles from a mangled slug, most likely first."""
    s = re.sub(r'[-_]+', ' ', slug).strip()
    s = re.sub(r"(\w) s\b", r"\1's", s)  # boyle-s-law -> boyle's law
    words = s.split()
    if not words:
        return []

    out = [slug, s, title_case(words)]

    # Ship hull numbers: uss-yorktown-cv-5 -> USS Yorktown (CV-5)
    m = re.match(r'(.+?)[-_]([a-z]{1,4})[-_](\d+)$', slug)
    if m:
        head = re.sub(r'[-_]+', ' ', m.group(1)).split()
        out.append(f"{title_case(head)} ({m.group(2).upper()}-{m.group(3)})")

    # Namespaced pages: category-titans -> Category:Titans
    if words[0] in NAMESPACES and len(words) > 1:
        rest = words[1:]
        out += [f"{words[0].capitalize()}:{' '.join(rest)}",
                f"{words[0].capitalize()}:{title_case(rest)}"]

    # Disambiguated titles: canon-music -> Canon (music)
    for k in (1, 2):
        if len(words) > k:
            head, qual = words[:-k], ' '.join(words[-k:])
            out += [f"{' '.join(head)} ({qual})", f"{title_case(head)} ({qual})",
                    f"{title_case(head)} ({title_case(qual.split())})"]

    return out


def text_candidates(text):
    """Candidate titles from the link text."""
    t = text.replace('\\', '').strip()
    m = TEXT_URL_RE.match(t)
    if m:
        return [urllib.parse.unquote(m.group(1))]
    t = re.sub(r'[*`]', '', t)
    t = re.sub(r'^(wikipedia|the wikipedia entry for( the)?)\s*:?\s*', '', t, flags=re.I)
    t = re.sub(r'\s*(\(wikipedia\)|at wikipedia(\.org)?)$', '', t, flags=re.I)
    if not t or len(t) > 100 or t.startswith('http'):
        return []
    return [t]


class TitleResolver:
    """Resolves candidate titles via the MediaWiki API, with an on-disk cache."""

    def __init__(self, cache_file):
        self.cache_file = cache_file
        self.cache = {}
        if os.path.exists(cache_file):
            with open(cache_file) as f:
                self.cache = json.load(f)

    def save(self):
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f, indent=1, ensure_ascii=False)

    def prefetch(self, site, titles):
        todo = sorted({t for t in titles
                       if f"{site}|{t}" not in self.cache
                       and not re.search(r'[|\[\]{}<>#]', t)})
        for i in range(0, len(todo), 50):
            self._query(site, todo[i:i + 50])
            print(f"  {site}: {min(i + 50, len(todo))}/{len(todo)}", file=sys.stderr)
        self.save()

    def _api(self, site, params):
        data = urllib.parse.urlencode({'format': 'json', **params}).encode()
        req = urllib.request.Request(f"https://{site}/w/api.php", data=data,
                                     headers={'User-Agent': USER_AGENT})
        for attempt in range(8):
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    result = json.load(resp)
                break
            except urllib.error.HTTPError as e:
                if e.code != 429:
                    raise
                time.sleep(5 * (attempt + 1))
        else:
            raise RuntimeError(f"rate limited by {site}")
        time.sleep(1)
        if 'error' in result:
            raise RuntimeError(f"{site}: {result['error']}")
        return result

    def search(self, site, slugs):
        """Find titles that equal a slug up to case, punctuation and accents."""
        todo = sorted({s for s in slugs if f"search|{site}|{s}" not in self.cache})
        for i, slug in enumerate(todo):
            query = re.sub(r'[-_]+', ' ', slug)
            _, titles, _, _ = self._api(site, {'action': 'opensearch', 'search': query,
                                               'limit': 10, 'redirects': 'resolve'})
            self.cache[f"search|{site}|{slug}"] = next(
                (t for t in titles if fold(t) == fold(query)), None)
            if i % 25 == 24:
                print(f"  {site} search: {i + 1}/{len(todo)}", file=sys.stderr)
                self.save()
        self.save()
        self.prefetch(site, [self.cache[f"search|{site}|{s}"] for s in slugs
                             if self.cache.get(f"search|{site}|{s}")])

    def searched(self, site, slug):
        title = self.cache.get(f"search|{site}|{slug}")
        return title and self.get(site, title)

    def _query(self, site, titles):
        result = self._api(site, {
            'action': 'query', 'redirects': 1,
            'prop': 'pageprops', 'ppprop': 'disambiguation',
            'titles': '|'.join(titles),
        })
        q = result['query']
        normalized = {n['from']: n['to'] for n in q.get('normalized', [])}
        redirects = {r['from']: (r['to'], r.get('tofragment', '')) for r in q.get('redirects', [])}
        pages = {p['title']: p for p in q.get('pages', {}).values()}
        for t in titles:
            n = normalized.get(t, t)
            target, fragment = redirects.get(n, (n, ''))
            page = pages.get(target)
            if not page or 'missing' in page or 'invalid' in page:
                self.cache[f"{site}|{t}"] = None
            else:
                self.cache[f"{site}|{t}"] = {
                    'title': target,
                    'fragment': fragment,
                    'disambig': 'disambiguation' in page.get('pageprops', {}),
                }

    def get(self, site, title):
        return self.cache.get(f"{site}|{title}")


def resolve(resolver, site, slug, text):
    """Return (resolution, how) or (None, reason)."""
    from_text_url = text_candidates(text) if TEXT_URL_RE.match(text.replace('\\', '').strip()) else []
    for t in from_text_url:
        hit = resolver.get(site, t)
        if hit:
            return hit, 'text-url'

    found = [(c, resolver.get(site, c)) for c in slug_candidates(slug)]
    found = [(c, h) for c, h in found if h]
    articles = [(c, h) for c, h in found if not h['disambig']]
    if articles:
        return articles[0][1], 'slug-as-is' if articles[0][0] == slug else 'slug'

    hit = resolver.searched(site, slug)
    if hit and not hit['disambig']:
        return hit, 'search'

    for t in text_candidates(text):
        hit = resolver.get(site, t)
        if hit and not hit['disambig'] and similar(hit['title'], slug):
            # A generic page from the text shouldn't beat the slug's own
            # disambiguation page: family-biology -> "Family" is wrong
            if found and not tokens(slug) <= tokens(hit['title']):
                break
            return hit, 'text'

    if found:
        return found[0][1], 'slug-as-is' if found[0][0] == slug else 'disambig'
    return None, 'unresolved'


def encode(s):
    """Wikipedia-style path: spaces to underscores, escape what breaks markdown."""
    return ''.join({' ': '_', '(': '%28', ')': '%29', '?': '%3F', '%': '%25', '"': '%22'}.get(ch, ch)
                   for ch in s)


def make_url(site, title, fragment):
    return f"https://{site}/wiki/{encode(title)}" + (f"#{encode(fragment)}" if fragment else '')


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--report', help='write a TSV of every changed/unresolved link')
    args = parser.parse_args()

    md_files = sorted(glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True))
    contents = {}
    links = []  # (site, slug, anchor, text)
    for path in md_files:
        with open(path, encoding='utf-8') as f:
            contents[path] = f.read()
        for text, url in LINK_RE.findall(contents[path]):
            parsed = parse_wikipedia_url(url)
            if parsed:
                links.append((*parsed, text))

    resolver = TitleResolver(CACHE_FILE)
    by_site = {}
    for site, slug, _, text in links:
        by_site.setdefault(site, set()).update(slug_candidates(slug) + text_candidates(text))
    for site, titles in by_site.items():
        resolver.prefetch(site, titles)

    # Titles with mixed case ("Japanese aircraft carrier Akagi") can't be
    # guessed from the slug, so search for whatever is still unresolved
    by_site = {}
    for site, slug, _, text in links:
        if resolve(resolver, site, slug, text)[1] not in ('slug', 'slug-as-is', 'text-url'):
            by_site.setdefault(site, set()).add(slug)
    for site, slugs in by_site.items():
        resolver.search(site, slugs)

    report = []
    stats = {}

    def fix(m):
        text, url = m.group(1), m.group(2)
        parsed = parse_wikipedia_url(url)
        if not parsed:
            return m.group(0)
        site, slug, anchor = parsed
        hit, how = resolve(resolver, site, slug, text)
        new_url = url
        if hit and not (how == 'slug-as-is' and url.startswith(f"https://{site}/")):
            new_url = make_url(site, hit['title'], anchor.lstrip('#') or hit['fragment'])
        stats[how] = stats.get(how, 0) + 1
        if new_url != url or not hit:
            report.append((how, current_file, text, url, new_url if hit else ''))
        return f"[{text}]({new_url})"

    files_changed = 0
    for path in md_files:
        current_file = path
        new = LINK_RE.sub(fix, contents[path])
        if new != contents[path]:
            files_changed += 1
            if not args.dry_run:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new)

    if args.report:
        with open(args.report, 'w', encoding='utf-8') as f:
            f.write("how\tfile\ttext\told\tnew\n")
            for row in report:
                f.write('\t'.join(c.replace('\t', ' ') for c in row) + '\n')

    for how, n in sorted(stats.items(), key=lambda x: -x[1]):
        print(f"  {n:5d} {how}")
    print(f"\n{'Would change' if args.dry_run else 'Changed'} "
          f"{sum(1 for r in report if r[4])} links across {files_changed} files")


if __name__ == "__main__":
    main()
