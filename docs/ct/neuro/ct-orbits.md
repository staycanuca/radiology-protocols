---
author: Departamentul de Radiologie
category: neuro
clinical_indications:
- Formațiune tumorală intraorbitară sau a glandei lacrimale
- Oftalmopatie tiroidiană / boală Basedow-Graves (exoftalmie)
- Celulită orbitară (preseptală vs. postseptală) / abces subperiostal
- Traumatism orbitar (fractură de planșeu / fractură blow-out, corp străin intraocular)
- Neuropatie optică / evaluarea canalului optic
contrast:
  agent: Omnipaque 350 dacă se administrează contrast
  flow_rate: 3 mL/s
  volume: 75-100 mL dacă se administrează contrast
last_updated: '2026-01-01'
notes:
  additional_recons: Evaluarea canalului optic în plan oblic. Măsurarea calibrului
    mușchilor oculomotori. Randare 3D în fracturi complexe.
  nursing: Linie venoasă pentru studiile cu contrast. Instruiți pacientul să mențină
    privirea fixă înainte fără mișcări oculare.
  rad: Glob ocular și cameră anterioară/posterioară. Mușchii extraoculari (măsurarea
    grosimii corpului muscular vs. tendoanelor în oftalmopatia Basedow). Nervul optic
    și teaca sa. Grăsimea retrobulbară. Integritatea pereților osoși (planșeu, perete
    medial).
  tech: De la marginea orbitară superioară până sub podeaua sinusului maxilar. Achiziție
    axială fină orientată paralel cu nervii optici. Reformatări coronale perpendiculare
    pe nervul optic. Nativ pentru corpi străini și traumă; cu contrast pentru inflamație
    și tumori.
  tips: Angulați planul axial paralel cu traiectul nervilor optici. Secțiuni submilimetrice.
npo: Repaus alimentar 4 ore dacă se administrează contrast
position: Decubit dorsal cu capul fixat în suport dedicat; privirea imobilizată înainte
premedication: ''
protocol_type: contrast-enhanced
recons:
- acquisition: CT Axial Orbite
  fov: Orbite
  kernel: Bone and Standard
  notes: Fereastră osoasă pentru fracturi și de părți moi pentru glob/mușchi
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: CT Axial Orbite
  fov: Orbite
  kernel: Bone and Standard
  notes: Plan coronal pentru planșeul orbitar și mușchii extraoculari
  plane: Coronal
  thickness_increment: 1 mm/1 mm
- acquisition: CT Axial Orbite
  fov: Orbite
  kernel: Standard
  notes: Plan sagital oblic pe axul nervului optic
  plane: Sagital
  thickness_increment: 1 mm/1 mm
- acquisition: CT Axial Orbite
  fov: Orbite
  kernel: Bone
  notes: Randare tridimensională 3D în fracturi complexe de cadru orbitar
  plane: 3D if trauma
  thickness_increment: 0.75 mm/0.75 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m² dacă se administrează contrast
series:
- delay: 0 sec
  end: Sinus maxilar
  name: CT Axial Orbite
  notes: Paralel cu traiectul nervilor optici
  start: Margine orbitară superioară
  thickness: 0.625 mm
slug: ct-orbits
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200-250 mAs)
  pitch: Helical
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Orbite
sources:
- title: AAPM CT Protocols — Adult Routine Head CT
  url: https://www.aapm.org/pubs/ctprotocols/documents/RoutineHeadCT.pdf
  institution: AAPM
  source_region: US
  kind: Protocol tehnic standardizat
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 503972f1004a69ab87fba33be79f28ad3647b389370870386d9af7967ea1691b
- title: UT Southwestern Radiology — CT Neuro / Head Protocols
  url: https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html
  institution: UT Southwestern
  source_region: US
  kind: Protocol instituțional
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 585ee440fc9feeb019a4a974e7113683b042c715bd8816718ff43384801f3b20
---

# CT Orbite

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Axial Orbite | 0 sec | Margine orbitară superioară → Sinus maxilar |

    === "Indicații Clinice"

        - Formațiune tumorală intraorbitară sau a glandei lacrimale
        - Oftalmopatie tiroidiană / boală Basedow-Graves (exoftalmie)
        - Celulită orbitară (preseptală vs. postseptală) / abces subperiostal
        - Traumatism orbitar (fractură de planșeu / fractură blow-out, corp străin intraocular)
        - Neuropatie optică / evaluarea canalului optic

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul fixat în suport dedicat; privirea imobilizată înainte
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore dacă se administrează contrast
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 dacă se administrează contrast |
        | Volum | 75-100 mL dacă se administrează contrast |
        | Rată de Flux | 3 mL/s |
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
    | **Curent Tub (mAs)** | Auto (referință 200-250 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - De la marginea orbitară superioară până sub podeaua sinusului maxilar. Achiziție axială fină orientată paralel cu nervii optici. Reformatări coronale perpendiculare pe nervul optic. Nativ pentru corpi străini și traumă; cu contrast pentru inflamație și tumori.

    === "Note Asistent"

        - Linie venoasă pentru studiile cu contrast. Instruiți pacientul să mențină privirea fixă înainte fără mișcări oculare.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m² dacă se administrează contrast
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Glob ocular și cameră anterioară/posterioară. Mușchii extraoculari (măsurarea grosimii corpului muscular vs. tendoanelor în oftalmopatia Basedow). Nervul optic și teaca sa. Grăsimea retrobulbară. Integritatea pereților osoși (planșeu, perete medial).

    === "Sfaturi & Recomandări"

        - Angulați planul axial paralel cu traiectul nervilor optici. Secțiuni submilimetrice.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Axial Orbite | Margine orbitară superioară | Sinus maxilar | 0 sec | 0.625 mm | Paralel cu traiectul nervilor optici |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Axial Orbite | Orbite | 1 mm/1 mm | Bone and Standard |  | Fereastră osoasă pentru fracturi și de părți moi pentru glob/mușchi |
    | Coronal | CT Axial Orbite | Orbite | 1 mm/1 mm | Bone and Standard |  | Plan coronal pentru planșeul orbitar și mușchii extraoculari |
    | Sagital | CT Axial Orbite | Orbite | 1 mm/1 mm | Standard |  | Plan sagital oblic pe axul nervului optic |
    | 3D if trauma | CT Axial Orbite | Orbite | 0.75 mm/0.75 mm | Bone |  | Randare tridimensională 3D în fracturi complexe de cadru orbitar |

## Surse și revizuire

- [AAPM CT Protocols — Adult Routine Head CT](https://www.aapm.org/pubs/ctprotocols/documents/RoutineHeadCT.pdf) — *AAPM* (US)
- [UT Southwestern Radiology — CT Neuro / Head Protocols](https://www.utsouthwestern.edu/departments/radiology/protocols/ct.html) — *UT Southwestern* (US)
