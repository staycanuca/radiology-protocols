/* body-map.js — Harta corporală interactivă a protocoalelor.
   Se activează doar pe paginile care conțin <div id="body-map-app">. */
(function () {
  'use strict';

  /* Capturăm URL-ul scriptului sincron, la execuție — în callback-ile
     asincrone document.currentScript este null. */
  var scriptUrl = (document.currentScript && document.currentScript.src) || '';

  function ready(fn) {
    if (document.readyState !== 'loading') { fn(); }
    else { document.addEventListener('DOMContentLoaded', fn); }
  }

  ready(function () {
    var root = document.getElementById('body-map-app');
    if (!root) { return; }

    var MODALITIES = {
      ct: { label: 'CT', color: '#1a237e' },
      irm: { label: 'IRM', color: '#0f766e' },
      rx: { label: 'RX', color: '#0284c7' },
      us: { label: 'US', color: '#65a30d' },
      fluoro: { label: 'FLOURO', color: '#047857' }
    };
    var MOD_ORDER = ['ct', 'irm', 'rx', 'us', 'fluoro'];

    /* ------------------------------------------------------------------ */
    /* Definirea zonelor anatomice                                         */
    /* viewBox 0 0 220 540; oglinzirea stânga/dreapta se face față de x=110 */
    /* ------------------------------------------------------------------ */

    function rect(x, y, w, h, rx) { return { t: 'r', x: x, y: y, w: w, h: h, rx: rx || 0 }; }
    function ell(cx, cy, rx, ry) { return { t: 'e', cx: cx, cy: cy, rx: rx, ry: ry }; }
    function circ(cx, cy, r) { return { t: 'c', cx: cx, cy: cy, r: r }; }

    function mirror(s) {
      if (s.t === 'r') { return rect(220 - s.x - s.w, s.y, s.w, s.h, s.rx); }
      if (s.t === 'e') { return ell(220 - s.cx, s.cy, s.rx, s.ry); }
      return s;
    }

    function zoneEl(segId, s) {
      var d = ' data-seg="' + segId + '"';
      if (s.t === 'r') {
        return '<rect' + d + ' x="' + s.x + '" y="' + s.y + '" width="' + s.w + '" height="' + s.h + '"' +
               (s.rx ? ' rx="' + s.rx + '"' : '') + '/>';
      }
      if (s.t === 'e') {
        return '<ellipse' + d + ' cx="' + s.cx + '" cy="' + s.cy + '" rx="' + s.rx + '" ry="' + s.ry + '"/>';
      }
      return '<circle' + d + ' cx="' + s.cx + '" cy="' + s.cy + '" r="' + s.r + '"/>';
    }

    /* Ținte uzuale (etichetă, url, mod, categorie pentru număr), grupate pe modalitate */
    var T_MSK_SUP = {
      ct: [['Musculoscheletic (MSK)', 'ct/msk/', 'ct', 'msk']],
      irm: [['MSK IRM', 'irm/msk/', 'irm', 'msk']],
      rx: [['Membru superior', 'rx/membru-superior/', 'rx', 'membru-superior']],
      us: [['MSK ecografie', 'eco/msk/', 'eco', 'msk']],
      fluoro: [['C-Arm (bloc operator)', 'fluoro/c-arm/', 'fluoro', 'c-arm']]
    };
    var T_MSK_INF = {
      ct: [['Musculoscheletic (MSK)', 'ct/msk/', 'ct', 'msk']],
      irm: [['MSK IRM', 'irm/msk/', 'irm', 'msk']],
      rx: [['Membru inferior', 'rx/membru-inferior/', 'rx', 'membru-inferior']],
      us: [['MSK ecografie', 'eco/msk/', 'eco', 'msk']],
      fluoro: [['C-Arm (bloc operator)', 'fluoro/c-arm/', 'fluoro', 'c-arm']]
    };

    /* Fiecare zonă: etichetă, forme (față/spate), ținte.
       paired: forma e definită pe partea stângă; dreapta se generează prin
       oglindire. sideF: sufixe feminine pentru acordul stângă/dreaptă. */
    var ZONE_DEFS = {
      torace: {
        label: 'Torace',
        front: '<path data-seg="torace" d="M70,90 Q110,74 150,90 L154,190 Q110,206 66,190 Z"/>',
        targets: {
          ct: [['Torace', 'ct/chest/', 'ct', 'chest']],
          irm: [['Cardio-IRM', 'irm/cardiac/', 'irm', 'cardiac']],
          rx: [['Torace', 'rx/torace/', 'rx', 'torace']]
        }
      },
      abdomen: {
        label: 'Abdomen',
        front: '<path data-seg="abdomen" d="M68,194 Q110,210 152,194 L146,290 Q110,302 74,290 Z"/>',
        targets: {
          ct: [['Abdomen & pelvis', 'ct/abdomen/', 'ct', 'abdomen']],
          irm: [['Abdomen & pelvis IRM', 'irm/abdomen-pelvis/', 'irm', 'abdomen-pelvis']],
          rx: [['Abdomen & bazin', 'rx/abdomen/', 'rx', 'abdomen']],
          us: [['Abdomen & pelvis', 'eco/abdomen-pelvis/', 'eco', 'abdomen-pelvis']],
          fluoro: [['Tub digestiv', 'fluoro/digestiv/', 'fluoro', 'digestiv']]
        }
      },
      inima: {
        label: 'Inimă',
        front: '<ellipse data-seg="inima" cx="124" cy="146" rx="12" ry="14"/>',
        targets: {
          ct: [['Cardiac & coronar', 'ct/cardiac/', 'ct', 'cardiac']],
          irm: [['Cardio-IRM', 'irm/cardiac/', 'irm', 'cardiac']],
          rx: [['Torace', 'rx/torace/', 'rx', 'torace']]
        }
      },
      spate: {
        label: 'Spate (torace dorsal)',
        back: '<path data-seg="spate" d="M66,88 Q110,72 154,88 L158,196 Q110,212 62,196 Z"/>',
        targets: {
          ct: [['Torace (dorsal)', 'ct/chest/', 'ct', 'chest']],
          rx: [['Torace', 'rx/torace/', 'rx', 'torace']],
          us: [['Vascular & doppler', 'eco/vascular-doppler/', 'eco', 'vascular-doppler']]
        }
      },
      coloana: {
        label: 'Coloană vertebrală',
        back: '<rect data-seg="coloana" x="100" y="86" width="20" height="190" rx="10"/>',
        targets: {
          ct: [['Neurologie (coloană)', 'ct/neuro/', 'ct', 'neuro']],
          irm: [['Neuroradiologie (coloană)', 'irm/neuro/', 'irm', 'neuro']],
          rx: [['Coloana vertebrală', 'rx/coloana/', 'rx', 'coloana']],
          us: [['Musculoscheletic', 'eco/msk/', 'eco', 'msk']],
          fluoro: [['C-Arm (infiltrații rahidiene)', 'fluoro/c-arm/', 'fluoro', 'c-arm']]
        }
      },
      bazin: {
        label: 'Bazin / șold',
        front: '<path data-seg="bazin" d="M74,296 Q110,310 146,296 L142,348 Q110,360 78,348 Z"/>',
        back: '<path data-seg="bazin" d="M70,298 Q110,312 150,298 L144,350 Q110,362 76,350 Z"/>',
        targets: {
          ct: [['MSK pelvis & șold', 'ct/msk/', 'ct', 'msk']],
          irm: [['MSK pelvis & șold IRM', 'irm/msk/', 'irm', 'msk']],
          rx: [['Bazin & membru inferior', 'rx/membru-inferior/', 'rx', 'membru-inferior']],
          us: [['MSK ecografie', 'eco/msk/', 'eco', 'msk']],
          fluoro: [
            ['Aparat urinar & pelvis', 'fluoro/urinar/', 'fluoro', 'urinar'],
            ['C-Arm (bloc operator)', 'fluoro/c-arm/', 'fluoro', 'c-arm']
          ]
        }
      },
      cap: {
        label: 'Cap',
        shape: circ(110, 42, 26),
        both: true,
        targets: {
          ct: [['Neurologie & coloană', 'ct/neuro/', 'ct', 'neuro']],
          irm: [['Neuroradiologie IRM', 'irm/neuro/', 'irm', 'neuro']],
          rx: [['Craniu & masiv facial', 'rx/craniu-saf/', 'rx', 'craniu-saf']]
        }
      },
      gat: {
        label: 'Gât & cervical',
        shape: rect(96, 64, 28, 24, 8),
        both: true,
        targets: {
          ct: [['Neurologie (coloană cervicală)', 'ct/neuro/', 'ct', 'neuro']],
          irm: [['Neuroradiologie IRM', 'irm/neuro/', 'irm', 'neuro']],
          rx: [['Coloana vertebrală', 'rx/coloana/', 'rx', 'coloana']],
          us: [['Părți moi & endocrin (tiroidă, salivare, ganglioni)', 'eco/parti-moi-endocrin/', 'eco', 'parti-moi-endocrin']]
        }
      },
      san: {
        label: 'Sân', paired: true, sideF: true,
        shape: ell(82, 156, 14, 12),
        front: true,
        targets: {
          irm: [['IRM mamar', 'irm/san/', 'irm', 'san']],
          rx: [['Mamografie', 'rx/mamografie/', 'rx', 'mamografie']],
          us: [['Senologie (sân)', 'eco/san/', 'eco', 'san']]
        }
      },
      umar: {
        label: 'Umăr', paired: true,
        shape: ell(64, 92, 16, 12), both: true,
        targets: T_MSK_SUP
      },
      brat: {
        label: 'Braț (humerus)', paired: true,
        shape: rect(48, 104, 24, 58, 10), both: true,
        targets: T_MSK_SUP
      },
      cot: {
        label: 'Cot', paired: true,
        shape: ell(60, 168, 13, 11), both: true,
        targets: T_MSK_SUP
      },
      antebrat: {
        label: 'Antebraț', paired: true,
        shape: rect(45, 176, 24, 56, 10), both: true,
        targets: T_MSK_SUP
      },
      pumn: {
        label: 'Pumn', paired: true,
        shape: ell(58, 240, 11, 9), both: true,
        targets: T_MSK_SUP
      },
      mana: {
        label: 'Mână', paired: true, sideF: true,
        shape: ell(56, 266, 14, 17), both: true,
        targets: T_MSK_SUP
      },
      coapsa: {
        label: 'Coapsă (femur)', paired: true, sideF: true,
        shape: rect(79, 354, 25, 66, 11), both: true,
        targets: T_MSK_INF
      },
      genunchi: {
        label: 'Genunchi', paired: true,
        shape: ell(91.5, 428, 13, 10), both: true,
        targets: T_MSK_INF
      },
      gamba: {
        label: 'Gambă', paired: true, sideF: true,
        shape: rect(79, 438, 24, 48, 10), both: true,
        targets: T_MSK_INF
      },
      glezna: {
        label: 'Gleznă', paired: true, sideF: true,
        shape: ell(91, 492, 11, 9), both: true,
        targets: T_MSK_INF
      },
      picior: {
        label: 'Picior', paired: true,
        shape: rect(77, 496, 29, 17, 8), both: true,
        targets: T_MSK_INF
      }
    };

    /* Ordinea de desenare controlează ce zona primește hoverul la suprapuneri. */
    var DRAW_ORDER = [
      'torace', 'abdomen', 'inima', 'san', 'spate', 'coloana', 'bazin', 'cap', 'gat',
      'umar', 'brat', 'cot', 'antebrat', 'pumn', 'mana',
      'coapsa', 'genunchi', 'gamba', 'glezna', 'picior'
    ];

    var SEGMENTS = {};
    var TARGETS = {};
    var FRONT_ZONES = '';
    var BACK_ZONES = '';

    DRAW_ORDER.forEach(function (key) {
      var z = ZONE_DEFS[key];
      if (!z) { return; }
      var sides = z.paired
        ? [[key + '-l', z.shape, z.sideF ? 'stângă' : 'stâng'],
           [key + '-r', mirror(z.shape), z.sideF ? 'dreaptă' : 'drept']]
        : [[key, z.shape || null, '']];
      sides.forEach(function (sd) {
        var id = sd[0];
        SEGMENTS[id] = { label: z.label + (z.paired ? ' ' + sd[2] : '') };
        TARGETS[id] = z.targets;
        if (z.front && sd[1]) { FRONT_ZONES += zoneEl(id, sd[1]); }
        if (z.back && sd[1]) { BACK_ZONES += zoneEl(id, sd[1]); }
        if (z.both && sd[1]) {
          FRONT_ZONES += zoneEl(id, sd[1]);
          BACK_ZONES += zoneEl(id, sd[1]);
        }
      });
      if (z.front && typeof z.front === 'string') { FRONT_ZONES += z.front; }
      if (z.back && typeof z.back === 'string') { BACK_ZONES += z.back; }
    });

    var SPECIALS = {
      vascular: {
        label: 'Vascular / Angio',
        targets: {
          ct: [['Angio-CT & vascular', 'ct/vascular/', 'ct', 'vascular']],
          us: [['Vascular & doppler', 'eco/vascular-doppler/', 'eco', 'vascular-doppler']]
        }
      },
      trauma: {
        label: 'Traumă & urgențe',
        targets: {
          ct: [['Traumă & urgențe', 'ct/trauma/', 'ct', 'trauma']]
        }
      },
      pediatrie: {
        label: 'Pediatrie',
        targets: {
          rx: [['Pediatrie RX', 'rx/pediatrie/', 'rx', 'pediatrie']],
          us: [['Pediatrie & neonatologie', 'eco/pediatrie/', 'eco', 'pediatrie']],
          fluoro: [['Fluoroscopie pediatrică', 'fluoro/pediatrie/', 'fluoro', 'pediatrie']]
        }
      }
    };

    var state = { view: 'front', modality: 'all', selected: null };
    var counts = {};

    /* Baza site-ului, derivată din URL-ul scriptului (.../javascripts/body-map.js),
       ca legăturile relative din TARGETS să nu depindă de pagina curentă. */
    var siteBase = '';
    if (scriptUrl) {
      try { siteBase = new URL('../', new URL('.', scriptUrl).href).href; } catch (e) { siteBase = ''; }
    }
    function absUrl(p) { return siteBase + p; }

    /* ------------------------------------------------------------------ */
    /* Siluetă SVG                                                         */
    /* ------------------------------------------------------------------ */

    var SILHOUETTE =
      '<circle class="bm-base" cx="110" cy="42" r="27"/>' +
      '<path class="bm-base" d="M97,64 C96,76 84,78 74,84 C60,92 54,104 52,120 C50,138 48,180 46,220 ' +
      'Q44,266 48,286 Q49,296 57,296 Q64,296 65,287 L68,244 Q69,222 73,210 L72,298 Q71,326 75,350 ' +
      'L79,486 Q79,500 86,500 L86,507 Q86,513 94,513 L101,513 Q109,513 109,505 L109,362 L109,505 ' +
      'Q109,513 117,513 L124,513 Q132,513 132,507 L132,500 Q139,500 139,486 L143,350 Q147,326 146,298 ' +
      'L145,210 Q149,222 150,244 L153,287 Q154,296 161,296 Q169,296 170,286 Q174,266 172,220 ' +
      'C170,180 168,138 166,120 C164,104 158,92 144,84 C134,78 122,76 121,64 Z"/>';

    /* ------------------------------------------------------------------ */
    /* Construirea DOM-ului                                                */
    /* ------------------------------------------------------------------ */

    function esc(s) {
      return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    }

    function modChipsHtml() {
      var html = '<button type="button" class="bm-chip active" data-mod="all">Toate</button>';
      MOD_ORDER.forEach(function (m) {
        html += '<button type="button" class="bm-chip" data-mod="' + m + '" style="--bm-color:' +
                MODALITIES[m].color + '">' + MODALITIES[m].label + '</button>';
      });
      return html;
    }

    function specialsHtml() {
      var html = '';
      Object.keys(SPECIALS).forEach(function (key) {
        html += '<button type="button" class="bm-special" data-special="' + key + '">' +
                esc(SPECIALS[key].label) + '</button>';
      });
      return html;
    }

    root.innerHTML =
      '<div class="bm-layout">' +
      '  <div class="bm-toolbar">' +
      '    <div class="bm-view-toggle" role="tablist" aria-label="Vedere corporală">' +
      '      <button type="button" class="bm-view-btn active" data-view="front" role="tab">Față</button>' +
      '      <button type="button" class="bm-view-btn" data-view="back" role="tab">Spate</button>' +
      '    </div>' +
      '    <div class="bm-mod-chips" role="group" aria-label="Selectare modalitate">' + modChipsHtml() + '</div>' +
      '  </div>' +
      '  <div class="bm-main">' +
      '    <div class="bm-figure">' +
      '      <svg id="bm-svg-front" viewBox="0 0 220 540" role="group" aria-label="Harta corporală — vedere anterioară">' +
               SILHOUETTE + FRONT_ZONES +
      '      </svg>' +
      '      <svg id="bm-svg-back" viewBox="0 0 220 540" role="group" aria-label="Harta corporală — vedere posterioară" style="display:none">' +
               SILHOUETTE + BACK_ZONES +
      '      </svg>' +
      '      <div class="bm-tooltip" hidden></div>' +
      '    </div>' +
      '    <div class="bm-panel">' +
      '      <div class="bm-panel-title" id="bm-panel-title">Selectează o zonă de pe hartă</div>' +
      '      <div class="bm-panel-body" id="bm-panel-body"></div>' +
      '      <div class="bm-specials-row"><span class="bm-specials-label">Accese rapide:</span>' + specialsHtml() + '</div>' +
      '    </div>' +
      '  </div>' +
      '  <div class="bm-toast" hidden></div>' +
      '</div>';

    var svgFront = root.querySelector('#bm-svg-front');
    var svgBack = root.querySelector('#bm-svg-back');
    var tooltip = root.querySelector('.bm-tooltip');
    var panelTitle = root.querySelector('#bm-panel-title');
    var panelBody = root.querySelector('#bm-panel-body');
    var toast = root.querySelector('.bm-toast');
    var toastTimer = null;

    /* ------------------------------------------------------------------ */
    /* Date: număr de protocoale per categorie                             */
    /* ------------------------------------------------------------------ */

    function loadCounts() {
      var base = 'protocol-forms-index.json';
      if (scriptUrl) {
        try { base = new URL('protocol-forms-index.json', scriptUrl).href; } catch (e) { /* fallback relativ */ }
      }
      fetch(base).then(function (r) {
        if (!r.ok) { throw new Error('HTTP ' + r.status); }
        return r.json();
      }).then(function (items) {
        if (!Array.isArray(items)) { return; }
        items.forEach(function (p) {
          if (!p || !p.modality || !p.category) { return; }
          var k = p.modality + ':' + String(p.category).toLowerCase();
          counts[k] = (counts[k] || 0) + 1;
        });
        refreshPanel();
        applyAvailability();
      }).catch(function () { /* fără numărători — funcționalitatea rămâne completă */ });
    }

    function countFor(mod, cat) {
      var n = counts[mod + ':' + cat];
      return typeof n === 'number' ? n : null;
    }

    function countLabel(n) {
      if (n === null || n === undefined) { return ''; }
      return n === 1 ? '1 protocol' : n + ' protocoale';
    }

    /* ------------------------------------------------------------------ */
    /* Interacțiune                                                        */
    /* ------------------------------------------------------------------ */

    function targetsFor(seg) { return TARGETS[seg] || {}; }

    function segAvailable(seg, mod) {
      if (mod === 'all') { return Object.keys(targetsFor(seg)).length > 0; }
      return !!targetsFor(seg)[mod];
    }

    function allZones(seg) {
      return root.querySelectorAll('svg [data-seg="' + seg + '"]');
    }

    function applyAvailability() {
      var zones = root.querySelectorAll('svg [data-seg]');
      zones.forEach(function (z) {
        var seg = z.getAttribute('data-seg');
        var ok = segAvailable(seg, state.modality);
        z.classList.toggle('bm-disabled', !ok);
        var label = SEGMENTS[seg] ? SEGMENTS[seg].label : seg;
        var ariaBits = [label];
        if (state.modality !== 'all') {
          ariaBits.push(ok ? ('deschide protocoale ' + MODALITIES[state.modality].label)
                           : ('fără protocoale ' + MODALITIES[state.modality].label));
        }
        z.setAttribute('aria-label', ariaBits.join(' — '));
      });
      Object.keys(SPECIALS).forEach(function (key) {
        var btn = root.querySelector('.bm-special[data-special="' + key + '"]');
        if (!btn) { return; }
        var ok = state.modality === 'all' || !!SPECIALS[key].targets[state.modality];
        btn.classList.toggle('bm-disabled', !ok);
      });
    }

    function select(seg) {
      state.selected = seg;
      root.querySelectorAll('svg [data-seg].bm-selected').forEach(function (z) {
        z.classList.remove('bm-selected');
      });
      allZones(seg).forEach(function (z) { z.classList.add('bm-selected'); });
      refreshPanel();
    }

    function targetRowsHtml(targetsMap, colorByMod) {
      var html = '';
      MOD_ORDER.forEach(function (m) {
        var list = targetsMap[m];
        if (!list) { return; }
        list.forEach(function (t) {
          var n = countFor(t[2], t[3]);
          var badgeStyle = colorByMod ? ' style="--bm-color:' + MODALITIES[m].color + '"' : '';
          html += '<a class="bm-link" href="' + esc(absUrl(t[1])) + '"' + badgeStyle + '>' +
                  '<span class="bm-badge">' + MODALITIES[m].label + '</span>' +
                  '<span class="bm-link-label">' + esc(t[0]) + '</span>' +
                  (n !== null ? '<span class="bm-count">' + esc(countLabel(n)) + '</span>' : '') +
                  '<span class="bm-arrow">→</span></a>';
        });
      });
      return html;
    }

    function refreshPanel() {
      var seg = state.selected;
      if (!seg || !SEGMENTS[seg]) {
        panelTitle.textContent = 'Selectează o zonă de pe hartă';
        var hint = state.modality === 'all'
          ? 'În modul <strong>Toate</strong>, un click pe o zonă anatomică afișează listele de protocoale disponibile pentru fiecare modalitate. Alege o modalitate pentru navigare directă.'
          : 'Un click pe o zonă anatomică deschide direct lista de protocoale <strong>' + esc(MODALITIES[state.modality].label) + '</strong> pentru zona respectivă.';
        panelBody.innerHTML = '<p class="bm-hint">' + hint + '</p>';
        return;
      }
      panelTitle.textContent = SEGMENTS[seg].label;
      if (state.modality === 'all') {
        var html = targetRowsHtml(targetsFor(seg), true);
        panelBody.innerHTML = html || '<p class="bm-hint">Nu există protocoale mapate pentru această zonă.</p>';
      } else {
        var list = targetsFor(seg)[state.modality] || [];
        if (list.length) {
          var rows = '';
          list.forEach(function (t) {
            var n = countFor(t[2], t[3]);
            rows += '<a class="bm-link" href="' + esc(absUrl(t[1])) + '" style="--bm-color:' + MODALITIES[state.modality].color + '">' +
                    '<span class="bm-badge">' + MODALITIES[state.modality].label + '</span>' +
                    '<span class="bm-link-label">' + esc(t[0]) + '</span>' +
                    (n !== null ? '<span class="bm-count">' + esc(countLabel(n)) + '</span>' : '') +
                    '<span class="bm-arrow">→</span></a>';
          });
          panelBody.innerHTML = rows;
        } else {
          panelBody.innerHTML = '<p class="bm-hint">Nu există protocoale ' + esc(MODALITIES[state.modality].label) +
                                ' pentru „' + esc(SEGMENTS[seg].label) + '”. Încearcă altă modalitate.</p>';
        }
      }
    }

    function showToast(msg) {
      toast.textContent = msg;
      toast.hidden = false;
      toast.classList.add('bm-show');
      if (toastTimer) { clearTimeout(toastTimer); }
      toastTimer = setTimeout(function () {
        toast.classList.remove('bm-show');
        toast.hidden = true;
      }, 2200);
    }

    function activate(seg) {
      if (!segAvailable(seg, state.modality)) {
        var modLabel = state.modality === 'all' ? '' : (' ' + MODALITIES[state.modality].label);
        showToast('Nu există protocoale' + modLabel + ' pentru „' +
                  (SEGMENTS[seg] ? SEGMENTS[seg].label : seg) + '".');
        return;
      }
      if (state.modality !== 'all') {
        var list = targetsFor(seg)[state.modality];
        if (list && list.length) { window.location.href = absUrl(list[0][1]); }
        return;
      }
      select(seg);
    }

    function activateSpecial(key) {
      var sp = SPECIALS[key];
      if (!sp) { return; }
      var ok = state.modality === 'all' || !!sp.targets[state.modality];
      if (!ok) {
        showToast('Nu există protocoale ' + MODALITIES[state.modality].label + ' pentru „' + sp.label + '".');
        return;
      }
      if (state.modality !== 'all') {
        var t = sp.targets[state.modality];
        if (t && t.length) { window.location.href = absUrl(t[0][1]); }
        return;
      }
      state.selected = null;
      root.querySelectorAll('svg [data-seg].bm-selected').forEach(function (z) {
        z.classList.remove('bm-selected');
      });
      panelTitle.textContent = sp.label;
      panelBody.innerHTML = targetRowsHtml(sp.targets, true) ||
        '<p class="bm-hint">Nu există protocoale mapate.</p>';
    }

    /* Evenimente pe zone */
    [svgFront, svgBack].forEach(function (svg) {
      svg.addEventListener('click', function (ev) {
        var z = ev.target.closest('[data-seg]');
        if (z) { activate(z.getAttribute('data-seg')); }
      });
      svg.addEventListener('keydown', function (ev) {
        if (ev.key !== 'Enter' && ev.key !== ' ') { return; }
        var z = ev.target.closest && ev.target.closest('[data-seg]');
        if (z) { ev.preventDefault(); activate(z.getAttribute('data-seg')); }
      });
      svg.addEventListener('mousemove', function (ev) {
        var z = ev.target.closest('[data-seg]');
        if (!z) { tooltip.hidden = true; return; }
        var seg = z.getAttribute('data-seg');
        var meta = SEGMENTS[seg];
        if (!meta) { tooltip.hidden = true; return; }
        var modCount = Object.keys(targetsFor(seg)).length;
        var line2;
        if (state.modality === 'all') {
          line2 = modCount ? (modCount + (modCount === 1 ? ' modalitate disponibilă' : ' modalități disponibile')) : '';
        } else {
          line2 = segAvailable(seg, state.modality)
            ? 'Click: protocoale ' + MODALITIES[state.modality].label
            : 'Fără protocoale ' + MODALITIES[state.modality].label;
        }
        tooltip.innerHTML = '<strong>' + esc(meta.label) + '</strong>' + (line2 ? '<span>' + esc(line2) + '</span>' : '');
        var rect = root.querySelector('.bm-figure').getBoundingClientRect();
        tooltip.style.left = (ev.clientX - rect.left + 14) + 'px';
        tooltip.style.top = (ev.clientY - rect.top + 14) + 'px';
        tooltip.hidden = false;
      });
      svg.addEventListener('mouseleave', function () { tooltip.hidden = true; });
    });

    /* Comutator față/spate */
    root.querySelectorAll('.bm-view-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        state.view = btn.getAttribute('data-view');
        root.querySelectorAll('.bm-view-btn').forEach(function (b) {
          b.classList.toggle('active', b === btn);
        });
        svgFront.style.display = state.view === 'front' ? '' : 'none';
        svgBack.style.display = state.view === 'back' ? '' : 'none';
        tooltip.hidden = true;
        applyAvailability();
        if (state.selected) { select(state.selected); }
      });
    });

    /* Selector modalitate */
    root.querySelectorAll('.bm-chip').forEach(function (chip) {
      chip.addEventListener('click', function () {
        state.modality = chip.getAttribute('data-mod');
        root.querySelectorAll('.bm-chip').forEach(function (c) {
          c.classList.toggle('active', c === chip);
        });
        root.classList.toggle('bm-mod-selected', state.modality !== 'all');
        if (state.modality !== 'all') {
          root.style.setProperty('--bm-accent', MODALITIES[state.modality].color);
        }
        applyAvailability();
        if (state.selected) { refreshPanel(); }
      });
    });

    /* Accese rapide */
    root.querySelectorAll('.bm-special').forEach(function (btn) {
      btn.addEventListener('click', function () { activateSpecial(btn.getAttribute('data-special')); });
    });

    /* Pregătire zone: focusabile */
    root.querySelectorAll('svg [data-seg]').forEach(function (z) {
      z.setAttribute('tabindex', '0');
      z.setAttribute('role', 'button');
    });

    applyAvailability();
    refreshPanel();
    loadCounts();
  });
})();
