#!/usr/bin/env python3
"""
Generate protocol forms index and institution config JSON files.

Reads all protocol files across all modalities (ct, irm, rx, eco, fluoro),
skipping index.md and compare.md, parses YAML front matter, and outputs:
  - docs/javascripts/protocol-forms-index.json  — one entry per protocol with all FM fields + modality
  - docs/javascripts/institution-config.json     — institution config from config/institution.yml
"""

import json
from pathlib import Path

import yaml


# ---------------------------------------------------------------------------
# Front matter parsing
# ---------------------------------------------------------------------------

def parse_frontmatter(content: str) -> dict:
    """Return front matter dict from a Markdown file with YAML front matter.

    Returns {} if no front matter is present or if YAML is malformed.
    """
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


# ---------------------------------------------------------------------------
# Protocol entry builder
# ---------------------------------------------------------------------------

def detect_modality(fm: dict, filepath: Path) -> str:
    """Detect modality code (ct, irm, rx, eco, fluoro)."""
    if fm.get('modality'):
        return str(fm.get('modality')).lower()
    p_str = str(filepath).replace('\\', '/').lower()
    for mod in ('ct', 'irm', 'rx', 'eco', 'fluoro'):
        if p_str.startswith(f"{mod}/") or f"/{mod}/" in p_str:
            return mod
    return 'ct'


def build_forms_entry(fm: dict, filepath: Path) -> dict:
    """Build a protocol dict for the forms index from front matter.

    All 17 required fields are always present. Missing fields use empty defaults:
      - dict fields: {}
      - list fields: []
      - string fields: ''
    None values are never passed through.
    """
    mod = detect_modality(fm, filepath)

    # Position
    pos = fm.get('position') or ''
    if not pos and isinstance(fm.get('patient_prep'), dict):
        pos = fm.get('patient_prep', {}).get('position', '')

    # NPO
    npo = fm.get('npo') or ''
    if not npo and isinstance(fm.get('patient_prep'), dict):
        npo = fm.get('patient_prep', {}).get('npo', '')

    # Premedication
    premed = fm.get('premedication') or ''
    if not premed and isinstance(fm.get('patient_prep'), dict):
        premed = fm.get('patient_prep', {}).get('premedication', '')
    if not premed and fm.get('contrast_preparation'):
        if isinstance(fm.get('contrast_preparation'), dict):
            premed = "; ".join(f"{k}: {v}" for k, v in fm.get('contrast_preparation').items())
        else:
            premed = str(fm.get('contrast_preparation'))

    # Contrast
    contrast = fm.get('contrast') or {}
    if not isinstance(contrast, dict):
        contrast = {'agent': str(contrast)}

    # Series / Sequences / Projections / Views
    series = fm.get('series') or []
    if not series:
        if fm.get('sequences') and isinstance(fm.get('sequences'), list):
            series = [
                {
                    'name': s.get('name') or s.get('sequence', ''),
                    'start': s.get('plane', ''),
                    'end': s.get('tr_te', ''),
                    'delay': '',
                    'thickness': str(s.get('slice_gap') or s.get('thickness', '')),
                    'notes': s.get('notes', ''),
                }
                for s in fm.get('sequences') if isinstance(s, dict)
            ]
        elif fm.get('standard_views') and isinstance(fm.get('standard_views'), list):
            series = [
                {
                    'name': v.get('view') or v.get('name', ''),
                    'start': v.get('structures', ''),
                    'end': '',
                    'delay': '',
                    'thickness': '',
                    'notes': v.get('landmarks', ''),
                }
                for v in fm.get('standard_views') if isinstance(v, dict)
            ]
        elif fm.get('phases') and isinstance(fm.get('phases'), list):
            series = [
                {
                    'name': p.get('name') or p.get('phase', ''),
                    'start': p.get('projection', ''),
                    'end': '',
                    'delay': p.get('timing', ''),
                    'thickness': '',
                    'notes': p.get('notes', ''),
                }
                for p in fm.get('phases') if isinstance(p, dict)
            ]
        elif fm.get('projections') and isinstance(fm.get('projections'), list):
            series = [
                {
                    'name': str(pr.get('name') if isinstance(pr, dict) else pr),
                    'start': '',
                    'end': '',
                    'delay': '',
                    'thickness': '',
                    'notes': '',
                }
                for pr in fm.get('projections')
            ]

    # Notes
    notes = fm.get('notes') or {}
    if not isinstance(notes, dict):
        notes = {'rad': str(notes)}

    # Safety
    safety = fm.get('safety') or {}
    if not isinstance(safety, dict):
        safety = {'renal': str(safety)}
    if not safety and fm.get('protection'):
        prot = fm.get('protection')
        if isinstance(prot, list):
            prot_str = "; ".join(prot)
        else:
            prot_str = str(prot)
        safety = {'renal': prot_str, 'allergy': ''}

    # Clinical indications
    indications = fm.get('clinical_indications') or []
    if isinstance(indications, str):
        indications = [indications]

    return {
        'filepath': str(filepath),
        'slug': fm.get('slug') or '',
        'title': fm.get('title') or '',
        'category': fm.get('category') or '',
        'modality': mod,
        'protocol_type': fm.get('protocol_type') or '',
        'last_updated': fm.get('last_updated') or '',
        'author': fm.get('author') or '',
        'synonyms': fm.get('synonyms') or [],
        'clinical_indications': indications,
        'position': pos,
        'npo': npo,
        'premedication': premed,
        'contrast': contrast,
        'series': series,
        'recons': fm.get('recons') or [],
        'notes': notes,
        'safety': safety,
    }


# ---------------------------------------------------------------------------
# Institution config builder
# ---------------------------------------------------------------------------

def build_institution_config(config_path: Path) -> dict:
    """Read institution.yml and return the institution-config dict."""
    try:
        with open(config_path, encoding='utf-8') as f:
            cfg = yaml.safe_load(f) or {}
    except (FileNotFoundError, yaml.YAMLError):
        cfg = {}

    institution = cfg.get('institution') or {}
    contact = cfg.get('contact') or {}

    return {
        'feedback_url': contact.get('feedback_url') or '',
        'google_form_url': contact.get('google_form_url') or '',
        'google_form_entry_title': contact.get('google_form_entry_title') or '',
        'google_form_entry_body': contact.get('google_form_entry_body') or '',
        'institution_name': institution.get('name') or '',
        'site_url': institution.get('site_url') or '',
        'base_path': institution.get('base_path') or '',
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def generate_forms_index():
    modalities = ['ct', 'irm', 'rx', 'eco', 'fluoro']
    protocols = []

    for mod in modalities:
        mod_dir = Path(f'docs/{mod}')
        if not mod_dir.exists():
            continue
        for md_file in sorted(mod_dir.rglob('*.md')):
            if md_file.name in ('index.md', 'compare.md'):
                continue

            content = md_file.read_text(encoding='utf-8')
            fm = parse_frontmatter(content)

            if not fm:
                print(f'WARNING: No front matter in {md_file} — skipping')
                continue

            entry = build_forms_entry(fm, md_file.relative_to('docs'))
            protocols.append(entry)

    protocols.sort(key=lambda x: (x.get('modality', ''), x.get('category', ''), x.get('title', '')))

    # Write protocol forms index
    forms_index_path = Path('docs/javascripts/protocol-forms-index.json')
    with open(forms_index_path, 'w', encoding='utf-8') as f:
        json.dump(protocols, f, indent=2, ensure_ascii=False)

    print(f'Generated forms index with {len(protocols)} protocols across modalities: {modalities}')
    print(f'Saved to: {forms_index_path}')

    # Write institution config
    institution_config = build_institution_config(Path('config/institution.yml'))
    config_output_path = Path('docs/javascripts/institution-config.json')
    with open(config_output_path, 'w', encoding='utf-8') as f:
        json.dump(institution_config, f, indent=2, ensure_ascii=False)

    print(f'Saved institution config to: {config_output_path}')


if __name__ == '__main__':
    generate_forms_index()
