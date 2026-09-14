---
author: null
category: neuro
clinical_indications:
- Evaluare post-mielografie cu contrast intratecal
- Stenoză severă de canal rahidian la pacienți cu contraindicație absolută de RMN
  (pacemaker, implanturi)
- Compresiune radiculară / avulsie de rădăcini nervoase
- Fistulă de lichid cefalorahidian (LCR) / hipotensiune intracraniană spontană
contrast:
  agent: Omnipaque 240 non-ionic aprobat intratecal
  flow_rate: Administrare manuală lentă fluoroghidată
  volume: 10-15 mL intratecal
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții oblice pe emergențele radiculare. Documentarea
    nivelului și severității compresiunii sacului dural.
  nursing: Pacientul a efectuat deja puncția lombară cu contrast IT. Mențineți capul
    ridicat la 30 de grade pentru a preveni cefaleea post-puncție.
  rad: Opacifierea tecii durale și a rădăcinilor cozii de cal. Amprentarea sacului
    dural de către hernii discale sau osteofite. Umplerea tecilor radiculare (lipsa
    opacifierii indică avulsie sau compresiune).
  tech: Scanare CT imediat după injectarea intratecală a contrastului sub fluoroscopie.
    Secțiuni fine submilimetrice. Reformatări multiplanare axiale și sagitale de înaltă
    rezoluție.
  tips: Precauții riguroase pentru cefaleea post-puncție lombară. Secțiuni submilimetrice
    indispensabile.
npo: Repaus alimentar 4 ore înainte de puncția lombară
position: Decubit dorsal sau ventral conform protocolului post-puncție lombară
premedication: Intrathecal contrast already given
protocol_type: spine
recons:
- acquisition: Mielo-CT
  fov: Coloană
  kernel: Bone and Standard
  notes: Rădăcini nervoase și sacul dural opacifiat
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Mielo-CT
  fov: Coloană
  kernel: Standard
  notes: Plan mediosagital pentru compresiunea sacului dural
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Mielo-CT
  fov: Coloană
  kernel: Standard
  notes: Plan coronal pentru simetria emergențelor radiculare
  plane: Coronal
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Mielo-CT
  fov: Coloană
  kernel: Standard
  notes: Reformatări oblice pe găurile de conjugare
  plane: Oblique sagittal
  thickness_increment: 1.5 mm/1.5 mm
safety:
  allergy: Verificați riscul de alergie la contrast iodat
  renal: Nu se excretă direct vascular - toleranță bună
series:
- delay: Imediat post-mielografie
  end: Acoperire extinsă
  name: Mielo-CT
  notes: Submilimetric pentru rezoluția rădăcinilor nervoase
  start: Regiunea de interes
  thickness: 0.625 mm
slug: ct-myelogram
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 250 mAs)
  pitch: Helical
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Mielo-CT (Mielografie CT)
---

# Mielo-CT (Mielografie CT)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Mielo-CT | Imediat post-mielografie | Regiunea de interes → Acoperire extinsă |

    === "Indicații Clinice"

        - Evaluare post-mielografie cu contrast intratecal
        - Stenoză severă de canal rahidian la pacienți cu contraindicație absolută de RMN (pacemaker, implanturi)
        - Compresiune radiculară / avulsie de rădăcini nervoase
        - Fistulă de lichid cefalorahidian (LCR) / hipotensiune intracraniană spontană

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal sau ventral conform protocolului post-puncție lombară
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore înainte de puncția lombară
    - **Premedicație / Pregătire:**
        - Intrathecal contrast already given

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 240 non-ionic aprobat intratecal |
        | Volum | 10-15 mL intratecal |
        | Rată de Flux | Administrare manuală lentă fluoroghidată |
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
    | **Curent Tub (mAs)** | Auto (referință 250 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare CT imediat după injectarea intratecală a contrastului sub fluoroscopie. Secțiuni fine submilimetrice. Reformatări multiplanare axiale și sagitale de înaltă rezoluție.

    === "Note Asistent"

        - Pacientul a efectuat deja puncția lombară cu contrast IT. Mențineți capul ridicat la 30 de grade pentru a preveni cefaleea post-puncție.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se excretă direct vascular - toleranță bună
            - **Alergii:** Verificați riscul de alergie la contrast iodat

    === "Note Radiolog"

        - Opacifierea tecii durale și a rădăcinilor cozii de cal. Amprentarea sacului dural de către hernii discale sau osteofite. Umplerea tecilor radiculare (lipsa opacifierii indică avulsie sau compresiune).

    === "Sfaturi & Recomandări"

        - Precauții riguroase pentru cefaleea post-puncție lombară. Secțiuni submilimetrice indispensabile.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Mielo-CT | Regiunea de interes | Acoperire extinsă | Imediat post-mielografie | 0.625 mm | Submilimetric pentru rezoluția rădăcinilor nervoase |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Mielo-CT | Coloană | 1 mm/1 mm | Bone and Standard |  | Rădăcini nervoase și sacul dural opacifiat |
    | Sagital | Mielo-CT | Coloană | 1.5 mm/1.5 mm | Standard |  | Plan mediosagital pentru compresiunea sacului dural |
    | Coronal | Mielo-CT | Coloană | 1.5 mm/1.5 mm | Standard |  | Plan coronal pentru simetria emergențelor radiculare |
    | Oblique sagittal | Mielo-CT | Coloană | 1.5 mm/1.5 mm | Standard |  | Reformatări oblice pe găurile de conjugare |
