---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: neuro
clinical_indications:
- Traumatism cranio-cerebral acut (TCC)
- Suspiciune de accident vascular cerebral acut hemoragic sau ischemic
- Cefalee acută intensă ('cea mai puternică durere din viață' — suspiciune HSA)
- Alterarea stării de conștiență, comă, sincope neelucidate
- Convulsii la debut, deficit neurologic focal acut
contrast:
  agent: FĂRĂ
  duration: 0s
  flow_rate: 0 mL/s
  roi: N/A
  timing: N/A
  trigger: N/A
  volume: 0 mL
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții fine 1.0 mm osoase în caz de suspiciune de fractură
    a stâncii temporale.
  nursing: Imobilizare atentă a capului la pacienți agitați sau confuzi.
  rad: Calcul scor ASPECTS în AVC ischemic acut în teritoriul ACM; căutați semnul
    arterei cerebrale medii hiperdense, edem cerebral precoce, hematoame extra-axiale.
  tech: 'Angulare gantry paralelă cu linia orbitomeatală pentru a exclude orbitele
    din fasciculul primar dacă este posibil. La Toshiba: achiziție de volum dacă apar
    artefacte de mișcare.'
  tips: La copii se aplică protocoalele specifice pediatrice OHSU cu reducerea corespunzătoare
    a kV și mAs.
npo: N/A — protocol nativ de urgență
position: Decubit dorsal, cap centrat pe linia mediană, bărbia ușor flectată
premedication: Fără contrast i.v. sau oral
protocol_type: non-contrast
recons:
- acquisition: CT Craniu Nativ
  fov: Cap
  ir_strength: Standard
  kernel: Creier (H31s / J30s)
  notes: Serii standard de creier (fereastră W80 / L35)
  plane: Axial, Coronal & Sagital (Adult)
  thickness_increment: 5.0 mm / 5.0 mm
- acquisition: CT Craniu Nativ
  fov: Cap
  ir_strength: Standard
  kernel: Creier Pediatric (H31s)
  notes: Grosime redusă de secțiune pentru rezoluție optimă la copil
  plane: Axial, Coronal & Sagital (Pediatric)
  thickness_increment: 3.0 mm / 3.0 mm
- acquisition: CT Craniu Nativ
  fov: Cap
  ir_strength: Standard
  kernel: Osos (H60s / J70s)
  notes: Fereastră osoasă pentru decelarea fracturilor calvariei și bazei craniului
  plane: Axial
  thickness_increment: 2.0 mm / 2.0 mm
safety:
  allergy: N/A — fără contrast
  renal: N/A — fără contrast
series:
- delay: 0 sec
  end: Deasupra vertexului
  name: CT Craniu Nativ
  notes: Scanare angulată pentru a proteja cristalinul; DFOV 220 mm
  start: Sub baza craniului (gaura occipitală)
  thickness: 0.625 mm
tech_params:
  collimation: 64 × 0.625 mm / 128 × 0.6 mm
  kv: 120 kV (Adult) / 100-120 kV (Pediatric)
  mas: CAREDose4D / SureExposure3D
  pitch: 0.8 - 1.0
  rotation_time: 0.5 - 1.0 s
  scan_mode: Secvențial sau Elicoidal angulat pentru a evita orbitele
  slice_thickness: 0.625 mm
title: CT Craniu Nativ Adult & Pediatric (Protocol OHSU)
---

# CT Craniu Nativ Adult & Pediatric (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Craniu Nativ | 0 sec | Sub baza craniului (gaura occipitală) → Deasupra vertexului |

    === "Indicații Clinice"

        - Traumatism cranio-cerebral acut (TCC)
        - Suspiciune de accident vascular cerebral acut hemoragic sau ischemic
        - Cefalee acută intensă ('cea mai puternică durere din viață' — suspiciune HSA)
        - Alterarea stării de conștiență, comă, sincope neelucidate
        - Convulsii la debut, deficit neurologic focal acut

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Cap, Gât & Coloană vertebrală*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal, cap centrat pe linia mediană, bărbia ușor flectată
    - **Repaus Alimentar (NPO):** N/A — protocol nativ de urgență
    - **Premedicație / Pregătire:**
        - Fără contrast i.v. sau oral

-   __3. Contrast IV & Injectare__

    ---
    !!! info "Fără Contrast Intravenos"
    Acest protocol nu necesită administrare de contrast intravenos.

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | 120 kV (Adult) / 100-120 kV (Pediatric) kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare angulară adaptivă / Curent fix fosa posterioară) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm / 128 × 0.6 mm |
    | **Timp de Rotație** | 0.5 - 1.0 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.0 |
    | **Mod Scanare** | Secvențial sau Elicoidal angulat pentru a evita orbitele |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Angulare gantry paralelă cu linia orbitomeatală pentru a exclude orbitele din fasciculul primar dacă este posibil. La Toshiba: achiziție de volum dacă apar artefacte de mișcare.

    === "Note Asistent"

        - Imobilizare atentă a capului la pacienți agitați sau confuzi.

        !!! warning "Siguranță"
            - **Funcție Renală:** N/A — fără contrast
            - **Alergii:** N/A — fără contrast

    === "Note Radiolog"

        - Calcul scor ASPECTS în AVC ischemic acut în teritoriul ACM; căutați semnul arterei cerebrale medii hiperdense, edem cerebral precoce, hematoame extra-axiale.

    === "Sfaturi & Recomandări"

        - La copii se aplică protocoalele specifice pediatrice OHSU cu reducerea corespunzătoare a kV și mAs.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Craniu Nativ | Sub baza craniului (gaura occipitală) | Deasupra vertexului | 0 sec | 0.625 mm | Scanare angulată pentru a proteja cristalinul; DFOV 220 mm |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial, Coronal & Sagital (Adult) | CT Craniu Nativ | Cap | 5.0 mm / 5.0 mm | Creier (H31s / J30s) | Standard | Serii standard de creier (fereastră W80 / L35) |
    | Axial, Coronal & Sagital (Pediatric) | CT Craniu Nativ | Cap | 3.0 mm / 3.0 mm | Creier Pediatric (H31s) | Standard | Grosime redusă de secțiune pentru rezoluție optimă la copil |
    | Axial | CT Craniu Nativ | Cap | 2.0 mm / 2.0 mm | Osos (H60s / J70s) | Standard | Fereastră osoasă pentru decelarea fracturilor calvariei și bazei craniului |
