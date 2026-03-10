"""
Fix broken external links in markdown files.

During the original scrape, URLs like:
  https://en.wikipedia.org/wiki/Mosquito
became:
  /http-en-wikipedia-org-wiki-mosquito

This script reverses that for Wikipedia links (high confidence) and
does best-effort reconstruction for other URLs.
"""

import re
import os
import glob

DOCS_DIR = "docs"

# Pattern: markdown link targets starting with /http- or /https-
BROKEN_LINK_RE = re.compile(r'\]\((/https?-[^)]+)\)')

def fix_wikipedia_url(mangled):
    """Fix Wikipedia URLs where the structure is known."""
    # Remove leading /
    s = mangled.lstrip('/')

    # Determine protocol
    if s.startswith('https-'):
        s = s[6:]  # remove 'https-'
    elif s.startswith('http-'):
        s = s[5:]  # remove 'http-'

    # Match wikipedia patterns:
    # en-wikipedia-org-wiki-PAGE
    # en2-wikipedia-org-wiki-PAGE
    # www-wikipedia-org-wiki-PAGE
    # es-wikipedia-org-wiki-PAGE
    wiki_match = re.match(r'([\w]+)-wikipedia-org-wiki-(.*)', s)
    if wiki_match:
        subdomain = wiki_match.group(1)
        page = wiki_match.group(2)
        # en2 was just an old mirror, use en
        if subdomain == 'en2':
            subdomain = 'en'
        elif subdomain == 'www':
            subdomain = 'en'
        # Wikipedia page names use underscores for spaces
        # The hyphens here likely replaced underscores/spaces
        # Leave hyphens as-is; Wikipedia handles them via redirects
        return f"https://{subdomain}.wikipedia.org/wiki/{page}"

    # meta-wikipedia-org pattern
    meta_match = re.match(r'meta-wikipedia-org-(.*)', s)
    if meta_match:
        path = meta_match.group(1).replace('-', '/', 1)
        return f"https://meta.wikipedia.org/{path}"

    return None


# Common TLD patterns to help reconstruct domains
TLDS = [
    '-co-uk-', '-org-uk-', '-ac-uk-',
    '-com-', '-org-', '-net-', '-edu-', '-gov-', '-info-', '-io-',
    '-co-uk', '-org-uk', '-ac-uk',
    '-com', '-org', '-net', '-edu', '-gov', '-info', '-io',
]


def fix_generic_url(mangled):
    """Best-effort fix for non-Wikipedia URLs."""
    s = mangled.lstrip('/')

    if s.startswith('https-'):
        protocol = 'https://'
        s = s[6:]
    elif s.startswith('http-'):
        protocol = 'http://'
        s = s[5:]
    else:
        return None

    # Remove www- prefix, track it
    has_www = s.startswith('www-')
    if has_www:
        s = s[4:]

    # Try to find the TLD boundary
    for tld in TLDS:
        idx = s.find(tld)
        if idx >= 0:
            # Domain is everything up to and including TLD
            domain_part = s[:idx]
            tld_clean = tld.strip('-')

            # The domain part has dots replaced with hyphens
            # This is ambiguous but domains with hyphens are less common
            domain = domain_part.replace('-', '.')
            domain = f"{'www.' if has_www else ''}{domain}.{tld_clean.replace('-', '.')}"

            # Path is everything after TLD
            path = s[idx + len(tld):]
            if path:
                # Fix common file extensions at end of path
                path = re.sub(r'-html?$', lambda m: '.' + m.group(0)[1:], path)
                path = re.sub(r'-php$', '.php', path)
                path = re.sub(r'-asp$', '.asp', path)
                path = re.sub(r'-pdf$', '.pdf', path)
                path = re.sub(r'-txt$', '.txt', path)
                path = re.sub(r'-jpg$', '.jpg', path)
                path = re.sub(r'-png$', '.png', path)
                path = re.sub(r'-gif$', '.gif', path)
                path = '/' + path
            return f"{protocol}{domain}{path}"

    return None


def fix_link(match):
    """Fix a single broken link match."""
    original = match.group(1)

    # Try Wikipedia first
    fixed = fix_wikipedia_url(original)
    if fixed:
        return f"]({fixed})"

    # Try generic
    fixed = fix_generic_url(original)
    if fixed:
        return f"]({fixed})"

    # Can't fix — leave as-is
    return match.group(0)


def process_file(filepath):
    """Process a single markdown file, return (changed, num_fixes)."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content, count = BROKEN_LINK_RE.subn(fix_link, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True, count
    return False, 0


def main():
    md_files = glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True)
    total_files_changed = 0
    total_links_fixed = 0

    for filepath in sorted(md_files):
        changed, count = process_file(filepath)
        if changed:
            total_files_changed += 1
            total_links_fixed += count
            print(f"  Fixed {count:3d} links in {filepath}")

    print(f"\nDone: fixed {total_links_fixed} links across {total_files_changed} files")


if __name__ == "__main__":
    main()
