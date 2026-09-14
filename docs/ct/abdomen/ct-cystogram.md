---
author: Departamentul de Radiologie
category: abdomen
clinical_indications:
- Suspiciune de ruptură vezicală (intraperitoneală vs. extraperitoneală)
- Traumatism pelvin cu leziune vezicală
- Evaluare post-operatorie a integrității vezicii urinare
contrast:
  agent: Isovue 370
  flow_rate: 3-4 mL/s
  volume: 100 mL
last_updated: '2026-01-01'
notes:
  additional_recons: Comparați achiziția în distensie cu cea nativă. Documentați cu
    precizie sediul extravazării. Reconstrucții 3D în leziuni complexe.
  nursing: Cateterism vezical (sondă Foley) necesar. Prepararea soluției diluate de
    contrast (30 mL în 350 mL ser fiziologic). Umplere gravitațională lentă. Pacientul
    semnalează senzația de plenitudine vezicală.
  rad: 'Cistografie: aprecierea integrității pereților vezicali și decelarea extravazării
    (extraperitoneală vs intraperitoneală).'
  tech: 'DOUĂ componente: 1) Scanare CT nativă a pelvisului 2) Umplerea vezicii prin
    sondă Foley cu substanță de contrast diluată prin gravitație 3) Scanare CT cu
    vezica în distensie maximă. Coordonați cu asistenta.'
  tips: Distensia adecvată a vezicii este critică. Umplere lentă prin cădere gravitațională
    (nu injectare forțată). Clampați sonda Foley în timpul scanării.
npo: Repaus alimentar 2-4 ore
position: Decubit dorsal
premedication: 'Contrast intravezical: 350-400 mL soluție de contrast diluată (30
  mL contrast iodat în 350 mL ser fiziologic)'
protocol_type: contrast-enhanced
recons:
- acquisition: Fază Nativă
  fov: Pelvis
  kernel: Standard
  notes: Evaluare pre-contrast
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Cistografie
  fov: Pelvis
  kernel: Standard
  notes: Evaluare vezică urinară în distensie
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Cistografie
  fov: Pelvis
  kernel: Standard
  notes: Privire de ansamblu vezicală și pelvină
  plane: Coronal
  thickness_increment: 3 mm/3 mm
- acquisition: Cistografie
  fov: Pelvis
  kernel: Standard
  notes: Evaluare dom vezical și bază vezicală
  plane: Sagital
  thickness_increment: 3 mm/3 mm
safety:
  allergy: Plasare sondă Foley în condiții sterile. Preparare soluție diluată de contrast.
  renal: eGFR nu este limitativ (contrastul este administrat intravezical, nu se excretă
    renal)
series:
- delay: 0 sec
  end: Simfiză pubiană
  name: Fază Nativă
  notes: Pelvis nativ pre-contrast
  start: Creste iliace
  thickness: 0.625 mm
- delay: Manual
  end: Simfiză pubiană
  name: Umplere Vezicală
  notes: Monitorizare umplere retrogradă
  start: Creste iliace
  thickness: 0.625 mm
- delay: Post-umplere
  end: Simfiză pubiană
  name: Cistografie
  notes: Achiziție cu vezica urinară în distensie maximă
  start: Creste iliace
  thickness: 0.625 mm
slug: ct-cystogram
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200 mAs)
  pitch: '1'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Cisto-CT (Cistografie CT Retrogradă)
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

# Cisto-CT (Cistografie CT Retrogradă)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă | 0 sec | Creste iliace → Simfiză pubiană |
        | Umplere Vezicală | Manual | Creste iliace → Simfiză pubiană |
        | Cistografie | Post-umplere | Creste iliace → Simfiză pubiană |

    === "Indicații Clinice"

        - Suspiciune de ruptură vezicală (intraperitoneală vs. extraperitoneală)
        - Traumatism pelvin cu leziune vezicală
        - Evaluare post-operatorie a integrității vezicii urinare

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal
    - **Repaus Alimentar (NPO):** Repaus alimentar 2-4 ore
    - **Premedicație / Pregătire:**
        - Contrast intravezical: 350-400 mL soluție de contrast diluată (30 mL contrast iodat în 350 mL ser fiziologic)

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 100 mL |
        | Rată de Flux | 3-4 mL/s |
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
    | **Pitch (Factor Pas)** | 1 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - DOUĂ componente: 1) Scanare CT nativă a pelvisului 2) Umplerea vezicii prin sondă Foley cu substanță de contrast diluată prin gravitație 3) Scanare CT cu vezica în distensie maximă. Coordonați cu asistenta.

    === "Note Asistent"

        - Cateterism vezical (sondă Foley) necesar. Prepararea soluției diluate de contrast (30 mL în 350 mL ser fiziologic). Umplere gravitațională lentă. Pacientul semnalează senzația de plenitudine vezicală.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR nu este limitativ (contrastul este administrat intravezical, nu se excretă renal)
            - **Alergii:** Plasare sondă Foley în condiții sterile. Preparare soluție diluată de contrast.

    === "Note Radiolog"

        - Cistografie: aprecierea integrității pereților vezicali și decelarea extravazării (extraperitoneală vs intraperitoneală).

    === "Sfaturi & Recomandări"

        - Distensia adecvată a vezicii este critică. Umplere lentă prin cădere gravitațională (nu injectare forțată). Clampați sonda Foley în timpul scanării.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă | Creste iliace | Simfiză pubiană | 0 sec | 0.625 mm | Pelvis nativ pre-contrast |
    | Umplere Vezicală | Creste iliace | Simfiză pubiană | Manual | 0.625 mm | Monitorizare umplere retrogradă |
    | Cistografie | Creste iliace | Simfiză pubiană | Post-umplere | 0.625 mm | Achiziție cu vezica urinară în distensie maximă |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Nativă | Pelvis | 2.5 mm/2.5 mm | Standard |  | Evaluare pre-contrast |
    | Axial | Cistografie | Pelvis | 2.5 mm/2.5 mm | Standard |  | Evaluare vezică urinară în distensie |
    | Coronal | Cistografie | Pelvis | 3 mm/3 mm | Standard |  | Privire de ansamblu vezicală și pelvină |
    | Sagital | Cistografie | Pelvis | 3 mm/3 mm | Standard |  | Evaluare dom vezical și bază vezicală |

## Surse și revizuire

- [AAPM CT Protocols — Adult Abdomen/Pelvis CT](https://www.aapm.org/pubs/ctprotocols/documents/AdultAbdomenPelvisCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Abdomen & Pelvis Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
