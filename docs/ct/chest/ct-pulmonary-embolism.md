---
author: null
category: vascular
clinical_indications:
- Suspiciune de trombembolism pulmonar (TEP)
- Dispnee acută de cauză neclară
- Durere toracică cu D-dimeri crescuți
contrast:
  agent: Isovue 370
  duration: 15 - 20s
  flow_rate: 5 mL/s
  roi: Artera pulmonară principală
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 100 HU
  volume: 1.3 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții MIP ale arterelor pulmonare
  nursing: Se preferă abord venos periferic 20G sau mai mare în plica cotului. Verificați
    fluxul adecvat înainte de injectare.
  rad: Evaluați raportul VD/VS. Căutați semne de suprasolicitare a cordului drept.
    Verificați venele periferice pentru tromboză dacă au fost incluse în câmp.
  tech: Direcție de scanare caudocranială. Instruiți pacientul privind apneea inspiratorie.
    ROI în artera pulmonară principală la nivelul bifurcației.
  tips: Brațele complet ridicate pentru a reduce artefactele de atenuare a fasciculului
    (beam hardening).
npo: Repaus alimentar 2 ore recomandat
position: Decubit dorsal cu picioarele înainte și brațele ridicate
premedication: Nu este necesară
protocol_type: contrast-enhanced
recons:
- acquisition: Angiografie
  fov: Torace
  ir_strength: '3'
  kernel: Standard
  notes: Fereastră mediastinală pentru evaluarea TEP
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Angiografie
  fov: Torace
  ir_strength: '3'
  kernel: Plămân
  notes: Fereastră pulmonară pentru parenchim
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Angiografie
  fov: Torace
  ir_strength: '3'
  kernel: Standard
  notes: Vedere de ansamblu a vascularizației pulmonare
  plane: Coronal
  thickness_increment: 3 mm/3 mm
- acquisition: Angiografie
  fov: Torace
  ir_strength: '3'
  kernel: Standard
  notes: Opțional pentru corelare clinică
  plane: Sagital
  thickness_increment: 3 mm/3 mm
safety:
  allergy: Verificați istoricul de alergie la iod și reacțiile anterioare
  renal: Verificați eGFR > 30 mL/min
series:
- delay: Urmărire bolus
  end: Glande suprarenale
  name: Angiografie Pulmonară
  notes: Direcție caudocranială de la diafragm spre vârfuri
  start: Vârfuri pulmonare
  thickness: 0.625 mm
slug: ct-pulmonary-embolism
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '100'
  mas: Auto (referință 200 mAs)
  pitch: 1.0-1.2
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Trombembolism Pulmonar
---

# Angio-CT Trombembolism Pulmonar

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angiografie Pulmonară | Urmărire bolus | Vârfuri pulmonare → Glande suprarenale |

    === "Indicații Clinice"

        - Suspiciune de trombembolism pulmonar (TEP)
        - Dispnee acută de cauză neclară
        - Durere toracică cu D-dimeri crescuți

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular & Sistem vascular*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu picioarele înainte și brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 2 ore recomandat
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.3 mL/kg |
        | Rată de Flux | 5 mL/s |
        | Durată | 15 - 20s |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Artera pulmonară principală |
        | Declanșator (HU) | 100 HU |

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
    | **Pitch (Factor Pas)** | 1.0-1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Direcție de scanare caudocranială. Instruiți pacientul privind apneea inspiratorie. ROI în artera pulmonară principală la nivelul bifurcației.

    === "Note Asistent"

        - Se preferă abord venos periferic 20G sau mai mare în plica cotului. Verificați fluxul adecvat înainte de injectare.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min
            - **Alergii:** Verificați istoricul de alergie la iod și reacțiile anterioare

    === "Note Radiolog"

        - Evaluați raportul VD/VS. Căutați semne de suprasolicitare a cordului drept. Verificați venele periferice pentru tromboză dacă au fost incluse în câmp.

    === "Sfaturi & Recomandări"

        - Brațele complet ridicate pentru a reduce artefactele de atenuare a fasciculului (beam hardening).

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angiografie Pulmonară | Vârfuri pulmonare | Glande suprarenale | Urmărire bolus | 0.625 mm | Direcție caudocranială de la diafragm spre vârfuri |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angiografie | Torace | 1.25 mm/1.25 mm | Standard | 3 | Fereastră mediastinală pentru evaluarea TEP |
    | Axial | Angiografie | Torace | 2.5 mm/2.5 mm | Plămân | 3 | Fereastră pulmonară pentru parenchim |
    | Coronal | Angiografie | Torace | 3 mm/3 mm | Standard | 3 | Vedere de ansamblu a vascularizației pulmonare |
    | Sagital | Angiografie | Torace | 3 mm/3 mm | Standard | 3 | Opțional pentru corelare clinică |
