"""
Fix the Wikipedia links fix_wikipedia_titles.py couldn't, using the archived
original pages.

Some titles can't be recovered from the mangled slug: the article was renamed,
the slug has a typo, or the scrape cut the title short ("Group_(mathematics)"
became "group", which now lands on a disambiguation page). The Internet Archive
still has the original pages, with the real link targets.

For each page with a link that doesn't resolve, or that lands on a
disambiguation page, this fetches the archived page nearest the scrape date,
finds the matching original link (same text, compatible title), and checks that
title against today's Wikipedia. A link is only changed when the original
points somewhere else and that page still exists.

Archive responses are cached in .wayback_cache/, so it can be interrupted and
re-run.

Usage:
  python fix_wikipedia_from_archive.py [--dry-run] [--report report.tsv]
"""

import argparse
import glob
import html
import os
import re
import sys
import time
import urllib.parse

import wayback
from fix_wikipedia_titles import (CACHE_FILE, LINK_RE, TitleResolver, fold,
                                  make_url, parse_wikipedia_url)

DOCS_DIR = "docs"
SCRAPE_DATE = "20060725"   # the image URLs in docs/ point at captures from this day
MAX_SNAPSHOTS = 3          # try this many captures per page before giving up

ANCHOR_RE = re.compile(
    r'''<a\s+href=(['"])(https?://[^'"]*wikipedia\.org/wiki/[^'"]+)\1[^>]*>(.*?)</a>''',
    re.S | re.I)


def page_title(content):
    m = re.search(r'^# (.+)$', content, re.M)
    return m.group(1).strip() if m else None


def decode(body):
    """Archived pages are UTF-8 or Windows-1252, depending on age."""
    try:
        return body.decode('utf-8')
    except UnicodeDecodeError:
        return body.decode('cp1252', 'replace')


def legacy_anchor(fragment):
    """Decode 2006-style section anchors: "Superman.27s_abilities" -> "Superman's abilities"."""
    fragment = urllib.parse.unquote(fragment.lstrip('#'))
    fragment = re.sub(r'\.([2-7][0-9A-F])', lambda m: chr(int(m.group(1), 16))
                      if not chr(int(m.group(1), 16)).isalnum() else m.group(0), fragment)
    return fragment.replace('_', ' ')


def original_links(page_html):
    """[(site, title, fragment, text)] for every Wikipedia link on an archived page."""
    out = []
    for _, href, inner in ANCHOR_RE.findall(page_html):
        parsed = parse_wikipedia_url(html.unescape(href))
        if parsed:
            site, title, fragment = parsed
            text = html.unescape(re.sub(r'<[^>]+>', '', inner))
            out.append((site, title.replace('_', ' '), legacy_anchor(fragment), text))
    return out


def text_matches(md_text, orig_text, orig_title):
    md = fold(md_text.replace('\\', ''))
    if md == fold(orig_text):
        return 2
    words = set(fold(orig_text).split()) | set(fold(orig_title).split())
    return 1 if md and set(md.split()) <= words else 0


def title_compatible(slug, orig_title, orig_fragment):
    """The slug is the original title (and section), or the start of it.

    The scrape cut some titles short ("Group_(mathematics)" became "group") and
    merged others with their section ("Term_logic#Syllogistic_maxims" became
    "term-logic-syllogistic-maxims").
    """
    s = fold(slug).split()
    t = fold(f"{orig_title} {orig_fragment}").split()
    return bool(s) and t[:len(s)] == s


def find_original(site, slug, md_text, originals):
    """The original (title, fragment) for a link, or None if missing or ambiguous."""
    same_site = [o for o in originals if o[0] == site]
    scored = [(text_matches(md_text, o_text, o_title), (o_title, o_frag))
              for _, o_title, o_frag, o_text in same_site
              if title_compatible(slug, o_title, o_frag)]
    scored = [s for s in scored if s[0]]
    if not scored:
        # The slug may already have been rewritten to a current title by
        # fix_wikipedia_titles.py; fall back to an exact, unambiguous text match
        scored = [(2, (o_title, o_frag)) for _, o_title, o_frag, o_text in same_site
                  if text_matches(md_text, o_text, o_title) == 2]
    if not scored:
        return None
    best = max(score for score, _ in scored)
    found = {t for score, t in scored if score == best}
    return found.pop() if len(found) == 1 else None


def current_section(resolver, site, title, section):
    """The page's current anchor for a 2006 section name, or '' if it's gone."""
    key = f"sections|{site}|{title}"
    if key not in resolver.cache:
        result = resolver._api(site, {'action': 'parse', 'page': title, 'prop': 'sections'})
        resolver.cache[key] = [(s['line'], s['anchor'])
                               for s in result.get('parse', {}).get('sections', [])]
        resolver.save()
    want = fold(section)
    return next((anchor for line, anchor in resolver.cache[key]
                 if fold(re.sub(r'<[^>]+>', '', line)) == want), '')


def target_links(resolver, content):
    """Links on a page that don't resolve or land on a disambiguation page."""
    out = []
    for text, url in LINK_RE.findall(content):
        parsed = parse_wikipedia_url(url)
        if not parsed:
            continue
        site, slug, _ = parsed
        hit = resolver.get(site, slug) or resolver.get(site, slug.replace('_', ' '))
        if not hit or hit['disambig']:
            out.append((text, url, site, slug, 'unresolved' if not hit else 'disambig'))
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--report', help='write a TSV of every target link and its outcome')
    args = parser.parse_args()

    resolver = TitleResolver(CACHE_FILE)
    md_files = sorted(glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True))
    contents = {}
    by_site = {}
    for path in md_files:
        with open(path, encoding='utf-8') as f:
            contents[path] = f.read()
        for _, url in LINK_RE.findall(contents[path]):
            parsed = parse_wikipedia_url(url)
            if parsed:
                site, slug, _ = parsed
                by_site.setdefault(site, set()).update([slug, slug.replace('_', ' ')])
    for site, titles in by_site.items():
        resolver.prefetch(site, titles)

    pages = {}
    for path, content in contents.items():
        targets = target_links(resolver, content)
        if targets:
            pages[path] = (content, targets)
    print(f"{sum(len(t) for _, t in pages.values())} target links on {len(pages)} pages",
          file=sys.stderr)

    # Find the original title of each target link in the archive
    found = {}      # (path, url, text) -> original title
    outcome = {}    # (path, url, text) -> reason it wasn't found
    started = time.time()
    for i, (path, (content, targets)) in enumerate(pages.items(), 1):
        title = page_title(content)
        caps = wayback.captures(title) if title else []
        caps = [c for c in caps if 'action=' not in c[1]]
        caps.sort(key=lambda c: abs(int(c[0][:8]) - int(SCRAPE_DATE)))
        todo = list(targets)
        for timestamp, url in caps[:MAX_SNAPSHOTS]:
            body = wayback.snapshot(timestamp, url)
            originals = original_links(decode(body)) if body else []
            still = []
            for t in todo:
                text, md_url, site, slug, _ = t
                orig = find_original(site, slug, text, originals)
                if orig:
                    found[(path, md_url, text)] = (site, *orig)
                else:
                    still.append(t)
            todo = still
            if not todo:
                break
        for text, md_url, *_ in todo:
            outcome[(path, md_url, text)] = 'no capture' if not caps else 'no match in archive'
        print(f"  [{i}/{len(pages)}] {len(targets) - len(todo)}/{len(targets)} found  "
              f"{path}  ({wayback.report()}, {time.time() - started:.0f}s)", file=sys.stderr)

    # Check the original titles against today's Wikipedia
    by_site = {}
    for site, orig, _ in found.values():
        by_site.setdefault(site, set()).add(orig)
    for site, titles in by_site.items():
        resolver.prefetch(site, titles)

    rows, changed_files, changed_links = [], 0, 0
    for path, (content, targets) in pages.items():
        new_content = content
        for text, md_url, site, slug, kind in targets:
            key = (path, md_url, text)
            new_url = ''
            if key in found:
                _, orig, fragment = found[key]
                hit = resolver.get(site, orig)
                current = resolver.get(site, slug) or resolver.get(site, slug.replace('_', ' '))
                if not hit:
                    outcome[key] = f'original "{orig}" no longer on Wikipedia'
                elif hit['disambig']:
                    outcome[key] = f'original "{orig}" is a disambiguation page'
                elif current and current['title'] == hit['title']:
                    outcome[key] = 'already correct'
                else:
                    # 2006 section names mostly no longer exist; keep only live ones
                    section = (current_section(resolver, site, hit['title'], fragment)
                               if fragment else hit['fragment'])
                    new_url = make_url(site, hit['title'], section)
                    outcome[key] = f'fixed from "{orig}"'
            if new_url:
                old = f"[{text}]({md_url})"
                new_content = new_content.replace(old, f"[{text}]({new_url})")
            rows.append((kind, outcome[key], path, text, md_url, new_url))
        if new_content != content:
            changed_files += 1
            changed_links += sum(1 for r in rows if r[2] == path and r[5])
            if not args.dry_run:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

    if args.report:
        with open(args.report, 'w', encoding='utf-8') as f:
            f.write("kind\toutcome\tfile\ttext\told\tnew\n")
            for row in rows:
                f.write('\t'.join(c.replace('\t', ' ') for c in row) + '\n')

    summary = {}
    for _, result, *_ in rows:
        key = re.sub(r'"[^"]*"', '…', result)
        summary[key] = summary.get(key, 0) + 1
    for key, n in sorted(summary.items(), key=lambda x: -x[1]):
        print(f"  {n:5d} {key}")
    print(f"\n{'Would change' if args.dry_run else 'Changed'} {changed_links} links "
          f"across {changed_files} files")
    print(f"Archive: {wayback.report()}, {time.time() - started:.0f}s total")


if __name__ == "__main__":
    main()
