---
author: null
category: vascular
clinical_indications:
- Tromboză venoasă profundă ilio-femurală sau cavă inferioară (TVP)
- Sindrom May-Thurner (compresiunea venei iliace comune stângi de către artera iliacă
  comună dreaptă)
- Planificare montare sau extragere filtru de venă cavă inferioară (filtru VCI)
- Malformații venoase pelvine / sindrom de congestie pelvină
contrast:
  agent: Isovue 370
  duration: 40s
  flow_rate: 3 mL/s
  timing: Timp fix de întârziere (110s)
  volume: 2.0 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Flebograme MIP multiplanare. Reconstrucții 3D VR ale arborelui
    venos ilio-cav.
  nursing: Linie venoasă 18-20G.
  rad: Evaluați vena cavă inferioară, venele renale, iliace și femurale pentru defecte
    de umplere endoluminale (trombi). Căutați compresiunea vasculară extrinsică (May-Thurner).
    Măsurați diametrul VCI pentru dimensionarea corectă a filtrului cav.
  tech: Scanare la 110-120 secunde pentru faza venoasă omogenă. Rata mai lentă de
    injectare (3 mL/s) este adecvată pentru opacifierea venoasă. Scanare de la diafragm
    până la nivelul venelor femurale.
  tips: Brațele complet ridicate. Se pot include și venele gambei dacă se suspectează
    TVP extinsă.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: Oral contrast optional
protocol_type: vascular
recons:
- acquisition: Fază Venoasă CTV
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Evaluarea defectelor de umplere intraluminale
  plane: Axial
  thickness_increment: 2 mm/2 mm
- acquisition: Fază Venoasă CTV
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: MIP al sistemului venos cavo-iliac
  plane: Coronal
  thickness_increment: 2 mm/2 mm
- acquisition: Fază Venoasă CTV
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: VCI și pensa iliacă (May-Thurner)
  plane: Sagital
  thickness_increment: 2 mm/2 mm
- acquisition: Fază Venoasă CTV
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Randare tridimensională 3D a anatomiei venoase
  plane: 3D VR
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 110 sec
  end: Femur proximal
  name: Fază Venoasă CTV
  notes: Timp prelungit de întârziere pentru opacifierea venoasă uniformă
  start: Diafragm
  thickness: 0.625 mm
slug: ctv-abdomen-pelvis
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200 mAs)
  pitch: 1.0-1.375
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Flebo-CT (CTV) Abdomen și Pelvis (Sistem Venos Ilio-Cav)
---

# Flebo-CT (CTV) Abdomen și Pelvis (Sistem Venos Ilio-Cav)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Venoasă CTV | 110 sec | Diafragm → Femur proximal |

    === "Indicații Clinice"

        - Tromboză venoasă profundă ilio-femurală sau cavă inferioară (TVP)
        - Sindrom May-Thurner (compresiunea venei iliace comune stângi de către artera iliacă comună dreaptă)
        - Planificare montare sau extragere filtru de venă cavă inferioară (filtru VCI)
        - Malformații venoase pelvine / sindrom de congestie pelvină

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular & Sistem vascular*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Oral contrast optional

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 2.0 mL/kg |
        | Rată de Flux | 3 mL/s |
        | Durată | 40s |
        | Metodă Temporizare | Timp fix de întârziere (110s) |
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
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.0-1.375 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare la 110-120 secunde pentru faza venoasă omogenă. Rata mai lentă de injectare (3 mL/s) este adecvată pentru opacifierea venoasă. Scanare de la diafragm până la nivelul venelor femurale.

    === "Note Asistent"

        - Linie venoasă 18-20G.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Evaluați vena cavă inferioară, venele renale, iliace și femurale pentru defecte de umplere endoluminale (trombi). Căutați compresiunea vasculară extrinsică (May-Thurner). Măsurați diametrul VCI pentru dimensionarea corectă a filtrului cav.

    === "Sfaturi & Recomandări"

        - Brațele complet ridicate. Se pot include și venele gambei dacă se suspectează TVP extinsă.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Venoasă CTV | Diafragm | Femur proximal | 110 sec | 0.625 mm | Timp prelungit de întârziere pentru opacifierea venoasă uniformă |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Venoasă CTV | Abdomen-Pelvis | 2 mm/2 mm | Standard |  | Evaluarea defectelor de umplere intraluminale |
    | Coronal | Fază Venoasă CTV | Abdomen-Pelvis | 2 mm/2 mm | Standard |  | MIP al sistemului venos cavo-iliac |
    | Sagital | Fază Venoasă CTV | Abdomen-Pelvis | 2 mm/2 mm | Standard |  | VCI și pensa iliacă (May-Thurner) |
    | 3D VR | Fază Venoasă CTV | Abdomen-Pelvis | 1 mm/1 mm | Standard |  | Randare tridimensională 3D a anatomiei venoase |
