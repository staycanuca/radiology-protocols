# Biblioteca MCB: celelalte modalități

Consultare: 2026-09-27. Portal: https://ref.mcbradiology.com/

Au fost importate 255 de PDF-uri distincte, însumând 2.763 de pagini:

| Modalitate | Documente |
|---|---:|
| CT | 103 protocoale + 9 manuale de aparat |
| Ecografie | 38 protocoale + 37 fișe de lucru |
| RX | 17 colecții de protocoale (9 adult, 8 pediatric) |
| Mamografie | 4 politici procedurale |
| DEXA | 1 ghid |
| Fluoroscopie | 3 documente de protocol/pregătire |
| Medicină nucleară | 36 protocoale |
| Intervențional | 7 ghiduri/documente procedurale |

25 de pagini existente de medicină nucleară au primit documentul original;
celelalte 230 sunt pagini noi. Sumarul existent nu este rescris, iar importul
original este delimitat și afișat înaintea lui. Identificarea se face prin URL-ul
sursei, nu prin similaritatea titlurilor. Protocoalele IRM importate anterior
sunt păstrate și legate din biblioteca centrală `docs/mcb/index.md`.

Colecțiile RX sunt importate integral, fiecare conținând mai multe examinări.
Fișele, politicile și manualele sunt etichetate distinct de protocoale.
PDF-urile COMBINED pentru CT nu se multiplică peste protocoalele individuale.
Formularele administrative, consimțămintele, facturarea, proiectul intern de
ordine IR și articolele bibliografice nu sunt importate ca protocoale.

Singura sursă selectată indisponibilă este
`https://ref.mcbradiology.com/DEXA/Reference%20Articles/FRAX%20Guidelines.pdf`
(HTTP 404). Nu s-a substituit cu o altă ediție sau alt document.

## Conținut și verificare

- `inventory.json`: paginile și documentele descoperite.
- `selection.json`: selecția explicită, clasificarea și titlurile românești.
- `manifest.json`: URL-uri, hash SHA-256, textul pe pagini și erorile de acces.
- `catalog.json`: corespondența sursă–pagină locală și numărul de pagini.
- `pdfs/`: snapshot original; copiile publicate sunt în `docs/assets/mcb-modalities/`.

Pentru PDF-uri de maximum 30 de pagini sunt afișate toate paginile ca imagini.
Cele șase manuale mai lungi au o previzualizare de trei pagini; PDF-urile de
descărcat sunt integrale. Textul extras din toate paginile este inclus în
documentație pentru căutarea nativă. Nu se inventează text pentru pagini scanate.
Titlurile/navigarea sunt în română, iar instrucțiunile clinice originale rămân în
engleză. Importul tehnic nu reprezintă revizuire medicală sau traducere clinică.

## Regenerare

```powershell
python scripts/import_mcb_modalities.py
python scripts/select_mcb_modalities.py
python scripts/import_mcb_modalities.py --download
python scripts/generate_mcb_modalities.py
python scripts/generate_omnisearch_index.py
python scripts/generate_forms_index.py
python scripts/generate_comparison_index.py
python scripts/generate_sitemap.py
python -m pytest tests/test_mcb_modalities.py tests/test_rx_catalog.py tests/test_search_catalog.py -q
python -m mkdocs build
```

Descărcările existente sunt reutilizate; pentru un nou snapshot se arhivează
directorul de date înaintea descărcării. Generatorul funcționează offline,
reutilizează imaginile neschimbate și păstrează secțiunile originale ale aplicației.
