---
author: null
category: cardiac
clinical_indications:
- Planificare pre-operatorie pentru resternotomie (chirurgie cardiacă secundară/iterativă)
- Evaluarea raporturilor structurilor mediastinale anterioare cu sternul
- Măsurarea distanței dintre peretele posterior sternal și cord / by-pass-uri
contrast:
  agent: Isovue 370
  duration: 15s
  flow_rate: 5 mL/s
  roi: Aorta ascendentă
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 180 HU
  volume: 1.2 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Randare 3D VR a rețelei venoase retrosternale. Măsurători precise
    ale distanței stern-ventricul drept, stern-aortă ascendentă și stern-grefon LIMA/SVG.
  nursing: Linie venoasă 20G.
  rad: 'Sincronizat: anatomia cardiacă și a vaselor mari. Arterial: patul vascular
    sistemic. Venoasă: venele retrosternale (trunchi brahiocefalic stâng, VMS) și
    aderențele la peretele sternal, esențiale pentru incizia chirurgicală în siguranță.'
  tech: 'TREI achiziții: 1) Angio-CT Torace sincronizat ECG retrospectiv 2) Flash
    spiral toraco-abdomino-pelvin 3) Flebografie toracică la 60s întârziere pentru
    structurile venoase retrosternale.'
  tips: Faza venoasă este critică pentru chirurgul cardiovascular. Cartografiați toate
    structurile retrosternale aderente.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: HR < 65 target. Premedication not required.
protocol_type: cardiac gated
recons:
- acquisition: Angio-CT Torace Sincronizat
  fov: Cord
  kernel: Cardiac
  notes: Anatomie cardiacă și traiectul grefoanelor
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Fază Venoasă Torace
  fov: Torace
  kernel: Standard
  notes: Raportul structurilor retrosternale pe faza venoasă
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Fază Venoasă Torace
  fov: Torace
  kernel: Standard
  notes: Structurile peretelui toracic anterior
  plane: Coronal
  thickness_increment: 2 mm/2 mm
- acquisition: Fază Venoasă Torace
  fov: Torace
  kernel: Standard
  notes: Hartă 3D a vaselor retrosternale pentru planificare chirurgicală
  plane: 3D VR
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Verificați istoricul alergic la contrast
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: Urmărire bolus
  end: Diafragm
  name: Angio-CT Torace Sincronizat
  notes: Sincronizare retrospectivă ECG pentru cord
  start: Apertura toracică superioară
  thickness: 0.625 mm
- delay: Post-torace
  end: Simfiză pubiană
  name: Flash AP
  notes: Fază arterială abdomen și pelvis
  start: Diafragm
  thickness: 1 mm
- delay: 60 sec
  end: Diafragm
  name: Fază Venoasă Torace
  notes: Structuri venoase retrosternale și mediastin anterior
  start: Apertura toracică superioară
  thickness: 0.625 mm
slug: gated-cta-cap-sternotomy-revision
synonyms: []
tech_params:
  aec: Modulare ECG activată (pulsare conform ritmului cardiac)
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: '100'
  mas: Auto modulare ECG torace / Curent crescut alte serii
  pitch: 0.2-0.24 / 1.2-1.5
  rotation_time: 0.28 / 0.5s
  scan_mode: Elicoidal sincronizat ECG (sau Secvențial prospectiv)
  slice_thickness: 0.625 mm
title: Angio-CT Sincronizat ECG Torace-Abdomen-Pelvis (Bilanț Resternotomie)
---

# Angio-CT Sincronizat ECG Torace-Abdomen-Pelvis (Bilanț Resternotomie)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Torace Sincronizat | Urmărire bolus | Apertura toracică superioară → Diafragm |
        | Flash AP | Post-torace | Diafragm → Simfiză pubiană |
        | Fază Venoasă Torace | 60 sec | Apertura toracică superioară → Diafragm |

    === "Indicații Clinice"

        - Planificare pre-operatorie pentru resternotomie (chirurgie cardiacă secundară/iterativă)
        - Evaluarea raporturilor structurilor mediastinale anterioare cu sternul
        - Măsurarea distanței dintre peretele posterior sternal și cord / by-pass-uri

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular (Cord)*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - HR < 65 target. Premedication not required.

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.2 mL/kg |
        | Rată de Flux | 5 mL/s |
        | Durată | 15s |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Aorta ascendentă |
        | Declanșator (HU) | 180 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 kV |
    | **Curent Tub (mAs)** | Auto modulare ECG torace / Curent crescut alte serii |
    | **Control Automat al Expunerii (AEC)** | Modulare ECG activată (pulsare conform ritmului cardiac) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 128 × 0.6 mm |
    | **Timp de Rotație** | 0.28 / 0.5 s |
    | **Pitch (Factor Pas)** | 0.2-0.24 / 1.2-1.5 |
    | **Mod Scanare** | Elicoidal sincronizat ECG (sau Secvențial prospectiv) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - TREI achiziții: 1) Angio-CT Torace sincronizat ECG retrospectiv 2) Flash spiral toraco-abdomino-pelvin 3) Flebografie toracică la 60s întârziere pentru structurile venoase retrosternale.

    === "Note Asistent"

        - Linie venoasă 20G.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic la contrast

    === "Note Radiolog"

        - Sincronizat: anatomia cardiacă și a vaselor mari. Arterial: patul vascular sistemic. Venoasă: venele retrosternale (trunchi brahiocefalic stâng, VMS) și aderențele la peretele sternal, esențiale pentru incizia chirurgicală în siguranță.

    === "Sfaturi & Recomandări"

        - Faza venoasă este critică pentru chirurgul cardiovascular. Cartografiați toate structurile retrosternale aderente.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Torace Sincronizat | Apertura toracică superioară | Diafragm | Urmărire bolus | 0.625 mm | Sincronizare retrospectivă ECG pentru cord |
    | Flash AP | Diafragm | Simfiză pubiană | Post-torace | 1 mm | Fază arterială abdomen și pelvis |
    | Fază Venoasă Torace | Apertura toracică superioară | Diafragm | 60 sec | 0.625 mm | Structuri venoase retrosternale și mediastin anterior |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Torace Sincronizat | Cord | 1.25 mm/1.25 mm | Cardiac |  | Anatomie cardiacă și traiectul grefoanelor |
    | Axial | Fază Venoasă Torace | Torace | 1.25 mm/1.25 mm | Standard |  | Raportul structurilor retrosternale pe faza venoasă |
    | Coronal | Fază Venoasă Torace | Torace | 2 mm/2 mm | Standard |  | Structurile peretelui toracic anterior |
    | 3D VR | Fază Venoasă Torace | Torace | 1 mm/1 mm | Standard |  | Hartă 3D a vaselor retrosternale pentru planificare chirurgicală |
