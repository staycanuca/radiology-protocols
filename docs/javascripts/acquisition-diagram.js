/**
 * acquisition-diagram.js
 * Custom SVG acquisition diagram renderer for CT protocol pages.
 * Exposed as globals on window for use in MkDocs Material pages.
 */

(function () {
  'use strict';

  // ─── 1. parseDelaySeconds ────────────────────────────────────────────────────

  /**
   * Parse the delay string from the series table into a number of seconds.
   *
   * @param {string|null} delayStr
   * @param {number} injectionDurationSeconds  - used for bolus-track fallback
   * @returns {number}
   */
  function parseDelaySeconds(delayStr, injectionDurationSeconds, salineDurationSeconds) {
    if (delayStr == null || delayStr === '' || /^n\/a$/i.test(delayStr.trim())) {
      return 0;
    }

    const s = delayStr.trim();

    // Bolus track: scan starts after injection + saline flush completes
    if (/bolus[\s-]*track(ed)?|urmarire[\s-]*bolus|urmărire[\s-]*bolus/i.test(s)) {
      const injDur = injectionDurationSeconds && injectionDurationSeconds > 0
        ? injectionDurationSeconds
        : 30;
      const salDur = salineDurationSeconds && salineDurationSeconds > 0
        ? salineDurationSeconds
        : 0;
      return injDur + salDur;
    }

    // Immediate
    if (/immediate|imediat/i.test(s)) {
      return 0;
    }

    // First integer
    const match = s.match(/(\d+)/);
    if (match) {
      return parseInt(match[1], 10);
    }

    return 0;
  }

  // Minimum gap (seconds) shown between last injection-1 phase and injection-2 bar.
  // This is a visual constant; actual clinical wait may differ.
  const SPLIT_BOLUS_GAP = 60;

  /**
   * Parse the delay string and extract both the delay in seconds and which
   * injection the phase is relative to (0-based index).
   *
   * injectionIndex is 1 only when the delay string explicitly says "from 2nd".
   *
   * @param {string|null} delayStr
   * @param {number} injectionDurationSeconds
   * @param {number} salineDurationSeconds
   * @returns {{ seconds: number, injectionIndex: number }}
   */
  function parseDelayInfo(delayStr, injectionDurationSeconds, salineDurationSeconds) {
    const injectionIndex = /\bfrom\s+(?:the\s+)?2nd\b/i.test((delayStr || '').trim()) ? 1 : 0;
    const seconds = parseDelaySeconds(delayStr, injectionDurationSeconds, salineDurationSeconds);
    return { seconds, injectionIndex };
  }

  // ─── 2. inferPhaseType ───────────────────────────────────────────────────────

  /**
   * Infer the phase type from the series name.
   *
   * @param {string} seriesName
   * @returns {'non-contrast'|'arterial'|'portal'|'delayed'|'other'}
   */
  function inferPhaseType(seriesName) {
    const s = seriesName || '';

    if (
      /non[\s-]contrast/i.test(s) ||
      /without/i.test(s) ||
      /unenhanced/i.test(s) ||
      /calcium score/i.test(s) ||
      /\bnc\b/i.test(s) ||
      /\bpre\b/i.test(s) ||
      /\bnativ\b/i.test(s) ||
      /fara[\s-]contrast/i.test(s) ||
      /fără[\s-]contrast/i.test(s) ||
      /scor[\s-]calciu/i.test(s)
    ) {
      return 'non-contrast';
    }

    if (
      /arterial/i.test(s) ||
      /arteri/i.test(s) ||
      /CTA */i.test(s) ||
      /pancreatic/i.test(s) ||
      /enteric/i.test(s) ||
      /flash/i.test(s)
    ) {
      return 'arterial';
    }

    if (/portal|venous|\bpv\b|venos|venoasa|venoasă/i.test(s)) {
      return 'portal';
    }

    if (/delayed|delay|nephrographic|excretory|equilibrium|venogram|tardiv|tardiva|tardivă|nefrogr|excret/i.test(s)) {
      return 'delayed';
    }

    return 'other';
  }

  // ─── 3. inferCoverageLabel ─────────────────────────────────────────────────────

  /**
   * Map a verbose coverage string (e.g. "Diaphragm → Pubic symphysis") to a
   * short anatomical region label (e.g. "Abdomen-Pelvis").
   *
   * @param {string} range  - raw "start → end" or coverage string
   * @returns {string}  short label
   */
  function inferCoverageLabel(range) {
    if (!range) return '';
    const s = range.toLowerCase();

    // ── Head / Brain ────────────────────────────────────────────────────────
    if (/vertex/.test(s) && /(foramen magnum|skull base)/.test(s)) return 'Head';
    if (/vertex/.test(s) && /skull base/.test(s)) return 'Head';

    // ── Face / Sinuses ──────────────────────────────────────────────────────
    if (/frontal/.test(s) && /(maxillary|hard palate|mandible)/.test(s)) return 'Face';
    if (/orbital/.test(s) && /maxillary/.test(s)) return 'Orbits';

    // ── Temporal bone ───────────────────────────────────────────────────────
    if (/eac/.test(s) && /(iac|petrous)/.test(s)) return 'Temporal Bone';

    // ── Neck ────────────────────────────────────────────────────────────────
    if (/skull base/.test(s) && /(carina|t1|thoracic inlet|sacrum)/.test(s)) return 'Neck';
    if (/aortic arch/.test(s) && /(vertex|skull base)/.test(s)) return 'Neck';
    if (/c7/.test(s) && /l1/.test(s)) return 'Spine';

    // ── Spine ───────────────────────────────────────────────────────────────
    if (/t12/.test(s) && /sacrum/.test(s)) return 'Spine';

    // ── Heart ───────────────────────────────────────────────────────────────
    if (/(lad|carina.*below|pulmonary vein|apex.*base|base.*apex)/.test(s)) return 'Heart';
    if (/carina/.test(s) && /(below heart|base of heart|costophrenic|mid heart)/.test(s)) return 'Heart';
    if (/carina level/.test(s)) return 'Heart';

    // ── Chest-Abdomen-Pelvis ────────────────────────────────────────────────
    if (/(thoracic inlet|lung)/.test(s) && /(pubic|femur|femoral|trochanter|toes)/.test(s)) return 'Chest-Abdomen-Pelvis';
    if (/diaphragm/.test(s) && /toes/.test(s)) return 'Abdomen-Pelvis-Runoff';
    if (/above the diaphragm/.test(s) && /toes/.test(s)) return 'Chest-Abdomen-Pelvis-Runoff';

    // ── Chest ───────────────────────────────────────────────────────────────
    if (/(lung|thoracic inlet)/.test(s) && /(diaphragm|costophrenic|adrenal|carina)/.test(s)) return 'Chest';
    if (/(lung|thoracic inlet)/.test(s) && /(below heart apex)/.test(s)) return 'Chest';

    // ── Abdomen-Pelvis ──────────────────────────────────────────────────────
    if (/diaphragm/.test(s) && /(pubic|symphysis|femur|femoral|trochanter)/.test(s)) return 'Abdomen-Pelvis';
    if (/lung bases/.test(s) && /(pubic|symphysis)/.test(s)) return 'Abdomen-Pelvis';
    if (/xiphoid/.test(s) && /pubic/.test(s)) return 'Abdomen-Pelvis';
    if (/mid-liver/.test(s) && /(trochanter|femur)/.test(s)) return 'Abdomen-Pelvis';

    // ── Abdomen ─────────────────────────────────────────────────────────────
    if (/diaphragm/.test(s) && /(iliac|kidney)/.test(s)) return 'Abdomen';

    // ── Renal ───────────────────────────────────────────────────────────────
    if (/kidney/.test(s)) return 'Renal';
    if (/renal/.test(s)) return 'Renal';

    // ── Pelvis ──────────────────────────────────────────────────────────────
    if (/iliac/.test(s) && /(bladder|femur|trochanter|proximal)/.test(s)) return 'Pelvis';
    if (/l3/.test(s) && /femur/.test(s)) return 'Pelvis';

    // ── Shoulder ────────────────────────────────────────────────────────────
    if (/(acromion|scapula)/.test(s) && /humerus/.test(s)) return 'Shoulder';

    // ── Elbow ───────────────────────────────────────────────────────────────
    if (/humerus/.test(s) && /(radius|ulna)/.test(s)) return 'Elbow';

    // ── Wrist / Hand ────────────────────────────────────────────────────────
    if (/(radius|ulna|carpus)/.test(s) && /(finger|carpus|hand)/.test(s)) return 'Wrist/Hand';

    // ── Upper extremity runoff ──────────────────────────────────────────────
    if (/aortic arch/.test(s) && /finger/.test(s)) return 'Upper Extremity Runoff';

    // ── Knee ────────────────────────────────────────────────────────────────
    if (/femur/.test(s) && /(tib|fib|ankle)/.test(s)) return 'Knee';

    // ── Ankle / Foot ────────────────────────────────────────────────────────
    if (/(tib|fib|calcaneus|hindfoot)/.test(s) && /(toes|hindfoot|foot)/.test(s)) return 'Ankle/Foot';

    // ── Lower extremity runoff ──────────────────────────────────────────────
    if (/(thigh)/.test(s) && /(toes|foot|ankle)/.test(s)) return 'Thigh Lower Extremity Runoff';
    if (/(knee)/.test(s) && /(toes|foot|ankle)/.test(s)) return 'Knee Lower Extremity Runoff';
    if (/(renal arteries)/.test(s) && /(toes|foot|ankle)/.test(s)) return 'Abdominal Lower Extremity Runoff';

    // ── Stent / other special ───────────────────────────────────────────────
    if (/stent/.test(s)) return 'Stent';
    if (/injury/.test(s) || /region/.test(s) || /joint/.test(s)) return 'Region of Interest';
    if (/n\/a/.test(s)) return '';

    // Fallback: return original
    return range;
  }

  // ─── 4. parseProtocolFromDOM ─────────────────────────────────────────────────

  /**
   * Parse injection and series data from the rendered MkDocs page DOM.
   *
   * @param {Document|Element} pageRoot
   * @returns {{ contrast: object|null, saline: object|null, phases: object[] }}
   */
  function parseProtocolFromDOM(pageRoot) {
    const root = pageRoot || document;

    // Saline flush duration: assumed 5s (≈ 20 mL at typical 4 mL/s flow rate).
    // No longer read from Mermaid gantt source.
    const SALINE_DURATION_SECONDS = 5;

    function findTabContent(labelText) {
      const labels = Array.from(root.querySelectorAll('label'));
      const label = labels.find(l => l.textContent.trim() === labelText);
      if (!label) return null;

      const forAttr = label.getAttribute('for');
      if (!forAttr) return null;

      const input = root.querySelector(`input#${CSS.escape(forAttr)}`);
      if (!input) return null;

      const tabSet = input.closest('.tabbed-set');
      if (!tabSet) return null;

      // More reliable: get all inputs that are direct-ish children in order
      const tabSetInputs = Array.from(tabSet.children).filter(el => el.tagName === 'INPUT');
      const idx = tabSetInputs.indexOf(input);
      if (idx === -1) return null;

      const tabContent = tabSet.querySelector('.tabbed-content');
      if (!tabContent) return null;

      const blocks = Array.from(tabContent.children).filter(el => el.classList.contains('tabbed-block'));
      return blocks[idx] || null;
    }

    function parseTable(block) {
      if (!block) return [];
      const rows = Array.from(block.querySelectorAll('tr'));
      if (rows.length === 0) return [];

      // Find header row
      const headerRow = rows.find(r => r.querySelector('th'));
      const headers = headerRow
        ? Array.from(headerRow.querySelectorAll('th')).map(th => th.textContent.trim().toLowerCase())
        : [];

      const dataRows = rows.filter(r => !r.querySelector('th') && r.querySelector('td'));
      return dataRows.map(row => {
        const cells = Array.from(row.querySelectorAll('td')).map(td => td.textContent.trim());
        if (headers.length > 0) {
          const obj = {};
          headers.forEach((h, i) => { obj[h] = cells[i] || ''; });
          return obj;
        }
        // Fallback: treat as key-value pairs
        return { key: cells[0] || '', value: cells[1] || '' };
      });
    }

    // ── Parse Injection Parameters ──────────────────────────────────────────
    const injBlock = findTabContent('Injection Parameters');
    let contrast = null;
    let saline = null;

    if (injBlock) {
      const rows = parseTable(injBlock);

      function getVal(paramName) {
        // Try header-based lookup first
        for (const row of rows) {
          if (row.parameter != null) {
            if (row.parameter.toLowerCase() === paramName.toLowerCase()) return row.value || '';
          } else if (row.key != null) {
            if (row.key.toLowerCase() === paramName.toLowerCase()) return row.value || '';
          }
        }
        return '';
      }

      const agent = getVal('Agent');
      const volume = getVal('Volume');
      const flowRate = getVal('Flow Rate');
      const durationRaw = getVal('Duration');
      const timingMethod = getVal('timing method') || getVal('timing');

      // Parse duration — may be split bolus: "18-20s + 5-10s"
      // Split on "+", extract first integer from each part.
      const durationParts = durationRaw.split('+').map(p => p.trim());
      const parsedDurations = durationParts.map(part => {
        const m = part.match(/(\d+(?:\.\d+)?)/);
        return m ? parseFloat(m[1]) : 0;
      });

      if (agent && !/^n\/a$/i.test(agent.trim())) {
        // Build a contrasts array (one entry per injection bolus).
        // contrast = first injection (backward compat).
        contrast = {
          volume, flowRate,
          durationSeconds: parsedDurations[0] || 30,
          timingMethod,
        };

        const contrasts = parsedDurations.map(dur => ({
          volume, flowRate,
          durationSeconds: dur || 30,
          timingMethod,
        }));

        // Saline: hardcoded 5s flush (≈ 20 mL at typical flow rate)
        saline = { durationSeconds: SALINE_DURATION_SECONDS };

        // Attach contrasts array to contrast for downstream use
        contrast._contrasts = contrasts;
      }
    }

    // ── Parse Series Acquisition ────────────────────────────────────────────
    const seriesBlock = findTabContent('Series Acquisition');
    const phases = [];

    if (seriesBlock) {
      const rows = parseTable(seriesBlock);
      const injDur = contrast ? contrast.durationSeconds : 0;
      const salDur = saline ? saline.durationSeconds : 0;
      // NC phase ends this many seconds before injection starts
      const NC_END_GAP = 5;

      // ── Pass 1: parse relative delays and injection index ─────────────────
      // lastPhaseEndTimes[i] tracks the latest phase end for injection i (relative to that injection's t=0).
      const lastPhaseEndTimes = [0, 0];
      const rawPhases = [];

      for (const row of rows) {
        // Normalize column access (headers may vary in casing)
        function col(names) {
          for (const n of names) {
            for (const [k, v] of Object.entries(row)) {
              if (k.toLowerCase().includes(n.toLowerCase())) return v || '';
            }
          }
          return '';
        }

        const seriesName = col(['series name', 'series', 'name']);
        if (!seriesName) continue;
        if (/^scout/i.test(seriesName.trim())) continue;

        const start = col(['start location', 'start']);
        const end = col(['end location', 'end']);
        const delay = col(['delay']);

        const phaseDuration = 5;
        const type = inferPhaseType(seriesName);
        let relativeDelay;
        let injectionIndex = 0;

        if (type === 'non-contrast' && contrast !== null) {
          // NC phase in a contrast study: bar ends NC_END_GAP seconds before injection 1
          relativeDelay = -(phaseDuration + NC_END_GAP);
          injectionIndex = 0;
        } else if (/immediate/i.test(delay.trim())) {
          // "Immediate" = right after previous scan for this injection
          injectionIndex = 0; // immediate phases always relative to injection 1
          relativeDelay = lastPhaseEndTimes[0];
        } else {
          const info = parseDelayInfo(delay, injDur, salDur);
          relativeDelay = info.seconds;
          injectionIndex = info.injectionIndex;
        }

        lastPhaseEndTimes[injectionIndex] = Math.max(
          lastPhaseEndTimes[injectionIndex],
          relativeDelay + phaseDuration
        );

        const rawRange = `${start} → ${end}`;
        rawPhases.push({
          name: seriesName,
          range: inferCoverageLabel(rawRange) || rawRange,
          relativeDelay,
          durationSeconds: phaseDuration,
          type,
          injectionIndex,
        });
      }

      // ── Pass 2: compute injection2StartTime and absolute delays ───────────
      const contrasts = (contrast && contrast._contrasts) || (contrast ? [contrast] : []);
      const isSplitBolus = contrasts.length > 1;
      const hasInj2Phases = rawPhases.some(p => p.injectionIndex === 1);

      let injection2StartTime = null;
      if (isSplitBolus && hasInj2Phases) {
        // injection 2 starts after the last injection-1 (non-NC) phase ends + gap
        const inj1End = rawPhases
          .filter(p => p.injectionIndex === 0 && p.type !== 'non-contrast')
          .reduce((max, p) => Math.max(max, p.relativeDelay + p.durationSeconds), 0);
        injection2StartTime = inj1End + SPLIT_BOLUS_GAP;
      }

      for (const ph of rawPhases) {
        const absDelay = (ph.injectionIndex === 1 && injection2StartTime != null)
          ? injection2StartTime + ph.relativeDelay
          : ph.relativeDelay;
        phases.push({
          name: ph.name,
          range: ph.range,
          delaySeconds: absDelay,
          durationSeconds: ph.durationSeconds,
          type: ph.type,
          injectionIndex: ph.injectionIndex,
        });
      }

      // Attach split-bolus metadata to contrast for renderAcquisitionDiagram
      if (contrast) {
        contrast._contrasts = contrasts;
        contrast._injection2StartTime = injection2StartTime;
      }
    }

    return { contrast, saline, phases };
  }

  // ─── 4. renderAcquisitionDiagram ─────────────────────────────────────────────

  const PHASE_COLORS = {
    'non-contrast': '#9e9e9e',
    'arterial': '#f44336',
    'portal': '#2196f3',
    'delayed': '#1565c0',
    'other': '#9e9e9e',
  };

  const DARK_PHASES = new Set(['arterial', 'portal', 'delayed']);

  const ROW_HEIGHT = 28;
  const BAR_HEIGHT = 18;
  const BAR_Y_OFFSET = 5;
  const LEFT_PAD = 8;
  const RIGHT_PAD = 8;
  const TOP_PAD = 20;
  const BOTTOM_PAD = 30;
  const LABEL_WIDTH = 100;
  const SVG_TOTAL_WIDTH = 800;

  const SVG_NS = 'http://www.w3.org/2000/svg';

  function createSVGEl(tag, attrs) {
    const el = document.createElementNS(SVG_NS, tag);
    if (attrs) {
      for (const [k, v] of Object.entries(attrs)) {
        el.setAttribute(k, v);
      }
    }
    return el;
  }

  function truncate(str, maxLen) {
    if (!str) return '';
    if (str.length <= maxLen) return str;
    return str.slice(0, maxLen) + '\u2026'; // …
  }

  /**
   * Compute the natural time extents for a protocol data object.
   * Returns { minTime, maxTime } in seconds.
   *
   * @param {{ contrast: object|null, saline: object|null, phases: object[] }} data
   * @returns {{ minTime: number, maxTime: number }}
   */
  function computeTimeExtents(data) {
    const { contrast, saline, phases } = data;
    const ncOnly = contrast === null;
    let minTime, maxTime;

    if (ncOnly) {
      minTime = 0;
      maxTime = 30;
      for (const ph of (phases || [])) {
        maxTime = Math.max(maxTime, ph.delaySeconds + ph.durationSeconds);
      }
    } else {
      // Derive minTime from actual NC phase start positions (with 5s visual margin)
      const ncPhases = (phases || []).filter(p => p.type === 'non-contrast');
      if (ncPhases.length > 0) {
        const earliestNC = Math.min(...ncPhases.map(p => p.delaySeconds));
        minTime = earliestNC - 5;
      } else {
        minTime = 0;
      }
      // Base maxTime on first injection, then extend for second injection if present
      maxTime = contrast.durationSeconds + (saline ? saline.durationSeconds : 0) + 10;
      const inj2Start = contrast._injection2StartTime;
      const contrasts = contrast._contrasts || [contrast];
      if (inj2Start != null && contrasts.length > 1) {
        const inj2End = inj2Start + contrasts[1].durationSeconds + (saline ? saline.durationSeconds : 0);
        maxTime = Math.max(maxTime, inj2End + 10);
      }
      for (const ph of (phases || [])) {
        if (ph.type !== 'non-contrast') {
          maxTime = Math.max(maxTime, ph.delaySeconds + ph.durationSeconds);
        }
      }
    }

    return { minTime, maxTime: maxTime + 20 };
  }

  /**
   * Render an SVG acquisition diagram into `container`.
   *
   * @param {Element} container
   * @param {{ contrast: object|null, saline: object|null, phases: object[] }} data
   * @param {{ minTime?: number, maxTime?: number }} [options]  - override time axis extents
   */
  function renderAcquisitionDiagram(container, data, options) {
    // Clear container
    while (container.firstChild) container.removeChild(container.firstChild);

    const { contrast, saline, phases } = data;
    const ncOnly = contrast === null;

    if (!phases || phases.length === 0) {
      const msg = document.createElement('p');
      msg.textContent = 'Nu sunt disponibile date de achiziție';
      msg.style.color = 'var(--md-default-fg-color--light, #888)';
      msg.style.fontStyle = 'italic';
      container.appendChild(msg);
      return;
    }

    // ── Determine rows ──────────────────────────────────────────────────────
    // Group phases by range for row grouping
    const rangeOrder = [];
    const rangeMap = {}; // range -> [phases]
    for (const ph of phases) {
      if (!rangeMap[ph.range]) {
        rangeOrder.push(ph.range);
        rangeMap[ph.range] = [];
      }
      rangeMap[ph.range].push(ph);
    }

    const hasInjection = !ncOnly;
    const injectionRowCount = hasInjection ? 1 : 0;
    const phaseRowCount = rangeOrder.length;
    const totalRows = injectionRowCount + phaseRowCount;

    // ── Resolve overlapping phases in the same row ──────────────────────────
    // Multi-phase protocols (e.g. respiratory: Inspiration + Mid-Expiration)
    // may have non-numeric delays that all parse to t=0, causing bars to
    // overlay each other. Spread them out end-to-end in document order.
    for (const range of rangeOrder) {
      const rowPhases = rangeMap[range];
      if (rowPhases.length < 2) continue;

      const hasOverlap = rowPhases.some((a, i) =>
        rowPhases.slice(i + 1).some(b =>
          a.delaySeconds < b.delaySeconds + b.durationSeconds &&
          b.delaySeconds < a.delaySeconds + a.durationSeconds
        )
      );

      if (hasOverlap) {
        let cursor = Math.min(...rowPhases.map(p => p.delaySeconds));
        for (const ph of rowPhases) {
          ph.delaySeconds = cursor;
          cursor += ph.durationSeconds + 10;
        }
      }
    }

    // ── Time extents ────────────────────────────────────────────────────────
    const natural = computeTimeExtents(data);
    let minTime = (options && options.minTime != null) ? options.minTime : natural.minTime;
    let maxTime = (options && options.maxTime != null) ? options.maxTime : natural.maxTime;

    // Ensure sequential layout didn't push phases past the computed max
    for (const ph of phases) {
      maxTime = Math.max(maxTime, ph.delaySeconds + ph.durationSeconds + 5);
    }

    const timeRange = maxTime - minTime;
    const svgContentWidth = SVG_TOTAL_WIDTH - LEFT_PAD - LABEL_WIDTH - RIGHT_PAD;
    const pixelsPerSecond = svgContentWidth / timeRange;

    function xAtTime(t) {
      return LEFT_PAD + LABEL_WIDTH + (t - minTime) * pixelsPerSecond;
    }

    // ── SVG dimensions ──────────────────────────────────────────────────────
    const totalHeight = TOP_PAD + totalRows * ROW_HEIGHT + BOTTOM_PAD;

    const svg = createSVGEl('svg', {
      viewBox: `0 0 ${SVG_TOTAL_WIDTH} ${totalHeight}`,
      width: '100%',
      preserveAspectRatio: 'xMinYMin meet',
      'aria-label': 'Diagramă achiziție protocol',
      role: 'img',
    });

    // ── Helper: render a bar with optional label ────────────────────────────
    function renderBar(parentEl, x, y, width, height, fill, labelText, labelColor, forceInside = false) {
      if (width <= 0) return;

      const rect = createSVGEl('rect', {
        x, y, width, height,
        rx: 4, ry: 4,
        fill,
      });
      parentEl.appendChild(rect);

      if (labelText) {
        const inside = forceInside || width >= 70;

        let textAnchor = 'middle';
        let textX = x + width / 2;

        if (inside && width < 70) {
          // If cramped inside, align left so we read the start of the word
          textAnchor = 'middle';
          textX = x + (width / 2);
        } else if (!inside) {
          // If outside, put it to the right
          textAnchor = 'start';
          textX = x + width + 4;
        }

        // Use currentColor when outside the bar so it adapts to light/dark mode
        const textFill = inside ? (labelColor || '#fff') : 'currentColor';

        const text = createSVGEl('text', {
          x: textX,
          y: y + height / 2 + 4, // vertical center
          'text-anchor': textAnchor,
          'font-size': 10,
          fill: textFill,
          'font-family': 'inherit',
        });

        // Smart abbreviation for tiny boxes
        let displayLabel = labelText;
        if (inside && width < 50) {
          if (labelText.toLowerCase() === 'contrast') displayLabel = 'Con';
          else if (labelText.toLowerCase() === 'ser') displayLabel = 'S';
          else if (labelText.toLowerCase() === 'saline') displayLabel = 'S';
          else displayLabel = labelText.substring(0, 3) + '\u2026';
        } else {
          displayLabel = truncate(labelText, 20);
        }
        text.textContent = displayLabel;

        // Clip text to bar if inside
        if (inside) {
          const clipId = `clip-${Math.random().toString(36).slice(2)}`;
          const clipPath = createSVGEl('clipPath', { id: clipId });
          const clipRect = createSVGEl('rect', { x, y: y - 2, width, height: height + 4 });
          clipPath.appendChild(clipRect);
          parentEl.appendChild(clipPath);
          text.setAttribute('clip-path', `url(#${clipId})`);
        }

        parentEl.appendChild(text);
      }
    }

    // ── Helper: render row label ────────────────────────────────────────────
    function renderRowLabel(parentEl, rowIndex, labelText) {
      const y = TOP_PAD + rowIndex * ROW_HEIGHT + ROW_HEIGHT / 2 + 4;
      const text = createSVGEl('text', {
        x: LEFT_PAD,
        y,
        'text-anchor': 'start',
        'font-size': 11,
        fill: 'currentColor',
        'font-family': 'inherit',
      });
      text.textContent = truncate(labelText, 22);
      parentEl.appendChild(text);
    }

    // ── Row 0: Injection ────────────────────────────────────────────────────
    let currentRow = 0;

    if (hasInjection) {
      renderRowLabel(svg, currentRow, 'Injectare');

      const rowY = TOP_PAD + currentRow * ROW_HEIGHT + BAR_Y_OFFSET;
      const splitContrasts = (contrast._contrasts && contrast._contrasts.length > 1) ? contrast._contrasts : null;
      const inj2Start = contrast._injection2StartTime;

      // First injection bar
      const c1Dur = (splitContrasts ? splitContrasts[0] : contrast).durationSeconds;
      const contrastStart = xAtTime(0);
      const contrastWidth = c1Dur * pixelsPerSecond;
      const c1Label = splitContrasts ? 'Contrast 1' : 'Contrast';
      renderBar(svg, contrastStart, rowY, contrastWidth, BAR_HEIGHT, '#4caf50', c1Label, '#fff', true);

      // Saline after first injection
      if (saline && saline.durationSeconds > 0) {
        const salineStart = xAtTime(c1Dur);
        const salineWidth = saline.durationSeconds * pixelsPerSecond;
        renderBar(svg, salineStart, rowY, salineWidth, BAR_HEIGHT, '#4ed5ff', 'Ser', '#333', true);
      }

      // Second injection bar (only when phases explicitly reference injection 2)
      if (splitContrasts && inj2Start != null) {
        const c2Dur = splitContrasts[1].durationSeconds;
        const c2BarX = xAtTime(inj2Start);
        const c2Width = c2Dur * pixelsPerSecond;
        renderBar(svg, c2BarX, rowY, c2Width, BAR_HEIGHT, '#4caf50', 'Contrast 2', '#fff', true);

        // Saline after second injection
        if (saline && saline.durationSeconds > 0) {
          const saline2Start = xAtTime(inj2Start + c2Dur);
          const salineWidth = saline.durationSeconds * pixelsPerSecond;
          renderBar(svg, saline2Start, rowY, salineWidth, BAR_HEIGHT, '#4ed5ff', 'Ser', '#333', true);
        }
      }

      currentRow++;
    }

    // ── Phase rows ──────────────────────────────────────────────────────────
    for (const range of rangeOrder) {
      const phasesInRow = rangeMap[range];
      renderRowLabel(svg, currentRow, range);

      const rowY = TOP_PAD + currentRow * ROW_HEIGHT + BAR_Y_OFFSET;

      for (const ph of phasesInRow) {
        const barX = xAtTime(ph.delaySeconds);
        const barW = ph.durationSeconds * pixelsPerSecond;
        const fill = PHASE_COLORS[ph.type] || PHASE_COLORS.other;
        const textColor = DARK_PHASES.has(ph.type) ? '#fff' : '#333';
        renderBar(svg, barX, rowY, barW, BAR_HEIGHT, fill, ph.name, textColor);
      }

      currentRow++;
    }

    // ── Axis ────────────────────────────────────────────────────────────────
    const axisY = TOP_PAD + totalRows * ROW_HEIGHT;
    const axisXStart = xAtTime(minTime);
    const axisXEnd = xAtTime(maxTime);

    // Horizontal axis line
    const axisLine = createSVGEl('line', {
      x1: axisXStart, y1: axisY,
      x2: axisXEnd, y2: axisY,
      stroke: 'currentColor',
      'stroke-width': 1,
      opacity: 0.4,
    });
    svg.appendChild(axisLine);

    // Tick interval
    const tickInterval = maxTime > 120 ? 30 : 10;

    // Ticks and labels
    const firstTick = Math.ceil(minTime / tickInterval) * tickInterval;
    for (let t = firstTick; t <= maxTime; t += tickInterval) {
      const tx = xAtTime(t);

      const tick = createSVGEl('line', {
        x1: tx, y1: axisY,
        x2: tx, y2: axisY + 5,
        stroke: 'currentColor',
        'stroke-width': 1,
        opacity: 0.4,
      });
      svg.appendChild(tick);

      const tickLabel = createSVGEl('text', {
        x: tx,
        y: axisY + 14,
        'text-anchor': 'middle',
        'font-size': 9,
        fill: 'currentColor',
        opacity: 0.6,
        'font-family': 'inherit',
      });
      tickLabel.textContent = t;
      svg.appendChild(tickLabel);
    }

    // t=0 vertical milestone line (only if not NC-only, where t=0 has meaning)
    if (!ncOnly) {
      const zeroX = xAtTime(0);
      const zeroLine = createSVGEl('line', {
        x1: zeroX, y1: TOP_PAD,
        x2: zeroX, y2: axisY,
        stroke: '#555',
        'stroke-dasharray': '4,3',
        'stroke-width': 1,
        opacity: 0.7,
      });
      svg.appendChild(zeroLine);
    }

    // Axis label
    const axisLabelText = ncOnly
      ? 'Timp (secunde de la startul scanării)'
      : 'Timp (secunde de la startul injectării)';

    const axisLabel = createSVGEl('text', {
      x: LEFT_PAD + LABEL_WIDTH + svgContentWidth / 2,
      y: axisY + 26,
      'text-anchor': 'middle',
      'font-size': 9,
      fill: 'currentColor',
      opacity: 0.5,
      'font-family': 'inherit',
    });
    axisLabel.textContent = axisLabelText;
    svg.appendChild(axisLabel);

    container.appendChild(svg);
  }

  // ─── Expose globals ───────────────────────────────────────────────────────────

  window.parseDelaySeconds = parseDelaySeconds;
  window.parseDelayInfo = parseDelayInfo;
  window.inferPhaseType = inferPhaseType;
  window.inferCoverageLabel = inferCoverageLabel;
  window.parseProtocolFromDOM = parseProtocolFromDOM;
  window.computeTimeExtents = computeTimeExtents;
  window.renderAcquisitionDiagram = renderAcquisitionDiagram;

})();
