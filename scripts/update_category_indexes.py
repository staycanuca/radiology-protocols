#!/usr/bin/env python3
"""update_category_indexes.py — Regenerează paginile index.md din docs/rx/<categorie>."""

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = Path(__file__).resolve().parents[1]
RX_DIR = ROOT_DIR / 'docs' / 'rx'

CAT_NAMES = {
    'abdomen': 'Abdomen & Bazin',
    'coloana': 'Coloană Vertebrală',
    'craniu-saf': 'Craniu & Masiv Facial',
    'membru-inferior': 'Membru Inferior',
    'membru-superior': 'Membru Superior',
    'pediatrie': 'Pediatrie Rx',
    'torace': 'Torace & Cutie Toracică',
    'neclasificat': 'Neclasificat',
}


def main():
    for cat_dir in sorted(RX_DIR.iterdir()):
        if not cat_dir.is_dir():
            continue
        cat_name = cat_dir.name
        display_cat = CAT_NAMES.get(cat_name, cat_name.replace('-', ' ').title())

        md_files = [f for f in cat_dir.glob('*.md') if f.name != 'index.md']
        protocols = []

        for f in md_files:
            content = f.read_text(encoding='utf-8')
            title = ''
            m_title = re.search(r'^title:\s*["\']?(.*?)["\']?\s*$', content, re.MULTILINE)
            if m_title:
                title = m_title.group(1).strip()
            else:
                m_h1 = re.search(r'^#\s+(.*)$', content, re.MULTILINE)
                if m_h1:
                    title = m_h1.group(1).strip()
                else:
                    title = f.stem
            protocols.append((title, f.name))

        protocols.sort(key=lambda x: x[0].lower())

        index_content = f"# Protocoale Rx — {display_cat}\n\n"
        index_content += f"Catalog cu **{len(protocols)} protocoale** din această categorie.\n\n"
        for title, fname in protocols:
            index_content += f"- [{title}]({fname})\n"

        index_file = cat_dir / 'index.md'
        index_file.write_text(index_content, encoding='utf-8')
        print(f"Actualizat index pentru {cat_name}: {len(protocols)} protocoale.")


if __name__ == '__main__':
    main()
