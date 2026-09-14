---
author: Departamentul de Radiologie
category: msk
clinical_indications:
- Fracturi ale extremității distale a radiusului (Pouteau-Colles, Goyrand-Smith, Barton)
- Fracturi de oase carpiene (scafoid, semilunar, piramidal, pisiform, trapez etc.)
- Instabilitate a articulației radio-ulnare distale (RUD)
- Leziune sau disjuncție a ligamentului scapholunatar (SLAC wrist)
contrast:
  agent: Nativ de regulă. Contrast dacă se suspectează tenosinovită/infecție
  flow_rate: 2 mL/s
  volume: 'Dacă este indicat: 50 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Reformatări specifice paralele și perpendiculare pe axul lung
    al scafoidului. Evaluarea aliniamentului carpian. Randare 3D VR.
  nursing: Fără linie venoasă de rutină.
  rad: Incongruență articulară a radiusului distal (treaptă articulară măsurată în
    mm). Fracturi de scafoid (pol proximal, col, pol distal; căutați semne de osteonecroză
    sau pseudartroză). Aliniament carpian (unghi scapholunatar, DISI/VISI). Articulație
    radio-ulnară distală.
  tech: De la nivelul radiusului/ulnei distale până la baza metacarpienelor. Achiziție
    submilimetrică esențială pentru trabeculația osoasă a carpienelor.
  tips: Secțiuni fine submilimetrice indispensabile pentru traiectele oculte de fractură
    ale scafoidului.
npo: Nu este necesar repaus alimentar
position: Decubit ventral cu pumnul întins deasupra capului ('poziție Superman') sau
  decubit dorsal pe abdomen dacă este dureros
premedication: ''
protocol_type: musculoskeletal
recons:
- acquisition: CT Pumn
  fov: Pumn
  kernel: Bone
  notes: Fereastră osoasă axială de înaltă rezoluție
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: CT Pumn
  fov: Pumn
  kernel: Bone
  notes: Plan coronal al articulației radio-carpiene
  plane: Coronal
  thickness_increment: 1 mm/1 mm
- acquisition: CT Pumn
  fov: Pumn
  kernel: Bone
  notes: Plan sagital pentru aliniamentul radio-luno-capitat
  plane: Sagital
  thickness_increment: 1 mm/1 mm
- acquisition: CT Pumn
  fov: Scafoid
  kernel: Bone
  notes: Plan oblic sagital pe axul lung al scafoidului
  plane: Oblique sagittal
  thickness_increment: 0.75 mm/0.75 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Baza metacarpienelor
  name: CT Pumn
  notes: Achiziție submilimetrică
  start: Radius/ulnă distală
  thickness: 0.625 mm
slug: ct-wrist
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 150-200 mAs)
  pitch: Helical
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Pumn / Articulație Radio-Carpiană
sources:
- title: ACR-SSR Practice Parameter for Musculoskeletal CT
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CT-MSK.pdf
  institution: ACR / SSR
  source_region: US
  kind: Standard de practică MSK
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: c0429ea24ea0955f09249fe969fc88b0a48e70073a42bab3ba08be042e1085f4
- title: UT Southwestern Radiology — Musculoskeletal CT Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# CT Pumn / Articulație Radio-Carpiană

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Pumn | 0 sec | Radius/ulnă distală → Baza metacarpienelor |

    === "Indicații Clinice"

        - Fracturi ale extremității distale a radiusului (Pouteau-Colles, Goyrand-Smith, Barton)
        - Fracturi de oase carpiene (scafoid, semilunar, piramidal, pisiform, trapez etc.)
        - Instabilitate a articulației radio-ulnare distale (RUD)
        - Leziune sau disjuncție a ligamentului scapholunatar (SLAC wrist)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat locomotor & Articulații*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit ventral cu pumnul întins deasupra capului ('poziție Superman') sau decubit dorsal pe abdomen dacă este dureros
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Contrast dacă se suspectează tenosinovită/infecție |
        | Volum | Dacă este indicat: 50 mL |
        | Rată de Flux | 2 mL/s |
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
    | **Curent Tub (mAs)** | Auto (referință 150-200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - De la nivelul radiusului/ulnei distale până la baza metacarpienelor. Achiziție submilimetrică esențială pentru trabeculația osoasă a carpienelor.

    === "Note Asistent"

        - Fără linie venoasă de rutină.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Incongruență articulară a radiusului distal (treaptă articulară măsurată în mm). Fracturi de scafoid (pol proximal, col, pol distal; căutați semne de osteonecroză sau pseudartroză). Aliniament carpian (unghi scapholunatar, DISI/VISI). Articulație radio-ulnară distală.

    === "Sfaturi & Recomandări"

        - Secțiuni fine submilimetrice indispensabile pentru traiectele oculte de fractură ale scafoidului.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Pumn | Radius/ulnă distală | Baza metacarpienelor | 0 sec | 0.625 mm | Achiziție submilimetrică |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Pumn | Pumn | 1 mm/1 mm | Bone |  | Fereastră osoasă axială de înaltă rezoluție |
    | Coronal | CT Pumn | Pumn | 1 mm/1 mm | Bone |  | Plan coronal al articulației radio-carpiene |
    | Sagital | CT Pumn | Pumn | 1 mm/1 mm | Bone |  | Plan sagital pentru aliniamentul radio-luno-capitat |
    | Oblique sagittal | CT Pumn | Scafoid | 0.75 mm/0.75 mm | Bone |  | Plan oblic sagital pe axul lung al scafoidului |

## Surse și revizuire

- [ACR-SSR Practice Parameter for Musculoskeletal CT](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CT-MSK.pdf) — *ACR / SSR* (US)
- [UT Southwestern Radiology — Musculoskeletal CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
