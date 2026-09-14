---
author: null
category: neuro
clinical_indications:
- Accident vascular cerebral ischemic acut (Cod AVC)
- Deficit neurologic focal cu debut brusc (< 24 ore)
- Candidat pentru tromboliză intravenoasă și/sau trombectomie mecanică
contrast:
  agent: IsoVue 370 pentru Angio-CT / Perfuzie CT
  flow_rate: 4-5 mL/s
  roi: Multiple ROI
  timing: 'Protocol multifazic AVC: Nativ + Angio-CT + Perfuzie (CTP)'
  trigger: Variabil
  volume: 100 mL
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucții MIP și 3D ale vaselor intracraniene. Hărți cantitative
    de perfuzie (CBF, CBV, MTT, Tmax > 6s). Scorp ASPECTS raportat obligatoriu.
  nursing: Fără linie pentru nativ. Linie venoasă 18-20G cu debit mare plasată imediat
    pentru Angio-CT/CTP. Coordonare de urgență cu echipa de neurologie.
  rad: 'Nativ: hemoragie intracraniană, calculare scor ASPECTS, semne precoce de ischemie
    (ștergerea diferențierii substanță albă-cenușie, semnul arterei cerebrale medii
    hiperdense). Angio-CT: ocluzie de vas mare (LVO - ACM M1/M2, ACI terminală, arteră
    bazilară), colaterale piale. CTP: volum miez necrotic (core) vs. penumbră ischemică
    salvabilă (mismatch).'
  tech: 'Protocol STAT: 1) CT Craniu nativ (excludere hemoragie intracraniană) 2)
    Angio-CT Vase mari gât și cap (arc aortic - vertex) 3) Perfuzie CT (CTP opțional/conform
    protocolului). Minimizați timpul ușă-la-scanare (door-to-needle/groin).'
  tips: Protocol STAT de urgență vitală. Fiecare minut contează ('Time is Brain').
    Detecția ocluziilor mari de vas este prioritară.
npo: Fără repaus alimentar - urgență medicală majoră
position: Decubit dorsal cu capul înainte
premedication: Fără premedicație
protocol_type: neuroradiology
recons:
- acquisition: CT Nativ Craniu
  fov: Craniu
  kernel: Brain
  notes: Detecția imediată a hemoragiei și calcul scor ASPECTS
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: Angio-CT Arc Aortic la Vertex
  fov: Craniu
  kernel: Brain
  notes: Detecția ocluziei de vas mare (LVO)
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: Angio-CT Arc Aortic la Vertex
  fov: Craniu
  kernel: Brain
  notes: MIP pentru rețeaua colaterală vasculară pială
  plane: MIP
  thickness_increment: 5 mm/2 mm
- acquisition: Perfuzie CT (opțional)
  fov: Craniu
  kernel: N/A
  notes: Hărți color de perfuzie cerebrală (CBF, CBV, MTT, Tmax)
  plane: CTP maps
  thickness_increment: 5 mm/5 mm
safety:
  allergy: Consemnați statutul de urgență dacă există antecedente alergice
  renal: Urgență AVC acut - nu se temporizează examinarea sau tromboliza în așteptarea
    creatininei
series:
- delay: 0 sec
  end: Vertex
  name: CT Nativ Craniu
  notes: STAT fără contrast pentru excluderea hemoragiei
  start: Baza craniului
  thickness: 2.5 mm
- delay: Urmărire bolus
  end: Vertex
  name: Angio-CT Arc Aortic la Vertex
  notes: Detecția ocluziilor de vas mare (LVO)
  start: Arc aortic
  thickness: 0.625 mm
- delay: Dinamic
  end: Vertex
  name: Perfuzie CT (opțional)
  notes: Evaluarea penumbrei ischemice dacă pacientul este candidat la trombectomie
  start: Baza craniului
  thickness: 5 mm
slug: brain-stroke-protocol
synonyms: []
tech_params:
  aec: Activat (Modulare angulară adaptivă / mAs fix fosa posterioară)
  collimation: 64 × 0.625 mm sau 16 × 0.75 mm
  kv: '120'
  mas: Auto (referință 300 mAs craniu)
  pitch: '0.5'
  rotation_time: 1.0 / 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: Protocol CT AVC Acut (Cod AVC Cerebral)
---

# Protocol CT AVC Acut (Cod AVC Cerebral)

**Ultima actualizare:** 2026-01-01
**Autor:** None

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Nativ Craniu | 0 sec | Baza craniului → Vertex |
        | Angio-CT Arc Aortic la Vertex | Urmărire bolus | Arc aortic → Vertex |
        | Perfuzie CT (opțional) | Dinamic | Baza craniului → Vertex |

    === "Indicații Clinice"

        - Accident vascular cerebral ischemic acut (Cod AVC)
        - Deficit neurologic focal cu debut brusc (< 24 ore)
        - Candidat pentru tromboliză intravenoasă și/sau trombectomie mecanică

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul înainte
    - **Repaus Alimentar (NPO):** Fără repaus alimentar - urgență medicală majoră
    - **Premedicație / Pregătire:**
        - Fără premedicație

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | IsoVue 370 pentru Angio-CT / Perfuzie CT |
        | Volum | 100 mL |
        | Rată de Flux | 4-5 mL/s |
        | Durată |  |
        | Metodă Temporizare | Protocol multifazic AVC: Nativ + Angio-CT + Perfuzie (CTP) |
        | Poziționare ROI | Multiple ROI |
        | Declanșator (HU) | Variabil |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | Auto (referință 300 mAs craniu) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare angulară adaptivă / mAs fix fosa posterioară) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 16 × 0.75 mm |
    | **Timp de Rotație** | 1.0 / 0.5 s |
    | **Pitch (Factor Pas)** | 0.5 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Protocol STAT: 1) CT Craniu nativ (excludere hemoragie intracraniană) 2) Angio-CT Vase mari gât și cap (arc aortic - vertex) 3) Perfuzie CT (CTP opțional/conform protocolului). Minimizați timpul ușă-la-scanare (door-to-needle/groin).

    === "Note Asistent"

        - Fără linie pentru nativ. Linie venoasă 18-20G cu debit mare plasată imediat pentru Angio-CT/CTP. Coordonare de urgență cu echipa de neurologie.

        !!! warning "Siguranță"
            - **Funcție Renală:** Urgență AVC acut - nu se temporizează examinarea sau tromboliza în așteptarea creatininei
            - **Alergii:** Consemnați statutul de urgență dacă există antecedente alergice

    === "Note Radiolog"

        - Nativ: hemoragie intracraniană, calculare scor ASPECTS, semne precoce de ischemie (ștergerea diferențierii substanță albă-cenușie, semnul arterei cerebrale medii hiperdense). Angio-CT: ocluzie de vas mare (LVO - ACM M1/M2, ACI terminală, arteră bazilară), colaterale piale. CTP: volum miez necrotic (core) vs. penumbră ischemică salvabilă (mismatch).

    === "Sfaturi & Recomandări"

        - Protocol STAT de urgență vitală. Fiecare minut contează ('Time is Brain'). Detecția ocluziilor mari de vas este prioritară.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Nativ Craniu | Baza craniului | Vertex | 0 sec | 2.5 mm | STAT fără contrast pentru excluderea hemoragiei |
    | Angio-CT Arc Aortic la Vertex | Arc aortic | Vertex | Urmărire bolus | 0.625 mm | Detecția ocluziilor de vas mare (LVO) |
    | Perfuzie CT (opțional) | Baza craniului | Vertex | Dinamic | 5 mm | Evaluarea penumbrei ischemice dacă pacientul este candidat la trombectomie |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Nativ Craniu | Craniu | 2.5 mm/2.5 mm | Brain |  | Detecția imediată a hemoragiei și calcul scor ASPECTS |
    | Axial | Angio-CT Arc Aortic la Vertex | Craniu | 1 mm/1 mm | Brain |  | Detecția ocluziei de vas mare (LVO) |
    | MIP | Angio-CT Arc Aortic la Vertex | Craniu | 5 mm/2 mm | Brain |  | MIP pentru rețeaua colaterală vasculară pială |
    | CTP maps | Perfuzie CT (opțional) | Craniu | 5 mm/5 mm | N/A |  | Hărți color de perfuzie cerebrală (CBF, CBV, MTT, Tmax) |
