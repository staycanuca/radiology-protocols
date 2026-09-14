"""test_enrich_existing_sources.py — Teste unitare pentru îmbogățirea surselor din protocoale."""

import os
import sys
from pathlib import Path
import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts.enrich_existing_sources import (
    parse_frontmatter,
    get_sources_for_protocol,
    build_references_section,
    enrich_protocol_file,
    SOURCE_CATALOG,
)


def test_parse_frontmatter_valid():
    content = "---\ntitle: Test\nmodality: rx\n---\n\n# Body content\n"
    fm, body = parse_frontmatter(content)
    assert fm['title'] == 'Test'
    assert fm['modality'] == 'rx'
    assert '# Body content' in body


def test_parse_frontmatter_empty():
    fm, body = parse_frontmatter("# No frontmatter")
    assert fm == {}
    assert body == "# No frontmatter"


@pytest.mark.parametrize('modality', ['rx', 'ct', 'irm', 'eco', 'fluoro'])
def test_get_sources_returns_valid_records(modality):
    sources = get_sources_for_protocol(modality, 'default', 'test-slug', 'Test Title', '2026-09-14T15:00:00Z')
    assert len(sources) >= 1
    for s in sources:
        assert s['title']
        assert s['url'].startswith('https://')
        assert s['sha256']
        assert s['checked_at'] == '2026-09-14T15:00:00Z'


def test_get_sources_pediatric_detection():
    # Detectare pediatrie prin slug
    sources_ped = get_sources_for_protocol('rx', 'torace', 'rx-torace-pediatric', 'Rx Torace Pediatric', '2026-09-14T15:00:00Z')
    assert any('Image Gently' in s['title'] for s in sources_ped)

    # Detectare pediatrie prin categorie
    sources_cat = get_sources_for_protocol('ct', 'pediatrie', 'ct-abdomen', 'CT Abdomen', '2026-09-14T15:00:00Z')
    assert any('Image Gently' in s['title'] for s in sources_cat)


def test_get_sources_category_specialization():
    sources_cardiac = get_sources_for_protocol('ct', 'cardiac', 'coronary-cta', 'Coronary CTA', '2026-09-14T15:00:00Z')
    assert any('SCCT' in s['title'] or 'Cardiac' in s['title'] or 'Cardiovascular' in s['title'] for s in sources_cardiac)

    sources_neuro = get_sources_for_protocol('irm', 'neuro', 'irm-cerebral', 'IRM Cerebral', '2026-09-14T15:00:00Z')
    assert any('Brain' in s['title'] or 'OHSU' in s['title'] for s in sources_neuro)


def test_build_references_section():
    sources = [
        {
            'title': 'Ghid Test',
            'url': 'https://example.org/ghid',
            'institution': 'Institut Test',
            'source_region': 'UE',
        }
    ]
    md = build_references_section(sources)
    assert '## Surse și revizuire' in md
    assert '- [Ghid Test](https://example.org/ghid) — *Institut Test* (UE)' in md


def test_enrich_protocol_file_dry_run(tmp_path):
    doc_path = tmp_path / 'rx-torace.md'
    doc_path.write_text(
        "---\ntitle: Rx Torace\nmodality: rx\ncategory: torace\nslug: rx-torace\n---\n\n# Rx Torace\nCorp text\n",
        encoding='utf-8'
    )
    res = enrich_protocol_file(doc_path, '2026-09-14T15:00:00Z', dry_run=True)
    assert res['status'] == 'updated'
    # Fișierul nu a fost modificat pe disc în dry-run
    content = doc_path.read_text(encoding='utf-8')
    assert '## Surse și revizuire' not in content


def test_enrich_protocol_file_apply(tmp_path):
    doc_path = tmp_path / 'rx-torace.md'
    doc_path.write_text(
        "---\ntitle: Rx Torace\nmodality: rx\ncategory: torace\nslug: rx-torace\n---\n\n# Rx Torace\nCorp text\n",
        encoding='utf-8'
    )
    res = enrich_protocol_file(doc_path, '2026-09-14T15:00:00Z', dry_run=False)
    assert res['status'] == 'updated'

    content = doc_path.read_text(encoding='utf-8')
    fm, body = parse_frontmatter(content)
    assert 'sources' in fm
    assert len(fm['sources']) >= 2
    assert fm['sources'][0]['title']
    assert '## Surse și revizuire' in body
    assert 'https://op.europa.eu' in body or 'https://www.acr.org' in body

    # A doua rulare fără force este omisă
    res_repeat = enrich_protocol_file(doc_path, '2026-09-14T15:00:00Z', force=False, dry_run=False)
    assert res_repeat['status'] == 'skipped'

    # Cu force=True se re-actualizează
    res_force = enrich_protocol_file(doc_path, '2026-09-14T15:00:00Z', force=True, dry_run=False)
    assert res_force['status'] == 'updated'
