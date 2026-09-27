const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const {JSDOM} = require('../.cache/ai-test/node_modules/jsdom');
const core = require('../docs/javascripts/ai-core.js');
const records = ['ct', 'irm', 'rx', 'eco', 'fluoro'].map(modality => ({
  title: `${modality} tiroidă`, modality, url: `${modality}/tiroida/`, category: 'gat',
  details: {position: 'Documentat'}, review: {medical: 'Nedocumentată', publication: 'Ciornă'},
  sources: [{title: 'Manual de referință'}]
}));
const read = file => fs.readFileSync('docs/javascripts/' + file, 'utf8');
const tick = () => new Promise(resolve => setTimeout(resolve, 5));
async function until(predicate) { for (let i = 0; i < 100; i++) { if (predicate()) return; await tick(); } throw Error('Timed out'); }
function setup({page = true, blockedStorage = false} = {}) {
  const dom = new JSDOM(page ? '<div id="ai-workspace-root"></div>' : '<main>Protocol</main>', {
    url: 'https://example.org/sub/ai/', runScripts: 'outside-only', pretendToBeVisual: true
  });
  const w = dom.window;
  Object.defineProperty(w.document, 'currentScript', {value: {src: 'https://example.org/sub/javascripts/ai-assistant.js'}});
  if (blockedStorage) Object.defineProperty(w, 'localStorage', {get() { throw Error('Denied'); }});
  w.IRIS = {situations: [], recommendations: []};
  const requests = [];
  w.fetch = async url => { requests.push(String(url)); return {ok: true, json: async () => ({protocols: records})}; };
  w.eval(read('ai-core.js')); w.eval(read('vendor/marked.umd.js')); w.eval(read('vendor/purify.min.js'));
  w.eval(read('ai-assistant.js'));
  w.document.dispatchEvent(new w.Event('DOMContentLoaded'));
  const find = selector => w.document.querySelector(selector);
  const submit = query => { find('textarea').value = query; find('form').dispatchEvent(new w.Event('submit', {cancelable: true})); };
  const choose = provider => { find('[data-control=provider]').value = provider; find('[data-control=provider]').dispatchEvent(new w.Event('change')); };
  return {dom, w, find, submit, choose, requests};
}

test('retrieval handles diacritics, each modality, no invented matches and safe links', () => {
  const catalog = core.prepareCatalog(records);
  for (const mode of ['ct', 'irm', 'rx', 'eco', 'fluoro']) {
    const found = core.retrieve('tiroida', mode, catalog, {}, 'https://example.org/sub/');
    assert.equal(found.length, 1); assert.equal(found[0].record.modality, mode);
  }
  assert.equal(core.retrieve('CT nonexistent', 'all', catalog, {}, 'https://example.org/').length, 0);
  assert.equal(core.safeLink('javascript:alert(1)', 'https://example.org/'), null);
  assert.equal(core.safeLink(null, 'https://example.org/'), null);
  const messages = core.messages('single question', [], Array.from({length: 10}, () => ({role: 'user', content: 'old'})));
  assert.equal(messages.length, 8);
  assert.equal(messages.filter(m => m.content.includes('single question')).length, 1);
  assert.ok(!JSON.stringify(core.evidence([{id: 'S1', record: {details: {}}, title: 't'}])).includes('120'));
});

test('local search is lazy, source aware, cached, works with blocked storage and subpaths', async () => {
  const t = setup({blockedStorage: true});
  try {
    assert.equal(t.requests.length, 0);
    assert.equal(t.find('#rad-ai-floating'), null);
    t.submit('CT tiroida');
    await until(() => !t.find('[data-action=send]').disabled);
    assert.match(t.find('.rad-ai-assistant').textContent, /Ciornă/);
    assert.equal(t.find('.rad-ai-sources a').href, 'https://example.org/sub/ct/tiroida/');
    t.submit('IRM tiroida'); await until(() => !t.find('[data-action=send]').disabled);
    assert.deepEqual(t.requests, ['https://example.org/sub/javascripts/ai-library.json']);
    assert.equal(t.find('script[src*="puter"]'), null);
  } finally { t.dom.window.close(); }
});

test('AI sanitizes generated HTML, submits once, and skips provider without evidence', async () => {
  const t = setup(); let calls = 0, sent;
  t.w.puter = {ai: {chat: async messages => { calls++; sent = messages; return '<img src=x onerror=alert(1)><script>alert(1)</script>**Rezultat** [link](javascript:alert(1))'; }}};
  try {
    t.choose('puter'); t.submit('CT tiroida'); t.submit('CT tiroida');
    await until(() => !t.find('[data-action=send]').disabled);
    assert.equal(calls, 1); assert.equal(t.w.document.querySelectorAll('.rad-ai-user').length, 1);
    assert.equal(t.find('.rad-ai-answer img'), null); assert.equal(t.find('.rad-ai-answer script'), null);
    assert.equal(t.find('.rad-ai-answer a[href^="javascript"]'), null);
    assert.equal(t.find('.rad-ai-assistant strong').textContent, 'Rezultat');
    assert.ok(sent.at(-1).content.includes('[S1]') || sent.at(-1).content.includes('"id":"S1"'));
    t.submit('CT nonexistent'); await until(() => !t.find('[data-action=send]').disabled);
    assert.equal(calls, 1);
  } finally { t.dom.window.close(); }
});

test('stop and clear prevent late provider output and retry does not duplicate the question', async () => {
  const t = setup(); let resolve, calls = 0;
  t.w.puter = {ai: {chat: () => { calls++; return new Promise(r => { resolve = r; }); }}};
  try {
    t.choose('puter'); t.submit('CT tiroida'); await until(() => calls === 1);
    t.find('[data-action=stop]').click(); await until(() => !t.find('[data-action=send]').disabled);
    assert.match(t.find('.rad-ai-assistant').textContent, /Afișare oprită/);
    resolve('late answer'); await tick(); assert.ok(!t.find('.rad-ai-thread').textContent.includes('late answer'));
    t.find('.rad-ai-assistant button').click(); await until(() => calls === 2);
    assert.equal(t.w.document.querySelectorAll('.rad-ai-user').length, 1);
    t.find('[data-action=clear]').click(); resolve('late again'); await tick();
    assert.equal(t.w.document.querySelectorAll('.rad-ai-message').length, 0);
  } finally { t.dom.window.close(); }
});

test('widget mounts on demand, close button closes it, and Escape returns focus', async () => {
  const t = setup({page: false});
  try {
    assert.equal(t.find('textarea'), null); assert.equal(t.requests.length, 0);
    t.find('.rad-ai-toggle').click(); assert.ok(t.find('textarea'));
    const closeBtn = t.find('.rad-ai-close-btn');
    assert.ok(closeBtn);
    assert.equal(closeBtn.getAttribute('aria-label'), 'Închide fereastra asistentului AI');
    assert.equal(closeBtn.dataset.action, 'close');

    // Test dedicated close button click
    closeBtn.click();
    assert.equal(t.find('#rad-ai-panel').hidden, true);
    assert.equal(t.w.document.activeElement, t.find('.rad-ai-toggle'));

    // Reopen and test Escape keydown
    t.find('.rad-ai-toggle').click();
    assert.equal(t.find('#rad-ai-panel').hidden, false);
    t.find('textarea').dispatchEvent(new t.w.KeyboardEvent('keydown', {key: 'Escape', bubbles: true}));
    assert.equal(t.find('#rad-ai-panel').hidden, true);
    assert.equal(t.w.document.activeElement, t.find('.rad-ai-toggle'));
  } finally { t.dom.window.close(); }
});

test('catalog fetch errors can be retried without a second user message', async () => {
  const t = setup(); let attempts = 0;
  t.w.fetch = async () => { if (++attempts === 1) throw Error('offline'); return {ok:true, json:async () => ({protocols: records})}; };
  try {
    t.submit('CT tiroida'); await until(() => !t.find('[data-action=send]').disabled);
    assert.match(t.find('.rad-ai-assistant').textContent, /indisponibil/);
    t.find('.rad-ai-assistant button').click(); await until(() => !t.find('[data-action=send]').disabled);
    assert.equal(attempts, 2); assert.ok(t.find('.rad-ai-sources'));
    assert.equal(t.w.document.querySelectorAll('.rad-ai-user').length, 1);
  } finally { t.dom.window.close(); }
});

test('streamed output stays inert and timeout returns controls', async () => {
  const t = setup(); const realTimeout = t.w.setTimeout.bind(t.w);
  t.w.setTimeout = (fn, delay, ...args) => realTimeout(fn, delay === 120000 ? 50 : delay, ...args);
  t.w.puter = {ai: {chat: async () => ({async *[Symbol.asyncIterator]() {
    yield {text: '<img src=x onerror=alert(1)>partial'};
    await new Promise(() => {});
  }})}};
  try {
    t.choose('puter'); t.submit('CT tiroida');
    await until(() => t.find('.rad-ai-assistant').textContent.includes('partial'));
    assert.equal(t.find('.rad-ai-answer img'), null);
    await until(() => !t.find('[data-action=send]').disabled);
    assert.match(t.find('.rad-ai-assistant').textContent, /Timpul de așteptare a expirat/);
  } finally { t.dom.window.close(); }
});

test('in-page context anchors to active protocol, renders contextual prompts, and grounds queries', async () => {
  const protocolRecord = {
    title: 'CT Colonografie Virtuală', modality: 'ct', url: 'ct/abdomen/ct-colon/', category: 'abdomen',
    details: {contrast: 'Fără contrast IV', position: 'Decubit dorsal și ventral'},
    review: {medical: 'Validat', publication: 'Publicat'}, sources: [{title: 'Dartmouth Protocol'}]
  };
  const dom = new JSDOM('<main><h1 id="ct-colon">CT Colonografie Virtuală</h1><p>Conținut protocol...</p></main>', {
    url: 'https://example.org/sub/ct/abdomen/ct-colon/', runScripts: 'outside-only', pretendToBeVisual: true
  });
  const w = dom.window;
  Object.defineProperty(w.document, 'currentScript', {value: {src: 'https://example.org/sub/javascripts/ai-assistant.js'}});
  w.IRIS = {situations: [], recommendations: []};
  let sentMessages = null;
  w.puter = {ai: {chat: async messages => { sentMessages = messages; return 'Răspuns despre colonografie.'; }}};
  w.fetch = async () => ({ok: true, json: async () => ({protocols: [protocolRecord, ...records]})});
  w.eval(read('ai-core.js')); w.eval(read('vendor/marked.umd.js')); w.eval(read('vendor/purify.min.js'));
  w.eval(read('ai-assistant.js'));
  w.document.dispatchEvent(new w.Event('DOMContentLoaded'));
  const find = selector => w.document.querySelector(selector);
  try {
    find('.rad-ai-toggle').click();
    await until(() => find('[data-slot=context-banner]'));
    assert.equal(find('[data-slot=context-banner]').hidden, false);
    assert.equal(find('[data-slot=context-title]').textContent, 'CT Colonografie Virtuală');

    const prompts = Array.from(w.document.querySelectorAll('[data-slot=prompts] button')).map(b => b.textContent);
    assert.ok(prompts.some(p => p.includes('Rezumat')));
    assert.ok(prompts.some(p => p.includes('Contrast')));

    find('[data-control=provider]').value = 'puter';
    find('[data-control=provider]').dispatchEvent(new w.Event('change'));
    find('textarea').value = 'ce contraindicatii are?';
    find('form').dispatchEvent(new w.Event('submit', {cancelable: true}));

    await until(() => !find('[data-action=send]').disabled);
    assert.ok(sentMessages, 'Provider should have been called due to active in-page context');
    const userPrompt = sentMessages.at(-1).content;
    assert.ok(userPrompt.includes('CT Colonografie Virtuală'));
    assert.ok(userPrompt.includes('Decubit dorsal și ventral'));

    find('[data-control=context-active]').click();
    find('[data-control=context-active]').dispatchEvent(new w.Event('change'));
    const defaultPrompts = Array.from(w.document.querySelectorAll('[data-slot=prompts] button')).map(b => b.textContent);
    assert.ok(defaultPrompts.includes('CT abdomen'));
  } finally { dom.window.close(); }
});

test('clinical query expansion maps acronyms and pathology to relevant protocols and IRIS situations', () => {
  const clinicalRecords = [
    { title: 'CT Angiografie Pulmonară (Protocol TEP)', modality: 'ct', url: 'ct/pulmonar/cta-tep/', category: 'torace', indications: ['trombembolism pulmonar', 'dispnee acuta'], details: {}, review: {}, sources: [] },
    { title: 'IRM Cerebral Difuzie (DWI - Stroke)', modality: 'irm', url: 'irm/neuro/dwi-stroke/', category: 'neuro', indications: ['ischemie cerebrala acuta', 'deficit neurologic'], details: {}, review: {}, sources: [] },
    { title: 'Ecografie Abdominală (Apendicită Acută)', modality: 'eco', url: 'eco/abdomen/apendicita/', category: 'abdomen', indications: ['durere fosa iliaca dreapta', 'febra'], details: {}, review: {}, sources: [] },
    { title: 'CT Renal Nativ (Colică Renală / Litiază KUB)', modality: 'ct', url: 'ct/urinar/kub-litiaza/', category: 'urinar', indications: ['colica nefretica', 'calcul renal'], details: {}, review: {}, sources: [] }
  ];
  const catalog = core.prepareCatalog(clinicalRecords);
  const iris = {
    situations: [
      { id: 'sit-1', name: 'Suspiciune de trombembolism pulmonar (TEP)', placeholder: false },
      { id: 'sit-2', name: 'Accident vascular cerebral acut în fereastră terapeutică', placeholder: false }
    ],
    recommendations: []
  };

  const tepMatches = core.retrieve('ce protocol aplic la TEP?', 'all', catalog, iris, 'https://example.org/');
  assert.ok(tepMatches.length >= 1);
  assert.equal(tepMatches[0].title, 'CT Angiografie Pulmonară (Protocol TEP)');

  const avcMatches = core.retrieve('suspiciune AVC ischemic acut', 'all', catalog, iris, 'https://example.org/');
  assert.ok(avcMatches.length >= 1);
  assert.equal(avcMatches[0].title, 'IRM Cerebral Difuzie (DWI - Stroke)');

  const fidMatches = core.retrieve('pacient cu durere acuta in FID', 'all', catalog, iris, 'https://example.org/');
  assert.ok(fidMatches.length >= 1);
  assert.equal(fidMatches[0].title, 'Ecografie Abdominală (Apendicită Acută)');

  const colicMatches = core.retrieve('investigatie pentru colica nefretica', 'all', catalog, iris, 'https://example.org/');
  assert.ok(colicMatches.length >= 1);
  assert.equal(colicMatches[0].title, 'CT Renal Nativ (Colică Renală / Litiază KUB)');
});

test('guideline fallback button consults international standards and quick tools populate queries', async () => {
  const t = setup();
  let calls = 0, sentMessages = null;
  t.w.puter = {ai: {chat: async messages => { calls++; sentMessages = messages; return 'Recomandare conform ACR / ESUR.'; }}};
  try {
    t.choose('puter');
    
    // Quick tool click: report template
    const reportBtn = t.find('[data-tool=report]');
    assert.ok(reportBtn);
    reportBtn.click();
    assert.ok(t.find('textarea').value.includes('șablon') || t.find('textarea').value.includes('buletin'));

    // Search nonexistent query -> zero matches in catalog
    t.submit('boala rara nespecificata');
    await until(() => !t.find('[data-action=send]').disabled);
    assert.equal(calls, 0, 'Should not auto-call provider without evidence');
    
    // Guideline fallback button must be available
    const fallbackBtn = t.find('.rad-ai-guideline-button');
    assert.ok(fallbackBtn, 'Fallback button to international guidelines should be rendered');
    assert.match(fallbackBtn.textContent, /Ghidurile Internaționale/);

    // Click fallback button -> calls Puter with international guidelines
    fallbackBtn.click();
    await until(() => !t.find('[data-action=send]').disabled && calls === 1);
    assert.equal(calls, 1);
    assert.ok(sentMessages);
    assert.ok(sentMessages[0].content.includes('ACR') || sentMessages[0].content.includes('ESUR'));
    assert.match(t.find('.rad-ai-assistant').textContent, /Recomandare conform ACR/);
  } finally { t.dom.window.close(); }
});

test('puter authentication lifecycle: detects session, displays connected badge and handles sign out', async () => {
  const t = setup();
  let isSignedIn = false;
  let signInCalled = false;
  let signOutCalled = false;

  t.w.puter = {
    ai: {
      chat: async () => 'ok'
    },
    auth: {
      isSignedIn: () => isSignedIn,
      getUser: async () => ({ username: 'dr_radiolog' }),
      signIn: async () => { signInCalled = true; isSignedIn = true; },
      signOut: async () => { signOutCalled = true; isSignedIn = false; }
    }
  };

  try {
    t.choose('puter');
    const authZone = t.find('[data-slot=auth-zone]');
    assert.ok(authZone);

    // Initial state: not signed in
    const connectBtn = authZone.querySelector('[data-action=connect]');
    assert.ok(connectBtn, 'Should show connect button when not signed in');
    assert.match(connectBtn.textContent, /Conectează/);

    // Click connect
    connectBtn.click();
    await until(() => authZone.querySelector('.rad-ai-auth-badge') !== null);

    assert.ok(signInCalled, 'signIn should have been called');
    const badge = authZone.querySelector('.rad-ai-auth-badge');
    assert.ok(badge);
    assert.match(badge.textContent, /@dr_radiolog/);
    assert.match(badge.textContent, /Conectat/);
    assert.match(t.find('[data-slot=notice]').textContent, /@dr_radiolog/);

    // Click disconnect
    const disconnectBtn = authZone.querySelector('[data-action=disconnect]');
    assert.ok(disconnectBtn, 'Should show disconnect button when signed in');
    disconnectBtn.click();
    await until(() => authZone.querySelector('[data-action=connect]') !== null);

    assert.ok(signOutCalled, 'signOut should have been called');
    assert.equal(authZone.querySelector('.rad-ai-auth-badge'), null);
    assert.ok(authZone.querySelector('[data-action=connect]'));
  } finally { t.dom.window.close(); }
});



