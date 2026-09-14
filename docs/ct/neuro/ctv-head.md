---
author: null
category: neuro
clinical_indications:
- Tromboză de sinusuri venoase cerebrale (tromboflebită cerebrală)
- Hipertensiune intracraniană idiopatică (pseudotumor cerebri)
- Malformații arteriovenoase durale cu flux inversat
- Bilanț tumoral cu invazie de sinus sagital superior sau lateral
contrast:
  agent: Isovue 370
  duration: 15-20s
  flow_rate: 3-4 mL/s
  roi: ''
  timing: Timp fix de întârziere (45-50s delay)
  trigger: ''
  volume: 75-100 mL
last_updated: '2026-01-01'
notes:
  additional_recons: Randare tridimensională 3D VR flebografică a sinusurilor venoase.
    Proiecții MIP coronale și sagitale.
  nursing: Linie venoasă 18-20G.
  rad: 'Nativ: căutați semnul coardei hiperdense în sinusul trombozat și hemoragii
    venoase. CTV: decelarea defectelor de umplere endoluminale în sinusurile durale
    (semnul delta gol / empty delta sign în sinusul sagital superior, sinusul transvers,
    sigmoid, drept). Tromboze ale venelor corticale.'
  tech: Scanare nativă de craniu inițial, urmată de Flebo-CT (CTV) în fază venoasă
    pură la 45-50 secunde de la debutul injectării. De la baza craniului până la vertex.
  tips: Temporizarea adecvată a fazei venoase este esențială pentru a evita confuzia
    dintre asimetriile anatomice normale (hipoplazie de sinus transvers) și tromboză.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu capul înainte
premedication: ''
protocol_type: vascular
recons:
- acquisition: Flebo-CT Cerebral
  fov: Craniu
  kernel: Brain
  notes: Sinusuri venoase durale și vene corticale
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Flebo-CT Cerebral
  fov: Craniu
  kernel: Brain
  notes: Privire de ansamblu MIP a flebografiei cerebrale
  plane: MIP
  thickness_increment: 5 mm/2 mm
- acquisition: Flebo-CT Cerebral
  fov: Craniu
  kernel: Brain
  notes: Randare tridimensională 3D a arborelui venos cerebral
  plane: 3D VR
  thickness_increment: 0.75 mm/0.75 mm
- acquisition: Flebo-CT Cerebral
  fov: Craniu
  kernel: Brain
  notes: Sinusul sagital superior, sinusul drept și vena Galen
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 0 sec
  end: Gaura occipitală
  name: CT Nativ Craniu
  notes: Referință nativă pentru trombi hiperdenși și hemoragie
  start: Vertex
  thickness: 2.5 mm
- delay: 45-50 sec
  end: Vertex
  name: Flebo-CT Cerebral
  notes: Fază venoasă dedicată pentru sinusurile durale
  start: Baza craniului
  thickness: 0.625 mm
slug: ctv-head
synonyms: []
tech_params:
  aec: Activat (Modulare angulară adaptivă / mAs fix fosa posterioară)
  collimation: 64 × 0.625 mm sau 16 × 0.75 mm
  kv: '120'
  mas: Auto (referință 250 mAs)
  pitch: Helical
  rotation_time: 0.5-0.6s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Flebo-CT Cerebral (CTV Sinusuri Venoase Durale)
---

# Flebo-CT Cerebral (CTV Sinusuri Venoase Durale)

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
        | Flebo-CT Cerebral | 45-50 sec | Baza craniului → Vertex |

    === "Indicații Clinice"

        - Tromboză de sinusuri venoase cerebrale (tromboflebită cerebrală)
        - Hipertensiune intracraniană idiopatică (pseudotumor cerebri)
        - Malformații arteriovenoase durale cu flux inversat
        - Bilanț tumoral cu invazie de sinus sagital superior sau lateral

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul înainte
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 75-100 mL |
        | Rată de Flux | 3-4 mL/s |
        | Durată | 15-20s |
        | Metodă Temporizare | Timp fix de întârziere (45-50s delay) |
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
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare angulară adaptivă / mAs fix fosa posterioară) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 16 × 0.75 mm |
    | **Timp de Rotație** | 0.5-0.6 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare nativă de craniu inițial, urmată de Flebo-CT (CTV) în fază venoasă pură la 45-50 secunde de la debutul injectării. De la baza craniului până la vertex.

    === "Note Asistent"

        - Linie venoasă 18-20G.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Nativ: căutați semnul coardei hiperdense în sinusul trombozat și hemoragii venoase. CTV: decelarea defectelor de umplere endoluminale în sinusurile durale (semnul delta gol / empty delta sign în sinusul sagital superior, sinusul transvers, sigmoid, drept). Tromboze ale venelor corticale.

    === "Sfaturi & Recomandări"

        - Temporizarea adecvată a fazei venoase este esențială pentru a evita confuzia dintre asimetriile anatomice normale (hipoplazie de sinus transvers) și tromboză.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Nativ Craniu | Vertex | Gaura occipitală | 0 sec | 2.5 mm | Referință nativă pentru trombi hiperdenși și hemoragie |
    | Flebo-CT Cerebral | Baza craniului | Vertex | 45-50 sec | 0.625 mm | Fază venoasă dedicată pentru sinusurile durale |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Flebo-CT Cerebral | Craniu | 1 mm/1 mm | Brain |  | Sinusuri venoase durale și vene corticale |
    | MIP | Flebo-CT Cerebral | Craniu | 5 mm/2 mm | Brain |  | Privire de ansamblu MIP a flebografiei cerebrale |
    | 3D VR | Flebo-CT Cerebral | Craniu | 0.75 mm/0.75 mm | Brain |  | Randare tridimensională 3D a arborelui venos cerebral |
    | Sagital | Flebo-CT Cerebral | Craniu | 1.5 mm/1.5 mm | Brain |  | Sinusul sagital superior, sinusul drept și vena Galen |
