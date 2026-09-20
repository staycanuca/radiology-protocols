---
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: abdomen
clinical_indications:
- Caracterizare noduli și leziuni hepatice la pacienți cirotici (evaluare LI-RADS
  / suspiciune HCC)
- Evaluare leziuni hepatice hipervasculare (hiperplazie nodulară focală FNH, adenom
  hepatic, hemangiom atipic)
- Stadializare pre-transplant hepatic, rezecție chirurgicală sau ablație tumorală
  (RFA/MWA/TACE)
- Metastaze hepatice hipervasculare (tumori neuroendocrine, melanom, carcinom renal,
  carcinom tiroidian)
contrast:
  agent: Isovue 370 / Omnipaque 350
  duration: 25-30s
  flow_rate: 4.0 - 5.0 mL/s
  roi: Aorta abdominală la originea trunchiului celiac
  timing: Bolus tracking în aorta abdominală (trigger 150 HU la nivelul trunchiului
    celiac)
  trigger: 150 HU (+15-18 sec delay pentru faza arterială tardivă)
  volume: 125-150 mL (2 mL/kg)
last_updated: '2026-09-20'
notes:
  additional_recons: Reconstrucții MIP și VR 3D pentru anatomia trunchiului celiac
    și arterei hepatice (pre-operator).
  nursing: Monitorizare debit injectare. La viteze de 4-5 mL/s se va folosi exclusiv
    canulă certificată high-pressure.
  rad: Aplicați criteriile LI-RADS v2018 pentru fiecare leziune focală observată.
    Evaluați permeabilitatea trunchiului portal, ramurilor portale și venelor hepatice.
  tech: Injectare rapidă cu injector automat bifașic (contrast + flush salin 40 mL).
    Canulă 18-20G în plica cotului. Respectați strict temporizarea bolus tracking.
  tips: Apă orală administrată chiar înainte de examinare asigură o distensie gastrică
    excelentă fără a masca încărcarea arterială a lobului stâng.
npo: Repaus alimentar 4 ore înainte de scanare; hidratare permisă
position: Decubit dorsal cu brațele ridicate deasupra capului
premedication: Contrast oral exclusiv apă (contrast neutru) 500 mL cu 15-20 min înainte
  de scanare (nu se utilizează bariu sau contrast iodat oral)
protocol_type: multiphase
recons:
- acquisition: Toate fazele (Nativ, Arterial, Portal, Tardiv)
  fov: Ficat / Abdomen
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard / I30f
  notes: Serii diagnostice de bază
  plane: Axial
  thickness_increment: 2.5 mm / 2.5 mm
- acquisition: Fază Venoasă Portală & Arterială
  fov: Abdomen
  ir_strength: Admire 3 / AIDR 3D
  kernel: Standard / I30f
  notes: Raport lezional cu venele suprahepatice și vena portă
  plane: Coronal
  thickness_increment: 2.0 mm / 2.0 mm
safety:
  allergy: Screening conform politicii OHSU. Premedicație standard dacă există istoric
    de reacții alergice la substanțe iodate.
  renal: eGFR > 30 mL/min obligatoriu. Hidratare i.v. recomandată pentru valori limitrofe
    (30-44 mL/min).
series:
- delay: 0 sec
  end: Pol inferior hepatic
  name: Fază Nativă (Ficat)
  notes: Detectare hemoragii intratumorale, calcificări, depuneri de grăsime sau fier
    (hemocromatoză)
  start: Cupolă diafragmatică dreaptă
  thickness: 1.0 mm
- delay: Trigger + 15-18 sec
  end: Creste iliace
  name: Fază Arterială Tardivă
  notes: Spălare arterială (wash-in) a leziunilor hipervasculare (HCC, FNH, TNE)
  start: Diafragm
  thickness: 0.625 mm
- delay: 65-70 sec
  end: Simfiză pubiană
  name: Fază Venoasă Portală
  notes: Contrastare maximă parenchim hepatic normal; detectare metastaze hipovasculare
    și tromboză portală
  start: Diafragm
  thickness: 0.625 mm
- delay: 180 sec (3 min)
  end: Pol inferior hepatic
  name: Fază Tardivă / Echilibru
  notes: Spălare capsulară (wash-out) specifică HCC; persistență contrast în hemangioame
    și colangiocarcinom
  start: Cupolă diafragmatică
  thickness: 1.0 mm
tech_params:
  collimation: 128 × 0.6 mm / 64 × 0.625 mm
  kv: CAREkV (Ref 120 kV)
  mas: CAREDose4D / SureExposure3D (Ref 200-240 mAs)
  pitch: 0.8 - 1.0
  rotation_time: 0.5 s
  scan_mode: Elicoidal (Helical)
  slice_thickness: 0.625 mm
title: CT Ficat Multifazic Triphasic (Protocol OHSU)
---

# CT Ficat Multifazic Triphasic (Protocol OHSU)

**Ultima actualizare:** 2026-09-20
**Autor:** OHSU Diagnostic Radiology / Departamentul de Radiologie

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic__

    ---

    === "Rezumat Achiziție"

        | Serie | Fază | Acoperire |
        |:-------|:------|:---------|
        | Fază Nativă (Ficat) | 0 sec | Cupolă diafragmatică dreaptă → Pol inferior hepatic |
        | Fază Arterială Tardivă | Trigger + 15-18 sec | Diafragm → Creste iliace |
        | Fază Venoasă Portală | 65-70 sec | Diafragm → Simfiză pubiană |
        | Fază Tardivă / Echilibru | 180 sec (3 min) | Cupolă diafragmatică → Pol inferior hepatic |

    === "Indicații Clinice"

        - Caracterizare noduli și leziuni hepatice la pacienți cirotici (evaluare LI-RADS / suspiciune HCC)
        - Evaluare leziuni hepatice hipervasculare (hiperplazie nodulară focală FNH, adenom hepatic, hemangiom atipic)
        - Stadializare pre-transplant hepatic, rezecție chirurgicală sau ablație tumorală (RFA/MWA/TACE)
        - Metastaze hepatice hipervasculare (tumori neuroendocrine, melanom, carcinom renal, carcinom tiroidian)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            Pentru evaluarea oportunității clinice, gradul de recomandare (A/B/C) și nivelul de iradiere (comparativ cu Ecografia, RMN sau Radiografia), consultați **[Ghidul Național IRIS](../../iris.md)** (Capitolul: *Aparat digestiv & Abdomen*).

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Web PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient__

    ---

    - **Poziție:** Decubit dorsal cu brațele ridicate deasupra capului
    - **Repaus Alimentar (NPO):** Repaus alimentar 4 ore înainte de scanare; hidratare permisă
    - **Premedicație / Pregătire:**
        - Contrast oral exclusiv apă (contrast neutru) 500 mL cu 15-20 min înainte de scanare (nu se utilizează bariu sau contrast iodat oral)

-   __3. Contrast IV & Injectare__

    ---
    === "Parametri de Injectare"

        | Parametru | Valoare |
        |-----------|-------|
        | Agent | Isovue 370 / Omnipaque 350 |
        | Volum | 125-150 mL (2 mL/kg) |
        | Rată de Flux | 4.0 - 5.0 mL/s |
        | Durată | 25-30s |
        | Metodă Temporizare | Bolus tracking în aorta abdominală (trigger 150 HU la nivelul trunchiului celiac) |
        | Poziționare ROI | Aorta abdominală la originea trunchiului celiac |
        | Declanșator (HU) | 150 HU (+15-18 sec delay pentru faza arterială tardivă) |

    === "Cerințe de Laborator"
        Doză completă dacă eGFR > 30 mL/min
        !!! warning "Dacă eGFR < 30 mL/min"
            **Contrast Maxim** = \(2*\left[\frac{\text{Greutate Pacient}}{75 \text{ kg}} * \text{eGFR}\right]\)

-   __4. Parametri Tehnici Achiziție__

    ---
    | Parametru Tehnic | Valoare Configurare |
    |:-----------------|:---------------------|
    | **Tensiune Tub (kV)** | CAREkV (Ref 120 kV) kV |
    | **Curent Tub (mAs)** | CAREDose4D / SureExposure3D (Ref 200-240 mAs) |
    | **Control Automat al Expunerii (AEC)** | Activat (Modulare automată 3D conform topogramei / scout) |
    | **Grosime Secțiune Achiziție (Slice)** | 0.625 mm |
    | **Colimare Detector** | 128 × 0.6 mm / 64 × 0.625 mm |
    | **Timp de Rotație** | 0.5 s |
    | **Pitch (Factor Pas)** | 0.8 - 1.0 |
    | **Mod Scanare** | Elicoidal (Helical) |

-   __5. Note Speciale__

    ---

    === "Note Tehnician"

        - Injectare rapidă cu injector automat bifașic (contrast + flush salin 40 mL). Canulă 18-20G în plica cotului. Respectați strict temporizarea bolus tracking.

    === "Note Asistent"

        - Monitorizare debit injectare. La viteze de 4-5 mL/s se va folosi exclusiv canulă certificată high-pressure.

        !!! warning "Siguranță"
            - **Funcție Renală:** eGFR > 30 mL/min obligatoriu. Hidratare i.v. recomandată pentru valori limitrofe (30-44 mL/min).
            - **Alergii:** Screening conform politicii OHSU. Premedicație standard dacă există istoric de reacții alergice la substanțe iodate.

    === "Note Radiolog"

        - Aplicați criteriile LI-RADS v2018 pentru fiecare leziune focală observată. Evaluați permeabilitatea trunchiului portal, ramurilor portale și venelor hepatice.

    === "Sfaturi & Recomandări"

        - Apă orală administrată chiar înainte de examinare asigură o distensie gastrică excelentă fără a masca încărcarea arterială a lobului stâng.

</div>

<div class="acquisition-diagram"></div>

=== "Achiziție Serii"

    | Nume Serie | Limită Superioară | Limită Inferioară | Întârziere | Grosime Strat | Note |
    |:------------|:---------------|:-------------|:------|:----------------|:------|
    | Fază Nativă (Ficat) | Cupolă diafragmatică dreaptă | Pol inferior hepatic | 0 sec | 1.0 mm | Detectare hemoragii intratumorale, calcificări, depuneri de grăsime sau fier (hemocromatoză) |
    | Fază Arterială Tardivă | Diafragm | Creste iliace | Trigger + 15-18 sec | 0.625 mm | Spălare arterială (wash-in) a leziunilor hipervasculare (HCC, FNH, TNE) |
    | Fază Venoasă Portală | Diafragm | Simfiză pubiană | 65-70 sec | 0.625 mm | Contrastare maximă parenchim hepatic normal; detectare metastaze hipovasculare și tromboză portală |
    | Fază Tardivă / Echilibru | Cupolă diafragmatică | Pol inferior hepatic | 180 sec (3 min) | 1.0 mm | Spălare capsulară (wash-out) specifică HCC; persistență contrast în hemangioame și colangiocarcinom |

=== "Post-procesare & Reconstrucții"

    | Plan | Achiziție | FOV | Grosime/Increment | Filtru (Kernel) | Putere IR | Note |
    |:------|:------------|:----|:--------------------|:-------|:------------|:------|
    | Axial | Toate fazele (Nativ, Arterial, Portal, Tardiv) | Ficat / Abdomen | 2.5 mm / 2.5 mm | Standard / I30f | Admire 3 / AIDR 3D | Serii diagnostice de bază |
    | Coronal | Fază Venoasă Portală & Arterială | Abdomen | 2.0 mm / 2.0 mm | Standard / I30f | Admire 3 / AIDR 3D | Raport lezional cu venele suprahepatice și vena portă |
