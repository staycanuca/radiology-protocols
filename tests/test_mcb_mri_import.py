"""Integrity checks for the MCB PDF import and variable sequence table layouts."""
import hashlib
import importlib.util
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('generate_mcb_mri', ROOT / 'scripts/generate_mcb_mri.py')
generator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)


def test_breast_water_suppression_does_not_shift_thickness():
    record = {'tables': [[[
        ['Pulse Sequence', 'PACS Name', 'plane', 'fat\nsat', 'w a t e r\nsat', 's l i c e\n(mm)', 'g a p\n(mm)', 'f i r s t\nslice'],
        ['T2', 'SILICONE', 'ax', 'yes', 'yes', '3', '0.5', 'top'],
        ['CONTRAST instructions', None, None, None, None, None, None, None],
    ]]]}
    row = generator.sequence_tables(record)[0]['rows'][0]
    assert row['slice_mm'] == '3'
    assert row['water_sat'] == 'yes'
    assert row['gap_mm'] == '0.5'


def test_absent_gap_is_not_inferred_from_first_slice():
    record = {'tables': [[[
        ['Pulse Sequence', 'PACS Name', 'plane', 'fat sat', 'slice (mm)', 'first slice'],
        ['T1', 'T1 AX', 'ax', 'no', '2', 'top'],
    ]]]}
    row = generator.sequence_tables(record)[0]['rows'][0]
    assert row['slice_mm'] == '2'
    assert 'gap_mm' not in row
    assert row['first_slice'] == 'top'


def test_entire_catalog_has_original_assets_and_source_metadata():
    catalog = json.loads((ROOT / 'data/mcb-mri/catalog.json').read_text(encoding='utf-8'))
    assert len(catalog) == 78
    assert sum(c['number'] > 0 for c in catalog) == 77
    assert len({c['source_url'] for c in catalog}) == len(catalog)
    assert len({c['slug'] for c in catalog}) == len(catalog)
    for item in catalog:
        page = ROOT / 'docs/irm' / item['category'] / (item['slug'] + '.md')
        content = page.read_text(encoding='utf-8')
        fm = yaml.safe_load(content.split('---', 2)[1])
        assert fm['sources'][0]['url'] == item['source_url']
        assert fm['sources'][0]['pages'] == list(range(1, item['pages'] + 1))
        assets = ROOT / 'docs/assets/mcb-mri' / item['slug']
        assert hashlib.sha256((assets / 'protocol.pdf').read_bytes()).hexdigest() == item['sha256']
        assert len(list(assets.glob('pagina-*.png'))) == item['pages']
        if item['number'] > 0:
            assert fm['sequences'], item['title']


def test_only_unavailable_source_is_stale_duplicate_tmj_link():
    records = json.loads((ROOT / 'data/mcb-mri/manifest.json').read_text(encoding='utf-8'))
    errors = [r for r in records if 'error' in r]
    assert len(errors) == 1
    assert errors[0]['url'].endswith('/Neuro/20%20TMJs.pdf')
    assert any(r.get('file') == 'Neuro/21 TMJs.pdf' for r in records)
