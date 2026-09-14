---
author: None
category: chest
clinical_indications:
- Boală a căilor aeriene mici (small airway disease)
- Pneumonită de hipersensibilitate
- Astm refractar și bronșiolită obliterantă
- Evaluare combinată interstițiu + capcană aerică
contrast:
  agent: N/A
  duration: ''
  flow_rate: ''
  roi: ''
  timing: ''
  trigger: ''
  volume: ''
last_updated: '2026-01-01'
notes:
  additional_recons: MinIP pentru evidențierea hipoatenuării în mozaic
  nursing: Fără linie venoasă. Antrenați pacientul să expire complet și să mențină
    apneea în expir.
  rad: Comparați atenuarea pulmonară inspir vs expir. Capcana aerică persistentă în
    expir indică boală obstructivă a căilor mici.
  tech: 'DOUĂ achiziții volumetrice elicoidale: 1) Inspir profund complet; 2) Expir
    complet la doză redusă.'
  tips: Faza de expir se execută cu kV și mA reduse pentru radioprotecție.
npo: Nu este necesar
position: Decubit dorsal cu brațele ridicate
premedication: Nu este necesară
protocol_type: chest/pulmonary
recons:
- acquisition: Inspir
  fov: Torace
  ir_strength: '3'
  kernel: Plămân
  notes: Parenchim inspir
  plane: Axial
  thickness_increment: 1.0 mm/0.8 mm
- acquisition: Expir
  fov: Torace
  ir_strength: '3'
  kernel: Plămân
  notes: Parenchim expir
  plane: Axial
  thickness_increment: 1.0 mm/0.8 mm
- acquisition: Inspir
  fov: Torace
  ir_strength: '3'
  kernel: Plămân
  notes: Coronal inspir
  plane: Coronal
  thickness_increment: 2.0 mm/2.0 mm
safety:
  allergy: Nu este cazul
  renal: Nu este cazul
series:
- delay: Inspir
  end: Sinusuri costodiafragmatice
  name: Volum Inspir Complet
  notes: Achiziție volumetrică continuă
  start: Vârfuri pulmonare
  thickness: 1.0 mm
- delay: Expir complet
  end: Sinusuri costodiafragmatice
  name: Volum Expir Complet (Doză Redusă)
  notes: Doză joasă pentru capcană aerică
  start: Vârfuri pulmonare
  thickness: 1.0 mm
slug: volumetric-hrct-2-respiratory-phases
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 150-200 mAs)
  pitch: '1'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 1.0 mm
title: HRCT Volumetric 2 Faze Respiratorii (Inspir/Expir)
sources:
- title: AAPM CT Protocols — Routine Adult Chest CT
  url: https://www.aapm.org/pubs/ctprotocols/documents/RoutineChestCT.pdf
  institution: AAPM
  source_region: US
  kind: Protocol tehnic standardizat
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: bec845e0b9aa0e1fbdd4cdc56ff2a4bb55e22590ee1e2f9b7329c8b90b876734
- title: UT Southwestern Radiology — CT Chest Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# HRCT Volumetric 2 Faze Respiratorii (Inspir/Expir)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Volum Inspir Complet | Inspir | Vârfuri pulmonare → Sinusuri costodiafragmatice |
        | Volum Expir Complet (Doză Redusă) | Expir complet | Vârfuri pulmonare → Sinusuri costodiafragmatice |

    === "Indicații Clinice"

        - Boală a căilor aeriene mici (small airway disease)
        - Pneumonită de hipersensibilitate
        - Astm refractar și bronșiolită obliterantă
        - Evaluare combinată interstițiu + capcană aerică

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Torace & Pulmon*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Nu este necesar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    !!! info "Fără Contrast Intravenos"
    Acest protocol nu necesită administrare de contrast intravenos.

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | Auto (referință 150-200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 1.0 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - DOUĂ achiziții volumetrice elicoidale: 1) Inspir profund complet; 2) Expir complet la doză redusă.

    === "Note Asistent"

        - Fără linie venoasă. Antrenați pacientul să expire complet și să mențină apneea în expir.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu este cazul
            - **Alergii:** Nu este cazul

    === "Note Radiolog"

        - Comparați atenuarea pulmonară inspir vs expir. Capcana aerică persistentă în expir indică boală obstructivă a căilor mici.

    === "Sfaturi & Recomandări"

        - Faza de expir se execută cu kV și mA reduse pentru radioprotecție.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Volum Inspir Complet | Vârfuri pulmonare | Sinusuri costodiafragmatice | Inspir | 1.0 mm | Achiziție volumetrică continuă |
    | Volum Expir Complet (Doză Redusă) | Vârfuri pulmonare | Sinusuri costodiafragmatice | Expir complet | 1.0 mm | Doză joasă pentru capcană aerică |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Inspir | Torace | 1.0 mm/0.8 mm | Plămân | 3 | Parenchim inspir |
    | Axial | Expir | Torace | 1.0 mm/0.8 mm | Plămân | 3 | Parenchim expir |
    | Coronal | Inspir | Torace | 2.0 mm/2.0 mm | Plămân | 3 | Coronal inspir |

## Surse și revizuire

- [AAPM CT Protocols — Routine Adult Chest CT](https://www.aapm.org/pubs/ctprotocols/documents/RoutineChestCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Chest Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
