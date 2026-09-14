---
author: Departamentul de Radiologie
category: neuro
clinical_indications:
- Pan-scan în politraumatism sever cu leziuni vertebrale multiple suspectate
- Bilanț lezional multietajat
- Bilanț metastaze osoase vertebrale (diseminare secundară)
- Spondilodiscită multifocală
contrast:
  agent: Nativ de regulă. Contrast dacă se evaluează metastaze sau infecție
  flow_rate: 3 mL/s
  volume: 'Dacă este indicat: 125 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții sagitale și coronale pe întreg axul spinal. Reformatări
    fine pe segmentele cu fracturi identificate.
  nursing: Linie venoasă dacă se administrează contrast. Imobilizare completă pe targă
    rigidă.
  rad: Aliniamentul întregului ax rahidian. Fracturi la multiple niveluri. Reculul
    fragmentelor în canalul spinal. Hematom epidural sau compresie medulară. Mase
    tumorale paravertebrale sau osteolitice.
  tech: De la baza craniului până la sacru/coccis. CÂMP FOARTE EXTINS. Achiziție submilimetrică
    continuă sau în segmente contigue. Reformatări sagitale și coronale continue pe
    toată coloana.
  tips: Examinare pe distanță lungă; asigurați poziționarea fără mișcare a pacientului.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu brațele de-a lungul corpului sau ridicate adaptat
premedication: ''
protocol_type: spine
recons:
- acquisition: CT Coloană Completă
  fov: Coloană
  kernel: Bone
  notes: Secțiuni fine axiale etajate
  plane: Axial
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: CT Coloană Completă
  fov: Coloană completă
  kernel: Bone
  notes: Plan sagital panoramic complet al coloanei vertebrale
  plane: Sagital
  thickness_increment: 2 mm/2 mm
- acquisition: CT Coloană Completă
  fov: Coloană completă
  kernel: Bone
  notes: Plan coronal de ansamblu
  plane: Coronal
  thickness_increment: 2 mm/2 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Sacru
  name: CT Coloană Completă
  notes: Achiziție submilimetrică pe toată coloana
  start: Baza craniului
  thickness: 0.625 mm
slug: ct-complete-spine
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
title: CT Coloană Vertebrală Completă (Cervico-Toraco-Lombară)
sources:
- title: AAPM CT Protocols — Adult Routine Head CT
  url: https://www.aapm.org/pubs/ctprotocols/documents/RoutineHeadCT.pdf
  institution: AAPM
  source_region: US
  kind: Protocol tehnic standardizat
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 503972f1004a69ab87fba33be79f28ad3647b389370870386d9af7967ea1691b
- title: UT Southwestern Radiology — CT Neuro / Head Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# CT Coloană Vertebrală Completă (Cervico-Toraco-Lombară)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Coloană Completă | 0 sec | Baza craniului → Sacru |

    === "Indicații Clinice"

        - Pan-scan în politraumatism sever cu leziuni vertebrale multiple suspectate
        - Bilanț lezional multietajat
        - Bilanț metastaze osoase vertebrale (diseminare secundară)
        - Spondilodiscită multifocală

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele de-a lungul corpului sau ridicate adaptat
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Contrast dacă se evaluează metastaze sau infecție |
        | Volum | Dacă este indicat: 125 mL |
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

        - De la baza craniului până la sacru/coccis. CÂMP FOARTE EXTINS. Achiziție submilimetrică continuă sau în segmente contigue. Reformatări sagitale și coronale continue pe toată coloana.

    === "Note Asistent"

        - Linie venoasă dacă se administrează contrast. Imobilizare completă pe targă rigidă.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Aliniamentul întregului ax rahidian. Fracturi la multiple niveluri. Reculul fragmentelor în canalul spinal. Hematom epidural sau compresie medulară. Mase tumorale paravertebrale sau osteolitice.

    === "Sfaturi & Recomandări"

        - Examinare pe distanță lungă; asigurați poziționarea fără mișcare a pacientului.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Coloană Completă | Baza craniului | Sacru | 0 sec | 0.625 mm | Achiziție submilimetrică pe toată coloana |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Coloană Completă | Coloană | 1.5 mm/1.5 mm | Bone |  | Secțiuni fine axiale etajate |
    | Sagital | CT Coloană Completă | Coloană completă | 2 mm/2 mm | Bone |  | Plan sagital panoramic complet al coloanei vertebrale |
    | Coronal | CT Coloană Completă | Coloană completă | 2 mm/2 mm | Bone |  | Plan coronal de ansamblu |

## Surse și revizuire

- [AAPM CT Protocols — Adult Routine Head CT](https://www.aapm.org/pubs/ctprotocols/documents/RoutineHeadCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Neuro / Head Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
