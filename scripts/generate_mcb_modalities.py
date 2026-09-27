"""Offline import of selected non-MRI MCB PDFs into the documentation site."""
from __future__ import annotations
from collections import Counter
import hashlib
import html
import json
import os
from pathlib import Path
import re
import shutil
from urllib.parse import unquote
import fitz
import yaml

try:
    from .generate_mcb_mri import slugify
except ImportError:
    from generate_mcb_mri import slugify

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
DATA = ROOT / 'data/mcb-modalities'
DATE = '2026-09-27'
LABELS = {'ct':'CT', 'eco':'Ecografie', 'rx':'Radiografie, mamografie și DEXA', 'fluoro':'Fluoroscopie', 'mn':'Medicină nucleară', 'ir':'Radiologie intervențională'}
KINDS = {'protocol':'Protocol', 'colectie_protocoale':'Colecție de protocoale', 'fisa_lucru':'Fișă de lucru', 'manual_aparat':'Manual de aparat', 'ghid':'Ghid', 'politica_procedurala':'Politică procedurală', 'ghid_procedural':'Ghid procedural'}
CATEGORIES = {'aparate':'Parametri aparate CT','pediatrie':'Pediatrie','fise':'Fișe de lucru ecografice','dexa':'Densitometrie DEXA','proceduri':'Proceduri intervenționale'}
START, END = '<!-- mcb-modalities:start -->', '<!-- mcb-modalities:end -->'

def block(text, content, after_heading=False):
    replacement = START + '\n' + content + '\n' + END
    if START in text:
        return text[:text.index(START)] + replacement + text[text.index(END)+len(END):]
    if after_heading:
        heading = re.search(r'^# .+$', text, re.M)
        if not heading: raise ValueError('Missing H1')
        return text[:heading.end()] + '\n\n' + replacement + '\n\n## Sinteza existentă în aplicație\n' + text[heading.end():]
    return text.rstrip() + '\n\n' + replacement + '\n'

def relative(source, target):
    return os.path.relpath(target, source.parent).replace('\\', '/')

def known_sources(records):
    wanted = {unquote(r['url']) for r in records}
    result = {}
    # Existing nuclear medicine summaries can receive the original without duplication.
    for path in (DOCS / 'mn').rglob('*.md'):
        text = path.read_text(encoding='utf-8')
        if not text.startswith('---'): continue
        fm = yaml.safe_load(text.split('---',2)[1]) or {}
        if fm.get('mcb_import'): continue
        for src in fm.get('sources', []) or []:
            if isinstance(src,dict) and unquote(str(src.get('url'))) in wanted:
                result.setdefault(unquote(src['url']), path)
    return result

def add_nav(path, title, entry):
    text = path.read_text(encoding='utf-8') if path.exists() else 'nav:\n  - index.md\n'
    if re.search(r'^  - (?:.*: )?' + re.escape(entry) + r'\s*$', text, re.M): return
    if 'nav:' in text:
        # Insert into the nav sequence, before any following top-level setting.
        match = re.search(r'(?m)^nav:\s*\n', text)
        following = re.search(r'(?m)^\S', text[match.end():])
        end = match.end() + following.start() if following else len(text)
        text = text[:end].rstrip() + f'\n  - {title}: {entry}\n' + text[end:]
    else:
        text = text.rstrip() + f'\nnav:\n  - index.md\n  - {title}: {entry}\n  - ...\n'
    path.write_text(text, encoding='utf-8')

def generate():
    records = json.loads((DATA / 'manifest.json').read_text(encoding='utf-8'))
    existing = known_sources(records)
    catalog, failures = [], []
    for record in records:
        if 'file' not in record:
            failures.append({'title':record['title'],'url':record['url'],'error':record.get('error')})
            continue
        mod, cat = record['modality'], record['category']
        slug = mod + '-' + slugify(record['title']) + '-mcb'
        default = DOCS / mod / cat / (slug + '.md')
        path = existing.get(unquote(record['url']), default)
        reused = path != default
        path.parent.mkdir(parents=True, exist_ok=True)
        assets = DOCS / 'assets/mcb-modalities' / slug
        assets.mkdir(parents=True, exist_ok=True)
        source = DATA / record['file']
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        assert digest == record['sha256']
        target = assets / 'document.pdf'
        changed = not target.exists() or hashlib.sha256(target.read_bytes()).hexdigest() != digest
        shutil.copyfile(source, target)
        page_count = len(record['pages'])
        preview_count = page_count if page_count <= 30 else 3
        content = [f"## Documentul original MCB — {record['title']}\n",
                   f"**{KINDS[record['kind']]} · {page_count} pagini · consultat la {DATE}.**\n",
                   f"[Descarcă PDF-ul integral]({relative(path,target)}) · [Sursa MCB]({record['url']}) · [Catalogul MCB pentru această modalitate]({relative(path,DOCS/mod/'mcb/index.md')})\n",
                   'Instrucțiunile, valorile și ilustrațiile din documentul original sunt păstrate în **engleză**. Titlul și navigarea sunt în română.\n']
        if preview_count < page_count:
            content.append(f'Previzualizarea de mai jos prezintă primele {preview_count} pagini. **PDF-ul descărcabil conține toate cele {page_count} de pagini.**\n')
        with fitz.open(source) as pdf:
            for index in range(preview_count):
                image = assets / f'pagina-{index+1}.png'
                if changed or not image.exists():
                    pdf[index].get_pixmap(matrix=fitz.Matrix(1.4,1.4)).save(image)
                content.append(f"### Pagina {index+1}\n\n![{html.escape(record['title'])} — pagina {index+1}]({relative(path,image)}){{ loading=lazy }}\n")
        # All text remains available for native site search, including long manuals.
        content.append('## Textul documentului original\n')
        for index, text in enumerate(record['pages'], 1):
            if text.strip():
                content.append(f'??? abstract "Pagina {index} — text în engleză"\n\n    <div lang="en" style="white-space: pre-wrap">' + html.escape(text).replace('\n','\n    ') + '</div>\n')
            else:
                content.append(f'Pagina {index}: document scanat; conținutul se consultă în PDF-ul original.\n')
        content = '\n'.join(content)
        if reused:
            path.write_text(block(path.read_text(encoding='utf-8'), content, after_heading=True), encoding='utf-8')
        else:
            prefix = {'ct':'CT', 'eco':'Ecografie', 'rx':'RX', 'fluoro':'Fluoroscopie', 'mn':'Medicină nucleară', 'ir':'Intervențional'}[mod]
            fm = {'title':prefix+' — '+record['title']+' (MCB)', 'modality':mod, 'category':cat, 'slug':slug,
                  'author':'MCB Radiology (portalul sursă)', 'last_updated':DATE,
                  'document_kind':record['kind'], 'mcb_import':'modalities-2026-09-27',
                  'tags':['MCB Radiology',LABELS[mod],KINDS[record['kind']]],
                  'synonyms':[record['source_title'],*[' '.join(x.split()) for x in record['labels']]],
                  'sources':[{'title':'MCB Radiology — '+record['source_title'],'url':record['url'],'pages':f'1–{page_count}','consulted_on':DATE,'relationship':'Document original importat integral; atribuirea autorilor rămâne cea din PDF.'}],
                  'provenance':{'version':'mcb-'+digest[:12], 'processing':['Titlu și navigare în română; documentul sursă în engleză.', 'PDF original integral, previzualizare și text extras automat; fără completarea parametrilor clinici lipsă.']}}
            path.write_text('---\n'+yaml.safe_dump(fm,allow_unicode=True,sort_keys=False)+'---\n\n# '+fm['title']+'\n\n'+content+'\n',encoding='utf-8')
        catalog.append({**{k:record[k] for k in ['url','title','modality','category','kind','sha256']}, 'path':path.relative_to(DOCS).as_posix(),'assets':assets.relative_to(DOCS).as_posix(),'pages':page_count,'preview_pages':preview_count,'updated_existing':reused})

    for mod, label in LABELS.items():
        folder = DOCS / mod
        folder.mkdir(exist_ok=True)
        home = folder / 'index.md'
        if not home.exists(): home.write_text(f'---\ntitle: {label}\n---\n\n# {label}\n',encoding='utf-8')
        items = [c for c in catalog if c['modality']==mod]
        index = folder / 'mcb/index.md'
        index.parent.mkdir(exist_ok=True)
        lines = [f'---\ntitle: {label} — documente MCB\ncatalog_manual: true\n---\n\n# {label} — documente MCB\n',
                 f'{len(items)} documente disponibile local. PDF-urile sunt complete; textul clinic original este în engleză.\n',
                 '[Toate modalitățile MCB](../../mcb/index.md)\n', '| Document | Tip | Pagini PDF |\n|---|---|---:|']
        for item in sorted(items,key=lambda x:(x['kind'],x['title'])):
            lines.append(f"| [{item['title']}]({relative(index,DOCS/item['path'])}) | {KINDS[item['kind']]} | {item['pages']} |")
        index.write_text('\n'.join(lines)+'\n',encoding='utf-8')
        add_nav(folder/'.pages','Catalog MCB Radiology','mcb')
        home.write_text(block(home.read_text(encoding='utf-8'), f'## Documente MCB disponibile local\n\n[Deschide catalogul MCB: {len(items)} documente](mcb/index.md). Protocoale și documente tehnice, cu PDF-uri integrale și previzualizare.'),encoding='utf-8')
        for cat in sorted({c['category'] for c in items}):
            category_dir = folder / cat
            category_dir.mkdir(exist_ok=True)
            category_index = category_dir / 'index.md'
            if not category_index.exists():
                cat_title = CATEGORIES.get(cat,cat)
                category_index.write_text(f'---\ntitle: {cat_title}\n---\n\n# {cat_title}\n',encoding='utf-8')
                if not (category_dir/'.pages').exists(): (category_dir/'.pages').write_text(f'title: {cat_title}\n',encoding='utf-8')
                add_nav(folder/'.pages',cat_title,cat)
            links = ['## Documente MCB Radiology\n']
            for item in sorted((x for x in items if x['category']==cat),key=lambda x:x['title']):
                links.append(f"- [{item['title']}]({relative(category_index,DOCS/item['path'])}) — {KINDS[item['kind']]}")
            category_index.write_text(block(category_index.read_text(encoding='utf-8'),'\n'.join(links)),encoding='utf-8')
    central = DOCS / 'mcb/index.md'
    central.parent.mkdir(exist_ok=True)
    lines = ['---\ntitle: Biblioteca MCB Radiology\n---\n\n# Biblioteca MCB Radiology\n',
             'Documente originale din [portalul MCB Radiology](https://ref.mcbradiology.com/), organizate după modalitate. PDF-urile sunt disponibile local; textul clinic original este în engleză.\n',
             '| Modalitate | Documente |\n|---|---:|', '| [IRM](../irm/mcb/index.md) | 77 protocoale + o fișă Body |']
    for mod,label in LABELS.items():
        lines.append(f'| [{label}](../{mod}/mcb/index.md) | {sum(c["modality"]==mod for c in catalog)} |')
    lines += ['\nProtocoalele, fișele de lucru, manualele de aparat și ghidurile procedurale sunt etichetate distinct în cataloage. Colecțiile RX păstrează toate examinările incluse în PDF-ul sursă.']
    central.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    add_nav(DOCS/'.pages','Radiologie intervențională','ir')
    add_nav(DOCS/'.pages','Biblioteca MCB','mcb')
    institutional = DOCS/'for-institutions/mcb-radiology-protocols.md'
    institutional.write_text(block(institutional.read_text(encoding='utf-8'),'## Biblioteca locală de documente originale\n\n[Deschide biblioteca MCB pentru toate modalitățile](../mcb/index.md).'),encoding='utf-8')
    report = {'catalog':catalog,'failures':failures,'counts':dict(Counter(c['modality'] for c in catalog)), 'updated_existing':sum(c['updated_existing'] for c in catalog)}
    (DATA/'catalog.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k!='catalog'},ensure_ascii=True,indent=2))

if __name__ == '__main__': generate()
