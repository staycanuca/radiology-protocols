# Omnisearch și căutarea nativă

`search_catalog.py` citește metadatele actuale și subgrupele din fișierele `.pages`. Hookul `search_enhancer.py` reconstruiește catalogul Omnisearch la fiecare build MkDocs, inclusiv după adăugări, ștergeri și schimbări de titluri sau sinonime. Indexarea respectă `search.exclude`. Comanda `python scripts/generate_omnisearch_index.py` actualizează și copia din `docs/javascripts`, folosită de launcher; fișierul final din `site/` este regenerat din paginile incluse efectiv în build.

Omnisearch utilizează schema 2: toate sinonimele și indicațiile declarate, surse, echipamente, subgrupe anatomice și starea revizuirii. Titlurile au prioritate față de potrivirile incidentale în indicații. Toți termenii semnificativi trebuie să se potrivească; nu se schimbă automat o denumire medicală prin corectare aproximativă. Dicționarul comun `data/search-aliases.json` include denumiri RO/EN și abrevieri de modalități, fără a crea indicații clinice noi.

Contrastul este clasificat din metadate în `contrast`, `native`, `variable` sau `unknown`. Lipsa informației nu înseamnă „nativ”, iar contrastul declarat nu implică automat administrare IV. Starea revizuirii este informativă și nu influențează relevanța medicală a documentelor.

Căutarea nativă rămâne motorul Material/Lunr, inclusiv gruparea pe pagini, sugestiile și evidențierea. Câmpurile au ponderi moderate: titlu și titlu normalizat 12, metadate 6, text 1. Sinonimele și sursele se adaugă paginii principale, fără a propulsa fiecare secțiune secundară. Cuvintele suplimentare sunt câmpuri indexate separate, nu etichete vizibile. Slugurile vechi nu mai primesc o pondere artificială. Secțiunile goale de proveniență sunt eliminate din index; cardul vizibil de proveniență rămâne în pagină.

Un adaptor mic (`native-search-query.js`) cere toți termenii interogării simple, normalizează diacriticele și tratează exact abrevierile de cel mult trei caractere. Operatorii avansați expliciți rămân neschimbați. Hookul construiește o copie a workerului Material cu adaptorul înaintea motorului și cu un nume derivat din conținut, apoi actualizează referința din configurația fiecărei pagini. Workerul original al temei nu este modificat. La actualizarea Material, testul de relevanță verifică protocolul de mesaje și configurarea efectiv generată.

Interogarea și filtrele Omnisearch pot fi distribuite prin URL (`omni_q`, `omni_modality`, `omni_region`, `omni_segment`, `omni_source`, `omni_contrast`). Aceste valori nu sunt păstrate în localStorage. URL-ul partajat conține termenii căutați, deci nu introduce identificatori de pacienți. Căutarea nu apelează servicii AI.

## Verificare

```powershell
python -m pytest tests/test_search_catalog.py tests/test_search_enhancer_index.py tests/test_rx_catalog.py -q
node --test tests/search_frontend.test.cjs
python -m mkdocs build
node --test tests/search_relevance.test.cjs
```

Testele DOM folosesc jsdom instalat în `.cache/ai-test` (același mediu ca testele AI). Testul de relevanță execută workerul Material construit, cu fișiere locale și fără rețea, și scrie `reports/search-relevance-validation.json`. Pentru verificarea finală se folosește un build complet, nu `--dirty`.

Configurarea motorului nativ urmează [documentația Material Search](https://squidfunk.github.io/mkdocs-material/plugins/search/).
