/* Exercise the actual Material worker shipped in site/, with no browser or network. */
const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const core = require('../docs/javascripts/search-core.js');

const indexFile = path.resolve('site/search/search_index.json');
test('built Omnisearch and native Material search resolve current catalog queries', {skip: !fs.existsSync(indexFile), timeout:120000}, async () => {
  const data = JSON.parse(fs.readFileSync('site/javascripts/omnisearch-index.json', 'utf8'));
  const records = core.prepare(data.protocols), byUrl = new Map(records.map(r => [r.url, r]));
  const workerDir = path.resolve('site/assets/javascripts/workers');
  const homepage = fs.readFileSync('site/index.html','utf8');
  const configMatch = homepage.match(/<script\b[^>]*\bid=(?:"__config"|'__config'|__config)[^>]*>([\s\S]*?)<\/script>/);
  assert.ok(configMatch, 'Material configuration must exist');
  const worker = path.resolve('site', JSON.parse(configMatch[1]).search);
  assert.match(worker,/protocol-search\.[a-f0-9]+\.js$/);
  const listeners = []; let response;
  const context = vm.createContext({console, URL, setTimeout, clearTimeout});
  context.self = context;
  context.addEventListener = (type, fn) => { if (type === 'message') listeners.push(fn); };
  context.postMessage = value => { response = value; };
  context.importScripts = (...urls) => { for (const url of urls) vm.runInContext(fs.readFileSync(path.resolve(workerDir, url), 'utf8'), context); };
  vm.runInContext(fs.readFileSync(worker, 'utf8'), context);
  const listener = async event => { for (const fn of listeners) await fn(event); };
  const native = JSON.parse(fs.readFileSync(indexFile, 'utf8'));
  await listener({data: {type:0, data:{...native, options:{suggest:true}}}});
  assert.equal(response.type,1);
  const cases = [
    ['rx cot clark', r => r.modality === 'rx' && /cot/i.test(r.title) && r.source_filters.includes('Clark')],
    ['RMN genunchi', r => r.modality === 'irm' && /genunchi/i.test(r.title)],
    ['mana PA', r => r.modality === 'rx' && /mana/i.test(core.normalize(r.title))],
    ['Dartmouth', r => /Dartmouth/i.test(r.title)],
    ['Merrill umar', r => /umar/i.test(core.normalize(r.title)) && r.source_filters.includes('Merrill')],
    ['ecografie tiroida', r => r.modality === 'eco' && /tiroid/i.test(r.title)],
    ['coloana cervicala', r => /cervical/i.test(r.title)],
  ];
  const report = [];
  for (const [query, expected] of cases) {
    const omni = core.search(records,{q:query}).slice(0,5);
    await listener({data:{type:2,data:query}});
    const groups = response.data.items.slice(0,5);
    const nativeRecords = groups.map(group => byUrl.get(group[0].location.split('#')[0])).filter(Boolean);
    report.push({query, omni:omni.map(r=>r.title), native:groups.map(g=>g[0].title),
      omni_pass:omni.some(expected), native_pass:nativeRecords.some(expected),
      native_first_pass: Boolean(nativeRecords[0] && expected(nativeRecords[0]))});
  }
  fs.writeFileSync('reports/search-relevance-validation.json', JSON.stringify({protocols:records.length,native_entries:native.docs.length,queries:report},null,2)+'\n');
  for (const row of report) {
    assert.ok(row.omni_pass, 'Omnisearch: '+row.query+' => '+row.omni.join('; '));
    assert.ok(row.native_pass, 'Native: '+row.query+' => '+row.native.join('; '));
    if (['RMN genunchi','ecografie tiroida','mana PA'].includes(row.query)) assert.ok(row.native_first_pass,'First result: '+row.query);
  }
  assert.ok(!native.docs.some(d=>d.location.endsWith('#protocol-provenance-title')));
  for (const r of records) assert.ok(fs.existsSync(path.join('site',r.url,'index.html')),r.url);
});
