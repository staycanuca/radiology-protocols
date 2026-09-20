---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: trauma
clinical_indications:
- Politraumă majoră cu mecanism de înaltă energie cinetică (accidente rutiere de mare
  viteză, cădere > 3 metri)
- Pacient politraumatizat cu instabilitate hemodinamică sau alterare a conștienței
  (GCS < 13)
- Suspiciune de leziuni traumatice multisistemice (craniu, coloană cervicală, torace,
  abdomen, pelvis)
- Traumatism toraco-abdominal sever cu suspiciune de sângerare activă sau ruptură
  viscerală
contrast:
  agent: Isovue 370 / Omnipaque 350
  duration: 35-40s
  flow_rate: 3.5 - 4.0 mL/s
  roi: N/A
  timing: 65-70 secunde de la debutul injectării (fază venoasă portală/parenchimatoasă)
  trigger: N/A
  volume: 130-150 mL
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții 3D VR pentru bazin și cutie toracică (fracturi
    costale multiple, volet costal).
  nursing: Canulă de calibru mare (18G). Pregătire echipament de resuscitare și hemostatice.
  rad: 'Verificare prioritară: 1) Leziuni intracraniene cu efect de masă; 2) Fracturi
    cervicale instabile; 3) Leziuni de aortă toracică; 4) Extravazare activă de contrast
    intraabdominală; 5) Fracturi de bazin instabile.'
  tech: Scanare rapidă fără întârziere. Monitorizare semne vitale în sala de scanare.
    Brațele ridicate pentru achiziția toraco-abdominală dacă nu sunt contraindicații
    ortopedice.
  tips: În caz de blush vascular activ, se realizează o achiziție tardivă țintită
    la 3-5 minute pentru a diferenția pseudoanevrismul de sângerarea activă liberă.
npo: Urgență majoră — N/A
position: Decubit dorsal, cap centrat în izocentru, brațele imobilizate inițial pe
  lângă corp pentru craniu/coloană, apoi ridicate dacă starea permite
premedication: Fără premedicație orală — urgență de cod roșu/galben
protocol_type: trauma
recons:
- acquisition: Craniu Nativ
  fov: Cap
  ir_strength: Standard
  kernel: Creier (H31s) + Osos (H60s)
  notes: Fereastră de creier și fereastră osoasă
  plane: Axial
  thickness_increment: 3.0 mm / 3.0 mm
- acquisition: Coloană Cervicală
  fov: C-Spine
  ir_strength: Standard
  kernel: Osos (B60s)
  notes: Aliniament coloană și stabilitate ligamentară
  plane: Sagital & Coronal
  thickness_increment: 1.5 mm / 1.5 mm
- acquisition: Torace, Abdomen & Pelvis
  fov: Torace / Abdomen
  ir_strength: Admire 3 / AIDR 3D
  kernel: Parenchim (I30f) + Osos (I70f) + Pulmonar (I50f)
  notes: Fereastră mediastinală, pulmonară, parenchim abdominal și fereastră de os
    pentru bazin/coloană
  plane: Axial, Coronal & Sagital
  thickness_increment: 2.0 mm / 2.0 mm
safety:
  allergy: În urgență vitală imediată, contrastul se administrează cu monitorizare
    atentă chiar dacă există istoric alergic, asigurând acces imediat la tratament
    de resuscitare.
  renal: În traumă acută severă, beneficiul diagnosticului vital depășește riscul
    de nefrotoxicitate indusă de contrast.
series:
- delay: 0 sec
  end: Vertex
  name: CT Craniu Nativ
  notes: Detectare hematoame epidurale/subdurale, hemoragie subarahnoidiană, fracturi
    craniene
  start: Baza craniului / gaura occipitală
  thickness: 1.0 mm
- delay: 0 sec
  end: T1-T2
  name: CT Coloană Cervicală Nativ
  notes: Evaluare leziuni osteo-articulare, luxații, fracturi de corp vertebral sau
    arcuri posterioare
  start: Baza craniului
  thickness: 0.625 mm
- delay: 65-70 sec
  end: Mici trohantere
  name: CT Torace, Abdomen & Pelvis cu Contrast
  notes: Detectare lacerații hepatice/splenice/renale, pneumotorax, hemotorax, extravazare
    activă de contrast (blush vascular)
  start: Vârfuri pulmonare
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: 120 kV (sau CAREkV)
  mas: CAREDose4D / SureExposure3D mod trauma
  pitch: 0.9 - 1.2
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Politraumă Pan-Scan Whole Body (Protocol OHSU)
---

# CT Politraumă Pan-Scan Whole Body (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Craniu Nativ | 0 sec | Baza craniului / gaura occipitală → Vertex |
        | CT Coloană Cervicală Nativ | 0 sec | Baza craniului → T1-T2 |
        | CT Torace, Abdomen & Pelvis cu Contrast | 65-70 sec | Vârfuri pulmonare → Mici trohantere |

    === "Indicații Clinice"

        - Politraumă majoră cu mecanism de înaltă energie cinetică (accidente rutiere de mare viteză, cădere > 3 metri)
        - Pacient politraumatizat cu instabilitate hemodinamică sau alterare a conștienței (GCS < 13)
        - Suspiciune de leziuni traumatice multisistemice (craniu, coloană cervicală, torace, abdomen, pelvis)
        - Traumatism toraco-abdominal sever cu suspiciune de sângerare activă sau ruptură viscerală

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Traumatisme & Politraumă*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal, cap centrat în izocentru, brațele imobilizate inițial pe lângă corp pentru craniu/coloană, apoi ridicate dacă starea permite
    - **Repaus Alimentar (NPO):** Urgență majoră — N/A
    - **Premedicație / Pregătire:**
        - Fără premedicație orală — urgență de cod roșu/galben

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 / Omnipaque 350 |
        | Volum | 130-150 mL |
        | Rată de Flux | 3.5 - 4.0 mL/s |
        | Durată | 35-40s |
        | Metodă Temporizare | 65-70 secunde de la debutul injectării (fază venoasă portală/parenchimatoasă) |
        | Poziționare ROI | N/A |
        | Declanșator (HU) | N/A |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 120 kV (sau CAREkV) kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D mod trauma |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D pentru politraumă) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9 - 1.2 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Scanare rapidă fără întârziere. Monitorizare semne vitale în sala de scanare. Brațele ridicate pentru achiziția toraco-abdominală dacă nu sunt contraindicații ortopedice.

    === "Note Asistent"

        - Canulă de calibru mare (18G). Pregătire echipament de resuscitare și hemostatice.

        !!! warning "Siguranță"
            - **Funcție Renală:** În traumă acută severă, beneficiul diagnosticului vital depășește riscul de nefrotoxicitate indusă de contrast.
            - **Alergii:** În urgență vitală imediată, contrastul se administrează cu monitorizare atentă chiar dacă există istoric alergic, asigurând acces imediat la tratament de resuscitare.

    === "Note Radiolog"

        - Verificare prioritară: 1) Leziuni intracraniene cu efect de masă; 2) Fracturi cervicale instabile; 3) Leziuni de aortă toracică; 4) Extravazare activă de contrast intraabdominală; 5) Fracturi de bazin instabile.

    === "Sfaturi & Recomandări"

        - În caz de blush vascular activ, se realizează o achiziție tardivă țintită la 3-5 minute pentru a diferenția pseudoanevrismul de sângerarea activă liberă.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Craniu Nativ | Baza craniului / gaura occipitală | Vertex | 0 sec | 1.0 mm | Detectare hematoame epidurale/subdurale, hemoragie subarahnoidiană, fracturi craniene |
    | CT Coloană Cervicală Nativ | Baza craniului | T1-T2 | 0 sec | 0.625 mm | Evaluare leziuni osteo-articulare, luxații, fracturi de corp vertebral sau arcuri posterioare |
    | CT Torace, Abdomen & Pelvis cu Contrast | Vârfuri pulmonare | Mici trohantere | 65-70 sec | 0.625 mm | Detectare lacerații hepatice/splenice/renale, pneumotorax, hemotorax, extravazare activă de contrast (blush vascular) |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Craniu Nativ | Cap | 3.0 mm / 3.0 mm | Creier (H31s) + Osos (H60s) | Standard | Fereastră de creier și fereastră osoasă |
    | Sagital & Coronal | Coloană Cervicală | C-Spine | 1.5 mm / 1.5 mm | Osos (B60s) | Standard | Aliniament coloană și stabilitate ligamentară |
    | Axial, Coronal & Sagital | Torace, Abdomen & Pelvis | Torace / Abdomen | 2.0 mm / 2.0 mm | Parenchim (I30f) + Osos (I70f) + Pulmonar (I50f) | Admire 3 / AIDR 3D | Fereastră mediastinală, pulmonară, parenchim abdominal și fereastră de os pentru bazin/coloană |
