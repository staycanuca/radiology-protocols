---
author: Departamentul de Radiologie
category: abdomen
clinical_indications:
- Bilanț și stadializare oncologică (CAP)
- Căutarea focarului de infecție / sindrom febril prelungit
- Durere abdominală și toracică nespecifică
contrast:
  agent: Isovue 370
  duration: 40s
  flow_rate: 3 mL/s
  timing: Timp empiric de întârziere (70s)
  volume: 1.5 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții sagitale opționale pentru coloană și mediastin.
  nursing: Abord venos periferic 20-22G. Verificați funcția renală a pacientului.
  rad: Faza venoasă portală este optimă pentru organele parenchimatoase și peretele
    intestinal. Analiză sistematică a tuturor segmentelor toraco-abdomino-pelvine.
  tech: Achiziție unică în fază venoasă portală. Timp de injectare 40 secunde. Scanare
    la 70 secunde de la debutul injectării.
  tips: Brațele complet ridicate. Contrastul oral neutru este de preferat celui pozitiv
    în bilanțul vascular/parenchimatos.
npo: Repaus alimentar 4 ore pentru alimente solide
position: Decubit dorsal cu brațele ridicate
premedication: 'Contrast oral: 250-500 mL contrast neutru (Volumen sau apă) administrat
  cu 60-90 min înainte de scanare'
protocol_type: contrast-enhanced
recons:
- acquisition: Fază Venoasă Portală
  fov: Torace
  kernel: Standard
  notes: Diagnostic mediastinal și pulmonar
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Venoasă Portală
  fov: Abdomen
  kernel: Standard
  notes: Diagnostic abdomen și pelvis
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Venoasă Portală
  fov: Torace-Abdomen-Pelvis
  kernel: Standard
  notes: Vedere coronală de ansamblu
  plane: Coronal
  thickness_increment: 3 mm/3 mm
safety:
  allergy: Verificați istoricul reacțiilor alergice la contrast iodat.
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 70 sec
  end: Simfiză pubiană
  name: Fază Venoasă Portală
  notes: Achiziție completă torace-abdomen-pelvis
  start: Vârfuri pulmonare
  thickness: 0.625 mm
- delay: 300 sec
  end: 1-2cm sub rinichi
  name: Tardiv Renal
  notes: Serie tardivă renală dacă este indicată clinic
  start: 1-2cm deasupra rinichilor
  thickness: 0.625 mm
slug: ct-chest-abdomen-pelvis-with-contrast
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200 mAs)
  pitch: 1.0-1.375
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Torace, Abdomen și Pelvis cu Substanță de Contrast
sources:
- title: AAPM CT Protocols — Adult Abdomen/Pelvis CT
  url: https://www.aapm.org/pubs/ctprotocols/documents/AdultAbdomenPelvisCT.pdf
  institution: AAPM
  source_region: US
  kind: Protocol tehnic standardizat
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: f0c7c2e31da9a9ed24dbdef7bd5b38994d670ba52d21b702faac79b97ace00c3
- title: UT Southwestern Radiology — CT Abdomen & Pelvis Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# CT Torace, Abdomen și Pelvis cu Substanță de Contrast

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Venoasă Portală | 70 sec | Vârfuri pulmonare → Simfiză pubiană |
        | Tardiv Renal | 300 sec | 1-2cm deasupra rinichilor → 1-2cm sub rinichi |

    === "Indicații Clinice"

        - Bilanț și stadializare oncologică (CAP)
        - Căutarea focarului de infecție / sindrom febril prelungit
        - Durere abdominală și toracică nespecifică

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore pentru alimente solide
    - **Premedicație / Pregătire:**
        - Contrast oral: 250-500 mL contrast neutru (Volumen sau apă) administrat cu 60-90 min înainte de scanare

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.5 mL/kg |
        | Rată de Flux | 3 mL/s |
        | Durată | 40s |
        | Metodă Temporizare | Timp empiric de întârziere (70s) |
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
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | Auto (referință 200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.0-1.375 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Achiziție unică în fază venoasă portală. Timp de injectare 40 secunde. Scanare la 70 secunde de la debutul injectării.

    === "Note Asistent"

        - Abord venos periferic 20-22G. Verificați funcția renală a pacientului.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul reacțiilor alergice la contrast iodat.

    === "Note Radiolog"

        - Faza venoasă portală este optimă pentru organele parenchimatoase și peretele intestinal. Analiză sistematică a tuturor segmentelor toraco-abdomino-pelvine.

    === "Sfaturi & Recomandări"

        - Brațele complet ridicate. Contrastul oral neutru este de preferat celui pozitiv în bilanțul vascular/parenchimatos.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Venoasă Portală | Vârfuri pulmonare | Simfiză pubiană | 70 sec | 0.625 mm | Achiziție completă torace-abdomen-pelvis |
    | Tardiv Renal | 1-2cm deasupra rinichilor | 1-2cm sub rinichi | 300 sec | 0.625 mm | Serie tardivă renală dacă este indicată clinic |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Venoasă Portală | Torace | 2.5 mm/2.5 mm | Standard |  | Diagnostic mediastinal și pulmonar |
    | Axial | Fază Venoasă Portală | Abdomen | 2.5 mm/2.5 mm | Standard |  | Diagnostic abdomen și pelvis |
    | Coronal | Fază Venoasă Portală | Torace-Abdomen-Pelvis | 3 mm/3 mm | Standard |  | Vedere coronală de ansamblu |

## Surse și revizuire

- [AAPM CT Protocols — Adult Abdomen/Pelvis CT](https://www.aapm.org/pubs/ctprotocols/documents/AdultAbdomenPelvisCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Abdomen & Pelvis Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
