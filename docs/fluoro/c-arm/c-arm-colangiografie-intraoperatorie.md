---
acquisition_steps:
- description: Medicul anestezist oprește temporar ventilația mecanică a pacientului
    la cererea chirurgului (apnee voluntară de 5-10 secunde pentru a elimina artefactele
    respiratorii diafragmatice).
  phase: Plasare Cateter & Apnee Anestezică
- description: 'Injectare lentă sub control fluoroscopic: se opacifiază canalul cistic
    și porțiunea distală a căii biliare principale; se evaluează ampula hepatopancreatică
    Vater și se caută microcalculi inclavați distal.'
  phase: Injectare Inițială Mică (3 - 5 ml)
- description: Opacifierea canalului hepatic comun, a joncțiunii hepatice și a ramurilor
    biliare intrahepatice dreaptă și stângă; excluderea defectelor de umplere sau
    a canalelor biliare aberante ligaturate eronat.
  phase: Injectare Completă Arbore Biliar (5 - 8 ml)
- description: Verificarea scurgerii libere și nestânjenite a substanței de contrast
    în lumenul duodenal (C duodenal) prin deschiderea sfincterului Oddi.
  phase: Pasaj Duodenal
author: Departamentul de Radiologie și Imagistică Medicală
category: c-arm
clinical_indications:
- Colecistectomie laparoscopică sau clasică dificilă (anatomie neclară a triunghiului
  hepatocistic Calot)
- Suspiciune de litiază coledociană (calculi restanți în calea biliară principală
  decelați clinic, biologic sau ecografic)
- Prevenirea și decelarea precoce a leziunilor iatrogene de cale biliară principală
  sau canal hepatic drept aberant
- Dilatație inexplicabilă a căii biliare principale observată intraoperator
- Verificarea permeabilității joncțiunii bilio-duodenale și a funcției sfincterului
  Oddi
contraindications:
- Alergie severă cunoscută (șoc anafilactic anterior) la substanțe de contrast iodate
- Instabilitate hemodinamică severă intraoperatorie care impune finalizarea de urgență
  a actului chirurgical
contrast:
  agent: Contrast iodat hidrosolubil non-ionic (Omnipaque 300 / Iopamiro 300) DILUAT
    OBLIGATORIU 1:1 cu ser fiziologic steril (concentrație finală ~150 mg I/ml; contrastul
    pur 100% este prea dens și maschează microcalculii biliari radiotransparenți!)
  instructions: 'EXTREM DE IMPORTANT: seringa și cateterul trebuie să fie purjate
    perfect de orice bulă de aer; o bulă de aer injectată accidental în coledoc mimează
    perfect un calcul biliar!'
  route: Injectare pe cateterul colangiografic (cateter ureteral 4-5 Fr sau cateter
    dedicat Olsen) introdus prin canalul cistic canulat
  volume: 10 - 20 ml contrast diluat
fluoro_params:
  filtration: ≥ 3.0 mm Al
  grid: Cu grilă
  kv: 75 - 85 kV
  lih: Activ
  ma_range: 1.0 - 2.5 mA
  mode: Fluoroscopie Pulsată + Radiografie Digitală (Digital Snap)
  target_fluoro_time: < 1 minut timp total scopie
iris_reference:
  chapter: Chirurgie Digestivă & Căi Biliare
  radiation_dose: Clasa 1 (Minimă < 1 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: fluoro
notes: Dacă sfincterul Oddi este în spasm și contrastul nu trece în duoden, administrarea
  intravenoasă de 1 mg Glucagon de către anestezist relaxează sfincterul în 60 de
  secunde, confirmând absența unui obstacol mecanic litiazic.
patient_prep: Masă chirurgicală radiotransparentă; înclinare în poziție anti-Trendelenburg
  (15°) și ușoară rotație a mesei pe partea dreaptă a pacientului (degajează calea
  biliară de suprapunerea pe coloana vertebrală lombară); drapaj steril al arcului
  C.
positioning_equipment:
  equipment_setup: Arc în C mobil centrat pe hipocondrul drept; tubul sub masă, detectorul
    plat coborât cât mai aproape de abdomenul pacientului
  patient_position: Decubit dorsal pe masa de operație cu brațul stâng la 90° și dreptul
    la trunchi
  sid: 90 - 100 cm
quality_criteria:
- Vizualizarea integrală a arborelui biliar intrahepatic și extrahepatic
- Demonstrarea pasajului liber al contrastului în duoden
- Contururi biliare regulate, fără extravazare de contrast în cavitatea peritoneală
- Diferențierea certă a calculilor de bulele de aer (calculul este fixat parietal
  sau decliv, bula de aer se mișcă spre hil)
radiation_safety:
- Timp extrem de scurt de expunere (de obicei sub 20-30 secunde de scopie cumulată)
- Avertizare sonoră cu 5 secunde înainte ('Atenție, raze!') pentru ca personalul neesențial
  să se îndepărteze la > 2 metri
- Echipa operatorie poartă șorțuri de plumb și gulere tiroidiene
- DAP < 3 Gy·cm²
slug: c-arm-colangiografie-intraoperatorie
title: 'C-Arm în Chirurgie: Colangiografie Intraoperatorie (CIO)'
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
position: Decubit dorsal pe masa de operație cu brațul stâng la 90° și dreptul la
  trunchi
---

# C-Arm în Chirurgie: Colangiografie Intraoperatorie (CIO)

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

        - Colecistectomie laparoscopică sau clasică dificilă (anatomie neclară a triunghiului hepatocistic Calot)
        - Suspiciune de litiază coledociană (calculi restanți în calea biliară principală decelați clinic, biologic sau ecografic)
        - Prevenirea și decelarea precoce a leziunilor iatrogene de cale biliară principală sau canal hepatic drept aberant
        - Dilatație inexplicabilă a căii biliare principale observată intraoperator
        - Verificarea permeabilității joncțiunii bilio-duodenale și a funcției sfincterului Oddi

    === "Contraindicații & Atenționări"

        - Alergie severă cunoscută (șoc anafilactic anterior) la substanțe de contrast iodate
        - Instabilitate hemodinamică severă intraoperatorie care impune finalizarea de urgență a actului chirurgical

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Chirurgie Digestivă & Căi Biliare*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 1 (Minimă < 1 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Substanță de Contrast__

    ---

    - **Pregătire Prealabilă:** Masă chirurgicală radiotransparentă; înclinare în poziție anti-Trendelenburg (15°) și ușoară rotație a mesei pe partea dreaptă a pacientului (degajează calea biliară de suprapunerea pe coloana vertebrală lombară); drapaj steril al arcului C.
    - **Agent de Contrast:** Contrast iodat hidrosolubil non-ionic (Omnipaque 300 / Iopamiro 300) DILUAT OBLIGATORIU 1:1 cu ser fiziologic steril (concentrație finală ~150 mg I/ml; contrastul pur 100% este prea dens și maschează microcalculii biliari radiotransparenți!)
    - **Cale de Administrare:** Injectare pe cateterul colangiografic (cateter ureteral 4-5 Fr sau cateter dedicat Olsen) introdus prin canalul cistic canulat
    - **Volum & Diluție:** 10 - 20 ml contrast diluat
    - **Instrucțiuni Specifice:** EXTREM DE IMPORTANT: seringa și cateterul trebuie să fie purjate perfect de orice bulă de aer; o bulă de aer injectată accidental în coledoc mimează perfect un calcul biliar!

-   __3. Poziționare & Configurare Echipament (Masă / C-Arm)__

    ---

    - **Poziție Inițială Pacient:** Decubit dorsal pe masa de operație cu brațul stâng la 90° și dreptul la trunchi
    - **Configurare Braț C / Echipament:** Arc în C mobil centrat pe hipocondrul drept; tubul sub masă, detectorul plat coborât cât mai aproape de abdomenul pacientului
    - **Distanță Focar-Receptor:** 90 - 100 cm

-   __4. Parametri Tehnici Scopie & Expunere__

    ---

    | Parametru Tehnic Scopie & Grafie | Valoare Configurare Generator / Arc C |
    |:---------------------------------|:---------------------------------------|
    | **Regim Fluoroscopie** | Fluoroscopie Pulsată + Radiografie Digitală (Digital Snap) |
    | **Tensiune Tub (kV)** | 75 - 85 kV |
    | **Curent Tub Scopie (mA)** | 1.0 - 2.5 mA |
    | **Distanță Focar-Receptor (SID)** | 100 - 115 cm (detector cât mai aproape de pacient) |
    | **Grilă Antidifuzoare** | Cu grilă |
    | **Filtrare Suplimentară** | ≥ 3.0 mm Al |
    | **Timp Țintă Scopie** | < 1 minut timp total scopie |
    | **Last Image Hold (LIH)** | Activ |

-   __5. Secvență Achiziție & Incidențe Seriate__

    ---

    - **Plasare Cateter & Apnee Anestezică:** Medicul anestezist oprește temporar ventilația mecanică a pacientului la cererea chirurgului (apnee voluntară de 5-10 secunde pentru a elimina artefactele respiratorii diafragmatice).
    - **Injectare Inițială Mică (3 - 5 ml):** Injectare lentă sub control fluoroscopic: se opacifiază canalul cistic și porțiunea distală a căii biliare principale; se evaluează ampula hepatopancreatică Vater și se caută microcalculi inclavați distal.
    - **Injectare Completă Arbore Biliar (5 - 8 ml):** Opacifierea canalului hepatic comun, a joncțiunii hepatice și a ramurilor biliare intrahepatice dreaptă și stângă; excluderea defectelor de umplere sau a canalelor biliare aberante ligaturate eronat.
    - **Pasaj Duodenal:** Verificarea scurgerii libere și nestânjenite a substanței de contrast în lumenul duodenal (C duodenal) prin deschiderea sfincterului Oddi.

-   __6. Criterii de Calitate & Diagnostic__

    ---

    - Vizualizarea integrală a arborelui biliar intrahepatic și extrahepatic
    - Demonstrarea pasajului liber al contrastului în duoden
    - Contururi biliare regulate, fără extravazare de contrast în cavitatea peritoneală
    - Diferențierea certă a calculilor de bulele de aer (calculul este fixat parietal sau decliv, bula de aer se mișcă spre hil)

-   __7. Radioprotecție & Dozimetrie (ALARA)__

    ---

    - Timp extrem de scurt de expunere (de obicei sub 20-30 secunde de scopie cumulată)
    - Avertizare sonoră cu 5 secunde înainte ('Atenție, raze!') pentru ca personalul neesențial să se îndepărteze la > 2 metri
    - Echipa operatorie poartă șorțuri de plumb și gulere tiroidiene
    - DAP < 3 Gy·cm²

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Dacă sfincterul Oddi este în spasm și contrastul nu trece în duoden, administrarea intravenoasă de 1 mg Glucagon de către anestezist relaxează sfincterul în 60 de secunde, confirmând absența unui obstacol mecanic litiazic.

=== "Ghid Rapid de Execuție & Siguranță Fluoroscopică"

    1. **Pregătire și Informare:** Verificarea identității pacientului, a indicației clinice, a excluderii sarcinii la paciente fertile și informarea privind substanța de contrast.
    2. **Configurare Echipament:** La C-Arm mobil, tubul se poziționează OBLIGATORIU sub masa operatorie, iar detectorul plat cât mai aproape de pacient pentru minimalizarea radiației difuze către operator.
    3. **Optimizare Doză (ALARA):** Se utilizează regim de fluoroscopie pulsată (4 - 7.5 - 15 fps) în locul modului continuu și colimare strânsă strict pe zona de interes.
    4. **Last Image Hold (LIH):** Utilizarea imaginii înghețate pe monitor pentru decizii operatorii sau analize anatomice, fără reactivarea inutilă a pedalei de expunere.
    5. **Protecție Personal:** Toți membrii echipei prezenți în sală poartă echipament individual de protecție din plumb (șorț echivalent 0.35-0.5 mm Pb, guler tiroidian, ochelari plumbuiți) și păstrează o distanță maximă posibilă față de tub conform legii pătratului invers al distanței.

## Surse și revizuire

- [ACR-AAPM Technical Standard for Management of the Fluoroscopic Step in Interventional Procedures (C-Arm)](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Fluoro.pdf) — *ACR / AAPM* (US)
- [IAEA — Radiation Protection in Fluoroscopically Guided Procedures](https://www.iaea.org/resources/rpop/health-professionals/radiology/fluoroscopy) — *IAEA* (Internațional)
