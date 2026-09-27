import pytest
import yaml

from scripts import admin


@pytest.mark.parametrize('modality', ['ct', 'irm', 'rx', 'eco', 'fluoro'])
def test_editor_keeps_documented_sources_and_flags_review(tmp_path, monkeypatch, modality):
    path = tmp_path / 'exam.md'
    original = {'slug': 'exam', 'title': 'Titlu inițial', 'category': 'abdomen',
                'modality': modality, 'clinical_indications': [], 'notes': {},
                'sources': [{'title': 'Manual', 'url': 'https://example.org/manual', 'edition': '12'}],
                'clinical_status': 'draft_not_for_clinical_use',
                'provenance': {'version': 'v1', 'source_verification': {'reviewer': 'Test'}}}
    monkeypatch.setattr(admin, 'find_protocol', lambda slug: {'fm': original, 'filepath': path})
    monkeypatch.setattr(admin, 'rebuild_indexes', lambda: [])
    monkeypatch.setattr(admin, 'trigger_background_build', lambda: None)
    with admin.app.test_client() as client:
        response = client.post('/edit/exam', data={'modality': modality, 'title': 'Titlu nou', 'category': 'abdomen'})
    assert response.json['success'], response.json
    metadata = yaml.safe_load(path.read_text(encoding='utf-8').split('---', 2)[1])
    assert metadata['sources'] == original['sources']
    assert metadata['clinical_status'] == original['clinical_status']
    assert metadata['provenance']['review_required'] is True
    assert not original['provenance'].get('review_required')
