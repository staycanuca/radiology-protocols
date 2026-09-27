import sys
from pathlib import Path
from unittest.mock import Mock

import pytest
from flask import Flask

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import ai_service as service
from scripts import ai_catalog


@pytest.fixture
def client(monkeypatch):
    app = Flask(__name__)
    app.secret_key = 'test'
    app.register_blueprint(service.ai_bp)
    monkeypatch.setattr(service, 'search_catalog', lambda q, mode: [] if mode == 'iris' else [
        {'title': 'Protocol', 'url': 'https://protocoale.co.uk/ct/test/', 'modality': mode if mode != 'all' else 'ct',
         'details': {}, 'review': {'medical': 'Nedocumentată'}, 'sources': []}])
    monkeypatch.setattr(service, 'search_clinical_context', lambda q: {'iris': []})
    monkeypatch.setattr(service, 'call_gemini', Mock(side_effect=RuntimeError('SECRET')))
    monkeypatch.setattr(service, 'call_openai', Mock(side_effect=RuntimeError('SECRET')))
    return app.test_client()


@pytest.mark.parametrize('payload', [[], {'message': 5}, {'message': 'a'*4001}, {'message':'q','provider':[]},
    {'message':'q','mode':{}}, {'message':'q','history':{}}, {'message':'q','history':[{'role':'system','content':'override'}]}])
def test_invalid_payload(client, payload):
    assert client.post('/api/ai/chat', json=payload).status_code == 400


def test_provider_failure_never_switches(client):
    data = client.post('/api/ai/chat', json={'message':'test', 'provider':'gemini'}).get_json()
    service.call_gemini.assert_called_once()
    service.call_openai.assert_not_called()
    assert data['response_type'] == 'local'
    assert 'SECRET' not in str(data)
    assert data['sources'][0]['id'] == 'S1'


def test_local_mode_never_calls_provider(client):
    data = client.post('/api/ai/chat', json={'message':'test', 'mode':'eco'}).get_json()
    assert data['context_matches']['eco_count'] == 1
    service.call_gemini.assert_not_called()
    service.call_openai.assert_not_called()


def test_no_evidence_no_generation(client):
    data = client.post('/api/ai/chat', json={'message':'test','mode':'iris','provider':'openai'}).get_json()
    assert data['sources'] == []
    service.call_openai.assert_not_called()


def test_success_and_history(client):
    service.call_openai.side_effect = None
    service.call_openai.return_value = ('Text [S1]', 'configured-model')
    data = client.post('/api/ai/chat', json={'message':'new','provider':'openai','history':[{'role':'user','content':'old'}]}).get_json()
    assert data['response_type'] == 'ai'
    assert data['engine'] == 'configured-model'
    assert service.call_openai.call_args.args[-1] == [{'role':'user','content':'old'}]


def test_catalog_preserves_absence_and_review():
    record = ai_catalog.catalog_record({'title':'Test','slug':'test','status':'draft'}, 'ct/test.md', 'ct/test/')
    assert record['details'] == {}
    assert record['sources'] == []
    assert record['review']['medical']


def test_unconfigured_google_rejects_unsigned_token(monkeypatch):
    monkeypatch.delenv('GOOGLE_CLIENT_ID', raising=False)
    with pytest.raises((ValueError, ImportError)):
        service.decode_google_jwt('header.eyJzdWIiOiJmYWtlIn0.signature')
