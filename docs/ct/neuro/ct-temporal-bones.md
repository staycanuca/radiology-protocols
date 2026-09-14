---
author: null
category: neuro
clinical_indications:
- Hipoacuzie de transmisie, neurosenzorială sau mixtă
- Otite medii cronice / otomastoidită
- Suspiciune de colesteatom
- Fractură de stâncă temporală (longitudinală / transversală)
- Bilanț pre-implant cohlear
contrast:
  agent: Fără substanță de contrast
  type: non-contrast
last_updated: '2026-01-01'
notes:
  additional_recons: Reformatări oblice Pöschl (paralel cu canalul semicircular superior)
    și Stenvers (perpendicular pe stâncă). Măsurarea apeductului vestibular.
  nursing: Fără linie venoasă. Îndepărtați aparatele auditive și cerceii.
  rad: Lanțul osicular (ciocan, nicovală, scăriță). Melcul (cohleea), canalele semicirculare,
    vestibulul. Conductul auditiv intern (CAI) și meatul acustic extern. Celulele
    mastoidiene. Integritatea tegmen tympani și a canalului nervului facial.
  tech: 'Stânci temporale: de la canalul auditiv extern până la vârful stâncii (apexul
    petros). ACHIZIȚIE SUBMILIMETRICĂ < 0.625 mm. Reconstrucții directe axiale și
    coronale ultra-fine cu filtru de os de rezoluție extremă.'
  tips: Rezoluție extremă obligatorie. Kernel osos foarte dur (Bone sharp).
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu capul imobilizat în suport dedicat
premedication: ''
protocol_type: neuroradiology
recons:
- acquisition: CT Axial Stânci Temporale
  fov: Stâncă temporală
  kernel: Bone sharp
  notes: Filtru osos de rezoluție ultra-înaltă
  plane: Axial
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: CT Coronal Stânci Temporale
  fov: Stâncă temporală
  kernel: Bone sharp
  notes: Plan coronal osos pentru lanțul osicular și tegmen
  plane: Coronal
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: CT Axial Stânci Temporale
  fov: Ureche medie
  kernel: Bone
  notes: Plan oblic orientat pe lanțul de oscioare
  plane: Oblique sagittal
  thickness_increment: 0.5 mm/0.5 mm
- acquisition: CT Axial Stânci Temporale
  fov: Ureche internă
  kernel: Bone
  notes: Incidențe specifice Pöschl și Stenvers pentru CAI și canale semicirculare
  plane: Pöschl/Stenvers
  thickness_increment: 0.5 mm/0.5 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Vârful stâncii temporale
  name: CT Axial Stânci Temporale
  notes: Paralel cu canalul semicircular lateral
  start: Conduct auditiv extern
  thickness: 0.625 mm
- delay: 0 sec
  end: Conduct auditiv intern
  name: CT Coronal Stânci Temporale
  notes: Perpendicular pe axul stâncii petroase
  start: Conduct auditiv extern
  thickness: 0.625 mm
slug: ct-temporal-bones
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Curent crescut (referință 300-400 mAs)
  pitch: Sequential or helical
  rotation_time: Axial/Coronals
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Stânci Temporale / Ureche Medie și Internă
---

# CT Stânci Temporale / Ureche Medie și Internă

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Axial Stânci Temporale | 0 sec | Conduct auditiv extern → Vârful stâncii temporale |
        | CT Coronal Stânci Temporale | 0 sec | Conduct auditiv extern → Conduct auditiv intern |

    === "Indicații Clinice"

        - Hipoacuzie de transmisie, neurosenzorială sau mixtă
        - Otite medii cronice / otomastoidită
        - Suspiciune de colesteatom
        - Fractură de stâncă temporală (longitudinală / transversală)
        - Bilanț pre-implant cohlear

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul imobilizat în suport dedicat
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
    | **Curent Tub (mAs)** | Curent crescut (referință 300-400 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | Axial/Coronal s |
    | **Pitch (Factor Pas)** | Sequential or helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Stânci temporale: de la canalul auditiv extern până la vârful stâncii (apexul petros). ACHIZIȚIE SUBMILIMETRICĂ < 0.625 mm. Reconstrucții directe axiale și coronale ultra-fine cu filtru de os de rezoluție extremă.

    === "Note Asistent"

        - Fără linie venoasă. Îndepărtați aparatele auditive și cerceii.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Lanțul osicular (ciocan, nicovală, scăriță). Melcul (cohleea), canalele semicirculare, vestibulul. Conductul auditiv intern (CAI) și meatul acustic extern. Celulele mastoidiene. Integritatea tegmen tympani și a canalului nervului facial.

    === "Sfaturi & Recomandări"

        - Rezoluție extremă obligatorie. Kernel osos foarte dur (Bone sharp).

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Axial Stânci Temporale | Conduct auditiv extern | Vârful stâncii temporale | 0 sec | 0.625 mm | Paralel cu canalul semicircular lateral |
    | CT Coronal Stânci Temporale | Conduct auditiv extern | Conduct auditiv intern | 0 sec | 0.625 mm | Perpendicular pe axul stâncii petroase |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Axial Stânci Temporale | Stâncă temporală | 0.625 mm/0.625 mm | Bone sharp |  | Filtru osos de rezoluție ultra-înaltă |
    | Coronal | CT Coronal Stânci Temporale | Stâncă temporală | 0.625 mm/0.625 mm | Bone sharp |  | Plan coronal osos pentru lanțul osicular și tegmen |
    | Oblique sagittal | CT Axial Stânci Temporale | Ureche medie | 0.5 mm/0.5 mm | Bone |  | Plan oblic orientat pe lanțul de oscioare |
    | Pöschl/Stenvers | CT Axial Stânci Temporale | Ureche internă | 0.5 mm/0.5 mm | Bone |  | Incidențe specifice Pöschl și Stenvers pentru CAI și canale semicirculare |
