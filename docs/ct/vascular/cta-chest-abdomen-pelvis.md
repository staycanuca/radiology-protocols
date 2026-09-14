---
author: Departamentul de Radiologie
category: vascular
clinical_indications:
- Anevrism toraco-abdominal de aortă (TAAA)
- Disecție extinsă de aortă
- Vasculite ale vaselor mari (Takayasu, celule gigante)
- Pan-scan vascular în traumă majoră
contrast:
  agent: Isovue 370
  duration: 20s
  flow_rate: 4 mL/s
  roi: Aorta toracică descendentă
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 150 HU
  volume: 1.1 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Randare 3D VR și MPR curbat pe întregul ax aortic. Comparație
    pe secțiuni fine în fază tardivă pentru vasculită.
  nursing: Linie venoasă minim 20G (ideal 18G în plica cotului).
  rad: Evaluați întreaga lungime a aortei pentru semne de disecție, hematom intramural,
    anevrism sau ulcerație aterosclerotică penetrantă. Măsurați diametrele aortei.
    Evaluați permeabilitatea ramurilor viscerale și iliace.
  tech: Achiziție unică de la apertura toracică superioară până la simfiza pubiană.
    Direcție caudo-cranială. Urmărire bolus în aorta toracică descendentă.
  tips: Brațele complet ridicate deasupra capului pentru a preveni artefactele pe
    torace și abdomen superior.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: ''
protocol_type: vascular
recons:
- acquisition: Angio-CT Arterial
  fov: Torace
  kernel: Vascular
  notes: Evaluarea aortei toracice
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Angio-CT Arterial
  fov: Abdomen-Pelvis
  kernel: Vascular
  notes: Aorta abdominală și ramurile viscerale
  plane: Axial
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Angio-CT Arterial
  fov: Torace-Abdomen-Pelvis
  kernel: Vascular
  notes: MIP coronal de ansamblu pe toată aorta
  plane: Coronal
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Angio-CT Arterial
  fov: Torace-Abdomen-Pelvis
  kernel: Vascular
  notes: MIP sagital și MPR curbat pe crosa și aorta descendentă
  plane: Sagital
  thickness_increment: 2 mm/2 mm
safety:
  allergy: Verificați istoricul de alergie
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: Urmărire bolus
  end: Simfiză pubiană
  name: Angio-CT Arterial
  notes: Achiziție caudo-cranială pentru opacifiere uniformă
  start: Apertura toracică superioară
  thickness: 0.625 mm
- delay: 40 sec
  end: Margine inferioară stent
  name: Tardiv Stent (opțional)
  notes: Acoperire zonă stent
  start: Margine superioară stent
  thickness: 1 mm
- delay: 70 sec
  end: Simfiză pubiană
  name: Tardiv Vasculită (opțional)
  notes: Încărcare parietală și îngroșare concentrică în vasculite
  start: Apertura toracică superioară
  thickness: 1 mm
slug: cta-chest-abdomen-pelvis
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '100'
  mas: Auto (referință 250 mAs)
  pitch: 1.0-1.2
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Torace, Abdomen și Pelvis
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

# Angio-CT Torace, Abdomen și Pelvis

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Arterial | Urmărire bolus | Apertura toracică superioară → Simfiză pubiană |
        | Tardiv Stent (opțional) | 40 sec | Margine superioară stent → Margine inferioară stent |
        | Tardiv Vasculită (opțional) | 70 sec | Apertura toracică superioară → Simfiză pubiană |

    === "Indicații Clinice"

        - Anevrism toraco-abdominal de aortă (TAAA)
        - Disecție extinsă de aortă
        - Vasculite ale vaselor mari (Takayasu, celule gigante)
        - Pan-scan vascular în traumă majoră

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
        | Volum | 1.1 mL/kg |
        | Rată de Flux | 4 mL/s |
        | Durată | 20s |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Aorta toracică descendentă |
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
    | **Pitch (Factor Pas)** | 1.0-1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Achiziție unică de la apertura toracică superioară până la simfiza pubiană. Direcție caudo-cranială. Urmărire bolus în aorta toracică descendentă.

    === "Note Asistent"

        - Linie venoasă minim 20G (ideal 18G în plica cotului).

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul de alergie

    === "Note Radiolog"

        - Evaluați întreaga lungime a aortei pentru semne de disecție, hematom intramural, anevrism sau ulcerație aterosclerotică penetrantă. Măsurați diametrele aortei. Evaluați permeabilitatea ramurilor viscerale și iliace.

    === "Sfaturi & Recomandări"

        - Brațele complet ridicate deasupra capului pentru a preveni artefactele pe torace și abdomen superior.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Arterial | Apertura toracică superioară | Simfiză pubiană | Urmărire bolus | 0.625 mm | Achiziție caudo-cranială pentru opacifiere uniformă |
    | Tardiv Stent (opțional) | Margine superioară stent | Margine inferioară stent | 40 sec | 1 mm | Acoperire zonă stent |
    | Tardiv Vasculită (opțional) | Apertura toracică superioară | Simfiză pubiană | 70 sec | 1 mm | Încărcare parietală și îngroșare concentrică în vasculite |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Arterial | Torace | 1.25 mm/1.25 mm | Vascular |  | Evaluarea aortei toracice |
    | Axial | Angio-CT Arterial | Abdomen-Pelvis | 1.5 mm/1.5 mm | Vascular |  | Aorta abdominală și ramurile viscerale |
    | Coronal | Angio-CT Arterial | Torace-Abdomen-Pelvis | 2.5 mm/2.5 mm | Vascular |  | MIP coronal de ansamblu pe toată aorta |
    | Sagital | Angio-CT Arterial | Torace-Abdomen-Pelvis | 2 mm/2 mm | Vascular |  | MIP sagital și MPR curbat pe crosa și aorta descendentă |

## Surse și revizuire

- [ACR-NASCI-SIR Practice Parameter for Performance of Body Computed Tomographic Angiography (CTA)](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Body.pdf) — *ACR / NASCI / SIR* (US)
- [UT Southwestern Radiology — CTA & Vascular CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
