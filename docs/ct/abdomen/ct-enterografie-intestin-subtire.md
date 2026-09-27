---
author: MIA Radiology / Imagistică Abdominală
category: abdomen
clinical_indications:
- Boală Crohn cunoscută sau suspectată (evaluarea activității inflamatorii, extinderii și complicațiilor)
- Diferențierea stenozelor inflamatorii active de stenozele fibrotice cicatriciale
- Decelarea fistulelor enterice (entero-enterice, entero-vezicale, entero-cutanate) și a abceselor intraabdominale
- Hemoragie digestivă obscură fără leziune identificată la endoscopia digestivă superioară și colonoscopie
- Suspiciune de neoplazie a intestinului subțire (carcinoid, GIST, adenocarcinom, limfom)
- Evaluarea polipozei intestinale și a sindroamelor de malabsorbție
contrast:
  agent: 'Substanță de contrast iodată non-ionică (300 - 350 mg I/mL) IV + Contrast enteric oral neutru'
  flow_rate: 4.0 mL/s
  roi: Fără ROI de tracking; întârziere fixă
  timing: Fază enterică capilară mucosală la 60 secunde întârziere de la debutul injectării
  trigger: 60 secunde delay fix
  volume: 80 - 100 mL contrast IV; 1000 - 1500 mL contrast oral neutru (apă cu manitol / sorbitol sau Volumen)
iris_reference:
  chapter: Aparat Digestiv & Abdomen
  radiation_dose: Clasa 3 (Medie 3 - 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-27'
modality: ct
notes:
  additional_recons: Reconstrucții coronale și sagitale multiplanare MPR 3x3 mm în fereastră de părți moi.
  nursing: Pacientul începe ingestia contrastului oral cu 45-60 minute înainte de scanare. Plasare canulă IV 18G în plica cotului pentru debitul de 4 mL/s.
  rad: >-
    Analiză meticuloasă a peretelui intestinal destins: grosime parietală (> 3 mm patologic), hiperemie mucosală în faza enterică, stratificare parietală (&laquo;target sign&raquo; / &laquo;halo sign&raquo; în faza activă), edem submucos, angorjare a vaselor drepte (&laquo;comb sign&raquo;), fistule și limfadenopatii mezenterice.
  tech: Distensia luminală adecvată este cheia calității examinării. Pacientul bea 1350 mL soluție neutră împărțită în 3-4 doze la intervale de 15 minute. Scanare de la diafragm până sub trohanterii mici la exact 60 de secunde post-injectare IV.
  tips: Fără pregătire purgativă a colonului (fără clismă sau fosfat). NPO 4 ore înainte de sosire. Contrastul neutru asigură atenuare similară apei în lumen, oferind cel mai bun contrast fațǎ de peretele intens iodofil.
npo: 4 ore repaus alimentar pentru solide
position: Decubit dorsal cu brațele ridicate deasupra capului
premedication: Fără antispastice de rutină
protocol_type: abdomen
recons:
- acquisition: Fază Enterică Mucoasă (60s Delay)
  fov: Diafragm până sub trohanterii mici
  kernel: Standard Soft Tissue
  notes: Serie axială volumetrică pentru ansele destinse și mezenter
  plane: Axial
  thickness_increment: 2.5 mm / 2.5 mm
- acquisition: Fază Enterică Mucoasă
  fov: Abdomen și pelvis
  kernel: Standard Soft Tissue
  notes: Reconstrucție coronală MPR 3x3 mm (esențială pentru ansele jejuno-ileale)
  plane: Coronal
  thickness_increment: 3 mm / 3 mm
- acquisition: Fază Enterică Mucoasă
  fov: Abdomen și pelvis
  kernel: Standard Soft Tissue
  notes: Reconstrucție sagitală MPR 3x3 mm
  plane: Sagital
  thickness_increment: 3 mm / 3 mm
slug: ct-enterografie-intestin-subtire
sources:
- institution: Medical Imaging Associates (MIA)
  relationship: Adaptare conform protocolului instituțional oficial
  title: 'MIA Modality Wiki: CT Enterography'
  url: https://miaradmodalitywiki.powerappsportals.com/CT-Enterography
  version: '2025'
synonyms:
- Entero-CT
- CT Enterografie Boala Crohn
- Enteroclysis CT
- CT Evaluare Intestin Subtire
title: Protocol CT Enterografie (Evaluare Intestin Subțire & Boală Crohn)
---

# Protocol CT Enterografie (Evaluare Intestin Subțire & Boală Crohn)

Protocol de tomografie computerizată cu distensie enterică neutră de volum mare și achiziție în fază capilară mucosală, dezvoltat de **Medical Imaging Associates (MIA Radiology)** pentru caracterizarea inflamației parietale intestinale și a complicațiilor din boala Crohn.

<div class="iris-official-banner" style="margin-bottom: 24px; background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%); color: #ffffff; padding: 20px 24px; border-radius: 12px; border: 1px solid rgba(147, 197, 253, 0.3);">
  <div class="iris-official-badge" style="background: rgba(147, 197, 253, 0.2); color: #bfdbfe; padding: 4px 12px; border-radius: 999px; display: inline-block; font-weight: 700; font-size: 0.82rem; margin-bottom: 8px;">
    🔬 IMAGISTICĂ ENTERICĂ &bull; DISTENSIE NEUTRĂ
  </div>
  <p class="iris-official-desc" style="margin-bottom: 12px !important; color: #eff6ff; font-size: 0.95rem; line-height: 1.55;">
    Spre deosebire de scanarea CT abdominală clasică cu contrast oral iodat pozitiv, <strong>CT Enterografia</strong> folosește agenți orali hipodenși izo/hiperosmolari (Volumen sau soluție de manitol) care nu maschează mucoasa ci o destind optim, permițând vizualizarea prizei intense de contrast în faza enterică la <strong>60 de secunde</strong>.
  </p>
  <a href="https://miaradmodalitywiki.powerappsportals.com/CT-Enterography" target="_blank" rel="noopener" style="font-weight: 600; color: #93c5fd; text-decoration: none;">
    Consultați specificațiile originale MIA CT Enterography ➔
  </a>
</div>

---

## 1. Justificare Clinică & Recomandare IRIS

- **Indicație:** Evaluarea extensiei, activității inflamatorii, stenozelor și complicațiilor fistuloase sau abcedate în boala Crohn; hemoragie digestivă de cauză neelucidată.
- **Grad de Recomandare:** **Grad A** (metodă imagistică de primă linie în ghidurile ECCO și ESGAR alături de Entero-IRM).
- **Clasă de Doză:** **Clasa 3** (Doză medie, 3 - 10 mSv).

---

## 2. Pregătirea Pacientului & Protocolul Ingestiei Orale

Calitatea examinării depinde în proporție de peste 80% de complianța la protocolul de distensie orală:

1. **Repaus Alimentar (NPO):** 4 ore înainte de prezentare; fără purgative sau clisme colonice agresive;
2. **Volum Total Administrat:** **1000 – 1500 mL** soluție de contrast enteric hipodens (Volumen sau apă cu 2.5-3% manitol);
3. **Calendarul Ingestiei Fracționate:**
   - **Ora T - 45 minute:** Pacientul bea prima sticlă/doză (450 mL);
   - **Ora T - 30 minute:** Pacientul bea a doua doză (450 mL);
   - **Ora T - 15 minute:** Pacientul bea a treia doză (450 mL);
   - **Ora T - 0 minute:** Așezarea pe masa de scanare și inițierea protocolului IV.

---

## 3. Protocolul Injectorului IV & Faza Enterică (60s Delay)

| Parametru | Valoare |
|:----------|:--------|
| **Acces Intravenos** | Cateter **18G** în vena antecubitală |
| **Agent de Contrast IV** | Non-ionic 300 – 350 mg I/mL (Omnipaque 300, Isovue 300/370) |
| **Volum Injectat** | **80 – 100 mL** |
| **Debit de Injectare** | **4.0 mL/s** |
| **Saline Flush** | 40 mL ser fiziologic la 4.0 mL/s |
| **Temporizare Scanare** | **60 secunde întârziere fixă** de la debutul injectării (faza enterică mucoasă capilară) |
| **Acoperire Anatomică** | Imediat deasupra cupolelor diafragmatice până sub trohanterii mici |

---

## 4. Reconstrucții & Transmisie PACS

- **Serie Axială:** 2.5 mm grosime / 2.5 mm increment, fereastră standard de părți moi (W:400, L:40);
- **Serie Coronală MPR:** 3.0 mm x 3.0 mm MPR (esențială pentru urmărirea anselor jejunale și a ileonului terminal în plan anatomic extins);
- **Serie Sagitală MPR:** 3.0 mm x 3.0 mm MPR pentru pelvis, rect și perineu (aprecierea fistulelor perianale și recto-vaginale).

---

## 5. Criterii de Evaluare a Activității în Boala Crohn

| Semn Imagistic CT | Interpretare Clinică & Patologică |
|:------------------|:----------------------------------|
| **Îngroșare Parietală > 3 mm** | Criteriu de bază pentru afectare inflamatorie a ansei |
| **Hiperemie Mucoasă Intensă** | Reflectă activitate inflamatorie acută a mucoasei |
| **Semnul Țintei (&laquo;Target Sign&raquo;)** | Stratificare parietală cu mucoasă și seroasă hiperdense separate de edem submucos hipodens — **inflamație activă reversibilă** |
| **Semnul Pieptenului (&laquo;Comb Sign&raquo;)** | Dilatația și hipervascularizația vaselor drepte mezenterice perpendiculare pe ansa afectată |
| **Proliferare Fibrogrăsoasă (&laquo;Fat Creeping&raquo;)** | Hipertrofia grăsimii mezenterice perienterice cu efect de masă asupra anselor vecine |
| **Stenoză fără Edem Submucos** | Stenoză fibrotică cicatricială cronică (adesea necesită dilatație endoscopică sau stricturoplastie chirurgicală) |
| **Tract Fistulos / Abces Mezenteric** | Complicație transmurală penetrantă — contraindică terapia biologică până la rezolvarea colecției |
