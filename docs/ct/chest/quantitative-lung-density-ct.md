---
author: Departamentul de Radiologie
category: chest
clinical_indications:
- Evaluare și cuantificare emfizem pulmonar în BPOC
- Planificare tratament intervențional de reducere volum pulmonar (valve endobronșice
  / chirurgie)
- Monitorizare deficit de alfa-1 antitripsină
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
  additional_recons: Calcul procentual al scorului de emfizem pe lobi
  nursing: Fără linie venoasă.
  rad: Densitate < -950 HU pe secțiuni fine în inspir indică distrucție emfizematoasă.
    Evaluați integritatea fisurilor pulmonare.
  tech: Calibrarea scannerului CT este critică pentru densitometrie HU precisă. Volumetric
    complet în inspir profund susținut.
  tips: Pacientul nu trebuie să execute manevra Valsalva în timpul inspirului.
npo: Nu este necesar
position: Decubit dorsal cu picioarele înainte și brațele ridicate
premedication: Nu este necesară
protocol_type: chest/pulmonary
recons:
- acquisition: Densitometrie
  fov: Torace
  ir_strength: Standard
  kernel: Standard
  notes: Kernel standard pentru densitometrie cantitativă
  plane: Axial
  thickness_increment: 0.75 mm/0.5 mm
- acquisition: Parenchim
  fov: Torace
  ir_strength: '3'
  kernel: Plămân
  notes: Evaluare vizuală a parenchimului
  plane: Axial
  thickness_increment: 1.0 mm/1.0 mm
- acquisition: Parenchim
  fov: Torace
  ir_strength: '3'
  kernel: Plămân
  notes: Distribuție lobară cranio-caudală
  plane: Coronal
  thickness_increment: 2.0 mm/2.0 mm
safety:
  allergy: Nu este cazul
  renal: Nu este cazul
series:
- delay: Inspir profund
  end: Sinusuri costodiafragmatice
  name: Volumetric Nativ Densitometrie
  notes: Secțiuni izotropice fine
  start: Vârfuri pulmonare
  thickness: 0.625-1.0 mm
slug: quantitative-lung-density-ct
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 150-200 mAs)
  pitch: '1'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625-1.0 mm
title: CT Cuantificare Densitate Pulmonară (Emfizem)
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

# CT Cuantificare Densitate Pulmonară (Emfizem)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Volumetric Nativ Densitometrie | Inspir profund | Vârfuri pulmonare → Sinusuri costodiafragmatice |

    === "Indicații Clinice"

        - Evaluare și cuantificare emfizem pulmonar în BPOC
        - Planificare tratament intervențional de reducere volum pulmonar (valve endobronșice / chirurgie)
        - Monitorizare deficit de alfa-1 antitripsină

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
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | Auto (referință 150-200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625-1.0 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Calibrarea scannerului CT este critică pentru densitometrie HU precisă. Volumetric complet în inspir profund susținut.

    === "Note Asistent"

        - Fără linie venoasă.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu este cazul
            - **Alergii:** Nu este cazul

    === "Note Radiolog"

        - Densitate < -950 HU pe secțiuni fine în inspir indică distrucție emfizematoasă. Evaluați integritatea fisurilor pulmonare.

    === "Sfaturi & Recomandări"

        - Pacientul nu trebuie să execute manevra Valsalva în timpul inspirului.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Volumetric Nativ Densitometrie | Vârfuri pulmonare | Sinusuri costodiafragmatice | Inspir profund | 0.625-1.0 mm | Secțiuni izotropice fine |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Densitometrie | Torace | 0.75 mm/0.5 mm | Standard | Standard | Kernel standard pentru densitometrie cantitativă |
    | Axial | Parenchim | Torace | 1.0 mm/1.0 mm | Plămân | 3 | Evaluare vizuală a parenchimului |
    | Coronal | Parenchim | Torace | 2.0 mm/2.0 mm | Plămân | 3 | Distribuție lobară cranio-caudală |

## Surse și revizuire

- [AAPM CT Protocols — Routine Adult Chest CT](https://www.aapm.org/pubs/ctprotocols/documents/RoutineChestCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Chest Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
