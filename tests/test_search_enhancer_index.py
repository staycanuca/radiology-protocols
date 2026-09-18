import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from scripts.search_enhancer import on_post_build


class SearchIndexTests(unittest.TestCase):
    def test_normalization_keeps_index_valid_and_does_not_duplicate_body(self):
        with TemporaryDirectory() as tmp:
            index = Path(tmp) / 'search/search_index.json'
            index.parent.mkdir()
            index.write_text(json.dumps({'docs': [{'title': 'Mână', 'text': 'Poziție mână ' * 100,
                                                  'location': 'rx/mana/'}]}), encoding='utf-8')
            on_post_build({'site_dir': tmp})
            first = index.read_text(encoding='utf-8')
            entry = json.loads(first)['docs'][0]
            self.assertIn('pozitie', entry['text'])
            self.assertIn('mana', entry['text'])
            self.assertEqual(entry['text'].count('Poziție'), 100)
            on_post_build({'site_dir': tmp})
            self.assertEqual(index.read_text(encoding='utf-8'), first)
            self.assertFalse(index.with_suffix('.json.tmp').exists())
