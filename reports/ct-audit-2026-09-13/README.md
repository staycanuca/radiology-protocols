# Audit de acoperire a bibliotecii CT

Data: 13 septembrie 2026. Bibliotecă analizată: `docs/ct/`.

## Rezultat și metodă

Au fost găsite **87 de fișiere de protocol și au fost citite toate cele 87**, excluzând paginile `index.md` și `compare.md`. Au fost inspectate titlurile, slug-urile, indicațiile, contrastul, seriile, notele și, pentru verificarea suprapunerilor, corpul documentelor relevante.

Distribuție: abdomen 10, cardiac 12, torace 9, MSK 14, neuro 19, vascular 16, traumă 7. Nu există protocoale CT pediatrice dedicate în inventarul analizat. Legăturile generice către IRIS/radiologie-pediatrica.ro nu constituie protocoale pediatrice.

Comparația a folosit catalogul [UT Southwestern CT](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html), resursele [AAPM CT](https://www.aapm.org/pubs/ctprotocols/) și referința [ACR pentru colonografie CT](https://gravitas.acr.org/PPTS/GetDocumentView?docId=33). Au fost colectate 101 de intrări UT Southwestern și 38 de resurse AAPM; resursele AAPM includ și materiale auxiliare, nu numai protocoale. Aceste numere **nu se scad din numărul local**: instituțiile împart diferit investigațiile și variantele.

Constatările de mai jos sunt inferențe despre **acoperirea documentației locale**, nu o validare a parametrilor medicali și nici o listă obligatorie de servicii. Prioritatea finală depinde de activitatea departamentului, echipament și populația deservită. Existența unui document american nu justifică automat folosirea sau republicarea lui.

## 1. Completări de bază: lipsesc ca protocoale independente, cu acoperire parțială existentă

| Propunere | Dovada locală și delimitarea lipsului | Referință externă |
| --- | --- | --- |
| CT torace cu contrast, de rutină, fără componentă angio | Există [CT torace-abdomen-pelvis cu contrast](../../docs/ct/abdomen/ct-chest-abdomen-pelvis-with-contrast.md), CTPA și protocoale de traumă. Nu există fișier dedicat toracelui de rutină cu contrast; examinarea combinată CAP nu este un protocol toracic separat. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/Routine%20Chest%20W%20Contrast.pdf) |
| CT cerebral diagnostic cu contrast / nativ și cu contrast, după indicație | Există [CT cerebral nativ](../../docs/ct/neuro/non-contrast-ct-head.md), CT stereotaxic cu contrast opțional și o fază cerebrală postcontrast în [SCAD/FMD](../../docs/ct/vascular/cta-scadfmd-protocol.md). Nu există un protocol diagnostic cerebral cu contrast de sine stătător. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/Head%20Without%20and%20With.pdf) |
| CT abdomen-pelvis nativ, general | Există [KUB nativ low-dose](../../docs/ct/abdomen/ct-kub-non-contrast.md), cu acoperire declarată de la polul renal superior la simfiză și optimizare pentru calculi. Nu documentează o examinare nativă generală abdomen-pelvis. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/AP%20No%20IV.pdf) |

Aceste trei intrări pot fi create prin adaptarea controlată a protocoalelor locale apropiate. Nu recomand copierea integrală a examinărilor CAP sau SCAD/FMD pentru a obține un examen restrâns.

## 2. Lipsuri dedicate în familii de investigații

| Propunere | Ce am găsit în aplicație | Referință pentru documentare |
| --- | --- | --- |
| Colonografie CT / colonoscopie virtuală | Niciun protocol dedicat. Entero-CT și protocolul pentru hemoragie digestivă nu acoperă această examinare. | [ACR, revizia 2024](https://gravitas.acr.org/PPTS/GetDocumentView?docId=33) |
| CT pentru evaluarea donatorului renal | Există masă renală, uro-CT și angio-CT abdomen-pelvis; nu există indicație/protocol dedicat donatorului. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/CTA%20Abd%20Renal%20Donor.pdf) |
| CTV membru inferior | Există [CTV abdomen-pelvis](../../docs/ct/vascular/ctv-abdomen-pelvis.md) și CTA runoff arterial. Niciun protocol dedicat venografiei membrului inferior. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/CTV%20Lower%20Extremity.pdf) |
| CTV membru superior | Există CTA membru superior și CTV torace-abdomen-pelvis; lipsește protocolul venos dedicat membrului superior. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/CTV%20Upper%20Extremity.pdf) |
| Artro-CT cot | CT cot documentează achiziție obișnuită, cu contrast opțional intravenos pentru infecție; nu artrografie. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/CT%20Elbow%20Arthrogram.pdf) |
| Artro-CT genunchi | CT genunchi nu documentează o examinare artrografică. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/Knee%20CT%20Arthrogram.pdf) |
| Artro-CT pumn | CT pumn nu documentează o examinare artrografică. Singurul artro-CT dedicat existent este cel de umăr. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/Wrist%20CT%20Arthrogram.pdf) |
| CT pectus / deformare de perete toracic | Niciun protocol dedicat. Mențiunile locale „Haller” se referă la celule sinusale, nu la evaluarea pectusului. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/Pectus%20CT.pdf) |
| CTA pentru sindrom Bow Hunter | Există CTA cervical standard; nu există protocol dedicat acestei examinări dinamice. Relevant numai dacă se oferă acest serviciu specializat. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/CTA%20Bow%20Hunters%20Syndrome.pdf) |
| CT pentru litiază salivară | CT masiv facial este orientat spre os/traumă, iar CT părți moi gât folosește contrast. Nu am identificat un protocol pentru calculi salivari. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/Max_Face%20Stone.pdf) |
| CT gleznă pentru artroplastie / planificare specifică | CT gleznă acoperă fracturi și osteosinteză. Nu există protocol dedicat artroplastiei; necesitatea depinde de programul ortopedic și sistemul de planificare. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/CT%20Ankle%20Arthroplasty.pdf) |

## 3. Variante ORL absente din documentația dedicată

| Variantă | Protocol apropiat și lipsă observată | Referință |
| --- | --- | --- |
| CT sinusuri / masiv facial cu contrast | [CT sinusuri](../../docs/ct/neuro/ct-sinus.md) și [CT masiv facial](../../docs/ct/neuro/ct-facial-bones.md) sunt native. CT orbite și CT gât au suprapunere anatomică, dar nu documentează explicit această variantă. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/Sinus%20With.pdf) |
| CT stânci temporale cu contrast | [Protocolul actual](../../docs/ct/neuro/ct-temporal-bones.md) este nativ. Nu există variantă dedicată cu contrast. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/Temporal%20Bone%20With.pdf) |
| CT părți moi gât nativ | [Protocolul actual](../../docs/ct/neuro/ct-soft-tissue-neck.md) este cu contrast. Nu există variantă nativă explicită. | [UTSW](https://www.utsouthwestern.edu/departments/radiology/protocols/assets/Neck%20Without.pdf) |

Aceste variante trebuie activate numai pentru indicațiile stabilite local; catalogul extern nu înseamnă că toate examinările ORL trebuie efectuate atât nativ, cât și cu contrast.

## 4. Familia pediatrică lipsește

Nu există protocoale CT pediatrice dedicate pentru:

- **Craniu** — [referință AAPM](https://www.aapm.org/pubs/CTProtocols/documents/PediatricRoutineHeadCT.pdf).
- **Torace** — [referință AAPM](https://www.aapm.org/pubs/CTProtocols/documents/PediatricRoutineChestCT.pdf).
- **Abdomen-pelvis** — [referință AAPM](https://www.aapm.org/pubs/CTProtocols/documents/PediatricRoutineAbdomenPelvisCT.pdf).

Dacă departamentul examinează copii, aceasta este o prioritate de documentare și revizuire. Sursele AAPM sunt puncte de pornire, unele publicate în 2015–2017; nu reprezintă automat parametrii potriviți aparatului și practicii locale din 2026.

## 5. Ce NU trebuie raportat ca lipsă totală

| Investigație / variantă | Acoperire găsită |
| --- | --- |
| Perfuzie cerebrală CT | Inclusă ca serie opțională în [protocolul AVC](../../docs/ct/neuro/brain-stroke-protocol.md), cu referire la hărți de perfuzie. Poate necesita detalierea unui subprotocol, dar nu este absentă. |
| Evaluare endoleak după endoproteză aortică | Există serii „Tardiv Stent” și mențiuni explicite în [CTA abdomen-pelvis](../../docs/ct/vascular/cta-abdomen-pelvis.md) și [CTA CAP sincronizat](../../docs/ct/cardiac/gated-cta-cap.md). Un protocol EVAR/TEVAR separat ar clarifica fluxul, dar acoperirea nu este zero. |
| FAI / conflict femuro-acetabular | Explicit în indicațiile și măsurătorile [CT șold](../../docs/ct/msk/ct-hip.md), cu achiziție bilaterală și reconstrucții 3D. |
| CT MSK cu contrast intravenos | Majoritatea fișierelor regionale prevăd contrast opțional; există și [protocol MSK general](../../docs/ct/msk/msk-protocol-general.md). Este de verificat detalierea fazelor, nu de declarat fiecare regiune absentă. |
| CT orbite cu contrast | Prevăzut în [CT orbite](../../docs/ct/neuro/ct-orbits.md). |
| Mielo-CT cervical/toracic/lombar | Există [mielo-CT general](../../docs/ct/neuro/ct-myelogram.md). Separarea pe regiuni este o decizie de organizare, după verificarea acoperirii tehnice. |
| CT pentru artroplastie de genunchi | Menționat în [CT genunchi](../../docs/ct/msk/ct-knee.md); un flux specific unui sistem de planificare poate necesita completări. |
| Litiază urinară, urografie, masă renală, suprarenală, ficat și pancreas multifazic | Există protocoale dedicate. |
| Screening / monitorizare pulmonară low-dose | Există [CT torace low-dose](../../docs/ct/chest/non-contrast-ct-chest-low-dose.md) și protocol ultra-low-dose pentru nodul. Nu am auditat completitudinea programului de screening sau raportarea. |

## 6. Ordinea propusă pentru completare

1. CT torace cu contrast, CT cerebral diagnostic cu contrast și CT abdomen-pelvis nativ general: acoperire de bază ca protocoale independente.
2. Cele trei protocoale pediatrice, **dacă sunt examinați copii**; în acest caz pot preceda celelalte completări.
3. Artro-CT cot/genunchi/pumn, CTV membre, colonografie și donator renal, în funcție de serviciile efectiv oferite.
4. Variante ORL și protocoale specializate pectus, Bow Hunter și artroplastie de gleznă, după confirmarea necesității locale.

## 7. Observație separată: imagini

**0 din 87** protocoale CT au imagini declarate în câmpul `images` din front matter. Aceasta măsoară galeria structurată folosită de unealtă; nu afirmă că toate paginile sunt lipsite de diagrame, SVG-uri sau alte ilustrații în corpul documentului.

## Fișiere de evidență

- [Inventarul complet local](inventory.json): metadatele și corpul celor 87 de protocoale la momentul auditului.
- [Cataloagele americane consultate](us-catalogs.json): titluri, URL-uri și data accesării catalogului. Data accesării nu este data ediției protocolului.

Auditul nu a modificat protocoalele aplicației și nu a importat documente noi. Alegerea și validarea clinică a completărilor rămân în fluxul de revizuire stabilit.
