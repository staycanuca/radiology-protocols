---
author: null
category: trauma
clinical_indications:
- Traumatism facial sever / agresiune fizică
- Fracturi maxilo-faciale complexe (Le Fort, mandibulă, oase proprii nazale)
- Fracturi de orbită asociate cu suspiciune de traumatism cranian și cervical
contrast:
  agent: N/A
  type: non-contrast
last_updated: '2026-01-01'
notes:
  additional_recons: Reconstrucție tridimensională (3D VR) a feței. Clasificare Le
    Fort. Evaluarea atentă a planșeului și peretelui medial orbitar.
  nursing: Precauții de imobilizare cervicală. Documentați mecanismul traumatismului.
  rad: 'Craniu: leziuni intracraniene post-traumatice. Coloană: fracturi și stabilitate.
    Masiv facial: fracturi de tip Le Fort (I, II, III), fracturi orbitare (blowout),
    fracturi mandibulare și ale arcurilor zigomatice.'
  tech: 'TREI achiziții: 1) Craniu 2) Coloană cervicală 3) Masiv facial. Față: achiziție
    elicoidală submilimetrică optimizată pentru randare 3D. Gulerul cervical rămâne
    fixat.'
  tips: Mențineți gulerul cervical montat. Îndepărtați protezele dentare mobile dacă
    este în siguranță pentru pacient.
npo: Fără repaus alimentar - urgență
position: Decubit dorsal cu capul înainte. Guler cervical montat
premedication: ''
protocol_type: trauma
recons:
- acquisition: CT Nativ Craniu
  fov: Craniu
  kernel: Brain/Bone
  notes: Parenchim cerebral și calotă craniană
  plane: Axial
  thickness_increment: 2.5 mm/2.5 mm
- acquisition: CT Nativ Coloană Cervicală
  fov: Coloană cervicală
  kernel: Bone
  notes: Aliniament coloană cervicală
  plane: Sagital
  thickness_increment: 1.25 mm/1.25 mm
- acquisition: CT Nativ Masiv Facial
  fov: Față
  kernel: Bone
  notes: Oase faciale și sinusuri paranazale
  plane: Axial
  thickness_increment: 1 mm/1 mm
- acquisition: CT Nativ Masiv Facial
  fov: Față
  kernel: Bone
  notes: Plan coronal pentru orbite și schelet facial
  plane: Coronal
  thickness_increment: 1 mm/1 mm
safety:
  allergy: Nu se aplică
  renal: Nu se aplică (examinare nativă)
series:
- delay: 0 sec
  end: Gaura occipitală
  name: CT Nativ Craniu
  notes: Examinare standard nativă de craniu
  start: Vertex
  thickness: 1.25 mm
- delay: 0 sec
  end: T1
  name: CT Nativ Coloană Cervicală
  notes: Achiziție elicoidală submilimetrică
  start: Baza craniului
  thickness: 0.625 mm
- delay: 0 sec
  end: Marginea inferioară mandibulară
  name: CT Nativ Masiv Facial
  notes: Achiziție submilimetrică dedicată pentru randare 3D
  start: Sinusuri frontale
  thickness: 0.625 mm
slug: trauma-head-c-spine-and-facial-bones
synonyms: []
tech_params:
  aec: Activat (Modulare automată 3D pentru politraumă)
  collimation: 64 × 0.625 mm sau 16 × 0.75 mm
  kv: '120'
  mas: Auto (300 mAs craniu / 250 mAs alte regiuni)
  pitch: '0.5'
  rotation_time: 1.0 / 0.5s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Craniu, Coloană Cervicală și Masiv Facial în Traumatism
---

# CT Craniu, Coloană Cervicală și Masiv Facial în Traumatism

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
        | CT Nativ Coloană Cervicală | 0 sec | Baza craniului → T1 |
        | CT Nativ Masiv Facial | 0 sec | Sinusuri frontale → Marginea inferioară mandibulară |

    === "Indicații Clinice"

        - Traumatism facial sever / agresiune fizică
        - Fracturi maxilo-faciale complexe (Le Fort, mandibulă, oase proprii nazale)
        - Fracturi de orbită asociate cu suspiciune de traumatism cranian și cervical

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Traumatisme & Politraumă*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu capul înainte. Guler cervical montat
    - **Repaus Alimentar (NPO):** Fără repaus alimentar - urgență
    - **Premedicație / Pregătire:**
        - Nu este necesară

-   __3. Contrast IV & Injectare__

    ---
    !!! info "Fără Contrast Intravenos"
    Acest protocol nu necesită administrare de contrast intravenos.

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | Auto (300 mAs craniu / 250 mAs alte regiuni) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D pentru politraumă) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm sau 16 × 0.75 mm |
    | **Timp de Rotație** | 1.0 / 0.5 s |
    | **Pitch (Factor Pas)** | 0.5 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - TREI achiziții: 1) Craniu 2) Coloană cervicală 3) Masiv facial. Față: achiziție elicoidală submilimetrică optimizată pentru randare 3D. Gulerul cervical rămâne fixat.

    === "Note Asistent"

        - Precauții de imobilizare cervicală. Documentați mecanismul traumatismului.

        !!! warning "Siguranță"
            - **Funcție Renală:** Nu se aplică (examinare nativă)
            - **Alergii:** Nu se aplică

    === "Note Radiolog"

        - Craniu: leziuni intracraniene post-traumatice. Coloană: fracturi și stabilitate. Masiv facial: fracturi de tip Le Fort (I, II, III), fracturi orbitare (blowout), fracturi mandibulare și ale arcurilor zigomatice.

    === "Sfaturi & Recomandări"

        - Mențineți gulerul cervical montat. Îndepărtați protezele dentare mobile dacă este în siguranță pentru pacient.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Nativ Craniu | Vertex | Gaura occipitală | 0 sec | 1.25 mm | Examinare standard nativă de craniu |
    | CT Nativ Coloană Cervicală | Baza craniului | T1 | 0 sec | 0.625 mm | Achiziție elicoidală submilimetrică |
    | CT Nativ Masiv Facial | Sinusuri frontale | Marginea inferioară mandibulară | 0 sec | 0.625 mm | Achiziție submilimetrică dedicată pentru randare 3D |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | CT Nativ Craniu | Craniu | 2.5 mm/2.5 mm | Brain/Bone |  | Parenchim cerebral și calotă craniană |
    | Sagital | CT Nativ Coloană Cervicală | Coloană cervicală | 1.25 mm/1.25 mm | Bone |  | Aliniament coloană cervicală |
    | Axial | CT Nativ Masiv Facial | Față | 1 mm/1 mm | Bone |  | Oase faciale și sinusuri paranazale |
    | Coronal | CT Nativ Masiv Facial | Față | 1 mm/1 mm | Bone |  | Plan coronal pentru orbite și schelet facial |
