---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen
clinical_indications:
- Bilanț oncologic la pacienți cu contraindicație absolută la contrastul iodat
- Evaluare metastaze pulmonare și leziuni osoase la pacienți cu insuficiență renală
  severă
- Suspiciune de colecții lichidiene masive, ascită, hemoragii mari
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
  additional_recons: MIP pulmonar pentru noduli.
  nursing: Confort pacient.
  rad: Apreciați limitele diagnostice ale examinării fără contrast în ceea ce privește
    diferențierea leziunilor focale hepatice mici și adenopatiilor abdominale.
  tech: Scanare continuă torace, abdomen și pelvis.
  tips: Se poate asocia RMN fără contrast pentru caracterizarea leziunilor hepatice
    suspecte.
npo: N/A
position: Decubit dorsal cu brațele ridicate
premedication: Fără contrast oral iodat
protocol_type: non-contrast
recons:
- acquisition: CT CAP Nativ
  fov: Torace / Abdomen
  ir_strength: Admire 3 / AIDR 3D
  kernel: Pulmonar (I50f) + Mediastinal (I30f) + Osos (I70f)
  notes: Serii multiplanare native
  plane: Axial, Coronal & Sagital
  thickness_increment: 2.5 mm / 2.5 mm
safety:
  allergy: N/A — fără contrast
  renal: N/A — fără contrast
series:
- delay: 0 sec
  end: Simfiză pubiană
  name: CT CAP Nativ
  notes: Apnee inspiratorie completă
  start: Vârfuri pulmonare
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: CAREkV 100-120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 1.0 - 1.2
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Torace, Abdomen & Pelvis (CAP) Nativ (Protocol OHSU)
---

# CT Torace, Abdomen & Pelvis (CAP) Nativ (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT CAP Nativ | 0 sec | Vârfuri pulmonare → Simfiză pubiană |

    === "Indicații Clinice"

        - Bilanț oncologic la pacienți cu contraindicație absolută la contrastul iodat
        - Evaluare metastaze pulmonare și leziuni osoase la pacienți cu insuficiență renală severă
        - Suspiciune de colecții lichidiene masive, ascită, hemoragii mari

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** N/A
    - **Premedicație / Pregătire:**
        - Fără contrast oral iodat

-   __3. Contrast IV & Injectare__

    ---
    !!! info "Fără Contrast Intravenos"
    Acest protocol nu necesită administrare de contrast intravenos.

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | CAREkV 100-120 kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.0 - 1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare continuă torace, abdomen și pelvis.

    === "Note Asistent"

        - Confort pacient.

        !!! warning "Siguranță"
            - **Funcție Renală:** N/A — fără contrast
            - **Alergii:** N/A — fără contrast

    === "Note Radiolog"

        - Apreciați limitele diagnostice ale examinării fără contrast în ceea ce privește diferențierea leziunilor focale hepatice mici și adenopatiilor abdominale.

    === "Sfaturi & Recomandări"

        - Se poate asocia RMN fără contrast pentru caracterizarea leziunilor hepatice suspecte.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT CAP Nativ | Vârfuri pulmonare | Simfiză pubiană | 0 sec | 0.625 mm | Apnee inspiratorie completă |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial, Coronal & Sagital | CT CAP Nativ | Torace / Abdomen | 2.5 mm / 2.5 mm | Pulmonar (I50f) + Mediastinal (I30f) + Osos (I70f) | Admire 3 / AIDR 3D | Serii multiplanare native |
