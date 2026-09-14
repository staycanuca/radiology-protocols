---
author: null
category: abdomen
clinical_indications:
- Litiaza reno-vezicală (nefrolitiază / ureterolitiază)
- Colică renală acută
- Durere acută în flanc
- Hematurie macroscopică recentă
contrast:
  agent: Fără substanță de contrast
  type: non-contrast
last_updated: '2026-01-01'
notes:
  additional_recons: Secțiuni submilimetrice sau de 1 mm pentru calculii mici. Măsurători
    tridimensionale ale calculului.
  nursing: Fără linie venoasă necesară. Fără substanță de contrast orală. Explicați
    pacientului utilizarea tehnicii cu iradiere minimă.
  rad: 'Identificarea calculilor: măsurați dimensiunea maximă și densitatea în HU.
    Verificați prezența hidronefrozei sau a edemului perirenal/periureteral. Evaluați
    posibile diagnostice diferențiale (apendicită, diverticulită etc.).'
  tech: Protocol cu DOZĂ REDUSĂ (Low Dose). mAs redus. Acoperire de la polul superior
    al rinichilor până la simfiza pubiană. Parametri optimizați pentru calculi.
  tips: Protocol doză redusă de radiații. Calitatea imaginii este optimizată specific
    pentru densitatea calculilor calcici și urici.
npo: Nu este necesar repaus alimentar
position: Decubit dorsal cu brațele ridicate
premedication: Fără premedicație. Fără contrast oral.
protocol_type: non-contrast
recons:
- acquisition: Fază Nativă KUB
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Detecția și măsurarea calculilor
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Nativă KUB
  fov: Abdomen-Pelvis
  kernel: Bone
  notes: Fereastră osoasă pentru delimitarea densității calculilor
  plane: Axial
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: Fază Nativă KUB
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Vedere coronală de ansamblu a tractului urinar
  plane: Coronal
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Nativă KUB
  fov: Abdomen-Pelvis
  kernel: Standard
  notes: Localizare topografică a calculului
  plane: MIP
  thickness_increment: 5 mm/2 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică (examinare nativă fără contrast)
series:
- delay: 0 sec
  end: Simfiză pubiană
  name: Fază Nativă KUB
  notes: Achiziție nativă cu doză redusă de iradiere
  start: Polul superior renal
  thickness: 0.625 mm
slug: ct-kub-non-contrast
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: 100-120
  mas: Doză redusă (referință 50-100 mAs)
  pitch: 1.375-1.5
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Renal-Uretero-Vezical Nativ (CT KUB Doză Redusă)
---

# CT Renal-Uretero-Vezical Nativ (CT KUB Doză Redusă)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă KUB | 0 sec | Polul superior renal → Simfiză pubiană |

    === "Indicații Clinice"

        - Litiaza reno-vezicală (nefrolitiază / ureterolitiază)
        - Colică renală acută
        - Durere acută în flanc
        - Hematurie macroscopică recentă

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Nu este necesar repaus alimentar
    - **Premedicație / Pregătire:**
        - Fără premedicație. Fără contrast oral.

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Fără substanță de contrast |
        | Volum |  |
        | Rată de Flux |  |
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
    | **Tensiune Tub (kV)** | 100-120 kV |
    | **Curent Tub (mAs)** | Doză redusă (referință 50-100 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 1.375-1.5 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol cu DOZĂ REDUSĂ (Low Dose). mAs redus. Acoperire de la polul superior al rinichilor până la simfiza pubiană. Parametri optimizați pentru calculi.

    === "Note Asistent"

        - Fără linie venoasă necesară. Fără substanță de contrast orală. Explicați pacientului utilizarea tehnicii cu iradiere minimă.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică (examinare nativă fără contrast)
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Identificarea calculilor: măsurați dimensiunea maximă și densitatea în HU. Verificați prezența hidronefrozei sau a edemului perirenal/periureteral. Evaluați posibile diagnostice diferențiale (apendicită, diverticulită etc.).

    === "Sfaturi & Recomandări"

        - Protocol doză redusă de radiații. Calitatea imaginii este optimizată specific pentru densitatea calculilor calcici și urici.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă KUB | Polul superior renal | Simfiză pubiană | 0 sec | 0.625 mm | Achiziție nativă cu doză redusă de iradiere |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Nativă KUB | Abdomen-Pelvis | 2.5 mm/2.5 mm | Standard |  | Detecția și măsurarea calculilor |
    | Axial | Fază Nativă KUB | Abdomen-Pelvis | 1.25 mm/1.25 mm | Bone |  | Fereastră osoasă pentru delimitarea densității calculilor |
    | Coronal | Fază Nativă KUB | Abdomen-Pelvis | 2.5 mm/2.5 mm | Standard |  | Vedere coronală de ansamblu a tractului urinar |
    | MIP | Fază Nativă KUB | Abdomen-Pelvis | 5 mm/2 mm | Standard |  | Localizare topografică a calculului |
