from copy import deepcopy
from datetime import date, timedelta
from types import SimpleNamespace

import pytest

from scripts.provenance import (audit, build_provenance, is_protocol, on_page_content,
                                recorded_date, safe_url, source_record, preserve_provenance_on_edit)


def protocol(**kwargs):
    return {'title': 'Protocol CT', 'category': 'abdomen', 'clinical_indications': [], **kwargs}


def test_missing_slug_is_still_a_protocol_but_landing_pages_are_not():
    assert is_protocol('ct/abdomen/test.md', protocol())
    assert not is_protocol('ct/abdomen/index.md', protocol(slug='index'))
    assert not is_protocol('ct/compare.md', protocol(slug='compare'))
    assert not is_protocol('rx/radioprotectie.md', {'title': 'Politică RX'})
    assert not is_protocol('despre-proiect.md', {'title': 'Despre proiect'})


def test_default_states_do_not_invent_source_processing_or_reviews():
    meta = protocol(author='OHSU / Departamentul de Radiologie', last_updated='2026-01-02')
    original = deepcopy(meta)
    data = build_provenance(meta, 'ct/abdomen/exam.md')
    assert meta == original
    assert data['sources'] == []
    assert data['processing'] == []
    assert data['adaptations'] == []
    assert data['fidelity']['state'] == data['medical']['state'] == 'missing'
    assert 'missing_sources' in data['gaps']
    assert data['updated'] == '2026-01-02'


def test_technical_timestamp_is_not_consultation_or_review():
    data = build_provenance(protocol(sources=[{
        'title': 'Ghid', 'url': 'https://example.org/guide',
        'checked_at': '2026-01-02T12:00:00+00:00', 'sha256': 'hash-of-url',
    }]), 'ct/abdomen/exam.md')
    source = data['sources'][0]
    assert source['recorded_on'] == '2026-01-02'
    assert not source['consulted_on']
    assert not source['relationship']
    assert data['medical']['state'] == 'missing'
    assert 'sha256' not in source


def test_bibliography_uses_only_explicit_edition_and_page():
    clark = source_record({'title': "Clark's Positioning in Radiography (Ed. 12), Pagina 373"})
    assert clark['edition'] == '12'
    assert clark['locator'] == 'Pagini: 373'
    ambiguous = source_record({'title': 'Bontrager (Ed. 9/10), Pagina 666'})
    assert ambiguous['edition_ambiguous']
    merrill = source_record({'title': 'Merrill’s Atlas, pagini 1487–1490', 'url': 'https://example.org/edition-15'})
    assert not merrill['edition']
    assert merrill['locator'] == 'Pagini: 1487–1490'


def test_page_numbers_are_not_assigned_to_every_source():
    data = build_provenance(protocol(source_pages=[123, 124], sources=[{'title': 'A'}, {'title': 'B'}]), 'rx/abdomen/exam.md')
    assert data['source_pages'] == '123, 124'
    assert all(not source['locator'] for source in data['sources'])


def test_legacy_workbench_record_is_preserved_without_claiming_full_review():
    data = build_provenance(protocol(workbench_review={
        'clinical_review': True, 'reviewer': 'operator', 'reviewed_at': '2026-01-02T12:00:00',
    }), 'rx/coloana/exam.md')
    assert data['medical']['state'] == 'incomplete'
    assert 'operator' in data['legacy_note']
    assert data['fidelity']['state'] == 'missing'


def test_review_requires_identity_date_scope_qualification_and_matching_version():
    review = {'reviewer': 'Persoană de test', 'reviewed_on': '2026-01-02',
              'scope': 'Confruntare cu sursa', 'qualification': 'Calificare de test', 'version': 'v1'}
    meta = protocol(provenance={'version': 'v1', 'source_verification': review, 'medical_review': review})
    data = build_provenance(meta, 'ct/abdomen/exam.md')
    assert data['medical']['state'] == data['fidelity']['state'] == 'recorded'
    meta['provenance']['version'] = 'v2'
    assert build_provenance(meta, 'ct/abdomen/exam.md')['medical']['state'] == 'outdated'
    meta['provenance']['version'] = 'v1'
    del review['qualification']
    data = build_provenance(meta, 'ct/abdomen/exam.md')
    assert data['medical']['state'] == 'incomplete'
    assert data['fidelity']['state'] == 'recorded'


def test_draft_restrictions_remain_visible():
    data = build_provenance(protocol(clinical_status='draft_not_for_clinical_use', sources=['Manual']), 'rx/exam.md')
    assert data['publication'] == 'Ciornă — nu se utilizează clinic'


@pytest.mark.parametrize('url', ['javascript:alert(1)', 'file:///C:/private.pdf', '//example.org',
                                     'https://user:password@example.org', 'https://[invalid'])
def test_non_public_and_unsafe_urls_are_rejected(url):
    assert not safe_url(url)


def test_dates_reject_future_or_invalid_values():
    assert not recorded_date(date.today() + timedelta(days=1))
    assert not recorded_date('not-a-date')
    assert recorded_date('2026-01-02T12:00:00Z') == '2026-01-02'


@pytest.mark.parametrize('html', ['<h1>Titlu</h1><p>Conținut</p>', '<p>Conținut</p>'])
def test_card_is_escaped_after_one_h1_and_feedback_identifies_protocol(html):
    meta = protocol(slug='exam test', sources=[{'title': '<script>alert(1)</script>', 'url': 'javascript:alert(1)'}])
    page = SimpleNamespace(meta=meta, file=SimpleNamespace(src_uri='ct/abdomen/exam.md'), title='Titlu')
    result = on_page_content(html, page, {'site_url': 'https://example.org/subpath/'}, [])
    assert result.count('<h1>') == 1
    assert result.index('</h1>') < result.index('protocol-provenance-title') < result.index('<p>Conținut</p>')
    assert '<script>' not in result and 'javascript:' not in result
    assert '&lt;script&gt;' in result
    assert 'https://example.org/subpath/request-change/?protocol=exam+test' in result
    assert 'data-search-exclude' in result


def test_audit_counts_missing_sources_and_never_promotes_generic_author(tmp_path):
    folder = tmp_path / 'ct' / 'abdomen'
    folder.mkdir(parents=True)
    (folder / 'exam.md').write_text('---\ntitle: CT\ncategory: abdomen\nclinical_indications: []\nauthor: Departament\n---\n# CT', encoding='utf-8')
    (folder / 'index.md').write_text('# Index', encoding='utf-8')
    report = audit(tmp_path)
    assert report['protocols'] == 1
    assert report['with_sources'] == 0
    assert report['gaps']['medical_review_missing'] == 1


def test_edit_preserves_references_and_invalidates_existing_review_without_mutation():
    original = protocol(sources=[{'title': 'Manual'}], provenance={'version': 'v1',
        'medical_review': {'reviewer': 'Test', 'qualification': 'Test', 'reviewed_on': '2026-01-02', 'scope': 'Test', 'version': 'v1'}})
    snapshot = deepcopy(original)
    edited = protocol(title='Conținut modificat')
    saved = preserve_provenance_on_edit(original, edited)
    assert saved['sources'] == original['sources']
    assert saved['provenance']['review_required'] is True
    assert build_provenance(saved, 'ct/abdomen/exam.md')['medical']['state'] == 'needs_review'
    assert original == snapshot
    unchanged = preserve_provenance_on_edit(original, {**protocol(), 'last_updated': '2026-02-01'})
    assert not unchanged['provenance'].get('review_required')
