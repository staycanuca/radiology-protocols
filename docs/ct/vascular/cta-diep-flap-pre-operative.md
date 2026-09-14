---
author: null
category: vascular
clinical_indications:
- Planificare pre-operatorie pentru reconstrucție mamară cu lambou liber DIEP (Deep
  Inferior Epigastric Perforator)
- Cartografierea perforatoarelor arterei epigastrice inferioare profunde
contrast:
  agent: Isovue 370
  duration: 20s
  flow_rate: 4-5 mL/s
  roi: Aorta abdominală
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 150 HU
  volume: 1.5 mL/kg
last_updated: '2026-01-01'
notes:
  additional_recons: Randare tridimensională 3D VR codificată color a peretelui abdominal
    și perforatoarelor. Măsurarea distanțelor în plan x-y față de ombilic.
  nursing: Linie venoasă 18-20G.
  rad: Cartografiați sediul ramurilor perforatoare. Măsurați calibrul vaselor perforatoare
    la emergența din fascia musculară a dreptului abdominal. Identificați perforatoarea
    dominantă. Precizați raportul topografic față de ombilic (de preferat cele subombilicale).
    Menționați traiectul intramuscular (lung vs. scurt).
  tech: Scanare de la mijlocul ficatului până la marii trohanteri. Îndepărtați lenjeria
    strânsă pe corp pentru a nu comprima vasele cutanate. Dacă pacienta poate, se
    recomandă ridicarea ușoară a picioarelor înainte de injectare pentru stimularea
    fluxului.
  tips: Brațele poziționate astfel încât să nu creeze artefacte pe peretele abdominal
    anterior.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu brațele ridicate
premedication: ''
protocol_type: vascular
recons:
- acquisition: Angio-CT Arterial
  fov: Perete abdominal
  kernel: Vascular
  notes: Secțiuni fine pentru identificarea perforatoarelor
  plane: Axial
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: Angio-CT Arterial
  fov: Perete abdominal
  kernel: Vascular
  notes: MIP pentru vizualizarea traiectului perforatoarelor
  plane: Coronal
  thickness_increment: 1 mm/1 mm
- acquisition: Angio-CT Arterial
  fov: Perete abdominal
  kernel: Vascular
  notes: Vederi sagitale ale perforatoarelor traversând fascia
  plane: Sagital
  thickness_increment: 1 mm/1 mm
- acquisition: Angio-CT Arterial
  fov: Perete abdominal
  kernel: Vascular
  notes: Reconstrucție 3D pentru planificarea chirurgicală a lamboului
  plane: 3D VR
  thickness_increment: 0.75 mm/0.75 mm
safety:
  allergy: Verificați istoricul alergic
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: Urmărire bolus
  end: Simfiză pubiană
  name: Angio-CT Arterial
  notes: Focus pe peretele abdominal anterior și perforatoare
  start: Apendice xifoid
  thickness: 0.625 mm
slug: cta-diep-flap-pre-operative
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D conform topogramei / scout)
  collimation: 'Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm)'
  kv: '100'
  mas: Auto (referință 200 mAs)
  pitch: '0.9'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Pre-operator Lambou DIEP (Reconstrucție Mamară)
---

# Angio-CT Pre-operator Lambou DIEP (Reconstrucție Mamară)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Arterial | Urmărire bolus | Apendice xifoid → Simfiză pubiană |

    === "Indicații Clinice"

        - Planificare pre-operatorie pentru reconstrucție mamară cu lambou liber DIEP (Deep Inferior Epigastric Perforator)
        - Cartografierea perforatoarelor arterei epigastrice inferioare profunde

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat cardiovascular & Sistem vascular*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 1.5 mL/kg |
        | Rată de Flux | 4-5 mL/s |
        | Durată | 20s |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
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
    | **Curent Tub (mAs)** | Auto (referință 200 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | Sub-milimetrică (ex: 64 × 0.625 mm / 128 × 0.6 mm) |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare de la mijlocul ficatului până la marii trohanteri. Îndepărtați lenjeria strânsă pe corp pentru a nu comprima vasele cutanate. Dacă pacienta poate, se recomandă ridicarea ușoară a picioarelor înainte de injectare pentru stimularea fluxului.

    === "Note Asistent"

        - Linie venoasă 18-20G.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic

    === "Note Radiolog"

        - Cartografiați sediul ramurilor perforatoare. Măsurați calibrul vaselor perforatoare la emergența din fascia musculară a dreptului abdominal. Identificați perforatoarea dominantă. Precizați raportul topografic față de ombilic (de preferat cele subombilicale). Menționați traiectul intramuscular (lung vs. scurt).

    === "Sfaturi & Recomandări"

        - Brațele poziționate astfel încât să nu creeze artefacte pe peretele abdominal anterior.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Arterial | Apendice xifoid | Simfiză pubiană | Urmărire bolus | 0.625 mm | Focus pe peretele abdominal anterior și perforatoare |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Arterial | Perete abdominal | 0.625 mm/0.625 mm | Vascular |  | Secțiuni fine pentru identificarea perforatoarelor |
    | Coronal | Angio-CT Arterial | Perete abdominal | 1 mm/1 mm | Vascular |  | MIP pentru vizualizarea traiectului perforatoarelor |
    | Sagital | Angio-CT Arterial | Perete abdominal | 1 mm/1 mm | Vascular |  | Vederi sagitale ale perforatoarelor traversând fascia |
    | 3D VR | Angio-CT Arterial | Perete abdominal | 0.75 mm/0.75 mm | Vascular |  | Reconstrucție 3D pentru planificarea chirurgicală a lamboului |
