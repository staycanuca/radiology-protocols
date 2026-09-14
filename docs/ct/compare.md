---
title: Instrument de Comparare Protocoale CT
hide:
  - navigation
  - toc
---
# Instrument de Comparare Protocoale CT

Compară mai multe protocoale CT în paralel pentru a analiza diferențele în strategiile de contrast, temporizare și parametrii de achiziție.

<style>
.protocoller-search-container {
  margin-bottom: 32px;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
}
.protocoller-input-wrapper {
  display: flex;
  align-items: center;
  gap: 0;
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 50px;
  padding: 4px 4px 4px 16px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.05);
  transition: all 0.3s ease;
}
.protocoller-input-wrapper:focus-within {
  border-color: var(--md-primary-fg-color);
  box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
.search-icon {
  color: var(--md-default-fg-color--light);
  margin-right: 10px;
}
.protocoller-input {
  flex: 1;
  border: none !important;
  background: transparent !important;
  padding: 10px 0 !important;
  font-size: 0.95rem;
  outline: none !important;
  color: var(--md-default-fg-color);
}
.protocoller-submit-btn {
  background: var(--md-primary-fg-color);
  color: white;
  border: none;
  border-radius: 50px;
  padding: 10px 24px;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: background 0.2s;
}
.protocoller-submit-btn:hover {
  background: var(--md-accent-fg-color);
}
.protocoller-results {
  margin-bottom: 40px;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-start;
  gap: 16px;
  padding: 20px;
  background: rgba(var(--md-primary-fg-color--rgb), 0.03);
  border-radius: 12px;
  min-height: 100px;
}
.protocol-rec-card {
  flex: 1 1 calc(33.333% - 16px);
  min-width: 250px;
  max-width: calc(33.333% - 16px);
  padding: 20px;
  border: 1px solid var(--md-default-fg-color--lightest);
  background: var(--md-default-bg-color);
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  border-left: 4px solid var(--md-primary-fg-color);
  display: flex;
  flex-direction: column;
  position: relative;
}
.protocol-rec-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 20px rgba(0,0,0,0.1);
  border-color: var(--md-primary-fg-color);
}
.rec-badge {
  position: absolute;
  top: 12px;
  right: 12px;
  font-size: 0.7rem;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}
.badge-standard {
  background: rgba(var(--md-primary-fg-color--rgb), 0.1);
  color: var(--md-primary-fg-color);
}
.badge-custom {
  background: rgba(233, 30, 99, 0.1);
  color: #e91e63;
}
.rec-title {
  font-weight: bold;
  font-size: 1.35em;
  color: var(--md-primary-fg-color);
  margin-bottom: 8px;
  padding-right: 60px; /* Space for badge */
}
.rec-reasoning {
  font-size: 0.85em;
  opacity: 0.8;
  line-height: 1.5;
  flex-grow: 1;
}
.rec-action-hint {
  margin-top: 12px;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--md-primary-fg-color);
  opacity: 0.7;
}
.protocol-suggestions-container {
  margin-top: 24px;
}
.protocol-suggestions-container summary {
  cursor: pointer;
  font-weight: 600;
  padding: 8px 0;
  color: var(--md-primary-fg-color);
  list-style: none;
  display: flex;
  align-items: center;
  gap: 8px;
}
.protocol-suggestions-container summary::-webkit-details-marker {
  display: none;
}
.protocol-suggestions-container summary::before {
  content: '▶';
  font-size: 0.8em;
  transition: transform 0.2s;
}
.protocol-suggestions-container[open] summary::before {
  transform: rotate(90deg);
}
.pulse {
  display: inline-block;
  animation: pulse 2s infinite;
}
/* Searchable Select Styling */
.searchable-select-container {
  position: relative;
  width: 100%;
  max-width: 400px;
}
.search-select-input {
  width: 100%;
  padding: 10px 16px;
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 8px;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
  font-size: 0.9rem;
  outline: none;
  transition: border-color 0.2s;
}
.search-select-input:focus {
  border-color: var(--md-primary-fg-color);
}
.search-select-results {
  position: absolute;
  top: 100%;
  left: 0;
  right: 0;
  z-index: 100;
  background: var(--md-default-bg-color);
  border: 1px solid var(--md-default-fg-color--lightest);
  border-radius: 8px;
  margin-top: 4px;
  max-height: 250px;
  overflow-y: auto;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  display: none;
}
.search-select-results.active {
  display: block;
}
.search-select-item {
  padding: 8px 16px;
  cursor: pointer;
  font-size: 0.85rem;
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
}
.search-select-item:last-child {
  border-bottom: none;
}
.search-select-item:hover, .search-select-item.highlighted {
  background: rgba(var(--md-primary-fg-color--rgb), 0.1);
  color: var(--md-primary-fg-color);
}
.search-select-item .category {
  display: block;
  font-size: 0.7rem;
  opacity: 0.6;
  text-transform: uppercase;
}
@keyframes pulse {
  0% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.2); opacity: 0.7; }
  100% { transform: scale(1); opacity: 1; }
}
</style>

<!-- Search Bar is commented out for now until backend can be hooked up>
<!-- Sleek AI Protocolizer Search Bar
<div class="protocoller-search-container">
  <div class="protocoller-input-wrapper">
    <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
    <input type="text" id="protocoller-input" class="protocoller-input" placeholder="Search for protocols by clinical indication (e.g. 'Hematuria')...">
    <button id="protocoller-btn" class="protocoller-submit-btn">
      <span>Search</span>
    </button>
  </div>
  <div id="protocoller-loading" style="display: none; margin-top: 8px; color: var(--md-default-fg-color--light); font-size: 0.85em; text-align: center;">
  Matching clinical indications...
  </div>
</div> -->

<details id="protocol-suggestions-wrapper" class="protocol-suggestions-container" style="display: none;">
  <summary>Sugestii de Protocoale</summary>
  <div id="protocoller-results" class="protocoller-results"></div>
</details>
<div id="protocol-compare-container">
  <div class="protocol-selector">
    <h3>Selectează Protocoalele pentru Comparare</h3>
    <div id="protocol-selectors">
      <select id="protocol-select-1" class="protocol-select">
        <option value="">-- Selectează Protocolul 1 --</option>
      </select>
      <select id="protocol-select-2" class="protocol-select">
        <option value="">-- Selectează Protocolul 2 --</option>
      </select>
    </div>
    <button id="add-protocol-btn" class="md-button">+ Adaugă Protocol</button>
    <button id="compare-btn" class="md-button md-button--primary">Compară</button>
    <button id="clear-btn" class="md-button">Resetează</button>
    <button id="copy-link-btn" class="md-button" style="display:none;">🔗 Copiază Link</button>
  </div>

  <div id="comparison-results" style="display: none;">
    <!-- Gantt Diagrams -->
    <div id="gantt-comparison" class="gantt-grid">
      <h3>Comparare Cronologie Achiziție</h3>
      <div id="gantt-container" class="gantt-container"></div>
    </div>

    <!-- Contrast Comparison -->
    <div id="contrast-comparison">
      <h3>Comparare Strategie de Contrast</h3>
      <div id="contrast-table-container"></div>
    </div>

    <!-- Technical Parameters Comparison -->
    <div id="tech-params-comparison">
      <h3>Comparare Parametri Tehnici de Achiziție</h3>
      <div id="tech-params-table-container"></div>
    </div>

    <!-- Series Comparison -->
    <div id="series-comparison">
      <h3>Comparare Serii de Achiziție</h3>
      <div id="series-table-container"></div>
    </div>
  </div>
</div>