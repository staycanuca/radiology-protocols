"""Source-backed completion with field ownership and conservative merging."""
from copy import deepcopy
import hashlib
import json
import re
import yaml

from .smart_extractor import extract_parameters_by_modality, sync_body_parameters

SUMMARY_START = '<!-- workbench:parameters -->'
SUMMARY_END = '<!-- /workbench:parameters -->'


def parameter_summary(fm, schema):
    rows = []
    for field, value in leaves(fm):
        if field.split('.')[0] not in schema or field.split('.')[0] in {'title', 'slug', 'modality', 'category', 'author', 'last_updated', 'images'}:
            continue
        if value in (None, '', [], {}):
            continue
        display = yaml.safe_dump(value, allow_unicode=True, default_flow_style=True).removesuffix('...\n').strip()
        display = display.replace('|', '&#124;').replace('\n', ' ').replace('<', '&lt;').replace('>', '&gt;')
        rows.append('| ' + field.replace('_', ' ') + ' | ' + display + ' |')
    return SUMMARY_START + '\n## Parametri ai protocolului\n\n| Câmp | Valoare |\n| --- | --- |\n' + '\n'.join(rows) + '\n' + SUMMARY_END


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, default=str).encode()).hexdigest()


def leaves(value, prefix=''):
    for key, item in value.items():
        path = f'{prefix}.{key}' if prefix else key
        if isinstance(item, dict):
            yield from leaves(item, path)
        else:
            yield path, item


def get_field(value, path):
    for key in path.split('.'):
        if not isinstance(value, dict):
            return None
        value = value.get(key)
    return value


def set_field(value, path, item):
    keys = path.split('.')
    for key in keys[:-1]:
        if not isinstance(value.get(key), dict):
            value[key] = {}
        value = value[key]
    value[keys[-1]] = deepcopy(item)


def complete(draft, parse, template, apply=True):
    fm, body = parse(draft['document'])
    schema, _ = parse(template)
    # Clinical sections shared by the modality templates and existing extractor.
    allowed = set(schema) | {'contraindications', 'npo', 'premedication', 'patient_prep',
                            'breathing', 'safety', 'quality_criteria'}
    allowed -= {'title', 'slug', 'author', 'category', 'modality', 'images', 'last_updated'}
    context = fingerprint([fm.get('title'), fm.get('modality')])
    previous = draft.get('completion', {})
    provenance = deepcopy(previous.get('provenance', {}))
    candidates = {}
    for source in draft['sources']:
        extracted = extract_parameters_by_modality(source.get('excerpt', ''), fm['modality'], fm.get('title', ''))
        for field, value in leaves(extracted):
            if field.split('.')[0] not in allowed or value in (None, '', [], {}):
                continue
            candidates.setdefault(field, []).append({'source_id': source['id'], 'title': source['title'],
                'sha256': source.get('sha256'), 'excerpt_sha256': fingerprint(source.get('excerpt', '')),
                'value': value})
    changes, conflicts, stale = [], [], []
    accepted = {}
    for field, options in candidates.items():
        old = get_field(fm, field)
        distinct = {fingerprint(o['value']) for o in options}
        owner = provenance.get(field)
        decision = draft.get('completion_decisions', {}).get(field)
        if decision and decision['candidates'] == fingerprint(options) and decision['value'] == old:
            continue
        protected = any(field == manual or field.startswith(manual + '.') for manual in draft.get('manual_fields', []))
        editable = not protected and (old in (None, '', [], {}) or (owner and old == owner['value'] and owner.get('context') == context))
        if len(distinct) > 1 or (not editable and old != options[0]['value']):
            conflicts.append({'field': field, 'current': old, 'candidates': options})
            continue
        value = options[0]['value']
        if old != value and apply:
            set_field(fm, field, value)
            set_field(accepted, field, value)
            changes.append({'field': field, 'old_value': old, 'new_value': value})
            provenance[field] = {'value': deepcopy(value), 'context': context, 'sources': options}
        elif owner and old == value and owner.get('context') == context:
            provenance[field]['sources'] = options
    source_ids = {s['id'] for s in draft['sources']}
    for field, owner in provenance.items():
        if owner.get('context') != context or any(s['source_id'] not in source_ids for s in owner['sources']) or field not in candidates:
            stale.append(field)
    if changes:
        # Preserve authored prose; only synchronize known template slots.
        if not draft.get('manual_body'):
            body = sync_body_parameters(body, accepted, fm['modality'])
    summary = re.search(re.escape(SUMMARY_START) + r'.*?' + re.escape(SUMMARY_END), body, re.S)
    if summary and (not previous.get('summary_sha256') or fingerprint(summary[0]) == previous['summary_sha256']):
        replacement = parameter_summary(fm, allowed)
        body = body[:summary.start()] + replacement + body[summary.end():]
        summary_hash = fingerprint(replacement)
    else:
        summary_hash = previous.get('summary_sha256')
    if changes or body != parse(draft['document'])[1]:
        draft['document'] = '---\n' + yaml.safe_dump(fm, allow_unicode=True, sort_keys=False) + '---\n\n' + body.strip() + '\n'
    draft['completion'] = {'context': context, 'provenance': provenance, 'conflicts': conflicts,
        'stale_fields': stale, 'changes': changes,
        'missing_fields': sorted(key for key in allowed if key in schema and fm.get(key) in (None, '', [], {})),
        'inputs_sha256': fingerprint([draft['sources'], template]), 'summary_sha256': summary_hash}
    return changes
