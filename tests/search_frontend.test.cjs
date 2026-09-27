const {test} = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const {JSDOM} = require('../.cache/ai-test/node_modules/jsdom');
const core = require('../docs/javascripts/search-core.js');
const record = (title, extra = {}) => ({title, url:'rx/cot/'+encodeURIComponent(title)+'/', modality:'rx', region:'upper', segment:'Cot', contrast:'unknown', indications:[], sources:[], source_filters:[], medical_review:'Nedocumentată', aliases:['radiografie'], ...extra});
const records = [record('Rx Cot PA', {sources:['Clark'], source_filters:['Clark'], aliases:['radiografie','clarck']}),
  record('Rx Umăr', {indications:['cot']}), record('IRM Genunchi', {modality:'irm',region:'msk',segment:'',aliases:['rmn','mri'],contrast:'native'})];
const tick = () => new Promise(r => setTimeout(r, 5));
async function until(f) { for(let i=0;i<100;i++){if(f())return;await tick();}throw Error('Timed out'); }
function setup(url = 'https://example.org/sub/?untouched=1', data = records, options = {}) {
  const dom = new JSDOM(options.noRoot ? '<main>Protocol</main>' : '<div id="omnisearch-root"></div>', {url,runScripts:'outside-only'}), w = dom.window;
  Object.defineProperty(w.document,'currentScript',{value:{src:'https://example.org/sub/javascripts/omnisearch.js'}});
  let fetches = 0, subscriber;
  w.fetch = async url => { fetches++; if (options.failOnce && fetches === 1) throw Error('offline'); assert.equal(String(url),'https://example.org/sub/javascripts/omnisearch-index.json');return {ok:true,json:async()=>({schema_version:2,regions:{upper:'Membru superior',msk:'MSK'},protocols:data})};};
  w.document$ = {subscribe: fn => {subscriber = fn; fn();}};
  w.eval(fs.readFileSync('docs/javascripts/search-core.js','utf8'));
  w.eval(fs.readFileSync('docs/javascripts/omnisearch.js','utf8'));
  w.document.dispatchEvent(new w.Event('DOMContentLoaded'));
  const find = s => w.document.querySelector(s);
  const query = q => {find('input').value=q;find('form').dispatchEvent(new w.Event('submit',{cancelable:true}));};
  const choose = (key,value) => {const node=find('[data-filter='+key+']');node.value=value;node.dispatchEvent(new w.Event('change'));};
  return {dom,w,find,query,choose,get fetches(){return fetches;},init:()=>subscriber()};
}

test('ranking favors title over incidental body; aliases, diacritics, filters are exact',()=>{
  const prepared=core.prepare([...records,record('Rx Mână PA')]);
  assert.equal(core.search(prepared,{q:'cot'})[0].title,'Rx Cot PA');
  assert.equal(core.search(prepared,{q:'rx cot clarck'}).length,1);
  assert.equal(core.search(prepared,{q:'RMN genunchi'})[0].modality,'irm');
  assert.equal(core.search(prepared,{q:'mana pa'})[0].title,'Rx Mână PA');
  assert.equal(core.search(prepared,{q:'CT nonexistent'}).length,0);
  assert.equal(core.search(prepared,{contrast:'native'}).length,1);
  assert.equal(core.search(prepared,{modality:'ct',q:'cot'}).length,0);
  assert.equal(core.safeUrl('javascript:alert(1)','https://example.org/sub/'),null);
  assert.equal(core.safeUrl('../outside/','https://example.org/sub/'),null);
});

test('UI has one fetch, safe cards, shareable query and accurate filter reset',async()=>{
  const t=setup();try{
    await until(()=>t.find('[aria-busy]').getAttribute('aria-busy')==='false');
    t.init();assert.equal(t.fetches,1);
    t.query('cot');assert.equal(t.w.document.querySelectorAll('.omni-card').length,2);
    t.choose('source','Clark');assert.equal(t.w.document.querySelectorAll('.omni-card').length,1);
    assert.match(t.w.location.search,/omni_q=cot/);assert.match(t.w.location.search,/untouched=1/);
    t.find('[data-action=reset]').click();assert.equal(t.find('input').value,'');
    assert.equal(t.w.location.search,'?untouched=1');
    assert.equal(t.find('[data-mod=all]').getAttribute('aria-pressed'),'true');
  }finally{t.dom.window.close();}
});

test('URL restoration, pagination, keyboard focus and inert catalog HTML',async()=>{
  const unsafe=record('<img src=x onerror=alert(1)> Cot', {sources:['<svg onload=alert(1)>']});
  const t=setup('https://example.org/sub/?omni_modality=rx',[unsafe,...Array.from({length:30},(_,i)=>record('Rx Cot '+i))]);
  try{
    await until(()=>t.find('.omni-card'));
    assert.equal(t.w.document.querySelectorAll('.omni-card').length,24);
    assert.equal(t.find('.omni-card img'),null);assert.equal(t.find('.omni-card svg'),null);
    t.find('.omni-load-more-btn').click();assert.equal(t.w.document.querySelectorAll('.omni-card').length,31);
    assert.ok(t.w.document.activeElement.classList.contains('omni-card'));
    t.w.history.replaceState(null,'','?omni_q=nonexistent');t.w.dispatchEvent(new t.w.PopStateEvent('popstate'));
    assert.ok(t.find('.omni-empty-state'));
  }finally{t.dom.window.close();}
});

test('instant navigation remount reuses the catalog',async()=>{
  const t=setup();try{
    await until(()=>t.find('[aria-busy]').getAttribute('aria-busy')==='false');
    t.find('#omnisearch-root').remove();
    const root=t.w.document.createElement('div');root.id='omnisearch-root';t.w.document.body.append(root);t.init();
    await until(()=>t.find('[aria-busy]').getAttribute('aria-busy')==='false');
    assert.equal(t.fetches,1);t.query('cot');assert.ok(t.find('.omni-card'));
  }finally{t.dom.window.close();}
});

test('offline loading offers retry and does not masquerade as zero results', async()=>{
  const t=setup(undefined,records,{failOnce:true});try{
    await until(()=>t.find('#omnisearch-results button'));
    assert.match(t.find('[role=status]').textContent,/nu a putut/);
    t.find('#omnisearch-results button').click();
    await until(()=>t.find('[role=status]').textContent.includes('în bibliotecă'));
    assert.equal(t.fetches,2);t.query('cot');assert.ok(t.find('.omni-card'));
  }finally{t.dom.window.close();}
});

test('pages without Omnisearch do not download its catalog',()=>{
  const t=setup(undefined,records,{noRoot:true});try{assert.equal(t.fetches,0);}finally{t.dom.window.close();}
});

test('native query adapter requires words, preserves operators and short abbreviations',()=>{
  const query=require('../docs/javascripts/native-search-query.js');
  assert.equal(query('mână PA'),'+mana* +pa');
  assert.equal(query('RMN genunchi'),'+rmn +genunchi*');
  assert.equal(query('CT/AP'),'+ct +ap');
  assert.equal(query('title:CT +abdomen -contrast'),'title:CT +abdomen -contrast');
  assert.equal(query('"coloana cervicala"'),'"coloana cervicala"');
});
