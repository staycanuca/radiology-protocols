---
acquisition_steps:
- description: 'Înainte de incizia chirurgicală: arcul C este poziționat și se verifică
    obținerea facilă atât a incidenței AP, cât și a incidenței Profil strict la 90°,
    fără coliziune cu masa sau câmpurile sterile.'
  phase: Test Preliminar de Geometrie & Centrare
- description: Impulsuri scurte de scopie (1 secundă) pentru verificarea alinierii
    fragmentelor osoase în timpul tracțiunii și manevrelor ortopedice de reducere.
  phase: Ghidaj Reducere Focar de Fractură
- description: Controlul avansării broșelor de ghidaj Kirschner în spongioasa osoasă
    sau canalul medular; verificare în două planuri ortogonale (AP și profil).
  phase: Ghidaj Broșe & Foraj
- description: Arcul C este angulat oblic până când orificiile transversale ale tijei
    centromedulare apar ca cercuri perfect rotunde pe monitor (nu ovale); introducerea
    șuruburilor de zăvorâre prin centrul cercului fără deviație.
  phase: Zăvorârea Tijei (Tehnica 'Perfect Circles')
- description: 'Clisee radiografice finale salvate în AP și profil strict: documentarea
    lungimii tuturor șuruburilor, excluderea efracturii articulare și alinierea axelor
    mecanice.'
  phase: Verificare Finală Multiax & Arhivare Documentară
author: Departamentul de Radiologie și Imagistică Medicală
category: c-arm
clinical_indications:
- Reducerea ortopedică și osteosinteza internă a fracturilor diafizare și metafizare
  de oase lungi (tije centromedulare blocate femur/tibie/humerus)
- Fixarea fracturilor de col femural și trohanteriene (șuruburi canulate, cui gamma,
  lamă-placă DHS)
- Osteosinteză minim invazivă cu plăci blocate (MIPO) la radius distal, tibie distală,
  humerus proximal
- Verificarea intraoperatorie a lungimii șuruburilor și a non-penetrării spațiului
  articular
- Controlul alinierii axiale și a lungimii membrelor în timpul manevrelor de tracțiune
  pe masa ortopedică
- Verificarea orientării componentelor protetice în artroplastiile complexe de șold
  sau genunchi
contraindications:
- Absența echipamentului individual de radioprotecție (șorțuri de plumb, gulere) pentru
  personalul din sala de operație
- Lipsa drapajului steril impermeabil dedicat pentru arcul C mobil
- Aparat C-arm fără verificare dozimetrică CNCAN valabilă
contrast:
  agent: Procedură standard fără contrast; La artrografie intraoperatorie de control
    se folosește contrast iodat non-ionic diluat 50%
  instructions: N/A
  route: N/A
  volume: N/A
fluoro_params:
  filtration: ≥ 3.0 mm Al echivalent
  grid: Cu grilă la segmente groase (șold/bazin); fără grilă la mână/antebraț
  kv: 60 - 75 kV (extremități distale) / 80 - 100 kV (șold, pelvis, femur)
  lih: Activ obligatoriu
  ma_range: 0.8 - 2.5 mA
  mode: Fluoroscopie Pulsată Joasă (Low-Dose Pulse 4 - 7.5 fps) + Last Image Hold
    (LIH) obligatoriu
  target_fluoro_time: < 2.0 - 3.0 minute timp total scopie pe intervenție
iris_reference:
  chapter: Traumatologie & Ortopedie
  radiation_dose: Clasa 1 (Minimă < 1 mSv) - Clasa 2
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: fluoro
notes: Rotirea arcului C mobil se face întotdeauna pe axul circular al brațului; NU
  se mobilizează membrul operat al pacientului pentru a obține profilul, evitând deplasarea
  fragmentelor reduse și compromiterea sterilului.
patient_prep: Masă chirurgicală ortopedică radiotransparentă de tracțiune sau masă
  standard cu extensii de fibră de carbon; drapaj steril complet al arcului C (huse
  sterile transparente); pacient anesteziat și monitorizat.
positioning_equipment:
  equipment_setup: 'POZIȚIONARE MANDATORIE C-ARM: Tubul generator de raze X se plasează
    OBLIGATORIU SUB masa de operație, iar detectorul plat/amplificatorul de imagine
    DEASUPRA pacientului; această geometrie reduce radiația difuză către ochii și
    trunchiul chirurgului cu 70-75% comparativ cu inversul ei; detectorul se apropie
    cât mai mult de pielea pacientului'
  patient_position: Decubit dorsal (sau lateral) pe masa ortopedică radiotransparentă
    conform segmentului osos operat
  sid: Distanță focar-receptor standard 90 - 100 cm
quality_criteria:
- Vizualizarea netă a corticalelor osoase și a focarului de fractură în două planuri
  perfect ortogonale (la 90°)
- Excluderea oricărei pătrunderi a materialului de osteosinteză în cavitatea articulară
- Confirmarea zăvorârii bi-corticale corecte a șuruburilor
- Imagini finale salvate și transmise în sistemul PACS al spitalului
radiation_safety:
- 'CHIRURGUL ȘI ASISTENȚII: Echipament de protecție obligatoriu — șorț plumbat (minim
  0.35 mm Pb, preferat 0.5 mm Pb), guler tiroidian și ochelari de protecție cu sticlă
  plumbată pentru prevenirea opacifierii cristalinului'
- 'REGULA INVERSULUI PĂTRATULUI DISTANȚEI: Personalul care nu asistă direct la masă
  face 2 pași înapoi (la > 2 metri, nivelul radiației difuze scade cu peste 90%)'
- 'MÂINILE CHIRURGULUI: Nu se introduc niciodată mâinile în fasciculul primar direct
  de raze X! Se folosesc instrumente cu mâner lung de ghidaj'
- 'COLIMARE: Colimatoarele lamelare ale arcului C se închid strâns strict pe focarul
  de osteosinteză'
- 'UTILIZAREA LAST IMAGE HOLD (LIH): Chirurgul analizează imaginea oprită pe monitor,
  fără a menține piciorul pe pedala de expunere'
slug: c-arm-osteosinteza-trauma-ortopedie
title: 'C-Arm în Ortopedie & Traumatologie: Reducere și Osteosinteză Fracturi'
sources:
- title: ACR-AAPM Technical Standard for Management of the Fluoroscopic Step in Interventional
    Procedures (C-Arm)
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Fluoro.pdf
  institution: ACR / AAPM
  source_region: US
  kind: Standard tehnic fluoroscopie C-Arm
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 45621b1990b6eabf74f9996a8a9c707b6d18590d018367baf4fe51409a0450b0
- title: IAEA — Radiation Protection in Fluoroscopically Guided Procedures
  url: https://www.iaea.org/resources/rpop/health-professionals/radiology/fluoroscopy
  institution: IAEA
  source_region: Internațional
  kind: Standard internațional de radioprotecție
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: fd2fa0ce9ba7efff54f416412f61219daf64504650a6a468b204fc00e14c54fa
position: Decubit dorsal (sau lateral) pe masa ortopedică radiotransparentă conform
  segmentului osos operat
---

# C-Arm în Ortopedie & Traumatologie: Reducere și Osteosinteză Fracturi

<div class="fluoro-meta-bar">
  <span class="fluoro-modality-badge">✨ Fluoroscopie & C-Arm</span>
  <span><strong>Actualizat:</strong> 2026-09-13</span>
  <span><strong>Autor:</strong> Departamentul de Radiologie și Imagistică Medicală</span>
</div>

---

<div class="grid cards" markdown>

-   __1. Rezumat Clinic, Indicații & Contraindicații__

    ---

    === "Indicații Clinice"

        - Reducerea ortopedică și osteosinteza internă a fracturilor diafizare și metafizare de oase lungi (tije centromedulare blocate femur/tibie/humerus)
        - Fixarea fracturilor de col femural și trohanteriene (șuruburi canulate, cui gamma, lamă-placă DHS)
        - Osteosinteză minim invazivă cu plăci blocate (MIPO) la radius distal, tibie distală, humerus proximal
        - Verificarea intraoperatorie a lungimii șuruburilor și a non-penetrării spațiului articular
        - Controlul alinierii axiale și a lungimii membrelor în timpul manevrelor de tracțiune pe masa ortopedică
        - Verificarea orientării componentelor protetice în artroplastiile complexe de șold sau genunchi

    === "Contraindicații & Atenționări"

        - Absența echipamentului individual de radioprotecție (șorțuri de plumb, gulere) pentru personalul din sala de operație
        - Lipsa drapajului steril impermeabil dedicat pentru arcul C mobil
        - Aparat C-arm fără verificare dozimetrică CNCAN valabilă

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Traumatologie & Ortopedie*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 1 (Minimă < 1 mSv) - Clasa 2`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Substanță de Contrast__

    ---

    - **Pregătire Prealabilă:** Masă chirurgicală ortopedică radiotransparentă de tracțiune sau masă standard cu extensii de fibră de carbon; drapaj steril complet al arcului C (huse sterile transparente); pacient anesteziat și monitorizat.
    - **Agent de Contrast:** Procedură standard fără contrast; La artrografie intraoperatorie de control se folosește contrast iodat non-ionic diluat 50%
    - **Cale de Administrare:** N/A
    - **Volum & Diluție:** N/A
    - **Instrucțiuni Specifice:** N/A

-   __3. Poziționare & Configurare Echipament (Masă / C-Arm)__

    ---

    - **Poziție Inițială Pacient:** Decubit dorsal (sau lateral) pe masa ortopedică radiotransparentă conform segmentului osos operat
    - **Configurare Braț C / Echipament:** POZIȚIONARE MANDATORIE C-ARM: Tubul generator de raze X se plasează OBLIGATORIU SUB masa de operație, iar detectorul plat/amplificatorul de imagine DEASUPRA pacientului; această geometrie reduce radiația difuză către ochii și trunchiul chirurgului cu 70-75% comparativ cu inversul ei; detectorul se apropie cât mai mult de pielea pacientului
    - **Distanță Focar-Receptor:** Distanță focar-receptor standard 90 - 100 cm

-   __4. Parametri Tehnici Scopie & Expunere__

    ---

    | Parametru Tehnic Scopie & Grafie | Valoare Configurare Generator / Arc C |
    |:---------------------------------|:---------------------------------------|
    | **Regim Fluoroscopie** | Fluoroscopie Pulsată Joasă (Low-Dose Pulse 4 - 7.5 fps) + Last Image Hold (LIH) obligatoriu |
    | **Tensiune Tub (kV)** | 60 - 75 kV (extremități distale) / 80 - 100 kV (șold, pelvis, femur) kV |
    | **Curent Tub Scopie (mA)** | 0.8 - 2.5 mA |
    | **Distanță Focar-Receptor (SID)** | 100 - 115 cm (detector cât mai aproape de pacient) |
    | **Grilă Antidifuzoare** | Cu grilă la segmente groase (șold/bazin); fără grilă la mână/antebraț |
    | **Filtrare Suplimentară** | ≥ 3.0 mm Al echivalent |
    | **Timp Țintă Scopie** | < 2.0 - 3.0 minute timp total scopie pe intervenție |
    | **Last Image Hold (LIH)** | Activ obligatoriu |

-   __5. Secvență Achiziție & Incidențe Seriate__

    ---

    - **Test Preliminar de Geometrie & Centrare:** Înainte de incizia chirurgicală: arcul C este poziționat și se verifică obținerea facilă atât a incidenței AP, cât și a incidenței Profil strict la 90°, fără coliziune cu masa sau câmpurile sterile.
    - **Ghidaj Reducere Focar de Fractură:** Impulsuri scurte de scopie (1 secundă) pentru verificarea alinierii fragmentelor osoase în timpul tracțiunii și manevrelor ortopedice de reducere.
    - **Ghidaj Broșe & Foraj:** Controlul avansării broșelor de ghidaj Kirschner în spongioasa osoasă sau canalul medular; verificare în două planuri ortogonale (AP și profil).
    - **Zăvorârea Tijei (Tehnica 'Perfect Circles'):** Arcul C este angulat oblic până când orificiile transversale ale tijei centromedulare apar ca cercuri perfect rotunde pe monitor (nu ovale); introducerea șuruburilor de zăvorâre prin centrul cercului fără deviație.
    - **Verificare Finală Multiax & Arhivare Documentară:** Clisee radiografice finale salvate în AP și profil strict: documentarea lungimii tuturor șuruburilor, excluderea efracturii articulare și alinierea axelor mecanice.

-   __6. Criterii de Calitate & Diagnostic__

    ---

    - Vizualizarea netă a corticalelor osoase și a focarului de fractură în două planuri perfect ortogonale (la 90°)
    - Excluderea oricărei pătrunderi a materialului de osteosinteză în cavitatea articulară
    - Confirmarea zăvorârii bi-corticale corecte a șuruburilor
    - Imagini finale salvate și transmise în sistemul PACS al spitalului

-   __7. Radioprotecție & Dozimetrie (ALARA)__

    ---

    - CHIRURGUL ȘI ASISTENȚII: Echipament de protecție obligatoriu — șorț plumbat (minim 0.35 mm Pb, preferat 0.5 mm Pb), guler tiroidian și ochelari de protecție cu sticlă plumbată pentru prevenirea opacifierii cristalinului
    - REGULA INVERSULUI PĂTRATULUI DISTANȚEI: Personalul care nu asistă direct la masă face 2 pași înapoi (la > 2 metri, nivelul radiației difuze scade cu peste 90%)
    - MÂINILE CHIRURGULUI: Nu se introduc niciodată mâinile în fasciculul primar direct de raze X! Se folosesc instrumente cu mâner lung de ghidaj
    - COLIMARE: Colimatoarele lamelare ale arcului C se închid strâns strict pe focarul de osteosinteză
    - UTILIZAREA LAST IMAGE HOLD (LIH): Chirurgul analizează imaginea oprită pe monitor, fără a menține piciorul pe pedala de expunere

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Rotirea arcului C mobil se face întotdeauna pe axul circular al brațului; NU se mobilizează membrul operat al pacientului pentru a obține profilul, evitând deplasarea fragmentelor reduse și compromiterea sterilului.

=== "Ghid Rapid de Execuție & Siguranță Fluoroscopică"

    1. **Pregătire și Informare:** Verificarea identității pacientului, a indicației clinice, a excluderii sarcinii la paciente fertile și informarea privind substanța de contrast.
    2. **Configurare Echipament:** La C-Arm mobil, tubul se poziționează OBLIGATORIU sub masa operatorie, iar detectorul plat cât mai aproape de pacient pentru minimalizarea radiației difuze către operator.
    3. **Optimizare Doză (ALARA):** Se utilizează regim de fluoroscopie pulsată (4 - 7.5 - 15 fps) în locul modului continuu și colimare strânsă strict pe zona de interes.
    4. **Last Image Hold (LIH):** Utilizarea imaginii înghețate pe monitor pentru decizii operatorii sau analize anatomice, fără reactivarea inutilă a pedalei de expunere.
    5. **Protecție Personal:** Toți membrii echipei prezenți în sală poartă echipament individual de protecție din plumb (șorț echivalent 0.35-0.5 mm Pb, guler tiroidian, ochelari plumbuiți) și păstrează o distanță maximă posibilă față de tub conform legii pătratului invers al distanței.

## Surse și revizuire

- [ACR-AAPM Technical Standard for Management of the Fluoroscopic Step in Interventional Procedures (C-Arm)](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Fluoro.pdf) — *ACR / AAPM* (US)
- [IAEA — Radiation Protection in Fluoroscopically Guided Procedures](https://www.iaea.org/resources/rpop/health-professionals/radiology/fluoroscopy) — *IAEA* (Internațional)
