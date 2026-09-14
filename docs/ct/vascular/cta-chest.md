---
author: Departamentul de Radiologie
category: vascular
clinical_indications:
- Anevrism de aortă toracică (fără interesarea rădăcinii aortice)
- Evaluarea anomaliilor și variantelor anatomice ale vaselor mari
- Suspiciune de coarctație de aortă sau pseudoanevrism aortic
contrast:
  agent: Isovue 370
  duration: 15 - 20s
  flow_rate: 4 mL/s
  roi: Aorta ascendentă sau trunchiul arterei pulmonare
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 150 HU
  volume: 1.2 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Randare tridimensională 3D VR a arborelui vascular toracic. Reconstrucții
    MIP coronale și sagitale.
  nursing: Linie venoasă minim 20G.
  rad: Evaluați calibrul aortei și al vaselor supraaortice. Măsurați diametrele anevrismului.
    Căutați flap de disecție sau hematom parietal.
  tech: 'Alegeți ROI conform indicației clinice: aorta ascendentă pentru patologie
    aortică sau trunchiul arterei pulmonare pentru suspiciune de TEP. Direcție de
    scanare caudo-cranială.'
  tips: Brațele complet ridicate deasupra capului.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: ''
protocol_type: vascular
recons:
- acquisition: Angio-CT Arterial Torace
  fov: Torace
  kernel: Vascular
  notes: Serie diagnostică vasculară primară
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Angio-CT Arterial Torace
  fov: Torace
  kernel: Lung
  notes: Fereastră pulmonară pentru parenchim
  plane: Axial
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Angio-CT Arterial Torace
  fov: Torace
  kernel: Vascular
  notes: MIP coronal pentru vasele mari
  plane: Coronal
  thickness_increment: 2 mm/2 mm
- acquisition: Angio-CT Arterial Torace
  fov: Torace
  kernel: Vascular
  notes: MIP sagital pentru crosa aortică
  plane: Sagital
  thickness_increment: 2 mm/2 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: Urmărire bolus
  end: Glande suprarenale
  name: Angio-CT Arterial Torace
  notes: Direcție caudo-cranială
  start: Vârfuri pulmonare
  thickness: 0.625 mm
- delay: 40 sec
  end: Margine inferioară stent
  name: Tardiv Stent (opțional)
  notes: Evaluare zonă stentată toracică
  start: Margine superioară stent
  thickness: 1 mm
slug: cta-chest
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '100'
  mas: Auto (referință 200 mAs)
  pitch: 1.0-1.2
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Torace (Aortă Toracică și Vase Mari)
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

# Angio-CT Torace (Aortă Toracică și Vase Mari)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Arterial Torace | Urmărire bolus | Vârfuri pulmonare → Glande suprarenale |
        | Tardiv Stent (opțional) | 40 sec | Margine superioară stent → Margine inferioară stent |

    === "Indicații Clinice"

        - Anevrism de aortă toracică (fără interesarea rădăcinii aortice)
        - Evaluarea anomaliilor și variantelor anatomice ale vaselor mari
        - Suspiciune de coarctație de aortă sau pseudoanevrism aortic

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
        | Rată de Flux | 4 mL/s |
        | Durată | 15 - 20s |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Aorta ascendentă sau trunchiul arterei pulmonare |
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
    | **Pitch (Factor Pas)** | 1.0-1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Alegeți ROI conform indicației clinice: aorta ascendentă pentru patologie aortică sau trunchiul arterei pulmonare pentru suspiciune de TEP. Direcție de scanare caudo-cranială.

    === "Note Asistent"

        - Linie venoasă minim 20G.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Evaluați calibrul aortei și al vaselor supraaortice. Măsurați diametrele anevrismului. Căutați flap de disecție sau hematom parietal.

    === "Sfaturi & Recomandări"

        - Brațele complet ridicate deasupra capului.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Arterial Torace | Vârfuri pulmonare | Glande suprarenale | Urmărire bolus | 0.625 mm | Direcție caudo-cranială |
    | Tardiv Stent (opțional) | Margine superioară stent | Margine inferioară stent | 40 sec | 1 mm | Evaluare zonă stentată toracică |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Arterial Torace | Torace | 1.25 mm/1.25 mm | Vascular |  | Serie diagnostică vasculară primară |
    | Axial | Angio-CT Arterial Torace | Torace | 1.5 mm/1.5 mm | Lung |  | Fereastră pulmonară pentru parenchim |
    | Coronal | Angio-CT Arterial Torace | Torace | 2 mm/2 mm | Vascular |  | MIP coronal pentru vasele mari |
    | Sagital | Angio-CT Arterial Torace | Torace | 2 mm/2 mm | Vascular |  | MIP sagital pentru crosa aortică |

## Surse și revizuire

- [ACR-NASCI-SIR Practice Parameter for Performance of Body Computed Tomographic Angiography (CTA)](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Body.pdf) — *ACR / NASCI / SIR* (US)
- [UT Southwestern Radiology — CTA & Vascular CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
