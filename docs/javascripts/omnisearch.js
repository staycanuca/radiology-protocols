/**
 * omnisearch.js — Motor de căutare instantanee și filtrare cu chips pentru Ghidul Protocoalelor
 * Mobile-first, stil minimalist, paletă calmă pastel (bleu, verde pastel, alb), fonturi rotunjite.
 */

(function () {
  'use strict';

  let allProtocols = [];
  let activeModality = 'all';
  let activeCategory = 'all';
  let activeContrast = 'all';
  let searchQuery = '';
  let visibleCount = 24;

  const MODALITY_LABELS = {
    all: 'Toate',
    ct: '⚡ CT',
    irm: '🧲 IRM',
    rx: '📷 RX',
    eco: '📡 US / Eco',
    fluoro: '✨ Fluoro'
  };

  const CATEGORY_LABELS = {
    all: 'Toate Regiunile',
    abdomen: 'Abdomen & Pelvis',
    chest: 'Torace & Plămân',
    cardiac: 'Cardiac & Coronar',
    neuro: 'Neurologie & Cap',
    vascular: 'Vascular & Angio',
    msk: 'Musculoscheletic',
    pediatrie: 'Pediatrie',
    trauma: 'Traumă & Urgențe'
  };

  function removeDiacritics(str) {
    if (!str) return '';
    return str.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
  }

  function getBaseUrl() {
    let basePath = '';
    const configScript = document.getElementById('__config');
    if (configScript) {
      try {
        const cfg = JSON.parse(configScript.textContent);
        if (cfg.base) basePath = cfg.base.replace(/\/?$/, '/');
      } catch (e) {}
    }
    return basePath || '/radiology-protocols/';
  }

  async function loadProtocols() {
    const basePath = getBaseUrl();
    const candidateUrls = [
      basePath + 'javascripts/omnisearch-index.json',
      '/radiology-protocols/javascripts/omnisearch-index.json',
      '/javascripts/omnisearch-index.json',
      'javascripts/omnisearch-index.json'
    ];

    for (const url of candidateUrls) {
      try {
        const res = await fetch(url);
        if (res.ok) {
          allProtocols = await res.json();
          console.log(`[OmniSearch] S-au încărcat ${allProtocols.length} protocoale.`);
          updateModalityCounts();
          render();
          return;
        }
      } catch (e) {}
    }
    console.warn('[OmniSearch] Nu s-a putut încărca omnisearch-index.json');
  }

  function updateModalityCounts() {
    const counts = { all: allProtocols.length, ct: 0, irm: 0, rx: 0, eco: 0, fluoro: 0 };
    for (const p of allProtocols) {
      if (counts[p.modality] !== undefined) {
        counts[p.modality]++;
      }
    }

    for (const [key, count] of Object.entries(counts)) {
      const btn = document.querySelector(`.omni-mod-chip[data-mod="${key}"]`);
      if (btn) {
        btn.innerHTML = `${MODALITY_LABELS[key]} <span class="omni-chip-count">${count}</span>`;
      }
    }
  }

  function filterProtocols() {
    const q = removeDiacritics(searchQuery.trim());
    const queryTokens = q ? q.split(/\s+/).filter(Boolean) : [];

    return allProtocols.filter(p => {
      // 1. Modality filter
      if (activeModality !== 'all' && p.modality !== activeModality) {
        return false;
      }

      // 2. Category filter
      if (activeCategory !== 'all' && p.category !== activeCategory) {
        return false;
      }

      // 3. Contrast filter
      if (activeContrast === 'contrast' && !p.contrast) {
        return false;
      }
      if (activeContrast === 'native' && p.contrast) {
        return false;
      }

      // 4. Text search matching
      if (queryTokens.length > 0) {
        const searchableText = removeDiacritics(
          `${p.title} ${p.scanner} ${p.category} ${p.raw_category || ''} ${(p.indications || []).join(' ')} ${(p.synonyms || []).join(' ')}`
        );
        for (const token of queryTokens) {
          if (!searchableText.includes(token)) {
            return false;
          }
        }
      }

      return true;
    });
  }

  function render() {
    const container = document.getElementById('omnisearch-results');
    const countBadge = document.getElementById('omnisearch-count-badge');
    const clearBtn = document.getElementById('omnisearch-clear');
    if (!container) return;

    if (clearBtn) {
      clearBtn.style.display = searchQuery ? 'flex' : 'none';
    }

    const filtered = filterProtocols();
    const isFiltering = searchQuery.trim() !== '' || activeModality !== 'all' || activeCategory !== 'all' || activeContrast !== 'all';

    if (countBadge) {
      countBadge.textContent = `${filtered.length} protocoale găsite`;
    }

    // Daca utilizatorul nu cauta nimic si nu a setat filtre specifice, afisam un modul discret de pornire rapida
    if (!isFiltering) {
      container.innerHTML = `
        <div class="omni-idle-banner">
          <div class="omni-idle-icon">💡</div>
          <div class="omni-idle-text">
            <strong>Căutare instantanee în 1.667 de protocoale</strong>
            <span>Tastați o afecțiune (ex: <em>TEP, AVC, Pancreas, Hidrocefalie</em>), alegeți o modalitate sau o regiune anatomică mai sus.</span>
          </div>
        </div>
      `;
      return;
    }

    if (filtered.length === 0) {
      container.innerHTML = `
        <div class="omni-empty-state">
          <div class="omni-empty-icon">🔍</div>
          <h3>Niciun protocol găsit</h3>
          <p>Nu am găsit niciun rezultat pentru criteriile selectate. Încercați cuvinte cheie mai generale sau resetați filtrele.</p>
          <button type="button" class="omni-btn-reset" id="omni-reset-all">Resetează toate filtrele</button>
        </div>
      `;
      const resetBtn = document.getElementById('omni-reset-all');
      if (resetBtn) {
        resetBtn.addEventListener('click', resetFilters);
      }
      return;
    }

    const basePath = getBaseUrl();
    const toShow = filtered.slice(0, visibleCount);

    const cardsHtml = toShow.map(p => {
      const fullUrl = basePath + p.url.replace(/^\//, '');
      const modLabel = MODALITY_LABELS[p.modality] || p.modality.toUpperCase();
      const catLabel = CATEGORY_LABELS[p.category] || p.category;
      const contrastBadge = p.contrast 
        ? '<span class="omni-badge omni-badge-contrast">💧 Contrast IV</span>' 
        : '<span class="omni-badge omni-badge-native">🌿 Nativ</span>';
      
      const scannerBadge = p.scanner && p.scanner !== 'Standard' 
        ? `<span class="omni-badge omni-badge-scanner">${p.scanner}</span>` 
        : '';

      const indicationSnippet = (p.indications && p.indications.length > 0)
        ? `<div class="omni-card-indications">${p.indications[0]}</div>`
        : '';

      return `
        <a href="${fullUrl}" class="omni-card omni-card-${p.modality}">
          <div class="omni-card-header">
            <span class="omni-badge omni-badge-mod omni-badge-mod-${p.modality}">${modLabel}</span>
            <span class="omni-badge omni-badge-cat">${catLabel}</span>
            ${contrastBadge}
            ${scannerBadge}
          </div>
          <h4 class="omni-card-title">${p.title}</h4>
          ${indicationSnippet}
          <div class="omni-card-footer">
            <span class="omni-card-action">Vezi Protocol ➔</span>
          </div>
        </a>
      `;
    }).join('');

    let loadMoreHtml = '';
    if (filtered.length > visibleCount) {
      loadMoreHtml = `
        <div class="omni-load-more-container">
          <button type="button" class="omni-load-more-btn" id="omni-load-more">
            Afișează încă 24 de protocoale (rămase: ${filtered.length - visibleCount})
          </button>
        </div>
      `;
    }

    container.innerHTML = `
      <div class="omni-cards-grid">
        ${cardsHtml}
      </div>
      ${loadMoreHtml}
    `;

    const loadMoreBtn = document.getElementById('omni-load-more');
    if (loadMoreBtn) {
      loadMoreBtn.addEventListener('click', () => {
        visibleCount += 24;
        render();
      });
    }
  }

  function resetFilters() {
    searchQuery = '';
    activeModality = 'all';
    activeCategory = 'all';
    activeContrast = 'all';
    visibleCount = 24;

    const input = document.getElementById('omnisearch-input');
    if (input) input.value = '';

    document.querySelectorAll('.omni-mod-chip').forEach(c => {
      c.classList.toggle('active', c.dataset.mod === 'all');
    });
    document.querySelectorAll('.omni-cat-chip').forEach(c => {
      c.classList.toggle('active', c.dataset.cat === 'all');
    });
    document.querySelectorAll('.omni-contrast-chip').forEach(c => {
      c.classList.toggle('active', c.dataset.contrast === 'all');
    });

    render();
  }

  function initOmniSearch() {
    const root = document.getElementById('omnisearch-root');
    if (!root) return;

    root.innerHTML = `
      <div class="omni-container">
        <!-- Bara de Cautare Principala -->
        <div class="omni-search-wrapper">
          <span class="omni-search-icon">🔍</span>
          <input 
            type="text" 
            id="omnisearch-input" 
            class="omni-search-input" 
            placeholder="Caută după patologie, organ, procedură sau scaner (ex: TEP, AVC, Pancreas, Aquilion, TAVI)..." 
            autocomplete="off"
            spellcheck="false"
          >
          <button type="button" id="omnisearch-clear" class="omni-search-clear" title="Șterge textul">×</button>
        </div>

        <!-- Randul 1: Modalitati -->
        <div class="omni-chips-row omni-chips-modalities" aria-label="Filtru Modalitate">
          <button type="button" class="omni-chip omni-mod-chip active" data-mod="all">Toate</button>
          <button type="button" class="omni-chip omni-mod-chip" data-mod="ct">⚡ CT</button>
          <button type="button" class="omni-chip omni-mod-chip" data-mod="irm">🧲 IRM</button>
          <button type="button" class="omni-chip omni-mod-chip" data-mod="rx">📷 RX</button>
          <button type="button" class="omni-chip omni-mod-chip" data-mod="eco">📡 US / Eco</button>
          <button type="button" class="omni-chip omni-mod-chip" data-mod="fluoro">✨ Fluoro</button>
        </div>

        <!-- Randul 2: Regiuni Anatomice & Contrast -->
        <div class="omni-chips-row omni-chips-categories" aria-label="Filtru Regiune Anatomică">
          <button type="button" class="omni-chip omni-cat-chip active" data-cat="all">Toate Regiunile</button>
          <button type="button" class="omni-chip omni-cat-chip" data-cat="abdomen">Abdomen & Pelvis</button>
          <button type="button" class="omni-chip omni-cat-chip" data-cat="chest">Torace & Plămân</button>
          <button type="button" class="omni-chip omni-cat-chip" data-cat="cardiac">Cardiac & Coronar</button>
          <button type="button" class="omni-chip omni-cat-chip" data-cat="neuro">Neurologie & Cap</button>
          <button type="button" class="omni-chip omni-cat-chip" data-cat="vascular">Vascular & Angio</button>
          <button type="button" class="omni-chip omni-cat-chip" data-cat="msk">Musculoscheletic</button>
          <button type="button" class="omni-chip omni-cat-chip" data-cat="pediatrie">Pediatrie</button>
          <button type="button" class="omni-chip omni-contrast-chip" data-contrast="contrast">💧 Contrast IV</button>
          <button type="button" class="omni-chip omni-contrast-chip" data-contrast="native">🌿 Fără Contrast (Nativ)</button>
        </div>

        <!-- Bara de Stare Rezultate -->
        <div class="omni-status-bar">
          <span id="omnisearch-count-badge" class="omni-count-badge">Se încarcă protocoalele...</span>
        </div>

        <!-- Container Rezultate Live -->
        <div id="omnisearch-results" class="omni-results-container"></div>
      </div>
    `;

    // Event listeners
    const input = document.getElementById('omnisearch-input');
    const clearBtn = document.getElementById('omnisearch-clear');

    input.addEventListener('input', (e) => {
      searchQuery = e.target.value;
      visibleCount = 24;
      render();
    });

    clearBtn.addEventListener('click', () => {
      input.value = '';
      searchQuery = '';
      visibleCount = 24;
      render();
      input.focus();
    });

    // Modality chips
    document.querySelectorAll('.omni-mod-chip').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.omni-mod-chip').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeModality = btn.dataset.mod;
        visibleCount = 24;
        render();
      });
    });

    // Category chips
    document.querySelectorAll('.omni-cat-chip').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.omni-cat-chip').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeCategory = btn.dataset.cat;
        visibleCount = 24;
        render();
      });
    });

    // Contrast chips
    document.querySelectorAll('.omni-contrast-chip').forEach(btn => {
      btn.addEventListener('click', () => {
        if (btn.classList.contains('active')) {
          btn.classList.remove('active');
          activeContrast = 'all';
        } else {
          document.querySelectorAll('.omni-contrast-chip').forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          activeContrast = btn.dataset.contrast;
        }
        visibleCount = 24;
        render();
      });
    });

    loadProtocols();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initOmniSearch);
  } else {
    initOmniSearch();
  }
})();
