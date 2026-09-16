"""Synthetic field research: grounding, refusal, context and editor integration."""
import json
import sys
from pathlib import Path

import pytest
import requests

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import field_ai as ai
from admin import app


@pytest.fixture
def context():
    return {'protocol': {'title': 'Synthetic RX fixture', 'modality': 'rx', 'category': 'torace'},
            'field': {'name': 'position', 'label': 'Poziționare', 'value': 'Before', 'options': []},
            'context': [{'name': 'projection', 'value': 'Synthetic projection'}], 'provider': 'gemini'}


@pytest.fixture
def answer():
    return {'status': 'supported', 'suggestion': 'Synthetic software value',
            'explanation': 'Synthetic evidence explanation', 'limitations': ['Verify local context']}


@pytest.fixture
def client(monkeypatch):
    monkeypatch.setenv('GEMINI_API_KEY', 'synthetic-test-key')
    def unexpected(*args, **kwargs):
        raise AssertionError('Tests must not contact external providers')
    monkeypatch.setattr(ai.requests, 'post', unexpected)
    monkeypatch.setattr(ai.requests, 'get', unexpected)
    return app.test_client()


def test_grounded_result_preserves_context_and_requires_review(client, monkeypatch, context, answer):
    def call(data, provider):
        assert data['protocol'] == context['protocol']
        assert data['field'] == context['field']
        assert data['context'] == context['context']
        assert provider == 'gemini'
        return json.dumps(answer), [{'url': 'https://www.acr.org/fixture', 'title': 'Fixture'}], 'fixture-model', ''
    monkeypatch.setattr(ai, 'call_research', call)
    result = client.post('/api/ai/field-research', json=context)
    assert result.status_code == 200
    assert result.json['suggestion'] == answer['suggestion']
    assert result.json['review_required'] is True
    assert result.json['sources'][0]['url'] == 'https://www.acr.org/fixture'


@pytest.mark.parametrize('url', [None, 'javascript:alert(1)', 'https://acr.org.attacker.test/a', 'http://acr.org/a', 'https://user@acr.org/a', 'https://acr.org:bad/a'])
def test_unverified_sources_cannot_enable_application(client, monkeypatch, context, answer, url):
    monkeypatch.setattr(ai, 'call_research', lambda *args: (json.dumps(answer), [{'url': url}], 'fixture', ''))
    # Invalid URLs must never be visited, even when present in provider output.
    result = client.post('/api/ai/field-research', json=context)
    assert result.status_code == 200
    assert result.json['status'] == 'insufficient'
    assert result.json['suggestion'] == ''


def test_no_grounding_and_insufficient_status_block_suggestion(client, monkeypatch, context, answer):
    monkeypatch.setattr(ai, 'call_research', lambda *args: (json.dumps(answer), [], 'fixture', ''))
    assert client.post('/api/ai/field-research', json=context).json['suggestion'] == ''
    answer['status'] = 'insufficient'
    monkeypatch.setattr(ai, 'call_research', lambda *args: (json.dumps(answer), [{'url': 'https://acr.org/fixture'}], 'fixture', ''))
    assert client.post('/api/ai/field-research', json=context).json['suggestion'] == ''


def test_safety_field_needs_professional_source(client, monkeypatch, context, answer):
    context['field']['name'] = 'contrast_volume'
    monkeypatch.setattr(ai, 'call_research', lambda *args: (json.dumps(answer), [{'url': 'https://radiography101.org/fixture'}], 'fixture', ''))
    result = client.post('/api/ai/field-research', json=context).json
    assert result['status'] == 'insufficient'
    assert result['suggestion'] == ''


def test_invalid_option_not_applied(client, monkeypatch, context, answer):
    context['field']['options'] = [{'value': 'allowed'}]
    monkeypatch.setattr(ai, 'call_research', lambda *args: (json.dumps(answer), [{'url': 'https://acr.org/fixture'}], 'fixture', ''))
    assert client.post('/api/ai/field-research', json=context).json['suggestion'] == ''


def test_google_source_redirect_only_visits_google(client, monkeypatch):
    visits = []
    class Response:
        status_code = 302
        headers = {'Location': 'https://acr.org/fixture'}
        def __enter__(self): return self
        def __exit__(self, *args): pass
    def get(url, **kwargs):
        visits.append(url)
        assert kwargs['allow_redirects'] is False
        return Response()
    monkeypatch.setattr(ai.requests, 'get', get)
    source = {'url': 'https://vertexaisearch.cloud.google.com/grounding-api-redirect/fixture', 'title': 'Fixture'}
    assert ai.resolve_source(source)['url'] == 'https://acr.org/fixture'
    assert visits == [source['url']]
    Response.headers = {'Location': 'http://127.0.0.1/private'}
    assert ai.resolve_source(source) is None


@pytest.mark.parametrize('text', ['not JSON', '[]', '{"status":"supported"}', '{"status":"supported","suggestion":3,"explanation":"test","limitations":[]}'])
def test_malformed_model_response_is_not_applied(client, monkeypatch, context, text):
    monkeypatch.setattr(ai, 'call_research', lambda *args: (text, [], 'fixture', ''))
    result = client.post('/api/ai/field-research', json=context)
    assert result.status_code == 422
    assert 'error' in result.json


def test_local_fields_do_not_call_ai(client, context):
    for name in ['author', 'last_updated', 'slug', 'url', 'caption']:
        context['field']['name'] = name
        result = client.post('/api/ai/field-research', json=context)
        assert result.status_code == 200
        assert result.json['status'] == 'insufficient'


def test_bad_context_and_provider_fail_cleanly(client, context):
    assert client.post('/api/ai/field-research', json=[]).status_code == 400
    assert client.post('/api/ai/field-research', json={}).status_code == 400
    assert client.post('/api/ai/field-research', json={**context, 'provider': 'unknown'}).status_code == 400
    context['field']['options'] = [None]
    assert client.post('/api/ai/field-research', json=context).status_code == 400


def test_missing_key_and_network_error_do_not_fallback(client, monkeypatch, context):
    monkeypatch.delenv('GEMINI_API_KEY', raising=False)
    monkeypatch.delenv('GOOGLE_API_KEY', raising=False)
    assert client.post('/api/ai/field-research', json=context).status_code == 422
    def fail(*args):
        raise requests.ConnectionError('secret-provider-response')
    monkeypatch.setattr(ai, 'call_research', fail)
    result = client.post('/api/ai/field-research', json=context)
    assert result.status_code == 503
    assert 'secret-provider-response' not in result.get_data(as_text=True)


def test_gemini_uses_search_metadata_not_invented_citations(client, monkeypatch, context, answer):
    class Response:
        def raise_for_status(self): pass
        def json(self):
            return {'candidates': [{'finishReason': 'STOP', 'content': {'parts': [{'text': json.dumps(answer)}]},
                'groundingMetadata': {'webSearchQueries': ['fixture'],
                    'groundingChunks': [{'web': {'uri': 'https://acr.org/fixture', 'title': 'Fixture'}}, {'web': {'uri': 'https://acr.org/unused'}}],
                    'groundingSupports': [{'groundingChunkIndices': [0]}]}}]}
    def post(url, **kwargs):
        assert kwargs['json']['tools'] == [{'google_search': {}}]
        assert kwargs['headers']['x-goog-api-key'] == 'synthetic-test-key'
        assert 'Nu inventa' in kwargs['json']['systemInstruction']['parts'][0]['text']
        return Response()
    monkeypatch.setattr(ai.requests, 'post', post)
    result = client.post('/api/ai/field-research', json=context).json
    assert len(result['sources']) == 1
    assert result['status'] == 'supported'


def test_openai_requires_web_search_and_citations(client, monkeypatch, context, answer):
    monkeypatch.setenv('OPENAI_API_KEY', 'synthetic-test-key')
    context['provider'] = 'openai'
    class Response:
        def raise_for_status(self): pass
        def json(self):
            return {'status': 'completed', 'output': [{'type': 'web_search_call', 'status': 'completed'},
                {'type': 'message', 'content': [{'type': 'output_text', 'text': json.dumps(answer),
                    'annotations': [{'type': 'url_citation', 'url': 'https://acr.org/fixture', 'title': 'Fixture'}]}]}]}
    def post(url, **kwargs):
        assert kwargs['json']['tool_choice'] == 'required'
        assert kwargs['json']['store'] is False
        assert 'acr.org' in kwargs['json']['tools'][0]['filters']['allowed_domains']
        return Response()
    monkeypatch.setattr(ai.requests, 'post', post)
    assert client.post('/api/ai/field-research', json=context).json['status'] == 'supported'


def test_editor_serves_assets_for_all_modalities(client):
    for slug in ['rx-torace-pa', 'ct-abdomen-pelvis-with-contrast', 'irm-cerebral-nativ-si-cu-contrast', 'eco-abdomen-total', 'tranzit-esofagian']:
        response = client.get('/edit/' + slug)
        assert response.status_code == 200
        assert 'editor-field-ai.js' in response.get_data(as_text=True)
    assert client.get('/new').status_code == 200
    for file in ['editor-field-ai.js', 'editor-field-ai.css']:
        assert client.get('/static/' + file).status_code == 200
