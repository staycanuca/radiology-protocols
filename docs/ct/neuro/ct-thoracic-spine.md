---
author: null
category: neuro
clinical_indications:
- Traumatism de coloană toracală
- Fractură prin tasare osteoporotică sau traumatică
- Dorsalgie severă persistentă
- Suspiciune de proces expansiv tumoral sau infecțios
contrast:
  agent: Nativ de regulă. Contrast dacă este suspectată infecție sau tumoră
  flow_rate: 3 mL/s
  volume: 'Dacă este indicat: 100 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții osoase sagitale și coronale fine.
  nursing: Fără linie venoasă de rutină.
  rad: Aliniament toracal și cifoză. Tasări sau fracturi cominutive ale corpilor vertebrali.
    Reculul peretelui posterior vertebral în canal. Spațiile discale și articulațiile
    costo-vertebrale. Părțile moi paratoracale.
  tech: De la nivelul C7 până la L1. Achiziție elicoidală submilimetrică. Reformatări
    sagitale și coronale de calitate. Brațele ridicate pentru a reduce atenuarea fasciculului
    prin umeri.
  tips: Brațele ridicate reduc semnificativ zgomotul de imagine.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu brațele ridicate deasupra capului dacă starea permite
premedication: ''
protocol_type: spine
recons:
- acquisition: CT Coloană Toracală Elicoidal
  fov: Coloană toracală
  kernel: Bone
  notes: Fereastră osoasă și de părți moi
  plane: Axial
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: CT Coloană Toracală Elicoidal
  fov: Coloană toracală
  kernel: Bone
  notes: Plan mediosagital și parasagital
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: CT Coloană Toracală Elicoidal
  fov: Coloană toracală
  kernel: Bone
  notes: Plan coronal de ansamblu
  plane: Coronal
  thickness_increment: 1.5 mm/1.5 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: L1
  name: CT Coloană Toracală Elicoidal
  notes: Achiziție elicoidală submilimetrică
  start: C7
  thickness: 0.625 mm
slug: ct-thoracic-spine
synonyms: []
tech_params:
  aec: Activat (Modulare 3D adaptată coloanei vertebrale)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 250 mAs)
  pitch: Helical
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Coloană Toracală
---

# CT Coloană Toracală

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Coloană Toracală Elicoidal | 0 sec | C7 → L1 |

    === "Indicații Clinice"

        - Traumatism de coloană toracală
        - Fractură prin tasare osteoporotică sau traumatică
        - Dorsalgie severă persistentă
        - Suspiciune de proces expansiv tumoral sau infecțios

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate deasupra capului dacă starea permite
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Contrast dacă este suspectată infecție sau tumoră |
        | Volum | Dacă este indicat: 100 mL |
        | Rată de Flux | 3 mL/s |
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
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare 3D adaptată coloanei vertebrale) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - De la nivelul C7 până la L1. Achiziție elicoidală submilimetrică. Reformatări sagitale și coronale de calitate. Brațele ridicate pentru a reduce atenuarea fasciculului prin umeri.

    === "Note Asistent"

        - Fără linie venoasă de rutină.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Aliniament toracal și cifoză. Tasări sau fracturi cominutive ale corpilor vertebrali. Reculul peretelui posterior vertebral în canal. Spațiile discale și articulațiile costo-vertebrale. Părțile moi paratoracale.

    === "Sfaturi & Recomandări"

        - Brațele ridicate reduc semnificativ zgomotul de imagine.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Coloană Toracală Elicoidal | C7 | L1 | 0 sec | 0.625 mm | Achiziție elicoidală submilimetrică |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Coloană Toracală Elicoidal | Coloană toracală | 1.5 mm/1.5 mm | Bone |  | Fereastră osoasă și de părți moi |
    | Sagital | CT Coloană Toracală Elicoidal | Coloană toracală | 1.5 mm/1.5 mm | Bone |  | Plan mediosagital și parasagital |
    | Coronal | CT Coloană Toracală Elicoidal | Coloană toracală | 1.5 mm/1.5 mm | Bone |  | Plan coronal de ansamblu |
