#!/usr/bin/env python3
"""generate_mcb_protocols.py — Generează protocoalele MCB Radiology (Florida / Baptist Health System)
și creează zona completă de Radiologie Nucleară (Medicină Nucleară - MN).

Sursă: MCB Radiology Reference Manual
URL de bază: https://ref.mcbradiology.com/
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

# UTF-8 pe terminale Windows
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
AUTHOR_MCB = "MCB Radiology / Baptist Health System / Clinical Imaging Reference"
DATE_NOW = "2026-09-27"

def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)

# ==============================================================================
# 1. GENERATOR CT SCANNER DEFAULTS
# ==============================================================================
def generate_ct_scanner_defaults():
    content = """---
title: Parametri Impliciti Scanere CT (Siemens, GE, Philips) - MCB Radiology
author: MCB Radiology / Baptist Health System / Clinical Engineering
category: ct
modality: ct
slug: parametri-aparate-scanner-defaults
clinical_indications:
  - Ghid tehnic de referință pentru parametri impliciți de scanare CT
  - Standardizare protocoale Siemens, GE și Philips în rețeaua spitalicească
last_updated: '2026-09-27'
sources:
  - title: MCB Radiology Scanner Default Protocols Manual
    url: https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Scanner%20Default%20Protocols.html
    relationship: authoritative_institutional_reference
---

# ⚙️ Parametri Impliciti Scanere CT (Siemens, GE, Philips) & Flota MCB Radiology

Ghid tehnic de referință pentru parametrii impliciți de scanare, tehnologiile de modulare automată a dozei și algoritmii de reconstrucție iterativă pe platformele tomografice majore (**Siemens Healthineers**, **GE HealthCare**, **Philips Healthcare**), conform standardelor **MCB Radiology / Baptist Health System**.

<div class="iris-official-banner" style="margin-bottom: 24px; background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; padding: 20px 24px; border-radius: 12px; border: 1px solid rgba(56, 189, 248, 0.3);">
  <div class="iris-official-badge" style="background: rgba(56, 189, 248, 0.2); color: #38bdf8; padding: 4px 12px; border-radius: 999px; display: inline-block; font-weight: 700; font-size: 0.82rem; margin-bottom: 8px;">
    ⚡ FLOTĂ SCANERE &bull; STANDARDE DE FABRICĂ &bull; RECONSTRUCȚIE ITERATIVĂ
  </div>
  <p class="iris-official-desc" style="margin-bottom: 12px !important; color: #f1f5f9; font-size: 0.95rem; line-height: 1.55;">
    Parametrii de mai jos reprezintă valorile de referință instalate pe computerele tomografe din rețeaua spitalicească (Riverside, Southside, Clay, St. Johns, Freestanding ERs). Fiecare protocol include kilovoltajul (kV), modularea mAs (CARE Dose4D / Smart mA / DoseWise), colimarea, timpul de rotație și kernele de reconstrucție recomandate.
  </p>
  <a href="https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Scanner%20Default%20Protocols.html" target="_blank" rel="noopener" style="font-weight: 600; color: #38bdf8; text-decoration: none;">
    Consultă catalogul oficial Scanner Default Protocols pe portalul MCB ➔
  </a>
</div>

---

## 1. Distribuția Scanerelor CT în Rețeaua Spitalicească

| Spital / Locație | Scaner CT Principal | Scaner CT Secundar / Urgențe | Documentație Tehnică Implicită |
|:-----------------|:--------------------|:-----------------------------|:-------------------------------|
| **Baptist Riverside** | Siemens SOMATOM Drive (128 slice Dual Source) | Siemens SOMATOM Force (192 slice Dual Source) | [Vezi Drive VB20](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/SOMATOM%20Drive%20Protocols%20%28VB20%29.pdf){ target="_blank" rel="noopener" } &bull; [Vezi Force VA40](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/SOMATOM%20Force%20Protocols%20%28VA40%29.pdf){ target="_blank" rel="noopener" } |
| **Baptist Southside** | GE Revolution Ascend Plus | Siemens SOMATOM Definition AS 64 | [Vezi GE Ascend Plus](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/GE%20Revolution%20Ascend%20Plus%20Protocols.pdf){ target="_blank" rel="noopener" } &bull; [Vezi Definition AS](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/Definition%20AS%2064%20Protocols%20%28VB20%29.pdf){ target="_blank" rel="noopener" } |
| **Baptist Clay** | Siemens SOMATOM go.Top (128 slice) | GE LightSpeed VCT 64 | [Vezi go.Top 128](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/SOMATOM%20go.Top%20Protocols.pdf){ target="_blank" rel="noopener" } &bull; [Vezi LS VCT 64](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/GE%20LightSpeed%20VCT%2064%20Protocols.pdf){ target="_blank" rel="noopener" } |
| **Baptist St. Johns** | Philips Incisive 128 | GE Revolution Maxima 64 | [Vezi Philips Incisive](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/Philips%20Incisive%20128%20Protocols.pdf){ target="_blank" rel="noopener" } &bull; [Vezi Rev Maxima](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/GE%20Revolution%20Maxima%2064%20Protocols.pdf){ target="_blank" rel="noopener" } |
| **Freestanding ER / Optimals** | Siemens SOMATOM go.Top / GE LS 16 | Siemens Definition AS 64 | [Vezi GE LS 16](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/GE%20LightSpeed%2016%20Protocols.pdf){ target="_blank" rel="noopener" } |

---

## 2. Comparație Tehnologică Parametri Impliciti

| Parametru Tehnic | Siemens SOMATOM Drive / Force | GE Revolution Ascend Plus / Maxima | Philips Incisive 128 |
|:-----------------|:------------------------------|:-----------------------------------|:---------------------|
| **Modulare Automată Curent Tub** | **CARE Dose4D** (calibrare calitativă ref mAs) | **Smart mA / Auto mA** (zgomot țintă Noise Index - NI) | **DoseWise / Z-DOM / D-DOM** (DRI index) |
| **Selecție Automată Tensiune** | **CARE kV** (optimizat pentru substanță de contrast iodată) | **kV Assist** (adaptat la mărimea pacientului) | **Patient Specific kV** |
| **Reconstrucție Iterativă** | **ADMIRE** (Advanced Modeled Iterative Reconstruction, nivele 2-4) | **ASiR-V** (Adaptive Statistical Iterative Recon, 40-60%) / **TrueFidelity** (DLIR - Deep Learning) | **iDose4** (nivele 3-5) & **IMR** (Knowledge-based Iterative Model) |
| **Filtrare & Reducere Artefacte Metal** | **iMAR** (Iterative Metal Artifact Reduction) | **Smart MAR** | **O-MAR** (Orthopedic Metal Artifact Reduction) |
| **Viteze Rotație Gantry** | 0.28 s (Drive) / 0.25 s (Force) | 0.35 s (Ascend Plus) / 0.5 s | 0.33 s - 0.5 s |
| **Detector / Colimare Maximă** | $2 \times 64 \times 0.6$ mm / $2 \times 96 \times 0.6$ mm | $64 \times 0.625$ mm ($40$ mm lățime) | $64 \times 0.625$ mm ($40$ mm lățime) |

---

## 3. Parametri Impliciti de Scanare pe Regiuni Anatomice (MCB Protocol Matrix)

### 3.1. Abdomen & Pelvis (Rutină cu Contrast)
- **Siemens Drive / Force:**
    - Mod scanare: Spirală, colimare $128 \times 0.6$ mm (Drive) / $192 \times 0.6$ mm (Force), pitch 0.8.
    - Tensiune/Curent: CARE kV (On, referință 100-120 kV), CARE Dose4D On (Quality Ref. mAs: 150-180 mAs).
    - Reconstrucție: Grosime secțiune 3.0 mm, increment 3.0 mm; Reconstrucție subțire 0.75 mm / 0.5 mm pentru reformate 3D MPR; Kernel I30f / I31f (ADMIRE 3).
- **GE Revolution Ascend Plus / VCT 64:**
    - Mod scanare: Helical, colimare $64 \times 0.625$ mm (40 mm beam), pitch 0.984:1, viteză rotație 0.5 s.
    - Tensiune/Curent: 120 kV (sau kV Assist), Smart mA On (interval 100-450 mA, Noise Index NI: 12.5 - 13.5).
    - Reconstrucție: 2.5 mm axiale + 2.5 mm coronale/sagitale; Reconstrucție iterativă ASiR-V 50%; Kernel Standard.
- **Philips Incisive 128:**
    - Mod scanare: Helical, colimare $64 \times 0.625$ mm, pitch 0.891, timp rotație 0.5 s.
    - Tensiune/Curent: 120 kV, DoseWise On (Dose Right Index DRI: 17).
    - Reconstrucție: 3.0 mm / 3.0 mm, Reconstrucție iterativă iDose4 nivel 3; Filter B (Smooth/Standard).

### 3.2. Torace Rutină & Angio-CT Pulmonar (PE Protocol)
- **Siemens SOMATOM:**
    - Colimare: $128 \times 0.6$ mm, pitch 1.2 (scanare ultra-rapidă sub 2 secunde pentru stop respirator optim).
    - Parametri: CARE kV On (la Angio PE selectează frecvent 80-90 kV pentru amplificarea densității iodului la k-edge de 33.2 keV).
    - Kernele de reconstrucție:
        - Țesut moale / mediastin: I30f (ADMIRE 3), grosime 3.0 mm.
        - Fereastră pulmonară de înaltă rezoluție: I70f / B70f (Sharp), grosime 1.0 - 1.5 mm.
- **GE Revolution:**
    - Helical, pitch 1.375:1, Noise Index 14.0, rotație 0.35 s.
    - Kernele: Standard pentru mediastin; Lung / Bone pentru parenchim pulmonar; ASiR-V 50%.
- **Philips Incisive:**
    - Helical, DRI 16, rotație 0.33 s, iDose4 nivel 4.
    - Kernele: Filter B pentru mediastin, Filter Y (Sharp) pentru parenchim pulmonar.

### 3.3. Neuro / Craniu Nativ (Head Non-Contrast)
- **Siemens Drive / go.Top:**
    - Mod: Secvențial (Axial) pentru eliminarea artefactelor de con/spirală în fosa posterioară, sau spirală dedicată cu pitch redus (0.55).
    - 120 kV fix, Quality Ref. mAs: 320 mAs (supra-tentorial) / 400 mAs (fosa posterioară).
    - Kernele: H31s / J30s (Creier țesut moale), H70h (Fereastră osoasă).
- **GE Ascend / VCT:**
    - Mod: Axial step-and-shoot, 120 kV, 300-350 mA fix sau Smart mA cu NI redus (8.5 - 9.5).
    - Kernele: Soft Tissue (Brain) 5.0 mm fosa posterioară + 5.0 mm vertex; Bone 1.25 mm.
- **Philips Incisive:**
    - Mod: Axial, 120 kV, 320 mAs, iDose4 nivel 4, Filter UB (Ultra Brain) + Filter HD (Bone).

---

## 4. Manualele Oficiale PDF Scanner Defaults (MCB Radiology)

Documentația completă originală a fiecărui scaner din rețeaua Baptist Health / MCB Radiology:

- [:material-file-pdf-box: Siemens SOMATOM Drive VB20 Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/SOMATOM%20Drive%20Protocols%20%28VB20%29.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: Siemens SOMATOM Force VA40 Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/SOMATOM%20Force%20Protocols%20%28VA40%29.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: GE Revolution Ascend Plus Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/GE%20Revolution%20Ascend%20Plus%20Protocols.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: Siemens SOMATOM go.Top Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/SOMATOM%20go.Top%20Protocols.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: GE LightSpeed VCT 64 Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/GE%20LightSpeed%20VCT%2064%20Protocols.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: Philips Incisive 128 CT Exam Protocol List](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/Philips%20Incisive%20128%20Protocols.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: Siemens SOMATOM Definition AS 64 Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/Definition%20AS%2064%20Protocols%20%28VB20%29.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: GE Revolution Maxima 64 Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/GE%20Revolution%20Maxima%2064%20Protocols.pdf){ target="_blank" rel="noopener" }
- [:material-file-pdf-box: GE LightSpeed 16 Reference Protocol Guide](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Default/GE%20LightSpeed%2016%20Protocols.pdf){ target="_blank" rel="noopener" }
"""
    target = ROOT / 'docs' / 'ct' / 'parametri-aparate-scanner-defaults.md'
    target.write_text(content, encoding='utf-8')
    print(f"Generated: {target}")

# ==============================================================================
# 2. GENERATOR PROTOCOALE MEDICINĂ NUCLEARĂ (MN) - 26 PROTOCOALE COMPLETE
# ==============================================================================

NUCS_PROTOCOLS = [
    # 1. Pulmonar - V/Q Scan
    {
        "path": "pulmonar/scintigrafie-ventilatie-perfuzie-vq.md",
        "category": "pulmonar",
        "title": "Scintigrafie de Ventilație și Perfuzie Pulmonară (V/Q Scan)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Lung%20Ventilation%20Xenon.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Lung%20Scintigraphy.pdf",
        "radiofarm": "Xenon-133 gaz (370-740 MBq / 10-20 mCi) sau Tc-99m DTPA aerosol (925-1110 MBq / 25-30 mCi în nebulizator); Tc-99m MAA (Macroagregate de Albumină, 74-148 MBq / 2-4 mCi, 200.000-500.000 particule)",
        "dose_class": "Clasa 2 (2 - 3 mSv)",
        "indications": [
            "Suspiciune de trombembolism pulmonar acut (TEP), în special la pacienți cu contraindicație la substanță de contrast iodată (insuficiență renală severă, alergie la iod)",
            "Suspiciune de TEP la paciente gravide (doză de iradiere fetală mai redusă comparativ cu angio-CT)",
            "Evaluare cantitativă pre-operatorie a funcției pulmonare segmentare înainte de rezecție sau lobectomie",
            "Monitorizarea hipertensiunii pulmonare cronice tromboembolice (CTEPH)"
        ],
        "prep": "Radiografie toracică PA și profil efectuată în ultimele 24 de ore (obligatorie pentru interpretare). Pacient așezat în șezut pentru faza de ventilație.",
        "acquisition": "Faza 1 - Ventilație: Respirație unică, echilibru (3-5 min) și wash-out (evacuare) cu Xenon-133, achiziție posterioară continuă. Faza 2 - Perfuzie: Injectare intravenoasă lentă de Tc-99m MAA în decubit dorsal (asigură distribuție uniformă a particulelor), urmată de achiziții planare în 8 incidențe (Ant, Post, OAD, OAS, OPD, OPS, Profil Drept, Profil Stâng) cu colimator de joasă energie și înaltă rezoluție (LEHR) sau SPECT/CT.",
        "interpretation": "Criterii PIOPED II revizuite: Mismatch V/Q (defecte de perfuzie segmentare/subsegmentare cu ventilație normală și radiografie toracică normală) indică probabilitate înaltă de embolie pulmonară. Match V/Q (defecte concordante) sugerează boală parenchimatoasă (BPOC, pneumonie, atelectazie)."
    },
    # 2. Cardiac - MUGA Scan
    {
        "path": "cardiac/ventriculografie-muga.md",
        "category": "cardiac",
        "title": "Ventriculografie Radionulcidică Sincronizată ECG (MUGA Scan)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/MUGA%20Ventriculography.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/MUGA%20Ventriculography.pdf",
        "radiofarm": "Tc-99m Hematii Marcate Autologe (UltraTag RBC kit, 740-925 MBq / 20-25 mCi i.v.)",
        "dose_class": "Clasa 2 (4 - 6 mSv)",
        "indications": [
            "Evaluarea exactă și reproductibilă a fracției de ejecție a ventriculului stâng (FEVS) înainte și în timpul chimioterapiei cardiotoxice (antracicline: Doxorubicină, Epirubicină; anticorpi monoclonali: Trastuzumab/Herceptin)",
            "Evaluarea cineticii parietale regionale și globale în insuficiența cardiacă și cardiomiopatii",
            "Calculul volumelor ventriculare telesistolice și telediastolice (VTS, VTD)"
        ],
        "prep": "Fără restricții alimentare. Evitarea consumului masiv de cafea/tutun înainte de test. Montare electrozi ECG cu semnal stabil (ritm sinusal regulat; aritmiile severe pot invalida gating-ul).",
        "acquisition": "Marcare hematii in vitro (UltraTag RBC). Pacient în decubit dorsal, gating ECG cu împărțirea ciclului cardiac R-R în 16 sau 32 de cadre temporale. Incidențe statice sincronizate: Oblică Anterioară Stângă (OAS 45° cu înclinare caudală de 10-15° pentru izolarea optimă a septului interventricular), Incidență Anterioară și Profil Stâng. Minim 5-6 milioane de impulsuri/achiziție.",
        "interpretation": "Calculul FEVS prin trasarea zonelor de interes (ROI) telediastolică și telesistolică cu scăderea fondului (background). FEVS normală: 50 - 70%. O scădere a FEVS > 10% față de valoarea inițială sau sub pragul de 50% impune reevaluarea oncologică și oprirea temporară a chimioterapiei."
    },
    # 3. Digestiv - HIDA Scan
    {
        "path": "digestiv/scintigrafie-hepatobiliara-hida.md",
        "category": "digestiv",
        "title": "Scintigrafie Hepatobiliară (HIDA Scan / Colecistoscintigrafie)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/HIDA.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Hepatobiliary%20Scintigraphy.pdf",
        "radiofarm": "Tc-99m Mebrofenin sau Tc-99m Disofenin (185-370 MBq / 5-10 mCi i.v.)",
        "dose_class": "Clasa 2 (2 - 4 mSv)",
        "indications": [
            "Suspiciune de colecistită acută calculoasă sau acalculoasă (obstrucția ductului cistic)",
            "Evaluarea colecistitei cronice și a dischineziei biliare prin calculul fracției de ejecție a vezicii biliare (GBEF cu stimulare CCK / Sincalidă)",
            "Detectarea fistulelor biliare și a extravazării biliare post-colecistectomie sau post-traumă",
            "Diagnosticul atreziei biliare neonatale la nou-născuți cu icter colestatic prelungit",
            "Disfuncția de sfincter Oddi"
        ],
        "prep": "Post alimentar strict minim 4 ore și maxim 24 ore. Dacă pacientul a postit > 24 ore sau este pe nutriție parenterală totală (NPT), se pre-tratează cu Sincalidă (Kinevac) 0.02 mcg/kg cu 30 min înainte de examinare pentru evacuarea bilei vâscoase.",
        "acquisition": "Pacient în decubit dorsal, detector anterior peste hipocondrul drept și epigastru. Achiziție dinamică continuă timp de 60 minute (1 cadru/minut). Dacă vezica biliară nu se vizualizează la 60 minute: opțiunea A - imagini tardive la 2-4 ore; opțiunea B - administrare de Morfină sulfat 0.04 mg/kg i.v. pe 3 minute (induce spasmul sfincterului Oddi) și continuare scanare 30 min. Protocol GBEF: perfuzie lentă de Sincalidă 0.02 mcg/kg pe durata a 30-60 minute cu achiziție concomitentă.",
        "interpretation": "Examen normal: vizualizarea ficatului la 5 min, a căilor biliare și vezicii biliare la 15-30 min, și a duodenului/intestinului subțire în decurs de 60 min. Colecistită acută: persistența absenței vezicii biliare la 4 ore sau post-morfină, cu căi biliare și intestin vizualizate normal. GBEF normal: > 38% la 60 min post-Sincalidă (valori sub 38% indică dischinezie biliară)."
    },
    # 4. Digestiv - Ficat & Splină
    {
        "path": "digestiv/scintigrafie-ficat-splina.md",
        "category": "digestiv",
        "title": "Scintigrafie Ficat-Splină cu Sulf Coloidal (Liver-Spleen Scan)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Liver%20Spleen.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Liver%20and%20Spleen%20Imaging.pdf",
        "radiofarm": "Tc-99m Sulf Coloid (111-296 MBq / 3-8 mCi i.v.)",
        "dose_class": "Clasa 1 - 2 (2 mSv)",
        "indications": [
            "Evaluarea cirozei hepatice, hepatopatiilor cronice și a hipertensiunii portale („colloid shift”)",
            "Diferențierea hiperplaziei nodulare focale (FNH) care conține celule Kupffer de adenomul hepatic",
            "Evaluarea splenomegaliei și a țesutului splenic ectopic / splenoză peritoneală post-traumă sau post-splenectomie",
            "Evaluarea funcțională a sistemului reticuloendotelial"
        ],
        "prep": "Fără pregătire specială. Pacientul nu necesită post alimentar.",
        "acquisition": "Particulele coloidale sunt fagocitate de celulele Kupffer hepatice (80-85%), macrofagele splenice (10-15%) și măduva osoasă (1-5%). Achiziția începe la 15-20 minute post-injectare. Proiecții planare multiple (Ant, Post, OAD, OAS, Profil Drept, Profil Stâng) și SPECT sau SPECT/CT abdominal.",
        "interpretation": "Distribuție omogenă hepato-splenică normală. Ciroză / Hipertensiune portală: scăderea captării hepatice cu devierea coloidului („colloid shift”) masivă către splină și măduva hematopoietică osoasă. FNH: captare egală sau crescută de coloid comparativ cu parenchimul hepatic adiacent."
    },
    # 5. Digestiv - Sângerare Digestivă
    {
        "path": "digestiv/scintigrafie-sangerare-digestiva.md",
        "category": "digestiv",
        "title": "Scintigrafie pentru Detecția Sângerării Digestive Acute (GI Bleed Scan)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/GI%20Bleeding.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/GI%20Bleeding%20Scintigraphy.pdf",
        "radiofarm": "Tc-99m Hematii Marcate Autologe (UltraTag RBC kit, 740-925 MBq / 20-25 mCi i.v.)",
        "dose_class": "Clasa 2 (4 - 6 mSv)",
        "indications": [
            "Localizarea focarului de sângerare digestivă inferioară acută activă sau intermitentă",
            "Sângerări digestive cu debit scăzut (sensibilitate de la 0.05 - 0.1 mL/minut, de 10 ori mai sensibilă decât angiografia clasică)",
            "Trieri înainte de angiografia intervențională sau embolizare selectivă"
        ],
        "prep": "Acces venos periferic stabil. Trusă de marcare in vitro UltraTag RBC. Verificarea stabilității hemodinamice a pacientului.",
        "acquisition": "Faza 1 - Dinamică de flux: 1 cadru la fiecare 1-2 secunde timp de 60 secunde. Faza 2 - Dinamică continuă: 1 cadru la fiecare 60 secunde timp de 60-90 minute. Dacă testul este inițial negativ, se pot relua achiziții la 2-4 ore sau până la 24 ore pentru detecția sângerărilor intermitente.",
        "interpretation": "Examinare pozitivă: apariția unui focar anormal de acumulare a trasorului care crește în intensitate în timp și se deplasează anterograd sau retrograd de-a lungul lumenului anselor intestinale (conformează peristaltismului)."
    },
    # 6. Digestiv - Evacuare Gastrică
    {
        "path": "digestiv/scintigrafie-evacuare-gastrica.md",
        "category": "digestiv",
        "title": "Scintigrafie de Evacuare Gastrică pentru Solide (Gastric Emptying)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Gastric%20Emptying.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Gastric%20Emptying%20Scintigraphy.pdf",
        "radiofarm": "Tc-99m Sulf Coloid (18.5-37 MBq / 0.5-1.0 mCi amestecat și gătit în albuș de ou)",
        "dose_class": "Clasa 1 (< 1 mSv)",
        "indications": [
            "Diagnosticul gastroparezei diabetice sau idiopatice",
            "Investigarea grețurilor cronice, vărsăturilor postprandiale, sațietății precoce și meteorismului",
            "Evaluarea evacuării gastrice rapide (sindrom de dumping post-chirurgie bariatrică)",
            "Monitorizarea răspunsului la medicamente prokinetice (Metoclopramid, Domperidonă, Eritromicină)"
        ],
        "prep": "Post alimentar complet de minim 6 ore. Oprirea medicamentelor prokinetice, opioidelor și anticolinergicelor cu 48-72 ore înainte de test. Glicemie < 200 mg/dL în dimineața examinării (hiperglicemia întârzie evacuarea fiziologică).",
        "acquisition": "Prânz standardizat Tougas/SNMMI: albușul a 2 ouă mari amestecate cu Tc-99m sulf coloid și gătite la microunde, 2 felii de pâine prăjită cu gem de căpșuni (30 g) și 120 mL apă plată (consumate în maxim 10 minute). Imagini statice planare anterioare și posterioare (geometric mean) la minutul 0 (imediat), 1 oră, 2 ore și 4 ore.",
        "interpretation": "Retenție gastrică normală la 4 ore: < 10% (standard de aur). Retenție > 10% la 4 ore confirmă diagnosticul de gastropareză. Valori normale: 1 oră (30-90%), 2 ore (< 60%), 4 ore (< 10%). Evacuare rapidă: retenție < 30% la 1 oră."
    },
    # 7. Renal - MAG3 Renogramă & Lasix
    {
        "path": "urinar/scintigrafie-renala-mag3-diuretic.md",
        "category": "urinar",
        "title": "Scintigrafie Renală Dinamică cu MAG3 și Diuretic (Lasix)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Renal%20MAG3%20Lasix.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Renal%20Diuretic%20Scintigraphy.pdf",
        "radiofarm": "Tc-99m Mertiatide (MAG3, 185-370 MBq / 5-10 mCi i.v.)",
        "dose_class": "Clasa 1 - 2 (1.5 - 3 mSv)",
        "indications": [
            "Diferențierea obstrucției mecanice de joncțiune pielo-ureterală (JPU) de o simplă dilatație hipotonă non-obstructivă a bazinetului",
            "Evaluarea funcției renale diferențiale / separate (Split Renal Function)",
            "Urmărirea rinichiului transplantat (necroză tubulară acută vs. rejet acut vs. obstrucție)",
            "Evaluarea hidronefrozei congenitale la copii"
        ],
        "prep": "Hidratare orală generoasă (500 mL apă cu 30-60 min înainte). Golirea vezicii urinare imediat înainte de începerea examinării (sau cateter vezical la copii).",
        "acquisition": "Pacient în decubit dorsal, detector posterior sub lojele renale. Achiziție dinamică continuă timp de 20-30 minute. Administrare de Furosemid (Lasix, 20-40 mg adult sau 1 mg/kg copil) la minutul 15 sau 20 (protocol F+20) sau concomitent la minutul 0 (protocol F-0).",
        "interpretation": "Curba renografică normală: vârf la 3-5 min urmat de scădere rapidă; clearance Lasix T½ < 10-15 minute. Obstrucție mecanică: acumulare progresivă fără scădere post-Lasix (T½ > 20 minute). Dilatație non-obstructivă: wash-out prompt post-Lasix (T½ < 10 minute)."
    },
    # 8. Renal - DMSA Cortical
    {
        "path": "urinar/scintigrafie-corticala-renala-dmsa.md",
        "category": "urinar",
        "title": "Scintigrafie Renală Corticală cu DMSA",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Renal%20DMSA.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Renal%20Scintigraphy.pdf",
        "radiofarm": "Tc-99m DMSA (Acid Dimercaptosuccinic, 74-185 MBq / 2-5 mCi i.v.)",
        "dose_class": "Clasa 1 (1 - 2 mSv)",
        "indications": [
            "Standardul de aur imagistic pentru detecția cicatricilor renale post-pielonefrită la copii cu reflux vezico-ureteral (RVU)",
            "Diagnosticul pielonefritei acute (defecte focale fotopenice)",
            "Calculul precis al masei corticale funcționale renale relative",
            "Anomalii de poziție/fuziune (rinichi în potcoavă, ectopie renală)"
        ],
        "prep": "Hidratare adecvată. Nu necesită post alimentar.",
        "acquisition": "DMSA se leagă stabil de tubii contorți proximali. Achiziția începe la 2-4 ore post-injectare pentru a permite clearance-ul sangvin. Incidențe planare de înaltă rezoluție (Posterior, OAP Dreaptă și Stângă) sau SPECT / SPECT-CT.",
        "interpretation": "Contur cortical neted și fixare omogenă. Cicatrice renală: defect cortical fotopenic triunghiular sau liniar cu pierdere de volum cortical. Pielonefrită acută: defect fără pierdere de volum."
    },
    # 9. Renal - Captopril Renogram
    {
        "path": "urinar/renograma-hipertensiune-renovasculara.md",
        "category": "urinar",
        "title": "Scintigrafie Renală cu Captopril pentru Hipertensiune Renovasculară",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Renal%20Vascular%20HTN.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Renal%20Captopril%20Scintigraphy.pdf",
        "radiofarm": "Tc-99m MAG3 sau Tc-99m DTPA (185-370 MBq / 5-10 mCi i.v.)",
        "dose_class": "Clasa 1 - 2 (2 mSv)",
        "indications": [
            "Diagnosticul stenozei de arteră renală hemodinamic semnificative cu hipertensiune renovasculară",
            "Prezicerea succesului clinic al revascularizării (angioplastie percutanată cu stent sau chirurgie)",
            "Hipertensiune arterială refractară la tratament triplu sau debut la vârste tinere / avansate"
        ],
        "prep": "Oprirea inhibitorilor ECA (Captopril, Enalapril) cu 48-72 ore înainte și a blocanților de receptori AT1 (sartani) cu 5-7 zile înainte. Hidratare orală bună.",
        "acquisition": "Protocol în 1 sau 2 zile: Administrare Captopril oral (25-50 mg sfărâmat în apă) cu 60 minute înainte de injectarea trasorului. Monitorizarea tensiunii arteriale la fiecare 15 minute. Achiziție dinamică timp de 30 minute identică cu renograma de bază.",
        "interpretation": "Test pozitiv de probabilitate înaltă: scăderea marcată a funcției renale relative a rinichiului afectat (> 10%) și/sau întârzierea marcată a timpului până la vârful de captare (Tmax) post-Captopril, comparativ cu renograma de bază fără inhibitor."
    },
    # 10. Osos - Whole Body
    {
        "path": "osos/scintigrafie-osoasa-whole-body.md",
        "category": "osos",
        "title": "Scintigrafie Osoasă Corp Întreg (Bone Scan Whole Body)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Bone%20Scan%20Whole%20Body.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Bone%20Scintigraphy.pdf",
        "radiofarm": "Tc-99m MDP (Metilen Difosfonat) sau Tc-99m HDP (740-1110 MBq / 20-30 mCi i.v.)",
        "dose_class": "Clasa 2 (3 - 4 mSv)",
        "indications": [
            "Depistarea și bilanțul metastazelor osoase osteoblastice (cancer de prostată, sân, plămân)",
            "Evaluarea durerilor osoase neelucidate prin radiografie convențională",
            "Boala Paget a osului (cartografierea extensiei scheletice și monitorizarea răspunsului terapeutic)",
            "Fracturi de stres sau de insuficiență oculte radiologic",
            "Necroză avasculară de cap femural"
        ],
        "prep": "Hidratare abundentă (1-1.5 litri apă) în intervalul de 2-4 ore dintre injectare și scanare. Golirea completă a vezicii urinare imediat înainte de examinare.",
        "acquisition": "Scanare corp întreg antero-posterioară la 2.5 - 4 ore post-injectare. Viteză scanare 12-15 cm/minut. Incidențe statice suplimentare pentru craniu, bazin, torace sau extremități la nevoie.",
        "interpretation": "Fixare simetrică normală a scheletului axial și apendicular. Metastaze osoase: focare multiple asimetrice hipercaptante distribuite predominant în scheletul axial (coloană, coaste, bazin)."
    },
    # 11. Osos - Trei Faze
    {
        "path": "osos/scintigrafie-osoasa-trei-faze.md",
        "category": "osos",
        "title": "Scintigrafie Osoasă în Trei Faze (Three-Phase Bone Scan)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Bone%20Scan%20Three%20Phase.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Bone%20Scintigraphy.pdf",
        "radiofarm": "Tc-99m MDP sau HDP (740-1110 MBq / 20-30 mCi i.v.)",
        "dose_class": "Clasa 2 (3 - 4 mSv)",
        "indications": [
            "Diagnosticul diferențial între osteomielită acută și infecție de părți moi / celulită",
            "Evaluarea protezelor articulare dureroase (șold, genunchi): decimentare aseptică vs. infecție",
            "Sindrom dureros regional complex (CRPS / distrofie simpatică reflexă)",
            "Fracturi oculte recente de scafoid sau col femural"
        ],
        "prep": "Hidratare bună. Fără post alimentar.",
        "acquisition": "Faza 1 (Angiografică / Perfuze): 1-2 sec/cadru timp de 60 secunde imediat post-bolus i.v. Faza 2 (Blood Pool / Echilibru tisular): imagini statice la 5-10 minute. Faza 3 (Osoasă tardivă): imagini la 2.5 - 4 ore post-injectare.",
        "interpretation": "Osteomielită acută: hipercaptare focală intensă în toate cele 3 faze. Celulită: pozitivă în fazele 1 și 2, difuză sau absentă în faza 3. Decimentare proteză: hipercaptare la capetele protezei fără focar septic cald difuz."
    },
    # 12. Osos - SPECT / SPECT-CT
    {
        "path": "osos/scintigrafie-osoasa-spect.md",
        "category": "osos",
        "title": "Scintigrafie Osoasă SPECT și SPECT/CT Focalizat",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Bone%20Scan%20SPECT.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Bone%20Scintigraphy.pdf",
        "radiofarm": "Tc-99m MDP / HDP (740-1110 MBq / 20-30 mCi i.v.)",
        "dose_class": "Clasa 2 (4 - 5 mSv)",
        "indications": [
            "Spondiloliză și leziuni de stres ale pars interarticularis la tineri sportivi cu lombalgie",
            "Localizarea exactă a leziunilor articulare complexe în picior, gleznă și încheietura mâinii",
            "Diferențierea leziunilor degenerative de metastaze pe corpii vertebrali sau arcurile posterioare"
        ],
        "prep": "Hidratare adecvată și evacuare vezicală.",
        "acquisition": "Achiziție tomografică SPECT (rotație 360°, 60-128 proiecții) combinată cu CT cu doză joasă pentru corecție de atenuare și fuziune anatomică milimetrică.",
        "interpretation": "Rezoluție de contrast superioară scintigrafiei planare. Permite separarea captării din fațetele articulare de pedicul sau corpul vertebral."
    },
    # 13. Osos - NaF PET
    {
        "path": "osos/pet-ct-os-naf.md",
        "category": "osos",
        "title": "PET-CT Osos cu Fluorură de Sodiu (18F-NaF Bone PET/CT)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/PET%20NaF.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Sodium%20Fluoride%20PET.pdf",
        "radiofarm": "Fluor-18 Fluorură de Sodiu (18F-NaF, 185-370 MBq / 5-10 mCi i.v.)",
        "dose_class": "Clasa 2 (4 - 6 mSv)",
        "indications": [
            "Cea mai sensibilă metodă imagistică pentru detectarea metastazelor osoase în cancerul de prostată și cancerul mamar",
            "Evaluarea metastazelor atât osteoblastice cât și osteolitice timpurii",
            "Evaluarea durerilor scheletice la pacienți cu scintigrafie Tc-99m echivocă"
        ],
        "prep": "Hidratare generoasă cu apă. Nu necesită post alimentar (spre deosebire de 18F-FDG).",
        "acquisition": "Timp de repaus post-injectare: 45-60 minute. Scanare hibridă PET-CT vertex-picioare (sau trunchi) cu achiziție 3D PET (1-2 min/pat) și CT cu doză joasă.",
        "interpretation": "Rezoluție spațială de 4-5 mm (mult superioară camerei gama). Clearance sangvin rapid și captare scheletică dublă comparativ cu fosfonații clasici de Tc-99m."
    },
    # 14. Endocrin - Tiroidă Uptake & Scan
    {
        "path": "endocrin/scintigrafie-captare-tiroidiana.md",
        "category": "endocrin",
        "title": "Scintigrafie și Captare Tiroidiană (Iod-123 & Tc-99m)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Thyroid%20Imaging%20Uptake.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Thyroid%20Scintigraphy%20&%20Uptake.pdf",
        "radiofarm": "Iod-123 sodiu oral (3.7-14.8 MBq / 100-400 uCi capsule) sau Tc-99m Pertehnetat (74-185 MBq / 2-5 mCi i.v.)",
        "dose_class": "Clasa 1 (1 - 2 mSv)",
        "indications": [
            "Diagnosticul diferențial al hipertiroidismului: boala Basedow-Graves vs. gușă multinodulară toxică (Plummer) vs. adenom toxic autonom vs. tiroidită subacută",
            "Caracterizarea funcțională a nodulilor tiroidieni: nodul „cald” (hipercaptant, benign) vs. nodul „rece” (hipocaptant, risc de malignitate ce necesită puncție FNB)",
            "Localizarea țesutului tiroidian ectopic (tiroidă linguală, chist tireoglos, struma ovarii)"
        ],
        "prep": "Oprirea alimentelor bogate în iod și a suplimentelor cu iod/alge cu 2 săptămâni înainte. Fără substanțe de contrast CT iodate în ultimele 4-6 săptămâni. Oprirea medicamentelor antitiroidiene (Tiamazol) cu 3-5 zile înainte, iar a Levotiroxinei (T4) cu 4-6 săptămâni înainte.",
        "acquisition": "Captare cu sondă de scintilație la 4-6 ore și 24 ore post-ingestie I-123. Imagini planare cu colimator pinhole (incidențe anterioară, OAD, OAS). Pentru Tc-99m: imagini la 15-20 min post-i.v.",
        "interpretation": "Captare normală la 24 ore: 10 - 30%. Boala Graves: captare difuză crescută (40-80%) cu lob piramidal vizibil. Adenom toxic: nodul hipercaptant unic cu supresia restului parenchimului. Tiroidită subacută: captare extrem de scăzută (< 2%)."
    },
    # 15. Endocrin - Tiroidă I-131 Whole Body
    {
        "path": "endocrin/scintigrafie-whole-body-i131.md",
        "category": "endocrin",
        "title": "Scintigrafie Whole-Body cu Iod-131 în Cancerul Tiroidian Diferențiat",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Thyroid%20I131.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Thyroid%20Cancer%20I131.pdf",
        "radiofarm": "Iod-131 sodiu oral (74-185 MBq / 2-5 mCi diagnostic; sau post-terapeutic 1110-7400 MBq / 30-200 mCi)",
        "dose_class": "Terapeutic / Diagnostic",
        "indications": [
            "Bilanțul post-tiroidectomie totală în cancerul tiroidian diferențiat (papilar sau folicular)",
            "Detectarea țesutului tiroidian restant în loja cervicală înainte de ablația cu radioiod",
            "Depistarea metastazelor la distanță (ganglionare, pulmonare miliare, osoase) la pacienți cu tiroglobulină serică detectabilă"
        ],
        "prep": "Stimulare TSH obligatorie (TSH > 30 uIU/mL): fie prin sevraj hormonal de levotiroxină 4 săptămâni, fie prin administrare de TSH uman recombinant (Thyrogen). Dietă strictă hipoiodată timp de 14 zile.",
        "acquisition": "Scanare corp întreg antero-posterioară la 48-72 ore post-ingestie (diagnostic) sau la 5-7 zile post-terapeutic. Colimator de înaltă energie (HEGP), fotopic la 364 keV.",
        "interpretation": "Fixare normală fiziologică în mucoasa nazală, glande salivare, stomac, tract urinar. Orice focar focal în afara acestor arii reprezintă metastază sau rest tisular tiroidian."
    },
    # 16. Endocrin - Paratiroidă Sestamibi
    {
        "path": "endocrin/scintigrafie-paratiroida-sestamibi.md",
        "category": "endocrin",
        "title": "Scintigrafie Paratiroidiană cu Tc-99m Sestamibi și SPECT/CT",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Parathyroid.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Parathyroid%20Scintigraphy.pdf",
        "radiofarm": "Tc-99m Sestamibi (MIBI, 740-925 MBq / 20-25 mCi i.v.)",
        "dose_class": "Clasa 2 (4 - 6 mSv)",
        "indications": [
            "Localizarea pre-operatorie a adenomului paratiroidian solitar sau multiplu în hiperparatiroidismul primar",
            "Ghidarea chirurgiei paratiroidiene minim invazive (MIP)",
            "Localizarea adenoamelor paratiroidiene ectopice (mediastin antero-superior, șanț traheoesofagian, retrofaringian)",
            "Recidivă de hiperparatiroidism post-chirurgical"
        ],
        "prep": "Fără pregătire specială. Se recomandă corelarea cu ecografia cervicală de înaltă rezoluție.",
        "acquisition": "Protocol dublă fază (wash-out): Sestamibi se captează inițial atât în tiroidă cât și în paratiroidele bogate în mitocondrii; tiroida elimină trasorul mult mai rapid. Imagini precoce la 10-15 min și imagini tardive la 1.5 - 2.5 ore post-injectare. Achiziție hibridă SPECT/CT cervical și mediastinal la faza tardivă.",
        "interpretation": "Adenom paratiroidian: focar persistent de retenție crescută a trasorului la faza tardivă după evacuarea activității din parenchimul tiroidian normal. SPECT/CT oferă localizarea spațială anatomică precisă pentru abordul chirurgical minim invaziv."
    },
    # 17. Neuro - Moarte Cerebrală
    {
        "path": "neuro/scintigrafie-perfuzie-cerebrala-moarte-cerebrala.md",
        "category": "neuro",
        "title": "Scintigrafie de Perfuzie Cerebrală pentru Confirmarea Morții Cerebrale",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Brain%20Death.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Brain%20Death%20Scintigraphy.pdf",
        "radiofarm": "Tc-99m HMPAO (Exametazimă) sau Tc-99m ECD (Bicisat) (740-1110 MBq / 20-30 mCi i.v.)",
        "dose_class": "Clasa 2 (4 - 5 mSv)",
        "indications": [
            "Test paraclinic instrumental de confirmare a morții cerebrale conform legislației de transplant",
            "Situații clinice în care examenul neurologic nu poate fi evaluat concludent (hipotermie terapeutică, comă barbiturică indusă, leziuni faciale majore)"
        ],
        "prep": "Trusă radiofarmaceutică preparată proaspăt cu verificare a purității radiochimice > 90%. Acces venos periferic larg permeabil.",
        "acquisition": "Faza 1 (Angiografie de flux): 1 cadru/secundă timp de 60 secunde anterior cap/gât. Faza 2 (Statică parenchimatoasă): imagini statice la 15-30 minute în proiecții anterioară, posterioară și laterale.",
        "interpretation": "Moarte cerebrală: absența completă a fluxului arterial intracranian pe arterele carotide interne și absența fixării parenchimatoase în emisfere și trunchi cerebral (semnul „hollow skull” / craniu vid). Prezența fluxului în carotida externă cu persistarea captării faciale / nazale (semnul „hot nose”)."
    },
    # 18. Neuro - Cisternografie LCR
    {
        "path": "neuro/cisternografie-fuga-lcr.md",
        "category": "neuro",
        "title": "Cisternografie Radioizotopică pentru Fistulă de Lichid Cefalorahidian (CSF Leak)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Cisternogram%20CSF%20Leak.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Cisternography.pdf",
        "radiofarm": "Indiu-111 DTPA (18.5-37 MBq / 0.5-1.0 mCi injectat intratecal prin puncție lombară)",
        "dose_class": "Clasa 2 (2 - 3 mSv)",
        "indications": [
            "Localizarea și confirmarea fistulelor de lichid cefalorahidian (rinolicvoree sau otolicvoree post-traumatică sau post-chirurgicală)",
            "Diagnosticul hidrocefaliei cu presiune normală (NPH)",
            "Evaluarea permeabilității șunturilor ventriculo-peritoneale"
        ],
        "prep": "Puncție lombară sterilă L3-L4 efectuată de medic. Plasare de tampoane nazale/auriculare numerotate pentru contorizare radioactivă comparativă cu plasma.",
        "acquisition": "Injectare intratecală lentă. Imagini statice ale coloanei și capului la 4-6 ore, 24 ore și 48 ore post-injectare. Măsurarea radioactivității tampoanelor în spectrometru gama.",
        "interpretation": "Fistulă LCR activă: apariția unui focar anormal de radiotrasor în cavitatea nazală, sinusuri paranazale sau conduct auditiv extern, confirmat de un raport radioactivitate tampon/ser > 2-3:1."
    },
    # 19. Neuro - PET FDG Brain
    {
        "path": "neuro/pet-ct-cerebral-fdg.md",
        "category": "neuro",
        "title": "PET-CT Cerebral cu 18F-FDG în Neurologie (Brain Metabolism)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/PET%20FDG%20Brain.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/FDG%20PET%20Brain.pdf",
        "radiofarm": "Fluor-18 Fluordeoxiglucoză (18F-FDG, 185-370 MBq / 5-10 mCi i.v.)",
        "dose_class": "Clasa 2 (5 - 7 mSv)",
        "indications": [
            "Localizarea focarului epileptogen interictal în epilepsia refractară farmacologic în vederea rezecției chirurgicale",
            "Diferențierea bolilor neurodegenerative: Demență Alzheimer (hipometabolism temporo-parietal posterior și cingular posterior) vs. Demență Fronto-Temporală vs. Demență cu Corpi Lewy",
            "Diferențierea recidivei tumorale cerebrale de radionecroza post-radioterapie"
        ],
        "prep": "Post alimentar strict minim 4-6 ore. Glicemie < 150 mg/dL. Cameră de injectare liniștită, întunecată, fără stimuli vizuali sau auditivi timp de 30-45 minute post-injectare.",
        "acquisition": "Timp de biodistribuție: 45 minute. Scanare dedicată a extremității cefalice (10-15 minute PET 3D de înaltă rezoluție + CT pentru corecție de atenuare).",
        "interpretation": "Cartografiere metabolică a consumului regional de glucoză. Focar epileptogen interictal: zonă focală de hipometabolism. Boala Alzheimer: hipometabolism bilateral simetric/asimetric în cortexul temporo-parietal și precuneus."
    },
    # 20. Infectie - Ceretec WBC
    {
        "path": "infectie/scintigrafie-leucocite-marcate-ceretec.md",
        "category": "infectie",
        "title": "Scintigrafie cu Leucocite Marcate cu Tc-99m HMPAO (Ceretec WBC)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/WBC%20Ceretec.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/WBC%20Scintigraphy.pdf",
        "radiofarm": "Leucocite autologe marcate cu Tc-99m HMPAO (Ceretec, 370-740 MBq / 10-20 mCi i.v.)",
        "dose_class": "Clasa 2 (5 - 7 mSv)",
        "indications": [
            "Infecții musculoscheletale la extremități (picior diabetic neuropat cu suspiciune de osteomielită)",
            "Evaluarea extinderii și activității bolilor inflamatorii intestinale (boala Crohn, colită ulcerativă)",
            "Infecții acute de proteză articulară sau de material de osteosinteză",
            "Infecții de grefon vascular periferic"
        ],
        "prep": "Recoltare a 50-60 mL sânge heparinat autolog pentru separare leucocitară în laborator radiofarmaceutic (durată 2-3 ore). Număr leucocite pacient > 3.000/uL. Reinjectare sigură a celulelor pacientului.",
        "acquisition": "Imagini timpurii la 30-60 min (obligatorii pentru patologia abdominală înainte de excreția biliară nespecifică) și imagini tardive la 3-4 ore. SPECT/CT focalizat pe regiunea afectată.",
        "interpretation": "Focar de acumulare crescută a leucocitelor care crește în timp confirmă prezența procesului infecțios activ bacterian cu neutrofile."
    },
    # 21. Infectie - Indium-111 WBC
    {
        "path": "infectie/scintigrafie-leucocite-marcate-indium111.md",
        "category": "infectie",
        "title": "Scintigrafie cu Leucocite Marcate cu Indiu-111 Oxină (In-111 WBC)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/WBC%20Indium.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/WBC%20Scintigraphy.pdf",
        "radiofarm": "Leucocite autologe marcate cu In-111 Oxină (11-18.5 MBq / 300-500 uCi reinjectate i.v.)",
        "dose_class": "Clasa 3 (7 - 10 mSv)",
        "indications": [
            "Febra de origine necunoscută (FUO) și localizarea abceselor oculte intra-abdominale sau retroperitoneale",
            "Osteomielită cronică sau suprapusă pe schelet modificat structural",
            "Infecții de proteză valvulară cardiacă sau de dispozitive cardiace (stimulatoare, defibrilatoare)",
            "Avantaj major: absența excreției fiziologice gastrointestinale la 24 ore (contrast superior în abdomen față de Tc-99m Ceretec)"
        ],
        "prep": "Separare celulară autologă a sângelui pacientului în laborator de radiofarmacie. Reinjectare lentă strict intravenoasă.",
        "acquisition": "Colimator de energie medie (MEGP), fotopicuri la 171 keV și 245 keV. Achiziții planare la 18-24 ore post-injectare (opțional imagini la 4 ore) + SPECT/CT.",
        "interpretation": "Focar focal patologic asimetric de hiperfixare a leucocitelor la 24 ore indică focar infecțios activ."
    },
    # 22. Oncologie - PET FDG Body
    {
        "path": "oncologie/pet-ct-fdg-oncologie.md",
        "category": "oncologie",
        "title": "PET-CT cu 18F-FDG în Oncologie (Whole Body Tumor Imaging)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/PET%20FDG%20Body.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/FDG%20PET%20for%20Tumor%20Imaging.pdf",
        "radiofarm": "Fluor-18 Fluordeoxiglucoză (18F-FDG, 185-370 MBq / 5-10 mCi i.v. calculat la 3.7-5.2 MBq/kg)",
        "dose_class": "Clasa 3 (7 - 12 mSv)",
        "indications": [
            "Stadializarea inițială, restadializarea și evaluarea eficienței terapeutice (chimioterapie, radioterapie, imunoterapie) în limfoame, cancer bronhopulmonar, cancer colo-rectal, melanom, cancere ORL, esofagiene etc.",
            "Detectarea recidivelor tumorale la pacienți cu markeri tumorali serici în creștere și imagistică convențională negativă",
            "Caracterizarea nodulului pulmonar solitar > 8 mm"
        ],
        "prep": "Post alimentar strict de minim 6 ore. Hidratare cu apă plată (fără zahăr). Glicemie < 150-180 mg/dL înainte de injectare. Repaus fizic absolut și mediu cald timp de 60 min post-injectare pentru prevenirea captării în mușchi și grăsimea brună.",
        "acquisition": "Timp de biodistribuție: 60 ± 10 minute în cameră de liniște. Scanare hibridă PET-CT de la vertex până la jumătatea coapselor (sau din creștet până în tălpi pentru melanom), combinând CT cu doză joasă pentru corecție de atenuare și localizare anatomică cu achiziție 3D PET (1.5 - 3 min/pat).",
        "interpretation": "Calculul valorii standardizate a captării (SUVmax). Zone de hipermetabolism glucidic suspecte oncologic corelate cu leziunile anatomice CT. Criterii RECIST / PERCIST pentru răspuns terapeutic."
    },
    # 23. Oncologie - Octreotide Scan
    {
        "path": "oncologie/scintigrafie-receptori-somatostatina-octreotid.md",
        "category": "oncologie",
        "title": "Scintigrafie a Receptorilor de Somatostatină cu In-111 Pentetreotid (OctreoScan)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Octreotide.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Somatostatin%20Receptor%20Scintigraphy.pdf",
        "radiofarm": "Indiu-111 Pentetreotide (OctreoScan, 111-222 MBq / 3-6 mCi i.v.)",
        "dose_class": "Clasa 3 (8 - 10 mSv)",
        "indications": [
            "Diagnosticul, stadializarea și monitorizarea tumorilor neuroendocrine (NET) gastro-entero-pancreatice (carcinoid, gastrinom, insulinom, glucagonom)",
            "Localizarea tumorilor primitive și a metastazelor hepatice sau ganglionare cu receptori de somatostatină (SSTR2 și SSTR5)",
            "Selecția candidaților eligibili pentru terapia cu radioliganzii peptidici Lu-177 Dotatate (PRRT)"
        ],
        "prep": "Hidratare bună. Oprirea analogilor de somatostatină cu acțiune scurtă (Octreotid subcutanat) cu 24-48 ore înainte, iar a formelor retard (LAR) cu 3-4 săptămâni înainte (dacă este tolerat clinic). Laxativ ușor în seara anterioară scanării de 24 ore pentru clearance-ul intestinal.",
        "acquisition": "Imagini planare la 4 ore și 24 ore post-injectare (opțional 48 ore). Colimator MEGP. SPECT sau SPECT/CT obligatoriu pentru abdomen și pelvis la 24 ore.",
        "interpretation": "Fixare intensă în tumorile neuroendocrine bogate în receptori de somatostatină. Evaluare Krenning score (grad 1-4) pentru stabilirea indicației de radioterapie PRRT."
    },
    # 24. Oncologie - MIBG Scan
    {
        "path": "oncologie/scintigrafie-mibg.md",
        "category": "oncologie",
        "title": "Scintigrafie cu I-123 / I-131 MIBG (Metaiodobenzilguanidină)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/MIBG.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/MIBG%20Scintigraphy.pdf",
        "radiofarm": "Iod-123 MIBG (111-370 MBq / 3-10 mCi i.v.) sau Iod-131 MIBG (18.5-37 MBq / 0.5-1.0 mCi)",
        "dose_class": "Clasa 2 - 3 (5 - 8 mSv)",
        "indications": [
            "Stadializarea, evaluarea răspunsului și depistarea recidivelor în neuroblastom la sugari și copii",
            "Localizarea feocromocitoamelor suprarenaliene și a paraganglioamelor extra-adrenale",
            "Evaluarea carcinomului medular tiroidian",
            "Evaluarea pacienților înainte de radioterapia metabolică cu doze mari de I-131 MIBG"
        ],
        "prep": "Blocarea tiroidei cu soluție Lugol sau iodură de potasiu (SSKI) începută cu 24-48 ore înainte și continuată 3-5 zile. Oprirea medicamentelor interferente: simpatomimetice, decongestionante, antidepresive triciclice, labetalol, rezerpină cu 1-2 săptămâni înainte.",
        "acquisition": "Injectare intravenoasă lentă pe durata a 2-5 minute. Achiziții planare corp întreg la 24 ore (și 48 ore pentru I-131) post-injectare + SPECT/CT toraco-abdominal.",
        "interpretation": "Localizarea focarelor de hiperfixare pe lanțurile simpatice, suprarenale sau metastaze scheletice/ganglionare."
    },
    # 25. Oncologie - SLND Breast
    {
        "path": "oncologie/limfoscintigrafie-ganglion-santinela-mamar.md",
        "category": "oncologie",
        "title": "Limfoscintigrafie pentru Detecția Ganglionului Santinelă Mamar (SLND)",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Lympho%20Breast.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Lymphoscintigraphy%20Breast.pdf",
        "radiofarm": "Tc-99m Tilmanocept (Lymphoseek) sau Tc-99m Nanocoloid de Albumină filtrat (18.5-37 MBq / 0.5-1.0 mCi)",
        "dose_class": "Clasa 1 (< 1 mSv)",
        "indications": [
            "Identificarea primului releu ganglionar limfatic (ganglion santinelă) la paciente cu cancer mamar stadiul incipient (T1-T2, N0 clinic)",
            "Ghidarea biopsiei minim invazive intraoperatorii pentru evitarea limfadenectomiei axilare complete inutile"
        ],
        "prep": "Fără pregătire specială. Procedură efectuată în dimineața intervenției sau în după-amiaza precedentă (protocol 2 zile).",
        "acquisition": "Injectare intradermică periareolară sau peritumorală subareolară în 2-4 cadrane (volum 0.1-0.2 mL/depozit) urmată de masaj blând 3-5 min. Imagini planare anterioare și oblice la 15-45 min + reperaj cutanat cu marker radioactiv și cerneală chirurgicală.",
        "interpretation": "Migrare rapidă pe vasele limfatice axilare către 1-2 ganglioni santinelă. Detectare acustică intraoperatorie cu gamma-probe chirurgical."
    },
    # 26. Oncologie - Sentinel Node Melanom
    {
        "path": "oncologie/limfoscintigrafie-melanom.md",
        "category": "oncologie",
        "title": "Limfoscintigrafie Cutanată pentru Ganglionul Santinelă în Melanom Malign",
        "source_pdf": "https://ref.mcbradiology.com/Nucs/Protocols/Lympho%20Skin.pdf",
        "guideline_pdf": "https://ref.mcbradiology.com/Nucs/Practice%20Guidelines/Lymphoscintigraphy%20Melanoma.pdf",
        "radiofarm": "Tc-99m Tilmanocept (Lymphoseek) sau Nanocoloid de Albumină filtrat (18.5-37 MBq / 0.5-1.0 mCi)",
        "dose_class": "Clasa 1 (< 1 mSv)",
        "indications": [
            "Identificarea bazinului limfatic de drenaj și a primului releu ganglionar (ganglion santinelă) în melanomul malign cu grosime Breslow > 0.8 mm sau cu factori de risc histologic (ulcerație, mitoze)",
            "Determinarea drenajului limfatic imprevizibil (melanoame de trunchi, cap și gât ce pot drena în multiple bazine limfatice)",
            "Reperaj cutanat preoperator pentru biopsie țintită"
        ],
        "prep": "Fără pregătire specială. Se realizează în ziua intervenției chirurgicale.",
        "acquisition": "Injectare strict intradermică a 4 micro-depozite (0.1 mL fiecare) în jurul leziunii primare sau cicatricii de biopsie. Achiziție dinamică imediată la camera gama timp de 15-30 minute pentru vizualizarea canalelor limfatice, urmată de imagini statice și marcare cutanată a ganglionilor calzi.",
        "interpretation": "Identificarea precisă a tuturor ganglionilor limfatici care primesc drenaj direct din leziune și ghidarea exciziei cu sondă gamma intraoperatorie."
    }
]

def generate_nucs_files():
    mn_dir = ROOT / 'docs' / 'mn'
    ensure_dir(mn_dir)
    
    # 1. Generate main .pages
    pages_content = """nav:
  - index.md
  - Pulmonar: pulmonar
  - Cardiac: cardiac
  - Digestiv: digestiv
  - Renal & Urinar: urinar
  - Sistem Osos: osos
  - Endocrin: endocrin
  - Neuro: neuro
  - Infecții: infectie
  - Oncologie: oncologie
"""
    (mn_dir / '.pages').write_text(pages_content, encoding='utf-8')

    # 2. Generate subdirectories and protocols
    for p in NUCS_PROTOCOLS:
        target_path = mn_dir / p['path']
        ensure_dir(target_path.parent)
        
        slug = Path(p['path']).stem
        inds_yaml = "\n".join(f"  - {json.dumps(ind, ensure_ascii=False)}" for ind in p['indications'])
        
        md_content = f"""---
title: {p['title']}
author: {AUTHOR_MCB}
category: {p['category']}
modality: mn
slug: {slug}
clinical_indications:
{inds_yaml}
last_updated: '{DATE_NOW}'
sources:
  - title: MCB Radiology Protocol Manual
    url: {p['source_pdf']}
    relationship: authoritative_institutional_reference
  - title: Practice Guideline Reference
    url: {p['guideline_pdf']}
    relationship: clinical_practice_guideline
---

# ☢️ {p['title']}

Protocol oficial de **Medicină Nucleară & Radiologie Nucleară** integrat conform standardelor de calitate și radiofarmacie clinică ale **MCB Radiology** și ghidurilor internaționale **SNMMI / EANM**.

<div class="iris-official-banner" style="margin-bottom: 24px; background: linear-gradient(135deg, #4c1d95 0%, #312e81 100%); color: #ffffff; padding: 18px 24px; border-radius: 10px; border: 1px solid rgba(167, 139, 250, 0.3);">
  <div class="iris-official-badge" style="background: rgba(167, 139, 250, 0.2); color: #c4b5fd; padding: 4px 10px; border-radius: 4px; display: inline-block; font-weight: 700; font-size: 0.82rem; margin-bottom: 8px;">
    ☢️ MEDICINĂ NUCLEARĂ &bull; {p['dose_class']}
  </div>
  <p class="iris-official-desc" style="margin-bottom: 12px !important; color: #ede9fe; font-size: 0.95rem; line-height: 1.5;">
    Procedură diagnostică funcțională și moleculară. Evaluarea fiziologică in vivo a metabolismului tisular utilizând radiotrasori specifici de emisie gama sau pozitroni (PET/SPECT).
  </p>
  <div style="display: flex; gap: 16px; flex-wrap: wrap;">
    <a href="{p['source_pdf']}" target="_blank" rel="noopener" style="font-weight: 600; color: #a78bfa; text-decoration: none;">
      [:material-file-pdf-box: Protocol Tehnic MCB (PDF)] ➔
    </a>
    <a href="{p['guideline_pdf']}" target="_blank" rel="noopener" style="font-weight: 600; color: #c4b5fd; text-decoration: none;">
      [:material-file-pdf-box: Ghid de Practică Clinică (PDF)] ➔
    </a>
  </div>
</div>

---

## 1. Indicații Clinice Majore
{"".join(f"- {ind}\n" for ind in p['indications'])}
---

## 2. Radiofarmaceutic, Doză & Radioprotecție
- **Trasor administrat:** `{p['radiofarm']}`
- **Clasă de iradiere IRIS:** **{p['dose_class']}**
- **Cale de administrare:** Intravenoasă, inhalatorie sau orală conform protocolului specific.
- **Măsuri de radioprotecție:** Hidratare abundentă post-procedură pentru favorizarea eliminării urinare a radiofarmaceuticului nefixat. Evitarea contactului prelungit cu femei gravide și copii mici timp de 24 ore.

---

## 3. Pregătirea Pacientului
{p['prep']}

---

## 4. Protocol Tehnic de Achiziție Imagistică
{p['acquisition']}

---

## 5. Criterii de Interpretare Diagnostică
{p['interpretation']}

---

## 6. Documente și Ghiduri Asociate
- [:material-file-pdf-box: Protocol Original MCB Radiology]({p['source_pdf']}){{ target="_blank" rel="noopener" }}
- [:material-file-pdf-box: Ghid de Practică Medicală SNMMI / EANM]({p['guideline_pdf']}){{ target="_blank" rel="noopener" }}
- [:material-arrow-left: Înapoi la Indexul de Medicină Nucleară](../index.md)
"""
        target_path.write_text(md_content, encoding='utf-8')
        print(f"Generated MN Protocol: {target_path}")

    # 3. Generate category index files
    generate_mn_category_indexes(mn_dir)

    # 4. Generate docs/mn/index.md
    generate_mn_index(mn_dir)

def generate_mn_category_indexes(mn_dir: Path):
    CATEGORY_INFO = {
        "pulmonar": ("Protocoale Medicină Nucleară — Pulmonar & Torace", "Scintigrafie de ventilație și perfuzie (V/Q Scan) pentru excluderea trombembolismului pulmonar (TEP) la paciente gravide sau pacienți cu insuficiență renală."),
        "cardiac": ("Protocoale Medicină Nucleară — Cardiologie (MUGA)", "Ventriculografie sincronizată ECG (MUGA Scan) pentru calculul exact al fracției de ejecție și monitorizarea cardiotoxicității chimioterapice."),
        "digestiv": ("Protocoale Medicină Nucleară — Gastroenterologie & Hepatobiliar", "Colecistoscintigrafie HIDA cu stimulare Sincalidă/morfină, evacuare gastrică solidă, sângerare digestivă activă și scintigrafie ficat-splină."),
        "urinar": ("Protocoale Medicină Nucleară — Nefrologie & Urologie", "Renogramă dinamică MAG3 cu diuretic Lasix, evaluarea stenozei de arteră renală prin test Captopril și scintigrafie renală corticală DMSA pentru cicatrici pielonefritice."),
        "osos": ("Protocoale Medicină Nucleară — Sistem Osos & Schelet", "Scintigrafie osoasă Whole Body, scintigrafie în trei faze pentru osteomielită vs celulită, achiziție SPECT/CT focalizată și PET-CT osos cu NaF-18."),
        "endocrin": ("Protocoale Medicină Nucleară — Endocrinologie", "Scintigrafie și captare tiroidiană cu I-123 / Tc-99m, evaluare Whole Body I-131 pentru cancer tiroidian și localizare adenom paratiroidian Sestamibi SPECT/CT."),
        "neuro": ("Protocoale Medicină Nucleară — Neurologie & Neuroimagistică", "Perfuzie cerebrală pentru confirmarea morții cerebrale, cisternografie radioizotopică pentru fugă de LCR și PET-CT cerebral cu 18F-FDG."),
        "infectie": ("Protocoale Medicină Nucleară — Infecții & Inflamație Ocultă", "Scintigrafie cu leucocite marcate autologe Tc-99m Ceretec și Indiu-111 Oxină pentru picior diabetic, infecții de proteză și febră de etiologie necunoscută."),
        "oncologie": ("Protocoale Medicină Nucleară — Oncologie & PET-CT", "PET-CT oncologic Whole Body cu 18F-FDG, evaluarea tumorilor neuroendocrine cu Octreotid (OctreoScan), scintigrafie MIBG și limfoscintigrafie ganglion santinelă (SLND) sân și melanom."),
    }
    for cat, (title, desc) in CATEGORY_INFO.items():
        cat_dir = mn_dir / cat
        ensure_dir(cat_dir)
        cat_protos = [p for p in NUCS_PROTOCOLS if p['category'] == cat]
        rows = []
        for p in cat_protos:
            filename = Path(p['path']).name
            rows.append(f"| [{p['title']}]({filename}) | `{p['radiofarm'].split('(')[0].strip()}` | **{p['dose_class']}** | [:material-file-pdf-box: PDF MCB]({p['source_pdf']}){{ target='_blank' rel='noopener' }} |")
        
        table_rows = "\n".join(rows)
        cat_content = f"""---
title: {title}
---

# {title}

{desc}

<div class="hero-buttons" style="margin-bottom: 24px; display: flex; flex-wrap: wrap; gap: 12px;">
  <a href="../index.md" class="hero-btn primary" style="background: #4c1d95;">
    ☢️ Înapoi la Index Medicină Nucleară ➔
  </a>
  <a href="../../iris/" class="hero-btn secondary" style="border-color: #6d28d9; color: #6d28d9;">
    🏛️ Justificare Clinică Ghid IRIS
  </a>
</div>

## Catalog Protocoale ({len(cat_protos)} disponibile)

| Denumire Protocol | Radiofarmaceutic | Clasă Doză | Resursă Tehnică |
|:------------------|:-----------------|:-----------|:----------------|
{table_rows}
"""
        (cat_dir / 'index.md').write_text(cat_content, encoding='utf-8')
        print(f"Generated Category Index: {cat_dir / 'index.md'}")

def generate_mn_index(mn_dir: Path):
    content = """---
title: Ghidul Protocoalelor de Radiologie Nucleară & Medicină Nucleară (MN)
hide:
  - navigation
  - toc
---

# ☢️ Ghidul Protocoalelor de Radiologie Nucleară & Medicină Nucleară (MN)

Compendiu clinic complet al protocoalelor de **Medicină Nucleară**, **Scintigrafie Planară & SPECT/CT** și **Tomografie cu Emisie de Pozitroni (PET/CT)**, integrat conform standardelor de referință **MCB Radiology** și ghidurilor societăților de profil (**SNMMI / EANM**).

<div class="hero-buttons" style="margin-bottom: 24px;">
  <a href="https://ref.mcbradiology.com/Nucs/Protocols/Nucs%20Protocols.html" target="_blank" rel="noopener" class="hero-btn primary" style="background: #4c1d95;">
    🌐 Portalul Oficial MCB Nuclear Medicine Protocols ➔
  </a>
  <a href="../iris/" class="hero-btn secondary" style="border-color: #6d28d9; color: #6d28d9;">
    🏛️ Criterii Ghid Național IRIS
  </a>
</div>

<div class="iris-official-banner" style="margin-bottom: 24px; background: linear-gradient(135deg, #2e1065 0%, #4c1d95 100%); color: #ffffff; padding: 20px 24px; border-radius: 12px; border: 1px solid rgba(196, 181, 253, 0.3);">
  <div class="iris-official-badge" style="background: rgba(196, 181, 253, 0.2); color: #ddd6fe; padding: 4px 12px; border-radius: 999px; display: inline-block; font-weight: 700; font-size: 0.82rem; margin-bottom: 8px;">
    ⚛️ DIAGNOSTIC MOLECULAR ȘI FUNCȚIONAL IN VIVO
  </div>
  <p class="iris-official-desc" style="margin-bottom: 12px !important; color: #f5f3ff; font-size: 0.95rem; line-height: 1.55;">
    Spre deosebire de tehnicile imagistice structurale (CT, RX, ecografie), medicina nucleară vizualizează procesele fiziopatologice la nivel celular și molecular, oferind sensibilitate diagnostică precoce în afecțiuni oncologice, cardiace, osoase, renale și infecțioase.
  </p>
  <a href="https://ref.mcbradiology.com/Nucs/Protocols/Nucs%20Protocols.html" target="_blank" rel="noopener" style="font-weight: 600; color: #c4b5fd; text-decoration: none;">
    Accesează protocoalele complete de medicină nucleară pe portalul MCB Radiology ➔
  </a>
</div>

<p class="body-parts-section-heading">Navigare după Specialitatea Clinică</p>

<div class="body-parts-grid">
  <a href="pulmonar/" class="body-part-card" style="border-top: 3px solid #7c3aed;">
    <h3>Pulmonar &bull; V/Q Scan</h3>
    <p class="body-part-desc">Ventilație Xenon-133, Perfuzie MAA, TEP la gravide / alergie contrast</p>
  </a>
  <a href="cardiac/" class="body-part-card" style="border-top: 3px solid #7c3aed;">
    <h3>Cardiologie Nucleară &bull; MUGA</h3>
    <p class="body-part-desc">Ventriculografie sincronizată ECG, FEVS cardiotoxicitate chimio</p>
  </a>
  <a href="digestiv/" class="body-part-card" style="border-top: 3px solid #7c3aed;">
    <h3>Gastroenterologie &amp; Hepatobiliar</h3>
    <p class="body-part-desc">HIDA colecistită/dischinezie, hemoragie digestivă activă, golire gastrică</p>
  </a>
  <a href="urinar/" class="body-part-card" style="border-top: 3px solid #7c3aed;">
    <h3>Nefrologie &amp; Urologie</h3>
    <p class="body-part-desc">Renogramă MAG3 diuretic Lasix, DMSA cortical pediatrie, HTA Captopril</p>
  </a>
  <a href="osos/" class="body-part-card" style="border-top: 3px solid #7c3aed;">
    <h3>Sistem Osos &bull; Whole Body &amp; 3-Faze</h3>
    <p class="body-part-desc">Metastaze osteoblastice, osteomielită vs celulită, SPECT/CT, NaF PET</p>
  </a>
  <a href="endocrin/" class="body-part-card" style="border-top: 3px solid #7c3aed;">
    <h3>Endocrinologie Nucleară</h3>
    <p class="body-part-desc">Scintigrafie tiroidă I-123, cancer tiroidian I-131, adenom paratiroidă Sestamibi</p>
  </a>
  <a href="neuro/" class="body-part-card" style="border-top: 3px solid #7c3aed;">
    <h3>Neurologie &amp; Neuroimagistică</h3>
    <p class="body-part-desc">Perfuzie cerebrală moarte cerebrală, cisternografie fugă LCR, PET FDG creier</p>
  </a>
  <a href="infectie/" class="body-part-card" style="border-top: 3px solid #7c3aed;">
    <h3>Infecții &amp; Inflamație Ocultă</h3>
    <p class="body-part-desc">Leucocite marcate Ceretec Tc-99m, Indium-111 WBC, febră de cauză necunoscută</p>
  </a>
  <a href="oncologie/" class="body-part-card" style="border-top: 3px solid #7c3aed;">
    <h3>Oncologie Moleculară &amp; PET-CT</h3>
    <p class="body-part-desc">PET-CT FDG corp întreg, OctreoScan neuroendocrin, santinelă sân/melanom</p>
  </a>
</div>

---

## Catalog Sinoptic al Protocoalelor de Medicină Nucleară (MCB Radiology)

| Protocol Clinic | Radiofarmaceutic | Doză / Clasă | Indicație Cheie | Link Protocol | Ghid Oficial Sursă |
|:----------------|:-----------------|:-------------|:----------------|:--------------|:-------------------|
| **V/Q Lung Scan (Ventilație & Perfuzie)** | Xe-133 gaz + Tc-99m MAA | 2-3 mSv (Clasa 2) | Trombembolism pulmonar (TEP) la gravide / alergie iod | [Vezi Protocol](pulmonar/scintigrafie-ventilatie-perfuzie-vq.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Lung%20Ventilation%20Xenon.pdf){ target="_blank" rel="noopener" } |
| **MUGA Scan (Ventriculografie)** | Tc-99m RBC UltraTag | 4-6 mSv (Clasa 2) | Monitorizare FEVS chimioterapie antracicline / Herceptin | [Vezi Protocol](cardiac/ventriculografie-muga.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/MUGA%20Ventriculography.pdf){ target="_blank" rel="noopener" } |
| **HIDA Cholescintigraphy (Colecist)** | Tc-99m Mebrofenin | 2-4 mSv (Clasa 2) | Colecistită acută obstrucție cistic, GBEF CCK | [Vezi Protocol](digestiv/scintigrafie-hepatobiliara-hida.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/HIDA.pdf){ target="_blank" rel="noopener" } |
| **Ficat & Splină** | Tc-99m Sulfur Colloid | 2 mSv (Clasa 2) | Ciroză, hipertensiune portală, coloid shift | [Vezi Protocol](digestiv/scintigrafie-ficat-splina.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Liver%20Spleen.pdf){ target="_blank" rel="noopener" } |
| **Sângerare Digestivă Acută** | Tc-99m RBC UltraTag | 4-6 mSv (Clasa 2) | Detecție sângerare joasă lentă (0.05 mL/min) | [Vezi Protocol](digestiv/scintigrafie-sangerare-digestiva.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/GI%20Bleeding.pdf){ target="_blank" rel="noopener" } |
| **Evacuare Gastrică Solidă** | Tc-99m Sulfur Colloid | < 1 mSv (Clasa 1) | Gastropareză diabetică, greață cronică | [Vezi Protocol](digestiv/scintigrafie-evacuare-gastrica.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Gastric%20Emptying.pdf){ target="_blank" rel="noopener" } |
| **MAG3 Renogramă & Lasix** | Tc-99m MAG3 | 2 mSv (Clasa 1-2) | Obstrucție joncțiune pielo-ureterală vs. dilatație | [Vezi Protocol](urinar/scintigrafie-renala-mag3-diuretic.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Renal%20MAG3%20Lasix.pdf){ target="_blank" rel="noopener" } |
| **DMSA Renal Cortical** | Tc-99m DMSA | 1.5 mSv (Clasa 1) | Cicatrici pielonefrită pediatrie, RVU | [Vezi Protocol](urinar/scintigrafie-corticala-renala-dmsa.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Renal%20DMSA.pdf){ target="_blank" rel="noopener" } |
| **HTA Renovasculară (Captopril)** | Tc-99m MAG3 | 2 mSv (Clasa 1-2) | Stenoză arteră renală funcțională | [Vezi Protocol](urinar/renograma-hipertensiune-renovasculara.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Renal%20Vascular%20HTN.pdf){ target="_blank" rel="noopener" } |
| **Scintigrafie Osoasă Corp Întreg** | Tc-99m MDP / HDP | 3-4 mSv (Clasa 2) | Metastaze osoase osteoblastice prostată, sân | [Vezi Protocol](osos/scintigrafie-osoasa-whole-body.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Bone%20Scan%20Whole%20Body.pdf){ target="_blank" rel="noopener" } |
| **Scintigrafie Osoasă 3 Faze** | Tc-99m MDP / HDP | 3-4 mSv (Clasa 2) | Osteomielită acută vs. celulită, proteze | [Vezi Protocol](osos/scintigrafie-osoasa-trei-faze.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Bone%20Scan%20Three%20Phase.pdf){ target="_blank" rel="noopener" } |
| **SPECT Osos / SPECT-CT** | Tc-99m MDP / HDP | 4-5 mSv (Clasa 2) | Spondiloliză, durere mecanică coloană, tars | [Vezi Protocol](osos/scintigrafie-osoasa-spect.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Bone%20Scan%20SPECT.pdf){ target="_blank" rel="noopener" } |
| **NaF-18 PET Osos** | 18F-NaF PET | 4-6 mSv (Clasa 2) | Cea mai înaltă rezoluție osoasă PET | [Vezi Protocol](osos/pet-ct-os-naf.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/PET%20NaF.pdf){ target="_blank" rel="noopener" } |
| **Tiroidă Captare & Scan** | I-123 / Tc-99m | 1-2 mSv (Clasa 1) | Basedow, noduli toxici calzi vs. reci | [Vezi Protocol](endocrin/scintigrafie-captare-tiroidiana.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Thyroid%20Imaging%20Uptake.pdf){ target="_blank" rel="noopener" } |
| **Cancer Tiroidian I-131 Whole Body** | I-131 oral | Terapeutic/Diag | Resturi tiroidiene, metastaze la distanță | [Vezi Protocol](endocrin/scintigrafie-whole-body-i131.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Thyroid%20I131.pdf){ target="_blank" rel="noopener" } |
| **Paratiroidă Sestamibi SPECT/CT** | Tc-99m MIBI | 4-6 mSv (Clasa 2) | Adenom paratiroidian în hiperparatiroidism | [Vezi Protocol](endocrin/scintigrafie-paratiroida-sestamibi.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Parathyroid.pdf){ target="_blank" rel="noopener" } |
| **Perfuzie Cerebrală Moarte Cerebrală** | Tc-99m HMPAO | 4-5 mSv (Clasa 2) | Confirmare paraclinică moarte cerebrală | [Vezi Protocol](neuro/scintigrafie-perfuzie-cerebrala-moarte-cerebrala.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Brain%20Death.pdf){ target="_blank" rel="noopener" } |
| **Cisternografie Fugă LCR** | In-111 DTPA | 2-3 mSv (Clasa 2) | Rinolicvoree, otolicvoree, hidrocefalie NPH | [Vezi Protocol](neuro/cisternografie-fuga-lcr.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Cisternogram%20CSF%20Leak.pdf){ target="_blank" rel="noopener" } |
| **PET-CT Cerebral FDG** | 18F-FDG | 5-7 mSv (Clasa 2) | Focar epileptogen, Alzheimer, demență FTD | [Vezi Protocol](neuro/pet-ct-cerebral-fdg.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/PET%20FDG%20Brain.pdf){ target="_blank" rel="noopener" } |
| **Leucocite Ceretec WBC** | Tc-99m HMPAO WBC | 5-7 mSv (Clasa 2) | Infecții osoase picior diabetic, IBD acut | [Vezi Protocol](infectie/scintigrafie-leucocite-marcate-ceretec.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/WBC%20Ceretec.pdf){ target="_blank" rel="noopener" } |
| **Leucocite Indium-111 WBC** | In-111 Oxine WBC | 7-10 mSv (Clasa 3) | Osteomielită cronică, febră de origine necunoscută | [Vezi Protocol](infectie/scintigrafie-leucocite-marcate-indium111.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/WBC%20Indium.pdf){ target="_blank" rel="noopener" } |
| **PET-CT Oncologie F-18 FDG** | 18F-FDG | 7-12 mSv (Clasa 3) | Stadializare cancere limfom, plămân, colon | [Vezi Protocol](oncologie/pet-ct-fdg-oncologie.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/PET%20FDG%20Body.pdf){ target="_blank" rel="noopener" } |
| **Octreotid (Tumori Neuroendocrine)** | In-111 Pentetreotide | 8-10 mSv (Clasa 3) | Carcinoid, gastrinom, feocromocitom | [Vezi Protocol](oncologie/scintigrafie-receptori-somatostatina-octreotid.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Octreotide.pdf){ target="_blank" rel="noopener" } |
| **MIBG Scintigrafie** | I-123 / I-131 MIBG | 5-8 mSv (Clasa 2-3) | Feocromocitom, neuroblastom copii | [Vezi Protocol](oncologie/scintigrafie-mibg.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/MIBG.pdf){ target="_blank" rel="noopener" } |
| **Ganglion Santinelă Sân (SLND)** | Tc-99m Nanocoloid | < 1 mSv (Clasa 1) | Biopsie ghidată axilă cancer mamar incipient | [Vezi Protocol](oncologie/limfoscintigrafie-ganglion-santinela-mamar.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Lympho%20Breast.pdf){ target="_blank" rel="noopener" } |
| **Ganglion Santinelă Melanom** | Tc-99m Nanocoloid | < 1 mSv (Clasa 1) | Reperaj limfatic drenaj cutanat melanom | [Vezi Protocol](oncologie/limfoscintigrafie-melanom.md) | [:material-file-pdf-box: PDF MCB](https://ref.mcbradiology.com/Nucs/Protocols/Lympho%20Skin.pdf){ target="_blank" rel="noopener" } |
"""
    target = mn_dir / 'index.md'
    target.write_text(content, encoding='utf-8')
    print(f"Generated: {target}")

# ==============================================================================
# 3. GENERATOR GHID INSTITUȚIONAL MCB RADIOLOGY
# ==============================================================================
def generate_mcb_institution_guide():
    content = """---
title: Ghidul Protocoalelor Clinice & Standardelor Tehnice MCB Radiology
author: MCB Radiology / Baptist Health System / Clinical Engineering
category: for-institutions
last_updated: '2026-09-27'
---

# Protocoale Clinice, Standarde Tehnice & Manual de Referință MCB Radiology

Ghid instituțional sinoptic al protocoalelor clinice, politicilor procedurale și ghidurilor tehnice aplicate în cadrul **MCB Radiology / Millennium Physician Group** și rețelei spitalicești afiliate (**Baptist Health System Florida** - Spitalele Riverside, Southside, Clay, St. Johns și centrele Freestanding ER).

<div class="iris-official-banner" style="margin-bottom: 24px; background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #ffffff; padding: 20px 24px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.2);">
  <div class="iris-official-badge" style="background: rgba(255,255,255,0.2); color: #fff; padding: 4px 12px; border-radius: 999px; display: inline-block; font-weight: 700; font-size: 0.82rem; margin-bottom: 8px;">
    🏥 PROTOCOALE INSTITUȚIONALE MCB RADIOLOGY (FLORIDA)
  </div>
  <p class="iris-official-desc" style="margin-bottom: 12px !important; color: #f0fdf4; font-size: 0.95rem; line-height: 1.55;">
    Manualul online oficial de proceduri acoperă parametrii impliciți de tomografie computerizată (Siemens, GE, Philips), rezonanță magnetică (1.5T &amp; 3T), ultrasonografie vasculară și generală cu foi de lucru de tehnician, radiografie digitală, senologie/mamografie și spectrul complet de medicină nucleară.
  </p>
  <a href="https://ref.mcbradiology.com/" target="_blank" rel="noopener" style="font-weight: 600; color: #bae6fd; text-decoration: none;">
    Accesează portalul oficial online MCB Radiology Reference Manual ➔
  </a>
</div>

---

## 1. Sinteza Secțiunilor Tehnice MCB Radiology

| Domeniu Imagistic | Resurse Principale MCB | Echipamente & Tehnologii | Ghiduri & Formulare Asociate |
|:------------------|:-----------------------|:-------------------------|:-----------------------------|
| **Tomografie Computerizată (CT)** | [CT Protocols Manual](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/CT.html) | Siemens Drive 128, Force 192, GE Rev Ascend Plus, Go Top 128, Philips Incisive 128 | [Scanner Default Protocols](../ct/parametri-aparate-scanner-defaults.md), Foi de lucru tehnician, Ghid contrast oral |
| **Rezonanță Magnetică (IRM)** | [MRI Protocols Manual](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/MRI.html) | Siemens & GE 1.5T / 3.0T, Body, Neuro, MSK, Breast, Vascular | Politici feromagnetice, implanturi CIED, ghid Clariscan |
| **Ultrasonografie & Ecografie (US)** | [US Worksheets & Protocols](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/US/Worksheets%20&%20Protocols.html) | Doppler vascular periferic, transplant renal/hepatic, părți moi, OB | Fișe de măsurători tehnician (Tech Worksheets) pentru fiecare organ |
| **Radiologie Convențională (RX)** | [X-Ray Protocols Manual](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/Xray/Xray.html) | Radiografie digitală adulți (9 secțiuni) & pediatrie (6 secțiuni) | Tehnici de poziționare, colimare și radioprotecție ALARA |
| **Senologie & Mamografie (Breast)** | [Breast Imaging & Policies](https://ref.mcbradiology.com/Breast/Breast.html) | Mamografie 2D/3D (Tomosinteză), RMN mamar, Biopsie stereotaxică | Politici poziționare adecvată, compoziție metalică clipuri biopsie |
| **Medicină Nucleară (Nucs / MN)** | [Nucs Protocols Manual](https://ref.mcbradiology.com/Nucs/Protocols/Nucs%20Protocols.html) | SPECT/CT, PET-CT FDG & NaF, Gamma-camere LFOV | Protocoale clinice și practice guidelines SNMMI |

---

## 2. Puncte Forte și Inovații Tehnice MCB

### 2.1. Standarizarea Parametrilor Impliciti de Scaner (CT Defaults)
Departamentul a compilat o matrice tehnică detaliată a fiecărui computer tomograf din rețea, specificând:
- Kilovoltajul adaptiv (CARE kV la Siemens, kV Assist la GE, DoseWise la Philips);
- Modularea automată mAs bazată pe Noise Index sau Quality Reference mAs;
- Grosimile de achiziție versus grosimile de reconstrucție pentru PACS;
- Filtrele/kernelele de convoluție și procentul de reconstrucție iterativă (ADMIRE, ASiR-V, iDose4).
Consultați ghidul complet dedicat: [:material-file-document-outline: Parametri Impliciti Scanere CT](../ct/parametri-aparate-scanner-defaults.md).

### 2.2. Foi de Lucru pentru Tehnician în Ecografie (Sonographer Worksheets)
Pentru a elimina variația inter-operator și a asigura exhaustivitatea examinării ecografice, protocolul MCB impune completarea unor fișe standardizate de măsurători (Worksheets) disponibile pe portal pentru:
- **Abdomen complet:** dimensiuni ficat, ecogenitate, calibru CBP și căi intrahepatice, colecist (grosime perete, calculi), ax lung splină, rinichi bilateral (ax bipolar și indice parenchimatos), calibru aortă abdominală supra- și infrarenală.
- **Ecografie Doppler carotidiană:** viteze maxime sistolice (PSV) și telediastolice (EDV) pe artera carotidă comună (ACC), internă (ACI proximal/mediu/distal) și externă (ACE), raport ACI/ACC, direcția fluxului pe arterele vertebrale.
- **Doppler venos membre inferioare:** compresibilitate pas cu pas la fiecare 2 cm de la vena femurală comună până la venele gambiere, augmentare distală și reflux la manevra Valsalva.

### 2.3. Politici de Securitate IRM & Implanturi Condiționate
Secțiunea IRM oferă un ghid clar de management al pacienților purtători de stimulatoare cardiace (PPM) și defibrilatoare implantabile (ICD) clasificate MR Conditional, incluzând verificarea bateriei, reprogramarea temporară în mod asincron (VOO/DOO) și monitorizarea prin pulsoximetrie optică continuă pe durata scanării în câmp de 1.5T.

---

## 3. Linkuri Directe Către Secțiunile MCB Radiology

- [CT Manual & Protocols](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/CT.html){ target="_blank" rel="noopener" }
- [CT Scanner Default Protocols](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/CT/Protocols/Scanner%20Default%20Protocols.html){ target="_blank" rel="noopener" }
- [MRI Protocols Manual](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/MRI/MRI.html){ target="_blank" rel="noopener" }
- [US Worksheets & Protocols](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/US/Worksheets%20&%20Protocols.html){ target="_blank" rel="noopener" }
- [X-Ray Protocols Manual](https://ref.mcbradiology.com/Protocols,%20Policies,%20Worksheets%20&%20Forms/Xray/Xray.html){ target="_blank" rel="noopener" }
- [Breast Imaging & Biopsy](https://ref.mcbradiology.com/Breast/Breast.html){ target="_blank" rel="noopener" }
- [Nuclear Medicine Protocols](https://ref.mcbradiology.com/Nucs/Protocols/Nucs%20Protocols.html){ target="_blank" rel="noopener" }
"""
    target = ROOT / 'docs' / 'for-institutions' / 'mcb-radiology-protocols.md'
    target.write_text(content, encoding='utf-8')
    print(f"Generated: {target}")

def main():
    print("=== Generare Protocoale MCB Radiology & Medicină Nucleară ===")
    generate_ct_scanner_defaults()
    generate_nucs_files()
    generate_mcb_institution_guide()
    print("=== Toate fișierele de bază au fost generate cu succes! ===")

if __name__ == '__main__':
    main()
