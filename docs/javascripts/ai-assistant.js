/* Source-aware documentation assistant. Conversation content stays in memory. */
(function () {
  'use strict';
  const core = window.RadiologyAI;
  if (!core) return;
  const scriptUrl = document.currentScript?.src || new URL('javascripts/ai-assistant.js', location.href).href;
  const base = new URL('../', scriptUrl).href;
  const local = ['localhost', '127.0.0.1', '[::1]'].includes(location.hostname);
  const api = location.port === '5173' ? '' : 'http://localhost:5173';
  const MAX_INPUT = 4000, MAX_REPLY = 32000;
  const views = new Set(), modules = new Map(), entries = [];
  let catalogPromise, discovery, active = null, serial = 0, history = [];
  let backend = {gemini: false, openai: false};
  function pref(key, fallback) { try { return localStorage.getItem(key) || fallback; } catch (_) { return fallback; } }
  function savePref(key, value) { try { localStorage.setItem(key, value); } catch (_) {} }
  let provider = pref('rad_ai_provider_v2', 'local');
  if (!['local', 'puter'].includes(provider)) provider = 'local';
  let mode = 'all', model = pref('rad_ai_puter_model', 'gpt-4o-mini');
  function element(tag, cls, value) {
    const node = document.createElement(tag);
    if (cls) node.className = cls;
    if (value !== undefined) node.textContent = value;
    return node;
  }
  function announce(message) { for (const v of views) if (v.root.isConnected) v.status.textContent = message; }
  function abortError() { return new DOMException('Oprit', 'AbortError'); }
  function waitFor(promise, signal) {
    return new Promise((resolve, reject) => {
      if (signal.aborted) return reject(abortError());
      const stop = () => { signal.removeEventListener('abort', stop); reject(abortError()); };
      signal.addEventListener('abort', stop, {once: true});
      Promise.resolve(promise).then(value => { signal.removeEventListener('abort', stop); resolve(value); }, error => {
        signal.removeEventListener('abort', stop); reject(error);
      });
    });
  }
  function loadScript(key, url, ready) {
    if (ready()) return Promise.resolve();
    if (modules.has(key)) return modules.get(key);
    const promise = new Promise((resolve, reject) => {
      const script = document.createElement('script'); script.src = url; script.async = true;
      const timer = setTimeout(() => finish(new Error('Încărcarea componentei a expirat.')), 15000);
      function finish(error) {
        clearTimeout(timer); script.onload = script.onerror = null;
        if (error) { script.remove(); reject(error); } else resolve();
      }
      script.onload = () => finish(ready() ? null : new Error('Componenta nu a putut fi inițializată.'));
      script.onerror = () => finish(new Error('Componenta nu s-a încărcat.'));
      document.head.appendChild(script);
    }).catch(error => { modules.delete(key); throw error; });
    modules.set(key, promise); return promise;
  }
  function loadPuter() { return loadScript('puter', 'https://js.puter.com/v2/', () => Boolean(window.puter?.ai)); }

  const DEFAULT_PUTER_MODELS = [
    // ⭐ Recomandate & Populare
    { id: 'gpt-4o-mini', name: 'GPT-4o Mini', provider: 'openai', popular: true },
    { id: 'gpt-4o', name: 'GPT-4o', provider: 'openai', popular: true },
    { id: 'o3-mini', name: 'OpenAI o3-mini', provider: 'openai', popular: true },
    { id: 'o1', name: 'OpenAI o1', provider: 'openai', popular: true },
    { id: 'claude-sonnet-5', name: 'Claude Sonnet 5', provider: 'claude', popular: true },
    { id: 'claude-sonnet-4-5-20250929', name: 'Claude Sonnet 4.5', provider: 'claude', popular: true },
    { id: 'claude-haiku-4-5-20251001', name: 'Claude Haiku 4.5', provider: 'claude', popular: true },
    { id: 'gemini-2.5-flash', name: 'Gemini 2.5 Flash', provider: 'gemini', popular: true },
    { id: 'gemini-2.5-pro', name: 'Gemini 2.5 Pro', provider: 'gemini', popular: true },
    { id: 'deepseek-v3.2', name: 'DeepSeek V3.2', provider: 'deepseek', popular: true },
    { id: 'deepseek-chat', name: 'DeepSeek Chat', provider: 'deepseek', popular: true },
    { id: 'mistral-large-2512', name: 'Mistral Large', provider: 'mistral', popular: true },
    { id: 'infron:meta-llama/llama-3.3-70b-instruct', name: 'LLaMA 3.3 70B', provider: 'meta', popular: true },
    // OpenAI
    { id: 'gpt-5', name: 'GPT-5', provider: 'openai' },
    { id: 'gpt-5-mini', name: 'GPT-5 Mini', provider: 'openai' },
    { id: 'gpt-4.1', name: 'GPT-4.1', provider: 'openai' },
    { id: 'gpt-4.1-mini', name: 'GPT-4.1 Mini', provider: 'openai' },
    { id: 'gpt-4-turbo', name: 'GPT-4 Turbo', provider: 'openai' },
    { id: 'gpt-3.5-turbo', name: 'GPT-3.5 Turbo', provider: 'openai' },
    { id: 'o1-mini', name: 'OpenAI o1-mini', provider: 'openai' },
    // Anthropic Claude
    { id: 'claude-opus-5', name: 'Claude Opus 5', provider: 'claude' },
    { id: 'claude-opus-4-6', name: 'Claude Opus 4.6', provider: 'claude' },
    { id: 'claude-sonnet-4-6', name: 'Claude Sonnet 4.6', provider: 'claude' },
    { id: 'openrouter:anthropic/claude-3-haiku', name: 'Claude 3 Haiku', provider: 'claude' },
    // Google Gemini
    { id: 'gemini-2.5-flash-lite', name: 'Gemini 2.5 Flash-Lite', provider: 'gemini' },
    { id: 'gemini-3-flash-preview', name: 'Gemini 3 Flash Preview', provider: 'gemini' },
    { id: 'gemini-2.0-flash', name: 'Gemini 2.0 Flash', provider: 'gemini' },
    { id: 'gemini-1.5-pro', name: 'Gemini 1.5 Pro', provider: 'gemini' },
    // DeepSeek
    { id: 'deepseek-reasoner', name: 'DeepSeek Reasoner', provider: 'deepseek' },
    { id: 'deepseek-v4-pro-0813', name: 'DeepSeek V4 Pro', provider: 'deepseek' },
    { id: 'deepseek-v4-flash-0731', name: 'DeepSeek V4 Flash', provider: 'deepseek' },
    // xAI Grok
    { id: 'grok-4.5', name: 'Grok 4.5', provider: 'xai' },
    { id: 'grok-4.6', name: 'Grok 4.6', provider: 'xai' },
    { id: 'grok-4.20-reasoning', name: 'Grok 4.20 Reasoning', provider: 'xai' },
    // Mistral
    { id: 'codestral-2508', name: 'Codestral', provider: 'mistral' },
    { id: 'ministral-8b-2512', name: 'Ministral 8B', provider: 'mistral' },
    { id: 'mistral-small-latest', name: 'Mistral Small', provider: 'mistral' }
  ];

  let puterModelsList = [...DEFAULT_PUTER_MODELS];
  let puterModelsPromise = null;

  function categorizeModelKey(m) {
    const id = (m.id || '').toLowerCase();
    const name = (m.name || '').toLowerCase();
    const prov = (m.provider || '').toLowerCase();
    if (id.includes('gpt') || id.startsWith('o1') || id.startsWith('o3') || id.startsWith('chat-') || prov.includes('openai') || prov.includes('azure-openai')) return 'openai';
    if (id.includes('claude') || name.includes('claude') || prov.includes('anthropic') || prov.includes('claude')) return 'claude';
    if (id.includes('gemini') || name.includes('gemini') || prov.includes('google') || prov.includes('gemini')) return 'gemini';
    if (id.includes('deepseek') || name.includes('deepseek') || prov.includes('deepseek')) return 'deepseek';
    if (id.includes('llama') || name.includes('llama') || prov.includes('meta')) return 'meta';
    if (id.includes('mistral') || id.includes('codestral') || prov.includes('mistral')) return 'mistral';
    if (id.includes('grok') || prov.includes('xai')) return 'xai';
    return 'other';
  }

  function renderModelOptions(filterQuery = '') {
    const q = filterQuery.toLowerCase().trim();
    for (const v of views) {
      if (!v.root.isConnected || !v.model) continue;
      const select = v.model;
      const currentSelected = model;
      
      const filtered = q
        ? puterModelsList.filter(m => ((m.name || '') + ' ' + (m.id || '') + ' ' + (m.provider || '')).toLowerCase().includes(q))
        : puterModelsList;

      select.replaceChildren();

      if (!q) {
        const popularGroup = document.createElement('optgroup');
        popularGroup.label = '⭐ Recomandate & Populare';
        for (const m of DEFAULT_PUTER_MODELS) {
          if (m.popular) {
            popularGroup.appendChild(new Option(`${m.name} (${m.id})`, m.id));
          }
        }
        select.appendChild(popularGroup);
      }

      const groups = new Map();
      const groupLabels = [
        ['openai', '🟢 OpenAI (GPT & Reasoning)'],
        ['claude', '🟣 Anthropic (Claude)'],
        ['gemini', '🔵 Google (Gemini)'],
        ['deepseek', '🟡 DeepSeek'],
        ['meta', '🔴 Meta (LLaMA)'],
        ['mistral', '🟠 Mistral AI'],
        ['xai', '⚪ xAI (Grok)'],
        ['other', '🌐 Alte Modele Puter']
      ];

      for (const [key, label] of groupLabels) {
        groups.set(key, { label, items: [] });
      }

      for (const m of filtered) {
        const catKey = categorizeModelKey(m);
        const g = groups.get(catKey) || groups.get('other');
        g.items.push(m);
      }

      for (const [key, g] of groups) {
        if (!g.items.length) continue;
        const optgroup = document.createElement('optgroup');
        optgroup.label = `${g.label} (${g.items.length})`;
        for (const m of g.items) {
          const label = m.name && m.name !== m.id ? `${m.name} [${m.id}]` : m.id;
          optgroup.appendChild(new Option(label, m.id));
        }
        select.appendChild(optgroup);
      }

      const customGroup = document.createElement('optgroup');
      customGroup.label = '✏️ Personalizat';
      customGroup.appendChild(new Option('Alt model Puter (introducere manuală)...', '__custom__'));
      select.appendChild(customGroup);

      let hasCurrent = false;
      for (const opt of select.options) {
        if (opt.value === currentSelected) {
          hasCurrent = true;
          break;
        }
      }
      if (!hasCurrent && currentSelected && currentSelected !== '__custom__') {
        const customOpt = new Option(`Model selectat: ${currentSelected}`, currentSelected);
        select.insertBefore(customOpt, select.firstChild);
      }

      select.value = currentSelected;
    }
  }

  async function fetchPuterModels() {
    if (puterModelsPromise) return puterModelsPromise;
    puterModelsPromise = (async () => {
      try {
        let models = [];
        if (window.puter?.ai?.listModels) {
          models = await window.puter.ai.listModels();
        } else if (typeof fetch === 'function') {
          const res = await fetch('https://api.puter.com/puterai/chat/models/details', { signal: AbortSignal.timeout(6000) });
          if (res.ok) {
            const data = await res.json();
            models = Array.isArray(data?.models) ? data.models : [];
          }
        }
        if (Array.isArray(models) && models.length > 0) {
          const map = new Map();
          for (const m of DEFAULT_PUTER_MODELS) {
            map.set(m.id, m);
          }
          for (const m of models) {
            if (!m || !m.id) continue;
            if (!map.has(m.id)) {
              map.set(m.id, {
                id: m.id,
                name: m.name || m.id,
                provider: m.provider || ''
              });
            }
          }
          puterModelsList = Array.from(map.values());
          renderModelOptions();
        }
      } catch (_) {}
    })();
    return puterModelsPromise;
  }
  let puterUser = null;
  let puterCheckingAuth = false;

  async function checkPuterAuth() {
    if (typeof window === 'undefined') return null;
    if (!window.puter?.auth && provider === 'puter' && !puterCheckingAuth) {
      puterCheckingAuth = true;
      try { await loadPuter(); } catch (_) {}
      puterCheckingAuth = false;
    }
    if (window.puter?.auth) {
      try {
        const signedIn = typeof window.puter.auth.isSignedIn === 'function'
          ? await window.puter.auth.isSignedIn()
          : false;
        if (signedIn) {
          if (typeof window.puter.auth.getUser === 'function') {
            const u = await window.puter.auth.getUser();
            puterUser = u?.username || u?.email || 'Conectat';
          } else {
            puterUser = 'Conectat';
          }
        } else {
          puterUser = null;
        }
      } catch (_) {
        puterUser = null;
      }
    } else {
      puterUser = null;
    }
    updateAuthViews();
    syncControls();
    return puterUser;
  }

  function updateAuthViews() {
    for (const v of views) {
      if (!v.root.isConnected || !v.authZone) continue;
      v.authZone.replaceChildren();

      if (puterUser) {
        const badge = element('div', 'rad-ai-auth-badge is-connected');
        badge.title = 'Cont Puter conectat activ';

        const dot = element('span', 'rad-ai-auth-status-dot', '●');
        dot.setAttribute('aria-hidden', 'true');

        const label = element('span', 'rad-ai-auth-status-text');
        label.append(document.createTextNode('Conectat: '));
        const userStrong = element('strong', 'rad-ai-auth-username', '@' + puterUser);
        label.append(userStrong);

        const disconnectBtn = element('button', 'rad-ai-auth-disconnect-btn', 'Deconectare');
        disconnectBtn.type = 'button';
        disconnectBtn.dataset.action = 'disconnect';
        disconnectBtn.title = 'Deconectează contul Puter';
        disconnectBtn.disabled = Boolean(active);

        badge.append(dot, label, disconnectBtn);
        v.authZone.append(badge);
      } else {
        const connectBtn = element('button', 'rad-ai-auth-connect-btn');
        connectBtn.type = 'button';
        connectBtn.dataset.action = 'connect';
        connectBtn.title = 'Conectează contul tău Puter pentru acces deplin la modele avansate';
        connectBtn.disabled = Boolean(active);
        connectBtn.innerHTML = '<span class="rad-ai-auth-icon">🔑</span><span>Conectează contul Puter</span>';
        v.authZone.append(connectBtn);
      }
      v.connect = v.authZone.querySelector('[data-action=connect]');
    }
  }

  async function handlePuterConnect() {
    try {
      announce('Se deschide conectarea Puter…');
      await loadPuter();
      if (window.puter?.auth?.signIn) {
        await window.puter.auth.signIn();
      }
      await checkPuterAuth();
      if (puterUser) {
        announce('Conectat cu succes la Puter ca @' + puterUser + '.');
      } else {
        announce('Conectarea Puter a fost finalizată.');
      }
      fetchPuterModels();
    } catch (_) {
      announce('Conectarea nu a reușit. Reîncearcă sau folosește căutarea locală.');
    }
  }

  async function handlePuterDisconnect() {
    try {
      if (window.puter?.auth?.signOut) {
        await window.puter.auth.signOut();
      }
      puterUser = null;
      updateAuthViews();
      syncControls();
      announce('Ai fost deconectat din contul Puter.');
    } catch (_) {
      announce('Deconectarea nu a reușit.');
    }
  }
  async function loadRenderer() {
    await Promise.all([
      loadScript('marked', new URL('javascripts/vendor/marked.umd.js', base).href, () => Boolean(window.marked?.parse)),
      loadScript('purify', new URL('javascripts/vendor/purify.min.js', base).href, () => Boolean(window.DOMPurify?.sanitize)),
    ]);
  }
  function renderText(node, content, markdown) {
    if (!markdown || !window.marked?.parse || !window.DOMPurify?.sanitize) {
      node.textContent = content; node.classList.add('rad-ai-plain'); return;
    }
    node.innerHTML = window.DOMPurify.sanitize(window.marked.parse(content, {breaks: true}), {
      ALLOWED_TAGS: ['p','br','strong','em','ul','ol','li','blockquote','pre','code','h2','h3','h4','table','thead','tbody','tr','td','th','a','hr'],
      ALLOWED_ATTR: ['href', 'title'], ALLOW_DATA_ATTR: false,
    });
    for (const a of node.querySelectorAll('a')) {
      const url = core.safeLink(a.getAttribute('href'), base);
      if (url) { a.href = url; a.rel = 'noopener noreferrer'; }
      else a.replaceWith(document.createTextNode(a.textContent));
    }
  }
  async function loadCatalog() {
    if (!catalogPromise) catalogPromise = (async () => {
      const response = await fetch(new URL('javascripts/ai-library.json', base), {signal: AbortSignal.timeout(20000)});
      if (!response.ok) throw new Error('Catalog indisponibil');
      const data = await response.json();
      if (!Array.isArray(data.protocols)) throw new Error('Catalog nevalid');
      return core.prepareCatalog(data.protocols);
    })().catch(error => { catalogPromise = null; throw error; });
    return catalogPromise;
  }
  async function discoverBackend() {
    if (!local || discovery) return discovery;
    discovery = (async () => {
      try {
        const response = await fetch(api + '/api/ai/auth/status', {signal: AbortSignal.timeout(3500)});
        if (response.ok) { const data = await response.json(); backend = {gemini: Boolean(data.providers?.gemini), openai: Boolean(data.providers?.openai)}; }
      } catch (_) {}
      syncControls();
    })();
    return discovery;
  }
  function sourceList(matches) {
    const block = element('div', 'rad-ai-sources'), list = element('ol');
    block.append(element('p', 'rad-ai-sources-title', 'Documente selectate în catalog'));
    for (const match of matches) {
      const li = element('li'), link = element('a', '', '[' + match.id + '] ' + match.title);
      link.href = match.url; li.append(link);
      const review = match.record?.review;
      if (review) li.append(element('small', '', [review.publication,
        review.fidelity && 'Fidelitatea preluării: ' + review.fidelity,
        'Revizuire medicală: ' + (review.medical || 'Nedocumentată')].filter(Boolean).join(' · ')));
      if (match.record?.sources?.length) {
        const details = element('details'), refs = element('ul');
        details.append(element('summary', '', 'Referințe declarate în protocol'));
        for (const source of match.record.sources) {
          const item = element('li'), url = source.url && core.safeLink(source.url, base);
          const label = [source.title, source.edition && 'Ediția ' + source.edition, source.locator].filter(Boolean).join(' · ');
          if (url) { const a = element('a', '', label); a.href = url; a.rel = 'noopener noreferrer'; item.append(a); }
          else item.textContent = label;
          refs.append(item);
        }
        details.append(refs); li.append(details);
      }
      list.append(li);
    }
    block.append(list, element('p', 'rad-ai-note', 'Potriviri de căutare, nu confirmări ale indicației clinice. Consultă sursa originală și stadiul verificărilor.'));
    return block;
  }
  function renderEntry(entry) {
    const article = element('article', 'rad-ai-message rad-ai-' + entry.role);
    article.dataset.entry = entry.id; article.setAttribute('aria-label', entry.role === 'user' ? 'Întrebarea ta' : 'Răspuns');
    article.append(element('div', 'rad-ai-message-label', entry.role === 'user' ? 'Tu' : entry.engine || 'Asistent de documentare'));
    const body = element('div', 'rad-ai-answer');
    renderText(body, entry.text, entry.role !== 'user' && entry.status === 'done'); article.append(body);
    if (entry.matches?.length) article.append(sourceList(entry.matches));
    if (entry.status === 'done' && entry.role !== 'user') {
      const copy = element('button', 'rad-ai-text-button', 'Copiază răspunsul și sursele'); copy.type = 'button';
      copy.addEventListener('click', async () => {
        const refs = (entry.matches || []).map(s => '[' + s.id + '] ' + s.title + ': ' + s.url).join('\n');
        try { await navigator.clipboard.writeText(entry.engine + '\n\n' + entry.text + '\n\n' + refs); copy.textContent = 'Copiat'; }
        catch (_) { announce('Copierea nu este disponibilă. Poți selecta textul răspunsului.'); }
      }); article.append(copy);
    }
    if (entry.showGuidelineFallback && provider === 'puter') {
      const askAcr = element('button', 'rad-ai-guideline-button', '🌐 Consultă Ghidurile Internaționale (ACR / ESUR / ESR)');
      askAcr.type = 'button';
      askAcr.disabled = Boolean(active);
      askAcr.addEventListener('click', () => submitGuidelineFallback(entry.query, entry));
      article.append(askAcr);
    }
    if (['error', 'stopped'].includes(entry.status)) {
      const retry = element('button', 'rad-ai-text-button', 'Reîncearcă întrebarea'); retry.type = 'button'; retry.disabled = Boolean(active);
      retry.addEventListener('click', () => submit(entry.query, entry)); article.append(retry);
    }
    return article;
  }
  function renderThread(forceBottom = false) {
    for (const v of views) {
      if (!v.root.isConnected) { views.delete(v); continue; }
      const nearBottom = v.thread.scrollHeight - v.thread.scrollTop - v.thread.clientHeight < 100;
      v.thread.replaceChildren();
      if (!entries.length) v.thread.append(element('p', 'rad-ai-empty', 'Caută o examinare, o regiune anatomică sau un protocol. Vei vedea documentele găsite și stadiul verificărilor lor.'));
      for (const entry of entries) v.thread.append(renderEntry(entry));
      if (forceBottom || nearBottom) v.thread.scrollTop = v.thread.scrollHeight;
    }
    syncControls();
  }
  function paintStream(entry) {
    for (const v of views) {
      if (!v.root.isConnected) continue;
      const nearBottom = v.thread.scrollHeight - v.thread.scrollTop - v.thread.clientHeight < 100;
      const article = v.thread.querySelector('[data-entry="' + entry.id + '"]');
      if (article) article.querySelector('.rad-ai-answer').textContent = entry.text;
      if (nearBottom) v.thread.scrollTop = v.thread.scrollHeight;
    }
  }
  function syncControls() {
    for (const v of views) {
      if (!v.root.isConnected) { views.delete(v); continue; }
      const choices = [['local', 'Căutare locală · fără AI'], ['puter', 'AI prin Puter'],
        ...(backend.gemini ? [['gemini', 'Gemini · server local']] : []), ...(backend.openai ? [['openai', 'OpenAI · server local']] : [])];
      v.provider.replaceChildren(...choices.map(([value, label]) => new Option(label, value)));
      v.provider.value = provider; v.mode.value = mode;
      if (v.model) v.model.value = model;
      v.modelRow.hidden = provider !== 'puter';
      v.provider.disabled = v.mode.disabled = Boolean(active);
      if (v.connect) v.connect.disabled = Boolean(active);
      if (v.authZone) {
        for (const b of v.authZone.querySelectorAll('button')) b.disabled = Boolean(active);
      }
      if (v.model) v.model.disabled = Boolean(active);
      if (v.modelFilter) v.modelFilter.disabled = Boolean(active);
      v.send.disabled = Boolean(active); v.stop.hidden = !active;
      v.thread.setAttribute('aria-busy', String(Boolean(active)));
      v.notice.textContent = provider === 'local' ? 'Căutarea rulează în browser; întrebarea nu este trimisă unui furnizor AI.'
        : 'Prin trimitere, întrebarea, istoricul recent și fragmentele selectate ajung la ' + (provider === 'puter' ? 'Puter (' + (puterUser ? 'autentificat ca @' + puterUser : 'cont gratuit / neconectat') + ') și furnizorul modelului ales (' + model + ')' : provider === 'gemini' ? 'Google, prin serverul local' : 'OpenAI, prin serverul local') + '. Nu introduce date de identificare ale pacienților. Accesul și costurile depind de furnizor.';
    }
  }
  function stop() { if (active) { active.reason = 'stopped'; active.controller.abort(); } }
  function clear() { stop(); active = null; serial++; entries.length = 0; history = []; renderThread(); announce('Conversația a fost ștearsă din această pagină.'); }
  async function generatePuter(query, matches, request) {
    await waitFor(loadPuter(), request.controller.signal);
    const response = await waitFor(window.puter.ai.chat(core.messages(query, matches, history), {model, stream: true}), request.controller.signal);
    if (!response?.[Symbol.asyncIterator]) {
      const text = typeof response === 'string' ? response : response?.message?.content;
      if (typeof text !== 'string' || !text.trim()) throw new Error('Răspuns gol');
      return text.slice(0, MAX_REPLY);
    }
    const iterator = response[Symbol.asyncIterator](); let text = '', lastPaint = 0;
    try {
      while (true) {
        const next = await waitFor(iterator.next(), request.controller.signal);
        if (next.done) break;
        if (next.value?.type === 'error') throw new Error('Generare întreruptă');
        if (typeof next.value?.text !== 'string') continue;
        text += next.value.text;
        if (text.length > MAX_REPLY) throw new Error('Răspuns prea lung');
        if (Date.now() - lastPaint > 100 && active === request) { request.entry.text = text; paintStream(request.entry); lastPaint = Date.now(); }
      }
    } finally {
      // Closing the iterator cannot guarantee cancellation at the remote provider.
      if (iterator.return) Promise.resolve(iterator.return()).catch(() => {});
    }
    if (!text.trim()) throw new Error('Răspuns gol');
    return text;
  }
  async function submitGuidelineFallback(query, entry) {
    if (active) return;
    entry.status = 'loading';
    entry.showGuidelineFallback = false;
    entry.engine = 'Orientare Ghiduri Internaționale · Puter / ' + model;
    entry.text = 'Se consultă recomandările internaționale (ACR / ESUR / ESR)…';
    const request = {id: ++serial, controller: new AbortController(), entry, reason: '', stage: 'provider'};
    active = request;
    const timer = setTimeout(() => { request.reason = 'timeout'; request.controller.abort(); }, 120000);
    renderThread();
    announce('Se pregătește răspunsul din ghidurile internaționale.');
    try {
      await waitFor(loadPuter(), request.controller.signal);
      const msgs = core.guidelineMessages(query, history);
      const response = await waitFor(window.puter.ai.chat(msgs, {model, stream: true}), request.controller.signal);
      let text = '';
      if (!response?.[Symbol.asyncIterator]) {
        text = typeof response === 'string' ? response : response?.message?.content || '';
        if (!text.trim()) throw new Error('Răspuns gol');
      } else {
        const iterator = response[Symbol.asyncIterator]();
        let lastPaint = 0;
        try {
          while (true) {
            const next = await waitFor(iterator.next(), request.controller.signal);
            if (next.done) break;
            if (next.value?.type === 'error') throw new Error('Generare întreruptă');
            if (typeof next.value?.text !== 'string') continue;
            text += next.value.text;
            if (text.length > MAX_REPLY) throw new Error('Răspuns prea lung');
            if (Date.now() - lastPaint > 100 && active === request) {
              request.entry.text = text;
              paintStream(request.entry);
              lastPaint = Date.now();
            }
          }
        } finally {
          if (iterator.return) Promise.resolve(iterator.return()).catch(() => {});
        }
      }
      if (active !== request) return;
      if (request.controller.signal.aborted) throw abortError();
      try { await waitFor(loadRenderer(), request.controller.signal); } catch (_) {}
      entry.text = text;
      entry.status = 'done';
      history.push({role: 'user', content: query}, {role: 'assistant', content: entry.text.slice(0, 6000)});
      history = history.slice(-6);
      announce('Răspuns din ghiduri internaționale disponibil.');
    } catch (_) {
      if (active !== request) return;
      entry.status = request.reason === 'stopped' ? 'stopped' : 'error';
      entry.engine = entry.status === 'stopped' ? 'Afișare oprită' : 'Răspuns indisponibil';
      entry.text = request.reason === 'stopped' ? 'Afișarea a fost oprită.'
        : request.reason === 'timeout' ? 'Timpul de așteptare a expirat. Reîncearcă mai târziu.'
        : 'Nu am putut finaliza consultarea ghidurilor internaționale. Verifică accesul la furnizor și conexiunea.';
      announce(entry.engine);
    } finally {
      clearTimeout(timer);
      if (active === request) { active = null; renderThread(); }
    }
  }

  async function submit(query, retryEntry = null) {
    query = String(query || '').trim();
    if (active || !query) return;
    if (query.length > MAX_INPUT) { announce('Limita este de 4000 de caractere. Restrânge întrebarea.'); return; }
    if (!retryEntry) entries.push({id: ++serial, role: 'user', text: query, status: 'done'});
    const entry = retryEntry || {id: ++serial, role: 'assistant'};
    Object.assign(entry, {query, status: 'loading', text: 'Se caută documente în catalog…', engine: 'Căutare în bibliotecă', matches: [], showGuidelineFallback: false});
    if (!retryEntry) entries.push(entry);
    const request = {id: ++serial, controller: new AbortController(), entry, reason: '', stage: 'catalog'}; active = request;
    const timer = setTimeout(() => { request.reason = 'timeout'; request.controller.abort(); }, 120000);
    renderThread(true); announce('Se pregătește răspunsul.');
    try {
      const catalog = mode === 'iris' ? [] : await waitFor(loadCatalog(), request.controller.signal);
      if (['all', 'iris'].includes(mode) && !window.IRIS) await waitFor(loadScript('iris', new URL('javascripts/iris-data.js', base).href, () => Boolean(window.IRIS)), request.controller.signal);
      const activeContext = (contextActive && pageProtocolContext) ? pageProtocolContext : null;
      const matches = core.retrieve(query, mode, catalog, window.IRIS, base, activeContext); entry.matches = matches;
      request.stage = 'provider';
      const isContextAware = matches.some(m => m.isCurrentPage);
      if (!matches.length) {
        entry.text = 'Nu am găsit documente pentru termenii și filtrul selectat în biblioteca locală. Încearcă denumirea examinării sau regiunea anatomică. Nu a fost solicitat un răspuns AI fără documente de referință.';
        entry.engine = 'Căutare locală · fără generare AI';
        entry.showGuidelineFallback = (provider === 'puter');
      } else if (provider === 'local') {
        entry.text = isContextAware
          ? 'Date din protocolul curent: ' + (activeContext?.title || '') + '. Deschide paginile de mai jos pentru parametri și verificări. Pentru o analiză detaliată sau sinteză, selectează un model AI (Puter).'
          : 'Am găsit ' + matches.length + ' documente asociate termenilor căutați. Deschide paginile de mai jos pentru parametri, surse și verificări. Pentru o sinteză, selectează explicit un furnizor AI.';
        entry.engine = isContextAware ? 'Protocol pagină curentă · Local' : 'Căutare locală · fără generare AI';
      } else if (provider === 'puter') {
        entry.engine = 'Răspuns AI · Puter / ' + model + (isContextAware ? ' (Context pagină)' : ''); entry.text = 'Se așteaptă furnizorul ales…'; renderThread();
        entry.text = await generatePuter(query, matches, request);
      } else {
        entry.engine = 'Se așteaptă furnizorul ales…'; renderThread();
        const response = await fetch(api + '/api/ai/chat', {method: 'POST', signal: request.controller.signal,
          headers: {'Content-Type': 'application/json'}, body: JSON.stringify({message: query, provider, mode, history})});
        const data = await response.json();
        if (!response.ok || !data.ok || typeof data.reply !== 'string') throw new Error('Serviciul AI nu a răspuns.');
        entry.text = data.reply.slice(0, MAX_REPLY);
        entry.engine = data.response_type === 'local' ? 'Rezultate locale · furnizor indisponibil' : 'Răspuns AI · ' + data.engine;
        if (Array.isArray(data.sources)) entry.matches = data.sources.map(s => ({id: s.id, title: s.title,
          url: core.safeLink(s.url, base), record: {review: s.review, sources: s.references || []}})).filter(s => s.url);
        if (data.notice) entry.text = data.notice + '\n\n' + entry.text;
      }
      if (active !== request) return;
      if (request.controller.signal.aborted) throw abortError();
      try { await waitFor(loadRenderer(), request.controller.signal); } catch (_) {}
      if (active !== request) return;
      if (request.controller.signal.aborted) throw abortError();
      entry.status = 'done';
      if (provider !== 'local' && matches.length && entry.engine.startsWith('Răspuns AI')) {
        history.push({role: 'user', content: query}, {role: 'assistant', content: entry.text.slice(0, 6000)}); history = history.slice(-6);
      }
      announce('Răspuns disponibil. Verifică documentele afișate.');
    } catch (_) {
      if (active !== request) return;
      entry.status = request.reason === 'stopped' ? 'stopped' : 'error';
      entry.engine = entry.status === 'stopped' ? 'Afișare oprită' : 'Răspuns indisponibil';
      entry.text = request.reason === 'stopped' ? 'Afișarea a fost oprită. Solicitarea poate continua la furnizor; conținutul parțial nu a fost adăugat în istoricul conversației.'
        : request.reason === 'timeout' ? 'Timpul de așteptare a expirat. Reîncearcă sau folosește căutarea locală.'
        : request.stage === 'catalog' ? 'Biblioteca nu a putut fi încărcată. Verifică conexiunea și reîncearcă. Întrebarea nu a fost trimisă unui furnizor AI.'
        : 'Nu am putut finaliza răspunsul. Verifică accesul la furnizor, modelul și conexiunea, apoi reîncearcă. Documentele găsite rămân disponibile mai jos.';
      announce(entry.engine);
    } finally { clearTimeout(timer); if (active === request) { active = null; renderThread(); } }
  }

  let pageProtocolContext = null;
  let contextActive = true;

  function extractDomProtocol() {
    const path = (typeof window !== 'undefined' ? window.location?.pathname : '') || '';
    const m = path.match(/\/(ct|irm|rx|eco|fluoro|mn)\/([^/]+)\/([^/]+)/);
    if (!m) return null;
    const h1 = document.querySelector('h1')?.textContent?.trim().replace(/\s*#.*$/, '') || '';
    if (!h1) return null;
    return {
      title: h1,
      modality: m[1],
      category: m[2],
      url: path.replace(/^\/+/, ''),
      details: {},
      sources: [],
      review: { medical: 'Protocol deschis în pagina curentă', publication: 'Activ' }
    };
  }

  async function resolvePageContext() {
    if (pageProtocolContext && pageProtocolContext.details && Object.keys(pageProtocolContext.details).length) {
      return pageProtocolContext;
    }
    const domProto = pageProtocolContext || extractDomProtocol();
    if (!domProto) return null;
    try {
      const catalog = await loadCatalog();
      const matched = core.detectPageContext(window.location.pathname, catalog, base);
      pageProtocolContext = matched || domProto;
    } catch (_) {
      pageProtocolContext = domProto;
    }
    updateContextViews();
    return pageProtocolContext;
  }

  function renderPrompts(v) {
    if (!v.prompts) return;
    v.prompts.replaceChildren();
    const isContextual = pageProtocolContext && contextActive;
    const items = isContextual ? [
      ['📌 Rezumat & Timpi', `Rezumatul protocolului și timpii cheie de scanare pentru: ${pageProtocolContext.title}`],
      ['💉 Contrast & Doză', `Ce substanță de contrast, volum și debit/întârziere se folosesc pentru: ${pageProtocolContext.title}?`],
      ['⚠️ Pregătire & Siguranță', `Care sunt cerințele de pregătire a pacientului și contraindicațiile pentru: ${pageProtocolContext.title}?`],
      ['📋 Șablon Raport', `Generează un șablon structurat de raportare radiologică pentru examinarea: ${pageProtocolContext.title}`]
    ] : [
      ['CT abdomen', 'CT abdomen pelvis contrast'],
      ['IRM genunchi', 'IRM genunchi menisc'],
      ['RX torace', 'Radiografie torace PA'],
      ['Ecografie tiroidă', 'Ecografie tiroida']
    ];

    for (const [label, prompt] of items) {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.textContent = label;
      btn.dataset.prompt = prompt;
      btn.addEventListener('click', () => {
        v.input.value = prompt;
        v.input.dispatchEvent(new Event('input'));
        v.input.focus();
      });
      v.prompts.appendChild(btn);
    }
  }

  function updateContextViews() {
    for (const v of views) {
      if (!v.root.isConnected) { views.delete(v); continue; }
      if (v.contextBanner) {
        if (pageProtocolContext) {
          v.contextBanner.hidden = false;
          if (v.contextTitle) v.contextTitle.textContent = pageProtocolContext.title;
          if (v.contextModality) {
            const modLabel = core.MODALITIES[pageProtocolContext.modality] || pageProtocolContext.modality.toUpperCase();
            v.contextModality.textContent = modLabel + (pageProtocolContext.category ? ` · ${pageProtocolContext.category}` : '');
          }
          if (v.contextToggle) v.contextToggle.checked = contextActive;
        } else {
          v.contextBanner.hidden = true;
        }
      }
      renderPrompts(v);
    }
  }

  function mount(root, compact = false) {
    if (root.dataset.aiMounted) return;
    root.dataset.aiMounted = 'true'; root.classList.add('rad-ai');
    const prefix = compact ? 'rad-ai-widget' : 'rad-ai-page';
    root.innerHTML = `<div class="rad-ai-toolbar">
      <label>Mod de răspuns<select data-control="provider" aria-label="Mod de răspuns"></select></label>
      <label>Caută în<select data-control="mode" aria-label="Filtru de documente"><option value="all">Toată biblioteca</option><option value="iris">Ghid IRIS</option><option value="ct">CT</option><option value="irm">IRM</option><option value="rx">RX</option><option value="eco">Ecografie</option><option value="fluoro">Fluoroscopie</option><option value="mn">Medicină Nucleară</option></select></label>
      <button type="button" data-action="clear" class="rad-ai-text-button">Conversație nouă</button></div>
    <div class="rad-ai-model-row" data-slot="model-row" hidden>
      <label class="rad-ai-model-select-label">Model Puter<select data-control="model" aria-label="Model Puter"></select></label>
      <label class="rad-ai-model-filter-label" title="Filtrează lista de modele Puter">Caută model<input type="search" data-control="model-filter" placeholder="Ex: claude, gemini, o3..." aria-label="Filtrează modele Puter"></label>
      <div class="rad-ai-auth-zone" data-slot="auth-zone">
        <button type="button" data-action="connect" class="rad-ai-auth-connect-btn"><span class="rad-ai-auth-icon">🔑</span><span>Conectează contul Puter</span></button>
      </div>
    </div>
    <div class="rad-ai-context-banner" data-slot="context-banner" hidden>
      <div class="rad-ai-context-info">
        <span class="rad-ai-context-icon">📌</span>
        <div class="rad-ai-context-text">
          <span class="rad-ai-context-modality" data-slot="context-modality"></span>
          <strong class="rad-ai-context-title" data-slot="context-title"></strong>
        </div>
      </div>
      <label class="rad-ai-context-toggle" title="Include protocolul curent ca referință principală">
        <input type="checkbox" data-control="context-active" checked>
        <span>Context pagină</span>
      </label>
    </div>
    <p class="rad-ai-notice" data-slot="notice"></p>
    <div class="rad-ai-thread" data-slot="thread" role="log" aria-label="Conversație" aria-live="off"></div>
    <div class="rad-ai-tools" data-slot="tools" aria-label="Instrumente clinice rapide">
      <button type="button" class="rad-ai-tool-btn" data-tool="report" title="Generează un șablon structurat de raport">📋 Șablon Raport</button>
      <button type="button" class="rad-ai-tool-btn" data-tool="contrast" title="Calculează doza de contrast și parametrii de injectare">💉 Doză Contrast</button>
      <button type="button" class="rad-ai-tool-btn" data-tool="iris" title="Verifică gradul de recomandare conform ghidului IRIS">🧭 Ghid IRIS</button>
      <button type="button" class="rad-ai-tool-btn" data-tool="compare" title="Compară opțiunile de examinare">⚖️ Compară</button>
    </div>
    <div class="rad-ai-prompts" data-slot="prompts" aria-label="Exemple de căutare"></div>
    <form class="rad-ai-form"><label for="${prefix}-input">Întrebarea ta</label><textarea id="${prefix}-input" rows="3" maxlength="4000" placeholder="De exemplu: ce documente descriu protocolul IRM de genunchi?"></textarea><div class="rad-ai-compose-actions"><small data-slot="counter">0 / 4000 · Enter trimite · Shift+Enter rând nou</small><button type="button" data-action="stop" hidden>Oprește afișarea</button><button type="submit" data-action="send">Trimite</button></div></form>
    <p class="rad-ai-status" data-slot="status" role="status" aria-live="polite"></p>
    <p class="rad-ai-note">Conversația este păstrată numai în memoria acestei pagini. Răspunsurile AI nu reprezintă revizuirea medicală a protocoalelor.</p>`;
    const find = selector => root.querySelector(selector);
    const v = {root, provider: find('[data-control=provider]'), mode: find('[data-control=mode]'), model: find('[data-control=model]'),
      modelFilter: find('[data-control=model-filter]'),
      modelRow: find('[data-slot=model-row]'),
      authZone: find('[data-slot=auth-zone]'),
      contextBanner: find('[data-slot=context-banner]'),
      contextModality: find('[data-slot=context-modality]'),
      contextTitle: find('[data-slot=context-title]'),
      contextToggle: find('[data-control=context-active]'),
      prompts: find('[data-slot=prompts]'),
      connect: find('[data-action=connect]'), thread: find('[data-slot=thread]'),
      notice: find('[data-slot=notice]'), send: find('[data-action=send]'), stop: find('[data-action=stop]'), input: find('textarea'), status: find('[data-slot=status]')};
    views.add(v);
    renderModelOptions();
    if (!pageProtocolContext) pageProtocolContext = extractDomProtocol();
    updateContextViews();
    updateAuthViews();
    v.provider.addEventListener('change', () => { provider = v.provider.value; history = []; savePref('rad_ai_provider_v2', provider); if (provider === 'puter') { fetchPuterModels(); checkPuterAuth(); } syncControls(); });
    v.mode.addEventListener('change', () => { mode = v.mode.value; history = []; syncControls(); });
    v.model.addEventListener('change', () => {
      if (v.model.value === '__custom__') {
        const custom = window.prompt('Introdu ID-ul modelului Puter (ex: openrouter:anthropic/claude-3-5-sonnet):', model);
        if (custom && custom.trim()) {
          model = custom.trim();
          savePref('rad_ai_puter_model', model);
        }
        renderModelOptions(v.modelFilter ? v.modelFilter.value.trim() : '');
        syncControls();
        return;
      }
      model = v.model.value.trim() || 'gpt-4o-mini';
      history = [];
      savePref('rad_ai_puter_model', model);
      syncControls();
    });
    if (v.modelFilter) {
      v.modelFilter.addEventListener('input', () => {
        renderModelOptions(v.modelFilter.value.trim());
      });
    }
    if (v.contextToggle) {
      v.contextToggle.addEventListener('change', () => {
        contextActive = Boolean(v.contextToggle.checked);
        updateContextViews();
      });
    }
    if (v.authZone) {
      v.authZone.addEventListener('click', async event => {
        const btn = event.target.closest('button');
        if (!btn) return;
        if (btn.dataset.action === 'connect') {
          await handlePuterConnect();
        } else if (btn.dataset.action === 'disconnect') {
          await handlePuterDisconnect();
        }
      });
    }
    for (const btn of root.querySelectorAll('[data-tool]')) {
      btn.addEventListener('click', () => {
        const tool = btn.dataset.tool;
        const currentTitle = pageProtocolContext ? pageProtocolContext.title : '';
        if (tool === 'report') {
          v.input.value = currentTitle
            ? `Generează un șablon structurat de raportare radiologică pentru examinarea: ${currentTitle}.`
            : 'Generează un șablon structurat de buletin radiologic pentru un examen CT abdomen și pelvis cu substanță de contrast.';
        } else if (tool === 'contrast') {
          v.input.value = currentTitle
            ? `Calculează doza de substanță de contrast, volumul și debitul recomandat pentru protocolul ${currentTitle} la un pacient adult de 70 kg conform ghidului ESUR.`
            : 'Calculează doza de substanță de contrast iodat pentru un adult de 70 kg cu funcție renală normală (eGFR > 60), specificând volumul și debitul de injectare conform ghidului ESUR.';
        } else if (tool === 'iris') {
          v.mode.value = 'iris';
          mode = 'iris';
          syncControls();
          v.input.value = 'Care este gradul de recomandare conform ghidului IRIS pentru indicația: ';
        } else if (tool === 'compare') {
          v.input.value = currentTitle
            ? `Compară indicațiile, timpii de scanare și beneficiile protocolului ${currentTitle} cu alternativa sa fără substanță de contrast.`
            : 'Compară diferențele tehnice și indicațiile între o examinare CT nativă și una cu substanță de contrast.';
        }
        updateCounter();
        v.input.focus();
      });
    }
    function updateCounter() { find('[data-slot=counter]').textContent = v.input.value.length + ' / 4000 · Enter trimite · Shift+Enter rând nou'; }
    const send = () => {
      const query = v.input.value.trim(); if (!query || active) return;
      if (query.length > MAX_INPUT) { announce('Limita este de 4000 de caractere.'); return; }
      v.input.value = ''; updateCounter(); submit(query);
    };
    v.input.addEventListener('input', updateCounter);
    find('form').addEventListener('submit', event => { event.preventDefault(); send(); });
    v.input.addEventListener('keydown', event => { if (event.key === 'Enter' && !event.shiftKey && !event.isComposing) { event.preventDefault(); send(); } });
    v.stop.addEventListener('click', stop); find('[data-action=clear]').addEventListener('click', clear);
    renderThread(); discoverBackend();
    resolvePageContext();
  }
  function init() {
    if (provider === 'puter') { fetchPuterModels(); checkPuterAuth(); }
    resolvePageContext();
    const dedicated = document.getElementById('ai-workspace-root'); let widget = document.getElementById('rad-ai-floating');
    if (dedicated) { mount(dedicated); if (widget) widget.hidden = true; return; }
    if (widget) { widget.hidden = false; return; }
    widget = element('div', 'rad-ai-floating'); widget.id = 'rad-ai-floating';
    const toggle = element('button', 'ai-widget-toggle rad-ai-toggle'); toggle.type = 'button';
    toggle.innerHTML = '<span class="ai-toggle-icon">✨</span><span class="ai-toggle-label">Asistent AI Clinic</span>';
    toggle.title = 'Deschide Asistentul AI Clinic';
    toggle.setAttribute('aria-expanded', 'false'); toggle.setAttribute('aria-controls', 'rad-ai-panel');
    const panel = element('section', 'rad-ai-panel'); panel.id = 'rad-ai-panel'; panel.hidden = true; panel.setAttribute('aria-label', 'Asistent de documentare');
    const header = element('div', 'rad-ai-panel-header');
    const title = element('div', 'rad-ai-panel-title');
    title.innerHTML = '<span class="rad-ai-panel-title-icon">✨</span><span class="rad-ai-panel-title-text">Asistent AI Clinic</span>';
    const actions = element('div', 'rad-ai-panel-actions');
    const full = element('a', 'rad-ai-panel-link', 'Pagină dedicată ↗');
    full.href = new URL('ai/', base).href;
    full.title = 'Deschide asistentul în pagină completă';
    const close = element('button', 'rad-ai-close-btn');
    close.type = 'button';
    close.dataset.action = 'close';
    close.setAttribute('aria-label', 'Închide fereastra asistentului AI');
    close.title = 'Închide fereastra (Esc)';
    close.innerHTML = '<span class="rad-ai-close-icon" aria-hidden="true">✕</span><span class="rad-ai-close-text">Închide</span>';
    actions.append(full, close);
    header.append(title, actions);
    const content = element('div'); panel.append(header, content); widget.append(toggle, panel); document.body.append(widget);
    function hide() { panel.hidden = true; toggle.setAttribute('aria-expanded', 'false'); toggle.focus(); }
    toggle.addEventListener('click', () => { if (!panel.hidden) return hide(); panel.hidden = false; toggle.setAttribute('aria-expanded', 'true'); mount(content, true); content.querySelector('textarea').focus(); });
    close.addEventListener('click', hide); panel.addEventListener('keydown', event => { if (event.key === 'Escape') { event.preventDefault(); hide(); } });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
  if (window.document$) window.document$.subscribe(init);
})();
