/* body-map.js — Harta corporală interactivă a protocoalelor.
   Optimizat: încărcare instantanee (counts in-memory + lightweight counts JSON),
   interfață mobile-first cu selecție și căutare rapidă de regiuni,
   paletă calmă inspirată din natură (albastru senin, salvie pastel, verde mentă).
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

    /* Paletă calmă, inspirată din natură */
    var MODALITIES = {
      ct: { label: 'CT', color: '#0284c7', name: 'Tomografie Computerizată' },
      irm: { label: 'IRM', color: '#0f766e', name: 'Rezonanță Magnetică' },
      rx: { label: 'RX', color: '#0369a1', name: 'Radiografie' },
      us: { label: 'US', color: '#16a34a', name: 'Ecografie' },
      fluoro: { label: 'FLOURO', color: '#059669', name: 'Fluoroscopie' }
    };
    var MOD_ORDER = ['ct', 'irm', 'rx', 'us', 'fluoro'];

    /* ------------------------------------------------------------------ */
    /* Numărători precalculate pentru încărcare instantanee (0ms latență) */
    /* ------------------------------------------------------------------ */
    var DEFAULT_COUNTS = {
      "ct:abdomen": 271, "ct:cardiac": 83, "ct:chest": 82, "ct:msk": 14, "ct:neuro": 209, "ct:trauma": 14, "ct:vascular": 268,
      "eco:abdomen-pelvis": 6, "eco:msk": 3, "eco:parti-moi-endocrin": 4, "eco:pediatrie": 3, "eco:san": 2, "eco:vascular-doppler": 4,
      "fluoro:c-arm": 4, "fluoro:digestiv": 4, "fluoro:pediatrie": 2, "fluoro:urinar": 3,
      "irm:abdomen-pelvis": 10, "irm:cardiac": 2, "irm:msk": 5, "irm:neuro": 9, "irm:pediatrie": 9, "irm:san": 3,
      "rx:abdomen": 79, "rx:coloana": 75, "rx:craniu-saf": 100, "rx:mamografie": 14, "rx:membru-inferior": 150,
      "rx:membru-superior": 166, "rx:neclasificat": 2, "rx:pediatrie": 23, "rx:torace": 69
    };

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
        label: 'Sân', paired: true,
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

      if (z.paired) {
        var idL = key + '-l';
        var idR = key + '-r';
        var labelL = z.label + ' ' + (z.sideF ? 'stângă' : 'stâng');
        var labelR = z.label + ' ' + (z.sideF ? 'dreaptă' : 'drept');

        SEGMENTS[idL] = {
          label: labelL,
          baseKey: key,
          baseLabel: z.label,
          view: z.both ? 'both' : (z.front ? 'front' : 'back')
        };
        SEGMENTS[idR] = {
          label: labelR,
          baseKey: key,
          baseLabel: z.label,
          view: z.both ? 'both' : (z.front ? 'front' : 'back')
        };
        TARGETS[idL] = z.targets;
        TARGETS[idR] = z.targets;

        var shapeScreenLeft = z.shape;
        var shapeScreenRight = mirror(z.shape);

        /* Orientare anatomică medicală standard pentru toate zonele pereche:
           - În vedere anterioară (față în față cu pacientul):
             Stânga ecranului (x < 110) = Partea DREAPTĂ a pacientului (-r)
             Dreapta ecranului (x > 110) = Partea STÂNGĂ a pacientului (-l)
           - În vedere posterioară (privit din spate):
             Stânga ecranului (x < 110) = Partea STÂNGĂ a pacientului (-l)
             Dreapta ecranului (x > 110) = Partea DREAPTĂ a pacientului (-r) */
        if (z.front || z.both) {
          FRONT_ZONES += zoneEl(idR, shapeScreenLeft);
          FRONT_ZONES += zoneEl(idL, shapeScreenRight);
        }
        if (z.back || z.both) {
          BACK_ZONES += zoneEl(idL, shapeScreenLeft);
          BACK_ZONES += zoneEl(idR, shapeScreenRight);
        }
      } else {
        var id = key;
        SEGMENTS[id] = {
          label: z.label,
          baseKey: key,
          baseLabel: z.label,
          view: z.both ? 'both' : (z.front ? 'front' : 'back')
        };
        TARGETS[id] = z.targets;
        if (z.front && z.shape) { FRONT_ZONES += zoneEl(id, z.shape); }
        if (z.back && z.shape) { BACK_ZONES += zoneEl(id, z.shape); }
        if (z.both && z.shape) {
          FRONT_ZONES += zoneEl(id, z.shape);
          BACK_ZONES += zoneEl(id, z.shape);
        }
      }

      if (z.front && typeof z.front === 'string') { FRONT_ZONES += z.front; }
      if (z.back && typeof z.back === 'string') { BACK_ZONES += z.back; }
    });

    var SPECIALS = {
      vascular: {
        label: 'Vascular / Angio',
        icon: '🩺',
        targets: {
          ct: [['Angio-CT & vascular', 'ct/vascular/', 'ct', 'vascular']],
          us: [['Vascular & doppler', 'eco/vascular-doppler/', 'eco', 'vascular-doppler']]
        }
      },
      trauma: {
        label: 'Traumă & urgențe',
        icon: '🚨',
        targets: {
          ct: [['Traumă & urgențe', 'ct/trauma/', 'ct', 'trauma']]
        }
      },
      pediatrie: {
        label: 'Pediatrie',
        icon: '👶',
        targets: {
          irm: [['Pediatrie IRM', 'irm/pediatrie/', 'irm', 'pediatrie']],
          rx: [['Pediatrie RX', 'rx/pediatrie/', 'rx', 'pediatrie']],
          us: [['Pediatrie & neonatologie', 'eco/pediatrie/', 'eco', 'pediatrie']],
          fluoro: [['Fluoroscopie pediatrică', 'fluoro/pediatrie/', 'fluoro', 'pediatrie']]
        }
      }
    };

    /* Zone curatoriate pentru navigarea tactilă / selecție rapidă pe mobil */
    var QUICK_ZONES = [
      { id: 'cap', label: 'Cap', view: 'both' },
      { id: 'gat', label: 'Gât', view: 'both' },
      { id: 'torace', label: 'Torace', view: 'front' },
      { id: 'inima', label: 'Inimă', view: 'front' },
      { id: 'san-l', label: 'Sân', view: 'front' },
      { id: 'coloana', label: 'Coloană', view: 'back' },
      { id: 'spate', label: 'Spate', view: 'back' },
      { id: 'abdomen', label: 'Abdomen', view: 'front' },
      { id: 'bazin', label: 'Bazin / Șold', view: 'both' },
      { id: 'umar-l', label: 'Umăr', view: 'both' },
      { id: 'brat-l', label: 'Braț', view: 'both' },
      { id: 'cot-l', label: 'Cot', view: 'both' },
      { id: 'antebrat-l', label: 'Antebraț', view: 'both' },
      { id: 'pumn-l', label: 'Pumn', view: 'both' },
      { id: 'mana-l', label: 'Mână', view: 'both' },
      { id: 'coapsa-l', label: 'Coapsă', view: 'both' },
      { id: 'genunchi-l', label: 'Genunchi', view: 'both' },
      { id: 'gamba-l', label: 'Gambă', view: 'both' },
      { id: 'glezna-l', label: 'Gleznă', view: 'both' },
      { id: 'picior-l', label: 'Picior', view: 'both' }
    ];

    /* Sinonime pentru căutarea rapidă */
    var SYNONYMS = {
      cap: ['cap', 'craniu', 'creier', 'encefal', 'neuro', 'saf', 'sinusuri', 'fata', 'orbite', 'cerebral'],
      gat: ['gat', 'gât', 'cervical', 'laringe', 'faringe', 'tiroida', 'tiroidă', 'salivare', 'ganglioni'],
      torace: ['torace', 'plamani', 'plămâni', 'pulmonar', 'pleura', 'pleură', 'coaste', 'stern', 'mediastin'],
      inima: ['inima', 'inimă', 'cord', 'cardiac', 'coronar', 'aorta', 'aortă', 'miocard', 'pericard'],
      san: ['san', 'sân', 'mamar', 'mamelar', 'axila', 'axilă', 'senologie'],
      spate: ['spate', 'dorsal', 'scapula', 'omoplat', 'toracic dorsal'],
      coloana: ['coloana', 'coloană', 'vertebral', 'vertebra', 'vertebre', 'lombar', 'toracal', 'sacru', 'coccis', 'cervicala'],
      abdomen: ['abdomen', 'abdominal', 'ficat', 'stomac', 'splina', 'rinichi', 'pancreas', 'biliar', 'digestiv', 'vezicula'],
      bazin: ['bazin', 'pelvis', 'sold', 'șold', 'coxo', 'urinar', 'vezica', 'vezică', 'prostata', 'uter', 'ovare'],
      umar: ['umar', 'umăr', 'clavicula', 'scapula', 'acromio', 'coafa rotatorie'],
      brat: ['brat', 'braț', 'humerus', 'brahial'],
      cot: ['cot', 'olecran', 'epitrohlee'],
      antebrat: ['antebrat', 'antebraț', 'radius', 'cubitus', 'ulna'],
      pumn: ['pumn', 'carp', 'scafoid', 'radiocarpian'],
      mana: ['mana', 'mână', 'degete', 'falange', 'metacarp', 'palma'],
      coapsa: ['coapsa', 'coapsă', 'femur', 'femural'],
      genunchi: ['genunchi', 'rotula', 'rotulă', 'patela', 'menisc', 'ligamente incrucisate'],
      gamba: ['gamba', 'gambă', 'tibie', 'peroneu', 'fibula'],
      glezna: ['glezna', 'gleznă', 'maleola', 'talus', 'tibiotarsiana'],
      picior: ['picior', 'tars', 'metatars', 'calcaneu', 'degete picior', 'haluce']
    };

    var state = { view: 'front', modality: 'all', selected: null, searchQuery: '' };
    var counts = Object.assign({}, DEFAULT_COUNTS);

    /* Baza site-ului, derivată din URL-ul scriptului (.../javascripts/body-map.js),
       ca legăturile relative din TARGETS să nu depindă de pagina curentă. */
    var siteBase = '';
    if (scriptUrl) {
      try { siteBase = new URL('../', new URL('.', scriptUrl).href).href; } catch (e) { siteBase = ''; }
    }
    function absUrl(p) { return siteBase + p; }

    /* ------------------------------------------------------------------ */
    /* Siluetă SVG Calmantă și Fluidă                                      */
    /* ------------------------------------------------------------------ */

    var SILHOUETTE =
      '<defs>' +
      '  <linearGradient id="bm-base-grad" x1="0%" y1="0%" x2="0%" y2="100%">' +
      '    <stop offset="0%" stop-color="#e0f2fe" stop-opacity="0.95"/>' +
      '    <stop offset="50%" stop-color="#e8f5e9" stop-opacity="0.85"/>' +
      '    <stop offset="100%" stop-color="#f0fdf4" stop-opacity="0.9"/>' +
      '  </linearGradient>' +
      '  <filter id="bm-soft-glow" x="-15%" y="-15%" width="130%" height="130%">' +
      '    <feDropShadow dx="0" dy="2" stdDeviation="3" flood-color="#0284c7" flood-opacity="0.15"/>' +
      '  </filter>' +
      '</defs>' +
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
      var html = '<button type="button" class="bm-chip active" data-mod="all" aria-pressed="true">🌐 Toate</button>';
      MOD_ORDER.forEach(function (m) {
        html += '<button type="button" class="bm-chip" data-mod="' + m + '" style="--bm-color:' +
                MODALITIES[m].color + '" aria-pressed="false">' + MODALITIES[m].label + '</button>';
      });
      return html;
    }

    function specialsHtml() {
      var html = '';
      Object.keys(SPECIALS).forEach(function (key) {
        var sp = SPECIALS[key];
        var total = 0;
        MOD_ORDER.forEach(function (m) {
          (sp.targets[m] || []).forEach(function (t) {
            var n = countFor(t[2], t[3]);
            if (n) { total += n; }
          });
        });
        html += '<button type="button" class="bm-special" data-special="' + key + '">' +
                '<span class="bm-special-icon">' + sp.icon + '</span> ' +
                esc(sp.label) +
                (total > 0 ? ' <span class="bm-special-badge">' + total + '</span>' : '') +
                '</button>';
      });
      return html;
    }

    function quickZonesHtml() {
      var html = '';
      QUICK_ZONES.forEach(function (z) {
        html += '<button type="button" class="bm-zone-pill" data-zone-id="' + z.id + '">' +
                esc(z.label) + '</button>';
      });
      return html;
    }

    root.innerHTML =
      '<div class="bm-layout">' +
      '  <!-- Bara superioară de control -->' +
      '  <div class="bm-toolbar">' +
      '    <div class="bm-view-toggle" role="tablist" aria-label="Perspectivă anatomică">' +
      '      <button type="button" class="bm-view-btn active" data-view="front" role="tab" aria-selected="true">' +
      '        <span class="bm-tab-icon">👤</span> Față (Anterior)' +
      '      </button>' +
      '      <button type="button" class="bm-view-btn" data-view="back" role="tab" aria-selected="false">' +
      '        <span class="bm-tab-icon">🔄</span> Spate (Posterior)' +
      '      </button>' +
      '    </div>' +
      '    <div class="bm-mod-chips" role="group" aria-label="Selectare modalitate imagistică">' + modChipsHtml() + '</div>' +
      '  </div>' +
      '' +
      '  <!-- Căutare rapidă regiune anatomică (Mobile-First) -->' +
      '  <div class="bm-search-wrap">' +
      '    <div class="bm-search-field">' +
      '      <span class="bm-search-icon" aria-hidden="true">🔍</span>' +
      '      <input type="text" class="bm-search-input" id="bm-search-input" ' +
      '             placeholder="Caută zonă anatomică (ex: coloană, torace, genunchi, cap, abdomen)..." ' +
      '             aria-label="Caută zonă anatomică">' +
      '      <button type="button" class="bm-search-clear" id="bm-search-clear" title="Șterge căutarea" hidden aria-label="Șterge căutarea">✕</button>' +
      '    </div>' +
      '    <div class="bm-quick-zones" id="bm-quick-zones" role="group" aria-label="Selecție rapidă regiuni">' +
             quickZonesHtml() +
      '    </div>' +
      '  </div>' +
      '' +
      '  <!-- Corpul principal: Siluetă + Panou -->' +
      '  <div class="bm-main">' +
      '    <div class="bm-figure">' +
      '      <div class="bm-figure-badge" id="bm-figure-badge">Vedere Anterioară</div>' +
      '      <svg id="bm-svg-front" viewBox="0 0 220 540" role="group" aria-label="Harta corporală — vedere anterioară">' +
               SILHOUETTE + FRONT_ZONES +
      '      </svg>' +
      '      <svg id="bm-svg-back" viewBox="0 0 220 540" role="group" aria-label="Harta corporală — vedere posterioară" style="display:none">' +
               SILHOUETTE + BACK_ZONES +
      '      </svg>' +
      '      <div class="bm-tooltip" hidden></div>' +
      '    </div>' +
      '    <div class="bm-panel" id="bm-panel">' +
      '      <div class="bm-panel-header">' +
      '        <div>' +
      '          <span class="bm-panel-sub" id="bm-panel-sub">Regiune anatomică</span>' +
      '          <div class="bm-panel-title" id="bm-panel-title">Selectează o zonă de pe hartă</div>' +
      '        </div>' +
      '        <button type="button" class="bm-reset-btn" id="bm-reset-btn" title="Resetează selecția" style="display:none;">' +
      '          ✕ Resetează' +
      '        </button>' +
      '      </div>' +
      '      <div class="bm-panel-body" id="bm-panel-body"></div>' +
      '      <div class="bm-specials-row">' +
      '        <span class="bm-specials-label">Accese rapide:</span>' + specialsHtml() +
      '      </div>' +
      '    </div>' +
      '  </div>' +
      '  <div class="bm-toast" hidden></div>' +
      '</div>';

    var svgFront = root.querySelector('#bm-svg-front');
    var svgBack = root.querySelector('#bm-svg-back');
    var figureBadge = root.querySelector('#bm-figure-badge');
    var tooltip = root.querySelector('.bm-tooltip');
    var panelTitle = root.querySelector('#bm-panel-title');
    var panelSub = root.querySelector('#bm-panel-sub');
    var panelBody = root.querySelector('#bm-panel-body');
    var resetBtn = root.querySelector('#bm-reset-btn');
    var searchInput = root.querySelector('#bm-search-input');
    var searchClear = root.querySelector('#bm-search-clear');
    var toast = root.querySelector('.bm-toast');
    var toastTimer = null;

    /* ------------------------------------------------------------------ */
    /* Date: număr de protocoale per categorie                             */
    /* Încărcare rapidă din body-map-counts.json (<1KB) cu fallback       */
    /* ------------------------------------------------------------------ */

    function loadCounts() {
      /* Încercăm întâi endpoint-ul dedicat și ultra-ușor */
      var lightweightUrl = 'javascripts/body-map-counts.json';
      if (scriptUrl) {
        try { lightweightUrl = new URL('body-map-counts.json', scriptUrl).href; } catch (e) {}
      }

      fetch(lightweightUrl).then(function (r) {
        if (!r.ok) { throw new Error('HTTP ' + r.status); }
        return r.json();
      }).then(function (data) {
        if (data && typeof data === 'object') {
          counts = Object.assign({}, DEFAULT_COUNTS, data);
          refreshPanel();
          applyAvailability();
          updateSpecialBadges();
        }
      }).catch(function () {
        /* Fallback secundar la indexul complet doar dacă cel ușor lipsește */
        var fullIndexUrl = 'javascripts/protocol-forms-index.json';
        if (scriptUrl) {
          try { fullIndexUrl = new URL('protocol-forms-index.json', scriptUrl).href; } catch (e) {}
        }
        fetch(fullIndexUrl).then(function (r) {
          if (!r.ok) { throw new Error('HTTP ' + r.status); }
          return r.json();
        }).then(function (items) {
          if (!Array.isArray(items)) { return; }
          var newCounts = {};
          items.forEach(function (p) {
            if (!p || !p.modality || !p.category) { return; }
            var k = p.modality + ':' + String(p.category).toLowerCase();
            newCounts[k] = (newCounts[k] || 0) + 1;
          });
          counts = Object.assign({}, DEFAULT_COUNTS, newCounts);
          refreshPanel();
          applyAvailability();
          updateSpecialBadges();
        }).catch(function () {
          /* Rămânem cu DEFAULT_COUNTS calculate inițial */
        });
      });
    }

    function countFor(mod, cat) {
      var n = counts[mod + ':' + cat];
      return typeof n === 'number' ? n : null;
    }

    function countLabel(n) {
      if (n === null || n === undefined) { return ''; }
      return n === 1 ? '1 protocol' : n + ' protocoale';
    }

    function updateSpecialBadges() {
      Object.keys(SPECIALS).forEach(function (key) {
        var sp = SPECIALS[key];
        var total = 0;
        MOD_ORDER.forEach(function (m) {
          (sp.targets[m] || []).forEach(function (t) {
            var n = countFor(t[2], t[3]);
            if (n) { total += n; }
          });
        });
        var btn = root.querySelector('.bm-special[data-special="' + key + '"]');
        if (btn) {
          var b = btn.querySelector('.bm-special-badge');
          if (b) { b.textContent = total; }
        }
      });
    }

    /* ------------------------------------------------------------------ */
    /* Interacțiune și Navigare                                           */
    /* ------------------------------------------------------------------ */

    function targetsFor(seg) { return TARGETS[seg] || {}; }

    function segAvailable(seg, mod) {
      if (mod === 'all') { return Object.keys(targetsFor(seg)).length > 0; }
      return !!targetsFor(seg)[mod];
    }

    function allZones(seg) {
      return root.querySelectorAll('svg [data-seg="' + seg + '"]');
    }

    function setView(viewMode) {
      state.view = viewMode;
      root.querySelectorAll('.bm-view-btn').forEach(function (b) {
        var isActive = b.getAttribute('data-view') === viewMode;
        b.classList.toggle('active', isActive);
        b.setAttribute('aria-selected', isActive ? 'true' : 'false');
      });
      svgFront.style.display = viewMode === 'front' ? '' : 'none';
      svgBack.style.display = viewMode === 'back' ? '' : 'none';
      if (figureBadge) {
        figureBadge.textContent = viewMode === 'front' ? 'Vedere Anterioară (Față)' : 'Vedere Posterioară (Spate)';
      }
      tooltip.hidden = true;
      applyAvailability();
      if (state.selected) {
        allZones(state.selected).forEach(function (z) { z.classList.add('bm-selected'); });
      }
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
      /* Actualizare stare pastile de acces rapid */
      root.querySelectorAll('.bm-zone-pill').forEach(function (pill) {
        var zid = pill.getAttribute('data-zone-id');
        var ok = segAvailable(zid, state.modality);
        pill.classList.toggle('bm-pill-disabled', !ok);
      });
    }

    function select(seg, shouldScrollMobile) {
      state.selected = seg;
      root.querySelectorAll('svg [data-seg].bm-selected').forEach(function (z) {
        z.classList.remove('bm-selected');
      });
      allZones(seg).forEach(function (z) { z.classList.add('bm-selected'); });

      /* Actualizează pastilele de selecție rapidă */
      var baseKey = SEGMENTS[seg] ? SEGMENTS[seg].baseKey : seg;
      root.querySelectorAll('.bm-zone-pill').forEach(function (pill) {
        var zid = pill.getAttribute('data-zone-id');
        var match = zid === seg || zid === baseKey || (SEGMENTS[zid] && SEGMENTS[zid].baseKey === baseKey);
        pill.classList.toggle('active', match);
      });

      refreshPanel();

      /* Pe mobil (lățime mică), derulăm lin către panoul cu detalii */
      if (shouldScrollMobile && window.innerWidth <= 768) {
        var panelEl = root.querySelector('#bm-panel');
        if (panelEl) {
          panelEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
        }
      }
    }

    function targetRowsHtml(targetsMap, colorByMod) {
      var html = '';
      var total = 0;
      MOD_ORDER.forEach(function (m) {
        var list = targetsMap[m];
        if (!list) { return; }
        list.forEach(function (t) {
          total++;
          var n = countFor(t[2], t[3]);
          var badgeColor = MODALITIES[m].color;
          var badgeStyle = ' style="--bm-color:' + badgeColor + '"';
          html += '<a class="bm-link" href="' + esc(absUrl(t[1])) + '"' + badgeStyle + '>' +
                  '<span class="bm-badge">' + MODALITIES[m].label + '</span>' +
                  '<span class="bm-link-label">' + esc(t[0]) + '</span>' +
                  (n !== null ? '<span class="bm-count">' + esc(countLabel(n)) + '</span>' : '') +
                  '<span class="bm-arrow" aria-hidden="true">→</span></a>';
        });
      });
      return { html: html, count: total };
    }

    function refreshPanel() {
      var seg = state.selected;
      if (!seg || !SEGMENTS[seg]) {
        panelSub.textContent = 'Ghid interactiv';
        panelTitle.textContent = 'Selectează o zonă de pe hartă';
        resetBtn.style.display = 'none';
        var hint = state.modality === 'all'
          ? 'Apasă pe o <strong>zonă anatomică</strong> sau folosește <strong>căutarea rapidă</strong> pentru a consulta protocoalele disponibile în toate cele 5 modalități imagistice.'
          : 'Apasă pe o regiune anatomică pentru a accesa direct colecția de protocoale <strong>' +
            esc(MODALITIES[state.modality].name || MODALITIES[state.modality].label) + '</strong>.';
        panelBody.innerHTML =
          '<div class="bm-hint-card">' +
          '  <p class="bm-hint">' + hint + '</p>' +
          '  <div class="bm-quick-tips">' +
          '    <span>💡 <strong>Sfat:</strong> Poți comuta între <em>Față</em> și <em>Spate</em> pentru coloană sau spate dorsal.</span>' +
          '  </div>' +
          '</div>';
        return;
      }

      resetBtn.style.display = 'inline-flex';
      var meta = SEGMENTS[seg];
      panelSub.textContent = 'Regiune: ' + (meta.view === 'back' ? 'Posterior' : (meta.view === 'front' ? 'Anterior' : 'Anterior / Posterior'));
      panelTitle.textContent = meta.label;

      if (state.modality === 'all') {
        var res = targetRowsHtml(targetsFor(seg), true);
        panelBody.innerHTML = res.html ||
          '<div class="bm-hint-card"><p class="bm-hint">Nu există protocoale mapate pentru această zonă.</p></div>';
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
                    '<span class="bm-arrow" aria-hidden="true">→</span></a>';
          });
          panelBody.innerHTML = rows;
        } else {
          panelBody.innerHTML =
            '<div class="bm-hint-card">' +
            '  <p class="bm-hint">Nu există protocoale ' + esc(MODALITIES[state.modality].label) +
            ' pentru „' + esc(meta.label) + '”. Încearcă modalitatea <strong>Toate</strong> pentru alte examinări.</p>' +
            '</div>';
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
      }, 2400);
    }

    function activate(seg) {
      if (!segAvailable(seg, state.modality)) {
        var modLabel = state.modality === 'all' ? '' : (' ' + MODALITIES[state.modality].label);
        showToast('Nu există protocoale' + modLabel + ' pentru „' +
                  (SEGMENTS[seg] ? SEGMENTS[seg].label : seg) + '”.');
        return;
      }
      if (state.modality !== 'all') {
        var list = targetsFor(seg)[state.modality];
        if (list && list.length) {
          window.location.href = absUrl(list[0][1]);
          return;
        }
      }
      select(seg, true);
    }

    function activateSpecial(key) {
      var sp = SPECIALS[key];
      if (!sp) { return; }
      var ok = state.modality === 'all' || !!sp.targets[state.modality];
      if (!ok) {
        showToast('Nu există protocoale ' + MODALITIES[state.modality].label + ' pentru „' + sp.label + '”.');
        return;
      }
      if (state.modality !== 'all') {
        var t = sp.targets[state.modality];
        if (t && t.length) {
          window.location.href = absUrl(t[0][1]);
          return;
        }
      }
      state.selected = null;
      root.querySelectorAll('svg [data-seg].bm-selected').forEach(function (z) {
        z.classList.remove('bm-selected');
      });
      root.querySelectorAll('.bm-zone-pill').forEach(function (p) {
        p.classList.remove('active');
      });
      resetBtn.style.display = 'inline-flex';
      panelSub.textContent = 'Secțiune specială';
      panelTitle.textContent = (sp.icon ? sp.icon + ' ' : '') + sp.label;
      var res = targetRowsHtml(sp.targets, true);
      panelBody.innerHTML = res.html ||
        '<div class="bm-hint-card"><p class="bm-hint">Nu există protocoale mapate.</p></div>';

      if (window.innerWidth <= 768) {
        var panelEl = root.querySelector('#bm-panel');
        if (panelEl) { panelEl.scrollIntoView({ behavior: 'smooth', block: 'nearest' }); }
      }
    }

    /* ------------------------------------------------------------------ */
    /* Căutare și filtrare în timp real                                   */
    /* ------------------------------------------------------------------ */

    function filterZonesBySearch(query) {
      var q = query.trim().toLowerCase();
      searchClear.hidden = (q.length === 0);

      if (!q) {
        root.querySelectorAll('.bm-zone-pill').forEach(function (p) { p.hidden = false; });
        return;
      }

      var matchFound = false;
      var firstMatchedZid = null;

      root.querySelectorAll('.bm-zone-pill').forEach(function (p) {
        var zid = p.getAttribute('data-zone-id');
        var label = p.textContent.toLowerCase();
        var base = (SEGMENTS[zid] && SEGMENTS[zid].baseKey) || zid;
        var synList = SYNONYMS[base] || [base];

        var match = label.indexOf(q) !== -1 || synList.some(function (s) { return s.indexOf(q) !== -1; });
        p.hidden = !match;
        if (match && !firstMatchedZid) {
          firstMatchedZid = zid;
          matchFound = true;
        }
      });

      return { found: matchFound, firstId: firstMatchedZid };
    }

    function selectFromSearch(zid) {
      if (!zid || !SEGMENTS[zid]) { return; }
      var meta = SEGMENTS[zid];
      /* Comută automat la vederea corectă dacă e nevoie */
      if (meta.view === 'back' && state.view !== 'back') {
        setView('back');
      } else if (meta.view === 'front' && state.view !== 'front') {
        setView('front');
      }
      activate(zid);
    }

    /* ------------------------------------------------------------------ */
    /* Evenimente și Ascultători                                           */
    /* ------------------------------------------------------------------ */

    /* Evenimente pe zonele SVG */
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
        setView(btn.getAttribute('data-view'));
      });
    });

    /* Selector modalitate */
    root.querySelectorAll('.bm-chip').forEach(function (chip) {
      chip.addEventListener('click', function () {
        state.modality = chip.getAttribute('data-mod');
        root.querySelectorAll('.bm-chip').forEach(function (c) {
          var active = (c === chip);
          c.classList.toggle('active', active);
          c.setAttribute('aria-pressed', active ? 'true' : 'false');
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

    /* Pastile rapide de zonă */
    root.querySelectorAll('.bm-zone-pill').forEach(function (pill) {
      pill.addEventListener('click', function () {
        var zid = pill.getAttribute('data-zone-id');
        selectFromSearch(zid);
      });
    });

    /* Căutare rapidă */
    if (searchInput) {
      searchInput.addEventListener('input', function (ev) {
        filterZonesBySearch(ev.target.value);
      });
      searchInput.addEventListener('keydown', function (ev) {
        if (ev.key === 'Enter') {
          ev.preventDefault();
          var res = filterZonesBySearch(searchInput.value);
          if (res && res.firstId) {
            selectFromSearch(res.firstId);
          }
        }
      });
    }

    if (searchClear) {
      searchClear.addEventListener('click', function () {
        searchInput.value = '';
        filterZonesBySearch('');
        searchInput.focus();
      });
    }

    /* Buton de resetare a selecției */
    if (resetBtn) {
      resetBtn.addEventListener('click', function () {
        state.selected = null;
        root.querySelectorAll('svg [data-seg].bm-selected').forEach(function (z) {
          z.classList.remove('bm-selected');
        });
        root.querySelectorAll('.bm-zone-pill').forEach(function (p) {
          p.classList.remove('active');
        });
        refreshPanel();
      });
    }

    /* Pregătire zone: focusabile pentru accesibilitate */
    root.querySelectorAll('svg [data-seg]').forEach(function (z) {
      z.setAttribute('tabindex', '0');
      z.setAttribute('role', 'button');
    });

    applyAvailability();
    refreshPanel();
    loadCounts();
  });
})();
