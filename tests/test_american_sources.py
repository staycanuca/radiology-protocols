"""American catalog search behavior with offline HTML fixtures."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from protocol_workbench.american_sources import AmericanSearch, CATALOGS, parse_catalog, provenance
from protocol_workbench.app import create_app


def html(*links):
    return ('<html>' + ''.join('<a href="' + url + '">' + title + '</a>' for url, title in links) + '</html>').encode()


def test_catalog_resolves_relative_links_and_rejects_offsite_and_navigation():
    raw = html(('assets/Knee.pdf', 'Knee <strong>Routine</strong>'),
               ('assets/Knee.pdf#page=2', 'duplicate'), ('/careers/', 'Knee job'),
               ('https://utsouthwestern.edu.attacker.test/protocols/assets/Knee.pdf', 'bad'),
               ('javascript:alert(1)', 'bad'))
    entries = parse_catalog(raw, CATALOGS[0]['pages']['irm'], CATALOGS[0])
    assert len(entries) == 1
    assert entries[0]['title'] == 'Knee Routine'
    assert entries[0]['url'].endswith('/protocols/assets/Knee.pdf')
    assert entries[0]['country'] == 'US'


def test_romanian_aliases_cache_and_modality_filter():
    calls = []
    def fetch(url):
        calls.append(url)
        return html(('assets/Knee.pdf', 'Knee Routine'), ('assets/Head.pdf', 'Head')), 'text/html', url
    search = AmericanSearch(fetch)
    result = search.search('IRM genunchi', 'irm', 'utsw')
    assert len(result['results']) == 1
    assert result['results'][0]['title'] == 'Knee Routine'
    assert result['results'][0]['catalog_checked_at']
    assert search.search('knee', 'irm', 'utsw')['total'] == 1
    assert len(calls) == 1
    assert search.search('knee', 'rx', 'ohsu')['catalogs'] == []


def test_one_unavailable_catalog_preserves_other_results():
    def fetch(url):
        if 'ohsu' in url:
            raise OSError('Source unavailable')
        return html(('assets/Knee.pdf', 'Knee')), 'text/html', url
    result = AmericanSearch(fetch).search('knee', 'irm')
    assert result['total'] == 1
    assert len(result['catalogs']) == 2
    assert not result['catalogs'][1]['ok']
    assert result['catalogs'][1]['error'] == 'Source unavailable'
    assert len(result['portals']) == 2


def test_changed_catalog_is_distinct_from_zero_search_matches():
    broken = AmericanSearch(lambda url: (b'<html>Login required</html>', 'text/html', url))
    assert not broken.search('knee', 'irm', 'utsw')['catalogs'][0]['ok']
    healthy = AmericanSearch(lambda url: (html(('assets/Head.pdf', 'Head')), 'text/html', url))
    result = healthy.search('knee', 'irm', 'utsw')
    assert result['catalogs'][0]['ok']
    assert result['total'] == 0


def test_provenance_requires_actual_institutional_hostname():
    assert provenance('https://radiology.utsouthwestern.edu/file.pdf')['institution'] == 'UT Southwestern'
    assert provenance('https://acsearch.acr.org/topic')['institution'] == 'ACR'
    assert provenance('https://doi.org/10.1002/test') == {}
    assert provenance('https://acr.org.attacker.test/test') == {}


def test_unknown_institution_rejected():
    with pytest.raises(ValueError):
        AmericanSearch(lambda url: None).search('knee', 'irm', 'unknown')


def test_search_api_and_existing_provider(tmp_path, monkeypatch):
    from protocol_workbench import app as wb
    client = create_app(tmp_path, tmp_path / 'state').test_client()
    monkeypatch.setattr(wb, 'fetch', lambda url: (html(('assets/Knee.pdf', 'Knee')), 'text/html', url))
    response = client.get('/api/search?provider=us&institution=utsw&modality=irm&q=genunchi')
    assert response.status_code == 200
    assert response.json['total'] == 1
    assert client.get('/api/search?provider=unknown&modality=irm&q=knee').status_code == 400
    monkeypatch.setattr(wb, 'remote_json', lambda *a: {'resultList': {'result': [
        {'title': 'Test publication', 'source': 'MED', 'id': '1'}]}})
    response = client.get('/api/search?provider=europepmc&modality=irm&q=knee')
    assert response.status_code == 200
    assert response.json['results'][0]['title'] == 'Test publication'
