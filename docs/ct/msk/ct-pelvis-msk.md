---
author: null
category: msk
clinical_indications:
- Fracturi ale inelului pelvin (clasificare Young-Burgess / Tile)
- Fracturi sacrate (clasificare Denis)
- Disjuncție a articulațiilor sacroiliace sau a simfizei pubiene
- Planificare chirurgicală pre-operatorie pentru fixare internă
contrast:
  agent: Nativ de regulă. Substanță de contrast dacă se suspectează leziune vasculară
    asociată sau hematom activ
  flow_rate: 2-3 mL/s
  volume: 'Dacă este indicat: 100 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Randare 3D VR a întregului inel pelvin. Incidențe specifice Inlet
    (înclinație caudo-cranială) și Outlet (înclinație cranio-caudală). Măsurarea deplasării
    fragmentelor.
  nursing: Fără linie venoasă de rutină decât dacă este suspectat traumatism vascular.
  rad: Integritatea inelului pelvin anterior și posterior. Fracturi sacrate și lărgirea
    găurilor sacrate. Deplasarea articulațiilor sacro-iliace. Disjuncția simfizei
    pubiene. Interesarea cotilului.
  tech: De la crestele iliace până sub micul trohanter. Achiziție submilimetrică optimizată
    pentru randare 3D a inelului pelvin. Incidențe reconstructive 'Inlet' și 'Outlet'.
  tips: Secțiuni fine submilimetrice pentru reconstrucțiile 3D indispensabile chirurgului
    ortoped.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu membrele inferioare aliniate simetric
premedication: ''
protocol_type: contrast-enhanced
recons:
- acquisition: CT Pelvis Osos
  fov: Pelvis
  kernel: Bone
  notes: Fereastră osoasă axială
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: CT Pelvis Osos
  fov: Pelvis
  kernel: Bone
  notes: Plan coronal al pelvisului
  plane: Coronal
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: CT Pelvis Osos
  fov: Pelvis
  kernel: Bone
  notes: Plan sagital centrat pe sacru și coloana lombo-sacrată
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: CT Pelvis Osos
  fov: Pelvis
  kernel: Bone
  notes: Incidențe specifice reconstructive Inlet și Outlet pe inelul pelvin
  plane: Inlet/Outlet
  thickness_increment: 1.5 mm/1.5 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Mici trohanteri
  name: CT Pelvis Osos
  notes: Achiziție submilimetrică pentru randare 3D a bazinului
  start: Creste iliace
  thickness: 0.625 mm
slug: ct-pelvis-msk
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
title: CT Pelvis Osos / Bazin (MSK)
---

# CT Pelvis Osos / Bazin (MSK)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Pelvis Osos | 0 sec | Creste iliace → Mici trohanteri |

    === "Indicații Clinice"

        - Fracturi ale inelului pelvin (clasificare Young-Burgess / Tile)
        - Fracturi sacrate (clasificare Denis)
        - Disjuncție a articulațiilor sacroiliace sau a simfizei pubiene
        - Planificare chirurgicală pre-operatorie pentru fixare internă

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat locomotor & Articulații*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu membrele inferioare aliniate simetric
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Substanță de contrast dacă se suspectează leziune vasculară asociată sau hematom activ |
        | Volum | Dacă este indicat: 100 mL |
        | Rată de Flux | 2-3 mL/s |
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

        - De la crestele iliace până sub micul trohanter. Achiziție submilimetrică optimizată pentru randare 3D a inelului pelvin. Incidențe reconstructive 'Inlet' și 'Outlet'.

    === "Note Asistent"

        - Fără linie venoasă de rutină decât dacă este suspectat traumatism vascular.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Integritatea inelului pelvin anterior și posterior. Fracturi sacrate și lărgirea găurilor sacrate. Deplasarea articulațiilor sacro-iliace. Disjuncția simfizei pubiene. Interesarea cotilului.

    === "Sfaturi & Recomandări"

        - Secțiuni fine submilimetrice pentru reconstrucțiile 3D indispensabile chirurgului ortoped.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Pelvis Osos | Creste iliace | Mici trohanteri | 0 sec | 0.625 mm | Achiziție submilimetrică pentru randare 3D a bazinului |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Pelvis Osos | Pelvis | 1.25 mm/1.25 mm | Bone |  | Fereastră osoasă axială |
    | Coronal | CT Pelvis Osos | Pelvis | 1.5 mm/1.5 mm | Bone |  | Plan coronal al pelvisului |
    | Sagital | CT Pelvis Osos | Pelvis | 1.5 mm/1.5 mm | Bone |  | Plan sagital centrat pe sacru și coloana lombo-sacrată |
    | Inlet/Outlet | CT Pelvis Osos | Pelvis | 1.5 mm/1.5 mm | Bone |  | Incidențe specifice reconstructive Inlet și Outlet pe inelul pelvin |
