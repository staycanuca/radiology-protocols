---
author: Departamentul de Radiologie
category: chest
clinical_indications:
- Urmărire nodul pulmonar solid/subsolid cunoscut
- Screening cancer pulmonar la pacienți eligibili
- Pacienți tineri care necesită scanări repetate de control
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
  additional_recons: Reconstrucții MIP și volumetrie automată dacă este disponibil
    software dedicat
  nursing: Fără linie venoasă necesară.
  rad: Comparați dimensiunile și volumetria nodulului cu examinarea anterioară conform
    ghidurilor Fleischner.
  tech: Scanare în apnee inspiratorie completă. Utilizați protocoale specifice de
    doză ultra-redusă (ULD) cu reconstrucție iterativă avansată.
  tips: Asigurați-vă că pacientul menține apneea corect pentru a evita artefactele
    de mișcare care pot mima creșterea nodulilor.
npo: Nu este necesar
position: Decubit dorsal cu picioarele înainte și brațele ridicate
premedication: Nu este necesară
protocol_type: chest/pulmonary
recons:
- acquisition: Nativ ULD
  fov: Torace
  ir_strength: '5'
  kernel: Plămân
  notes: Fereastră pulmonară
  plane: Axial
  thickness_increment: 1.0 mm/0.8 mm
- acquisition: Nativ ULD
  fov: Torace
  ir_strength: '5'
  kernel: Standard
  notes: Fereastră mediastinală
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Nativ ULD
  fov: Torace
  ir_strength: '5'
  kernel: Plămân
  notes: Fereastră pulmonară
  plane: Coronal
  thickness_increment: 2.0 mm/2.0 mm
- acquisition: Nativ ULD
  fov: Torace
  ir_strength: '5'
  kernel: Plămân
  notes: Fereastră pulmonară
  plane: Sagital
  thickness_increment: 2.0 mm/2.0 mm
safety:
  allergy: Nu este cazul
  renal: Nu este cazul
series:
- delay: Imediat
  end: Sinusuri costodiafragmatice
  name: Torace Nativ Doză Ultra-Redusă
  notes: Protocol ultra-low dose
  start: Vârfuri pulmonare
  thickness: 1.0 mm
slug: non-contrast-chest-lung-nodule-ultra-low-dose
synonyms: []
tech_params:
  aec: Activat (Protocol doză redusă / Ultra low-dose)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '100'
  mas: Doză ultra-redusă (referință 20-30 mAs)
  pitch: 1.0-1.2
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 1.0 mm
title: CT Torace Nativ Doză Ultra-Redusă (Nodul Pulmonar)
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

# CT Torace Nativ Doză Ultra-Redusă (Nodul Pulmonar)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Torace Nativ Doză Ultra-Redusă | Imediat | Vârfuri pulmonare → Sinusuri costodiafragmatice |

    === "Indicații Clinice"

        - Urmărire nodul pulmonar solid/subsolid cunoscut
        - Screening cancer pulmonar la pacienți eligibili
        - Pacienți tineri care necesită scanări repetate de control

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Torace & Pulmon*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu picioarele înainte și brațele ridicate
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
    | **Tensiune Tub (kV)** | 100 kV |
    | **Curent Tub (mAs)** | Doză ultra-redusă (referință 20-30 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Protocol doză redusă / Ultra low-dose) |
    | **Grosime Secțiune Achiziție (Slice)** | 1.0 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.0-1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare în apnee inspiratorie completă. Utilizați protocoale specifice de doză ultra-redusă (ULD) cu reconstrucție iterativă avansată.

    === "Note Asistent"

        - Fără linie venoasă necesară.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu este cazul
            - **Alergii:** Nu este cazul

    === "Note Radiolog"

        - Comparați dimensiunile și volumetria nodulului cu examinarea anterioară conform ghidurilor Fleischner.

    === "Sfaturi & Recomandări"

        - Asigurați-vă că pacientul menține apneea corect pentru a evita artefactele de mișcare care pot mima creșterea nodulilor.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Torace Nativ Doză Ultra-Redusă | Vârfuri pulmonare | Sinusuri costodiafragmatice | Imediat | 1.0 mm | Protocol ultra-low dose |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Nativ ULD | Torace | 1.0 mm/0.8 mm | Plămân | 5 | Fereastră pulmonară |
    | Axial | Nativ ULD | Torace | 2.5 mm/2.5 mm | Standard | 5 | Fereastră mediastinală |
    | Coronal | Nativ ULD | Torace | 2.0 mm/2.0 mm | Plămân | 5 | Fereastră pulmonară |
    | Sagital | Nativ ULD | Torace | 2.0 mm/2.0 mm | Plămân | 5 | Fereastră pulmonară |

## Surse și revizuire

- [AAPM CT Protocols — Routine Adult Chest CT](https://www.aapm.org/pubs/ctprotocols/documents/RoutineChestCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Chest Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
