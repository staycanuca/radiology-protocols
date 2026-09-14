---
author: Departamentul de Radiologie
category: chest
clinical_indications:
- Diferențierea atelectaziilor posterioare dependente de fibroza subpleurală precoce
- Suspiciune de azbestoză sau expunere profesională
- Confirmare pattern UIP incipient
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
  additional_recons: Filtru osos de înaltă rezoluție
  nursing: Asigurați confortul pacientului în decubit ventral; atenție la respirație.
  rad: Dacă opacitățile subpleurale posterioare dispar în procubitus, ele reprezintă
    atelectazii dependente, nu fibroză.
  tech: Pacient poziționat pe burtă (procubitus). Secțiuni axiale secvențiale (non-volumetrice)
    la intervale de 10-20 mm.
  tips: Sprijiniți capul și umerii pentru stabilitate optimă.
npo: Nu este necesar
position: Decubit ventral (procubitus) cu brațele ridicate
premedication: Nu este necesară
protocol_type: chest/pulmonary
recons:
- acquisition: HRCT Procubitus
  fov: Torace
  ir_strength: '3'
  kernel: Înaltă rezoluție
  notes: Fereastră pulmonară de înaltă rezoluție
  plane: Axial
  thickness_increment: 1.0 mm secvențial
safety:
  allergy: Nu este cazul
  renal: Nu este cazul
series:
- delay: Imediat
  end: Baze pulmonare
  name: HRCT Secvențial Procubitus
  notes: Scanare secvențială intermitentă
  start: Vârfuri pulmonare
  thickness: 1.0 mm
slug: non-volumetric-hrct-1-phase-prone
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Doză redusă (referință 100-150 mAs)
  pitch: N/A
  rotation_time: Sequentials
  scan_mode: Secvențial în procubitus (Axial 1 mm)
  slice_thickness: 1.0 mm
title: HRCT Non-Volumetric 1 Fază în Decubit Ventral (Procubitus)
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

# HRCT Non-Volumetric 1 Fază în Decubit Ventral (Procubitus)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | HRCT Secvențial Procubitus | Imediat | Vârfuri pulmonare → Baze pulmonare |

    === "Indicații Clinice"

        - Diferențierea atelectaziilor posterioare dependente de fibroza subpleurală precoce
        - Suspiciune de azbestoză sau expunere profesională
        - Confirmare pattern UIP incipient

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Torace & Pulmon*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit ventral (procubitus) cu brațele ridicate
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
    | **Curent Tub (mAs)** | Doză redusă (referință 100-150 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 1.0 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | Sequential s |
    | **Pitch (Factor Pas)** | N/A |
    | **Mod Scanare** | Secvențial în procubitus (Axial 1 mm) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Pacient poziționat pe burtă (procubitus). Secțiuni axiale secvențiale (non-volumetrice) la intervale de 10-20 mm.

    === "Note Asistent"

        - Asigurați confortul pacientului în decubit ventral; atenție la respirație.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu este cazul
            - **Alergii:** Nu este cazul

    === "Note Radiolog"

        - Dacă opacitățile subpleurale posterioare dispar în procubitus, ele reprezintă atelectazii dependente, nu fibroză.

    === "Sfaturi & Recomandări"

        - Sprijiniți capul și umerii pentru stabilitate optimă.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | HRCT Secvențial Procubitus | Vârfuri pulmonare | Baze pulmonare | Imediat | 1.0 mm | Scanare secvențială intermitentă |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | HRCT Procubitus | Torace | 1.0 mm secvențial | Înaltă rezoluție | 3 | Fereastră pulmonară de înaltă rezoluție |

## Surse și revizuire

- [AAPM CT Protocols — Routine Adult Chest CT](https://www.aapm.org/pubs/ctprotocols/documents/RoutineChestCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Chest Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
