---
author: Departamentul de Radiologie
category: vascular
clinical_indications:
- Endofibroza arterei iliace externe la cicliști de performanță
- Claudicație atipică / durere la efort maximal la nivelul coapsei la atleți
contrast:
  agent: Isovue 370
  duration: 18s + 18s
  flow_rate: 4 mL/s
  roi: Artera iliacă externă
  timing: 'Poziționare dublă: Repaus + Poziție flexie șold (pedalare)'
  trigger: 150 HU
  volume: 'Injectare fracționată (split bolus): prima injectare 1.1 mL/kg + a doua
    injectare 1.1 mL/kg'
last_updated: '2026-01-01'
notes:
  additional_recons: Afișare MIP paralelă repaus vs. flexie. Măsurarea procentului
    de stenoză dinamică. Randare 3D VR.
  nursing: Linie venoasă 18-20G.
  rad: Comparați achiziția de repaus cu cea în flexie. Căutați pliuri vasculare (kinking),
    stenoze dinamice, traiect alungit tortuos sau ocluzia arterei iliace externe în
    poziția flectată.
  tech: 'DOUĂ achiziții arteriale: 1) În decubit dorsal de repaus 2) Cu flexia șoldurilor
    la 90 grade simulând poziția pe bicicletă. Scanare bilaterală pentru comparație.'
  tips: Poziționați pacientul cu genunchii și șoldurile flectate utilizând suporturi
    de poziționare pentru a menține unghiul stabil în timpul celei de-a doua scanări.
npo: Repaus alimentar 4 ore
position: Decubit dorsal inițial, apoi în poziție simulantă pedalării
premedication: ''
protocol_type: vascular
recons:
- acquisition: Angio-CT Poziție Repaus
  fov: Pelvis
  kernel: Vascular
  notes: Anatomia de bază a arterelor iliace
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Angio-CT Flexie Șold
  fov: Pelvis
  kernel: Vascular
  notes: Aprecierea compresiunii sau plierii în flexie
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Angio-CT Flexie Șold
  fov: Pelvis
  kernel: Vascular
  notes: MIP comparativ repaus vs. manevră
  plane: Coronal
  thickness_increment: 2 mm/2 mm
- acquisition: Angio-CT Flexie Șold
  fov: Pelvis
  kernel: Vascular
  notes: Vedere laterală a curburii vaselor iliace
  plane: Sagital
  thickness_increment: 2 mm/2 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: Urmărire bolus
  end: Mijlocul femurului
  name: Angio-CT Poziție Repaus
  notes: Decubit dorsal relaxat - referință bazală
  start: L3
  thickness: 0.625 mm
- delay: Urmărire bolus
  end: Mijlocul femurului
  name: Angio-CT Flexie Șold
  notes: Șolduri flectate la 90 de grade - poziție de pedalare
  start: L3
  thickness: 0.625 mm
slug: cta-pelvis-cyclist-iliac-artery-maneuver
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
title: Angio-CT Pelvis Manevră Flexie Șold pentru Bicicliști (Endofibroză Iliacă)
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

# Angio-CT Pelvis Manevră Flexie Șold pentru Bicicliști (Endofibroză Iliacă)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Poziție Repaus | Urmărire bolus | L3 → Mijlocul femurului |
        | Angio-CT Flexie Șold | Urmărire bolus | L3 → Mijlocul femurului |

    === "Indicații Clinice"

        - Endofibroza arterei iliace externe la cicliști de performanță
        - Claudicație atipică / durere la efort maximal la nivelul coapsei la atleți

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular & Sistem vascular*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal inițial, apoi în poziție simulantă pedalării
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | Injectare fracționată (split bolus): prima injectare 1.1 mL/kg + a doua injectare 1.1 mL/kg |
        | Rată de Flux | 4 mL/s |
        | Durată | 18s + 18s |
        | Metodă Temporizare | Poziționare dublă: Repaus + Poziție flexie șold (pedalare) |
        | Poziționare ROI | Artera iliacă externă |
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

        - DOUĂ achiziții arteriale: 1) În decubit dorsal de repaus 2) Cu flexia șoldurilor la 90 grade simulând poziția pe bicicletă. Scanare bilaterală pentru comparație.

    === "Note Asistent"

        - Linie venoasă 18-20G.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Comparați achiziția de repaus cu cea în flexie. Căutați pliuri vasculare (kinking), stenoze dinamice, traiect alungit tortuos sau ocluzia arterei iliace externe în poziția flectată.

    === "Sfaturi & Recomandări"

        - Poziționați pacientul cu genunchii și șoldurile flectate utilizând suporturi de poziționare pentru a menține unghiul stabil în timpul celei de-a doua scanări.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Poziție Repaus | L3 | Mijlocul femurului | Urmărire bolus | 0.625 mm | Decubit dorsal relaxat - referință bazală |
    | Angio-CT Flexie Șold | L3 | Mijlocul femurului | Urmărire bolus | 0.625 mm | Șolduri flectate la 90 de grade - poziție de pedalare |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Poziție Repaus | Pelvis | 1.25 mm/1.25 mm | Vascular |  | Anatomia de bază a arterelor iliace |
    | Axial | Angio-CT Flexie Șold | Pelvis | 1.25 mm/1.25 mm | Vascular |  | Aprecierea compresiunii sau plierii în flexie |
    | Coronal | Angio-CT Flexie Șold | Pelvis | 2 mm/2 mm | Vascular |  | MIP comparativ repaus vs. manevră |
    | Sagital | Angio-CT Flexie Șold | Pelvis | 2 mm/2 mm | Vascular |  | Vedere laterală a curburii vaselor iliace |

## Surse și revizuire

- [ACR-NASCI-SIR Practice Parameter for Performance of Body Computed Tomographic Angiography (CTA)](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Body.pdf) — *ACR / NASCI / SIR* (US)
- [UT Southwestern Radiology — CTA & Vascular CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
