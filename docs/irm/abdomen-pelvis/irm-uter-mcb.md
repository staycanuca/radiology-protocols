---
title: IRM – Uter (MCB)
modality: irm
category: abdomen-pelvis
slug: irm-uter-mcb
author: MCB Radiology (documentul sursă)
last_updated: '2026-09-27'
tags:
- MCB Radiology
- IRM
- Body
synonyms:
- Uterus
- 14 Uterus
sources:
- title: 14 Uterus
  url: https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/Protocols/Body/14%20Uterus.pdf
  pages:
  - 1
  - 2
  - 3
  consulted_on: '2026-09-27'
  relationship: Document instituțional original importat integral
provenance:
  version: mcb-mri-8b7996dc0b3e
  processing:
  - Titlu și etichete de parametri în română; textul clinic original păstrat în engleză.
  - Import PDF integral, imagini ale tuturor paginilor și extragere automată a parametrilor
    secvențelor.
sequences:
- name: T2 HASTE/SSFSE
  plane: Coronal
  fat_sat: Nu
  slice_gap: 7 mm / 1.4 mm
  fov_matrix: full pelvis
  notes: 'PACS: T2 COR; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T2 HASTE/SSFSE
    pacs_name: T2 COR
    plane: cor
    fat_sat: 'no'
    slice_mm: '7'
    gap_mm: '1.4'
    first_slice: front
    fov_matrix: full pelvis
- name: T2 TSE
  plane: Sagital
  fat_sat: Nu
  slice_gap: 5 mm / 1 mm
  fov_matrix: ''
  notes: 'PACS: T2 SAG; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T2 TSE
    pacs_name: T2 SAG
    plane: sag
    fat_sat: 'no'
    slice_mm: '5'
    gap_mm: '1'
    first_slice: left
    fov_matrix: ''
- name: T2 HASTE/SSFSE
  plane: Axial
  fat_sat: Nu
  slice_gap: 7 mm / 1.4 mm
  fov_matrix: ''
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
    fov_matrix: ''
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
- name: T2 TSE
  plane: obl ax
  fat_sat: Nu
  slice_gap: 3.5 mm / 0.5 mm
  fov_matrix: uterus, cervix or vagina (depends on indication & lesion location)
  notes: 'PACS: T2 OBL AX; pagina 1. Variantele și condițiile sunt precizate în documentul
    original.'
  source_page: 1
  source_parameters:
    name: T2 TSE
    pacs_name: T2 OBL AX
    plane: obl ax
    fat_sat: 'no'
    slice_mm: '3.5'
    gap_mm: '0.5'
    first_slice: top
    fov_matrix: uterus, cervix or vagina (depends on indication & lesion location)
- name: Diffusion (b50, b1000, ADC)
  plane: obl ax
  fat_sat: Da
  slice_gap: 5 mm / 0 mm
  fov_matrix: ''
  notes: 'PACS: DIFFUSION OBL AX; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: Diffusion (b50, b1000, ADC)
    pacs_name: DIFFUSION OBL AX
    plane: obl ax
    fat_sat: 'yes'
    slice_mm: '5'
    gap_mm: '0'
    first_slice: top
    fov_matrix: ''
- name: T1 VIBE/LAVA
  plane: Sagital
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: full pelvis
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
    fov_matrix: full pelvis
- name: T1 VIBE/LAVA
  plane: obl ax
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS PRE OBL AX; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS PRE OBL AX
    plane: obl ax
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: top
    fov_matrix: ''
- name: T1 VIBE/LAVA
  plane: Sagital
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: full pelvis
  notes: 'PACS: T1 FS 35 SEC SAG; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS 35 SEC SAG
    plane: sag
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: left
    fov_matrix: full pelvis
- name: T1 VIBE/LAVA
  plane: Sagital
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS 60 SEC SAG; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS 60 SEC SAG
    plane: sag
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: left
    fov_matrix: ''
- name: T1 VIBE/LAVA
  plane: obl ax
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS 90 SEC OBL AX; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS 90 SEC OBL AX
    plane: obl ax
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: top
    fov_matrix: ''
- name: T1 VIBE/LAVA
  plane: Sagital
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS 120 SAG; pagina 1. Variantele și condițiile sunt precizate în
    documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS 120 SAG
    plane: sag
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: left
    fov_matrix: ''
- name: T1 VIBE/LAVA
  plane: obl ax
  fat_sat: Da
  slice_gap: 3.5 mm / 0.6 mm
  fov_matrix: ''
  notes: 'PACS: T1 FS 4 MIN OBL AX; pagina 1. Variantele și condițiile sunt precizate
    în documentul original.'
  source_page: 1
  source_parameters:
    name: T1 VIBE/LAVA
    pacs_name: T1 FS 4 MIN OBL AX
    plane: obl ax
    fat_sat: 'yes'
    slice_mm: '3.5'
    gap_mm: '0.6'
    first_slice: top
    fov_matrix: ''
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
    fov_matrix: ''
---

# IRM – Uter (MCB)

[Catalog MCB](../mcb/index.md) · [Descarcă PDF-ul complet](../../assets/mcb-mri/irm-uter-mcb/protocol.pdf) · [Sursa MCB](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/Protocols/Body/14%20Uterus.pdf)

Documentul MCB este disponibil integral mai jos, inclusiv notele, condițiile de utilizare a contrastului și imaginile de planificare. Textul clinic al sursei este în **engleză**; titlul și etichetele parametrilor sunt în română.

## Protocolul original

### Pagina 1

![Uter — pagina 1](../../assets/mcb-mri/irm-uter-mcb/pagina-1.png){ loading=lazy }

??? abstract "Textul paginii (engleză)"

    <div lang="en" style="white-space: pre-wrap">Updated
    06/06/26
    MRI Uterus
    Reviewed
    06/06/26
    Indications: cancers/masses/lesions of the uterus, endometrium, cervix &amp; vagina; uterine fibroids and leiomyomas; 
    uterine adenomyosis; vaginal/uterine bleeding, pre/post menopausal uterine bleeding &amp; dysfunctional uterine bleeding.
    Use unisex protocol for ovarian cancers/masses/cysts, endometriosis &amp; vulvar cancers.
    US Gel: patient administers 30 mL US gel into vagina.
    US gel required for cervix &amp; vaginal indications.
    US gel not required for uterine indications, fibroids.
    Full Pelvis FOV: Iliac crests to few slices below introitus/anus (top/bottom coverage), greater trochanter to 
    greater trochanter (right/left coverage), anterior pelvic wall skin to posterior buttock skin (front/back coverage).
    Mass FOV: centered on mass, FOV 13-15 cm, 320 x 256 matrix, cover several slices above and below mass.
    Go to MRIMaster.com for a guide of proper positioning.
    slice                    
    gap                    
    Pulse Sequence
    PACS Name
    Field of View
    plane
    fat                   
    sat
    (mm)
    (mm)
    first                               
    slice
    GLUCAGON - 1 mg slow IV push just before beginning imaging.
    T2 HASTE/SSFSE
    T2 COR
    cor
    no
    7
    1.4
    front
    T2 TSE
    T2 SAG
    sag
    no
    5
    1
    left
    full pelvis
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
    Send the above sequences to PACS for a body Radiologist check to localize the lesion and determine the oblique axial plane
    through the lesion (see axial oblique examples on next patient).
    T2 TSE
    T2 OBL AX
    obl ax
    no
    3.5
    0.5
    top
    uterus, cervix or vagina              
    (depends on indication &amp; 
    Diffusion                                      
    obl ax
    yes
    5
    0
    top
    lesion location)               
    (b50, b1000, ADC)
    DIFFUSION OBL AX
    T1 VIBE/LAVA
    T1 FS PRE SAG
    sag
    yes
    3.5
    0.6
    left
    T1 VIBE/LAVA
    full pelvis
    T1 FS PRE OBL AX
    obl ax
    yes
    3.5
    0.6
    top
    GLUCAGON - 1 mg slow IV push just before giving IV contrast.
    CONTRAST - 2 mL/sec standard dose gadolinium (0.2 mL/kg Clariscan or 0.1 mL/kg Gadavist) followed by 20 mL saline flush. 
    T1 VIBE/LAVA
    T1 FS 35 SEC SAG
    sag
    yes
    3.5
    0.6
    left
    T1 VIBE/LAVA
    T1 FS 60 SEC SAG
    sag
    yes
    3.5
    0.6
    left
    T1 VIBE/LAVA
    T1 FS 90 SEC OBL AX
    obl ax
    yes
    3.5
    0.6
    top
    full pelvis
    T1 VIBE/LAVA
    T1 FS 120 SAG
    sag
    yes
    3.5
    0.6
    left
    T1 VIBE/LAVA
    T1 FS 4 MIN OBL AX
    obl ax
    yes
    3.5
    0.6
    top
    T1 VIBE/LAVA
    T1 FS 5 MIN AX
    ax
    yes
    3.5
    0.6
    top
    RECONS:
    oblique axial and sagittal subtractions
    </div>

### Pagina 2

![Uter — pagina 2](../../assets/mcb-mri/irm-uter-mcb/pagina-2.png){ loading=lazy }

??? abstract "Textul paginii (engleză)"

    <div lang="en" style="white-space: pre-wrap">MRI Uterus
    Uterine/Endometrial Lesions/Indications
    Oblique axial angulation (perpendicular to the long axis of the endometrial canal in the sagittal plane)
    Cervical Lesions/Indications
    Oblique axial angulation (perpendicular to the long axis of the endocervical canal in the sagittal plane)
    </div>

### Pagina 3

![Uter — pagina 3](../../assets/mcb-mri/irm-uter-mcb/pagina-3.png){ loading=lazy }

??? abstract "Textul paginii (engleză)"

    <div lang="en" style="white-space: pre-wrap">Vaginal Lesions/Indications
    Oblique axial angulation (perpendicular to the long axis of the vagina in the sagittal plane)
    </div>

## Parametrii secvențelor

Tabele extrase din PDF. Variantele, secvențele condiționate și momentele administrării contrastului se citesc împreună cu notele de pe pagina originală indicată.

### Tabelul 1 — pagina 1

| Secvență | Denumire PACS | Plan | Supresie grăsime | Grosime (mm) | Interval (mm) | Prima secțiune | FOV |
|---|---|---|---|---|---|---|---|
| T2 HASTE/SSFSE | T2 COR | Coronal | Nu | 7 | 1.4 | Anterior | full pelvis |
| T2 TSE | T2 SAG | Sagital | Nu | 5 | 1 | Stânga |  |
| T2 HASTE/SSFSE | T2 AX | Axial | Nu | 7 | 1.4 | Superior |  |
| T2 HASTE/SSFSE | T2 FS AX | Axial | Da | 7 | 1.4 | Superior |  |
| T2 TSE | T2 OBL AX | obl ax | Nu | 3.5 | 0.5 | Superior | uterus, cervix or vagina (depends on indication &amp; lesion location) |
| Diffusion (b50, b1000, ADC) | DIFFUSION OBL AX | obl ax | Da | 5 | 0 | Superior |  |
| T1 VIBE/LAVA | T1 FS PRE SAG | Sagital | Da | 3.5 | 0.6 | Stânga | full pelvis |
| T1 VIBE/LAVA | T1 FS PRE OBL AX | obl ax | Da | 3.5 | 0.6 | Superior |  |
| T1 VIBE/LAVA | T1 FS 35 SEC SAG | Sagital | Da | 3.5 | 0.6 | Stânga | full pelvis |
| T1 VIBE/LAVA | T1 FS 60 SEC SAG | Sagital | Da | 3.5 | 0.6 | Stânga |  |
| T1 VIBE/LAVA | T1 FS 90 SEC OBL AX | obl ax | Da | 3.5 | 0.6 | Superior |  |
| T1 VIBE/LAVA | T1 FS 120 SAG | Sagital | Da | 3.5 | 0.6 | Stânga |  |
| T1 VIBE/LAVA | T1 FS 4 MIN OBL AX | obl ax | Da | 3.5 | 0.6 | Superior |  |
| T1 VIBE/LAVA | T1 FS 5 MIN AX | Axial | Da | 3.5 | 0.6 | Superior |  |

