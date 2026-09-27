# Asistentul de documentare

Pagina `/ai/` și widgetul folosesc `ai-core.js` pentru căutare și `ai-assistant.js` pentru interfață. Căutarea locală este implicită. Catalogul `javascripts/ai-library.json` este generat de hookul `ai_catalog.py` din metadatele actuale ale protocoalelor, inclusiv referințe și starea revizuirii. Indexul nu este o validare medicală și nu indexează integral textul liber al paginilor.

Puter se încarcă doar când utilizatorul cere conectarea sau trimite o întrebare cu acest furnizor selectat. Marked și DOMPurify sunt incluse local, cu versiuni fixe, și se încarcă la primul răspuns. Răspunsurile Markdown sunt sanitizate, iar URL-urile sunt limitate la HTTP/HTTPS. Nu se salvează conversațiile în localStorage; sunt păstrate doar preferințele furnizorului și modelului.

Serverul local expune opțional Gemini și OpenAI, conform cheilor din mediul său. `OPENAI_MODEL` are implicit `gpt-4o-mini`; `GEMINI_MODEL` are implicit `gemini-2.5-flash`. Cheile `OPENAI_API_KEY`, `GEMINI_API_KEY`/`GOOGLE_API_KEY` rămân pe server. Nu include chei în JavaScript sau în fișiere publicate. Endpointurile serverului de administrare sunt destinate utilizării locale, nu expunerii publice ca serviciu AI.

Fiecare cerere folosește numai furnizorul ales. Dacă acesta eșuează, se returnează documentele găsite, etichetate ca rezultate locale. Nu se apelează alt furnizor. Fără documente relevante nu se cere o completare AI. Istoricul este limitat la șase mesaje; întrebarea curentă apare o singură dată. Schimbarea furnizorului, modelului sau filtrului golește contextul trimis pentru următoarea întrebare.

Oprirea în browser anulează așteptarea și împiedică afișarea fragmentelor întârziate. Nu garantează anularea procesării sau a costurilor la furnizor. Conectarea unui cont nu confirmă o calificare medicală. Endpointul Google verifică semnătura, audiența și expirarea tokenului cu biblioteca Google Auth și necesită `GOOGLE_CLIENT_ID`.

## Verificare locală

```powershell
python -m pytest tests/test_ai_service.py tests/test_ai_safety.py -q
npm install --prefix .cache/ai-test --no-audit --no-fund --ignore-scripts jsdom@29.1.1 dompurify@3.4.16 marked@18.0.14
node --test tests/test_ai_frontend.cjs
python -m mkdocs build
```

Testele folosesc furnizori simulați: nu verifică disponibilitatea modelelor, facturarea sau corectitudinea medicală a răspunsurilor generate. Testele DOM acoperă surse, subdirectoare, stocare blocată, filtrare, sanitizare, trimitere unică, oprire și reluare. O verificare vizuală în browser și o probă cu un cont propriu sunt utile înainte de publicare.

Documentație de integrare: [Puter chat](https://docs.puter.com/AI/chat/), [OpenAI prompting](https://developers.openai.com/api/docs/guides/prompt-engineering), [verificarea tokenurilor Google](https://developers.google.com/identity/gsi/web/guides/verify-google-id-token).
