---
author: null
category: neuro
clinical_indications:
- Planificare chirurgicală endoscopică rinosinusală (FESS)
- Chirurgie ghidată prin imagine (IGS - Image-Guided Surgery)
- Polipoză rinosinusală masivă recidivată / reintervenție ORL
contrast:
  agent: Fără substanță de contrast
  type: non-contrast
last_updated: '2026-01-01'
notes:
  additional_recons: Export direct al setului de date DICOM cu grosime izotropă de
    0.625 mm. Randare 3D a scheletului facial.
  nursing: Poziționare strictă fără rotație a capului. Montare markeri fiduciali cutanați
    dacă sunt solicitați.
  rad: Anatomia completă a sinusurilor paranazale. Complexul osteo-meatal (OMC). Înălțimea
    lamei ciuruite a etmoidului (clasificare Keros). Dehiscențe ale lamei papiracee,
    canalului optic sau arterei carotide interne. Celule Onodi și celule Haller.
  tech: Achiziție elicoidală izotropă submilimetrică (< 0.625 mm) cu gantry 0 grade.
    Set de date DICOM compatibil cu sistemele de navigație chirurgicală ORL (Medtronic
    StealthStation, Brainlab etc.).
  tips: Voxelii izotropi sunt esențiali pentru reformatări în timp real pe stația
    de neuronavigație intraoperatorie.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu capul imobilizat în poziție neutră
premedication: ''
protocol_type: neuroradiology
recons:
- acquisition: CT Sinusuri Stereotaxic
  fov: Sinusuri
  kernel: Bone
  notes: Plan axial izotrop osos
  plane: Axial
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: CT Sinusuri Stereotaxic
  fov: Sinusuri
  kernel: Bone
  notes: Plan coronal izotrop osos
  plane: Coronal
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: CT Sinusuri Stereotaxic
  fov: Sinusuri
  kernel: Bone
  notes: Plan sagital izotrop osos
  plane: Sagital
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: CT Sinusuri Stereotaxic
  fov: Sinusuri
  kernel: Bone
  notes: Randare de suprafață 3D pentru corelare intraoperatorie
  plane: 3D surface
  thickness_increment: 0.625 mm/0.625 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Palat dur
  name: CT Sinusuri Stereotaxic
  notes: Achiziție izotropă submilimetrică pentru neuronavigație
  start: Sinusuri frontale
  thickness: 0.625 mm
slug: ct-sinus-stereotactic
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200 mAs)
  pitch: Pitch for isotropic
  rotation_time: Helicals
  scan_mode: Secvențial (Axial) sau Elicoidal fin
  slice_thickness: 0.625 mm
title: CT Sinusuri Paranazale Stereotaxic (Neuronavigație ORL)
---

# CT Sinusuri Paranazale Stereotaxic (Neuronavigație ORL)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Sinusuri Stereotaxic | 0 sec | Sinusuri frontale → Palat dur |

    === "Indicații Clinice"

        - Planificare chirurgicală endoscopică rinosinusală (FESS)
        - Chirurgie ghidată prin imagine (IGS - Image-Guided Surgery)
        - Polipoză rinosinusală masivă recidivată / reintervenție ORL

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul imobilizat în poziție neutră
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Fără substanță de contrast |
        | Volum |  |
        | Rată de Flux |  |
        | Durată |  |
        | Metodă Temporizare |  |
        | Poziționare ROI |  |
        | Declanșator (HU) |  |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | Auto (referință 200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | Helical s |
    | **Pitch (Factor Pas)** | Pitch for isotropic |
    | **Mod Scanare** | Secvențial (Axial) sau Elicoidal fin |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Achiziție elicoidală izotropă submilimetrică (< 0.625 mm) cu gantry 0 grade. Set de date DICOM compatibil cu sistemele de navigație chirurgicală ORL (Medtronic StealthStation, Brainlab etc.).

    === "Note Asistent"

        - Poziționare strictă fără rotație a capului. Montare markeri fiduciali cutanați dacă sunt solicitați.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Anatomia completă a sinusurilor paranazale. Complexul osteo-meatal (OMC). Înălțimea lamei ciuruite a etmoidului (clasificare Keros). Dehiscențe ale lamei papiracee, canalului optic sau arterei carotide interne. Celule Onodi și celule Haller.

    === "Sfaturi & Recomandări"

        - Voxelii izotropi sunt esențiali pentru reformatări în timp real pe stația de neuronavigație intraoperatorie.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Sinusuri Stereotaxic | Sinusuri frontale | Palat dur | 0 sec | 0.625 mm | Achiziție izotropă submilimetrică pentru neuronavigație |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Sinusuri Stereotaxic | Sinusuri | 0.625 mm/0.625 mm | Bone |  | Plan axial izotrop osos |
    | Coronal | CT Sinusuri Stereotaxic | Sinusuri | 0.625 mm/0.625 mm | Bone |  | Plan coronal izotrop osos |
    | Sagital | CT Sinusuri Stereotaxic | Sinusuri | 0.625 mm/0.625 mm | Bone |  | Plan sagital izotrop osos |
    | 3D surface | CT Sinusuri Stereotaxic | Sinusuri | 0.625 mm/0.625 mm | Bone |  | Randare de suprafață 3D pentru corelare intraoperatorie |
