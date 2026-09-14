"""Isolated workflow tests; never modify the actual clinical library."""
import io
import json
import re
import shutil
import sys
from pathlib import Path

import pytest
import yaml
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from protocol_workbench import app as wb


@pytest.fixture
def workbench(tmp_path, monkeypatch):
    repo = tmp_path / 'repo'
    (repo / 'scripts').mkdir(parents=True)
    (repo / 'docs' / 'javascripts').mkdir(parents=True)
    (repo / 'config').mkdir()
    (repo / 'config' / 'institution.yml').write_text('institution: {}', encoding='utf-8')
    for name in ('generate_comparison_index.py', 'generate_sitemap.py', 'generate_forms_index.py'):
        shutil.copyfile(Path(__file__).resolve().parents[1] / 'scripts' / name, repo / 'scripts' / name)
    application = wb.create_app(repo, tmp_path / 'state')
    client = application.test_client()
    page = client.get('/').get_data(as_text=True)
    token = json.loads(re.search(r'const TOKEN=("[^"]+")', page)[1])
    headers = {'X-Workbench-Token': token}
    monkeypatch.setattr(wb, 'public_url', lambda url: url)
    monkeypatch.setattr(wb, 'fetch', lambda url, params=None: (
        b'<html><body>' + b'Synthetic source for software testing. ' * 20 + b'</body></html>', 'text/html', url))
    return client, headers, repo, application.config['STATE']


def draft(workbench, modality='ct'):
    client, headers, _, _ = workbench
    response = client.post('/api/drafts', json={'title': 'Synthetic test ' + modality, 'modality': modality}, headers=headers)
    assert response.status_code == 200
    return response.json


def ready(workbench, modality='ct'):
    client, headers, _, _ = workbench
    d = draft(workbench, modality)
    fm, _ = wb.frontmatter(d['document'])
    fm.update(author='Software test', position='Synthetic test position', clinical_indications=['Synthetic test indication'])
    for key, shape in wb.STRUCTURES[modality].items():
        fm[key] = ['Synthetic test entry'] if shape is list else {'test': 'Synthetic value'}
        if key in ('series', 'sequences', 'standard_views', 'acquisition_steps'):
            fm[key] = [{'name': 'Synthetic test entry'}]
    document = '---\n' + yaml.safe_dump(fm) + '---\n\n# Synthetic protocol\n\n' + ('Software fixture, not clinical guidance. ' * 10)
    prefix = '/api/drafts/' + d['id']
    assert client.put(prefix, json={'document': document}, headers=headers).status_code == 200
    assert client.post(prefix + '/sources', json={'url': 'https://example.org/source', 'title': 'Test source'}, headers=headers).status_code == 200
    image = io.BytesIO()
    Image.new('RGB', (50, 50), 'white').save(image, format='PNG')
    image.seek(0)
    response = client.post(prefix + '/images', data={'file': (image, 'test.png'), 'caption': 'Synthetic illustration',
                           'author': 'Test author', 'license': 'CC0', 'source_url': 'https://example.org/image'}, headers=headers)
    assert response.status_code == 200, response.json
    return prefix


REVIEW = {'reviewer': 'Test reviewer', 'clinical_review': True, 'image_review': True, 'rights_review': True}


@pytest.mark.parametrize('modality', list(wb.CATEGORIES))
def test_import_all_modalities_with_assets_and_review(workbench, modality):
    client, headers, repo, _ = workbench
    prefix = ready(workbench, modality)
    assert client.post(prefix + '/validate', json={}, headers=headers).json['valid']
    response = client.post(prefix + '/import', json=REVIEW, headers=headers)
    assert response.status_code == 200, response.json
    assert response.json['indexed']
    forms = json.loads((repo / 'docs' / 'javascripts' / 'protocol-forms-index.json').read_text(encoding='utf-8'))
    assert any(p['modality'] == modality for p in forms)
    path = repo / response.json['path']
    fm, body = wb.frontmatter(path.read_text(encoding='utf-8'))
    assert fm['modality'] == modality
    assert fm['workbench_review']['reviewer'] == 'Test reviewer'
    assert fm['sources'][0]['sha256']
    assert 'excerpt' not in fm['sources'][0]
    assert (repo / 'docs' / fm['images'][0]['url']).exists()
    assert '../../assets/images/protocols/workbench/' in body
    before = path.read_bytes()
    assert client.post(prefix + '/import', json=REVIEW, headers=headers).status_code == 400
    assert path.read_bytes() == before


def test_review_required_and_new_draft_not_ready(workbench):
    client, headers, repo, _ = workbench
    d = draft(workbench)
    result = client.post('/api/drafts/' + d['id'] + '/validate', json={}, headers=headers).json
    assert not result['valid']
    assert len(result['errors']) >= 5
    prefix = ready(workbench)
    assert client.post(prefix + '/import', json={'reviewer': 'Test'}, headers=headers).status_code == 400
    assert not list((repo / 'docs').rglob('*.md'))


def test_csrf_and_host_restrictions(workbench):
    client, _, _, _ = workbench
    assert client.post('/api/drafts', json={'title': 'bad'}).status_code == 403
    assert client.get('/api/drafts', headers={'Host': 'attacker.example'}).status_code == 403


@pytest.mark.parametrize('slug', ['../../outside', 'CON/secret', 'a\\b', '', 'a' * 101])
def test_invalid_destination_is_blocked(workbench, slug):
    client, headers, _, _ = workbench
    prefix = ready(workbench)
    d = client.get('/api/drafts').json[0]
    fm, body = wb.frontmatter(d['document'])
    fm['slug'] = slug
    client.put(prefix, json={'document': '---\n' + yaml.safe_dump(fm) + '---\n' + body}, headers=headers)
    response = client.post(prefix + '/import', json=REVIEW, headers=headers)
    assert response.status_code == 400


def test_tampered_image_and_duplicate_are_blocked(workbench):
    client, headers, repo, state = workbench
    prefix = ready(workbench)
    d = client.get('/api/drafts').json[0]
    (state / 'images' / d['images'][0]['file']).write_bytes(b'corrupt')
    assert not client.post(prefix + '/validate', json={}, headers=headers).json['valid']
    existing = repo / 'docs' / 'ct' / 'abdomen' / 'existing.md'
    existing.parent.mkdir(parents=True)
    existing.write_text(d['document'], encoding='utf-8')
    result = client.post(prefix + '/validate', json={}, headers=headers).json
    assert any('slug' in e for e in result['errors'])


def test_partial_index_failure_is_reported_without_duplicate_import(workbench):
    client, headers, repo, _ = workbench
    prefix = ready(workbench)
    (repo / 'scripts' / 'generate_sitemap.py').write_text('raise RuntimeError("test failure")', encoding='utf-8')
    response = client.post(prefix + '/import', json=REVIEW, headers=headers)
    assert response.status_code == 200
    assert not response.json['indexed']
    assert (repo / response.json['path']).exists()
    assert client.get('/api/drafts').json[0]['status'] == 'imported'
    (repo / 'scripts' / 'generate_sitemap.py').write_text('print("ok")', encoding='utf-8')
    assert all(x['ok'] for x in client.post('/api/reindex', json={}, headers=headers).json['logs'])


def test_source_and_image_failures_are_visible(workbench, monkeypatch):
    client, headers, _, _ = workbench
    d = draft(workbench)
    prefix = '/api/drafts/' + d['id']
    monkeypatch.setattr(wb, 'fetch', lambda *args, **kwargs: (b'', 'text/html', 'https://example.org'))
    response = client.post(prefix + '/sources', json={'url': 'https://example.org'}, headers=headers)
    assert response.status_code == 400
    assert 'extrage' in response.json['error']
    response = client.post(prefix + '/images', json={'url': 'https://example.org'}, headers=headers)
    assert response.status_code == 400
    assert 'licență' in response.json['error']


def test_public_url_rejects_private_and_non_https(monkeypatch):
    monkeypatch.setattr(wb.socket, 'getaddrinfo', lambda *a, **k: [(2, 1, 6, '', ('127.0.0.1', 443))])
    for url in ('https://localhost', 'http://example.org', 'file:///etc/passwd', 'https://example.org:8000'):
        with pytest.raises(ValueError):
            wb.public_url(url)


def test_aliases_and_diacritic_search(workbench):
    client, headers, repo, _ = workbench
    for alias, actual in [('us', 'eco'), ('flouro', 'fluoro'), ('mri', 'irm')]:
        assert wb.frontmatter(draft(workbench, alias)['document'])[0]['modality'] == actual
    path = repo / 'docs' / 'rx' / 'torace' / 'test.md'
    path.parent.mkdir(parents=True)
    path.write_text(wb.seed('rx', 'Investigație toracică'), encoding='utf-8')
    assert len(client.get('/api/library?q=investigatie&modality=rx').json) == 1


def test_frontmatter_delimiters_and_malformed_modality(workbench):
    fm, body = wb.frontmatter('---\ntitle: "A --- B"\n---\nContent')
    assert fm['title'] == 'A --- B'
    assert body == 'Content'
    client, headers, _, _ = workbench
    d = draft(workbench)
    prefix = '/api/drafts/' + d['id']
    client.put(prefix, json={'document': '---\nmodality: []\n---\nBody'}, headers=headers)
    assert client.post(prefix + '/validate', json={}, headers=headers).status_code == 400


def test_unquoted_yaml_date_is_compatible_with_indices(workbench):
    client, headers, _, _ = workbench
    prefix = ready(workbench)
    d = client.get('/api/drafts').json[0]
    document = re.sub(r"last_updated: '[^']+'", 'last_updated: 2026-01-01', d['document'])
    client.put(prefix, json={'document': document}, headers=headers)
    result = client.post(prefix + '/import', json=REVIEW, headers=headers)
    assert result.status_code == 200
    assert result.json['indexed']


def test_proxy_failure_has_actionable_message_without_bypass(monkeypatch):
    calls = []
    def blocked(url, params=None):
        calls.append(url)
        raise wb.requests.exceptions.ProxyError('proxy refused connection')
    monkeypatch.setattr(wb, '_fetch', blocked)
    with pytest.raises(ValueError, match='proxy-ul cu care a pornit serverul'):
        wb.fetch('https://example.org')
    assert calls == ['https://example.org']


def test_delete_draft_and_manual_excerpt_fallback(workbench, monkeypatch):
    client, headers, _, state = workbench
    d = draft(workbench)
    draft_id = d['id']
    assert (state / f'{draft_id}.json').exists()

    # Test manual excerpt fallback when PDF has empty/short text
    monkeypatch.setattr(wb, 'fetch', lambda *args, **kwargs: (b'%PDF-dummy', 'application/pdf', 'https://example.org/doc.pdf'))
    # Without manual excerpt, should fail
    res = client.post(f'/api/drafts/{draft_id}/sources', json={'url': 'https://example.org/doc.pdf'}, headers=headers)
    assert res.status_code == 400

    # With manual excerpt >= 50 chars, should succeed
    long_manual = 'Aceasta este o descriere manuala a sursei scanate pentru a asigura documentarea clinica adecvata.'
    res = client.post(f'/api/drafts/{draft_id}/sources', json={'url': 'https://example.org/doc.pdf', 'manual_excerpt': long_manual}, headers=headers)
    assert res.status_code == 200
    assert len(res.json['sources']) == 1
    assert '[Extras manual / PDF scanat]' in res.json['sources'][0]['excerpt']

    # Test DELETE draft
    del_res = client.delete(f'/api/drafts/{draft_id}', headers=headers)
    assert del_res.status_code == 200
    assert not (state / f'{draft_id}.json').exists()

    # Deleting nonexistent draft should 404
    assert client.delete(f'/api/drafts/{draft_id}', headers=headers).status_code == 404


def test_load_protocol_from_library_and_bulk_import(workbench):
    client, headers, repo, _ = workbench
    # Create an existing protocol in the repo
    proto_dir = repo / 'docs' / 'rx' / 'torace'
    proto_dir.mkdir(parents=True, exist_ok=True)
    proto_file = proto_dir / 'radiografie-pulmonara-pa.md'
    proto_content = wb.seed('rx', 'Radiografie Pulmonară PA')
    proto_file.write_text(proto_content, encoding='utf-8')

    # Test single import in revision mode
    rel_path = 'docs/rx/torace/radiografie-pulmonara-pa.md'
    res = client.post('/api/drafts/from-library', json={'path': rel_path, 'mode': 'revision'}, headers=headers)
    assert res.status_code == 200
    draft_rev = res.json
    assert draft_rev['is_revision'] is True
    assert draft_rev['origin_path'] == rel_path
    assert 'Radiografie Pulmonară PA' in draft_rev['document']

    # Test single import in clone mode
    res_clone = client.post('/api/drafts/from-library', json={'path': rel_path, 'mode': 'clone'}, headers=headers)
    assert res_clone.status_code == 200
    draft_clone = res_clone.json
    assert draft_clone['is_revision'] is False
    assert draft_clone['origin_path'] is None
    assert '-adaptat' in draft_clone['document']

    # Test bulk import
    bulk_res = client.post('/api/drafts/import-bulk', json={'modality': 'rx'}, headers=headers)
    assert bulk_res.status_code == 200


def test_upload_local_text_and_docx_sources(workbench):
    client, headers, repo, state = workbench
    d = draft(workbench, 'ct')
    prefix = '/api/drafts/' + d['id']

    # 1. Upload a plain text local source
    txt_content = b"Protocol clinic intern de examinare CT Torace pentru Spitalul Clinic de Urgenta. Parametri tehnici: 120 kV, mod automat AEC."
    res_txt = client.post(
        prefix + '/sources/upload',
        data={
            'file': (io.BytesIO(txt_content), 'protocol_spital.txt'),
            'title': 'Protocol Intern Spital Clinic',
            'institution': 'Spitalul Clinic de Urgenta',
        },
        headers=headers
    )
    assert res_txt.status_code == 200
    sources = res_txt.json['sources']
    assert len(sources) == 1
    assert sources[0]['title'] == 'Protocol Intern Spital Clinic'
    assert 'local://' in sources[0]['url']
    assert '120 kV' in sources[0]['excerpt']
    assert sources[0]['local_file_ref']

    # 2. Verify file download endpoint
    source_id = sources[0]['id']
    file_res = client.get(f"{prefix}/sources/{source_id}/file", headers=headers)
    assert file_res.status_code == 200
    assert file_res.data == txt_content

    # 3. Upload a synthetic DOCX local source
    import zipfile
    docx_buf = io.BytesIO()
    with zipfile.ZipFile(docx_buf, 'w') as zf:
        zf.writestr(
            'word/document.xml',
            '<?xml version="1.0" encoding="UTF-8"?><w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body><w:p><w:r><w:t>Procedura operationala standardizata pentru scanare CT Abdomen.</w:t></w:r></w:p></w:body></w:document>'
        )
    docx_buf.seek(0)
    res_docx = client.post(
        prefix + '/sources/upload',
        data={
            'file': (docx_buf, 'procedura_abdomen.docx'),
            'title': 'Procedura Abdomen DOCX',
            'institution': 'Institutul de Radiologie',
        },
        headers=headers
    )
    assert res_docx.status_code == 200
    sources2 = res_docx.json['sources']
    assert len(sources2) == 2
    assert any('Procedura operationala standardizata' in s['excerpt'] for s in sources2)
    # Check that both sources were auto-injected into draft['document']
    doc2 = res_docx.json['document']
    assert '## Conținut preluat: Protocol Intern Spital Clinic' in doc2
    assert '120 kV' in doc2
    assert '## Conținut preluat: Procedura Abdomen DOCX' in doc2
    assert 'Procedura operationala standardizata' in doc2


def test_import_with_local_source_archives_file(workbench):
    client, headers, repo, state = workbench
    prefix = ready(workbench, 'ct')

    # Upload local source to the ready draft
    txt_data = b"Ghid local de diagnostic CT si doze de radiatie aprobate institutional."
    client.post(
        prefix + '/sources/upload',
        data={
            'file': (io.BytesIO(txt_data), 'ghid_local.txt'),
            'title': 'Ghid Local Arobat',
            'institution': 'Comisia Clinica',
        },
        headers=headers
    )

    # Import the draft
    res_import = client.post(prefix + '/import', json=REVIEW, headers=headers)
    assert res_import.status_code == 200
    path = repo / res_import.json['path']
    doc_text = path.read_text(encoding='utf-8')

    # Check that the local source was copied to docs/assets/protocols/sources/
    sources_dest = repo / 'docs' / 'assets' / 'protocols' / 'sources'
    assert sources_dest.exists()
    assert any('ghid_local.txt' in f.name for f in sources_dest.glob('*'))

    # Check that the markdown body has relative links to the archived source
    assert '## Surse și revizuire' in doc_text
    assert 'assets/protocols/sources/' in doc_text


def test_local_sources_catalog_and_reuse(workbench):
    client, headers, repo, state = workbench
    d1 = draft(workbench, 'ct')
    prefix1 = '/api/drafts/' + d1['id']

    # 1. Initially catalog is empty (or has existing repo docs)
    cat_res = client.get('/api/sources/local-library', headers=headers)
    assert cat_res.status_code == 200
    initial_count = len(cat_res.json)

    # 2. Upload a file to draft 1
    file_bytes = b"Procedura tehnica de radioprotectie si justificare clinica 2026."
    res_upload = client.post(
        prefix1 + '/sources/upload',
        data={
            'file': (io.BytesIO(file_bytes), 'norme_radioprotectie.txt'),
            'title': 'Norme Radioprotectie Spital',
            'institution': 'Laborator Radiologie',
            'manual_excerpt': 'Rezumat radioprotectie',
        },
        headers=headers
    )
    assert res_upload.status_code == 200
    s1 = res_upload.json['sources'][0]
    saved_ref = s1['local_file_ref']

    # 3. Check catalog endpoint contains the uploaded item
    cat_res2 = client.get('/api/sources/local-library', headers=headers)
    assert cat_res2.status_code == 200
    items = cat_res2.json
    assert len(items) == initial_count + 1
    matched = next((i for i in items if i['local_file_ref'] == saved_ref), None)
    assert matched is not None
    assert matched['title'] == 'Norme Radioprotectie Spital'
    assert matched['institution'] == 'Laborator Radiologie'
    assert matched['size_bytes'] == len(file_bytes)
    assert matched['sha256'] == s1['sha256']

    # 4. Create a completely separate draft 2
    d2 = draft(workbench, 'mri')
    prefix2 = '/api/drafts/' + d2['id']

    # 5. Attach the existing local document to draft 2 from catalog
    attach_res = client.post(
        prefix2 + '/sources/attach-local',
        json={'local_file_ref': saved_ref},
        headers=headers
    )
    assert attach_res.status_code == 200
    d2_sources = attach_res.json['sources']
    assert len(d2_sources) == 1
    s2 = d2_sources[0]
    assert s2['local_file_ref'] == saved_ref
    assert s2['title'] == 'Norme Radioprotectie Spital'
    assert s2['sha256'] == s1['sha256']
    assert s2['id'] != s1['id']  # Unique source ID per attachment
    assert '## Conținut preluat: Norme Radioprotectie Spital' in attach_res.json['document']
    assert 'Procedura tehnica de radioprotectie' in attach_res.json['document']

    # 6. Verify draft 2 can serve the file
    d2_file_res = client.get(f"{prefix2}/sources/{s2['id']}/file", headers=headers)
    assert d2_file_res.status_code == 200
    assert d2_file_res.data == file_bytes

    # 7. Re-attaching should update the source, not duplicate
    attach_res_repeat = client.post(
        prefix2 + '/sources/attach-local',
        json={'local_file_ref': saved_ref},
        headers=headers
    )
    assert attach_res_repeat.status_code == 200
    assert len(attach_res_repeat.json['sources']) == 1

    # 8. Error handling: invalid local_file_ref
    err_res = client.post(
        prefix2 + '/sources/attach-local',
        json={'local_file_ref': 'fisier_inexistent.pdf'},
        headers=headers
    )
    assert err_res.status_code == 400
    assert 'nu a fost găsit' in err_res.json['error']


def test_smart_extract_source_endpoint(workbench):
    client, headers, repo, state = workbench
    d = draft(workbench, 'rx')
    prefix = '/api/drafts/' + d['id']

    # Update document to represent Rx Coloană Toracală
    custom_doc = """---
title: Rx Coloană Toracală (Față & Profil)
modality: rx
category: coloana
author: Departamentul de Radiologie
last_updated: '2026-09-14'
clinical_indications:
- Dorsalgii cronice
position: Decubit dorsal
tech_params:
  kv: 75 - 85 (Față); 80 - 90 (Profil)
  mas: 25 - 50 (AEC)
sid_dff: 100 - 115 cm
slug: rx-coloana-toracala
---

# Rx Coloană Toracală
"""
    client.put(prefix, json={'document': custom_doc}, headers=headers)

    # Upload local source with new parameters
    src_content = b"""
    Protocol Spital Coloana Toracala:
    Parametrii tehnici generator:
    Tensiune: Fata 75 - 80 kV; Profil 80 - 95 kV.
    Curent-timp: 35 - 60 mAs.
    DFF: 120 cm.
    Focar mare.
    """
    up_res = client.post(
        prefix + '/sources/upload',
        data={'file': (io.BytesIO(src_content), 'protocol_toracala.txt'), 'title': 'Ghid Tehnic Toracala'},
        headers=headers
    )
    assert up_res.status_code == 200
    sources = up_res.json['sources']
    sid = sources[0]['id']

    # Call smart-extract endpoint explicitly
    extract_res = client.post(f"{prefix}/sources/{sid}/smart-extract", headers=headers)
    assert extract_res.status_code == 200
    data = extract_res.json
    assert data['count'] >= 2
    doc = data['draft']['document']
    assert '75 - 80 (Față); 80 - 95 (Profil)' in doc
    assert '35 - 60' in doc
    assert '120 cm' in doc



