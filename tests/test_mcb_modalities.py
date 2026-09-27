"""Check imported source integrity, catalog coverage and navigation integration."""
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
import yaml
from scripts.generate_mcb_modalities import add_nav, block
from scripts.rx_catalog import on_page_markdown
from scripts.search_catalog import record_for

ROOT = Path(__file__).resolve().parents[1]

def test_nav_preserves_following_top_level_settings(tmp_path):
    path = tmp_path/'.pages'
    path.write_text('title: CT\nnav:\n  - index.md\ncollapse_single_pages: true',encoding='utf-8')
    add_nav(path, 'MCB', 'mcb')
    add_nav(path, 'MCB', 'mcb')
    data = yaml.safe_load(path.read_text(encoding='utf-8'))
    assert data['collapse_single_pages'] is True
    assert data['nav'] == ['index.md', {'MCB':'mcb'}]

def test_attaching_original_preserves_existing_summary_and_is_idempotent():
    original = '---\ntitle: Existing\n---\n# Existing\n\nClinical content\n'
    once = block(original, 'Original PDF', after_heading=True)
    assert block(once, 'Original PDF', after_heading=True) == once
    assert once.startswith('---\ntitle: Existing\n---\n# Existing')
    assert 'Clinical content' in once
    assert once.count('## Sinteza existentă') == 1

def test_curated_rx_catalog_is_not_replaced_by_empty_auto_catalog():
    page = SimpleNamespace(meta={'catalog_manual':True}, file=SimpleNamespace(src_path='rx/mcb/index.md'))
    assert on_page_markdown('Curated documents',page,{},[]) == 'Curated documents'

def test_interventional_documents_are_searchable_with_mcb_source_filter():
    meta = {'title':'IR Medicație', 'slug':'ir-med', 'modality':'ir', 'category':'proceduri', 'sources':[{'title':'MCB Radiology — Med & Lab','url':'https://ref.mcbradiology.com/IR/example.pdf'}]}
    record = record_for(meta,'ir/proceduri/ir-med.md','ir/proceduri/ir-med/')
    assert record['modality'] == 'ir'
    assert record['source_filters'] == ['MCB Radiology']

def test_imported_catalog_and_pdf_hashes():
    report = json.loads((ROOT/'data/mcb-modalities/catalog.json').read_text(encoding='utf-8'))
    catalog = report['catalog']
    assert report['counts'] == {'rx':22,'eco':75,'ir':7,'fluoro':3,'mn':36,'ct':112}
    assert len(catalog) == 255
    assert report['updated_existing'] == 25
    assert len({r['url'] for r in catalog}) == 255
    assert len({r['path'] for r in catalog}) == 255
    assert len(report['failures']) == 1
    assert report['failures'][0]['url'].endswith('/FRAX%20Guidelines.pdf')
    for row in catalog:
        page = ROOT/'docs'/row['path']
        text = page.read_text(encoding='utf-8')
        assert row['url'] in text
        assets = ROOT/'docs'/row['assets']
        assert hashlib.sha256((assets/'document.pdf').read_bytes()).hexdigest() == row['sha256']
        assert len(list(assets.glob('pagina-*.png'))) == row['preview_pages']
        if row['pages'] > 30:
            assert row['preview_pages'] == 3
            assert f"toate cele {row['pages']} de pagini" in text
    for path in (ROOT/'docs').rglob('.pages'):
        data = yaml.safe_load(path.read_text(encoding='utf-8'))
        nav = data.get('nav',[]) if isinstance(data,dict) else []
        assert sum(isinstance(x,dict) and 'mcb' in x.values() for x in nav) <= 1, path
