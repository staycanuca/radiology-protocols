---
author: Departamentul de Radiologie
category: msk
clinical_indications:
- Fractură de șold (col femural, trohanteriană, subtrohanteriană)
- Fractură de cotil / acetabul (clasificare Letournel)
- Luxație traumatică posterioară sau anterioară de șold
- Conflict femuro-acetabular (FAI - Cam/Pincer)
- Necroză avasculară de cap femural (NAVCF)
contrast:
  agent: Nativ de regulă. Contrast dacă se suspectează infecție de proteză sau formațiune
    tumorală
  flow_rate: 2-3 mL/s
  volume: 'Dacă este indicat: 100 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Randare 3D VR a bazinului și șoldului. Incidențe oblice Judet
    (obturatorie și iliacă). Măsurarea unghiului alfa și a profunzimii acetabulare.
  nursing: Fără linie venoasă decât dacă este indicată substanță de contrast.
  rad: Fracturi de col femural (Garden). Fracturi acetabulare (stâlpul anterior/posterior,
    peretele anterior/posterior, transverse). Fragmente osteocondrale în spațiul articular.
    Morfologie FAI (unghi alfa, retroversie acetabulară). Semne de NAVCF.
  tech: De la nivelul crestelor iliace până sub micul trohanter. Scanare bilaterală
    pentru comparație anatomică. Achiziție submilimetrică dedicată reconstrucțiilor
    3D acetabulare.
  tips: Acoperire bilaterală simetrică. Secțiuni submilimetrice pentru măsurători
    FAI și randare 3D.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu membrele inferioare paralele
premedication: ''
protocol_type: musculoskeletal
recons:
- acquisition: CT Șold / Bazin
  fov: Șold
  kernel: Bone
  notes: Fereastră osoasă axială de înaltă rezoluție
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: CT Șold / Bazin
  fov: Bazin-Șold
  kernel: Bone
  notes: Plan coronal ambele șolduri pentru comparație
  plane: Coronal
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: CT Șold / Bazin
  fov: Șold
  kernel: Bone
  notes: Plan sagital pe articulația coxo-femurală
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: CT Șold / Bazin
  fov: Bazin
  kernel: Bone
  notes: Incidențe oblice Judet (obturatorie și alară)
  plane: Judet views
  thickness_increment: 1.5 mm/1.5 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Mici trohanteri
  name: CT Șold / Bazin
  notes: Submilimetric pentru randare 3D acetabulară
  start: Creste iliace
  thickness: 0.625 mm
slug: ct-hip
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 250 mAs)
  pitch: Helical
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Șold (Articulație Coxo-Femurală)
sources:
- title: ACR-SSR Practice Parameter for Musculoskeletal CT
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CT-MSK.pdf
  institution: ACR / SSR
  source_region: US
  kind: Standard de practică MSK
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: c0429ea24ea0955f09249fe969fc88b0a48e70073a42bab3ba08be042e1085f4
- title: UT Southwestern Radiology — Musculoskeletal CT Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# CT Șold (Articulație Coxo-Femurală)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Șold / Bazin | 0 sec | Creste iliace → Mici trohanteri |

    === "Indicații Clinice"

        - Fractură de șold (col femural, trohanteriană, subtrohanteriană)
        - Fractură de cotil / acetabul (clasificare Letournel)
        - Luxație traumatică posterioară sau anterioară de șold
        - Conflict femuro-acetabular (FAI - Cam/Pincer)
        - Necroză avasculară de cap femural (NAVCF)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat locomotor & Articulații*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu membrele inferioare paralele
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Contrast dacă se suspectează infecție de proteză sau formațiune tumorală |
        | Volum | Dacă este indicat: 100 mL |
        | Rată de Flux | 2-3 mL/s |
        | Durată |  |
        | Metodă Temporizare |  |
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
    | **Curent Tub (mAs)** | Auto (referință 250 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - De la nivelul crestelor iliace până sub micul trohanter. Scanare bilaterală pentru comparație anatomică. Achiziție submilimetrică dedicată reconstrucțiilor 3D acetabulare.

    === "Note Asistent"

        - Fără linie venoasă decât dacă este indicată substanță de contrast.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Fracturi de col femural (Garden). Fracturi acetabulare (stâlpul anterior/posterior, peretele anterior/posterior, transverse). Fragmente osteocondrale în spațiul articular. Morfologie FAI (unghi alfa, retroversie acetabulară). Semne de NAVCF.

    === "Sfaturi & Recomandări"

        - Acoperire bilaterală simetrică. Secțiuni submilimetrice pentru măsurători FAI și randare 3D.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Șold / Bazin | Creste iliace | Mici trohanteri | 0 sec | 0.625 mm | Submilimetric pentru randare 3D acetabulară |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Șold / Bazin | Șold | 1.25 mm/1.25 mm | Bone |  | Fereastră osoasă axială de înaltă rezoluție |
    | Coronal | CT Șold / Bazin | Bazin-Șold | 1.5 mm/1.5 mm | Bone |  | Plan coronal ambele șolduri pentru comparație |
    | Sagital | CT Șold / Bazin | Șold | 1.5 mm/1.5 mm | Bone |  | Plan sagital pe articulația coxo-femurală |
    | Judet views | CT Șold / Bazin | Bazin | 1.5 mm/1.5 mm | Bone |  | Incidențe oblice Judet (obturatorie și alară) |

## Surse și revizuire

- [ACR-SSR Practice Parameter for Musculoskeletal CT](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CT-MSK.pdf) — *ACR / SSR* (US)
- [UT Southwestern Radiology — Musculoskeletal CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
