# Proveniența protocoalelor

`provenance.py` este un hook MkDocs: construiește caseta din datele existente,
imediat după H1. Nu rescrie protocoalele și nu generează autori, surse, date sau
aprobări. Include paginile de protocol CT/IRM/RX/US/fluoro chiar dacă nu au `slug`.
Nu include indexurile, comparația sau paginile de politică generală.

## Audit reproductibil

```powershell
python scripts/provenance.py --audit reports/provenance-audit
python -m pytest tests/test_provenance.py -q
python -m mkdocs build
```

Auditul JSON include înregistrările și lipsurile pentru fiecare protocol;
CSV-ul poate fi folosit la triere. `missing_source_locator` înseamnă lipsa unei
pagini/secțiuni explicite, nu dovada că URL-ul nu conduce la un document specific.
Auditul nu accesează sursele externe și nu verifică validitatea medicală.

## Date deja acceptate

- `sources`: listă de obiecte (sau citări text). Sunt păstrate titlul, instituția,
  linkurile HTTP(S), ediția, versiunea/anul, secțiunea și paginile declarate.
- Ediția/paginile se pot extrage din formulări explicite precum `Ed. 12, Pagina 373`.
  `Ed. 9/10` rămâne ambiguă; nu se alege automat o ediție. URL-urile editorilor nu
  sunt folosite pentru a ghici ediții.
- `source_pages`: pagini în evidența preluării, afișate separat. Nu se atribuie
  automat fiecărei referințe când sunt mai multe surse.
- `checked_at`: dată tehnică în evidență, niciodată echivalată cu consultarea.
  `sha256` nu este afișat ca dovadă: unele importuri au calculat hash-ul URL-ului.
- `consulted_on`: data explicită a consultării. Datele viitoare/nevalide nu sunt
  afișate drept date efective de consultare sau revizuire.
- `last_updated`: actualizarea declarată a paginii, separată de revizuire.
- `author`: atribuire existentă, fără promovare la autor original/revizor.
- `workbench_review`: înregistrările anterioare sunt menționate, dar fără calificare,
  obiectul revizuirii și versiune nu devin înregistrări complete pentru pagina curentă.
- `status: draft` și `clinical_status: draft_not_for_clinical_use`: păstrează stadiul
  de ciornă. Nici o referință sau înregistrare nu elimină această restricție.

## Completări editoriale explicite

Următoarea structură este un **exemplu de schemă**, nu o verificare efectuată.
Nu copia placeholder-ele în protocoalele publicate. Completează numai fapte
documentate; omite înregistrările de verificare până la efectuarea lor.

```yaml
sources:
  - title: "Titlul exact al sursei"
    url: "https://example.org/document"
    edition: "Ediția folosită"
    version: "Versiunea sau anul sursei"
    section: "Capitolul / secțiunea"
    pages: [123, 124]
    relationship: "Sursă de preluare pentru poziționare; referință suplimentară pentru alte câmpuri"
    consulted_on: "AAAA-LL-ZZ"

provenance:
  version: "Identificatorul versiunii curente"
  editor: "Persoana responsabilă pentru prelucrare"
  processing:
    - "Traducere și reorganizare în câmpuri"
  adaptations:
    - "Descrierea modificărilor efective față de sursă"
  source_verification:
    reviewer: "Persoana care a confruntat preluarea cu originalul"
    reviewed_on: "AAAA-LL-ZZ"
    scope: "Câmpurile, valorile și unitățile confruntate"
    version: "Aceeași versiune ca provenance.version"
  medical_review:
    reviewer: "Persoana care a efectuat revizuirea medicală"
    qualification: "Calificarea relevantă declarată"
    profile_url: "https://example.org/profil-profesional"
    reviewed_on: "AAAA-LL-ZZ"
    scope: "Ce anume a fost evaluat și limitele revizuirii"
    version: "Aceeași versiune ca provenance.version"
```

La schimbări de conținut, modifică versiunea. Nu actualiza versiunea din înregistrarea
de revizuire decât după revizuirea efectivă a noului conținut. Pentru auditul istoric,
păstrează versiunile și documentele de revizuire în evidența editorială / Git.
Aceste câmpuri nu constituie un mecanism de semnătură sau certificare independentă.

Editorul de protocoale păstrează sursele și câmpurile editoriale care nu sunt expuse
în formular, pentru toate cele cinci modalități. La schimbarea câmpurilor de conținut,
înregistrările explicite de verificare existente primesc `provenance.review_required: true`.
Caseta afișează „De reverificat după modificare”. Elimină acest marcaj numai după
revizuirea noii versiuni și actualizarea înregistrărilor corespunzătoare.

URL-urile locale, schemele executabile și căile fișierelor de lucru nu sunt expuse
ca linkuri publice. HTML-ul din metadate este escapăt. Toate stările pot fi citite
fără JavaScript; detaliile folosesc elementul nativ `details`.
