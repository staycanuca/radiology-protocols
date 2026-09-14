---
author: null
category: neuro
clinical_indications:
- Bilanț complet AVC ischemic / accident ischemic tranzitor (AIT)
- Stenoză carotidiană extracraniană sau intracraniană
- Disecție de arteră carotidă sau vertebrală
- Screening anevrisme cerebrale și malformații arteriovenoase (MAV)
contrast:
  agent: Isovue 370
  flow_rate: 4-5 mL/s
  roi: Crosa aortei
  timing: Urmărire bolus (Bolus Tracking)
  trigger: 150 HU
  volume: 80-100 mL
last_updated: '2026-01-04'
notes:
  additional_recons: Reconstrucții MIP și 3D VR ale axelor vasculare cervico-cerebrale.
    Reconstrucții MPR curbate pentru ambele carotide interne.
  nursing: Acces venos excelent în plica cotului - linie 20G minimum (ideal 18G).
    Verificați refluxul sanguin înainte de pornire.
  rad: Originea vaselor din crosa aortei. Bifurcațiile carotidiene (gradarea stenozei
    conform criteriilor NASCET). Arterele vertebrale pe tot traiectul. Poligonul Willis
    complet (segmentele A1, A2, M1, M2, P1, P2, arterele comunicante). Căutați stenoze,
    tromboze, disecții sau anevrisme saculare.
  tech: Scanare continuă de la crosa aortei până la vertex. Urmărire bolus în crosa
    aortei. Înclinarea gantry-ului dacă este necesar pentru reducerea artefactelor
    produse de amalgamul dentar.
  tips: Îndepărtați protezele dentare. Instruiți pacientul să evite înghițitul în
    timpul achiziției pe gât.
npo: Repaus alimentar 4 ore
position: Decubit dorsal cu capul înainte și brațele de-a lungul corpului
premedication: None typically. Consider anxiolytic if severe claustrophobia
protocol_type: vascular
recons:
- acquisition: Angio-CT Gât
  fov: Gât
  kernel: Vascular
  notes: Secțiuni submilimetrice pentru evaluarea carotidelor
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Angio-CT Cerebral
  fov: Craniu
  kernel: Vascular
  notes: Secțiuni submilimetrice pentru poligonul Willis
  plane: Axial
  thickness_increment: 0.625 mm/0.625 mm
- acquisition: Angio-CT Gât
  fov: Gât-Craniu
  kernel: Vascular
  notes: MIP coronal pentru ansamblul bifurcațiilor carotidiene
  plane: Coronal
  thickness_increment: 2 mm/2 mm
- acquisition: Angio-CT Gât
  fov: Gât-Craniu
  kernel: Vascular
  notes: MIP sagital pentru traiectul arterelor vertebrale
  plane: Sagital
  thickness_increment: 2 mm/2 mm
safety:
  allergy: Verificați istoricul alergic la contrast
  renal: Verificați eGFR > 30 mL/min/1.73m²
series:
- delay: Urmărire bolus
  end: Baza craniului
  name: Angio-CT Gât
  notes: Fază arterială caudo-cranială
  start: Arc aortic
  thickness: 0.625 mm
- delay: Continuare
  end: Vertex
  name: Angio-CT Cerebral
  notes: Același bolus - achiziție unică neîntreruptă
  start: Baza craniului
  thickness: 0.625 mm
slug: cta-head-and-neck-arch-to-vertex
synonyms: []
tech_params:
  aec: Activat (Modulare angulară adaptivă / mAs fix fosa posterioară)
  collimation: 64 × 0.625 mm sau 16 × 0.75 mm
  kv: 100-120
  mas: Auto (referință 250 mAs)
  pitch: '0.9'
  rotation_time: 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Angio-CT Vase Gât și Poligon Willis (Arc Aortic - Vertex)
---

# Angio-CT Vase Gât și Poligon Willis (Arc Aortic - Vertex)

**Ultima actualizare:** 2026-01-04
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Angio-CT Gât | Urmărire bolus | Arc aortic → Baza craniului |
        | Angio-CT Cerebral | Continuare | Baza craniului → Vertex |

    === "Indicații Clinice"

        - Bilanț complet AVC ischemic / accident ischemic tranzitor (AIT)
        - Stenoză carotidiană extracraniană sau intracraniană
        - Disecție de arteră carotidă sau vertebrală
        - Screening anevrisme cerebrale și malformații arteriovenoase (MAV)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul înainte și brațele de-a lungul corpului
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore
    - **Premedicație / Pregătire:**
        - None typically. Consider anxiolytic if severe claustrophobia

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 |
        | Volum | 80-100 mL |
        | Rată de Flux | 4-5 mL/s |
        | Durată |  |
        | Metodă Temporizare | Urmărire bolus (Bolus Tracking) |
        | Poziționare ROI | Crosa aortei |
        | Declanșator (HU) | 150 HU |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 100-120 kV |
    | **Curent Tub (mAs)** | Auto (referință 250 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare angulară adaptivă / mAs fix fosa posterioară) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 16 × 0.75 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare continuă de la crosa aortei până la vertex. Urmărire bolus în crosa aortei. Înclinarea gantry-ului dacă este necesar pentru reducerea artefactelor produse de amalgamul dentar.

    === "Note Asistent"

        - Acces venos excelent în plica cotului - linie 20G minimum (ideal 18G). Verificați refluxul sanguin înainte de pornire.

        !!! warning "Siguranță"
            - **Funcție Renală:** Verificați eGFR > 30 mL/min/1.73m²
            - **Alergii:** Verificați istoricul alergic la contrast

    === "Note Radiolog"

        - Originea vaselor din crosa aortei. Bifurcațiile carotidiene (gradarea stenozei conform criteriilor NASCET). Arterele vertebrale pe tot traiectul. Poligonul Willis complet (segmentele A1, A2, M1, M2, P1, P2, arterele comunicante). Căutați stenoze, tromboze, disecții sau anevrisme saculare.

    === "Sfaturi & Recomandări"

        - Îndepărtați protezele dentare. Instruiți pacientul să evite înghițitul în timpul achiziției pe gât.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Angio-CT Gât | Arc aortic | Baza craniului | Urmărire bolus | 0.625 mm | Fază arterială caudo-cranială |
    | Angio-CT Cerebral | Baza craniului | Vertex | Continuare | 0.625 mm | Același bolus - achiziție unică neîntreruptă |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Angio-CT Gât | Gât | 1 mm/1 mm | Vascular |  | Secțiuni submilimetrice pentru evaluarea carotidelor |
    | Axial | Angio-CT Cerebral | Craniu | 0.625 mm/0.625 mm | Vascular |  | Secțiuni submilimetrice pentru poligonul Willis |
    | Coronal | Angio-CT Gât | Gât-Craniu | 2 mm/2 mm | Vascular |  | MIP coronal pentru ansamblul bifurcațiilor carotidiene |
    | Sagital | Angio-CT Gât | Gât-Craniu | 2 mm/2 mm | Vascular |  | MIP sagital pentru traiectul arterelor vertebrale |
