---
author: Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth
category: neuro
clinical_indications:
- Accident vascular cerebral acut ischemic (AVC) în fereastra terapeutică (tromboliză
  / trombectomie)
- Atac ischemic tranzitor (AIT) sau suflu carotidian asimptomatic
- Evaluarea stenozei arterei carotide interne (clasificare NASCET / ECST)
- Suspiciune de anevrism arterial intracranian sau disecție vasculară cervico-cerebrală
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 15-18s
  flow_rate: 4.5 - 5.0 mL/s
  roi: Crosa aortică / artera carotidă comună la nivel C4-C5
  timing: Bolus tracking pe crosa aortică sau artera carotidă comună; trigger 120-150
    HU
  trigger: 120-150 HU
  volume: 70-80 mL contrast + 40-50 mL flush salin
iris_reference:
  chapter: Cap, Gât & Coloană vertebrală
  radiation_dose: Clasa 3 (Moderată 5 - 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-26'
notes:
  nursing: În caz de AVC acut (Cod AVC), deplasare imediată la tomograf; timpul până
    la recanalizare este creier.
  rad: Evaluați ocluziile de vas mare (LVO) la nivelul ACM (M1/M2), carotidei interne
    terminale (T-carotidian) sau arterei bazilare. Raportați scorul de colateralitate
    vasculară.
  tech: Canulă 18G în plica cotului. Declanșare precisă a bolus tracking-ului pentru
    a evita contaminarea venoasă jugulară precoce.
  tips: Pentru diferențierea ocluziei complete de carotida cu lumen filiform (pseudo-ocluzie),
    analizați secțiunile tardive sau MIP-urile reconstruite atent.
npo: Repaus alimentar 2-4 ore dacă timpul permite; în urgență N/A
position: Decubit dorsal, capul poziționat simetric în tetieră, bărbia coborâtă ușor,
  imobilizare cu bandă
premedication: Fără contrast oral
protocol_type: contrast-enhanced
recons:
- acquisition: CTA Crosa Aortică - Vertex
  fov: Craniu & Gât
  ir_strength: Standard
  kernel: Head Standard / Vascular
  notes: Detectare trombi endoluminali și cuantificare stenoză
  plane: Axial Cerebral Subțire
  thickness_increment: 0.625 mm / 0.5 mm
- acquisition: CTA Crosa Aortică - Vertex
  fov: Bifurcații carotidiene
  ir_strength: Standard
  kernel: Vascular
  notes: Măsurare diametru lumen rezidual conform criteriilor NASCET
  plane: MIP Coronal & Sagital Carotidian
  thickness_increment: 3.0 mm q 1.5 mm MIP
- acquisition: CTA Crosa Aortică - Vertex
  fov: Poligonul lui Willis
  ir_strength: Standard
  kernel: Vascular
  notes: Căutare anevrisme saculare pe AComA, AComP, bifurcația ACM
  plane: 3D VR & MIP Poligonul lui Willis
  thickness_increment: Rotire 360° MIP
safety:
  allergy: În AVC acut, beneficiul trombectomiei și diagnosticului imediat depășește
    riscul reacției alergice ușoare.
  renal: Nu amânați scanarea la pacienți cu suspiciune de ocluzie arterială acută.
series:
- delay: Trigger + 3-4 sec
  end: Vertex (creștetul craniului)
  name: CTA Crosa Aortică până la Vertex
  notes: Opacifiere densă de la originile vaselor mari supraaortice până la ramurile
    distale M2/M3 și A2/A3
  start: Nivelul crosei aortice (baza gâtului)
  thickness: 0.625 mm
tech_params:
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: 100 - 120 kVp
  mas: Modulare automată de doză neuro
  pitch: 0.8 - 1.0
  rotation_time: 0.33 - 0.5 s
  scan_mode: Elicoidal rapid cranio-caudal sau caudo-cranial
  slice_thickness: 0.625 mm
title: CTA Carotide și Poligonul lui Willis (Protocol Dartmouth Hitchcock)
---

# CTA Carotide și Poligonul lui Willis (Protocol Dartmouth Hitchcock)

**Ultima actualizare:** 2026-09-26
**Autor:** Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CTA Crosa Aortică până la Vertex | Trigger + 3-4 sec | Nivelul crosei aortice (baza gâtului) → Vertex (creștetul craniului) |

    === "Indicații Clinice"

        - Accident vascular cerebral acut ischemic (AVC) în fereastra terapeutică (tromboliză / trombectomie)
        - Atac ischemic tranzitor (AIT) sau suflu carotidian asimptomatic
        - Evaluarea stenozei arterei carotide interne (clasificare NASCET / ECST)
        - Suspiciune de anevrism arterial intracranian sau disecție vasculară cervico-cerebrală

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Cap, Gât & Coloană vertebrală*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 5 - 10 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal, capul poziționat simetric în tetieră, bărbia coborâtă ușor, imobilizare cu bandă
    - **Repaus Alimentar (NPO):** Repaus alimentar 2-4 ore dacă timpul permite; în urgență N/A
    - **Premedicație / Pregătire:**
        - Fără contrast oral

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 70-80 mL contrast + 40-50 mL flush salin |
        | Rată de Flux | 4.5 - 5.0 mL/s |
        | Durată | 15-18s |
        | Metodă Temporizare | Bolus tracking pe crosa aortică sau artera carotidă comună; trigger 120-150 HU |
        | Poziționare ROI | Crosa aortică / artera carotidă comună la nivel C4-C5 |
        | Declanșator (HU) | 120-150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 - 120 kVp kV |
    | **Curent Tub (mAs)** | Modulare automată de doză neuro |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare angulară adaptivă / Curent fix fosa posterioară) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 128 × 0.6 mm |
    | **Timp de Rotație** | 0.33 - 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.0 |
    | **Mod Scanare** | Elicoidal rapid cranio-caudal sau caudo-cranial |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Canulă 18G în plica cotului. Declanșare precisă a bolus tracking-ului pentru a evita contaminarea venoasă jugulară precoce.

    === "Note Asistent"

        - În caz de AVC acut (Cod AVC), deplasare imediată la tomograf; timpul până la recanalizare este creier.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu amânați scanarea la pacienți cu suspiciune de ocluzie arterială acută.
            - **Alergii:** În AVC acut, beneficiul trombectomiei și diagnosticului imediat depășește riscul reacției alergice ușoare.

    === "Note Radiolog"

        - Evaluați ocluziile de vas mare (LVO) la nivelul ACM (M1/M2), carotidei interne terminale (T-carotidian) sau arterei bazilare. Raportați scorul de colateralitate vasculară.

    === "Sfaturi & Recomandări"

        - Pentru diferențierea ocluziei complete de carotida cu lumen filiform (pseudo-ocluzie), analizați secțiunile tardive sau MIP-urile reconstruite atent.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CTA Crosa Aortică până la Vertex | Nivelul crosei aortice (baza gâtului) | Vertex (creștetul craniului) | Trigger + 3-4 sec | 0.625 mm | Opacifiere densă de la originile vaselor mari supraaortice până la ramurile distale M2/M3 și A2/A3 |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial Cerebral Subțire | CTA Crosa Aortică - Vertex | Craniu & Gât | 0.625 mm / 0.5 mm | Head Standard / Vascular | Standard | Detectare trombi endoluminali și cuantificare stenoză |
    | MIP Coronal & Sagital Carotidian | CTA Crosa Aortică - Vertex | Bifurcații carotidiene | 3.0 mm q 1.5 mm MIP | Vascular | Standard | Măsurare diametru lumen rezidual conform criteriilor NASCET |
    | 3D VR & MIP Poligonul lui Willis | CTA Crosa Aortică - Vertex | Poligonul lui Willis | Rotire 360° MIP | Vascular | Standard | Căutare anevrisme saculare pe AComA, AComP, bifurcația ACM |
