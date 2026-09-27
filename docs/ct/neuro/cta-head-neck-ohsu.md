---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: neuro
clinical_indications:
- Accident vascular cerebral acut ischemic (evaluare ocluzie vase mari LVO pentru
  trombectomie)
- AIT (atac ischemic tranzitor), amaurosis fugax
- Stenoze, ocluzii sau disecții ale arterelor carotide și vertebrale
- Anevrism intracranian, malformații arterio-venoase (MAV)
- Traumatism cervical penetrant sau contondent cu suspiciune de leziune vasculară
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 10-12s
  flow_rate: 5.0 mL/s (Adult) / 1.0-4.0 mL/s (Pediatric)
  roi: Crosa aortică / Artera carotidă comună
  timing: 'Bolus tracking: Trigger la 120 HU în crosa aortică / artera carotidă comună'
  trigger: 120 HU
  volume: 50 mL (Adult) / 2 mL/kg (Pediatric, max 50 mL)
iris_reference:
  chapter: Gât (părți moi)
  radiation_dose: Clasa 3 (Moderată 3 - 6 mSv)
  recommendation_grade: Grad B
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții 3D VR ale trunchiurilor supra-aortice și poligonului
    lui Willis.
  nursing: Verificare obligatorie a permeabilității căii venoase cu jet rapid înainte
    de injectarea la 5.0 mL/s.
  rad: Evaluați calibrul vascular conform criteriilor NASCET pentru stenoza carotidiană;
    verificați semnele de ocluzie de vas mare (M1, A1, basilară) și circulația colaterală.
  tech: Abord venos 20G sau mai mare în plica cotului (antecubital). Nu angulați gantry-ul.
    Flush salin 40 mL imediat după contrast.
  tips: În caz de aparat Philips 16 slice se poate folosi un volum de până la 80 mL
    contrast conform instrucțiunilor OHSU.
npo: Repaus alimentar 2-4 ore dacă starea permite; în AVC acut N/A
position: Decubit dorsal, cap drept în suport dedicat, fără angularea gantry-ului
premedication: CT Craniu Nativ efectuat imediat anterior conform ghidului OHSU
protocol_type: contrast-enhanced
recons:
- acquisition: CTA Cap & Gât
  fov: Cap / Gât
  ir_strength: Standard
  kernel: Creier / Vascular
  notes: MIP axial gros pentru urmărirea rapidă a poligonului Willis și a ramurilor
    carotidiene
  plane: Axial
  thickness_increment: 5.0 mm / 2.5 mm MIP
- acquisition: CTA Cap & Gât
  fov: Cap / Gât
  ir_strength: Standard
  kernel: Creier / Vascular
  notes: MIP coronal și sagital pentru evaluarea bifurcației carotidiene și arterelor
    vertebrale
  plane: Coronal & Sagital
  thickness_increment: 5.0 mm / 2.5 mm MIP
- acquisition: CTA Cap & Gât
  fov: Cap / Gât
  ir_strength: Standard
  kernel: Vascular / Țesut moale
  notes: Secțiuni submilimetrice pentru analiza pereților vasculari și a plăcilor
    de aterom
  plane: Axial, Coronal & Sagital
  thickness_increment: 1.0 mm / 1.0 mm Avg
safety:
  allergy: Conform politicii OHSU. În AVC acut, beneficiul trombectomiei este prioritar.
  renal: eGFR conform protocolului OHSU.
series:
- delay: Trigger + 3-4 sec
  end: Deasupra vertexului (inclusiv țesuturi moi)
  name: CTA Cap & Gât
  notes: Acoperire completă de la crosa aortică până la vertex; DFOV 220 mm
  start: Nivelul crosei aortice (sub baza nasului)
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: CAREkV 100-120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 0.8 - 1.0
  rotation_time: 0.33 - 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CTA Cap & Gât cu Contrast (Protocol OHSU)
---

# CTA Cap & Gât cu Contrast (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CTA Cap & Gât | Trigger + 3-4 sec | Nivelul crosei aortice (sub baza nasului) → Deasupra vertexului (inclusiv țesuturi moi) |

    === "Indicații Clinice"

        - Accident vascular cerebral acut ischemic (evaluare ocluzie vase mari LVO pentru trombectomie)
        - AIT (atac ischemic tranzitor), amaurosis fugax
        - Stenoze, ocluzii sau disecții ale arterelor carotide și vertebrale
        - Anevrism intracranian, malformații arterio-venoase (MAV)
        - Traumatism cervical penetrant sau contondent cu suspiciune de leziune vasculară

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Gât (părți moi)*
            - **Grad de Recomandare:** **Grad B**
            - **Nivel de Iradiere Estimată:** `Clasa 3 (Moderată 3 - 6 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal, cap drept în suport dedicat, fără angularea gantry-ului
    - **Repaus Alimentar (NPO):** Repaus alimentar 2-4 ore dacă starea permite; în AVC acut N/A
    - **Premedicație / Pregătire:**
        - CT Craniu Nativ efectuat imediat anterior conform ghidului OHSU

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 50 mL (Adult) / 2 mL/kg (Pediatric, max 50 mL) |
        | Rată de Flux | 5.0 mL/s (Adult) / 1.0-4.0 mL/s (Pediatric) |
        | Durată | 10-12s |
        | Metodă Temporizare | Bolus tracking: Trigger la 120 HU în crosa aortică / artera carotidă comună |
        | Poziționare ROI | Crosa aortică / Artera carotidă comună |
        | Declanșator (HU) | 120 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | CAREkV 100-120 kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare angulară adaptivă / Curent fix fosa posterioară) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.33 - 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.0 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Abord venos 20G sau mai mare în plica cotului (antecubital). Nu angulați gantry-ul. Flush salin 40 mL imediat după contrast.

    === "Note Asistent"

        - Verificare obligatorie a permeabilității căii venoase cu jet rapid înainte de injectarea la 5.0 mL/s.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR conform protocolului OHSU.
            - **Alergii:** Conform politicii OHSU. În AVC acut, beneficiul trombectomiei este prioritar.

    === "Note Radiolog"

        - Evaluați calibrul vascular conform criteriilor NASCET pentru stenoza carotidiană; verificați semnele de ocluzie de vas mare (M1, A1, basilară) și circulația colaterală.

    === "Sfaturi & Recomandări"

        - În caz de aparat Philips 16 slice se poate folosi un volum de până la 80 mL contrast conform instrucțiunilor OHSU.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CTA Cap & Gât | Nivelul crosei aortice (sub baza nasului) | Deasupra vertexului (inclusiv țesuturi moi) | Trigger + 3-4 sec | 0.625 mm | Acoperire completă de la crosa aortică până la vertex; DFOV 220 mm |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CTA Cap & Gât | Cap / Gât | 5.0 mm / 2.5 mm MIP | Creier / Vascular | Standard | MIP axial gros pentru urmărirea rapidă a poligonului Willis și a ramurilor carotidiene |
    | Coronal & Sagital | CTA Cap & Gât | Cap / Gât | 5.0 mm / 2.5 mm MIP | Creier / Vascular | Standard | MIP coronal și sagital pentru evaluarea bifurcației carotidiene și arterelor vertebrale |
    | Axial, Coronal & Sagital | CTA Cap & Gât | Cap / Gât | 1.0 mm / 1.0 mm Avg | Vascular / Țesut moale | Standard | Secțiuni submilimetrice pentru analiza pereților vasculari și a plăcilor de aterom |
