/**
 * ai-assistant.js — Asistent AI Clinic & Autentificare Prietenoasă (Google & Quick Clinic)
 * Suportă comutarea transparentă între Google Gemini și OpenAI.
 * Oferă widget plutitor și interfață dedicată în /radiology-protocols/ai/.
 */

(function () {
  'use strict';

  // Determinare URL backend API (implicit Flask pe port 5173 sau origin curent)
  const API_BASE = (window.location.port === '5173')
    ? ''
    : 'http://localhost:5173';

  // Stare locală
  let currentUser = null;
  let activeProvider = 'gemini'; // 'gemini' | 'openai'
  let activeMode = 'all'; // 'all' | 'iris' | 'ct'
  let chatHistory = [];
  let availableProviders = { gemini: true, openai: false };
  let googleClientId = null;
  let isBackendAvailable = false;

  // Încărcare utilizator salvat în localStorage
  try {
    const savedUser = localStorage.getItem('rad_ai_user');
    if (savedUser) {
      currentUser = JSON.parse(savedUser);
    }
  } catch (e) {}

  // -------------------------------------------------------------------------
  // Verificare Stare Backend & Google Auth
  // -------------------------------------------------------------------------

  async function checkBackendStatus() {
    try {
      const res = await fetch(`${API_BASE}/api/ai/auth/status`, {
        method: 'GET',
        headers: { 'Accept': 'application/json' },
      });
      if (res.ok) {
        isBackendAvailable = true;
        const data = await res.json();
        if (data.providers) {
          availableProviders = data.providers;
        }
        if (data.google_client_id) {
          googleClientId = data.google_client_id;
        }
        if (data.user && !currentUser) {
          currentUser = data.user;
          localStorage.setItem('rad_ai_user', JSON.stringify(currentUser));
        }
      } else {
        isBackendAvailable = false;
      }
    } catch (err) {
      isBackendAvailable = false;
      console.warn('[AI Assistant] Backend offline sau inaccesibil pe ' + API_BASE + ' — se activează motorul clinic offline IRIS.');
    }
    updateAllUI();
  }

  // -------------------------------------------------------------------------
  // Google Sign-In Setup (Google Identity Services)
  // -------------------------------------------------------------------------

  function loadGoogleSDK() {
    if (window.google && window.google.accounts) return;
    const script = document.createElement('script');
    script.src = 'https://accounts.google.com/gsi/client';
    script.async = true;
    script.defer = true;
    document.head.appendChild(script);
  }

  function renderGoogleButton(containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    if (!googleClientId) {
      container.innerHTML = `
        <div class="ai-auth-local-tip">
          <p>Pentru conectare oficială cu Google în producție, specificați <code>GOOGLE_CLIENT_ID</code> în fișierul <code>.env</code>.</p>
          <button id="ai-quick-login-btn" class="ai-btn-quick-login">
            🩺 Conectare Rapidă ca Medic / Radiolog
          </button>
        </div>
      `;
      const qBtn = document.getElementById('ai-quick-login-btn');
      if (qBtn) {
        qBtn.addEventListener('click', handleQuickLogin);
      }
      return;
    }

    if (window.google && window.google.accounts && window.google.accounts.id) {
      window.google.accounts.id.initialize({
        client_id: googleClientId,
        callback: handleGoogleResponse,
      });
      window.google.accounts.id.renderButton(container, {
        theme: 'outline',
        size: 'large',
        text: 'signin_with',
        shape: 'pill',
        logo_alignment: 'left',
      });
    } else {
      setTimeout(() => renderGoogleButton(containerId), 300);
    }
  }

  async function handleGoogleResponse(response) {
    if (!response || !response.credential) return;
    try {
      const res = await fetch(`${API_BASE}/api/ai/auth/google`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ credential: response.credential }),
      });
      const data = await res.json();
      if (data.ok && data.user) {
        currentUser = data.user;
        localStorage.setItem('rad_ai_user', JSON.stringify(currentUser));
        updateAllUI();
      }
    } catch (e) {
      alert('Eroare la autentificarea Google: ' + e);
    }
  }

  async function handleQuickLogin() {
    const name = prompt('Introduceți numele dvs. (ex: Dr. Andrei Ionescu):', 'Dr. Medic Radiolog');
    if (!name) return;
    try {
      const res = await fetch(`${API_BASE}/api/ai/auth/quick`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: name, role: 'Medic Radiolog' }),
      });
      const data = await res.json();
      if (data.ok && data.user) {
        currentUser = data.user;
        localStorage.setItem('rad_ai_user', JSON.stringify(currentUser));
        updateAllUI();
      }
    } catch (e) {
      // Fallback local pur în browser
      currentUser = {
        name: name,
        email: `${name.toLowerCase().replace(/\s+/g, '.')}@radiologie.spital.ro`,
        picture: 'https://api.dicebear.com/7.x/bottts/svg?seed=' + encodeURIComponent(name),
        role: 'Medic Radiolog',
      };
      localStorage.setItem('rad_ai_user', JSON.stringify(currentUser));
      updateAllUI();
    }
  }

  async function handleLogout() {
    try {
      await fetch(`${API_BASE}/api/ai/auth/logout`, { method: 'POST' });
    } catch (e) {}
    currentUser = null;
    localStorage.removeItem('rad_ai_user');
    updateAllUI();
  }

  // -------------------------------------------------------------------------
  // Motor Clinic Local Offline (Ghidul Național IRIS & Fallback Static)
  // -------------------------------------------------------------------------

  function stripDiacritics(str) {
    if (!str) return '';
    return str
      .normalize('NFD')
      .replace(/[\u0300-\u036f]/g, '')
      .replace(/[șş]/g, 's')
      .replace(/[țţ]/g, 't')
      .replace(/[ăâ]/g, 'a')
      .replace(/[îï]/g, 'i')
      .toLowerCase();
  }

  const STOP_WORDS = new Set([
    'de', 'la', 'in', 'si', 'cu', 'pe', 'sub', 'din', 'un', 'o', 'unui', 'unei',
    'ce', 'care', 'este', 'sunt', 'pentru', 'recomanzi', 'recomandat', 'recomandata',
    'investigatie', 'investigatii', 'protocol', 'protocoale', 'cand', 'cum', 'sau',
    'mai', 'bun', 'buna', 'indicat', 'indicata', 'pacient', 'pacientul', 'pacienta',
    'ani', 'an', 'varsta', 'dupa', 'prin', 'ale', 'lui', 'ei', 'ai', 'fara'
  ]);

  function getDoseBadge(doseMin, doseMax) {
    const d = doseMax !== undefined && doseMax !== null ? doseMax : (doseMin || 0);
    if (d === 0) return '`○○○○` *(Clasa 0 — Fără Iradiere)*';
    if (d === 1) return '`●○○○` *(Clasa 1 — Minimă < 1 mSv)*';
    if (d === 2) return '`●●○○` *(Clasa 2 — Mică 1-5 mSv)*';
    if (d === 3) return '`●●●○` *(Clasa 3 — Moderată 5-10 mSv)*';
    return '`●●●●` *(Clasa 4 — Mare > 10 mSv)*';
  }

  function getIndicationBadge(ind) {
    const s = stripDiacritics(ind || '').toLowerCase();
    if (s.includes('indicat') && !s.includes('neindicat')) return '🟢 **INDICAT**';
    if (s.includes('specializat') || s.includes('aviz')) return '🟡 **AVIZ SPECIALIZAT**';
    if (s.includes('particular') || s.includes('cazuri')) return '🟠 **CAZURI PARTICULARE**';
    if (s.includes('neindicat') || s.includes('contraindicat')) return '🔴 **NEINDICAT**';
    return '🔵 **' + (ind || 'OPȚIUNE') + '**';
  }

  function generateOfflineReply(query, mode) {
    if (!window.IRIS || !window.IRIS.situations || !window.IRIS.recommendations) {
      return null;
    }

    const qClean = stripDiacritics(query.trim());
    const tokens = qClean
      .split(/[^a-z0-9]+/)
      .filter(t => t.length > 2 && !STOP_WORDS.has(t));

    if (tokens.length === 0) {
      return 'Vă rugăm să specificați mai multe detalii clinice (de exemplu: simptomul, regiunea anatomică sau suspiciunea de diagnostic a pacientului).';
    }

    if (!window._irisRecsMap) {
      window._irisRecsMap = new Map();
      (window.IRIS.recommendations || []).forEach(r => {
        if (!window._irisRecsMap.has(r.situationId)) {
          window._irisRecsMap.set(r.situationId, []);
        }
        window._irisRecsMap.get(r.situationId).push(r);
      });
    }

    const recsMap = window._irisRecsMap;
    const scored = [];

    for (const sit of window.IRIS.situations) {
      if (sit.placeholder) continue;
      const sName = stripDiacritics(sit.name || '');
      let score = 0;

      if (sName.includes(qClean)) {
        score += 50;
      }

      let matchedTokens = 0;
      for (const t of tokens) {
        if (sName.includes(t)) {
          matchedTokens++;
          score += 15;
        }
      }
      if (matchedTokens === tokens.length && tokens.length > 1) {
        score += 30;
      }

      const recs = recsMap.get(sit.id) || [];
      for (const r of recs) {
        const comm = stripDiacritics((r.comments || '') + ' ' + (r.otherInfo || ''));
        for (const t of tokens) {
          if (comm.includes(t)) {
            score += 2;
          }
        }
      }

      if (score > 0) {
        scored.push({ sit, recs, score });
      }
    }

    scored.sort((a, b) => b.score - a.score);

    if (scored.length === 0) {
      return `Nu a fost găsită o situație clinică exactă în Ghidul IRIS pentru: **"${query}"**.\n\n` +
        `💡 **Sugestii:**\n` +
        `- Căutați după simptome sau suspiciuni frecvente (de ex: *apendicită*, *durere toracică*, *cefalee*, *trombembolism*, *traumatism genunchi*, *hematurie*, *litiază*).\n` +
        `- Puteți naviga direct în [Ghidul Interactiv IRIS](iris/) pe capitole anatomice.\n\n` +
        `> ℹ️ *Pentru procesare conversațională prin AI generativ (Google Gemini / OpenAI GPT-4o), asigurați-vă că serverul local este pornit rulând în terminal:*\n` +
        `> \`\`\`bash\n` +
        `> python run.py --all\n` +
        `> \`\`\``;
    }

    const topMatches = scored.slice(0, 3);
    let out = `### 🩺 Recomandare Clinică conform Ghidului Național IRIS (Ordinul MS 1342/2012)\n\n`;

    for (const match of topMatches) {
      const { sit, recs } = match;
      out += `#### Situație Clinică: **${sit.name}**\n\n`;

      if (!recs || recs.length === 0) {
        out += `*Nu există investigații specifice înregistrate pentru această situație.*\n\n`;
        continue;
      }

      let filteredRecs = recs;
      if (mode === 'ct') {
        filteredRecs = recs.filter(r => (r.exam || '').toLowerCase().includes('ct') || (r.exam || '').toLowerCase().includes('tomograf'));
        if (filteredRecs.length === 0) filteredRecs = recs;
      }

      for (const r of filteredRecs) {
        const badge = getIndicationBadge(r.indication);
        const gradeStr = r.grade ? ` · **Grad ${r.grade}**` : '';
        const doseStr = getDoseBadge(r.doseMin, r.doseMax);

        out += `- ${badge} — **${r.exam || 'Examinare'}**${gradeStr}\n`;
        out += `  - **Nivel iradiere:** ${doseStr}\n`;
        if (r.comments && r.comments.trim()) {
          out += `  - *Comentarii clinice:* ${r.comments.trim()}\n`;
        }
        if (r.otherInfo && r.otherInfo.trim()) {
          out += `  - *Context suplimentar:* ${r.otherInfo.trim()}\n`;
        }
      }
      out += `\n`;
    }

    out += `---\n\n`;
    out += `> ℹ️ **Mod Offline (Build Static):** Răspunsul a fost extras direct din baza de date a **Ghidului Național IRIS** (790 situații, 1655 recomandări) integrată offline în aplicație.\n`;
    out += `>\n`;
    out += `> 💡 *Pentru a activa funcțiile generative avansate (Google Gemini / OpenAI GPT-4o), porniți backend-ul local rulând în consolă: \`python run.py --all\`.*`;

    return out;
  }

  // -------------------------------------------------------------------------
  // Trimitere Mesaj către AI
  // -------------------------------------------------------------------------

  async function sendChatMessage(message, onChunkOrDone, onError) {
    if (!message || !message.trim()) return;

    chatHistory.push({ role: 'user', content: message });

    // Dacă backend-ul este indisponibil, folosim direct motorul offline
    if (!isBackendAvailable) {
      const offlineReply = generateOfflineReply(message, activeMode);
      if (offlineReply) {
        chatHistory.push({ role: 'assistant', content: offlineReply });
        onChunkOrDone(offlineReply, 'Ghid Național IRIS (Offline / Mod Static)');
        return;
      }
    }

    try {
      const res = await fetch(`${API_BASE}/api/ai/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: message,
          provider: activeProvider,
          mode: activeMode,
          history: chatHistory,
          user: currentUser,
        }),
      });

      if (!res.ok) {
        throw new Error(`Eroare server: ${res.status}`);
      }

      const data = await res.json();
      if (data.ok) {
        isBackendAvailable = true;
        chatHistory.push({ role: 'assistant', content: data.reply });
        onChunkOrDone(data.reply, data.engine);
        return;
      } else {
        throw new Error(data.error || 'Răspuns invalid de la asistentul AI.');
      }
    } catch (err) {
      console.warn('[AI Chat] Backend indisponibil pe ' + API_BASE + ', se activează motorul offline IRIS...', err);
      isBackendAvailable = false;
      updateAllUI();

      const offlineReply = generateOfflineReply(message, activeMode);
      if (offlineReply) {
        chatHistory.push({ role: 'assistant', content: offlineReply });
        onChunkOrDone(offlineReply, 'Ghid Național IRIS (Offline / Mod Static)');
        return;
      }
      onError(err.message || 'Nu s-a putut contacta serverul AI.');
    }
  }

  // -------------------------------------------------------------------------
  // Parsare Simplă Markdown în HTML
  // -------------------------------------------------------------------------

  function renderMarkdown(text) {
    if (window.marked && typeof window.marked.parse === 'function') {
      return window.marked.parse(text);
    }
    // Fallback minim
    return text
      .replace(/^### (.*$)/gim, '<h4>$1</h4>')
      .replace(/^## (.*$)/gim, '<h3>$1</h3>')
      .replace(/^# (.*$)/gim, '<h2>$1</h2>')
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>')
      .replace(/\n/g, '<br/>');
  }

  // -------------------------------------------------------------------------
  // Randare Pagină Dedicată (/ai/)
  // -------------------------------------------------------------------------

  function initDedicatedAIPage() {
    const root = document.getElementById('ai-workspace-root');
    if (!root) return;

    root.innerHTML = `
      <div class="ai-workspace">
        <!-- Bara de sus: Autentificare Prietenoasă & Comutator Modele -->
        <div class="ai-workspace-header">
          <div class="ai-user-profile-zone" id="ai-user-profile-zone">
            <!-- Populat dinamic de updateAllUI -->
          </div>
          <div class="ai-controls-zone">
            <div class="ai-provider-toggle" id="ai-provider-toggle">
              <button class="ai-provider-btn ${activeProvider === 'gemini' ? 'active' : ''}" data-provider="gemini">
                🌟 Google Gemini
              </button>
              <button class="ai-provider-btn ${activeProvider === 'openai' ? 'active' : ''}" data-provider="openai">
                ⚡ OpenAI GPT-4o
              </button>
            </div>
            <div class="ai-mode-selector">
              <select id="ai-mode-select" class="ai-mode-dropdown">
                <option value="all" ${activeMode === 'all' ? 'selected' : ''}>🩺 Mod Complet (IRIS + CT)</option>
                <option value="iris" ${activeMode === 'iris' ? 'selected' : ''}>🏛️ Doar Ghid IRIS (Indicație)</option>
                <option value="ct" ${activeMode === 'ct' ? 'selected' : ''}>⚡ Doar Protocoale CT (Tehnic)</option>
              </select>
            </div>
          </div>
        </div>

        <!-- Zona Principală de Conversație -->
        <div class="ai-chat-thread" id="ai-chat-thread">
          <div class="ai-message ai-assistant-msg">
            <div class="ai-msg-avatar">🩺</div>
            <div class="ai-msg-bubble">
              <strong>Bună ziua! Sunt Asistentul AI Clinic al Departamentului de Radiologie.</strong>
              <p>Vă pot ajuta cu:</p>
              <ul>
                <li><strong>Ghidul Național IRIS (Ordinul MS 1342/2012):</strong> recomandarea primei investigații pentru simptomele pacientului, gradul de dovezi (A/B/C) și nivelul de iradiere (ALARA).</li>
                <li><strong>Protocoalele de Scanare CT:</strong> timpi de contrast, volume, flux (mL/s), kV, mAs, modulație AEC, colimare și reconstrucții.</li>
              </ul>
              <p class="ai-tip-muted">Alegeți una dintre sugestiile clinice de mai jos sau scrieți direct cazul pacientului:</p>
            </div>
          </div>
        </div>

        <!-- Sugestii Clinice Rapide -->
        <div class="ai-prompt-chips" id="ai-prompt-chips">
          <button class="ai-chip" data-q="Copil de 8 ani cu durere acută în fosa iliacă dreaptă. Ce investigație este indicată și ce grad are?">
            👶 Apendicită la copil
          </button>
          <button class="ai-chip" data-q="Suspiciune disecție de aortă acută la pacient hipertensiv. Protocol CT și timpi de contrast.">
            🫀 Suspiciune disecție aortă
          </button>
          <button class="ai-chip" data-q="Cefalee bruscă în 'lovitură de trăsnet'. Este indicat CT nativ sau angio-CT?">
            🧠 Cefalee bruscă acută
          </button>
          <button class="ai-chip" data-q="Suspiciune trombembolism pulmonar (TEP). Tehnica injectării și bolus tracking.">
            🫁 Protocol CT TEP (Angio Pulmonar)
          </button>
          <button class="ai-chip" data-q="Calcul renal suspectat. Parametri doză CT KUB nativ low dose.">
            Kidney Litiază urinară (Low-Dose)
          </button>
        </div>

        <!-- Bara de Intrare Mesaj -->
        <div class="ai-input-bar">
          <textarea 
            id="ai-user-input" 
            class="ai-input-field" 
            placeholder="Descrieți simptomele, diagnosticul de trimitere sau protocolul CT dorit..."
            rows="2"
          ></textarea>
          <button id="ai-send-btn" class="ai-send-btn" title="Trimite întrebarea">
            <span>Trimite</span> ➤
          </button>
        </div>
      </div>
    `;

    // Evenimente Comutator Modele
    const provBtns = root.querySelectorAll('.ai-provider-btn');
    provBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        provBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        activeProvider = btn.getAttribute('data-provider');
      });
    });

    // Eveniment Mod
    const modeSelect = document.getElementById('ai-mode-select');
    if (modeSelect) {
      modeSelect.addEventListener('change', (e) => {
        activeMode = e.target.value;
      });
    }

    // Evenimente Sugestii Clinice
    const chipBtns = root.querySelectorAll('.ai-chip');
    chipBtns.forEach(c => {
      c.addEventListener('click', () => {
        const q = c.getAttribute('data-q');
        const input = document.getElementById('ai-user-input');
        if (input) {
          input.value = q;
          triggerSendMessage();
        }
      });
    });

    // Eveniment Buton Trimitere & Enter
    const sendBtn = document.getElementById('ai-send-btn');
    const userInput = document.getElementById('ai-user-input');

    function triggerSendMessage() {
      const text = userInput.value.trim();
      if (!text) return;

      appendUserMessage(text);
      userInput.value = '';

      const thread = document.getElementById('ai-chat-thread');
      const loadingEl = document.createElement('div');
      loadingEl.className = 'ai-message ai-assistant-msg ai-loading-msg';
      loadingEl.innerHTML = `
        <div class="ai-msg-avatar">🩺</div>
        <div class="ai-msg-bubble">
          <div class="ai-pulse-dot"></div> Se consultă Ghidul IRIS & Protocoalele CT...
        </div>
      `;
      thread.appendChild(loadingEl);
      thread.scrollTop = thread.scrollHeight;

      sendChatMessage(
        text,
        (reply, engine) => {
          thread.removeChild(loadingEl);
          appendAssistantMessage(reply, engine);
        },
        (err) => {
          thread.removeChild(loadingEl);
          appendAssistantMessage(`⚠️ **Atenție:** ${err}`, 'Eroare');
        }
      );
    }

    if (sendBtn) {
      sendBtn.addEventListener('click', triggerSendMessage);
    }
    if (userInput) {
      userInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
          e.preventDefault();
          triggerSendMessage();
        }
      });
    }

    updateUserProfileZone();
  }

  function appendUserMessage(text) {
    const thread = document.getElementById('ai-chat-thread') || document.getElementById('ai-widget-thread');
    if (!thread) return;
    const msg = document.createElement('div');
    msg.className = 'ai-message ai-user-msg';
    msg.innerHTML = `
      <div class="ai-msg-bubble">${escapeHtml(text)}</div>
      <div class="ai-msg-avatar user-avatar">${currentUser ? '👨‍⚕️' : '👤'}</div>
    `;
    thread.appendChild(msg);
    thread.scrollTop = thread.scrollHeight;
  }

  function appendAssistantMessage(text, engine) {
    const thread = document.getElementById('ai-chat-thread') || document.getElementById('ai-widget-thread');
    if (!thread) return;
    const msg = document.createElement('div');
    msg.className = 'ai-message ai-assistant-msg';
    const htmlContent = renderMarkdown(text);
    msg.innerHTML = `
      <div class="ai-msg-avatar">🩺</div>
      <div class="ai-msg-bubble">
        ${htmlContent}
        ${engine ? `<div class="ai-engine-tag">⚡ Motor utilizat: ${escapeHtml(engine)}</div>` : ''}
      </div>
    `;
    thread.appendChild(msg);
    thread.scrollTop = thread.scrollHeight;
  }

  function updateUserProfileZone() {
    const zone = document.getElementById('ai-user-profile-zone');
    if (!zone) return;

    const statusBadge = isBackendAvailable
      ? `<span class="ai-status-pill online" title="Conectat la serverul AI local (Port 5173)">🟢 Server AI Conectat</span>`
      : `<span class="ai-status-pill offline" title="Backend local offline (Port 5173). Asistentul utilizează motorul clinic offline IRIS. Porniți 'python run.py --all' pentru Google Gemini / OpenAI.">🍃 Mod Offline (Ghid IRIS)</span>`;

    if (currentUser) {
      zone.innerHTML = `
        <div class="ai-profile-card">
          <div class="ai-avatar-circle">
            ${currentUser.picture ? `<img src="${currentUser.picture}" alt="" />` : '👨‍⚕️'}
          </div>
          <div class="ai-profile-details">
            <span class="ai-profile-name">${escapeHtml(currentUser.name)}</span>
            <span class="ai-profile-badge">✓ Autorizat (${currentUser.role || 'Medic'})</span>
          </div>
          ${statusBadge}
          <button id="ai-logout-btn" class="ai-logout-btn" title="Deconectare">Ieșire</button>
        </div>
      `;
      const logoutBtn = document.getElementById('ai-logout-btn');
      if (logoutBtn) logoutBtn.addEventListener('click', handleLogout);
    } else {
      zone.innerHTML = `
        <div class="ai-login-prompt">
          <div id="ai-google-btn-slot"></div>
          <button id="ai-inline-quick-login" class="ai-btn-quick-login">
            🩺 Conectare Rapidă (Doctor)
          </button>
          ${statusBadge}
        </div>
      `;
      renderGoogleButton('ai-google-btn-slot');
      const qBtn = document.getElementById('ai-inline-quick-login');
      if (qBtn) qBtn.addEventListener('click', handleQuickLogin);
    }
  }

  // -------------------------------------------------------------------------
  // Floating Assistant Widget (Prezent pe toate paginile)
  // -------------------------------------------------------------------------

  function initFloatingWidget() {
    if (document.getElementById('ai-floating-widget-root')) return;

    let fullscreenUrl = 'ai/';
    if (typeof __md_scope !== 'undefined' && __md_scope && __md_scope.pathname && !location.protocol.startsWith('file')) {
      fullscreenUrl = (__md_scope.pathname.endsWith('/') ? __md_scope.pathname : __md_scope.pathname + '/') + 'ai/';
    } else {
      const depth = (location.pathname.match(/\//g) || []).length;
      fullscreenUrl = depth > 2 ? '../../ai/' : (depth > 1 ? '../ai/' : 'ai/');
    }

    const widgetRoot = document.createElement('div');
    widgetRoot.id = 'ai-floating-widget-root';
    widgetRoot.className = 'ai-widget-root';

    widgetRoot.innerHTML = `
      <!-- Buton Plutitor Deschidere -->
      <button id="ai-widget-toggle-btn" class="ai-widget-toggle" title="Deschide Asistentul AI Clinic">
        <span class="ai-toggle-icon">✨</span>
        <span class="ai-toggle-label">Asistent AI Clinic</span>
      </button>

      <!-- Panou Drawer Plutitor -->
      <div id="ai-widget-panel" class="ai-widget-panel" style="display:none;">
        <div class="ai-widget-header">
          <div class="ai-widget-title-row">
            <span class="ai-widget-icon">🩺</span>
            <div>
              <strong>Asistent AI Clinic</strong>
              <small>Ghid IRIS & Protocoale CT</small>
            </div>
          </div>
          <div class="ai-widget-actions">
            <a href="${fullscreenUrl}" class="ai-widget-fullscreen-btn" title="Deschide în pagină completă">↗</a>
            <button id="ai-widget-close-btn" class="ai-widget-close-btn" title="Închide">✕</button>
          </div>
        </div>

        <div class="ai-widget-thread" id="ai-widget-thread">
          <div class="ai-message ai-assistant-msg">
            <div class="ai-msg-avatar">🩺</div>
            <div class="ai-msg-bubble">
              Puneți o întrebare despre recomandări IRIS sau protocoale CT:
            </div>
          </div>
        </div>

        <div class="ai-widget-input-row">
          <input type="text" id="ai-widget-input" class="ai-widget-input" placeholder="Întrebați asistentul..." />
          <button id="ai-widget-send" class="ai-widget-send">➤</button>
        </div>
      </div>
    `;

    document.body.appendChild(widgetRoot);

    const toggleBtn = document.getElementById('ai-widget-toggle-btn');
    const panel = document.getElementById('ai-widget-panel');
    const closeBtn = document.getElementById('ai-widget-close-btn');
    const widgetInput = document.getElementById('ai-widget-input');
    const widgetSend = document.getElementById('ai-widget-send');

    function togglePanel() {
      if (panel.style.display === 'none') {
        panel.style.display = 'flex';
        toggleBtn.classList.add('open');
        if (widgetInput) widgetInput.focus();
      } else {
        panel.style.display = 'none';
        toggleBtn.classList.remove('open');
      }
    }

    toggleBtn.addEventListener('click', togglePanel);
    closeBtn.addEventListener('click', () => {
      panel.style.display = 'none';
      toggleBtn.classList.remove('open');
    });

    function triggerWidgetSend() {
      const txt = widgetInput.value.trim();
      if (!txt) return;

      appendUserMessage(txt);
      widgetInput.value = '';

      const thread = document.getElementById('ai-widget-thread');
      const load = document.createElement('div');
      load.className = 'ai-message ai-assistant-msg';
      load.innerHTML = `<div class="ai-msg-avatar">🩺</div><div class="ai-msg-bubble"><div class="ai-pulse-dot"></div> Procesare...</div>`;
      thread.appendChild(load);
      thread.scrollTop = thread.scrollHeight;

      sendChatMessage(
        txt,
        (reply, engine) => {
          thread.removeChild(load);
          appendAssistantMessage(reply, engine);
        },
        (err) => {
          thread.removeChild(load);
          appendAssistantMessage(`⚠️ ${err}`, 'Eroare');
        }
      );
    }

    widgetSend.addEventListener('click', triggerWidgetSend);
    widgetInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        e.preventDefault();
        triggerWidgetSend();
      }
    });
  }

  function updateAllUI() {
    updateUserProfileZone();
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  // -------------------------------------------------------------------------
  // Inițializare Generală
  // -------------------------------------------------------------------------

  async function init() {
    loadGoogleSDK();
    await checkBackendStatus();
    initDedicatedAIPage();
    initFloatingWidget();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  if (window.document$) {
    window.document$.subscribe(() => {
      initDedicatedAIPage();
      initFloatingWidget();
    });
  }
})();
