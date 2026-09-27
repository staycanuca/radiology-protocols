#!/usr/bin/env python3
"""generate_dartmouth_protocols.py — Generează protocoalele Dartmouth-Hitchcock Medical Center (DHMC) / Geisel School of Medicine at Dartmouth.

Sursă: Geisel School of Medicine at Dartmouth / Department of Radiology
URL: https://geiselmed.dartmouth.edu/radiology/policies-protocols/protocols/
"""

from __future__ import annotations

import sys
from pathlib import Path

# UTF-8 pe terminale Windows
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from render_protocol import render_document
from render_irm_protocol import render_irm_document
from render_eco_protocol import render_eco_document
from render_rx_protocol import render_rx_document

DARTMOUTH_BASE_URL = "https://geiselmed.dartmouth.edu/radiology/policies-protocols/protocols/"
AUTHOR_DHMC = "Dartmouth-Hitchcock Medical Center / Geisel School of Medicine at Dartmouth"
DATE_NOW = "2026-09-26"

# ==============================================================================
# 1. PROTOCOALE CT DARTMOUTH
# ==============================================================================

CT_PROTOCOLS = [
    # 1. CTA Disecție Aortă Toracică
    {
        "file_path": ROOT / "docs" / "ct" / "chest" / "ct-cta-thorax-dissection-dartmouth.md",
        "fm": {
            "title": "CTA Disecție Aortă Toracică (Protocol Dartmouth Hitchcock)",
            "author": AUTHOR_DHMC,
            "category": "chest",
            "last_updated": DATE_NOW,
            "protocol_type": "contrast-enhanced",
            "clinical_indications": [
                "Suspiciune de disecție acută de aortă toracică (Stanford tip A sau B)",
                "Sindrom aortic acut: hematom intramural (IMH), ulcer penetrant aterosclerotic (PAU)",
                "Durere toracică posterioară sfâșietoare sau migratoare, asimetrie de puls/tensiune arterială",
                "Evaluare pre și post-operatorie de anevrism aortic toracic / proteză vasculară (TEVAR)",
            ],
            "position": "Decubit dorsal, brațele ridicate deasupra capului",
            "npo": "Repaus alimentar 2-4 ore dacă starea clinică permite; în urgență N/A",
            "premedication": "Fără contrast oral. Monitorizare continuă a tensiunii arteriale și a ritmului cardiac.",
            "contrast": {
                "agent": "Omnipaque 350 / Isovue 370",
                "volume": "100-120 mL (adaptat la greutate)",
                "flow_rate": "4.0 - 5.0 mL/s",
                "duration": "20-25s",
                "timing": "Bolus tracking pe aorta descendentă / crosa aortică; trigger la 120-150 HU",
                "roi": "Lumenul aortei descendente la nivelul bifurcației traheale",
                "trigger": "120-150 HU",
            },
            "tech_params": {
                "kv": "100 - 120 kVp (AEC activ)",
                "mas": "CAREDose4D / SmartmA modulare automată",
                "slice_thickness": "0.625 - 1.25 mm",
                "rotation_time": "0.33 - 0.5 s",
                "pitch": "0.8 - 1.0",
                "scan_mode": "Elicoidal sincronizat ECG (ECG-gated opțional la rădăcina aortică)",
                "collimation": "128 × 0.6 mm / 64 × 0.625 mm",
            },
            "series": [
                {
                    "name": "CT Torace Nativ (Pre-contrast)",
                    "start": "Deasupra apexurilor pulmonare",
                    "end": "Sub diafragm / glande suprarenale",
                    "delay": "0 sec",
                    "thickness": "2.5 mm",
                    "notes": "Esențial pentru evidențierea hematomului intramural hiperdens și a deplasării calcificărilor intimale",
                },
                {
                    "name": "CTA Aortă Toracică Angiografică",
                    "start": "Deasupra apexurilor pulmonare",
                    "end": "Sub diafragm (sau extins pelvin până la arterele femurale comune dacă disecția este extinsă)",
                    "delay": "Trigger + 3-5 sec",
                    "thickness": "0.625 mm",
                    "notes": "Opacifiere densă a lumenului adevărat și fals (> 300 HU); identificare fald intimal și orificiu de intrare",
                },
            ],
            "recons": [
                {
                    "plane": "Axial",
                    "acquisition": "CTA Aortă Toracică",
                    "fov": "Torace",
                    "thickness_increment": "1.25 mm / 1.0 mm",
                    "kernel": "Mediastinal Standard",
                    "ir_strength": "Standard",
                    "notes": "Serie diagnostică primară de înaltă rezoluție",
                },
                {
                    "plane": "Coronal & Sagital",
                    "acquisition": "CTA Aortă Toracică",
                    "fov": "Torace",
                    "thickness_increment": "2.0 mm / 2.0 mm",
                    "kernel": "Mediastinal Standard",
                    "ir_strength": "Standard",
                    "notes": "Vizualizare completă a crosei și aortei descendente",
                },
                {
                    "plane": "MIP Oblic & 3D VR",
                    "acquisition": "CTA Aortă Toracică",
                    "fov": "Aortă Toracică",
                    "thickness_increment": "3.0 mm MIP",
                    "kernel": "Standard",
                    "ir_strength": "Standard",
                    "notes": "MIP de-a lungul curburii aortice (candy cane view) și reconstrucții 3D VR",
                },
            ],
            "notes": {
                "tech": "Scanare caudo-cranială sau cranio-caudală rapidă. Canulă 18G în plica cotului. Flush salin 50 mL la 4.5 mL/s imediat post-contrast.",
                "nursing": "Verificare eGFR, tensiune arterială la ambele brațe. Nu se întârzie examinarea în suspiciune clinică de disecție de tip A.",
                "rad": "Verificați implicarea ostiilor coronariene, a trunchiului brahiocefalic, arterei carotide comune stângi și subclaviei stângi. Evaluați hemopericardul și hemotoracele.",
                "tips": "Apnee inspiratorie completă; asigurați-vă că scanarea se extinde suficient distal dacă există suspiciune de ischemie mezenterică sau renală secundară.",
            },
            "safety": {
                "allergy": "Conform politicii instituționale de urgență. Beneficiul salvării vieții primează.",
                "renal": "eGFR de referință; la pacienți instabili cu suspiciune acută se administrează hidratare post-procedurală.",
            },
            "iris_reference": {
                "chapter": "Torace & Pulmon",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 3 (Moderată 5 - 10 mSv)",
            },
        },
    },
    # 2. CTA Planificare TAVR
    {
        "file_path": ROOT / "docs" / "ct" / "chest" / "ct-cta-tavr-dartmouth.md",
        "fm": {
            "title": "CTA Planificare Transcateter TAVR / TAVI (Protocol Dartmouth Hitchcock)",
            "author": AUTHOR_DHMC,
            "category": "chest",
            "last_updated": DATE_NOW,
            "protocol_type": "contrast-enhanced",
            "clinical_indications": [
                "Stenoză aortică severă simptomatică evaluată pentru implantare transcateter de valvă aortică (TAVR / TAVI)",
                "Măsurare inel aortic (arie, perimetru, diametre min/max) pentru alegerea mărimii protezei",
                "Calculul distanței de la inelul valvular la ostiile arterelor coronare stângă și dreaptă",
                "Evaluarea calcificărilor aparatului valvular și a tractului de ejecție al ventriculului stâng (LVOT)",
                "Cartografierea accesului vascular ilio-femural și aortei toraco-abdominale",
            ],
            "position": "Decubit dorsal, brațele ridicate complet, electrozi ECG conectați, brățară de împământare",
            "npo": "Repaus alimentar 4 ore",
            "premedication": "Fără contrast oral. Verificare ritm cardiac; beta-blocante conform protocolului cardiologic dacă ritmul este > 65 bpm.",
            "contrast": {
                "agent": "Omnipaque 350 / Isovue 370",
                "volume": "80-100 mL la prima fază cardiacă + 40-50 mL la faza thoraco-abdominală",
                "flow_rate": "4.5 - 5.0 mL/s",
                "duration": "18-22s",
                "timing": "Bolus tracking pe aorta descendentă / rădăcina aortică",
                "roi": "Aorta descendentă la nivelul carinei",
                "trigger": "120-150 HU",
            },
            "tech_params": {
                "kv": "100 - 120 kVp",
                "mas": "Modulare adaptivă cardiacă",
                "slice_thickness": "0.625 mm",
                "rotation_time": "0.28 - 0.33 s",
                "pitch": "ECG gated elicoidal sau Flash spiral",
                "scan_mode": "Cardio ECG-gated pentru rădăcina aortică + Spirală rapidă pentru acces vascular",
                "collimation": "128 × 0.6 mm",
            },
            "series": [
                {
                    "name": "Calcium Score Cardiac (Nativ)",
                    "start": "Nivelul carinei traheale",
                    "end": "Sub baza cordului / diafragm",
                    "delay": "Fără întârziere",
                    "thickness": "2.5 - 3.0 mm",
                    "notes": "Gated ECG prospectiv la 70-75% din ciclul R-R; cuantificare scor calciu Agatston valvular",
                },
                {
                    "name": "CTA Angio-Cardiac TAVR (Gated ECG)",
                    "start": "Carină",
                    "end": "Sub cord",
                    "delay": "Trigger + 4 sec",
                    "thickness": "0.625 mm",
                    "notes": "Achiziție sincronizată ECG multipafazică (30-80% din ciclu) pentru analiza dinamicii sistolo-diastolice a inelului aortic",
                },
                {
                    "name": "CTA Aortă Toraco-Abdomino-Pelvină (CAP Access)",
                    "start": "Apexuri pulmonare",
                    "end": "Sub simfiza pubiană (arterele femurale comune)",
                    "delay": "Continuare imediată fără pauză",
                    "thickness": "1.0 - 1.25 mm",
                    "notes": "Evaluare calibru minim, tortuozitate și calcificări circumferențiale ale arterelor iliace și femurale",
                },
            ],
            "recons": [
                {
                    "plane": "Axial Cardiac Multi-phase",
                    "acquisition": "CTA Angio-Cardiac TAVR",
                    "fov": "Cord (18-20 cm)",
                    "thickness_increment": "0.625 mm / 0.5 mm",
                    "kernel": "Cardiac Standard",
                    "ir_strength": "High",
                    "notes": "Reconstrucții la 30-40% (sistolă) și 70-75% (diastolă) pentru măsurarea inelului",
                },
                {
                    "plane": "Axial, Coronal & Sagital",
                    "acquisition": "CTA CAP Access",
                    "fov": "Torace-Abdomen-Pelvis",
                    "thickness_increment": "1.5 mm / 1.5 mm",
                    "kernel": "Standard",
                    "ir_strength": "Standard",
                    "notes": "Cartografiere acces femural vascular",
                },
            ],
            "notes": {
                "tech": "Asigurați conexiune stabilă ECG cu undă R clară. Injector cu seringă dublă: contrast 90 mL urmat de 40 mL flush salin la 4.5 mL/s.",
                "nursing": "Canulă venoasă periferică 18G în plica cotului drept preferată (evită artefactele de contrast din vena brahiocefalică stângă pe rădăcina aortică).",
                "rad": "Măsurați perimetrul și aria inelului la nivelul planului cel mai caudal al celor 3 cuspe. Raportați distanța de la inel la ostiul coronarei stângi (< 10 mm indică risc de ocluzie coronariană la expansiunea valvei).",
                "tips": "Faza sistolică (30-40%) oferă adesea cele mai mari dimensiuni ale inelului aortic și este preferată pentru dimensionare.",
            },
            "safety": {
                "allergy": "Screening alergie contrast.",
                "renal": "Verificare eGFR > 30 mL/min; pacienții cu stenoză aortică severă sunt fragili renal, optimizați volumul de contrast.",
            },
            "iris_reference": {
                "chapter": "Cardiologie & Angiografie",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 3 (Moderată 5 - 10 mSv)",
            },
        },
    },
    # 3. CT Pectus Excavatum
    {
        "file_path": ROOT / "docs" / "ct" / "chest" / "ct-pectus-excavatum-dartmouth.md",
        "fm": {
            "title": "CT Torace Pectus Excavatum (Protocol Dartmouth Hitchcock)",
            "author": AUTHOR_DHMC,
            "category": "chest",
            "last_updated": DATE_NOW,
            "protocol_type": "non-contrast",
            "clinical_indications": [
                "Deformare congenitală a peretelui toracic anterior (Pectus excavatum)",
                "Calculul indicelui Haller și al indicelui de asimetrie toracică",
                "Evaluarea compresiei sau deplasării cardiace (ventricul drept împins spre stânga)",
                "Planificare chirurgicală (procedura minim invazivă Nuss sau intervenția Ravitch)",
            ],
            "position": "Decubit dorsal, brațele ridicate confortabil deasupra capului",
            "npo": "Nu este necesar repaus alimentar",
            "premedication": "Fără contrast oral sau intravenos",
            "contrast": {
                "agent": "N/A",
                "volume": "Fără contrast",
                "flow_rate": "N/A",
                "duration": "N/A",
                "timing": "N/A",
                "roi": "N/A",
                "trigger": "N/A",
            },
            "tech_params": {
                "kv": "80 - 100 kVp (Protocol pediatric / tânăr adult low-dose)",
                "mas": "30 - 50 mAs (Optimizat ALARA pentru reducere maximă de doză)",
                "slice_thickness": "1.0 - 1.25 mm",
                "rotation_time": "0.33 - 0.5 s",
                "pitch": "1.2 - 1.4",
                "scan_mode": "Elicoidal ultra-rapid",
                "collimation": "64 × 0.625 mm sau 128 × 0.6 mm",
            },
            "series": [
                {
                    "name": "CT Torace în Apnee Inspiratorie",
                    "start": "Imediat deasupra apexurilor pulmonare",
                    "end": "Baza toracelui (la nivelul recesurilor costodiafragmatice)",
                    "delay": "0 sec",
                    "thickness": "1.0 mm",
                    "notes": "Scanare în inspir profund pentru calculul standard Haller",
                },
                {
                    "name": "CT Torace Focussat în Expir (Opțional)",
                    "start": "Nivelul unghiului Louis sternal",
                    "end": "Sub apendicele xifoid",
                    "delay": "0 sec",
                    "thickness": "1.25 mm",
                    "notes": "Expirul evidențiază compresia maximă sternovertebrală și poate crește indicele Haller",
                },
            ],
            "recons": [
                {
                    "plane": "Axial",
                    "acquisition": "CT Torace Pectus",
                    "fov": "Cutie toracică completă",
                    "thickness_increment": "2.0 mm / 2.0 mm",
                    "kernel": "Mediastinal (I30f) & Osos (I70f)",
                    "ir_strength": "Iterative Reconstruction High",
                    "notes": "Plan de măsurare la nivelul depresiunii sternale maxime",
                },
                {
                    "plane": "Sagital & Coronal",
                    "acquisition": "CT Torace Pectus",
                    "fov": "Cutie toracică",
                    "thickness_increment": "2.0 mm / 2.0 mm",
                    "kernel": "Mediastinal & Osos",
                    "ir_strength": "High",
                    "notes": "Evaluarea lungimii și angulației sternale",
                },
                {
                    "plane": "3D VR Schelet Toracic",
                    "acquisition": "CT Torace Pectus",
                    "fov": "Perete toracic",
                    "thickness_increment": "VR 3D",
                    "kernel": "Osos",
                    "ir_strength": "High",
                    "notes": "Randare volumetrică 3D pentru consiliere chirurgicală",
                },
            ],
            "notes": {
                "tech": "Instructaj atent de respirație înainte de poziționare. Pacienții sunt de regulă adolescenți sau tineri; prioritizați protocoalele de doză foarte scăzută (Low Dose CT).",
                "nursing": "Nu necesită linie venoasă periferică.",
                "rad": "Calculați Indicele Haller = (Distanța transversă maximă a cutiei toracice) / (Distanța antero-posterioară minimă între fața posterioară a sternului și fața anterioară a corpului vertebral). Indice Haller > 3.25 este considerat sever și indică intervenție chirurgicală.",
                "tips": "Măsurați de asemenea indicele de asimetrie (raportul între hemitoracele drept și stâng la punctul cel mai deprimat).",
            },
            "safety": {
                "allergy": "Fără risc — examinare nativă fără contrast.",
                "renal": "Fără restricții renale.",
            },
            "iris_reference": {
                "chapter": "Torace & Pulmon",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 2 (Scăzută 1 - 5 mSv)",
            },
        },
    },
    # 4. CTA Ischemie Mezenterică - Split Bolus
    {
        "file_path": ROOT / "docs" / "ct" / "abdomen" / "ct-cta-mesenteric-ischemia-dartmouth.md",
        "fm": {
            "title": "CTA Ischemie Mezenterică - Split Bolus (Protocol Dartmouth Hitchcock)",
            "author": AUTHOR_DHMC,
            "category": "abdomen",
            "last_updated": DATE_NOW,
            "protocol_type": "contrast-enhanced",
            "clinical_indications": [
                "Suspiciune de ischemie mezenterică acută (durere abdominală severă disproporționată cu datele obiective)",
                "Tromboză sau embolie acută a arterei mezenterice superioare (AMS) sau a trunchiului celiac",
                "Tromboză venoasă mezenterică (VMS, venă portă)",
                "Ischemie non-ocluzivă mezenterică (NOMI) la pacienți în stare critică / șoc septic sau cardiogen",
            ],
            "position": "Decubit dorsal, picioarele înainte (feet first), brațele ridicate deasupra capului",
            "npo": "Repaus alimentar de urgență",
            "premedication": "FĂRĂ contrast oral (contrastul oral pozitiv maschează hiperemia, edemul sau absența încărcării parietale a anselor intestinale)",
            "contrast": {
                "agent": "Omnipaque 350 / Isovue 370 (Tehnică Split-Bolus 150 mL)",
                "volume": "150 mL total: 100 mL la prima fază + 50 mL la a doua fază",
                "flow_rate": "4.0 mL/s",
                "duration": "Bipazic cu pauză de 25s între injectări",
                "timing": "Injectare 100 mL contrast -> pauză 25s -> injectare restul de 50 mL cu Smart Prep pe aortă",
                "roi": "Aorta abdominală deasupra trunchiului celiac",
                "trigger": "150 HU",
            },
            "tech_params": {
                "kv": "100 - 120 kVp (AEC activ)",
                "mas": "Modulare automată de doză",
                "slice_thickness": "0.625 - 1.25 mm",
                "rotation_time": "0.5 s",
                "pitch": "0.9 - 1.1",
                "scan_mode": "Elicoidal rapid",
                "collimation": "64 × 0.625 mm sau 128 × 0.6 mm",
            },
            "series": [
                {
                    "name": "CTA Abdomen & Pelvis Split-Bolus",
                    "start": "Deasupra cupolelor diafragmatice",
                    "end": "Sub simfiza pubiană",
                    "delay": "Trigger Smart Prep pe aortă",
                    "thickness": "0.625 mm",
                    "notes": "Tehnica split-bolus DHMC realizează opacifiere arterială intensă concomitent cu faza venoasă mezenterică și parietală",
                }
            ],
            "recons": [
                {
                    "plane": "Axial Standard",
                    "acquisition": "CTA Abdomen & Pelvis",
                    "fov": "Abdomen-Pelvis",
                    "thickness_increment": "2.5 mm / 2.5 mm",
                    "kernel": "Standard",
                    "ir_strength": "Standard",
                    "notes": "Serie trimisă în PACS pentru evaluare inițială",
                },
                {
                    "plane": "Axial Thin Slice",
                    "acquisition": "CTA Abdomen & Pelvis",
                    "fov": "Abdomen-Pelvis",
                    "thickness_increment": "1.25 mm / 1.0 mm",
                    "kernel": "Standard",
                    "ir_strength": "Standard",
                    "notes": "Serie subțire pentru vizualizarea ramurilor jejunale și ileale ale AMS",
                },
                {
                    "plane": "Coronal & Sagital MIP",
                    "acquisition": "CTA Abdomen & Pelvis",
                    "fov": "Vase mezenterice",
                    "thickness_increment": "2.0 mm q 2.0 mm MIP",
                    "kernel": "Standard",
                    "ir_strength": "Standard",
                    "notes": "Originea trunchiului celiac și AMS evaluate optim în plan sagital",
                },
                {
                    "plane": "3D VR & Curbat Aorto-Mezenteric",
                    "acquisition": "CTA Abdomen & Pelvis",
                    "fov": "Vase mezenterice",
                    "thickness_increment": "Reformatare curbată",
                    "kernel": "Standard",
                    "ir_strength": "Standard",
                    "notes": "Rotire 3D aortă și reconstrucție dublu oblică a originilor viscerale",
                },
            ],
            "notes": {
                "tech": "Canulă 18G sau 20G cu debit verificat la ser 4 mL/s. Respectați strict schema split bolus: 100 mL injectat, pauză 25s, apoi 50 mL cu Smart Prep.",
                "nursing": "Urgență chirurgicală și imagistică majoră — transport prompt și alertare radiolog.",
                "rad": "Căutați semne de ischemie intestinală: defect de încărcare arterial/venos, îngroșare parietală, pneumatoză intestinală, gaz în sistemul portomezenteric, lichid liber, perforație (pneumoperitoneu).",
                "tips": "Planul sagital este crucial pentru evaluarea stenozei sau ocluziei ostiale a AMS și a trunchiului celiac.",
            },
            "safety": {
                "allergy": "Conform politicii instituționale de urgență.",
                "renal": "În suspiciune critică de ischemie mezenterică acută, scanarea nu se amână pentru așteptarea creatininei.",
            },
            "iris_reference": {
                "chapter": "Abdomen & Pelvis",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 3 (Moderată 5 - 10 mSv)",
            },
        },
    },
    # 5. CTA DIEAP Flap
    {
        "file_path": ROOT / "docs" / "ct" / "abdomen" / "ct-cta-dieap-flap-dartmouth.md",
        "fm": {
            "title": "CTA Abdomen & Pelvis DIEP Flap (Protocol Dartmouth Hitchcock)",
            "author": AUTHOR_DHMC,
            "category": "abdomen",
            "last_updated": DATE_NOW,
            "protocol_type": "contrast-enhanced",
            "clinical_indications": [
                "Planificare preoperatorie pentru reconstrucție mamară autologă cu lambou liber perforant din artera epigastrică inferioară profundă (DIEP flap)",
                "Cartografierea vaselor perforante (calibru, traiect intramuscular vs. fascial, punct de emergență)",
                "Alegerea celui mai bun pedicul vascular (drept vs. stâng, medial vs. lateral) pentru reducerea timpului operator",
            ],
            "position": "Decubit dorsal, picioarele înainte (feet first), brațele ridicate confortabil",
            "npo": "Repaus alimentar 4 ore",
            "premedication": "FĂRĂ contrast oral. PĂTURĂ CALDĂ aplicată pe abdomen înainte de scanare pentru a preveni vasoconstricția reflexă a vaselor perforante cutanate. Îndepărtarea completă a îmbrăcămintei și a lenjeriei intime din zona abdominală/pelvină pentru a evita compresia cutanată.",
            "contrast": {
                "agent": "Omnipaque 350 / Isovue 370",
                "volume": "150 mL contrast + 50 mL flush salin",
                "flow_rate": "5.0 mL/s",
                "duration": "30s",
                "timing": "Smart Prep pe artera femurală comună la nivelul simfizei pubiene",
                "roi": "Lumenul arterei femurale comune (zoom pe imaginea de monitorizare pentru plasare precisă a ROI)",
                "trigger": "150 HU",
            },
            "tech_params": {
                "kv": "100 - 120 kVp",
                "mas": "AEC CAREDose4D / SureExposure",
                "slice_thickness": "0.625 mm",
                "rotation_time": "0.5 s",
                "pitch": "0.8 - 0.9",
                "scan_mode": "Elicoidal fin",
                "collimation": "128 × 0.6 mm sau 64 × 0.625 mm",
            },
            "series": [
                {
                    "name": "CTA Arterial DIEAP Abdomen & Pelvis",
                    "start": "Sub simfiza pubiană (nivel inghinal)",
                    "end": "Imediat deasupra diafragmului (direcție CAUDO-CRANIALĂ)",
                    "delay": "Trigger Smart Prep femural",
                    "thickness": "0.625 mm",
                    "notes": "Direcția caudo-cranială optimizează sincronizarea cu bolusul arterial în peretele abdominal inferior",
                }
            ],
            "recons": [
                {
                    "plane": "Axial Diagnostic",
                    "acquisition": "CTA Arterial DIEAP",
                    "fov": "Abdomen-Pelvis",
                    "thickness_increment": "2.5 mm / 2.5 mm",
                    "kernel": "Standard",
                    "ir_strength": "Standard",
                    "notes": "Evaluare de ansamblu",
                },
                {
                    "plane": "Axial Ultra-Subțire",
                    "acquisition": "CTA Arterial DIEAP",
                    "fov": "Perete abdominal anterior",
                    "thickness_increment": "0.625 mm / 0.5 mm",
                    "kernel": "Standard",
                    "ir_strength": "High",
                    "notes": "Esențial pentru urmărirea traiectului perforantelor milimetrice prin mușchiul drept abdominal",
                },
                {
                    "plane": "MIP Axial, Coronal & Sagital",
                    "acquisition": "CTA Arterial DIEAP",
                    "fov": "Perete abdominal",
                    "thickness_increment": "3.0 mm q 1.5 mm MIP",
                    "kernel": "Standard",
                    "ir_strength": "High",
                    "notes": "Proiecții de intensitate maximă pentru cartografierea arborizației perforantelor",
                },
                {
                    "plane": "3D Reconstrucție Volumetrică (VR)",
                    "acquisition": "CTA Arterial DIEAP",
                    "fov": "Tegument & perete abdominal",
                    "thickness_increment": "3D VR",
                    "kernel": "Standard",
                    "ir_strength": "High",
                    "notes": "Hartă de navigație chirurgicală de suprafață cu poziționarea perforantelor față de ombilic",
                },
            ],
            "notes": {
                "tech": "Canulă 18G în plica cotului. Asigurați debit constant de 5 mL/s. Încălziți abdomenul pacientei cu pătură caldă înainte de achiziție.",
                "nursing": "Verificare funcție renală și antecedente alergice.",
                "rad": "Localizați coordonatele X/Y/Z ale perforantelor dominante (distanță față de ombilic și linia mediană), calibrul la emergența fascială (> 1.0-1.5 mm) și traiectul intramuscular (scurt este preferat).",
                "tips": "Verificați și calibrul venelor comitante profunde și al venei epigastrice superficiale (SIEV) pentru drenaj venos de rezervă.",
            },
            "safety": {
                "allergy": "Screening alergie.",
                "renal": "eGFR > 30 mL/min.",
            },
            "iris_reference": {
                "chapter": "Abdomen & Pelvis",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 3 (Moderată 5 - 10 mSv)",
            },
        },
    },
    # 6. CT Colonografie Virtuală
    {
        "file_path": ROOT / "docs" / "ct" / "abdomen" / "ct-colonography-virtual-dartmouth.md",
        "fm": {
            "title": "CT Colonografie Virtuală - Pregătire & Scanare (Protocol Dartmouth Hitchcock)",
            "author": AUTHOR_DHMC,
            "category": "abdomen",
            "last_updated": DATE_NOW,
            "protocol_type": "non-contrast",
            "clinical_indications": [
                "Screening cancer colorectal la adulți cu risc mediu care refuză sau au contraindicație la colonoscopie optică",
                "Colonoscopie optică incompletă (stenoză ocluzivă, dolicocolon, aderențe postoperatorii, intoleranță)",
                "Pacienți vârstnici, fragili sau aflați sub tratament anticoagulant/antiagregant ce nu poate fi întrerupt",
            ],
            "position": "Dublă poziționare: decubit dorsal (supine) urmat de decubit ventral (prone) — sau decubit lateral stâng dacă pacienta nu poate sta pe burtă",
            "npo": "Dietă cu conținut scăzut de reziduuri 2-3 zile înainte; lichide clare în ziua precedentă",
            "premedication": "Protocol DHMC GoLytely cu Stool Tagging: Tagitol V (suspensie de bariu) administrat fracționat cu mesele în ziua pre-scanare + Gastrografin 20-30 mL seara înainte pentru marcarea lichidului rezidual. Administrare antispastic (Buscopan / Glucagon) i.v./i.m. la insuflație dacă nu există contraindicații.",
            "contrast": {
                "agent": "N/A (Fără contrast intravenos standard)",
                "volume": "Fără contrast IV",
                "flow_rate": "N/A",
                "duration": "N/A",
                "timing": "N/A",
                "roi": "N/A",
                "trigger": "N/A",
            },
            "tech_params": {
                "kv": "100 - 120 kVp",
                "mas": "30 - 50 mAs (Supine) / 25 - 40 mAs (Prone) — Protocol ultra low-dose",
                "slice_thickness": "1.0 - 1.25 mm",
                "rotation_time": "0.5 s",
                "pitch": "1.2 - 1.4",
                "scan_mode": "Elicoidal ultra-rapid",
                "collimation": "64 × 0.625 mm sau 128 × 0.6 mm",
            },
            "series": [
                {
                    "name": "Scanare 1: Decubit Dorsal (Supine)",
                    "start": "Cupole diafragmatice",
                    "end": "Simfiză pubiană / canal anal",
                    "delay": "După confirmarea distensiei colice optime pe topogramă",
                    "thickness": "1.0 mm",
                    "notes": "Insuficare automată cu CO2 sau pompă manuală cu aer până la toleranță și distensie completă a celor 6 segmente colice",
                },
                {
                    "name": "Scanare 2: Decubit Ventral (Prone)",
                    "start": "Cupole diafragmatice",
                    "end": "Simfiză pubiană",
                    "delay": "Imediat după rotirea pacientului",
                    "thickness": "1.0 mm",
                    "notes": "Mobilizarea polipilor vs. resturi fecale și redistribuirea aerului în segmentele dependente (rect, cecum)",
                },
            ],
            "recons": [
                {
                    "plane": "Axial Primar",
                    "acquisition": "Supine & Prone",
                    "fov": "Abdomen-Pelvis",
                    "thickness_increment": "1.25 mm / 1.0 mm",
                    "kernel": "Standard Abdominal & Fereastră Plămân/Colon (-1000/200 HU)",
                    "ir_strength": "High",
                    "notes": "Analiză 2D detaliată a peretelui colic și a organelor extracolice",
                },
                {
                    "plane": "Endoluminal 3D (Navigație Virtuală)",
                    "acquisition": "Supine & Prone",
                    "fov": "Lumen colic",
                    "thickness_increment": "Endoscopic 3D Fly-through",
                    "kernel": "Standard",
                    "ir_strength": "High",
                    "notes": "Vizualizare tridimensională endoluminală bidirecțională (retrogradă și anterogradă)",
                },
            ],
            "notes": {
                "tech": "Verificați topograma înainte de scanare pentru a vă asigura că toate segmentele (rect, sigmoid, colon descendent, transvers, ascendent, cec) sunt bine destinse. Reinsuflați dacă un segment este colabat.",
                "nursing": "Explicați pacientului senzația de plenitudine abdominală cauzată de insuflație. CO2 se absoarbe mult mai rapid decât aerul ambiant, reducând disconfortul post-procedural.",
                "rad": "Evaluați leziunile polipoide: mărime (dimensiune ≥ 6 mm este semnificativă), mobilitate între decubit dorsal și ventral, prezența marcajului baritat/iodat (fecaloamele captează bariu). Raportați conform clasificării C-RADS.",
                "tips": "Evaluarea combinată 2D (secțiuni axiale și coronale cu ferestre largi) și 3D endoluminal maximizează sensibilitatea pentru polipi sesili.",
            },
            "safety": {
                "allergy": "Fără risc de reacție la contrast IV.",
                "renal": "Nu afectează funcția renală.",
            },
            "iris_reference": {
                "chapter": "Abdomen & Pelvis",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 2 (Scăzută 1 - 5 mSv)",
            },
        },
    },
    # 7. Ghid Clinic Contrast Oral CT 2026
    {
        "file_path": ROOT / "docs" / "ct" / "abdomen" / "ct-oral-contrast-guidelines-dartmouth.md",
        "fm": {
            "title": "Ghid Clinic de Administrare a Contrastului Oral în CT (Ghid Dartmouth Geisel 2026)",
            "author": AUTHOR_DHMC,
            "category": "abdomen",
            "last_updated": DATE_NOW,
            "protocol_type": "contrast-enhanced",
            "clinical_indications": [
                "Recomandări bazate pe consens internațional (ACR, SAR, AGA 2024–2026) privind utilizarea rațională a contrastului oral",
                "Când contrastul oral este INDISPENSABIL: suspiciune de dehiscență anastomotică postoperatorie, fistulă digestivă, abces intraabdominal delimitat",
                "Când contrastul oral este CONTRAINDICAT sau INUTIL: hemoragie digestivă activă acută, colică renală, traumatism acut major, ischemie mezenterică, pancreatită acută",
            ],
            "position": "Standard conform protocolului de bază (Abdomen & Pelvis)",
            "npo": "Conform ghidului de mai jos",
            "premedication": "Selecție între contrast pozitiv (bariu diluat sau Gastrografin hidrosolubil) și contrast neutru/volumic (apă sau PEG)",
            "contrast": {
                "agent": "Contrast oral selectat specific + Contrast IV conform indicației",
                "volume": "500 - 1000 mL oral conform matricei de decizie",
                "flow_rate": "Oral fracționat",
                "duration": "45-90 min pre-scanare",
                "timing": "Fracționat: 1/3 la 60-90 min, 1/3 la 30-45 min, 1/3 chiar înainte de scanare",
                "roi": "Conform protocolului primar",
                "trigger": "Conform protocolului primar",
            },
            "tech_params": {
                "kv": "Conform protocolului primar",
                "mas": "Conform protocolului primar",
                "slice_thickness": "Conform protocolului primar",
                "rotation_time": "0.5 s",
                "pitch": "Conform protocolului primar",
                "scan_mode": "Elicoidal",
                "collimation": "Standard",
            },
            "series": [
                {
                    "name": "Matrice de Decizie Contrast Oral Dartmouth Geisel",
                    "start": "N/A",
                    "end": "N/A",
                    "delay": "N/A",
                    "thickness": "N/A",
                    "notes": "Tabel clinic de selecție rapidă pentru radiologi și tehnicieni",
                }
            ],
            "recons": [
                {
                    "plane": "Axial, Coronal & Sagital",
                    "acquisition": "Matrice Clinică",
                    "fov": "Abdomen",
                    "thickness_increment": "Standard",
                    "kernel": "Standard",
                    "ir_strength": "Standard",
                    "notes": "Integrare cu examinările standard de abdomen",
                }
            ],
            "notes": {
                "tech": "Nu administrați contrast oral pozitiv din oficiu! Consultați indicația clinică și radiologul de gardă.",
                "nursing": "În caz de suspiciune de perforație esofagiană sau dehiscență gastrică, utilizați exclusiv contrast iodat hidrosolubil (Gastrografin / Omnipaque oral), NICIODATĂ bariu (risc de mediastinită sau peritonită chimică gravă).",
                "rad": "Eliminarea contrastului oral de rutină scurtează timpul de staționare în Urgență cu 45–90 de minute și previne aspirația pulmonară la pacienții instabili.",
                "tips": "Pentru enterografie CT (boală Crohn), folosiți contrast neutru cu osmolaritate ridicată (PEG / sorbitol) pentru a destinde ansele fără a masca încărcarea mucoasei la contrastul IV.",
            },
            "safety": {
                "allergy": "Alergie la contrast oral extrem de rară.",
                "renal": "Contrastul oral nu este absorbit sistemic în cantități semnificative și nu afectează rinichiul.",
            },
            "iris_reference": {
                "chapter": "Abdomen & Pelvis",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 3 (Moderată 5 - 10 mSv)",
            },
        },
    },
    # 8. CTA Carotide și Poligon Willis
    {
        "file_path": ROOT / "docs" / "ct" / "neuro" / "ct-cta-carotids-circle-of-willis-dartmouth.md",
        "fm": {
            "title": "CTA Carotide și Poligonul lui Willis (Protocol Dartmouth Hitchcock)",
            "author": AUTHOR_DHMC,
            "category": "neuro",
            "last_updated": DATE_NOW,
            "protocol_type": "contrast-enhanced",
            "clinical_indications": [
                "Accident vascular cerebral acut ischemic (AVC) în fereastra terapeutică (tromboliză / trombectomie)",
                "Atac ischemic tranzitor (AIT) sau suflu carotidian asimptomatic",
                "Evaluarea stenozei arterei carotide interne (clasificare NASCET / ECST)",
                "Suspiciune de anevrism arterial intracranian sau disecție vasculară cervico-cerebrală",
            ],
            "position": "Decubit dorsal, capul poziționat simetric în tetieră, bărbia coborâtă ușor, imobilizare cu bandă",
            "npo": "Repaus alimentar 2-4 ore dacă timpul permite; în urgență N/A",
            "premedication": "Fără contrast oral",
            "contrast": {
                "agent": "Omnipaque 350 / Isovue 370",
                "volume": "70-80 mL contrast + 40-50 mL flush salin",
                "flow_rate": "4.5 - 5.0 mL/s",
                "duration": "15-18s",
                "timing": "Bolus tracking pe crosa aortică sau artera carotidă comună; trigger 120-150 HU",
                "roi": "Crosa aortică / artera carotidă comună la nivel C4-C5",
                "trigger": "120-150 HU",
            },
            "tech_params": {
                "kv": "100 - 120 kVp",
                "mas": "Modulare automată de doză neuro",
                "slice_thickness": "0.625 mm",
                "rotation_time": "0.33 - 0.5 s",
                "pitch": "0.8 - 1.0",
                "scan_mode": "Elicoidal rapid cranio-caudal sau caudo-cranial",
                "collimation": "64 × 0.625 mm sau 128 × 0.6 mm",
            },
            "series": [
                {
                    "name": "CTA Crosa Aortică până la Vertex",
                    "start": "Nivelul crosei aortice (baza gâtului)",
                    "end": "Vertex (creștetul craniului)",
                    "delay": "Trigger + 3-4 sec",
                    "thickness": "0.625 mm",
                    "notes": "Opacifiere densă de la originile vaselor mari supraaortice până la ramurile distale M2/M3 și A2/A3",
                }
            ],
            "recons": [
                {
                    "plane": "Axial Cerebral Subțire",
                    "acquisition": "CTA Crosa Aortică - Vertex",
                    "fov": "Craniu & Gât",
                    "thickness_increment": "0.625 mm / 0.5 mm",
                    "kernel": "Head Standard / Vascular",
                    "ir_strength": "Standard",
                    "notes": "Detectare trombi endoluminali și cuantificare stenoză",
                },
                {
                    "plane": "MIP Coronal & Sagital Carotidian",
                    "acquisition": "CTA Crosa Aortică - Vertex",
                    "fov": "Bifurcații carotidiene",
                    "thickness_increment": "3.0 mm q 1.5 mm MIP",
                    "kernel": "Vascular",
                    "ir_strength": "Standard",
                    "notes": "Măsurare diametru lumen rezidual conform criteriilor NASCET",
                },
                {
                    "plane": "3D VR & MIP Poligonul lui Willis",
                    "acquisition": "CTA Crosa Aortică - Vertex",
                    "fov": "Poligonul lui Willis",
                    "thickness_increment": "Rotire 360° MIP",
                    "kernel": "Vascular",
                    "ir_strength": "Standard",
                    "notes": "Căutare anevrisme saculare pe AComA, AComP, bifurcația ACM",
                },
            ],
            "notes": {
                "tech": "Canulă 18G în plica cotului. Declanșare precisă a bolus tracking-ului pentru a evita contaminarea venoasă jugulară precoce.",
                "nursing": "În caz de AVC acut (Cod AVC), deplasare imediată la tomograf; timpul până la recanalizare este creier.",
                "rad": "Evaluați ocluziile de vas mare (LVO) la nivelul ACM (M1/M2), carotidei interne terminale (T-carotidian) sau arterei bazilare. Raportați scorul de colateralitate vasculară.",
                "tips": "Pentru diferențierea ocluziei complete de carotida cu lumen filiform (pseudo-ocluzie), analizați secțiunile tardive sau MIP-urile reconstruite atent.",
            },
            "safety": {
                "allergy": "În AVC acut, beneficiul trombectomiei și diagnosticului imediat depășește riscul reacției alergice ușoare.",
                "renal": "Nu amânați scanarea la pacienți cu suspiciune de ocluzie arterială acută.",
            },
            "iris_reference": {
                "chapter": "Cap, Gât & Coloană vertebrală",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 3 (Moderată 5 - 10 mSv)",
            },
        },
    },
    # 9. CT Masiv Facial Traumă
    {
        "file_path": ROOT / "docs" / "ct" / "neuro" / "ct-face-trauma-dartmouth.md",
        "fm": {
            "title": "CT Masiv Facial Traumă (Protocol Dartmouth Hitchcock)",
            "author": AUTHOR_DHMC,
            "category": "neuro",
            "last_updated": DATE_NOW,
            "protocol_type": "non-contrast",
            "clinical_indications": [
                "Traumatism cranio-facial acut (accidente rutiere, agresiuni, căderi)",
                "Suspiciune de fracturi maxilo-faciale: orbite (blow-out), oase nazale, complex zigomatico-maxilar (ZMC), mandibulă",
                "Fracturi Le Fort tip I, II sau III",
                "Evaluarea corpilor străini radioopaci intraorbitali sau faciale și a hematoamelor retrobulbare",
            ],
            "position": "Decubit dorsal, capul centrat în tetieră, planul ocluzal perpendicular pe masă dacă este posibil",
            "npo": "Nu este necesar repaus alimentar",
            "premedication": "Fără contrast",
            "contrast": {
                "agent": "N/A",
                "volume": "Fără contrast",
                "flow_rate": "N/A",
                "duration": "N/A",
                "timing": "N/A",
                "roi": "N/A",
                "trigger": "N/A",
            },
            "tech_params": {
                "kv": "120 kVp",
                "mas": "CAREDose4D / SureExposure (Ref 180-220 mAs)",
                "slice_thickness": "0.625 mm",
                "rotation_time": "0.5 s",
                "pitch": "0.8 - 0.9",
                "scan_mode": "Elicoidal fin izotrop",
                "collimation": "64 × 0.625 mm sau 128 × 0.6 mm",
            },
            "series": [
                {
                    "name": "CT Masiv Facial Nativ",
                    "start": "Imediat deasupra sinusurilor frontale",
                    "end": "Sub marginea inferioară a mandibulei (simfiză mentonieră)",
                    "delay": "0 sec",
                    "thickness": "0.625 mm",
                    "notes": "Acoperire completă a tuturor structurilor scheletice faciale și cavităților aeriene",
                }
            ],
            "recons": [
                {
                    "plane": "Axial Osos & Părți Moi",
                    "acquisition": "CT Masiv Facial Nativ",
                    "fov": "Masiv Facial (16-18 cm)",
                    "thickness_increment": "1.0 mm / 0.8 mm",
                    "kernel": "Bone High-Resolution (I70f) & Soft Tissue (I30f)",
                    "ir_strength": "High",
                    "notes": "Fereastră osoasă strictă pentru detectarea microfracturilor",
                },
                {
                    "plane": "Coronal & Sagital",
                    "acquisition": "CT Masiv Facial Nativ",
                    "fov": "Masiv Facial",
                    "thickness_increment": "1.5 mm / 1.5 mm",
                    "kernel": "Bone & Soft Tissue",
                    "ir_strength": "High",
                    "notes": "Planul coronal este crucial pentru evaluarea planșeului orbitar și a lamelor pterigoidiene",
                },
                {
                    "plane": "3D VR Schelet Facial",
                    "acquisition": "CT Masiv Facial Nativ",
                    "fov": "Masiv facial",
                    "thickness_increment": "3D VR",
                    "kernel": "Bone",
                    "ir_strength": "High",
                    "notes": "Reconstrucție tridimensională esențială pentru chirurgia maxilo-facială (OMFS)",
                },
            ],
            "notes": {
                "tech": "Îndepărtați protezele dentare mobile, cerceii și piercingurile faciale pentru a minimiza artefactele metalice de striere.",
                "nursing": "Atenție la menținerea căilor aeriene permeabile la pacienții politraumatizați cu sângerare orofaringiană masivă.",
                "rad": "Căutați semne de herniere sau pensare a mușchiului drept inferior în fracturile de planșeu orbitar (urgență oftalmologică), fracturi ale plăcii cribriforme cu fistulă LCR (rinolicvoree) și integritatea proceselor pterigoide (fracturile de pterigoide definesc complexul Le Fort).",
                "tips": "Utilizați algoritmi de reducere a artefactelor metalice (iMAR / SEMAR) dacă pacientul are implanturi dentare voluminoase.",
            },
            "safety": {
                "allergy": "Fără risc — examinare nativă.",
                "renal": "Fără risc renal.",
            },
            "iris_reference": {
                "chapter": "Cap, Gât & Coloană vertebrală",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 2 (Scăzută 1 - 5 mSv)",
            },
        },
    },
]

# ==============================================================================
# 2. PROTOCOALE IRM DARTMOUTH
# ==============================================================================

IRM_PROTOCOLS = [
    # 1. IRM Abdomen Basic
    {
        "file_path": ROOT / "docs" / "irm" / "abdomen-pelvis" / "irm-abdomen-basic-dartmouth.md",
        "fm": {
            "title": "IRM Abdomen Rutină Nativ & cu Contrast (Protocol DHMC)",
            "author": AUTHOR_DHMC,
            "category": "abdomen-pelvis",
            "last_updated": DATE_NOW,
            "modality": "irm",
            "clinical_indications": [
                "Evaluare generală abdominală pentru leziuni focale sau procese inflamatorii/infecțioase",
                "Suspiciune de colecții intraabdominale, abcese viscerale sau periviscerale",
                "Dureri abdominale persistente nespecifice fără diagnostic cert la ecografie sau CT",
                "Caracterizarea formațiunilor chistice vs. solide la pacienți cu contraindicație de contrast iodat",
            ],
            "contraindications": [
                "Stimulator cardiac / pacemaker vechi non-MR conditional sau electrozi intracardiaci abandonați",
                "Clipsuri anevrismale intracraniene feromagnetice",
                "Corpi străini metalici intraoculari",
                "Implanturi cohleare non-compatibile",
            ],
            "patient_prep": "Repaus alimentar 4-6 ore înainte de examinare pentru a reduce peristaltismul intestinal și a asigura repleția colecistului. Chestionar complet de securitate feromagnetică.",
            "coils_hardware": {
                "field_strength": "1.5 Tesla sau 3.0 Tesla (Siemens / GE / Philips)",
                "coil": "Antenă de corp multicanal Phased Array (Body Coil 18–32 canale) + antenă Spine posterioară",
                "positioning": "Decubit dorsal, picioarele sau capul înainte, centrare optică la nivelul apendicelui xifoid",
            },
            "contrast": {
                "agent": "Chelat de Gadoliniu macrociclic hidrosolubil (Gadobutrol / Gadoterat de meglumină)",
                "dose": "0.1 mmol/kg (standard)",
                "flow_rate": "1.5 - 2.0 mL/s urmat de flush salin 20-30 mL",
                "timing": "Fază dinamică multifazică: Arterială tardivă (18-22 sec), Venoasă portală (60-70 sec), Echilibru (3 min)",
            },
            "sequences": [
                {
                    "name": "Coronal T2 HASTE / Single-Shot",
                    "plane": "Coronal",
                    "tr_te": "TR 1400 ms / TE 91 ms",
                    "slice_gap": "5.0 mm / 1.0 mm gap",
                    "fov_matrix": "FOV 440 mm / Matrice 320×256",
                    "fat_sat": "Nu",
                    "notes": "Apnee inspiratorie / expiratorie scurtă; vedere de ansamblu a întregului abdomen și retroperitoneu",
                },
                {
                    "name": "Axial T1 Dual Echo In / Out of Phase",
                    "plane": "Axial",
                    "tr_te": "TR 170 ms / TE 1.2 & 2.4 ms (la 3T) sau 2.3 & 4.6 ms (la 1.5T)",
                    "slice_gap": "5.0 mm / 1.0 mm gap",
                    "fov_matrix": "FOV 380 mm / Matrice 256×192",
                    "fat_sat": "Nativ (In/Opposed phase)",
                    "notes": "Detecție grăsime microscopică intracelulară (steatoză hepatică, adenom suprarenalian)",
                },
                {
                    "name": "Axial T2 FS (Fat Suppressed BLADE / TSE)",
                    "plane": "Axial",
                    "tr_te": "TR 1600 ms / TE 95 ms",
                    "slice_gap": "5.0 mm / 1.0 mm gap",
                    "fov_matrix": "FOV 380 mm / Matrice 320×256",
                    "fat_sat": "Da (Spectral Fat Saturation / SPAIR)",
                    "notes": "Caracterizare leziuni chistice, edem, hemangioame și procese inflamatorii",
                },
                {
                    "name": "Axial DWI cu coeficient ADC",
                    "plane": "Axial",
                    "tr_te": "TR 5800 ms / TE 61 ms",
                    "slice_gap": "5.0 mm / 1.0 mm gap",
                    "fov_matrix": "FOV 380 mm / Matrice 192×144",
                    "fat_sat": "Da",
                    "notes": "Valori b: 50, 400, 750 s/mm² cu generare automată de hartă cantitativă ADC; detecție celularitate înaltă / abcese",
                },
                {
                    "name": "Axial 3D T1 VIBE FS Pre-Contrast",
                    "plane": "Axial",
                    "tr_te": "TR 3.5 ms / TE 1.4 ms",
                    "slice_gap": "3.0 mm (izotrop interpolat)",
                    "fov_matrix": "FOV 380 mm / Matrice 288×216",
                    "fat_sat": "Da",
                    "notes": "Secvență nativă volumetrică de referință pentru scăderile digitale",
                },
                {
                    "name": "Axial 3D T1 VIBE FS Dinamic Post-Contrast (60-70s)",
                    "plane": "Axial",
                    "tr_te": "TR 3.5 ms / TE 1.4 ms",
                    "slice_gap": "3.0 mm",
                    "fov_matrix": "FOV 380 mm / Matrice 288×216",
                    "fat_sat": "Da",
                    "notes": "Fază venoasă portală clasică cu scăderi digitale automate (Subtractions)",
                },
                {
                    "name": "Coronal 3D T1 VIBE FS Post-Contrast",
                    "plane": "Coronal",
                    "tr_te": "TR 3.8 ms / TE 1.5 ms",
                    "slice_gap": "3.5 mm",
                    "fov_matrix": "FOV 420 mm / Matrice 288×216",
                    "fat_sat": "Da",
                    "notes": "Completare multiplanară a fazei tardive de echilibru",
                },
            ],
            "quality_criteria": [
                "Absența artefactelor majore de mișcare respiratorie prin instruirea corectă a pacientului",
                "Supresie omogenă a semnalului grăsimii pe întreg volumul abdominal la secvențele FatSat",
                "Calcul automat al hărților ADC și al seriilor de substracție digitală (Post minus Pre-contrast)",
            ],
            "safety_considerations": [
                "Screening feromagnetic riguros Zonele III/IV",
                "Verificare eGFR conform recomandărilor ACR/ESUR pentru agenți macrociclici",
                "Supraveghere acustică și furnizare de dopuri / căști fonoizolante",
            ],
            "iris_reference": {
                "chapter": "Abdomen & Pelvis",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            },
            "notes": "Protocol de bază DHMC optimizat pe platforma Siemens, transpozabil direct pe aparate GE și Philips. În caz de ascită masivă, se recomandă utilizarea SPAIR sau DIXON pentru supresie adipoasă omogenă.",
        },
    },
    # 2. IRM Fistulă Perianală 3T
    {
        "file_path": ROOT / "docs" / "irm" / "abdomen-pelvis" / "irm-fistula-perianala-dartmouth.md",
        "fm": {
            "title": "IRM Fistulă Perianală 3T (Protocol Dedicat DHMC)",
            "author": AUTHOR_DHMC,
            "category": "abdomen-pelvis",
            "last_updated": DATE_NOW,
            "modality": "irm",
            "clinical_indications": [
                "Evaluarea preoperatorie a fistulelor anale complexe sau recidivante (clasificare Parks și St. James University Hospital)",
                "Suspiciune de abcese anorectale oculte, fosa ischioanală sau spațiul intersfincterian",
                "Boală Crohn perianală pentru monitorizarea răspunsului la terapia biologică / seton",
                "Fistule rectovaginale sau rectovezicale",
            ],
            "contraindications": [
                "Implanturi feromagnetice active incompatibile RM",
                "Fragilitate critică sau incapacitate de menținere a imobilității în decubit dorsal",
            ],
            "patient_prep": "Mică clismă evacuatorie cu 1-2 ore înainte de procedură pentru golirea ampulei rectale (reduce artefactele provocate de materiile fecale și gaze). Fără dilatare mecanică a canalului.",
            "coils_hardware": {
                "field_strength": "Preferabil 3.0 Tesla (conform protocolului dedicat DHMC) sau 1.5 Tesla cu antenă dedicată",
                "coil": "Antenă Phased Array multicanal Pelvis de înaltă densitate (fără antenă endorectală)",
                "positioning": "Decubit dorsal, pernă sub genunchi pentru relaxarea musculaturii planșeului pelvin",
            },
            "contrast": {
                "agent": "Gadoliniu macrociclic 0.1 mmol/kg",
                "dose": "0.1 mmol/kg",
                "flow_rate": "1.5 - 2.0 mL/s",
                "timing": "Achiziție tardivă post-contrast la 70-90 secunde și 3 minute",
            },
            "sequences": [
                {
                    "name": "Sagital T2 TSE (Full FOV Pelvis)",
                    "plane": "Sagital",
                    "tr_te": "TR 3500-4500 ms / TE 100 ms",
                    "slice_gap": "3.5 mm / 0.5 mm gap",
                    "fov_matrix": "FOV 240 mm / Matrice 384×288",
                    "fat_sat": "Nu",
                    "notes": "Secvență de planificare fundamentală: se identifică orientarea axului lung al canalului anal",
                },
                {
                    "name": "Axial Oblic T2 TSE (Small FOV)",
                    "plane": "Axial Oblic (strict perpendicular pe axul lung al canalului anal)",
                    "tr_te": "TR 3500-4000 ms / TE 105 ms",
                    "slice_gap": "3.0 mm / 0.3 mm gap",
                    "fov_matrix": "FOV 180 mm / Matrice 320×320 (rezoluție înaltă)",
                    "fat_sat": "Nu",
                    "notes": "Anatomie detaliată a sfincterului anal intern (hipointens), extern (izointens) și spațiului intersfincterian",
                },
                {
                    "name": "Axial Oblic T2 FS / SPAIR (Small FOV)",
                    "plane": "Axial Oblic",
                    "tr_te": "TR 4000 ms / TE 85 ms",
                    "slice_gap": "3.0 mm / 0.3 mm gap",
                    "fov_matrix": "FOV 180 mm / Matrice 320×256",
                    "fat_sat": "Da",
                    "notes": "Hipersemnal intens al traiectelor fistuloase active, al ramificațiilor secundare și al abceselor",
                },
                {
                    "name": "Coronal Oblic T2 TSE (Small FOV)",
                    "plane": "Coronal Oblic (strict paralel cu axul lung al canalului anal)",
                    "tr_te": "TR 3500 ms / TE 100 ms",
                    "slice_gap": "3.0 mm / 0.3 mm gap",
                    "fov_matrix": "FOV 180 mm / Matrice 320×320",
                    "fat_sat": "Nu",
                    "notes": "Vizualizarea mușchilor ridicători anali (levator ani) și clasificarea fistulelor transsfincteriene vs. suprasfincteriene",
                },
                {
                    "name": "Coronal Oblic T2 FS / SPAIR",
                    "plane": "Coronal Oblic",
                    "tr_te": "TR 3800 ms / TE 85 ms",
                    "slice_gap": "3.0 mm / 0.3 mm gap",
                    "fov_matrix": "FOV 180 mm / Matrice 320×256",
                    "fat_sat": "Da",
                    "notes": "Diferențiere clară a extensiilor supra-sfincteriene în fosa ischioanală",
                },
                {
                    "name": "Axial Oblic T1 SE Nativ",
                    "plane": "Axial Oblic",
                    "tr_te": "TR 600 ms / TE 12 ms",
                    "slice_gap": "3.0 mm / 0.3 mm gap",
                    "fov_matrix": "FOV 180 mm / Matrice 320×256",
                    "fat_sat": "Nu",
                    "notes": "Aprecierea anatomiei sfincteriene și identificarea sângelui / methemoglobinei",
                },
                {
                    "name": "Axial Oblic DWI Resolve",
                    "plane": "Axial Oblic",
                    "tr_te": "TR 4500 ms / TE 65 ms",
                    "slice_gap": "3.0 mm",
                    "fov_matrix": "FOV 180 mm / Matrice 192×144",
                    "fat_sat": "Da",
                    "notes": "Difuzie de înaltă rezoluție (b=50, 800) pentru identificarea abceselor oculte colectate",
                },
                {
                    "name": "Axial & Coronal Oblic 3D T1 VIBE FS Post-Contrast",
                    "plane": "Axial & Coronal Oblic",
                    "tr_te": "TR 4.2 ms / TE 1.6 ms",
                    "slice_gap": "1.5 - 2.0 mm izotrop",
                    "fov_matrix": "FOV 180 mm / Matrice 320×256",
                    "fat_sat": "Da",
                    "notes": "Priză intensă de contrast a pereților traiectului fistulos activ și a țesutului de granulație; scăderi digitale (Subtractions)",
                },
            ],
            "quality_criteria": [
                "Planificarea oblică impecabilă după axul canalului anal (oblicitatea incorectă distorsionează anatomia sfincteriană)",
                "Rezoluție spațială submilimetrică în plan (pixel < 0.6 mm)",
                "Delimitarea precisă a orificiului intern (la nivelul liniei pectinee) și extern perianal",
            ],
            "safety_considerations": [
                "Screening 3T feromagnetic riguros",
                "Verificare eGFR pre-contrast",
            ],
            "iris_reference": {
                "chapter": "Abdomen & Pelvis",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            },
            "notes": "Protocolul Dartmouth Hitchcock este optimizat pentru aparatele de 3 Tesla, oferind o delimitare superioară a complexului sfincterian. Descrierea fistulei se face conform cadranului orar (ora 12 = anterior / perineu, ora 6 = posterior / coccis).",
        },
    },
    # 3. IRM Cardiac Viabilitate
    {
        "file_path": ROOT / "docs" / "irm" / "cardiac" / "irm-cardiac-rutina-viabilitate-dartmouth.md",
        "fm": {
            "title": "IRM Cardiac Funcție & Viabilitate LGE (Protocol DHMC)",
            "author": AUTHOR_DHMC,
            "category": "cardiac",
            "last_updated": DATE_NOW,
            "modality": "irm",
            "clinical_indications": [
                "Evaluarea viabilității miocardice și a necrozei/cicatricii fibroase post-infarct miocardic",
                "Miocardită acută sau subacută (criteriile Lake Louise actualizate)",
                "Cardiomiopatii neischemice (dilatativă, hipertrofică, amiloidoză, sarcoidoză cardiacă)",
                "Cuantificarea precisă a volumelor, masei și fracției de ejecție a ventriculului stâng și drept (FEVS, FEVD)",
            ],
            "contraindications": [
                "Stimulatoare cardiace / defibrilatoare non-compatibile RM sau electrozi abandonați",
                "Aritmii severe necontrolate (fibrilație atrială rapidă cu ritm complet neregulat degradează CINE-ul)",
                "Imposibilitatea cooperării pentru apnee scurtă de 8–10 secunde",
            ],
            "patient_prep": "Evitarea cafelei și a stimulentelor cu 12 ore înainte de procedură. Aplicare riguroasă a electrozilor ECG pentru sincronizare cardiacă de calitate (semnal undă R înalt).",
            "coils_hardware": {
                "field_strength": "Preferabil 1.5 Tesla (recomandat de DHMC pentru minimizarea artefactelor de flux) sau 3.0 Tesla cu shim dedicat",
                "coil": "Antenă Cardiac Phased Array dedicată 16–32 canale cu gating ECG optic/vectorial",
                "positioning": "Decubit dorsal, capul înainte, electrozi ECG pe hemitoracele anterior stâng",
            },
            "contrast": {
                "agent": "Gadoliniu macrociclic (Gadovist / Dotarem)",
                "dose": "0.15 - 0.20 mmol/kg (doză împărțită sau bolus unic pentru LGE)",
                "flow_rate": "2.0 - 3.0 mL/s + 30 mL flush salin",
                "timing": "Examinare LGE (Late Gadolinium Enhancement) efectuată la 10–15 minute post-injectare",
            },
            "sequences": [
                {
                    "name": "Localizatoare Cardiace 3-Plane (Scout)",
                    "plane": "Axial, Coronal, Sagital",
                    "tr_te": "Ultra-rapid bSSFP",
                    "slice_gap": "8.0 mm",
                    "fov_matrix": "FOV 400 mm",
                    "fat_sat": "Nu",
                    "notes": "Identificarea axului lung al cordului",
                },
                {
                    "name": "CINE bSSFP 2-Camere (2CH - Ax Lung Vertical)",
                    "plane": "2-Camere (plan prin apex și centrul valvei mitrale)",
                    "tr_te": "TR 2.8 ms / TE 1.2 ms",
                    "slice_gap": "6.0 - 8.0 mm",
                    "fov_matrix": "FOV 340 mm / Matrice 256×208",
                    "fat_sat": "Nu",
                    "notes": "25-30 faze/ciclu cardiac în apnee; evaluare perete anterior și inferior VS",
                },
                {
                    "name": "CINE bSSFP 4-Camere (4CH - Ax Lung Orizontal)",
                    "plane": "4-Camere (plan prin apex, septul interventricular și peretele lateral)",
                    "tr_te": "TR 2.8 ms / TE 1.2 ms",
                    "slice_gap": "6.0 - 8.0 mm",
                    "fov_matrix": "FOV 340 mm / Matrice 256×208",
                    "fat_sat": "Nu",
                    "notes": "Evaluare ventricul stâng, ventricul drept, atrii și valve atrio-ventriculare",
                },
                {
                    "name": "CINE bSSFP Ax Scurt Stivă Completă (SAX Stack)",
                    "plane": "Short Axis (perpendicular pe sept de la inelul mitral la apex)",
                    "tr_te": "TR 2.8 ms / TE 1.2 ms",
                    "slice_gap": "8.0 mm contiguu (fără gap)",
                    "fov_matrix": "FOV 340 mm / Matrice 256×208",
                    "fat_sat": "Nu",
                    "notes": "10-12 secțiuni contigue ce acoperă întreg ventriculul; standardul de aur pentru FEVS, VTD, VTS și masă miocardică",
                },
                {
                    "name": "T2 TIRM / Black Blood Axial & SAX (Edem Miocardic)",
                    "plane": "Short Axis & 4CH",
                    "tr_te": "TR 2 cicluri R-R / TE 60-70 ms",
                    "slice_gap": "8.0 mm",
                    "fov_matrix": "FOV 340 mm",
                    "fat_sat": "Da (Inversion Recovery)",
                    "notes": "Raport semnal miocard/mușchi scheletic > 1.9 indică edem miocardic acut (miocardită sau infarct acut)",
                },
                {
                    "name": "TI Scout (Look-Locker CINE)",
                    "plane": "Short Axis medioventricular",
                    "tr_te": "Single shot inversion recovery",
                    "slice_gap": "8.0 mm",
                    "fov_matrix": "FOV 340 mm",
                    "fat_sat": "Nu",
                    "notes": "Identificarea timpului de inversie optim (TI de nul miocardic, uzual 280–340 ms) înainte de LGE",
                },
                {
                    "name": "LGE / PSIR 2D & 3D (Late Gadolinium Enhancement)",
                    "plane": "Short Axis (stivă completă) + 2CH + 4CH",
                    "tr_te": "TR 700 ms / TE 1.5 ms / TI optimizat din Look-Locker",
                    "slice_gap": "8.0 mm",
                    "fov_matrix": "FOV 340 mm / Matrice 256×208",
                    "fat_sat": "Da",
                    "notes": "Faza tardivă (10-15 min post contrast): hipersemnal alb transmural/subendocardic în necroză ischemică vs. subepicardic/mediomiocardic în miocardită/cardiomiopatii neischemice",
                },
            ],
            "quality_criteria": [
                "Nul miocardic impecabil pe LGE (miocardul sănătos apare complet negru, evidențiind contrastul leziunii)",
                "Unde CINE fluide fără artefacte de aritmie",
                "Acoperire completă a ventriculului stâng de la baza inelului mitral până la apexul veritabil",
            ],
            "safety_considerations": [
                "Monitorizare puls și saturație O2 continuă pe monitorul compatibil RM",
                "Verificare eGFR > 30 mL/min",
            ],
            "iris_reference": {
                "chapter": "Cardiologie & Angiografie",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            },
            "notes": "Ghidul DHMC recomandă 1.5T pentru minimizarea artefactelor de susceptibilitate pe secvențele bSSFP. Viabilitatea este definită prin extensia transmurală LGE: transmuralitate < 50% indică șanse mari de recuperare a funcției contractile post-revascularizare.",
        },
    },
    # 4. IRM Mamar Bilateral
    {
        "file_path": ROOT / "docs" / "irm" / "san" / "irm-mamar-bilateral-dartmouth.md",
        "fm": {
            "title": "IRM Mamar Bilateral Nativ & Dinamic (Protocol DHMC)",
            "author": AUTHOR_DHMC,
            "category": "san",
            "last_updated": DATE_NOW,
            "modality": "irm",
            "clinical_indications": [
                "Stadializarea locală a cancerului de sân recent diagnosticat (multifocalitate, multicentricitate, bilateralitate)",
                "Evaluarea răspunsului terapeutic la chimioterapia neoadjuvantă (NAC)",
                "Screening anual la femei cu risc înalt (mutații genetice BRCA1/BRCA2, risc pe viață > 20-25%)",
                "Cancer ocult cu adenopatie axilară metastatică și mamografie/ecografie negative",
                "Evaluarea leziunilor neconcludente mamografic sau ecografic",
            ],
            "contraindications": [
                "Stimulator cardiac / implanturi feromagnetice incompatibile RM",
                "Sarcină în primul trimestru (examinare electivă fără contrast se reprogramează)",
                "Insuficiență renală severă (eGFR < 30 mL/min) — contraindicație la Gadoliniu",
            ],
            "patient_prep": "Examinarea se programează optim între zilele 7–14 ale ciclului menstrual (faza foliculară) pentru a minimiza încărcarea de fond a parenchimului fibroglandular (BPE). Documentare dată ultimă menstruație (LMP).",
            "coils_hardware": {
                "field_strength": "1.5 Tesla sau 3.0 Tesla",
                "coil": "Antenă dedicată de sân multicanal (Breast Coil 8–16 canale)",
                "positioning": "Decubit ventral (prone), ambii sâni așezați simetric în cupele antenei fără pliuri cutanate",
            },
            "contrast": {
                "agent": "Gadoliniu macrociclic 0.1 mmol/kg",
                "dose": "0.1 mmol/kg urmat de 20-30 mL flush salin",
                "flow_rate": "2.0 mL/s injectare automată",
                "timing": "Achiziție dinamică rapidă: fază nativă pre-contrast urmată de minim 5 faze secvențiale la intervale de 60-90 secunde",
            },
            "sequences": [
                {
                    "name": "Axial T2 FS Dixon / Water Excitation",
                    "plane": "Axial bilateral",
                    "tr_te": "TR 4500 ms / TE 80 ms",
                    "slice_gap": "3.0 mm / 0.5 mm gap",
                    "fov_matrix": "FOV 340 mm / Matrice 384×384",
                    "fat_sat": "Da (Dixon / SPAIR omogen)",
                    "notes": "Caracterizare chisturi, edem peritumoral, ganglioni axilari și leziuni benigne (fibroadenoame)",
                },
                {
                    "name": "Axial T1 VIBE Non-FS Nativ",
                    "plane": "Axial bilateral",
                    "tr_te": "TR 4.5 ms / TE 1.8 ms",
                    "slice_gap": "2.5 mm",
                    "fov_matrix": "FOV 340 mm / Matrice 384×288",
                    "fat_sat": "Nu",
                    "notes": "Aprecierea densității parenchimului glandular și a focarelor hemoragice sau proteice preexistente",
                },
                {
                    "name": "Axial 3D T1 VIBE FS Pre-Contrast",
                    "plane": "Axial bilateral",
                    "tr_te": "TR 4.2 ms / TE 1.6 ms",
                    "slice_gap": "1.2 - 1.5 mm izotrop",
                    "fov_matrix": "FOV 340 mm / Matrice 384×320",
                    "fat_sat": "Da",
                    "notes": "Faza 1 nativă: bază de comparație pentru scăderile digitale și verificarea supresiei grăsimii",
                },
                {
                    "name": "Axial 3D T1 VIBE FS Dinamic Post-Contrast (Fazele 2–6)",
                    "plane": "Axial bilateral",
                    "tr_te": "TR 4.2 ms / TE 1.6 ms",
                    "slice_gap": "1.2 - 1.5 mm izotrop",
                    "fov_matrix": "FOV 340 mm / Matrice 384×320",
                    "fat_sat": "Da",
                    "notes": "Achiziții seriate la 60s, 120s, 180s, 240s, 360s post-contrast. Generare automată Subtraction și curbe cinetice",
                },
                {
                    "name": "Sagital 3D T1 VIBE FS Post-Contrast Tardiv",
                    "plane": "Sagital (unilateral sau bilateral pe sânul cu leziune)",
                    "tr_te": "TR 4.5 ms / TE 1.7 ms",
                    "slice_gap": "1.5 mm",
                    "fov_matrix": "FOV 220 mm / Matrice 320×256",
                    "fat_sat": "Da",
                    "notes": "Evaluare anatomică a raportului leziunii cu fascia mușchiului pectoral și mamelonul",
                },
                {
                    "name": "Reconstrucție MIP Axial Dinamic 3D",
                    "plane": "Axial 3D MIP",
                    "tr_te": "MIP din scăderea fazei precoce (Faza 2 minus Faza 1)",
                    "slice_gap": "Proiecție volumetrică",
                    "fov_matrix": "FOV 340 mm",
                    "fat_sat": "Da",
                    "notes": "Harta vasculară a sânilor pentru detecția instantanee a leziunilor hipervasculare și asimetriilor",
                },
            ],
            "quality_criteria": [
                "Supresie a grăsimii absolut omogenă bilaterală",
                "Rezoluție spațială înaltă (submilimetrică) și temporală (< 90-120 sec per achiziție dinamică)",
                "Calculul curbei intensitate-timp (Tip I progresiv = probabil benign, Tip II platou = suspect, Tip III wash-out = înalt sugestiv pentru malignitate)",
            ],
            "safety_considerations": [
                "Verificare eGFR pre-contrast",
                "Documentare status mamar prealabil (biopsii recente, intervenții chirurgicale, radioterapie anterioară)",
            ],
            "iris_reference": {
                "chapter": "Senologie & Mamografie",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            },
            "notes": "Protocolul Dartmouth Hitchcock include obligatoriu scăderi digitale automate (Subtractions) pe consola PACS. Raportarea leziunilor se efectuează conform terminologiei standardizate BI-RADS IRM.",
        },
    },
    # 5. IRM Mamar Abreviat
    {
        "file_path": ROOT / "docs" / "irm" / "san" / "irm-mamar-abreviat-screening-dartmouth.md",
        "fm": {
            "title": "IRM Mamar Abreviat Fast Screening (Protocol Dartmouth Hitchcock)",
            "author": AUTHOR_DHMC,
            "category": "san",
            "last_updated": DATE_NOW,
            "modality": "irm",
            "clinical_indications": [
                "Screening rapid la femei asimptomatice cu sâni denși (ACR C și D) la mamografie",
                "Femei cu risc intermediar de cancer mamar (istoric personal de neoplazie mamară, atipii epiteliale la biopsie anterioară)",
                "Protocol economic și confortabil (< 10 minute timp în gantry) cu sensibilitate similară protocolului complet",
            ],
            "contraindications": [
                "Contraindicații generale la câmpul magnetic RM",
                "Insuficiență renală severă (eGFR < 30 mL/min)",
                "Femei cu leziuni clinice palpabile evidente sau secreții mamelonare (acestea necesită protocolul diagnostic complet)",
            ],
            "patient_prep": "Zilele 7–14 ale ciclului menstrual recomandate. Chestionar RM standard.",
            "coils_hardware": {
                "field_strength": "1.5 Tesla sau 3.0 Tesla",
                "coil": "Antenă dedicată Breast Coil multicanal",
                "positioning": "Decubit ventral (prone)",
            },
            "contrast": {
                "agent": "Gadoliniu macrociclic 0.1 mmol/kg",
                "dose": "0.1 mmol/kg + flush salin 20 mL",
                "flow_rate": "2.0 mL/s",
                "timing": "O singură achiziție post-contrast precoce la 90–120 secunde",
            },
            "sequences": [
                {
                    "name": "Axial T2 FS (Localizare & Benignitate)",
                    "plane": "Axial bilateral",
                    "tr_te": "TR 4000 ms / TE 80 ms",
                    "slice_gap": "3.0 mm",
                    "fov_matrix": "FOV 340 mm",
                    "fat_sat": "Da",
                    "notes": "Diferențiere rapidă a chisturilor simple de mase solide",
                },
                {
                    "name": "Axial 3D T1 VIBE FS Pre-Contrast",
                    "plane": "Axial bilateral",
                    "tr_te": "TR 4.0 ms / TE 1.5 ms",
                    "slice_gap": "1.2 mm",
                    "fov_matrix": "FOV 340 mm / Matrice 384×320",
                    "fat_sat": "Da",
                    "notes": "Referință nativă (durată scanare ~1.5 minute)",
                },
                {
                    "name": "Axial 3D T1 VIBE FS Precoce Post-Contrast (la 90-120s)",
                    "plane": "Axial bilateral",
                    "tr_te": "TR 4.0 ms / TE 1.5 ms",
                    "slice_gap": "1.2 mm",
                    "fov_matrix": "FOV 340 mm / Matrice 384×320",
                    "fat_sat": "Da",
                    "notes": "Achiziție unică la vârful încărcării neoplazice (durată ~1.5 minute)",
                },
                {
                    "name": "Reconstrucție MIP Unică (Subtracție Post minus Pre)",
                    "plane": "Axial MIP 3D",
                    "tr_te": "Post-procesare automată",
                    "slice_gap": "Volumetric",
                    "fov_matrix": "FOV 340 mm",
                    "fat_sat": "Da",
                    "notes": "Interpretare în < 30 secunde: un MIP complet 'negru' exclude leziunile hipervasculare suspecte",
                },
            ],
            "quality_criteria": [
                "Timp total de achiziție sub 10 minute pe masă",
                "Scădere digitală automată impecabilă",
                "Dacă se identifică o leziune suspectă pe MIP, se recomandă completare cu secvențe tardive sau ecografie țintită second-look",
            ],
            "safety_considerations": [
                "Screening securitate RM",
                "Verificare eGFR",
            ],
            "iris_reference": {
                "chapter": "Senologie & Mamografie",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            },
            "notes": "Protocolul Fast Breast MRI dezvoltat de DHMC sporește accesibilitatea screening-ului prin rezonanță magnetică la femeile cu densitate mamară crescută, dublând rata de detecție a neoplaziilor mamare incipiente comparativ cu mamografia digitală simplă.",
        },
    },
    # 6. IRM Plex Brahial
    {
        "file_path": ROOT / "docs" / "irm" / "neuro" / "irm-plex-brahial-dartmouth.md",
        "fm": {
            "title": "IRM Plex Brahial Nativ & cu Contrast (Protocol DHMC)",
            "author": AUTHOR_DHMC,
            "category": "neuro",
            "last_updated": DATE_NOW,
            "modality": "irm",
            "clinical_indications": [
                "Plexopatie brahială de etiologie neprecizată (durere radiculară, parestezii, slăbiciune musculară a membrului superior)",
                "Traumatisme de plex brahial (suspiciune de avulsie radiculară preganglionară sau ruptură postganglionară)",
                "Tumori ale tecii nervoase periferice (schwannom, neurofibrom) sau sindrom de defileu toracic (TOS)",
                "Sindrom Pancoast-Tobias (tumoră de vârf pulmonar cu invazie de plex brahial C8-T1)",
                "Plexită post-radică vs. recidivă tumorală la pacienți oncologici tratați",
            ],
            "contraindications": [
                "Contraindicații feromagnetice clasice RM",
                "Imposibilitatea menținerii decubitului dorsal fără mișcare a umerilor",
            ],
            "patient_prep": "Screening feromagnetic complet. Se explică pacientului să evite înghițirea repetată în timpul scanărilor gâtului pentru a nu crea artefacte de mișcare pe rădăcinile nervoase.",
            "coils_hardware": {
                "field_strength": "1.5 Tesla sau 3.0 Tesla",
                "coil": "Combinație antenă Neurovasculară (Head & Neck Array) + antenă Body posterioară/anterioară pe claviculă și umăr",
                "positioning": "Decubit dorsal, brațele relaxate pe lângă corp (sau cu brațul afectat în ușoară abducție dacă se investighează TOS dinamic)",
            },
            "contrast": {
                "agent": "Gadoliniu macrociclic 0.1 mmol/kg",
                "dose": "0.1 mmol/kg + flush salin 20 mL",
                "flow_rate": "1.5 - 2.0 mL/s",
                "timing": "Achiziție post-contrast tardivă la 2-3 minute",
            },
            "sequences": [
                {
                    "name": "Coronal T2 STIR / SPAIR Bilateral (Vedere de Ansamblu)",
                    "plane": "Coronal",
                    "tr_te": "TR 4500 ms / TE 65 ms / TI 160 ms",
                    "slice_gap": "3.5 mm / 0.5 mm gap",
                    "fov_matrix": "FOV 360 mm / Matrice 384×256",
                    "fat_sat": "Da (STIR robust la interfețe osoase)",
                    "notes": "Comparație simetrică între plexul drept și cel stâng; identificare edem și hipersemnal radicular",
                },
                {
                    "name": "Sagital T1 SE Unilateral (Plex Afectat)",
                    "plane": "Sagital oblic (perpendicular pe claviculă de la coloană la axilă)",
                    "tr_te": "TR 650 ms / TE 12 ms",
                    "slice_gap": "3.0 mm / 0.5 mm gap",
                    "fov_matrix": "FOV 200 mm / Matrice 320×256",
                    "fat_sat": "Nu",
                    "notes": "Esențial pentru anatomia trunchiurilor și cordoanelor înconjurate de grăsime între mușchii scaleni",
                },
                {
                    "name": "Sagital T2 FS Unilateral",
                    "plane": "Sagital oblic",
                    "tr_te": "TR 3800 ms / TE 85 ms",
                    "slice_gap": "3.0 mm / 0.5 mm gap",
                    "fov_matrix": "FOV 200 mm / Matrice 320×256",
                    "fat_sat": "Da",
                    "notes": "Evidențierea inflamației, comprimării nervoase și leziunilor de continuitate",
                },
                {
                    "name": "Coronal T1 SE",
                    "plane": "Coronal",
                    "tr_te": "TR 600 ms / TE 11 ms",
                    "slice_gap": "3.0 mm",
                    "fov_matrix": "FOV 240 mm / Matrice 320×256",
                    "fat_sat": "Nu",
                    "notes": "Detecție pseudomeningocele post-traumatice și infiltrare tumorală",
                },
                {
                    "name": "3D T2 SPACE STIR Izotrop (opțional)",
                    "plane": "3D Volumetric Coronal",
                    "tr_te": "TR 2500 ms / TE 180 ms",
                    "slice_gap": "1.0 mm izotrop",
                    "fov_matrix": "FOV 260 mm",
                    "fat_sat": "Da",
                    "notes": "Navigare MPR în orice plan de-a lungul traiectului radicular C5–T1",
                },
                {
                    "name": "Post-Contrast Coronal & Axial 3D T1 FS",
                    "plane": "Coronal & Axial",
                    "tr_te": "TR 4.5 ms / TE 1.8 ms",
                    "slice_gap": "1.5 mm",
                    "fov_matrix": "FOV 240 mm / Matrice 320×256",
                    "fat_sat": "Da",
                    "notes": "Captare patologică de contrast în neurinoame, plexită infecțioasă/inflamatorie sau invazie neoplazică",
                },
            ],
            "quality_criteria": [
                "Acoperire completă a rădăcinilor emergente C5, C6, C7, C8 și T1 de la foramenul intervertebral până la diviziunile axilare",
                "Absența artefactelor de pulsație vasculară prin plasarea benzilor de presaturație pe artera subclavie",
            ],
            "safety_considerations": [
                "Screening feromagnetic riguros",
                "Verificare eGFR",
            ],
            "iris_reference": {
                "chapter": "Cap, Gât & Coloană vertebrală",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            },
            "notes": "Protocolul Dartmouth Hitchcock subliniază importanța secvenței sagitale T1/T2 perpendiculare pe claviculă pentru vizualizarea directă a 'triunghiului interscalenic' format de mușchiul scalen anterior, scalen mijlociu și prima coastă.",
        },
    },
]

# ==============================================================================
# 3. PROTOCOALE ECOGRAFIE (US / ECO) DARTMOUTH
# ==============================================================================

ECO_PROTOCOLS = [
    # 1. Ecografie Abdominală Completă DHMC
    {
        "file_path": ROOT / "docs" / "eco" / "abdomen-pelvis" / "eco-abdomen-complet-dartmouth.md",
        "fm": {
            "title": "Ecografie Abdominală Completă (Protocol Procedural DHMC #11184)",
            "author": AUTHOR_DHMC,
            "category": "abdomen-pelvis",
            "last_updated": DATE_NOW,
            "clinical_indications": [
                "Dureri abdominale acute sau cronice (hipocondru drept, epigastru, hipogaztru)",
                "Alterarea testelor hepatice biochimice (transaminaze, bilirubină, fosfatază alcalină, GGT crescute)",
                "Suspiciune de litiază biliară, colecistită, icter obstructiv, hepatopatie cronică sau ciroză",
                "Screening formațiuni tumorale renale sau hepatice și monitorizare ascită",
            ],
            "contraindications": [
                "Nu există contraindicații absolute (metodă non-ionizantă sigură)",
                "Limitări tehnice: meteorism abdominal sever, obezitate morbidă, pansamente chirurgicale extinse",
            ],
            "patient_prep": "Repaus alimentar strict minim 6-8 ore înainte de examinare (permite distensia optimă a colecistului și reduce gazele din stomac și duoden). Se permite consumul de apă plată necarbogazoasă.",
            "transducers_equipment": {
                "transducer_types": "Transductor convex 2.5 – 5.0 MHz pentru adulți; transductor liniar de înaltă frecvență 7.5 – 12.0 MHz opțional pentru peretele colecistului și suprafața hepatică",
                "patient_position": "Decubit dorsal inițial; decubit lateral stâng (45-90°) esențial pentru examinarea colecistului și a căilor biliare; decubit lateral drept pentru fereastra splenică",
                "gel_acoustic_window": "Gel ecografic hipoalergenic; utilizarea ficatului și a splinei ca ferestre acustice acustice naturale",
            },
            "technical_settings": {
                "frequency": "3.5 - 5.0 MHz (adaptat la profunzimea pacientului)",
                "gain": "Optimizat TGC (Time Gain Compensation) pentru ecogenitate uniformă antero-posterioară",
                "focus": "Focalizare poziționată la nivelul sau sub structura de interes",
                "doppler": "Doppler Color & Pulsat cu PRF ajustat la viteze venoase (15-25 cm/s) pentru vena portă și suprahepatice",
            },
            "standard_views": [
                {
                    "anatomical_region": "Ficat (Lob Drept & Stâng)",
                    "view_name": "Secțiuni longitudinale, transverse și subcostale",
                    "landmarks": "Măsurare ax lung lob drept în linia medioclaviculară (N < 15-16 cm), contur capsular fin, ecostructură comparată cu cortexul renal",
                    "measurements": "Diametru cranio-caudal lob drept, flux hepatopetal venă portă (Doppler color)",
                },
                {
                    "anatomical_region": "Colecist & Căi Biliare",
                    "view_name": "Incidențe ax lung și scurt în decubit dorsal și decubit lateral stâng",
                    "landmarks": "Grosime perete anterior colecist măsurată în secțiune transversă (N < 3 mm), căutare calculi mobili vs. polipi ficsi, semn Murphy ecografic",
                    "measurements": "Calea biliară principală (CBP) la nivelul hilului anterior de vena portă (N < 6 mm sau +1 mm per decadă peste 60 ani)",
                },
                {
                    "anatomical_region": "Pancreas",
                    "view_name": "Secțiune transversă epigastrică cu fereastră lob stâng hepatic",
                    "landmarks": "Cap, corp, coadă, raport cu vena splenică și trunchiul celiac/AMS; căutare dilatație canal Wirsung (N < 2 mm)",
                    "measurements": "Diametru antero-posterior cap, corp, calibru Wirsung",
                },
                {
                    "anatomical_region": "Splină",
                    "view_name": "Incidență intercostală postero-laterală stângă",
                    "landmarks": "Ecostructură omogenă, hil splenic, măsurare ax bipolar lungime (N < 12-13 cm)",
                    "measurements": "Lungime bipolară, ax transvers",
                },
                {
                    "anatomical_region": "Rinichi Bilateral",
                    "view_name": "Secțiuni coronale și parasagitale",
                    "landmarks": "Lungime bipolară (9–12 cm), diferențiere cortico-medulară, excludere litiază, chisturi sau dilatație pielocaliceală",
                    "measurements": "Lungime bipolară, grosime parenchim cortical",
                },
                {
                    "anatomical_region": "Aortă Abdominală & VCI",
                    "view_name": "Secțiuni longitudinale și transverse pe linia mediană",
                    "landmarks": "Aortă de la diafragm la bifurcație (calibru N < 20–25 mm, excludere anevrism > 30 mm); complianță respiratorie VCI",
                    "measurements": "Diametre antero-posterioare și transverse maxime aortă",
                },
            ],
            "quality_criteria": [
                "Documentare completă a fiecărui organ conform fișei procedurale DHMC #11184",
                "Examinarea obligatorie a colecistului în două poziții distincte pentru a dovedi mobilitatea calculilor",
                "Captură de imagini etichetate corespunzător cu markeri anatomici și măsuri calibrate",
            ],
            "safety_and_limitations": [
                "Tehnică non-iradiantă, complet sigură la gravide și copii",
                "În caz de interpoziție gazoasă marcată, se recomandă reexaminare după pregătire cu antiflatulente sau completare CT",
            ],
            "iris_reference": {
                "chapter": "Abdomen & Pelvis",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
            },
            "notes": "Protocolul procedural oficial DHMC #11184 (revizia 3) impune documentarea sistematică a venelor suprahepatice, a permeabilității venei porte și a foselor hepatorenale (Morison) și splenorenale pentru lichid liber.",
        },
    },
    # 2. Ecografie Renală Adulți DHMC
    {
        "file_path": ROOT / "docs" / "eco" / "abdomen-pelvis" / "eco-rinichi-nativi-adult-dartmouth.md",
        "fm": {
            "title": "Ecografie Renală Adulți - Rinichi Nativi (Protocol Procedural DHMC #11182)",
            "author": AUTHOR_DHMC,
            "category": "abdomen-pelvis",
            "last_updated": DATE_NOW,
            "clinical_indications": [
                "Colică renală sau suspiciune de litiază renoureterală / nefrolitiază",
                "Insuficiență renală acută sau cronică (evaluarea mărimii renale și a grosimii corticalei)",
                "Hematurie macroscopică sau microscopică inexplicabilă",
                "Infecții de tract urinar repetate (pielonefrită) sau suspiciune de abces renal",
                "Evaluarea și clasificarea formațiunilor chistice renale sau tumorilor solide",
            ],
            "contraindications": [
                "Fără contraindicații",
            ],
            "patient_prep": "Nu este necesar repaus alimentar strict, însă vezica urinară trebuie să fie confortabil destinsă (pacientul consumă 500–750 mL apă cu 1 oră înainte și nu urinează) pentru evaluarea joncțiunilor uretero-vezicale și a reziduului postmicțional.",
            "transducers_equipment": {
                "transducer_types": "Transductor convex broadband 2.5 – 5.0 MHz",
                "patient_position": "Decubit dorsal, decubite laterale drept și stâng pentru abord prin flanc / linia axilară posterioară",
                "gel_acoustic_window": "Gel ecografic abundent; folosirea ficatului pentru rinichiul drept și a splinei pentru rinichiul stâng ca ferestre acustice",
            },
            "technical_settings": {
                "frequency": "3.5 - 5.0 MHz",
                "gain": "Reglaj atent al amplificării pentru diferențierea ecogenității cortexului față de piramidele renale",
                "focus": "Focalizare pe complexul ecogen central și joncțiunea cortico-medulară",
                "doppler": "Doppler Color & Power Doppler pentru vascularizația parenchimatoasă și jeturile ureterale vezicale",
            },
            "standard_views": [
                {
                    "anatomical_region": "Rinichi Drept (Longitudinal & Transvers)",
                    "view_name": "Ax lung bipolar și stivă de secțiuni transverse (pol superior, mijloc hil, pol inferior)",
                    "landmarks": "Măsurare ax bipolar maxim în centimetri (N = 9.0 – 12.5 cm la adulți); evaluare contur și ecogenitate corticală (normal egală sau hipoecogenă față de ficat)",
                    "measurements": "Lungime bipolară, grosime parenchim cortical (N > 10–12 mm), calibru dilatație pielică dacă este prezentă",
                },
                {
                    "anatomical_region": "Rinichi Stâng (Longitudinal & Transvers)",
                    "view_name": "Ax lung bipolar și secțiuni transverse de la pol la pol",
                    "landmarks": "Abord intercostal posterior sau subcostal; măsurare lungime maximă (diferență între rinichi < 1.5 cm); comparare ecogenitate cu splina",
                    "measurements": "Lungime bipolară, grosime corticală",
                },
                {
                    "anatomical_region": "Vezică Urinară (Pre-micțională)",
                    "view_name": "Secțiuni transverse și sagitale suprapubiene",
                    "landmarks": "Simetrie perete vezical, grosime perete (N < 3–5 mm în repleție), absența calculilor sau maselor polipoide exofitice; evaluare Doppler a jeturilor ureterale",
                    "measurements": "Lungime, lățime, adâncime pentru calcul volum pre-micțional (V = 0.52 × L × W × H)",
                },
                {
                    "anatomical_region": "Vezică Urinară (Post-micțională)",
                    "view_name": "Secțiuni transverse și sagitale imediat după micțiune",
                    "landmarks": "Calcul reziduu vezical postmicțional (PVR). Normal la adult < 50 mL (< 100 mL la vârstnici)",
                    "measurements": "Volum rezidual postmicțional în mL",
                },
            ],
            "quality_criteria": [
                "Măsurarea axului lung renal în planul său anatomic oblic real, nu pe o secțiune scurtată falsă",
                "Gradarea hidronefrozei: Grad 1 (dilatare izolată a bazinetului), Grad 2 (ectazie caliceală fără atrofie), Grad 3 (dilatare caliceală marcată cu aplatizare papile), Grad 4 (subțiere severă a parenchimului cortical)",
                "Documentare obligatorie pre și post-micțională a vezicii conform normelor DHMC #11182",
            ],
            "safety_and_limitations": [
                "Litiază ureterală lombară mijlocie poate fi mascată de gazele digestive",
            ],
            "iris_reference": {
                "chapter": "Urologie & Nefrologie",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
            },
            "notes": "Protocolul Dartmouth Hitchcock #11182 impune compararea dimensiunilor celor doi rinichi (o diferență > 1.5–2.0 cm necesită investigarea unei stenoze de arteră renală sau a unei atrofii cronice congenitale/dobândite).",
        },
    },
    # 3. Ecografie Axilară & Biopsie Dartmouth
    {
        "file_path": ROOT / "docs" / "eco" / "san" / "eco-axila-biopsie-dartmouth.md",
        "fm": {
            "title": "Ecografie Axilară & Ghidaj Puncție Biopsie (Ghid Senologie Dartmouth)",
            "author": AUTHOR_DHMC,
            "category": "san",
            "last_updated": DATE_NOW,
            "clinical_indications": [
                "Evaluarea ganglionilor limfatici axilari la paciente cu suspiciune sau diagnostic confirmat de cancer mamar",
                "Aspect mamografic sau IRM suspect de adenopatie axilară (nodul dens, asimetrie, îngroșare corticală)",
                "Stadializare ganglionară locoregională pre-tratament chirurgical sau neoadjuvant",
                "Ghidaj ecografic în timp real pentru puncție aspirativă cu ac fin (FNAC) sau core biopsy cu plasare de clip",
            ],
            "contraindications": [
                "Tulburări majore de coagulare necorectate (INR > 1.5, trombocite < 50.000) în caz de procedură bioptică invazivă",
            ],
            "patient_prep": "Dezinfectare riguroasă a regiunii axilare. Pentru puncție biopsie: consimțământ informat, anestezie locală cu Lidocaină 1-2%, hemostază locală.",
            "transducers_equipment": {
                "transducer_types": "Transductor liniar de înaltă frecvență dedicat 10.0 – 18.0 MHz",
                "patient_position": "Decubit dorsal sau decubit oblic contralateral (la 30-45°), cu brațul ipsilateral ridicat deasupra capului pentru expunerea lojei axilare",
                "gel_acoustic_window": "Gel ecografic steril în caz de biopsie; compresie minimă pentru a nu colaba vasele din hil",
            },
            "technical_settings": {
                "frequency": "12.0 - 15.0 MHz",
                "gain": "Optimizat pentru structurile superficiale (profunzime 3-5 cm)",
                "focus": "Focalizare exactă pe ganglionul suspect",
                "doppler": "Doppler Color & Power Doppler cu PRF scăzut (2-5 cm/s) pentru a detecta vascularizația corticală excentrică",
            },
            "standard_views": [
                {
                    "anatomical_region": "Loja Axilară Nivelul I (Inferior & Lateral de Pectoralul Mic)",
                    "view_name": "Baleiere completă sagitală și transversă de-a lungul venei axilare",
                    "landmarks": "Vena axilară, mușchiul mare pectoral, mușchiul latissimus dorsi; identificarea ganglionilor anteriori, posteriori și laterali",
                    "measurements": "Grosime corticală maximă (N < 3.0 mm), raport ax lung / ax scurt (L/T)",
                },
                {
                    "anatomical_region": "Loja Axilară Nivelul II (Retropeitoral) & Nivelul III (Subclavicular)",
                    "view_name": "Orientare medială și cranială",
                    "landmarks": "În spatele și medial de mușchiul mic pectoral până la ligamentul costo-clavicular",
                    "measurements": "Număr de adenopatii suspecte, invazie capsulară extraganglionară",
                },
                {
                    "anatomical_region": "Ghidaj Biopsie / Puncție Core Needle",
                    "view_name": "Vizualizare longitudinală a acului 'in-plane' în timp real",
                    "landmarks": "Vârful acului avansat strict tangențial în porțiunea cea mai îngroșată a cortexului ganglionar, evitând pediculul hilar",
                    "measurements": "Poziția clipului de titan / marcare la finalul biopsiei",
                },
            ],
            "quality_criteria": [
                "Criterii Dartmouth de adenopatie axilară suspectă: îngroșare corticală focală sau concentrică > 3 mm, rotunjire ganglionară (L/T < 2), absența sau deplasarea hilului adipos central, hiperemie vasculară periferică non-hilară",
                "Verificarea traiectului acului fără risc de penetrare a vaselor mari axilare sau a peretelui toracic (risc de pneumotorax)",
                "Radiografie mamografică de control după plasarea clipului metalic pentru confirmarea poziției",
            ],
            "safety_and_limitations": [
                "Compresiune locală fermă minim 5-10 minute post-puncție pentru prevenirea hematomului",
            ],
            "iris_reference": {
                "chapter": "Senologie & Mamografie",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Unde Mecanice - Ultrasunete)",
            },
            "notes": "Conform ghidului Dartmouth Senologie 2024–2026, biopsia ganglionară axilară ghidată ecografic se efectuează obligatoriu dacă mamografia, ecografia sau IRM-ul evidențiază adenopatie suspectă la pacientele cu suspiciune de neoplazie mamară, determinând strategia de limfadenectomie vs. biopsie de ganglion santinelă.",
        },
    },
]

# ==============================================================================
# 4. PROTOCOALE RADIOGRAFIE (RX) DARTMOUTH
# ==============================================================================

RX_PROTOCOLS = [
    # 1. RX Pediatric Trauma X (Skeletal Survey)
    {
        "file_path": ROOT / "docs" / "rx" / "pediatrie" / "rx-trauma-x-pediatric-dartmouth.md",
        "fm": {
            "title": "Radiografie Pediatrică Trauma X - Skeletal Survey (Protocol DHMC)",
            "author": AUTHOR_DHMC,
            "category": "pediatrie",
            "last_updated": DATE_NOW,
            "modality": "rx",
            "clinical_indications": [
                "Suspiciune de traumatism non-accidental (NAT / Child Abuse / Abuz Infantil)",
                "Copil sub vârsta de 2 ani cu fractură inexplicabilă, hemoragie intracraniană sau leziuni cutanate suspecte",
                "Bilanț complet al scheletului pentru identificarea leziunilor oculte și a fracturilor cu vechimi diferite",
                "Fracturi caracteristice de înaltă specificitate: fracturi metafizare colțar (corner fracture / bucket-handle), fracturi de arcuri costale posterioare, fracturi scapulare sau sternale",
            ],
            "contraindications": [
                "Nu există contraindicații absolute în fața suspiciunii clinice de abuz",
            ],
            "patient_prep": "Studiul se efectuează de preferat în timpul orelor de program (8:00 - 17:00) cu tehnicieni experimentați. Părinții NU au voie să însoțească copilul în camera de examinare și NU vor participa la contenție (se utilizează asistenți medicali dedicați).",
            "distance_sid": "100 - 110 cm (DFF / SID standard)",
            "technical_parameters": {
                "kv": "50 - 65 kVp (adaptat la greutatea sugarului)",
                "mas": "1.5 - 4.0 mAs",
                "grid": "FĂRĂ grilă antidifuzoare la sugari și copii mici (reduce doza la 1/3 conform Image Gently)",
                "focal_spot": "Focar mic (Fine Focus)",
                "aec_chambers": "Manual prestabilit conform greutății copilului",
                "collimation": "Colimare strictă colimată pe fiecare segment anatomic (NICIODATĂ radiografii de ansamblu tip 'babygram')",
                "filtration": "Filtrare adițională cupru/aluminiu pentru reducerea radiației moi",
            },
            "projections": [
                {
                    "name": "Craniu AP & Profil (2 incidențe)",
                    "patient_position": "Decubit dorsal, cap imobilizat simetric",
                    "projection_details": "Proiecție antero-posterioară și laterală strictă a calvariei",
                    "central_ray": "Perpendicular pe centrul cutiei craniene",
                    "collimation": "Limitele osoase ale cutiei craniene",
                    "respiration": "Imobilitate",
                    "notes": "Detecție fracturi liniare, diastază suturală sau fracturi deprimante",
                },
                {
                    "name": "Torace AP & Oblice Bilaterale (3 incidențe)",
                    "patient_position": "Decubit dorsal, brațele ridicate ușor",
                    "projection_details": "AP torace centrat pe mediastin + incidențe oblice dreapta și stânga pentru arcurile costale",
                    "central_ray": "Nivelul T4-T5 pe linia mediană",
                    "collimation": "Apexuri pulmonare până la diafragm, incluzând claviculele",
                    "respiration": "Inspir dacă este posibil",
                    "notes": "Căutarea calusurilor osoase pe arcurile costale posterioare (semn patognomonic de strivire toracică)",
                },
                {
                    "name": "Coloană Vertebrală Profil (Cervicală, Toracică, Lombară)",
                    "patient_position": "Decubit lateral strict",
                    "projection_details": "Coloană cervicală profil, coloană toraco-lombară profil",
                    "central_ray": "Perpendicular pe axul vertebral",
                    "collimation": "Strict pe coloana vertebrală",
                    "respiration": "Imobilitate",
                    "notes": "Detecție tasări vertebrale, luxații sau fracturi de procese spinoase",
                },
                {
                    "name": "Bazin AP (Pelvis)",
                    "patient_position": "Decubit dorsal, membre inferioare în extensie",
                    "projection_details": "AP bazin incluzând ambele articulații coxofemurale",
                    "central_ray": "Linia mediană la jumătatea distanței între SIAS și simfiza pubiană",
                    "collimation": "Creste iliace până la treimea superioară a femurului",
                    "respiration": "Imobilitate",
                    "notes": "Excludere fracturi de ramuri pubiene sau fracturi metafizare proximale",
                },
                {
                    "name": "Membre Superioare AP Separate (4 incidențe)",
                    "patient_position": "Decubit dorsal",
                    "projection_details": "Humerus drept AP, Humerus stâng AP, Antebraț drept AP, Antebraț stâng AP + mâini separate",
                    "central_ray": "Centrat pe mijlocul fiecărui segment",
                    "collimation": "Strictă pe osul lung respectiv, incluzând articulația proximală și distală",
                    "respiration": "Imobilitate",
                    "notes": "Detecție leziuni metafizare clasice (CML / colțar)",
                },
                {
                    "name": "Membre Inferioare AP Separate (4 incidențe)",
                    "patient_position": "Decubit dorsal",
                    "projection_details": "Femur drept AP, Femur stâng AP, Gambă dreaptă AP, Gambă stângă AP + picioare separate",
                    "central_ray": "Centrat pe diafiză",
                    "collimation": "Strictă pe segmentul examinat",
                    "respiration": "Imobilitate",
                    "notes": "Leziuni metafizare distale femurale și tibiale proximale",
                },
            ],
            "quality_criteria": [
                "Fiecare segment osos trebuie radiografiat separat cu colimare strictă — interzis 'babygram' complet pe un singur film!",
                "Toate imaginile se revizuiesc imediat de către medicul radiolog specialist înainte de externarea pacientului",
                "Repetarea examenului (Follow-up skeletal survey) la 2 săptămâni pentru evidențierea calusului osos la leziunile inițial oculte",
            ],
            "radiation_protection": [
                "Utilizarea de protecție gonadică cu plumb atunci când nu maschează bazinul",
                "Fără grilă antidifuzoare pentru pacienți pediatrici mici conform recomandărilor Image Gently",
                "Echipament de protecție individuală pentru asistentul medical ce realizează contenția",
            ],
            "iris_reference": {
                "chapter": "Pediatrie Radiologică",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 2 (Scăzută 1 - 5 mSv)",
            },
            "notes": "Protocolul Dartmouth Trauma X urmează cele mai stricte ghiduri internaționale ACR-SPR pentru protecția copilului. Notificarea imediată a echipei clinice de protecție a copilului este obligatorie în caz de imagini suspecte.",
        },
    },
    # 2. RX Torace Diagnostic Dartmouth
    {
        "file_path": ROOT / "docs" / "rx" / "torace" / "rx-torace-diagnostic-dartmouth.md",
        "fm": {
            "title": "Radiografie Toracică Diagnostică (Protocol Tehnic DHMC)",
            "author": AUTHOR_DHMC,
            "category": "torace",
            "last_updated": DATE_NOW,
            "modality": "rx",
            "clinical_indications": [
                "Tuse persistentă, febră, dispnee, hemoptizie, durere toracică",
                "Suspiciune de pneumonie, revărsat lichidian pleural, pneumotorax, edem pulmonar",
                "Bilanț preoperator sau evaluare post-traumatism toracic închis",
                "Control poziționare catetere venoase centrale, tuburi de drenaj pleural, tub endotraheal",
            ],
            "contraindications": [
                "Sarcină (se utilizează șorț de plumb pelvin dacă investigația este strict justificată medical)",
            ],
            "patient_prep": "Îndepărtarea hainelor până la brâu, a colierelor, lănțișoarelor și obiectelor metalice. Părul lung prins deasupra umerilor.",
            "distance_sid": "180 cm (72 inch) — DFF obligatorie pentru reducerea măririi optice a cordului",
            "technical_parameters": {
                "kv": "110 - 125 kVp (Tehnică de tensiune înaltă)",
                "mas": "2.0 - 5.0 mAs (ajustat automat prin AEC)",
                "grid": "Grilă antidifuzoare focalizată raport 10:1 sau 12:1",
                "focal_spot": "Focar mare (Broad Focus)",
                "aec_chambers": "Camerele laterale active pentru PA; camera centrală activă pentru profil",
                "collimation": "De la C7/apexuri până sub unghiurile costodiafragmatice",
                "filtration": "Filtrare totală minim 2.5 mm Al",
            },
            "projections": [
                {
                    "name": "Torace Postero-Anterior (PA) în Ortostatism",
                    "patient_position": "Ortostatism, pieptul lipit de stativul vertical Bucky, umerii rotiți anterior cu dosul palmelor pe șolduri",
                    "projection_details": "Raza intră posterior la nivel T7 și iese anterior pe centrul receptorului",
                    "central_ray": "Orizontal, perpendicular pe receptor, centrat la nivelul unghiului inferior al scapulelor (T7)",
                    "collimation": "Deasupra umerilor până sub cupolele diafragmatice",
                    "respiration": "Apnee inspiratorie profundă la a doua comandă inspiratorie completă",
                    "notes": "Rotația coatelor anterior proiectează scapulele în afara câmpurilor pulmonare",
                },
                {
                    "name": "Torace Profil Stâng în Ortostatism",
                    "patient_position": "Ortostatism, profil stâng lipit de stativ, brațele ridicate deasupra capului sau încrucișate",
                    "projection_details": "Raza intră prin flancul drept și iese prin flancul stâng",
                    "central_ray": "Orizontal, centrat la nivel T7 în planul medio-coronal",
                    "collimation": "Contur toracic complet",
                    "respiration": "Apnee inspiratorie completă",
                    "notes": "Profilul stâng plasează cordul mai aproape de detector, minimizând mărirea siluetei cardiace",
                },
            ],
            "quality_criteria": [
                "Inspir profund demonstrat prin vizualizarea a cel puțin 9-10 arcuri costale posterioare deasupra diafragmului",
                "Simetrie toracică demonstrată prin distanțe egale de la extremitățile mediale ale claviculelor la linia proceselor spinoase",
                "Penetrare optimă la kVp înalt: desenul vascular retrocardiac și conturul coloanei toracice vizibile discret prin silueta cardiacă",
                "Vizualizarea clară a ambelor unghiuri costodiafragmatice și a apexurilor",
            ],
            "radiation_protection": [
                "Colimare strictă pe aria pulmonară",
                "Distanță focar-film de 180 cm ce reduce doza la tegument",
                "Optimizare automată a expunerii cu celule de ionizare AEC",
            ],
            "iris_reference": {
                "chapter": "Torace & Pulmon",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 1 (Minimă < 1 mSv / ~0.02 mSv)",
            },
            "notes": "Revizia tehnică Dartmouth Diagnostic Radiology reconfirmă utilizarea tehnicii de înalt voltaj (110–125 kVp) cu grilă Bucky pentru a asigura o penetrare optimă a mediastinului, reducând totodată doza absorbită la nivelul cutiei toracice.",
        },
    },
]

# ==============================================================================
# 5. GHID INSTITUȚIONAL DARTMOUTH GEISEL
# ==============================================================================

def generate_dartmouth_institution_guide() -> Path:
    target_file = ROOT / "docs" / "for-institutions" / "dartmouth-geisel-protocols.md"
    content = f"""---
title: Protocoale Clinice & Ghiduri Tehnice Dartmouth Geisel (DHMC)
author: {AUTHOR_DHMC}
category: for-institutions
last_updated: '{DATE_NOW}'
---

# Protocoale Clinice, Standarde Tehnice & Criterii Imagistice Dartmouth Geisel (DHMC)

Ghid instituțional sinoptic al protocoalelor clinice și politicilor procedurale aplicate în cadrul **Department of Radiology — Dartmouth-Hitchcock Medical Center (DHMC)** și **Geisel School of Medicine at Dartmouth**. Acest compendiu integrează protocoalele oficiale de achiziție tomografică (CT), rezonanță magnetică (IRM), ecografie clinică (US), radiografie convențională și pediatrică (RX), precum și ghidul de senologie și administrare a contrastului oral 2026.

<div class="iris-official-banner" style="margin-bottom: 24px; background: linear-gradient(135deg, #04452a 0%, #00693e 100%); color: #ffffff; padding: 18px 24px; border-radius: 8px;">
  <div class="iris-official-badge" style="background: rgba(255,255,255,0.2); color: #fff; padding: 4px 10px; border-radius: 4px; display: inline-block; font-weight: 700; font-size: 0.85rem; margin-bottom: 8px;">🌲 PROTOCOALE INSTITUȚIONALE DHMC / DARTMOUTH GEISEL</div>
  <p class="iris-official-desc" style="margin-bottom: 12px !important; color: #f0fdf4; font-size: 0.95rem; line-height: 1.5;">
    Protocoale oficiale clinice și ghiduri tehnice actualizate 2025–2026, gestionate de <strong>Departamentul de Radiologie al Dartmouth-Hitchcock Medical Center</strong> pentru asigurarea excelenței diagnostice, standardizării parametrilor fizici și protecției pacienților.
  </p>
  <a href="{DARTMOUTH_BASE_URL}" target="_blank" rel="noopener" style="font-weight: 600; color: #a7f3d0; text-decoration: none;">
    Consultă portalul oficial Dartmouth Geisel Radiology Policies &amp; Protocols ➔
  </a>
</div>

---

## 1. Sinteza Categoriilor de Protocoale Dartmouth Geisel

| Categorie Imagistică | Număr Pagini Sursă | Mod de Scanare / Echipamente | Documente de Referință DHMC |
|:----------------------|:------------------:|:-----------------------------|:----------------------------|
| **Tomografie Computerizată (CT) Abdomen & Pelvis** | 44 pagini | Multidetector CT (MDCT 64–128 slice), Split-Bolus, DIEP Flap | [Body-CT-Protocols.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2026/07/Body-CT-Protocols.pdf) |
| **Ghid Contrast Oral CT 2026** | 13 pagini | Consens ACR/SAR/AGA 2024–2026 | [CT-Oral-Contrast-Use-2026.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2026/08/CT-Oral-Contrast-Use-2026.pdf) |
| **Tomografie Computerizată (CT) Torace & Cord** | 33 pagini | Gated ECG, TAVR, Pectus Excavatum, Disecție Aortă | [Chest-CT-Protocols.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2026/07/Chest-CT-Protocols.pdf) |
| **Tomografie Computerizată (CT) Neuroradiologie** | 32 pagini | CTA Carotide & Poligon Willis, Traumă Facială, AVC acut | [Neuro-CT-Protocols.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2026/07/Neuro-CT-Protocols.pdf) |
| **CT Musculoscheletal (MSK) & Reformatare** | 124 pagini | IMAR (Reducere artefacte metal), Dual Energy | [MSK-Protocols.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2022/03/MSK-Protocols.pdf) |
| **CT Pediatric (Pedi Protocols)** | 104 pagini | Protocoale dedicate adaptate greutății | [pedi_protocols.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2019/03/pedi_protocols.pdf) |
| **Colonoscopie Virtuală (CTC Prep)** | 2 pagini | Protocol GoLytely cu Stool Tagging | [CT_colonography.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2019/04/CT_colonography.pdf) |
| **Rezonanță Magnetică (IRM) Abdomen & Pelvis** | 42 pagini | Siemens 1.5T & 3T, Fistulă Anală 3T, Ficat, MRCP | [MRI-BODY-PROTOCOL-BOOK-04-24-26.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2026/04/MRI-BODY-PROTOCOL-BOOK-04-24-26.pdf) |
| **Cardio-IRM (Cardiac Protocol Book)** | 66 pagini | CINE bSSFP, LGE Viabilitate, Valvulopatii, Rădăcină Aortă | [MRI-CARDIAC-PROTOCOL-BOOK-04-24-26.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2026/04/MRI-CARDIAC-PROTOCOL-BOOK-04-24-26.pdf) |
| **IRM Mamar & Fast Screening** | 7 pagini | Protocol Bilateral Dinamic & IRM Abreviat | [MRI-BREAST-PROTOCOL-BOOK-04-24-26.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2026/04/MRI-BREAST-PROTOCOL-BOOK-04-24-26.pdf) |
| **IRM Torace & Mediastin** | 9 pagini | Mase mediastinale, Angio-RM Aortă | [MRI-CHEST-PROTOCOL-BOOK-04-24-26.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2026/04/MRI-CHEST-PROTOCOL-BOOK-04-24-26.pdf) |
| **IRM Neuroradiologie & Plex Brahial** | 69 pagini | Plex Brahial, Protocol ARIA, Baza Craniului | [MRI-NEURO-PROTOCOL-BOOK-04-24-26.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2026/04/MRI-NEURO-PROTOCOL-BOOK-04-24-26.pdf) |
| **Ecografie Generală & Organe Specifice** | 73 pagini | Ghid Procedural DHMC (Abdomen #11184, Rinichi #11182) | [Ultrasound_Protocols_DHMC.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2026/05/Ultrasound_Protocols_DHMC.pdf) |
| **Radiografie Convențională (DX 2025/2026)** | 45 pagini | Proiecții standardizate, Tehnici kVp înalt | [DX-Protocol-2025-Updated.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2025/12/DX-Protocol-2025-Updated.pdf) |
| **Radiografie Pediatrică Trauma X** | 14 pagini | Bilanț scheletic complet (Skeletal Survey NAT) | [protocol_trauma_x.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2019/03/protocol_trauma_x.pdf) |
| **Ghid Diagnostic Senologie & Biopsie Axilă** | 3 documente | Criterii mamografice, ecografie axilară și puncție | [Diagnostic-Work-Up-Guidelines.pdf](https://geiselmed.dartmouth.edu/radiology/wp-content/uploads/sites/47/2025/09/Diagnostic-Work-Up-Guidelines8.18.25.pdf) |

---

## 2. Ghidul Clinic Dartmouth 2026 pentru Contrastul Oral în CT Abdomen/Pelvis

În conformitate cu consensul societăților internaționale de imagistică abdominală (**American College of Radiology - ACR**, **Society of Abdominal Radiology - SAR**, **American Gastroenterological Association - AGA**), Departamentul de Radiologie Dartmouth Geisel a revizuit radical recomandările privind administrarea substanței de contrast pe cale orală:

### 2.1. Când este INDISPENSABIL Contrastul Oral
1. **Pacienți postoperatori:** suspiciune de dehiscență de anastomoză digestivă, scurgere anastomotică (anastomotic leak), abces delimitat sau fistulă enterocutanată (se administrează contrast hidrosolubil Gastrografin / Omnipaque oral).
2. **Pacienți cașectici / BMI foarte scăzut (< 18.5 kg/m²):** absența grăsimii intraperitoneale îngreunează diferențierea anselor colabate de mase sau adenopatii.
3. **Suspiciune de fistulă enterovezicală sau enterovaginală:** opacifierea anselor demonstrează traiectul fistulos.
4. **Enterografie CT (Entero-CT):** administrare obligatorie de contrast neutru/volumic (PEG / Sorbitol) pentru destinderea anselor ileale în boala Crohn.

### 2.2. Când NU este Recomandat Contrastul Oral (Eliminat din Rutină)
- **Hemoragie digestivă acută:** contrastul oral pozitiv maschează extravazarea activă a contrastului intravenos în lumenul digestiv (semnul de blush arterial).
- **Colică renală / litiază urinară:** protocol nativ strict fără contrast.
- **Traumatism abdominal acut:** întârzierea scanării pentru băutul contrastului este periculoasă, iar contrastul oral crește riscul de aspirație bronșică.
- **Ischemie mezenterică acută:** contrastul oral împiedică aprecierea edemului parietal și a lipsei de captare a mucoasei intestinale.
- **Diverticulită acută necomplicată, colică biliară, pancreatită acută:** contrastul intravenos în fază venoasă portală este suficient pentru diagnostic.

---

## 3. Tehnici Speciale & Inovații Procedurale Dartmouth Hitchcock

### 3.1. Tehnica Split-Bolus în Ischemia Mezenterică
Pentru a obține simultan opacifierea de înaltă densitate a arterei mezenterice superioare (AMS) și a trunchiului celiac, precum și încărcarea venoasă mezenterică și parietală optimă pe o singură scanare, Dartmouth aplică protocolul split-bolus:
- Se injectează **100 mL contrast** la 4.0 mL/s;
- Se menține o pauză de **25 secunde**;
- Se injectează restul de **50 mL contrast** la 4.0 mL/s cu declanșare automată Smart Prep pe aorta abdominală;
- Scanarea acoperă abdomenul și pelvisul în apnee inspiratorie.

### 3.2. Pregătirea Termică & Măsuri Tehnice pentru DIEP Flap
În vederea cartografierii preoperatorii a perforantelor din artera epigastrică inferioară profundă (DIEP):
- Se plasează o **pătură caldă pe abdomen** înainte de scanare pentru a preveni vasoconstricția indusă de temperatura scăzută din sala tomografului;
- Se îndepărtează orice piesă de lenjerie intimă sau bandaj elastic pentru a evita compresia vasculară pe tegument;
- Scanarea se efectuează în direcție **caudo-cranială** (de la nivel inghinal spre diafragm), potrivindu-se perfect cu înaintarea bolusului de contrast arterial.

### 3.3. Screening IRM Mamar Abreviat (Fast Breast MRI)
Pentru a răspunde provocării reprezentate de sensibilitatea redusă a mamografiei în cazul sânilor denși (ACR C și D), Dartmouth a implementat protocolul de IRM mamar abreviat:
- Durata examinării în magnet este redusă la sub **10 minute**;
- Se achiziționează o secvență T2 FS, o secvență T1 VIBE FS nativă și o singură achiziție post-contrast la 90–120 secunde;
- Scăderea digitală automată (Subtraction) și proiecția de intensitate maximă (MIP) permit radiologului să formuleze un rezultat negativ în mai puțin de 1 minut, oferind o metodă eficientă și accesibilă de screening.

---

## 4. Protocoale Dartmouth Disponibile în Aplicație

Puteți consulta fișele complete de protocol, cu tab-uri interactive, parametri tehnici, tabele de reconstrucție și ghidaj IRIS accesând linkurile directe:

### Tomografie Computerizată (CT)
- [:material-file-document: CTA Disecție Aortă Toracică (Protocol Dartmouth Hitchcock)](../ct/chest/ct-cta-thorax-dissection-dartmouth.md)
- [:material-file-document: CTA Planificare TAVR / TAVI (Protocol Dartmouth Hitchcock)](../ct/chest/ct-cta-tavr-dartmouth.md)
- [:material-file-document: CT Torace Pectus Excavatum (Protocol Dartmouth Hitchcock)](../ct/chest/ct-pectus-excavatum-dartmouth.md)
- [:material-file-document: CTA Ischemie Mezenterică - Split Bolus (Protocol Dartmouth Hitchcock)](../ct/abdomen/ct-cta-mesenteric-ischemia-dartmouth.md)
- [:material-file-document: CTA Abdomen & Pelvis DIEP Flap (Protocol Dartmouth Hitchcock)](../ct/abdomen/ct-cta-dieap-flap-dartmouth.md)
- [:material-file-document: CT Colonografie Virtuală - Pregătire & Scanare (Protocol Dartmouth Hitchcock)](../ct/abdomen/ct-colonography-virtual-dartmouth.md)
- [:material-file-document: Ghid Clinic Administrare Contrast Oral CT Abdomen/Pelvis 2026](../ct/abdomen/ct-oral-contrast-guidelines-dartmouth.md)
- [:material-file-document: CTA Carotide și Poligonul lui Willis (Protocol Dartmouth Hitchcock)](../ct/neuro/ct-cta-carotids-circle-of-willis-dartmouth.md)
- [:material-file-document: CT Masiv Facial Traumă (Protocol Dartmouth Hitchcock)](../ct/neuro/ct-face-trauma-dartmouth.md)

### Rezonanță Magnetică (IRM)
- [:material-file-document: IRM Abdomen Rutină Nativ & cu Contrast (Protocol DHMC)](../irm/abdomen-pelvis/irm-abdomen-basic-dartmouth.md)
- [:material-file-document: IRM Fistulă Perianală 3T (Protocol Dedicat DHMC)](../irm/abdomen-pelvis/irm-fistula-perianala-dartmouth.md)
- [:material-file-document: IRM Cardiac Funcție & Viabilitate LGE (Protocol DHMC)](../irm/cardiac/irm-cardiac-rutina-viabilitate-dartmouth.md)
- [:material-file-document: IRM Mamar Bilateral Nativ & Dinamic (Protocol DHMC)](../irm/san/irm-mamar-bilateral-dartmouth.md)
- [:material-file-document: IRM Mamar Abreviat Fast Screening (Protocol Dartmouth Hitchcock)](../irm/san/irm-mamar-abreviat-screening-dartmouth.md)
- [:material-file-document: IRM Plex Brahial Nativ & cu Contrast (Protocol DHMC)](../irm/neuro/irm-plex-brahial-dartmouth.md)

### Ecografie & Ultrasonografie (ECO / US)
- [:material-file-document: Ecografie Abdominală Completă (Protocol Procedural DHMC #11184)](../eco/abdomen-pelvis/eco-abdomen-complet-dartmouth.md)
- [:material-file-document: Ecografie Renală Adulți - Rinichi Nativi (Protocol Procedural DHMC #11182)](../eco/abdomen-pelvis/eco-rinichi-nativi-adult-dartmouth.md)
- [:material-file-document: Ecografie Axilară & Ghidaj Puncție Biopsie (Ghid Senologie Dartmouth)](../eco/san/eco-axila-biopsie-dartmouth.md)

### Radiografie Convențională & Pediatrică (RX)
- [:material-file-document: Radiografie Pediatrică Trauma X - Skeletal Survey (Protocol DHMC)](../rx/pediatrie/rx-trauma-x-pediatric-dartmouth.md)
- [:material-file-document: Radiografie Toracică Diagnostică (Protocol Tehnic DHMC)](../rx/torace/rx-torace-diagnostic-dartmouth.md)
"""
    target_file.write_text(content, encoding="utf-8")
    print(f"Generat ghid instituțional: {target_file}")
    return target_file


def main():
    print("=== Generare Protocoale Dartmouth Geisel (DHMC) ===")
    
    # 1. CT
    print(f"\n--- Generare protocoale CT ({len(CT_PROTOCOLS)}) ---")
    for item in CT_PROTOCOLS:
        doc = render_document(item["fm"])
        item["file_path"].parent.mkdir(parents=True, exist_ok=True)
        item["file_path"].write_text(doc, encoding="utf-8")
        print(f"  + CT: {item['file_path'].name}")

    # 2. IRM
    print(f"\n--- Generare protocoale IRM ({len(IRM_PROTOCOLS)}) ---")
    for item in IRM_PROTOCOLS:
        doc = render_irm_document(item["fm"])
        item["file_path"].parent.mkdir(parents=True, exist_ok=True)
        item["file_path"].write_text(doc, encoding="utf-8")
        print(f"  + IRM: {item['file_path'].name}")

    # 3. ECO
    print(f"\n--- Generare protocoale ECO ({len(ECO_PROTOCOLS)}) ---")
    for item in ECO_PROTOCOLS:
        doc = render_eco_document(item["fm"])
        item["file_path"].parent.mkdir(parents=True, exist_ok=True)
        item["file_path"].write_text(doc, encoding="utf-8")
        print(f"  + ECO: {item['file_path'].name}")

    # 4. RX
    print(f"\n--- Generare protocoale RX ({len(RX_PROTOCOLS)}) ---")
    for item in RX_PROTOCOLS:
        doc = render_rx_document(item["fm"])
        item["file_path"].parent.mkdir(parents=True, exist_ok=True)
        item["file_path"].write_text(doc, encoding="utf-8")
        print(f"  + RX: {item['file_path'].name}")

    # 5. Ghid Instituțional
    print(f"\n--- Generare ghid instituțional Dartmouth ---")
    generate_dartmouth_institution_guide()

    print("\nToate protocoalele Dartmouth au fost generate cu succes!")

if __name__ == "__main__":
    main()
