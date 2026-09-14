---
author: null
category: msk
clinical_indications:
- Leziuni de burelet glenoidian (labrum) - leziuni SLAP, Bankart
- Rupturi parțiale sau transfixiante ale coafei rotatorilor
- Instabilitate glenohumerală recidivantă / luxație anterioară sau posterioară
- Leziuni capsulo-ligamentare (ligamente glenohumerale)
contrast:
  agent: Omnipaque 240 sau 300 diluat cu ser fiziologic
  flow_rate: Injectare manuală fluoroghidată / ecoghidată
  volume: 12-15 mL administrat intra-articular
last_updated: '2026-01-01'
notes:
  additional_recons: Planuri oblice coronale (paralele cu tendonul supraspinos) și
    oblice sagitale. Reformatări în poziție ABER (abducție și rotație externă) dacă
    s-a efectuat manevra.
  nursing: Puncția articulară este efectuată de medicul radiolog în condiții riguroase
    de asepsie. Transferul imediat al pacientului la CT.
  rad: Integritatea labrumului glenoidian anterior, posterior și superior (SLAP).
    Rupturi ale tendoanelor coafei rotatorilor (supraspinos, infraspinos, subscapular).
    Extravazarea contrastului, chisturi paralabrale, leziuni osoase Hill-Sachs și
    Bankart osos.
  tech: Scanare CT imediat după injectarea intra-articulară a substanței de contrast
    iodate. Scurtați intervalul dintre puncție și scanare pentru a evita resorbția
    contrastului. Secțiuni submilimetrice pentru detaliul labrumului.
  tips: Scanare efectuată fără întârziere post-injectare. Secțiuni fine obligatorii.
npo: Repaus alimentar 2 ore
position: Decubit dorsal cu brațul în poziție neutră sau rotație ușoară externă
premedication: Intra-articular contrast injection by radiologist
protocol_type: musculoskeletal
recons:
- acquisition: Artro-CT Umăr
  fov: Umăr
  kernel: Standard
  notes: Secțiuni fine pentru detaliul labrumului anterior și posterior
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Artro-CT Umăr
  fov: Umăr
  kernel: Standard
  notes: Plan oblic coronal de-a lungul tendonului supraspinos
  plane: Coronal
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Artro-CT Umăr
  fov: Umăr
  kernel: Standard
  notes: Plan oblic sagital pe fosa glenoidă
  plane: Sagital
  thickness_increment: 1.5 mm/1.5 mm
- acquisition: Artro-CT Umăr
  fov: Umăr
  kernel: Standard
  notes: Poziție ABER (abducție și rotație externă) dacă a fost realizată
  plane: Abduction ABER
  thickness_increment: 1.5 mm/1.5 mm
safety:
  allergy: Verificați riscul de alergie la contrast iodat
  renal: Nu este limitat de funcția renală (administrare intra-articulară)
series:
- delay: Imediat post-injectare
  end: Humerus proximal
  name: Artro-CT Umăr
  notes: Secțiuni submilimetrice pentru bureletul glenoidian
  start: Acromion
  thickness: 0.625 mm
slug: ct-arthrogram-shoulder
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '120'
  mas: Auto (referință 150-200 mAs)
  pitch: Helical
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Artro-CT Umăr
---

# Artro-CT Umăr

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Artro-CT Umăr | Imediat post-injectare | Acromion → Humerus proximal |

    === "Indicații Clinice"

        - Leziuni de burelet glenoidian (labrum) - leziuni SLAP, Bankart
        - Rupturi parțiale sau transfixiante ale coafei rotatorilor
        - Instabilitate glenohumerală recidivantă / luxație anterioară sau posterioară
        - Leziuni capsulo-ligamentare (ligamente glenohumerale)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat locomotor & Articulații*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațul în poziție neutră sau rotație ușoară externă
    - **Repaus Alimentar (NPO):** Repaus alimentar 2 ore
    - **Premedicație / Pregătire:**
        - Intra-articular contrast injection by radiologist

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 240 sau 300 diluat cu ser fiziologic |
        | Volum | 12-15 mL administrat intra-articular |
        | Rată de Flux | Injectare manuală fluoroghidată / ecoghidată |
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
    | **Curent Tub (mAs)** | Auto (referință 150-200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | Helical |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare CT imediat după injectarea intra-articulară a substanței de contrast iodate. Scurtați intervalul dintre puncție și scanare pentru a evita resorbția contrastului. Secțiuni submilimetrice pentru detaliul labrumului.

    === "Note Asistent"

        - Puncția articulară este efectuată de medicul radiolog în condiții riguroase de asepsie. Transferul imediat al pacientului la CT.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu este limitat de funcția renală (administrare intra-articulară)
            - **Alergii:** Verificați riscul de alergie la contrast iodat

    === "Note Radiolog"

        - Integritatea labrumului glenoidian anterior, posterior și superior (SLAP). Rupturi ale tendoanelor coafei rotatorilor (supraspinos, infraspinos, subscapular). Extravazarea contrastului, chisturi paralabrale, leziuni osoase Hill-Sachs și Bankart osos.

    === "Sfaturi & Recomandări"

        - Scanare efectuată fără întârziere post-injectare. Secțiuni fine obligatorii.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Artro-CT Umăr | Acromion | Humerus proximal | Imediat post-injectare | 0.625 mm | Secțiuni submilimetrice pentru bureletul glenoidian |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Artro-CT Umăr | Umăr | 1 mm/1 mm | Standard |  | Secțiuni fine pentru detaliul labrumului anterior și posterior |
    | Coronal | Artro-CT Umăr | Umăr | 1.5 mm/1.5 mm | Standard |  | Plan oblic coronal de-a lungul tendonului supraspinos |
    | Sagital | Artro-CT Umăr | Umăr | 1.5 mm/1.5 mm | Standard |  | Plan oblic sagital pe fosa glenoidă |
    | Abduction ABER | Artro-CT Umăr | Umăr | 1.5 mm/1.5 mm | Standard |  | Poziție ABER (abducție și rotație externă) dacă a fost realizată |
