"""Regression coverage for mixed Romanian/English protocol translation."""
from copy import deepcopy
import json
from pathlib import Path
import sys

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from radiology_translator import (
    calculate_english_score, detect_english_fragments, translate_field_text,
    translate_protocol_frontmatter, translation_review,
)
from translate_and_adapt_protocols import process_file

ENTRIES = json.loads((ROOT / 'scripts/radiology_translations_ro.json').read_text(encoding='utf-8'))


@pytest.mark.parametrize('entry', ENTRIES)
def test_reviewed_mixed_text_and_repeat_run(entry):
    translated = translate_field_text(entry['source'])
    assert translated == entry['translation']
    assert translate_field_text(translated) == translated


def test_unknown_sentence_is_not_partially_destroyed():
    source = 'The patient should never move the arm until the examination is finished.'
    assert translate_field_text(source) == source
    assert 'should' in detect_english_fragments(source)


def test_romanian_and_technical_values_unchanged():
    text = 'Evaluarea normală a articulației. Film radiologic, contrast normal; fascicul perpendicular. 2.5 cm, 90°, 70 kV, 4 mAs.'
    assert translate_field_text(text) == text
    assert not detect_english_fragments(text)
    assert translate_field_text('Nespecificat în fragmentul extras; de verificat în sursă') == 'Nespecificat în fragmentul extras; de verificat în sursă'


def test_known_sentences_preserve_negation_and_certainty():
    assert translate_field_text('fracture') == 'fractură'
    assert translate_field_text('Suspected fracture') == 'Suspiciune de fractură'
    assert translate_field_text('Suspend respiration.\nfracture') == 'Apnee pe durata expunerii.\nfractură'


def test_markdown_urls_and_line_breaks():
    text = 'fracture\n\n[fracture](https://example.org/fracture) `fracture`'
    assert translate_field_text(text) == 'fractură\n\n[fracture](https://example.org/fracture) `fracture`'


def test_detection_and_unicode_denominator():
    assert calculate_english_score('when în aceeași poziție') == .25
    assert {'most', 'obtained', 'when', 'pass', 'through', 'supracondylar'} <= set(
        detect_english_fragments('most obtained when pass through supracondylar'))


def test_frontmatter_no_input_mutation_and_all_review_fields():
    source = {
        'title': 'Rx Cot', 'slug': 'fracture',
        'tech_params': {'collimation': 'fracture'},
        'images': [{'caption': 'fracture', 'url': 'fracture.jpg'}],
        'clinical_indications': ['unusual injury'],
        'quality_criteria': ['obtained when'],
        'source_sections': {'Position': 'fracture'},
        'sources': [{'title': 'Basic projections', 'url': 'https://example.org'}],
    }
    before = deepcopy(source)
    translated, modified = translate_protocol_frontmatter(source)
    assert modified and source == before
    assert translated['images'][0]['caption'] == 'fractură'
    assert translated['images'][0]['url'] == 'fracture.jpg'
    assert translated['sources'] == source['sources']
    assert translated['slug'] == source['slug']
    assert {f['field'] for f in translation_review(translated)} == {
        'clinical_indications[0]', 'quality_criteria[0]'}


def test_dry_run_and_second_run_preserve_document(tmp_path):
    path = tmp_path / 'protocol.md'
    fm = {'title': 'Rx Cot', 'slug': 'rx-cot', 'modality': 'rx',
          'position': 'fracture', 'images': [], 'clinical_indications': []}
    path.write_text('---\n' + yaml.safe_dump(fm) + '---\nOriginal body\n', encoding='utf-8')
    before = path.read_bytes()
    assert process_file(path, dry_run=True)['modified']
    assert path.read_bytes() == before
    assert process_file(path)['modified']
    after = path.read_bytes()
    assert not process_file(path)['modified']
    assert path.read_bytes() == after


def test_noop_does_not_replace_custom_body(tmp_path):
    path = tmp_path / 'protocol.md'
    path.write_text('---\ntitle: Rx Cot\nposition: Text românesc\n---\nCustom body\n', encoding='utf-8')
    before = path.read_bytes()
    assert not process_file(path)['modified']
    assert path.read_bytes() == before
