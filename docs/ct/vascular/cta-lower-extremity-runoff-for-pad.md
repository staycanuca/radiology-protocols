---
author: null
category: vascular
clinical_indications:
- Boală arterială periferică (arteriopatie obliterantă a membrelor inferioare - AOMI)
- Claudicație intermitentă la distanțe mici
- Ischemie critică de membru (dureri de repaus, leziuni trofice, gangrenă)
- Planificare pre-operatorie by-pass vascular sau angioplastie/stentare
contrast:
  agent: Isovue 370
  duration: 35s (5s rapid la 5-6 mL/s urmat de 30s la 3-4 mL/s)
  flow_rate: 3-4 mL/s
  roi: Aorta abdominală
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 150 HU
  volume: 1.9 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții MIP și 3D VR. MPR curbat pentru fiecare segment
    arterial. Tehnici de substracție osoasă pentru vizualizarea vaselor mici calcificate.
  nursing: Linie venoasă 18-20G în plica cotului, suportând debite de până la 5-6
    mL/s.
  rad: Evaluați etajele aorto-iliac, femuro-popliteu și infra-popliteu/tibial. Stadializați
    stenozele (ușoare, moderate, strânse). Identificați ocluziile și lungimea acestora.
    Evaluați patul vascular distal de revascularizare (runoff vascular).
  tech: Scanare de la diafragm până la degetele picioarelor. Fixați picioarele cu
    bandă adezivă pentru imobilizare. Urmărire automată a bolusului. Extindeți timpul
    de întârziere dacă este cunoscută o AOMI severă cu flux extrem de lent. Acoperire
    obligatorie a vaselor gambei și pedioase.
  tips: Membrele perfect drepte, fără rotație. Îndepărtați încălțămintea și orice
    obiecte metalice.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu picioarele imobilizate ușor orientate median
premedication: ''
protocol_type: vascular
recons:
- acquisition: Angio-CT Arterial
  fov: Membre inferioare
  kernel: Vascular
  notes: Evaluarea tuturor segmentelor vasculare
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Angio-CT Arterial
  fov: Membre inferioare
  kernel: Vascular
  notes: MIP complet al arborelui arterial
  plane: Coronal
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Angio-CT Arterial
  fov: Membre inferioare
  kernel: Vascular
  notes: Vederi sagitale ale traiectului vascular
  plane: Sagital
  thickness_increment: 2 mm/2 mm
- acquisition: Angio-CT Arterial
  fov: Membre inferioare
  kernel: Vascular
  notes: Randare 3D pentru planificare chirurgicală și angioplastie
  plane: 3D VR
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m² (risc crescut la vasculopați diabetici)
series:
- delay: Urmărire bolus
  end: Glezne
  name: Angio-CT Arterial
  notes: Viteză a mesei adaptată fluxului distal
  start: Artere renale
  thickness: 0.625 mm
- delay: Post-arterial
  end: Picior / Degete
  name: Angio-CT Runoff Distal
  notes: Fază de umplere tardivă a axului tibial și arcadelor plantare
  start: Mijlocul coapsei
  thickness: 0.625 mm
slug: cta-lower-extremity-runoff-for-pad
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: 100-120
  mas: Auto (referință 250 mAs)
  pitch: 1.2-1.5
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Membre Inferioare (Runoff pentru Boală Arterială Periferică)
---

# Angio-CT Membre Inferioare (Runoff pentru Boală Arterială Periferică)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Arterial | Urmărire bolus | Artere renale → Glezne |
        | Angio-CT Runoff Distal | Post-arterial | Mijlocul coapsei → Picior / Degete |

    === "Indicații Clinice"

        - Boală arterială periferică (arteriopatie obliterantă a membrelor inferioare - AOMI)
        - Claudicație intermitentă la distanțe mici
        - Ischemie critică de membru (dureri de repaus, leziuni trofice, gangrenă)
        - Planificare pre-operatorie by-pass vascular sau angioplastie/stentare

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular & Sistem vascular*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu picioarele imobilizate ușor orientate median
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.9 mL/kg |
        | Rată de Flux | 3-4 mL/s |
        | Durată | 35s (5s rapid la 5-6 mL/s urmat de 30s la 3-4 mL/s) |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Aorta abdominală |
        | Declanșator (HU) | 150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100-120 kV |
    | **Curent Tub (mAs)** | Auto (referință 250 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.2-1.5 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare de la diafragm până la degetele picioarelor. Fixați picioarele cu bandă adezivă pentru imobilizare. Urmărire automată a bolusului. Extindeți timpul de întârziere dacă este cunoscută o AOMI severă cu flux extrem de lent. Acoperire obligatorie a vaselor gambei și pedioase.

    === "Note Asistent"

        - Linie venoasă 18-20G în plica cotului, suportând debite de până la 5-6 mL/s.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m² (risc crescut la vasculopați diabetici)
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Evaluați etajele aorto-iliac, femuro-popliteu și infra-popliteu/tibial. Stadializați stenozele (ușoare, moderate, strânse). Identificați ocluziile și lungimea acestora. Evaluați patul vascular distal de revascularizare (runoff vascular).

    === "Sfaturi & Recomandări"

        - Membrele perfect drepte, fără rotație. Îndepărtați încălțămintea și orice obiecte metalice.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Arterial | Artere renale | Glezne | Urmărire bolus | 0.625 mm | Viteză a mesei adaptată fluxului distal |
    | Angio-CT Runoff Distal | Mijlocul coapsei | Picior / Degete | Post-arterial | 0.625 mm | Fază de umplere tardivă a axului tibial și arcadelor plantare |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Arterial | Membre inferioare | 1.25 mm/1.25 mm | Vascular |  | Evaluarea tuturor segmentelor vasculare |
    | Coronal | Angio-CT Arterial | Membre inferioare | 2.5 mm/2.5 mm | Vascular |  | MIP complet al arborelui arterial |
    | Sagital | Angio-CT Arterial | Membre inferioare | 2 mm/2 mm | Vascular |  | Vederi sagitale ale traiectului vascular |
    | 3D VR | Angio-CT Arterial | Membre inferioare | 1 mm/1 mm | Vascular |  | Randare 3D pentru planificare chirurgicală și angioplastie |
