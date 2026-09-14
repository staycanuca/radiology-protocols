---
author: Departamentul de Radiologie
category: abdomen
clinical_indications:
- Hematurie microscopică sau macroscopică
- Suspiciune de carcinom urotelial
- Evaluarea sistemului pielocaliceal și ureteral
- Hidronefroză de etiologie neprecizată
contrast:
  agent: Isovue 370
  duration: 18-20s + 5-10s
  flow_rate: 4 mL/s
  timing: Tehnică Split-Bolus combinată
  volume: 'Tehnică Split Bolus: prima injectare 1.1 mL/kg + a doua injectare 0.4 mL/kg'
last_updated: '2026-01-01'
notes:
  additional_recons: Urografie MIP în plan coronal și sagital. Reconstrucții MPR curbate
    de-a lungul traiectului ureteral. Urografie 3D VR.
  nursing: Abord venos 18-20G. Tehnică split bolus. Se poate administra Furosemid
    10-20 mg IV la indicația medicului pentru o mai bună opacifiere și distensie ureterală.
  rad: 'Faza nativă: detectează litiaza. Faza venoasă timpurie: parenchimul renal.
    Faza excretorie: arborele urotelial, uretere, vezică urinară pentru formațiuni
    vegetative.'
  tech: 'Protocol COMPLEX: 1) Fază nativă (evaluare litiază) 2) Prima injectare de
    contrast 3) Fază venoasă timpurie la 60s 4) AȘTEPTARE 5-7 min 5) A doua injectare
    + flush ser 6) Fază excretorie / Uro-CT la 90-120s după a 2-a injectare.'
  tips: Sincronizarea split bolus este critică pentru opacifiere combinată parenchim-uroteliu.
    Scanarea în procubitus poate fi utilă pentru ureterele distale.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: Bună hidratare anterioară. Fără contrast oral pozitiv.
protocol_type: contrast-enhanced
recons:
- acquisition: Fază Nativă (opțională)
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Detecția calculilor pe nativ
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Venoasă Portală Timpurie
  fov: Abdomen
  kernel: Standard
  notes: Parenchim renal și stadializare
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Excretorie
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Suprafețe uroteliale și pereți vezicali
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Excretorie
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Urogramă coronală MIP
  plane: Coronal
  thickness_increment: 3 mm/3 mm
safety:
  allergy: Verificați istoricul alergic la substanța de contrast iodată.
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 0 sec
  end: Simfiză pubiană
  name: Fază Nativă (opțională)
  notes: Detecția calculilor reno-uretero-vezicali
  start: Polul superior renal
  thickness: 0.625 mm
- delay: 60-70 sec
  end: Creste iliace
  name: Fază Venoasă Portală Timpurie
  notes: Evaluarea parenchimului renal și hepatic
  start: Cupola hepatică
  thickness: 0.625 mm
- delay: 480-600 sec (8-10 min)
  end: Simfiză pubiană
  name: Fază Excretorie
  notes: Opacifierea completă a arborelui urotelial
  start: Polul superior renal
  thickness: 0.625 mm
slug: ct-ivp-intravenous-pyelogram
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: 100-120
  mas: Auto (referință 200 mAs)
  pitch: 1.0-1.375
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Uro-CT (Urografie CT / Pielografie Intravenoasă)
sources:
- title: AAPM CT Protocols — Adult Abdomen/Pelvis CT
  url: https://www.aapm.org/pubs/ctprotocols/documents/AdultAbdomenPelvisCT.pdf
  institution: AAPM
  source_region: US
  kind: Protocol tehnic standardizat
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: f0c7c2e31da9a9ed24dbdef7bd5b38994d670ba52d21b702faac79b97ace00c3
- title: UT Southwestern Radiology — CT Abdomen & Pelvis Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# Uro-CT (Urografie CT / Pielografie Intravenoasă)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă (opțională) | 0 sec | Polul superior renal → Simfiză pubiană |
        | Fază Venoasă Portală Timpurie | 60-70 sec | Cupola hepatică → Creste iliace |
        | Fază Excretorie | 480-600 sec (8-10 min) | Polul superior renal → Simfiză pubiană |

    === "Indicații Clinice"

        - Hematurie microscopică sau macroscopică
        - Suspiciune de carcinom urotelial
        - Evaluarea sistemului pielocaliceal și ureteral
        - Hidronefroză de etiologie neprecizată

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Bună hidratare anterioară. Fără contrast oral pozitiv.

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | Tehnică Split Bolus: prima injectare 1.1 mL/kg + a doua injectare 0.4 mL/kg |
        | Rată de Flux | 4 mL/s |
        | Durată | 18-20s + 5-10s |
        | Metodă Temporizare | Tehnică Split-Bolus combinată |
        | Poziționare ROI |  |
        | Declanșator (HU) |  |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100-120 kV |
    | **Curent Tub (mAs)** | Auto (referință 200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.0-1.375 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol COMPLEX: 1) Fază nativă (evaluare litiază) 2) Prima injectare de contrast 3) Fază venoasă timpurie la 60s 4) AȘTEPTARE 5-7 min 5) A doua injectare + flush ser 6) Fază excretorie / Uro-CT la 90-120s după a 2-a injectare.

    === "Note Asistent"

        - Abord venos 18-20G. Tehnică split bolus. Se poate administra Furosemid 10-20 mg IV la indicația medicului pentru o mai bună opacifiere și distensie ureterală.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic la substanța de contrast iodată.

    === "Note Radiolog"

        - Faza nativă: detectează litiaza. Faza venoasă timpurie: parenchimul renal. Faza excretorie: arborele urotelial, uretere, vezică urinară pentru formațiuni vegetative.

    === "Sfaturi & Recomandări"

        - Sincronizarea split bolus este critică pentru opacifiere combinată parenchim-uroteliu. Scanarea în procubitus poate fi utilă pentru ureterele distale.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă (opțională) | Polul superior renal | Simfiză pubiană | 0 sec | 0.625 mm | Detecția calculilor reno-uretero-vezicali |
    | Fază Venoasă Portală Timpurie | Cupola hepatică | Creste iliace | 60-70 sec | 0.625 mm | Evaluarea parenchimului renal și hepatic |
    | Fază Excretorie | Polul superior renal | Simfiză pubiană | 480-600 sec (8-10 min) | 0.625 mm | Opacifierea completă a arborelui urotelial |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Nativă (opțională) | Abdomen-Pelvis | 2.5 mm/2.5 mm | Standard |  | Detecția calculilor pe nativ |
    | Axial | Fază Venoasă Portală Timpurie | Abdomen | 2.5 mm/2.5 mm | Standard |  | Parenchim renal și stadializare |
    | Axial | Fază Excretorie | Abdomen-Pelvis | 2.5 mm/2.5 mm | Standard |  | Suprafețe uroteliale și pereți vezicali |
    | Coronal | Fază Excretorie | Abdomen-Pelvis | 3 mm/3 mm | Standard |  | Urogramă coronală MIP |

## Surse și revizuire

- [AAPM CT Protocols — Adult Abdomen/Pelvis CT](https://www.aapm.org/pubs/ctprotocols/documents/AdultAbdomenPelvisCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Abdomen & Pelvis Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
