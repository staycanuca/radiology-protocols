---
title: IRM – Creier de rutină și AVC rapid (MCB)
modality: irm
category: neuro
slug: irm-creier-de-rutina-si-avc-rapid-mcb
author: MCB Radiology (documentul sursă)
last_updated: '2026-09-27'
tags:
- MCB Radiology
- IRM
- Neuro
synonyms:
- Routine
- Fast Stroke
- 1 Brain Routine
sources:
- title: 1 Brain Routine
  url: https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/Protocols/Neuro/1%20Brain%20Routine.pdf
  pages:
  - 1
  consulted_on: '2026-09-27'
  relationship: Document instituțional original importat integral
provenance:
  version: mcb-mri-4571b3d3d0f5
  processing:
  - Titlu și etichete de parametri în română; textul clinic original păstrat în engleză.
  - Import PDF integral, imagini ale tuturor paginilor și extragere automată a parametrilor
    secvențelor.
sequences:
- name: T1
  plane: Sagital
  fat_sat: Nu
  slice_gap: 5 mm / 2 mm
  fov_matrix: ''
  notes: 'PACS: T1 SAG; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T1
    pacs_name: T1 SAG
    plane: sag
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '2'
    first_slice: left
- name: T2
  plane: Axial
  fat_sat: Da
  slice_gap: 5 mm / 1.5 mm
  fov_matrix: ''
  notes: 'PACS: T2 FS AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T2
    pacs_name: T2 FS AX
    plane: ax
    fat_sat: 'yes'
    slice_mm: '5'
    gap_mm: '1.5'
    first_slice: base
- name: T1
  plane: Axial
  fat_sat: Nu
  slice_gap: 5 mm / 1.5 mm
  fov_matrix: ''
  notes: 'PACS: T1 AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T1
    pacs_name: T1 AX
    plane: ax
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1.5'
    first_slice: base
- name: '*T1'
  plane: Coronal
  fat_sat: Nu
  slice_gap: 5 mm / 1.5 mm
  fov_matrix: ''
  notes: 'PACS: T1 COR; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: '*T1'
    pacs_name: T1 COR
    plane: cor
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1.5'
    first_slice: back
- name: FLAIR
  plane: Axial
  fat_sat: Nu
  slice_gap: 5 mm / 1.5 mm
  fov_matrix: ''
  notes: 'PACS: FLAIR AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: FLAIR
    pacs_name: FLAIR AX
    plane: ax
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1.5'
    first_slice: base
- name: '**SWI'
  plane: Axial
  fat_sat: Nu
  slice_gap: 5 mm / 1.5 mm
  fov_matrix: ''
  notes: 'PACS: SWI AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: '**SWI'
    pacs_name: SWI AX
    plane: ax
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1.5'
    first_slice: base
- name: DWI
  plane: Axial
  fat_sat: Da
  slice_gap: 5 mm / 1.5 mm
  fov_matrix: ''
  notes: 'PACS: DWI AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: DWI
    pacs_name: DWI AX
    plane: ax
    fat_sat: 'yes'
    slice_mm: '5'
    gap_mm: '1.5'
    first_slice: base
- name: T1
  plane: Axial
  fat_sat: Nu
  slice_gap: 5 mm / 1.5 mm
  fov_matrix: ''
  notes: 'PACS: T1 POST AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T1
    pacs_name: T1 POST AX
    plane: ax
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1.5'
    first_slice: base
- name: T1
  plane: Coronal
  fat_sat: Nu
  slice_gap: 5 mm / 1.5 mm
  fov_matrix: ''
  notes: 'PACS: T1 POST COR; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: T1
    pacs_name: T1 POST COR
    plane: cor
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1.5'
    first_slice: back
- name: T1
  plane: Sagital
  fat_sat: Nu
  slice_gap: 5 mm / 2 mm
  fov_matrix: ''
  notes: 'PACS: T1 POST SAG; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: T1
    pacs_name: T1 POST SAG
    plane: sag
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '2'
    first_slice: left
- name: '***3D T1 FSPGR/MPRAGE'
  plane: Axial
  fat_sat: Nu
  slice_gap: 1 mm / none
  fov_matrix: ''
  notes: 'PACS: AX THINS; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: '***3D T1 FSPGR/MPRAGE'
    pacs_name: AX THINS
    plane: ax
    fat_sat: 'no'
    slice_mm: '1'
    gap_mm: none
    first_slice: base
- name: FLAIR
  plane: Axial
  fat_sat: Nu
  slice_gap: 5 mm / 1.5 mm
  fov_matrix: ''
  notes: 'PACS: FLAIR AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: FLAIR
    pacs_name: FLAIR AX
    plane: ax
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1.5'
    first_slice: base
- name: '**SWI'
  plane: Axial
  fat_sat: Nu
  slice_gap: 5 mm / 1.5 mm
  fov_matrix: ''
  notes: 'PACS: SWI AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: '**SWI'
    pacs_name: SWI AX
    plane: ax
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1.5'
    first_slice: base
- name: DWI
  plane: Axial
  fat_sat: Da
  slice_gap: 5 mm / 1.5 mm
  fov_matrix: ''
  notes: 'PACS: DWI AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: DWI
    pacs_name: DWI AX
    plane: ax
    fat_sat: 'yes'
    slice_mm: '5'
    gap_mm: '1.5'
    first_slice: base
---

# IRM – Creier de rutină și AVC rapid (MCB)

[Catalog MCB](../mcb/index.md) · [Descarcă PDF-ul complet](../../assets/mcb-mri/irm-creier-de-rutina-si-avc-rapid-mcb/protocol.pdf) · [Sursa MCB](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/Protocols/Neuro/1%20Brain%20Routine.pdf)

Documentul MCB este disponibil integral mai jos, inclusiv notele, condițiile de utilizare a contrastului și imaginile de planificare. Textul clinic al sursei este în **engleză**; titlul și etichetele parametrilor sunt în română.

## Protocolul original

### Pagina 1

![Creier de rutină și AVC rapid — pagina 1](../../assets/mcb-mri/irm-creier-de-rutina-si-avc-rapid-mcb/pagina-1.png){ loading=lazy }

??? abstract "Textul paginii (engleză)"

    <div lang="en" style="white-space: pre-wrap">Updated
    07/04/24
    MRI Brain Routine (and Fast Stroke)
    Reviewed
    05/14/25
    Routine Brain:
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
    T1
    T1 SAG
    sag
    no
    5
    2
    left
    T2
    T2 FS AX
    ax
    yes
    5
    1.5
    base
    T1
    T1 AX
    ax
    no
    5
    1.5
    base
    *T1
    T1 COR
    cor
    no
    5
    1.5
    back
    FLAIR
    FLAIR AX
    ax
    no
    5
    1.5
    base
    **SWI
    SWI AX
    ax
    no
    5
    1.5
    base
    DWI
    DWI AX
    ax
    yes
    5
    1.5
    base
    CONTRAST - 2 mL/sec standard dose gadolinium (0.2 mL/kg Clariscan or 0.1 mL/kg Gadavist) followed by 20 mL saline flush.
    T1
    T1 POST AX
    ax
    no
    5
    1.5
    base
    T1
    T1 POST COR
    cor
    no
    5
    1.5
    back
    T1
    T1 POST SAG
    sag
    no
    5
    2
    left
    ***3D T1 FSPGR/MPRAGE
    AX THINS
    ax
    no
    1
    none
    base
    *Add the T1 COR pre contrast if the indication is hydrocephalus and/or NPH.
    **GRE if SWI is not available.
    ***Add the 3D T1 brain lab sequence in the following patients: known, suspected or previously treated brain mass; known cancer
    or metastatic workup and patients with headache.
    For the 3D T1 brain lab sequence: no angulation, anterior nose to posterior skull (front/back coverage) and top of skull to bottom
    of mandible (top/bottom coverage).
    Fast Stroke Protocol:
    FLAIR
    FLAIR AX
    ax
    no
    5
    1.5
    base
    **SWI
    SWI AX
    ax
    no
    5
    1.5
    base
    DWI
    DWI AX
    ax
    yes
    5
    1.5
    base
    **GRE if SWI is not available.
    </div>

## Parametrii secvențelor

Tabele extrase din PDF. Variantele, secvențele condiționate și momentele administrării contrastului se citesc împreună cu notele de pe pagina originală indicată.

### Tabelul 1 — pagina 1

| Secvență | Denumire PACS | Plan | Supresie grăsime | Grosime (mm) | Interval (mm) | Prima secțiune |
|---|---|---|---|---|---|---|
| T1 | T1 SAG | Sagital | Nu | 5 | 2 | Stânga |
| T2 | T2 FS AX | Axial | Da | 5 | 1.5 | Bază |
| T1 | T1 AX | Axial | Nu | 5 | 1.5 | Bază |
| *T1 | T1 COR | Coronal | Nu | 5 | 1.5 | Posterior |
| FLAIR | FLAIR AX | Axial | Nu | 5 | 1.5 | Bază |
| **SWI | SWI AX | Axial | Nu | 5 | 1.5 | Bază |
| DWI | DWI AX | Axial | Da | 5 | 1.5 | Bază |
| T1 | T1 POST AX | Axial | Nu | 5 | 1.5 | Bază |
| T1 | T1 POST COR | Coronal | Nu | 5 | 1.5 | Posterior |
| T1 | T1 POST SAG | Sagital | Nu | 5 | 2 | Stânga |
| ***3D T1 FSPGR/MPRAGE | AX THINS | Axial | Nu | 1 | none | Bază |
| FLAIR | FLAIR AX | Axial | Nu | 5 | 1.5 | Bază |
| **SWI | SWI AX | Axial | Nu | 5 | 1.5 | Bază |
| DWI | DWI AX | Axial | Da | 5 | 1.5 | Bază |

