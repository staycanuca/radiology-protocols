---
author: null
category: abdomen
clinical_indications:
- Dureri abdominale de cauză neelucidată
- Stadializare și reevaluare oncologică
- Identificarea focarului de infecție intraabdominal
- Complicații post-operatorii abdominale
contrast:
  agent: Isovue 370
  duration: 40s
  flow_rate: 3 mL/s
  timing: Timp empiric de întârziere (70s)
  volume: 1.5 mL/kg
last_updated: '2026-01-02'
notes:
  additional_recons: Reconstrucții cu secțiuni fine de 1 mm pentru randare 3D dacă
    este identificată o formațiune tumorală.
  nursing: Abord venos periferic 20-22G necesar. Verificați permeabilitatea căii venoase.
    Contrast oral 250-500 mL apă înainte de scanare.
  rad: Examinare sistematică a tuturor organelor parenchimatoase. Căutați colecții
    lichidiene sau aer liber intraperitoneal. Evaluați modelul de încărcare al pereților
    digestivi.
  tech: 'Asigurați opacifierea adecvată a tubului digestiv prin contrast oral. Scanare
    de la nivelul diafragmului până la simfiza pubiană. Timp tipic de întârziere:
    70 secunde.'
  tips: Brațele complet ridicate. Îndepărtați toate obiectele metalice din câmpul
    de scanare.
npo: Repaus alimentar 4 ore pentru alimente solide
position: Decubit dorsal cu brațele ridicate
premedication: 'Contrast oral: 900 mL Readi-Cat 2 fracționat pe parcursul a 90 minute.
  Ultimul pahar cu 30 min înainte de scanare'
protocol_type: contrast-enhanced
recons:
- acquisition: Fază Venoasă Portală
  fov: Abdomen
  kernel: Standard
  notes: Serie diagnostică primară
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Tardiv Renal
  fov: Abdomen
  kernel: Standard
  notes: Serie tardivă renală
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Fază Venoasă Portală
  fov: Abdomen
  kernel: Standard
  notes: Reconstrucții coronale de ansamblu
  plane: Coronal
  thickness_increment: 3 mm/3 mm
- acquisition: Fază Venoasă Portală
  fov: Abdomen
  kernel: Standard
  notes: Reconstrucții sagitale pentru ansele intestinale
  plane: Sagital
  thickness_increment: 3 mm/3 mm
safety:
  allergy: Verificați istoricul alergic. Premedicație dacă există reacție alergică
    anterioară la contrast.
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 70 sec
  end: Mici trohantere
  name: Fază Venoasă Portală
  notes: Temporizare standard fază venoasă portală
  start: Diafragm
  thickness: 0.625 mm
- delay: 300 sec
  end: 1-2cm sub rinichi
  name: Tardiv Renal
  notes: Serie tardivă de evaluare renală
  start: 1-2cm deasupra rinichilor
  thickness: 0.625 mm
slug: ct-abdomen-pelvis-with-contrast
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
title: CT Abdomen și Pelvis cu Substanță de Contrast
---

# CT Abdomen și Pelvis cu Substanță de Contrast

**Ultima actualizare:** 2026-01-02
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Venoasă Portală | 70 sec | Diafragm → Mici trohantere |
        | Tardiv Renal | 300 sec | 1-2cm deasupra rinichilor → 1-2cm sub rinichi |

    === "Indicații Clinice"

        - Dureri abdominale de cauză neelucidată
        - Stadializare și reevaluare oncologică
        - Identificarea focarului de infecție intraabdominal
        - Complicații post-operatorii abdominale

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore pentru alimente solide
    - **Premedicație / Pregătire:**
        - Contrast oral: 900 mL Readi-Cat 2 fracționat pe parcursul a 90 minute. Ultimul pahar cu 30 min înainte de scanare

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

        - Asigurați opacifierea adecvată a tubului digestiv prin contrast oral. Scanare de la nivelul diafragmului până la simfiza pubiană. Timp tipic de întârziere: 70 secunde.

    === "Note Asistent"

        - Abord venos periferic 20-22G necesar. Verificați permeabilitatea căii venoase. Contrast oral 250-500 mL apă înainte de scanare.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic. Premedicație dacă există reacție alergică anterioară la contrast.

    === "Note Radiolog"

        - Examinare sistematică a tuturor organelor parenchimatoase. Căutați colecții lichidiene sau aer liber intraperitoneal. Evaluați modelul de încărcare al pereților digestivi.

    === "Sfaturi & Recomandări"

        - Brațele complet ridicate. Îndepărtați toate obiectele metalice din câmpul de scanare.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Venoasă Portală | Diafragm | Mici trohantere | 70 sec | 0.625 mm | Temporizare standard fază venoasă portală |
    | Tardiv Renal | 1-2cm deasupra rinichilor | 1-2cm sub rinichi | 300 sec | 0.625 mm | Serie tardivă de evaluare renală |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Venoasă Portală | Abdomen | 2.5 mm/2.5 mm | Standard |  | Serie diagnostică primară |
    | Axial | Tardiv Renal | Abdomen | 2.5 mm/2.5 mm | Standard |  | Serie tardivă renală |
    | Coronal | Fază Venoasă Portală | Abdomen | 3 mm/3 mm | Standard |  | Reconstrucții coronale de ansamblu |
    | Sagital | Fază Venoasă Portală | Abdomen | 3 mm/3 mm | Standard |  | Reconstrucții sagitale pentru ansele intestinale |
