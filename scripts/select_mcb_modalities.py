"""Explicit scope and Romanian catalog titles for non-MRI MCB imports."""
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data/mcb-modalities'
CT = {
 'Body': ['Abdomen și pelvis de rutină', 'Abdomen de rutină', 'Pelvis de rutină', 'Torace, abdomen și pelvis de rutină', 'Torace și abdomen de rutină', 'Enterografie monofazică', 'Enterografie multifazică', 'Ischemie mezenterică', 'Hemoragie acută', 'Ficat', 'Ficat înainte de SIRT', 'Pancreas', 'Pancreatită', 'Suprarenale', 'Rinichi', 'Litiază renală', 'Urografie de rutină', 'Urografie split-bolus', 'Cistografie'],
 'Neuro': ['Craniu de rutină', 'Craniu preoperator', 'Angio-CT cerebral', 'Angio-CT cervical', 'Angio-CT cerebral și cervical', 'Perfuzie cerebrală', 'Venografie cerebrală', 'Masiv facial și orbite', 'Sinusuri', 'Conducte auditive interne și oase temporale', 'Părți moi cervicale', 'Paratiroide', 'Coloană cervicală', 'Coloană toracică', 'Coloană lombară', 'Coloană lombară preoperator', 'Mielografie', 'Cisternografie'],
 'MSK': ['Umăr', 'Claviculă', 'Cot', 'Pumn', 'Mână', 'Bazin osos', 'Șold', 'Genunchi', 'Gleznă și retropicior', 'Antepicior', 'Oase lungi', 'Măsurarea lungimii membrelor', 'Umăr Catalyst', 'Umăr Arthrex', 'Umăr Stryker', 'Șold Mako', 'Genunchi Mako', 'Genunchi Zimmer', 'Genunchi Restor3D Conformis', 'Genunchi DePuy', 'Gleznă Prophecy', 'Gleznă MAVEN'],
 'Cardiac': ['Scor de calciu coronarian', 'Artere coronare', 'Planificare TAVR', 'Planificare TMVR (Encircle)', 'Planificare Watchman', 'Planificare Converge', 'Planificare aMaze / Lariat'],
 'Vascular': ['Aortă completă (torace, abdomen și pelvis)', 'Aortă toracică', 'Aortă abdominală', 'Embolie pulmonară', 'Venă cavă superioară', 'Artere renale', 'Venă cavă inferioară', 'Angiografie runoff', 'Angio-CT membre inferioare', 'Venografie membre inferioare', 'Angio-CT membre superioare', 'Reconstrucție mamară DIEP'],
 'Peds': ['Craniu pediatric', 'Masiv facial și orbite la copil', 'Sinusuri la copil', 'Regiune cervicală la copil', 'Torace pediatric', 'Abdomen și pelvis la copil', 'Torace, abdomen și pelvis la copil', 'Coloană cervicală la copil', 'Coloană toracică la copil', 'Coloană lombară la copil', 'Bazin osos la copil', 'Extremități la copil'],
}
US = dict(zip([
 'Thyroid','Post Thyroidectomy','Abdomen Complete','Abdomen Limited (RUQ)','Abdomen Limited (GB Only)','Abdomen Limited (Ascites Check)','Renal Complete','Urinary Bladder','Histotripsy Pre Scan','Scrotum Testes','Penis','Female Pelvis (Non OB)','1st Trimester OB','OB Complete','OB Limited','Biophysical Profile','Neonatal Head','Arm Arteries','Arm Segmentals','Arm DVT','Arm Vein Mapping','Radial Artery Map','Leg Arteries','Leg Segmentals (Full)','Leg Sementals (Limited)','Leg DVT','Leg Vein Mapping','Groin Pseudoaneurysm','Carotid Arteries','Abdominal Aorta','Abdomen Duplex','Liver Transplant','TIPS','Mesenteric Artery','Renal Artery','Renal Transplant','Hemodialysis Access','Breast & Axilla'],[
 'Tiroidă','După tiroidectomie','Abdomen complet','Abdomen țintit: cadran superior drept','Abdomen țintit: vezică biliară','Verificarea ascitei','Rinichi: examinare completă','Vezică urinară','Evaluare înainte de histotripsie','Scrot și testicule','Penis','Pelvis feminin neobstetrical','Sarcină în trimestrul I','Examinare obstetricală completă','Examinare obstetricală limitată','Profil biofizic fetal','Creier neonatal','Artere ale membrului superior','Presiuni segmentare: membru superior','Tromboză venoasă profundă: membru superior','Cartografiere venoasă: membru superior','Cartografiere arteră radială','Artere ale membrului inferior','Presiuni segmentare complete: membru inferior','Presiuni segmentare limitate: membru inferior','Tromboză venoasă profundă: membru inferior','Cartografiere venoasă: membru inferior','Pseudoanevrism inghinal','Artere carotide','Aortă abdominală','Duplex abdominal','Transplant hepatic','Șunt TIPS','Artere mezenterice','Artere renale','Transplant renal','Acces vascular pentru hemodializă','Sân și axilă']))
NM = dict(zip([
 'Lung Ventilation Xenon','Lung Ventilation DTPA','Lung Perfusion','MUGA Ventriculography','HIDA','Liver Spleen','GI Bleeding','Gastric Emptying','Meckel','Renal Scan','Renal DMSA','Renal Vascular HTN','Bone Scan Whole Body','Bone Scan Limited','Bone Scan Three Phase','Bone Scan SPECT','WBC Marrow Combo','PET NaF','Thyroid Imaging Uptake','Thyroid I131','Parathyroid','Brain Death','Cisternogram CSF Leak','PET FDG Brain','Dacrocystogram','WBC Ceretec','WBC Indium','Gallium','PET FDG Body','Octreotide','MIBG','Lympho Breast','Lympho Skin','Lympho Gynecologic','Lympho Extremity','Lympho Procedure'],[
 'Ventilație pulmonară cu xenon','Ventilație pulmonară cu DTPA','Perfuzie pulmonară','Ventriculografie MUGA','Scintigrafie hepatobiliară HIDA','Scintigrafie ficat și splină','Sângerare digestivă','Evacuare gastrică','Diverticul Meckel','Scintigrafie renală','Scintigrafie renală DMSA','Hipertensiune renovasculară','Scintigrafie osoasă whole-body','Scintigrafie osoasă limitată','Scintigrafie osoasă trifazică','Scintigrafie osoasă SPECT','Leucocite marcate și măduvă osoasă','PET cu NaF','Tiroidă: imagistică și captare','Tiroidă cu iod-131','Paratiroide','Evaluarea morții cerebrale','Cisternografie și fistulă LCR','PET cerebral cu FDG','Dacrioscintigrafie','Leucocite marcate cu Ceretec','Leucocite marcate cu indiu','Scintigrafie cu galiu','PET corporal cu FDG','Scintigrafie cu octreotid','Scintigrafie MIBG','Limfoscintigrafie mamară','Limfoscintigrafie cutanată','Limfoscintigrafie ginecologică','Limfoscintigrafie extremități','Procedură de limfoscintigrafie']))

def classify(doc):
    path = unquote(urlsplit(doc['url']).path)
    stem = Path(path).stem
    kind, category, title, modality = 'protocol', None, None, None
    match = re.search(r'/CT/Protocols/(Body|Neuro|MSK|Chest|Cardiac|Vascular|Peds|Default)/', path)
    if match:
        group = match[1]
        modality = 'ct'
        category = {'Body':'abdomen','Neuro':'neuro','MSK':'msk','Chest':'chest','Cardiac':'cardiac','Vascular':'vascular','Peds':'pediatrie','Default':'aparate'}[group]
        if group == 'Default': title, kind = 'Parametri aparat: ' + stem, 'manual_aparat'
        elif group == 'Chest': title = {'1 Routine':'Torace de rutină','2 Low-Dose':'Torace cu doză redusă','3 Screening':'Screening cancer pulmonar','4 HRCT Routine':'HRCT de rutină','5 HRCT Full':'HRCT complet','11 Trachea':'Trahee','12 Esophagram':'Esofagografie'}.get(stem, 'Torace: ' + re.sub(r'^\d+ ', '', stem))
        else: title = CT[group][int(stem.split()[0])-1]
    elif '/US/Protocols/' in path:
        modality, title = 'eco', US[stem]
        if stem in ['Thyroid','Post Thyroidectomy']: category = 'parti-moi-endocrin'
        elif stem == 'Neonatal Head': category = 'pediatrie'
        elif stem == 'Breast & Axilla': category = 'san'
        elif stem.startswith(('Arm','Leg','Radial','Groin','Carotid','Abdominal Aorta','Abdomen Duplex','Liver Transplant','TIPS','Mesenteric','Renal Artery','Renal Transplant','Hemodialysis')): category = 'vascular-doppler'
        else: category = 'abdomen-pelvis'
    elif '/US/Tech Worksheets/' in path:
        modality, category, kind, title = 'eco','fise','fisa_lucru','Fișă de lucru: ' + US.get(stem, stem)
    elif re.search(r'/Xray/(Adult|Peds) Protocols/', path):
        modality = 'rx'
        region = re.sub(r'^\d+ (Adult|Peds) ', '', stem)
        category = 'pediatrie' if '/Peds ' in path else {'General':'neclasificat','Chest':'torace','Abdomen':'abdomen','Arm':'membru-superior','Bony Pelvis':'abdomen','Leg':'membru-inferior','Spine':'coloana','Head':'craniu-saf','Miscellaneous':'neclasificat'}[region]
        title = ('Copil: ' if '/Peds ' in path else 'Adult: ') + {'General':'reguli generale','Chest':'torace și grilaj costal','Abdomen':'abdomen','Arm':'membru superior','Bony Pelvis':'bazin osos','Leg':'membru inferior','Spine':'coloană vertebrală','Head':'craniu, față și gât','Miscellaneous':'examinări diverse'}[region]
        kind = 'colectie_protocoale'
    elif '/Xray/GI & Other Exams/' in path:
        modality, category = 'fluoro', 'urinar' if stem == 'HSG' else 'digestiv'
        title = {'HSG':'Histerosalpingografie (HSG)','Inpatient GI Fluoro Protocols':'Fluoroscopie digestivă la pacienți internați','Outpatient GI Prep':'Pregătire pentru examinări digestive în ambulatoriu'}[stem]
    elif '/Nucs/Protocols/' in path:
        modality, title = 'mn', NM[stem]
        if stem.startswith('Lung'): category = 'pulmonar'
        elif stem.startswith('MUGA'): category = 'cardiac'
        elif stem in ['HIDA','Liver Spleen','GI Bleeding','Gastric Emptying','Meckel']: category = 'digestiv'
        elif stem.startswith('Renal'): category = 'urinar'
        elif stem.startswith('Bone') or stem == 'PET NaF': category = 'osos'
        elif stem.startswith('Thyroid') or stem == 'Parathyroid': category = 'endocrin'
        elif stem in ['Brain Death','Cisternogram CSF Leak','PET FDG Brain','Dacrocystogram']: category = 'neuro'
        elif stem.startswith('WBC') or stem == 'Gallium': category = 'infectie'
        else: category = 'oncologie'
    elif path.endswith('/DEXA Guidelines.pdf') or path.endswith('/FRAX Guidelines.pdf'):
        modality, category, kind, title = 'rx', 'dexa', 'ghid', 'Densitometrie DEXA' if stem == 'DEXA Guidelines' else 'Evaluarea riscului de fractură FRAX'
    elif '/Breast/Policies/' in path and 'BREAST03' not in path:
        modality, category, kind = 'rx','mamografie','politica_procedurala'
        title = {'BREAST01':'Mamografie: politici de examinare','BREAST02':'Poziționare adecvată în screeningul mamar','BREAST04':'Imagistică mamară: pacienți internați și urgențe','BREAST05':'Proceduri mamare'}[stem.split()[0]]
    elif '/IR/Miscellaneous/' in path and stem in ['2025 Med & Lab Guidelines','2018 Antibiotic Prophylaxis Guidelines','Cryo Probes','Histotripsy Procedure Plan','Bonopty How To','Fluid Specimen Handling','Local Anesthetics']:
        modality, category, kind = 'ir','proceduri','ghid_procedural'
        title = {'2025 Med & Lab Guidelines':'Medicație și analize înaintea procedurilor (2025)','2018 Antibiotic Prophylaxis Guidelines':'Profilaxie antibiotică în intervențional (SIR 2018)','Cryo Probes':'Sonde pentru crioablație','Histotripsy Procedure Plan':'Plan procedural pentru histotripsie','Bonopty How To':'Utilizarea sistemului de biopsie Bonopty','Fluid Specimen Handling':'Manipularea probelor de lichid','Local Anesthetics':'Limite pentru anestezice locale'}[stem]
    if modality:
        return dict(doc, modality=modality, category=category, kind=kind, title=title, source_title=stem)
    return None

def select():
    inventory = json.loads((DATA / 'inventory.json').read_text(encoding='utf-8'))
    selected = [r for doc in inventory['documents'] if (r := classify(doc))]
    (DATA / 'selection.json').write_text(json.dumps(selected, ensure_ascii=False, indent=2), encoding='utf-8')
    from collections import Counter
    print(dict(Counter((r['modality'],r['kind']) for r in selected)))

if __name__ == '__main__': select()
