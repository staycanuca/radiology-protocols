"""Regenerate the source Omnisearch asset; normal MkDocs builds also refresh it."""
from pathlib import Path
try:
    from .search_catalog import collect, write_index
except ImportError:
    from search_catalog import collect, write_index

ROOT = Path(__file__).resolve().parents[1]


def generate_omnisearch_index():
    records, _ = collect(ROOT / 'docs')
    target = ROOT / 'docs/javascripts/omnisearch-index.json'
    write_index(target, records)
    print(f'Omnisearch: {len(records)} protocols -> {target}')


if __name__ == '__main__':
    generate_omnisearch_index()
