---
author: null
category: neuro
clinical_indications:
- Hiperparatiroidism primar sau secundar refractar
- Localizarea pre-operatorie a adenomului paratiroidian (eutopic sau ectopic)
- Chirurgie paratiroidiană minim invazivă orientată
contrast:
  agent: Omnipaque 350
  flow_rate: 4 mL/s
  roi: Artera carotidă
  timing: 'Protocol 4D multifazic: Nativ + Arterial + Venoasă + Tardiv'
  trigger: 150 HU
  volume: 75-100 mL
last_updated: '2026-01-01'
notes:
  additional_recons: Imagini de substracție (arterial minus nativ). Comparație densitometrică
    în 4 faze. Măsurarea dimensiunilor și a raporturilor topografice pentru chirurg.
  nursing: Linie venoasă 18-20G cu debit mare (4 mL/s). Instruiți pacientul să nu
    înghită în timpul scanării.
  rad: 'Adenomul paratiroidian prezintă cinetică tipică: hipodens pe nativ, încărcare
    intensă precoce în faza arterială (''lights up'') și spălare rapidă (washout)
    în fazele venoasă și tardivă (spre deosebire de tiroidă și ganglioni).'
  tech: 'PATRU faze sincronizate: 1) Nativ 2) Fază arterială la 25s 3) Fază venoasă
    la 55-60s 4) Fază tardivă/washout la 90s. De la baza craniului până la nivelul
    carenei/mediastinului anterior pentru adenoame ectopice.'
  tips: Protocolul cu 4 faze oferă o sensibilitate superioară ecografiei și scintigrafiei
    MIBI. Căutați adenoame ectopice mediastinale.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu capul în extensie ușoară și umerii coborâți
premedication: ''
protocol_type: contrast-enhanced
recons:
- acquisition: Fază Arterială
  fov: Gât-Mediastin
  kernel: Standard
  notes: Comparație dinamică între toate cele 4 faze
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Fază Arterială
  fov: Gât
  kernel: Standard
  notes: Vârful încărcării adenomului paratiroidian
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Fază Arterială
  fov: Gât
  kernel: Standard
  notes: Substracție digitală pentru evidențierea adenomului
  plane: Subtraction
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Fază Arterială
  fov: Gât-Mediastin
  kernel: Standard
  notes: Plan coronal pentru căutarea adenoamelor ectopice mediastinale
  plane: Coronal
  thickness_increment: 1.5 mm/1.5 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 0 sec
  end: Carenă
  name: Fază Nativă
  notes: Referință nativă
  start: Baza craniului
  thickness: 0.625 mm
- delay: 25 sec
  end: Carenă
  name: Fază Arterială
  notes: Încărcare arterială maximă a adenomului paratiroidian
  start: Baza craniului
  thickness: 0.625 mm
- delay: 55 sec
  end: Carenă
  name: Fază Venoasă
  notes: Încărcare tiroidiană maximă
  start: Baza craniului
  thickness: 0.625 mm
- delay: 90 sec
  end: Carenă
  name: Fază Tardivă
  notes: Fază de spălare (washout) a adenomului
  start: Baza craniului
  thickness: 0.625 mm
slug: ct-parathyroid-4d
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200 mAs)
  pitch: '1'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT 4D Glande Paratiroide
---

# CT 4D Glande Paratiroide

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă | 0 sec | Baza craniului → Carenă |
        | Fază Arterială | 25 sec | Baza craniului → Carenă |
        | Fază Venoasă | 55 sec | Baza craniului → Carenă |
        | Fază Tardivă | 90 sec | Baza craniului → Carenă |

    === "Indicații Clinice"

        - Hiperparatiroidism primar sau secundar refractar
        - Localizarea pre-operatorie a adenomului paratiroidian (eutopic sau ectopic)
        - Chirurgie paratiroidiană minim invazivă orientată

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul în extensie ușoară și umerii coborâți
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volum | 75-100 mL |
        | Rată de Flux | 4 mL/s |
        | Durată |  |
        | Metodă Temporizare | Protocol 4D multifazic: Nativ + Arterial + Venoasă + Tardiv |
        | Poziționare ROI | Artera carotidă |
        | Declanșator (HU) | 150 HU |

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
    | **Pitch (Factor Pas)** | 1 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - PATRU faze sincronizate: 1) Nativ 2) Fază arterială la 25s 3) Fază venoasă la 55-60s 4) Fază tardivă/washout la 90s. De la baza craniului până la nivelul carenei/mediastinului anterior pentru adenoame ectopice.

    === "Note Asistent"

        - Linie venoasă 18-20G cu debit mare (4 mL/s). Instruiți pacientul să nu înghită în timpul scanării.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Adenomul paratiroidian prezintă cinetică tipică: hipodens pe nativ, încărcare intensă precoce în faza arterială ('lights up') și spălare rapidă (washout) în fazele venoasă și tardivă (spre deosebire de tiroidă și ganglioni).

    === "Sfaturi & Recomandări"

        - Protocolul cu 4 faze oferă o sensibilitate superioară ecografiei și scintigrafiei MIBI. Căutați adenoame ectopice mediastinale.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă | Baza craniului | Carenă | 0 sec | 0.625 mm | Referință nativă |
    | Fază Arterială | Baza craniului | Carenă | 25 sec | 0.625 mm | Încărcare arterială maximă a adenomului paratiroidian |
    | Fază Venoasă | Baza craniului | Carenă | 55 sec | 0.625 mm | Încărcare tiroidiană maximă |
    | Fază Tardivă | Baza craniului | Carenă | 90 sec | 0.625 mm | Fază de spălare (washout) a adenomului |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Arterială | Gât-Mediastin | 1.25 mm/1.25 mm | Standard |  | Comparație dinamică între toate cele 4 faze |
    | Axial | Fază Arterială | Gât | 1.25 mm/1.25 mm | Standard |  | Vârful încărcării adenomului paratiroidian |
    | Subtraction | Fază Arterială | Gât | 1.25 mm/1.25 mm | Standard |  | Substracție digitală pentru evidențierea adenomului |
    | Coronal | Fază Arterială | Gât-Mediastin | 1.5 mm/1.5 mm | Standard |  | Plan coronal pentru căutarea adenoamelor ectopice mediastinale |
