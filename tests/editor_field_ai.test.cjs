// Run with Node and jsdom on NODE_PATH. No browser or provider requests.
const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const {JSDOM} = require('jsdom');
const code = fs.readFileSync(path.join(__dirname, '../scripts/static/editor-field-ai.js'), 'utf8');

function fixture() {
  const dom = new JSDOM(`<select id="field-ai-provider"><option value="auto">Auto</option><option value="codex_oauth">ChatGPT OAuth</option><option value="gemini_oauth">Gemini OAuth</option></select>
    <button id="field-ai-connect">Connect</button><button id="field-ai-check">Check</button><p id="field-ai-connection"></p>
    <form id="proto-form"><input name="title" value="Synthetic protocol"><input name="modality" type="hidden" value="rx">
      <select name="category"><option value="torace">Torace</option></select>
      <section class="section"><h2>Poziționare</h2><div><label for="position">Poziție</label><textarea id="position" name="position">Before</textarea></div>
      <div><label for="centering">Centrare</label><input id="centering" name="centering" value="Unchanged"></div>
      <input name="slug" readonly value="fixture"><input name="author" value="Private author">
      <div id="rows"></div></section></form>`, {url: 'http://localhost:5173', runScripts: 'outside-only'});
  const win = dom.window;
  win.HTMLElement.prototype.getClientRects = function () { return this.isConnected ? [{}] : []; };
  win.HTMLDialogElement.prototype.showModal = function () { this.open = true; };
  win.HTMLDialogElement.prototype.close = function () { this.open = false; };
  const requests = [];
  win.fetch = (url, options) => new Promise(resolve => requests.push({url, options, resolve}));
  win.eval(code);
  const doc = win.document;
  return {dom, win, doc, requests,
    click: id => doc.getElementById(id).nextElementSibling.click(),
    tick: () => new Promise(resolve => setImmediate(resolve)),
    answer: data => requests.at(-1).resolve({ok: true, json: async () => ({status: 'supported', suggestion: 'Synthetic proposal',
      explanation: 'Fixture explanation', limitations: [], sources: [{url: 'https://acr.org/fixture', title: 'Fixture'}],
      engine: 'fixture', searched_at: '2026-09-15T12:00:00Z', ...data})}),
    review() { const checkbox = doc.querySelector('[data-slot=review]'); checkbox.checked = true; checkbox.dispatchEvent(new win.Event('change')); },
    apply: () => doc.querySelector('[data-action=apply]').click()};
}

test('each editable field gets one button; applying changes only the target after review', async () => {
  const f = fixture();
  try {
    const inputs = f.doc.querySelectorAll('input:not([type=hidden]):not([readonly]),textarea,select');
    for (const input of inputs) {
      if (!input.closest('#proto-form')) continue;
      assert.equal(input.nextElementSibling.className, 'field-ai-button');
    }
    f.click('position');
    const request = JSON.parse(f.requests[0].options.body);
    assert.equal(request.field.label, 'Poziție');
    assert.ok(!request.context.some(x => x.name === 'author'));
    let inputEvents = 0;
    f.doc.getElementById('position').addEventListener('input', () => inputEvents++);
    f.answer(); await f.tick();
    f.apply(); assert.equal(f.doc.getElementById('position').value, 'Before');
    f.review(); f.apply();
    assert.equal(f.doc.getElementById('position').value, 'Synthetic proposal');
    assert.equal(f.doc.getElementById('centering').value, 'Unchanged');
    assert.equal(inputEvents, 1);
    assert.equal(f.requests.length, 1); // No implicit save.
  } finally { f.dom.window.close(); }
});

test('dynamic rows get independent buttons and row context without duplicates', async () => {
  const f = fixture();
  try {
    f.doc.getElementById('rows').innerHTML = '<div class="dynamic-row"><div><label>Name</label><input data-field="name" value="Axial fixture"></div><div><label>Thickness</label><input id="thickness" data-field="thickness" value="Before"></div></div>';
    await f.tick(); await f.tick();
    assert.equal(f.doc.querySelectorAll('.dynamic-row .field-ai-button').length, 2);
    f.click('thickness');
    const data = JSON.parse(f.requests[0].options.body);
    assert.equal(data.field.name, 'thickness');
    assert.equal(data.field.row[0].value, 'Axial fixture');
    f.answer(); await f.tick(); f.review(); f.apply();
    assert.equal(f.doc.getElementById('thickness').value, 'Synthetic proposal');
  } finally { f.dom.window.close(); }
});

test('edits made during research prevent stale overwrite', async () => {
  const f = fixture();
  try {
    f.click('position');
    f.doc.getElementById('position').value = 'New manual edit';
    f.answer(); await f.tick(); f.review(); f.apply();
    assert.equal(f.doc.getElementById('position').value, 'New manual edit');
    assert.match(f.doc.querySelector('[data-slot=status]').textContent, /s-a schimbat/);
  } finally { f.dom.window.close(); }
});

test('changing modality or deleting target prevents application', async () => {
  for (const change of [f => {f.doc.querySelector('[name=modality]').value = 'ct';}, f => f.doc.getElementById('position').remove()]) {
    const f = fixture();
    try {
      f.click('position'); f.answer(); await f.tick(); change(f); f.review(); f.apply();
      assert.match(f.doc.querySelector('[data-slot=status]').textContent, /s-a schimbat/);
    } finally { f.dom.window.close(); }
  }
});

test('unsupported result cannot apply; generated HTML is rendered as text', async () => {
  const f = fixture();
  try {
    f.click('position');
    f.answer({status: 'insufficient', suggestion: '', explanation: '<img src=x onerror=alert(1)>', sources: [{url: 'javascript:alert(1)', title: 'bad'}]});
    await f.tick();
    assert.equal(f.doc.querySelector('[data-slot=explanation] img'), null);
    assert.equal(f.doc.querySelector('[data-slot=sources] a'), null);
    assert.equal(f.doc.querySelector('[data-action=apply]').disabled, true);
    assert.equal(f.doc.getElementById('position').value, 'Before');
  } finally { f.dom.window.close(); }
});

test('older response never replaces a newer field result', async () => {
  const f = fixture();
  try {
    f.click('position');
    const first = f.requests[0];
    f.doc.querySelector('[data-action=close]').click();
    f.click('centering');
    f.answer({suggestion: 'Second proposal'}); await f.tick();
    first.resolve({ok: true, json: async () => ({suggestion: 'Stale'})}); await f.tick();
    assert.equal(f.doc.querySelector('[data-slot=suggestion]').textContent, 'Second proposal');
    f.review(); f.apply();
    assert.equal(f.doc.getElementById('centering').value, 'Second proposal');
    assert.equal(f.doc.getElementById('position').value, 'Before');
  } finally { f.dom.window.close(); }
});

test('OAuth controls require explicit provider and show server result without modifying form', async () => {
  const f = fixture();
  try {
    f.doc.getElementById('field-ai-check').click();
    assert.equal(f.requests.length, 0);
    f.doc.getElementById('field-ai-provider').value = 'codex_oauth';
    f.doc.getElementById('field-ai-check').click();
    assert.equal(f.requests[0].url, '/api/ai/cli-check');
    assert.deepEqual(JSON.parse(f.requests[0].options.body), {provider: 'codex_oauth'});
    f.requests[0].resolve({ok: true, json: async () => ({message: 'Connected fixture'})});
    await f.tick();
    assert.equal(f.doc.getElementById('field-ai-connection').textContent, 'Connected fixture');
    assert.equal(f.doc.getElementById('position').value, 'Before');
  } finally { f.dom.window.close(); }
});
