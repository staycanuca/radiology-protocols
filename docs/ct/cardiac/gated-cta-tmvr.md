---
author: Departamentul de Radiologie
category: cardiac
clinical_indications:
- Planificare pre-procedurală TMVR (implantare mitrală transcateter sau valve-in-valve)
- Insuficiență mitrală severă sau disfuncție de proteză mitrală
- Evaluarea riscului de obstrucție a tractului de ejecție ventricular stâng (LVOT)
contrast:
  agent: Isovue 370
  duration: 15s
  flow_rate: 5 mL/s
  roi: Aorta ascendentă
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 180 HU
  volume: 1.1 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: 'Măsurători specifice TMVR: geometrie inel mitral, arie neo-LVOT,
    înălțimea ostiilor coronare, volumul AS, evaluarea căilor de abord transseptal.'
  nursing: Linie venoasă 20G.
  rad: Măsurarea inelului mitral (dimensiuni septo-laterale, inter-comisurale, arie,
    perimetru). Calculul ariei estimate neo-LVOT. Proximitatea arterei circumflexe.
    Dimensiunile atriului stâng.
  tech: Angio-CT Torace sincronizat FĂRĂ MODULARE DE DOZĂ (doză completă pe tot ciclul
    cardiac pentru reconstrucții multifazice) + scanare tardivă la 80s Abdomen/Pelvis
    pentru acces vascular.
  tips: Fără modulare de doză pe torace pentru a avea calitate de imagine excelentă
    pe toate fazele diastolice și sistolice.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: HR < 65 target. Premedication not required.
protocol_type: cardiac gated
recons:
- acquisition: Scor de Calciu
  fov: Cord
  kernel: Cardiac
  notes: Evaluarea calcificării inelului mitral
  plane: Axial
  thickness_increment: 3 mm/3 mm
- acquisition: Angio-CT Torace Sincronizat
  fov: Cord
  kernel: Cardiac
  notes: Măsurători inel mitral și evaluare cuspe
  plane: Axial
  thickness_increment: 0.75 mm/0.75 mm
- acquisition: Fază Tardivă CAP
  fov: Abdomen-Pelvis
  kernel: Vascular
  notes: Evaluare vase de acces vascular periferic
  plane: Axial
  thickness_increment: 2 mm/2 mm
- acquisition: Angio-CT Torace Sincronizat
  fov: Cord
  kernel: Cardiac
  notes: Plan dublu oblic 'en face' pe inelul mitral
  plane: Double oblique
  thickness_increment: 0.75 mm/0.75 mm
- acquisition: Fază Tardivă CAP
  fov: Abdomen-Pelvis
  kernel: Vascular
  notes: Randare 3D pentru planificarea abordului
  plane: 3D VR
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 0 sec
  end: Baza cordului
  name: Scor de Calciu
  notes: Scor de calciu al inelului și foițelor mitrale
  start: Carenă
  thickness: 3 mm
- delay: Urmărire bolus
  end: Baza cordului
  name: Angio-CT Torace Sincronizat
  notes: FĂRĂ MODULARE DE DOZĂ - retrospectiv toate fazele
  start: Carenă
  thickness: 0.625 mm
- delay: 80 sec
  end: Capete femurale
  name: Fază Tardivă CAP
  notes: Planificare căi de abord și anatomie venoasă
  start: Diafragm
  thickness: 1.25 mm
slug: gated-cta-tmvr
synonyms: []
tech_params:
  aec: Modulare ECG activată (pulsare conform ritmului cardiac)
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: '100'
  mas: Fără modulare ECG torace / Auto AP
  pitch: 0.2-0.24 / 1.2-1.5
  rotation_time: 0.28 / 0.5s
  scan_mode: Elicoidal sincronizat ECG (sau Secvențial prospectiv)
  slice_thickness: 0.625 mm
title: Angio-CT Sincronizat ECG Planificare TMVR (Implantare Valvulară Mitrală Transcateter)
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

# Angio-CT Sincronizat ECG Planificare TMVR (Implantare Valvulară Mitrală Transcateter)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Scor de Calciu | 0 sec | Carenă → Baza cordului |
        | Angio-CT Torace Sincronizat | Urmărire bolus | Carenă → Baza cordului |
        | Fază Tardivă CAP | 80 sec | Diafragm → Capete femurale |

    === "Indicații Clinice"

        - Planificare pre-procedurală TMVR (implantare mitrală transcateter sau valve-in-valve)
        - Insuficiență mitrală severă sau disfuncție de proteză mitrală
        - Evaluarea riscului de obstrucție a tractului de ejecție ventricular stâng (LVOT)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular (Cord)*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - HR < 65 target. Premedication not required.

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.1 mL/kg |
        | Rată de Flux | 5 mL/s |
        | Durată | 15s |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Aorta ascendentă |
        | Declanșator (HU) | 180 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 kV |
    | **Curent Tub (mAs)** | Fără modulare ECG torace / Auto AP |
    | **Control Automat al Expunerii (AEC)** | Modulare ECG activată (pulsare conform ritmului cardiac) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 128 × 0.6 mm |
    | **Timp de Rotație** | 0.28 / 0.5 s |
    | **Pitch (Factor Pas)** | 0.2-0.24 / 1.2-1.5 |
    | **Mod Scanare** | Elicoidal sincronizat ECG (sau Secvențial prospectiv) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Angio-CT Torace sincronizat FĂRĂ MODULARE DE DOZĂ (doză completă pe tot ciclul cardiac pentru reconstrucții multifazice) + scanare tardivă la 80s Abdomen/Pelvis pentru acces vascular.

    === "Note Asistent"

        - Linie venoasă 20G.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Măsurarea inelului mitral (dimensiuni septo-laterale, inter-comisurale, arie, perimetru). Calculul ariei estimate neo-LVOT. Proximitatea arterei circumflexe. Dimensiunile atriului stâng.

    === "Sfaturi & Recomandări"

        - Fără modulare de doză pe torace pentru a avea calitate de imagine excelentă pe toate fazele diastolice și sistolice.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scor de Calciu | Carenă | Baza cordului | 0 sec | 3 mm | Scor de calciu al inelului și foițelor mitrale |
    | Angio-CT Torace Sincronizat | Carenă | Baza cordului | Urmărire bolus | 0.625 mm | FĂRĂ MODULARE DE DOZĂ - retrospectiv toate fazele |
    | Fază Tardivă CAP | Diafragm | Capete femurale | 80 sec | 1.25 mm | Planificare căi de abord și anatomie venoasă |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Scor de Calciu | Cord | 3 mm/3 mm | Cardiac |  | Evaluarea calcificării inelului mitral |
    | Axial | Angio-CT Torace Sincronizat | Cord | 0.75 mm/0.75 mm | Cardiac |  | Măsurători inel mitral și evaluare cuspe |
    | Axial | Fază Tardivă CAP | Abdomen-Pelvis | 2 mm/2 mm | Vascular |  | Evaluare vase de acces vascular periferic |
    | Double oblique | Angio-CT Torace Sincronizat | Cord | 0.75 mm/0.75 mm | Cardiac |  | Plan dublu oblic 'en face' pe inelul mitral |
    | 3D VR | Fază Tardivă CAP | Abdomen-Pelvis | 1 mm/1 mm | Vascular |  | Randare 3D pentru planificarea abordului |

## Surse și revizuire

- [SCCT / ACR-NASCI Practice Parameter for Coronary CT Angiography](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Heart.pdf) — *ACR / SCCT* (US)
- [UT Southwestern Radiology — Cardiovascular CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
