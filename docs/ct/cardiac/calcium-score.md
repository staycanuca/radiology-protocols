---
author: null
category: cardiac
clinical_indications:
- Stratificarea riscului cardiovascular la pacienți asimptomatici
- Durere toracică la pacienți cu probabilitate pre-test scăzută spre intermediară
- Screening asimptomatic la pacienți cu antecedente heredo-colaterale precoce
- Hipercolesterolemie / dislipidemie moderat-severă
- Factori multipli de risc cardiovascular asociați
contrast:
  agent: Fără substanță de contrast
  type: non-contrast
last_updated: '2026-02-02'
notes:
  additional_recons: Calcul scor Agatston, volum de calciu și distribuție pe percentile.
  nursing: Nu este necesară linie venoasă.
  rad: Verificați eventualele artefacte de mișcare pe câmpul pulmonar extins. Calcularea
    scorului Agatston total și pe fiecare trunchi coronarian. Raportați percentila
    conform vârstei și sexului. Menționați descoperirile extracardiace.
  tech: 'Sincronizare ECG prospectivă. Instrucțiuni de apnee inspiratorie fără Valsalva.
    Pentru echipamente single-source: scanare în telediastolă dacă FC < 63 bpm, altfel
    telediastolă și telesistolă. Pentru dual-source: telediastolă dacă FC < 79 bpm.
    Asigurați contact optim al electrozilor ECG. Țintă: FC <= 60 bpm, ritm regulat.'
  tips: Traseu ECG stabil fără paraziți. Antrenamentul apneei pacientului înainte
    de scanare este esențial.
npo: Fără repaus alimentar strict; fără cafea/fumat cu 4 ore înainte
position: Decubit dorsal cu picioarele înainte
premedication: Fără premedicație de rutină
protocol_type: non-contrast
recons:
- acquisition: Scor de Calciu
  fov: Cord
  kernel: Standard
  notes: Pentru calcularea scorului Agatston
  plane: Axial
  thickness_increment: 3 mm/3 mm
- acquisition: Scor de Calciu
  fov: Torace
  kernel: Lung
  notes: Câmp pulmonar pentru decelarea anomaliilor extracardiace
  plane: Axial
  thickness_increment: 1.5 mm/1.5 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică (fără contrast)
series:
- delay: 0 sec
  end: Sub vârful cordului
  name: Scor de Calciu
  notes: Achiziție secvențială axială sincronizată ECG prospectiv
  start: Carenă
  thickness: 3 mm
slug: calcium-score
synonyms: []
tech_params:
  aec: Modulare ECG activată (pulsare conform ritmului cardiac)
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: '120'
  mas: Auto (doză redusă)
  pitch: 1.0-1.2
  rotation_time: 0.28-0.35s
  scan_mode: Elicoidal sincronizat ECG (sau Secvențial prospectiv)
  slice_thickness: 3 mm
title: CT Scor de Calciu Coronarian (Scor Agatston)
---

# CT Scor de Calciu Coronarian (Scor Agatston)

**Ultima actualizare:** 2026-02-02
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Scor de Calciu | 0 sec | Carenă → Sub vârful cordului |

    === "Indicații Clinice"

        - Stratificarea riscului cardiovascular la pacienți asimptomatici
        - Durere toracică la pacienți cu probabilitate pre-test scăzută spre intermediară
        - Screening asimptomatic la pacienți cu antecedente heredo-colaterale precoce
        - Hipercolesterolemie / dislipidemie moderat-severă
        - Factori multipli de risc cardiovascular asociați

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular (Cord)*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu picioarele înainte
    - **Repaus Alimentar (NPO):** Fără repaus alimentar strict; fără cafea/fumat cu 4 ore înainte
    - **Premedicație / Pregătire:**
        - Fără premedicație de rutină

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
    | **Curent Tub (mAs)** | Auto (doză redusă) |
    | **Control Automat al Expunerii (AEC)** | Modulare ECG activată (pulsare conform ritmului cardiac) |
    | **Grosime Secțiune Achiziție (Slice)** | 3 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 128 × 0.6 mm |
    | **Timp de Rotație** | 0.28-0.35 s |
    | **Pitch (Factor Pas)** | 1.0-1.2 |
    | **Mod Scanare** | Elicoidal sincronizat ECG (sau Secvențial prospectiv) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Sincronizare ECG prospectivă. Instrucțiuni de apnee inspiratorie fără Valsalva. Pentru echipamente single-source: scanare în telediastolă dacă FC < 63 bpm, altfel telediastolă și telesistolă. Pentru dual-source: telediastolă dacă FC < 79 bpm. Asigurați contact optim al electrozilor ECG. Țintă: FC <= 60 bpm, ritm regulat.

    === "Note Asistent"

        - Nu este necesară linie venoasă.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică (fără contrast)
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Verificați eventualele artefacte de mișcare pe câmpul pulmonar extins. Calcularea scorului Agatston total și pe fiecare trunchi coronarian. Raportați percentila conform vârstei și sexului. Menționați descoperirile extracardiace.

    === "Sfaturi & Recomandări"

        - Traseu ECG stabil fără paraziți. Antrenamentul apneei pacientului înainte de scanare este esențial.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Scor de Calciu | Carenă | Sub vârful cordului | 0 sec | 3 mm | Achiziție secvențială axială sincronizată ECG prospectiv |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Scor de Calciu | Cord | 3 mm/3 mm | Standard |  | Pentru calcularea scorului Agatston |
    | Axial | Scor de Calciu | Torace | 1.5 mm/1.5 mm | Lung |  | Câmp pulmonar pentru decelarea anomaliilor extracardiace |
