---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen
clinical_indications:
- Traumatism pelvin cu fracturi de bazin și suspiciune de ruptură vezicală (intraperitoneală
  vs extraperitoneală)
- Hematurie macroscopică post-traumatică sau post-operatorie urologică/ginecologică
- Suspiciune de fistulă vezico-vaginală, vezico-uterină sau vezico-enterică
- Evaluarea integrității anastomozei vezicale post-cistectomie parțială sau reconstrucție
contrast:
  agent: Contrast iodat hidrosolubil diluat (Omnipaque 300 / Cysto-Conray) diluat
    1:10 cu ser fiziologic
  duration: Până la oprirea curgerii sau senzație de plenitudine vezicală
  flow_rate: Instilare gravitațională pasivă (sac suspendat la 1 metru deasupra pacientului)
  roi: N/A
  timing: Scanare imediat după umplerea vezicii urinare + serie post-evacuare
  trigger: N/A
  volume: 300 - 400 mL contrast diluat instilat gravitațional prin sonda Foley
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții 3D pentru traiectul fistulelor.
  nursing: Conectarea sistemului gravitațional și monitorizarea volumului instilat.
  rad: 'Diferențiere crucială: 1) Ruptură intraperitoneală (contrast între ansele
    intestinale și spațiile paracolice — necesită laparotomie de urgență); 2) Ruptură
    extraperitoneală (contrast limitat în spațiul Retzius și țesuturile moi pelvine
    — tratament conservator prin drenaj).'
  tech: NU injectați contrast i.v. pentru această fază (se instilează exclusiv retrograd
    prin cateterul Foley). Distensia adecvată (minim 300-350 mL) este obligatorie;
    o vezică subdistinsă generează rezultate fals-negative.
  tips: Dacă este asociat un CT Pan-Scan de traumă cu contrast i.v., CT cistografia
    se efectuează la sfârșit prin instilare retrogradă.
npo: N/A în urgență traumatică
position: Decubit dorsal
premedication: Cateterizare urinară vezicală Foley obligatorie
protocol_type: specialized
recons:
- acquisition: CT Cistografie
  fov: Bazin / Pelvis
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard (I30f) + Osos (I70f)
  notes: Fereastră de țesut moale și osoasă pentru fracturile de ramuri pubiene
  plane: Axial, Coronal & Sagital
  thickness_increment: 2.0 mm / 2.0 mm
safety:
  allergy: Absorbția sistemică este minimă la nivelul mucoasei vezicale intacte, dar
    se recomandă precauție în rupturi mari.
  renal: N/A — nu implică excreție renală a contrastului
series:
- delay: 0 sec post-umplere
  end: Sub simfiza pubiană și perineu
  name: CT Pelvis Plin (Distensie Vezicală Retrogradă)
  notes: Vezică destinsă complet cu 350-400 mL; pensarea sondei pe durata scanării
  start: Creste iliace (L4)
  thickness: 0.625 mm
- delay: Imediat după drenaj
  end: Simfiză pubiană
  name: CT Pelvis Post-Evacuare
  notes: Drenaj complet al vezicii prin deschiderea sondei; evidențiază mici scurgeri
    extraperitoneale mascate inițial de contrastul intravezical dens
  start: Creste iliace
  thickness: 1.0 mm
tech_params:
  collimation: 64 × 0.625 mm / 128 × 0.6 mm
  kv: 120 kV
  mas: CAREDose4D / SureExposure3D
  pitch: 0.9 - 1.1
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Cistografie Pelvină / Ruptură Vezicală (Protocol OHSU)
---

# CT Cistografie Pelvină / Ruptură Vezicală (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | CT Pelvis Plin (Distensie Vezicală Retrogradă) | 0 sec post-umplere | Creste iliace (L4) → Sub simfiza pubiană și perineu |
        | CT Pelvis Post-Evacuare | Imediat după drenaj | Creste iliace → Simfiză pubiană |

    === "Indicații Clinice"

        - Traumatism pelvin cu fracturi de bazin și suspiciune de ruptură vezicală (intraperitoneală vs extraperitoneală)
        - Hematurie macroscopică post-traumatică sau post-operatorie urologică/ginecologică
        - Suspiciune de fistulă vezico-vaginală, vezico-uterină sau vezico-enterică
        - Evaluarea integrității anastomozei vezicale post-cistectomie parțială sau reconstrucție

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal
    - **Repaus Alimentar (NPO):** N/A în urgență traumatică
    - **Premedicație / Pregătire:**
        - Cateterizare urinară vezicală Foley obligatorie

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Contrast iodat hidrosolubil diluat (Omnipaque 300 / Cysto-Conray) diluat 1:10 cu ser fiziologic |
        | Volum | 300 - 400 mL contrast diluat instilat gravitațional prin sonda Foley |
        | Rată de Flux | Instilare gravitațională pasivă (sac suspendat la 1 metru deasupra pacientului) |
        | Durată | Până la oprirea curgerii sau senzație de plenitudine vezicală |
        | Metodă Temporizare | Scanare imediat după umplerea vezicii urinare + serie post-evacuare |
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
    | **Tensiune Tub (kV)** | 120 kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 64 × 0.625 mm / 128 × 0.6 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.9 - 1.1 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - NU injectați contrast i.v. pentru această fază (se instilează exclusiv retrograd prin cateterul Foley). Distensia adecvată (minim 300-350 mL) este obligatorie; o vezică subdistinsă generează rezultate fals-negative.

    === "Note Asistent"

        - Conectarea sistemului gravitațional și monitorizarea volumului instilat.

        !!! warning "Siguranță"
            - **Funcție Renală:** N/A — nu implică excreție renală a contrastului
            - **Alergii:** Absorbția sistemică este minimă la nivelul mucoasei vezicale intacte, dar se recomandă precauție în rupturi mari.

    === "Note Radiolog"

        - Diferențiere crucială: 1) Ruptură intraperitoneală (contrast între ansele intestinale și spațiile paracolice — necesită laparotomie de urgență); 2) Ruptură extraperitoneală (contrast limitat în spațiul Retzius și țesuturile moi pelvine — tratament conservator prin drenaj).

    === "Sfaturi & Recomandări"

        - Dacă este asociat un CT Pan-Scan de traumă cu contrast i.v., CT cistografia se efectuează la sfârșit prin instilare retrogradă.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | CT Pelvis Plin (Distensie Vezicală Retrogradă) | Creste iliace (L4) | Sub simfiza pubiană și perineu | 0 sec post-umplere | 0.625 mm | Vezică destinsă complet cu 350-400 mL; pensarea sondei pe durata scanării |
    | CT Pelvis Post-Evacuare | Creste iliace | Simfiză pubiană | Imediat după drenaj | 1.0 mm | Drenaj complet al vezicii prin deschiderea sondei; evidențiază mici scurgeri extraperitoneale mascate inițial de contrastul intravezical dens |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial, Coronal & Sagital | CT Cistografie | Bazin / Pelvis | 2.0 mm / 2.0 mm | Standard (I30f) + Osos (I70f) | Admire 3 / AIDR 3D | Fereastră de țesut moale și osoasă pentru fracturile de ramuri pubiene |
