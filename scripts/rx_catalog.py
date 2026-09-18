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
    protocols = []
    for path in directory.glob('*.md'):
        if path.name == 'index.md':
            continue
        fm = read_metadata(path)
        if isinstance(fm, dict) and fm.get('slug'):
            label = ' '.join(str(fm.get('title') or path.stem).split())
            label = label.replace('\\', '\\\\').replace('[', r'\[').replace(']', r'\]')
            protocols.append((label, path.name))
    protocols.sort(key=lambda item: (item[0].casefold(), item[1]))
    links = '\n'.join(f'- [{title}]({name})' for title, name in protocols)
    return (f'# Protocoale Rx — {title}\n\n'
            f'Catalog cu **{len(protocols)} protocoale** din această categorie.\n\n'
            f'{links}\n')


def on_page_markdown(markdown, page, config, files):
    relative = Path(page.file.src_path)
    if len(relative.parts) == 3 and relative.parts[0] == 'rx' and relative.name == 'index.md':
        return render_catalog(Path(config['docs_dir']) / relative.parent)
    return markdown


if __name__ == '__main__':
    for directory in sorted((ROOT / 'docs/rx').iterdir()):
        if directory.is_dir() and any(directory.glob('*.md')):
            target = directory / 'index.md'
            content = render_catalog(directory)
            if not target.exists() or target.read_text(encoding='utf-8') != content:
                target.write_text(content, encoding='utf-8')
            print(f'Actualizat: {target.relative_to(ROOT)}')
