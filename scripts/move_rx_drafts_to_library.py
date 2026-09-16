"""User-authorized transfer for review in the main application, not clinical approval."""
from pathlib import Path
import json
import sys
from uuid import uuid5, NAMESPACE_URL

import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from protocol_workbench.rx_expansion import BATCH, SPECS
from protocol_workbench.app import frontmatter, now


def transfer(root=ROOT):
    root = Path(root)
    planned = []
    for spec in SPECS:
        identifier = uuid5(NAMESPACE_URL, BATCH + '/' + spec['slug']).hex
        source = root / '.protocol-workbench' / (identifier + '.json')
        draft = json.loads(source.read_text(encoding='utf-8'))
        fm, body = frontmatter(draft['document'])
        target = root / 'docs/rx' / spec['category'] / (spec['slug'] + '.md')
        if target.exists():
            if draft.get('imported_path') == target.relative_to(root).as_posix():
                continue
            raise FileExistsError(target)
        if (fm['slug'], fm['category'], fm['modality']) != (spec['slug'], spec['category'], 'rx'):
            raise ValueError('Draft identity changed: ' + identifier)
        if draft.get('images'):
            raise ValueError('Draft has images requiring asset transfer: ' + identifier)
        fm['sources'] = [{k: v for k, v in s.items() if k != 'excerpt'} for s in draft['sources']]
        fm['clinical_status'] = 'draft_not_for_clinical_use'
        fm['workbench_transfer'] = {'draft_id': identifier, 'transferred_at': now(), 'purpose': 'review_in_main_application'}
        body = body.replace('verificate înainte de import.', 'verificate înainte de utilizarea clinică.')
        document = '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n' + body + '\n'
        planned.append((source, draft, target, document, fm))
    for source, draft, target, document, fm in planned:
        backup = root / '.protocol-workbench/backups/rx-library-transfer' / source.name
        backup.parent.mkdir(parents=True, exist_ok=True)
        if not backup.exists():
            backup.write_bytes(source.read_bytes())
        target.parent.mkdir(parents=True, exist_ok=True)
        with target.open('x', encoding='utf-8') as handle:
            handle.write(document)
        relative = target.relative_to(root).as_posix()
        draft.update(status='imported', imported_path=relative, imported_for_review=True, updated_at=now())
        draft['revision'] = draft.get('revision', 0) + 1
        draft.setdefault('history', []).append({'at': now(), 'revision': draft['revision'],
            'changed': ['status', 'imported_path'], 'reason': 'Transfer autorizat pentru revizuire în aplicația principală; fără aprobare clinică'})
        source.write_text(json.dumps(draft, ensure_ascii=False, indent=2), encoding='utf-8')
        index = target.parent / 'index.md'
        text = index.read_text(encoding='utf-8') if index.exists() else '# Protocoale RX\n'
        link = f"- [{fm['title']}]({target.name}) — **Ciornă pentru revizuire**\n"
        if target.name not in text:
            index.write_text(text.rstrip() + '\n' + link, encoding='utf-8')
    return len(planned)


if __name__ == '__main__':
    print(f'Transferred {transfer()} drafts to main library for review.')
