"""search_enhancer.py — MkDocs hook for Romanian diacritic-insensitive search.

Enriches the search index so that queries without diacritics
(e.g., 'mana', 'sold', 'glezna', 'coloana', 'umar', 'plamani')
instantly match Romanian medical titles and contents with diacritics
(e.g., 'Mână', 'Șold', 'Gleznă', 'Coloană', 'Umăr', 'Plămâni').
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path


def normalize_ro(text: str) -> str:
    """Strip Romanian diacritics (both legacy cedilla and modern comma) to basic ASCII."""
    if not text:
        return ""
    table = str.maketrans({
        'ă': 'a', 'Ă': 'A',
        'â': 'a', 'Â': 'A',
        'î': 'i', 'Î': 'I',
        'ș': 's', 'Ș': 'S',
        'ş': 's', 'Ş': 'S',
        'ț': 't', 'Ț': 'T',
        'ţ': 't', 'Ţ': 'T',
    })
    text = text.translate(table)
    return ''.join(c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn')


def on_page_content(html: str, page, config, files) -> str:
    """Inject hidden unaccented terms into page HTML so SearchIndex naturally picks them up."""
    title = getattr(page, 'title', '') or ''
    norm_title = normalize_ro(title)

    meta = getattr(page, 'meta', {}) or {}
    synonyms = meta.get('synonyms', [])
    if isinstance(synonyms, list):
        syn_str = ' '.join(normalize_ro(str(s)) for s in synonyms)
    else:
        syn_str = normalize_ro(str(synonyms))

    url_str = getattr(page, 'url', '') or ''
    url_keywords = normalize_ro(url_str.replace('/', ' ').replace('-', ' '))

    extra_keywords = f"{norm_title} {syn_str} {url_keywords}".strip()
    if extra_keywords:
        hidden_div = (
            f'\n<div class="search-keywords" style="display:none;visibility:hidden;height:0;width:0;overflow:hidden;" aria-hidden="true">\n'
            f'{extra_keywords}\n'
            f'</div>\n'
        )
        return html + hidden_div
    return html


def on_post_build(config) -> None:
    """Post-process search_index.json to add high-boost tags and normalized text."""
    site_dir = Path(config['site_dir'])
    index_path = site_dir / 'search' / 'search_index.json'
    if not index_path.exists():
        return

    try:
        data = json.loads(index_path.read_text(encoding='utf-8'))
        docs = data.get('docs', [])

        import html
        for doc in docs:
            title = doc.get('title', '') or ''
            text = doc.get('text', '') or ''
            location = doc.get('location', '') or ''

            raw_title = html.unescape(title)
            norm_title = normalize_ro(raw_title)
            norm_loc = normalize_ro(location.replace('/', ' ').replace('-', ' '))
            norm_text = normalize_ro(html.unescape(text))

            # Extract distinct unaccented words from title and location (min 2 chars)
            title_words = re.findall(r'[a-zA-Z0-9]+', (norm_title + ' ' + norm_loc).lower())
            stop_entities = {'amp', 'quot', 'apos', 'lt', 'gt', 'nbsp'}
            distinct_words = [w for w in dict.fromkeys(title_words) if len(w) > 1 and w not in stop_entities]

            # In Material's Lunr configuration, 'tags' field has a boost of 1,000,000!
            existing_tags = doc.get('tags', [])
            if isinstance(existing_tags, list):
                combined_tags = list(dict.fromkeys(existing_tags + distinct_words))
            else:
                combined_tags = distinct_words
            doc['tags'] = combined_tags

            # Add only missing normalized words, not a second copy of the body.
            # Also remains stable if an incremental build reuses enhanced entries.
            existing_words = set(re.findall(r'\w+', text.lower()))
            normalized_words = dict.fromkeys(re.findall(r'\w+', (norm_title + ' ' + norm_text).lower()))
            extra_words = [word for word in normalized_words if word not in existing_words]
            doc['text'] = text + ('\n' + ' '.join(extra_words) if extra_words else '')

        # Readers must see either the complete old index or the complete new one.
        temporary = index_path.with_suffix('.json.tmp')
        temporary.write_text(json.dumps(data, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
        temporary.replace(index_path)
    except Exception as exc:
        print(f"[search_enhancer] Warning: could not enhance search index: {exc}")
