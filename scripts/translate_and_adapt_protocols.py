#!/usr/bin/env python3
"""translate_and_adapt_protocols.py — Script executabil pentru traducerea și adaptarea
medical-radiologică a protocoalelor radiografice din catalogul Ghidului de Radiologie.

Identifică fragmentele netraduse sau mixte din protocoalele Merrill, Bontrager, Clark și
instituționale, le traduce în limba română medicală standard, adaptează titlurile și descrierile
clinice și re-randează fișierele Markdown păstrând integritatea structurală și a imaginilor.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
import yaml

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

from radiology_translator import (
    translate_protocol_frontmatter,
    calculate_english_score,
    detect_english_fragments
)
from render_rx_protocol import render_rx_document


def process_file(
    file_path: Path,
    dry_run: bool = False,
    use_ai: bool = False
) -> dict | None:
    """Procesează, traduce și adaptează un fișier de protocol Markdown."""
    try:
        content = file_path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"[EROARE] Nu s-a putut citi {file_path}: {e}", file=sys.stderr)
        return None

    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return None

    raw_yaml = match.group(1)
    try:
        fm = yaml.safe_load(raw_yaml)
    except Exception as e:
        print(f"[EROARE YAML] {file_path.name}: {e}", file=sys.stderr)
        return None

    if not isinstance(fm, dict):
        return None

    # Text combinat înainte de traducere pentru calculul scorului
    text_before = f"{fm.get('title', '')} {fm.get('position', '')} {fm.get('centering', '')} {fm.get('breathing', '')}"
    score_before = calculate_english_score(text_before)

    # Traducere și adaptare frontmatter
    updated_fm, modified = translate_protocol_frontmatter(fm, use_ai=use_ai)

    # Text combinat după traducere
    text_after = f"{updated_fm.get('title', '')} {updated_fm.get('position', '')} {updated_fm.get('centering', '')} {updated_fm.get('breathing', '')}"
    score_after = calculate_english_score(text_after)

    # Re-randare completă a documentului Markdown
    new_body = render_rx_document(updated_fm)

    # Dacă există source_sections (Merrill), adăugăm secțiunea de referință tehnică tradusă
    if updated_fm.get('source_sections') and isinstance(updated_fm['source_sections'], dict):
        new_body += '\n## Fragmente sursă traduse (referință tehnică)\n\n'
        for sec_key, sec_val in updated_fm['source_sections'].items():
            new_body += f'### {sec_key}\n\n{sec_val}\n\n'

    title_changed = (fm.get('title') != updated_fm.get('title'))

    if not dry_run and (modified or content != new_body):
        file_path.write_text(new_body, encoding='utf-8')

    return {
        'file': str(file_path.relative_to(ROOT)).replace('\\', '/'),
        'filename': file_path.name,
        'category': file_path.parent.name,
        'title_before': fm.get('title', ''),
        'title_after': updated_fm.get('title', ''),
        'title_changed': title_changed,
        'score_before': round(score_before, 3),
        'score_after': round(score_after, 3),
        'modified': modified or (content != new_body)
    }


def main():
    parser = argparse.ArgumentParser(
        description="Traducător și adaptator medical-radiologic pentru protocoalele Rx."
    )
    parser.add_argument('--category', default='all', help="Categoria de procesat (default: all)")
    parser.add_argument('--source', default='all', choices=['all', 'merrill', 'bontrager', 'clark', 'other'],
                        help="Filtru după sursă (default: all)")
    parser.add_argument('--file', type=Path, help="Procesează un singur fișier specific")
    parser.add_argument('--limit', type=int, help="Limită maximă de fișiere procesate")
    parser.add_argument('--dry-run', action='store_true', help="Rulează în mod simulare (fără scriere pe disc)")
    parser.add_argument('--ai', action='store_true', help="Activează rafinarea AI suplimentară cu agy")
    parser.add_argument('--report', type=Path, default=ROOT / 'translation_report.json',
                        help="Fișierul JSON în care se salvează raportul detaliat")
    args = parser.parse_args()

    rx_dir = ROOT / 'docs' / 'rx'

    if args.file:
        files = [args.file.resolve()]
    else:
        files = sorted([f for f in rx_dir.glob('*/*.md') if f.name != 'index.md'])

    # Filtrare categorie
    if args.category != 'all':
        files = [f for f in files if f.parent.name == args.category]

    # Filtrare sursă
    if args.source != 'all':
        if args.source == 'merrill':
            files = [f for f in files if 'merrill' in f.name]
        elif args.source == 'bontrager':
            files = [f for f in files if 'bontrager' in f.name]
        elif args.source == 'clark':
            files = [f for f in files if 'clark' in f.name]
        elif args.source == 'other':
            files = [f for f in files if not any(s in f.name for s in ['merrill', 'bontrager', 'clark'])]

    if args.limit:
        files = files[:args.limit]

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Începere procesare {len(files)} protocoale...")
    start_time = time.time()

    results = []
    modified_count = 0
    title_changed_count = 0
    scores_before = []
    scores_after = []

    for i, file_path in enumerate(files, 1):
        res = process_file(file_path, dry_run=args.dry_run, use_ai=args.ai)
        if res:
            results.append(res)
            scores_before.append(res['score_before'])
            scores_after.append(res['score_after'])
            if res['modified']:
                modified_count += 1
            if res['title_changed']:
                title_changed_count += 1

            if i % 50 == 0 or i == len(files):
                print(f"  Progres: {i}/{len(files)} fișiere analizate ({modified_count} actualizate)...")

    duration = time.time() - start_time
    avg_before = (sum(scores_before) / len(scores_before) * 100) if scores_before else 0
    avg_after = (sum(scores_after) / len(scores_after) * 100) if scores_after else 0

    print("\n" + "=" * 65)
    print("REZUMAT RAPORT TRADUCERE & ADAPTARE MEDICALĂ")
    print("=" * 65)
    print(f"Total fișiere procesate:        {len(files)}")
    print(f"Fișiere modificate/adaptate:    {modified_count}")
    print(f"Titluri medicale standardizate: {title_changed_count}")
    print(f"Densitate engleză inițială:     {avg_before:.1f}%")
    print(f"Densitate engleză finală:       {avg_after:.1f}%")
    print(f"Timp de execuție:               {duration:.2f} secunde")
    print("=" * 65)

    # Salvare raport JSON
    report_data = {
        'timestamp': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'total_files': len(files),
        'modified_count': modified_count,
        'title_changed_count': title_changed_count,
        'avg_english_density_before': round(avg_before, 2),
        'avg_english_density_after': round(avg_after, 2),
        'duration_seconds': round(duration, 2),
        'details': results
    }

    try:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report_data, ensure_ascii=False, indent=2), encoding='utf-8')
        print(f"Raport complet salvat în: {args.report}")
    except Exception as e:
        print(f"[AVERTISMENT] Nu s-a putut salva raportul: {e}", file=sys.stderr)


if __name__ == '__main__':
    main()
