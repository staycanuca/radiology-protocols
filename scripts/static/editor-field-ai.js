/* Field research belongs to the application editor, not Protocol Workbench. */
(() => {
  'use strict';
  const form = document.getElementById('proto-form');
  if (!form) return;
  const selector = 'input:not([type=hidden]):not([type=button]):not([type=submit]), textarea, select';
  const excludedContext = new Set(['author', 'last_updated', 'slug', 'url', 'caption', 'description']);
  const wired = new WeakSet();
  const dialog = document.createElement('dialog');
  dialog.className = 'field-ai-dialog';
  dialog.setAttribute('aria-labelledby', 'field-ai-title');
  dialog.innerHTML = `
    <div class="field-ai-header"><h2 id="field-ai-title"></h2><button type="button" data-action="close" aria-label="Închide documentarea AI">Închide</button></div>
    <p class="field-ai-meta" data-slot="context"></p>
    <p data-slot="status" role="status" aria-live="polite"></p>
    <div data-slot="result" hidden>
      <h3>Valoare propusă</h3><pre data-slot="suggestion"></pre>
      <h3>Justificare și aplicabilitate</h3><p data-slot="explanation"></p>
      <h3>Limite și informații de verificat</h3><ul data-slot="limitations"></ul>
      <h3>Surse citate de căutarea web</h3><ul data-slot="sources"></ul>
      <p class="field-ai-meta" data-slot="engine"></p>
      <div data-slot="search-entry"></div>
      <label><input type="checkbox" data-slot="review">Am verificat sursele și aplicabilitatea propunerii pentru acest protocol.</label>
      <button type="button" data-action="apply" disabled>Aplică în câmp</button>
      <p class="field-ai-meta">Aplicarea modifică formularul. Salvarea protocolului se face prin „Salvează Protocolul”.</p>
    </div>`;
  document.body.append(dialog);
  const slot = name => dialog.querySelector(`[data-slot="${name}"]`);
  const apply = dialog.querySelector('[data-action=apply]');
  let pending = null, controller = null, generation = 0;

  async function connectionAction(action, button) {
    const provider = document.getElementById('field-ai-provider').value;
    const status = document.getElementById('field-ai-connection');
    if (!['codex_oauth', 'gemini_oauth'].includes(provider)) {
      status.textContent = 'Selectează explicit ChatGPT OAuth sau Gemini OAuth pentru această acțiune.';
      return;
    }
    button.disabled = true;
    status.textContent = action === 'check' ? 'Se verifică sesiunea OAuth…' : 'Se deschide conectarea oficială…';
    try {
      const response = await fetch('/api/ai/cli-' + action, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({provider})});
      const data = await response.json();
      status.textContent = data.message || data.error || 'Răspuns de conectare invalid.';
    } catch { status.textContent = 'Editorul nu poate contacta serviciul local de autentificare.'; }
    finally { button.disabled = false; }
  }
  for (const action of ['connect', 'check']) {
    const button = document.getElementById('field-ai-' + action);
    button?.addEventListener('click', () => connectionAction(action, button));
  }

  function fieldName(input) { return input.name || input.dataset.field || input.id || input.type; }
  function label(input) {
    return (input.labels?.[0]?.textContent || input.parentElement.querySelector('label')?.textContent || fieldName(input)).trim();
  }
  function value(input) {
    if (input.type === 'file') return '';
    if (input.type === 'checkbox' || input.type === 'radio') return input.checked ? input.value : '';
    return input.value;
  }
  function visible(input) { return input.getClientRects().length > 0; }
  function payload(input) {
    const row = input.closest('.dynamic-row');
    const section = input.closest('.section');
    const fields = Array.from(form.querySelectorAll(selector)).filter(el =>
      visible(el) && !excludedContext.has(fieldName(el)) && el.type !== 'file' && value(el));
    return {
      provider: document.getElementById('field-ai-provider').value,
      protocol: {title: form.querySelector('[name=title]').value, modality: form.querySelector('[name=modality]').value,
        category: form.querySelector('[name=category]').value},
      field: {name: fieldName(input), label: label(input), type: input.type || input.tagName.toLowerCase(),
        value: value(input), section: section?.querySelector('h2')?.textContent || '',
        row: row ? Array.from(row.querySelectorAll(selector)).map(el => ({name: fieldName(el), value: value(el)})) : [],
        options: input.options ? Array.from(input.options).map(o => ({value: o.value, label: o.text})) : []},
      context: fields.map(el => ({name: fieldName(el), label: label(el), value: value(el)}))
    };
  }
  function addTextList(root, items) {
    root.replaceChildren();
    for (const text of items) { const li = document.createElement('li'); li.textContent = text; root.append(li); }
  }
  function safeLink(url) {
    try { const parsed = new URL(url); return parsed.protocol === 'https:' && !parsed.username && !parsed.password; }
    catch { return false; }
  }
  function close() { generation++; controller?.abort(); pending = null; dialog.close(); }
  dialog.querySelector('[data-action=close]').addEventListener('click', close);
  dialog.addEventListener('cancel', event => { event.preventDefault(); close(); });
  slot('review').addEventListener('change', () => { apply.disabled = !pending || !slot('review').checked; });

  async function research(input) {
    const requestData = payload(input), signature = JSON.stringify(requestData);
    const requestGeneration = ++generation;
    controller?.abort();
    controller = new AbortController();
    const currentController = controller;
    const timeout = setTimeout(() => currentController.abort(), 330000);
    pending = null;
    slot('review').checked = false;
    apply.disabled = true;
    slot('result').hidden = true;
    document.getElementById('field-ai-title').textContent = 'Documentare AI · ' + label(input);
    slot('context').textContent = requestData.protocol.title + ' · ' + requestData.protocol.modality.toUpperCase() + ' · ' + requestData.field.section;
    slot('status').className = '';
    slot('status').textContent = 'Se caută surse și se verifică potrivirea cu acest câmp…';
    if (!dialog.open) dialog.showModal();
    try {
      const response = await fetch('/api/ai/field-research', {method: 'POST',
        headers: {'Content-Type': 'application/json'}, body: signature, signal: currentController.signal});
      const data = await response.json();
      if (requestGeneration !== generation) return;
      if (!response.ok) throw Error(data.error || 'Căutarea AI nu a reușit.');
      const supported = data.status === 'supported' && typeof data.suggestion === 'string' && data.suggestion.trim() && data.sources?.length;
      slot('status').textContent = supported ? 'Propunere cu surse — necesită revizuire clinică.' : 'Dovezi insuficiente pentru o valoare de aplicat.';
      slot('suggestion').textContent = data.suggestion || 'Nicio valoare propusă.';
      slot('explanation').textContent = data.explanation;
      addTextList(slot('limitations'), [...(data.limitations || []), 'Citările nu garantează corectitudinea clinică; verifică documentele originale și condițiile locale.']);
      slot('sources').replaceChildren();
      for (const source of data.sources || []) {
        if (!safeLink(source.url)) continue;
        const li = document.createElement('li'), a = document.createElement('a');
        a.href = source.url; a.target = '_blank'; a.rel = 'noopener noreferrer';
        a.textContent = (source.title || new URL(source.url).hostname) + ' — ' + new URL(source.url).hostname;
        li.append(a); slot('sources').append(li);
        if (source.evidence) {
          const quote = document.createElement('p');
          quote.textContent = 'Fragment verificat în sursă: „' + source.evidence + '”';
          li.append(quote);
        }
      }
      slot('engine').textContent = data.engine ? `${data.engine} · Căutare: ${new Date(data.searched_at).toLocaleString('ro-RO')}` : '';
      slot('search-entry').replaceChildren();
      if (data.search_html) {
        const iframe = document.createElement('iframe');
        iframe.title = 'Sugestii Google Search';
        iframe.setAttribute('sandbox', 'allow-popups allow-popups-to-escape-sandbox');
        iframe.srcdoc = data.search_html;
        slot('search-entry').append(iframe);
      }
      slot('result').hidden = false;
      slot('review').disabled = !supported;
      if (supported) pending = {input, signature, suggestion: data.suggestion};
    } catch (error) {
      if (requestGeneration !== generation) return;
      slot('status').className = 'field-ai-error';
      slot('status').textContent = error.name === 'AbortError' ? 'Căutarea a depășit timpul disponibil. Reîncearcă.' : error.message;
    } finally { clearTimeout(timeout); }
  }
  apply.addEventListener('click', () => {
    if (!pending || !slot('review').checked) return;
    const {input, signature, suggestion} = pending;
    if (!input.isConnected || !visible(input) || input.readOnly || input.disabled || JSON.stringify(payload(input)) !== signature) {
      slot('status').textContent = 'Câmpul sau contextul s-a schimbat. Închide și repetă căutarea pentru versiunea curentă.';
      apply.disabled = true; pending = null; return;
    }
    if (input.options && !Array.from(input.options).some(o => o.value === suggestion)) return;
    if (input.type === 'radio' || input.type === 'checkbox' || input.type === 'file') return;
    input.value = suggestion;
    input.dispatchEvent(new Event('input', {bubbles: true}));
    input.dispatchEvent(new Event('change', {bubbles: true}));
    input.classList.add('apply-highlight');
    pending = null; apply.disabled = true; slot('review').disabled = true;
    slot('status').textContent = 'Propunerea a fost aplicată în formular. Verifică și salvează protocolul când este pregătit.';
  });
  function wire(root) {
    const inputs = [...(root.matches?.(selector) ? [root] : []), ...root.querySelectorAll(selector)];
    for (const input of inputs) {
      if (wired.has(input) || input.readOnly || input.disabled) continue;
      wired.add(input);
      const button = document.createElement('button');
      button.type = 'button'; button.className = 'field-ai-button'; button.textContent = 'Caută cu AI';
      button.setAttribute('aria-label', 'Caută cu AI: ' + label(input));
      button.addEventListener('click', () => research(input));
      input.insertAdjacentElement('afterend', button);
    }
  }
  wire(form);
  new MutationObserver(records => {
    for (const record of records) for (const node of record.addedNodes) if (node.nodeType === 1) wire(node);
  }).observe(form, {childList: true, subtree: true});
})();
