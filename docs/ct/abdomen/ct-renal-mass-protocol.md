---
author: null
category: abdomen
clinical_indications:
- Caracterizarea maselor și formațiunilor renale solide
- Stadializarea carcinomului cu celule renale (RCC)
- Evaluarea și clasificarea Bosniak a chisturilor renale complexe
contrast:
  agent: Isovue 370
  duration: 18-22s + 20-30s
  flow_rate: 3-4 mL/s
  timing: Tehnică Split-Bolus dedicată renală
  volume: 'Tehnică Split Bolus: prima injectare 1.1 mL/kg + a doua injectare 0.4 mL/kg'
last_updated: '2026-01-01'
notes:
  additional_recons: Comparați nativ vs. corticomedular vs. nefrografic. Măsurare
    precisă HU în leziune. MIP urografic.
  nursing: Abord venos 18-20G. Explicați pacientului etapele injectării și pauzele
    dintre serii.
  rad: 'Nativ: detecția grăsimii microscopice/macroscopice (angiomiolipom) și calcificărilor.
    Corticomedulară: vascularizație tumorală și variante arteriale. Nefrografică:
    cea mai sensibilă pentru decelarea tumorilor hipovasculare și invazia venei renale/VCI.'
  tech: 'Protocol MULTIFAZIC: 1) Nativ 2) Fază corticomedulară (arterială) la 25-30s
    3) Fază nefrografică la 90-100s 4) Fază excretorie la 5-7 min.'
  tips: Temporizarea fazei nefrografice este cea mai importantă pentru detectarea
    și caracterizarea masei. Măsurători ROI atente pe nativ și faza de încărcare maximă
    (>15-20 HU creștere = încărcare semnificativă).
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: Fără contrast oral pozitiv.
protocol_type: contrast-enhanced
recons:
- acquisition: Fază Nativă
  fov: Rinichi
  kernel: Standard
  notes: Caracterizare densitometrică nativă
  plane: Axial
  thickness_increment: 2 mm/2 mm
- acquisition: Fază Corticomedulară
  fov: Rinichi
  kernel: Standard
  notes: Încărcare corticală și vascularizație
  plane: Axial
  thickness_increment: 2 mm/2 mm
- acquisition: Fază Nefrografică
  fov: Rinichi
  kernel: Standard
  notes: Omogenitate parenchimatoasă și extensie tumorală
  plane: Axial
  thickness_increment: 2 mm/2 mm
- acquisition: Fază Nefrografică
  fov: Abdomen
  kernel: Standard
  notes: Comparație faze în plan coronal
  plane: Coronal
  thickness_increment: 2.5 mm/2.5 mm
safety:
  allergy: Verificați istoricul alergic.
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 0 sec
  end: 1-2cm sub rinichi
  name: Fază Nativă
  notes: Determinarea densității bazale a masei renale
  start: 1-2cm deasupra rinichilor
  thickness: 0.625 mm
- delay: 25-30 sec
  end: Creste iliace
  name: Fază Corticomedulară
  notes: Anatomie arterială și tumori hipervasculare
  start: Diafragm
  thickness: 0.625 mm
- delay: 90-100 sec
  end: Creste iliace
  name: Fază Nefrografică
  notes: Încărcare omogenă a parenchimului renal
  start: Diafragm
  thickness: 0.625 mm
slug: ct-renal-mass-protocol
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: 100-120
  mas: Auto (referință 200 mAs)
  pitch: '1'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Protocol Masă Renală (Multifazic)
---

# CT Protocol Masă Renală (Multifazic)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă | 0 sec | 1-2cm deasupra rinichilor → 1-2cm sub rinichi |
        | Fază Corticomedulară | 25-30 sec | Diafragm → Creste iliace |
        | Fază Nefrografică | 90-100 sec | Diafragm → Creste iliace |

    === "Indicații Clinice"

        - Caracterizarea maselor și formațiunilor renale solide
        - Stadializarea carcinomului cu celule renale (RCC)
        - Evaluarea și clasificarea Bosniak a chisturilor renale complexe

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Fără contrast oral pozitiv.

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | Tehnică Split Bolus: prima injectare 1.1 mL/kg + a doua injectare 0.4 mL/kg |
        | Rată de Flux | 3-4 mL/s |
        | Durată | 18-22s + 20-30s |
        | Metodă Temporizare | Tehnică Split-Bolus dedicată renală |
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
    | **Tensiune Tub (kV)** | 100-120 kV |
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

        - Protocol MULTIFAZIC: 1) Nativ 2) Fază corticomedulară (arterială) la 25-30s 3) Fază nefrografică la 90-100s 4) Fază excretorie la 5-7 min.

    === "Note Asistent"

        - Abord venos 18-20G. Explicați pacientului etapele injectării și pauzele dintre serii.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic.

    === "Note Radiolog"

        - Nativ: detecția grăsimii microscopice/macroscopice (angiomiolipom) și calcificărilor. Corticomedulară: vascularizație tumorală și variante arteriale. Nefrografică: cea mai sensibilă pentru decelarea tumorilor hipovasculare și invazia venei renale/VCI.

    === "Sfaturi & Recomandări"

        - Temporizarea fazei nefrografice este cea mai importantă pentru detectarea și caracterizarea masei. Măsurători ROI atente pe nativ și faza de încărcare maximă (>15-20 HU creștere = încărcare semnificativă).

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă | 1-2cm deasupra rinichilor | 1-2cm sub rinichi | 0 sec | 0.625 mm | Determinarea densității bazale a masei renale |
    | Fază Corticomedulară | Diafragm | Creste iliace | 25-30 sec | 0.625 mm | Anatomie arterială și tumori hipervasculare |
    | Fază Nefrografică | Diafragm | Creste iliace | 90-100 sec | 0.625 mm | Încărcare omogenă a parenchimului renal |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Nativă | Rinichi | 2 mm/2 mm | Standard |  | Caracterizare densitometrică nativă |
    | Axial | Fază Corticomedulară | Rinichi | 2 mm/2 mm | Standard |  | Încărcare corticală și vascularizație |
    | Axial | Fază Nefrografică | Rinichi | 2 mm/2 mm | Standard |  | Omogenitate parenchimatoasă și extensie tumorală |
    | Coronal | Fază Nefrografică | Abdomen | 2.5 mm/2.5 mm | Standard |  | Comparație faze în plan coronal |
