"""
Handle stub "Redirected" pages.

Pages that are in mkdocs.yml redirect_maps are fine (plugin handles them).
Orphaned stubs with no redirect target should be deleted — they just show
"Redirected" with no actual redirect.
"""

import os
import re
import glob

DOCS_DIR = "docs"
MKDOCS_YML = "mkdocs.yml"


def get_redirect_sources():
    """Get all source files from mkdocs.yml redirect_maps."""
    with open(MKDOCS_YML, 'r') as f:
        content = f.read()

    sources = set()
    # Match lines like: 'source.md': 'target.md'
    for match in re.finditer(r"^\s+'([^']+\.md)'\s*:", content, re.MULTILINE):
        sources.add(match.group(1))
    return sources


def find_pure_stubs():
    """Find files whose entire content is just 'Redirected'."""
    stubs = []
    for filepath in glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        if content == 'Redirected':
            # Get path relative to docs dir
            rel = os.path.relpath(filepath, DOCS_DIR)
            stubs.append(rel)
    return stubs


def main():
    redirect_sources = get_redirect_sources()
    stubs = find_pure_stubs()

    has_redirect = []
    orphaned = []

    for stub in stubs:
        if stub in redirect_sources:
            has_redirect.append(stub)
        else:
            orphaned.append(stub)

    print(f"Total pure 'Redirected' stubs: {len(stubs)}")
    print(f"  With redirect_maps entry (OK): {len(has_redirect)}")
    print(f"  Orphaned (no redirect):         {len(orphaned)}")

    if orphaned:
        print(f"\nDeleting {len(orphaned)} orphaned stubs...")
        for stub in sorted(orphaned):
            filepath = os.path.join(DOCS_DIR, stub)
            os.remove(filepath)
            print(f"  Deleted {filepath}")

    print("\nDone.")


if __name__ == "__main__":
    main()
