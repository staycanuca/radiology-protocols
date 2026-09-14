---
author: Departamentul de Radiologie
category: msk
clinical_indications:
- Fracturi ale epifizei proximale humerale (clasificare Neer)
- Fracturi ale cavității glenoide (Bankart osos, fracturi de margini glenoide)
- Fracturi ale scapulei (corp, spina, coracoidă, acromion)
- Calcificări periarticulare (tendinopatie calcifiantă a coafei rotatorilor)
contrast:
  agent: Nativ de regulă. Contrast dacă se suspectează formațiune tumorală/abces
  flow_rate: 2-3 mL/s
  volume: 'Dacă este indicat: 75 mL'
last_updated: '2026-01-01'
notes:
  additional_recons: Randare tridimensională 3D a articulației glenohumerale cu substracția
    humerusului pentru măsurarea 'en face' a pierderii de os glenoidian (glenoid version
    and bone loss).
  nursing: Fără linie venoasă de rutină.
  rad: Fracturi de humerus proximal (cap, mare/mic trohiter, col chirurgical - segmente
    Neer). Pierderea de substanță osoasă glenoidiană (glenoid bone loss) în instabilitate.
    Fracturi scapulare. Articulație acromio-claviculară.
  tech: Include întreaga scapulă și treimea proximală a humerusului. Achiziție submilimetrică
    pentru detaliul marginii glenoide. Incidențe Y pentru profilul scapulei.
  tips: Includeți complet omoplatul în câmpul de scanare. Secțiuni submilimetrice.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu brațul de-a lungul corpului
premedication: ''
protocol_type: musculoskeletal
recons:
- acquisition: CT Umăr
  fov: Umăr
  kernel: Bone
  notes: Fereastră osoasă axială
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: CT Umăr
  fov: Umăr
  kernel: Bone
  notes: Plan oblic coronal în axul fosei glenoide
  plane: Coronal
  thickness_increment: 1 mm/1 mm
- acquisition: CT Umăr
  fov: Umăr
  kernel: Bone
  notes: Plan oblic sagital paralel cu suprafața glenoidiană
  plane: Sagital
  thickness_increment: 1 mm/1 mm
- acquisition: CT Umăr
  fov: Glenoidă
  kernel: Bone
  notes: Plan 'en face' pe suprafața articulară glenoidă
  plane: Oblique
  thickness_increment: 0.75 mm/0.75 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică
series:
- delay: 0 sec
  end: Humerus proximal
  name: CT Umăr
  notes: Achiziție elicoidală submilimetrică
  start: Marginea superioară a scapulei
  thickness: 0.625 mm
slug: ct-shoulder
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200 mAs)
  pitch: Helical
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Umăr
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

# CT Umăr

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Umăr | 0 sec | Marginea superioară a scapulei → Humerus proximal |

    === "Indicații Clinice"

        - Fracturi ale epifizei proximale humerale (clasificare Neer)
        - Fracturi ale cavității glenoide (Bankart osos, fracturi de margini glenoide)
        - Fracturi ale scapulei (corp, spina, coracoidă, acromion)
        - Calcificări periarticulare (tendinopatie calcifiantă a coafei rotatorilor)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat locomotor & Articulații*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațul de-a lungul corpului
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Nativ de regulă. Contrast dacă se suspectează formațiune tumorală/abces |
        | Volum | Dacă este indicat: 75 mL |
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
    | **Curent Tub (mAs)** | Auto (referință 200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Include întreaga scapulă și treimea proximală a humerusului. Achiziție submilimetrică pentru detaliul marginii glenoide. Incidențe Y pentru profilul scapulei.

    === "Note Asistent"

        - Fără linie venoasă de rutină.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Fracturi de humerus proximal (cap, mare/mic trohiter, col chirurgical - segmente Neer). Pierderea de substanță osoasă glenoidiană (glenoid bone loss) în instabilitate. Fracturi scapulare. Articulație acromio-claviculară.

    === "Sfaturi & Recomandări"

        - Includeți complet omoplatul în câmpul de scanare. Secțiuni submilimetrice.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Umăr | Marginea superioară a scapulei | Humerus proximal | 0 sec | 0.625 mm | Achiziție elicoidală submilimetrică |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Umăr | Umăr | 1 mm/1 mm | Bone |  | Fereastră osoasă axială |
    | Coronal | CT Umăr | Umăr | 1 mm/1 mm | Bone |  | Plan oblic coronal în axul fosei glenoide |
    | Sagital | CT Umăr | Umăr | 1 mm/1 mm | Bone |  | Plan oblic sagital paralel cu suprafața glenoidiană |
    | Oblique | CT Umăr | Glenoidă | 0.75 mm/0.75 mm | Bone |  | Plan 'en face' pe suprafața articulară glenoidă |

## Surse și revizuire

- [ACR-SSR Practice Parameter for Musculoskeletal CT](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CT-MSK.pdf) — *ACR / SSR* (US)
- [UT Southwestern Radiology — Musculoskeletal CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
