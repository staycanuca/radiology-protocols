---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen
clinical_indications:
- Boală Crohn suspectată sau cunoscută (evaluare activitate inflamatorie parietală,
  stenoze, fistule, abcese)
- Hemoragie digestivă obscură fără cauză identificată prin endoscopie și colonoscopie
- Suspiciune de tumori de intestin subțire (tumori carcinoide/TNE, polipi, limfom,
  adenocarcinom)
- Boală celiacă refractară, sindrom de malabsorbție neexplicat
contrast:
  agent: Omnipaque 350 / Isovue 370
  duration: 30-35s
  flow_rate: 3.5 - 4.0 mL/s
  roi: N/A
  timing: Fază enterică (45-50 secunde delay de la debutul injectării contrastului
    i.v.)
  trigger: N/A
  volume: 100-125 mL
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții 3D MIP coronale pentru vizualizarea vascularizației
    mezenterice (vase drepte dilatate).
  nursing: Monitorizați toleranța pacientului la ingestia orală; în caz de greață,
    se poate administra un antiemetic ușor cu acordul medicului.
  rad: Evaluați îngroșarea parietală (> 3 mm la anse destinse), hiperemia mucoasă,
    edemul subseros, hipertrofia grăsimii fibrogrăsoase (creeping fat) și adenopatiile
    mezenterice.
  tech: Pacientul trebuie să bea întregul volum de contrast neutru (VoLumen 1350 mL)
    conform orarului. Injectare i.v. rapidă cu flush salin 40 mL.
  tips: 'Distensia adecvată a anselor este cheia diagnostică: fără contrast neutru
    suficient, ansele colabate pot mima patologie inflamatorie fals-pozitivă.'
npo: Repaus alimentar strict 6 ore înainte de scanare; lichide clare permise până
  la sosirea în departament
position: Decubit dorsal cu brațele ridicate
premedication: 'Protocol Contrast Oral Neutru VoLumen (1350 mL / 3 sticle a 450 mL):
  Sticla 1 cu 60 min înainte, Sticla 2 cu 40 min înainte, Sticla 3 cu 20 min înainte
  de scanare.'
protocol_type: contrast-enhanced
recons:
- acquisition: Fază Enterică
  fov: Abdomen
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard / I30f
  notes: Măsurare grosime parietală, edem submucos, stratificare parietală
  plane: Axial
  thickness_increment: 2.0 mm / 2.0 mm
- acquisition: Fază Enterică
  fov: Abdomen
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard / I30f
  notes: Plan de elecție pentru urmărirea traiectului anselor ileale și jejunale și
    semnul pieptenului (comb sign)
  plane: Coronal
  thickness_increment: 1.5 mm / 1.5 mm
safety:
  allergy: Conform politicii OHSU. Premedicație dacă există reacții alergice anterioare.
  renal: eGFR > 30 mL/min/1.73m².
series:
- delay: 45-50 sec
  end: Simfiză pubiană
  name: Fază Enterică
  notes: Opacifiere maximă a peretelui anselor intestinale pe fondul lumenului destins
    hipodens (VoLumen)
  start: Cupole diafragmatice
  thickness: 0.625 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: CAREkV (Ref 100-120 kV)
  mas: CAREDose4D / SureExposure3D (Ref 180 mAs)
  pitch: 0.9 - 1.1
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Enterografie (Protocol OHSU)
---

# CT Enterografie (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Enterică | 45-50 sec | Cupole diafragmatice → Simfiză pubiană |

    === "Indicații Clinice"

        - Boală Crohn suspectată sau cunoscută (evaluare activitate inflamatorie parietală, stenoze, fistule, abcese)
        - Hemoragie digestivă obscură fără cauză identificată prin endoscopie și colonoscopie
        - Suspiciune de tumori de intestin subțire (tumori carcinoide/TNE, polipi, limfom, adenocarcinom)
        - Boală celiacă refractară, sindrom de malabsorbție neexplicat

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate
    - **Repaus Alimentar (NPO):** Repaus alimentar strict 6 ore înainte de scanare; lichide clare permise până la sosirea în departament
    - **Premedicație / Pregătire:**
        - Protocol Contrast Oral Neutru VoLumen (1350 mL / 3 sticle a 450 mL): Sticla 1 cu 60 min înainte, Sticla 2 cu 40 min înainte, Sticla 3 cu 20 min înainte de scanare.

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Omnipaque 350 / Isovue 370 |
        | Volum | 100-125 mL |
        | Rată de Flux | 3.5 - 4.0 mL/s |
        | Durată | 30-35s |
        | Metodă Temporizare | Fază enterică (45-50 secunde delay de la debutul injectării contrastului i.v.) |
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
    | **Tensiune Tub (kV)** | CAREkV (Ref 100-120 kV) kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D (Ref 180 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9 - 1.1 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Pacientul trebuie să bea întregul volum de contrast neutru (VoLumen 1350 mL) conform orarului. Injectare i.v. rapidă cu flush salin 40 mL.

    === "Note Asistent"

        - Monitorizați toleranța pacientului la ingestia orală; în caz de greață, se poate administra un antiemetic ușor cu acordul medicului.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR > 30 mL/min/1.73m².
            - **Alergii:** Conform politicii OHSU. Premedicație dacă există reacții alergice anterioare.

    === "Note Radiolog"

        - Evaluați îngroșarea parietală (> 3 mm la anse destinse), hiperemia mucoasă, edemul subseros, hipertrofia grăsimii fibrogrăsoase (creeping fat) și adenopatiile mezenterice.

    === "Sfaturi & Recomandări"

        - Distensia adecvată a anselor este cheia diagnostică: fără contrast neutru suficient, ansele colabate pot mima patologie inflamatorie fals-pozitivă.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Enterică | Cupole diafragmatice | Simfiză pubiană | 45-50 sec | 0.625 mm | Opacifiere maximă a peretelui anselor intestinale pe fondul lumenului destins hipodens (VoLumen) |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Fază Enterică | Abdomen | 2.0 mm / 2.0 mm | Standard / I30f | Admire 3 / AIDR 3D | Măsurare grosime parietală, edem submucos, stratificare parietală |
    | Coronal | Fază Enterică | Abdomen | 1.5 mm / 1.5 mm | Standard / I30f | Admire 3 / AIDR 3D | Plan de elecție pentru urmărirea traiectului anselor ileale și jejunale și semnul pieptenului (comb sign) |
