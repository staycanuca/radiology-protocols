"""One-time creation of pediatric review dossiers; never imports into docs/."""
import copy
import json
import re
import sys
import uuid
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from protocol_workbench.pediatric_ct import build_drafts, SOURCES, COMMON_SOURCES
from protocol_workbench.app import now


def main():
    output = Path(__file__).resolve().parent
    state = ROOT / '.protocol-workbench'
    session = requests.Session()
    base = 'http://127.0.0.1:5180'
    page = session.get(base, timeout=10).text
    token = json.loads(re.search(r'const TOKEN=("[^"]+")', page)[1])
    session.headers['X-Workbench-Token'] = token

    def api(path, data):
        result = session.post(base + path, json=data, timeout=60)
        result.raise_for_status()
        return result.json()

    existing = session.get(base + '/api/drafts', timeout=10).json()
    if any('ct-craniu-pediatric-nativ-' in d['document'] or 'ct-torace-pediatric-' in d['document']
           or 'ct-abdomen-pelvis-pediatric-' in d['document'] for d in existing):
        raise SystemExit('Dosare pediatrice deja existente: nu se suprascriu. Verifică manifestul.')
    selectors = {'head': '001.jpg', 'chest': 'Undifferentiated soft tissue', 'abdomen': 'Neuroblastoma 101'}
    captions = {
        'head': 'Exemplu CT cranian: hematom epidural și fractură la sugar, conform sursei. Nu este etalon de normalitate sau doză pentru grupa dosarului.',
        'chest': 'Exemplu CT toracic pediatric: masă tumorală în hemitoracele stâng, conform sursei. Nu este etalon de normalitate sau expunere.',
        'abdomen': 'Exemplu CT abdominal: neuroblastom, conform sursei. Vârsta și greutatea nu sunt precizate; imaginea nu validează grupa pediatrică.',
    }
    family_assets, manifest = {}, []
    for item in build_drafts():
        family = item['family']
        if family not in family_assets:
            draft = api('/api/drafts', {'title': item['fm']['title'], 'modality': 'ct'})
            prefix = '/api/drafts/' + draft['id']
            result = session.put(base + prefix, json={'document': item['document']}, timeout=10)
            result.raise_for_status()
            for title, url in [SOURCES[family], *COMMON_SOURCES]:
                draft = api(prefix + '/sources', {'title': title, 'url': url})
            candidates = json.loads((output / (family + '-image-candidates.json')).read_text(encoding='utf-8'))
            candidate = next(i for i in candidates if selectors[family] in i['caption'])
            candidate['caption'] = captions[family]
            draft = api(prefix + '/images', candidate)
            family_assets[family] = draft
        else:
            draft = copy.deepcopy(family_assets[family])
            draft.update(id=uuid.uuid4().hex, document=item['document'], created_at=now(), updated_at=now(), status='draft')
            with (state / (draft['id'] + '.json')).open('x', encoding='utf-8') as handle:
                json.dump(draft, handle, ensure_ascii=False, indent=2)
        export = output / 'protocols' / (item['fm']['slug'] + '.md')
        export.parent.mkdir(exist_ok=True)
        export.write_text(item['document'], encoding='utf-8')
        manifest.append({'id': draft['id'], 'title': item['fm']['title'], 'family': family,
                         'slug': item['fm']['slug'], 'group': item['group'], 'status': draft['status'],
                         'source_count': len(draft['sources']), 'images': draft['images'],
                         'review_required_fields': item['fm']['review_required_fields']})
        (output / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding='utf-8')
        print(item['fm']['slug'], 'saved', flush=True)


if __name__ == '__main__':
    main()
