#!/usr/bin/env python3
"""
Generate sitemap.json from YAML front matter in CT protocol Markdown files.

Reads config/institution.yml for site_url, then scans all docs/ct/**/*.md
front matter to output docs/javascripts/sitemap.json.

The radiology-agent extension polls this file at the deployed Pages URL to
incorporate protocols into query matching without requiring cross-repo pushes.

Sitemap entry shape:
  {
    "slug": "ct-pe",
    "title": "CT Pulmonary Embolism",
    "url": "https://hospital.github.io/radiology-protocols/ct/chest/ct-pe/",
    "synonyms": ["CTPA", "PE protocol"],
    "clinical_indications": ["suspected PE", "acute dyspnea"],
    "category": "chest"
  }
"""

import json
from pathlib import Path

import yaml


def parse_frontmatter(content):
    """Return frontmatter dict from a Markdown file with YAML front matter."""
    if not content.startswith('---\n'):
        return {}
    end = content.find('\n---\n', 4)
    if end == -1:
        return {}
    fm_text = content[4:end]
    try:
        return yaml.safe_load(fm_text) or {}
    except yaml.YAMLError:
        return {}


def load_institution_config():
    config_path = Path('config/institution.yml')
    if not config_path.exists():
        print('WARNING: config/institution.yml not found — using empty site_url')
        return {}
    with open(config_path, encoding='utf-8') as f:
        cfg = yaml.safe_load(f) or {}
    return cfg.get('institution', {})


def build_url(site_url, category, slug):
    """Construct the deployed Pages URL for a protocol.

    site_url from institution.yml is the full base (e.g. https://host/repo),
    so URL = site_url/ct/category/slug/.
    """
    base = site_url.rstrip('/') if site_url else ''
    return f"{base}/ct/{category}/{slug}/"


def generate_sitemap():
    institution = load_institution_config()
    site_url = institution.get('site_url', '')

    docs_dir = Path('docs/ct')
    entries = []

    for md_file in sorted(docs_dir.rglob('*.md')):
        if md_file.name in ('index.md', 'compare.md'):
            continue

        content = md_file.read_text(encoding='utf-8')
        fm = parse_frontmatter(content)

        if not fm:
            print(f'WARNING: No front matter in {md_file} — skipping')
            continue

        slug = fm.get('slug') or md_file.stem
        title = fm.get('title', '')
        category = fm.get('category', '')
        synonyms = fm.get('synonyms') or []
        indications = fm.get('clinical_indications') or []

        url = build_url(site_url, category, slug)

        entries.append({
            'slug': slug,
            'title': title,
            'url': url,
            'synonyms': synonyms,
            'clinical_indications': indications,
            'category': category,
        })

    entries.sort(key=lambda x: (x['category'], x['title']))

    output_path = Path('docs/javascripts/sitemap.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(entries, f, indent=2)

    print(f'Generated sitemap with {len(entries)} protocols')
    print(f'Saved to: {output_path}')


if __name__ == '__main__':
    generate_sitemap()
