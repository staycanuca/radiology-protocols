---
author: Departamentul de Radiologie
category: trauma
clinical_indications:
- Traumatism toracic închis cu suspiciune de leziune aortică traumatică
- Leziune traumatică a vaselor mari intratoracice
- Politraumatism toraco-abdominal sever
contrast:
  agent: Omnipaque 350
  flow_rate: 4 mL/s
  roi: Aorta descendentă
  timing: 'Fază dublă: Angio-CT Torace arterial + Fază venoasă portală AP'
  trigger: 150 HU
  volume: 125 mL
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții 3D VR pentru aortă și ramurile arcului aortic.
    Reconstrucții MPR curbate pe lumenul aortei. Clasificarea gradului leziunii aortice.
  nursing: Linie venoasă de calibru mare 18-20G. Verificați debitul de injectare înainte
    de pornire.
  rad: 'Torace arterial: leziune traumatică de aortă (flap intimal, pseudoanevrism
    traumatic, transecțiune). Abdomen-pelvis portal: traumatisme splenice, hepatice,
    renale, mezenterice.'
  tech: 'DOUĂ achiziții sincronizate: 1) Angio-CT Torace arterial (urmărire bolus)
    2) Fază venoasă portală Abdomen/Pelvis la 70s. Achiziția toracică arterială este
    esențială pentru aortă și ramurile sale.'
  tips: Indicație de traumă majoră. Scanare rapidă. Acces venos periferic fiabil indispensabil.
npo: Fără repaus alimentar - urgență traumatologică
position: Decubit dorsal cu brațele ridicate
premedication: ''
protocol_type: vascular
recons:
- acquisition: Angio-CT Torace
  fov: Torace
  kernel: Vascular
  notes: Aorta toracică și vasele mari
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Fază Venoasă Portală AP
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Organe parenchimatoase abdominale
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Angio-CT Torace
  fov: Torace
  kernel: Vascular
  notes: Vedere de ansamblu a aortei toracice
  plane: Coronal
  thickness_increment: 2 mm/2 mm
- acquisition: Angio-CT Torace
  fov: Torace
  kernel: Vascular
  notes: Plan sagital oblic pe cârja și aorta descendentă
  plane: Sagital
  thickness_increment: 2 mm/2 mm
safety:
  allergy: Indicație de urgență traumatologică
  renal: eGFR > 30 mL/min/1.73m² dacă este cunoscută; urgență traumatologică
series:
- delay: Urmărire bolus
  end: Diafragm
  name: Angio-CT Torace
  notes: Fază arterială dedicată pentru aorta toracică
  start: Vârfuri pulmonare
  thickness: 0.625 mm
- delay: 70 sec de la start
  end: Simfiză pubiană
  name: Fază Venoasă Portală AP
  notes: Fază venoasă portală pentru organele abdominale
  start: Diafragm
  thickness: 0.625 mm
slug: trauma-cta-chest-with-pv-ct-ap
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D pentru politraumă)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: 100-120
  mas: Auto (referință 250 mAs)
  pitch: 1.0-1.2
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Torace cu CT Abdomen și Pelvis în Fază Portală (Traumă)
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

# Angio-CT Torace cu CT Abdomen și Pelvis în Fază Portală (Traumă)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Torace | Urmărire bolus | Vârfuri pulmonare → Diafragm |
        | Fază Venoasă Portală AP | 70 sec de la start | Diafragm → Simfiză pubiană |

    === "Indicații Clinice"

        - Traumatism toracic închis cu suspiciune de leziune aortică traumatică
        - Leziune traumatică a vaselor mari intratoracice
        - Politraumatism toraco-abdominal sever

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Traumatisme & Politraumă*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
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
        | Rată de Flux | 4 mL/s |
        | Durată |  |
        | Metodă Temporizare | Fază dublă: Angio-CT Torace arterial + Fază venoasă portală AP |
        | Poziționare ROI | Aorta descendentă |
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
    | **Pitch (Factor Pas)** | 1.0-1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - DOUĂ achiziții sincronizate: 1) Angio-CT Torace arterial (urmărire bolus) 2) Fază venoasă portală Abdomen/Pelvis la 70s. Achiziția toracică arterială este esențială pentru aortă și ramurile sale.

    === "Note Asistent"

        - Linie venoasă de calibru mare 18-20G. Verificați debitul de injectare înainte de pornire.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR > 30 mL/min/1.73m² dacă este cunoscută; urgență traumatologică
            - **Alergii:** Indicație de urgență traumatologică

    === "Note Radiolog"

        - Torace arterial: leziune traumatică de aortă (flap intimal, pseudoanevrism traumatic, transecțiune). Abdomen-pelvis portal: traumatisme splenice, hepatice, renale, mezenterice.

    === "Sfaturi & Recomandări"

        - Indicație de traumă majoră. Scanare rapidă. Acces venos periferic fiabil indispensabil.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Torace | Vârfuri pulmonare | Diafragm | Urmărire bolus | 0.625 mm | Fază arterială dedicată pentru aorta toracică |
    | Fază Venoasă Portală AP | Diafragm | Simfiză pubiană | 70 sec de la start | 0.625 mm | Fază venoasă portală pentru organele abdominale |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Torace | Torace | 1.25 mm/1.25 mm | Vascular |  | Aorta toracică și vasele mari |
    | Axial | Fază Venoasă Portală AP | Abdomen-Pelvis | 2.5 mm/2.5 mm | Standard |  | Organe parenchimatoase abdominale |
    | Coronal | Angio-CT Torace | Torace | 2 mm/2 mm | Vascular |  | Vedere de ansamblu a aortei toracice |
    | Sagital | Angio-CT Torace | Torace | 2 mm/2 mm | Vascular |  | Plan sagital oblic pe cârja și aorta descendentă |

## Surse și revizuire

- [ACR Appropriateness Criteria — Major Blunt Trauma](https://www.acr.org/clinical-resources/clinical-tools-and-reference/appropriateness-criteria) — *ACR* (US)
- [UT Southwestern Radiology — Trauma Whole-Body CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
