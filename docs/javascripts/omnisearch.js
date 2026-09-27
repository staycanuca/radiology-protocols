/* Accessible catalog search; no provider calls and no persistent query history. */
(function () {
  'use strict';
  const core = window.ProtocolSearch;
  if (!core) return;
  const base = new URL('../', document.currentScript.src).href;
  const MODALITIES = {all: 'Toate', ct: 'CT', irm: 'IRM', rx: 'RX', eco: 'US / Eco', fluoro: 'Fluoro', mn: 'Med. Nucleară', ir: 'Intervențional'};
  const CONTRAST = {all: 'Orice informație despre contrast', contrast: 'Contrast declarat', native: 'Fără contrast declarat', variable: 'Variabil / opțional', unknown: 'Neprecizat'};
  const defaults = () => ({q: '', modality: 'all', region: 'all', segment: 'all', contrast: 'all', source: 'all'});
  let loading, catalog, current;
  function el(tag, cls, text) {
    const node = document.createElement(tag); if (cls) node.className = cls;
    if (text !== undefined) node.textContent = text; return node;
  }
  async function load() {
    if (!loading) loading = (async () => {
      const response = await fetch(new URL('javascripts/omnisearch-index.json', base), {signal: AbortSignal.timeout(20000)});
      if (!response.ok) throw new Error('Catalog unavailable');
      const data = await response.json();
      if (data.schema_version !== 2 || !Array.isArray(data.protocols)) throw new Error('Catalog version mismatch');
      catalog = {...data, protocols: core.prepare(data.protocols).filter(r => core.safeUrl(r.url, base))};
      return catalog;
    })().catch(error => { loading = null; throw error; });
    return loading;
  }
  function fromUrl() {
    const state = defaults(), params = new URL(location.href).searchParams;
    for (const key of Object.keys(state)) state[key] = (params.get('omni_' + key) || state[key]).slice(0, 400);
    if (!MODALITIES[state.modality]) state.modality = 'all';
    if (!CONTRAST[state.contrast]) state.contrast = 'all';
    return state;
  }
  function saveUrl(state) {
    const url = new URL(location.href), initial = defaults();
    for (const [key, value] of Object.entries(state)) {
      if (value === initial[key]) url.searchParams.delete('omni_' + key);
      else url.searchParams.set('omni_' + key, value);
    }
    try { history.replaceState(history.state, '', url); } catch (_) {}
  }
  function init() {
    if (current && !current.root.isConnected) clearTimeout(current.timer);
    const root = document.getElementById('omnisearch-root');
    if (!root || root.dataset.omniMounted) return;
    root.dataset.omniMounted = 'true';
    const view = {root, state: fromUrl(), limit: 24, timer: null}; current = view;
    root.innerHTML = `<div class="omni-container">
      <form class="omni-search-form" role="search" aria-label="Căutare în protocoale"><label for="omnisearch-input">Caută în biblioteca de protocoale</label>
      <div class="omni-search-wrapper"><span aria-hidden="true">⌕</span><input id="omnisearch-input" class="omni-search-input" type="search" maxlength="400" autocomplete="off" placeholder="Ex.: RX cot Clark, RMN genunchi, CT abdomen Dartmouth" aria-describedby="omni-help"><button type="button" id="omnisearch-clear" class="omni-search-clear" aria-label="Șterge textul">×</button></div></form>
      <p id="omni-help" class="omni-help">Caută după examinare, regiune, indicație, aparat sau sursă. Sunt acceptate cuvinte cu și fără diacritice.</p>
      <div class="omni-chips-row" role="group" aria-label="Modalitate" data-slot="modalities"></div>
      <div class="omni-filters"><label>Regiune<select data-filter="region"></select></label><label>Subgrupă din catalog<select data-filter="segment"></select></label><label>Contrast<select data-filter="contrast"></select></label><label>Sursă declarată<select data-filter="source"></select></label></div>
      <div class="omni-status-bar"><span id="omnisearch-count-badge" role="status" aria-live="polite">Se încarcă biblioteca…</span><button type="button" class="omni-btn-reset" data-action="reset">Resetează filtrele</button></div>
      <div id="omnisearch-results" aria-busy="true"></div>
      <p class="omni-help">Potrivirile indică documente din bibliotecă, nu confirmă indicația clinică sau validarea protocolului. Contrastul este afișat numai conform metadatelor declarate.</p>
    </div>`;
    const find = selector => root.querySelector(selector);
    view.input = find('input'); view.results = find('#omnisearch-results'); view.status = find('[role=status]');
    view.input.value = view.state.q;
    for (const [value, label] of Object.entries(MODALITIES)) {
      const button = el('button', 'omni-chip omni-mod-chip', label); button.type = 'button'; button.dataset.mod = value;
      button.addEventListener('click', () => { clearTimeout(view.timer); view.state.q = view.input.value.trim(); view.state.modality = value; view.state.segment = 'all'; view.limit = 24; render(view); saveUrl(view.state); });
      find('[data-slot=modalities]').append(button);
    }
    const updateQuery = () => { clearTimeout(view.timer); if (!root.isConnected) return; view.state.q = view.input.value.trim(); view.limit = 24; render(view); saveUrl(view.state); };
    view.input.addEventListener('input', () => { clearTimeout(view.timer); view.timer = setTimeout(updateQuery, 120); });
    find('form').addEventListener('submit', event => { event.preventDefault(); updateQuery(); });
    find('#omnisearch-clear').addEventListener('click', () => { view.input.value = ''; updateQuery(); view.input.focus(); });
    find('[data-action=reset]').addEventListener('click', () => {
      clearTimeout(view.timer); view.state = defaults(); view.input.value = ''; view.limit = 24; render(view); saveUrl(view.state); view.input.focus();
    });
    for (const select of root.querySelectorAll('[data-filter]')) select.addEventListener('change', () => {
      clearTimeout(view.timer); view.state.q = view.input.value.trim(); view.state[select.dataset.filter] = select.value;
      if (select.dataset.filter === 'region') view.state.segment = 'all';
      view.limit = 24; render(view); saveUrl(view.state);
    });
    view.retry = async () => {
      view.status.textContent = 'Se încarcă biblioteca…'; view.results.setAttribute('aria-busy', 'true');
      view.results.replaceChildren();
      try { await load(); if (root.isConnected) render(view); }
      catch (_) {
        if (!root.isConnected) return;
        view.status.textContent = 'Biblioteca nu a putut fi încărcată. Verifică conexiunea și reîncearcă.';
        view.results.setAttribute('aria-busy', 'false');
        const retry = el('button', 'omni-btn-reset', 'Reîncearcă încărcarea'); retry.type = 'button';
        retry.addEventListener('click', view.retry); view.results.replaceChildren(retry);
      }
    };
    view.retry();
  }
  function options(view, key, choices, placeholder) {
    const select = view.root.querySelector('[data-filter=' + key + ']');
    const values = [[ 'all', placeholder ], ...choices];
    if (!values.some(([value]) => value === view.state[key])) view.state[key] = 'all';
    select.replaceChildren(...values.map(([value, label]) => new Option(label, value)));
    select.value = view.state[key]; select.disabled = choices.length === 0;
  }
  function render(view, focusIndex = null) {
    if (!catalog || !view.root.isConnected) return;
    const records = catalog.protocols, state = view.state;
    const unique = values => [...new Set(values.filter(Boolean))].sort((a,b) => a.localeCompare(b,'ro')).map(v => [v, v]);
    options(view, 'region', Object.entries(catalog.regions).filter(([key]) => records.some(r => r.region === key)), 'Toate regiunile');
    const scoped = records.filter(r => (state.modality === 'all' || r.modality === state.modality) && (state.region === 'all' || r.region === state.region));
    options(view, 'segment', unique(scoped.map(r => r.segment)), 'Toate subgrupele');
    options(view, 'source', unique(records.flatMap(r => r.source_filters || [])), 'Toate sursele');
    options(view, 'contrast', Object.entries(CONTRAST).filter(([key]) => key !== 'all'), CONTRAST.all);
    const matches = core.search(records, state);
    const facets = core.search(records, state, 'modality');
    for (const button of view.root.querySelectorAll('[data-mod]')) {
      const key = button.dataset.mod, count = key === 'all' ? facets.length : facets.filter(r => r.modality === key).length;
      button.textContent = MODALITIES[key] + ' (' + count + ')';
      button.classList.toggle('active', state.modality === key); button.setAttribute('aria-pressed', String(state.modality === key));
    }
    view.root.querySelector('#omnisearch-clear').hidden = !view.input.value;
    view.results.setAttribute('aria-busy', 'false');
    view.status.textContent = `${matches.length.toLocaleString('ro-RO')} protocoale găsite · afișate ${Math.min(view.limit, matches.length)}`;
    view.results.replaceChildren();
    const filtering = Object.entries(state).some(([key, value]) => value !== defaults()[key]);
    if (!filtering) {
      view.status.textContent = `${records.length.toLocaleString('ro-RO')} protocoale în bibliotecă`;
      view.results.append(el('p', 'omni-idle-banner', 'Introdu termenii căutați sau alege un filtru. Indexul reflectă paginile incluse în această versiune a site-ului.'));
      return;
    }
    if (!matches.length) {
      view.results.append(el('p', 'omni-empty-state', 'Niciun protocol pentru combinația selectată. Elimină un filtru sau încearcă denumirea examinării, regiunii ori sursei.'));
      return;
    }
    const grid = el('div', 'omni-cards-grid');
    for (const record of matches.slice(0, view.limit)) {
      const card = el('a', 'omni-card'); card.href = core.safeUrl(record.url, base);
      const badges = el('div', 'omni-card-header');
      badges.append(el('span', 'omni-badge omni-badge-mod', MODALITIES[record.modality]), el('span', 'omni-badge', catalog.regions[record.region] || record.category_label),
        el('span', 'omni-badge', CONTRAST[record.contrast] || CONTRAST.unknown));
      card.append(badges, el('h3', 'omni-card-title', record.title));
      if (record.segment) card.append(el('p', 'omni-card-segment', record.segment));
      const words = core.tokens(state.q);
      const indication = (record.indications || []).find(text => words.some(w => core.normalize(text).includes(w))) || record.indications?.[0];
      if (indication) card.append(el('p', 'omni-card-indications', indication));
      card.append(el('p', 'omni-card-source', record.sources.length ? 'Surse: ' + record.sources.join(' · ') : 'Sursa exactă nu este precizată'));
      card.append(el('p', 'omni-card-review', [record.publication, 'Revizuire medicală: ' + record.medical_review].filter(Boolean).join(' · ')));
      card.append(el('span', 'omni-card-action', 'Deschide protocolul →')); grid.append(card);
    }
    view.results.append(grid);
    if (focusIndex !== null) grid.children[focusIndex]?.focus();
    if (matches.length > view.limit) {
      const more = el('button', 'omni-load-more-btn', `Afișează încă ${Math.min(24, matches.length - view.limit)} (rămase: ${matches.length - view.limit})`); more.type = 'button';
      more.addEventListener('click', () => { const previous = view.limit; view.limit += 24; render(view, previous); }); view.results.append(more);
    }
  }
  addEventListener('popstate', () => { if (current?.root.isConnected) { clearTimeout(current.timer); current.state = fromUrl(); current.input.value = current.state.q; current.limit = 24; render(current); } });
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  if (window.document$) window.document$.subscribe(init);
})();
