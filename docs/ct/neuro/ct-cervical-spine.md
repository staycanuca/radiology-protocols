---
author: Departamentul de Radiologie
category: neuro
clinical_indications:
- Traumatism de coloană cervicală / accident rutier / cădere
- Cervicalgie acută sau cronică severă
- Radiculopatie cervico-brahială
- Mielopatie cervicală spondilotică
contrast:
  agent: Nativ de regulă. Substanță de contrast dacă se suspectează infecție (spondilodiscită)
    sau tumoră
  flow_rate: 3 mL/s
  volume: 'Dacă este indicat: 100 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții osoase sagitale și coronale submilimetrice. Reformatări
    oblice paralele cu găurile de conjugare.
  nursing: Fără linie venoasă de rutină. Mențineți gulerul cervical dacă este caz
    de traumatism.
  rad: Aliniamentul corpilor vertebrali și linia spinolaminară. Fracturi (odontoidă,
    masive articulare, pediculi, apofize spinoase). Lățimea canalului rahidian. Găurile
    de conjugare (foramene). Articulații interapofizare.
  tech: De la baza craniului până la nivelul T1. Achiziție elicoidală submilimetrică.
    Reformatări sagitale și coronale fine obligatorii. Filtru de os de înaltă rezoluție.
  tips: Coborârea la maxim a umerilor pacientului pentru a evita artefactele la joncțiunea
    C7-T1.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu capul înainte; umerii coborâți la maxim
premedication: ''
protocol_type: spine
recons:
- acquisition: CT Coloană Cervicală Elicoidal
  fov: Coloană cervicală
  kernel: Bone
  notes: Fereastră osoasă și de părți moi
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: CT Coloană Cervicală Elicoidal
  fov: Coloană cervicală
  kernel: Bone
  notes: Plan mediosagital și parasagital
  plane: Sagital
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: CT Coloană Cervicală Elicoidal
  fov: Coloană cervicală
  kernel: Bone
  notes: Aliniament coronal și odontoidă
  plane: Coronal
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: CT Coloană Cervicală Elicoidal
  fov: Coloană cervicală
  kernel: Bone
  notes: Plan oblic pentru stenozele de foramen neural
  plane: Oblique sagittal
  thickness_increment: 1.25 mm/1.25 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: T1
  name: CT Coloană Cervicală Elicoidal
  notes: Achiziție elicoidală submilimetrică
  start: Baza craniului
  thickness: 0.625 mm
slug: ct-cervical-spine
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
title: CT Coloană Cervicală
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

# CT Coloană Cervicală

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Coloană Cervicală Elicoidal | 0 sec | Baza craniului → T1 |

    === "Indicații Clinice"

        - Traumatism de coloană cervicală / accident rutier / cădere
        - Cervicalgie acută sau cronică severă
        - Radiculopatie cervico-brahială
        - Mielopatie cervicală spondilotică

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul înainte; umerii coborâți la maxim
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Substanță de contrast dacă se suspectează infecție (spondilodiscită) sau tumoră |
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

        - De la baza craniului până la nivelul T1. Achiziție elicoidală submilimetrică. Reformatări sagitale și coronale fine obligatorii. Filtru de os de înaltă rezoluție.

    === "Note Asistent"

        - Fără linie venoasă de rutină. Mențineți gulerul cervical dacă este caz de traumatism.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Aliniamentul corpilor vertebrali și linia spinolaminară. Fracturi (odontoidă, masive articulare, pediculi, apofize spinoase). Lățimea canalului rahidian. Găurile de conjugare (foramene). Articulații interapofizare.

    === "Sfaturi & Recomandări"

        - Coborârea la maxim a umerilor pacientului pentru a evita artefactele la joncțiunea C7-T1.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Coloană Cervicală Elicoidal | Baza craniului | T1 | 0 sec | 0.625 mm | Achiziție elicoidală submilimetrică |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Coloană Cervicală Elicoidal | Coloană cervicală | 1.25 mm/1.25 mm | Bone |  | Fereastră osoasă și de părți moi |
    | Sagital | CT Coloană Cervicală Elicoidal | Coloană cervicală | 1.25 mm/1.25 mm | Bone |  | Plan mediosagital și parasagital |
    | Coronal | CT Coloană Cervicală Elicoidal | Coloană cervicală | 1.25 mm/1.25 mm | Bone |  | Aliniament coronal și odontoidă |
    | Oblique sagittal | CT Coloană Cervicală Elicoidal | Coloană cervicală | 1.25 mm/1.25 mm | Bone |  | Plan oblic pentru stenozele de foramen neural |

## Surse și revizuire

- [AAPM CT Protocols — Adult Routine Head CT](https://www.aapm.org/pubs/ctprotocols/documents/RoutineHeadCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Neuro / Head Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
