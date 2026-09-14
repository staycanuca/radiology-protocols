---
author: null
category: neuro
clinical_indications:
- Formațiune tumorală cervicală / suspiciune neoplazie căi aero-digestive superioare
- Infecție profundă a spațiilor gâtului (flegmon periamigdalian, abces retrofaringian,
  abces parafaringian)
- Adenopatii cervicale de etiologie necunoscută
- Evaluarea căilor respiratorii superioare (laringe, trahee cervicală)
contrast:
  agent: Omnipaque 350
  flow_rate: 3 mL/s
  timing: Timp empiric (60-70s delay)
  volume: 100 mL
last_updated: '2026-01-01'
notes:
  additional_recons: Evaluarea compartimentată a tuturor spațiilor cervicale. Măsurarea
    ganglionilor limfatici. Diametrul căilor aeriene laringo-traheale.
  nursing: Linie venoasă 18-20G. Antrenați pacientul să respire liniștit și să evite
    complet deglutiția în timpul scanării.
  rad: 'Spațiile profunde ale gâtului: retrofaringian, parafaringian, masticator,
    parotidian, submandibular, visceral. Loja tiroidiană. Stadializarea ganglionară
    cervicală (nivelurile I-VII). Diferențierea flegmon vs. abces colectat cu perete
    captant.'
  tech: De la baza craniului până la apertura toracică superioară. Întârziere de 60-70
    secunde pentru faza venoasă cervicală optimă. Brațele coborâte la maxim. Instruiți
    pacientul să NU înghită în timpul achiziției.
  tips: Coborâți umerii la maxim. Interzicerea deglutiției elimină artefactele de
    mișcare pe laringe și hipofaringe.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele coborâte de-a lungul corpului
premedication: ''
protocol_type: contrast-enhanced
recons:
- acquisition: CT Cervical cu Contrast
  fov: Gât
  kernel: Standard
  notes: Fereastră de părți moi cervicale
  plane: Axial
  thickness_increment: 2 mm/2 mm
- acquisition: CT Cervical cu Contrast
  fov: Gât
  kernel: Standard
  notes: Plan coronal pentru spațiile parafaringiene și tiroidă
  plane: Coronal
  thickness_increment: 2 mm/2 mm
- acquisition: CT Cervical cu Contrast
  fov: Gât
  kernel: Standard
  notes: Plan sagital pentru calea aeriană și spațiul retrofaringian
  plane: Sagital
  thickness_increment: 2 mm/2 mm
safety:
  allergy: Verificați istoricul alergic la contrast iodat
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: 65 sec
  end: Apertura toracică superioară
  name: CT Cervical cu Contrast
  notes: Fază venoasă pentru opacifierea spațiilor profunde
  start: Baza craniului
  thickness: 0.625 mm
slug: ct-soft-tissue-neck
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 200-250 mAs)
  pitch: '1'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Părți Moi Gât / Regiune Cervicală cu Substanță de Contrast
---

# CT Părți Moi Gât / Regiune Cervicală cu Substanță de Contrast

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Cervical cu Contrast | 65 sec | Baza craniului → Apertura toracică superioară |

    === "Indicații Clinice"

        - Formațiune tumorală cervicală / suspiciune neoplazie căi aero-digestive superioare
        - Infecție profundă a spațiilor gâtului (flegmon periamigdalian, abces retrofaringian, abces parafaringian)
        - Adenopatii cervicale de etiologie necunoscută
        - Evaluarea căilor respiratorii superioare (laringe, trahee cervicală)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele coborâte de-a lungul corpului
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 |
        | Volum | 100 mL |
        | Rată de Flux | 3 mL/s |
        | Durată |  |
        | Metodă Temporizare | Timp empiric (60-70s delay) |
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
    | **Pitch (Factor Pas)** | 1 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - De la baza craniului până la apertura toracică superioară. Întârziere de 60-70 secunde pentru faza venoasă cervicală optimă. Brațele coborâte la maxim. Instruiți pacientul să NU înghită în timpul achiziției.

    === "Note Asistent"

        - Linie venoasă 18-20G. Antrenați pacientul să respire liniștit și să evite complet deglutiția în timpul scanării.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic la contrast iodat

    === "Note Radiolog"

        - Spațiile profunde ale gâtului: retrofaringian, parafaringian, masticator, parotidian, submandibular, visceral. Loja tiroidiană. Stadializarea ganglionară cervicală (nivelurile I-VII). Diferențierea flegmon vs. abces colectat cu perete captant.

    === "Sfaturi & Recomandări"

        - Coborâți umerii la maxim. Interzicerea deglutiției elimină artefactele de mișcare pe laringe și hipofaringe.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Cervical cu Contrast | Baza craniului | Apertura toracică superioară | 65 sec | 0.625 mm | Fază venoasă pentru opacifierea spațiilor profunde |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Cervical cu Contrast | Gât | 2 mm/2 mm | Standard |  | Fereastră de părți moi cervicale |
    | Coronal | CT Cervical cu Contrast | Gât | 2 mm/2 mm | Standard |  | Plan coronal pentru spațiile parafaringiene și tiroidă |
    | Sagital | CT Cervical cu Contrast | Gât | 2 mm/2 mm | Standard |  | Plan sagital pentru calea aeriană și spațiul retrofaringian |
