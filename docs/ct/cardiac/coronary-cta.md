---
author: Departamentul de Radiologie
category: cardiac
clinical_indications:
- Durere toracică cu probabilitate pre-test intermediară de boală coronariană
- Suspiciune de sindrom coronarian acut fără supradenivelare de segment ST (troponină
  negativă)
- Disecție coronariană spontană sau anevrisme de artere coronare (boală Kawasaki etc.)
- Anomalii congenitale de origine și traiect coronarian
- Evaluarea permeabilității stenturilor coronariene (>= 3 mm)
contrast:
  agent: Isovue 370
  duration: 20s
  flow_rate: 4-5 mL/s
  roi: Aorta ascendentă
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 200 HU
  volume: 1.1 mL/kg
last_updated: '2026-02-02'
notes:
  additional_recons: Reconstrucții MPR curbate pentru toate trunchiurile (LM, LAD,
    LCx, RCA). Reconstrucții de ax scurt și ax lung cardiac.
  nursing: Linie venoasă minim 20G în plica cotului. Verificați contraindicațiile
    pentru metoprolol (astm sever, BAV avansat) sau nitroglicerină (stenoze aortice
    severe, medicație tip inhibitori PDE-5).
  rad: Calculați scorul Agatston. Acordați categoria CAD-RADS (0-5, P, N, G, V). Evaluați
    caracteristicile plăcii (stenoză, compoziție, remodelare pozitivă, atenuare redusă).
    Analizați cinetica pereților pe seriile multifazice.
  tech: 'Tehnică de respirație non-Valsalva. Notificați în observații dacă pacientul
    nu poate respecta apneea. Țintă: telediastolă (70-75%) la FC < 65 bpm; telesistolă
    (35-45%) la FC > 80 bpm; telediastolă și telesistolă la FC intermediară.'
  tips: Pregătirea pacientului și controlul frecvenței cardiace sunt definitorii pentru
    calitatea examinării.
npo: Repaus alimentar 4 ore; fără cafeină cu 12 ore înainte
position: Decubit dorsal cu picioarele înainte
premedication: Controlul frecvenței cardiace cu beta-blocant (oral sau IV, de ex.
  Metoprolol) țintind FC <= 60 bpm; Nitroglicerină sublingual (spray/comprimat 0.4-0.8
  mg) cu 2-3 minute înainte de injectare
protocol_type: vascular
recons:
- acquisition: Scor de Calciu
  fov: Cord
  kernel: Standard
  notes: Pentru calcularea scorului Agatston
  plane: Axial
  thickness_increment: 3 mm/3 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Torace
  kernel: Lung
  notes: Câmp pulmonar pentru leziuni extracardiace
  plane: Axial
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Cord
  kernel: Cardiac
  notes: Evaluarea nativă a lumenului coronarian
  plane: Axial
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Cord
  kernel: Cardiac
  notes: Randări 3D VR și MPR pe arborele coronarian
  plane: 3D VR
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Verificați istoricul alergic la contrast iodat
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 0 sec
  end: Sub cord
  name: Scor de Calciu
  notes: Scor de calciu coronarian de referință
  start: Carenă
  thickness: 3 mm
- delay: Urmărire bolus
  end: 2 cm sub apexul cordului
  name: Angio-CT Sincronizat ECG
  notes: Angio-CT sincronizat ECG prospectiv sau retrospectiv
  start: 2 cm deasupra ostiilor coronare
  thickness: 0.625 mm
slug: coronary-cta
synonyms: []
tech_params:
  aec: Modulare ECG activată (pulsare conform ritmului cardiac)
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: 100-120
  mas: Auto (modulare sincronizată ECG)
  pitch: 0.2-0.24
  rotation_time: 0.28s
  scan_mode: Elicoidal sincronizat ECG (sau Secvențial prospectiv)
  slice_thickness: 0.625 mm
title: Angio-CT Coronarian (Coronarografie CT)
sources:
- title: SCCT / ACR-NASCI Practice Parameter for Coronary CT Angiography
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Heart.pdf
  institution: ACR / SCCT
  source_region: US
  kind: Standard de practică cardiovasculară
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 16bdb917dce22c0f1620d70ff041aa5d8e0fb7f9d2139d1b15479b41a9f34a32
- title: UT Southwestern Radiology — Cardiovascular CT Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# Angio-CT Coronarian (Coronarografie CT)

**Ultima actualizare:** 2026-02-02
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Scor de Calciu | 0 sec | Carenă → Sub cord |
        | Angio-CT Sincronizat ECG | Urmărire bolus | 2 cm deasupra ostiilor coronare → 2 cm sub apexul cordului |

    === "Indicații Clinice"

        - Durere toracică cu probabilitate pre-test intermediară de boală coronariană
        - Suspiciune de sindrom coronarian acut fără supradenivelare de segment ST (troponină negativă)
        - Disecție coronariană spontană sau anevrisme de artere coronare (boală Kawasaki etc.)
        - Anomalii congenitale de origine și traiect coronarian
        - Evaluarea permeabilității stenturilor coronariene (>= 3 mm)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular (Cord)*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu picioarele înainte
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore; fără cafeină cu 12 ore înainte
    - **Premedicație / Pregătire:**
        - Controlul frecvenței cardiace cu beta-blocant (oral sau IV, de ex. Metoprolol) țintind FC <= 60 bpm; Nitroglicerină sublingual (spray/comprimat 0.4-0.8 mg) cu 2-3 minute înainte de injectare

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.1 mL/kg |
        | Rată de Flux | 4-5 mL/s |
        | Durată | 20s |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Aorta ascendentă |
        | Declanșator (HU) | 200 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100-120 kV |
    | **Curent Tub (mAs)** | Auto (modulare sincronizată ECG) |
    | **Control Automat al Expunerii (AEC)** | Modulare ECG activată (pulsare conform ritmului cardiac) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 128 × 0.6 mm |
    | **Timp de Rotație** | 0.28 s |
    | **Pitch (Factor Pas)** | 0.2-0.24 |
    | **Mod Scanare** | Elicoidal sincronizat ECG (sau Secvențial prospectiv) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Tehnică de respirație non-Valsalva. Notificați în observații dacă pacientul nu poate respecta apneea. Țintă: telediastolă (70-75%) la FC < 65 bpm; telesistolă (35-45%) la FC > 80 bpm; telediastolă și telesistolă la FC intermediară.

    === "Note Asistent"

        - Linie venoasă minim 20G în plica cotului. Verificați contraindicațiile pentru metoprolol (astm sever, BAV avansat) sau nitroglicerină (stenoze aortice severe, medicație tip inhibitori PDE-5).

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic la contrast iodat

    === "Note Radiolog"

        - Calculați scorul Agatston. Acordați categoria CAD-RADS (0-5, P, N, G, V). Evaluați caracteristicile plăcii (stenoză, compoziție, remodelare pozitivă, atenuare redusă). Analizați cinetica pereților pe seriile multifazice.

    === "Sfaturi & Recomandări"

        - Pregătirea pacientului și controlul frecvenței cardiace sunt definitorii pentru calitatea examinării.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scor de Calciu | Carenă | Sub cord | 0 sec | 3 mm | Scor de calciu coronarian de referință |
    | Angio-CT Sincronizat ECG | 2 cm deasupra ostiilor coronare | 2 cm sub apexul cordului | Urmărire bolus | 0.625 mm | Angio-CT sincronizat ECG prospectiv sau retrospectiv |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Scor de Calciu | Cord | 3 mm/3 mm | Standard |  | Pentru calcularea scorului Agatston |
    | Axial | Angio-CT Sincronizat ECG | Torace | 1.5 mm/1.5 mm | Lung |  | Câmp pulmonar pentru leziuni extracardiace |
    | Axial | Angio-CT Sincronizat ECG | Cord | 0.625 mm/0.625 mm | Cardiac |  | Evaluarea nativă a lumenului coronarian |
    | 3D VR | Angio-CT Sincronizat ECG | Cord | 1 mm/1 mm | Cardiac |  | Randări 3D VR și MPR pe arborele coronarian |

## Surse și revizuire

- [SCCT / ACR-NASCI Practice Parameter for Coronary CT Angiography](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Heart.pdf) — *ACR / SCCT* (US)
- [UT Southwestern Radiology — Cardiovascular CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
