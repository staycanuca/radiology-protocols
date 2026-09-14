/**
 * iris-browser.js — Ghid Național IRIS Interactive Explorer
 * Interfață optimizată pentru mobil și desktop bazată pe datasetul oficial IRIS
 * (Ghidul de utilizare a investigațiilor radiologice și imagistice medicale - Ordinul MS 1342/2012)
 */

(function () {
  'use strict';

  function resolveSiteUrl(path) {
    if (typeof __md_scope !== 'undefined' && __md_scope && __md_scope.pathname && !location.protocol.startsWith('file')) {
      const base = __md_scope.pathname.endsWith('/') ? __md_scope.pathname : __md_scope.pathname + '/';
      return base + path.replace(/^\//, '');
    }
    return '../' + path.replace(/^\//, '');
  }

  // Corespondență între capitolele IRIS și secțiunile noastre de Protocoale CT
  const CHAPTER_TO_CT_CATEGORY = {
    'c-torace': { category: 'chest', label: 'Protocoale CT Torace', url: 'ct/chest/' },
    'c-aparat-cardiovascular': { category: 'cardiac', label: 'Protocoale CT Cord & Vascular', url: 'ct/cardiac/' },
    'c-aparat-digestiv': { category: 'abdomen', label: 'Protocoale CT Abdomen', url: 'ct/abdomen/' },
    'c-aparat-uro-genital-si-glande-suprarenale': { category: 'abdomen', label: 'Protocoale CT Abdomen & Uro', url: 'ct/abdomen/' },
    'c-cap': { category: 'neuro', label: 'Protocoale CT Neurologie (Cap & Gât)', url: 'ct/neuro/' },
    'c-coloana-vertebrala': { category: 'neuro', label: 'Protocoale CT Coloană', url: 'ct/neuro/' },
    'c-gat-parti-moi': { category: 'neuro', label: 'Protocoale CT Gât & Părți Moi', url: 'ct/neuro/' },
    'c-aparat-locomotor': { category: 'msk', label: 'Protocoale CT Musculoscheletic', url: 'ct/msk/' },
    'c-traumatisme': { category: 'trauma', label: 'Protocoale CT Traumă & Politraumă', url: 'ct/trauma/' },
    'c-cancer': { category: 'abdomen', label: 'Protocoale CT Oncologie', url: 'ct/abdomen/' },
  };

  const DOSE_LABELS = {
    0: { label: 'Fără iradiere', class: 'dose-0', dots: 0 },
    1: { label: 'Minimă (< 1 mSv)', class: 'dose-1', dots: 1 },
    2: { label: 'Foarte mică (1-5 mSv)', class: 'dose-2', dots: 2 },
    3: { label: 'Moderată (5-10 mSv)', class: 'dose-3', dots: 3 },
    4: { label: 'Mare (> 10 mSv)', class: 'dose-4', dots: 4 }
  };

  function getDoseInfo(doseMin, doseMax) {
    const d = doseMax !== undefined && doseMax !== null ? doseMax : (doseMin || 0);
    if (d === 0) return DOSE_LABELS[0];
    if (d === 1) return DOSE_LABELS[1];
    if (d === 2) return DOSE_LABELS[2];
    if (d === 3) return DOSE_LABELS[3];
    return DOSE_LABELS[4];
  }

  function getIndicationBadgeClass(indication) {
    if (!indication) return 'ind-default';
    const s = indication.toLowerCase();
    if (s.includes('indicat') && !s.includes('neindicat')) return 'ind-indicat';
    if (s.includes('particulare')) return 'ind-particular';
    if (s.includes('specializat')) return 'ind-specializat';
    if (s.includes('neindicat')) return 'ind-neindicat';
    return 'ind-default';
  }

  function getExamChipClass(exam) {
    if (!exam) return 'chip-other';
    const e = exam.toLowerCase();
    if (e.includes('ct') || e.includes('tomograf')) return 'chip-ct';
    if (e.includes('eco') || e.includes('ultrason')) return 'chip-eco';
    if (e.includes('rmn') || e.includes('irm') || e.includes('rezonant')) return 'chip-rmn';
    if (e.includes('radiograf') || e.includes('rx') || e.includes('scopie')) return 'chip-rx';
    return 'chip-other';
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function initIrisExplorer() {
    const container = document.getElementById('iris-explorer-app');
    if (!container) return;

    if (!window.IRIS || !window.IRIS.situations) {
      container.innerHTML = `
        <div class="iris-loading-state">
          <div class="iris-spinner"></div>
          <p>Se încarcă baza de date a Ghidului Național IRIS...</p>
        </div>
      `;
      setTimeout(initIrisExplorer, 200);
      return;
    }

    const { chapters, subchapters, situations, recommendations } = window.IRIS;

    // Index subchapters and recommendations for instant lookup
    const subMap = new Map();
    (subchapters || []).forEach(s => subMap.set(s.id, s));

    const chapterMap = new Map();
    (chapters || []).forEach(c => chapterMap.set(c.id, c));

    const recsBySituation = new Map();
    (recommendations || []).forEach(r => {
      if (!recsBySituation.has(r.situationId)) {
        recsBySituation.set(r.situationId, []);
      }
      recsBySituation.get(r.situationId).push(r);
    });

    let currentChapter = 'all';
    let searchQuery = '';
    let visibleLimit = 15;

    // Render Main Shell
    container.innerHTML = `
      <div class="iris-wrapper">
        <!-- Antet & Căutare Principală -->
        <div class="iris-search-box-wrap">
          <div class="iris-search-bar">
            <span class="iris-search-icon">🔍</span>
            <input 
              type="search" 
              id="iris-search-input" 
              class="iris-search-input" 
              placeholder="Caută simptom clinic, patologie sau examen (ex: apendicită, embolie, cefalee, calcul)..."
              autocomplete="off"
            />
            <button id="iris-clear-btn" class="iris-clear-btn" style="display:none;" title="Șterge căutarea">✕</button>
          </div>
          <div class="iris-stats-summary">
            <span>📚 <strong>${chapters.length}</strong> capitole</span>
            <span>🩺 <strong>${situations.length}</strong> situații clinice</span>
            <span>📋 <strong>${recommendations.length}</strong> recomandări</span>
          </div>
        </div>

        <!-- Filtre Capitole (Pills) -->
        <div class="iris-chapters-bar-container">
          <div class="iris-chapters-bar" id="iris-chapters-pills">
            <button class="iris-chip-btn active" data-ch="all">Toate (${situations.length})</button>
            ${chapters.map(ch => `
              <button class="iris-chip-btn" data-ch="${ch.id}">
                ${escapeHtml(ch.name)} (${ch.count})
              </button>
            `).join('')}
          </div>
        </div>

        <!-- Listă Rezultate -->
        <div class="iris-results-meta" id="iris-results-meta"></div>
        <div class="iris-situations-list" id="iris-situations-container"></div>
        
        <div class="iris-pagination-row" id="iris-pagination-row" style="display:none;">
          <button id="iris-load-more-btn" class="iris-load-more-btn">
            Afișează mai multe situații clinice...
          </button>
        </div>
      </div>
    `;

    const searchInput = document.getElementById('iris-search-input');
    const clearBtn = document.getElementById('iris-clear-btn');
    const pillsContainer = document.getElementById('iris-chapters-pills');
    const situationsContainer = document.getElementById('iris-situations-container');
    const resultsMeta = document.getElementById('iris-results-meta');
    const paginationRow = document.getElementById('iris-pagination-row');
    const loadMoreBtn = document.getElementById('iris-load-more-btn');

    function filterSituations() {
      const q = searchQuery.trim().toLowerCase();
      
      return situations.filter(sit => {
        if (sit.placeholder) return false;
        if (currentChapter !== 'all' && sit.chapterId !== currentChapter) {
          return false;
        }
        if (!q) return true;

        // Căutare în denumirea situației
        if (sit.name && sit.name.toLowerCase().includes(q)) return true;

        // Căutare în subcapitol sau capitol
        const sub = subMap.get(sit.subchapterId);
        if (sub && sub.name && sub.name.toLowerCase().includes(q)) return true;

        const ch = chapterMap.get(sit.chapterId);
        if (ch && ch.name && ch.name.toLowerCase().includes(q)) return true;

        // Căutare în recomandări asociate
        const recs = recsBySituation.get(sit.id) || [];
        for (let i = 0; i < recs.length; i++) {
          const r = recs[i];
          if (r.exam && r.exam.toLowerCase().includes(q)) return true;
          if (r.indication && r.indication.toLowerCase().includes(q)) return true;
          if (r.comments && r.comments.toLowerCase().includes(q)) return true;
          if (r.otherInfo && r.otherInfo.toLowerCase().includes(q)) return true;
        }

        return false;
      });
    }

    function renderList() {
      const filtered = filterSituations();
      const total = filtered.length;
      const visible = filtered.slice(0, visibleLimit);

      // Meta info
      let chapterName = 'Toate capitolele';
      if (currentChapter !== 'all') {
        const c = chapterMap.get(currentChapter);
        if (c) chapterName = c.name;
      }

      if (total === 0) {
        resultsMeta.innerHTML = `<span>Niciun rezultat găsit pentru selecția curentă.</span>`;
        situationsContainer.innerHTML = `
          <div class="iris-empty-state">
            <div class="iris-empty-icon">🔍</div>
            <h3>Nicio situație clinică identificată</h3>
            <p>Încercați alți termeni de căutare (ex: <em>apendice, colecistită, traumă, fractură, embolie</em>) sau alegeți alt capitol.</p>
          </div>
        `;
        paginationRow.style.display = 'none';
        return;
      }

      resultsMeta.innerHTML = `
        <span>Afișare <strong>${visible.length}</strong> din <strong>${total}</strong> situații clinice &bull; <em>${escapeHtml(chapterName)}</em></span>
      `;

      situationsContainer.innerHTML = visible.map(sit => {
        const ch = chapterMap.get(sit.chapterId);
        const sub = subMap.get(sit.subchapterId);
        const recs = recsBySituation.get(sit.id) || [];
        const ctLinkInfo = CHAPTER_TO_CT_CATEGORY[sit.chapterId];

        // Breadcrumb
        const chName = ch ? ch.name : '';
        const subName = sub ? sub.name : '';

        return `
          <div class="iris-sit-card" id="sit-${sit.id}">
            <div class="iris-sit-header">
              <div class="iris-sit-crumbs">
                <span>${escapeHtml(chName)}</span>
                ${subName ? `<span class="sep">/</span><span>${escapeHtml(subName)}</span>` : ''}
              </div>
              <h3 class="iris-sit-title">${escapeHtml(sit.name)}</h3>
            </div>

            <div class="iris-recs-container">
              ${recs.length === 0 ? '<p class="iris-no-recs">Fără recomandări specifice detaliate.</p>' : recs.map(r => {
                const doseInfo = getDoseInfo(r.doseMin, r.doseMax);
                const indClass = getIndicationBadgeClass(r.indication);
                const chipClass = getExamChipClass(r.exam);
                const isCT = r.exam && (r.exam.toLowerCase().includes('ct') || r.exam.toLowerCase().includes('tomograf'));

                return `
                  <div class="iris-rec-item ${isCT ? 'is-ct-recommendation' : ''}">
                    <div class="iris-rec-top">
                      <div class="iris-rec-exam-wrap">
                        <span class="iris-exam-chip ${chipClass}">${escapeHtml(r.exam || 'Examinare')}</span>
                        ${r.grade ? `<span class="iris-grade-badge" title="Grad de recomandare bazat pe dovezi">GRAD ${escapeHtml(r.grade)}</span>` : ''}
                      </div>
                      <div class="iris-rec-dose-wrap">
                        <span class="iris-dose-badge ${doseInfo.class}" title="Nivel de iradiere: ${doseInfo.label}">
                          ${'●'.repeat(doseInfo.dots)}${'○'.repeat(4 - doseInfo.dots)}
                          <span class="iris-dose-text">${doseInfo.label}</span>
                        </span>
                      </div>
                    </div>

                    <div class="iris-rec-indication-row">
                      <span class="iris-indication-badge ${indClass}">
                        ${escapeHtml(r.indication || 'Nespecificat')}
                      </span>
                    </div>

                    ${r.comments ? `
                      <div class="iris-rec-comments">
                        <p>${escapeHtml(r.comments)}</p>
                      </div>
                    ` : ''}

                    ${r.otherInfo ? `
                      <div class="iris-rec-other">
                        <strong>Context clinic:</strong> ${escapeHtml(r.otherInfo)}
                      </div>
                    ` : ''}

                    ${isCT && ctLinkInfo ? `
                      <div class="iris-ct-action-wrap">
                        <a href="${resolveSiteUrl(ctLinkInfo.url)}" class="iris-ct-protocol-link">
                          ⚡ Vezi ${ctLinkInfo.label} asociate ➔
                        </a>
                      </div>
                    ` : ''}
                  </div>
                `;
              }).join('')}
            </div>
          </div>
        `;
      }).join('');

      if (total > visibleLimit) {
        paginationRow.style.display = 'flex';
        loadMoreBtn.textContent = `Afișează încă 15 situații clinice (${total - visible.length} rămase)`;
      } else {
        paginationRow.style.display = 'none';
      }
    }

    // Evenimente Căutare
    let debounceTimer = null;
    searchInput.addEventListener('input', function (e) {
      searchQuery = e.target.value;
      if (searchQuery.length > 0) {
        clearBtn.style.display = 'block';
      } else {
        clearBtn.style.display = 'none';
      }
      visibleLimit = 15;
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(renderList, 150);
    });

    clearBtn.addEventListener('click', function () {
      searchInput.value = '';
      searchQuery = '';
      clearBtn.style.display = 'none';
      visibleLimit = 15;
      renderList();
      searchInput.focus();
    });

    // Evenimente Filtrare Capitole
    pillsContainer.addEventListener('click', function (e) {
      const btn = e.target.closest('.iris-chip-btn');
      if (!btn) return;
      const chId = btn.getAttribute('data-ch');
      if (!chId) return;

      pillsContainer.querySelectorAll('.iris-chip-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      currentChapter = chId;
      visibleLimit = 15;
      renderList();
    });

    // Eveniment Paginare
    loadMoreBtn.addEventListener('click', function () {
      visibleLimit += 15;
      renderList();
    });

    // Render inițial
    renderList();
  }

  // Inițializare la încărcarea paginii sau la navigare MkDocs
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initIrisExplorer);
  } else {
    initIrisExplorer();
  }

  // MkDocs instant navigation hook
  if (window.document$) {
    window.document$.subscribe(function () {
      initIrisExplorer();
    });
  }
})();
