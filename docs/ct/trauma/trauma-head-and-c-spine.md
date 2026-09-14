---
author: Departamentul de Radiologie
category: trauma
clinical_indications:
- Traumatism cranio-cerebral (TCC)
- Degajarea / evaluarea leziunilor de coloană cervicală
- Bilanț inițial în politraumatism
contrast:
  agent: N/A
  type: non-contrast
last_updated: '2026-01-01'
notes:
  additional_recons: 'Coloană cervicală: reconstrucții sagitale și coronale osoase
    submilimetrice. Randare 3D în caz de fracturi complexe cu deplasare.'
  nursing: Mențineți precauțiile de imobilizare a coloanei cervicale. Gulerul cervical
    rămâne montat. Consemnați scorul Glasgow (GCS).
  rad: 'Craniu: hemoragie acută (epidurală, subdurală, subarahnoidiană, contuzii hemoragice),
    fracturi craniene. Coloană: fracturi vertebrale, aliniament, disjuncții, suspiciune
    de leziune ligamentară.'
  tech: 'DOUĂ achiziții: 1) Craniu de la vertex la C1 2) Coloană cervicală de la baza
    craniului la T1. Craniu: 5 mm axial (și reconstrucții submilimetrice). Coloană
    cervicală: 0.625 mm elicoidal cu reconstrucții multiplanare fine. Imobilizare
    riguroasă.'
  tips: Mențineți gulerul cervical montat. Asigurați poziția neutră a capului.
npo: Fără repaus alimentar - urgență traumatologică
position: Decubit dorsal cu capul înainte. Guler cervical imobilizator fixat
premedication: ''
protocol_type: trauma
recons:
- acquisition: CT Nativ Craniu
  fov: Craniu
  kernel: Brain
  notes: Fereastră de parenchim cerebral și fereastră osoasă
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: CT Nativ Coloană Cervicală
  fov: Coloană cervicală
  kernel: Bone
  notes: Plan mediosagital și parasagital coloană cervicală
  plane: Sagital
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: CT Nativ Coloană Cervicală
  fov: Coloană cervicală
  kernel: Bone
  notes: Aliniament coronal și apofiza odontoidă
  plane: Coronal
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: CT Nativ Coloană Cervicală
  fov: Coloană cervicală
  kernel: Bone
  notes: Fereastră osoasă axială coloană cervicală
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică (examinare fără contrast)
series:
- delay: 0 sec
  end: Gaura occipitală (foramen magnum)
  name: CT Nativ Craniu
  notes: Paralel cu linia orbitomeatală / palatul dur
  start: Vertex
  thickness: 1.25 mm
- delay: 0 sec
  end: T1
  name: CT Nativ Coloană Cervicală
  notes: Elicoidal submilimetric pentru coloana cervicală
  start: Baza craniului
  thickness: 0.625 mm
slug: trauma-head-and-c-spine
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D pentru politraumă)
  collimation: 64 × 0.625 mm sau 16 × 0.75 mm
  kv: '120'
  mas: Auto (300 mAs craniu / 250 mAs coloană)
  pitch: '0.5'
  rotation_time: 1.0 head / 0.5 spines
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Craniu și Coloană Cervicală în Politraumatism
sources:
- title: ACR Appropriateness Criteria — Major Blunt Trauma
  url: https://www.acr.org/clinical-resources/clinical-tools-and-reference/appropriateness-criteria
  institution: ACR
  source_region: US
  kind: Criterii de oportunitate clinică
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 7a9944bf40cbdca19afa54c99c357074c28dc49534ed1c21c814d9f71c93b198
- title: UT Southwestern Radiology — Trauma Whole-Body CT Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# CT Craniu și Coloană Cervicală în Politraumatism

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Nativ Craniu | 0 sec | Vertex → Gaura occipitală (foramen magnum) |
        | CT Nativ Coloană Cervicală | 0 sec | Baza craniului → T1 |

    === "Indicații Clinice"

        - Traumatism cranio-cerebral (TCC)
        - Degajarea / evaluarea leziunilor de coloană cervicală
        - Bilanț inițial în politraumatism

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Traumatisme & Politraumă*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul înainte. Guler cervical imobilizator fixat
    - **Repaus Alimentar (NPO):** Fără repaus alimentar - urgență traumatologică
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
    | **Curent Tub (mAs)** | Auto (300 mAs craniu / 250 mAs coloană) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D pentru politraumă) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 16 × 0.75 mm |
    | **Timp de Rotație** | 1.0 head / 0.5 spine s |
    | **Pitch (Factor Pas)** | 0.5 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - DOUĂ achiziții: 1) Craniu de la vertex la C1 2) Coloană cervicală de la baza craniului la T1. Craniu: 5 mm axial (și reconstrucții submilimetrice). Coloană cervicală: 0.625 mm elicoidal cu reconstrucții multiplanare fine. Imobilizare riguroasă.

    === "Note Asistent"

        - Mențineți precauțiile de imobilizare a coloanei cervicale. Gulerul cervical rămâne montat. Consemnați scorul Glasgow (GCS).

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică (examinare fără contrast)
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Craniu: hemoragie acută (epidurală, subdurală, subarahnoidiană, contuzii hemoragice), fracturi craniene. Coloană: fracturi vertebrale, aliniament, disjuncții, suspiciune de leziune ligamentară.

    === "Sfaturi & Recomandări"

        - Mențineți gulerul cervical montat. Asigurați poziția neutră a capului.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Nativ Craniu | Vertex | Gaura occipitală (foramen magnum) | 0 sec | 1.25 mm | Paralel cu linia orbitomeatală / palatul dur |
    | CT Nativ Coloană Cervicală | Baza craniului | T1 | 0 sec | 0.625 mm | Elicoidal submilimetric pentru coloana cervicală |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Nativ Craniu | Craniu | 2.5 mm/2.5 mm | Brain |  | Fereastră de parenchim cerebral și fereastră osoasă |
    | Sagital | CT Nativ Coloană Cervicală | Coloană cervicală | 1.25 mm/1.25 mm | Bone |  | Plan mediosagital și parasagital coloană cervicală |
    | Coronal | CT Nativ Coloană Cervicală | Coloană cervicală | 1.25 mm/1.25 mm | Bone |  | Aliniament coronal și apofiza odontoidă |
    | Axial | CT Nativ Coloană Cervicală | Coloană cervicală | 1.25 mm/1.25 mm | Bone |  | Fereastră osoasă axială coloană cervicală |

## Surse și revizuire

- [ACR Appropriateness Criteria — Major Blunt Trauma](https://www.acr.org/clinical-resources/clinical-tools-and-reference/appropriateness-criteria) — *ACR* (US)
- [UT Southwestern Radiology — Trauma Whole-Body CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
