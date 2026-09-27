---
title: IRM – Fluxul lichidului cefalorahidian (LCR) (MCB)
modality: irm
category: neuro
slug: irm-fluxul-lichidului-cefalorahidian-lcr-mcb
author: MCB Radiology (documentul sursă)
last_updated: '2026-09-27'
tags:
- MCB Radiology
- IRM
- Neuro
synonyms:
- CSF Flow
- 14 CSF Flow
sources:
- title: 14 CSF Flow
  url: https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/Protocols/Neuro/14%20CSF%20Flow.pdf
  pages:
  - 1
  consulted_on: '2026-09-27'
  relationship: Document instituțional original importat integral
provenance:
  version: mcb-mri-bba458bdff51
  processing:
  - Titlu și etichete de parametri în română; textul clinic original păstrat în engleză.
  - Import PDF integral, imagini ale tuturor paginilor și extragere automată a parametrilor
    secvențelor.
sequences:
- name: 2D Phase Contrast Cine
  plane: Sagital
  fat_sat: Nu
  slice_gap: 5 mm / 0 mm
  fov_matrix: normal brain
  notes: 'PACS: 2D CINE SAG; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: 2D Phase Contrast Cine
    pacs_name: 2D CINE SAG
    plane: sag
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '0'
    first_slice: left
    fov_matrix: normal brain
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
    fov_matrix: ''
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
    fov_matrix: ''
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
    fov_matrix: ''
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
    fov_matrix: ''
- name: '*SWI'
  plane: Axial
  fat_sat: Nu
  slice_gap: 5 mm / 1.5 mm
  fov_matrix: ''
  notes: 'PACS: SWI AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: '*SWI'
    pacs_name: SWI AX
    plane: ax
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1.5'
    first_slice: base
    fov_matrix: ''
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
    fov_matrix: ''
- name: '**T2'
  plane: Sagital
  fat_sat: Nu
  slice_gap: 3 mm / 0.3 mm
  fov_matrix: normal cervical spine
  notes: 'PACS: T2 SAG; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: '**T2'
    pacs_name: T2 SAG
    plane: sag
    fat_sat: 'no'
    slice_mm: '3'
    gap_mm: '0.3'
    first_slice: left
    fov_matrix: normal cervical spine
- name: T1
  plane: Axial
  fat_sat: Nu
  slice_gap: 5 mm / 1.5 mm
  fov_matrix: normal brain
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
    fov_matrix: normal brain
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
    fov_matrix: ''
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
    fov_matrix: ''
- name: 3D T1 FSPGR/MPRAGE
  plane: Axial
  fat_sat: Nu
  slice_gap: 1 mm / none
  fov_matrix: normal brain lab
  notes: 'PACS: AX THINS; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: 3D T1 FSPGR/MPRAGE
    pacs_name: AX THINS
    plane: ax
    fat_sat: 'no'
    slice_mm: '1'
    gap_mm: none
    first_slice: base
    fov_matrix: normal brain lab
---

# IRM – Fluxul lichidului cefalorahidian (LCR) (MCB)

[Catalog MCB](../mcb/index.md) · [Descarcă PDF-ul complet](../../assets/mcb-mri/irm-fluxul-lichidului-cefalorahidian-lcr-mcb/protocol.pdf) · [Sursa MCB](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/Protocols/Neuro/14%20CSF%20Flow.pdf)

Documentul MCB este disponibil integral mai jos, inclusiv notele, condițiile de utilizare a contrastului și imaginile de planificare. Textul clinic al sursei este în **engleză**; titlul și etichetele parametrilor sunt în română.

## Protocolul original

### Pagina 1

![Fluxul lichidului cefalorahidian (LCR) — pagina 1](../../assets/mcb-mri/irm-fluxul-lichidului-cefalorahidian-lcr-mcb/pagina-1.png){ loading=lazy }

??? abstract "Textul paginii (engleză)"

    <div lang="en" style="white-space: pre-wrap">Updated
    05/07/26
    Reviewed
    05/07/26
    MRI CSF Flow
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
    2D Phase Contrast Cine
    2D CINE SAG
    sag
    no
    5
    0
    left
    T1
    T1 SAG
    sag
    no
    5
    2
    left
    T2 FS AX
    T2
    ax
    yes
    5
    1.5
    base
    T1 AX
    T1
    ax
    no
    5
    1.5
    base
    normal brain
    FLAIR
    FLAIR AX
    ax
    no
    5
    1.5
    base
    *SWI
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
    **T2
    T2 SAG
    normal cervical spine
    sag
    no
    3
    0.3
    left
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
    normal brain
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
    3D T1 FSPGR/MPRAGE
    AX THINS
    normal brain lab
    ax
    no
    1
    none
    base
    *GRE if SWI is not available.
    **Run a routine sagittal T2 non fat sat of the cervical spine (don&#x27;t need a separate order or requisition).
    For the 3D T1 brain lab sequence: no angulation, anterior nose to posterior skull (front/back coverage) and top of skull to bottom
    of mandible (top/bottom coverage).
    </div>

## Parametrii secvențelor

Tabele extrase din PDF. Variantele, secvențele condiționate și momentele administrării contrastului se citesc împreună cu notele de pe pagina originală indicată.

### Tabelul 1 — pagina 1

| Secvență | Denumire PACS | Plan | Supresie grăsime | Grosime (mm) | Interval (mm) | Prima secțiune | FOV |
|---|---|---|---|---|---|---|---|
| 2D Phase Contrast Cine | 2D CINE SAG | Sagital | Nu | 5 | 0 | Stânga | normal brain |
| T1 | T1 SAG | Sagital | Nu | 5 | 2 | Stânga |  |
| T2 | T2 FS AX | Axial | Da | 5 | 1.5 | Bază |  |
| T1 | T1 AX | Axial | Nu | 5 | 1.5 | Bază |  |
| FLAIR | FLAIR AX | Axial | Nu | 5 | 1.5 | Bază |  |
| *SWI | SWI AX | Axial | Nu | 5 | 1.5 | Bază |  |
| DWI | DWI AX | Axial | Da | 5 | 1.5 | Bază |  |
| **T2 | T2 SAG | Sagital | Nu | 3 | 0.3 | Stânga | normal cervical spine |
| T1 | T1 POST AX | Axial | Nu | 5 | 1.5 | Bază | normal brain |
| T1 | T1 POST COR | Coronal | Nu | 5 | 1.5 | Posterior |  |
| T1 | T1 POST SAG | Sagital | Nu | 5 | 2 | Stânga |  |
| 3D T1 FSPGR/MPRAGE | AX THINS | Axial | Nu | 1 | none | Bază | normal brain lab |

