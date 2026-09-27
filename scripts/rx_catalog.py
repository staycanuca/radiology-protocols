"""Keep RX category landing pages in sync with their protocol files.

Used as a MkDocs hook; run directly to refresh the Markdown catalogs on disk.
"""
from pathlib import Path
import re

import yaml

ROOT = Path(__file__).resolve().parents[1]


def read_metadata(path):
    text = path.read_text(encoding='utf-8')
    match = re.match(r'\A---\s*\n(.*?)\n---(?:\s*\n|$)', text, re.S)
    return (yaml.safe_load(match[1]) or {}) if match else {}


def on_nav(nav, config, files):
    """Use exactly the catalog's title ordering in RX sidebar sections."""
    def visit(items):
        for item in items:
            children = getattr(item, 'children', None)
            if children is None:
                continue
            pages = [child for child in children if getattr(child, 'is_page', False)]
            if pages and all(len(Path(p.file.src_path).parts) == 3
                             and Path(p.file.src_path).parts[0] == 'rx' for p in pages):
                for page in pages:
                    # on_nav runs before MkDocs reads page frontmatter.
                    metadata = read_metadata(Path(config['docs_dir']) / page.file.src_path)
                    if metadata.get('slug'):
                        page.title = ' '.join(str(metadata.get('title') or Path(page.file.src_path).stem).split())
                # Sort pages alphabetically if this section contains only pages (e.g. subsection items or flat section)
                if len(pages) == len(children):
                    children.sort(key=lambda child: (
                        0 if getattr(child, 'is_page', False) and Path(child.file.src_path).name == 'index.md' else 1,
                        (child.title or '').casefold(),
                        getattr(getattr(child, 'file', None), 'src_path', ''),
                    ))
            visit(children)
    visit(nav.items)
    return nav


def render_catalog(directory: Path) -> str:
    navigation = directory / '.pages'
    metadata = yaml.safe_load(navigation.read_text(encoding='utf-8')) if navigation.exists() else {}
    title = (metadata or {}).get('title', directory.name.replace('-', ' ').title())
    nav = (metadata or {}).get('nav', [])

    # Map all protocols in this directory to their clean display title
    proto_map = {}
    for path in directory.glob('*.md'):
        if path.name == 'index.md':
            continue
        fm = read_metadata(path)
        if isinstance(fm, dict) and fm.get('slug'):
            label = ' '.join(str(fm.get('title') or path.stem).split())
            label = label.replace('\\', '\\\\').replace('[', r'\[').replace(']', r'\]')
            proto_map[path.name] = label

    # Check if nav defines subsections (dict entries with lists of files)
    subsections = []
    handled_files = set()
    for item in nav:
        if isinstance(item, dict):
            for sec_title, sec_files in item.items():
                if isinstance(sec_files, list):
                    subsections.append((sec_title, sec_files))
                    handled_files.update(sec_files)

    if subsections:
        total_count = len(proto_map)
        lines = [
            f'# Protocoale Rx — {title}\n',
            f'Catalog cu **{total_count} protocoale** din această categorie, structurate pe segmente anatomice.\n'
        ]
        for sec_title, sec_files in subsections:
            sec_protos = []
            for fname in sec_files:
                if fname in proto_map:
                    sec_protos.append((proto_map[fname], fname))
            sec_protos.sort(key=lambda x: x[0].casefold())
            if sec_protos:
                lines.append(f'## {sec_title} ({len(sec_protos)})\n')
                for p_label, fname in sec_protos:
                    lines.append(f'- [{p_label}]({fname})')
                lines.append('')

        # Uncategorized in subsections if any
        remaining = [(p_label, fname) for fname, p_label in proto_map.items() if fname not in handled_files]
        if remaining:
            remaining.sort(key=lambda x: x[0].casefold())
            lines.append(f'## Alte Protocoale ({len(remaining)})\n')
            for p_label, fname in remaining:
                lines.append(f'- [{p_label}]({fname})')
            lines.append('')

        return '\n'.join(lines)
    else:
        protocols = [(label, fname) for fname, label in proto_map.items()]
        protocols.sort(key=lambda item: (item[0].casefold(), item[1]))
        links = '\n'.join(f'- [{label}]({name})' for label, name in protocols)
        return (f'# Protocoale Rx — {title}\n\n'
                f'Catalog cu **{len(protocols)} protocoale** din această categorie.\n\n'
                f'{links}\n')


def on_page_markdown(markdown, page, config, files):
    if getattr(page, 'meta', {}).get('catalog_manual'):
        return markdown
    relative = Path(page.file.src_path)
    if len(relative.parts) == 3 and relative.parts[0] == 'rx' and relative.name == 'index.md':
        return render_catalog(Path(config['docs_dir']) / relative.parent)
    return markdown


if __name__ == '__main__':
    for directory in sorted((ROOT / 'docs/rx').iterdir()):
        if directory.is_dir() and any(directory.glob('*.md')):
            target = directory / 'index.md'
            if target.exists() and read_metadata(target).get('catalog_manual'):
                continue
            content = render_catalog(directory)
            if not target.exists() or target.read_text(encoding='utf-8') != content:
                target.write_text(content, encoding='utf-8')
            print(f'Actualizat: {target.relative_to(ROOT)}')
