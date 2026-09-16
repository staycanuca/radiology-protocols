"""Apply the reviewed RX wording corrections, preserving document bodies and backups."""
from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
PATIENT = 'Ecranarea pacientului se stabilește conform politicii RX actualizate; fără aplicare automată din template.'
PREGNANCY = 'Evaluarea posibilității unei sarcini se documentează conform procedurii locale și examinării solicitate.'
POSITION = 'AP în ortostatism sau decubit dorsal; profil în ortostatism ori adaptat stării pacientului. În traumatism, fără mobilizare forțată, cu tehnică cu rază orizontală când este indicată.'


def main():
    from scripts.render_rx_protocol import QUICK_PROTECTION
    generator = ROOT / 'scripts/generate_rx_protocols.py'
    generator_text = generator.read_text(encoding='utf-8')
    count = 0
    for path in (ROOT / 'docs/rx').glob('*/*.md'):
        original = path.read_text(encoding='utf-8')
        if not original.startswith('---\n'):
            continue
        _, header, body = original.split('---', 2)
        fm = yaml.safe_load(header)
        if fm.get('modality') != 'rx':
            continue
        protection = []
        for item in fm.get('protection', []):
            lower = item.lower()
            replacement = item
            if '10 zile' in lower:
                replacement = PREGNANCY
            elif any(word in lower for word in ('plumb', 'gonad', 'guler tiroid')) and not any(word in lower for word in ('personal', 'însoțitor', 'părint')):
                replacement = PATIENT
            protection.append(replacement)
            if replacement != item:
                body = body.replace(item, replacement)
                generator_text = generator_text.replace(item, replacement)
        fm['protection'] = list(dict.fromkeys(protection))
        body = re.sub(r'^    5\. \*\*Protecție gonade/tiroidă:\*\*.*$', QUICK_PROTECTION, body, flags=re.M)
        if fm.get('position') == 'Terminology':
            fm['position'] = POSITION
            body = body.replace('**Poziție Pacient:** Terminology', '**Poziție Pacient:** ' + POSITION)
            body += '\n\nPoziționare revizuită: [NNUH, ghid RX v8, p.36](https://www.nnuh.nhs.uk/publication/download/justification-criteria-technique-guide-for-plain-radiological-examinations-version-8/).\n'
        body = body.replace('semnătură consimțământ și absență sarcină la pacientele de vârstă fertilă', 'consimțământ conform procedurii și evaluarea posibilității unei sarcini, când este relevantă')
        fm['last_updated'] = '2026-09-15'
        updated = '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + '---' + body
        if updated != original:
            backup = ROOT / '.protocol-workbench/backups/rx-expansion-2026-09-15' / path.relative_to(ROOT)
            backup.parent.mkdir(parents=True, exist_ok=True)
            if not backup.exists():
                backup.write_text(original, encoding='utf-8')
            path.write_text(updated, encoding='utf-8')
            count += 1
    generator_text = generator_text.replace('  - index.md\n  - Torace:', '  - index.md\n  - Radioprotecție: radioprotectie.md\n  - Torace:')
    generator.write_text(generator_text, encoding='utf-8')
    nav = ROOT / 'docs/rx/.pages'
    nav.write_text(nav.read_text(encoding='utf-8').replace('  - index.md\n  - Torace:', '  - index.md\n  - Radioprotecție: radioprotectie.md\n  - Torace:'), encoding='utf-8')
    print(f'Updated {count} RX documents; originals backed up.')


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(ROOT))
    main()
