---
acquisition_steps:
- description: 'PAS OBLIGATORIU: radiografie abdominală în decubit pentru a exclude
    categoric pneumoperitoneul (prezența aerului liber subdiafragmatic contraindică
    manevra).'
  phase: Radiografie Abdominală Nativă Preliminară
- description: Se începe insuflarea de aer menținând presiunea la 80 mmHg; la nevoie
    se poate crește progresiv până la maxim 110 - 120 mmHg; NU SE DEPĂȘEȘTE NICIODATĂ
    PRESIUNEA DE 120 mmHg din cauza riscului de barotraumă și perforație colonică!
  phase: Insuflare Controlată de Aer & Monitorizare Presiune
- description: Prin impulsuri scurte de fluoroscopie de 1-2 secunde se urmărește retragerea
    masei de invaginație (semnul meniscului convex) din colonul stâng, prin transvers
    și ascendent către cec.
  phase: Urmărirea Progresiei Capului de Invaginație
- description: 'CRITERIUL DE AUR AL SUCCESULUI: La nivelul cecului, capul de invaginație
    cedează brusc, iar aerul / contrastul refulează MASIV și liber în ansele ileonului
    terminal pe o distanță de minim 25-30 cm, concomitent cu dispariția masei tumorale
    palpabile.'
  phase: Reducerea Ileo-Cecală & Refularea Masivă de Aer
- description: Cliseu radiologic documentar al reducerii complete cu aer în ileonul
    terminal; deschiderea sondei rectale pentru evacuarea aerului din colon; ameliorare
    clinică spectaculoasă a copilului.
  phase: Cliseu Final & Decompresie
author: Departamentul de Radiologie și Imagistică Medicală
category: pediatrie
clinical_indications:
- Invaginație intestinală ileo-colică acută idiopatică la sugar și copil mic (vârstă
  tipică 3 luni - 3 ani) diagnosticată ecografic (aspect în cocardă / pseudorinichi)
- Copil stabil hemodinamic, fără semne clinice de peritonită, fără șoc toxico-septic
  și fără pneumoperitoneu
- Debut al simptomatologiei de preferință sub 24 - 48 ore de la debutul primelor colici
  abdominale
contraindications:
- Semne clinice de peritonită acută generalizată sau abdomen acut chirurgical
- Pneumoperitoneu decelat pe radiografia abdominală simplă (dovadă de perforație enterală
  prealabilă)
- Stare de șoc hipovolemic / septic sau instabilitate hemodinamică severă
- Invaginație ileo-ileală izolată (nu poate fi redusă pe cale retrogradă colonică;
  necesită chirurgie)
- Suspiciune certă de punct de plecare anatomic secundar patologic (diverticul Meckel,
  polip voluminos, limfom intestinal)
contrast:
  agent: Reducere Pneumatică (AER insuflat controlat printr-un sistem dedicat cu manometru
    de presiune și valvă de suprapresiune) — METODA DE ELECȚIE MODERNA; SAU Reducere
    Hidrostatică cu substanță de contrast iodată hidrosolubilă izoosmolară călduță
    / ser fiziologic călduț; CONTRAINDICAȚIE FORMALĂ pentru Sulfatul de Bariu din
    cauza riscului de peritonită chimică gravă în cazul unei perforații
  instructions: Balonașul sondei Foley se umflă cu 15-20 ml aer sau ser, se trage
    ușor pe perineu și se etanșează fesele ferm cu benzi adezive elastice late pentru
    a împiedica scăpările de presiune
  route: Retrogradă, pe cateter rectal moale (Foley 18-22 Fr) introdus în rect
  volume: Aer insuflat sub presiune strict monitorizată
fluoro_params:
  filtration: Totală ≥ 3.0 mm Al + 0.1 mm Cu
  grid: Fără grilă (Grid removal)
  kv: 65 - 75 kV
  lih: Activ obligatoriu
  ma_range: 0.5 - 1.5 mA
  mode: Fluoroscopie Pulsată Scurtă la 3 - 7.5 fps; FĂRĂ GRILĂ ANTIDIFUZOARE
  target_fluoro_time: < 2.0 minute cumulat pe procedură
iris_reference:
  chapter: Pediatrie & Urgențe Digestive
  radiation_dose: Clasa 1 (Minimă < 1 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-13'
modality: fluoro
notes: Rata de succes a dezinvaginării pneumatice este de 80-90% în centrele specializate.
  Rata de recidivă în primele 24-48 ore este de aproximativ 5-10%; copilul rămâne
  internat sub supraveghere medicală 24 de ore post-procedură.
patient_prep: Linie venoasă periferică funcțională montată obligatoriu și reechilibrare
  volemică hidro-electrolitică inițiată; sondă nazo-gastrică deschisă la pungă pentru
  decomprimarea stomacului; **CHIRURGUL PEDIATRU ȘI SALA DE OPERAȚIE ALERTATE ÎN STANDBY
  OBLIGATORIU** înainte de a începe procedura; consimțământ informat semnat de părinți.
positioning_equipment:
  equipment_setup: Masă fluoroscopică digitală sau sistem C-Arm; dispozitiv de insuflare
    de aer conectat la manometru mecanic de presiune calibrat
  patient_position: Decubit dorsal pe masa radiologică
  sid: 100 - 115 cm
quality_criteria:
- Evidențierea certă a refulării masive de aer sau contrast în ansele intestinului
  subțire (ileon)
- Dispariția completă a defectului de umplere rotund-ovalar din cec/colon
- Oprirea colicilor abdominale și adormirea liniștită a copilului după procedură
- Confirmare ecografică post-reducere a dispariției imaginii în cocardă
radiation_safety:
- 'Regulă strictă de timp: scopia se acționează doar 1-2 secunde per verificare a
  poziției masei'
- Fără grilă antidifuzoare pentru a proteja țesuturile pediatrice hipersensibile la
  radiații
- DAP mediu < 1.0 - 2.0 Gy·cm²
- 'Regula celor 3 încercări: dacă după 3 tentative de câte 3 minute de insuflare masa
  nu avansează deloc dincolo de cec, procedura se întrerupe și se trece la cura chirurgicală'
slug: dezinvaginare-intestinala-fluoro
title: Dezinvaginare Intestinală sub Control Fluoroscopic (Reducere Pneumatică / Hidrostatică)
sources:
- title: Image Gently — Pediatric Fluoroscopy Protocols & Radiation Safety
  url: https://www.imagegently.org/Procedures/Fluoroscopy
  institution: Image Gently Alliance
  source_region: US
  kind: Ghid pediatric de reducere a dozei fluoroscopie
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 8980473d4f9eebbc8a011eeb2d625b631a9b984fceb163adf52955f8668af536
- title: ACR-SPR Practice Parameter for the Performance of Pediatric Fluoroscopy
  url: https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Fluoro.pdf
  institution: ACR / SPR
  source_region: US
  kind: Standard de practică fluoroscopie pediatrică
  checked_at: '2026-09-14T15:57:46.637480+00:00'
  sha256: 45621b1990b6eabf74f9996a8a9c707b6d18590d018367baf4fe51409a0450b0
position: Decubit dorsal pe masa radiologică
---

# Dezinvaginare Intestinală sub Control Fluoroscopic (Reducere Pneumatică / Hidrostatică)

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

        - Invaginație intestinală ileo-colică acută idiopatică la sugar și copil mic (vârstă tipică 3 luni - 3 ani) diagnosticată ecografic (aspect în cocardă / pseudorinichi)
        - Copil stabil hemodinamic, fără semne clinice de peritonită, fără șoc toxico-septic și fără pneumoperitoneu
        - Debut al simptomatologiei de preferință sub 24 - 48 ore de la debutul primelor colici abdominale

    === "Contraindicații & Atenționări"

        - Semne clinice de peritonită acută generalizată sau abdomen acut chirurgical
        - Pneumoperitoneu decelat pe radiografia abdominală simplă (dovadă de perforație enterală prealabilă)
        - Stare de șoc hipovolemic / septic sau instabilitate hemodinamică severă
        - Invaginație ileo-ileală izolată (nu poate fi redusă pe cale retrogradă colonică; necesită chirurgie)
        - Suspiciune certă de punct de plecare anatomic secundar patologic (diverticul Meckel, polip voluminos, limfom intestinal)

    === "Ghid Național IRIS"

        !!! info "Referință Primară: Ghidul Național IRIS (Ordinul MS 1342/2012)"
            - **Capitol Ghid IRIS:** *Pediatrie & Urgențe Digestive*
            - **Grad de Recomandare:** **Grad A**
            - **Nivel de Iradiere Estimată:** `Clasa 1 (Minimă < 1 mSv)`

            [:octicons-search-16: Deschide Ghidul IRIS](../../iris.md){ .md-button .md-button--primary } [:material-open-in-new: Aplicația Oficială PWA](https://radiologie-pediatrica.ro/iris/){ .md-button target="_blank" rel="noopener" }
-   __2. Pregătire Pacient & Substanță de Contrast__

    ---

    - **Pregătire Prealabilă:** Linie venoasă periferică funcțională montată obligatoriu și reechilibrare volemică hidro-electrolitică inițiată; sondă nazo-gastrică deschisă la pungă pentru decomprimarea stomacului; **CHIRURGUL PEDIATRU ȘI SALA DE OPERAȚIE ALERTATE ÎN STANDBY OBLIGATORIU** înainte de a începe procedura; consimțământ informat semnat de părinți.
    - **Agent de Contrast:** Reducere Pneumatică (AER insuflat controlat printr-un sistem dedicat cu manometru de presiune și valvă de suprapresiune) — METODA DE ELECȚIE MODERNA; SAU Reducere Hidrostatică cu substanță de contrast iodată hidrosolubilă izoosmolară călduță / ser fiziologic călduț; CONTRAINDICAȚIE FORMALĂ pentru Sulfatul de Bariu din cauza riscului de peritonită chimică gravă în cazul unei perforații
    - **Cale de Administrare:** Retrogradă, pe cateter rectal moale (Foley 18-22 Fr) introdus în rect
    - **Volum & Diluție:** Aer insuflat sub presiune strict monitorizată
    - **Instrucțiuni Specifice:** Balonașul sondei Foley se umflă cu 15-20 ml aer sau ser, se trage ușor pe perineu și se etanșează fesele ferm cu benzi adezive elastice late pentru a împiedica scăpările de presiune

-   __3. Poziționare & Configurare Echipament (Masă / C-Arm)__

    ---

    - **Poziție Inițială Pacient:** Decubit dorsal pe masa radiologică
    - **Configurare Braț C / Echipament:** Masă fluoroscopică digitală sau sistem C-Arm; dispozitiv de insuflare de aer conectat la manometru mecanic de presiune calibrat
    - **Distanță Focar-Receptor:** 100 - 115 cm

-   __4. Parametri Tehnici Scopie & Expunere__

    ---

    | Parametru Tehnic Scopie & Grafie | Valoare Configurare Generator / Arc C |
    |:---------------------------------|:---------------------------------------|
    | **Regim Fluoroscopie** | Fluoroscopie Pulsată Scurtă la 3 - 7.5 fps; FĂRĂ GRILĂ ANTIDIFUZOARE |
    | **Tensiune Tub (kV)** | 65 - 75 kV |
    | **Curent Tub Scopie (mA)** | 0.5 - 1.5 mA |
    | **Distanță Focar-Receptor (SID)** | 100 - 115 cm (detector cât mai aproape de pacient) |
    | **Grilă Antidifuzoare** | Fără grilă (Grid removal) |
    | **Filtrare Suplimentară** | Totală ≥ 3.0 mm Al + 0.1 mm Cu |
    | **Timp Țintă Scopie** | < 2.0 minute cumulat pe procedură |
    | **Last Image Hold (LIH)** | Activ obligatoriu |

-   __5. Secvență Achiziție & Incidențe Seriate__

    ---

    - **Radiografie Abdominală Nativă Preliminară:** PAS OBLIGATORIU: radiografie abdominală în decubit pentru a exclude categoric pneumoperitoneul (prezența aerului liber subdiafragmatic contraindică manevra).
    - **Insuflare Controlată de Aer & Monitorizare Presiune:** Se începe insuflarea de aer menținând presiunea la 80 mmHg; la nevoie se poate crește progresiv până la maxim 110 - 120 mmHg; NU SE DEPĂȘEȘTE NICIODATĂ PRESIUNEA DE 120 mmHg din cauza riscului de barotraumă și perforație colonică!
    - **Urmărirea Progresiei Capului de Invaginație:** Prin impulsuri scurte de fluoroscopie de 1-2 secunde se urmărește retragerea masei de invaginație (semnul meniscului convex) din colonul stâng, prin transvers și ascendent către cec.
    - **Reducerea Ileo-Cecală & Refularea Masivă de Aer:** CRITERIUL DE AUR AL SUCCESULUI: La nivelul cecului, capul de invaginație cedează brusc, iar aerul / contrastul refulează MASIV și liber în ansele ileonului terminal pe o distanță de minim 25-30 cm, concomitent cu dispariția masei tumorale palpabile.
    - **Cliseu Final & Decompresie:** Cliseu radiologic documentar al reducerii complete cu aer în ileonul terminal; deschiderea sondei rectale pentru evacuarea aerului din colon; ameliorare clinică spectaculoasă a copilului.

-   __6. Criterii de Calitate & Diagnostic__

    ---

    - Evidențierea certă a refulării masive de aer sau contrast în ansele intestinului subțire (ileon)
    - Dispariția completă a defectului de umplere rotund-ovalar din cec/colon
    - Oprirea colicilor abdominale și adormirea liniștită a copilului după procedură
    - Confirmare ecografică post-reducere a dispariției imaginii în cocardă

-   __7. Radioprotecție & Dozimetrie (ALARA)__

    ---

    - Regulă strictă de timp: scopia se acționează doar 1-2 secunde per verificare a poziției masei
    - Fără grilă antidifuzoare pentru a proteja țesuturile pediatrice hipersensibile la radiații
    - DAP mediu < 1.0 - 2.0 Gy·cm²
    - Regula celor 3 încercări: dacă după 3 tentative de câte 3 minute de insuflare masa nu avansează deloc dincolo de cec, procedura se întrerupe și se trece la cura chirurgicală

</div>

!!! note "Observații Clinice, Capcane & Recomandări Practice"
    Rata de succes a dezinvaginării pneumatice este de 80-90% în centrele specializate. Rata de recidivă în primele 24-48 ore este de aproximativ 5-10%; copilul rămâne internat sub supraveghere medicală 24 de ore post-procedură.

=== "Ghid Rapid de Execuție & Siguranță Fluoroscopică"

    1. **Pregătire și Informare:** Verificarea identității pacientului, a indicației clinice, a excluderii sarcinii la paciente fertile și informarea privind substanța de contrast.
    2. **Configurare Echipament:** La C-Arm mobil, tubul se poziționează OBLIGATORIU sub masa operatorie, iar detectorul plat cât mai aproape de pacient pentru minimalizarea radiației difuze către operator.
    3. **Optimizare Doză (ALARA):** Se utilizează regim de fluoroscopie pulsată (4 - 7.5 - 15 fps) în locul modului continuu și colimare strânsă strict pe zona de interes.
    4. **Last Image Hold (LIH):** Utilizarea imaginii înghețate pe monitor pentru decizii operatorii sau analize anatomice, fără reactivarea inutilă a pedalei de expunere.
    5. **Protecție Personal:** Toți membrii echipei prezenți în sală poartă echipament individual de protecție din plumb (șorț echivalent 0.35-0.5 mm Pb, guler tiroidian, ochelari plumbuiți) și păstrează o distanță maximă posibilă față de tub conform legii pătratului invers al distanței.

## Surse și revizuire

- [Image Gently — Pediatric Fluoroscopy Protocols & Radiation Safety](https://www.imagegently.org/Procedures/Fluoroscopy) — *Image Gently Alliance* (US)
- [ACR-SPR Practice Parameter for the Performance of Pediatric Fluoroscopy](https://www.acr.org/-/media/ACR/Files/Practice-Parameters/Fluoro.pdf) — *ACR / SPR* (US)
