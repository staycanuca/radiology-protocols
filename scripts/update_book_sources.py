#!/usr/bin/env python3
"""update_book_sources.py — Înlocuiește sursele PDF locale de cărți cu link-uri oficiale online către cărțile respective.

Cărți actualizate:
1. Merrill’s Atlas of Radiographic Positioning & Procedures
   -> https://books.google.com/books/about/Merrill_s_Atlas_of_Radiographic_Position.html?id=BM0lEQAAQBAJ
2. Clark's Positioning in Radiography (12th Edition)
   -> https://books.google.com/books/about/Clark_s_Positioning_in_Radiography.html?id=Xxu6MwEACAAJ
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

# Asigură codarea UTF-8 pe Windows
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
SOURCES_DIR = DOCS_DIR / "assets" / "protocols" / "sources"

MERRILL_URL = "https://books.google.com/books/about/Merrill_s_Atlas_of_Radiographic_Position.html?id=BM0lEQAAQBAJ"
CLARK_URL = "https://books.google.com/books/about/Clark_s_Positioning_in_Radiography.html?id=Xxu6MwEACAAJ"


def update_file(path: Path) -> bool:
    content = path.read_text(encoding="utf-8")
    original = content

    # 1. Merrill PDF URLs (toate căile relative și ancorele de pagină)
    content = re.sub(
        r'(?:\.\./)+assets/protocols/sources/[^)\s]*Merrill[^)\s]*\.pdf(?:#page=\d+)?',
        MERRILL_URL,
        content
    )
    content = re.sub(
        r'(?:\.\./)+[^)\s]*Merrills_Atlas[^)\s]*\.pdf(?:#page=\d+)?',
        MERRILL_URL,
        content
    )
    content = re.sub(
        r'assets/protocols/sources/[^)\s]*Merrill[^)\s]*\.pdf(?:#page=\d+)?',
        MERRILL_URL,
        content
    )

    # 2. Clark PDF URLs (toate căile relative și ancorele de pagină)
    content = re.sub(
        r'(?:\.\./)+assets/protocols/sources/[^)\s]*Clark[^)\s]*\.pdf(?:#page=\d+)?',
        CLARK_URL,
        content
    )
    content = re.sub(
        r'(?:\.\./)+[^)\s]*Clark[^)\s]*\.pdf(?:#page=\d+)?',
        CLARK_URL,
        content
    )
    content = re.sub(
        r'assets/protocols/sources/[^)\s]*Clark[^)\s]*\.pdf(?:#page=\d+)?',
        CLARK_URL,
        content
    )

    # 3. Curățare mențiuni "pagini PDF" / "pagina PDF" în text
    content = re.sub(r'pagini PDF\b', 'pagini', content)
    content = re.sub(r'pagina PDF\b', 'pagina', content)

    if content != original:
        path.write_text(content, encoding="utf-8")
        return True
    return False


def main():
    print(f"Scanare documente Markdown în: {DOCS_DIR}")
    updated_count = 0
    for md_file in DOCS_DIR.rglob("*.md"):
        if update_file(md_file):
            updated_count += 1

    print(f"Total fișiere Markdown actualizate: {updated_count}")

    # Elimină fișierele PDF locale de cărți din docs/assets/protocols/sources/
    removed_files = []
    if SOURCES_DIR.exists():
        for pdf in SOURCES_DIR.glob("*.pdf"):
            if "merrill" in pdf.name.lower() or "clark" in pdf.name.lower():
                size_mb = pdf.stat().st_size / (1024 * 1024)
                pdf.unlink()
                removed_files.append((pdf.name, size_mb))
                print(f"Șters fișier PDF local: {pdf.name} ({size_mb:.1f} MB)")

    print(f"\nFinalizat! {updated_count} fișiere au fost convertite către link-uri online.")
    if removed_files:
        total_freed = sum(s for _, s in removed_files)
        print(f"Spațiu eliberat prin eliminarea PDF-urilor locale: {total_freed:.1f} MB.")


if __name__ == "__main__":
    main()
