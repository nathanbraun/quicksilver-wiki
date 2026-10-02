"""
Remove link spam left over from the original wiki.

Two kinds of spam survived the scrape:

1. A blob pasted in front of a page's real content:
     ... no changes ... no changes ... Thanks!!! Links: <a href='...'>yellow
     pages main</a> : ... [http://www.dirare.com|online directory] This is ...
   The blob is cut out and the rest of the line is kept.

2. Pages whose archived revision was overwritten entirely by spam: one huge
   line of pharmacy/ringtone links. The spam line is removed.

Pages left with no content get a short note instead, so the pages that link to
them still work. The original text may be recoverable from earlier snapshots.
"""

import glob
import os
import re

DOCS_DIR = "docs"

BLOB_RE = re.compile(
    r'(?:\.\.\. no changes )*\.\.\. Thanks!!! Links: .*?'
    r'\[http://www\.(?:dirare|areaseo)\.com\|(?:online directory|google pr)\] ?'
)

LINK_RE = re.compile(r'\[((?:[^\[\]\\]|\\.)*)\]\(([^)\s]+)\)')
SPAM_WORDS = re.compile(
    r'\b(actos|adderall|adipex|ambien|carisoprodol|cialis|hydrocodone|levitra|'
    r'lorcet|lortab|meridia|phentermine|ringtones?|soma|tramadol|valium|viagra|'
    r'vigrx|xanax|zocor|zoloft)\b', re.I)

PLACEHOLDER = ("*The archived copy of this page had been overwritten by spam, so "
               "its original content is missing. The spam has been removed.*")


def is_spam_line(line):
    """A line of many links, padded with pharmacy/ringtone keywords."""
    links = LINK_RE.findall(line)
    return len(links) >= 20 and len(SPAM_WORDS.findall(line)) >= len(links) / 2


def clean(content):
    lines = content.split('\n')
    # Keep the "# Title / From the Quicksilver Metaweb." header intact
    header_end = next((i + 1 for i, line in enumerate(lines[:8])
                       if line.startswith('From the Quicksilver Metaweb')), 0)
    header, body = lines[:header_end], lines[header_end:]

    new_body = [BLOB_RE.sub('', line) for line in body]
    new_body = [line for line in new_body if not is_spam_line(line)]
    if new_body == body:
        return content

    if not ''.join(new_body).strip():
        new_body = ['', PLACEHOLDER, '']
    body = new_body
    return '\n'.join(header + body)


def main():
    md_files = sorted(glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True))
    cleaned, emptied = [], []
    for path in md_files:
        with open(path, encoding='utf-8') as f:
            content = f.read()
        new = clean(content)
        if new != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new)
            (emptied if PLACEHOLDER in new else cleaned).append(path)

    print(f"Removed spam from {len(cleaned)} pages:")
    for path in cleaned:
        print(f"  {path}")
    print(f"\nReplaced {len(emptied)} spam-only pages with a placeholder:")
    for path in emptied:
        print(f"  {path}")


if __name__ == "__main__":
    main()
