# Traducerea protocoalelor Rx

## Traducere integrală, reluabilă

`translate_catalog.py` inventariază toate câmpurile de conținut, inclusiv DFF/SID,
incidențele standard și titlurile secțiunilor sursă. Citările bibliografice,
identificatorii și adresele imaginilor rămân în forma originală.

```powershell
python scripts/translate_catalog.py prepare
python scripts/translate_catalog.py translate --provider codex --model gpt-5.6-luna --reasoning-effort low --workers 2 --batch-chars 12000 --batch-items 60
python scripts/translate_catalog.py apply
python scripts/rx_catalog.py
python scripts/generate_forms_index.py
```

Modul `codex` folosește sesiunea OAuth existentă prin `cli_ai.py`, fără instrumente
sau acces al agentului la fișierele proiectului. `--provider gemini` este disponibil
pentru o cheie funcțională `GEMINI_API_KEY`. Textele sunt trimise furnizorului ales.
La trei erori consecutive de serviciu, loturile rămase se opresc automat.

Progresul și originalele sunt salvate în
`.protocol-workbench/catalog-translation/`. Reexecutarea comenzii `translate`
procesează doar textele încă lipsă. `failures.json` păstrează traducerile respinse
și motivele; acestea trebuie corectate sau retraduse înainte de aplicare.

`python scripts/translate_catalog.py checkpoint` salvează progresul validat și
dicționarul reutilizabil, fără să modifice protocoalele. Pentru publicarea locală
a protocoalelor deja traduse complet se poate folosi `apply-ready`, urmat de
regenerarea indexurilor de mai sus. Protocoalele cu câmpuri încă netraduse sunt
amânate integral. Comanda `apply` rămâne condiționată de completarea catalogului.

Dacă aplicația sau documentele au fost modificate între timp, nu recrea automat
inventarul și nu restaura documentele din copii vechi. Compară modificările cu
hashurile inventarului și ale ultimei aplicări; păstrează metadatele și sursele
curente. Orice actualizare a acestor hashuri necesită verificarea diferențelor.

Aplicarea este blocată dacă lipsesc traduceri, dacă s-au schimbat documentele
de la inventariere sau dacă validarea eșuează. Validatorul compară numerele,
asocierile valoare–unitate, semnele și fracțiile și URL-urile. El nu înlocuiește
revizia sensului clinic. Fragmentele ambigue/trunchiate sunt evidențiate în raport,
fără completarea arbitrară a sursei.

Denumirile `inch/inches` după valori numerice sau fracții sunt localizate ca
`țol/țoli`, fără conversia valorilor. Separatorul OCR deteriorat dintre două
dimensiuni de casetă este redat prin `×`. Alte caractere de control rămase în
traducere sunt respinse. Validatorul verifică și fracțiile tipografice (`½`, `⅓`
etc.) și distinge ordinalul din `Fig. 6.39 Second ...` de o durată în secunde.

La aplicare sunt produse `reports/catalog-translation.json` și dicționarul
`scripts/radiology_translations_catalog_ro.json`, reutilizat de traducătorul local.

## Corecturi locale de fraze

`radiology_translator.py` aplică traduceri de fraze complete. Corecturile pentru
textele mixte deja existente sunt în `radiology_translations_ro.json`, sub forma
`source` / `translation`. Pot fi adăugate fraze sau paragrafe; potrivirea ignoră
majusculele și diferențele de spațiere. Valorile numerice, negațiile și gradul de
certitudine trebuie păstrate. Un fragment trunchiat nu trebuie completat prin
presupuneri. Acest dicționar este o resursă lingvistică, nu o validare clinică.

Motorul caută mai întâi o corectură pentru întregul câmp, apoi pentru fiecare
linie și propoziție. Regulile terminologice se aplică numai dacă acoperă întreaga
unitate. Nu mai înlocuiește individual articolele, verbele și prepozițiile într-o
propoziție necunoscută. Româna rezultată nu trece din nou prin aceleași înlocuiri.
Textele necunoscute rămân disponibile pentru traducere ulterioară în raport.

Simulare pentru întregul catalog:

```powershell
python scripts/translate_and_adapt_protocols.py --dry-run --report reports/translation-audit.json
```

Aplicare, inclusiv regenerarea corpului Markdown pentru protocoalele modificate:

```powershell
python scripts/translate_and_adapt_protocols.py --report reports/translation-audit.json
python scripts/generate_forms_index.py
```

Se pot folosi și `--file`, `--category` sau `--source`. Simularea nu modifică
protocoalele, dar scrie raportul indicat. `unresolved_fields` include calea
câmpului, cuvintele detectate și textul pentru revizie; `needs_review_count`
numără protocoalele semnalate. Detectorul este euristic: poate avea rezultate
fals pozitive și fals negative. Un scor zero nu certifică o traducere completă.
Raportul exclude URL-urile și citările bibliografice din evaluare.

Opțiunea istorică `--ai` folosește mecanismul separat de îmbogățire `agy`; nu
reprezintă o traducere integrală garantată și nu este necesară pentru aceste
corecturi. Fluxul implicit este local și nu trimite textele către servicii externe.

Verificări de regresie:

```powershell
python -m pytest tests/test_radiology_translator.py tests/test_render_rx_protocol.py -q
```
