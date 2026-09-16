"""OAuth CLI adapters: no credentials or external services used in tests."""
import json
import os
from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import cli_ai as cli
import field_ai
from admin import app


def events(*items):
    return '\n'.join(json.dumps(item) for item in items)


def test_codex_events_require_completed_turn():
    raw = events({'type': 'item.completed', 'item': {'type': 'web_search', 'query': 'fixture'}},
                 {'type': 'item.completed', 'item': {'type': 'agent_message', 'text': 'OK'}},
                 {'type': 'turn.completed'})
    assert cli.parse_events(raw, 'codex')[:2] == ('OK', True)
    with pytest.raises(ValueError):
        cli.parse_events(events({'type': 'turn.failed'}), 'codex')


def test_gemini_joins_stream_deltas_and_checks_actual_search_success():
    raw = events({'type': 'tool_use', 'tool_id': '1', 'tool_name': 'google_web_search'},
                 {'type': 'tool_result', 'tool_id': '1', 'status': 'success'},
                 {'type': 'message', 'role': 'assistant', 'content': '{"sta', 'delta': True},
                 {'type': 'message', 'role': 'assistant', 'content': 'tus":"supported"}', 'delta': True},
                 {'type': 'result', 'status': 'success'})
    text, searched, _ = cli.parse_events(raw, 'gemini')
    assert json.loads(text)['status'] == 'supported'
    assert searched is True
    assert cli.parse_events(raw.replace('"tool_id": "1", "status": "success"', '"tool_id": "1", "status": "error"'), 'gemini')[1] is False


def test_agy_events_parse_cleanly():
    raw_success = json.dumps({'status': 'SUCCESS', 'response': 'OK'})
    text, searched, model = cli.parse_events(raw_success, 'agy')
    assert text == 'OK'
    assert searched is True
    assert 'Antigravity' in model

    raw_stream = json.dumps({'event': 'result', 'result': {'status': 'SUCCESS', 'response': 'Stream OK'}})
    text, searched, model = cli.parse_events(raw_stream, 'agy')
    assert text == 'Stream OK'
    assert searched is True

    with pytest.raises(ValueError, match='Antigravity CLI nu a putut finaliza cererea'):
        cli.parse_events(json.dumps({'status': 'ERROR', 'error': 'Rate limited'}), 'agy')


def test_oauth_environment_never_falls_back_to_api_keys(monkeypatch):
    for key in cli.KEY_ENV:
        monkeypatch.setenv(key, 'secret-fixture')
    env = cli.oauth_environment()
    assert all(key not in env for key in cli.KEY_ENV)
    assert env.get('PATH') == os.environ.get('PATH')


@pytest.mark.parametrize('provider,backend', [('codex_oauth', None), ('gemini_oauth', 'gemini'), ('gemini_oauth', 'agy')])
def test_cli_run_uses_stdin_and_restricts_tools(monkeypatch, provider, backend):
    if backend:
        monkeypatch.setenv('FIELD_AI_GEMINI_CLI_BACKEND', backend)
    monkeypatch.setattr(cli, 'cli_command', lambda name: [name + '.exe'])
    def process(command, prompt, directory, env):
        assert prompt == 'Sensitive fixture stays on stdin'
        assert prompt not in command
        assert Path(directory).name.startswith('radiology-ai-')
        if provider == 'codex_oauth':
            assert '--sandbox' in command and 'read-only' in command
            assert '--ignore-user-config' in command
            assert 'forced_login_method="chatgpt"' in command
            assert 'features.shell_tool=false' in command
            return events({'type': 'item.completed', 'item': {'type': 'agent_message', 'text': 'OK'}}, {'type': 'turn.completed'})
        if backend == 'agy':
            assert '--input-format' in command and 'text' in command
            assert '--output-format' in command and 'json' in command
            assert '--dangerously-skip-permissions' in command
            return json.dumps({'status': 'SUCCESS', 'response': 'OK'})
        settings = json.loads(Path(env['GEMINI_CLI_SYSTEM_SETTINGS_PATH']).read_text())
        assert settings['security']['auth']['enforcedType'] == 'oauth-personal'
        assert settings['advanced']['ignoreLocalEnv'] is True
        assert settings['tools']['core'] == ['google_web_search', 'web_fetch']
        assert settings['hooksConfig']['enabled'] is False
        return events({'type': 'message', 'role': 'assistant', 'content': 'OK'}, {'type': 'result', 'status': 'success'})
    monkeypatch.setattr(cli, 'run_process', process)
    assert cli.run_cli(provider, 'Sensitive fixture stays on stdin')[0] == 'OK'


def test_cli_source_requires_literal_evidence(monkeypatch):
    from protocol_workbench import app as wb
    content = 'This is synthetic evidence for a software test only.'
    calls = []
    def fetch(url):
        calls.append(url)
        return ('<html><p>' + content + '</p></html>').encode(), 'text/html', url
    monkeypatch.setattr(wb, 'fetch', fetch)
    source = {'url': 'https://acr.org/fixture', 'title': 'Fixture', 'evidence': content}
    assert cli.verify_evidence(source)['evidence'] == content
    assert cli.verify_evidence({**source, 'evidence': 'These other words were never in that document.'}) is None
    assert cli.verify_evidence({**source, 'url': 'https://acr.org.attacker.test/x'}) is None
    assert len(calls) == 2


def test_no_search_event_cannot_produce_verified_sources(monkeypatch):
    result = {'status': 'supported', 'suggestion': 'Fixture', 'explanation': 'Fixture', 'limitations': [],
              'sources': [{'url': 'https://acr.org/fixture', 'evidence': 'A fabricated piece of evidence for testing only.'}]}
    monkeypatch.setattr(cli, 'run_cli', lambda *args: (json.dumps(result), False, 'fixture'))
    def verify(source):
        raise AssertionError('No search was made')
    monkeypatch.setattr(cli, 'verify_evidence', verify)
    assert cli.call_cli_research({}, 'codex_oauth', 'Policy')[1] == []


def test_cli_endpoints_local_origin_and_enum_only(monkeypatch):
    client = app.test_client()
    monkeypatch.setattr(cli, 'connect_interactively', lambda provider: None)
    monkeypatch.setattr(cli, 'run_cli', lambda *args, **kwargs: ('OK', False, 'fixture'))
    assert client.post('/api/ai/cli-check', json={'provider': 'codex_oauth'}).status_code == 200
    assert client.post('/api/ai/cli-check', json={'provider': 'openai'}).status_code == 400
    assert client.post('/api/ai/cli-connect', json={'provider': 'codex_oauth'}, headers={'Origin': 'https://attacker.test'}).status_code == 403
    assert client.post('/api/ai/cli-connect', json={'provider': 'codex_oauth'}, environ_overrides={'REMOTE_ADDR': '192.0.2.1'}).status_code == 403
    assert client.post('/api/ai/cli-connect', json={'provider': 'codex_oauth'}).status_code == 200


def test_automatic_provider_uses_oauth_even_when_api_key_exists(monkeypatch):
    monkeypatch.setenv('GEMINI_API_KEY', 'old-api-key')
    monkeypatch.setattr(field_ai.shutil, 'which', lambda name: '/fixture/codex')
    selected = []
    def research(context, provider):
        selected.append(provider)
        return {'status': 'insufficient', 'suggestion': ''}
    monkeypatch.setattr(field_ai, 'research_field', research)
    response = app.test_client().post('/api/ai/field-research', json={
        'provider': 'auto', 'field': {'name': 'position', 'label': 'Position'},
        'protocol': {'title': 'Fixture', 'modality': 'rx'}})
    assert response.status_code == 200
    assert selected == ['codex_oauth']


def test_process_failure_does_not_expose_auth_output(monkeypatch):
    class Process:
        returncode = 1
        def communicate(self, prompt, timeout):
            return '', 'secret-token-and-auth-url'
    monkeypatch.setattr(cli.subprocess, 'Popen', lambda *a, **k: Process())
    with pytest.raises(ValueError) as exc:
        cli.run_process(['fixture'], 'test', '.', {})
    assert 'secret-token' not in str(exc.value)


def test_google_unsupported_client_is_actionable_without_exposing_output(monkeypatch):
    class Process:
        returncode = 55
        def communicate(self, prompt, timeout):
            return '', 'UNSUPPORTED_CLIENT secret-token'
    monkeypatch.setattr(cli.subprocess, 'Popen', lambda *a, **k: Process())
    response = app.test_client().post('/api/ai/cli-check', json={'provider': 'gemini_oauth'})
    assert response.status_code == 422
    assert 'UNSUPPORTED_CLIENT' in response.json['error']
    assert 'secret-token' not in response.json['error']
