---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: chest
clinical_indications:
- Screening anual pentru cancer bronhopulmonar la pacienți asimptomatici cu risc crescut
- 'Criterii USPSTF / OHSU: Vârstă 50–80 ani, istoric de fumat ≥ 20 pachete-an, fumător
  activ sau renunțat în ultimii 15 ani'
- Monitorizare noduli pulmonari solizi sau subsolizi conform criteriilor Lung-RADS
  v2022
contrast:
  agent: FĂRĂ
  duration: 0s
  flow_rate: 0 mL/s
  roi: N/A
  timing: N/A
  trigger: N/A
  volume: 0 mL
iris_reference:
  chapter: Torace & Pulmon
  radiation_dose: Clasa 2 (Redusă 1 - 2 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-20'
notes:
  additional_recons: Volumetrie automată computerizată a nodulilor dacă este disponibil
    software dedicat.
  nursing: Educare pacient privind necesitatea continuării screening-ului anual și
    renunțarea la fumat.
  rad: Clasificare obligatorie conform Lung-RADS (categoriile 1, 2, 3, 4A, 4B, 4X).
    Măsurare diametru mediu (media dintre axul lung și axul scurt).
  tech: Protocol optimizat strict pentru minimizarea dozei de radiație (ALARA). Durata
    scanării sub 5 secunde.
  tips: Utilizarea filtrelor spectrale (staniu/Sn) permite scanarea la niveluri de
    iradiere comparabile cu o radiografie toracică convențională în 2 incidențe.
npo: N/A — protocol nativ
position: Decubit dorsal cu brațele ridicate
premedication: Fără contrast oral sau i.v.
protocol_type: non-contrast
recons:
- acquisition: Low-Dose CT
  fov: Torace
  ir_strength: Iterative Reconstruction Maximă (Admire 4-5 / AIDR 3D Strong)
  kernel: Pulmonar (I50f) + Mediastinal (I30f)
  notes: Reconstrucție iterativă puternică pentru eliminarea zgomotului asociat dozei
    joase
  plane: Axial, Coronal & Sagital
  thickness_increment: 1.0 mm / 1.0 mm
- acquisition: Low-Dose CT
  fov: Torace
  ir_strength: Standard
  kernel: Pulmonar
  notes: MIP pentru detecția rapidă a nodulilor pulmonari solizi
  plane: Axial
  thickness_increment: 5.0 mm / 5.0 mm MIP
safety:
  allergy: N/A — fără contrast
  renal: N/A — fără contrast
series:
- delay: 0 sec
  end: Recesuri costo-diafragmatice
  name: Low-Dose Chest CT
  notes: Apnee inspiratorie completă; achiziție într-o singură trecere rapidă (< 5
    secunde)
  start: Vârfuri pulmonare
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: 100-120 kV (sau Sn100 kV cu filtru de staniu)
  mas: 20-40 mAs (Doză efectivă ultra-joasă < 1.5 mSv; CTDIvol < 3.0 mGy)
  pitch: 1.2 - 1.5
  rotation_time: 0.33 - 0.5 s
  scan_mode: Elicoidal ultra-rapid
  slice_thickness: 0.625 mm
title: CT Screening Noduli Pulmonari Low-Dose (Protocol OHSU)
---

# CT Screening Noduli Pulmonari Low-Dose (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Low-Dose Chest CT | 0 sec | Vârfuri pulmonare → Recesuri costo-diafragmatice |

    === "Indicații Clinice"

        - Screening anual pentru cancer bronhopulmonar la pacienți asimptomatici cu risc crescut
        - Criterii USPSTF / OHSU: Vârstă 50–80 ani, istoric de fumat ≥ 20 pachete-an, fumător activ sau renunțat în ultimii 15 ani
        - Monitorizare noduli pulmonari solizi sau subsolizi conform criteriilor Lung-RADS v2022

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Torace & Pulmon*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 2 (Redusă 1 - 2 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }

-   __2. Pregătire Pacient__


    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
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
    | **Tensiune Tub (kV)** | 100-120 kV (sau Sn100 kV cu filtru de staniu) kV |
    | **Curent Tub (mAs)** | 20-40 mAs (Doză efectivă ultra-joasă < 1.5 mSv; CTDIvol < 3.0 mGy) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.33 - 0.5 s |
    | **Pitch (Factor Pas)** | 1.2 - 1.5 |
    | **Mod Scanare** | Elicoidal ultra-rapid |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol optimizat strict pentru minimizarea dozei de radiație (ALARA). Durata scanării sub 5 secunde.

    === "Note Asistent"

        - Educare pacient privind necesitatea continuării screening-ului anual și renunțarea la fumat.

        !!! warning "Siguranță"
            - **Funcție Renală:** N/A — fără contrast
            - **Alergii:** N/A — fără contrast

    === "Note Radiolog"

        - Clasificare obligatorie conform Lung-RADS (categoriile 1, 2, 3, 4A, 4B, 4X). Măsurare diametru mediu (media dintre axul lung și axul scurt).

    === "Sfaturi & Recomandări"

        - Utilizarea filtrelor spectrale (staniu/Sn) permite scanarea la niveluri de iradiere comparabile cu o radiografie toracică convențională în 2 incidențe.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Low-Dose Chest CT | Vârfuri pulmonare | Recesuri costo-diafragmatice | 0 sec | 0.625 mm | Apnee inspiratorie completă; achiziție într-o singură trecere rapidă (< 5 secunde) |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial, Coronal & Sagital | Low-Dose CT | Torace | 1.0 mm / 1.0 mm | Pulmonar (I50f) + Mediastinal (I30f) | Iterative Reconstruction Maximă (Admire 4-5 / AIDR 3D Strong) | Reconstrucție iterativă puternică pentru eliminarea zgomotului asociat dozei joase |
    | Axial | Low-Dose CT | Torace | 5.0 mm / 5.0 mm MIP | Pulmonar | Standard | MIP pentru detecția rapidă a nodulilor pulmonari solizi |
