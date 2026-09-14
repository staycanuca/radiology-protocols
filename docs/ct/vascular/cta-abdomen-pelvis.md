---
author: Departamentul de Radiologie
category: vascular
clinical_indications:
- Anevrism de aortă abdominală (AAA)
- Suspiciune de ischemie mezenterică
- Stenoză de arteră renală (hipertensiune renovasculară)
- Planificare pre- și post-endoprotezare aortică (EVAR)
contrast:
  agent: Isovue 370
  duration: 20s
  flow_rate: 4 mL/s
  roi: Aorta abdominală la originea trunchiului celiac
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 150 HU
  volume: 1.1 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Randare 3D VR și MPR curbat pe axul aortei și arterelor iliace.
    Măsurători ale diametrelor anevrismale în 3 planuri ortogonale pe axul lumenului.
  nursing: Linie venoasă 18-20G în plica cotului.
  rad: Măsurați diametrele AAA în 3 planuri dacă este prezent. Evaluați originea și
    calibrul arterelor renale și mezenterice. Analizați axul arterial iliac (diametru,
    calcificări, tortuozitate).
  tech: 'Direcție de scanare caudo-cranială. Câmpul minim de scanare: de la nivelul
    arterelor renale până la bifurcația femurală comună.'
  tips: Brațele complet ridicate. Fără contrast oral pozitiv pentru examinările pur
    vasculare.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: Fără contrast oral pozitiv (pentru a nu masca vasele)
protocol_type: vascular
recons:
- acquisition: Angio-CT Arterial
  fov: Abdomen
  kernel: Vascular
  notes: Aorta abdominală și ramurile viscerale
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Angio-CT Arterial
  fov: Pelvis
  kernel: Vascular
  notes: Vasele iliace și bifurcația femurală
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Angio-CT Arterial
  fov: Abdomen-Pelvis
  kernel: Vascular
  notes: MIP coronal al aortei și ramurilor sale
  plane: Coronal
  thickness_increment: 2 mm/2 mm
- acquisition: Angio-CT Arterial
  fov: Abdomen-Pelvis
  kernel: Vascular
  notes: MPR curbat al aortei abdominale
  plane: Sagital
  thickness_increment: 2 mm/2 mm
safety:
  allergy: Verificați istoricul alergic la contrast iodat
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: Urmărire bolus
  end: Capete femurale
  name: Angio-CT Arterial
  notes: Direcție caudo-cranială pentru optimizarea opacifierii
  start: Diafragm
  thickness: 0.625 mm
- delay: 40 sec
  end: Margine inferioară stent
  name: Tardiv Stent (opțional)
  notes: Acoperire zonă endoproteză pentru decelarea endoleak-urilor
  start: Margine superioară stent
  thickness: 1 mm
slug: cta-abdomen-pelvis
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '100'
  mas: Auto (referință 250 mAs)
  pitch: 1.0-1.375
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Abdomen și Pelvis
sources:
- title: ACR-NASCI-SIR Practice Parameter for Performance of Body Computed Tomographic
    Angiography (CTA)
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Body.pdf
  institution: ACR / NASCI / SIR
  source_region: US
  kind: Standard de practică angio-CT
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: bf7ff18eff996f000474c6a03d89a358f09f8af2ee90da1217121760ae1ae6f9
- title: UT Southwestern Radiology — CTA & Vascular CT Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# Angio-CT Abdomen și Pelvis

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Arterial | Urmărire bolus | Diafragm → Capete femurale |
        | Tardiv Stent (opțional) | 40 sec | Margine superioară stent → Margine inferioară stent |

    === "Indicații Clinice"

        - Anevrism de aortă abdominală (AAA)
        - Suspiciune de ischemie mezenterică
        - Stenoză de arteră renală (hipertensiune renovasculară)
        - Planificare pre- și post-endoprotezare aortică (EVAR)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular & Sistem vascular*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Fără contrast oral pozitiv (pentru a nu masca vasele)

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.1 mL/kg |
        | Rată de Flux | 4 mL/s |
        | Durată | 20s |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Aorta abdominală la originea trunchiului celiac |
        | Declanșator (HU) | 150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 kV |
    | **Curent Tub (mAs)** | Auto (referință 250 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.0-1.375 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Direcție de scanare caudo-cranială. Câmpul minim de scanare: de la nivelul arterelor renale până la bifurcația femurală comună.

    === "Note Asistent"

        - Linie venoasă 18-20G în plica cotului.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic la contrast iodat

    === "Note Radiolog"

        - Măsurați diametrele AAA în 3 planuri dacă este prezent. Evaluați originea și calibrul arterelor renale și mezenterice. Analizați axul arterial iliac (diametru, calcificări, tortuozitate).

    === "Sfaturi & Recomandări"

        - Brațele complet ridicate. Fără contrast oral pozitiv pentru examinările pur vasculare.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Arterial | Diafragm | Capete femurale | Urmărire bolus | 0.625 mm | Direcție caudo-cranială pentru optimizarea opacifierii |
    | Tardiv Stent (opțional) | Margine superioară stent | Margine inferioară stent | 40 sec | 1 mm | Acoperire zonă endoproteză pentru decelarea endoleak-urilor |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Arterial | Abdomen | 1.25 mm/1.25 mm | Vascular |  | Aorta abdominală și ramurile viscerale |
    | Axial | Angio-CT Arterial | Pelvis | 1.25 mm/1.25 mm | Vascular |  | Vasele iliace și bifurcația femurală |
    | Coronal | Angio-CT Arterial | Abdomen-Pelvis | 2 mm/2 mm | Vascular |  | MIP coronal al aortei și ramurilor sale |
    | Sagital | Angio-CT Arterial | Abdomen-Pelvis | 2 mm/2 mm | Vascular |  | MPR curbat al aortei abdominale |

## Surse și revizuire

- [ACR-NASCI-SIR Practice Parameter for Performance of Body Computed Tomographic Angiography (CTA)](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Body.pdf) — *ACR / NASCI / SIR* (US)
- [UT Southwestern Radiology — CTA & Vascular CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
