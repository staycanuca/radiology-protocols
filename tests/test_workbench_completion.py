"""Synthetic values only: verifies merge semantics, not clinical recommendations."""
import io
import json
import subprocess
import shutil
import re
from pathlib import Path

import pytest
import yaml

from test_protocol_workbench import workbench, draft
from protocol_workbench import app as wb, completion
from protocol_workbench.image_search import search_images, rank_images


def attach(workbench, identifier, value):
    client, headers, _, _ = workbench
    response = client.post('/api/drafts/' + identifier + '/sources/upload',
        data={'file': (io.BytesIO((value + '\n' + 'Synthetic evidence for software tests. ' * 3).encode()), value + '.txt'), 'title': value}, headers=headers)
    assert response.status_code == 200, response.json
    return response.json


@pytest.fixture
def extractor(monkeypatch):
    monkeypatch.setattr(completion, 'extract_parameters_by_modality',
        lambda text, modality, title: {'position': text.strip().splitlines()[0]})


def test_completion_conflicts_resolution_and_history(workbench, extractor):
    client, headers, _, _ = workbench
    d = draft(workbench)
    first = attach(workbench, d['id'], 'Synthetic first position')
    assert wb.frontmatter(first['document'])[0]['position'] == 'Synthetic first position'
    assert first['completion']['provenance']['position']['sources'][0]['source_id'] == first['sources'][0]['id']
    second = attach(workbench, d['id'], 'Synthetic second position')
    assert wb.frontmatter(second['document'])[0]['position'] == 'Synthetic first position'
    assert len(second['completion']['conflicts']) == 1
    prefix = '/api/drafts/' + d['id']
    resolved = client.post(prefix + '/completion/resolve', json={'field': 'position',
        'source_id': second['sources'][1]['id'], 'revision': second['revision']}, headers=headers)
    assert resolved.status_code == 200, resolved.json
    assert not resolved.json['completion']['conflicts']
    assert wb.frontmatter(resolved.json['document'])[0]['position'] == 'Synthetic second position'
    assert resolved.json['history'][-1]['fields'][0]['old_value'] == 'Synthetic first position'
    repeated = client.post(prefix + '/complete', headers=headers).json
    assert repeated['revision'] == resolved.json['revision']
    assert not repeated['completion']['conflicts']


def test_manual_edits_and_deletions_survive_reanalysis(workbench, extractor):
    client, headers, _, _ = workbench
    d = draft(workbench)
    current = attach(workbench, d['id'], 'Synthetic source value')
    prefix = '/api/drafts/' + d['id']
    fm, body = wb.frontmatter(current['document'])
    fm['position'] = ''
    document = '---\n' + yaml.safe_dump(fm) + '---\n' + body
    result = client.put(prefix, json={'document': document, 'revision': current['revision']}, headers=headers).json
    assert wb.frontmatter(result['document'])[0]['position'] == ''
    assert result['completion']['conflicts'][0]['current'] == ''
    kept = client.post(prefix + '/completion/resolve', json={'field': 'position', 'keep_current': True,
        'revision': result['revision']}, headers=headers).json
    assert not kept['completion']['conflicts']
    assert wb.frontmatter(client.post(prefix + '/complete', headers=headers).json['document'])[0]['position'] == ''
    stale = client.put(prefix, json={'document': document, 'revision': current['revision']}, headers=headers)
    assert stale.status_code == 409


def test_removed_source_and_changed_context_are_reported(workbench, extractor):
    client, headers, _, _ = workbench
    d = draft(workbench)
    current = attach(workbench, d['id'], 'Synthetic source value')
    prefix = '/api/drafts/' + d['id']
    result = client.delete(prefix + '/sources/' + current['sources'][0]['id'], headers=headers).json
    assert result['completion']['stale_fields'] == ['position']
    assert wb.frontmatter(result['document'])[0]['position'] == 'Synthetic source value'


@pytest.mark.parametrize('modality', list(wb.CATEGORIES))
def test_modality_schema_and_summary(workbench, monkeypatch, modality):
    field = next(iter(wb.STRUCTURES[modality]))
    value = {'fixture': 'Synthetic setting'}
    monkeypatch.setattr(completion, 'extract_parameters_by_modality',
        lambda text, mod, title: {field: value, 'author': 'Untrusted author', 'unknown_setting': 'unrecognized'})
    d = draft(workbench, modality)
    result = attach(workbench, d['id'], 'Synthetic source text')
    fm, body = wb.frontmatter(result['document'])
    assert fm[field] == value
    assert not fm['author']
    assert 'unknown_setting' not in fm
    assert 'Synthetic setting' in body


def test_manual_prose_is_preserved(workbench, extractor):
    client, headers, _, _ = workbench
    d = draft(workbench)
    prefix = '/api/drafts/' + d['id']
    fm, _ = wb.frontmatter(d['document'])
    custom = '---\n' + yaml.safe_dump(fm) + '---\n\n**Poziție:** Authored prose\n'
    assert client.put(prefix, json={'document': custom}, headers=headers).status_code == 200
    result = attach(workbench, d['id'], 'Synthetic new position')
    assert '**Poziție:** Authored prose' in result['document']


def item(caption, url='https://example.org/image.jpg'):
    return {'caption': caption, 'url': url, 'source_url': 'https://example.org/source', 'author': 'Fixture', 'license': 'CC0'}


def test_image_ranking_translation_deduplication_and_modality():
    ranked = rank_images([item('CT chest scanner', 'https://example.org/machine.jpg'),
        item('Chest CT axial'), item('Chest CT axial duplicate'),
        item('Chest radiograph', 'https://example.org/rx.jpg'),
        item('Butterfly', 'https://example.org/unrelated.jpg')], 'CT torace', 'ct')
    assert ranked[0]['caption'] == 'Chest CT axial'
    assert len(ranked) == 3
    assert 'Modalitate compatibilă' in ranked[0]['relevance']


def test_image_provider_failure_keeps_other_results():
    def remote(url, params):
        assert 'chest' in str(params)
        if 'wikimedia' in url:
            raise ValueError('Synthetic unavailable provider')
        return {'list': [{'title': 'Chest CT axial', 'imgLarge': '/imgs/ct.jpg',
            'pmcid': '1234', 'authors': 'Fixture'}]}
    result = search_images(remote, lambda x: x, 'torace', 'ct')
    assert len(result['results']) == 1
    assert result['providers'][0]['error']
    assert result['providers'][1]['count'] == 1
    assert result['query'] == 'chest ct'
    assert result['results'][0]['license'] == ''
    assert result['results'][0]['source_url'] == 'https://pmc.ncbi.nlm.nih.gov/articles/PMC1234/'


def test_library_detects_existing_file_edits(tmp_path):
    target = tmp_path / 'docs' / 'ct' / 'chest' / 'fixture.md'
    target.parent.mkdir(parents=True)
    target.write_text('---\nslug: fixture\ntitle: Before\n---\nBody', encoding='utf-8')
    assert wb.library(tmp_path)[0]['fm']['title'] == 'Before'
    target.write_text('---\nslug: fixture\ntitle: Changed after opening\n---\nBody', encoding='utf-8')
    assert wb.library(tmp_path)[0]['fm']['title'] == 'Changed after opening'


def test_frontend_javascript_syntax(workbench, tmp_path):
    node = shutil.which('node')
    if not node:
        pytest.skip('Node is not available')
    html = workbench[0].get('/').get_data(as_text=True)
    scripts = re.findall(r'<script(?:\s[^>]*)?>(.*?)</script>', html, re.S)
    path = tmp_path / 'workbench.js'
    path.write_text('\n'.join(scripts), encoding='utf-8')
    result = subprocess.run([node, '--check', str(path)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr


def test_autosave_keeps_edits_made_during_request(workbench, tmp_path):
    node = shutil.which('node')
    if not node:
        pytest.skip('Node is not available')
    html = workbench[0].get('/').get_data(as_text=True)
    persist = html.split('async function persist(', 1)[1].split('async function changeAttachment', 1)[0]
    script = """
const assert = require('node:assert/strict');
let active = {id: 'fixture', revision: 1}, dirty = true, saveInFlight = null;
const editor = {value: 'first edit'};
const $ = () => editor;
const updateAutoSaveStatus = () => {}, message = () => {}, renderCompletion = () => {}, renderPreview = () => {};
const pending = [], sent = [];
function api(path, method, data) { sent.push(data); return new Promise(resolve => pending.push(resolve)); }
""" + 'async function persist(' + persist + """
(async () => {
  const saving = persist();
  editor.value = 'second edit';
  pending.shift()({id: 'fixture', revision: 2, document: 'first edit'});
  await new Promise(resolve => setImmediate(resolve));
  assert.equal(sent.length, 2);
  assert.equal(sent[1].document, 'second edit');
  assert.equal(sent[1].revision, 2);
  pending.shift()({id: 'fixture', revision: 3, document: 'second edit'});
  await saving;
  assert.equal(editor.value, 'second edit');
  assert.equal(active.revision, 3);
  assert.equal(dirty, false);
})().catch(error => { console.error(error); process.exitCode = 1; });
"""
    path = tmp_path / 'autosave.js'
    path.write_text(script, encoding='utf-8')
    result = subprocess.run([node, str(path)], capture_output=True, text=True, timeout=10)
    assert result.returncode == 0, result.stderr


def test_imported_draft_ui_requires_revision(workbench, tmp_path):
    node = shutil.which('node')
    if not node:
        pytest.skip('Node is not available')
    html = workbench[0].get('/').get_data(as_text=True)
    editing = html.split('function updateEditingState()', 1)[1].split('function setActive', 1)[0]
    attachment = html.split('async function changeAttachment(', 1)[1].split('function renderCompletion', 1)[0]
    revision = html.split("on('reviseImported', async () => {", 1)[1].split("\non('import'", 1)[0]
    script = """
const assert = require('node:assert/strict');
let active = {id: 'old', status: 'imported', imported_path: 'docs/rx/fixture.md'};
const elements = new Map();
const $ = id => {
  if (!elements.has(id)) elements.set(id, {classList: {toggle(name, value) { this.hidden = value; }}});
  return elements.get(id);
};
const buttons = [{}, {}];
const document = {querySelectorAll: () => buttons};
let calls = [];
async function api(path, method, data) {
  calls.push({path, method, data});
  return {id: 'new', status: 'draft', document: 'Synthetic revision'};
}
const setActive = d => {active = d; updateEditingState();};
const refresh = async () => {}, message = () => {};
""" + 'function updateEditingState()' + editing + 'async function changeAttachment(' + attachment + """
async function revise() {
""" + revision.rsplit('});', 1)[0] + """
}
(async () => {
  updateEditingState();
  assert.equal($('importedNotice').classList.hidden, false);
  assert.equal($('document').readOnly, true);
  assert.equal($('btnAttachFromCatalog').disabled, true);
  assert.ok(buttons.every(b => b.disabled));
  await assert.rejects(changeAttachment('/sources/attach-local', 'POST', {}), /revizuire/);
  await assert.rejects(changeAttachment('/sources/source-id/smart-extract', 'POST', {}), /revizuire/);
  assert.equal(calls.length, 0);
  await revise();
  assert.deepEqual(calls, [{path: '/api/drafts/from-library', method: 'POST', data: {path: 'docs/rx/fixture.md', mode: 'revision'}}]);
  assert.equal(active.id, 'new');
  assert.equal($('importedNotice').classList.hidden, true);
  assert.equal($('document').readOnly, false);
  assert.equal($('btnAttachFromCatalog').disabled, false);
  assert.ok(buttons.every(b => !b.disabled));
})().catch(error => { console.error(error); process.exitCode = 1; });
"""
    path = tmp_path / 'imported-draft.js'
    path.write_text(script, encoding='utf-8')
    result = subprocess.run([node, str(path)], capture_output=True, text=True, timeout=10)
    assert result.returncode == 0, result.stderr


def test_online_recheck_updates_owned_field_and_preserves_source_id(workbench, monkeypatch, extractor):
    client, headers, _, _ = workbench
    d = draft(workbench)
    prefix = '/api/drafts/' + d['id']
    def response(value):
        return (value + '\n' + 'Synthetic evidence. ' * 10).encode(), 'text/plain', 'https://example.org/source'
    monkeypatch.setattr(wb, 'fetch', lambda url: response('First fixture'))
    first = client.post(prefix + '/sources', json={'url': 'https://example.org/source'}, headers=headers).json
    monkeypatch.setattr(wb, 'fetch', lambda url: response('Second fixture'))
    second = client.post(prefix + '/sources', json={'url': 'https://example.org/source'}, headers=headers).json
    assert wb.frontmatter(second['document'])[0]['position'] == 'Second fixture'
    assert first['sources'][0]['id'] == second['sources'][0]['id']
    assert first['sources'][0]['sha256'] != second['sources'][0]['sha256']
    assert not second['completion']['stale_fields']
    stale_headers = {**headers, 'X-Workbench-Revision': str(first['revision'])}
    assert client.post(prefix + '/complete', headers=stale_headers).status_code == 409


def test_revision_detects_original_changed_outside_workbench(workbench):
    client, headers, repo, _ = workbench
    target = repo / 'docs' / 'ct' / 'abdomen' / 'fixture.md'
    target.parent.mkdir(parents=True)
    target.write_text(wb.seed('ct', 'Fixture'), encoding='utf-8')
    current = client.post('/api/drafts/from-library', json={'path': target.relative_to(repo).as_posix()}, headers=headers).json
    target.write_text(target.read_text(encoding='utf-8') + '\nChanged elsewhere\n', encoding='utf-8')
    report = client.post('/api/drafts/' + current['id'] + '/validate', headers=headers).json
    assert any('original a fost modificat' in e for e in report['errors'])
