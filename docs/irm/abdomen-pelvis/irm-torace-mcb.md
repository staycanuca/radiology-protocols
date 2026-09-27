---
title: IRM – Torace (MCB)
modality: irm
category: abdomen-pelvis
slug: irm-torace-mcb
author: MCB Radiology (documentul sursă)
last_updated: '2026-09-27'
tags:
- MCB Radiology
- IRM
- Body
synonyms:
- Chest
- 4 Chest
sources:
- title: 4 Chest
  url: https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/Protocols/Body/4%20Chest.pdf
  pages:
  - 1
  - 2
  consulted_on: '2026-09-27'
  relationship: Document instituțional original importat integral
provenance:
  version: mcb-mri-1c7646938537
  processing:
  - Titlu și etichete de parametri în română; textul clinic original păstrat în engleză.
  - Import PDF integral, imagini ale tuturor paginilor și extragere automată a parametrilor
    secvențelor.
sequences:
- name: T2 HASTE/SSFSE
  plane: Coronal
  fat_sat: Nu
  slice_gap: 5 mm / 1 mm
  fov_matrix: ''
  notes: 'PACS: T2 COR; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T2 HASTE/SSFSE
    pacs_name: T2 COR
    plane: cor
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1'
    first_slice: front
- name: T2 HASTE/SSFSE
  plane: Sagital
  fat_sat: Nu
  slice_gap: 5 mm / 1 mm
  fov_matrix: ''
  notes: 'PACS: T2 SAG; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T2 HASTE/SSFSE
    pacs_name: T2 SAG
    plane: sag
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1'
    first_slice: left
- name: T2 HASTE/SSFSE
  plane: Axial
  fat_sat: Nu
  slice_gap: 5 mm / 1 mm
  fov_matrix: ''
  notes: 'PACS: T2 AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T2 HASTE/SSFSE
    pacs_name: T2 AX
    plane: ax
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1'
    first_slice: top
- name: T2 HASTE/SSFSE
  plane: Axial
  fat_sat: Da
  slice_gap: 5 mm / 1 mm
  fov_matrix: ''
  notes: 'PACS: T2 FS AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T2 HASTE/SSFSE
    pacs_name: T2 FS AX
    plane: ax
    fat_sat: 'yes'
    slice_mm: '5'
    gap_mm: '1'
    first_slice: top
- name: Diffusion (b50, b400, b800, ADC)
  plane: Axial
  fat_sat: Da
  slice_gap: 7 mm / 1.4 mm
  fov_matrix: ''
  notes: 'PACS: DIFFUSION AX; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: Diffusion (b50, b400, b800, ADC)
    pacs_name: DIFFUSION AX
    plane: ax
    fat_sat: 'yes'
    slice_mm: '7'
    gap_mm: '1.4'
    first_slice: top
- name: In/Out Phase
  plane: Axial
  fat_sat: Nu
  slice_gap: 5 mm / 1 mm
  fov_matrix: ''
  notes: 'PACS: IN/OUT AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: In/Out Phase
    pacs_name: IN/OUT AX
    plane: ax
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1'
    first_slice: top
- name: T1 VIBE/LAVA
  plane: Coronal
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS PRE COR; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS PRE COR
    plane: cor
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: front
- name: T1 VIBE/LAVA
  plane: Sagital
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS PRE SAG; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS PRE SAG
    plane: sag
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: left
- name: T1 VIBE/LAVA
  plane: Axial
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS PRE AX; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS PRE AX
    plane: ax
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: top
- name: T1 VIBE/LAVA
  plane: Axial
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS 20 SEC AX; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS 20 SEC AX
    plane: ax
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: top
- name: T1 VIBE/LAVA
  plane: Axial
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS 70 SEC AX; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS 70 SEC AX
    plane: ax
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: top
- name: T1 VIBE/LAVA
  plane: Coronal
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS 2 MIN COR; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS 2 MIN COR
    plane: cor
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: front
- name: T1 VIBE/LAVA
  plane: Axial
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS 3 MIN AX; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS 3 MIN AX
    plane: ax
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: top
- name: T1 VIBE/LAVA
  plane: Sagital
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS 4 MIN SAG; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS 4 MIN SAG
    plane: sag
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: left
- name: T1 VIBE/LAVA
  plane: Axial
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS 5 MIN AX; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS 5 MIN AX
    plane: ax
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: top
- name: Cine True FISP
  plane: Coronal
  fat_sat: Nu
  slice_gap: 40 mm / 0 mm
  fov_matrix: ''
  notes: 'PACS: CINE COR TIDAL; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: Cine True FISP
    pacs_name: CINE COR TIDAL
    plane: cor
    fat_sat: 'no'
    slice_mm: '40'
    gap_mm: '0'
    first_slice: front
- name: Cine True FISP
  plane: Coronal
  fat_sat: Nu
  slice_gap: 40 mm / 0 mm
  fov_matrix: ''
  notes: 'PACS: CINE COR MAX; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: Cine True FISP
    pacs_name: CINE COR MAX
    plane: cor
    fat_sat: 'no'
    slice_mm: '40'
    gap_mm: '0'
    first_slice: front
- name: Cine True FISP
  plane: Coronal
  fat_sat: Nu
  slice_gap: 10 mm / 0 mm
  fov_matrix: ''
  notes: 'PACS: CINE COR MAX; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: Cine True FISP
    pacs_name: CINE COR MAX
    plane: cor
    fat_sat: 'no'
    slice_mm: '10'
    gap_mm: '0'
    first_slice: front
- name: Cine True FISP
  plane: Coronal
  fat_sat: Nu
  slice_gap: 10 mm / 0 mm
  fov_matrix: ''
  notes: 'PACS: CINE COR SNIFF; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: Cine True FISP
    pacs_name: CINE COR SNIFF
    plane: cor
    fat_sat: 'no'
    slice_mm: '10'
    gap_mm: '0'
    first_slice: front
---

# IRM – Torace (MCB)

[Catalog MCB](../mcb/index.md) · [Descarcă PDF-ul complet](../../assets/mcb-mri/irm-torace-mcb/protocol.pdf) · [Sursa MCB](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/Protocols/Body/4%20Chest.pdf)

Documentul MCB este disponibil integral mai jos, inclusiv notele, condițiile de utilizare a contrastului și imaginile de planificare. Textul clinic al sursei este în **engleză**; titlul și etichetele parametrilor sunt în română.

## Protocolul original

### Pagina 1

![Torace — pagina 1](../../assets/mcb-mri/irm-torace-mcb/pagina-1.png){ loading=lazy }

??? abstract "Textul paginii (engleză)"

    <div lang="en" style="white-space: pre-wrap">Updated
    06/06/26
    Reviewed
    06/06/26
    MRI Chest
    Indications: lung nodule, mass, lesion; pericardial, mediastinal, thymic, bronchogenic mass; lymphadenopathy, lung cancer
    evaluation,  tracheal / central airway evaluation, diaphragmatic dysfunction/paralysis evaluation.
    This protocol is not used for chest wall masses (use MSK protocols) or cardiac exams.
    Check with rad to see if any additional sequences are needed based on history and/or prior images.
     
    Chest FOV: supraclavicular to adrenals (top/bottom coverage), anterior to posterior subq fat (front/back coverage), 
    right to left subq fat (right/left coverage).
    Go to MRIMaster.com for a guide of proper positioning.
    slice                    
    gap                    
    Pulse Sequence
    PACS Name
    plane
    fat                   
    sat
    (mm)
    (mm)
    first                               
    slice
    T2 HASTE/SSFSE
    T2 COR
    cor
    no
    5
    1
    front
    T2 HASTE/SSFSE
    T2 SAG
    sag
    no
    5
    1
    left
    T2 HASTE/SSFSE
    T2 AX
    ax
    no
    5
    1
    top
    T2 HASTE/SSFSE
    T2 FS AX
    ax
    yes
    5
    1
    top
    Diffusion                                      
    ax
    yes
    7
    1.4
    top
    (b50, b400, b800, ADC)
    DIFFUSION AX
    In/Out Phase
    IN/OUT AX
    ax
    no
    5
    1
    top
    T1 VIBE/LAVA
    T1 FS PRE COR
    cor
    yes
    3.5
    0.6
    front
    T1 VIBE/LAVA
    T1 FS PRE SAG
    sag
    yes
    3.5
    0.6
    left
    T1 VIBE/LAVA
    T1 FS PRE AX
    ax
    yes
    3.5
    0.6
    top
    CONTRAST - 2 mL/sec standard dose gadolinium (0.2 mL/kg Clariscan or 0.1 mL/kg Gadavist) followed by 20 mL saline flush.
    T1 FS 20 SEC AX
    T1 VIBE/LAVA
    ax
    yes
    3.5
    0.6
    top
    T1 VIBE/LAVA
    T1 FS 70 SEC AX
    ax
    yes
    3.5
    0.6
    top
    T1 VIBE/LAVA
    T1 FS 2 MIN COR
    cor
    yes
    3.5
    0.6
    front
    T1 VIBE/LAVA
    T1 FS 3 MIN AX
    ax
    yes
    3.5
    0.6
    top
    T1 VIBE/LAVA
    T1 FS 4 MIN SAG
    sag
    yes
    3.5
    0.6
    left
    T1 VIBE/LAVA
    T1 FS 5 MIN AX
    ax
    yes
    3.5
    0.6
    top
    RECONS:
    axial, coronal and sagittal subtractions
    CINE IMAGING:
    Ask Radiologist if cine imaging is needed based on indication.
    For central airway / trachea evaluation, obtain coronal cine imaging at the level of the tracheal during normal breathing (image 
    for 20 secs) and another sequence during maximum inspiration and expiration (image for 20 secs). 
    Cine True FISP
    CINE COR TIDAL
    cor
    no
    40
    0
    front
    Cine True FISP
    CINE COR MAX
    cor
    no
    40
    0
    front
    For diaphragmatic dysfunction evaluation, obtain coronal cine imaging of both hemidiaphragms together approximately 
    halfway front to back during maximum inspiration and expiration (image for 20 secs) and another sequence during repetitive 
    deep sniffing (image for 20 secs). 
    Cine True FISP
    CINE COR MAX
    cor
    no
    10
    0
    front
    Cine True FISP
    CINE COR SNIFF
    cor
    no
    10
    0
    front
    </div>

### Pagina 2

![Torace — pagina 2](../../assets/mcb-mri/irm-torace-mcb/pagina-2.png){ loading=lazy }

??? abstract "Textul paginii (engleză)"

    <div lang="en" style="white-space: pre-wrap">MRI Chest
    For lung mass fixation evaluation, obtain either axial, coronal or sagittal (ask Radiologist) cine imaging at the level of the mass
    during maximum inspiration and expiration (image for 20 secs).
    Cine True FISP
    CINE
    cor
    no
    10
    0
    front
    </div>

## Parametrii secvențelor

Tabele extrase din PDF. Variantele, secvențele condiționate și momentele administrării contrastului se citesc împreună cu notele de pe pagina originală indicată.

### Tabelul 1 — pagina 1

| Secvență | Denumire PACS | Plan | Supresie grăsime | Grosime (mm) | Interval (mm) | Prima secțiune |
|---|---|---|---|---|---|---|
| T2 HASTE/SSFSE | T2 COR | Coronal | Nu | 5 | 1 | Anterior |
| T2 HASTE/SSFSE | T2 SAG | Sagital | Nu | 5 | 1 | Stânga |
| T2 HASTE/SSFSE | T2 AX | Axial | Nu | 5 | 1 | Superior |
| T2 HASTE/SSFSE | T2 FS AX | Axial | Da | 5 | 1 | Superior |
| Diffusion (b50, b400, b800, ADC) | DIFFUSION AX | Axial | Da | 7 | 1.4 | Superior |
| In/Out Phase | IN/OUT AX | Axial | Nu | 5 | 1 | Superior |
| T1 VIBE/LAVA | T1 FS PRE COR | Coronal | Da | 3.5 | 0.6 | Anterior |
| T1 VIBE/LAVA | T1 FS PRE SAG | Sagital | Da | 3.5 | 0.6 | Stânga |
| T1 VIBE/LAVA | T1 FS PRE AX | Axial | Da | 3.5 | 0.6 | Superior |
| T1 VIBE/LAVA | T1 FS 20 SEC AX | Axial | Da | 3.5 | 0.6 | Superior |
| T1 VIBE/LAVA | T1 FS 70 SEC AX | Axial | Da | 3.5 | 0.6 | Superior |
| T1 VIBE/LAVA | T1 FS 2 MIN COR | Coronal | Da | 3.5 | 0.6 | Anterior |
| T1 VIBE/LAVA | T1 FS 3 MIN AX | Axial | Da | 3.5 | 0.6 | Superior |
| T1 VIBE/LAVA | T1 FS 4 MIN SAG | Sagital | Da | 3.5 | 0.6 | Stânga |
| T1 VIBE/LAVA | T1 FS 5 MIN AX | Axial | Da | 3.5 | 0.6 | Superior |
| Cine True FISP | CINE COR TIDAL | Coronal | Nu | 40 | 0 | Anterior |
| Cine True FISP | CINE COR MAX | Coronal | Nu | 40 | 0 | Anterior |
| Cine True FISP | CINE COR MAX | Coronal | Nu | 10 | 0 | Anterior |
| Cine True FISP | CINE COR SNIFF | Coronal | Nu | 10 | 0 | Anterior |

