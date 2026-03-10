"""
Fix broken archive.org image links.

Images reference paths like:
  /web/20060725165628im_/http://www.metaweb.com/wiki/upload/b/b5/Spouts.jpg

This script:
1. Finds all archive.org image references in markdown
2. Tries to download them from the Internet Archive
3. Saves locally to docs/images/
4. Updates the markdown to use local paths
"""

import re
import os
import glob
import urllib.request
import urllib.error
import time

DOCS_DIR = "docs"
IMAGES_DIR = os.path.join(DOCS_DIR, "images")

# Match archive.org image paths in markdown image syntax
# Handles both ![alt](/web/...) and [![alt](/web/...)](link)
ARCHIVE_IMG_RE = re.compile(
    r'(/web/\d+im_/https?://[^)\s]+)'
)


def extract_filename(url):
    """Extract the filename from an archive.org image URL."""
    # URL like: /web/20060725165628im_/http://www.metaweb.com/wiki/upload/b/b5/Spouts.jpg
    # We want: Spouts.jpg
    parts = url.split('/')
    filename = parts[-1]
    # Clean up any query params
    filename = filename.split('?')[0]
    return filename


def build_archive_url(path):
    """Build a full archive.org URL from the path."""
    return f"https://web.archive.org{path}"


def download_image(url, local_path):
    """Try to download an image. Returns True on success."""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (quicksilver-wiki image recovery)'
        })
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = resp.read()
            # Basic sanity check - should be at least a few hundred bytes
            if len(data) < 100:
                return False
            with open(local_path, 'wb') as f:
                f.write(data)
            return True
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as e:
        return False


def main():
    os.makedirs(IMAGES_DIR, exist_ok=True)

    # Collect all unique archive image paths
    all_refs = {}  # path -> set of files that reference it
    for filepath in glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        for match in ARCHIVE_IMG_RE.finditer(content):
            path = match.group(1)
            if path not in all_refs:
                all_refs[path] = set()
            all_refs[path].add(filepath)

    print(f"Found {len(all_refs)} unique archive.org image references")
    print(f"across {len(set(f for files in all_refs.values() for f in files))} files")

    downloaded = 0
    failed = 0
    already_local = 0
    skipped_dup = 0

    # Track filename -> archive path to handle duplicates
    filename_map = {}

    for i, (path, files) in enumerate(sorted(all_refs.items())):
        filename = extract_filename(path)
        local_path = os.path.join(IMAGES_DIR, filename)

        if os.path.exists(local_path):
            already_local += 1
            filename_map[path] = filename
            continue

        if filename in filename_map.values():
            # Different archive path, same filename - skip to avoid overwriting
            skipped_dup += 1
            continue

        url = build_archive_url(path)
        print(f"  [{i+1}/{len(all_refs)}] Downloading {filename}...", end=" ", flush=True)

        if download_image(url, local_path):
            print("OK")
            downloaded += 1
            filename_map[path] = filename
        else:
            print("FAILED")
            failed += 1

        # Be polite to archive.org
        time.sleep(0.3)

    print(f"\nDownloads: {downloaded} new, {already_local} already existed, "
          f"{failed} failed, {skipped_dup} skipped (duplicate filenames)")

    # Now update markdown files
    files_updated = 0
    refs_updated = 0

    for filepath in glob.glob(os.path.join(DOCS_DIR, "**/*.md"), recursive=True):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content
        for path, filename in filename_map.items():
            if path in content:
                content = content.replace(path, f"/images/{filename}")
                refs_updated += content.count(f"/images/{filename}")  # approximate

        if content != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            files_updated += 1

    print(f"Updated {files_updated} markdown files")


if __name__ == "__main__":
    main()
