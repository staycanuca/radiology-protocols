import json
from scripts.prepare_rx_rollout import prepare
from scripts.move_rx_drafts_to_library import transfer
from protocol_workbench.app import frontmatter


def test_transfer_keeps_review_status_and_is_repeatable(tmp_path):
    prepare(tmp_path)
    assert transfer(tmp_path) == 10
    assert transfer(tmp_path) == 0
    documents = list((tmp_path / 'docs/rx').glob('*/rx-*.md'))
    assert len(documents) == 10
    for path in documents:
        fm, body = frontmatter(path.read_text(encoding='utf-8'))
        assert fm['clinical_status'] == 'draft_not_for_clinical_use'
        assert fm['sources'] and fm['review_required_fields']
        assert 'workbench_review' not in fm
        assert 'Ciornă pentru revizuire' in body
        assert path.name in (path.parent / 'index.md').read_text(encoding='utf-8')


def test_main_editor_preserves_review_metadata(tmp_path, monkeypatch):
    from scripts import admin
    prepare(tmp_path)
    transfer(tmp_path)
    path = next((tmp_path / 'docs/rx').glob('*/rx-*.md'))
    fm, _ = frontmatter(path.read_text(encoding='utf-8'))
    monkeypatch.setattr(admin, 'find_protocol', lambda slug: {'fm': fm, 'filepath': path})
    monkeypatch.setattr(admin, 'rebuild_indexes', lambda: [])
    monkeypatch.setattr(admin, 'trigger_background_build', lambda: None)
    response = admin.app.test_client().post('/edit/' + fm['slug'], data={
        'modality': 'rx', 'title': fm['title'], 'category': fm['category']})
    assert response.json['success'], response.json
    saved, body = frontmatter(path.read_text(encoding='utf-8'))
    for key in ('clinical_status', 'sources', 'standard_views', 'review_required_fields'):
        assert saved[key] == fm[key]
    assert '## Surse de documentare' in body
