---
author: null
category: vascular
clinical_indications:
- Sindrom de pensare / încarcerare a arterei poplitee
- Durere la efort muscular la nivelul gambei la sportivi tineri fără factori de risc
  cardiovascular
- Claudicație la pacient tânăr
contrast:
  agent: Isovue 370
  duration: 18-20s + 18-20s
  flow_rate: 4 mL/s
  roi: Artera poplitee
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 150 HU
  volume: 'Injectare fracționată (duală): 1.2 mL/kg + 1.2 mL/kg'
last_updated: '2026-01-01'
notes:
  additional_recons: Comparație în paralel poziție neutră vs. flexie plantară. Randare
    3D VR demonstrând raportul mușchi-arteră poplitee.
  nursing: Linie venoasă 18-20G în plica cotului.
  rad: Comparați imaginile din poziția neutră cu cele din flexie plantară. Căutați
    compresiunea, devierea medială sau ocluzia arterei poplitee la flexia plantară.
    Evaluați raporturile anatomice cu capul medial al mușchiului gastrocnemian.
  tech: 'DOUĂ achiziții obligatorii: 1) În poziție neutră de repaus 2) Cu flexie plantară
    activă contra unei rezistențe. Ambele gambe scanate pentru comparație.'
  tips: Instruiți pacientul cum să mențină flexia plantară activă în timpul celei
    de-a doua scanări.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu membrele inferioare extinse în poziție neutră inițial
premedication: ''
protocol_type: vascular
recons:
- acquisition: Angio-CT Poziție Neutră
  fov: Genunchi-Gambă
  kernel: Vascular
  notes: Anatomie de bază a arterei poplitee și foselor poplitee
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Angio-CT Flexie Plantară
  fov: Genunchi-Gambă
  kernel: Vascular
  notes: Aprecierea compresiunii arteriale în timpul flexiei plantare
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Angio-CT Flexie Plantară
  fov: Genunchi-Gambă
  kernel: Vascular
  notes: MIP comparativ neutru vs. manevră activă
  plane: Coronal
  thickness_increment: 2 mm/2 mm
- acquisition: Angio-CT Flexie Plantară
  fov: Genunchi-Gambă
  kernel: Vascular
  notes: Vedere sagitală a fosei poplitee
  plane: Sagital
  thickness_increment: 2 mm/2 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: Urmărire bolus
  end: Gleznă
  name: Angio-CT Poziție Neutră
  notes: Ambele membre în repaus neutru
  start: Femur distal
  thickness: 0.625 mm
- delay: 40 sec
  end: Gleznă
  name: Angio-CT Tardiv Poziție Neutră
  notes: Fază venoasă poplitee
  start: Femur distal
  thickness: 1 mm
- delay: Urmărire bolus
  end: Gleznă
  name: Angio-CT Flexie Plantară
  notes: Pacientul menține flexia plantară activă a ambelor picioare
  start: Femur distal
  thickness: 0.625 mm
slug: cta-popliteal-entrapment
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '100'
  mas: Auto (referință 200 mAs)
  pitch: '0.9'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Sindrom de Încarcerare a Arterei Poplitee (Popliteal Entrapment)
---

# Angio-CT Sindrom de Încarcerare a Arterei Poplitee (Popliteal Entrapment)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Poziție Neutră | Urmărire bolus | Femur distal → Gleznă |
        | Angio-CT Tardiv Poziție Neutră | 40 sec | Femur distal → Gleznă |
        | Angio-CT Flexie Plantară | Urmărire bolus | Femur distal → Gleznă |

    === "Indicații Clinice"

        - Sindrom de pensare / încarcerare a arterei poplitee
        - Durere la efort muscular la nivelul gambei la sportivi tineri fără factori de risc cardiovascular
        - Claudicație la pacient tânăr

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular & Sistem vascular*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu membrele inferioare extinse în poziție neutră inițial
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | Injectare fracționată (duală): 1.2 mL/kg + 1.2 mL/kg |
        | Rată de Flux | 4 mL/s |
        | Durată | 18-20s + 18-20s |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Artera poplitee |
        | Declanșator (HU) | 150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 kV |
    | **Curent Tub (mAs)** | Auto (referință 200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - DOUĂ achiziții obligatorii: 1) În poziție neutră de repaus 2) Cu flexie plantară activă contra unei rezistențe. Ambele gambe scanate pentru comparație.

    === "Note Asistent"

        - Linie venoasă 18-20G în plica cotului.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Comparați imaginile din poziția neutră cu cele din flexie plantară. Căutați compresiunea, devierea medială sau ocluzia arterei poplitee la flexia plantară. Evaluați raporturile anatomice cu capul medial al mușchiului gastrocnemian.

    === "Sfaturi & Recomandări"

        - Instruiți pacientul cum să mențină flexia plantară activă în timpul celei de-a doua scanări.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Poziție Neutră | Femur distal | Gleznă | Urmărire bolus | 0.625 mm | Ambele membre în repaus neutru |
    | Angio-CT Tardiv Poziție Neutră | Femur distal | Gleznă | 40 sec | 1 mm | Fază venoasă poplitee |
    | Angio-CT Flexie Plantară | Femur distal | Gleznă | Urmărire bolus | 0.625 mm | Pacientul menține flexia plantară activă a ambelor picioare |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Poziție Neutră | Genunchi-Gambă | 1 mm/1 mm | Vascular |  | Anatomie de bază a arterei poplitee și foselor poplitee |
    | Axial | Angio-CT Flexie Plantară | Genunchi-Gambă | 1 mm/1 mm | Vascular |  | Aprecierea compresiunii arteriale în timpul flexiei plantare |
    | Coronal | Angio-CT Flexie Plantară | Genunchi-Gambă | 2 mm/2 mm | Vascular |  | MIP comparativ neutru vs. manevră activă |
    | Sagital | Angio-CT Flexie Plantară | Genunchi-Gambă | 2 mm/2 mm | Vascular |  | Vedere sagitală a fosei poplitee |
