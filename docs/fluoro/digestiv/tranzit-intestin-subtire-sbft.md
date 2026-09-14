---
acquisition_steps:
- description: 'Radiografie abdominală în decubit ventral: se evaluează jejunul proximal,
    pliurile kerckringiene feathery (valvulele connivente) și viteza inițială de golire
    gastrică.'
  phase: Cliseu de Debut (15 minute)
- description: Radiografii seriate la intervale de 30 minute în decubit ventral; se
    urmărește progresia coloanei opace prin jejunul distal și ansele ileale, monitorizând
    calibrul luminal și motilitatea.
  phase: Seriere Temporizată (30 - 60 - 90 minute)
- description: 'În momentul în care bariul atinge fosa iliacă dreaptă: se trece în
    regim de fluoroscopie scurtă; se aplică compresiune dozată cu paleta/conul pentru
    a derula ultima ansă ileală și valva ileo-cecală fără suprapunerea anselor pelvine.'
  phase: Examen Țintit Fluoroscopic pe Ileonul Terminal
- description: Opacifierea cecului și a colonului ascendent confirmă tranzitul complet
    prin întregul intestin subțire; se face un cliseu panoramic final.
  phase: Confirmarea Pasajului în Cec (Final de Examen)
author: Departamentul de Radiologie și Imagistică Medicală
category: digestiv
clinical_indications:
- Boala Crohn cu afectare a intestinului subțire (aprecierea localizării, a numărului
  și lungimii stenozelor, a fistulelor entero-enterice sau entero-cutanate și a leziunilor
  de tip 'skip')
- Sindrom cronic de malabsorbție (boală celiacă refractară, sindrom de ansă oarbă,
  amiloidoză)
- Dureri abdominale recidivante de etiologie neelucidată endoscopic
- Sângerare digestivă ocultă fără cauză evidențiată la endoscopia superioară și colonoscopie
- Suspiciune de neoplazie sau limfom al intestinului subțire, diverticul Meckel complicat
- Episoade repetate de subocluzie mecanică prin bride peritoneale postoperatorii
contraindications:
- Ocluzie intestinală completă mecanică instalată cu distensie masivă de anse (contraindicație
  pentru administrare orală de contrast dens)
- Suspiciune de perforație enterală cu peritonită acută
- Megacolon toxic sau colită fulminantă asociată
contrast:
  agent: 'Sulfat de Bariu suspensie enterală de densitate medie (40-50% w/v) pentru
    tranzit per os (SBFT); La Enterocliză: administrare prin sondă nazo-jejunală a
    250 ml suspensie de bariu urmată de infuzie de 1000-1500 ml soluție de metilceluloză
    0.5% pentru realizarea dublului contrast enteral'
  instructions: Pacientul bea suspensia treptat în ritm susținut; se menține în decubit
    lateral drept pentru stimularea evacuării rapide gastrice a bariului în duoden
  route: Orală (SBFT) SAU pe sondă nazo-jejunală avansată fluoroscopic dincolo de
    ligamentul Treitz (Enterocliză)
  volume: 300 - 600 ml suspensie baritată
fluoro_params:
  filtration: ≥ 3.0 mm Al
  grid: Cu grilă antidifuzoare
  kv: 100 - 120 kV (contrast baritat enteral)
  lih: Activ
  ma_range: 1.0 - 3.0 mA în scopie
  mode: Radiografii seriate discrete la intervale regulate + Fluoroscopie Pulsată
    scurtă DOAR la compresia ileală
  target_fluoro_time: < 2.0 minute cumulat pe toată durata tranzitului
iris_reference:
  chapter: Intestin Subțire
  radiation_dose: Clasa 2 (Medie 1 - 5 mSv)
  recommendation_grade: Grad B
last_updated: '2026-09-13'
modality: fluoro
notes: Utilizarea unui agent prokinetic (ex. metoclopramid 10 mg oral cu 15 min înainte)
  poate fi indicată la pacienții cu tranzit lent pentru a scurta timpul de așteptare
  de la 3-4 ore la sub 60-90 de minute, reducând numărul de expuneri necesare.
patient_prep: Regim alimentar fără reziduuri cu 2 zile anterior; à jeun cu 8-12 ore
  înainte de procedură; eventual administrarea unui laxativ osmotic ușor în ajun conform
  protocoalelor secției pentru un colon neîncărcat fecaloid.
positioning_equipment:
  equipment_setup: Masă fluoroscopică digitală cu paletă sau con mecanic de compresiune
    dozată; distanță focar-film 100-115 cm
  patient_position: 'Decubit ventral (poziție esențială: compresiunea naturală exercitată
    de greutatea pacientului pe planul mesei etalează ansele jejuno-ileale prevenind
    aglomerarea lor în pelvis); decubit dorsal la compresia manuală țintită'
  sid: 100 - 115 cm
quality_criteria:
- Demonstrarea completă a tuturor segmentelor intestinului subțire până la nivelul
  cecului
- Etalarea fără suprapunere a ileonului terminal (sediul predilect al bolii Crohn)
- Distincție clară între desenul feathery jejunal și mucoasa mai netedă ileală
- Identificarea oricărei rigidități parietale, fistule, stenoze sau imagini lacunare
radiation_safety:
- 'REGULĂ DE AUR: Fluoroscopia NU se lasă deschisă în așteptarea pasajului! Tranzitul
  se monitorizează prin radiografii punctuale (spot films) la intervale stabilite'
- Timpul total cumulat de fluoroscopie trebuie să fie strict < 1.5 - 2 minute
- Colimare strictă la compresia ileonului terminal pe fosa iliacă dreaptă
- DAP < 12 Gy·cm²
- Protecție gonadală poziționată atunci când nu maschează ansele din micul bazin
slug: tranzit-intestin-subtire-sbft
title: Tranzit Intestin Subțire (Enterocliză / Small Bowel Follow-Through - SBFT)
sources:
- title: ACR-SAR-SPR Practice Parameter for the Performance of Gastrointestinal Fluoroscopy
    in Adults
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Fluoro.pdf
  institution: ACR / SAR / SPR
  source_region: US
  kind: Standard de practică fluoroscopie digestivă
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 45621b1990b6eabf74f9996a8a9c707b6d18590d018367baf4fe51409a0450b0
- title: UT Southwestern Radiology — Diagnostic Fluoroscopy Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/diagnostic.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional fluoroscopie
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 4d9de4a012f12a5d0ac28d46131bf9ab7e4668e6fae1937eaf76d68167f9290d
position: 'Decubit ventral (poziție esențială: compresiunea naturală exercitată de
  greutatea pacientului pe planul mesei etalează ansele jejuno-ileale prevenind aglomerarea
  lor în pelvis); decubit dorsal la compresia manuală țintită'
---

# Tranzit Intestin Subțire (Enterocliză / Small Bowel Follow-Through - SBFT)

<div class="fluoro-meta-bar">
  <span class="fluoro-modality-badge">✨ Fluoroscopie & C-Arm</span>
  <span><strong>Actualizat:</strong> 2026-09-13</span>
  <span><strong>Autor:</strong> Departamentul de Radiologie și Imagistică Medicală</span>
</div>

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic, Indicații & Contraindicații__

    ---

    === "Indicații Clinice"

        - Boala Crohn cu afectare a intestinului subțire (aprecierea localizării, a numărului și lungimii stenozelor, a fistulelor entero-enterice sau entero-cutanate și a leziunilor de tip 'skip')
        - Sindrom cronic de malabsorbție (boală celiacă refractară, sindrom de ansă oarbă, amiloidoză)
        - Dureri abdominale recidivante de etiologie neelucidată endoscopic
        - Sângerare digestivă ocultă fără cauză evidențiată la endoscopia superioară și colonoscopie
        - Suspiciune de neoplazie sau limfom al intestinului subțire, diverticul Meckel complicat
        - Episoade repetate de subocluzie mecanică prin bride peritoneale postoperatorii

    === "Contraindicații & Atenționări"

        - Ocluzie intestinală completă mecanică instalată cu distensie masivă de anse (contraindicație pentru administrare orală de contrast dens)
        - Suspiciune de perforație enterală cu peritonită acută
        - Megacolon toxic sau colită fulminantă asociată

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Intestin Subțire*
            - **Grad de Recomandare:** **Grad B**
            - **Nivel de Iradiere Estimată:** `Clasa 2 (Medie 1 - 5 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Substanță de Contrast__

    ---

    - **Pregătire Prealabilă:** Regim alimentar fără reziduuri cu 2 zile anterior; à jeun cu 8-12 ore înainte de procedură; eventual administrarea unui laxativ osmotic ușor în ajun conform protocoalelor secției pentru un colon neîncărcat fecaloid.
    - **Agent de Contrast:** Sulfat de Bariu suspensie enterală de densitate medie (40-50% w/v) pentru tranzit per os (SBFT); La Enterocliză: administrare prin sondă nazo-jejunală a 250 ml suspensie de bariu urmată de infuzie de 1000-1500 ml soluție de metilceluloză 0.5% pentru realizarea dublului contrast enteral
    - **Cale de Administrare:** Orală (SBFT) SAU pe sondă nazo-jejunală avansată fluoroscopic dincolo de ligamentul Treitz (Enterocliză)
    - **Volum & Diluție:** 300 - 600 ml suspensie baritată
    - **Instrucțiuni Specifice:** Pacientul bea suspensia treptat în ritm susținut; se menține în decubit lateral drept pentru stimularea evacuării rapide gastrice a bariului în duoden

-   __3. Poziționare & Configurare Echipament (Masă / C-Arm)__

    ---

    - **Poziție Inițială Pacient:** Decubit ventral (poziție esențială: compresiunea naturală exercitată de greutatea pacientului pe planul mesei etalează ansele jejuno-ileale prevenind aglomerarea lor în pelvis); decubit dorsal la compresia manuală țintită
    - **Configurare Braț C / Echipament:** Masă fluoroscopică digitală cu paletă sau con mecanic de compresiune dozată; distanță focar-film 100-115 cm
    - **Distanță Focar-Receptor:** 100 - 115 cm

-   __4. Parametri Tehnici Scopie & Expunere__

    ---

    | Parametru Tehnic Scopie & Grafie | Valoare Configurare Generator / Arc C |
    |:---------------------------------|:---------------------------------------|
    | **Regim Fluoroscopie** | Radiografii seriate discrete la intervale regulate + Fluoroscopie Pulsată scurtă DOAR la compresia ileală |
    | **Tensiune Tub (kV)** | 100 - 120 kV (contrast baritat enteral) kV |
    | **Curent Tub Scopie (mA)** | 1.0 - 3.0 mA în scopie |
    | **Distanță Focar-Receptor (SID)** | 100 - 115 cm (detector cât mai aproape de pacient) |
    | **Grilă Antidifuzoare** | Cu grilă antidifuzoare |
    | **Filtrare Suplimentară** | ≥ 3.0 mm Al |
    | **Timp Țintă Scopie** | < 2.0 minute cumulat pe toată durata tranzitului |
    | **Last Image Hold (LIH)** | Activ |

-   __5. Secvență Achiziție & Incidențe Seriate__

    ---

    - **Cliseu de Debut (15 minute):** Radiografie abdominală în decubit ventral: se evaluează jejunul proximal, pliurile kerckringiene feathery (valvulele connivente) și viteza inițială de golire gastrică.
    - **Seriere Temporizată (30 - 60 - 90 minute):** Radiografii seriate la intervale de 30 minute în decubit ventral; se urmărește progresia coloanei opace prin jejunul distal și ansele ileale, monitorizând calibrul luminal și motilitatea.
    - **Examen Țintit Fluoroscopic pe Ileonul Terminal:** În momentul în care bariul atinge fosa iliacă dreaptă: se trece în regim de fluoroscopie scurtă; se aplică compresiune dozată cu paleta/conul pentru a derula ultima ansă ileală și valva ileo-cecală fără suprapunerea anselor pelvine.
    - **Confirmarea Pasajului în Cec (Final de Examen):** Opacifierea cecului și a colonului ascendent confirmă tranzitul complet prin întregul intestin subțire; se face un cliseu panoramic final.

-   __6. Criterii de Calitate & Diagnostic__

    ---

    - Demonstrarea completă a tuturor segmentelor intestinului subțire până la nivelul cecului
    - Etalarea fără suprapunere a ileonului terminal (sediul predilect al bolii Crohn)
    - Distincție clară între desenul feathery jejunal și mucoasa mai netedă ileală
    - Identificarea oricărei rigidități parietale, fistule, stenoze sau imagini lacunare

-   __7. Radioprotecție & Dozimetrie (ALARA)__

    ---

    - REGULĂ DE AUR: Fluoroscopia NU se lasă deschisă în așteptarea pasajului! Tranzitul se monitorizează prin radiografii punctuale (spot films) la intervale stabilite
    - Timpul total cumulat de fluoroscopie trebuie să fie strict < 1.5 - 2 minute
    - Colimare strictă la compresia ileonului terminal pe fosa iliacă dreaptă
    - DAP < 12 Gy·cm²
    - Protecție gonadală poziționată atunci când nu maschează ansele din micul bazin

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Utilizarea unui agent prokinetic (ex. metoclopramid 10 mg oral cu 15 min înainte) poate fi indicată la pacienții cu tranzit lent pentru a scurta timpul de așteptare de la 3-4 ore la sub 60-90 de minute, reducând numărul de expuneri necesare.

=== "Ghid Rapid de Execuție & Siguranță Fluoroscopică"

    1. **Pregătire și Informare:** Verificarea identității pacientului, a indicației clinice, a excluderii sarcinii la paciente fertile și informarea privind substanța de contrast.
    2. **Configurare Echipament:** La C-Arm mobil, tubul se poziționează OBLIGATORIU sub masa operatorie, iar detectorul plat cât mai aproape de pacient pentru minimalizarea radiației difuze către operator.
    3. **Optimizare Doză (ALARA):** Se utilizează regim de fluoroscopie pulsată (4 - 7.5 - 15 fps) în locul modului continuu și colimare strânsă strict pe zona de interes.
    4. **Last Image Hold (LIH):** Utilizarea imaginii înghețate pe monitor pentru decizii operatorii sau analize anatomice, fără reactivarea inutilă a pedalei de expunere.
    5. **Protecție Personal:** Toți membrii echipei prezenți în sală poartă echipament individual de protecție din plumb (șorț echivalent 0.35-0.5 mm Pb, guler tiroidian, ochelari plumbuiți) și păstrează o distanță maximă posibilă față de tub conform legii pătratului invers al distanței.

## Surse și revizuire

- [ACR-SAR-SPR Practice Parameter for the Performance of Gastrointestinal Fluoroscopy in Adults](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Fluoro.pdf) — *ACR / SAR / SPR* (US)
- [UT Southwestern Radiology — Diagnostic Fluoroscopy Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/diagnostic.html) — *UT Southwestern* (US)
