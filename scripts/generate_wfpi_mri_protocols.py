#!/usr/bin/env python3
"""generate_wfpi_mri_protocols.py — Generează protocoalele IRM pediatrice standardizate WFPI.

Sursa: World Federation of Pediatric Imaging (WFPI)
URL: https://wfpiweb.org/Resources/Modalities/MRIProtocols.aspx
Ghid: "International standardization of pediatric magnetic resonance imaging protocols"
      (Pediatr Radiol 2024, DOI: 10.1007/s00247-024-06041-0)
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

from render_irm_protocol import render_irm_document

TARGET_DIR = ROOT / "docs" / "irm" / "pediatrie"
TARGET_DIR.mkdir(parents=True, exist_ok=True)

COMMON_SOURCES = [
    {
        "title": "WFPI Pediatric MRI Protocols — World Federation of Pediatric Imaging",
        "url": "https://wfpiweb.org/Resources/Modalities/MRIProtocols.aspx",
        "institution": "WFPI",
        "kind": "Standard internațional de imagistică pediatrică",
    },
    {
        "title": "International standardization of pediatric MRI protocols (Ferraciolli et al., Pediatr Radiol 2024)",
        "url": "https://doi.org/10.1007/s00247-024-06041-0",
        "institution": "WFPI / Springer",
        "kind": "Ghid clinic publicat",
    },
    {
        "title": "Ghidul Național de Utilizare a Tehnologiilor Imagistice (Ordinul MS 1342/2012 - Ghid IRIS)",
        "url": "https://radiologie-pediatrica.ro/iris/",
        "institution": "Ministerul Sănătății România",
        "kind": "Ghid național de referință",
    },
]

PROTOCOLS = [
    # 1. Rapid Brain Protocol
    {
        "slug": "irm-pediatric-rapid-brain",
        "title": "RM Pediatric — Protocol Cerebral Rapid (Rapid Brain)",
        "category": "pediatrie",
        "modality": "irm",
        "author": "World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie",
        "last_updated": "2026-09-20",
        "clinical_indications": [
            "Copii mici sau necooperanți cu toleranță scăzută la examinare (< 10-11 minute)",
            "Traumatism cranio-cerebral acut în urgență când se dorește evitarea iradierii prin CT",
            "Suspiciune de leziuni axonale difuze sau hemoragie intracraniană subacută",
            "Alterare acută a stării de conștiență / letargie de cauză neelucidată",
            "Screening neuro-pediatric rapid fără necesitatea anesteziei generale sau a sedării",
        ],
        "contraindications": [
            "Implanturi metalice feromagnetice sau dispozitive active non-MR Conditional",
            "Instabilitate hemodinamică sau respiratorie severă care necesită monitorizare invazivă de terapie intensivă",
        ],
        "patient_prep": "Pregătire 'feed-and-wrap' pentru sugari (hrănire și înfășare înainte de scanare); căști audio cu muzică/povești pentru copii cooperanți; fără sedare medicamentoasă.",
        "coils_hardware": {
            "coil": "Antenă dedicată Head/Neck multicanal (16–32 canale) cu pernuțe de imobilizare",
            "field_strength": "1.5 Tesla / 3.0 Tesla",
            "positioning": "Decubit dorsal, cap centrat în izocentru, pernuțe moi laterale pentru prevenirea rotației",
        },
        "contrast": {
            "agent": "Fără contrast (protocol nativ rapid)",
            "dose": "N/A",
            "flow_rate": "N/A",
            "timing": "N/A",
            "notes": "Examinare exclusiv nativă pentru reducerea timpului total la sub 10-11 minute.",
        },
        "sequences": [
            {
                "name": "Axial DWI (b=0, b=1000) + hartă ADC",
                "plane": "Axial",
                "tr_te": "TR 3000-4000 ms / TE 60-80 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 200-220 mm / 128x128",
                "fat_sat": "FatSat (EPI)",
                "notes": "Detectare ischemie acută, edem citotoxic, celularitate crescută (1-2 min)",
            },
            {
                "name": "Axial EPI T2* / GRE",
                "plane": "Axial",
                "tr_te": "TR 500-800 ms / TE 15-25 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 200-220 mm / 256x192",
                "fat_sat": "Nu",
                "notes": "Sensibilitate înaltă la hemoragie acută/subacută, depuneri de hemosiderină (0.5 min)",
            },
            {
                "name": "Sagital T1WI TSE / SE",
                "plane": "Sagital",
                "tr_te": "TR 450-600 ms / TE 8-12 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 200-220 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Anatomie linie mediană, corp calos, fosă posterioară, poziție amigdale cerebeloase (2-3 min)",
            },
            {
                "name": "Axial T2WI TSE",
                "plane": "Axial",
                "tr_te": "TR 3500-4500 ms / TE 90-110 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 200-220 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Diferențiere substanță albă/cenușie, edem vasogenic, mielinizare conform vârstei (2-3 min)",
            },
            {
                "name": "Coronal FLAIR",
                "plane": "Coronal",
                "tr_te": "TR 8000-9000 ms / TE 90-120 ms / TI 2200-2500 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 200-220 mm / 256x224",
                "fat_sat": "Nu",
                "notes": "Supresie semnal LCR, leziuni cortico-subcorticale, spații periventriculare (2-3 min)",
            },
        ],
        "quality_criteria": [
            "Timp total de scanare la aparat menținut strict sub 11 minute",
            "Axial DWI și T2* fără artefacte severe de mișcare",
            "Vizualizare clară a ventriculilor și a fosei posterioare fără trunchiere anatomică",
        ],
        "safety_considerations": [
            "Protecție fonică dublă obligatorie (căști fonoizolante + dopuri moi adaptate pediatric)",
            "Monitorizare vizuală permanentă și pulsoximetrie compatibilă RM",
            "SAR menținut în limite normale (< 2.0 W/kg)",
        ],
        "iris_reference": {
            "chapter": "Pediatrie - Sistem Nervos Central",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            "recommendation_grade": "Grad A",
        },
        "notes": "Standard internațional WFPI conceput pentru a oferi un diagnostic complet în 10 minute, evitând sedarea și iradierea pediatrică.",
        "sources": COMMON_SOURCES,
    },

    # 2. Seizure Brain Protocol
    {
        "slug": "irm-pediatric-epilepsie-convulsii",
        "title": "RM Pediatric — Protocol Convulsii & Epilepsie (Seizure Brain)",
        "category": "pediatrie",
        "modality": "irm",
        "author": "World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie",
        "last_updated": "2026-09-20",
        "clinical_indications": [
            "Crize convulsive cu debut recent sau epilepsie refractară la tratament medicamentos",
            "Suspiciune de displazie corticală focală (FCD) sau anomalie de migrare neuronală",
            "Scleroză mezială temporală / hipocampică",
            "Evaluare prechirurgicală a epilepsiei rezistente la copil",
            "Convulsii febrile atipice sau prelungite",
        ],
        "contraindications": [
            "Dispozitive medicale implantate non-MR Conditional",
            "Claustrofobie severă sau agitație extremă necontrolată",
        ],
        "patient_prep": "Pregătire atentă a copilului; la pacienții sub 2 ani se ajustează parametrii de mielinizare; pentru examinări de înaltă rezoluție se recomandă tehnici 'feed-and-wrap' sau sedare dacă este strict necesară.",
        "coils_hardware": {
            "coil": "Antenă Head/Neck de înaltă densitate (32 sau 64 canale)",
            "field_strength": "3.0 Tesla (preferat) sau 1.5 Tesla",
            "positioning": "Decubit dorsal, aliniere anatomică riguroasă, fixare cap cu suporturi speciale",
        },
        "contrast": {
            "agent": "Nativ (contrastul nu este indicat de rutină în epilepsie fără suspiciune tumorală)",
            "dose": "N/A",
            "flow_rate": "N/A",
            "timing": "N/A",
            "notes": "Contrastul se administrează doar dacă se identifică leziuni focale suspecte de natură tumorală sau infecțioasă.",
        },
        "sequences": [
            {
                "name": "Axial DWI (b=0, b=1000) + hartă ADC",
                "plane": "Axial",
                "tr_te": "TR 3500 ms / TE 70 ms",
                "slice_gap": "3.0-4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 220 mm / 192x192",
                "fat_sat": "FatSat (EPI)",
                "notes": "Excludere edem citotoxic post-critic, leziuni ischemice recente (1-2 min)",
            },
            {
                "name": "3D T1WI Izotrop Sagital (MPRAGE / BRAVO)",
                "plane": "Sagital 3D Izotrop",
                "tr_te": "TR 1900-2300 ms / TE 2.5-3.0 ms / TI 900 ms",
                "slice_gap": "1.0 mm izotrop (fără gap)",
                "fov_matrix": "FOV 240 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Grosime corticală, joncțiune substanță albă/cenușie, reformate multiplanare fine (5-7 min)",
            },
            {
                "name": "Axial T2WI TSE",
                "plane": "Axial",
                "tr_te": "TR 4000-5000 ms / TE 100 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 220 mm / 384x288",
                "fat_sat": "Nu",
                "notes": "Diferențiere structurală lobară, heterotopii nodulare (3-5 min)",
            },
            {
                "name": "Coronal T2WI Oblic (perpendicular pe axul hipocampilor)",
                "plane": "Coronal Oblic",
                "tr_te": "TR 4000-5000 ms / TE 100-110 ms",
                "slice_gap": "2.0-3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 180-200 mm / 320x256",
                "fat_sat": "Nu",
                "notes": "Orientat strict perpendicular pe axul lung al hipocampilor; volumetrie și semnal hipocampic (3-4 min)",
            },
            {
                "name": "Axial EPI / T2* GRE / SWI",
                "plane": "Axial",
                "tr_te": "TR 600-800 ms / TE 20 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 220 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Detecție cavernoame, calcificări (tuberoză scleroasă, Sturge-Weber) (2 min)",
            },
            {
                "name": "3D FLAIR Axial (Opțional, recomandat la > 2 ani)",
                "plane": "Axial 3D",
                "tr_te": "TR 8000 ms / TE 100 ms / TI 2400 ms",
                "slice_gap": "1.0-1.2 mm izotrop",
                "fov_matrix": "FOV 230 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Hipersemnal discret în displaziile corticale focale și scleroza hipocampică (4-5 min)",
            },
        ],
        "quality_criteria": [
            "Rezoluție sub-milimetrică pe secvența 3D T1 cu contrast optim substanță albă / substanță cenușie",
            "Orientare precisă a planului coronal perpendicular pe axul hipocampilor",
            "Absența artefactelor de mișcare la nivelul lobilor temporali",
        ],
        "safety_considerations": [
            "La 3.0T se monitorizează atent SAR-ul din cauza secvențelor FSE/FLAIR lungi",
            "Protecție acustică dublă adaptată vârstei",
        ],
        "iris_reference": {
            "chapter": "Pediatrie - Sistem Nervos Central",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            "recommendation_grade": "Grad A",
        },
        "notes": "Protocol optimizat conform ghidurilor WFPI și ILAE pentru detecția focarelor epileptogene subtile la copil.",
        "sources": COMMON_SOURCES,
    },

    # 3. Hydrocephalus - Ventricle Check Protocol
    {
        "slug": "irm-pediatric-hidrocefalie-control-ventriculi",
        "title": "RM Pediatric — Protocol Hidrocefalie & Control Ventriculi / Șunt (Quick Brain)",
        "category": "pediatrie",
        "modality": "irm",
        "author": "World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie",
        "last_updated": "2026-09-20",
        "clinical_indications": [
            "Monitorizare ventriculomegalie și dinamică ventriculară la copilul cu hidrocefalie",
            "Suspiciune de disfuncție de șunt ventriculo-peritoneal (obstrucție, hiperdrenaj)",
            "Evaluare colecții lichidiene extra-axiale / subdurale",
            "Alternativă completă non-iradiantă la scanarea CT repetată a capului",
            "Control rapid post-operator neurochirurgical",
        ],
        "contraindications": [
            "Implanturi feromagnetice nesigure RM (atenție la valvele de șunt reglabile: necesită reverificarea setării de presiune după RM conform indicațiilor producătorului)",
        ],
        "patient_prep": "Nu necesită pregătire specială, post alimentar sau sedare. Copilul poate rămâne îmbrăcat în haine fără capse metalice.",
        "coils_hardware": {
            "coil": "Antenă Head standard sau antenă flexibilă de corp dacă e necesar",
            "field_strength": "1.5 Tesla sau 3.0 Tesla",
            "positioning": "Decubit dorsal, poziționare rapidă",
        },
        "contrast": {
            "agent": "Fără contrast (protocol ultra-rapid)",
            "dose": "N/A",
            "flow_rate": "N/A",
            "timing": "N/A",
            "notes": "Protocol exclusiv nativ ultra-rapid (3–5 minute).",
        },
        "sequences": [
            {
                "name": "Axial Single-shot T2WI (HASTE / SSFSE)",
                "plane": "Axial",
                "tr_te": "TR 1000-1500 ms / TE 90-120 ms",
                "slice_gap": "3.0-4.0 mm / gap 0 mm",
                "fov_matrix": "FOV 200-220 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Achiziție ultra-rapidă (sub 1 secundă per secțiune), complet insensibilă la mișcarea pacientului (1 min)",
            },
            {
                "name": "Sagital Single-shot T2WI (HASTE / SSFSE)",
                "plane": "Sagital",
                "tr_te": "TR 1000-1500 ms / TE 90-120 ms",
                "slice_gap": "3.0-4.0 mm / gap 0 mm",
                "fov_matrix": "FOV 200-220 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Evaluare apeduct Sylvius, ventricul IV, foramen magnum și traiect cateter ventricular (1 min)",
            },
            {
                "name": "Coronal Single-shot T2WI (HASTE / SSFSE)",
                "plane": "Coronal",
                "tr_te": "TR 1000-1500 ms / TE 90-120 ms",
                "slice_gap": "3.0-4.0 mm / gap 0 mm",
                "fov_matrix": "FOV 200-220 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Evaluare coarne frontale și temporale ale ventriculilor laterali, colecții extra-axiale (1 min)",
            },
            {
                "name": "Axial DWI (Opțional)",
                "plane": "Axial",
                "tr_te": "TR 3000 ms / TE 70 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 200 mm / 128x128",
                "fat_sat": "FatSat",
                "notes": "Opțional, pentru excludere ventriculită sau complicații ischemice (1-2 min)",
            },
        ],
        "quality_criteria": [
            "Timp total de examinare la aparat: 3 până la 5 minute",
            "Vizualizare clară a conturului ventricular în toate cele 3 planuri",
            "Complet imun la artefactele respiratorii sau de agitație motorie",
        ],
        "safety_considerations": [
            "Verificare obligatorie a tipului de valvă de șunt: dacă este valvă reglabilă magnetic (ex. Codman, Strata, Polaris), este obligatorie verificarea și reprogramarea presiunii de către neurochirurg imediat după examinare!",
        ],
        "iris_reference": {
            "chapter": "Pediatrie - Sistem Nervos Central",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            "recommendation_grade": "Grad A",
        },
        "notes": "Protocolul 'Ventricle Check' de la WFPI înlocuiește cu succes scanările CT repetate, scutind copiii cu hidrocefalie de doze cumulative masive de radiații ionizante.",
        "sources": COMMON_SOURCES,
    },

    # 4. Tumor/Infection Brain Protocol
    {
        "slug": "irm-pediatric-tumori-infectii-cerebrale",
        "title": "RM Pediatric — Protocol Tumori & Infecții Cerebrale (Brain Tumor & Infection)",
        "category": "pediatrie",
        "modality": "irm",
        "author": "World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie",
        "last_updated": "2026-09-20",
        "clinical_indications": [
            "Suspiciune sau monitorizare de proces expansiv intracranian la copil (tumori de fosă posterioară, gliome, craniofaringiom)",
            "Infecții acute și subacute ale SNC: meningoencefalită, empiem subdural, abces cerebral",
            "Boli inflamatorii și demielinizante (ADEM, scleroză multiplă pediatrică)",
            "Suspiciune de diseminare leptomeningiană tumorală sau infecțioasă",
        ],
        "contraindications": [
            "Implanturi feromagnetice incompatibile RM",
            "Insuficiență renală acută sau eGFR < 30 mL/min/1.73m² (precauție la chelati de Gadoliniu)",
        ],
        "patient_prep": "Abord venos periferic montat înainte de intrarea în sala RM; repaus alimentar 2-4 ore dacă se folosește anestezie/sedare; verificarea funcției renale.",
        "coils_hardware": {
            "coil": "Antenă dedicată Head/Neck multicanal (16-32 canale)",
            "field_strength": "1.5 Tesla / 3.0 Tesla",
            "positioning": "Decubit dorsal, imobilizare simetrică a extremității cefalice",
        },
        "contrast": {
            "agent": "Chelat de Gadoliniu macrociclic hidrosolubil (ex: Gadobutrol, Gadoterat de meglumină)",
            "dose": "0.1 mmol/kg corp (0.1 ml/kg pentru 1.0 M sau 0.2 ml/kg pentru 0.5 M)",
            "flow_rate": "1.0 - 1.5 ml/s injectare manuală sau automată, urmată de spălare cu 10-15 ml ser fiziologic",
            "timing": "Achiziție secvențe post-contrast T1 la 2-3 minute post-injectare",
            "notes": "Risc de NSF minimizat prin utilizarea exclusivă a agenților macrociclici stabili.",
        },
        "sequences": [
            {
                "name": "Axial DWI (b=0, b=1000) + hartă ADC",
                "plane": "Axial",
                "tr_te": "TR 3500 ms / TE 70 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 220 mm / 192x192",
                "fat_sat": "FatSat (EPI)",
                "notes": "Restricție de difuzie în abcese, tumori hipercelulare (ex. meduloblastom) (1-2 min)",
            },
            {
                "name": "3D T1WI Izotrop Sagital Nativ (MPRAGE / BRAVO)",
                "plane": "Sagital 3D Izotrop",
                "tr_te": "TR 1900 ms / TE 2.5 ms / TI 900 ms",
                "slice_gap": "1.0 mm izotrop",
                "fov_matrix": "FOV 240 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Morfologie nativă de referință pre-contrast (5-7 min)",
            },
            {
                "name": "Axial T2WI TSE",
                "plane": "Axial",
                "tr_te": "TR 4000 ms / TE 100 ms",
                "slice_gap": "3.5 mm / gap 0.3 mm",
                "fov_matrix": "FOV 220 mm / 384x288",
                "fat_sat": "Nu",
                "notes": "Edem peritumoral, componență chistică/necrotică (3 min)",
            },
            {
                "name": "Axial SWI / T2* GRE",
                "plane": "Axial",
                "tr_te": "TR 600 ms / TE 20 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 220 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Hemoragie intratumorală, calcificări, neovascularizație (3-5 min)",
            },
            {
                "name": "3D T1WI Izotrop Sagital Post-Contrast (MPRAGE / BRAVO)",
                "plane": "Sagital 3D Izotrop",
                "tr_te": "TR 1900 ms / TE 2.5 ms / TI 900 ms",
                "slice_gap": "1.0 mm izotrop",
                "fov_matrix": "FOV 240 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Captare tumorală, noduli milimetrici, reformate MPR coronale și axiale (5-7 min)",
            },
            {
                "name": "Coronal FLAIR Post-Contrast",
                "plane": "Coronal",
                "tr_te": "TR 8500 ms / TE 100 ms / TI 2400 ms",
                "slice_gap": "3.5 mm / gap 0.3 mm",
                "fov_matrix": "FOV 220 mm / 256x224",
                "fat_sat": "Nu",
                "notes": "Sensibilitate extrem de ridicată pentru captare leptomeningiană tumorală sau meningită (3 min)",
            },
        ],
        "quality_criteria": [
            "Comparație riguroasă 3D T1 nativ vs. post-contrast în aceeași geometrie",
            "FLAIR post-contrast fără hipersemnal fals pozitiv de la debit LCR",
            "Acoperire completă de la vertex până la joncțiunea cranio-cervicală (C2-C3)",
        ],
        "safety_considerations": [
            "Monitorizare atentă la injectarea de contrast",
            "SAR corp întreg menținut în limite normale",
        ],
        "iris_reference": {
            "chapter": "Pediatrie - Sistem Nervos Central",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            "recommendation_grade": "Grad A",
        },
        "notes": "Protocol standardizat WFPI optimizat pentru evaluarea completă a patologiei oncologice și infecțioase cerebrale în 20-30 minute.",
        "sources": COMMON_SOURCES,
    },

    # 5. Tumor/Infection Spine Protocol
    {
        "slug": "irm-pediatric-tumori-infectii-coloana",
        "title": "RM Pediatric — Protocol Tumori & Infecții Coloană Vertebrală (Spine Tumor & Infection)",
        "category": "pediatrie",
        "modality": "irm",
        "author": "World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie",
        "last_updated": "2026-09-20",
        "clinical_indications": [
            "Suspiciune de diseminare tumorală secundară pe cale LCR ('drop metastasis' din meduloblastom, ependimom)",
            "Tumori primare intramedulare (astrocitom, ependimom) sau extramedulare (schwanom, neuroblastom)",
            "Spondilodiscită infantilă sau juvenilă",
            "Suspiciune de abces epidural spinal sau flegmon paravertebral",
            "Mielită transversă sau afecțiuni demielinizante ale măduvei",
        ],
        "contraindications": [
            "Dispozitive medicale implantabile nesigure RM",
            "Insuficiență renală acută severă",
        ],
        "patient_prep": "Copilul așezat confortabil în decubit dorsal; linie venoasă verificată prealabil.",
        "coils_hardware": {
            "coil": "Antenă spinală phased-array dedicată (Spine matrix)",
            "field_strength": "1.5 Tesla / 3.0 Tesla",
            "positioning": "Decubit dorsal, coloana aliniată pe linia mediană",
        },
        "contrast": {
            "agent": "Chelat de Gadoliniu macrociclic",
            "dose": "0.1 mmol/kg corp",
            "flow_rate": "1.0 - 1.5 ml/s urmat de ser fiziologic",
            "timing": "Achiziție secvențe T1 post-contrast la 2-3 minute",
            "notes": "Esențial pentru diferențierea flegmon vs. abces lichefiat și evidențierea 'drop metastases'.",
        },
        "sequences": [
            {
                "name": "Sagital T1WI TSE",
                "plane": "Sagital",
                "tr_te": "TR 450-600 ms / TE 8-12 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 250-300 mm / 320x224",
                "fat_sat": "Nu",
                "notes": "Anatomie corpi vertebrali, înlocuire grăsime medulară în infecții/infiltrare (3 min)",
            },
            {
                "name": "Sagital T2WI FS / STIR",
                "plane": "Sagital",
                "tr_te": "TR 3500 ms / TE 80-100 ms / TI 150 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 250-300 mm / 320x224",
                "fat_sat": "FatSat / STIR",
                "notes": "Edem osos vertebral, afectare discală, semnal lichidian epidural (2:30 min)",
            },
            {
                "name": "Sagital DWI (b=0, b=800)",
                "plane": "Sagital",
                "tr_te": "TR 3000 ms / TE 65 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 250-300 mm / 128x128",
                "fat_sat": "FatSat",
                "notes": "Restricție de difuzie în abcese epidurale și metastaze celulare (1 min)",
            },
            {
                "name": "Sagital T1WI FS Post-Contrast",
                "plane": "Sagital",
                "tr_te": "TR 500-650 ms / TE 10 ms",
                "slice_gap": "3.0 mm / gap 0.3 mm",
                "fov_matrix": "FOV 250-300 mm / 320x224",
                "fat_sat": "FatSat",
                "notes": "Evaluare captare măduvă osoasă, afectare meningiană și epidurală (5 min)",
            },
            {
                "name": "Axial T2WI TSE",
                "plane": "Axial (centrat pe leziune)",
                "tr_te": "TR 3500-4500 ms / TE 100 ms",
                "slice_gap": "3.5 mm / gap 0.3 mm",
                "fov_matrix": "FOV 180-200 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Compresie medulară, foramene de conjugare, extensie paravertebrală (4 min)",
            },
            {
                "name": "Axial T1WI FS Post-Contrast",
                "plane": "Axial (centrat pe leziune)",
                "tr_te": "TR 500-600 ms / TE 10 ms",
                "slice_gap": "3.5 mm / gap 0.3 mm",
                "fov_matrix": "FOV 180-200 mm / 256x256",
                "fat_sat": "FatSat",
                "notes": "Evaluare măduvă spinării, spații radiculare și delimitare capsulă abces (3:30 min)",
            },
        ],
        "quality_criteria": [
            "Timp total de scanare: aproximativ 20 minute",
            "Acoperire completă a segmentului de coloană vizat (cervico-toracal sau toraco-lombar)",
            "Supresie de grăsime uniformă pe secvențele sagitale STIR și T1 FS",
        ],
        "safety_considerations": [
            "Imobilizare confortabilă pentru prevenirea durerii la copiii cu patologie spinală acută",
            "Respectare limite SAR",
        ],
        "iris_reference": {
            "chapter": "Pediatrie - Coloană vertebrală",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            "recommendation_grade": "Grad A",
        },
        "notes": "Protocol standardizat WFPI pentru coloana vertebrală pediatrică (tumori și infecții), cu durată optimizată la 20 minute.",
        "sources": COMMON_SOURCES,
    },

    # 6. Short Abdomen Protocol (Free Breathing)
    {
        "slug": "irm-pediatric-abdomen-scurt-free-breathing",
        "title": "RM Pediatric — Protocol Abdomen Scurt / Respirație Liberă (Short Abdomen)",
        "category": "pediatrie",
        "modality": "irm",
        "author": "World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie",
        "last_updated": "2026-09-20",
        "clinical_indications": [
            "Sugari și copii mici incapabili de apnee voluntară",
            "Durere abdominală acută la copil când ecografia este neconcludentă (ex: apendicită atipică, diverticulită)",
            "Suspiciune de invaginație intestinală sau masă pelvină/abdominală palpabilă",
            "Screening abdominal rapid fără sedare și fără expunere la radiații ionizante",
        ],
        "contraindications": [
            "Implanturi feromagnetice incompatibile RM",
        ],
        "patient_prep": "Post alimentar ușor (2 ore pentru lichide clare la sugari); tehnici de liniștire fără sedare.",
        "coils_hardware": {
            "coil": "Antenă Phased-Array de corp (Body/Torso array)",
            "field_strength": "1.5 Tesla (preferat pentru mai puține artefacte de susceptibilitate) sau 3.0 Tesla",
            "positioning": "Decubit dorsal, antenă ușor fixată pe abdomen fără a jena excursiile respiratorii",
        },
        "contrast": {
            "agent": "Fără contrast (examinare nativă rapidă)",
            "dose": "N/A",
            "flow_rate": "N/A",
            "timing": "N/A",
            "notes": "Protocol exclusiv nativ conceput pentru durată minimă (8-10 minute).",
        },
        "sequences": [
            {
                "name": "Coronal T2WI Single-Shot (HASTE / SSFSE)",
                "plane": "Coronal",
                "tr_te": "TR 1000 ms / TE 80-90 ms",
                "slice_gap": "4.0 mm / gap 0 mm",
                "fov_matrix": "FOV 280-350 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Respirație liberă (Free-Breathing), imagine panoramică abdomen-pelvis (30–45 s)",
            },
            {
                "name": "Axial T2WI Single-Shot (HASTE / SSFSE)",
                "plane": "Axial",
                "tr_te": "TR 1000 ms / TE 80-90 ms",
                "slice_gap": "4.0 mm / gap 0 mm",
                "fov_matrix": "FOV 250-300 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Respirație liberă (FB), orientare anatomică transversală (30–45 s)",
            },
            {
                "name": "Axial T2WI SSFSE FS (cu supresie de grăsime)",
                "plane": "Axial",
                "tr_te": "TR 1500 ms / TE 80 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 250-300 mm / 256x224",
                "fat_sat": "FatSat",
                "notes": "Trigger respirator (Respiratory Trigger), edem perivisceral, apendice, limfonoduli (3–5 min)",
            },
            {
                "name": "Axial DWI (b=50, b=400, b=800) + ADC",
                "plane": "Axial",
                "tr_te": "TR 3000-4000 ms / TE 60 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 250-300 mm / 128x128",
                "fat_sat": "FatSat",
                "notes": "Respirație liberă cu medieri crescute (NEX variabil), detecție focare inflamatorii/tumori (3–4 min)",
            },
            {
                "name": "Axial T1WI In-Phase / Opposed-Phase",
                "plane": "Axial",
                "tr_te": "TR 120-150 ms / TE 2.2 ms & 4.4 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 250-300 mm / 256x192",
                "fat_sat": "Nu (Dual-Echo)",
                "notes": "Trigger respirator sau respirație liberă, evaluare grăsime intraparenchimatoasă și hemoragie (3–4 min)",
            },
        ],
        "quality_criteria": [
            "Timp total de scanare la aparat: 8–10 minute",
            "Complet realizabil în respirație liberă (Free-Breathing) la sugari și copii mici",
            "Vizualizare clară a tractului digestiv, a ficatului, splinei și rinichilor",
        ],
        "safety_considerations": [
            "Nu comprimă toracele/abdomenul copilului cu antena de corp (se folosesc distanțiere moi)",
            "Protecție acustică adecvată",
        ],
        "iris_reference": {
            "chapter": "Pediatrie - Aparat digestiv & Abdomen",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            "recommendation_grade": "Grad A",
        },
        "notes": "Protocol WFPI conceput pentru a detecta rapid patologia abdominală pediatrică fără sedare și în respirație liberă.",
        "sources": COMMON_SOURCES,
    },

    # 7. Long Abdomen Protocol
    {
        "slug": "irm-pediatric-abdomen-lung-extins",
        "title": "RM Pediatric — Protocol Abdomen Lung / Extins (Long Abdomen)",
        "category": "pediatrie",
        "modality": "irm",
        "author": "World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie",
        "last_updated": "2026-09-20",
        "clinical_indications": [
            "Caracterizare avansată mase abdominale solide (nefroblastom / tumoare Wilms, neuroblastom, hepatoblastom)",
            "Evaluare patologie pancreatică / biliară (pancreas divisum, chist de coledoc) la copil",
            "Boli inflamatorii intestinale pediatrice (boală Crohn) - protocol de enterografie RM extinsă",
            "Bilanț oncologic abdominal complet pre- și post-chimioterapie",
        ],
        "contraindications": [
            "Implanturi feromagnetice incompatibile RM",
            "Alergie documentată la chelati de Gadoliniu sau insuficiență renală severă fără epurare",
        ],
        "patient_prep": "Repaus alimentar 4 ore; la copii cooperanți se exersează comenzile scurte de apnee; dacă nu e posibilă apneea, se utilizează secvențe cu medieri crescute (5 NEX) în respirație liberă.",
        "coils_hardware": {
            "coil": "Antenă Phased-Array Body multicanal",
            "field_strength": "1.5 Tesla / 3.0 Tesla",
            "positioning": "Decubit dorsal, brațele ridicate deasupra capului dacă este confortabil",
        },
        "contrast": {
            "agent": "Chelat de Gadoliniu macrociclic hidrosolubil",
            "dose": "0.1 mmol/kg corp (sau 0.1-0.2 ml/kg în funcție de concentrație)",
            "flow_rate": "1.0 - 1.5 ml/s urmat de 15 ml ser fiziologic",
            "timing": "Faze dinamice: arterială (15-20 s), venoasă portală (50-60 s), tardivă (2-3 min)",
            "notes": "Secvențe dinamice 3D T1 cu supresie de grăsime.",
        },
        "sequences": [
            {
                "name": "Coronal T2WI Single-Shot (HASTE / SSFSE)",
                "plane": "Coronal",
                "tr_te": "TR 1000 ms / TE 80 ms",
                "slice_gap": "4.0 mm / gap 0 mm",
                "fov_matrix": "FOV 300-360 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Respirație liberă (FB), panoramă abdominală (30–45 s)",
            },
            {
                "name": "Axial T2WI Single-Shot (HASTE / SSFSE)",
                "plane": "Axial",
                "tr_te": "TR 1000 ms / TE 80 ms",
                "slice_gap": "4.0 mm / gap 0 mm",
                "fov_matrix": "FOV 280-320 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Respirație liberă (FB), morfologie organe parenchimatoase (30–45 s)",
            },
            {
                "name": "Coronal bSSFP (TrueFISP / FIESTA)",
                "plane": "Coronal",
                "tr_te": "TR 3.5 ms / TE 1.5 ms / FA 60°",
                "slice_gap": "3.5 mm / gap 0 mm",
                "fov_matrix": "FOV 300-340 mm / 256x256",
                "fat_sat": "Nu",
                "notes": "Trigger respirator (RT), contrast excelent sânge/țesut, anatomie vasculară (2 min)",
            },
            {
                "name": "Axial T2WI FSE FS (cu supresie de grăsime)",
                "plane": "Axial",
                "tr_te": "TR 3000-4500 ms / TE 85 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 280-320 mm / 320x256",
                "fat_sat": "FatSat",
                "notes": "Trigger respirator (RT), detectare edem, afectare chistică sau inflamatorie (3–5 min)",
            },
            {
                "name": "Axial T1WI In/Opposed Phase",
                "plane": "Axial",
                "tr_te": "TR 140 ms / TE 2.2 ms & 4.4 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 280-320 mm / 256x192",
                "fat_sat": "Nu (Dual-Echo)",
                "notes": "Apnee (BH) sau respirație liberă cu 5 NEX (2–6 min)",
            },
            {
                "name": "Axial DWI (b=50, b=400, b=800) + ADC",
                "plane": "Axial",
                "tr_te": "TR 3500 ms / TE 65 ms",
                "slice_gap": "4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 280-320 mm / 128x128",
                "fat_sat": "FatSat",
                "notes": "Efectuată înainte de contrast; evaluare celularitate tumorală (3–4 min)",
            },
            {
                "name": "Axial 3D T1WI FS Dinamic Pre- și Post-Contrast",
                "plane": "Axial 3D",
                "tr_te": "TR 3.5 ms / TE 1.4 ms / FA 12°",
                "slice_gap": "2.0-3.0 mm reconstruit la 1.5 mm",
                "fov_matrix": "FOV 280-320 mm / 256x224",
                "fat_sat": "FatSat (VIBE / LAVA)",
                "notes": "Faze dinamice arteriale, venoase și tardive în apnee sau respirație liberă cu medieri (6 min)",
            },
        ],
        "quality_criteria": [
            "Timp total de scanare: 15–20 minute",
            "Sincronizare excelentă a fazei arteriale pentru evaluarea pediculilor vasculari tumorali",
            "Rezoluție spațială adecvată pentru detectarea trombozei de venă cavă inferioară sau renală",
        ],
        "safety_considerations": [
            "Monitorizare funcție renală (eGFR)",
            "Menținere SAR în limitele modului normal",
        ],
        "iris_reference": {
            "chapter": "Pediatrie - Aparat digestiv & Abdomen",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            "recommendation_grade": "Grad A",
        },
        "notes": "Protocol avansat WFPI pentru caracterizarea completă a maselor abdominale și patologiei hepato-bilio-pancreatice pediatrice.",
        "sources": COMMON_SOURCES,
    },

    # 8. Osteomyelitis / MSK Infection Protocol
    {
        "slug": "irm-pediatric-osteomielita-infectii-msk",
        "title": "RM Pediatric — Protocol Osteomielită & Infecții Musculoscheletale (Osteomyelitis / MSK)",
        "category": "pediatrie",
        "modality": "irm",
        "author": "World Federation of Pediatric Imaging (WFPI) / Departamentul de Radiologie",
        "last_updated": "2026-09-20",
        "clinical_indications": [
            "Suspiciune de osteomielită acută hematogenă la copil (febră, durere osoasă localizată, refuzul sprijinului)",
            "Artrită septică (evaluare revărsat articular și afectare epifizară)",
            "Miozită, flegmon sau abces de părți moi profunde (ex: mușchiul psoas, obturator intern)",
            "Suspiciune de abces subperiostal care necesită drenaj chirurgical de urgență",
        ],
        "contraindications": [
            "Implanturi metalice feromagnetice nesigure RM",
            "Alergie la substanța de contrast pe bază de Gadoliniu",
        ],
        "patient_prep": "Imobilizare atentă a membrului afectat; atelare confortabilă pentru a reduce durerea provocată de mișcare.",
        "coils_hardware": {
            "coil": "Antenă dedicată extremității (genunchi, gleznă, umăr) sau antenă flexibilă de suprafață",
            "field_strength": "1.5 Tesla / 3.0 Tesla",
            "positioning": "Poziționare confortabilă a segmentului anatomic de interes în izocentru",
        },
        "contrast": {
            "agent": "Chelat de Gadoliniu macrociclic",
            "dose": "0.1 mmol/kg corp",
            "flow_rate": "1.0 - 1.5 ml/s urmat de 15 ml ser fiziologic",
            "timing": "Achiziție secvențe T1 FS post-contrast imediat și la 2-3 minute",
            "notes": "Contrastul este esențial pentru diferențierea flegmonului ne-necrozat de abcesul lichefiat cu lizereu periferic captant.",
        },
        "sequences": [
            {
                "name": "Coronal T1WI TSE",
                "plane": "Coronal",
                "tr_te": "TR 500-600 ms / TE 10 ms",
                "slice_gap": "3.0-4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 180-240 mm / 320x224",
                "fat_sat": "Nu",
                "notes": "Înlocuire grăsime medulară hematopoietică/osoasă (hiposemnal T1 patologic) (3 min)",
            },
            {
                "name": "Coronal STIR",
                "plane": "Coronal",
                "tr_te": "TR 3500-4500 ms / TE 45-60 ms / TI 150 ms",
                "slice_gap": "3.0-4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 180-240 mm / 256x256",
                "fat_sat": "STIR",
                "notes": "Sensibilitate maximă pentru edem osos inflamator, revărsat articular și edem muscular (3 min)",
            },
            {
                "name": "Axial T2WI FS",
                "plane": "Axial",
                "tr_te": "TR 3500-4500 ms / TE 75-90 ms",
                "slice_gap": "3.5-4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 160-220 mm / 256x256",
                "fat_sat": "FatSat",
                "notes": "Delimitare abcese subperiostale, traiecte fistuloase, colecții intramusculare (4–6 min)",
            },
            {
                "name": "Sagital T1WI TSE",
                "plane": "Sagital",
                "tr_te": "TR 500-600 ms / TE 10 ms",
                "slice_gap": "3.0-4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 180-240 mm / 320x224",
                "fat_sat": "Nu",
                "notes": "Confirmare anatomică în plan ortogonal a extensiei lezionale (3 min)",
            },
            {
                "name": "Sagital T1WI FS Post-Contrast",
                "plane": "Sagital",
                "tr_te": "TR 550-650 ms / TE 10 ms",
                "slice_gap": "3.0-4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 180-240 mm / 320x224",
                "fat_sat": "FatSat",
                "notes": "Captare măduvă osoasă, periost și sinovială (3 min)",
            },
            {
                "name": "Coronal T1WI FS Post-Contrast",
                "plane": "Coronal",
                "tr_te": "TR 550-650 ms / TE 10 ms",
                "slice_gap": "3.0-4.0 mm / gap 0.4 mm",
                "fov_matrix": "FOV 180-240 mm / 320x224",
                "fat_sat": "FatSat",
                "notes": "Evaluare colecții purulente (centru necrotic non-captant cu lizereu periferic) (3 min)",
            },
        ],
        "quality_criteria": [
            "Timp total de scanare: 10–15 min nativ; 20–25 min cu contrast",
            "Supresie de grăsime uniformă și eficientă pe secvențele STIR și T1 FS",
            "Includerea completă a focarului osos și a compartimentelor musculare adiacente",
        ],
        "safety_considerations": [
            "Poziționare blândă pentru a nu agrava durerea membrului inflamat",
            "Doza de contrast strict adaptată greutății corporale (0.1 mmol/kg)",
        ],
        "iris_reference": {
            "chapter": "Pediatrie - Aparat locomotor & Articulații",
            "radiation_dose": "Clasa 0 (Fără Iradiere / Câmp Magnetic Non-Ionant)",
            "recommendation_grade": "Grad A",
        },
        "notes": "Protocol standardizat WFPI pentru diagnosticul precoce și precis al infecțiilor musculoscheletale la copil, prevenind sechelele de creștere osoasă.",
        "sources": COMMON_SOURCES,
    },
]


def generate_all():
    print(f"Generare {len(PROTOCOLS)} protocoale IRM pediatrice WFPI în: {TARGET_DIR}")

    for proto in PROTOCOLS:
        doc_str = render_irm_document(proto)
        file_path = TARGET_DIR / f"{proto['slug']}.md"
        file_path.write_text(doc_str, encoding="utf-8")
        print(f"  ✔ Creat: {file_path.name}")

    # Creează index.md pentru categoria docs/irm/pediatrie/
    index_content = """# Protocoale IRM Pediatrică (WFPI)

Ghid clinic și tehnic de protocoale de **Rezonanță Magnetică (IRM) Pediatrică**, standardizate la nivel internațional de către **World Federation of Pediatric Imaging (WFPI)** și comitetul condus de Dr. Michael Gee (*Pediatric Radiology*, 2024).

!!! info "Standarde Internaționale WFPI"
    Aceste protocoale au fost optimizate pentru a:
    
    1. **Minimiza sau elimina necesitatea sedării și a anesteziei generale** la copiii mici prin secvențe ultra-rapide și respirație liberă (*Free-Breathing*).
    2. **Înlocui tomografia computerizată (CT)** în monitorizarea hidrocefaliei și a traumatismelor, eliminând complet expunerea la radiații ionizante.
    3. **Standardiza achizițiile la nivel global**, fiind adaptate atât pentru aparate 1.5 Tesla, cât și 3.0 Tesla ale producătorilor majori (GE, Philips, Siemens).

---

## Catalog Protocoale IRM Pediatrice

<div class="grid cards" markdown>

-   __🧠 Neuroradiologie Pediatrică__

    ---

    - [RM Cerebral Rapid (Rapid Brain — ~10 min)](irm-pediatric-rapid-brain.md)
    - [RM Convulsii & Epilepsie (Seizure Brain)](irm-pediatric-epilepsie-convulsii.md)
    - [RM Hidrocefalie & Control Șunt / Ventriculi (3-5 min)](irm-pediatric-hidrocefalie-control-ventriculi.md)
    - [RM Tumori & Infecții Cerebrale (20-30 min)](irm-pediatric-tumori-infectii-cerebrale.md)
    - [RM Tumori & Infecții Coloană Vertebrală (20 min)](irm-pediatric-tumori-infectii-coloana.md)

-   __🫁 Abdomen & Musculoscheletal Pediatric__

    ---

    - [RM Abdomen Scurt / Respirație Liberă (Short Abdomen — 8-10 min)](irm-pediatric-abdomen-scurt-free-breathing.md)
    - [RM Abdomen Lung / Extins (Long Abdomen — 15-20 min)](irm-pediatric-abdomen-lung-extins.md)
    - [RM Osteomielită & Infecții Musculoscheletale (MSK)](irm-pediatric-osteomielita-infectii-msk.md)

</div>

---

### Referințe & Colaborare Internațională
- **Portal Oficial WFPI:** [wfpiweb.org/Resources/Modalities/MRIProtocols.aspx](https://wfpiweb.org/Resources/Modalities/MRIProtocols.aspx){ target="_blank" rel="noopener" }
- **Articol Standard:** *International standardization of pediatric magnetic resonance imaging protocols: creation of the World Federation of Pediatric Imaging MR Protocols Committee* (Ferraciolli SF, Boechat MI, Gee MS et al. — *Pediatric Radiology*, 2024. [DOI: 10.1007/s00247-024-06041-0](https://doi.org/10.1007/s00247-024-06041-0){ target="_blank" rel="noopener" })
"""
    (TARGET_DIR / "index.md").write_text(index_content, encoding="utf-8")
    print("  ✔ Creat: docs/irm/pediatrie/index.md")

    # Creează .pages pentru docs/irm/pediatrie/
    pages_content = """title: Imagistică Pediatrică (WFPI)
nav:
  - index.md
  - rm-cerebral-rapid: irm-pediatric-rapid-brain.md
  - rm-epilepsie: irm-pediatric-epilepsie-convulsii.md
  - rm-hidrocefalie: irm-pediatric-hidrocefalie-control-ventriculi.md
  - rm-tumori-creier: irm-pediatric-tumori-infectii-cerebrale.md
  - rm-coloana: irm-pediatric-tumori-infectii-coloana.md
  - rm-abdomen-scurt: irm-pediatric-abdomen-scurt-free-breathing.md
  - rm-abdomen-lung: irm-pediatric-abdomen-lung-extins.md
  - rm-osteomielita: irm-pediatric-osteomielita-infectii-msk.md
"""
    (TARGET_DIR / ".pages").write_text(pages_content, encoding="utf-8")
    print("  ✔ Creat: docs/irm/pediatrie/.pages")


if __name__ == "__main__":
    generate_all()
