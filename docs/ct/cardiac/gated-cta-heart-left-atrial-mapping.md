---
author: null
category: cardiac
clinical_indications:
- Planificare pre-intervențională pentru ablația de fibrilație atrială (izolare de
  vene pulmonare)
- Evaluarea morfologiei și anomaliilor de drenaj ale venelor pulmonare
- Excluderea trombozei de urechiușă atrială stângă (LAA)
contrast:
  agent: Isovue 370
  duration: 15 sec
  flow_rate: 5 mL/s
  roi: Atriul stâng
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 200 HU
  volume: 1.1 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Randare tridimensională 3D a atriului stâng pentru integrare
    în sistemul de electrofiziologie (Carto/EnSite). Măsurători ostiale (arii, diametre
    maxime/minime). Morfologia LAA. Poziția esofagului.
  nursing: Linie venoasă 20G.
  rad: Cartografierea detaliată a anatomiei venelor pulmonare (număr, trunchiuri comune,
    diametre ostiale, variante anatomice). Morfologia urechiușei atriului stâng. Raportul
    anatomic cu esofagul.
  tech: Sincronizare retrospectivă. Focus pe atriul stâng și confluența venelor pulmonare.
    Secțiuni submilimetrice critice. Câmp extins pentru a include toate ostiile venoase
    pulmonare.
  tips: Secțiuni fine esențiale. Acoperire completă a tuturor venelor pulmonare. Descrieți
    prezența trunchiului comun stâng sau a venelor accesorii drepte.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu picioarele înainte
premedication: HR < 65 preferred. Premedication not required.
protocol_type: cardiac gated
recons:
- acquisition: Angio-CT Sincronizat ECG
  fov: Atriu stâng
  kernel: Cardiac
  notes: Anatomie primară a venelor pulmonare și AS
  plane: Axial
  thickness_increment: 0.75 mm/0.75 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Atriu stâng
  kernel: Cardiac
  notes: Plan coronal 'en face' pe ostiile venelor pulmonare
  plane: Coronal
  thickness_increment: 1 mm/1 mm
- acquisition: Angio-CT Sincronizat ECG
  fov: Atriu stâng
  kernel: Cardiac
  notes: Vederi sagitale laterale ale venelor pulmonare
  plane: Sagital
  thickness_increment: 1 mm/1 mm
- acquisition: Angio-CT Tardiv
  fov: Atriu stâng
  kernel: Cardiac
  notes: Evaluare tromb urechiușă atrială stângă pe seria tardivă
  plane: Axial
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: Urmărire bolus
  end: Sub atriul stâng
  name: Angio-CT Sincronizat ECG
  notes: Sincronizare retrospectivă - secțiuni fine obligatorii
  start: Vene pulmonare superioare
  thickness: 0.625 mm
- delay: 30 sec
  end: Sub atriul stâng
  name: Angio-CT Tardiv
  notes: Fază tardivă pentru diferențiere stază vs. tromb în urechiușă
  start: Vene pulmonare superioare
  thickness: 0.625 mm
slug: gated-cta-heart-left-atrial-mapping
synonyms: []
tech_params:
  aec: Modulare ECG activată (pulsare conform ritmului cardiac)
  collimation: 64 × 0.625 mm sau 128 × 0.6 mm
  kv: '100'
  mas: Auto (modulare sincronizată ECG)
  pitch: 0.2-0.24
  rotation_time: 0.28s
  scan_mode: Elicoidal sincronizat ECG (sau Secvențial prospectiv)
  slice_thickness: 0.625 mm
title: Angio-CT Cardiac Sincronizat ECG Cartografiere Atriu Stâng & Vene Pulmonare
---

# Angio-CT Cardiac Sincronizat ECG Cartografiere Atriu Stâng & Vene Pulmonare

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Sincronizat ECG | Urmărire bolus | Vene pulmonare superioare → Sub atriul stâng |
        | Angio-CT Tardiv | 30 sec | Vene pulmonare superioare → Sub atriul stâng |

    === "Indicații Clinice"

        - Planificare pre-intervențională pentru ablația de fibrilație atrială (izolare de vene pulmonare)
        - Evaluarea morfologiei și anomaliilor de drenaj ale venelor pulmonare
        - Excluderea trombozei de urechiușă atrială stângă (LAA)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular (Cord)*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu picioarele înainte
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - HR < 65 preferred. Premedication not required.

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.1 mL/kg |
        | Rată de Flux | 5 mL/s |
        | Durată | 15 sec |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Atriul stâng |
        | Declanșator (HU) | 200 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 kV |
    | **Curent Tub (mAs)** | Auto (modulare sincronizată ECG) |
    | **Control Automat al Expunerii (AEC)** | Modulare ECG activată (pulsare conform ritmului cardiac) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 128 × 0.6 mm |
    | **Timp de Rotație** | 0.28 s |
    | **Pitch (Factor Pas)** | 0.2-0.24 |
    | **Mod Scanare** | Elicoidal sincronizat ECG (sau Secvențial prospectiv) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Sincronizare retrospectivă. Focus pe atriul stâng și confluența venelor pulmonare. Secțiuni submilimetrice critice. Câmp extins pentru a include toate ostiile venoase pulmonare.

    === "Note Asistent"

        - Linie venoasă 20G.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Cartografierea detaliată a anatomiei venelor pulmonare (număr, trunchiuri comune, diametre ostiale, variante anatomice). Morfologia urechiușei atriului stâng. Raportul anatomic cu esofagul.

    === "Sfaturi & Recomandări"

        - Secțiuni fine esențiale. Acoperire completă a tuturor venelor pulmonare. Descrieți prezența trunchiului comun stâng sau a venelor accesorii drepte.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Sincronizat ECG | Vene pulmonare superioare | Sub atriul stâng | Urmărire bolus | 0.625 mm | Sincronizare retrospectivă - secțiuni fine obligatorii |
    | Angio-CT Tardiv | Vene pulmonare superioare | Sub atriul stâng | 30 sec | 0.625 mm | Fază tardivă pentru diferențiere stază vs. tromb în urechiușă |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Sincronizat ECG | Atriu stâng | 0.75 mm/0.75 mm | Cardiac |  | Anatomie primară a venelor pulmonare și AS |
    | Coronal | Angio-CT Sincronizat ECG | Atriu stâng | 1 mm/1 mm | Cardiac |  | Plan coronal 'en face' pe ostiile venelor pulmonare |
    | Sagital | Angio-CT Sincronizat ECG | Atriu stâng | 1 mm/1 mm | Cardiac |  | Vederi sagitale laterale ale venelor pulmonare |
    | Axial | Angio-CT Tardiv | Atriu stâng | 1 mm/1 mm | Cardiac |  | Evaluare tromb urechiușă atrială stângă pe seria tardivă |
