import json
import re
import yaml

from scripts.prepare_rx_rollout import prepare
from scripts.render_rx_protocol import render_rx_document, PENDING
from protocol_workbench.smart_extractor import extract_rx_parameters


def test_missing_values_are_not_clinical_defaults():
    document = render_rx_document({'title': 'Test', 'tech_params': {}})
    assert PENDING in document
    assert 'Grad A' not in document
    assert '70 - 80' not in document


def test_heading_is_not_patient_position():
    assert 'position' not in extract_rx_parameters('Patient position\nTerminology\nOther content')
    assert extract_rx_parameters('Patient position: supine on table')['position'] == 'supine on table'


def test_batch_is_complete_and_preserves_user_edits(tmp_path):
    assert prepare(tmp_path) == 10
    files = list((tmp_path / '.protocol-workbench').glob('*.json'))
    assert len(files) == 10
    for path in files:
        draft = json.loads(path.read_text(encoding='utf-8'))
        fm = yaml.safe_load(draft['document'].split('---', 2)[1])
        assert fm['clinical_status'] == 'draft_not_for_clinical_use'
        assert fm['review_required_fields']
        assert len(fm['standard_views']) >= 2
        assert draft['sources']
        assert fm['tech_params']['kv'] == PENDING
    preserved = files[0]
    data = json.loads(preserved.read_text(encoding='utf-8'))
    data['document'] += '\nUser revision\n'
    preserved.write_text(json.dumps(data), encoding='utf-8')
    before = preserved.read_bytes()
    assert prepare(tmp_path) == 0
    assert preserved.read_bytes() == before


def test_prepared_draft_is_visible_but_cannot_be_published(tmp_path):
    from protocol_workbench.app import create_app
    prepare(tmp_path)
    client = create_app(tmp_path, tmp_path / '.protocol-workbench').test_client()
    page = client.get('/').get_data(as_text=True)
    token = json.loads(re.search(r'const TOKEN=("[^"]+")', page)[1])
    listing = client.get('/api/drafts')
    assert listing.status_code == 200
    assert len(listing.json) == 10
    identifier = next((tmp_path / '.protocol-workbench').glob('*.json')).stem
    response = client.post(f'/api/drafts/{identifier}/validate', headers={'X-Workbench-Token': token})
    assert response.status_code == 200
    assert response.json['errors']
    assert any('clinic' in error.lower() for error in response.json['errors'])
