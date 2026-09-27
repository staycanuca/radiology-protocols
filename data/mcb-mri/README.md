# Import IRM MCB Radiology

Snapshot consultat la 2026-09-27 al celor cinci cataloage din
https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/MRI.html

- 77 PDF-uri de protocol: Body 22, Neuro 23, MSK 22, Breast 4, Vascular & IR 6.
- O fișă Body de orientare pentru alegerea protocolului.
- 78 documente distincte; legăturile comune între cataloage nu creează copii de protocol.
- Linkul `Neuro/20 TMJs.pdf` din catalogul MSK răspunde cu 404. Documentul
  corect, legat de catalogul Neuro, este `Neuro/21 TMJs.pdf` și a fost importat.
- Documentele COMBINED sunt agregate ale protocoalelor individuale, deci nu
  sunt importate a doua oară. Formularele și politicile de pe pagina principală
  sunt în afara acestei colecții de protocoale.

`manifest.json` păstrează URL-urile exacte, etichetele/cataloagele originale,
SHA-256 al PDF-urilor, textul pe pagini, tabelele extrase și erorile de acces.
`catalog.json` leagă documentele de paginile aplicației. Originalele distribuite
cu site-ul și imaginile tuturor paginilor sunt în `docs/assets/mcb-mri/`.

Titlurile, navigarea și etichetele parametrilor sunt în română. Textul clinic,
schemele de poziționare și denumirile PACS rămân în forma originală engleză.
Nu se deduc valori TR/TE, câmp magnetic, indicații, aprobări sau doze absente.
Extragerea automată a parametrilor nu constituie o revizuire medicală.
În special, rândurile secvențelor pot descrie variante alternative sau
condiționate: se citesc împreună cu instrucțiunile din pagina PDF originală.

Regenerare (din rădăcina proiectului):

```powershell
# Necesită requests, beautifulsoup4, PyMuPDF și PyYAML.
python scripts/import_mcb_mri.py
# Sau reextragere offline din PDF-urile deja descărcate:
python scripts/import_mcb_mri.py --extract-only
python scripts/generate_mcb_mri.py
python scripts/generate_omnisearch_index.py
python scripts/generate_forms_index.py
python -m pytest tests/test_mcb_mri_import.py tests/test_render_irm_protocol.py -q
python -m mkdocs build
```

Generatorul este limitat la paginile `*-mcb.md`, resursele aferente, catalogul
MCB, secțiunile MCB din indexuri și cele două intrări de navigare. Nu executa
vechiul generator general `generate_mcb_protocols.py` pentru acest import.
