from datetime import date, timedelta
import gzip
import json
from pathlib import Path
from types import SimpleNamespace
import xml.etree.ElementTree as ET

from jinja2 import Environment

from scripts import seo, search_enhancer


def page(source, title, url, **meta):
    return SimpleNamespace(file=SimpleNamespace(src_uri=source), title=title, url=url,
                           canonical_url='https://protocoale.co.uk/' + url,
                           is_homepage=source == 'index.md', meta=meta)


CONFIG = {'site_url': 'https://protocoale.co.uk/', 'site_name': 'Radiologie',
          'site_description': 'Protocoale de radiologie.'}


def test_breadcrumbs_link_only_existing_ancestors_and_escape_json():
    home = page('index.md', 'Acasă', '')
    ct = page('ct/index.md', 'CT', 'ct/')
    protocol = page('ct/abdomen/exam.md', 'CT </script><script>alert(1)</script>', 'ct/abdomen/exam/', slug='exam')
    seo.on_page_content('', protocol, CONFIG, [])
    seo.on_page_context({}, protocol, CONFIG, SimpleNamespace(pages=[home, ct, protocol]))
    metadata = protocol.meta['seo']
    assert [item['url'] for item in metadata['breadcrumbs']] == [home.canonical_url, ct.canonical_url, protocol.canonical_url]
    rendered = Environment().from_string('{{ data | tojson }}').render(data=metadata['schema'])
    assert '</script>' not in rendered
    assert json.loads(rendered)['@graph'][1]['url'] == protocol.canonical_url


def test_editorial_description_and_page_specific_fallback():
    first = page('ct/a.md', 'CT torace', 'ct/a/', slug='a')
    second = page('ct/b.md', 'CT abdomen', 'ct/b/', slug='b')
    assert seo.description_for(first, CONFIG) != seo.description_for(second, CONFIG)
    first.meta['description'] = 'Descriere editorială &amp; detalii.'
    assert seo.description_for(first, CONFIG) == 'Descriere editorială & detalii.'


def test_editorial_title_wins_over_short_navigation_label():
    home = page('index.md', 'Acasă', '')
    home.meta['title'] = 'Protocoale CT, IRM și RX'
    seo.on_page_content('', home, CONFIG, [])
    seo.on_page_context({}, home, CONFIG, SimpleNamespace(pages=[home]))
    assert home.meta['seo']['title'] == home.meta['title']


def test_sitemap_matches_indexability_and_uses_only_editorial_dates(tmp_path):
    seo.on_pre_build(CONFIG)
    home = page('index.md', 'Acasă', '')
    form = page('request-change.md', 'Formular', 'request-change/', robots='noindex, follow')
    exam = page('ct/exam.md', 'CT', 'ct/exam/', last_updated='2026-01-02')
    for item in [home, form, exam]:
        seo.on_page_content('', item, CONFIG, [])
        seo.on_page_context({}, item, CONFIG, SimpleNamespace(pages=[home, form, exam]))
    entries = ''.join(f'<url><loc>{item.canonical_url}</loc><lastmod>2099-01-01</lastmod></url>' for item in [home, form, exam])
    sitemap = tmp_path / 'sitemap.xml'
    sitemap.write_text(f'<urlset xmlns="{seo._SITEMAP_NS}">{entries}</urlset>', encoding='utf-8')
    seo.on_post_build({**CONFIG, 'site_dir': tmp_path})
    root = ET.parse(sitemap).getroot()
    ns = {'s': seo._SITEMAP_NS}
    assert [item.findtext('s:loc', namespaces=ns) for item in root] == [home.canonical_url, exam.canonical_url]
    assert root[0].find('s:lastmod', ns) is None
    assert root[1].findtext('s:lastmod', namespaces=ns) == '2026-01-02'
    assert gzip.decompress((tmp_path / 'sitemap.xml.gz').read_bytes()) == sitemap.read_bytes()
    assert 'Sitemap: https://protocoale.co.uk/sitemap.xml' in (tmp_path / 'robots.txt').read_text()
    seo.on_pre_build(CONFIG)
    assert not seo._pages


def test_invalid_and_future_dates_are_omitted():
    assert seo.valid_date('invalid') is None
    assert seo.valid_date(None) is None
    assert seo.valid_date(date.today() + timedelta(days=1)) is None
    assert seo.valid_date('2026-01-02') == '2026-01-02'


def test_search_synonyms_live_in_index_instead_of_hidden_html(tmp_path):
    search_enhancer.on_pre_build({})
    exam = page('rx/mana.md', 'Mână', 'rx/mana/', synonyms=['Scafoid carpian'])
    assert search_enhancer.on_page_content('<h1>Mână</h1>', exam, {}, []) == '<h1>Mână</h1>'
    search_dir = tmp_path / 'search'
    search_dir.mkdir()
    index = search_dir / 'search_index.json'
    index.write_text(json.dumps({'docs': [{'title': 'Mână', 'text': 'Poziție mână', 'location': exam.url}]}), encoding='utf-8')
    search_enhancer.on_post_build({'site_dir': tmp_path})
    doc = json.loads(index.read_text(encoding='utf-8'))['docs'][0]
    assert 'scafoid' in doc['keywords']
    assert 'mana' in doc['text']
    search_enhancer.on_pre_build({})
