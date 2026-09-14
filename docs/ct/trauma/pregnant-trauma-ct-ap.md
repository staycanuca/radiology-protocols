---
author: Departamentul de Radiologie
category: trauma
clinical_indications:
- Pacientă gravidă cu politraumatism
- Traumatism abdominal / pelvin în sarcină
- Evaluarea leziunilor organelor materne și fetale
contrast:
  agent: Omnipaque 350
  flow_rate: 3 mL/s
  timing: Timp empiric (70s)
  volume: 125 mL
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții sagitale pentru evaluarea uterului și a inserției
    placentare.
  nursing: Sarcină documentată. Monitorizarea bătăilor cordului fetal dacă echipamentul
    este disponibil. Protecție plumbată dacă este fezabil clinic.
  rad: Evaluați cu prioritate leziunile materne traumatice vitale. Minimizarea expunerii
    fetale. Evaluați integritatea placentară (hematom retroplacentar, decolară de
    placentă) și a peretelui uterin.
  tech: Fază venoasă portală la 70 secunde. ACHIZIȚIE UNICĂ (monofazică) pentru a
    minimiza expunerea fătului la radiații. Protejați fătul dacă leziunea suspectată
    este la distanță. Consemnați săptămânile de gestație.
  tips: Notați vârsta gestațională. Protejați fătul pe cât posibil. Reduceți parametrii
    mAs adaptat greutății.
npo: Fără repaus alimentar - urgență traumatologică
position: Decubit dorsal cu înclinare laterală stângă (15 grade) dacă este posibil
premedication: Fără premedicație
protocol_type: trauma
recons:
- acquisition: Fază Venoasă Portală AP
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Organe parenchimatoase materne
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Venoasă Portală AP
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Privire coronală de ansamblu
  plane: Coronal
  thickness_increment: 3 mm/3 mm
- acquisition: Fază Venoasă Portală AP
  fov: Pelvis
  kernel: Standard
  notes: Evaluare uter și placentă
  plane: Sagital
  thickness_increment: 3 mm/3 mm
safety:
  allergy: Indicație de urgență traumatologică documentată
  renal: Verificați dacă este cunoscută funcția renală; nu întârziați în caz de urgență
    vitală
series:
- delay: 70 sec
  end: Simfiză pubiană
  name: Fază Venoasă Portală AP
  notes: Achiziție monofazică pentru minimizarea iradierii fetale
  start: Diafragm
  thickness: 2.5 mm
slug: pregnant-trauma-ct-ap
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D pentru politraumă)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '100'
  mas: Curent redus pe cât posibil
  pitch: '1.375'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 2.5 mm
title: CT Abdomen și Pelvis în Traumatism la Gravidă
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

# CT Abdomen și Pelvis în Traumatism la Gravidă

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Venoasă Portală AP | 70 sec | Diafragm → Simfiză pubiană |

    === "Indicații Clinice"

        - Pacientă gravidă cu politraumatism
        - Traumatism abdominal / pelvin în sarcină
        - Evaluarea leziunilor organelor materne și fetale

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Traumatisme & Politraumă*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu înclinare laterală stângă (15 grade) dacă este posibil
    - **Repaus Alimentar (NPO):** Fără repaus alimentar - urgență traumatologică
    - **Premedicație / Pregătire:**
        - Fără premedicație

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volum | 125 mL |
        | Rată de Flux | 3 mL/s |
        | Durată |  |
        | Metodă Temporizare | Timp empiric (70s) |
        | Poziționare ROI |  |
        | Declanșator (HU) |  |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100 kV |
    | **Curent Tub (mAs)** | Curent redus pe cât posibil |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D pentru politraumă) |
    | **Grosime Secțiune Achiziție (Slice)** | 2.5 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.375 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Fază venoasă portală la 70 secunde. ACHIZIȚIE UNICĂ (monofazică) pentru a minimiza expunerea fătului la radiații. Protejați fătul dacă leziunea suspectată este la distanță. Consemnați săptămânile de gestație.

    === "Note Asistent"

        - Sarcină documentată. Monitorizarea bătăilor cordului fetal dacă echipamentul este disponibil. Protecție plumbată dacă este fezabil clinic.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați dacă este cunoscută funcția renală; nu întârziați în caz de urgență vitală
            - **Alergii:** Indicație de urgență traumatologică documentată

    === "Note Radiolog"

        - Evaluați cu prioritate leziunile materne traumatice vitale. Minimizarea expunerii fetale. Evaluați integritatea placentară (hematom retroplacentar, decolară de placentă) și a peretelui uterin.

    === "Sfaturi & Recomandări"

        - Notați vârsta gestațională. Protejați fătul pe cât posibil. Reduceți parametrii mAs adaptat greutății.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Venoasă Portală AP | Diafragm | Simfiză pubiană | 70 sec | 2.5 mm | Achiziție monofazică pentru minimizarea iradierii fetale |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Venoasă Portală AP | Abdomen-Pelvis | 2.5 mm/2.5 mm | Standard |  | Organe parenchimatoase materne |
    | Coronal | Fază Venoasă Portală AP | Abdomen-Pelvis | 3 mm/3 mm | Standard |  | Privire coronală de ansamblu |
    | Sagital | Fază Venoasă Portală AP | Pelvis | 3 mm/3 mm | Standard |  | Evaluare uter și placentă |

## Surse și revizuire

- [ACR Appropriateness Criteria — Major Blunt Trauma](https://www.acr.org/clinical-resources/clinical-tools-and-reference/appropriateness-criteria) — *ACR* (US)
- [UT Southwestern Radiology — Trauma Whole-Body CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
