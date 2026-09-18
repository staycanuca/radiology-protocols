"""Regresii pentru delimitarea incidențelor și secțiunilor Merrill."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import extract_merrill_protocols as extractor


class Document:
    def get_toc(self):
        return [[2, '3. Thoracic Viscera: Chest and Upper Airway', 135],
                [3, 'Chest', 167], [2, '4. Abdomen', 204]]


class MerrillTests(unittest.TestCase):
    def test_multiline_heading_and_continuation(self):
        lines = [extractor.Line(page, 10 + i * 10, text) for i, (page, text) in enumerate([
            (167, 'Lateral Projection'), (167, 'R or L position'),
            (168, 'Position of patient'), (168, '• Upright'),
            (169, 'Central ray'), (169, '• Horizontal'),
            (169, 'Evaluation Criteria'), (169, '▪ No rotation'),
            (170, 'AP Projection'), (170, 'Position of patient'),
            (170, '• Supine'), (171, 'Central ray'), (171, '• Perpendicular'),
        ])]
        protocols = extractor.discover(Document(), lines)
        self.assertEqual(len(protocols), 2)
        self.assertIn('Lateral Projection', protocols[0].title)
        self.assertIn('R or L position', protocols[0].title)
        self.assertEqual(protocols[0].lines[-1].page, 169)
        self.assertEqual(protocols[0].category, 'torace')

    def test_captions_do_not_contaminate_positioning(self):
        lines = [extractor.Line(167, 10, text) for text in [
            'Position of part', '• Rotate shoulders',
            'FIG. 3.34 Positioning', 'A patient stands against the detector.',
            '• Shield gonads.', '• Respiration: Full inspiration',
            'Central ray', '• Perpendicular', 'Evaluation Criteria', '▪ No rotation',
        ]]
        sections = extractor.parse_sections(lines)
        self.assertNotIn('A patient', sections['part_pos'])
        self.assertIn('Shield gonads', sections['part_pos'])
        self.assertEqual(sections['respiration'], 'Full inspiration')
        self.assertIn('No rotation', sections['criteria'])

    def test_page_validation(self):
        self.assertEqual(extractor.parse_pages('1,3-5,3', 5), {1, 3, 4, 5})
        for value in ['0', '-1', '6', '4-2', '1,', 'abc']:
            with self.assertRaises(ValueError):
                extractor.parse_pages(value, 5)

    def test_missing_data_is_not_invented(self):
        line = extractor.Line(167, 10, 'PA Projection')
        protocol = extractor.Protocol('Chest PA', 'torace', 'Chest', 0, 1, [line])
        fm = extractor.build_frontmatter(protocol, {}, 'test', [],
                                         Path('source.pdf').resolve(), Path('out/test.md').resolve())
        self.assertEqual(fm['centering'], extractor.MISSING)
        self.assertEqual(fm['quality_criteria'], [extractor.MISSING])
        self.assertEqual(fm['status'], 'draft')
        self.assertNotIn('kv', fm['tech_params'])


if __name__ == '__main__':
    unittest.main()
