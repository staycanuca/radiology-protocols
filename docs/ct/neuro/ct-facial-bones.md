---
author: null
category: neuro
clinical_indications:
- Traumatism maxilo-facial / agresiune fizică
- Fracturi ale orbitelor (blow-out) și arcurilor zigomatice
- Fracturi de piramidă nazală și sept nazal
- Fracturi de mandibulă și ale complexului nazo-orbito-etmoidal (NOE)
contrast:
  agent: Fără substanță de contrast
  type: non-contrast
last_updated: '2026-01-01'
notes:
  additional_recons: Randare tridimensională 3D VR a scheletului facial. Documentarea
    detaliată a fracturilor cominutive pentru chirurgul BMF.
  nursing: Îndepărtați cerceii, piercingurile faciale și protezele dentare mobile.
  rad: Clasificare Le Fort (I, II, III). Fracturi ale planșeului și peretelui medial
    orbitar (hernierea grăsimii/mușchiului drept inferior). Complexul zigomatico-maxilar
    (ZMC) și nazo-orbito-etmoidal (NOE). Fracturi mandibulare (condil, unghi, corp,
    simfiză).
  tech: De la nivelul sinusurilor frontale până sub marginea inferioară a mandibulei.
    Achiziție elicoidală submilimetrică esențială pentru randare 3D. Îndepărtați protezele
    dentare.
  tips: Îndepărtați toate obiectele metalice faciale pentru a elimina artefactele
    de dungă.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu capul imobilizat în suportul dedicat
premedication: ''
protocol_type: non-contrast
recons:
- acquisition: CT Masiv Facial
  fov: Față
  kernel: Bone
  notes: Fereastră osoasă de înaltă rezoluție
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: CT Masiv Facial
  fov: Față
  kernel: Bone
  notes: Plan coronal pentru orbite și sinusuri
  plane: Coronal
  thickness_increment: 1 mm/1 mm
- acquisition: CT Masiv Facial
  fov: Față
  kernel: Bone
  notes: Plan mediosagital pentru oasele proprii nazale
  plane: Sagital
  thickness_increment: 1 mm/1 mm
- acquisition: CT Masiv Facial
  fov: Față
  kernel: Bone
  notes: Randare tridimensională 3D de suprafață a masivului facial
  plane: 3D
  thickness_increment: 0.75 mm/0.75 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Mandibulă
  name: CT Masiv Facial
  notes: Submilimetric pentru randare 3D a feței
  start: Sinusuri frontale
  thickness: 0.625 mm
slug: ct-facial-bones
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
title: CT Masiv Facial și Schelet Nazal
---

# CT Masiv Facial și Schelet Nazal

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Masiv Facial | 0 sec | Sinusuri frontale → Mandibulă |

    === "Indicații Clinice"

        - Traumatism maxilo-facial / agresiune fizică
        - Fracturi ale orbitelor (blow-out) și arcurilor zigomatice
        - Fracturi de piramidă nazală și sept nazal
        - Fracturi de mandibulă și ale complexului nazo-orbito-etmoidal (NOE)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul imobilizat în suportul dedicat
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

        - De la nivelul sinusurilor frontale până sub marginea inferioară a mandibulei. Achiziție elicoidală submilimetrică esențială pentru randare 3D. Îndepărtați protezele dentare.

    === "Note Asistent"

        - Îndepărtați cerceii, piercingurile faciale și protezele dentare mobile.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Clasificare Le Fort (I, II, III). Fracturi ale planșeului și peretelui medial orbitar (hernierea grăsimii/mușchiului drept inferior). Complexul zigomatico-maxilar (ZMC) și nazo-orbito-etmoidal (NOE). Fracturi mandibulare (condil, unghi, corp, simfiză).

    === "Sfaturi & Recomandări"

        - Îndepărtați toate obiectele metalice faciale pentru a elimina artefactele de dungă.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Masiv Facial | Sinusuri frontale | Mandibulă | 0 sec | 0.625 mm | Submilimetric pentru randare 3D a feței |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Masiv Facial | Față | 1 mm/1 mm | Bone |  | Fereastră osoasă de înaltă rezoluție |
    | Coronal | CT Masiv Facial | Față | 1 mm/1 mm | Bone |  | Plan coronal pentru orbite și sinusuri |
    | Sagital | CT Masiv Facial | Față | 1 mm/1 mm | Bone |  | Plan mediosagital pentru oasele proprii nazale |
    | 3D | CT Masiv Facial | Față | 0.75 mm/0.75 mm | Bone |  | Randare tridimensională 3D de suprafață a masivului facial |
