"""
Clean up remaining broken archive.org image references.

For images we couldn't download, remove the broken markdown image tags
rather than leaving them pointing to dead archive.org URLs.
"""

import re
import os
import glob

DOCS_DIR = "docs"

# Match image syntax with archive.org paths that weren't fixed
# Handles: ![alt](/web/...) and [![alt](/web/...)](link)
BROKEN_IMG_RE = re.compile(
    r'!?\[([^\]]*)\]\(/web/\d+im_/[^)]+\)'
)


def count_remaining():
    """Count files still referencing archive.org images."""
    count = 0
    files = []
    for filepath in glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        matches = BROKEN_IMG_RE.findall(content)
        if matches:
            count += len(matches)
            files.append((filepath, len(matches)))
    return count, files


def remove_broken_images(filepath):
    """Remove broken archive.org image references from a file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove linked images: [![alt](/web/...)](link) -> empty
    content = re.sub(
        r'\[!\[[^\]]*\]\(/web/\d+im_/[^)]+\)\]\([^)]+\)',
        '',
        content
    )

    # Remove standalone images: ![alt](/web/...) -> empty
    content = re.sub(
        r'!\[[^\]]*\]\(/web/\d+im_/[^)]+\)',
        '',
        content
    )

    # Clean up leftover empty lines (max 2 consecutive)
    content = re.sub(r'\n{3,}', '\n\n', content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    count, files = count_remaining()
    print(f"Found {count} remaining broken archive.org image refs in {len(files)} files")

    for filepath, n in sorted(files):
        remove_broken_images(filepath)
        print(f"  Cleaned {n:3d} refs in {filepath}")

    # Verify
    count2, _ = count_remaining()
    print(f"\nRemaining broken refs: {count2}")


if __name__ == "__main__":
    main()
