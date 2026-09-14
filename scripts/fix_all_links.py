"""fix_all_links.py — Fix hardcoded absolute links across documentation files.
Replaces /radiology-protocols/ links with correct relative links so pages
navigate properly in static HTML (file://, local server at root, or subpath).
"""

from pathlib import Path

def update_file(path: Path, replacements: list[tuple[str, str]]) -> int:
    content = path.read_text(encoding='utf-8')
    orig = content
    for old, new in replacements:
        content = content.replace(old, new)
    if content != orig:
        path.write_text(content, encoding='utf-8')
        return 1
    return 0

def main():
    modified = 0

    # 1. docs/index.md
    p_index = Path('docs/index.md')
    if p_index.exists():
        modified += update_file(p_index, [
            ('href="/radiology-protocols/', 'href="')
        ])
        print("Updated docs/index.md")

    # 2. docs/ct/index.md
    p_ct = Path('docs/ct/index.md')
    if p_ct.exists():
        modified += update_file(p_ct, [
            ('href="/radiology-protocols/ct/compare/"', 'href="compare/"'),
            ('href="/radiology-protocols/iris/"', 'href="../iris/"'),
            ('href="/radiology-protocols/ct/', 'href="')
        ])
        print("Updated docs/ct/index.md")

    # 3. docs/irm/index.md
    p_irm = Path('docs/irm/index.md')
    if p_irm.exists():
        modified += update_file(p_irm, [
            ('href="/radiology-protocols/iris/"', 'href="../iris/"'),
            ('href="/radiology-protocols/irm/', 'href="')
        ])
        print("Updated docs/irm/index.md")

    # 4. docs/rx/index.md
    p_rx = Path('docs/rx/index.md')
    if p_rx.exists():
        modified += update_file(p_rx, [
            ('href="/radiology-protocols/iris/"', 'href="../iris/"'),
            ('href="/radiology-protocols/rx/', 'href="')
        ])
        print("Updated docs/rx/index.md")

    # 5. docs/eco/index.md
    p_eco = Path('docs/eco/index.md')
    if p_eco.exists():
        modified += update_file(p_eco, [
            ('href="/radiology-protocols/iris/"', 'href="../iris/"'),
            ('href="/radiology-protocols/eco/', 'href="')
        ])
        print("Updated docs/eco/index.md")

    # 6. docs/fluoro/index.md
    p_fluoro = Path('docs/fluoro/index.md')
    if p_fluoro.exists():
        modified += update_file(p_fluoro, [
            ('href="/radiology-protocols/iris/"', 'href="../iris/"'),
            ('href="/radiology-protocols/fluoro/', 'href="')
        ])
        print("Updated docs/fluoro/index.md")

    # 7. docs/iris.md
    p_iris = Path('docs/iris.md')
    if p_iris.exists():
        modified += update_file(p_iris, [
            ('href="/radiology-protocols/ct/compare/"', 'href="../ct/compare/"')
        ])
        print("Updated docs/iris.md")

    # 8 & 9. Protocol files and subcategory index files in docs/<modality>/<category>/
    proto_count = 0
    for p in Path('docs').glob('**/*.md'):
        rel = p.relative_to('docs')
        if len(rel.parts) >= 2 and rel.parts[0] in ('ct', 'irm', 'rx', 'eco', 'fluoro'):
            # Any link to iris in these subfolders should be relative ../../iris.md
            if len(rel.parts) == 3:
                # e.g. ct/chest/ct-pe.md or ct/chest/index.md
                c = update_file(p, [
                    ('](/radiology-protocols/iris/)', '](../../iris.md)'),
                    ('"/radiology-protocols/iris/"', '"../../iris.md"'),
                ])
                if c:
                    proto_count += 1

    print(f"Updated {proto_count} protocol and subcategory markdown files with relative IRIS links.")

if __name__ == '__main__':
    main()
