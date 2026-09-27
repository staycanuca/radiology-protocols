---
title: IRM – Angio-IRM toracic (MCB)
modality: irm
category: vascular
slug: irm-angio-irm-toracic-mcb
author: MCB Radiology (documentul sursă)
last_updated: '2026-09-27'
tags:
- MCB Radiology
- IRM
- Vascular & IR
synonyms:
- Chest
- MRA Chest
- 1 MRA Chest
sources:
- title: 1 MRA Chest
  url: https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/Protocols/Vascular%20&%20IR/1%20MRA%20Chest.pdf
  pages:
  - 1
  consulted_on: '2026-09-27'
  relationship: Document instituțional original importat integral
provenance:
  version: mcb-mri-3c908aadf153
  processing:
  - Titlu și etichete de parametri în română; textul clinic original păstrat în engleză.
  - Import PDF integral, imagini ale tuturor paginilor și extragere automată a parametrilor
    secvențelor.
sequences:
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
- name: True FISP
  plane: Coronal
  fat_sat: Nu
  slice_gap: 5 mm / 1 mm
  fov_matrix: ''
  notes: 'PACS: TRUE FISP COR; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: True FISP
    pacs_name: TRUE FISP COR
    plane: cor
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1'
    first_slice: front
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
- name: 3D FLASH T1
  plane: Sagital
  fat_sat: Nu
  slice_gap: 1.35 mm / 0.27 mm
  fov_matrix: ''
  notes: 'PACS: 3D T1 PRE SAG; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: 3D FLASH T1
    pacs_name: 3D T1 PRE SAG
    plane: sag
    fat_sat: 'no'
    slice_mm: '1.35'
    gap_mm: '0.27'
    first_slice: left
- name: 3D FLASH T1
  plane: Coronal
  fat_sat: Nu
  slice_gap: 1.35 mm / 0.27 mm
  fov_matrix: ''
  notes: 'PACS: 3D T1 PRE COR; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: 3D FLASH T1
    pacs_name: 3D T1 PRE COR
    plane: cor
    fat_sat: 'no'
    slice_mm: '1.35'
    gap_mm: '0.27'
    first_slice: front
- name: 3D FLASH T1
  plane: Sagital
  fat_sat: Nu
  slice_gap: 1.35 mm / 0.27 mm
  fov_matrix: ''
  notes: 'PACS: 3D T1 ANGIO SAG; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: 3D FLASH T1
    pacs_name: 3D T1 ANGIO SAG
    plane: sag
    fat_sat: 'no'
    slice_mm: '1.35'
    gap_mm: '0.27'
    first_slice: left
- name: 3D FLASH T1
  plane: Coronal
  fat_sat: Nu
  slice_gap: 1.35 mm / 0.27 mm
  fov_matrix: ''
  notes: 'PACS: 3D T1 ANGIO COR; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: 3D FLASH T1
    pacs_name: 3D T1 ANGIO COR
    plane: cor
    fat_sat: 'no'
    slice_mm: '1.35'
    gap_mm: '0.27'
    first_slice: front
- name: '*T1 VIBE/LAVA'
  plane: Axial
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS POST AX; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: '*T1 VIBE/LAVA'
    pacs_name: T1 FS POST AX
    plane: ax
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: top
- name: '*T1 VIBE/LAVA'
  plane: Sagital
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS POST SAG; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: '*T1 VIBE/LAVA'
    pacs_name: T1 FS POST SAG
    plane: sag
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: left
- name: '*T1 VIBE/LAVA'
  plane: Coronal
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS POST COR; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: '*T1 VIBE/LAVA'
    pacs_name: T1 FS POST COR
    plane: cor
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: front
---

# IRM – Angio-IRM toracic (MCB)

[Catalog MCB](../mcb/index.md) · [Descarcă PDF-ul complet](../../assets/mcb-mri/irm-angio-irm-toracic-mcb/protocol.pdf) · [Sursa MCB](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/Protocols/Vascular%20&%20IR/1%20MRA%20Chest.pdf)

Documentul MCB este disponibil integral mai jos, inclusiv notele, condițiile de utilizare a contrastului și imaginile de planificare. Textul clinic al sursei este în **engleză**; titlul și etichetele parametrilor sunt în română.

## Protocolul original

### Pagina 1

![Angio-IRM toracic — pagina 1](../../assets/mcb-mri/irm-angio-irm-toracic-mcb/pagina-1.png){ loading=lazy }

??? abstract "Textul paginii (engleză)"

    <div lang="en" style="white-space: pre-wrap">Updated
    11/04/23
    MRA Chest
    Reviewed
    06/06/26
    Indications: aortic aneurysm/dissection and pulmonary embolus.
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
    True FISP
    TRUE FISP COR
    cor
    no
    5
    1
    front
    T1 VIBE/LAVA
    T1 FS PRE AX
    ax
    yes
    3.5
    0.6
    top
    3D FLASH T1
    3D T1 PRE SAG
    sag
    no
    1.35
    0.27
    left
    3D FLASH T1
    3D T1 PRE COR
    cor
    no
    1.35
    0.27
    front
    CONTRAST - 2 mL/sec standard dose gadolinium (0.2 mL/kg Clariscan or 0.1 mL/kg Gadavist) followed by 20 mL saline flush.
    For the angio phase bolus track and trigger when contrast reaches the ascending aorta.
    3D FLASH T1
    3D T1 ANGIO SAG
    sag
    no
    1.35
    0.27
    left
    3D FLASH T1
    3D T1 ANGIO COR
    cor
    no
    1.35
    0.27
    front
    *T1 VIBE/LAVA
    T1 FS POST AX
    ax
    yes
    3.5
    0.6
    top
    *T1 VIBE/LAVA
    T1 FS POST SAG
    sag
    yes
    3.5
    0.6
    left
    *T1 VIBE/LAVA
    T1 FS POST COR
    cor
    yes
    3.5
    0.6
    front
    *The post T1 VIBE/LAVA sequences are begun just after the 3D angio sequences finish scanning.
    RECONS:
    sagittal subtractions of the angio sequence
    axial and coronal MPRs of the subtracted sagittal angio sequence (3 mm thick no gap)
    horizontal MIP spinners of the subtracted sagittal angio sequence
    axial subtractions of the T1 VIBE/LAVA sequence
    </div>

## Parametrii secvențelor

Tabele extrase din PDF. Variantele, secvențele condiționate și momentele administrării contrastului se citesc împreună cu notele de pe pagina originală indicată.

### Tabelul 1 — pagina 1

| Secvență | Denumire PACS | Plan | Supresie grăsime | Grosime (mm) | Interval (mm) | Prima secțiune |
|---|---|---|---|---|---|---|
| T2 HASTE/SSFSE | T2 AX | Axial | Nu | 5 | 1 | Superior |
| T2 HASTE/SSFSE | T2 FS AX | Axial | Da | 5 | 1 | Superior |
| True FISP | TRUE FISP COR | Coronal | Nu | 5 | 1 | Anterior |
| T1 VIBE/LAVA | T1 FS PRE AX | Axial | Da | 3.5 | 0.6 | Superior |
| 3D FLASH T1 | 3D T1 PRE SAG | Sagital | Nu | 1.35 | 0.27 | Stânga |
| 3D FLASH T1 | 3D T1 PRE COR | Coronal | Nu | 1.35 | 0.27 | Anterior |
| 3D FLASH T1 | 3D T1 ANGIO SAG | Sagital | Nu | 1.35 | 0.27 | Stânga |
| 3D FLASH T1 | 3D T1 ANGIO COR | Coronal | Nu | 1.35 | 0.27 | Anterior |
| *T1 VIBE/LAVA | T1 FS POST AX | Axial | Da | 3.5 | 0.6 | Superior |
| *T1 VIBE/LAVA | T1 FS POST SAG | Sagital | Da | 3.5 | 0.6 | Stânga |
| *T1 VIBE/LAVA | T1 FS POST COR | Coronal | Da | 3.5 | 0.6 | Anterior |

