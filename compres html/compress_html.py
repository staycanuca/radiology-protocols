#!/usr/bin/env python3
"""
Compress (minify) all HTML files in the current directory and its subdirectories.
Supports both minify-html (ultra-fast Rust-based) and a built-in regex fallback.
"""

import os
import sys
import time
import re
from pathlib import Path

try:
    import minify_html
    HAS_MINIFY_HTML = True
except ImportError:
    HAS_MINIFY_HTML = False


def fallback_minify(html: str) -> str:
    """Basic fallback minifier when minify-html is not installed."""
    # Preserve pre, code, textarea, script blocks
    preserved = []
    def preserve(match):
        preserved.append(match.group(0))
        return f"___PRESERVED_BLOCK_{len(preserved)-1}___"

    pattern = re.compile(r"<(pre|code|textarea|script)\b[^>]*>.*?</\1>", re.DOTALL | re.IGNORECASE)
    html = pattern.sub(preserve, html)

    # Remove HTML comments (excluding conditional comments)
    html = re.sub(r"<!--(?!\[if).*?-->", "", html, flags=re.DOTALL)
    # Collapse consecutive whitespace to single space
    html = re.sub(r"\s+", " ", html)
    # Remove whitespace between tags
    html = re.sub(r">\s+<", "><", html)
    # Remove leading/trailing whitespace around tags
    html = re.sub(r"^\s+|\s+$", "", html)

    # Restore preserved blocks
    for i, block in enumerate(preserved):
        html = html.replace(f"___PRESERVED_BLOCK_{i}___", block)

    return html.strip()


def minify_content(content: str) -> str:
    if HAS_MINIFY_HTML:
        try:
            return minify_html.minify(
                content,
                minify_js=True,
                minify_css=True,
                keep_comments=False
            )
        except Exception:
            return fallback_minify(content)
    return fallback_minify(content)


def format_size(size_bytes: int) -> str:
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.2f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.2f} MB"


def compress_directory(target_dir: Path):
    print(f"==================================================")
    print(f" HTML Compressor / Minifier")
    print(f" Engine: {'minify-html (Rust, ultra-fast)' if HAS_MINIFY_HTML else 'Built-in regex fallback'}")
    print(f" Target: {target_dir.resolve()}")
    print(f"==================================================")

    html_files = []
    for root, dirs, files in os.walk(target_dir):
        # Skip hidden folders / git
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for file in files:
            if file.lower().endswith(".html"):
                html_files.append(Path(root) / file)

    total_files = len(html_files)
    if total_files == 0:
        print("No HTML files found.")
        return

    print(f"Found {total_files} HTML files. Processing...\n")

    start_time = time.time()
    total_orig_size = 0
    total_min_size = 0
    modified_count = 0

    for idx, file_path in enumerate(html_files, 1):
        try:
            orig_size = file_path.stat().st_size
            total_orig_size += orig_size

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except UnicodeDecodeError:
                with open(file_path, "r", encoding="latin-1", errors="replace") as f:
                    content = f.read()

            minified = minify_content(content)
            min_size = len(minified.encode("utf-8"))

            if min_size < orig_size:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(minified)
                total_min_size += min_size
                modified_count += 1
            else:
                total_min_size += orig_size

            # Print progress every 100 files or on the last file
            if idx % 100 == 0 or idx == total_files:
                percent = (idx / total_files) * 100
                print(f" [{idx}/{total_files}] ({percent:.1f}%) processed...")

        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            total_min_size += orig_size

    elapsed = time.time() - start_time
    saved_bytes = total_orig_size - total_min_size
    saved_percent = (saved_bytes / total_orig_size * 100) if total_orig_size > 0 else 0

    print(f"\n==================================================")
    print(f" Results:")
    print(f" - Files processed : {total_files}")
    print(f" - Files optimized : {modified_count}")
    print(f" - Original size   : {format_size(total_orig_size)}")
    print(f" - Minified size   : {format_size(total_min_size)}")
    print(f" - Space saved     : {format_size(saved_bytes)} (-{saved_percent:.2f}%)")
    print(f" - Time elapsed    : {elapsed:.2f} seconds")
    print(f"==================================================")


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    compress_directory(target)
