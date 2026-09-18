#!/usr/bin/env python3
"""Extrage incidențe Merrill în formatul Rx folosit de extractorul Bontrager.

Dependențe: python -m pip install pymupdf pyyaml
Exemple (paginile sunt numere PDF, de la 1, nu pagini tipărite):
    python scripts/extract_merrill_protocols.py --pages 167 --dry-run
    python scripts/extract_merrill_protocols.py --category torace --limit 3
    python scripts/extract_merrill_protocols.py --category all --no-overwrite

O selecție include incidențele care intersectează paginile cerute, cu toate
paginile lor de continuare. Traducerea terminologică este parțială; rezultatele
sunt ciorne pentru revizie. Nu sunt completate valori clinice lipsă din sursă.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date
import os
from pathlib import Path
import re

import extract_bontrager_protocols as common

try:
    import pymupdf as fitz
except ImportError:
    fitz = common.fitz

ROOT = Path(__file__).resolve().parents[1]
PDF_NAME = 'Merrills_Atlas_of_Radiographic_Positioning__Procedures_3Vol_Set.pdf'
MISSING = 'Nespecificat în fragmentul extras; de verificat în sursă'
CHAPTERS = {
    3: 'torace', 4: 'abdomen', 5: 'membru-superior', 6: 'membru-superior',
    7: 'membru-inferior', 8: 'membru-inferior', 9: 'coloana', 10: 'torace',
    11: 'craniu-saf', 15: 'abdomen', 16: 'abdomen', 17: 'abdomen',
    18: 'torace', 22: 'pediatrie',
}
CATEGORIES = sorted(set(CHAPTERS.values()) | {'neclasificat'})
PROJECTION = re.compile(
    r'^(?=.{3,100}$)(?:[\w(),/–— -]+\s)?(?:projections?|positions?)'
    r'(?:\s+[a-z])?$', re.I)
SECTIONS = [
    ('patient_pos', r'Position of patient'), ('part_pos', r'Position of part'),
    ('cr', r'Central ray'), ('collimation', r'Collimation'),
    ('respiration', r'Respiration'), ('criteria', r'Evaluation Criteria'),
    ('anatomy', r'Structures shown'), ('tech', r'Image receptor(?:\s*\+\s*grid)?'),
    ('sid', r'SID'), ('shielding', r'Shielding'),
    ('indications', r'(?:Clinical indications|Indications)'), ('notes', r'NOTE'),
]


def translate_terms(text: str) -> str:
    """Folosește numai termenii, fără completările clinice din PHRASE_TRANSLATIONS."""
    for pattern, replacement in common.DICTIONARY_TERMS:
        text = re.sub(pattern, replacement, text, flags=re.I)
    return text


@dataclass
class Line:
    page: int
    top: float
    text: str


@dataclass
class Protocol:
    title: str
    category: str
    chapter: str
    start: int
    end: int
    lines: list[Line]


def clean(text: str) -> str:
    # Encodage defectuoase recurente în stratul text al PDF-ului furnizat.
    for old, new in [('ȇ', 'Th'), ('О', 'ft'), ('и', 'fi'), ('й', 'fl'), ('͡ ', 'q')]:
        text = text.replace(old, new)
    return text.strip()


def read_lines(doc) -> list[Line]:
    result = []
    for pno, page in enumerate(doc, 1):
        for block in page.get_text('dict', flags=fitz.TEXTFLAGS_DICT & ~fitz.TEXT_PRESERVE_IMAGES)['blocks']:
            for line in block.get('lines', []):
                text = clean(''.join(s['text'] for s in line['spans']))
                if not text or re.search(r'ebook/|960126734|ALGrawany', text, re.I):
                    continue
                result.append(Line(pno, line['bbox'][1], text))
    return result


def discover(doc, lines: list[Line]) -> list[Protocol]:
    toc = sorted((p, level, clean(title)) for level, title, p in doc.get_toc()
                 if p > 1 and level in (2, 3))
    boundaries = {p for p, level, title in toc if level == 2 or
                  title.lower() not in ('anatomy', 'radiography', 'summary of projections')}
    starts = [i for i, line in enumerate(lines) if PROJECTION.fullmatch(line.text)
              and not re.search(r'radiographic|summary|patient|part|general', line.text, re.I)]
    # « Lateral Projection / R or L position » este un singur antet.
    starts = [i for n, i in enumerate(starts) if n == 0 or i - starts[n-1] > 3
              or re.search(r'Position of|Image receptor|Central ray',
                           ' '.join(x.text for x in lines[starts[n-1]+1:i]), re.I)]
    results = []
    for ordinal, start in enumerate(starts):
        first = lines[start]
        chapter = ''
        region = ''
        chapter_num = 0
        for p, level, title in toc:
            if p > first.page:
                break
            if level == 2:
                chapter = title
                match = re.match(r'(\d+)\.', title)
                chapter_num = int(match[1]) if match else 0
                region = ''
            elif title.lower() not in ('anatomy', 'radiography', 'summary of projections'):
                region = title
        # Exclut chapitres introductifs, modalités non Rx et index.
        if not 3 <= chapter_num <= 23:
            continue
        end = starts[ordinal + 1] if ordinal + 1 < len(starts) else len(lines)
        for i in range(start + 1, end):
            if lines[i].page > first.page and lines[i].page in boundaries:
                end = i
                break
        fragment = lines[start:end]
        text = '\n'.join(x.text for x in fragment)
        if not re.search(r'Position of (?:patient|part)', text, re.I):
            continue
        if not re.search(r'Central ray', text, re.I):
            continue
        # Le nom anatomique peut suivre « Radiography » sans signet dédié.
        if start and lines[start-1].page == first.page:
            previous = lines[start-1].text
            if len(previous) < 65 and not re.search(
                    r'[.:;]|criteria|shown|seen|\bposition\b|\bprojection\b', previous, re.I):
                region = previous
        title = f'{region or chapter} — {first.text}'
        extra = []
        for line in fragment[1:5]:
            if re.match(r'Image receptor|Position of|SID|NOTE', line.text, re.I):
                break
            if len(line.text) < 80:
                extra.append(line.text)
        if extra:
            title += ' — ' + ' '.join(extra)
        category = CHAPTERS.get(chapter_num, 'neclasificat')
        if category == 'neclasificat':
            for keyword, cat in common.CHAPTER_CATEGORY_MAP.items():
                if keyword in title.lower():
                    category = cat
                    break
        results.append(Protocol(title, category, chapter, start, end, fragment))
    return results


def parse_sections(lines: list[Line]) -> dict[str, str]:
    sections: dict[str, list[str]] = {}
    current = None
    before_figure = None
    for line in lines:
        text = line.text.lstrip('•▪□ ').strip()
        if re.match(r'^FIG\.?\s*\d', text, re.I):
            if current:
                before_figure = current
            current = None  # Exclut aussi les descriptions d'images accessibles.
            continue
        if current is None and before_figure and line.text.startswith(('•', '▪', '□')):
            current = before_figure
        matched = False
        for key, pattern in SECTIONS:
            match = re.match(r'^' + pattern + r'(?:\s*:\s*|\s*$)', text, re.I)
            if match:
                current = key
                sections.setdefault(key, [])
                if text[match.end():]:
                    sections[key].append(text[match.end():])
                matched = True
                break
        if not matched and current:
            sections[current].append(line.text.replace('▪', '•').replace('□', '•'))
    return {key: '\n'.join(value) for key, value in sections.items()}


def page_bounds(doc, protocol: Protocol, all_lines: list[Line], page: int):
    top = protocol.lines[0].top if page == protocol.lines[0].page else 0
    bottom = doc[page-1].rect.height
    if protocol.end < len(all_lines) and all_lines[protocol.end].page == page:
        bottom = all_lines[protocol.end].top
    return top, bottom


def extract_figures(doc, protocol, lines, target: Path, markdown: Path) -> list[dict]:
    figures = []
    for pno in range(protocol.lines[0].page, protocol.lines[-1].page + 1):
        page = doc[pno-1]
        top, bottom = page_bounds(doc, protocol, lines, pno)
        for info in page.get_image_info():
            box = fitz.Rect(info['bbox'])
            if min(info['width'], info['height']) < 100 or box.y0 < top or box.y1 > bottom:
                continue
            target.mkdir(parents=True, exist_ok=True)
            path = target / f'p{pno}_fig{len(figures)+1}.png'
            page.get_pixmap(clip=box, matrix=fitz.Matrix(1.5, 1.5)).save(path)
            figures.append({
                'url': Path(os.path.relpath(path, markdown.parent)).as_posix(),
                'caption': f'Merrill — pagina PDF {pno}, imaginea {len(figures)+1}',
                'description': 'Imagine din fragmentul sursă; asocierea necesită revizie.',
            })
    return figures


def build_frontmatter(protocol, sections, slug, figures, pdf, markdown):
    def translated(key):
        return translate_terms(common.clean_multiline(sections[key])) if sections.get(key) else MISSING

    def bullets(key):
        return [translate_terms(common.clean_multiline(item))
                for item in re.split(r'[•▪□]', sections.get(key, '')) if item.strip()] or [MISSING]

    first, last = protocol.lines[0].page, protocol.lines[-1].page
    return {
        'title': 'Rx ' + translate_terms(protocol.title) + ' (Merrill)',
        'slug': slug, 'category': protocol.category, 'modality': 'rx',
        'author': 'Referință Merrill', 'last_updated': date.today().isoformat(),
        'status': 'draft', 'clinical_indications': bullets('indications'),
        'position': translated('patient_pos') + '; ' + translated('part_pos'),
        'centering': translated('cr'), 'sid_dff': translated('sid'),
        'breathing': translated('respiration'),
        'tech_params': {'collimation': translated('collimation')},
        'quality_criteria': bullets('criteria'), 'protection': bullets('shielding'),
        'notes': 'Extragere automată; traducere terminologică parțială. Necesită revizie.\n'
                 + translated('notes'),
        'images': figures,
        'sources': [{
            'title': f"Merrill’s Atlas, {protocol.chapter}, pagini PDF {first}–{last}",
            'url': (
                Path(os.path.relpath(
                    next((ROOT / 'docs/assets/protocols/sources').glob('*Merrill*.pdf'), pdf),
                    markdown.parent
                )).as_posix() + f'#page={first}'
            )
        }],
        'source_pages': list(range(first, last + 1)),
        'source_sections': sections,
    }


def parse_pages(value: str, count: int) -> set[int]:
    result = set()
    for part in value.split(','):
        match = re.fullmatch(r'\s*(\d+)(?:\s*-\s*(\d+))?\s*', part)
        if not match:
            raise ValueError(f'Selecție invalidă: {part!r}')
        first, last = int(match[1]), int(match[2] or match[1])
        if not 1 <= first <= last <= count:
            raise ValueError(f'Paginile trebuie să fie între 1 și {count}: {part}')
        result.update(range(first, last + 1))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--pdf', type=Path, default=ROOT / PDF_NAME)
    parser.add_argument('--output-dir', type=Path, default=ROOT / 'docs/rx')
    parser.add_argument('--images-dir', type=Path, default=ROOT / 'docs/assets/images/protocols/merrill')
    parser.add_argument('--category', choices=['all', *CATEGORIES], default='all')
    parser.add_argument('--pages', help='Pagini PDF: 167,188 sau 167-190')
    parser.add_argument('--limit', type=int)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--no-overwrite', action='store_true')
    args = parser.parse_args()
    if not fitz or not common.render_rx_document:
        parser.error('Instalează dependențele: python -m pip install pymupdf pyyaml')
    if not args.pdf.is_file():
        parser.error(f'PDF inexistent: {args.pdf}')
    if args.limit is not None and args.limit < 1:
        parser.error('--limit trebuie să fie pozitiv')
    with fitz.open(args.pdf) as doc:
        try:
            selected = parse_pages(args.pages, len(doc)) if args.pages else None
        except ValueError as error:
            parser.error(str(error))
        print(f'Scanare Merrill: {len(doc)} pagini PDF...')
        lines = read_lines(doc)
        protocols = discover(doc, lines)
        print(f'Identificate {len(protocols)} incidențe cu poziționare și rază centrală.')
        count = 0
        for protocol in protocols:
            pages = set(x.page for x in protocol.lines)
            if selected is not None and not pages & selected:
                continue
            if args.category != 'all' and protocol.category != args.category:
                continue
            slug = 'rx-' + common.slugify(translate_terms(protocol.title))[:130]
            slug += f'-p{protocol.lines[0].page}-merrill'
            markdown = args.output_dir.resolve() / protocol.category / f'{slug}.md'
            if args.no_overwrite and markdown.exists():
                continue
            sections = parse_sections(protocol.lines)
            figures = [] if args.dry_run else extract_figures(
                doc, protocol, lines, args.images_dir.resolve() / slug, markdown)
            fm = build_frontmatter(protocol, sections, slug, figures, args.pdf.resolve(), markdown)
            content = common.render_rx_document(fm)
            # Păstrează textul englezesc pentru verificarea traducerii și a parametrilor.
            content += '\n## Fragment sursă (pentru revizie)\n\n'
            for key, value in sections.items():
                content += f'### {key}\n\n{value}\n\n'
            if not args.dry_run:
                markdown.parent.mkdir(parents=True, exist_ok=True)
                markdown.write_text(content, encoding='utf-8')
            count += 1
            print(f'{"[DRY RUN] " if args.dry_run else ""}{min(pages)}–{max(pages)}: {markdown.name} ({len(figures)} imagini)')
            if args.limit and count >= args.limit:
                break
        print(f'Finalizat: {count} protocoale {"simulate" if args.dry_run else "generate"}.')


if __name__ == '__main__':
    main()
