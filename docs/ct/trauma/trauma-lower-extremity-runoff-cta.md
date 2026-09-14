---
author: Departamentul de Radiologie
category: trauma
clinical_indications:
- Leziune vasculară post-traumatică la nivelul membrului inferior
- Plagă penetrantă prin armă albă sau foc cu traiect vascular
- Fractură sau luxație severă asociată cu absența pulsului distal
- Sindrom de ischemie acută post-traumatică sau suspiciune de compartiment
contrast:
  agent: Omnipaque 350
  flow_rate: 4-5 mL/s
  roi: Aorta abdominală sau proximal de sediul leziunii
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 150 HU
  volume: 125 mL
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții MIP și 3D VR ale axului arterial. Documentați exact
    lungimea defectului vascular și calibrul vaselor receptoare pentru revascularizare.
  nursing: Abord venos 18-20G. Dacă există traumatism la brațul de injectare, folosiți
    brațul contralateral sau abord proximal.
  rad: 'Evaluați integritatea arterială: secționare completă, spasm marcat, pseudoanevrism
    post-traumatic, ocluzie trombotică, extravazare activă de contrast. Evaluați raportul
    fragmentelor osoase fracturate cu vasele sanguine.'
  tech: Extindeți câmpul de scanare în funcție de nivelul leziunii. De la bifurcația
    aortei până la glezne dacă este bilateral. Se poate efectua studiu unilateral
    focalizat dacă leziunea este izolată.
  tips: Adaptați acoperirea la mecanismul leziunii. Achiziție rapidă sincronizată
    cu bolusul arterial.
npo: Fără repaus alimentar - urgență traumatologică
position: Decubit dorsal cu membrele inferioare extinse
premedication: ''
protocol_type: vascular
recons:
- acquisition: Angio-CT Arterial Membre Inferioare
  fov: Membre inferioare
  kernel: Vascular
  notes: Evaluare lumen arterial și extravazare
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Angio-CT Arterial Membre Inferioare
  fov: Membre inferioare
  kernel: Vascular
  notes: Vedere de ansamblu MIP pe axul arterial
  plane: Coronal
  thickness_increment: 2 mm/2 mm
- acquisition: Angio-CT Arterial Membre Inferioare
  fov: Membre inferioare
  kernel: Vascular
  notes: Raportul axului vascular cu structurile osoase
  plane: Sagital
  thickness_increment: 2 mm/2 mm
- acquisition: Angio-CT Arterial Membre Inferioare
  fov: Membre inferioare
  kernel: Vascular
  notes: Randare tridimensională 3D VR vasculară
  plane: 3D VR
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Indicație de urgență traumatologică
  renal: Verificați dacă este disponibilă funcția renală; urgență traumatologică
series:
- delay: Urmărire bolus
  end: Distal de leziune / Glezne
  name: Angio-CT Arterial Membre Inferioare
  notes: Fază arterială runoff pentru membrele inferioare
  start: Bifurcația aortei
  thickness: 0.625 mm
slug: trauma-lower-extremity-runoff-cta
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D pentru politraumă)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: 100-120
  mas: Auto (referință 250 mAs)
  pitch: 1.2-1.5
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Membre Inferioare în Traumatism (Runoff Extremități)
sources:
- title: ACR Appropriateness Criteria — Major Blunt Trauma
  url: https://www.acr.org/clinical-resources/clinical-tools-and-reference/appropriateness-criteria
  institution: ACR
  source_region: US
  kind: Criterii de oportunitate clinică
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 7a9944bf40cbdca19afa54c99c357074c28dc49534ed1c21c814d9f71c93b198
- title: UT Southwestern Radiology — Trauma Whole-Body CT Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# Angio-CT Membre Inferioare în Traumatism (Runoff Extremități)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Arterial Membre Inferioare | Urmărire bolus | Bifurcația aortei → Distal de leziune / Glezne |

    === "Indicații Clinice"

        - Leziune vasculară post-traumatică la nivelul membrului inferior
        - Plagă penetrantă prin armă albă sau foc cu traiect vascular
        - Fractură sau luxație severă asociată cu absența pulsului distal
        - Sindrom de ischemie acută post-traumatică sau suspiciune de compartiment

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Traumatisme & Politraumă*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu membrele inferioare extinse
    - **Repaus Alimentar (NPO):** Fără repaus alimentar - urgență traumatologică
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volum | 125 mL |
        | Rată de Flux | 4-5 mL/s |
        | Durată |  |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Aorta abdominală sau proximal de sediul leziunii |
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
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D pentru politraumă) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.2-1.5 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Extindeți câmpul de scanare în funcție de nivelul leziunii. De la bifurcația aortei până la glezne dacă este bilateral. Se poate efectua studiu unilateral focalizat dacă leziunea este izolată.

    === "Note Asistent"

        - Abord venos 18-20G. Dacă există traumatism la brațul de injectare, folosiți brațul contralateral sau abord proximal.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați dacă este disponibilă funcția renală; urgență traumatologică
            - **Alergii:** Indicație de urgență traumatologică

    === "Note Radiolog"

        - Evaluați integritatea arterială: secționare completă, spasm marcat, pseudoanevrism post-traumatic, ocluzie trombotică, extravazare activă de contrast. Evaluați raportul fragmentelor osoase fracturate cu vasele sanguine.

    === "Sfaturi & Recomandări"

        - Adaptați acoperirea la mecanismul leziunii. Achiziție rapidă sincronizată cu bolusul arterial.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Arterial Membre Inferioare | Bifurcația aortei | Distal de leziune / Glezne | Urmărire bolus | 0.625 mm | Fază arterială runoff pentru membrele inferioare |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Arterial Membre Inferioare | Membre inferioare | 1.25 mm/1.25 mm | Vascular |  | Evaluare lumen arterial și extravazare |
    | Coronal | Angio-CT Arterial Membre Inferioare | Membre inferioare | 2 mm/2 mm | Vascular |  | Vedere de ansamblu MIP pe axul arterial |
    | Sagital | Angio-CT Arterial Membre Inferioare | Membre inferioare | 2 mm/2 mm | Vascular |  | Raportul axului vascular cu structurile osoase |
    | 3D VR | Angio-CT Arterial Membre Inferioare | Membre inferioare | 1 mm/1 mm | Vascular |  | Randare tridimensională 3D VR vasculară |

## Surse și revizuire

- [ACR Appropriateness Criteria — Major Blunt Trauma](https://www.acr.org/clinical-resources/clinical-tools-and-reference/appropriateness-criteria) — *ACR* (US)
- [UT Southwestern Radiology — Trauma Whole-Body CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
