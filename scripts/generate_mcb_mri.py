"""Build local MRI protocol pages from the downloaded MCB source snapshot.

Run import_mcb_mri.py first. This command is offline and deterministic.
Original PDF pages are kept intact, alongside searchable text and structured
sequence parameters. No missing clinical parameters are inferred.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import shutil
import unicodedata
from pathlib import Path

import fitz
import yaml

ROOT = Path(__file__).resolve().parents[1]
CACHE = ROOT / 'data/mcb-mri'
DOCS = ROOT / 'docs'
DATE = '2026-09-27'
TITLES = {
    'Body': ['Fișă de orientare pentru alegerea protocolului Body', 'Abdomen de rutină', 'Pelvis de rutină (unisex)', 'Abdomen și pelvis combinat', 'Torace', 'Pancreas', 'Colangio-IRM (MRCP)', 'Ficat cu Eovist', 'Vezică urinară', 'Urografie IRM', 'Enterografie IRM', 'Tumori rectale și anale', 'Fistulă pelvină', 'Fistulă anală', 'Uter', 'Malformații congenitale uterine', 'Prostată', 'Penis și scrot', 'Defecografie IRM (planșeu pelvin)', 'Pacientă gravidă', 'Placentă', 'Abdomen în urgență la adult', 'Abdomen la pacientul pediatric'],
    'Neuro': ['','Creier de rutină și AVC rapid', 'Orbite', 'Epilepsie și convulsii', 'Scleroză multiplă', 'Angio-IRM cerebral (poligon Willis)', 'Angio-IRM cervical (carotide)', 'Angio-IRM cervical pentru disecție', 'Venografie IRM cerebrală', 'Hipofiză', 'Sinusuri paranazale', 'Conducte auditive interne (IAC)', 'Nevralgie de trigemen', 'Baza craniului', 'Fluxul lichidului cefalorahidian (LCR)', 'Părți moi cervicale', 'Glande parotide', 'Coloană cervicală', 'Coloană toracică', 'Coloană lombară', 'Coloană vertebrală completă', 'Articulații temporomandibulare (ATM)', 'Plex brahial', 'Plex lombar'],
    'MSK': ['', 'Umăr', 'Cot', 'Pumn', 'Mână', 'Police și ligament colateral ulnar', 'Șold', 'Artrografie IRM de șold', 'Genunchi', 'Gleznă și retropicior', 'Antepicior și mediopicior', 'Oase lungi (humerus, antebraț, femur, tibie și fibulă)', 'Bazin de rutină', 'Infecții ale bazinului', 'Tumori ale bazinului', 'Sacru și plex sacral', 'Articulații sacroiliace', 'Claviculă', 'Stern', 'Articulații sternoclaviculare', 'Mușchi pectoral', 'Infecție și osteomielită', 'Tumori osoase și de părți moi'],
    'Breast': ['', 'Sân: detecția leziunilor', 'Sân: integritatea implanturilor', 'Sân: leziuni și implanturi (combinat)', 'Biopsie mamară ghidată IRM'],
    'Vascular & IR': ['', 'Angio-IRM toracic', 'Angio-IRM renal', 'Angio-IRM mezenteric și portal', 'Angio-IRM pelvin', 'Angio-IRM iliofemural (runoff)', 'Limfangiografie IRM a extremităților'],
}
CATEGORIES = {'Body': 'abdomen-pelvis', 'Neuro': 'neuro', 'MSK': 'msk', 'Breast': 'san', 'Vascular & IR': 'vascular'}
GROUP_NAMES = {'Body': 'Body – abdomen, pelvis și torace', 'Neuro': 'Neuroradiologie', 'MSK': 'Musculoscheletic', 'Breast': 'Sân', 'Vascular & IR': 'Vascular și intervențional'}
HEADERS = {'pulsesequence': 'name', 'pacsname': 'pacs_name', 'plane': 'plane', 'fatsat': 'fat_sat', 'watersat': 'water_sat', 'slice(mm)': 'slice_mm', 'gap(mm)': 'gap_mm', 'firstslice': 'first_slice', 'fieldofview': 'fov_matrix'}
LABELS = {'name': 'Secvență', 'pacs_name': 'Denumire PACS', 'plane': 'Plan', 'fat_sat': 'Supresie grăsime', 'water_sat': 'Supresie apă', 'slice_mm': 'Grosime (mm)', 'gap_mm': 'Interval (mm)', 'first_slice': 'Prima secțiune', 'fov_matrix': 'FOV'}
VALUES = {'ax': 'Axial', 'cor': 'Coronal', 'sag': 'Sagital', 'yes': 'Da', 'no': 'Nu', 'none': 'Fără', 'top': 'Superior', 'base': 'Bază', 'front': 'Anterior', 'back': 'Posterior', 'left': 'Stânga', 'right': 'Dreapta'}


def slugify(value):
    return re.sub(r'[^a-z0-9]+', '-', unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode().lower()).strip('-')


def clean(value):
    return re.sub(r'\s+', ' ', value or '').strip()


def sequence_tables(record):
    """Recognize headers, including breast water-sat and absent gap columns."""
    result = []
    for page_no, tables in enumerate(record['tables'], 1):
        columns = None
        for table in tables:
            rows = []
            for raw in table:
                if clean(raw[0]) == 'Pulse Sequence':
                    columns = [HEADERS[re.sub(r'\s+', '', c or '').lower()] for c in raw]
                elif columns and len(raw) == len(columns) and raw[1] and raw[2]:
                    rows.append(dict(zip(columns, [clean(c) for c in raw])))
            if rows:
                result.append({'page': page_no, 'columns': columns, 'rows': rows})
    return result


def replace_section(path, content):
    start, end = '<!-- mcb-mri:start -->', '<!-- mcb-mri:end -->'
    text = path.read_text(encoding='utf-8')
    section = start + '\n' + content + '\n' + end
    if start in text:
        text = text[:text.index(start)] + section + text[text.index(end) + len(end):]
    else:
        text = text.rstrip() + '\n\n' + section + '\n'
    path.write_text(text, encoding='utf-8')


def generate():
    records = json.loads((CACHE / 'manifest.json').read_text(encoding='utf-8'))
    catalog = []
    for record in records:
        if 'file' not in record:
            # The MSK page contains a stale TMJ URL; the Neuro PDF is canonical.
            if record['url'].endswith('/Neuro/20%20TMJs.pdf'):
                continue
            raise ValueError(f"Unresolved source: {record['url']}")
        group, filename = record['file'].split('/')
        number = int(filename.split()[0])
        title = TITLES[group][number]
        category = CATEGORIES[group]
        if group == 'Body' and number == 22:
            category = 'pediatrie'
        slug = 'irm-' + slugify(title) + '-mcb'
        path = DOCS / 'irm' / category / (slug + '.md')
        path.parent.mkdir(parents=True, exist_ok=True)
        assets = DOCS / 'assets/mcb-mri' / slug
        assets.mkdir(parents=True, exist_ok=True)
        source = CACHE / record['file']
        assert hashlib.sha256(source.read_bytes()).hexdigest() == record['sha256']
        existing_pdf = assets / 'protocol.pdf'
        source_changed = not existing_pdf.exists() or hashlib.sha256(existing_pdf.read_bytes()).hexdigest() != record['sha256']
        shutil.copyfile(source, assets / 'protocol.pdf')
        tables = sequence_tables(record)
        sequences = []
        for table in tables:
            for row in table['rows']:
                sequences.append({
                    'name': row['name'], 'plane': VALUES.get(row['plane'], row['plane']),
                    'fat_sat': VALUES.get(row['fat_sat'], row['fat_sat']),
                    'slice_gap': row['slice_mm'] + ' mm' + ((' / ' + row['gap_mm'] + ' mm') if row.get('gap_mm', '').replace('.', '').isdigit() else (' / ' + row.get('gap_mm', 'nespecificat'))),
                    'fov_matrix': row.get('fov_matrix', ''),
                    'notes': f"PACS: {row['pacs_name']}; pagina {table['page']}. Variantele și condițiile sunt precizate în documentul original.",
                    'source_page': table['page'], 'source_parameters': row,
                })
        fm = {'title': 'IRM – ' + title + ' (MCB)', 'modality': 'irm', 'category': category,
              'slug': slug, 'author': 'MCB Radiology (documentul sursă)', 'last_updated': DATE,
              'tags': ['MCB Radiology', 'IRM', group], 'synonyms': record['labels'] + [filename.removesuffix('.pdf')],
              'sources': [{'title': filename.removesuffix('.pdf'), 'url': record['url'], 'pages': list(range(1, len(record['pages']) + 1)), 'consulted_on': DATE, 'relationship': 'Document instituțional original importat integral'}],
              'provenance': {'version': 'mcb-mri-' + record['sha256'][:12], 'processing': ['Titlu și etichete de parametri în română; textul clinic original păstrat în engleză.', 'Import PDF integral, imagini ale tuturor paginilor și extragere automată a parametrilor secvențelor.']},
              'sequences': sequences}
        if number == 0:
            fm.pop('sequences')
        prefix = '../../assets/mcb-mri/' + slug
        body = [f"# {fm['title']}\n", f"[Catalog MCB](../mcb/index.md) · [Descarcă PDF-ul complet]({prefix}/protocol.pdf) · [Sursa MCB]({record['url']})\n",
                'Documentul MCB este disponibil integral mai jos, inclusiv notele, condițiile de utilizare a contrastului și imaginile de planificare. Textul clinic al sursei este în **engleză**; titlul și etichetele parametrilor sunt în română.\n',
                '## Protocolul original\n']
        with fitz.open(source) as pdf:
            for page_no, page in enumerate(pdf, 1):
                target = assets / f'pagina-{page_no}.png'
                if source_changed or not target.exists():
                    page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5)).save(target)
                body.append(f'### Pagina {page_no}\n\n![{html.escape(title)} — pagina {page_no}]({prefix}/pagina-{page_no}.png){{ loading=lazy }}\n')
                body.append('??? abstract "Textul paginii (engleză)"\n\n    <div lang="en" style="white-space: pre-wrap">' + html.escape(record['pages'][page_no-1]).replace('\n', '\n    ') + '</div>\n')
        if tables:
            body += ['## Parametrii secvențelor\n', 'Tabele extrase din PDF. Variantele, secvențele condiționate și momentele administrării contrastului se citesc împreună cu notele de pe pagina originală indicată.\n']
            for index, table in enumerate(tables, 1):
                columns = table['columns']
                body.append(f"### Tabelul {index} — pagina {table['page']}\n")
                body.append('| ' + ' | '.join(LABELS[c] for c in columns) + ' |\n|' + '|'.join(['---'] * len(columns)) + '|')
                for row in table['rows']:
                    body.append('| ' + ' | '.join(html.escape(VALUES.get(row[c], row[c]) if c in ['plane', 'fat_sat', 'water_sat', 'first_slice'] else row[c]).replace('|', '&#124;') for c in columns) + ' |')
                body.append('')
        path.write_text('---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n' + '\n'.join(body) + '\n', encoding='utf-8')
        catalog.append({'title': title, 'category': category, 'group': group, 'number': number, 'slug': slug, 'pages': len(record['pages']), 'sequences': len(sequences), 'sha256': record['sha256'], 'source_url': record['url']})

    index_dir = DOCS / 'irm/mcb'
    index_dir.mkdir(exist_ok=True)
    lines = ['---\ntitle: Protocoale IRM MCB Radiology\n---\n', '# Protocoale IRM MCB Radiology\n',
             '77 de protocoale și o fișă de orientare, importate din cele cinci cataloage MCB. Fiecare pagină include documentul PDF local, toate paginile originale și textul căutabil. Titlurile și etichetele parametrilor sunt în română; instrucțiunile clinice originale sunt în engleză.\n']
    for group in TITLES:
        lines += [f'## {GROUP_NAMES[group]}\n', '| Protocol | Pagini PDF |\n|---|---:|']
        for item in sorted((c for c in catalog if c['group'] == group), key=lambda c: c['number']):
            lines.append(f"| [{item['title']}](../{item['category']}/{item['slug']}.md) | {item['pages']} |")
        lines.append('')
    (index_dir / 'index.md').write_text('\n'.join(lines), encoding='utf-8')
    for category in {c['category'] for c in catalog}:
        path = DOCS / 'irm' / category / 'index.md'
        if not path.exists():
            path.write_text('---\ntitle: Protocoale IRM vasculare și intervenționale\n---\n\n# Protocoale IRM vasculare și intervenționale\n', encoding='utf-8')
        selected = [c for c in catalog if c['category'] == category]
        # Cross-references from the official catalogs, without duplicate protocols.
        group = next((g for g, cat in CATEGORIES.items() if cat == category), None)
        for record in records:
            if group and group in record['catalogs'] and 'file' in record:
                item = next(c for c in catalog if c['source_url'] == record['url'])
                if item not in selected:
                    selected.append(item)
        links = ['## Protocoale MCB Radiology\n', '[Catalogul complet MCB](../mcb/index.md)\n']
        for item in sorted(selected, key=lambda c: c['title']):
            rel = '' if item['category'] == category else '../' + item['category'] + '/'
            links.append(f"- [{item['title']}]({rel}{item['slug']}.md)")
        replace_section(path, '\n'.join(links))
    home = DOCS / 'irm/index.md'
    home_text = home.read_text(encoding='utf-8')
    home_text = re.sub(r'\n<!-- mcb-mri:start -->.*?<!-- mcb-mri:end -->\n?', '\n', home_text, flags=re.S)
    mcb_section = '\n'.join([
        '## Protocoale IRM MCB Radiology\n',
        '**[Deschide catalogul complet MCB](mcb/index.md)** — 77 de protocoale și o fișă de orientare Body, disponibile direct în aplicație. Fiecare protocol include PDF-ul local, toate paginile originale, textul căutabil și parametrii secvențelor.\n',
        'Titlurile și etichetele parametrilor sunt în română; instrucțiunile clinice originale sunt păstrate în engleză.\n',
        '| Catalog sursă | Protocoale |\n|---|---:|',
        '| [Body: abdomen, pelvis și torace](abdomen-pelvis/index.md) | 22 + o fișă de orientare |',
        '| [Neuroradiologie](neuro/index.md) | 23 |',
        '| [Musculoscheletic](msk/index.md) | 22 |',
        '| [Sân](san/index.md) | 4 |',
        '| [Vascular și intervențional](vascular/index.md) | 6 |',
        '\n---\n\n',
    ])
    # Replace the former external-link-only MCB overview in place.
    home_text, changed = re.subn(r'## (?:🧲 Protocoale & Politici Tehnice IRM Instituționale \(MCB Radiology\)|Protocoale IRM MCB Radiology)\n.*?(?=## 🏥 Portofoliul IRM MIA)', mcb_section, home_text, flags=re.S)
    if not changed:
        raise ValueError('Cannot locate the MCB section in the IRM home page')
    home.write_text(home_text, encoding='utf-8')
    nav = DOCS / 'irm/.pages'
    text = nav.read_text(encoding='utf-8')
    for entry in ['  - Protocoale MCB Radiology: mcb', '  - Vascular și intervențional IRM: vascular']:
        if entry not in text:
            text = text.rstrip() + '\n' + entry + '\n'
    nav.write_text(text, encoding='utf-8')
    (CACHE / 'catalog.json').write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'Generated {len(catalog)} pages; {sum(c["sequences"] for c in catalog)} sequence rows.')


if __name__ == '__main__':
    generate()
