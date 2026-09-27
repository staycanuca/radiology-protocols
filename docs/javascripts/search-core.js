/* Pure ranking and filtering. All indexed terms come from the current catalog. */
(function (root) {
  'use strict';
  const normalize = value => String(value || '').normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  const tokens = value => [...new Set(normalize(value).match(/[a-z0-9]+/g) || [])];
  const STOP = new Set('de si cu la pentru din pe in un o protocol protocoale cauta arata'.split(' '));
  function prepare(records) {
    return records.map(record => {
      const field = values => tokens((Array.isArray(values) ? values.flat(Infinity) : [values]).join(' '));
      return {...record, _title: field(record.title), _titleAlias: field(record.title_aliases || []), _name: normalize(record.title),
        _meta: field([record.modality, record.category_label, record.segment, ...(record.equipment || []), ...(record.synonyms || []), ...(record.sources || []), ...(record.source_terms || [])]),
        _alias: field(record.aliases || []), _body: field(record.indications || [])};
    });
  }
  function match(word, terms) { return terms.some(t => t === word || (word.length >= 3 && t.startsWith(word))); }
  function score(record, query) {
    const words = tokens(query).filter(w => !STOP.has(w));
    if (!words.length) return 0;
    let total = 0;
    for (const word of words) {
      if (record._title.includes(word)) total += 18;
      else if (match(word, record._title)) total += 12;
      else if (match(word, record._titleAlias)) total += 10;
      else if (match(word, record._meta)) total += 8;
      else if (match(word, record._alias)) total += 6;
      else if (match(word, record._body)) total += 2;
      else return -1;
    }
    if (record._name.includes(normalize(query).trim())) total += 25;
    return total;
  }
  function search(records, state = {}, ignore = '') {
    const result = [];
    for (const record of records) {
      if (ignore !== 'modality' && state.modality && state.modality !== 'all' && record.modality !== state.modality) continue;
      if (ignore !== 'region' && state.region && state.region !== 'all' && record.region !== state.region) continue;
      if (ignore !== 'segment' && state.segment && state.segment !== 'all' && record.segment !== state.segment) continue;
      if (ignore !== 'contrast' && state.contrast && state.contrast !== 'all' && record.contrast !== state.contrast) continue;
      if (ignore !== 'source' && state.source && state.source !== 'all' && !(record.source_filters || []).includes(state.source)) continue;
      const rank = score(record, state.q || '');
      if (rank >= 0) result.push({record, rank});
    }
    return result.sort((a, b) => b.rank - a.rank || a.record.title.localeCompare(b.record.title, 'ro') || a.record.url.localeCompare(b.record.url)).map(r => r.record);
  }
  function safeUrl(value, base) {
    if (typeof value !== 'string' || !value) return null;
    try { const u = new URL(value, base), b = new URL(base); return u.origin === b.origin && u.pathname.startsWith(b.pathname) && ['https:', 'http:'].includes(u.protocol) ? u.href : null; }
    catch (_) { return null; }
  }
  const api = {normalize, tokens, prepare, score, search, safeUrl};
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
  else root.ProtocolSearch = api;
})(typeof window !== 'undefined' ? window : globalThis);
