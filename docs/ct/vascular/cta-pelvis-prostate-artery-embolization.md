---
author: Departamentul de Radiologie
category: vascular
clinical_indications:
- Planificare pre-procedurală pentru embolizarea arterelor prostatice (PAE)
- Hiperplazie benignă de prostată (HBP) simptomatică refractară
contrast:
  agent: Isovue 370
  duration: 18-22s
  flow_rate: 3-4 mL/s
  roi: Artera iliacă comună
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 150 HU
  volume: 1.2 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Randare 3D VR evidențiind specific vascularizația prostatică.
    Reconstrucții MPR curbate ale ramurilor iliace interne. Măsurători de calibru
    și angulație ale ostiilor.
  nursing: Linie venoasă 18-20G. Verificați tensiunea arterială dacă se administrează
    nitroglicerină.
  rad: Identificați cu precizie originea arterelor prostatice (trunchi vezico-prostatic,
    arteră obturatorie, arteră rușinoasă internă etc.). Cartografiați anatomia pelvină
    pentru radiologia intervențională. Identificați anastomozele periculoase (rectale,
    vezicale, peniene).
  tech: Scanare de la L3 până la femurul proximal. Faza arterială este obligatorie.
    Focus pe ramurile diviziunii anterioare a arterei iliace interne și originea arterei
    prostatice.
  tips: Vezica urinară în semirepleție este utilă pentru delimitarea conturului prostatic.
    Sincronizare atentă cu medicul radiolog intervenționist.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: ''
protocol_type: vascular
recons:
- acquisition: Angio-CT Arterial
  fov: Pelvis
  kernel: Vascular
  notes: Identificarea originii arterelor prostatice
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Angio-CT Arterial
  fov: Pelvis
  kernel: Vascular
  notes: MIP al vaselor iliace pelvine
  plane: Coronal
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Angio-CT Arterial
  fov: Pelvis
  kernel: Vascular
  notes: Vedere sagitală a ramurilor pelvine
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Angio-CT Arterial
  fov: Pelvis
  kernel: Vascular
  notes: Hartă tridimensională 3D pentru medicul radiolog intervenționist
  plane: 3D VR
  thickness_increment: 0.75 mm/0.75 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: Urmărire bolus
  end: Mici trohantere
  name: Angio-CT Arterial
  notes: Focus pe ramurile arterei iliace interne
  start: Creste iliace
  thickness: 0.625 mm
slug: cta-pelvis-prostate-artery-embolization
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '100'
  mas: Auto (referință 200 mAs)
  pitch: '0.9'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Pelvis Planificare Embolizare de Arteră Prostatică (PAE)
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

# Angio-CT Pelvis Planificare Embolizare de Arteră Prostatică (PAE)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Arterial | Urmărire bolus | Creste iliace → Mici trohantere |

    === "Indicații Clinice"

        - Planificare pre-procedurală pentru embolizarea arterelor prostatice (PAE)
        - Hiperplazie benignă de prostată (HBP) simptomatică refractară

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular & Sistem vascular*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.2 mL/kg |
        | Rată de Flux | 3-4 mL/s |
        | Durată | 18-22s |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Artera iliacă comună |
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
    | **Curent Tub (mAs)** | Auto (referință 200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare de la L3 până la femurul proximal. Faza arterială este obligatorie. Focus pe ramurile diviziunii anterioare a arterei iliace interne și originea arterei prostatice.

    === "Note Asistent"

        - Linie venoasă 18-20G. Verificați tensiunea arterială dacă se administrează nitroglicerină.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Identificați cu precizie originea arterelor prostatice (trunchi vezico-prostatic, arteră obturatorie, arteră rușinoasă internă etc.). Cartografiați anatomia pelvină pentru radiologia intervențională. Identificați anastomozele periculoase (rectale, vezicale, peniene).

    === "Sfaturi & Recomandări"

        - Vezica urinară în semirepleție este utilă pentru delimitarea conturului prostatic. Sincronizare atentă cu medicul radiolog intervenționist.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Arterial | Creste iliace | Mici trohantere | Urmărire bolus | 0.625 mm | Focus pe ramurile arterei iliace interne |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Arterial | Pelvis | 1 mm/1 mm | Vascular |  | Identificarea originii arterelor prostatice |
    | Coronal | Angio-CT Arterial | Pelvis | 1.5 mm/1.5 mm | Vascular |  | MIP al vaselor iliace pelvine |
    | Sagital | Angio-CT Arterial | Pelvis | 1.5 mm/1.5 mm | Vascular |  | Vedere sagitală a ramurilor pelvine |
    | 3D VR | Angio-CT Arterial | Pelvis | 0.75 mm/0.75 mm | Vascular |  | Hartă tridimensională 3D pentru medicul radiolog intervenționist |

## Surse și revizuire

- [ACR-NASCI-SIR Practice Parameter for Performance of Body Computed Tomographic Angiography (CTA)](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Body.pdf) — *ACR / NASCI / SIR* (US)
- [UT Southwestern Radiology — CTA & Vascular CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
