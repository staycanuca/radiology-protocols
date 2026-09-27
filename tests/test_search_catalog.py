import json
from pathlib import Path
from types import SimpleNamespace
import pytest
from scripts import search_catalog as catalog, search_enhancer as native


@pytest.mark.parametrize('meta,expected', [({}, 'unknown'), ({'contrast': {'agent': 'N/A'}}, 'unknown'),
    ({'contrast': {'agent': 'Neprecizat în sursă'}}, 'unknown'), ({'contrast': {'agent': '—'}}, 'unknown'),
    ({'contrast': {'agent': 'Fără contrast'}}, 'native'), ({'protocol_type':'non-contrast'}, 'native'),
    ({'contrast': {'agent': 'Gadoliniu'}}, 'contrast'), ({'contrast': {'agent': 'Bariu oral'}}, 'contrast'),
    ({'contrast': {'agent': 'Gadoliniu opțional'}}, 'variable'),
    ({'title':'IRM nativ și cu contrast','protocol_type':'contrast-enhanced'}, 'variable'),
    ({'title':'CT without contrast','protocol_type':'contrast-enhanced'}, 'variable')])
def test_contrast_is_not_guessed(meta, expected):
    assert catalog.contrast_state(meta) == expected


def test_record_preserves_full_terms_and_current_source():
    meta = {'title':'RX Mână PA', 'slug':'old-english-slug', 'category':'membru-superior',
            'synonyms':['s'+str(i) for i in range(9)], 'clinical_indications':['i'+str(i) for i in range(9)],
            'author':'Department', 'sources':[{'title':'Clark atlas', 'edition':'12', 'pages':'80'}], 'status':'draft'}
    record = catalog.record_for(meta, 'rx/membru-superior/test.md', 'rx/membru-superior/test/', 'Membru superior', 'Mână')
    assert len(record['synonyms']) == len(record['indications']) == 9
    assert record['source_filters'] == ['Clark']
    assert record['equipment'] == []
    assert record['region'] == 'upper'
    assert 'hand' in record['aliases']
    assert 'clarck' in record['aliases']
    assert 'Ciornă' in record['publication']


def test_source_family_recognizes_mia():
    assert catalog.source_family('MIA Radiology Modality Wiki') == 'MIA Radiology'
    assert catalog.source_family('MCB Radiology Protocols') == 'MCB Radiology'
    assert catalog.source_family('Medford Radiology Group Clinical Guidelines') == 'Medford Radiology'
    assert catalog.source_family('MRG Reading Room Documents') == 'Medford Radiology'


def test_build_refreshes_metadata_and_removes_deleted_files(tmp_path):
    docs = tmp_path/'docs'; (docs/'rx/coloana').mkdir(parents=True)
    path = docs/'rx/coloana/test.md'
    path.write_text('---\ntitle: Titlu nou\nslug: old\ncategory: coloana\nsynonyms: [ultimul]\n---\n# Test', encoding='utf-8')
    (path.parent/'.pages').write_text('title: Coloană\nnav:\n  - Cervicală:\n    - test.md\n', encoding='utf-8')
    config = {'docs_dir':str(docs), 'site_dir':str(tmp_path/'site')}
    file = SimpleNamespace(src_uri='rx/coloana/test.md', url='rx/coloana/test/', is_documentation_page=lambda: True)
    native.on_pre_build(config); native.on_files([file], config); native.on_post_build(config)
    index = tmp_path/'site/javascripts/omnisearch-index.json'
    record = json.loads(index.read_text(encoding='utf-8'))['protocols'][0]
    assert record['title'] == 'Titlu nou'
    assert record['segment'] == 'Cervicală'
    path.unlink()
    native.on_pre_build(config); native.on_files([], config); native.on_post_build(config)
    assert json.loads(index.read_text())['protocols'] == []
    native.on_pre_build({})


def test_worker_has_content_hash_and_nested_pages_reference_it(tmp_path):
    directory = tmp_path/'assets/javascripts/workers'
    directory.mkdir(parents=True)
    worker = directory/'search.123.min.js'
    worker.write_text('self.original = true;', encoding='utf-8')
    config = SimpleNamespace(theme=SimpleNamespace(dirs=[str(tmp_path)]))
    native.on_config(config)
    first_name = native._worker_name
    html = '<script id="__config">{"search":"../../assets/javascripts/workers/search.123.min.js"}</script>'
    updated = native.on_post_page(html, None, config)
    assert first_name in updated
    assert first_name in native.on_post_template(html, '404.html', config)
    assert '../../assets/' in updated
    assert worker.read_text() == 'self.original = true;'
    worker.write_text('self.original = false;', encoding='utf-8')
    native.on_config(config)
    assert native._worker_name != first_name
    native._worker_name = native._worker_source = None


def test_native_excludes_ghosts_and_old_slug_boosts():
    native.on_pre_build({})
    native._pages['rx/test/'] = {'synonyms':['ultimul sinonim']}
    data = {'docs':[{'location':'rx/test/', 'title':'Mână', 'text':'Poziție mână'},
                    {'location':'rx/test/#protocol-provenance-title', 'title':'Fake', 'text':''},
                    {'location':'rx/test/#surse', 'title':'Surse', 'text':'Merrill'}]}
    result = native.enhance(data)
    assert len(result['docs']) == 2
    assert 'mana' in result['docs'][0]['title_terms']
    assert 'sinonim' in result['docs'][0]['keywords']
    assert 'test' not in result['docs'][0]['keywords']
    assert 'sinonim' not in result['docs'][1]['keywords']
    assert 'tags' not in result['docs'][0]
    assert native.enhance(json.loads(json.dumps(result))) == result
    native.on_pre_build({})
