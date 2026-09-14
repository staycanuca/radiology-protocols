---
author: null
category: msk
clinical_indications:
- Planificare pre-operatorie ortopedică sau tumorală
- Bilanț post-operator al consolidării sau complicațiilor
- Suspiciune de proces infecțios musculoscheletic (osteomielită, flegmon, abces de
  părți moi)
- Formațiune tumorală de părți moi sau osoasă primară/secundară
contrast:
  agent: Omnipaque 350 dacă se administrează contrast
  flow_rate: 2-3 mL/s
  volume: 100 mL dacă se administrează contrast
last_updated: '2026-01-01'
notes:
  additional_recons: Comparație cu partea controlaterală. Măsurarea exactă a dimensiunilor
    leziunii. Reconstrucții atât în fereastră de os cât și în fereastră de părți moi.
  nursing: Linie venoasă pentru studiile cu contrast. Consemnați antecedentele traumatice
    sau chirurgicale.
  rad: 'Nativ: calcificări, matrice osoasă, hematoame. Contrast: modelul de încărcare
    al masei (omogen, periferic, septal). Tardiv: încărcare persistentă sau spălare
    (washout). Evaluarea invaziei osoase și a raporturilor vasculo-nervoase.'
  tech: Câmp de vedere adaptat strict regiunii. Achiziție submilimetrică dacă este
    necesară randare 3D. Nativ și/sau fază cu substanță de contrast în funcție de
    indicație. Fază tardivă la 5-10 minute pentru infecție sau tumoră.
  tips: Personalizați protocolul în funcție de întrebarea clinică. Examinarea segmentului
    contralateral poate fi utilă pentru comparație.
npo: Repaus alimentar 4 ore dacă se administrează contrast
position: În funcție de segmentul anatomic investigat; imobilizare stabilă
premedication: ''
protocol_type: contrast-enhanced
recons:
- acquisition: Fază cu Contrast
  fov: Regiune MSK
  kernel: Bone and Standard
  notes: Serii primare în fereastră osoasă și părți moi
  plane: Axial
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Fază cu Contrast
  fov: Regiune MSK
  kernel: Bone and Standard
  notes: Reformatări coronale multiplanare
  plane: Coronal
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Fază cu Contrast
  fov: Regiune MSK
  kernel: Bone and Standard
  notes: Reformatări sagitale
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Fază Nativă
  fov: Regiune MSK
  kernel: Bone
  notes: Randare tridimensională 3D pentru planificare chirurgicală
  plane: 3D if needed
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m² dacă se administrează contrast
series:
- delay: 0 sec
  end: Regiunea anatomică
  name: Fază Nativă
  notes: Examinare nativă de referință
  start: Regiunea anatomică
  thickness: 1 mm
- delay: 60-70 sec
  end: Regiunea anatomică
  name: Fază cu Contrast
  notes: Evaluarea încărcării vasculare și a vascularizației lezionale
  start: Regiunea anatomică
  thickness: 1 mm
- delay: 300 sec (5 min)
  end: Regiunea anatomică
  name: Fază Tardivă
  notes: Pentru delimitarea abcesului sau caracterizarea tumorală
  start: Regiunea anatomică
  thickness: 1 mm
slug: msk-protocol-general
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200-250 mAs)
  pitch: Helical
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 1 mm
title: CT Musculoscheletic General (Părți Moi / Osos)
---

# CT Musculoscheletic General (Părți Moi / Osos)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă | 0 sec | Regiunea anatomică → Regiunea anatomică |
        | Fază cu Contrast | 60-70 sec | Regiunea anatomică → Regiunea anatomică |
        | Fază Tardivă | 300 sec (5 min) | Regiunea anatomică → Regiunea anatomică |

    === "Indicații Clinice"

        - Planificare pre-operatorie ortopedică sau tumorală
        - Bilanț post-operator al consolidării sau complicațiilor
        - Suspiciune de proces infecțios musculoscheletic (osteomielită, flegmon, abces de părți moi)
        - Formațiune tumorală de părți moi sau osoasă primară/secundară

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat locomotor & Articulații*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** În funcție de segmentul anatomic investigat; imobilizare stabilă
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore dacă se administrează contrast
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 dacă se administrează contrast |
        | Volum | 100 mL dacă se administrează contrast |
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
    | **Curent Tub (mAs)** | Auto (referință 200-250 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 1 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Câmp de vedere adaptat strict regiunii. Achiziție submilimetrică dacă este necesară randare 3D. Nativ și/sau fază cu substanță de contrast în funcție de indicație. Fază tardivă la 5-10 minute pentru infecție sau tumoră.

    === "Note Asistent"

        - Linie venoasă pentru studiile cu contrast. Consemnați antecedentele traumatice sau chirurgicale.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m² dacă se administrează contrast
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Nativ: calcificări, matrice osoasă, hematoame. Contrast: modelul de încărcare al masei (omogen, periferic, septal). Tardiv: încărcare persistentă sau spălare (washout). Evaluarea invaziei osoase și a raporturilor vasculo-nervoase.

    === "Sfaturi & Recomandări"

        - Personalizați protocolul în funcție de întrebarea clinică. Examinarea segmentului contralateral poate fi utilă pentru comparație.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă | Regiunea anatomică | Regiunea anatomică | 0 sec | 1 mm | Examinare nativă de referință |
    | Fază cu Contrast | Regiunea anatomică | Regiunea anatomică | 60-70 sec | 1 mm | Evaluarea încărcării vasculare și a vascularizației lezionale |
    | Fază Tardivă | Regiunea anatomică | Regiunea anatomică | 300 sec (5 min) | 1 mm | Pentru delimitarea abcesului sau caracterizarea tumorală |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază cu Contrast | Regiune MSK | 1.5 mm/1.5 mm | Bone and Standard |  | Serii primare în fereastră osoasă și părți moi |
    | Coronal | Fază cu Contrast | Regiune MSK | 1.5 mm/1.5 mm | Bone and Standard |  | Reformatări coronale multiplanare |
    | Sagital | Fază cu Contrast | Regiune MSK | 1.5 mm/1.5 mm | Bone and Standard |  | Reformatări sagitale |
    | 3D if needed | Fază Nativă | Regiune MSK | 1 mm/1 mm | Bone |  | Randare tridimensională 3D pentru planificare chirurgicală |
