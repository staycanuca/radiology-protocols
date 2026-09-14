---
acquisition_steps:
- description: Înclinarea craniocaudală a arcului C până când platourile vertebrale
    superioare și inferioare ale discului țintă sunt aliniate perfect paralel (linie
    unică pe monitor).
  phase: Alinierea Nivelului Vertebral Țintă (AP)
- description: 'Rotirea arcului C oblic ipsilateral 20-25°: foramenul intervertebral
    și ''ochiul cățelului'' (pediculul vertebral) devin vizibile; reperarea zonei
    de siguranță subpediculare.'
  phase: Vizualizare Oblică ('Scotty Dog')
- description: Acul spinal este orientat coaxial, perfect paralel cu traiectul razelor
    X (apare ca un singur punct pe ecran); avansare progresivă către treimea postero-superioară
    a foramenului.
  phase: Avansarea Acului (Tehnica 'Gun-Barrel')
- description: 'Comutarea arcului C la 90° în profil: vârful acului se oprește în
    treimea postero-superioară a foramenului intervertebral, fără a depăși peretele
    posterior al corpului vertebral în canalul medular.'
  phase: Verificare Profil Strict
- description: 'Injectarea a 1 ml de contrast non-ionic sub fluoroscopie: se evidențiază
    delimitarea tecii radiculare (epidurogramă) și se exclude diseminarea intravasculară
    (contrastul vascular se spală instantaneu) sau subarahnoidiană (mielogramă).'
  phase: Epidurograma cu Contrast & Excluderea Intravasculară
- description: 'După validarea contrastografică certă: injectarea lentă a amestecului
    de anestezic local (Ropivacaină/Bupivacaină) și corticosteroid (Dexametazonă /
    Triamcinolon).'
  phase: Injectarea Terapeutică
author: Departamentul de Radiologie și Imagistică Medicală
category: c-arm
clinical_indications:
- Radiculopatie lombară sau cervicală rebelă secundară unei hernii discale sau stenoze
  foraminale (infiltrație transforaminală peridurală)
- Sindrom fațetar lombar sau cervical (bloc de ramură medială / infiltrație intra-articulară
  fațetară)
- Sacroileită cronică, disfuncție articulară sacroiliacă dureroasă refractară la medicație
  conservatoare
- Stenoză degenerativă de canal vertebral cu claudicație neurogenă (infiltrație interlaminară
  sau transforaminală)
- Sindrom dureros post-laminectomie (failed back surgery syndrome)
contraindications:
- Coagulopatie activă severă sau tratament anticoagulant/antiagregant neîntrerupt
  conform intervalelor ghidului ASRA (risc de hematom peridural compresiv)
- Infecție locală cutanată la locul puncției sau infecție sistemică (bacteriemie /
  discită / abces peridural)
- Alergie cunoscută severă la anestezice locale, corticosteroizi sau contrast iodat
- Sarcină documentată
contrast:
  agent: Contrast iodat hidrosolubil non-ionic izoosmolar (Omnipaque 240/300) pur
  instructions: 'MOMENT CRITIC: Testul cu contrast iodat este OBLIGATORIU înainte
    de injectarea oricărui corticosteroid; dacă se decelează difuzie vasculară intravasculară,
    acul se repoziționează IMEDIAT (injectarea intra-arterială a corticoidului particulat
    provoacă infarct medular paraplegic!)'
  route: Injectare pe acul spinal (Tuohy 20-22G sau Quincke 22-25G) sub vizualizare
    fluoroscopică continuă în timp real
  volume: 0.5 - 2.0 ml contrast
fluoro_params:
  filtration: ≥ 3.0 mm Al
  grid: Cu grilă
  kv: 75 - 90 kV
  lih: Activ obligatoriu
  ma_range: 1.0 - 2.5 mA
  mode: Fluoroscopie Pulsată (4 - 7.5 fps) cu colimare strânsă + Last Image Hold
  target_fluoro_time: < 45 - 60 secunde timp total scopie
iris_reference:
  chapter: Coloană & Terapia Durerii
  radiation_dose: Clasa 1 (Minimă < 1 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: fluoro
notes: Se recomandă cu prioritate utilizarea corticosteroizilor non-particulați (Dexametazonă
  fosfat sodic) pentru infiltrațiile transforaminale cervicale și lombare, deoarece
  particulele de depozit (ex. dipropionat de betametazonă) pot cauza tromboză microvasculară
  fatală în cazul unei pătrunderi neintenționate într-o arteră radiculară (artera
  Adamkiewicz).
patient_prep: Decubit ventral pe masa radiotransparentă cu pernă sub abdomen (atenuează
  lordoza lombară și deschide spațiile interlaminare și foramenele); monitorizare
  puls-oximetrie și tensiune arterială; asepsie chirurgicală cu betadină; câmp steril
  fenestrat.
positioning_equipment:
  equipment_setup: 'Arc C mobil manevrat milimetric în 3 incidențe cheie: AP (aliniere
    platouri vertebrale), Oblic 20-30° (vizualizarea foramenului intervertebral și
    a aspectului de ''Scotty Dog'' / cățel scoțian), Profil strict (verificarea adâncimii
    pătrunderii acului)'
  patient_position: Decubit ventral relaxat cu brațele deasupra capului
  sid: 90 - 100 cm
quality_criteria:
- Poziționarea vârfului acului în ținta anatomică precisă confirmată în două planuri
  perpendiculare
- Diseminare contrastografică peridurală sau periradiculară tipică fără semne de efracție
  durală
- Excluderea absolută a difuziei intravasculare pe secvența fluoroscopică dinamică
- Cliseu radiologic martor salvat în sistemul PACS cu acul și contrastul pe poziție
radiation_safety:
- Colimare milimetrică pe spațiul foraminal/articular (câmp de expunere sub 8x8 cm)
- Fiecare verificare se face printr-un scurt impuls de pedală de 0.5 secunde
- Timpul cumulat de scopie este extrem de redus (< 45 secunde)
- DAP < 2.5 Gy·cm²
- Mâinile medicului operator sunt ținute la distanță de fascicul prin utilizarea penselor
  de ghidaj sau a extensiilor de injectare
slug: c-arm-infiltratii-rahidiene-si-durere
title: 'C-Arm în Terapia Durerii: Infiltrații Peridurale, Fațetare & Sacroiliace'
---
# C-Arm în Terapia Durerii: Infiltrații Peridurale, Fațetare & Sacroiliace

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

        - Radiculopatie lombară sau cervicală rebelă secundară unei hernii discale sau stenoze foraminale (infiltrație transforaminală peridurală)
        - Sindrom fațetar lombar sau cervical (bloc de ramură medială / infiltrație intra-articulară fațetară)
        - Sacroileită cronică, disfuncție articulară sacroiliacă dureroasă refractară la medicație conservatoare
        - Stenoză degenerativă de canal vertebral cu claudicație neurogenă (infiltrație interlaminară sau transforaminală)
        - Sindrom dureros post-laminectomie (failed back surgery syndrome)

    === "Contraindicații & Atenționări"

        - Coagulopatie activă severă sau tratament anticoagulant/antiagregant neîntrerupt conform intervalelor ghidului ASRA (risc de hematom peridural compresiv)
        - Infecție locală cutanată la locul puncției sau infecție sistemică (bacteriemie / discită / abces peridural)
        - Alergie cunoscută severă la anestezice locale, corticosteroizi sau contrast iodat
        - Sarcină documentată

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Coloană & Terapia Durerii*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 1 (Minimă < 1 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Substanță de Contrast__

    ---

    - **Pregătire Prealabilă:** Decubit ventral pe masa radiotransparentă cu pernă sub abdomen (atenuează lordoza lombară și deschide spațiile interlaminare și foramenele); monitorizare puls-oximetrie și tensiune arterială; asepsie chirurgicală cu betadină; câmp steril fenestrat.
    - **Agent de Contrast:** Contrast iodat hidrosolubil non-ionic izoosmolar (Omnipaque 240/300) pur
    - **Cale de Administrare:** Injectare pe acul spinal (Tuohy 20-22G sau Quincke 22-25G) sub vizualizare fluoroscopică continuă în timp real
    - **Volum & Diluție:** 0.5 - 2.0 ml contrast
    - **Instrucțiuni Specifice:** MOMENT CRITIC: Testul cu contrast iodat este OBLIGATORIU înainte de injectarea oricărui corticosteroid; dacă se decelează difuzie vasculară intravasculară, acul se repoziționează IMEDIAT (injectarea intra-arterială a corticoidului particulat provoacă infarct medular paraplegic!)

-   __3. Poziționare & Configurare Echipament (Masă / C-Arm)__

    ---

    - **Poziție Inițială Pacient:** Decubit ventral relaxat cu brațele deasupra capului
    - **Configurare Braț C / Echipament:** Arc C mobil manevrat milimetric în 3 incidențe cheie: AP (aliniere platouri vertebrale), Oblic 20-30° (vizualizarea foramenului intervertebral și a aspectului de 'Scotty Dog' / cățel scoțian), Profil strict (verificarea adâncimii pătrunderii acului)
    - **Distanță Focar-Receptor:** 90 - 100 cm

-   __4. Parametri Tehnici Scopie & Expunere__

    ---

    | Parametru Tehnic Scopie & Grafie | Valoare Configurare Generator / Arc C |
    |:---------------------------------|:---------------------------------------|
    | **Regim Fluoroscopie** | Fluoroscopie Pulsată (4 - 7.5 fps) cu colimare strânsă + Last Image Hold |
    | **Tensiune Tub (kV)** | 75 - 90 kV |
    | **Curent Tub Scopie (mA)** | 1.0 - 2.5 mA |
    | **Distanță Focar-Receptor (SID)** | 100 - 115 cm (detector cât mai aproape de pacient) |
    | **Grilă Antidifuzoare** | Cu grilă |
    | **Filtrare Suplimentară** | ≥ 3.0 mm Al |
    | **Timp Țintă Scopie** | < 45 - 60 secunde timp total scopie |
    | **Last Image Hold (LIH)** | Activ obligatoriu |

-   __5. Secvență Achiziție & Incidențe Seriate__

    ---

    - **Alinierea Nivelului Vertebral Țintă (AP):** Înclinarea craniocaudală a arcului C până când platourile vertebrale superioare și inferioare ale discului țintă sunt aliniate perfect paralel (linie unică pe monitor).
    - **Vizualizare Oblică ('Scotty Dog'):** Rotirea arcului C oblic ipsilateral 20-25°: foramenul intervertebral și 'ochiul cățelului' (pediculul vertebral) devin vizibile; reperarea zonei de siguranță subpediculare.
    - **Avansarea Acului (Tehnica 'Gun-Barrel'):** Acul spinal este orientat coaxial, perfect paralel cu traiectul razelor X (apare ca un singur punct pe ecran); avansare progresivă către treimea postero-superioară a foramenului.
    - **Verificare Profil Strict:** Comutarea arcului C la 90° în profil: vârful acului se oprește în treimea postero-superioară a foramenului intervertebral, fără a depăși peretele posterior al corpului vertebral în canalul medular.
    - **Epidurograma cu Contrast & Excluderea Intravasculară:** Injectarea a 1 ml de contrast non-ionic sub fluoroscopie: se evidențiază delimitarea tecii radiculare (epidurogramă) și se exclude diseminarea intravasculară (contrastul vascular se spală instantaneu) sau subarahnoidiană (mielogramă).
    - **Injectarea Terapeutică:** După validarea contrastografică certă: injectarea lentă a amestecului de anestezic local (Ropivacaină/Bupivacaină) și corticosteroid (Dexametazonă / Triamcinolon).

-   __6. Criterii de Calitate & Diagnostic__

    ---

    - Poziționarea vârfului acului în ținta anatomică precisă confirmată în două planuri perpendiculare
    - Diseminare contrastografică peridurală sau periradiculară tipică fără semne de efracție durală
    - Excluderea absolută a difuziei intravasculare pe secvența fluoroscopică dinamică
    - Cliseu radiologic martor salvat în sistemul PACS cu acul și contrastul pe poziție

-   __7. Radioprotecție & Dozimetrie (ALARA)__

    ---

    - Colimare milimetrică pe spațiul foraminal/articular (câmp de expunere sub 8x8 cm)
    - Fiecare verificare se face printr-un scurt impuls de pedală de 0.5 secunde
    - Timpul cumulat de scopie este extrem de redus (< 45 secunde)
    - DAP < 2.5 Gy·cm²
    - Mâinile medicului operator sunt ținute la distanță de fascicul prin utilizarea penselor de ghidaj sau a extensiilor de injectare

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Se recomandă cu prioritate utilizarea corticosteroizilor non-particulați (Dexametazonă fosfat sodic) pentru infiltrațiile transforaminale cervicale și lombare, deoarece particulele de depozit (ex. dipropionat de betametazonă) pot cauza tromboză microvasculară fatală în cazul unei pătrunderi neintenționate într-o arteră radiculară (artera Adamkiewicz).

=== "Ghid Rapid de Execuție & Siguranță Fluoroscopică"

    1. **Pregătire și Informare:** Verificarea identității pacientului, a indicației clinice, a excluderii sarcinii la paciente fertile și informarea privind substanța de contrast.
    2. **Configurare Echipament:** La C-Arm mobil, tubul se poziționează OBLIGATORIU sub masa operatorie, iar detectorul plat cât mai aproape de pacient pentru minimalizarea radiației difuze către operator.
    3. **Optimizare Doză (ALARA):** Se utilizează regim de fluoroscopie pulsată (4 - 7.5 - 15 fps) în locul modului continuu și colimare strânsă strict pe zona de interes.
    4. **Last Image Hold (LIH):** Utilizarea imaginii înghețate pe monitor pentru decizii operatorii sau analize anatomice, fără reactivarea inutilă a pedalei de expunere.
    5. **Protecție Personal:** Toți membrii echipei prezenți în sală poartă echipament individual de protecție din plumb (șorț echivalent 0.35-0.5 mm Pb, guler tiroidian, ochelari plumbuiți) și păstrează o distanță maximă posibilă față de tub conform legii pătratului invers al distanței.
