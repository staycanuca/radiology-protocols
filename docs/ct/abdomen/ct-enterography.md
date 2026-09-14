---
author: null
category: abdomen
clinical_indications:
- Boala Crohn (activitate, stenoze, traiecte fistuloase)
- Ocluzie / subocluzie de intestin subțire de cauză neclară
- Hemoragie digestivă obscură
- Formațiuni tumorale ale intestinului subțire (tumori carcinoide, GIST, limfoame)
contrast:
  agent: Isovue 370
  duration: 25s
  flow_rate: 4-5 mL/s
  timing: Timp empiric de întârziere (45s)
  volume: 1.5 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții MPR curbate de-a lungul segmentelor afectate. Evaluare
    vasculară mezenterică.
  nursing: Abord venos 18-20G. Asigurați consumul conform protocolului orar al volumului
    de contrast neutru (~1350 mL în total). Se poate administra spasmolitic/antiperistaltic
    (ex. Buscopan/Glucagon).
  rad: Evaluați priza de contrast a peretelui intestinal și grosimea acestuia. Căutați
    stenoze, traiecte fistuloase, abcese și hipervascularizație mezenterică (semnul
    pieptenelui).
  tech: Fază enterică (45 sec). Volum mare de contrast oral neutru pentru distensia
    anselor. Injectare rapidă în 25 secunde. Scanare la 45 secunde de la debut.
  tips: Distensia optimă a anselor prin contrast oral este critică. Rata de injectare
    a contrastului IV trebuie să fie ridicată.
npo: Repaus alimentar 4 ore pentru alimente solide
position: Decubit dorsal cu brațele ridicate
premedication: 'Contrast oral neutru (VoLumen sau soluție de manitol/apă): primul
  flacon (450 mL) la 90 min; al doilea (450 mL) la 60 min; jumătate flacon (225 mL)
  la 30 min; restul de 225 mL cu 5 min înainte de scanare'
protocol_type: contrast-enhanced
recons:
- acquisition: Fază Enterică
  fov: Abdomen
  kernel: Standard
  notes: Serie diagnostică primară pentru anse
  plane: Axial
  thickness_increment: 2 mm/2 mm
- acquisition: Fază Enterică
  fov: Abdomen
  kernel: Standard
  notes: Evaluarea dispoziției anselor intestinale
  plane: Coronal
  thickness_increment: 2 mm/2 mm
- acquisition: Fază Enterică
  fov: Abdomen
  kernel: Standard
  notes: Evaluare mezenterică și pelvină
  plane: Sagital
  thickness_increment: 2 mm/2 mm
- acquisition: Fază Enterică
  fov: Abdomen
  kernel: Vascular
  notes: Evaluarea vascularizației mezenterice
  plane: MIP
  thickness_increment: 5 mm/2 mm
safety:
  allergy: Verificați istoricul alergic. Sincronizați cu atenție orarul administrării
    contrastului oral.
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 45 sec
  end: Simfiză pubiană
  name: Fază Enterică
  notes: Fază enterică optimă pentru peretele intestinal
  start: Cupola hepatică
  thickness: 0.625 mm
- delay: 70-90 sec
  end: Simfiză pubiană
  name: Tardiv Renal
  notes: Fază tardivă / venoasă complementară
  start: Diafragm
  thickness: 0.625 mm
slug: ct-enterography
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '100'
  mas: Auto (referință 200 mAs)
  pitch: 1.0-1.375
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Entero-CT (Enterografie CT cu Contrast Neutru)
---

# Entero-CT (Enterografie CT cu Contrast Neutru)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Enterică | 45 sec | Cupola hepatică → Simfiză pubiană |
        | Tardiv Renal | 70-90 sec | Diafragm → Simfiză pubiană |

    === "Indicații Clinice"

        - Boala Crohn (activitate, stenoze, traiecte fistuloase)
        - Ocluzie / subocluzie de intestin subțire de cauză neclară
        - Hemoragie digestivă obscură
        - Formațiuni tumorale ale intestinului subțire (tumori carcinoide, GIST, limfoame)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore pentru alimente solide
    - **Premedicație / Pregătire:**
        - Contrast oral neutru (VoLumen sau soluție de manitol/apă): primul flacon (450 mL) la 90 min; al doilea (450 mL) la 60 min; jumătate flacon (225 mL) la 30 min; restul de 225 mL cu 5 min înainte de scanare

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.5 mL/kg |
        | Rată de Flux | 4-5 mL/s |
        | Durată | 25s |
        | Metodă Temporizare | Timp empiric de întârziere (45s) |
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

        - Fază enterică (45 sec). Volum mare de contrast oral neutru pentru distensia anselor. Injectare rapidă în 25 secunde. Scanare la 45 secunde de la debut.

    === "Note Asistent"

        - Abord venos 18-20G. Asigurați consumul conform protocolului orar al volumului de contrast neutru (~1350 mL în total). Se poate administra spasmolitic/antiperistaltic (ex. Buscopan/Glucagon).

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic. Sincronizați cu atenție orarul administrării contrastului oral.

    === "Note Radiolog"

        - Evaluați priza de contrast a peretelui intestinal și grosimea acestuia. Căutați stenoze, traiecte fistuloase, abcese și hipervascularizație mezenterică (semnul pieptenelui).

    === "Sfaturi & Recomandări"

        - Distensia optimă a anselor prin contrast oral este critică. Rata de injectare a contrastului IV trebuie să fie ridicată.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Enterică | Cupola hepatică | Simfiză pubiană | 45 sec | 0.625 mm | Fază enterică optimă pentru peretele intestinal |
    | Tardiv Renal | Diafragm | Simfiză pubiană | 70-90 sec | 0.625 mm | Fază tardivă / venoasă complementară |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Enterică | Abdomen | 2 mm/2 mm | Standard |  | Serie diagnostică primară pentru anse |
    | Coronal | Fază Enterică | Abdomen | 2 mm/2 mm | Standard |  | Evaluarea dispoziției anselor intestinale |
    | Sagital | Fază Enterică | Abdomen | 2 mm/2 mm | Standard |  | Evaluare mezenterică și pelvină |
    | MIP | Fază Enterică | Abdomen | 5 mm/2 mm | Vascular |  | Evaluarea vascularizației mezenterice |
