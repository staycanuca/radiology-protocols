(function () {
  'use strict';

  // ─── Helpers ────────────────────────────────────────────────────────────────

  var MODALITY_LABELS = {
    'ct': '⚡ CT - Tomografie Computerizată',
    'irm': '🧲 IRM - Rezonanță Magnetică',
    'rx': '📷 RX - Radiologie Clasică',
    'eco': '📡 US - Ecografie (Ultrasonografie)',
    'fluoro': '✨ FLOURO - Fluoroscopie & C-Arm'
  };

  var MODALITY_SHORT = {
    'ct': 'CT',
    'irm': 'IRM',
    'rx': 'RX',
    'eco': 'US',
    'fluoro': 'FLOURO'
  };

  function getModalityName(mod) {
    var m = (mod || 'ct').toLowerCase();
    return MODALITY_LABELS[m] || m.toUpperCase();
  }

  function getBasePath(pathname) {
    var parts = pathname.split('/request-change');
    return parts[0] || '';
  }

  function getParam(name) {
    var params = new URLSearchParams(window.location.search);
    return params.get(name);
  }

  function slugify(text) {
    return text
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-|-$/g, '');
  }

  function arrayToLines(arr) {
    if (!arr || !Array.isArray(arr)) return '';
    return arr.join('\n');
  }

  function linesToArray(str) {
    return (str || '')
      .split('\n')
      .map(function (s) { return s.trim(); })
      .filter(function (s) { return s.length > 0; });
  }

  function val(id) {
    var el = document.getElementById(id);
    return el ? el.value : '';
  }

  function setVal(id, value) {
    var el = document.getElementById(id);
    if (el) el.value = value || '';
  }

  // ─── Button injection on protocol pages across ALL modalities ───────────────

  function injectProtocolButton() {
    if (document.getElementById('rc-app')) return;

    var path = window.location.pathname;
    // Matches /<modality>/<category>/<slug>/ where modality in (ct, rx, irm, eco, fluoro)
    var match = path.match(/^(.*(?:\/ct|\/rx|\/irm|\/eco|\/fluoro)\/[^/]+\/)([^/]+)\/?$/);
    if (!match) return;

    var beforeSlug = match[1];
    var slug = match[2];
    if (slug === 'index' || slug === 'compare') return;

    var modMatch = beforeSlug.match(/^(.*?)(?:\/ct|\/rx|\/irm|\/eco|\/fluoro)\//);
    var base = modMatch ? modMatch[1] : '';

    var h1 = document.querySelector('article h1');
    if (!h1) return;

    var link = document.createElement('a');
    link.href = base + '/request-change/?protocol=' + encodeURIComponent(slug);
    link.textContent = 'Solicită o Modificare';
    link.className = 'rc-request-btn';
    link.style.cssText = [
      'display:inline-block',
      'flex-shrink:0',
      'margin-left:1rem',
      'padding:0.3rem 0.85rem',
      'border:1px solid #1565c0',
      'color:#1565c0',
      'background:#f0f7ff',
      'border-radius:6px',
      'font-size:0.75rem',
      'font-weight:600',
      'text-decoration:none',
      'white-space:nowrap',
      'align-self:center',
      'box-shadow:0 1px 3px rgba(0,0,0,0.06)'
    ].join(';');

    h1.style.cssText = 'display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;';
    h1.appendChild(link);
  }

  // ─── Series row helpers ──────────────────────────────────────────────────────

  function makeSeriesRow(s) {
    s = s || {};
    var row = document.createElement('div');
    row.className = 'rc-series-row';
    row.style.cssText = 'display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1fr 2fr auto;gap:0.4rem;margin-bottom:0.4rem;align-items:center;';

    var fields = [
      { name: 'name', placeholder: 'Nume serie / Secvență / Incidență', value: s.name || '' },
      { name: 'start', placeholder: 'Început / Plan', value: s.start || '' },
      { name: 'end', placeholder: 'Sfârșit / Parametri', value: s.end || '' },
      { name: 'delay', placeholder: 'Întârziere / Fază', value: s.delay || '' },
      { name: 'thickness', placeholder: 'Grosime / Gap', value: s.thickness || '' },
      { name: 'notes', placeholder: 'Note serie', value: s.notes || '' }
    ];

    fields.forEach(function (f) {
      var input = document.createElement('input');
      input.type = 'text';
      input.className = 'rc-series-field';
      input.dataset.field = f.name;
      input.placeholder = f.placeholder;
      input.value = f.value;
      input.style.cssText = 'padding:0.35rem 0.5rem;border:1px solid #ccc;border-radius:4px;font-size:0.85rem;width:100%;box-sizing:border-box;';
      row.appendChild(input);
    });

    var delBtn = document.createElement('button');
    delBtn.type = 'button';
    delBtn.textContent = '✕';
    delBtn.title = 'Șterge seria';
    delBtn.style.cssText = 'padding:0.3rem 0.6rem;background:#fee2e2;color:#b91c1c;border:1px solid #fca5a5;border-radius:4px;cursor:pointer;font-size:0.85rem;font-weight:bold;';
    delBtn.addEventListener('click', function () {
      row.remove();
    });
    row.appendChild(delBtn);

    return row;
  }

  function getSeriesRows() {
    var rows = document.querySelectorAll('#rc-series-container .rc-series-row');
    var result = [];
    rows.forEach(function (row) {
      var obj = {};
      row.querySelectorAll('.rc-series-field').forEach(function (input) {
        obj[input.dataset.field] = input.value.trim();
      });
      result.push(obj);
    });
    return result;
  }

  function populateSeries(seriesArr) {
    var container = document.getElementById('rc-series-container');
    if (!container) return;
    container.innerHTML = '';
    (seriesArr || []).forEach(function (s) {
      container.appendChild(makeSeriesRow(s));
    });
  }

  // ─── Form population & clear ─────────────────────────────────────────────────

  function clearForm() {
    setVal('rc-title', '');
    setVal('rc-slug', '');
    setVal('rc-category', '');
    setVal('rc-position', '');
    setVal('rc-npo', '');
    setVal('rc-indications', '');
    setVal('rc-premedication', '');

    setVal('rc-agent', '');
    setVal('rc-volume', '');
    setVal('rc-flow-rate', '');
    setVal('rc-duration', '');
    setVal('rc-timing', '');
    setVal('rc-roi', '');
    setVal('rc-trigger', '');

    populateSeries([]);

    setVal('rc-tech', '');
    setVal('rc-nursing', '');
    setVal('rc-rad', '');
    setVal('rc-tips', '');

    setVal('rc-renal', '');
    setVal('rc-allergy', '');
    setVal('rc-free-text', '');
  }

  function populateForm(protocol) {
    if (!protocol) {
      clearForm();
      return;
    }
    setVal('rc-title', protocol.title || '');
    setVal('rc-slug', protocol.slug || '');
    setVal('rc-category', protocol.category || '');
    setVal('rc-position', protocol.position || '');
    setVal('rc-npo', protocol.npo || '');
    setVal('rc-indications', arrayToLines(protocol.clinical_indications));
    setVal('rc-premedication', protocol.premedication || '');

    var contrast = protocol.contrast || {};
    setVal('rc-agent', contrast.agent || '');
    setVal('rc-volume', contrast.volume || '');
    setVal('rc-flow-rate', contrast.flow_rate || '');
    setVal('rc-duration', contrast.duration || '');
    setVal('rc-timing', contrast.timing || '');
    setVal('rc-roi', contrast.roi || '');
    setVal('rc-trigger', contrast.trigger || '');

    populateSeries(protocol.series || []);

    var notes = protocol.notes || {};
    setVal('rc-tech', notes.tech || '');
    setVal('rc-nursing', notes.nursing || '');
    setVal('rc-rad', notes.rad || '');
    setVal('rc-tips', notes.tips || '');

    var safety = protocol.safety || {};
    setVal('rc-renal', safety.renal || '');
    setVal('rc-allergy', safety.allergy || '');
  }

  function readFormValues() {
    return {
      title: val('rc-title'),
      slug: val('rc-slug'),
      category: val('rc-category'),
      position: val('rc-position'),
      npo: val('rc-npo'),
      clinical_indications: linesToArray(val('rc-indications')),
      premedication: val('rc-premedication'),
      contrast: {
        agent: val('rc-agent'),
        volume: val('rc-volume'),
        flow_rate: val('rc-flow-rate'),
        duration: val('rc-duration'),
        timing: val('rc-timing'),
        roi: val('rc-roi'),
        trigger: val('rc-trigger'),
      },
      series: getSeriesRows(),
      notes: {
        tech: val('rc-tech'),
        nursing: val('rc-nursing'),
        rad: val('rc-rad'),
        tips: val('rc-tips'),
      },
      safety: {
        renal: val('rc-renal'),
        allergy: val('rc-allergy'),
      },
      free_text: val('rc-free-text'),
    };
  }

  // ─── Diff logic ──────────────────────────────────────────────────────────────

  var FIELD_KEYS = {
    'Title': 'title', 'Category': 'category', 'Position': 'position',
    'NPO': 'npo', 'Clinical Indications': 'indications_json',
    'Premedication': 'premedication',
    'Contrast Agent': 'contrast_agent', 'Contrast Volume': 'contrast_volume',
    'Flow Rate': 'contrast_flow_rate', 'Duration': 'contrast_duration',
    'Timing': 'contrast_timing', 'ROI': 'contrast_roi', 'Trigger': 'contrast_trigger',
    'Series': 'series_json',
    'Tech Notes': 'notes_tech', 'Nursing Notes': 'notes_nursing',
    'Radiologist Notes': 'notes_rad', 'Tips': 'notes_tips',
    'Renal / Protecție': 'safety_renal', 'Allergy': 'safety_allergy'
  };

  function diffValues(original, current) {
    var changes = [];

    function addChange(label, origVal, newVal) {
      var o = (origVal === undefined || origVal === null) ? '' : String(origVal).trim();
      var n = (newVal === undefined || newVal === null) ? '' : String(newVal).trim();
      if (o !== n) {
        changes.push({ label: label, key: FIELD_KEYS[label] || label, original: o, proposed: n });
      }
    }

    addChange('Title', original.title, current.title);
    addChange('Category', original.category, current.category);
    addChange('Position', original.position, current.position);
    addChange('NPO', original.npo, current.npo);

    var origIndic = arrayToLines(original.clinical_indications || []);
    addChange('Clinical Indications', origIndic, val('rc-indications'));

    addChange('Premedication', original.premedication, current.premedication);

    var oc = original.contrast || {};
    addChange('Contrast Agent', oc.agent, current.contrast.agent);
    addChange('Contrast Volume', oc.volume, current.contrast.volume);
    addChange('Flow Rate', oc.flow_rate, current.contrast.flow_rate);
    addChange('Duration', oc.duration, current.contrast.duration);
    addChange('Timing', oc.timing, current.contrast.timing);
    addChange('ROI', oc.roi, current.contrast.roi);
    addChange('Trigger', oc.trigger, current.contrast.trigger);

    var origSeries = JSON.stringify(original.series || []);
    var newSeries = JSON.stringify(current.series || []);
    if (origSeries !== newSeries) {
      changes.push({ label: 'Series', key: 'series_json', original: origSeries, proposed: newSeries });
    }

    var on = original.notes || {};
    addChange('Tech Notes', on.tech, current.notes.tech);
    addChange('Nursing Notes', on.nursing, current.notes.nursing);
    addChange('Radiologist Notes', on.rad, current.notes.rad);
    addChange('Tips', on.tips, current.notes.tips);

    var os = original.safety || {};
    addChange('Renal / Protecție', os.renal, current.safety.renal);
    addChange('Allergy', os.allergy, current.safety.allergy);

    return changes;
  }

  // ─── Formatting ─────────────────────────────────────────────────────────────

  function formatChangeBody(protocol, changes, freeText) {
    var lines = [
      '**Protocol:** ' + protocol.title,
      '**Modalitate:** ' + getModalityName(protocol.modality),
      '**Slug:** ' + protocol.slug,
      '**Categorie:** ' + (protocol.category || ''),
      '',
    ];

    if (freeText && changes.length === 0) {
      lines.push('## Note de la Solicitant', '', '> ' + freeText.replace(/\n/g, '\n> '), '');
    }

    lines.push('## Modificări Solicitate', '');

    if (changes.length === 0) {
      lines.push('_(Nicio modificare de câmp specificată — consultați notele de mai sus)_', '');
    }

    changes.forEach(function (c) {
      lines.push('**' + c.label + '**');
      lines.push('- Valoare Actuală: ' + (c.original || '(necompletat)'));
      lines.push('- Valoare Propusă: ' + (c.proposed || '(necompletat)'));
      lines.push('');
    });

    if (freeText && changes.length > 0) {
      lines.push('## Note / Motivație Suplimentară', '', freeText);
    }

    return lines.join('\n');
  }

  function formatNewProtocolBody(baseProtocol, current, modality) {
    var lines = [
      '**Solicitare Protocol Nou**',
      '**Modalitate:** ' + getModalityName(modality),
      '**Protocol de Bază (referință):** ' + (baseProtocol ? baseProtocol.title : '(niciunul - de la zero)'),
      '',
      '## Detalii Protocol',
      '',
      '**Titlu:** ' + current.title,
      '**Slug:** ' + current.slug,
      '**Categorie:** ' + current.category,
      '**Indicații Clinice:** ' + (current.clinical_indications || []).join(', '),
      '**Poziție Pacient:** ' + current.position,
      '**Instrucțiuni NPO:** ' + current.npo,
      '**Pregătire / Premedicație:** ' + current.premedication,
      '',
      '## Substanță de Contrast / Tehnologie',
      '**Agent:** ' + current.contrast.agent,
      '**Volum:** ' + current.contrast.volume,
      '**Rată de Flux:** ' + current.contrast.flow_rate,
      '**Durată:** ' + current.contrast.duration,
      '**Temporizare:** ' + current.contrast.timing,
      '**ROI:** ' + current.contrast.roi,
      '**Declanșator:** ' + current.contrast.trigger,
      '',
      '## Serii / Secvențe / Incidențe de Achiziție',
      JSON.stringify(current.series, null, 2),
      '',
      '## Note Clinice',
      '**Tehnician:** ' + current.notes.tech,
      '**Asistent:** ' + current.notes.nursing,
      '**Radiolog:** ' + current.notes.rad,
      '**Sfaturi & Recomandări:** ' + current.notes.tips,
      '',
      '## Siguranță & Radioprotecție',
      '**Ghidaj Renal / Protecție:** ' + current.safety.renal,
      '**Ghidaj Alergii:** ' + current.safety.allergy,
    ];

    if (current.free_text) {
      lines.push('', '## Note Suplimentare / Context', '', current.free_text);
    }

    return lines.join('\n');
  }

  // ─── Submission ─────────────────────────────────────────────────────────────

  function submitViaGoogleForm(formUrl, entryTitle, entryBody, subject, body) {
    var submitBtn = document.querySelector('.rc-submit-btn');
    if (submitBtn) { submitBtn.disabled = true; submitBtn.textContent = 'Se trimite…'; }

    var payload = entryTitle + '=' + encodeURIComponent(subject) +
                  '&' + entryBody + '=' + encodeURIComponent(body);

    fetch(formUrl, {
      method: 'POST',
      mode: 'no-cors',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: payload,
    }).then(function () {
      showMessage('Solicitarea a fost trimisă cu succes!', 'info');
      if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = 'Trimite Solicitarea'; }
    }).catch(function () {
      showMessage('Trimiterea a eșuat. Vă rugăm să încercați din nou sau să contactați direct responsabilul de protocoale.', 'error');
      if (submitBtn) { submitBtn.disabled = false; submitBtn.textContent = 'Trimite Solicitarea'; }
    });
  }

  function submitRequest(config, title, slug, body, modality) {
    var feedbackUrl  = config.feedback_url || '';
    var formUrl      = config.google_form_url || '';
    var entryTitle   = config.google_form_entry_title || '';
    var entryBody    = config.google_form_entry_body || '';
    var modTag = MODALITY_SHORT[modality] || (modality ? modality.toUpperCase() : 'RADIO');
    var subject = '[' + modTag + '] Solicitare Modificare Protocol: ' + title + ' (' + slug + ')';

    if (formUrl && entryTitle && entryBody) {
      submitViaGoogleForm(formUrl, entryTitle, entryBody, subject, body);
      return;
    }

    if (!feedbackUrl) {
      showMessage('Contactați direct responsabilul de protocoale.', 'info');
      return;
    }

    if (feedbackUrl.startsWith('mailto:')) {
      var mailUrl = feedbackUrl +
        '?subject=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(body);
      window.location.href = mailUrl;
      return;
    }

    if (feedbackUrl.indexOf('github.com') !== -1) {
      var issueUrl = feedbackUrl +
        '?title=' + encodeURIComponent(subject) +
        '&body=' + encodeURIComponent(body);
      window.open(issueUrl, '_blank');
      return;
    }

    showMessage('Contactați direct responsabilul de protocoale.', 'info');
  }

  function showMessage(msg, type) {
    var el = document.getElementById('rc-message');
    if (!el) return;
    el.textContent = msg;
    el.style.display = 'block';
    el.className = 'rc-message rc-message--' + (type || 'info');
  }

  // ─── Form Builder with 2 Dynamic Selectors ───────────────────────────────────

  function buildApp(protocols, config, initialProtocol) {
    var app = document.getElementById('rc-app');
    app.innerHTML = '';

    var activeProtocol = initialProtocol || null;
    var activeModality = initialProtocol ? (initialProtocol.modality || 'ct').toLowerCase() : '';

    var style = document.createElement('style');
    style.textContent = [
      '.rc-form { max-width: 920px; }',
      '.rc-fieldset { border: 1px solid var(--md-default-fg-color--lightest, #ddd); border-radius: 8px; padding: 1.2rem 1.4rem; margin-bottom: 1.5rem; background: var(--md-default-bg-color, #ffffff); box-shadow: 0 1px 3px rgba(0,0,0,0.04); }',
      '.rc-fieldset legend { font-weight: 700; padding: 0 0.6rem; color: var(--md-primary-fg-color, #1a237e); font-size: 1rem; }',
      '.rc-field-group { display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 0.75rem; }',
      '.rc-field-group.single { grid-template-columns: 1fr; }',
      '.rc-field { display: flex; flex-direction: column; gap: 0.35rem; }',
      '.rc-field label { font-size: 0.85rem; font-weight: 600; color: var(--md-default-fg-color, #212529); }',
      '.rc-field input, .rc-field textarea, .rc-field select { padding: 0.5rem 0.75rem; border: 1px solid var(--md-default-fg-color--lightest, #ccc); border-radius: 6px; font-size: 0.92rem; width: 100%; box-sizing: border-box; background: var(--md-default-bg-color, #fff); color: var(--md-default-fg-color, #000); transition: border-color 0.2s; }',
      '.rc-field input:focus, .rc-field textarea:focus, .rc-field select:focus { border-color: var(--md-accent-fg-color, #1565c0); outline: none; }',
      '.rc-field textarea { resize: vertical; min-height: 80px; }',
      '.rc-series-header { display: grid; grid-template-columns: 2fr 1fr 1fr 1fr 1fr 2fr auto; gap: 0.4rem; margin-bottom: 0.4rem; }',
      '.rc-series-header span { font-size: 0.75rem; font-weight: 700; color: var(--md-default-fg-color--light, #555); }',
      '.rc-add-series-btn { margin-top: 0.75rem; padding: 0.4rem 1rem; background: #e8eaf6; color: #1a237e; border: 1px solid #c5cae9; border-radius: 6px; cursor: pointer; font-size: 0.85rem; font-weight: 600; transition: all 0.2s; }',
      '.rc-add-series-btn:hover { background: #c5cae9; }',
      '.rc-submit-btn { padding: 0.7rem 2rem; background: var(--md-primary-fg-color, #1a237e); color: #fff; border: none; border-radius: 6px; cursor: pointer; font-size: 1rem; font-weight: 600; transition: opacity 0.2s; box-shadow: 0 2px 6px rgba(0,0,0,0.15); }',
      '.rc-submit-btn:hover { opacity: 0.92; }',
      '.rc-message { display: none; padding: 0.85rem 1.2rem; border-radius: 6px; margin-top: 1.2rem; font-size: 0.95rem; }',
      '.rc-message--info { background: #e3f2fd; color: #1565c0; border: 1px solid #90caf9; }',
      '.rc-message--error { background: #ffebee; color: #b71c1c; border: 1px solid #ef9a9a; }',
      '.rc-protocol-badge { background: #f0fdf4; border: 1px solid #86efac; border-radius: 6px; padding: 0.75rem 1rem; margin-top: 0.75rem; font-size: 0.92rem; color: #166534; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 8px; }',
      '.rc-badge-pill { background: #dcfce7; border: 1px solid #bbf7d0; padding: 0.2rem 0.6rem; border-radius: 4px; font-weight: 700; font-size: 0.8rem; }',
      '@media (max-width: 600px) { .rc-field-group { grid-template-columns: 1fr; } .rc-series-header { display: none; } .rc-series-row { grid-template-columns: 1fr !important; } }'
    ].join('\n');
    app.appendChild(style);

    var form = document.createElement('form');
    form.className = 'rc-form';
    form.id = 'rc-form';

    // ── 1. Selector Fieldset with TWO Selectors ──────────────────────────────
    var selectorFS = document.createElement('fieldset');
    selectorFS.className = 'rc-fieldset';
    var selectorLeg = document.createElement('legend');
    selectorLeg.textContent = '1. Selectare Modalitate & Protocol';
    selectorFS.appendChild(selectorLeg);

    var selGroup = document.createElement('div');
    selGroup.className = 'rc-field-group';

    // Selector 1: Modalitate
    var modField = document.createElement('div');
    modField.className = 'rc-field';
    var modLabel = document.createElement('label');
    modLabel.textContent = 'Selector 1: Modalitate Imagistică';
    modLabel.htmlFor = 'rc-modality-select';

    var modSelect = document.createElement('select');
    modSelect.id = 'rc-modality-select';

    var allModOpt = document.createElement('option');
    allModOpt.value = '';
    allModOpt.textContent = '-- Toate Modalitățile --';
    modSelect.appendChild(allModOpt);

    [
      { value: 'ct', label: '⚡ CT (Tomografie Computerizată)' },
      { value: 'irm', label: '🧲 IRM (Rezonanță Magnetică)' },
      { value: 'rx', label: '📷 RX (Radiologie Clasică)' },
      { value: 'eco', label: '📡 US (Ecografie & Ultrasonografie)' },
      { value: 'fluoro', label: '✨ FLOURO (Fluoroscopie & C-Arm)' }
    ].forEach(function (m) {
      var opt = document.createElement('option');
      opt.value = m.value;
      opt.textContent = m.label;
      modSelect.appendChild(opt);
    });

    modField.appendChild(modLabel);
    modField.appendChild(modSelect);
    selGroup.appendChild(modField);

    // Selector 2: Protocol
    var protField = document.createElement('div');
    protField.className = 'rc-field';
    var protLabel = document.createElement('label');
    protLabel.textContent = 'Selector 2: Protocol spre Modificare';
    protLabel.htmlFor = 'rc-protocol-select';

    var protSelect = document.createElement('select');
    protSelect.id = 'rc-protocol-select';

    protField.appendChild(protLabel);
    protField.appendChild(protSelect);
    selGroup.appendChild(protField);

    selectorFS.appendChild(selGroup);

    // Protocol status badge
    var badge = document.createElement('div');
    badge.id = 'rc-selected-protocol-badge';
    badge.className = 'rc-protocol-badge';
    badge.style.display = 'none';
    selectorFS.appendChild(badge);

    form.appendChild(selectorFS);

    // Helper to populate Selector 2 options based on selected modality
    function refreshProtocolSelector(filterModality, preserveSlug) {
      protSelect.innerHTML = '';

      var defaultOpt = document.createElement('option');
      defaultOpt.value = '';
      defaultOpt.textContent = '-- Alege un Protocol spre Modificare --';
      protSelect.appendChild(defaultOpt);

      var newOpt = document.createElement('option');
      newOpt.value = '__new__';
      newOpt.textContent = '➕ Protocol Nou (începe de la zero)';
      protSelect.appendChild(newOpt);

      var filtered = protocols.filter(function (p) {
        if (!filterModality) return true;
        return (p.modality || '').toLowerCase() === filterModality.toLowerCase();
      });

      // Group filtered protocols by category
      var byCategory = {};
      filtered.forEach(function (p) {
        var catKey = (p.category || 'Altele');
        if (!filterModality) {
          catKey = (MODALITY_SHORT[p.modality] || p.modality || 'CT').toUpperCase() + ' - ' + catKey;
        }
        if (!byCategory[catKey]) byCategory[catKey] = [];
        byCategory[catKey].push(p);
      });

      Object.keys(byCategory).sort().forEach(function (cat) {
        var optgroup = document.createElement('optgroup');
        optgroup.label = cat.charAt(0).toUpperCase() + cat.slice(1);
        byCategory[cat].forEach(function (p) {
          var opt = document.createElement('option');
          opt.value = p.slug;
          opt.textContent = p.title + (filterModality ? '' : ' [' + (MODALITY_SHORT[p.modality] || p.modality).toUpperCase() + ']');
          optgroup.appendChild(opt);
        });
        protSelect.appendChild(optgroup);
      });

      if (preserveSlug) {
        protSelect.value = preserveSlug;
      }
    }

    function updateBadge(protocol, isNew) {
      if (isNew) {
        badge.style.display = 'flex';
        badge.style.background = '#eff6ff';
        badge.style.borderColor = '#93c5fd';
        badge.style.color = '#1e40af';
        badge.innerHTML = '<span>➕ <strong>Mod: Creare Protocol Nou</strong> (completați formularul de mai jos)</span><span class="rc-badge-pill" style="background:#dbeafe;border-color:#bfdbfe;color:#1e40af;">Nou</span>';
      } else if (protocol) {
        badge.style.display = 'flex';
        badge.style.background = '#f0fdf4';
        badge.style.borderColor = '#86efac';
        badge.style.color = '#166534';
        badge.innerHTML = '<span>✏️ <strong>Protocol selectat:</strong> ' + protocol.title + '</span>' +
          '<span class="rc-badge-pill">' + getModalityName(protocol.modality) + ' &bull; ' + (protocol.category || '') + '</span>';
      } else {
        badge.style.display = 'none';
      }
    }

    // Event listener: Selector 1 (Modalitate)
    modSelect.addEventListener('change', function () {
      var chosenMod = this.value;
      var curSlug = protSelect.value;
      // If current protocol belongs to chosen modality, keep it, otherwise reset
      var keepSlug = '';
      if (curSlug && curSlug !== '__new__') {
        var found = protocols.find(function (p) { return p.slug === curSlug; });
        if (found && (!chosenMod || (found.modality || '').toLowerCase() === chosenMod.toLowerCase())) {
          keepSlug = curSlug;
        }
      }
      refreshProtocolSelector(chosenMod, keepSlug);

      if (keepSlug) {
        // Keep active protocol
      } else if (protSelect.value === '__new__') {
        updateBadge(null, true);
      } else {
        activeProtocol = null;
        clearForm();
        updateBadge(null, false);
      }
    });

    // Event listener: Selector 2 (Protocol)
    protSelect.addEventListener('change', function () {
      var selectedVal = this.value;
      if (!selectedVal) {
        activeProtocol = null;
        clearForm();
        updateBadge(null, false);
        return;
      }

      if (selectedVal === '__new__') {
        activeProtocol = null;
        clearForm();
        updateBadge(null, true);
        return;
      }

      var found = protocols.find(function (p) { return p.slug === selectedVal; });
      if (found) {
        activeProtocol = found;
        // Sync Selector 1 if currently "All"
        if (!modSelect.value && found.modality) {
          modSelect.value = found.modality.toLowerCase();
          refreshProtocolSelector(found.modality, found.slug);
        }
        populateForm(found);
        updateBadge(found, false);
      }
    });

    // Initialize selectors with initial values
    if (activeModality) {
      modSelect.value = activeModality;
    }
    refreshProtocolSelector(activeModality, activeProtocol ? activeProtocol.slug : '');

    // ── 2. Identification Fieldset ───────────────────────────────────────────
    form.appendChild(makeFieldset('2. Identificare Protocol', [
      makeField('rc-title', 'Titlu Protocol (obligatoriu)'),
      makeField('rc-slug', 'Slug (identificator unic URL)'),
      makeField('rc-category', 'Regiune Anatomică / Categorie'),
    ]));

    // Auto-generate slug from title for new protocols
    var titleInput = form.querySelector('#rc-title');
    if (titleInput) {
      titleInput.addEventListener('input', function () {
        if (!activeProtocol) {
          var slugInput = form.querySelector('#rc-slug');
          if (slugInput && !slugInput.dataset.userEdited) {
            slugInput.value = slugify(this.value);
          }
        }
      });
      var slugInput = form.querySelector('#rc-slug');
      if (slugInput) {
        slugInput.addEventListener('input', function () {
          this.dataset.userEdited = 'true';
        });
      }
    }

    // ── 3. Clinical Fieldset ─────────────────────────────────────────────────
    form.appendChild(makeFieldset('3. Indicații Clinice & Poziționare', [
      makeField('rc-indications', 'Indicații Clinice (câte una pe linie)', 'textarea'),
      makeField('rc-position', 'Poziție Pacient / Centrare'),
      makeField('rc-npo', 'Instrucțiuni NPO (repaus alimentar / hidratare)'),
    ]));

    // ── 4. Preparation Fieldset ──────────────────────────────────────────────
    form.appendChild(makeFieldset('4. Pregătire Pacient & Premedicație', [
      makeField('rc-premedication', 'Premedicație, Pregătire Specifică sau Contrast Oral', 'textarea', true),
    ]));

    // ── 5. Contrast & Acquisition Parameters ─────────────────────────────────
    form.appendChild(makeFieldset('5. Substanță de Contrast & Parametri Tehnici', [
      makeField('rc-agent', 'Substanță de Contrast / Agent / Sonda'),
      makeField('rc-volume', 'Volum / Doză / Kilovoltaj (kV)'),
      makeField('rc-flow-rate', 'Debit (Flow Rate) / mAs / Frecvență'),
      makeField('rc-duration', 'Durată Injectare / Timp Rotație'),
      makeField('rc-timing', 'Temporizare (Delay) / Fază / Declanșare'),
      makeField('rc-roi', 'Regiune de Interes (ROI) / Câmp'),
      makeField('rc-trigger', 'Prag Declanșare (Trigger) / Index'),
    ]));

    // ── 6. Series / Sequences / Projections ───────────────────────────────────
    var seriesFS = document.createElement('fieldset');
    seriesFS.className = 'rc-fieldset';
    var seriesLeg = document.createElement('legend');
    seriesLeg.textContent = '6. Serii / Secvențe / Incidențe de Achiziție';
    seriesFS.appendChild(seriesLeg);

    var headerDiv = document.createElement('div');
    headerDiv.className = 'rc-series-header';
    ['Nume Achiziție / Incidență', 'Început / Plan', 'Sfârșit / Parametri', 'Întârziere / Fază', 'Grosime / Gap', 'Note Achiziție', ''].forEach(function (h) {
      var span = document.createElement('span');
      span.textContent = h;
      headerDiv.appendChild(span);
    });
    seriesFS.appendChild(headerDiv);

    var container = document.createElement('div');
    container.id = 'rc-series-container';
    seriesFS.appendChild(container);

    var addBtn = document.createElement('button');
    addBtn.type = 'button';
    addBtn.className = 'rc-add-series-btn';
    addBtn.textContent = '+ Adaugă Serie / Incidență';
    addBtn.addEventListener('click', function () {
      container.appendChild(makeSeriesRow({}));
    });
    seriesFS.appendChild(addBtn);
    form.appendChild(seriesFS);

    // ── 7. Notes Fieldset ────────────────────────────────────────────────────
    form.appendChild(makeFieldset('7. Note Speciale & Recomandări', [
      makeField('rc-tech', 'Note Tehnician / Operator', 'textarea'),
      makeField('rc-nursing', 'Note Asistent Medical', 'textarea'),
      makeField('rc-rad', 'Note Medic Radiolog', 'textarea'),
      makeField('rc-tips', 'Sfaturi Tehnice & Bune Practici', 'textarea'),
    ]));

    // ── 8. Safety & Radioprotection ──────────────────────────────────────────
    form.appendChild(makeFieldset('8. Siguranță & Radioprotecție', [
      makeField('rc-renal', 'Ghidaj Renal / Protecție Gonadică / Sarcină / ALARA'),
      makeField('rc-allergy', 'Ghidaj Alergii / Contraindicații RMN / Siguranță'),
    ]));

    // ── 9. Free Text / Context ───────────────────────────────────────────────
    form.appendChild(makeFieldset('9. Note Suplimentare / Motivul Solicitării', [
      makeField('rc-free-text', 'Explicați succint contextul clinic sau motivele pentru care propuneți modificarea', 'textarea', true),
    ]));

    // ── Message Box ──────────────────────────────────────────────────────────
    var msg = document.createElement('div');
    msg.id = 'rc-message';
    msg.className = 'rc-message';
    form.appendChild(msg);

    // ── Submit Section ───────────────────────────────────────────────────────
    var submitWrap = document.createElement('div');
    submitWrap.style.cssText = 'margin-top:1.5rem;display:flex;align-items:center;gap:1rem;flex-wrap:wrap;';

    var submitBtn = document.createElement('button');
    submitBtn.type = 'submit';
    submitBtn.className = 'rc-submit-btn';
    submitBtn.textContent = 'Trimite Solicitarea spre Revizuire';
    submitWrap.appendChild(submitBtn);

    var resetBtn = document.createElement('button');
    resetBtn.type = 'button';
    resetBtn.textContent = 'Resetează Formularul';
    resetBtn.style.cssText = 'padding:0.7rem 1.2rem;background:#f1f5f9;color:#475569;border:1px solid #cbd5e1;border-radius:6px;cursor:pointer;font-size:0.95rem;font-weight:600;';
    resetBtn.addEventListener('click', function () {
      if (activeProtocol) {
        populateForm(activeProtocol);
      } else {
        clearForm();
      }
      showMessage('Formularul a fost resetat la valorile inițiale.', 'info');
    });
    submitWrap.appendChild(resetBtn);

    form.appendChild(submitWrap);

    // ── Submit Handler ───────────────────────────────────────────────────────
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var current = readFormValues();
      var chosenMod = modSelect.value || (activeProtocol ? activeProtocol.modality : 'ct');

      if (!activeProtocol || protSelect.value === '__new__') {
        // Mode: New protocol
        if (!current.title) {
          showMessage('Vă rugăm să introduceți un titlu pentru protocol.', 'error');
          return;
        }
        var baseProt = activeProtocol || null;
        var body = formatNewProtocolBody(baseProt, current, chosenMod);
        var title = 'Solicitare Protocol Nou: ' + current.title;
        var slug = current.slug || slugify(current.title);
        submitRequest(config, title, slug, body, chosenMod);
      } else {
        // Mode: Change request
        var original = activeProtocol;
        var changes = diffValues(original, current);
        var freeText = current.free_text;

        if (changes.length === 0 && !freeText) {
          showMessage('Nu au fost detectate modificări. Editați cel puțin un câmp sau adăugați o notă explicativă înainte de trimitere.', 'error');
          return;
        }

        var body = formatChangeBody(original, changes, freeText);
        var slug = original.slug || '';
        if (changes.length > 0) {
          var changesMap = {};
          changes.forEach(function (c) { if (c.key) { changesMap[c.key] = c.proposed; } });
          if (freeText) { changesMap['_notes'] = freeText; }
          var encoded = btoa(JSON.stringify(changesMap))
            .replace(/\+/g, '-').replace(/\//g, '_').replace(/=/g, '');
          body += '\n---\nDeschide în Panoul de Administrare: http://localhost:5173/edit/' + slug + '?apply=' + encoded;
        } else {
          body += '\n---\nDeschide în Panoul de Administrare: http://localhost:5173/edit/' + slug;
        }

        submitRequest(config, original.title || 'Protocol', slug, body, original.modality || chosenMod);
      }
    });

    app.appendChild(form);

    if (activeProtocol) {
      populateForm(activeProtocol);
      updateBadge(activeProtocol, false);
    }
  }

  function makeFieldset(legend, fields) {
    var fs = document.createElement('fieldset');
    fs.className = 'rc-fieldset';
    var leg = document.createElement('legend');
    leg.textContent = legend;
    fs.appendChild(leg);
    fields.forEach(function (f) { fs.appendChild(f); });
    return fs;
  }

  function makeField(id, labelText, type, fullWidth) {
    var wrapper = document.createElement('div');
    wrapper.className = 'rc-field-group' + (fullWidth || type === 'textarea' ? ' single' : '');

    var field = document.createElement('div');
    field.className = 'rc-field';

    var label = document.createElement('label');
    label.htmlFor = id;
    label.textContent = labelText;

    var input;
    if (type === 'textarea') {
      input = document.createElement('textarea');
    } else {
      input = document.createElement('input');
      input.type = 'text';
    }
    input.id = id;
    input.name = id;

    field.appendChild(label);
    field.appendChild(input);
    wrapper.appendChild(field);
    return wrapper;
  }

  // ─── Main form initializer ───────────────────────────────────────────────────

  function initForm() {
    var app = document.getElementById('rc-app');
    if (!app) return;

    var pathname = window.location.pathname;
    var base = getBasePath(pathname);

    var formsUrl = base + '/javascripts/protocol-forms-index.json';
    var configUrl = base + '/javascripts/institution-config.json';

    Promise.all([
      fetch(formsUrl).then(function (r) { return r.json(); }),
      fetch(configUrl).then(function (r) { return r.json(); }),
    ]).then(function (results) {
      var protocols = results[0] || [];
      var config = results[1] || {};

      var protocolSlug = getParam('protocol');
      var preselectedProtocol = null;
      if (protocolSlug) {
        preselectedProtocol = protocols.find(function (p) { return p.slug === protocolSlug; }) || null;
      }

      buildApp(protocols, config, preselectedProtocol);
    }).catch(function (err) {
      console.error('rc: failed to load data', err);
      app.innerHTML = '<p style="color:#b91c1c;">Nu s-au putut încărca datele formularului. Vă rugăm să reîncărcați pagina sau să contactați administratorul.</p>';
    });
  }

  // ─── Entry point ─────────────────────────────────────────────────────────────

  document.addEventListener('DOMContentLoaded', function () {
    injectProtocolButton();
    initForm();
  });

})();
