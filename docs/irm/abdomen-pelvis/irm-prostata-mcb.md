---
title: IRM – Prostată (MCB)
modality: irm
category: abdomen-pelvis
slug: irm-prostata-mcb
author: MCB Radiology (documentul sursă)
last_updated: '2026-09-27'
tags:
- MCB Radiology
- IRM
- Body
synonyms:
- Prostate
- 16 Prostate
sources:
- title: 16 Prostate
  url: https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/Protocols/Body/16%20Prostate.pdf
  pages:
  - 1
  - 2
  consulted_on: '2026-09-27'
  relationship: Document instituțional original importat integral
provenance:
  version: mcb-mri-5012fb9d7cb6
  processing:
  - Titlu și etichete de parametri în română; textul clinic original păstrat în engleză.
  - Import PDF integral, imagini ale tuturor paginilor și extragere automată a parametrilor
    secvențelor.
sequences:
- name: T2 TSE
  plane: Sagital
  fat_sat: Nu
  slice_gap: 3 mm / 0 mm
  fov_matrix: prostate & seminal vesicles
  notes: 'PACS: T2 SAG; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T2 TSE
    pacs_name: T2 SAG
    plane: sag
    fat_sat: 'no'
    slice_mm: '3'
    gap_mm: '0'
    first_slice: left
    fov_matrix: prostate & seminal vesicles
- name: T2 TSE
  plane: obl ax
  fat_sat: Nu
  slice_gap: 3 mm / 0 mm
  fov_matrix: ''
  notes: 'PACS: T2 OBL AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T2 TSE
    pacs_name: T2 OBL AX
    plane: obl ax
    fat_sat: 'no'
    slice_mm: '3'
    gap_mm: '0'
    first_slice: top
    fov_matrix: ''
- name: T2 TSE
  plane: obl cor
  fat_sat: Nu
  slice_gap: 3 mm / 0 mm
  fov_matrix: ''
  notes: 'PACS: T2S OBL COR; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: T2 TSE
    pacs_name: T2S OBL COR
    plane: obl cor
    fat_sat: 'no'
    slice_mm: '3'
    gap_mm: '0'
    first_slice: cor
    fov_matrix: ''
- name: Diffusion (b50, b800, b1400, ADC)
  plane: obl ax
  fat_sat: Da
  slice_gap: 6 mm / 1 mm
  fov_matrix: ''
  notes: 'PACS: DIFFUSION OBL AX; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: Diffusion (b50, b800, b1400, ADC)
    pacs_name: DIFFUSION OBL AX
    plane: obl ax
    fat_sat: 'yes'
    slice_mm: '6'
    gap_mm: '1'
    first_slice: top
    fov_matrix: ''
- name: T2 HASTE/SSFSE
  plane: Axial
  fat_sat: Nu
  slice_gap: 7 mm / 1.4 mm
  fov_matrix: full pelvis
  notes: 'PACS: T2 AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T2 HASTE/SSFSE
    pacs_name: T2 AX
    plane: ax
    fat_sat: 'no'
    slice_mm: '7'
    gap_mm: '1.4'
    first_slice: top
    fov_matrix: full pelvis
- name: T2 HASTE/SSFSE
  plane: Axial
  fat_sat: Da
  slice_gap: 7 mm / 1.4 mm
  fov_matrix: ''
  notes: 'PACS: T2 FS AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T2 HASTE/SSFSE
    pacs_name: T2 FS AX
    plane: ax
    fat_sat: 'yes'
    slice_mm: '7'
    gap_mm: '1.4'
    first_slice: top
    fov_matrix: ''
- name: T1 TSE
  plane: Axial
  fat_sat: Nu
  slice_gap: 8 mm / 2 mm
  fov_matrix: ''
  notes: 'PACS: T1 AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T1 TSE
    pacs_name: T1 AX
    plane: ax
    fat_sat: 'no'
    slice_mm: '8'
    gap_mm: '2'
    first_slice: top
    fov_matrix: ''
- name: T1 VIBE/LAVA
  plane: Axial
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS PRE; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS PRE
    plane: ax
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: top
    fov_matrix: ''
- name: '*T1 VIBE/LAVA'
  plane: obl ax
  fat_sat: Da
  slice_gap: 3 mm / 0 mm
  fov_matrix: prostate & seminal vesicles
  notes: 'PACS: T1 FS DYNAMIC; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: '*T1 VIBE/LAVA'
    pacs_name: T1 FS DYNAMIC
    plane: obl ax
    fat_sat: 'yes'
    slice_mm: '3'
    gap_mm: '0'
    first_slice: top
    fov_matrix: prostate & seminal vesicles
- name: T1 VIBE/LAVA
  plane: Axial
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: full pelvis
  notes: 'PACS: T1 FS POST AX; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS POST AX
    plane: ax
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: top
    fov_matrix: full pelvis
- name: T1 VIBE/LAVA
  plane: Sagital
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS POST SAG; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS POST SAG
    plane: sag
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: left
    fov_matrix: ''
- name: T1 VIBE/LAVA
  plane: Coronal
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS POST COR; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS POST COR
    plane: cor
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: front
    fov_matrix: ''
---

# IRM – Prostată (MCB)

[Catalog MCB](../mcb/index.md) · [Descarcă PDF-ul complet](../../assets/mcb-mri/irm-prostata-mcb/protocol.pdf) · [Sursa MCB](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/Protocols/Body/16%20Prostate.pdf)

Documentul MCB este disponibil integral mai jos, inclusiv notele, condițiile de utilizare a contrastului și imaginile de planificare. Textul clinic al sursei este în **engleză**; titlul și etichetele parametrilor sunt în română.

## Protocolul original

### Pagina 1

![Prostată — pagina 1](../../assets/mcb-mri/irm-prostata-mcb/pagina-1.png){ loading=lazy }

??? abstract "Textul paginii (engleză)"

    <div lang="en" style="white-space: pre-wrap">Updated
    11/04/23
    MRI Prostate
    Reviewed
    05/14/25
    Indications: prostate cancer and other prostate issues.
    Full Pelvis FOV: Iliac crests to few slices below introitus/anus (top/bottom coverage), greater trochanter to 
    greater trochanter (right/left coverage), anterior pelvic wall skin to posterior buttock skin (front/back coverage).
    Prostate FOV: cover few slices beyond prostate and seminal vesicles in every plane.
    T2 TSE: FOV 12-20 cm, in plane resolution ≤0.7 mm (phase) x ≤0.4 mm (frequency)
    DWI: FOV 16-22 cm, in plane resolution ≤2.5 mm (phase) x ≤2.5 mm (frequency), TE ≤90 msec, TR ≥3000 msec
    Dynamic T1 post: FOV 12-20 cm, in plane resolution ≤2 mm (phase) x ≤2 mm (frequency), TE &lt;5 msec, TR &lt;100 msec
    Go to MRIMaster.com for a guide of proper positioning.
    slice                    
    gap                    
    Field of View
    Pulse Sequence
    PACS Name
    plane
    fat                   
    sat
    (mm)
    (mm)
    first                               
    slice
    GLUCAGON - 1 mg slow IV push just before beginning imaging.
    T2 TSE
    T2 SAG
    sag
    no
    3
    0
    left
    T2 TSE
    T2 OBL AX
    obl ax
    no
    3
    0
    top
    prostate &amp;                                
    T2 TSE
    T2S OBL COR
    obl cor
    no
    3
    0
    cor
    seminal vesicles
    Diffusion                                      
    obl ax
    yes
    6
    1
    top
    (b50, b800, b1400, ADC)
    DIFFUSION OBL AX
    T2 HASTE/SSFSE
    T2 AX
    ax
    no
    7
    1.4
    top
    T2 HASTE/SSFSE
    T2 FS AX
    ax
    yes
    7
    1.4
    top
    full pelvis
    T1 TSE
    T1 AX
    ax
    no
    8
    2
    top
    T1 VIBE/LAVA
    T1 FS PRE
    ax
    yes
    3.5
    0.6
    top
    GLUCAGON - 1 mg slow IV push just before giving IV contrast.
    CONTRAST - 2 mL/sec standard dose gadolinium (0.2 mL/kg Clariscan or 0.1 mL/kg Gadavist) followed by 20 mL saline flush. 
    *T1 VIBE/LAVA
    T1 FS DYNAMIC
    prostate &amp; seminal vesicles
    obl ax
    yes
    3
    0
    top
    T1 VIBE/LAVA
    T1 FS POST AX
    ax
    yes
    3.5
    0.6
    top
    T1 VIBE/LAVA
    T1 FS POST SAG
    full pelvis
    sag
    yes
    3.5
    0.6
    left
    T1 VIBE/LAVA
    T1 FS POST COR
    cor
    yes
    3.5
    0.6
    front
    *Dynamic post contrast phase is axial block every 7-10 secs beginning at injection and continuing for 2-3 mins
    (similar to the dynamics in pituitary MR).
    RECONS:
    axial subtractions of the dynamic phases and axial whole pelvis
    </div>

### Pagina 2

![Prostată — pagina 2](../../assets/mcb-mri/irm-prostata-mcb/pagina-2.png){ loading=lazy }

??? abstract "Textul paginii (engleză)"

    <div lang="en" style="white-space: pre-wrap">MRI Prostate
    oblique axial angulation (perpendicular to the long axis of the prostate in the sagittal plane)
    oblique coronal angulation (perpendicular to the long axis of the prostate in the sagittal plane)
    </div>

## Parametrii secvențelor

Tabele extrase din PDF. Variantele, secvențele condiționate și momentele administrării contrastului se citesc împreună cu notele de pe pagina originală indicată.

### Tabelul 1 — pagina 1

| Secvență | Denumire PACS | Plan | Supresie grăsime | Grosime (mm) | Interval (mm) | Prima secțiune | FOV |
|---|---|---|---|---|---|---|---|
| T2 TSE | T2 SAG | Sagital | Nu | 3 | 0 | Stânga | prostate &amp; seminal vesicles |
| T2 TSE | T2 OBL AX | obl ax | Nu | 3 | 0 | Superior |  |
| T2 TSE | T2S OBL COR | obl cor | Nu | 3 | 0 | Coronal |  |
| Diffusion (b50, b800, b1400, ADC) | DIFFUSION OBL AX | obl ax | Da | 6 | 1 | Superior |  |
| T2 HASTE/SSFSE | T2 AX | Axial | Nu | 7 | 1.4 | Superior | full pelvis |
| T2 HASTE/SSFSE | T2 FS AX | Axial | Da | 7 | 1.4 | Superior |  |
| T1 TSE | T1 AX | Axial | Nu | 8 | 2 | Superior |  |
| T1 VIBE/LAVA | T1 FS PRE | Axial | Da | 3.5 | 0.6 | Superior |  |
| *T1 VIBE/LAVA | T1 FS DYNAMIC | obl ax | Da | 3 | 0 | Superior | prostate &amp; seminal vesicles |
| T1 VIBE/LAVA | T1 FS POST AX | Axial | Da | 3.5 | 0.6 | Superior | full pelvis |
| T1 VIBE/LAVA | T1 FS POST SAG | Sagital | Da | 3.5 | 0.6 | Stânga |  |
| T1 VIBE/LAVA | T1 FS POST COR | Coronal | Da | 3.5 | 0.6 | Anterior |  |

