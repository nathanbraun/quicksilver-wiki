"""
Polite, cached access to the Internet Archive's copies of the original wiki.

Every response is cached under .wayback_cache/, so an interrupted run can be
restarted and picks up where it left off. Requests are spaced out, and 429s,
5xx errors and timeouts are retried with exponential backoff. Timing and error
counts are kept in `stats` so we can see how the archive behaves.
"""

import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

CACHE_DIR = ".wayback_cache"
USER_AGENT = "quicksilver-wiki-linkfix/0.1 (https://github.com/nathanbraun/quicksilver-wiki)"
MIN_INTERVAL = 4.5   # seconds between requests; the archive refuses connections above ~15/min
MAX_RETRIES = 8
WIKI_URL = "www.metaweb.com/wiki/wiki.phtml?title="

stats = {'requests': 0, 'cached': 0, 'retries': 0, 'errors': {}, 'seconds': 0.0}
_last_request = 0.0


def _cache_path(kind, key):
    digest = hashlib.sha1(key.encode()).hexdigest()
    return os.path.join(CACHE_DIR, kind, digest[:2], digest)


def _get(url, timeout=120):
    """GET with spacing, retries and backoff. Returns bytes, or None on 404."""
    global _last_request
    for attempt in range(MAX_RETRIES):
        wait = _last_request + MIN_INTERVAL - time.time()
        if wait > 0:
            time.sleep(wait)
        _last_request = time.time()
        stats['requests'] += 1
        try:
            req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                body = resp.read()
            stats['seconds'] += time.time() - _last_request
            return body
        except urllib.error.HTTPError as e:
            stats['seconds'] += time.time() - _last_request
            stats['errors'][e.code] = stats['errors'].get(e.code, 0) + 1
            if e.code == 404:
                return None
            if e.code != 429 and e.code < 500:
                raise
            delay = int(e.headers.get('Retry-After') or 0) or 10 * 2 ** attempt
        except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
            stats['seconds'] += time.time() - _last_request
            name = type(getattr(e, 'reason', e)).__name__
            stats['errors'][name] = stats['errors'].get(name, 0) + 1
            # A refused connection is the archive's rate limit; give it time
            delay = (60 if name == 'ConnectionRefusedError' else 10) * 2 ** attempt
        stats['retries'] += 1
        delay = min(delay, 600)
        print(f"  retrying in {delay}s: {url[:100]}", file=sys.stderr)
        time.sleep(delay)
    raise RuntimeError(f"giving up after {MAX_RETRIES} attempts: {url}")


def _cached(kind, key, fetch):
    path = _cache_path(kind, key)
    if os.path.exists(path):
        stats['cached'] += 1
        with open(path, 'rb') as f:
            return f.read()
    body = fetch()
    if body is not None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path + '.tmp', 'wb') as f:
            f.write(body)
        os.replace(path + '.tmp', path)
    return body


def encode_title(title):
    """MediaWiki URL form of a page title: spaces to underscores, escape the rest."""
    return urllib.parse.quote(title.replace(' ', '_'), safe=":/(),'!*;@$-_.")


def captures(title):
    """Archived 200 captures of a wiki page, as [(timestamp, url)], oldest first.

    Lookups ignore case. Only the page itself and its edit form are kept; the
    prefix query also returns other pages whose titles start with this one.
    """
    # The index returns nothing for queries containing "(", encoded or not, and
    # some titles have stray bytes (%85) after a colon. So query up to the first
    # awkward character or the last colon, and compare full titles here.
    prefix = re.split(r'[()?&#%]', title)[0]
    if ':' in prefix:
        prefix = prefix[:prefix.rindex(':') + 1]
    prefix = encode_title(prefix)
    query = urllib.parse.urlencode({
        'url': WIKI_URL + prefix, 'matchType': 'prefix',
        'filter': 'statuscode:200', 'fl': 'timestamp,original',
    })
    body = _cached('cdx', prefix.lower(), lambda: _get(
        f"https://web.archive.org/cdx/search/cdx?{query}") or b'')
    want = _fold(title)
    out = []
    # Not splitlines(): some archived URLs contain characters it treats as breaks
    for line in body.decode('utf-8', 'replace').split('\n'):
        if ' ' not in line:
            continue
        timestamp, url = line.split(' ', 1)
        params = urllib.parse.parse_qs(urllib.parse.urlsplit(url.replace('&amp;', '&')).query)
        got = params.get('title', [''])[0]
        extra = set(params) - {'title', 'action', 'redirect'}
        if _fold(got) == want and not extra and params.get('action', ['edit'])[0] == 'edit':
            out.append((timestamp, url))
    return out


def _fold(title):
    """Compare titles ignoring case and punctuation (some have stray bytes)."""
    return ' '.join(re.findall(r'[a-z0-9]+', title.lower()))


def snapshot(timestamp, url):
    """The archived page exactly as captured (no Wayback toolbar or rewriting)."""
    key = f"{timestamp}|{url}"
    return _cached('pages', key, lambda: _get(
        f"https://web.archive.org/web/{timestamp}id_/{url}"))


def nearest(caps, target, edit=None):
    """The capture closest in time to `target` (YYYYMMDD...), optionally edit-only."""
    if edit is not None:
        caps = [c for c in caps if ('action=edit' in c[1]) == edit]
    return min(caps, key=lambda c: abs(int(c[0][:8]) - int(target[:8])), default=None)


def report():
    s = stats
    avg = s['seconds'] / max(1, s['requests'])
    return (f"{s['requests']} requests ({s['cached']} cached), {s['retries']} retries, "
            f"errors {json.dumps(s['errors'])}, avg {avg:.1f}s/request")
