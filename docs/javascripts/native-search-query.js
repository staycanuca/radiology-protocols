/* Protocol search query adapter */
/* Prepended to the installed Material worker at build time. Its original engine stays intact. */
(function () {
  'use strict';
  const STOP = new Set('de si la pentru din pe in un o care este sunt cauta arata protocol protocoale'.split(' '));
  function query(value) {
    if (typeof value !== 'string' || /[+:~^*"=]|(?:^|\s)-\S/.test(value)) return value;
    const normalized = value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();
    const words = [...new Set((normalized.match(/[a-z0-9]+/g) || []).filter(w => !STOP.has(w)))];
    // Requiring short abbreviations exactly prevents PA -> pancreas, AP -> apendicită.
    return words.map(w => '+' + w + (w.length >= 4 ? '*' : '')).join(' ');
  }
  if (typeof module !== 'undefined' && module.exports) module.exports = query;
  else self.addEventListener('message', event => {
    if (event.data?.type === 2) event.data.data = query(event.data.data);
  });
})();
