# Analiza bibliotecii RX și propuneri de extindere

Data: 15 septembrie 2026. Domeniu: aplicația principală, fișierele `docs/rx/` și indexul `docs/javascripts/protocol-forms-index.json`. Ciornele Workbench nu sunt numărate ca protocoale publicate.

## Concluzie

Biblioteca conține **22 de protocoale RX**, toate prezente și în indexul de formulare. Acoperă examinări uzuale, dar nu are protocoale dedicate pentru diafizele oaselor lungi, coloană totală, măsurarea membrelor inferioare sau unele examinări pediatrice specifice.

Propun un prim lot de **10 protocoale noi**, care ar duce biblioteca la 32 de documente, și completarea unor protocoale existente prin variante. Prioritățile de mai jos sunt o apreciere editorială bazată pe lipsurile bibliotecii și diferențele de execuție. Nu reprezintă grade ACR/IRIS și nu sunt calculate din volumele locale de examinări, care nu au fost analizate.

Înaintea reutilizării template-urilor trebuie corectate câteva probleme de conținut și trasabilitate. Acest raport este o propunere; nu modifică protocoalele clinice și nu introduce valori de expunere.

## 1. Inventarul existent

| Categorie | Număr | Protocoale existente |
| --- | ---: | --- |
| Torace | 4 | Torace PA; profil stâng; torace la pat AP; grilaj costal |
| Abdomen și bazin | 2 | Abdomen pe gol; bazin AP |
| Coloană | 3 | Cervicală; toracală; lombară și L5–S1 |
| Membru superior | 4 | Umăr AP/Y; cot; mână/degete; pumn/scafoid |
| Membru inferior | 4 | Șold AP/Lauenstein; genunchi inclusiv axială de rotulă; gleznă/morteză; picior |
| Pediatrie | 3 | Torace pediatric; bazin/șolduri sugar pentru DDH; vârstă osoasă |
| Craniu și masiv facial | 2 | Oase nazale; sinusuri/Waters |
| **Total** | **22** | |

Observații structurale:

- Toate cele 22 de documente au surse declarate. Totuși, 18 folosesc exact același set de trei referințe generale; unul adaugă un atlas local, iar cele trei pediatrice folosesc același set de două referințe. Existența bibliografiei nu demonstrează proveniența fiecărui parametru.
- **20 din 22 nu au imagini în metadate.** Celelalte două au probleme de documentare descrise mai jos.
- Există poziționare, centrare, SID, parametri tehnici și criterii de calitate. Incidențele sunt descrise predominant într-un singur text `position`, nu într-o listă structurată pe incidențe.
- Metadatele IRIS declară 16 protocoale „Grad A” și 6 „Grad B”, pentru documente care combină mai multe indicații. Lipsesc trimiterile precise care să permită verificarea fiecărui scenariu clinic.
- Un protocol regional poate acoperi mai multe incidențe. Numărul de fișiere nu trebuie confundat cu numărul de examinări sau proiecții disponibile.

## 2. Primul lot recomandat: 10 protocoale noi

### A. Completarea traumatologiei segmentare — 5 protocoale

| Protocol propus | Categorie / slug | Diferența față de biblioteca actuală |
| --- | --- | --- |
| RX humerus — AP și profil | `membru-superior/rx-humerus-ap-profil` | Umărul și cotul nu documentează achiziția pentru întregul humerus. Include adaptări de poziționare pentru traumatism. |
| RX antebraț — radius și ulna | `membru-superior/rx-antebrat-ap-profil` | Acoperă diafizele și evaluarea relației cu articulațiile vecine; legături către protocoalele dedicate de cot/pumn când sunt necesare. |
| RX femur — AP și profil | `membru-inferior/rx-femur-ap-profil` | Completează intervalul dintre șold și genunchi; definește acoperirea și achiziția adaptată pacientului care nu poate mobiliza membrul. |
| RX gambă — tibie și fibulă | `membru-inferior/rx-gamba-ap-profil` | Examinare distinctă de genunchi și gleznă; variantă pediatrică pentru suspiciune de fractură la copilul mic. |
| RX claviculă | `membru-superior/rx-clavicula` | Examinarea umărului nu oferă un protocol dedicat claviculei; definește incidențele necesare și adaptarea la durere. |

Aceste lipsuri sunt susținute de organizarea pe segmente și de recomandările de investigație din [RCH — Paediatric Fractures Guidelines](https://www.rch.org.au/clinicalguide/fractures/). Pentru antebraț, [ghidul RCH dedicat radiusului și ulnei](https://www.rch.org.au/clinicalguide/guideline_index/fractures/Radialulna_shaft_diaphysis_fractures_Emergency_Department/) oferă o bază specifică, mai potrivită decât o referință generală de radiografie. Recomandările pediatrice trebuie diferențiate de adaptările pentru adulți.

### B. Examinări cu obiectiv și execuție distincte — 5 protocoale

| Protocol propus | Categorie / slug | Ce trebuie să aducă în plus |
| --- | --- | --- |
| RX coloană totală în ortostatism — scolioză/deformări | `coloana/rx-coloana-totala-scolioza` | Acoperire completă, poziționare reproductibilă, evaluarea curburilor și comparație în timp. RX toracală segmentară nu o înlocuiește. [RCH — Scoliosis](https://www.rch.org.au/ortho/for_health_professionals/Scoliosis/) |
| RX telemetrie membre inferioare — axe și lungimi | `membru-inferior/rx-telemetrie-membre-inferioare` | Poziționare standardizată și calibrare pentru măsurători; separă analiza axelor în sprijin de tehnicile destinate exclusiv lungimii. Necesită verificarea capabilităților aparatului. [RCH — Limb Reconstruction](https://www.rch.org.au/limbrecon/the_lr_process/Clinic/) |
| RX bilanț scheletic pediatric — suspiciune de abuz fizic | `pediatrie/rx-bilant-scheletic-suspiciune-abuz` | Examinare multiregională standardizată, listă de verificare, criterii de includere, documentare și componentă de reevaluare conform ghidului aplicabil. Nu se reduce la o singură imagine a întregului corp. [ACR — Suspected Physical Abuse–Child, update 2025](https://www.sciencedirect.com/science/article/abs/pii/S1546144026000785) |
| RX pentru corp străin ingerat la copil | `pediatrie/rx-corp-strain-ingerat` | Definirea acoperirii în funcție de suspiciune/localizare, diferențierea obiectelor și comunicarea rapidă a constatărilor relevante. Mențiunea din RX abdomen nu descrie un flux complet. Aspirația necesită o ramură separată. [ACR — Ingested or Aspirated Foreign Body–Child](https://www.sciencedirect.com/science/article/pii/S1546144025007288) |
| RX abdomen neonatal — suspiciune de enterocolită necrozantă/perforație | `pediatrie/rx-abdomen-neonatal` | Achiziție la incubator, acoperire și comparație temporală; precizarea rolului complementar al ecografiei. Frecvența reevaluărilor se stabilește clinic, nu printr-un interval universal în template. [ACR — Abdominal Pain–Child, varianta pentru NEC](https://acsearch.acr.org/list/TopicNarrativePdf?topicId=351) |

Pentru un serviciu predominant pediatric, bilanțul scheletic și corpul străin pot preceda telemetria sau extinderile pentru adulți. Abdomenul neonatal are prioritate dacă există activitate neonatală efectivă. Aceasta este o adaptare propusă, nu o presupunere privind volumul local.

## 3. Etapa următoare

1. **RX șold la copil/adolescent — șchiopătat, Perthes, suspiciune de epifizioliză.** Protocolul actual pentru sugar este orientat spre displazia de dezvoltare a șoldului; nu acoperă aceste situații. Trebuie diferențiate prezentările stabile de cele acute/instabile, fără aplicarea automată a poziției „frog-leg”. Bază de documentare: [RCH — Slipped upper femoral epiphysis](https://www.rch.org.au/ortho/for_health_professionals/Slipped_upper_femoral_epiphysis_%E2%80%93_SUFE/), cu verificarea ghidului de urgență înaintea redactării.
2. **RX calcaneu.** Examinare dedicată, diferită de protocolul actual de picior. Bază: [RCH — catalogul fracturilor](https://www.rch.org.au/clinicalguide/fractures/), secțiunea calcaneu.
3. **RX degete de picior/hallux.** Achiziții centrate și criterii proprii, când examinarea întregului picior nu răspunde întrebării clinice. Bază: [RCH — catalogul fracturilor](https://www.rch.org.au/clinicalguide/fractures/), secțiunea degete.
4. **RX scapulă**, dacă volumul local și solicitările traumatologice justifică un protocol separat.
5. **Bilanț radiografic pentru suspiciune de displazie scheletală**, ca protocol separat de bilanțul pentru abuz. Se documentează împreună cu radiologul pediatru și echipa de genetică.
6. **RX țintită în suspiciunea de rahitism/boală metabolică osoasă**, dacă există această activitate; nu se confundă cu examinarea de vârstă osoasă. Setul de achiziții necesită sursă specifică înainte de redactare.

Ultimele trei sunt candidați pentru o etapă ulterioară; acest audit nu a stabilit seturile lor de incidențe sau parametrii tehnici.

## 4. Variante de completat în protocoalele existente

| Protocol existent | Completare propusă |
| --- | --- |
| Pumn/scafoid | Delimitarea seriei standard de pumn de seria dedicată scafoidului; scafoidul există deja, deci nu este o lipsă anatomică. |
| Genunchi | Variante clar delimitate pentru traumatism, examinare în sprijin și evaluare femuro-patelară. Axiala de rotulă există deja. |
| Șold AP/Lauenstein | Variantă tehnică completă pentru traumatism, cu profil cu rază orizontală; în prezent apare doar ca observație. |
| Mână/degete | Protocolul menționează degetele, dar descrie în principal mâna. Adăugarea unor variante dedicate degetului și policelui este o completare a acoperirii existente. |
| Picior | Revizuirea setului de incidențe în traumă și completarea variantei în sprijin. Evitarea unui al doilea document generic „RX picior”. |
| Cot | Variantă pediatrică și poziționare pentru mobilitate limitată; criterii tehnice distincte de observațiile de interpretare CRITOE. |
| Torace pediatric / la pat | Variantă neonatală și componentă pentru dispozitive, dacă serviciul efectuează aceste examinări. |
| Abdomen pe gol | Separarea achizițiilor pentru pacient mobil/nedeplasabil și pentru obiective diferite; decubitul lateral cu rază orizontală este deja menționat. |

Această structură evită multiplicarea documentelor cu același conținut și permite păstrarea unei singure surse de adevăr pentru parametrii comuni.

## 5. Conținut existent care trebuie revizuit înainte de extindere

### 5.1. Eroare explicită de conținut

În [RX coloană toracală](../../docs/rx/coloana/rx-coloana-toracala.md), `position` este **„Terminology”**, iar aceeași valoare apare în corpul documentului. Este un text care nu descrie poziționarea pacientului. Necesită corectare dintr-o sursă verificată. Fișierul singur nu dovedește ce operație a produs eroarea.

### 5.2. Radioprotecție și justificarea investigației

- Mai multe documente recomandă ecranare gonadală/tiroidiană ca pas de rutină; și [rendererul RX](../../scripts/render_rx_protocol.py) introduce un astfel de pas comun. Politica trebuie revizuită împreună cu fizicianul medical. [Poziția AAPM PS 8-A](https://www.aapm.org/org/policies/details.asp?id=2552) recomandă renunțarea la ecranarea gonadală/fetală de rutină a pacientului; aceasta nu trebuie confundată cu protecția personalului sau însoțitorilor.
- Protocolul [sinusuri/Waters](../../docs/rx/craniu-saf/rx-sinusuri-saf-waters.md) include sinuzita acută între indicații, fără delimitarea cazurilor necomplicate. Ghidurile actuale nu susțin imagistica de rutină în rinosinuzita acută necomplicată. Revizuirea indicațiilor are prioritate față de adăugarea mai multor proiecții cranio-faciale. [AAO-HNSF — Adult Sinusitis Update, 2025](https://aao-hnsfjournals.onlinelibrary.wiley.com/doi/10.1002/ohn.1344)
- Indicațiile largi pentru lombalgie/cervicalgie și etichetele IRIS trebuie verificate pe scenariu clinic, cu trimitere precisă la sursă. Auditul de față nu validează gradele atribuite și nici valorile de doză declarate.

### 5.3. Imagini și proveniență

- [Torace PA](../../docs/rx/torace/rx-torace-pa.md): imaginea are legendă și descriere goale și nu are metadate de autor/licență/pagină sursă.
- [Coloană toracală](../../docs/rx/coloana/rx-coloana-toracala.md): sunt declarate autor „Adobe”, licență „CC” și un domeniu CDN ca sursă. Aceste date nu identifică suficient licența și pagina imaginii. Este necesară clarificarea provenienței înainte de reutilizare.
- Imaginile nu au fost evaluate vizual în acest audit; constatările de mai sus privesc metadatele.

### 5.4. Template și surse

Pentru fiecare protocol nou propun:

1. Indicații și limite precise, cu ramuri adult/copil sau traumă/electiv când execuția diferă.
2. Incidențe obligatorii și condiționale, fiecare cu poziționare, centrare și criterii de acceptare proprii.
3. Parametri adaptați aparatului, detectorului și dimensiunii pacientului; valorile existente nu se copiază automat la o nouă regiune sau populație.
4. Proveniență pe câmp: document, ediție/pagină/secțiune și data verificării, distinctă de data actualizării protocolului.
5. Cel puțin o imagine reprezentativă documentată și, când este utilă, o schemă de poziționare.
6. Verificarea concordanței YAML–Markdown și a coerenței dintre slug, titlu și incidențele efective.

Exemple de nomenclatură de uniformizat: slugul umărului conține „axial”, dar titlul și textul descriu Y scapular; bazinul AP este clasificat la abdomen. Sunt probleme de organizare și căutare, nu argumente pentru duplicate.

## 6. Ordinea de lucru propusă

1. Corectarea poziționării toracale și revizuirea regulilor comune ale template-ului.
2. Redactarea în Workbench a celor cinci protocoale segmentare lipsă.
3. Redactarea celor cinci examinări specializate, în ordinea adaptată activității locale.
4. Completarea variantelor din documentele existente și a imaginilor.
5. Revizuirea și importul fiecărui protocol, cu proveniență și verificarea indexării.

## Limitele verificării surselor

Inventarul local a fost verificat direct în cele 22 de fișiere și în index. Documentarea externă a folosit ghiduri instituționale RCH, publicații ACR, AAPM și AAO-HNSF. Unele endpointuri PDF ACR au returnat 403, iar un URL vechi UT Southwestern a redirecționat către pagina departamentului; nu au fost tratate ca documente integrale verificate. Pentru unele teme ACR au fost disponibile rezumatele indexate/publicațiile editorului. Ediția și textul integral trebuie reconfirmate la redactarea protocolului propriu-zis.
