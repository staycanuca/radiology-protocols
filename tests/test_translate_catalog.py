"""Safety invariants for bulk translation, independent of the API."""
from copy import deepcopy
import json
from pathlib import Path
import sys

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from translate_catalog import fields, numeric_tokens, set_value, validate
import translate_catalog as catalog


def test_numbers_ranges_and_decimal_separator():
    assert not validate('Angle 15–20 degrees; 2.5 cm, 70 kV.', 'Unghi de 15–20 grade; 2,5 cm, 70 kV.')
    assert 'numeric mismatch' in validate('15–20 degrees; 2.5 cm', '15–25 grade; 2.5 cm')
    assert validate('90 degrees twice: 90', '90 grade') == ['numeric mismatch']


def test_localize_unit_names_preserves_values_fractions_and_urls():
    source = '1 inch; 1½ inches; 10 × 12 inches (24 × 30 cm); https://example.org/12-inches'
    target = catalog.localize_units(source)
    assert target == '1 țol; 1½ țoli; 10 × 12 țoli (24 × 30 cm); https://example.org/12-inches'
    assert not validate(source, target)
    assert catalog.localize_units(target) == target
    assert catalog.localize_units('Casetă 18\x02 24 cm') == 'Casetă 18 × 24 cm'
    assert catalog.localize_units('⅓ inch; ¾ inch') == '⅓ țol; ¾ țol'


def test_links_and_missing_prose_are_rejected():
    assert validate('See https://example.org/a', 'Vezi https://example.org/b') == ['URL mismatch']
    assert 'possible omission' in validate('word ' * 60, 'Cuvânt.')
    assert validate('word', '') == ['empty translation']


def test_units_signs_and_fractions_cannot_change():
    assert 'number-unit mismatch' in validate('70 kV; 2 mAs', '2 kV; 70 mAs')
    assert 'number-unit mismatch' in validate('90 degrees', '90 cm')
    assert 'sign/fraction mismatch' in validate('-10 degrees', '10 grade')
    assert 'sign/fraction mismatch' in validate('1/2 inch', '1-2 inci')
    assert not validate('Angle 20\x06', 'Unghi de 20°')
    assert 'number-unit mismatch' in validate('Angle 20\x06', '20 cm')
    assert 'sign/fraction mismatch' in validate('⅓ inch', '½ țol')
    assert not validate('Fig. 6.39 Second toe', 'Fig. 6.39 Al doilea deget')
    assert 'number-unit mismatch' in validate('2 second exposure', 'Expunere de 2 cm')


def test_codex_batch_accepts_literal_newlines_but_rejects_ocr_controls(monkeypatch):
    import cli_ai
    response = ('{"items":[{"id":"0","text":"Prima linie\nA doua linie","incomplete":false},'
                '{"id":"1","text":"Casetă 18 \u0001 24 cm","incomplete":false}]}')
    monkeypatch.setattr(cli_ai, 'run_cli', lambda *a, **kw: (response, False, 'test'))
    batch = [{'id': catalog.digest(s), 'source': s, 'context': 'Rx'}
             for s in ('First line\nSecond line', 'Cassette 18 × 24 cm')]
    accepted, rejected, _ = catalog.codex_batch(batch)
    assert len(accepted) == 1
    assert accepted[0]['translation'] == 'Prima linie\nA doua linie'
    assert rejected[0]['errors'] == ['unresolved control character']


def test_fields_include_nested_prose_but_not_identifiers():
    fm = {'title': 'Elbow', 'slug': 'elbow', 'category': 'upper-limb',
          'sources': [{'title': 'English book', 'url': 'https://example.org'}],
          'images': [{'url': 'elbow.jpeg', 'caption': 'Elbow projection'}],
          'standard_views': [{'id': 'ap', 'title': 'AP view', 'position': 'The patient is seated.'}],
          'tech_params': {'collimation': 'Include joint', 'kv': '70'},
          'source_sections': {'Patient position': 'Seat patient'}}
    found = dict(fields(fm))
    assert found == {
        ('title',): 'Elbow', ('images', 0, 'caption'): 'Elbow projection',
        ('standard_views', 0, 'title'): 'AP view',
        ('standard_views', 0, 'position'): 'The patient is seated.',
        ('tech_params', 'collimation'): 'Include joint',
        ('source_sections', 'Patient position'): 'Seat patient',
    }
    result = deepcopy(fm)
    for path in found:
        set_value(result, path, 'Traducere')
    assert result['slug'] == fm['slug']
    assert result['images'][0]['url'] == fm['images'][0]['url']
    assert result['sources'] == fm['sources']
    assert result['standard_views'][0]['id'] == 'ap'
    assert result['tech_params']['kv'] == '70'


def test_incremental_apply_is_complete_per_document_and_detects_user_edits(tmp_path, monkeypatch):
    work = tmp_path / 'work'
    work.mkdir()
    (tmp_path / 'scripts').mkdir()
    (tmp_path / 'reports').mkdir()
    monkeypatch.setattr(catalog, 'ROOT', tmp_path)
    monkeypatch.setattr(catalog, 'WORK', work)
    docs, texts, rows = [], [], []
    for i in range(2):
        source = f'Projection {i}'
        fm = {'title': f'Rx {i}', 'position': source, 'slug': f'rx-{i}', 'modality': 'rx'}
        content = '---\n' + yaml.safe_dump(fm) + '---\nOriginal body\n'
        path = tmp_path / f'{i}.md'
        path.write_text(content, encoding='utf-8')
        key = catalog.digest(source)
        docs.append({'file': f'{i}.md', 'sha256': catalog.digest(content),
                     'fields': [{'path': ['position'], 'id': key}]})
        texts.append({'id': key, 'source': source, 'context': fm['title']})
        if i == 0:
            rows.append({**texts[-1], 'translation': 'Incidența 0', 'incomplete': False})
    (work / 'manifest.json').write_text(json.dumps({'documents': docs, 'texts': texts}), encoding='utf-8')
    (work / 'translations.jsonl').write_text('\n'.join(json.dumps(row) for row in rows), encoding='utf-8')
    untouched = (tmp_path / '1.md').read_bytes()
    catalog.apply(ready_only=True)
    assert (tmp_path / '1.md').read_bytes() == untouched
    after = (tmp_path / '0.md').read_bytes()
    assert 'Incidența 0' in after.decode('utf-8')
    catalog.apply(ready_only=True)
    assert (tmp_path / '0.md').read_bytes() == after
    with pytest.raises(ValueError, match='translations still missing'):
        catalog.apply()
    (tmp_path / '0.md').write_text('Changed by user', encoding='utf-8')
    with pytest.raises(ValueError, match='Source changed'):
        catalog.apply(ready_only=True)
