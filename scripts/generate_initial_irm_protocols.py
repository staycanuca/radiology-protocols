"""generate_initial_irm_protocols.py

Generează structura completă de protocoale IRM (Imagistică prin Rezonanță Magnetică)
în docs/irm/, inclusiv .pages, index.md și protocoale clinice validate conform Ghidului IRIS.
"""

from __future__ import annotations

from pathlib import Path
import sys

if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SCRIPTS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPTS_DIR.parent
DOCS_IRM = REPO_ROOT / "docs" / "irm"

sys.path.insert(0, str(SCRIPTS_DIR))
from render_irm_protocol import render_irm_document  # noqa: E402


CATEGORIES = {
    "neuro": {
        "title": "Neuroradiologie IRM (Cerebral & Coloană)",
        "desc": "Protocoale IRM pentru sistemul nervos central și coloană vertebrală.",
    },
    "msk": {
        "title": "Sistem Musculoscheletal (MSK IRM)",
        "desc": "Protocoale IRM pentru articulații, tendoane, ligamente și leziuni cartilaginoase.",
    },
    "abdomen-pelvis": {
        "title": "Abdomen & Pelvis IRM",
        "desc": "Protocoale IRM hepatobiliare, digestive, ginecologice și prostatice (mpMRI).",
    },
    "cardiac": {
        "title": "Cardio-IRM",
        "desc": "Protocoale IRM pentru evaluarea funcției cardiace, viabilității și cardiomiopatiilor.",
    },
    "san": {
        "title": "IRM Mamar",
        "desc": "Protocoale IRM multiparametrice pentru diagnosticul și stadializarea leziunilor mamare.",
    },
}

PROTOCOLS = [
    # ------------------ NEURO ------------------
    {
        "title": "IRM Cerebral Nativ și cu Substanță de Contrast",
        "slug": "irm-cerebral-nativ-si-cu-contrast",
        "category": "neuro",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Cefalee cronică persistentă cu caractere atipice sau semne de focar neurologic",
            "Suspiciune de proces expansiv intracranian primitiv sau diseminări secundare (metastaze)",
            "Boală demielinizantă (scleroză multiplă) - diagnostic și monitorizare activitate lezională",
            "Epilepsie / crize convulsive cu debut recent",
            "Evaluare infecții SNC (meningo-encefalită, abces cerebral)",
        ],
        "contraindications": [
            "Stimulatoare cardiace, defibrilatoare (ICD) sau neurostimulatoare non-MR Conditional",
            "Clipurilor anevrismale intracraniene feromagnetice",
            "Corpi străini metalici intraoculari sau fragmente de schije în vecinătatea structurilor vitale",
            "Proteze auditive implantabile / implant cohlear nesigur RM",
            "Claustrofobie severă refractară (necesită sedare/anestezie)",
            "eGFR < 30 mL/min/1.73m² (precauție la chelati de Gadoliniu; risc de NSF)",
        ],
        "patient_prep": "Completare și semnare a chestionarului de securitate RM; îndepărtarea tuturor accesoriilor metalice, bijuteriilor, protezelor dentare mobile; verificare funcție renală (creatinină/eGFR).",
        "coils_hardware": {
            "coil": "Antenă dedicată Head/Neck 32 - 64 canale",
            "field_strength": "1.5 Tesla / 3.0 Tesla",
            "positioning": "Decubit dorsal, cap centrat în izocentru pe nasion, imobilizare confortabilă cu pernuțe de spumă.",
        },
        "contrast": {
            "agent": "Chelat de Gadoliniu macrociclic (Gadobutrol 1.0 mmol/ml sau Gadoterat 0.5 mmol/ml)",
            "dose": "0.1 mmol/kg corp (0.1 ml/kg Gadobutrol sau 0.2 ml/kg Gadoterat)",
            "flow_rate": "1.5 - 2.0 ml/s injectare automată urmată de 20 ml ser fiziologic",
            "timing": "Achiziție secvențe post-contrast T1 la minimum 2-3 minute de la injectare",
            "notes": "Risc de NSF minimizat prin utilizarea exclusivă a agenților macrociclici stabili conform ghidului ESUR.",
        },
        "sequences": [
            {
                "name": "Sagital T1 SE / TSE",
                "plane": "Sagital",
                "tr_te": "TR 500 ms / TE 10 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 230 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Anatomie linia mediană, corp calos, fosa posterioară",
            },
            {
                "name": "Axial T2 TSE",
                "plane": "Axial (paralel CA-CP)",
                "tr_te": "TR 4500 ms / TE 100 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 230 mm / 384x288",
                "fat_sat": "Nu",
                "notes": "Diferențiere substanță albă/cenușie, edem vasogenic",
            },
            {
                "name": "Axial FLAIR",
                "plane": "Axial",
                "tr_te": "TR 9000 ms / TE 90 ms / TI 2500 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 230 mm / 320x224",
                "fat_sat": "Nu",
                "notes": "Supresie LCR liber; leziuni periventriculare și corticale",
            },
            {
                "name": "Axial DWI (b=0, b=1000) + hartă ADC",
                "plane": "Axial",
                "tr_te": "TR 3500 ms / TE 70 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 230 mm / 192x192",
                "fat_sat": "FatSat (EPI)",
                "notes": "Restricție de difuzie (hipersemnal DWI + hiposemnal ADC)",
            },
            {
                "name": "Axial T2* GRE / SWI",
                "plane": "Axial",
                "tr_te": "TR 600 ms / TE 20 ms / FA 15°",
                "slice_gap": "3.0 - 4.0 mm / gap 0 mm",
                "fov_matrix": "FOV 230 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Detecție microsângerări, hemosiderină, calcificări",
            },
            {
                "name": "3D T1 GRE + C (MPRAGE / BRAVO)",
                "plane": "3D Sagital Izotrop",
                "tr_te": "TR 1900 ms / TE 2.5 ms / TI 900 ms",
                "slice_gap": "1.0 mm izotrop",
                "fov_matrix": "FOV 256 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Captare leptomeningiană, noduli milimetrici, reconstrucții MPR",
            },
        ],
        "quality_criteria": [
            "Raport semnal-zgomot (SNR) optim cu vizualizare netă a joncțiunii cortico-subcorticale",
            "Absența artefactelor de pulsație din sinusurile venoase sau arterele carotide/bazilară",
            "Acoperire completă vertex - foramen magnum fără trunchiere anatomică",
        ],
        "safety_considerations": [
            "SAR corp întreg menținut în mod normal de operare (< 2.0 W/kg)",
            "Protecție acustică obligatorie cu căști fonoizolante și dopuri de urechi",
            "Monitorizare continuă video și verbală prin interfon",
        ],
        "iris_reference": {
            "chapter": "Sistem Nervos Central - Neuroimagistică",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "În suspiciunea de scleroză multiplă se adaugă secvență 3D Sagital FLAIR cu reconstrucție axială și coronală.",
    },
    {
        "title": "IRM Cerebral Urgență - Protocol AVC Ischemic Acut (Stroke)",
        "slug": "irm-cerebral-stroke-ischemie",
        "category": "neuro",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Deficit neurologic acut în fereastră terapeutică de tromboliză / trombectomie (< 4.5h - 24h)",
            "Wake-up stroke (accident vascular cerebral cu oră de debut necunoscută - mismatch DWI-FLAIR)",
            "Suspiciune de ocluzie de vas mare intracranian (LVO)",
            "Diagnostic diferențial stroke-mimic (migrenă cu aură, criză epileptică post-ictală Todd, hipoglicemie)",
        ],
        "contraindications": [
            "Instabilitate hemodinamică sau respiratorie severă incompatibilă cu sala RM",
            "Prezența implanturilor feromagnetice nesigure RM",
        ],
        "patient_prep": "Protocol ultra-rapid 'Code Stroke' (< 10-15 minute); monitorizare TA și SpO2 compatibile RM; verificare rapidă a absenței protezelor cardiace non-RM.",
        "coils_hardware": {
            "coil": "Antenă Head 32 canale",
            "field_strength": "1.5T sau 3.0T",
            "positioning": "Decubit dorsal, centrare nasion, cap fixat pentru evitarea mișcării.",
        },
        "contrast": {
            "agent": "Nativ (fără contrast obligatoriu pentru mismatch) sau 0.1 mmol/kg Gd dacă se efectuează perfuzie PWI",
            "dose": "0.1 mmol/kg (opțional perfuzie)",
            "flow_rate": "4.0 - 5.0 ml/s pentru perfuzie dinamică DSC",
            "timing": "DSC-PWI cu urmărire bolus",
            "notes": "Mismatch DWI/FLAIR permite selecția pacienților pentru tromboliză în wake-up stroke fără a necesita contrast.",
        },
        "sequences": [
            {
                "name": "DWI (b=0, b=1000) + ADC Map (Ultra-fast)",
                "plane": "Axial",
                "tr_te": "TR 3000 ms / TE 65 ms",
                "slice_gap": "4.0 mm / gap 0 mm",
                "fov_matrix": "FOV 230 mm / 192x192",
                "fat_sat": "FatSat",
                "notes": "Core ischemic citotoxic precoce (minute de la debut)",
            },
            {
                "name": "Axial FLAIR",
                "plane": "Axial",
                "tr_te": "TR 9000 ms / TE 90 ms / TI 2500 ms",
                "slice_gap": "4.0 mm / gap 0 mm",
                "fov_matrix": "FOV 230 mm / 256x224",
                "fat_sat": "Nu",
                "notes": "Evaluare mismatch: leziune DWI pozitivă + FLAIR negativă = debut < 4.5 ore",
            },
            {
                "name": "Axial T2* GRE / SWI",
                "plane": "Axial",
                "tr_te": "TR 600 ms / TE 20 ms",
                "slice_gap": "4.0 mm / gap 0 mm",
                "fov_matrix": "FOV 230 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Excludere absolută a hemoragiei intracraniene și semn de trombus intraluminal (susceptibility sign)",
            },
            {
                "name": "3D TOF MRA Poligon Willis",
                "plane": "3D Axial",
                "tr_te": "TR 22 ms / TE 3.5 ms / FA 18°",
                "slice_gap": "0.6 - 0.7 mm subțire",
                "fov_matrix": "FOV 200 mm / 384x256",
                "fat_sat": "TONE ramp pulse",
                "notes": "Identificare ocluzie arteră cerebrală medie (M1/M2), arteră carotidă internă terminală sau trunchi bazilar",
            },
        ],
        "quality_criteria": [
            "Timp total de scanare 'door-to-image' sub 12-15 minute",
            "Hărți ADC calculate automat și disponibile instantaneu pe consola PACS",
            "MIP 3D TOF generat automat pentru orientarea echipei de neuroradiologie intervențională",
        ],
        "safety_considerations": [
            "Monitorizare electrocardiografică și pulsoximetrică continuă compatibilă RM",
            "Personal antrenat pentru transfer rapid la masa de angiografie intervențională în caz de trombectomie",
        ],
        "iris_reference": {
            "chapter": "Neurologie de Urgență - AVC Ischemic",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "Dacă există mismatch DWI-FLAIR (DWI pozitiv, FLAIR negativ), pacientul beneficiază de tromboliză chiar dacă ora debutului este necunoscută.",
    },
    {
        "title": "Angio-IRM Artere Intracraniene (3D TOF fără contrast)",
        "slug": "angio-irm-artere-intracraniene-tof-3d",
        "category": "neuro",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Screening și monitorizare anevrisme arteriale intracraniene",
            "Evaluare malformații arterio-venoase (MAV) și fistule durale",
            "Diagnostic stenoză / ocluzie aterosclerotică a arterelor cerebrale mari",
            "Cefalee acută brusc instalată (excludere anevrism fisurat / disecție arterială)",
        ],
        "contraindications": [
            "Contraindicații generale de securitate RM (implanturi feromagnetice, pacemaker non-RM)",
        ],
        "patient_prep": "Chestionar de securitate RM; pacientul este rugat să stea perfect nemișcat și să evite deglutiția frecventă în timpul achiziției.",
        "coils_hardware": {
            "coil": "Antenă Head 32 sau 64 canale",
            "field_strength": "1.5T sau 3.0T (3T oferă rezoluție și SNR net superioare pentru ramurile distale)",
            "positioning": "Decubit dorsal, centrare pe conductele auditive externe.",
        },
        "contrast": {
            "agent": "Fără substanță de contrast (tehnică Time-of-Flight bazată pe flux sanguin nativ)",
            "dose": "0 ml",
            "flow_rate": "Nu este cazul",
            "timing": "Nu este cazul",
            "notes": "Secvența 3D TOF se bazează pe efectul de inflow al spinilor sangvini nesaturați care pătrund în volumul de scanare.",
        },
        "sequences": [
            {
                "name": "3D TOF (Time-of-Flight) MRA Poligon Willis",
                "plane": "3D Transversal cu plăci suprapuse (MOTSA)",
                "tr_te": "TR 23 ms / TE 3.4 ms / FA 18-20°",
                "slice_gap": "Grosime efectivă strat 0.5 - 0.6 mm",
                "fov_matrix": "FOV 200 mm / Matrice 448x320",
                "fat_sat": "Filtrare TONE / Magnetization Transfer",
                "notes": "Bandă de saturație presaturație venoasă superioară pentru suprimarea fluxului din sinusul sagital",
            },
            {
                "name": "Axial T2 TSE",
                "plane": "Axial",
                "tr_te": "TR 4500 ms / TE 95 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 230 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Confirmare semnal 'flow-void' normal în lumenul arterial",
            },
        ],
        "quality_criteria": [
            "Reconstrucții MIP (Maximum Intensity Projection) radiale rotative la fiecare 15-30°",
            "Vizualizare clară a arterelor comunicantă anterioară (ACom) și posterioare (PCom)",
            "Absența artefactelor de mișcare (ghosting) sau saturație pe flux lent",
        ],
        "safety_considerations": [
            "SAR limitat în mod normal",
            "Atenție la clipuri de anevrism preexistente: necesară confirmarea fișei de implant non-feromagnetic",
        ],
        "iris_reference": {
            "chapter": "Vascular Cerebral - Angio-RM",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "Pentru anevrisme mici (< 3 mm) sau disecții, se examinează secțiunile native subțiri de 0.5 mm, nu doar reconstrucțiile MIP.",
    },
    {
        "title": "IRM Hipofiză (Regiune Selară) cu Substanță de Contrast Dinamic",
        "slug": "irm-hipofiza-cu-contrast-dinamic",
        "category": "neuro",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Suspiciune de microadenom hipofizar secretant (prolactinom, boală Cushing, acromegalie)",
            "Macroadenom hipofizar (evaluare invazie sinus cavernos și compresie chiasmă optică)",
            "Diabet insipid central (evaluare neurohipofiză și tijă pituitară)",
            "Deficite hormonale hipofizare / panhipopituitarism",
        ],
        "contraindications": [
            "Contraindicații generale RM; insuficiență renală severă dacă eGFR < 30 ml/min.",
        ],
        "patient_prep": "Completare chestionar securitate RM; verificare eGFR; imobilizare atentă a capului.",
        "coils_hardware": {
            "coil": "Antenă Head 32 sau 64 canale",
            "field_strength": "1.5T sau preferabil 3.0T (rezoluție spațială superioară pe câmp mic de 12-14 cm)",
            "positioning": "Decubit dorsal, centrare pe nasion, plan de scanare strict perpendicular pe planul selar.",
        },
        "contrast": {
            "agent": "Chelat de Gadoliniu macrociclic",
            "dose": "0.1 mmol/kg corp",
            "flow_rate": "2.0 - 2.5 ml/s urmat de flush de 20 ml ser fiziologic",
            "timing": "Achiziție dinamică rapidă coronală T1 (la fiecare 15-20 secunde timp de 2-3 minute)",
            "notes": "Microadenoamele apar tipic ca arii hipocaptante tardiv-contrastate pe fondul captării precoce a parenchimului hipofizar normal.",
        },
        "sequences": [
            {
                "name": "Sagital T1 SE de înaltă rezoluție",
                "plane": "Sagital selar",
                "tr_te": "TR 500 ms / TE 10 ms",
                "slice_gap": "2.0 - 2.5 mm / gap 0.2 mm",
                "fov_matrix": "FOV 140 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Identificare hipersemnal fiziologic neurohipofiză",
            },
            {
                "name": "Coronal T2 TSE subțire",
                "plane": "Coronal selar",
                "tr_te": "TR 3500 ms / TE 90 ms",
                "slice_gap": "2.0 - 2.5 mm / gap 0.2 mm",
                "fov_matrix": "FOV 140 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Evaluare sinusuri cavernoase și chiasmă optică",
            },
            {
                "name": "Coronal T1 SE Nativ",
                "plane": "Coronal selar",
                "tr_te": "TR 500 ms / TE 10 ms",
                "slice_gap": "2.0 - 2.5 mm / gap 0.2 mm",
                "fov_matrix": "FOV 140 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Bază de comparație pentru faza dinamică",
            },
            {
                "name": "Coronal T1 Dinamic post-Gd (5-6 faze)",
                "plane": "Coronal selar",
                "tr_te": "TR 250 - 300 ms / TE 8 ms",
                "slice_gap": "2.5 mm / gap 0 mm",
                "fov_matrix": "FOV 140 mm / 256x192",
                "fat_sat": "Nu",
                "notes": "Secvență la 0s, 20s, 40s, 60s, 90s, 120s de la bolus",
            },
            {
                "name": "Sagital & Coronal T1 Tardiv + C",
                "plane": "Sagital și Coronal",
                "tr_te": "TR 500 ms / TE 10 ms",
                "slice_gap": "2.0 mm / gap 0.2 mm",
                "fov_matrix": "FOV 140 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Studiu tardiv al leziunii și al extensiei supraselare",
            },
        ],
        "quality_criteria": [
            "Delimitare netă a chiasmei optice și a conturului glandei hipofize",
            "Rezoluție sub-milimetrică în plan (matrice mare raportată la FOV mic de 140 mm)",
            "Absența artefactelor de susceptibilitate provenite din sinusul sfenoid pneumatizat",
        ],
        "safety_considerations": [
            "SAR redus pe câmp mic de examinare",
            "Monitorizare confort pacient pentru evitarea mișcărilor în faza dinamică",
        ],
        "iris_reference": {
            "chapter": "Endocrinologie - Neuroimagistică Hipofizară",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "În caz de macroadenom voluminos, se adaugă o secvență axială T2 sau FLAIR a întregului creier pentru hidrocefalie obstructivă.",
    },
    {
        "title": "IRM Coloană Cervicală",
        "slug": "irm-coloana-cervicala",
        "category": "neuro",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Cervicobrahialgie acută sau cronică rebelă la tratament",
            "Suspiciune de mielopatie cervicală (mers spastic, hiporeflexie/hiperreflexie, parestezii membre)",
            "Traumatism vertebro-medular cervical (evaluare ligamente, discuri și măduvă)",
            "Suspiciune de leziune demielinizantă medulară cervicală sau siringomielie",
        ],
        "contraindications": [
            "Contraindicații generale RM; materiale de osteosinteză feromagnetice nestabile.",
        ],
        "patient_prep": "Chestionar de securitate RM; pacientul este instruit să nu înghită în timpul rulării secvențelor sagitale pentru a evita artefactele de mișcare ale faringelui.",
        "coils_hardware": {
            "coil": "Antenă Head/Neck/Spine dedicată",
            "field_strength": "1.5T sau 3.0T",
            "positioning": "Decubit dorsal, gâtul în rectitudine anatomică, pernuță sub cap și genunchi flectați ușor pe suport.",
        },
        "contrast": {
            "agent": "Nativ în mod obișnuit; se injectează Gd 0.1 mmol/kg în suspiciuni de tumori, infecții (spondilodiscită) sau plăci active demielinizante.",
            "dose": "0.1 mmol/kg (la indicație)",
            "flow_rate": "1.5 - 2.0 ml/s",
            "timing": "Achiziție T1 post-contrast cu FatSat în 2 planuri",
            "notes": "Examinarea de rutină pentru discopatie degenerativă nu necesită substanță de contrast.",
        },
        "sequences": [
            {
                "name": "Sagital T1 TSE",
                "plane": "Sagital cervical (C1-T2)",
                "tr_te": "TR 550 ms / TE 10 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 240 mm / 384x256",
                "fat_sat": "Nu",
                "notes": "Morfologie corpi vertebrali, măduvă galbenă, aliniament",
            },
            {
                "name": "Sagital T2 TSE",
                "plane": "Sagital cervical",
                "tr_te": "TR 3500 ms / TE 100 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 240 mm / 384x288",
                "fat_sat": "Nu",
                "notes": "Canal spinal, hipersemnal intramedular (mielomalacie / edem)",
            },
            {
                "name": "Sagital STIR / TIRM",
                "plane": "Sagital cervical",
                "tr_te": "TR 4000 ms / TE 50 ms / TI 160 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 240 mm / 320x224",
                "fat_sat": "STIR",
                "notes": "Edem osos, fracturi, leziuni ligamentare posterioare",
            },
            {
                "name": "Axial T2* MEDIC / FFE / T2 TSE",
                "plane": "Axial înclinat pe spațiile discale (C3-C7)",
                "tr_te": "TR 700 ms / TE 15 ms / FA 25°",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 180 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Gaura de conjugare, foramen neural, uncoartroză, compresie radiculară",
            },
        ],
        "quality_criteria": [
            "Vizualizare clară de la joncțiunea cranio-cervicală (gaura occipitală) până la vertebra T2",
            "Banda de presaturație plasată anterior pe esofag/trahee pentru reducerea artefactelor de deglutiție",
            "Semnal LCR omogen fără artefacte majore de flux pulsatil",
        ],
        "safety_considerations": [
            "Atenție la plăcuțele de titan cervicale anterioare: se utilizează secvențe TSE în loc de GRE pentru scăderea susceptibilității",
        ],
        "iris_reference": {
            "chapter": "Coloană Vertebrală - Segment Cervical",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "Dacă se constată mielopatie cervicală compresivă, se măsoară diametrul antero-posterior al canalului spinal și gradul de stenoză.",
    },
    {
        "title": "IRM Coloană Lombară",
        "slug": "irm-coloana-lombara",
        "category": "neuro",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Lombosciatică / lumbocruralgie rebelă la tratament conservator (> 4-6 săptămâni)",
            "Sindrom de coadă de cal (urgență neurochirurgicală - anestezie 'în șa', retenție/incontinență urinară)",
            "Suspiciune de stenoză de canal vertebral lombar sau spondilolistezis",
            "Suspiciune de spondilodiscită infecțioasă sau metastaze vertebrale",
            "Evaluare post-operatorie (diferențiere hernie recidivată vs. fibroză periradiculară cicatricială)",
        ],
        "contraindications": [
            "Contraindicații generale de compatibilitate RM.",
        ],
        "patient_prep": "Chestionar de securitate RM; decubit dorsal confortabil cu genunchii flectați pe un burete cilindric pentru rectitudinea lordozei lombare.",
        "coils_hardware": {
            "coil": "Antenă Spine integrată în masă (phased-array)",
            "field_strength": "1.5T sau 3.0T",
            "positioning": "Decubit dorsal, centrare pe vertebra L3 (la 2-3 cm deasupra crestelor iliace).",
        },
        "contrast": {
            "agent": "Nativ de rutină; se injectează Gd 0.1 mmol/kg la pacienții operați recent (< 1 an) pentru diferențierea fibrozei (captează precoce) de hernia discală recidivată (necaptantă precoce).",
            "dose": "0.1 mmol/kg (la indicație)",
            "flow_rate": "1.5 - 2.0 ml/s",
            "timing": "T1 post-contrast axial și sagital",
            "notes": "Spondilodiscita infecțioasă necesită obligatoriu contrast paramagnetic intravenos.",
        },
        "sequences": [
            {
                "name": "Sagital T1 TSE",
                "plane": "Sagital lombar (T11 - S2)",
                "tr_te": "TR 600 ms / TE 10 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 280 mm / 384x256",
                "fat_sat": "Nu",
                "notes": "Modificări Modic tip 1/2, aliniament corpi vertebrali",
            },
            {
                "name": "Sagital T2 TSE",
                "plane": "Sagital lombar",
                "tr_te": "TR 4000 ms / TE 100 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 280 mm / 384x288",
                "fat_sat": "Nu",
                "notes": "Deshidratare discală, hernie posterioară, con medular (T12-L1/L2)",
            },
            {
                "name": "Sagital STIR / TIRM",
                "plane": "Sagital lombar",
                "tr_te": "TR 4200 ms / TE 50 ms / TI 160 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 280 mm / 320x224",
                "fat_sat": "STIR",
                "notes": "Edem osos vertebral (fractură recentă osteoporotică vs. veche, spondilodiscită)",
            },
            {
                "name": "Axial T2 TSE disc-pe-disc",
                "plane": "Axial angulat paralel cu discurile L3-L4, L4-L5, L5-S1",
                "tr_te": "TR 4000 ms / TE 105 ms",
                "slice_gap": "3.5 - 4.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 200 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Rădăcini nervoase în recesurile laterale și foramen, ligament galben",
            },
            {
                "name": "Axial T1 TSE",
                "plane": "Axial lombar inferior (L4-S1)",
                "tr_te": "TR 550 ms / TE 10 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 200 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Grăsime epidurală, delimitare hernie discală foraminală",
            },
        ],
        "quality_criteria": [
            "Cuprinderea conului medular și a primelor două vertebre sacrate",
            "Banda de presaturație abdominală anterioară activată pentru tăierea artefactelor respiratorii și aortice",
            "Centrare corectă angulată a pachetelor axiale pe spațiile discale intervertebrale",
        ],
        "safety_considerations": [
            "SAR bine tolerat pe coloană lombară",
            "La pacienți cu dureri severe, poziționarea unui rulou sub fosele poplitee ameliorează semnificativ confortul",
        ],
        "iris_reference": {
            "chapter": "Coloană Vertebrală - Segment Lombar",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "În caz de sindrom de coadă de cal, examinarea se efectuează în regim de urgență maximă pentru decompresiune chirurgicală precoce.",
    },

    # ------------------ MSK ------------------
    {
        "title": "IRM Genunchi",
        "slug": "irm-genunchi",
        "category": "msk",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Leziuni traumatice meniscale (fisure, rupturi în toartă de coș)",
            "Ruptură de ligament încrucișat anterior (LIA) sau posterior (LIP)",
            "Leziuni de ligamente colaterale (LCM, LCL) și ale unghiului postero-lateral",
            "Leziuni osteocondrale, osteocondrită disecantă, corpi liberi intra-articulari",
            "Dureri anterioare de genunchi, patologie rotuliană (condromalacie, instabilitate)",
        ],
        "contraindications": [
            "Contraindicații generale RM; materiale de sinteză metalice necompatibile.",
        ],
        "patient_prep": "Chestionar RM; genunchiul în extensie lejeră cu rotație externă de 5° pentru alinierea ligamentului încrucișat anterior în plan sagital.",
        "coils_hardware": {
            "coil": "Antenă dedicată de genunchi 16 sau 18 canale (Transceive/Receive)",
            "field_strength": "1.5T sau 3.0T (3T excelent pentru cartografierea cartilajului)",
            "positioning": "Decubit dorsal cu picioarele înainte, genunchiul fixat rigid în antenă cu perne de spumă.",
        },
        "contrast": {
            "agent": "Nativ în 95% din cazuri; substanță de contrast IV doar în suspiciuni de sinovită proliferativă (artrită reumatoidă, PVNS) sau tumori.",
            "dose": "Fără contrast de rutină",
            "flow_rate": "Nu este cazul",
            "timing": "Nu este cazul",
            "notes": "Artro-IRM cu contrast intra-articular este rezervată cazurilor de evaluare a meniscului operat (re-ruptură meniscală).",
        },
        "sequences": [
            {
                "name": "Sagital DP FatSat (Densitate de Protoni cu supresie de grăsime)",
                "plane": "Sagital",
                "tr_te": "TR 2800 ms / TE 30 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 150 mm / 320x256",
                "fat_sat": "FatSat / SPAIR",
                "notes": "Evaluare primară LIA, LIP, coarne meniscale, edem osos contuzional",
            },
            {
                "name": "Sagital T1 SE",
                "plane": "Sagital",
                "tr_te": "TR 550 ms / TE 12 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 150 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Anatomie meniscală, cartilaj articular, măduvă osoasă",
            },
            {
                "name": "Coronal DP FatSat",
                "plane": "Coronal",
                "tr_te": "TR 2800 ms / TE 30 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 150 mm / 320x256",
                "fat_sat": "FatSat / SPAIR",
                "notes": "Corpuri meniscale, ligamente colaterale (LCM, LCL), platou tibial",
            },
            {
                "name": "Coronal T1 SE",
                "plane": "Coronal",
                "tr_te": "TR 550 ms / TE 12 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 150 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Anatomie ligamentară colaterală și evaluare corticală",
            },
            {
                "name": "Axial DP FatSat",
                "plane": "Axial",
                "tr_te": "TR 2800 ms / TE 30 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 150 mm / 320x256",
                "fat_sat": "FatSat",
                "notes": "Cartilaj femuro-patelar, retinacule patelare, tendon rotulian și cvadricipital",
            },
        ],
        "quality_criteria": [
            "Supresie de grăsime uniformă și omogenă pe întregul FOV de 15 cm",
            "Vizualizarea continuă a traiectului LIA pe secvențele sagitale",
            "Absența artefactelor de mișcare (pacientul trebuie să mențină piciorul complet relaxat)",
        ],
        "safety_considerations": [
            "Antena dedicată reduce substanțial puterea necesară și SAR-ul total",
        ],
        "iris_reference": {
            "chapter": "Sistem Musculoscheletal - Articulația Genunchiului",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "Semnul 'kissing contusion' (edem pe condilul femural lateral și platoul tibial postero-lateral) indică cu specificitate înaltă ruptura acută de LIA.",
    },
    {
        "title": "IRM Umăr",
        "slug": "irm-umar",
        "category": "msk",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Ruptură de coafă a rotatorilor (tendon supraspinos, infraspinos, subscapular)",
            "Sindrom de impingement / conflict subacromial",
            "Instabilitate gleno-humerală anterioară/posterioară (leziuni Bankart, Hill-Sachs)",
            "Leziuni de labrum superior (SLAP lesion) și tendon lung al bicepsului",
            "Capsulită retractilă ('umăr înghețat') sau osteonecroză aseptică cap humeral",
        ],
        "contraindications": [
            "Contraindicații generale de securitate RM.",
        ],
        "patient_prep": "Chestionar RM; brațul în rotație neutră lejeră de-a lungul corpului cu palma în sus (supinație ușoară); se evită rotația internă forțată care suprapune structurile coafei.",
        "coils_hardware": {
            "coil": "Antenă dedicată de umăr 16 canale (Shoulder Coil mulată pe relief)",
            "field_strength": "1.5T sau 3.0T",
            "positioning": "Decubit dorsal, pacientul decalat ușor spre partea opusă pentru a aduce umărul cât mai aproape de izocentrul magnetului.",
        },
        "contrast": {
            "agent": "Nativ de regulă; Artro-IRM cu Gd diluat intra-articular (1:200 în ser) la sportivi tineri pentru leziuni de labrum și instabilitate glenohumerală.",
            "dose": "Nativ sau 12-15 ml soluție diluată intra-articular",
            "flow_rate": "Nu este cazul",
            "timing": "Scanare în maxim 30-45 minute de la puncția intra-articulară",
            "notes": "Pentru patologia degenerativă a coafei la vârstnici, examinarea nativă este pe deplin suficientă.",
        },
        "sequences": [
            {
                "name": "Coronal Oblic DP FatSat",
                "plane": "Coronal paralel cu tendonul supraspinos",
                "tr_te": "TR 2600 ms / TE 32 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 160 mm / 320x256",
                "fat_sat": "FatSat / SPAIR",
                "notes": "Secvența cheie pentru tendonul supraspinos și joncțiunea miotendinoasă",
            },
            {
                "name": "Coronal Oblic T1 SE",
                "plane": "Coronal oblic",
                "tr_te": "TR 550 ms / TE 12 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 160 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Atrofie musculară (clasificare Goutallier), bursă subacromială",
            },
            {
                "name": "Sagital Oblic T2 FatSat",
                "plane": "Sagital perpendicular pe fosa glenoidă",
                "tr_te": "TR 3000 ms / TE 45 ms",
                "slice_gap": "3.5 mm / gap 0.3 mm",
                "fov_matrix": "FOV 160 mm / 320x256",
                "fat_sat": "FatSat",
                "notes": "Forma acromionului (clasificare Bigliani), intervalul rotatorilor",
            },
            {
                "name": "Axial DP FatSat",
                "plane": "Axial",
                "tr_te": "TR 2800 ms / TE 30 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 160 mm / 320x256",
                "fat_sat": "FatSat",
                "notes": "Tendon subscapular, tendonul capului lung al bicepsului, labrum anterior/posterior",
            },
        ],
        "quality_criteria": [
            "Angulare precisă a planurilor coronale paralele cu corpul scapulei și fosa supraspinoasă",
            "Izocentrare optimă a articulației pentru eliminarea artefactelor de câmp la periferie",
            "Supresie spectrală excelentă a grăsimii pe întreaga arie periarticulară",
        ],
        "safety_considerations": [
            "Verificare prezență ancore de sutură sau șuruburi de interferență post-operatorii (de regulă titan sau PEEK bioresorbabil - compatibile)",
        ],
        "iris_reference": {
            "chapter": "Sistem Musculoscheletal - Articulația Umărului",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "Retracția tendonului supraspinos (stadiile Patte I-III) și degenerarea grasă musculară orientează decizia de reparare artroscopică.",
    },
    {
        "title": "IRM Bazin & Articulații Sacroiliace (Protocol Spondilartrită axSpA)",
        "slug": "irm-bazin-si-articulatii-sacroiliace",
        "category": "msk",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Lombalgie inflamatorie cronică la adult tânăr (< 45 ani) conform criteriilor ASAS",
            "Suspiciune de spondiloartrită axială / Spondilită anchilozantă în stadiu pre-radiografic",
            "Evaluarea activității inflamatorii (edem osos subcondral activ) înaintea inițierii terapiei biologice",
            "Diagnostic diferențial: osteitis condensans ilii, infecție (sacroiliită septică), fracturi de insuficiență",
        ],
        "contraindications": [
            "Contraindicații generale RM.",
        ],
        "patient_prep": "Chestionar RM; decubit dorsal, membre inferioare în extensie lejeră, bandă de compresie elastică pe abdomen inferior pentru reducerea artefactelor respiratorii.",
        "coils_hardware": {
            "coil": "Antenă Phased-Array Body / Pelvis 16-32 canale combinată cu antena Spine din masă",
            "field_strength": "1.5T sau 3.0T",
            "positioning": "Decubit dorsal, centrare pe linia medio-sagitală la 3 cm sub spinele iliace antero-superioare.",
        },
        "contrast": {
            "agent": "Nativ este suficient în 90% din cazuri conform ghidului ASAS/ESR; contrast IV rezervat pentru suspiciuni de sacroiliită septică (abcese pelvine).",
            "dose": "Fără contrast de rutină",
            "flow_rate": "Nu este cazul",
            "timing": "Nu este cazul",
            "notes": "Edemul osos activ subcondral se evaluează cu maximă sensibilitate pe secvența STIR.",
        },
        "sequences": [
            {
                "name": "Coronal Oblic STIR / TIRM",
                "plane": "Coronal oblic paralel cu axul lung al sacrului (S1-S3)",
                "tr_te": "TR 4500 ms / TE 45 ms / TI 160 ms",
                "slice_gap": "3.5 - 4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 200 - 220 mm / 320x256",
                "fat_sat": "STIR",
                "notes": "Secvența definitorie pentru sacroiliită activă conform criteriilor ASAS",
            },
            {
                "name": "Coronal Oblic T1 TSE",
                "plane": "Coronal oblic paralel cu sacrul",
                "tr_te": "TR 550 ms / TE 10 ms",
                "slice_gap": "3.5 - 4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 200 - 220 mm / 384x256",
                "fat_sat": "Nu",
                "notes": "Modificări structurale cronice: metaplazie grasă subcondrală, eroziuni, punți osoase, anchiloză",
            },
            {
                "name": "Axial Oblic T2 FatSat",
                "plane": "Axial oblic perpendicular pe sacru",
                "tr_te": "TR 3500 ms / TE 65 ms",
                "slice_gap": "3.5 mm / gap 0.4 mm",
                "fov_matrix": "FOV 200 mm / 320x256",
                "fat_sat": "FatSat / SPAIR",
                "notes": "Confirmare edem versant iliac vs. sacrat, capsulită și entezită",
            },
            {
                "name": "Coronal T1 TSE Bazin Întreg",
                "plane": "Coronal clasic",
                "tr_te": "TR 550 ms / TE 12 ms",
                "slice_gap": "4.0 mm / gap 0.5 mm",
                "fov_matrix": "FOV 380 mm / 384x256",
                "fat_sat": "Nu",
                "notes": "Evaluare globală articulații coxo-femurale (excludere necroză cap femural)",
            },
        ],
        "quality_criteria": [
            "Angulare obligatorie a planului coronal oblic pe fața anterioară a corpului sacrat S1-S3",
            "Supresie de grăsime omogenă pe ambele aripi iliace și masiv sacrat",
            "Rezoluție suficientă pentru decelarea eroziunilor subcondrale milimetrice",
        ],
        "safety_considerations": [
            "SAR moderat, examinare bine tolerată",
        ],
        "iris_reference": {
            "chapter": "Reumatologie - Spondilartropatii Seronegative",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "Criteriul ASAS pozitiv: prezența edemului osos subcondral (hipersemnal STIR) pe cel puțin două secțiuni consecutive sau în cel puțin două localizări pe aceeași secțiune.",
    },
    {
        "title": "IRM Gleznă & Picior",
        "slug": "irm-glezna-si-picior",
        "category": "msk",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Leziuni ligamentare după entorse severe (LFTA, LFC, ligament deltoid, sindesmoză tibio-fibulară)",
            "Tendinopatii și rupturi (tendon achilian, tendon tibial posterior, tendoane peroniere)",
            "Leziuni osteocondrale ale domului talar",
            "Sindrom de impingement de gleznă (anterior / posterior - os trigonum)",
            "Fasciită plantară, neurom Morton sau fracturi de stres metatarsiene",
        ],
        "contraindications": [
            "Contraindicații generale RM.",
        ],
        "patient_prep": "Chestionar RM; piciorul fixat la 90° flexie dorsală în antenă cu pernuțe de spumă pentru a evita tensionarea tendoanelor și relaxarea ligamentelor.",
        "coils_hardware": {
            "coil": "Antenă dedicată de picior/gleznă 16 canale (Foot/Ankle Coil)",
            "field_strength": "1.5T sau 3.0T",
            "positioning": "Decubit dorsal cu picioarele înainte, piciorul afectat în unghi drept (90°).",
        },
        "contrast": {
            "agent": "Nativ de regulă; contrast doar în caz de suspiciune de osteomielită, sinovită inflamatorie sau tumori de părți moi.",
            "dose": "Fără contrast de rutină",
            "flow_rate": "Nu este cazul",
            "timing": "Nu este cazul",
            "notes": "Nu se administrează contrast de rutină.",
        },
        "sequences": [
            {
                "name": "Sagital T1 SE",
                "plane": "Sagital",
                "tr_te": "TR 550 ms / TE 12 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 150 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Morfologie tendon achilian, aponevroză plantară, unghi talo-navicular",
            },
            {
                "name": "Sagital DP FatSat",
                "plane": "Sagital",
                "tr_te": "TR 2800 ms / TE 30 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 150 mm / 320x256",
                "fat_sat": "FatSat / SPAIR",
                "notes": "Rupturi tendinoase, bursită retrocalcaneană, edem dom talar",
            },
            {
                "name": "Coronal DP FatSat",
                "plane": "Coronal (paralel cu linia bimaleolară)",
                "tr_te": "TR 2800 ms / TE 30 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 140 mm / 320x256",
                "fat_sat": "FatSat",
                "notes": "Cartilaj dom talar, ligament deltoid și ligament calcaneo-fibular",
            },
            {
                "name": "Axial T2 TSE FatSat",
                "plane": "Axial (perpendicular pe tibie)",
                "tr_te": "TR 3500 ms / TE 65 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 140 mm / 320x256",
                "fat_sat": "FatSat",
                "notes": "Tendoane retromaleolare (tibial posterior, flexor lung, peroniere în culise)",
            },
        ],
        "quality_criteria": [
            "Menținerea strictă a unghiului de 90° fără inversie sau eversie pe durata scanării",
            "Absența artefactului de 'unghi magic' (magic angle artifact la 55°) pe tendoanele peroniere prin calibrarea TE > 30 ms",
        ],
        "safety_considerations": [
            "SAR scăzut pe extremitate periferică",
        ],
        "iris_reference": {
            "chapter": "Sistem Musculoscheletal - Gleznă și Picior",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "Leziunile ligamentului talo-fibular anterior (LFTA) se analizează excelent pe planul axial și coronal oblic ușor înclinat la 20°.",
    },

    # ------------------ ABDOMEN-PELVIS ------------------
    {
        "title": "IRM Ficat Multipfazic cu Substanță de Contrast Paramagnetic",
        "slug": "irm-ficat-multipfazic-cu-contrast",
        "category": "abdomen-pelvis",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Caracterizarea nodulilor hepatici descoperiți incidental la ecografie sau CT",
            "Screening și diagnostic hepatocarcinom (HCC) la pacienți cirotici conform criteriilor LI-RADS",
            "Diferențiere leziuni benigne (hemangiom, hiperplazie nodulară focală FNH, adenom hepatic) de leziuni maligne",
            "Bilanț pre-operator / transplant hepatic și stadializare metastaze hepatice",
        ],
        "contraindications": [
            "Contraindicații generale RM; eGFR < 30 ml/min (risc NSF la agenți non-recomandați).",
        ],
        "patient_prep": "À jeun minim 6 ore (repaus alimentar); exerciții de apnee ghidată explicate pacientului înainte de scanare; abord venos periferic de calibru mare (18-20G) în plica cotului.",
        "coils_hardware": {
            "coil": "Antenă Phased-Array Toraco-Abdominală 16-32 canale + antenă Spine",
            "field_strength": "1.5T sau 3.0T",
            "positioning": "Decubit dorsal, centrare pe rebordul costal inferior (apendice xifoid), curea de monitorizare respiratorie montată pe abdomen.",
        },
        "contrast": {
            "agent": "Chelat de Gadoliniu macrociclic extracelular sau agent hepato-specific (Acid Gadoxetic / Primovist)",
            "dose": "0.1 mmol/kg (sau 0.025 mmol/kg pentru Primovist)",
            "flow_rate": "2.0 ml/s urmat de bolus de spălare de 30 ml ser fiziologic",
            "timing": "Arterial tardiv (fluorotrigger pe aorta celiacă sau 18-22s), Portal (60-70s), Venos de tranziție (120s), Tardiv / Hepatobiliar (20 min la Primovist)",
            "notes": "Injectarea automată cu seringă cu două corpuri și temporizare precisă a fazei arteriale este critică pentru detecția hipercaptării arteriale HCC.",
        },
        "sequences": [
            {
                "name": "Coronal T2 HASTE / SSFSE",
                "plane": "Coronal",
                "tr_te": "Single-shot / TE 90 ms",
                "slice_gap": "5.0 mm / gap 0.5 mm",
                "fov_matrix": "FOV 380 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Anatomie generală abdominală și repere vasculare",
            },
            {
                "name": "Axial T1 Dual Echo (In-Phase / Out-of-Phase)",
                "plane": "Axial",
                "tr_te": "TR 140 ms / TE 2.2 ms (OP) și 4.4 ms (IP)",
                "slice_gap": "5.0 mm / gap 1.0 mm",
                "fov_matrix": "FOV 380 mm / 320x224",
                "fat_sat": "Nu",
                "notes": "Steatoză hepatică, încărcare lipidică intracelulară în adenoame",
            },
            {
                "name": "Axial T2 TSE cu supresie de grăsime (FatSat / SPAIR)",
                "plane": "Axial",
                "tr_te": "Gating respirator / TE 85 ms",
                "slice_gap": "5.0 mm / gap 1.0 mm",
                "fov_matrix": "FOV 380 mm / 320x256",
                "fat_sat": "FatSat",
                "notes": "Diferențiere hemangiom/chist (foarte strălucitor) de tumori solide",
            },
            {
                "name": "Axial DWI (b=50, 400, 800) + ADC Map",
                "plane": "Axial",
                "tr_te": "Gating respirator / TE 60 ms",
                "slice_gap": "5.0 mm / gap 1.0 mm",
                "fov_matrix": "FOV 380 mm / 192x160",
                "fat_sat": "FatSat",
                "notes": "Restricție de difuzie în leziuni maligne celulare (HCC, metastaze)",
            },
            {
                "name": "3D T1 GRE Dinamic multipfazic (VIBE / LAVA / THRIVE)",
                "plane": "Axial (apnee de 15 secunde per fază)",
                "tr_te": "TR 3.5 ms / TE 1.4 ms / FA 10°",
                "slice_gap": "3.0 mm interpolat la 1.5 mm",
                "fov_matrix": "FOV 380 mm / 320x224",
                "fat_sat": "Dixon / FatSat",
                "notes": "Faze: Nativ, Arterial tardiv, Portal venos, Echilibru (3 min) și Tardiv",
            },
        ],
        "quality_criteria": [
            "Apnee inspiratorie reproductibilă fără artefacte de 'ghosting' pe faza arterială",
            "Capacitatea de a surprinde wash-in arterial și wash-out venos tipice pentru LI-RADS 5",
            "Supresie omogenă a semnalului grăsimii pe întregul parenchim hepatic",
        ],
        "safety_considerations": [
            "Monitorizare respiratorie strictă; pacienții decompensați ascitici necesită secvențe 'free-breathing' cu navigare",
        ],
        "iris_reference": {
            "chapter": "Ficat și Căi Biliare - Hepatocarcinom și Leziuni Focale",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "Criteriile LI-RADS 5 (certitudine absolută de HCC): nodul > 10 mm pe ficat cirotic cu hipercaptare arterială non-încapsulată și wash-out tardiv cu pseudocapsulă.",
    },
    {
        "title": "Colangio-IRM (MRCP) - Evaluare Non-invazivă a Căilor Biliare",
        "slug": "colangio-irm-mrcp",
        "category": "abdomen-pelvis",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Icter mecanic obstructiv (diferențiere litiază coledociană vs. stenoză tumorală)",
            "Suspiciune de coledocolitiază cu ecografie neconcludentă",
            "Stadializare colangiocarcinom (tumoare Klatskin) și neoplasm de cap de pancreas",
            "Colangită sclerozantă primitivă (CSP) - diagnostic și monitorizare stricturi",
            "Anomalii congenitale ale arborelui biliar (chist de coledoc, pancreas divisum)",
        ],
        "contraindications": [
            "Contraindicații generale de securitate RM.",
        ],
        "patient_prep": "À jeun strict 6-8 ore pentru golirea stomacului și reținerea bilei în veziculă; administrare per os de 100-150 ml suc de ananas sau afine (bogat în mangan) cu 15 min înainte de examinare ca agent de contrast negativ natural pentru stingerea semnalului T2 din stomac și duoden.",
        "coils_hardware": {
            "coil": "Antenă Phased-Array Abdomen 16-32 canale",
            "field_strength": "1.5T sau 3.0T",
            "positioning": "Decubit dorsal, centrare pe rebordul costal drept.",
        },
        "contrast": {
            "agent": "Nativ (tehnică puternic hidroponderată T2 bazată pe proprietatea lichidului biliar staționar de a avea un timp T2 foarte lung). Substanță de contrast IV paramagnetică se asociază doar dacă se suspectează o masă tumorală pancreatică sau hepatică asociată.",
            "dose": "0 ml de rutină (sau 0.1 mmol/kg dacă se asociază bilanț tumoral)",
            "flow_rate": "Nu este cazul",
            "timing": "Nu este cazul",
            "notes": "MRCP este o procedură complet non-invazivă, înlocuind ERCP diagnostică care are risc de pancreatită post-procedurală de 3-5%.",
        },
        "sequences": [
            {
                "name": "Coronal T2 HASTE / SSFSE câmp mare",
                "plane": "Coronal",
                "tr_te": "Single-shot / TE 90 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 360 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Vedere de ansamblu hipocondru drept, ficat, stomac",
            },
            {
                "name": "Axial T2 FatSat subțire",
                "plane": "Axial",
                "tr_te": "Gating respirator / TE 85 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 350 mm / 320x256",
                "fat_sat": "FatSat",
                "notes": "Coledoc distal intrapancreatic, ampulă Vater, canal Wirsung",
            },
            {
                "name": "MRCP Gros Radiale Single-Shot (Thick-Slab)",
                "plane": "Radiale oblice centrate pe coledoc (la fiecare 15°)",
                "tr_te": "TR 4500 ms / TE 700 - 800 ms (ultra-T2)",
                "slice_gap": "Grosime 30 - 40 mm (o singură secțiune groasă)",
                "fov_matrix": "FOV 280 mm / 384x288",
                "fat_sat": "FatSat",
                "notes": "Imagine 'colangiografică' de proiecție instantanee a întregului arbore",
            },
            {
                "name": "3D MRCP Subțire de Înaltă Rezoluție (Navigated / Triggered)",
                "plane": "Coronal oblic 3D volumetric",
                "tr_te": "TR 2500 ms / TE 550 ms",
                "slice_gap": "1.0 mm izotrop reconstruibil multiplanar",
                "fov_matrix": "FOV 300 mm / 320x320",
                "fat_sat": "FatSat / SPAIR",
                "notes": "Gold standard pentru calculi milimetrici și stenoze fine",
            },
        ],
        "quality_criteria": [
            "Semnal intens alb strălucitor al căilor biliare intra- și extrahepatice și al canalului pancreatic",
            "Supresie completă a grăsimii și a lichidului digestiv suprapus",
            "Absența artefactelor de respirație prin utilizarea triggerului respirator adecvat",
        ],
        "safety_considerations": [
            "Complet non-invaziv, fără risc de pancreatită acută iatrogenă",
        ],
        "iris_reference": {
            "chapter": "Căi Biliare & Pancreas - Icter Mecanic",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "Calculii biliari apar caracteristic ca defecte de umplere cu semnal negru (hiposemnal) înconjurate de bila hiperintensă T2.",
    },
    {
        "title": "Entero-IRM (Protocol Boală Inflamatorie Intestinală - Crohn)",
        "slug": "entero-irm",
        "category": "abdomen-pelvis",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Evaluare inițială și monitorizare activitate inflamatorie în Boala Crohn",
            "Detecție complicații transmurale (stenoze fibroase vs. inflamatorii, fistule entero-enterice/cutanate, abcese mezenterice)",
            "Evaluare răspuns terapeutic la medicație biologică anti-TNF",
            "Urmărire la tineri și copii fără expunere la radiații ionizante",
        ],
        "contraindications": [
            "Ocluzie intestinală completă acută; contraindicații generale RM.",
        ],
        "patient_prep": "À jeun 6 ore; ingestie fracționată de 1000-1500 ml soluție hiperosmolară non-absorbabilă (PEG - polietilenglicol sau Manitol 2.5%) în decurs de 45-60 minute înainte de scanare pentru distensia uniformă a anselor de intestin subțire; administrare IV de antispastic (Butilscopolamină / Buscopan 20 mg sau Glucagon 1 mg) imediat înainte de secvențe.",
        "coils_hardware": {
            "coil": "Antenă Phased-Array Abdomen-Pelvis combinată (acoperire de la diafragm la simfiza pubiană)",
            "field_strength": "1.5T (preferabil pentru mai puține artefacte de susceptibilitate gazoasă) sau 3.0T",
            "positioning": "Decubit ventral (prone) preferat deoarece reduce grosimea abdomenului și separă ansele ileale, sau decubit dorsal dacă nu este tolerat.",
        },
        "contrast": {
            "agent": "Chelat de Gadoliniu macrociclic IV",
            "dose": "0.1 - 0.15 mmol/kg corp",
            "flow_rate": "2.0 - 2.5 ml/s injectare automată + 30 ml ser fiziologic",
            "timing": "Secvențe 3D T1 cu FatSat la 45s (arterial enteric), 70s (portal) și 180s (tardiv)",
            "notes": "Îngroșarea parietală > 3 mm cu hipercaptare stratificată mucoasă/submucoasă și edem T2 indică inflamație acută activă.",
        },
        "sequences": [
            {
                "name": "Coronal T2 HASTE / SSFSE Free-breathing",
                "plane": "Coronal abdomen-pelvis",
                "tr_te": "Single-shot / TE 90 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 420 mm / 384x256",
                "fat_sat": "Nu",
                "notes": "Evaluare distensie luminală pe tot cadrul jejuno-ileal",
            },
            {
                "name": "Coronal T2 cu supresie de grăsime (FatSat / SPAIR)",
                "plane": "Coronal",
                "tr_te": "Single-shot / TE 90 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 420 mm / 320x256",
                "fat_sat": "FatSat",
                "notes": "Edem parietal în strat submucos, lichid liber, colecții peridigestive",
            },
            {
                "name": "Axial T2 HASTE / TrueFISP cine-motilitate",
                "plane": "Axial pe ansele afectate (ileon terminal)",
                "tr_te": "TR 3.5 ms / TE 1.5 ms",
                "slice_gap": "4.0 mm / gap 0 mm",
                "fov_matrix": "FOV 350 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Apreciere peristaltică: stenozele rigide lipsite de motilitate",
            },
            {
                "name": "Axial & Coronal DWI (b=0, 600, 900) + ADC",
                "plane": "Axial și Coronal",
                "tr_te": "TR 4500 ms / TE 65 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 380 mm / 192x160",
                "fat_sat": "FatSat",
                "notes": "Restricție de difuzie corelată direct cu scorul endoscopic de inflamație",
            },
            {
                "name": "3D T1 GRE Dinamic multipfazic post-Gd",
                "plane": "Coronal și Axial",
                "tr_te": "TR 3.8 ms / TE 1.6 ms",
                "slice_gap": "2.5 mm interpolat la 1.2 mm",
                "fov_matrix": "FOV 400 mm / 320x256",
                "fat_sat": "Dixon / FatSat",
                "notes": "Priză de contrast parietală, semnul pieptenului (comb sign - vase vasa recta dilatate)",
            },
        ],
        "quality_criteria": [
            "Distensie luminală adecvată a anselor jejunale și a ileonului terminal (> 2-2.5 cm calibru)",
            "Absența artefactelor de peristaltică prin administrarea promptă a antispasticului",
            "Acoperire anatomică completă de la unghiul Treitz până la ampula rectală",
        ],
        "safety_considerations": [
            "Buscopan este contraindicat la pacienți cu glaucom cu unghi îngust, hipertrofie de prostată cu retenție de urină sau tahiaritmii severe (se poate folosi Glucagon)",
        ],
        "iris_reference": {
            "chapter": "Tub Digestiv - Boală Crohn și Boli Inflamatorii",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "Permite diferențierea precisă între stenoza inflamatorie activă (edem T2, difuzie restricționată, captare intensă) ce răspunde la terapie medicamentoasă și stenoza fibroasă cicatricială ce necesită rezecție chirurgicală sau dilatare.",
    },
    {
        "title": "IRM Prostată Multiparametrică (mpMRI) - Protocol PI-RADS v2.1",
        "slug": "irm-prostata-multiparametrica-mpmri",
        "category": "abdomen-pelvis",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Valoare PSA seric crescută sau în dinamică ascendentă (suspiciune cancer de prostată)",
            "Ghidare pentru biopsie prostatică țintită prin fuziune RMN-Ecografie (Fusion Biopsy)",
            "Stadializare loco-regională a adenocarcinomului de prostată (extensie extracapsulară ECE, invazie vezicule seminale)",
            "Supraveghere activă a pacienților cu cancer de prostată cu risc scăzut",
            "Evaluare recidivă biochimică după prostatectomie radicală sau radioterapie",
        ],
        "contraindications": [
            "Contraindicații generale RM; proteză totală de șold bilaterală din metal feromagnetic (artefacte majore).",
        ],
        "patient_prep": "Evacuare rectală în dimineața examinării (microclismă opțională); abstinență sexuală 3-4 zile anterior (pentru repleția veziculelor seminale); administrare Buscopan 20 mg IV pentru oprirea peristaltismului rectal; vezică urinară semi-plină (nu destinsă la maximum).",
        "coils_hardware": {
            "coil": "Antenă Pelvic Phased-Array multicanal de suprafață (fără necesar de antenă endorectală la 3.0T)",
            "field_strength": "Preferabil 3.0 Tesla (sau 1.5 Tesla cu antenă de suprafață performantă)",
            "positioning": "Decubit dorsal, centrare la 2 cm deasupra simfizei pubiene.",
        },
        "contrast": {
            "agent": "Chelat de Gadoliniu macrociclic",
            "dose": "0.1 mmol/kg corp",
            "flow_rate": "2.5 - 3.0 ml/s cu injector automat + 30 ml ser fiziologic",
            "timing": "Achiziție dinamică rapidă DCE (Dynamic Contrast-Enhanced) la fiecare 5-10 secunde timp de minimum 2 minute",
            "notes": "DCE este secvență secundară utilă în special pentru clarificarea leziunilor de zonă periferică clasificate PI-RADS 3.",
        },
        "sequences": [
            {
                "name": "T2 TSE de Înaltă Rezoluție Axial (Small FOV)",
                "plane": "Axial perpendicular pe uretra prostatică",
                "tr_te": "TR 4500 ms / TE 110 ms",
                "slice_gap": "3.0 mm / gap 0 mm",
                "fov_matrix": "FOV 180 mm / 384x320",
                "fat_sat": "Nu",
                "notes": "Anatomie zonală: zona de tranziție (TZ) și zona periferică (PZ), capsulă",
            },
            {
                "name": "T2 TSE Sagital și Coronal",
                "plane": "Sagital și Coronal",
                "tr_te": "TR 4000 ms / TE 100 ms",
                "slice_gap": "3.0 mm / gap 0 mm",
                "fov_matrix": "FOV 180 - 200 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Bază, apex, vezicule seminale, col vezical",
            },
            {
                "name": "DWI Multi-b (b=50, 800, 1400 s/mm²) + ADC Map",
                "plane": "Axial",
                "tr_te": "TR 5000 ms / TE 70 ms",
                "slice_gap": "3.0 mm / gap 0 mm",
                "fov_matrix": "FOV 180 mm / 128x128",
                "fat_sat": "FatSat",
                "notes": "Secvența dominantă pentru Zona Periferică (PZ)",
            },
            {
                "name": "Calculated Ultra-High b-value (b=2000 s/mm²)",
                "plane": "Axial",
                "tr_te": "Calculat sintetic sau achiziționat",
                "slice_gap": "3.0 mm / gap 0 mm",
                "fov_matrix": "FOV 180 mm / 128x128",
                "fat_sat": "FatSat",
                "notes": "Supresie completă a semnalului adenomatos benign de fond",
            },
            {
                "name": "3D T1 Dinamic DCE (Perfusion)",
                "plane": "Axial",
                "tr_te": "TR 3.5 ms / TE 1.4 ms / Rezoluție temporală < 7-10s",
                "slice_gap": "3.0 mm / gap 0 mm",
                "fov_matrix": "FOV 200 mm / 192x160",
                "fat_sat": "FatSat",
                "notes": "Captare precoce focală asimetrică și wash-out rapid",
            },
            {
                "name": "Axial T1 Pelvis Mare",
                "plane": "Axial",
                "tr_te": "TR 600 ms / TE 10 ms",
                "slice_gap": "4.0 mm / gap 0.5 mm",
                "fov_matrix": "FOV 360 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Adenopatii pelvine obturatorii/iliace și hemoragie post-biopsie",
            },
        ],
        "quality_criteria": [
            "Respectarea strictă a specificațiilor tehnice PI-RADS v2.1",
            "Absența artefactelor de distorsiune geometrică rectală pe secvența DWI (asigurată prin evacuare)",
            "Grosime de strat maximă de 3.0 mm fără spațiu între secțiuni (gap 0)",
        ],
        "safety_considerations": [
            "SAR bine controlat pe pelvis",
            "Examinarea se programează la minimum 6-8 săptămâni după o puncție biopsie prostatică pentru resorbția hematoamelor ce pot mima sau masca tumori",
        ],
        "iris_reference": {
            "chapter": "Urologie & Oncologie - Neoplasm Prostatic",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "Scor PI-RADS 1-5 atribuit fiecărei leziuni suspecte. Categoriile PI-RADS 4 și 5 indică suspiciune înaltă / foarte înaltă de malignitate clinic semnificativă (Gleason ≥ 3+4) și necesită biopsie țintită.",
    },
    {
        "title": "IRM Pelvis Feminin & Endometrioză Profundă Infiltrativă (DIE)",
        "slug": "irm-pelvis-feminin-si-endometrioza",
        "category": "abdomen-pelvis",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Suspiciune sau bilanț de endometrioză pelvină profundă (ligamente utero-sacrate, sept recto-vaginal, vezică, rect)",
            "Dismenoree severă, dispareunie profundă, dischezie și infertilitate",
            "Stadializare cancer de col uterin (extensie parametrială) și cancer de endometru (invazie miometrială)",
            "Caracterizarea maselor ovariene complexe conform scorului O-RADS MRI",
            "Cartografiere fibromatoză uterină (miometrectomie vs. embolizare artere uterine)",
        ],
        "contraindications": [
            "Contraindicații generale RM.",
        ],
        "patient_prep": "À jeun 4 ore; vezică urinară în semi-repleție (nu complet destinsă pentru a nu împinge uterul posterior); administrare Buscopan 20 mg IV pentru imobilizarea anselor sigmoidiene; opțional gel ultrasonografic opacifiant steril 50-100 ml vaginal și 100-150 ml rectal pentru distensia cavităților și evidențierea infiltrației septale.",
        "coils_hardware": {
            "coil": "Antenă Phased-Array Pelvis multicanal",
            "field_strength": "1.5T sau 3.0T",
            "positioning": "Decubit dorsal, centrare pe simfiza pubiană.",
        },
        "contrast": {
            "agent": "Chelat de Gadoliniu macrociclic",
            "dose": "0.1 mmol/kg corp",
            "flow_rate": "2.0 ml/s",
            "timing": "3D T1 FatSat dinamic precoce și tardiv",
            "notes": "În endometrioză nativul T1 cu și fără FatSat este critic pentru sângerările subacute; contrastul este util în adenocarcinom și diferențiere leziuni ovariene.",
        },
        "sequences": [
            {
                "name": "Sagital T2 TSE de Înaltă Rezoluție",
                "plane": "Sagital axat pe uter și canal anal",
                "tr_te": "TR 4500 ms / TE 105 ms",
                "slice_gap": "3.5 mm / gap 0.3 mm",
                "fov_matrix": "FOV 200 mm / 384x288",
                "fat_sat": "Nu",
                "notes": "Secvență de referință pentru fund de sac Douglas, sept recto-vaginal, perete rectal anterior",
            },
            {
                "name": "Axial T2 TSE oblic (perpendicular pe cavitatea uterină)",
                "plane": "Axial oblic",
                "tr_te": "TR 4000 ms / TE 100 ms",
                "slice_gap": "3.5 mm / gap 0.3 mm",
                "fov_matrix": "FOV 200 mm / 384x256",
                "fat_sat": "Nu",
                "notes": "Ligamente utero-sacrate, torul uterin, parametre, ovare",
            },
            {
                "name": "Axial T1 SE / TSE Nativ",
                "plane": "Axial",
                "tr_te": "TR 600 ms / TE 10 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 240 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Hipersemnal în chisturi endometrizice (endometrioame) și sângerări vechi",
            },
            {
                "name": "Axial T1 FatSat",
                "plane": "Axial",
                "tr_te": "TR 600 ms / TE 10 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 240 mm / 320x256",
                "fat_sat": "FatSat / SPAIR",
                "notes": "Diferențiere chist dermoid/teratom (semnal stins pe FatSat) de endometriom (semnal persistent înalt)",
            },
            {
                "name": "Axial DWI (b=0, 800) + ADC",
                "plane": "Axial",
                "tr_te": "TR 4500 ms / TE 70 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 240 mm / 192x160",
                "fat_sat": "FatSat",
                "notes": "Caracterizare noduli solizi ovarieni și stadializare neoplasm col/endometru",
            },
        ],
        "quality_criteria": [
            "Delimitare netă a zonei joncționale miometriale și a faldurilor seroase peritoneale",
            "Oprirea motilității rectale și uterine prin administrarea antispasticului",
        ],
        "safety_considerations": [
            "Nu se efectuează în timpul menstruației abundente dacă nu este urgent",
        ],
        "iris_reference": {
            "chapter": "Ginecologie & Pelvis Feminin - Endometrioză și Neoplasme",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "Semnul 'kissing ovaries' (ovare alipite pe linia mediană posterior de uter) indică aderențe pelvine severe și obliterarea fundului de sac Douglas.",
    },

    # ------------------ CARDIAC ------------------
    {
        "title": "IRM Cardiac - Evaluare Funcțională, Ischemie & Viabilitate (LGE)",
        "slug": "irm-cardiac-functional-si-viabilitate",
        "category": "cardiac",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Evaluare viabilitate miocardică post-infarct miocardic înainte de revascularizare (PCI/CABG)",
            "Diagnostic și diferențiere cardiomiopatii (dilatativă, hipertrofică, non-compactare, amiloidoză)",
            "Suspiciune de miocardită acută (criteriile Lake Louise actualizate)",
            "Cuantificare precisă volume ventriculare și fracție de ejecție (FEVS, FEVD - gold standard)",
            "Aritmii ventriculare de cauză neclară, displazie aritmogenă de ventricul drept (ARVD)",
        ],
        "contraindications": [
            "Stimulatoare cardiace sau ICD incompatibile RM; aritmii frecvente necontrolate (fibrilație atrială rapidă - afectează triggerul ECG); eGFR < 30 ml/min.",
        ],
        "patient_prep": "Fără cofeină, fumat sau energizante cu 12 ore înainte; electrozi ECG compatibili RM plasați pe torace; instruire atentă privind apneea inspiratorie repetată de 8-12 secunde.",
        "coils_hardware": {
            "coil": "Antenă Phased-Array Cardiacă dedicată 32 canale cu gating ECG integrat",
            "field_strength": "1.5T (standard de aur pentru bSSFP fără artefacte de banding) sau 3.0T",
            "positioning": "Decubit dorsal, centrare pe linia mediosternală la nivelul spațiului IV intercostal.",
        },
        "contrast": {
            "agent": "Chelat de Gadoliniu macrociclic",
            "dose": "0.15 - 0.20 mmol/kg corp (împărțit în bolus de perfuzie și bolus de viabilitate)",
            "flow_rate": "3.5 - 4.0 ml/s cu injector automat",
            "timing": "Secvențe LGE (Late Gadolinium Enhancement) achiziționate la 10-15 minute post-injectare",
            "notes": "Timpul de inversie (TI) se calibrează precis prin secvență Look-Locker pentru a anula complet semnalul miocardului sănătos (miocard negru).",
        },
        "sequences": [
            {
                "name": "Cine-bSSFP Ax Scurt (Short-Axis Stack)",
                "plane": "Ax scurt ventricular de la bază la apex",
                "tr_te": "TR 3.0 ms / TE 1.5 ms / 30 faze/ciclu",
                "slice_gap": "8.0 mm / gap 2.0 mm",
                "fov_matrix": "FOV 340 mm / 256x216",
                "fat_sat": "Nu",
                "notes": "Cuantificare volume end-diastolice/sistolice, masă VS, fracție de ejecție",
            },
            {
                "name": "Cine-bSSFP Axe Lungi (2-Chamber, 3-Chamber, 4-Chamber)",
                "plane": "Axe lungi cardiace",
                "tr_te": "TR 3.0 ms / TE 1.5 ms",
                "slice_gap": "6.0 mm / gap 0 mm",
                "fov_matrix": "FOV 340 mm / 256x216",
                "fat_sat": "Nu",
                "notes": "Cinetica segmentară a pereților conform modelului AHA 17 segmente",
            },
            {
                "name": "T2-STIR Black Blood (Edem Miocardic)",
                "plane": "Ax scurt și 4 camere",
                "tr_te": "Dual-inversion recovery / TE 65 ms",
                "slice_gap": "8.0 mm / gap 2.0 mm",
                "fov_matrix": "FOV 340 mm / 256x192",
                "fat_sat": "STIR",
                "notes": "Raport intensitate semnal miocard/mușchi scheletic > 1.9 indică edem acut",
            },
            {
                "name": "T1 Mapping nativ și post-contrast (ECV)",
                "plane": "Ax scurt (bază, mediu, apex)",
                "tr_te": "MOLLI / SASHA",
                "slice_gap": "8.0 mm",
                "fov_matrix": "FOV 340 mm / 256x192",
                "fat_sat": "Nu",
                "notes": "Cuantificare fracție de volum extracelular (ECV) - crescut în amiloidoză și fibroză difuză",
            },
            {
                "name": "Late Gadolinium Enhancement (LGE 2D/3D PSIR)",
                "plane": "Ax scurt complet, 2C, 3C, 4C",
                "tr_te": "TR 700 ms / TE 3.0 ms / TI 250-320 ms",
                "slice_gap": "8.0 mm / gap 2.0 mm",
                "fov_matrix": "FOV 340 mm / 256x216",
                "fat_sat": "Inversion Recovery",
                "notes": "Infarct: captare subendocardică/transmurală pe teritoriu coronarian; Miocardită: captare subepicardică/mediomiocardică",
            },
        ],
        "quality_criteria": [
            "Sincronizare ECG stabilă fără erori de trigger pe unda R",
            "Anularea perfectă a semnalului miocardului normal (miocard 'negru') pe secvențele LGE",
            "Apnee inspiratorie stabilă și reproductibilă",
        ],
        "safety_considerations": [
            "Monitorizare ritm cardiac în permanență în sala de scanare",
            "Defibrilator extern compatibil RM disponibil în zona de pregătire",
        ],
        "iris_reference": {
            "chapter": "Cardiologie - Imagistică Cardiovasculară",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "Transmuralitatea LGE prezice șansa de recuperare funcțională post-revascularizare: dacă fibroza ocupă < 50% din grosimea peretelui, segmentul este viabil și contractilitatea se poate recupera.",
    },

    # ------------------ SAN ------------------
    {
        "title": "IRM Mamar Bilateral cu Substanță de Contrast - Protocol BI-RADS",
        "slug": "irm-mamar-bilateral-cu-contrast",
        "category": "san",
        "modality": "irm",
        "last_updated": "2026-09-13",
        "author": "Departamentul de Radiologie și Imagistică Medicală",
        "clinical_indications": [
            "Screening la femei cu risc înalt genetic (mutații BRCA1, BRCA2, istoric familial marcat)",
            "Stadializare loco-regională cancer mamar nou diagnosticat (evaluare multifocalitate, multicentricitate, bilateralitate)",
            "Evaluare răspuns la chimioterapie neoadjuvantă (monitorizare reducere volum tumoral)",
            "Suspiciune de recidivă tumorală pe cicatrice post-operatorie",
            "Carcinom ocult cu metastază ganglionară axilară și mamografie/ecografie negative",
            "Evaluarea integrității implantelor mamare (ruptură intracapsulară / extracapsulară)",
        ],
        "contraindications": [
            "Contraindicații generale RM; sarcină (contraindicație relativă la Gadoliniu); eGFR < 30 ml/min.",
        ],
        "patient_prep": "Programare optimă în zilele 7 - 14 ale ciclului menstrual (faza foliculară) pentru minimalizarea captării hormonale fiziologice de fond (BPE - background parenchymal enhancement); cateter venos 20G montat în antebraț cu prelungitor lung pentru injectare din exterior.",
        "coils_hardware": {
            "coil": "Antenă mamară dedicată multicanal (Bilateral Breast Coil 8-16 canale)",
            "field_strength": "1.5T sau 3.0T",
            "positioning": "Decubit ventral (prone), ambii sâni coborâți liber în cupele antenei fără compresie excesivă.",
        },
        "contrast": {
            "agent": "Chelat de Gadoliniu macrociclic",
            "dose": "0.1 mmol/kg corp",
            "flow_rate": "2.0 - 2.5 ml/s cu injector automat + 20-30 ml ser fiziologic",
            "timing": "Achiziție dinamică rapidă pre-contrast și post-contrast în 5-6 faze consecutive la fiecare 60-90 secunde timp de minimum 6-7 minute",
            "notes": "Generarea automată a imaginilor de substracție (post-contrast minus pre-contrast) și a curbelor cinetice (Tip I progresivă, Tip II platou, Tip III wash-out).",
        },
        "sequences": [
            {
                "name": "Axial T2 TSE de Înaltă Rezoluție",
                "plane": "Axial bilateral",
                "tr_te": "TR 4500 ms / TE 100 ms",
                "slice_gap": "3.0 mm / gap 0 mm",
                "fov_matrix": "FOV 340 mm / 384x320",
                "fat_sat": "Nu",
                "notes": "Chisturi, fibroadenoame (hipersemnal T2), edem cutanat, arhitectură glandulară",
            },
            {
                "name": "Axial DWI (b=0, 800-1000) + ADC Map",
                "plane": "Axial bilateral",
                "tr_te": "TR 4500 ms / TE 60 ms",
                "slice_gap": "3.0 mm / gap 0 mm",
                "fov_matrix": "FOV 340 mm / 192x160",
                "fat_sat": "FatSat",
                "notes": "Restricție de difuzie corelată cu celularitatea înaltă din leziuni maligne",
            },
            {
                "name": "Axial T1 Nativ Fără FatSat",
                "plane": "Axial",
                "tr_te": "TR 600 ms / TE 10 ms",
                "slice_gap": "3.0 mm / gap 0 mm",
                "fov_matrix": "FOV 340 mm / 384x256",
                "fat_sat": "Nu",
                "notes": "Cartografiere anatomie și diferențiere sângerare/chist hemoragic",
            },
            {
                "name": "3D T1 GRE Dinamic multipfazic cu supresie de grăsime",
                "plane": "Axial bilateral (apnee sau respirație superficială)",
                "tr_te": "TR 4.5 ms / TE 1.7 ms / FA 12°",
                "slice_gap": "1.0 - 1.5 mm izotrop",
                "fov_matrix": "FOV 340 mm / 384x384",
                "fat_sat": "Dixon / FatSat",
                "notes": "1 fază nativă + 5 faze post-contrast seriate la 60-90s; substracție automată",
            },
            {
                "name": "Sagital T1 + C de Înaltă Rezoluție (pe sânul afectat)",
                "plane": "Sagital unilateral",
                "tr_te": "TR 550 ms / TE 10 ms",
                "slice_gap": "2.5 mm / gap 0 mm",
                "fov_matrix": "FOV 200 mm / 320x256",
                "fat_sat": "FatSat",
                "notes": "Evaluare detaliată a extensiei ductale și a distanței față de mamelon și mușchiul pectoral",
            },
        ],
        "quality_criteria": [
            "Poziționare impecabilă a ambilor sâni fără plicaturare cutanată sau contact cu marginea antenei",
            "Supresie de grăsime perfect omogenă bilateral pe secvențele dinamice",
            "Calcularea obligatorie a curbelor cinetice intensitate-timp pe stația de post-procesare dedicată",
        ],
        "safety_considerations": [
            "SAR bine tolerat pe bobină dedicată",
            "Pentru evaluarea rupturii de implant mamar siliconic se rulează secvențe suplimentare dedicate de supresie a apei și supresie a grăsimii (secvență 'Silicon Only')",
        ],
        "iris_reference": {
            "chapter": "Senologie - Diagnostic și Screening Mamar",
            "recommendation_grade": "Grad A",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
        },
        "notes": "Curba cinetică de tip III (wash-out rapid precoce) are specificitate de peste 85-90% pentru carcinom invaziv. Leziunile se clasifică conform categoriilor BI-RADS MRI (1 la 6).",
    },
]


def main():
    print(f"Inițializare structură foldere IRM în {DOCS_IRM}...")
    DOCS_IRM.mkdir(parents=True, exist_ok=True)

    # 1. Creează .pages și index.md pentru docs/irm/
    pages_content = "title: Protocoale IRM\nnav:\n  - index.md\n"
    for cat_slug, cat_info in CATEGORIES.items():
        pages_content += f"  - {cat_info['title']}: {cat_slug}\n"
    (DOCS_IRM / ".pages").write_text(pages_content, encoding="utf-8")

    index_content = """---
title: Ghidul Protocoalelor de Rezonanță Magnetică (IRM)
hide:
  - navigation
  - toc
---

# Ghidul Protocoalelor de Rezonanță Magnetică (IRM)

Protocoale clinice și tehnice standardizate de **Imagistică prin Rezonanță Magnetică (IRM)** pentru domeniile esențiale: neuroradiologie, sistem musculoscheletal, abdomen-pelvis, cardio-IRM și senologie. Toate protocoalele sunt adaptate recomandărilor **Ghidului Național IRIS (Ordinul MS 1342/2012)** și ghidurilor internaționale de bună practică (ACR, ESR, ESUR, PI-RADS, BI-RADS).

<div class="iris-official-banner" style="margin-bottom: 24px;">
  <div class="iris-official-badge">🧲 CÂMP MAGNETIC NON-IONANT & SECURITATE RM</div>
  <p class="iris-official-desc" style="margin-bottom: 8px !important;">
    Examinările IRM nu utilizează radiații ionizante (Clasa de iradiere 0). Securitatea este guvernată de screening-ul feromagnetic riguros (Zona III / Zona IV), limitele SAR (&lt; 2.0 W/kg) și protocoalele stricte de utilizare a substanțelor de contrast pe bază de Gadoliniu macrociclic.
  </p>
  <a href="../iris/" style="font-weight: 600; color: #0f766e; text-decoration: none;">
    Consultă recomandările din Ghidul IRIS ➔
  </a>
</div>

<p class="body-parts-section-heading">Navigare după Domeniul Clinic</p>

<div class="body-parts-grid">
  <a href="neuro/" class="body-part-card">
    <h3>Neuroradiologie IRM (Cerebral & Coloană)</h3>
  </a>
  <a href="msk/" class="body-part-card">
    <h3>Sistem Musculoscheletal (Genunchi, Umăr, Bazin, Gleznă)</h3>
  </a>
  <a href="abdomen-pelvis/" class="body-part-card">
    <h3>Abdomen & Pelvis (Ficat, MRCP, Entero-IRM, Prostată, Pelvis Feminin)</h3>
  </a>
  <a href="cardiac/" class="body-part-card">
    <h3>Cardio-IRM (Funcție, Viabilitate LGE, Miocardită)</h3>
  </a>
  <a href="san/" class="body-part-card">
    <h3>IRM Mamar Multiparametric (Protocol BI-RADS)</h3>
  </a>
</div>
"""
    (DOCS_IRM / "index.md").write_text(index_content, encoding="utf-8")

    # 2. Creează subcategoriile
    for cat_slug, cat_info in CATEGORIES.items():
        cat_dir = DOCS_IRM / cat_slug
        cat_dir.mkdir(parents=True, exist_ok=True)

        # .pages pentru subcategorie
        sub_pages = f"title: {cat_info['title']}\n"
        (cat_dir / ".pages").write_text(sub_pages, encoding="utf-8")

        # index.md pentru subcategorie
        sub_index = f"""---
title: {cat_info['title']}
---

# {cat_info['title']}

{cat_info['desc']}

Conspectați lista de protocoale standardizate disponibile mai jos:
"""
        (cat_dir / "index.md").write_text(sub_index, encoding="utf-8")

    # 3. Generează fișierele protocoalelor
    print(f"Generare {len(PROTOCOLS)} protocoale clinice IRM...")
    for p in PROTOCOLS:
        cat_slug = p["category"]
        file_name = f"{p['slug']}.md"
        out_path = DOCS_IRM / cat_slug / file_name
        md_text = render_irm_document(p)
        out_path.write_text(md_text, encoding="utf-8")
        print(f"  ✓ Creat: {out_path.relative_to(REPO_ROOT)}")

    print("Toate protocoalele IRM au fost generate cu succes!")


if __name__ == "__main__":
    main()
