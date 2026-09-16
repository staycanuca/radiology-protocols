"""Create the approved RX draft batch without overwriting existing Workbench work."""
from pathlib import Path
import json
import sys
from uuid import uuid5, NAMESPACE_URL

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from protocol_workbench.rx_expansion import SOURCES, SPECS, BATCH, build_drafts
from protocol_workbench.app import now


def prepare(root=ROOT):
    root = Path(root)
    state = root / '.protocol-workbench'
    report = root / 'reports/rx-audit-2026-09-15/proposals'
    state.mkdir(parents=True, exist_ok=True)
    report.mkdir(parents=True, exist_ok=True)
    records = {key: dict(id=uuid5(NAMESPACE_URL, value['url']).hex,
        **{k: v for k, v in value.items() if k != 'summary'},
        excerpt=value['summary'], excerpt_kind='authored_summary',
        verification_method='Web consultation; no downloaded content hash',
        checked_at=now(),
        consulted_on='2026-09-15') for key, value in SOURCES.items()}
    rows = []
    created = 0
    for spec, draft in zip(SPECS, build_drafts(records)):
        target = state / (draft['id'] + '.json')
        try:
            with target.open('x', encoding='utf-8') as handle:
                json.dump(draft, handle, ensure_ascii=False, indent=2)
            created += 1
        except FileExistsError:
            pass  # User changes, including imported status, always win.
        current = json.loads(target.read_text(encoding='utf-8'))
        (report / (spec['slug'] + '.md')).write_text(current['document'], encoding='utf-8')
        rows.append(f"- [{spec['title']}]({spec['slug']}.md) — Workbench `{draft['id']}`")
    (report / 'README.md').write_text('# Lotul RX pentru revizuire\n\n'
        'Zece ciorne disponibile în Workbench. Publicarea necesită revizuire clinică, '
        'configurarea aparatului și imagini cu proveniență verificată. '
        'Sursele sunt documentate prin link și sinteză editorială; nu au hash de fișier descărcat.\n\n'
        + '\n'.join(rows) + '\n', encoding='utf-8')
    return created


if __name__ == '__main__':
    print(f'Created {prepare()} RX drafts; existing drafts preserved.')
