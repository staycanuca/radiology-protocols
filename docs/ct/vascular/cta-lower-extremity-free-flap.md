---
author: null
category: vascular
clinical_indications:
- Planificare pre-operatorie pentru recoltare de lambou liber (fibulă, lambou anterolateral
  de coapsă - ALT)
- Reconstrucție maxilofacială sau a membrelor după rezecții oncologice/traumă
contrast:
  agent: Isovue 370
  duration: 25s
  flow_rate: 4-5 mL/s
  roi: Artera femurală
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 150 HU
  volume: 1.5 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții MPR curbate ale vaselor principale. Măsurarea distanțelor
    perforatoarelor față de reperele osoase (trohanter mare, rotulă, capul fibulei).
  nursing: Linie venoasă 18-20G.
  rad: Cartografiați ramurile perforatoare septocutanate și musculocutanate. Măsurați
    calibrul și lungimea pediculului vascular. Identificați pediculul dominant. Notați
    variantele anatomice ale arterelor gambei (trifurcație, hipoplazii).
  tech: Scanare de la nivelul crestei iliace până la gleznă. Focus pe perforatoarele
    din regiunea de interes (coapsă sau gambă). Faza arterială este critică pentru
    cartografiere.
  tips: Membrele inferioare drepte, fără rotație internă/externă. Marcați tegumentul
    la nivelul regiunii de interes dacă este posibil.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu membrele inferioare extinse
premedication: ''
protocol_type: vascular
recons:
- acquisition: Angio-CT Arterial
  fov: Membre inferioare
  kernel: Vascular
  notes: Secțiuni fine pentru identificarea perforatoarelor
  plane: Axial
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: Angio-CT Arterial
  fov: Membre inferioare
  kernel: Vascular
  notes: MIP pentru evidențierea traiectului vascular complet
  plane: Coronal
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Angio-CT Arterial
  fov: Membre inferioare
  kernel: Vascular
  notes: Vederi sagitale ale perforatoarelor
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: Urmărire bolus
  end: Degete picioare
  name: Angio-CT Arterial
  notes: Bilateral pentru comparație și analiza variantelor
  start: Mijlocul coapsei
  thickness: 0.625 mm
- delay: 60 sec
  end: Degete picioare
  name: Angio-CT Tardiv
  notes: Fază venoasă pentru pediculul comitant
  start: Mijlocul coapsei
  thickness: 1 mm
slug: cta-lower-extremity-free-flap
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
title: Angio-CT Planificare Lambou Liber Membru Inferior (Fibulă / ALT)
---

# Angio-CT Planificare Lambou Liber Membru Inferior (Fibulă / ALT)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Arterial | Urmărire bolus | Mijlocul coapsei → Degete picioare |
        | Angio-CT Tardiv | 60 sec | Mijlocul coapsei → Degete picioare |

    === "Indicații Clinice"

        - Planificare pre-operatorie pentru recoltare de lambou liber (fibulă, lambou anterolateral de coapsă - ALT)
        - Reconstrucție maxilofacială sau a membrelor după rezecții oncologice/traumă

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular & Sistem vascular*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu membrele inferioare extinse
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.5 mL/kg |
        | Rată de Flux | 4-5 mL/s |
        | Durată | 25s |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Artera femurală |
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

        - Scanare de la nivelul crestei iliace până la gleznă. Focus pe perforatoarele din regiunea de interes (coapsă sau gambă). Faza arterială este critică pentru cartografiere.

    === "Note Asistent"

        - Linie venoasă 18-20G.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Cartografiați ramurile perforatoare septocutanate și musculocutanate. Măsurați calibrul și lungimea pediculului vascular. Identificați pediculul dominant. Notați variantele anatomice ale arterelor gambei (trifurcație, hipoplazii).

    === "Sfaturi & Recomandări"

        - Membrele inferioare drepte, fără rotație internă/externă. Marcați tegumentul la nivelul regiunii de interes dacă este posibil.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Arterial | Mijlocul coapsei | Degete picioare | Urmărire bolus | 0.625 mm | Bilateral pentru comparație și analiza variantelor |
    | Angio-CT Tardiv | Mijlocul coapsei | Degete picioare | 60 sec | 1 mm | Fază venoasă pentru pediculul comitant |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Arterial | Membre inferioare | 0.625 mm/0.625 mm | Vascular |  | Secțiuni fine pentru identificarea perforatoarelor |
    | Coronal | Angio-CT Arterial | Membre inferioare | 1.5 mm/1.5 mm | Vascular |  | MIP pentru evidențierea traiectului vascular complet |
    | Sagital | Angio-CT Arterial | Membre inferioare | 1.5 mm/1.5 mm | Vascular |  | Vederi sagitale ale perforatoarelor |
