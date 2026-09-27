---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen
clinical_indications:
- Hematurie macroscopică nedureroasă sau hematurie microscopică asimptomatică persistentă
- Suspiciune de carcinom urotelial la nivelul calicelor, bazinetului, ureterelor sau
  vezicii urinare
- Litiază renală și ureterală complicată sau recidivantă cu obstrucție
- Traumatisme sau stenoze ale tractului urinar superior și inferior
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 35-40s
  flow_rate: 3.0 mL/s
  roi: N/A
  timing: Fază Nefrografică (100 sec) și Fază Excretorie Tardivă (10-12 min) sau protocol
    Split-Bolus
  trigger: N/A
  volume: 100-120 mL (sau split-bolus)
iris_reference:
  chapter: Aparat uro-genital și glande suprarenale
  radiation_dose: Clasa 4 (Ridicată > 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții Coronal MIP 3D 'urografie CT' din faza excretorie
    pentru vizualizare completă tip urografie clasică.
  nursing: Canulă 20G. Supraveghere pacient în intervalul de 10 minute premergător
    fazei excretorii.
  rad: Căutați defecte de umplere uroteliale fixe, îngroșări parietale ureterale,
    asimetrii de excreție și calculi obstructivi.
  tech: Pacientul trebuie să evite micțiunea în perioada de așteptare dintre faza
    nefrografică și faza tardivă excretorie pentru a permite umplerea vezicii urinare.
  tips: 'Pentru a reduce doza de radiație la pacienți tineri, se poate utiliza tehnica
    Split-Bolus: 30-40 mL contrast i.v. inițial, pauză 10 minute, apoi 80 mL contrast
    și scanare la 100 secunde (obținând o fază combinată nefrografică + excretorie
    într-o singură scanare).'
npo: Repaus alimentar 4 ore; hidratare orală permisă (500 mL apă înainte de scanare
  pentru distensie vezicală)
position: Decubit dorsal
premedication: Fără contrast oral iodat sau baritat; hidratare per os cu apă
protocol_type: multiphase
recons:
- acquisition: Nativ, Nefrografic & Excretor
  fov: Abdomen / Bazin
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard / I30f
  notes: Serii de bază
  plane: Axial
  thickness_increment: 2.5 mm / 2.5 mm
- acquisition: Fază Excretorie
  fov: Tract Urinar
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard / I30f
  notes: Evaluare anatomică de ansamblu a arborelui pielo-ureteral
  plane: Coronal
  thickness_increment: 2.0 mm / 2.0 mm
safety:
  allergy: Screening conform politicii OHSU.
  renal: eGFR > 30 mL/min/1.73m² obligatoriu.
series:
- delay: 0 sec
  end: Simfiză pubiană
  name: Fază Nativă (Rinichi -> Pelvis)
  notes: Detectare calculi renali și ureterali radio-opaci fără mascare de către contrast
  start: Pol superior renal
  thickness: 1.0 mm
- delay: 100 sec
  end: Creste iliace
  name: Fază Nefrografică
  notes: Omogenitate maximă parenchimatoasă renală; detecție mase renale corticale
    și medulare
  start: Diafragm
  thickness: 0.625 mm
- delay: 10-12 min
  end: Simfiză pubiană
  name: Fază Excretorie Tardivă
  notes: Opacifiere completă calice, bazinete, uretere pe tot traiectul și vezică
    urinară; detectare defecte de umplere uroteliale
  start: Pol superior renal
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: CAREkV (Ref 120 kV)
  mas: CAREDose4D / SureExposure3D
  pitch: 0.9 - 1.1
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Urografie / Evaluare Hematurie (Protocol OHSU)
---

# CT Urografie / Evaluare Hematurie (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă (Rinichi -> Pelvis) | 0 sec | Pol superior renal → Simfiză pubiană |
        | Fază Nefrografică | 100 sec | Diafragm → Creste iliace |
        | Fază Excretorie Tardivă | 10-12 min | Pol superior renal → Simfiză pubiană |

    === "Indicații Clinice"

        - Hematurie macroscopică nedureroasă sau hematurie microscopică asimptomatică persistentă
        - Suspiciune de carcinom urotelial la nivelul calicelor, bazinetului, ureterelor sau vezicii urinare
        - Litiază renală și ureterală complicată sau recidivantă cu obstrucție
        - Traumatisme sau stenoze ale tractului urinar superior și inferior

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Aparat uro-genital și glande suprarenale*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 4 (Ridicată > 10 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore; hidratare orală permisă (500 mL apă înainte de scanare pentru distensie vezicală)
    - **Premedicație / Pregătire:**
        - Fără contrast oral iodat sau baritat; hidratare per os cu apă

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 100-120 mL (sau split-bolus) |
        | Rată de Flux | 3.0 mL/s |
        | Durată | 35-40s |
        | Metodă Temporizare | Fază Nefrografică (100 sec) și Fază Excretorie Tardivă (10-12 min) sau protocol Split-Bolus |
        | Poziționare ROI | N/A |
        | Declanșator (HU) | N/A |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | CAREkV (Ref 120 kV) kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9 - 1.1 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Pacientul trebuie să evite micțiunea în perioada de așteptare dintre faza nefrografică și faza tardivă excretorie pentru a permite umplerea vezicii urinare.

    === "Note Asistent"

        - Canulă 20G. Supraveghere pacient în intervalul de 10 minute premergător fazei excretorii.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR > 30 mL/min/1.73m² obligatoriu.
            - **Alergii:** Screening conform politicii OHSU.

    === "Note Radiolog"

        - Căutați defecte de umplere uroteliale fixe, îngroșări parietale ureterale, asimetrii de excreție și calculi obstructivi.

    === "Sfaturi & Recomandări"

        - Pentru a reduce doza de radiație la pacienți tineri, se poate utiliza tehnica Split-Bolus: 30-40 mL contrast i.v. inițial, pauză 10 minute, apoi 80 mL contrast și scanare la 100 secunde (obținând o fază combinată nefrografică + excretorie într-o singură scanare).

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă (Rinichi -> Pelvis) | Pol superior renal | Simfiză pubiană | 0 sec | 1.0 mm | Detectare calculi renali și ureterali radio-opaci fără mascare de către contrast |
    | Fază Nefrografică | Diafragm | Creste iliace | 100 sec | 0.625 mm | Omogenitate maximă parenchimatoasă renală; detecție mase renale corticale și medulare |
    | Fază Excretorie Tardivă | Pol superior renal | Simfiză pubiană | 10-12 min | 0.625 mm | Opacifiere completă calice, bazinete, uretere pe tot traiectul și vezică urinară; detectare defecte de umplere uroteliale |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Nativ, Nefrografic & Excretor | Abdomen / Bazin | 2.5 mm / 2.5 mm | Standard / I30f | Admire 3 / AIDR 3D | Serii de bază |
    | Coronal | Fază Excretorie | Tract Urinar | 2.0 mm / 2.0 mm | Standard / I30f | Admire 3 / AIDR 3D | Evaluare anatomică de ansamblu a arborelui pielo-ureteral |
