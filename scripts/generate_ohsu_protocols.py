#!/usr/bin/env python3
"""generate_ohsu_protocols.py — Generează protocoalele CT și IRM, precum și ghidul de politici clinice OHSU.

Sursă: Oregon Health & Science University (OHSU) — Department of Diagnostic Radiology
URL: https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/diagnostic-radiology-policies
MCN Policy Manager: https://ohsu.ellucid.com/home
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

OHSU_POLICY_URL = "https://www.ohsu.edu/school-of-medicine/diagnostic-radiology/diagnostic-radiology-policies"
OHSU_MCN_URL = "https://ohsu.ellucid.com/home"
IRIS_URL = "https://radiologie-pediatrica.ro/iris/"

# ==============================================================================
# 1. PROTOCOALE CT OHSU
# ==============================================================================

CT_PROTOCOLS = [
    {
        "file_path": ROOT / "docs" / "ct" / "abdomen" / "ct-abdomen-pelvis-ohsu.md",
        "fm": {
            "title": "CT Abdomen & Pelvis Rutină (Protocol OHSU)",
            "author": "OHSU Diagnostic Radiology / Departamentul de Radiologie",
            "category": "abdomen",
            "last_updated": "2026-09-20",
            "protocol_type": "contrast-enhanced",
            "clinical_indications": [
                "Dureri abdominale acute sau cronice de etiologie neprecizată",
                "Suspiciune de infecții intraabdominale, colecții sau abcese",
                "Diverticulită acută, apendicită sau patologie inflamatorie pelvină",
                "Monitorizare oncologică și stadializare neoplazică",
                "Ocluzie intestinală sau suspiciune de ischemie mezenterică",
            ],
            "position": "Decubit dorsal cu brațele ridicate deasupra capului",
            "npo": "Repaus alimentar 4 ore pentru alimente solide; hidratare orală permisă",
            "premedication": "Contrast oral (opțional conform indicației): 500-750 mL apă sau Readi-Cat 2 fracționat cu 30-45 min înainte de scanare",
            "contrast": {
                "agent": "Omnipaque 350 / Isovue 370",
                "volume": "100 mL (1.5 mL/kg, max 120 mL)",
                "flow_rate": "2.5 - 3.0 mL/s",
                "duration": "35-40s",
                "timing": "Timp empiric de întârziere 65-70 secunde (fază venoasă portală)",
                "roi": "N/A",
                "trigger": "N/A",
            },
            "tech_params": {
                "kv": "CAREkV (Ref 120 kV)",
                "mas": "CAREDose4D / SureExposure3D (Ref 180-220 mAs)",
                "slice_thickness": "0.625 mm",
                "rotation_time": "0.5 s",
                "pitch": "0.8 - 1.0",
                "scan_mode": "Elicoidal (Helical)",
                "collimation": "128 × 0.6 mm / 64 × 0.625 mm",
            },
            "series": [
                {
                    "name": "Fază Venoasă Portală",
                    "start": "Cupole diafragmatice",
                    "end": "Simfiză pubiană",
                    "delay": "65-70 sec",
                    "thickness": "0.625 mm",
                    "notes": "Achiziție în apnee inspiratorie completă; acoperire completă abdomen și pelvis",
                }
            ],
            "recons": [
                {
                    "plane": "Axial",
                    "acquisition": "Fază Venoasă Portală",
                    "fov": "Abdomen",
                    "thickness_increment": "3.0 mm / 3.0 mm",
                    "kernel": "Standard / I30f",
                    "ir_strength": "Admire 3 / AIDR 3D Standard",
                    "notes": "Serie diagnostică primară",
                },
                {
                    "plane": "Coronal",
                    "acquisition": "Fază Venoasă Portală",
                    "fov": "Abdomen",
                    "thickness_increment": "2.0 mm / 2.0 mm",
                    "kernel": "Standard / I30f",
                    "ir_strength": "Admire 3 / AIDR 3D Standard",
                    "notes": "Evaluare anatomică cranio-caudală a viscerelor și mezenterului",
                },
                {
                    "plane": "Sagital",
                    "acquisition": "Fază Venoasă Portală",
                    "fov": "Abdomen",
                    "thickness_increment": "2.0 mm / 2.0 mm",
                    "kernel": "Standard / I30f",
                    "ir_strength": "Admire 3 / AIDR 3D Standard",
                    "notes": "Relații topografice și anse digestive",
                },
            ],
            "notes": {
                "tech": "Verificați abordul venos periferic (20G preferat). Brațele complet ridicate deasupra capului pentru a preveni artefactele de beam-hardening. Ghidare respirație: apnee inspiratorie.",
                "rad": "Examinare sistematică a parenchimelor abdominale (ficat, splină, pancreas, rinichi, suprarenale), tractului digestiv, spațiilor peritoneale și retroperitoneale, ganglionilor și structurilor vasculare.",
                "nursing": "Canulă venoasă 20G în plica cotului. Verificare extravazare cu flush salin 20 mL înainte de injectarea contrastului.",
                "tips": "La pacienți tineri sau cu suspiciune de litiază urinară, se recomandă evaluare preliminară nativă cu doză ultra-joasă (ultra-low-dose).",
                "additional_recons": "Reconstrucții coronale și sagitale oblice la nevoie; secțiuni fine 1.0 mm pentru evaluare vasculară 3D MIP.",
            },
            "safety": {
                "allergy": "Screening conform politicii OHSU. Premedicație cu corticosteroizi + antihistaminice dacă pacientul are antecedente de reacție alergică la iod.",
                "renal": "Evaluare eGFR conform politicii OHSU. Dacă eGFR < 30 mL/min/1.73m², discutați cu medicul radiolog oportunitatea examinării sau hidratării.",
            },
        },
    },
    {
        "file_path": ROOT / "docs" / "ct" / "abdomen" / "ct-multiphase-liver-ohsu.md",
        "fm": {
            "title": "CT Ficat Multifazic Triphasic (Protocol OHSU)",
            "author": "OHSU Diagnostic Radiology / Departamentul de Radiologie",
            "category": "abdomen",
            "last_updated": "2026-09-20",
            "protocol_type": "multiphase",
            "clinical_indications": [
                "Caracterizare noduli și leziuni hepatice la pacienți cirotici (evaluare LI-RADS / suspiciune HCC)",
                "Evaluare leziuni hepatice hipervasculare (hiperplazie nodulară focală FNH, adenom hepatic, hemangiom atipic)",
                "Stadializare pre-transplant hepatic, rezecție chirurgicală sau ablație tumorală (RFA/MWA/TACE)",
                "Metastaze hepatice hipervasculare (tumori neuroendocrine, melanom, carcinom renal, carcinom tiroidian)",
            ],
            "position": "Decubit dorsal cu brațele ridicate deasupra capului",
            "npo": "Repaus alimentar 4 ore înainte de scanare; hidratare permisă",
            "premedication": "Contrast oral exclusiv apă (contrast neutru) 500 mL cu 15-20 min înainte de scanare (nu se utilizează bariu sau contrast iodat oral)",
            "contrast": {
                "agent": "Isovue 370 / Omnipaque 350",
                "volume": "125-150 mL (2 mL/kg)",
                "flow_rate": "4.0 - 5.0 mL/s",
                "duration": "25-30s",
                "timing": "Bolus tracking în aorta abdominală (trigger 150 HU la nivelul trunchiului celiac)",
                "roi": "Aorta abdominală la originea trunchiului celiac",
                "trigger": "150 HU (+15-18 sec delay pentru faza arterială tardivă)",
            },
            "tech_params": {
                "kv": "CAREkV (Ref 120 kV)",
                "mas": "CAREDose4D / SureExposure3D (Ref 200-240 mAs)",
                "slice_thickness": "0.625 mm",
                "rotation_time": "0.5 s",
                "pitch": "0.8 - 1.0",
                "scan_mode": "Elicoidal (Helical)",
                "collimation": "128 × 0.6 mm / 64 × 0.625 mm",
            },
            "series": [
                {
                    "name": "Fază Nativă (Ficat)",
                    "start": "Cupolă diafragmatică dreaptă",
                    "end": "Pol inferior hepatic",
                    "delay": "0 sec",
                    "thickness": "1.0 mm",
                    "notes": "Detectare hemoragii intratumorale, calcificări, depuneri de grăsime sau fier (hemocromatoză)",
                },
                {
                    "name": "Fază Arterială Tardivă",
                    "start": "Diafragm",
                    "end": "Creste iliace",
                    "delay": "Trigger + 15-18 sec",
                    "thickness": "0.625 mm",
                    "notes": "Spălare arterială (wash-in) a leziunilor hipervasculare (HCC, FNH, TNE)",
                },
                {
                    "name": "Fază Venoasă Portală",
                    "start": "Diafragm",
                    "end": "Simfiză pubiană",
                    "delay": "65-70 sec",
                    "thickness": "0.625 mm",
                    "notes": "Contrastare maximă parenchim hepatic normal; detectare metastaze hipovasculare și tromboză portală",
                },
                {
                    "name": "Fază Tardivă / Echilibru",
                    "start": "Cupolă diafragmatică",
                    "end": "Pol inferior hepatic",
                    "delay": "180 sec (3 min)",
                    "thickness": "1.0 mm",
                    "notes": "Spălare capsulară (wash-out) specifică HCC; persistență contrast în hemangioame și colangiocarcinom",
                },
            ],
            "recons": [
                {
                    "plane": "Axial",
                    "acquisition": "Toate fazele (Nativ, Arterial, Portal, Tardiv)",
                    "fov": "Ficat / Abdomen",
                    "thickness_increment": "2.5 mm / 2.5 mm",
                    "kernel": "Standard / I30f",
                    "ir_strength": "Admire 3 / AIDR 3D",
                    "notes": "Serii diagnostice de bază",
                },
                {
                    "plane": "Coronal",
                    "acquisition": "Fază Venoasă Portală & Arterială",
                    "fov": "Abdomen",
                    "thickness_increment": "2.0 mm / 2.0 mm",
                    "kernel": "Standard / I30f",
                    "ir_strength": "Admire 3 / AIDR 3D",
                    "notes": "Raport lezional cu venele suprahepatice și vena portă",
                },
            ],
            "notes": {
                "tech": "Injectare rapidă cu injector automat bifașic (contrast + flush salin 40 mL). Canulă 18-20G în plica cotului. Respectați strict temporizarea bolus tracking.",
                "rad": "Aplicați criteriile LI-RADS v2018 pentru fiecare leziune focală observată. Evaluați permeabilitatea trunchiului portal, ramurilor portale și venelor hepatice.",
                "nursing": "Monitorizare debit injectare. La viteze de 4-5 mL/s se va folosi exclusiv canulă certificată high-pressure.",
                "tips": "Apă orală administrată chiar înainte de examinare asigură o distensie gastrică excelentă fără a masca încărcarea arterială a lobului stâng.",
                "additional_recons": "Reconstrucții MIP și VR 3D pentru anatomia trunchiului celiac și arterei hepatice (pre-operator).",
            },
            "safety": {
                "allergy": "Screening conform politicii OHSU. Premedicație standard dacă există istoric de reacții alergice la substanțe iodate.",
                "renal": "eGFR > 30 mL/min obligatoriu. Hidratare i.v. recomandată pentru valori limitrofe (30-44 mL/min).",
            },
        },
    },
    {
        "file_path": ROOT / "docs" / "ct" / "abdomen" / "ct-enterography-ohsu.md",
        "fm": {
            "title": "CT Enterografie (Protocol OHSU)",
            "author": "OHSU Diagnostic Radiology / Departamentul de Radiologie",
            "category": "abdomen",
            "last_updated": "2026-09-20",
            "protocol_type": "contrast-enhanced",
            "clinical_indications": [
                "Boală Crohn suspectată sau cunoscută (evaluare activitate inflamatorie parietală, stenoze, fistule, abcese)",
                "Hemoragie digestivă obscură fără cauză identificată prin endoscopie și colonoscopie",
                "Suspiciune de tumori de intestin subțire (tumori carcinoide/TNE, polipi, limfom, adenocarcinom)",
                "Boală celiacă refractară, sindrom de malabsorbție neexplicat",
            ],
            "position": "Decubit dorsal cu brațele ridicate",
            "npo": "Repaus alimentar strict 6 ore înainte de scanare; lichide clare permise până la sosirea în departament",
            "premedication": "Protocol Contrast Oral Neutru VoLumen (1350 mL / 3 sticle a 450 mL): Sticla 1 cu 60 min înainte, Sticla 2 cu 40 min înainte, Sticla 3 cu 20 min înainte de scanare.",
            "contrast": {
                "agent": "Omnipaque 350 / Isovue 370",
                "volume": "100-125 mL",
                "flow_rate": "3.5 - 4.0 mL/s",
                "duration": "30-35s",
                "timing": "Fază enterică (45-50 secunde delay de la debutul injectării contrastului i.v.)",
                "roi": "N/A",
                "trigger": "N/A",
            },
            "tech_params": {
                "kv": "CAREkV (Ref 100-120 kV)",
                "mas": "CAREDose4D / SureExposure3D (Ref 180 mAs)",
                "slice_thickness": "0.625 mm",
                "rotation_time": "0.5 s",
                "pitch": "0.9 - 1.1",
                "scan_mode": "Elicoidal (Helical)",
                "collimation": "128 × 0.6 mm / 64 × 0.625 mm",
            },
            "series": [
                {
                    "name": "Fază Enterică",
                    "start": "Cupole diafragmatice",
                    "end": "Simfiză pubiană",
                    "delay": "45-50 sec",
                    "thickness": "0.625 mm",
                    "notes": "Opacifiere maximă a peretelui anselor intestinale pe fondul lumenului destins hipodens (VoLumen)",
                }
            ],
            "recons": [
                {
                    "plane": "Axial",
                    "acquisition": "Fază Enterică",
                    "fov": "Abdomen",
                    "thickness_increment": "2.0 mm / 2.0 mm",
                    "kernel": "Standard / I30f",
                    "ir_strength": "Admire 3 / AIDR 3D",
                    "notes": "Măsurare grosime parietală, edem submucos, stratificare parietală",
                },
                {
                    "plane": "Coronal",
                    "acquisition": "Fază Enterică",
                    "fov": "Abdomen",
                    "thickness_increment": "1.5 mm / 1.5 mm",
                    "kernel": "Standard / I30f",
                    "ir_strength": "Admire 3 / AIDR 3D",
                    "notes": "Plan de elecție pentru urmărirea traiectului anselor ileale și jejunale și semnul pieptenului (comb sign)",
                },
            ],
            "notes": {
                "tech": "Pacientul trebuie să bea întregul volum de contrast neutru (VoLumen 1350 mL) conform orarului. Injectare i.v. rapidă cu flush salin 40 mL.",
                "rad": "Evaluați îngroșarea parietală (> 3 mm la anse destinse), hiperemia mucoasă, edemul subseros, hipertrofia grăsimii fibrogrăsoase (creeping fat) și adenopatiile mezenterice.",
                "nursing": "Monitorizați toleranța pacientului la ingestia orală; în caz de greață, se poate administra un antiemetic ușor cu acordul medicului.",
                "tips": "Distensia adecvată a anselor este cheia diagnostică: fără contrast neutru suficient, ansele colabate pot mima patologie inflamatorie fals-pozitivă.",
                "additional_recons": "Reconstrucții 3D MIP coronale pentru vizualizarea vascularizației mezenterice (vase drepte dilatate).",
            },
            "safety": {
                "allergy": "Conform politicii OHSU. Premedicație dacă există reacții alergice anterioare.",
                "renal": "eGFR > 30 mL/min/1.73m².",
            },
        },
    },
    {
        "file_path": ROOT / "docs" / "ct" / "trauma" / "ct-pan-scan-trauma-ohsu.md",
        "fm": {
            "title": "CT Politraumă Pan-Scan Whole Body (Protocol OHSU)",
            "author": "OHSU Diagnostic Radiology / Departamentul de Radiologie",
            "category": "trauma",
            "last_updated": "2026-09-20",
            "protocol_type": "trauma",
            "clinical_indications": [
                "Politraumă majoră cu mecanism de înaltă energie cinetică (accidente rutiere de mare viteză, cădere > 3 metri)",
                "Pacient politraumatizat cu instabilitate hemodinamică sau alterare a conștienței (GCS < 13)",
                "Suspiciune de leziuni traumatice multisistemice (craniu, coloană cervicală, torace, abdomen, pelvis)",
                "Traumatism toraco-abdominal sever cu suspiciune de sângerare activă sau ruptură viscerală",
            ],
            "position": "Decubit dorsal, cap centrat în izocentru, brațele imobilizate inițial pe lângă corp pentru craniu/coloană, apoi ridicate dacă starea permite",
            "npo": "Urgență majoră — N/A",
            "premedication": "Fără premedicație orală — urgență de cod roșu/galben",
            "contrast": {
                "agent": "Isovue 370 / Omnipaque 350",
                "volume": "130-150 mL",
                "flow_rate": "3.5 - 4.0 mL/s",
                "duration": "35-40s",
                "timing": "65-70 secunde de la debutul injectării (fază venoasă portală/parenchimatoasă)",
                "roi": "N/A",
                "trigger": "N/A",
            },
            "tech_params": {
                "kv": "120 kV (sau CAREkV)",
                "mas": "CAREDose4D / SureExposure3D mod trauma",
                "slice_thickness": "0.625 mm",
                "rotation_time": "0.5 s",
                "pitch": "0.9 - 1.2",
                "scan_mode": "Elicoidal (Helical)",
                "collimation": "128 × 0.6 mm / 64 × 0.625 mm",
            },
            "series": [
                {
                    "name": "CT Craniu Nativ",
                    "start": "Baza craniului / gaura occipitală",
                    "end": "Vertex",
                    "delay": "0 sec",
                    "thickness": "1.0 mm",
                    "notes": "Detectare hematoame epidurale/subdurale, hemoragie subarahnoidiană, fracturi craniene",
                },
                {
                    "name": "CT Coloană Cervicală Nativ",
                    "start": "Baza craniului",
                    "end": "T1-T2",
                    "delay": "0 sec",
                    "thickness": "0.625 mm",
                    "notes": "Evaluare leziuni osteo-articulare, luxații, fracturi de corp vertebral sau arcuri posterioare",
                },
                {
                    "name": "CT Torace, Abdomen & Pelvis cu Contrast",
                    "start": "Vârfuri pulmonare",
                    "end": "Mici trohantere",
                    "delay": "65-70 sec",
                    "thickness": "0.625 mm",
                    "notes": "Detectare lacerații hepatice/splenice/renale, pneumotorax, hemotorax, extravazare activă de contrast (blush vascular)",
                },
            ],
            "recons": [
                {
                    "plane": "Axial",
                    "acquisition": "Craniu Nativ",
                    "fov": "Cap",
                    "thickness_increment": "3.0 mm / 3.0 mm",
                    "kernel": "Creier (H31s) + Osos (H60s)",
                    "ir_strength": "Standard",
                    "notes": "Fereastră de creier și fereastră osoasă",
                },
                {
                    "plane": "Sagital & Coronal",
                    "acquisition": "Coloană Cervicală",
                    "fov": "C-Spine",
                    "thickness_increment": "1.5 mm / 1.5 mm",
                    "kernel": "Osos (B60s)",
                    "ir_strength": "Standard",
                    "notes": "Aliniament coloană și stabilitate ligamentară",
                },
                {
                    "plane": "Axial, Coronal & Sagital",
                    "acquisition": "Torace, Abdomen & Pelvis",
                    "fov": "Torace / Abdomen",
                    "thickness_increment": "2.0 mm / 2.0 mm",
                    "kernel": "Parenchim (I30f) + Osos (I70f) + Pulmonar (I50f)",
                    "ir_strength": "Admire 3 / AIDR 3D",
                    "notes": "Fereastră mediastinală, pulmonară, parenchim abdominal și fereastră de os pentru bazin/coloană",
                },
            ],
            "notes": {
                "tech": "Scanare rapidă fără întârziere. Monitorizare semne vitale în sala de scanare. Brațele ridicate pentru achiziția toraco-abdominală dacă nu sunt contraindicații ortopedice.",
                "rad": "Verificare prioritară: 1) Leziuni intracraniene cu efect de masă; 2) Fracturi cervicale instabile; 3) Leziuni de aortă toracică; 4) Extravazare activă de contrast intraabdominală; 5) Fracturi de bazin instabile.",
                "nursing": "Canulă de calibru mare (18G). Pregătire echipament de resuscitare și hemostatice.",
                "tips": "În caz de blush vascular activ, se realizează o achiziție tardivă țintită la 3-5 minute pentru a diferenția pseudoanevrismul de sângerarea activă liberă.",
                "additional_recons": "Reconstrucții 3D VR pentru bazin și cutie toracică (fracturi costale multiple, volet costal).",
            },
            "safety": {
                "allergy": "În urgență vitală imediată, contrastul se administrează cu monitorizare atentă chiar dacă există istoric alergic, asigurând acces imediat la tratament de resuscitare.",
                "renal": "În traumă acută severă, beneficiul diagnosticului vital depășește riscul de nefrotoxicitate indusă de contrast.",
            },
        },
    },
    {
        "file_path": ROOT / "docs" / "ct" / "abdomen" / "ct-urogram-ohsu.md",
        "fm": {
            "title": "CT Urografie / Evaluare Hematurie (Protocol OHSU)",
            "author": "OHSU Diagnostic Radiology / Departamentul de Radiologie",
            "category": "abdomen",
            "last_updated": "2026-09-20",
            "protocol_type": "multiphase",
            "clinical_indications": [
                "Hematurie macroscopică nedureroasă sau hematurie microscopică asimptomatică persistentă",
                "Suspiciune de carcinom urotelial la nivelul calicelor, bazinetului, ureterelor sau vezicii urinare",
                "Litiază renală și ureterală complicată sau recidivantă cu obstrucție",
                "Traumatisme sau stenoze ale tractului urinar superior și inferior",
            ],
            "position": "Decubit dorsal",
            "npo": "Repaus alimentar 4 ore; hidratare orală permisă (500 mL apă înainte de scanare pentru distensie vezicală)",
            "premedication": "Fără contrast oral iodat sau baritat; hidratare per os cu apă",
            "contrast": {
                "agent": "Omnipaque 350 / Isovue 370",
                "volume": "100-120 mL (sau split-bolus)",
                "flow_rate": "3.0 mL/s",
                "duration": "35-40s",
                "timing": "Fază Nefrografică (100 sec) și Fază Excretorie Tardivă (10-12 min) sau protocol Split-Bolus",
                "roi": "N/A",
                "trigger": "N/A",
            },
            "tech_params": {
                "kv": "CAREkV (Ref 120 kV)",
                "mas": "CAREDose4D / SureExposure3D",
                "slice_thickness": "0.625 mm",
                "rotation_time": "0.5 s",
                "pitch": "0.9 - 1.1",
                "scan_mode": "Elicoidal (Helical)",
                "collimation": "128 × 0.6 mm / 64 × 0.625 mm",
            },
            "series": [
                {
                    "name": "Fază Nativă (Rinichi -> Pelvis)",
                    "start": "Pol superior renal",
                    "end": "Simfiză pubiană",
                    "delay": "0 sec",
                    "thickness": "1.0 mm",
                    "notes": "Detectare calculi renali și ureterali radio-opaci fără mascare de către contrast",
                },
                {
                    "name": "Fază Nefrografică",
                    "start": "Diafragm",
                    "end": "Creste iliace",
                    "delay": "100 sec",
                    "thickness": "0.625 mm",
                    "notes": "Omogenitate maximă parenchimatoasă renală; detecție mase renale corticale și medulare",
                },
                {
                    "name": "Fază Excretorie Tardivă",
                    "start": "Pol superior renal",
                    "end": "Simfiză pubiană",
                    "delay": "10-12 min",
                    "thickness": "0.625 mm",
                    "notes": "Opacifiere completă calice, bazinete, uretere pe tot traiectul și vezică urinară; detectare defecte de umplere uroteliale",
                },
            ],
            "recons": [
                {
                    "plane": "Axial",
                    "acquisition": "Nativ, Nefrografic & Excretor",
                    "fov": "Abdomen / Bazin",
                    "thickness_increment": "2.5 mm / 2.5 mm",
                    "kernel": "Standard / I30f",
                    "ir_strength": "Admire 3 / AIDR 3D",
                    "notes": "Serii de bază",
                },
                {
                    "plane": "Coronal",
                    "acquisition": "Fază Excretorie",
                    "fov": "Tract Urinar",
                    "thickness_increment": "2.0 mm / 2.0 mm",
                    "kernel": "Standard / I30f",
                    "ir_strength": "Admire 3 / AIDR 3D",
                    "notes": "Evaluare anatomică de ansamblu a arborelui pielo-ureteral",
                },
            ],
            "notes": {
                "tech": "Pacientul trebuie să evite micțiunea în perioada de așteptare dintre faza nefrografică și faza tardivă excretorie pentru a permite umplerea vezicii urinare.",
                "rad": "Căutați defecte de umplere uroteliale fixe, îngroșări parietale ureterale, asimetrii de excreție și calculi obstructivi.",
                "nursing": "Canulă 20G. Supraveghere pacient în intervalul de 10 minute premergător fazei excretorii.",
                "tips": "Pentru a reduce doza de radiație la pacienți tineri, se poate utiliza tehnica Split-Bolus: 30-40 mL contrast i.v. inițial, pauză 10 minute, apoi 80 mL contrast și scanare la 100 secunde (obținând o fază combinată nefrografică + excretorie într-o singură scanare).",
                "additional_recons": "Reconstrucții Coronal MIP 3D 'urografie CT' din faza excretorie pentru vizualizare completă tip urografie clasică.",
            },
            "safety": {
                "allergy": "Screening conform politicii OHSU.",
                "renal": "eGFR > 30 mL/min/1.73m² obligatoriu.",
            },
        },
    },
    {
        "file_path": ROOT / "docs" / "ct" / "chest" / "ct-pulmonary-embolism-ohsu.md",
        "fm": {
            "title": "CT Angiografie Pulmonară / TEP (Protocol OHSU)",
            "author": "OHSU Diagnostic Radiology / Departamentul de Radiologie",
            "category": "chest",
            "last_updated": "2026-09-20",
            "protocol_type": "contrast-enhanced",
            "clinical_indications": [
                "Suspiciune de trombembolism pulmonar acut (TEP)",
                "Scor Wells sau Geneva intermediar sau înalt, sau D-dimeri pozitivi",
                "Dispnee acută inexplicabilă, durere toracică pleuritică, hemoptizie, sincope",
                "Evaluare hipertensiune pulmonară cronică trombembolică (CTEPH)",
            ],
            "position": "Decubit dorsal cu brațele ridicate complet deasupra capului",
            "npo": "Repaus alimentar 2-4 ore dacă starea pacientului permite; în urgență N/A",
            "premedication": "Fără contrast oral",
            "contrast": {
                "agent": "Isovue 370 / Omnipaque 350",
                "volume": "60-75 mL",
                "flow_rate": "4.5 - 5.0 mL/s",
                "duration": "12-15s",
                "timing": "Bolus tracking în trunchiul arterei pulmonare, trigger 100 HU",
                "roi": "Trunchiul arterei pulmonare principale",
                "trigger": "100 HU",
            },
            "tech_params": {
                "kv": "CAREkV 80-100 kVp (optimizat pentru K-edge iod)",
                "mas": "CAREDose4D / SureExposure3D",
                "slice_thickness": "0.625 mm",
                "rotation_time": "0.28 - 0.33 s",
                "pitch": "1.2 - 1.5 (achiziție ultra-rapidă)",
                "scan_mode": "Elicoidal (Flash / Dual Source)",
                "collimation": "128 × 0.6 mm / 64 × 0.625 mm",
            },
            "series": [
                {
                    "name": "Angio-CT Pulmonar",
                    "start": "Baza plămânilor (direcție caudo-cranială pentru a reduce artefactele de respirație la baze)",
                    "end": "Vârfuri pulmonare",
                    "delay": "Trigger + 3-4 sec",
                    "thickness": "0.625 mm",
                    "notes": "Opacifiere densă a arterelor pulmonare principale, lobare, segmentare și subsegmentare (> 250 HU)",
                }
            ],
            "recons": [
                {
                    "plane": "Axial",
                    "acquisition": "Angio-CT Pulmonar",
                    "fov": "Torace",
                    "thickness_increment": "1.0 mm / 0.7 mm",
                    "kernel": "Mediastinal (I30f) + Pulmonar (I50f)",
                    "ir_strength": "Admire 3 / AIDR 3D",
                    "notes": "Detecție defecte de umplere endoluminale în arterele pulmonare",
                },
                {
                    "plane": "Coronal & Sagital",
                    "acquisition": "Angio-CT Pulmonar",
                    "fov": "Torace",
                    "thickness_increment": "1.5 mm / 1.5 mm",
                    "kernel": "Mediastinal (I30f)",
                    "ir_strength": "Admire 3 / AIDR 3D",
                    "notes": "Urmărire ramificații arteriale în plan anatomic",
                },
            ],
            "notes": {
                "tech": "Achiziție caudo-cranială preferată. Canulă 18G în plica cotului. Flush salin 40-50 mL la 4.5 mL/s imediat după contrast pentru a goli vena cavă superioară și a elimina artefactele de striere.",
                "rad": "Căutați defecte de umplere parțiale sau ocluzive (semnul călărețului pe bifurcație). Evaluați semnele de suprasolicitare a ventriculului drept (raport VD/VS > 1.0, reflux de contrast în vena cavă inferioară și venele suprahepatice).",
                "nursing": "Verificare permeabilitate canulă venoasă cu jet rapid de ser înainte de conectarea injectorului automat.",
                "tips": "Respirație: pacientul trebuie instruit să inspire ușor și să mențină apneea fără manevră Valsalva (care ar scădea întoarcerea venoasă și ar dilua contrastul în atriul drept cu sânge neopacifiat).",
                "additional_recons": "MIP axial și coronal cu grosime de 5-10 mm pentru analiza ramurilor subsegmentare periferice.",
            },
            "safety": {
                "allergy": "Conform politicii OHSU. În suspiciune acută de TEP masiv, beneficiul este prioritar.",
                "renal": "eGFR > 30 mL/min; la pacienți instabili hemodinamic se asigură hidratare promptă.",
            },
        },
    },
]

# ==============================================================================
# 2. PROTOCOALE IRM OHSU
# ==============================================================================

IRM_PROTOCOLS = [
    {
        "file_path": ROOT / "docs" / "irm" / "neuro" / "irm-mra-brain-ohsu.md",
        "fm": {
            "title": "RM Angiografie Cerebrală MRA 3D TOF & Contrast (Protocol OHSU)",
            "author": "OHSU Diagnostic Radiology / Departamentul de Radiologie",
            "category": "neuro",
            "modality": "irm",
            "last_updated": "2026-09-20",
            "clinical_indications": [
                "Suspiciune sau monitorizare de anevrism cerebral intracranian",
                "Stenoze sau ocluzii carotidiene, vertebrale sau ale arterelor cerebrale majore",
                "Suspiciune de disecție arterială cervico-cerebrală",
                "Malformații arterio-venoase (MAV) sau fistule durale",
                "Tromboză venoasă cerebrală (MRV asociat)",
            ],
            "coils_hardware": {
                "coil": "Antenă dedicată Head/Neck multicanal (16–32 canale)",
                "field_strength": "1.5 Tesla / 3.0 Tesla",
                "positioning": "Decubit dorsal, cap centrat în izocentru, imobilizare cu pernuțe laterale",
            },
            "patient_prep": "Screening complet de securitate RM conform politicii OHSU. Căști fonoizolante.",
            "contrast": {
                "agent": "Gadoliniu macrociclic (Gadobutrol / Gadoterat de meglumină)",
                "dose": "0.1 mmol/kg (standard)",
                "flow_rate": "1.5 - 2.0 mL/s urmat de flush salin 20 mL",
                "timing": "Bolus tracking dinamic la nivelul bifurcației carotidiene / crosei aortice",
                "notes": "Secvența 3D TOF este nativă; achiziția 3D CE-MRA este sincronizată cu contrastul.",
            },
            "sequences": [
                {
                    "name": "3D TOF MRA Arterial (Fără contrast)",
                    "plane": "Axial / 3D Volumetric",
                    "tr_te": "TR 20-25 ms / TE 3.0-4.0 ms / Flip angle 18-20°",
                    "slice_gap": "0.8 - 1.0 mm (izotrop)",
                    "fov_matrix": "FOV 200 mm / Matrice 320×256",
                    "fat_sat": "Nu (TOW fat suppression opțional)",
                    "notes": "Achiziție nativă de înaltă rezoluție a poligonului lui Willis; reconstrucții MIP rotate la 360°",
                },
                {
                    "name": "Axial 3D T1 MPRAGE Nativ",
                    "plane": "Sagital / Reconstrucție 3-plane",
                    "tr_te": "TR 1900-2300 ms / TE 2.5-3.5 ms / TI 900 ms",
                    "slice_gap": "1.0 mm izotrop",
                    "fov_matrix": "FOV 240 mm / Matrice 256×256",
                    "fat_sat": "Nu",
                    "notes": "Referință anatomică cerebrală și detectare hematoame intramurale (disecție)",
                },
                {
                    "name": "3D CE-MRA Dinamic Post-Contrast",
                    "plane": "Coronal / 3D Volumetric",
                    "tr_te": "TR 3.5-4.5 ms / TE 1.2-1.6 ms",
                    "slice_gap": "0.9 - 1.0 mm",
                    "fov_matrix": "FOV 300-350 mm / Matrice 384×384",
                    "fat_sat": "Nu",
                    "notes": "Acoperire de la arcul aortic până la vertex; bolus tracking pe arterele vertebrale/carotide",
                },
                {
                    "name": "Axial T2 TSE / FSE",
                    "plane": "Axial",
                    "tr_te": "TR 4000 ms / TE 100 ms",
                    "slice_gap": "4.0 mm / gap 0.4 mm",
                    "fov_matrix": "FOV 220 mm / Matrice 320×256",
                    "fat_sat": "Nu",
                    "notes": "Evaluare parenchim cerebral adiacent și absența fluxului (flow void)",
                },
                {
                    "name": "Axial DWI (b=0, b=1000) + hartă ADC",
                    "plane": "Axial",
                    "tr_te": "TR 3500 ms / TE 70 ms",
                    "slice_gap": "4.0 mm / gap 0.4 mm",
                    "fov_matrix": "FOV 220 mm / Matrice 128×128",
                    "fat_sat": "FatSat (EPI)",
                    "notes": "Excludere ischemie acută / microembolii cerebrale",
                },
            ],
            "quality_criteria": [
                "Reconstrucții MIP rotite în trepte de 15° pe axul stânga-dreapta și antero-posterior",
                "Vizualizare clară a ramurilor arteriale A1, A2, M1, M2, P1, P2 și a arterei comunicante anterioare/posterioare",
                "Absența artefactelor majore de mișcare sau turbulență la bifurcația carotidiană",
            ],
            "safety_considerations": [
                "Screening riguros feromagnetic Zonele III/IV conform politicii OHSU",
                "Verificare implanturi (stenturi, clipuri anevrismale) — documentație MR Conditional obligatorie",
                "Limită SAR < 2.0 W/kg în modul normal de operare",
            ],
            "contraindications": [
                "Clipurilor anevrismale feromagnetice non-MR Conditional",
                "Implanturi active incompatibile (pacemaker vechi, neurostimulatoare non-compatibile)",
            ],
            "notes": "Protocol standard OHSU de neuroradiologie pentru caracterizarea non-invazivă a sistemului arterial cerebral.",
            "iris_reference": {
                "chapter": "Cap, Gât & Coloană vertebrală",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            },
        },
    },
    {
        "file_path": ROOT / "docs" / "irm" / "neuro" / "irm-orbite-ohsu.md",
        "fm": {
            "title": "RM Orbite & Nervi Optici / Graves & Cine ENT (Protocol OHSU)",
            "author": "OHSU Diagnostic Radiology / Departamentul de Radiologie",
            "category": "neuro",
            "modality": "irm",
            "last_updated": "2026-09-20",
            "clinical_indications": [
                "Oftalmopatie tiroidiană Basedow-Graves (evaluare edem și activitate inflamatorie în mușchii oculomotori)",
                "Nevrită optică, neuropatii optice demielinizante sau ischemice",
                "Mase tumorale orbitare (hemangiom cavernos, meningiom de teacă de nerv optic, gliom, schwannom)",
                "Strabism restrictiv și evaluare dinamică a motilității musculare oculare (Cine ENT)",
                "Exoftalmie / proptoză unilaterală sau bilaterală neelucidată",
            ],
            "coils_hardware": {
                "coil": "Antenă dedicată Head/Neck multicanal de înaltă rezoluție",
                "field_strength": "1.5 Tesla / 3.0 Tesla",
                "positioning": "Decubit dorsal, privire fixată înainte pe un punct de referință cu ochii închiși ușor pentru secvențele statice",
            },
            "patient_prep": "Îndepărtarea completă a machiajului ocular (fardurile conțin oxizi de fier care produc artefacte severe de susceptibilitate). Instrucțiuni de fixare a privirii.",
            "contrast": {
                "agent": "Gadoliniu macrociclic (Gadoteridol / Gadobutrol)",
                "dose": "0.1 mmol/kg",
                "flow_rate": "1.5 - 2.0 mL/s",
                "timing": "Secvențe post-contrast la 2-3 minute de la injectare",
                "notes": "Supresia de grăsime (FatSat) este obligatorie pe secvențele post-contrast orbitare.",
            },
            "sequences": [
                {
                    "name": "Coronal T1 TSE (Secțiuni Fine)",
                    "plane": "Coronal (Perpendicular pe nervii optici)",
                    "tr_te": "TR 500-650 ms / TE 10-15 ms",
                    "slice_gap": "2.5 mm / gap 0.2 mm",
                    "fov_matrix": "FOV 140-160 mm / Matrice 256×256",
                    "fat_sat": "Nu",
                    "notes": "Anatomie de bază: apreciere calibru pântece musculare (drept inferior, medial, superior, lateral) și grăsime conică",
                },
                {
                    "name": "Coronal T2 FS (STIR / SPAIR)",
                    "plane": "Coronal",
                    "tr_te": "TR 3500-4500 ms / TE 60-80 ms",
                    "slice_gap": "2.5 mm / gap 0.2 mm",
                    "fov_matrix": "FOV 140-160 mm / Matrice 256×224",
                    "fat_sat": "FatSat / SPAIR",
                    "notes": "Cheie diagnostică pentru oftalmopatia Graves: hipersemnal T2 în mușchii oculari indică inflamație activă",
                },
                {
                    "name": "Axial T2 TSE / FSE",
                    "plane": "Axial (Paralel cu traiectul nervilor optici)",
                    "tr_te": "TR 3000-4000 ms / TE 80-90 ms",
                    "slice_gap": "2.5 mm / gap 0.2 mm",
                    "fov_matrix": "FOV 160 mm / Matrice 256×256",
                    "fat_sat": "Nu",
                    "notes": "Evaluare traiect intraconal și canalicular al nervului optic și apex orbitar",
                },
                {
                    "name": "Axial DWI (b=0, b=800) + ADC",
                    "plane": "Axial",
                    "tr_te": "TR 3000 ms / TE 70 ms",
                    "slice_gap": "3.0 mm / gap 0.3 mm",
                    "fov_matrix": "FOV 180 mm / Matrice 128×128",
                    "fat_sat": "FatSat (EPI)",
                    "notes": "Diferențiere celulită orbitară / abces / limfom orbitar",
                },
                {
                    "name": "Cine bSSFP ENT (Evaluare Dinamică Motilitate)",
                    "plane": "Coronal / Sagital oblic",
                    "tr_te": "TR 3.0 ms / TE 1.5 ms",
                    "slice_gap": "4.0 mm",
                    "fov_matrix": "FOV 180 mm / Matrice 192×192",
                    "fat_sat": "Nu",
                    "notes": "Pacientul privește succesiv punctele de reper (sus, jos, stânga, dreapta) pentru a evalua excursia musculară",
                },
                {
                    "name": "Coronal T1 FS + C Post-Contrast",
                    "plane": "Coronal",
                    "tr_te": "TR 550-700 ms / TE 10-15 ms",
                    "slice_gap": "2.5 mm / gap 0.2 mm",
                    "fov_matrix": "FOV 140-160 mm / Matrice 256×256",
                    "fat_sat": "FatSat obligatoriu",
                    "notes": "Captare patologică în teaca nervului optic (meningiom/nevrită) sau în pântecele musculare",
                },
                {
                    "name": "Axial T1 FS + C Post-Contrast",
                    "plane": "Axial",
                    "tr_te": "TR 550-700 ms / TE 10-15 ms",
                    "slice_gap": "2.5 mm / gap 0.2 mm",
                    "fov_matrix": "FOV 160 mm / Matrice 256×256",
                    "fat_sat": "FatSat obligatoriu",
                    "notes": "Acoperire de la globul ocular până la chiasma optică",
                },
            ],
            "quality_criteria": [
                "Supresie de grăsime omogenă pe secvențele coronale T2 FS și T1 FS post-contrast",
                "Absența artefactelor de clipire sau mișcare a globilor oculari",
                "Rezoluție spațială înaltă cu matrice minim 256×256 pe FOV mic (14-16 cm)",
            ],
            "safety_considerations": [
                "Screening pentru corpi străini metalici intraoculari (radiografie orbitară prealabilă dacă există istoric de polizare/sudură)",
                "Evitarea compresiei oculare cu pernuțele de imobilizare",
            ],
            "contraindications": [
                "Corpi străini intraoculari feromagnetici (contraindicație absolută)",
            ],
            "notes": "Protocol specializat OHSU integrând evaluarea statică și dinamică a patologiei orbitare și a nervului optic.",
            "iris_reference": {
                "chapter": "Cap, Gât & Coloană vertebrală",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            },
        },
    },
    {
        "file_path": ROOT / "docs" / "irm" / "abdomen-pelvis" / "irm-apendicita-gravide-pediatrie-ohsu.md",
        "fm": {
            "title": "RM Apendicită Acută Nativă - Gravide & Pediatrie (Protocol OHSU)",
            "author": "OHSU Diagnostic Radiology / Departamentul de Radiologie",
            "category": "abdomen-pelvis",
            "modality": "irm",
            "last_updated": "2026-09-20",
            "clinical_indications": [
                "Suspiciune clinică de apendicită acută la paciente gravide (în orice trimestru de sarcină)",
                "Apendicită acută suspectată la copii și adolescenți când ecografia este neconcludentă sau tehnic dificilă",
                "Durere acută de fosă iliacă dreaptă la pacienți la care se dorește evitarea completă a iradierii prin CT",
                "Diagnosticul diferențial al patologiei inflamatorii acute pelvine la paciente tinere",
            ],
            "coils_hardware": {
                "coil": "Antenă Body phased-array multicanal (16–32 canale) centrată pe abdomenul inferior și pelvis",
                "field_strength": "1.5 Tesla (preferat în sarcină pentru SAR redus) sau 3.0 Tesla",
                "positioning": "Decubit dorsal (sau decubit lateral stâng ușor în trimestrul III pentru prevenirea sindromului de compresie cavă)",
            },
            "patient_prep": "Fără contrast oral; fără substanță de contrast intravenos; vezică urinară parțial plină pentru reperaj anatomic.",
            "contrast": {
                "agent": "Fără contrast (protocol exclusiv nativ)",
                "dose": "N/A",
                "flow_rate": "N/A",
                "timing": "N/A",
                "notes": "Contraindicație de rutină a administrării de Gadoliniu în sarcină conform ghidurilor OHSU și ACR.",
            },
            "sequences": [
                {
                    "name": "Coronal SSFSE / HASTE T2 (Abdomen & Pelvis)",
                    "plane": "Coronal",
                    "tr_te": "TR 1000-1500 ms / TE 80-90 ms",
                    "slice_gap": "4.0 mm / gap 0 mm (sau overlap 50% dacă pacientul respiră)",
                    "fov_matrix": "FOV 350-400 mm / Matrice 256×256",
                    "fat_sat": "Nu",
                    "notes": "Vedere de ansamblu: poziție cec, deplasare uterină a anselor, lichid liber peritoneal",
                },
                {
                    "name": "Axial SSFSE / HASTE T2",
                    "plane": "Axial",
                    "tr_te": "TR 1000-1500 ms / TE 80-90 ms",
                    "slice_gap": "4.0 mm / gap 0 mm",
                    "fov_matrix": "FOV 300-350 mm / Matrice 256×256",
                    "fat_sat": "Nu",
                    "notes": "Identificare bază apendiculară la joncțiunea cu fundul cecului",
                },
                {
                    "name": "Sagital SSFSE / HASTE T2",
                    "plane": "Sagital",
                    "tr_te": "TR 1000-1500 ms / TE 80-90 ms",
                    "slice_gap": "4.0 mm / gap 0 mm",
                    "fov_matrix": "FOV 300-350 mm / Matrice 256×256",
                    "fat_sat": "Nu",
                    "notes": "Urmărire traiect retrocecal sau pelvin al apendicelui",
                },
                {
                    "name": "Axial T2 FatSat (SPAIR / FS)",
                    "plane": "Axial",
                    "tr_te": "TR 1500-2000 ms / TE 80 ms",
                    "slice_gap": "4.0 mm / gap 0.4 mm",
                    "fov_matrix": "FOV 300-350 mm / Matrice 256×224",
                    "fat_sat": "FatSat / SPAIR",
                    "notes": "Evidențiere edem periapendicular, infiltrare a grăsimii fosei iliace drepte și colecții lichidiene",
                },
                {
                    "name": "Axial DWI (b=50, b=800) + hartă ADC",
                    "plane": "Axial",
                    "tr_te": "TR 3000-4000 ms / TE 60-70 ms",
                    "slice_gap": "4.0 mm / gap 0.4 mm",
                    "fov_matrix": "FOV 300-350 mm / Matrice 128×128",
                    "fat_sat": "FatSat (EPI)",
                    "notes": "Hipersemnal b=800 în peretele apendicular și restricție pe ADC = semn înalt specific de apendicită supurată",
                },
                {
                    "name": "Axial In-Phase / Out-of-Phase T1 GRE",
                    "plane": "Axial",
                    "tr_te": "TR 150 ms / TE 2.2 / 4.4 ms (la 1.5T)",
                    "slice_gap": "4.0 mm / gap 0.4 mm",
                    "fov_matrix": "FOV 320 mm / Matrice 256×192",
                    "fat_sat": "Nu (Dual-echo)",
                    "notes": "Detectare apendicolit / fecalit (semnal negru pe ambele ecouri) și sânge subacut",
                },
            ],
            "quality_criteria": [
                "Identificarea apendicelui normal (diametru < 6 mm, perete fin < 2 mm, lumen colabat sau umplut cu gaz/lichid fără edem pericecal)",
                "Dacă apendicele nu poate fi menționat ca normal, identificarea clară a semnelor pozitive: diametru > 7 mm, îngroșare parietală, edem T2 FS periapendicular, restricție DWI",
                "Durată totală la aparat menținută sub 15-20 minute",
            ],
            "safety_considerations": [
                "La gravide: scanare exclusivă în mod SAR normal (< 2.0 W/kg)",
                "Fără contrast pe bază de Gadoliniu",
                "Evitarea apneei prelungite; secvențele SSFSE sunt achiziționate în respirație liberă sau apnee scurtă",
            ],
            "contraindications": [
                "Implanturi feromagnetice non-MR Conditional",
            ],
            "notes": "Protocol oficial OHSU de primă intenție la gravide cu suspiciune de apendicită după ecografie, cu sensibilitate și specificitate > 95%.",
            "iris_reference": {
                "chapter": "Aparat digestiv & Abdomen",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            },
        },
    },
    {
        "file_path": ROOT / "docs" / "irm" / "abdomen-pelvis" / "irm-cuantificare-fier-steatoza-hepatica-ohsu.md",
        "fm": {
            "title": "RM Cuantificare Fier Fe & Steatoză Hepatică PDFF (Protocol OHSU)",
            "author": "OHSU Diagnostic Radiology / Departamentul de Radiologie",
            "category": "abdomen-pelvis",
            "modality": "irm",
            "last_updated": "2026-09-20",
            "clinical_indications": [
                "Suspiciune de supraîncărcare hepatică cu fier (hemocromatoză ereditară, hemosideroză secundară după transfuzii repetate)",
                "Monitorizarea terapiei de chelare a fierului la pacienți cu talasemie majoră sau sindroame mielodisplazice",
                "Cuantificarea precisă a steatozei hepatice (NAFLD / NASH, steatohepatită metabolică)",
                "Evaluare pre-donare hepatică sau pre-chimioterapie hepatotoxică",
            ],
            "coils_hardware": {
                "coil": "Antenă Body multicanal (16–32 canale) centrată pe etajul abdominal superior",
                "field_strength": "1.5 Tesla (etalonul de aur pentru cuantificarea fierului) sau 3.0 Tesla",
                "positioning": "Decubit dorsal, brațele pe lângă cap",
            },
            "patient_prep": "Repaus alimentar 4 ore înainte de examinare. Fără contrast.",
            "contrast": {
                "agent": "Fără contrast (determinare biometrică pur nativă)",
                "dose": "N/A",
                "flow_rate": "N/A",
                "timing": "N/A",
                "notes": "Substanțele de contrast pe bază de Gadoliniu alterează măsurătorile de T2* și sunt strict contraindicate înaintea acestei achiziții.",
            },
            "sequences": [
                {
                    "name": "Multi-Echo GRE T2* / R2* Hepatic",
                    "plane": "Axial",
                    "tr_te": "TR 150-200 ms / 6 până la 12 ecouri (TE 1.1 - 18 ms)",
                    "slice_gap": "8.0 - 10.0 mm (3 secțiuni reprezentative prin ficat)",
                    "fov_matrix": "FOV 380 mm / Matrice 192×128",
                    "fat_sat": "Nu",
                    "notes": "Calcul direct al R2* (R2* = 1000 / T2* în Hz) corelat matematic cu concentrația de fier hepatic (LIC în mg Fe/g țesut uscat)",
                },
                {
                    "name": "3D Dixon Multi-Echo PDFF (Proton Density Fat Fraction)",
                    "plane": "Axial",
                    "tr_te": "TR 6-9 ms / 6 ecouri / Flip angle 3-4° (elimină T1 bias)",
                    "slice_gap": "4.0 mm izotrop",
                    "fov_matrix": "FOV 380 mm / Matrice 192×192",
                    "fat_sat": "Dixon (Fat, Water, In-phase, Out-of-phase, Fat-fraction map)",
                    "notes": "Harta procentuală a fracției de grăsime (PDFF %: normal < 5%, steatoză ușoară 5-15%, moderată 15-25%, severă > 25%)",
                },
                {
                    "name": "Axial T2 SSFSE / HASTE",
                    "plane": "Axial",
                    "tr_te": "TR 1200 ms / TE 80 ms",
                    "slice_gap": "5.0 mm / gap 1.0 mm",
                    "fov_matrix": "FOV 350 mm / Matrice 256×256",
                    "fat_sat": "Nu",
                    "notes": "Evaluare anatomică hepatică și splenomicroscopie",
                },
                {
                    "name": "Coronal T2 SSFSE / HASTE",
                    "plane": "Coronal",
                    "tr_te": "TR 1200 ms / TE 80 ms",
                    "slice_gap": "5.0 mm / gap 1.0 mm",
                    "fov_matrix": "FOV 380 mm / Matrice 256×256",
                    "fat_sat": "Nu",
                    "notes": "Raport topografic ficat-splină-pancreas (apreciere depuneri de fier splenice și pancreatice)",
                },
            ],
            "quality_criteria": [
                "Achiziție în apnee expiratorie stabilă pentru evitarea artefactelor de mișcare pe secvența multi-echo",
                "Amplasarea a minim 3 regiuni de interes (ROI) de 1-2 cm² în parenchimul hepatic omogen, evitând vasele mari și căile biliare",
                "Coeficient de corelație R² > 0.95 pentru curba de atenuare exponențială T2*",
            ],
            "safety_considerations": [
                "Screening standard RM conform politicii OHSU",
                "Pacienții cu hemocromatoză pot avea asociată cardiomiopatie — se recomandă monitorizare puls",
            ],
            "contraindications": [
                "Implanturi feromagnetice",
            ],
            "notes": "Protocol de referință OHSU pentru cuantificarea non-invazivă absolută a fierului și grăsimii hepatice, înlocuind biopsia hepatică.",
            "iris_reference": {
                "chapter": "Aparat digestiv & Abdomen",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            },
        },
    },
    {
        "file_path": ROOT / "docs" / "irm" / "msk" / "irm-glezna-retropicior-ohsu.md",
        "fm": {
            "title": "RM Retropicior & Gleznă MSK (Protocol OHSU)",
            "author": "OHSU Diagnostic Radiology / Departamentul de Radiologie",
            "category": "msk",
            "modality": "irm",
            "last_updated": "2026-09-20",
            "clinical_indications": [
                "Tendinopatie, ruptură parțială sau totală a tendonului achilian sau a tendonului tibial posterior",
                "Leziuni ligamentare acute sau instabilitate cronică de gleznă (ligament talofibular anterior, calcaneofibular, deltoid)",
                "Sindroame de impingement anterior, anterolateral sau posterior de gleznă",
                "Osteonecroză aseptică de talus, fracturi de stres sau leziuni osteocondrale ale domului talar",
                "Fasceită plantară proximală și durere nespecifică de retropicior",
            ],
            "coils_hardware": {
                "coil": "Antenă dedicată de gleznă / picior Foot/Ankle multicanal (8–16 canale)",
                "field_strength": "1.5 Tesla / 3.0 Tesla",
                "positioning": "Decubit dorsal, picior în flexie neutră la 90° imobilizat ferm în antenă pentru a preveni 'magic angle effect' pe tendoane",
            },
            "patient_prep": "Screening standard de securitate RM. Fără pregătire medicamentoasă specială.",
            "contrast": {
                "agent": "Fără contrast (protocol de rutină)",
                "dose": "N/A",
                "flow_rate": "N/A",
                "timing": "N/A",
                "notes": "Contrastul i.v. se administrează doar în suspiciuni specifice de artrită inflamatorie, sinovită proliferativă sau infecție/abces.",
            },
            "sequences": [
                {
                    "name": "Sagital T1 SE / TSE",
                    "plane": "Sagital",
                    "tr_te": "TR 500-650 ms / TE 10-15 ms",
                    "slice_gap": "3.0 mm / gap 0.3 mm",
                    "fov_matrix": "FOV 140 mm / Matrice 320×256",
                    "fat_sat": "Nu",
                    "notes": "Morfologie tendon achilian, fascie plantară, arhitectură osoasă calcaneu și talus",
                },
                {
                    "name": "Sagital PD FS (Proton Density FatSat)",
                    "plane": "Sagital",
                    "tr_te": "TR 2500-3500 ms / TE 30-40 ms",
                    "slice_gap": "3.0 mm / gap 0.3 mm",
                    "fov_matrix": "FOV 140 mm / Matrice 288×256",
                    "fat_sat": "FatSat",
                    "notes": "Edem osos, bursită retrocalcaneană, bursită pre-achiliană, rupturi fibrilare",
                },
                {
                    "name": "Coronal PD FS",
                    "plane": "Coronal (Orientat pe axul lung al calcaneului / maleole)",
                    "tr_te": "TR 2500-3500 ms / TE 30-40 ms",
                    "slice_gap": "3.0 mm / gap 0.3 mm",
                    "fov_matrix": "FOV 140 mm / Matrice 288×256",
                    "fat_sat": "FatSat",
                    "notes": "Ligament colateral medial (deltoid), ligament calcaneofibular, tendoane peroniere și tibial posterior",
                },
                {
                    "name": "Axial T1 SE / TSE",
                    "plane": "Axial (Perpendicular pe axul lung al tibiei)",
                    "tr_te": "TR 500-650 ms / TE 10-15 ms",
                    "slice_gap": "3.0 mm / gap 0.3 mm",
                    "fov_matrix": "FOV 120-140 mm / Matrice 320×256",
                    "fat_sat": "Nu",
                    "notes": "Anatomie de secțiune transversală a compartimentelor tendinoase retromaleolare",
                },
                {
                    "name": "Axial PD FS",
                    "plane": "Axial",
                    "tr_te": "TR 2500-3500 ms / TE 30-40 ms",
                    "slice_gap": "3.0 mm / gap 0.3 mm",
                    "fov_matrix": "FOV 120-140 mm / Matrice 288×256",
                    "fat_sat": "FatSat",
                    "notes": "Tenosinovită a tendoanelor peroniere, tibial posterior, flexor lung al halucelui, ligament talofibular anterior (LTFA)",
                },
            ],
            "quality_criteria": [
                "Poziționare strict neutră la 90° pentru a evita creșterea artificială de semnal pe tendoane datorită fenomenului 'Magic Angle' (55°)",
                "Supresie omogenă de grăsime pe întregul volum al retropiciorului",
                "Rezoluție spațială înaltă adaptată structurilor ligamentare fine",
            ],
            "safety_considerations": [
                "Screening feromagnetic obligatoriu",
                "Verificarea eventualelor materiale de osteosinteză la nivelul gleznei — utilizare secvențe de reducere a artefactelor metalice (WARP/MARS) dacă este necesar",
            ],
            "contraindications": [
                "Implanturi feromagnetice incompatibile",
            ],
            "notes": "Protocol standardizat OHSU MSK pentru diagnosticul precis al patologiei tendinoase, ligamentare și cartilaginoase de gleznă și retropicior.",
            "iris_reference": {
                "chapter": "Aparat locomotor & Articulații",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            },
        },
    },
    {
        "file_path": ROOT / "docs" / "irm" / "pediatrie" / "irm-pediatric-brain-wwo-ohsu.md",
        "fm": {
            "title": "RM Cerebral Pediatric cu/fără Contrast (Protocol OHSU)",
            "author": "OHSU Diagnostic Radiology / Departamentul de Radiologie",
            "category": "pediatrie",
            "modality": "irm",
            "last_updated": "2026-09-20",
            "clinical_indications": [
                "Leziuni focale cerebrale sau suspiciune de neoplazie SNC pediatrică (astrocitom, meduloblastom, ependimom)",
                "Infecții intracraniene pediatrice (meningită bacteriană/virală, encefalită, abces cerebral, empiem)",
                "Cefalee cronică progresivă sau cu semne neurologice de focar",
                "Evaluare post-operatorie sau monitorizare oncopediatrică neuroaxială",
                "Deficite neurologice acute sau subacute la copil",
            ],
            "coils_hardware": {
                "coil": "Antenă dedicată Head pediatrică multicanal (16–32 canale) cu pernuțe moi",
                "field_strength": "1.5 Tesla / 3.0 Tesla",
                "positioning": "Decubit dorsal, cap imobilizat confortabil, măsuri active de confort și distragere pediatrică (Child Life)",
            },
            "patient_prep": "La sugari (< 6 luni): tehnică feed-and-wrap (alimentare și înfășare înainte de scanare). La copii cooperanți: muzică / povești audio prin căști RM. La copii necooperanți: sedare conform politicii OHSU Moderate Sedation.",
            "contrast": {
                "agent": "Gadoliniu macrociclic cu stabilitate înaltă (Gadoterat de meglumină / Gadobutrol)",
                "dose": "0.1 mmol/kg (strict conform greutății copilului)",
                "flow_rate": "1.0 - 1.5 mL/s + flush salin 10-15 mL",
                "timing": "Scanare post-contrast imediat după injectare",
                "notes": "Administrare de contrast aprobată doar în indicații oncologice, infecțioase sau vasculare clare.",
            },
            "sequences": [
                {
                    "name": "Sagital 3D T1 MPRAGE Nativ",
                    "plane": "Sagital / Reconstrucție 3-plane",
                    "tr_te": "TR 2000-2400 ms / TE 2.5-3.5 ms / TI 900 ms",
                    "slice_gap": "0.9 - 1.0 mm izotrop",
                    "fov_matrix": "FOV 200-220 mm / Matrice 256×256",
                    "fat_sat": "Nu",
                    "notes": "Anatomie de înaltă rezoluție: corp calos, fosă posterioară, joncțiune cervico-medulară, mielinizare",
                },
                {
                    "name": "Axial T2 TSE / FSE",
                    "plane": "Axial",
                    "tr_te": "TR 4000-5000 ms / TE 100-110 ms",
                    "slice_gap": "3.5 - 4.0 mm / gap 0.4 mm",
                    "fov_matrix": "FOV 200 mm / Matrice 320×256",
                    "fat_sat": "Nu",
                    "notes": "Diferențiere substanță albă/cenușie și evaluare edem vasogenic",
                },
                {
                    "name": "Axial FLAIR",
                    "plane": "Axial",
                    "tr_te": "TR 8000-9000 ms / TE 90-110 ms / TI 2200-2400 ms",
                    "slice_gap": "3.5 - 4.0 mm / gap 0.4 mm",
                    "fov_matrix": "FOV 200 mm / Matrice 256×224",
                    "fat_sat": "Nu",
                    "notes": "Supresie LCR; evidențiere leziuni periventriculare și leptomeningeale",
                },
                {
                    "name": "Axial DWI (b=0, b=1000) + hartă ADC",
                    "plane": "Axial",
                    "tr_te": "TR 3000-4000 ms / TE 70 ms",
                    "slice_gap": "3.5 - 4.0 mm / gap 0.4 mm",
                    "fov_matrix": "FOV 200 mm / Matrice 128×128",
                    "fat_sat": "FatSat (EPI)",
                    "notes": "Restricție de difuzie în leziuni celulare hiperdense (meduloblastom) sau abcese cerebrale",
                },
                {
                    "name": "Axial T2* / SWI",
                    "plane": "Axial",
                    "tr_te": "TR 600-800 ms / TE 15-25 ms",
                    "slice_gap": "3.5 - 4.0 mm / gap 0.4 mm",
                    "fov_matrix": "FOV 200 mm / Matrice 256×192",
                    "fat_sat": "Nu",
                    "notes": "Sensibilitate la hemoragii intratumorale, microhemoragii și calcificări",
                },
                {
                    "name": "Axial T1 SE / TSE Post-Contrast",
                    "plane": "Axial",
                    "tr_te": "TR 500-650 ms / TE 10-15 ms",
                    "slice_gap": "3.5 - 4.0 mm / gap 0.4 mm",
                    "fov_matrix": "FOV 200 mm / Matrice 256×256",
                    "fat_sat": "Nu",
                    "notes": "Captare patologică focală sau difuză a barierei hemato-encefalice",
                },
                {
                    "name": "Coronal T1 FS Post-Contrast (sau 3D T1 FS)",
                    "plane": "Coronal",
                    "tr_te": "TR 550-700 ms / TE 10-15 ms",
                    "slice_gap": "3.5 - 4.0 mm / gap 0.4 mm",
                    "fov_matrix": "FOV 200 mm / Matrice 256×224",
                    "fat_sat": "FatSat obligatoriu",
                    "notes": "Evaluare fosa posterioară, unghi ponto-cerebelos și diseminare leptomeningeală",
                },
            ],
            "quality_criteria": [
                "Acoperire craniană completă fără trunchiere la nivelul foramen magnum",
                "Secvențe T1 post-contrast evaluate în comparație directă cu secvența T1 nativă",
                "Protecție acustică dublă certificată pentru volumul cranian pediatric",
            ],
            "safety_considerations": [
                "Protecție fonică dublă obligatorie (căști adaptate + dopuri siliconice)",
                "Monitorizare pulsoximetrie compatibilă RM pe durata întregii examinări",
                "SAR strict menținut în limita normală (< 2.0 W/kg)",
            ],
            "contraindications": [
                "Implanturi feromagnetice incompatibile RM",
            ],
            "notes": "Protocol complet pediatric OHSU pentru diagnostic neoplazic și infecțios de înaltă rezoluție.",
            "iris_reference": {
                "chapter": "Pediatrie - Sistem Nervos Central",
                "recommendation_grade": "Grad A",
                "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            },
        },
    },
]

# ==============================================================================
# 3. GHID POLITICI CLINICE OHSU
# ==============================================================================

OHSU_POLICIES_MD = f"""---
title: Politici Clinice & Securitate Diagnostic Radiology (Standard OHSU)
author: OHSU Diagnostic Radiology / Departamentul de Radiologie
category: for-institutions
last_updated: '2026-09-20'
---

# Politici Clinice, Standarde de Securitate & Administrare Substanțe de Contrast (OHSU)

Ghid instituțional sinoptic al politicilor clinice și procedurilor de siguranță aplicate în cadrul **Department of Diagnostic Radiology — Oregon Health & Science University (OHSU)**. Acest document integrează politicile oficiale de administrare a substanțelor de contrast iodate și paramagnetice, securitatea în mediul de rezonanță magnetică (Zonele I–IV) și sedarea procedurală moderată.

<div class="iris-official-banner" style="margin-bottom: 24px;">
  <div class="iris-official-badge">🏥 POLITICI & STANDARDE CLINICE OHSU</div>
  <p class="iris-official-desc" style="margin-bottom: 8px !important;">
    Politici instituționale gestionate prin <strong>MCN Policy Manager</strong> al OHSU, destinate radiologilor, tehnicienilor de radiologie și asistenților medicali pentru garantarea siguranței pacientului și standardizarea calității examinărilor imagistice.
  </p>
  <a href="{OHSU_POLICY_URL}" target="_blank" rel="noopener" style="font-weight: 600; color: #0f766e; text-decoration: none;">
    Consultă portalul oficial OHSU Diagnostic Radiology Policies ➔
  </a>
</div>

---

## 1. Administrarea Substanțelor de Contrast Iodate (CT & Fluoroscopie)

### 1.1. Criterii de Testare a Creatininei & Calcul eGFR Pre-Contrast
Conform politicii OHSU, determinarea nivelului creatininei serice și a **ratei estimate de filtrare glomerulară (eGFR)** este obligatorie înaintea injectării i.v. a substanțelor de contrast iodate la pacienții cu factori de risc:
- **Vârstă:** Pacienți cu vârsta peste 60 de ani.
- **Istoric renal:** Antecedente de insuficiență renală acută/cronică, rinichi unic chirurgical sau congenital, transplant renal sau rezecție renală.
- **Boli sistemice:** Diabet zaharat tratat medicamentos, hipertensiune arterială cronică necesitând tratament medical.
- **Valabilitate analiză:** Valoarea creatininei/eGFR este considerată valabilă dacă a fost efectuată în ultimele **30 de zile** pentru pacienți ambulatori stabili, respectiv **24–48 ore** pentru pacienți internați sau cu patologie acută instabilă.

### 1.2. Managementul Pacienților sub Tratament cu Metformin
- **eGFR ≥ 30 mL/min/1.73m² și fără injurie renală acută:** Tratamentul cu Metformin **nu necesită întrerupere** înainte sau după injectarea de contrast.
- **eGFR < 30 mL/min/1.73m² sau pacienți instabili / proceduri cu risc mare:** Metforminul se întrerupe în momentul procedurii și se reia după **48 de ore**, doar după verificarea stabilității funcției renale (re-evaluare eGFR).

### 1.3. Protocol de Premedicație pentru Reacții Alergice la Iod
Destinat pacienților cu istoric documentat de reacție alergică anterioară moderată sau severă la contrast iodat:
- **Protocol Electiv Standard (12–13 ore):**
  1. *Prednison:* 50 mg oral la **13 ore**, **7 ore** și **1 oră** înainte de administrarea contrastului.
  2. *Difenhidramină:* 50 mg oral (sau i.v.) cu **1 oră** înainte de administrarea contrastului.
- **Protocol de Urgență (4–6 ore):**
  1. *Hidrocortizon:* 200 mg i.v. la fiecare 4 ore până la scanare (minim 2 doze).
  2. *Difenhidramină:* 50 mg i.v. cu 1 oră înainte de procedură.

### 1.4. Managementul Reacțiilor Acute la Contrast
| Severitate | Simptome Clinice | Conduită Terapeutică Imediată |
|:-----------|:-----------------|:------------------------------|
| **Ușoară** | Greață, vărsături izolate, strănut, eritem cutanat localizat, gust metalic | Observație clinică, liniștirea pacientului, monitorizare parametri vitali |
| **Moderată** | Urticarie difuză, prurit sever, bronhospasm ușor, edem facial fără stridor | Antihistaminic (Difenhidramină 25–50 mg i.v./oral), bronhodilatator inhalator (Salbutamol 2–3 pufuri), oxigenoterapie pe mască |
| **Severă** | Șoc anafilactic, stridor laringian, hipotensiune severă, stop cardiorespirator | Alertare echipă urgență / Cod Albastru, **Epinefrină (Adrenalină) 1:1000 i.m. 0.3 mg** (repetabil la 5–15 min), fluide i.v. rapide (Ringer/NaCl 0.9%), oxigenoterapie cu debit mare, intubație la nevoie |

### 1.5. Conduită în Extravazarea Substanței de Contrast
- Oprirea imediată a injectării;
- Aspirarea cantității reziduale de contrast prin canulă înainte de retragerea acesteia;
- Aplicarea de comprese reci pentru reducerea edemului local;
- Elevarea membrului afectat deasupra nivelului inimii;
- **Consult chirurgical plastic / vascular urgent** dacă: volum extravazat > 100–150 mL, apariție de parestezii, modificări de perfuzie capilară distală sau suspiciune de sindrom de compartiment.

---

## 2. Administrarea Substanțelor de Contrast pe Bază de Gadoliniu (IRM)

### 2.1. Clasificarea Agenților și Riscul de Fibroză Sistemică Nefrogenă (NSF)
- OHSU utilizează predominant **agenți de contrast macrociclici (Grupul II)** cu stabilitate termodinamică și cinetică foarte înaltă (ex. *Gadobutrol — Gadovist*, *Gadoterat de meglumină — Dotarem*, *Gadoteridol — ProHance*).
- La pacienți cu insuficiență renală severă (eGFR < 30 mL/min/1.73m²) sau dializă, agenții din Grupul II prezintă un risc extrem de scăzut de NSF; administrarea se face exclusiv dacă beneficiul clinic diagnostic este cert.

### 2.2. Sarcina și Alăptarea
- **Sarcină:** Administrarea de Gadoliniu este de regulă **contraindicată** din cauza riscului teoretic de acumulare a ionilor liberi de gadoliniu în lichidul amniotic. Se recomandă protocoale native (vezi [RM Apendicită Nativă](file:///C:/Users/ionel/Downloads/radiology-protocols/docs/irm/abdomen-pelvis/irm-apendicita-gravide-pediatrie-ohsu.md)).
- **Alăptare:** Sub 0.04% din doza maternă se excretă în laptele matern, iar din aceasta sub 1% este absorbită de tractul gastrointestinal al sugarului. Întreruperea alăptării nu este obligatorie, dar la dorința mamei, laptele poate fi muls și aruncat timp de 24 de ore.

---

## 3. Politici Instituționale de Securitate RM (Zonele I–IV)

```mermaid
flowchart LR
    Z1["Zona I: Acces Public General"] --> Z2["Zona II: Triaj, Recepție & Screening"]
    Z2 --> Z3["Zona III: Control Acces Restricționat (Linie Roșie)"]
    Z3 --> Z4["Zona IV: Sala Magnetului (Câmp Magnetic Permanent)"]
```

1. **Zona I:** Spații publice accesibile tuturor pacienților și aparținătorilor (săli de așteptare, holuri exterioare).
2. **Zona II:** Zonă intermediară de primire unde se efectuează screeningul chestionarului de securitate RM sub supravegherea personalului instruit.
3. **Zona III:** Zonă cu acces strict controlat (uși securizate cu cartelă). Doar pacienții schimbați în halat spitalicesc și personalul autorizat pot pătrunde. Toate echipamentele trebuie să fie certificate "MR Conditional" sau "MR Safe".
4. **Zona IV:** Sala magnetului. Câmpul magnetic este **ACTIV PERMANENT** (24/7/365). Risc critic de proiectil mortal pentru orice obiect feromagnetic.
5. **Prioritizarea și Triajul:** Procedură standardizată de clasificare a urgențelor RM în funcție de patologie (urgențe vitale, urgențe oncologice, examinări de rutină).

---

## 4. Sedarea Procedurală Moderată în Radiologie Diagnostică

Pentru pacienții pediatrici sau adulți claustrofobi/necooperanți:
- Evaluare pre-sedare completă (istoric anestezic, clasă ASA, cale aeriană Mallampati, timp NPO de minim 6 ore pentru solide și 2 ore pentru lichide clare).
- Monitorizare continuă pe toată durata scanării și a recuperării: pulsoximetrie compatibilă RM, capnografie (EtCO2), tensiune arterială automată și traseu ECG.
- Prezența obligatorie a personalului instruit în suport vital avansat (ACLS / PALS) și a trusei de reversie farmacologică (Naloxonă, Flumazenil).

---

### Referințe Oficiale OHSU
- **OHSU Diagnostic Radiology Policies Portal:** [{OHSU_POLICY_URL}]({OHSU_POLICY_URL}){{ target="_blank" rel="noopener" }}
- **OHSU MCN Policy Manager:** [{OHSU_MCN_URL}]({OHSU_MCN_URL}){{ target="_blank" rel="noopener" }}
- **Ghidul Național IRIS (Ordinul MS 1342/2012):** [{IRIS_URL}]({IRIS_URL}){{ target="_blank" rel="noopener" }}
"""

def main() -> None:
    print("=" * 70)
    print("Generare protocoale CT & IRM OHSU și Ghid Politici Clinice")
    print("=" * 70)

    # 1. CT Protocols
    print("\n>>> Generare protocoale CT...")
    for proto in CT_PROTOCOLS:
        path = proto["file_path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        content = render_document(proto["fm"])
        path.write_text(content, encoding="utf-8")
        print(f"  ✔ Creat CT: {path.relative_to(ROOT)}")

    # 2. IRM Protocols
    print("\n>>> Generare protocoale IRM...")
    for proto in IRM_PROTOCOLS:
        path = proto["file_path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        content = render_irm_document(proto["fm"])
        path.write_text(content, encoding="utf-8")
        print(f"  ✔ Creat IRM: {path.relative_to(ROOT)}")

    # 3. Policy Guide
    print("\n>>> Generare Ghid Politici Clinice OHSU...")
    policy_path = ROOT / "docs" / "for-institutions" / "ohsu-diagnostic-radiology-policies.md"
    policy_path.write_text(OHSU_POLICIES_MD.strip() + "\n", encoding="utf-8")
    print(f"  ✔ Creat Ghid Politici: {policy_path.relative_to(ROOT)}")

    print("\n✔ Generare completă cu succes!")

if __name__ == "__main__":
    main()
