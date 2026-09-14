---
author: Departamentul de Radiologie
category: vascular
clinical_indications:
- Screening vascular după disecție spontană de arteră coronară (SCAD)
- Screening și bilanț complet pentru displazie fibromusculară (FMD)
- Evaluarea afectării arteriale multiteritoriale
contrast:
  agent: Isovue 370
  flow_rate: 4 mL/s
  roi: ROI multiple
  timing: 'Protocol multiteritoriu: Nativ Craniu + Angio-CT Gât + Angio-CT CAP + Post-contrast
    Craniu'
  trigger: 150 HU
  volume: 150 mL volum total
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții MIP și 3D VR ale tuturor teritoriilor arteriale
    (carotidian, renal, mezenteric, cerebral). Măsurarea calibrului leziunilor.
  nursing: Linie venoasă minim 20G cu flux excelent.
  rad: 'Screening-ul tuturor paturilor vasculare afectate de FMD: artere renale, carotide
    interne extracraniene, vertebrale, iliace și artere cerebrale. Căutați aspectul
    clasic în ''șirag de mărgele'' (string-of-beads), anevrisme saculare, stenoze
    focale sau disecții oculte.'
  tech: 'PATRU etape de achiziție: 1) Craniu nativ cu brațele jos 2) Angio-CT Gât
    cu brațele jos (carotide și vertebrale) 3) Angio-CT CAP cu brațele SUS (renale
    și mezenterice) 4) Craniu post-contrast cu brațele jos. Pacientul își repoziționează
    brațele între scanări conform indicațiilor.'
  tips: Antrenați pacientul pentru repoziționarea rapidă a brațelor. Pregătire meticuloasă.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele inițial JOS, apoi SUS
premedication: ''
protocol_type: vascular
recons:
- acquisition: Angio-CT Gât
  fov: Multiple
  kernel: Vascular
  notes: Evaluare arterială multiteritorială
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Angio-CT CAP
  fov: Multiple
  kernel: Vascular
  notes: MIP al teritoriilor renale și carotidiene
  plane: Coronal
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Angio-CT Gât
  fov: Multiple
  kernel: Vascular
  notes: Vederi sagitale ale traiectului carotidian și renal
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Angio-CT CAP
  fov: Multiple
  kernel: Vascular
  notes: Randare 3D tridimensională a tuturor axelor arteriale
  plane: 3D VR
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m² (se administrează ~150 mL contrast)
series:
- delay: 0 sec
  end: Gaura occipitală
  name: CT Nativ Craniu
  notes: Brațele jos - referință nativă
  start: Vertex
  thickness: 1.25 mm
- delay: Urmărire bolus
  end: Vertex
  name: Angio-CT Gât
  notes: Brațele jos - artere carotide și vertebrale
  start: Arc aortic
  thickness: 0.625 mm
- delay: Continuare
  end: Simfiză pubiană
  name: Angio-CT CAP
  notes: Brațele SUS - artere renale, mezenterice și iliace
  start: Diafragm
  thickness: 0.625 mm
- delay: Post-CAP
  end: Gaura occipitală
  name: CT Craniu Post-Contrast
  notes: Brațele JOS - poligonul Willis și circulația intracraniană
  start: Vertex
  thickness: 0.625 mm
slug: cta-scadfmd-protocol
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: 100-120
  mas: Auto (referință 200-250 mAs)
  pitch: 0.9-1.2
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Protocol Displazie Fibromusculară (FMD) și Disecție Coronariană (SCAD)
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

# Angio-CT Protocol Displazie Fibromusculară (FMD) și Disecție Coronariană (SCAD)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Nativ Craniu | 0 sec | Vertex → Gaura occipitală |
        | Angio-CT Gât | Urmărire bolus | Arc aortic → Vertex |
        | Angio-CT CAP | Continuare | Diafragm → Simfiză pubiană |
        | CT Craniu Post-Contrast | Post-CAP | Vertex → Gaura occipitală |

    === "Indicații Clinice"

        - Screening vascular după disecție spontană de arteră coronară (SCAD)
        - Screening și bilanț complet pentru displazie fibromusculară (FMD)
        - Evaluarea afectării arteriale multiteritoriale

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular & Sistem vascular*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele inițial JOS, apoi SUS
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 150 mL volum total |
        | Rată de Flux | 4 mL/s |
        | Durată |  |
        | Metodă Temporizare | Protocol multiteritoriu: Nativ Craniu + Angio-CT Gât + Angio-CT CAP + Post-contrast Craniu |
        | Poziționare ROI | ROI multiple |
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
    | **Curent Tub (mAs)** | Auto (referință 200-250 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9-1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - PATRU etape de achiziție: 1) Craniu nativ cu brațele jos 2) Angio-CT Gât cu brațele jos (carotide și vertebrale) 3) Angio-CT CAP cu brațele SUS (renale și mezenterice) 4) Craniu post-contrast cu brațele jos. Pacientul își repoziționează brațele între scanări conform indicațiilor.

    === "Note Asistent"

        - Linie venoasă minim 20G cu flux excelent.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m² (se administrează ~150 mL contrast)
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Screening-ul tuturor paturilor vasculare afectate de FMD: artere renale, carotide interne extracraniene, vertebrale, iliace și artere cerebrale. Căutați aspectul clasic în 'șirag de mărgele' (string-of-beads), anevrisme saculare, stenoze focale sau disecții oculte.

    === "Sfaturi & Recomandări"

        - Antrenați pacientul pentru repoziționarea rapidă a brațelor. Pregătire meticuloasă.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Nativ Craniu | Vertex | Gaura occipitală | 0 sec | 1.25 mm | Brațele jos - referință nativă |
    | Angio-CT Gât | Arc aortic | Vertex | Urmărire bolus | 0.625 mm | Brațele jos - artere carotide și vertebrale |
    | Angio-CT CAP | Diafragm | Simfiză pubiană | Continuare | 0.625 mm | Brațele SUS - artere renale, mezenterice și iliace |
    | CT Craniu Post-Contrast | Vertex | Gaura occipitală | Post-CAP | 0.625 mm | Brațele JOS - poligonul Willis și circulația intracraniană |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Gât | Multiple | 1 mm/1 mm | Vascular |  | Evaluare arterială multiteritorială |
    | Coronal | Angio-CT CAP | Multiple | 1.5 mm/1.5 mm | Vascular |  | MIP al teritoriilor renale și carotidiene |
    | Sagital | Angio-CT Gât | Multiple | 1.5 mm/1.5 mm | Vascular |  | Vederi sagitale ale traiectului carotidian și renal |
    | 3D VR | Angio-CT CAP | Multiple | 1 mm/1 mm | Vascular |  | Randare 3D tridimensională a tuturor axelor arteriale |

## Surse și revizuire

- [ACR-NASCI-SIR Practice Parameter for Performance of Body Computed Tomographic Angiography (CTA)](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/CTA-Body.pdf) — *ACR / NASCI / SIR* (US)
- [UT Southwestern Radiology — CTA & Vascular CT Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
