---
author: null
category: abdomen
clinical_indications:
- Formațiune tumorală pancreatică / suspiciune adenocarcinom
- Complicații pancreatită acută sau cronică
- Caracterizarea leziunilor chistice pancreatice
contrast:
  agent: Isovue 370
  duration: 25s
  flow_rate: 4-5 mL/s
  roi: Aorta abdominală
  timing: 'Fază dublă: arterială pancreatică parenchimatoasă + venoasă portală'
  trigger: 150 HU
  volume: 1.5 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții MPR curbate pe canalul pancreatic principal (Wirsung).
    Reconstrucții MIP pentru axul vascular peripancreatic.
  nursing: Abord venos 18-20G. Asigurați ingestia completă de apă pentru distensia
    duodenală.
  rad: 'Faza pancreatică: încărcare optimă a parenchimului și decelarea leziunilor
    hipovasculare mici. Faza portală: detecția metastazelor hepatice și invazia venoasă
    (VMS, trunchi portal).'
  tech: 'DOUĂ faze: Fază pancreatică parenchimatoasă (40-45s sau urmărire bolus) +
    Fază venoasă portală (70s). Apă pentru contrast negativ endoluminal.'
  tips: Distensia duodenului cu apă este esențială pentru demarcarea capului pancreatic.
    Secțiuni fine obligatorii.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: 'Apă per os: 900 mL apă oral cu 15-30 min înainte de scanare pentru
  distensie gastrică și duodenală'
protocol_type: contrast-enhanced
recons:
- acquisition: Fază Pancreatică
  fov: Abdomen
  kernel: Standard
  notes: Secțiuni fine pentru parenchimul pancreatic
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Fază Venoasă Portală
  fov: Abdomen
  kernel: Standard
  notes: Evaluare ficat și structuri venoase
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Pancreatică
  fov: Abdomen
  kernel: Standard
  notes: Plan coronal pentru regiunea pancreatică și peripancreatică
  plane: Coronal
  thickness_increment: 2 mm/2 mm
- acquisition: Fază Pancreatică
  fov: Pancreas
  kernel: Standard
  notes: Evaluare canal Wirsung și cale biliară principală
  plane: Curved MPR
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Verificați istoricul alergic. Coordonați temporizarea consumului de apă.
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 40-45 sec
  end: Sub bifurcația aortei
  name: Fază Pancreatică
  notes: Fază arterială pancreatică parenchimatoasă optimă
  start: Cupola hepatică
  thickness: 0.625 mm
- delay: 70 sec
  end: Simfiză pubiană
  name: Fază Venoasă Portală
  notes: Fază venoasă portală completă abdomen-pelvis
  start: Diafragm
  thickness: 0.625 mm
slug: ct-biphasic-pancreas
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '100'
  mas: Auto (referință 200-250 mAs)
  pitch: 0.9-1.0
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Pancreas Bifazic (Protocol Masă Pancreatică)
---

# CT Pancreas Bifazic (Protocol Masă Pancreatică)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Pancreatică | 40-45 sec | Cupola hepatică → Sub bifurcația aortei |
        | Fază Venoasă Portală | 70 sec | Diafragm → Simfiză pubiană |

    === "Indicații Clinice"

        - Formațiune tumorală pancreatică / suspiciune adenocarcinom
        - Complicații pancreatită acută sau cronică
        - Caracterizarea leziunilor chistice pancreatice

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Apă per os: 900 mL apă oral cu 15-30 min înainte de scanare pentru distensie gastrică și duodenală

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.5 mL/kg |
        | Rată de Flux | 4-5 mL/s |
        | Durată | 25s |
        | Metodă Temporizare | Fază dublă: arterială pancreatică parenchimatoasă + venoasă portală |
        | Poziționare ROI | Aorta abdominală |
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
    | **Curent Tub (mAs)** | Auto (referință 200-250 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9-1.0 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - DOUĂ faze: Fază pancreatică parenchimatoasă (40-45s sau urmărire bolus) + Fază venoasă portală (70s). Apă pentru contrast negativ endoluminal.

    === "Note Asistent"

        - Abord venos 18-20G. Asigurați ingestia completă de apă pentru distensia duodenală.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic. Coordonați temporizarea consumului de apă.

    === "Note Radiolog"

        - Faza pancreatică: încărcare optimă a parenchimului și decelarea leziunilor hipovasculare mici. Faza portală: detecția metastazelor hepatice și invazia venoasă (VMS, trunchi portal).

    === "Sfaturi & Recomandări"

        - Distensia duodenului cu apă este esențială pentru demarcarea capului pancreatic. Secțiuni fine obligatorii.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Pancreatică | Cupola hepatică | Sub bifurcația aortei | 40-45 sec | 0.625 mm | Fază arterială pancreatică parenchimatoasă optimă |
    | Fază Venoasă Portală | Diafragm | Simfiză pubiană | 70 sec | 0.625 mm | Fază venoasă portală completă abdomen-pelvis |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Pancreatică | Abdomen | 1.25 mm/1.25 mm | Standard |  | Secțiuni fine pentru parenchimul pancreatic |
    | Axial | Fază Venoasă Portală | Abdomen | 2.5 mm/2.5 mm | Standard |  | Evaluare ficat și structuri venoase |
    | Coronal | Fază Pancreatică | Abdomen | 2 mm/2 mm | Standard |  | Plan coronal pentru regiunea pancreatică și peripancreatică |
    | Curved MPR | Fază Pancreatică | Pancreas | 1 mm/1 mm | Standard |  | Evaluare canal Wirsung și cale biliară principală |
