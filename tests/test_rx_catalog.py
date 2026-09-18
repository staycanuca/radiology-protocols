from pathlib import Path
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest

from scripts.rx_catalog import on_nav, on_page_markdown, render_catalog


class CatalogTests(unittest.TestCase):
    def test_sidebar_uses_catalog_sort_order(self):
        def page(title, name, slug=True):
            return SimpleNamespace(title=title, is_page=True,
                                   meta={'title': title, 'slug': name} if slug else {},
                                   file=SimpleNamespace(src_path=f'rx/torace/{name}.md'))
        pages = [page('Zebra', 'a'), page('alpha', 'z'), page('Torace', 'index', False)]
        nav = SimpleNamespace(items=[SimpleNamespace(children=pages)])
        with TemporaryDirectory() as tmp:
            directory = Path(tmp) / 'rx/torace'
            directory.mkdir(parents=True)
            for p in pages:
                path = Path(tmp) / p.file.src_path
                path.write_text(f'---\nslug: {path.stem}\ntitle: {p.title}\n---\n', encoding='utf-8')
                p.meta = {}  # MkDocs has not read the page when on_nav fires.
            on_nav(nav, {'docs_dir': tmp}, [])
        self.assertEqual([p.title for p in pages], ['Torace', 'alpha', 'Zebra'])

    def test_new_protocol_appears_without_manual_index_update(self):
        with TemporaryDirectory() as tmp:
            category = Path(tmp) / 'rx/torace'
            category.mkdir(parents=True)
            (category / '.pages').write_text('title: Torace\n', encoding='utf-8')
            (category / 'index.md').write_text('Old list', encoding='utf-8')
            (category / 'first.md').write_text('---\nslug: first\ntitle: First\n---\n', encoding='utf-8')
            page = SimpleNamespace(file=SimpleNamespace(src_path='rx/torace/index.md'))
            self.assertIn('**1 protocoale**', on_page_markdown('Old list', page, {'docs_dir': tmp}, []))
            (category / 'merrill.md').write_text('---\nslug: merrill\ntitle: Merrill [AP]\n---\n', encoding='utf-8')
            output = render_catalog(category)
            self.assertIn('**2 protocoale**', output)
            self.assertIn(r'[Merrill \[AP\]](merrill.md)', output)
            self.assertNotIn('index.md)', output)

    def test_does_not_replace_protocol_or_rx_home(self):
        for path in ('rx/index.md', 'rx/torace/protocol.md', 'ct/chest/index.md'):
            page = SimpleNamespace(file=SimpleNamespace(src_path=path))
            self.assertEqual(on_page_markdown('Keep me', page, {}, []), 'Keep me')


if __name__ == '__main__':
    unittest.main()
