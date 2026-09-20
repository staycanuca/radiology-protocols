---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: chest
clinical_indications:
- 'Pneumopatii interstițiale difuze (PID / ILD: fibroză pulmonară idiopatică, sarcoidoză,
  hipersensibilitate)'
- Bronșiolită constrictivă / obliterantă și evaluare air-trapping (captare aerică)
- Bronșiectazii și boală obstructivă a căilor aeriene mici
- Evaluare afectare pulmonară în colagenoze (sclerodermie, artrită reumatoidă)
contrast:
  agent: FĂRĂ
  duration: 0s
  flow_rate: 0 mL/s
  roi: N/A
  timing: N/A
  trigger: N/A
  volume: 0 mL
last_updated: '2026-09-20'
notes:
  additional_recons: MinIP axial de 3-5 mm pentru detecția hipoatenuării în mozaic.
  nursing: Asistență respiratorie pentru pacienții dispneici.
  rad: 'Comparați densitatea parenchimului între inspir și expir: absența creșterii
    normale de densitate în expir indică obstrucție a căilor mici (air-trapping focal
    sau în mozaic).'
  tech: 'Instruiți pacientul foarte clar înainte de începerea scanării: seria 1 =
    inspirați adânc și țineți aerul; seria 2 = expirați complet aerul afară și țineți-vă
    respirația pe gol.'
  tips: Dacă se observă opacități posterioare la baze pe seria în decubit dorsal,
    o serie scurtă în decubit ventral (prone) poate diferenția atelectazia de hipoventilație
    de o fibroză subpleurală reală.
npo: N/A — protocol nativ
position: Decubit dorsal (opțional decubit ventral/prone dacă există opacități dependente
  la baze)
premedication: Fără contrast oral sau i.v.
protocol_type: non-contrast
recons:
- acquisition: HRCT Inspir & Expir
  fov: Torace
  ir_strength: Standard
  kernel: Ultra-High Resolution Lung (I70f / B80d)
  notes: Kernel de ultra-înaltă rezoluție pentru detalii interstițiale submilimetrice
  plane: Axial, Coronal & Sagital
  thickness_increment: 1.0 mm / 1.0 mm
- acquisition: HRCT Expir
  fov: Torace
  ir_strength: Standard
  kernel: Pulmonar
  notes: Reconstrucții MinIP pentru accentuarea zonelor de air-trapping hipodense
  plane: Axial
  thickness_increment: 2.0 mm / 2.0 mm MinIP
safety:
  allergy: N/A — fără contrast
  renal: N/A — fără contrast
series:
- delay: 0 sec
  end: Baza plămânilor
  name: HRCT Inspirator Volumetric
  notes: Apnee inspiratorie completă; evaluare reticulație, fagure de miere (honeycombing),
    geam mat
  start: Deasupra apexurilor
  thickness: 0.625 mm
- delay: 0 sec
  end: Baza plămânilor
  name: HRCT Expirator
  notes: Scanare în apnee expiratorie forțată completă; detectare air-trapping în
    mozaic
  start: Deasupra apexurilor
  thickness: 1.0 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: 100-120 kV
  mas: CAREDose4D (doză redusă pe seria de expir)
  pitch: 0.9 - 1.1
  rotation_time: 0.33 - 0.5 s
  scan_mode: Elicoidal volumetric de înaltă rezoluție
  slice_thickness: 0.625 mm
title: HRCT Torace Inspir & Expir (Protocol OHSU)
---

# HRCT Torace Inspir & Expir (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | HRCT Inspirator Volumetric | 0 sec | Deasupra apexurilor → Baza plămânilor |
        | HRCT Expirator | 0 sec | Deasupra apexurilor → Baza plămânilor |

    === "Indicații Clinice"

        - Pneumopatii interstițiale difuze (PID / ILD: fibroză pulmonară idiopatică, sarcoidoză, hipersensibilitate)
        - Bronșiolită constrictivă / obliterantă și evaluare air-trapping (captare aerică)
        - Bronșiectazii și boală obstructivă a căilor aeriene mici
        - Evaluare afectare pulmonară în colagenoze (sclerodermie, artrită reumatoidă)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Torace & Pulmon*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal (opțional decubit ventral/prone dacă există opacități dependente la baze)
    - **Repaus Alimentar (NPO):** N/A — protocol nativ
    - **Premedicație / Pregătire:**
        - Fără contrast oral sau i.v.

-   __3. Contrast IV & Injectare__

    ---
    !!! info "Fără Contrast Intravenos"
    Acest protocol nu necesită administrare de contrast intravenos.

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100-120 kV |
    | **Curent Tub (mAs)** | CAREDose4D (doză redusă pe seria de expir) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.33 - 0.5 s |
    | **Pitch (Factor Pas)** | 0.9 - 1.1 |
    | **Mod Scanare** | Elicoidal volumetric de înaltă rezoluție |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Instruiți pacientul foarte clar înainte de începerea scanării: seria 1 = inspirați adânc și țineți aerul; seria 2 = expirați complet aerul afară și țineți-vă respirația pe gol.

    === "Note Asistent"

        - Asistență respiratorie pentru pacienții dispneici.

        !!! warning "Siguranță"
            - **Funcție Renală:** N/A — fără contrast
            - **Alergii:** N/A — fără contrast

    === "Note Radiolog"

        - Comparați densitatea parenchimului între inspir și expir: absența creșterii normale de densitate în expir indică obstrucție a căilor mici (air-trapping focal sau în mozaic).

    === "Sfaturi & Recomandări"

        - Dacă se observă opacități posterioare la baze pe seria în decubit dorsal, o serie scurtă în decubit ventral (prone) poate diferenția atelectazia de hipoventilație de o fibroză subpleurală reală.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | HRCT Inspirator Volumetric | Deasupra apexurilor | Baza plămânilor | 0 sec | 0.625 mm | Apnee inspiratorie completă; evaluare reticulație, fagure de miere (honeycombing), geam mat |
    | HRCT Expirator | Deasupra apexurilor | Baza plămânilor | 0 sec | 1.0 mm | Scanare în apnee expiratorie forțată completă; detectare air-trapping în mozaic |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial, Coronal & Sagital | HRCT Inspir & Expir | Torace | 1.0 mm / 1.0 mm | Ultra-High Resolution Lung (I70f / B80d) | Standard | Kernel de ultra-înaltă rezoluție pentru detalii interstițiale submilimetrice |
    | Axial | HRCT Expir | Torace | 2.0 mm / 2.0 mm MinIP | Pulmonar | Standard | Reconstrucții MinIP pentru accentuarea zonelor de air-trapping hipodense |
