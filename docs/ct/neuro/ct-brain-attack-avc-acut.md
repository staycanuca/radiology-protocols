---
author: MIA Radiology / Clinical Quality Team
category: neuro
clinical_indications:
- Accident vascular cerebral ischemic acut (Cod AVC / Brain Attack)
- Deficit neurologic focal instalat brusc (< 24 ore de la debut)
- Suspiciune de ocluzie arterială de vas mare (LVO - Large Vessel Occlusion)
- Evaluare de urgență pentru tromboliză intravenoasă și/sau trombectomie mecanică endovasculară
contrast:
  agent: Substanță de contrast iodată non-ionică (350 - 370 mg I/mL)
  flow_rate: 4.0 - 5.0 mL/s
  roi: Arc aortic sau artera carotidă comună (SmartPrep / Bolus tracking)
  timing: CT Nativ urmat de Angio-CT de la crosa aortei la vertex cu export VizAI
  trigger: 100 - 120 HU prag automat
  volume: 100 mL contrast + 40 mL bolus ser fiziologic (Saline Chaser)
iris_reference:
  chapter: Cap, Gât & Coloană vertebrală
  radiation_dose: Clasa 2 (Mică 1 - 3 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-27'
modality: ct
notes:
  additional_recons: Reconstrucții coronale MIP 10 mm și 2 mm de la arcul aortic la baza craniului; sagital MIP 2 mm; serie axială subțire 0.6 - 1.0 mm transmisă automat către platforma de inteligență artificială VizAI.
  nursing: Acces venos 18G în plica cotului pentru a tolera debitul de 4-5 mL/s. Monitorizare semne vitale și transport direct CT fără staționare în CPU/UPU.
  rad: >-
    Evaluare secvențială ultra-rapidă: 1) Nativ — excluderea hemoragiei intracraniene (HIC, HSA), calcul scor ASPECTS (0-10); 2) Angio-CT — decelarea ocluziei de vas mare (segment M1/M2 ACM, ACI terminală, arteră bazilară), aprecierea circulației colaterale piale.
  tech: Protocol combinat STAT &laquo;One-Stop Shop&raquo;. Se poate include seria fără contrast în aceeași achiziție angiografică dacă scanerul o permite. O serie axială subțire de 1 mm este trimisă către PACS, iar o serie dedicată către sistemul VizAI.
  tips: >-
    'Time is Brain'. Minimizarea timpului ușă-la-scanare (Door-to-CT < 20 minute) și Door-to-Needle (< 45 minute).
npo: Fără restricție alimentară prealabilă — urgență medicală majoră
position: Decubit dorsal, cap centrat în tetieră, brațele pe lângă corp
premedication: Fără premedicație
protocol_type: neuroradiology
recons:
- acquisition: CT Nativ Craniu (Head WO)
  fov: Ajustat la anatomia craniului
  kernel: Vendor specific Standard Brain / Cerebrum
  notes: Axial 4 mm cerebrum pentru parenchim + Axial 2 mm kernel os (osteo)
  plane: Axial
  thickness_increment: 4 mm / 4 mm (axial 2 mm os)
- acquisition: CT Nativ Craniu
  fov: Craniu
  kernel: Vendor specific Standard Brain
  notes: Reconstrucție multiplanară coronară
  plane: Coronal
  thickness_increment: 2 mm / 2 mm
- acquisition: CT Nativ Craniu
  fov: Craniu
  kernel: Vendor specific Standard Brain
  notes: Reconstrucție multiplanară sagitală
  plane: Sagital
  thickness_increment: 2 mm / 2 mm
- acquisition: Angio-CT Arcul Aortic - Vertex (CTA H+N)
  fov: Arc aortic până la vertex
  kernel: Vendor appropriate angiography kernel
  notes: Serie axială de înaltă rezoluție pentru lumene vasculare
  plane: Axial
  thickness_increment: 1 mm / 0.8 mm
- acquisition: Angio-CT Arcul Aortic - Vertex
  fov: Arc aortic la baza craniului
  kernel: Angiography
  notes: Reconstrucție Coronal MIP 10 mm pentru analiza crosei și trunchiurilor supra-aortice
  plane: Coronal
  thickness_increment: 10 mm MIP
- acquisition: Angio-CT Arcul Aortic - Vertex
  fov: Arc aortic la baza craniului
  kernel: Angiography
  notes: Reconstrucție Coronal MIP 2 mm și Sagital MIP 2 mm
  plane: Coronal / Sagital
  thickness_increment: 2 mm MIP
- acquisition: Export dedicat Inteligență Artificială (VizAI)
  fov: Arc aortic la vertex
  kernel: Angiography
  notes: Transmis către serverul de analiză automată a ocluziilor de vas mare (LVO)
  plane: Axial
  thickness_increment: 0.6 - 1.0 mm
slug: ct-brain-attack-avc-acut
sources:
- institution: Medical Imaging Associates (MIA)
  relationship: Adaptare conform protocolului instituțional oficial
  title: 'MIA Modality Wiki: CT BRAIN ATTACK (CT HEAD WO+CTA H+N)'
  url: https://miaradmodalitywiki.powerappsportals.com/CT_BRAIN_ATTACK_CT_HEAD_WO_CTA_H_N
  version: '2025'
synonyms:
- CT AVC Acut
- Cod AVC Brain Attack
- CT Craniu Nativ si Angio-CT Cap si Gat
- Stroke Protocol CT
title: Protocol CT Brain Attack — AVC Ischemic Acut (CT Nativ + Angio-CT Craniu & Gât)
---

# Protocol CT Brain Attack — AVC Ischemic Acut (CT Nativ + Angio-CT Craniu & Gât)

Protocol integrat de urgență neurovasculară elaborat de **Medical Imaging Associates (MIA Radiology)** pentru managementul pacienților cu suspiciune de accident vascular cerebral (AVC) ischemic acut eligibili pentru terapie de revascularizare (tromboliză medicamentoasă intravenoasă și/sau trombectomie mecanică endovasculară).

<div class="iris-official-banner" style="margin-bottom: 24px; background: linear-gradient(135deg, #1e1b4b 0%, #312e81 100%); color: #ffffff; padding: 20px 24px; border-radius: 12px; border: 1px solid rgba(165, 180, 252, 0.3);">
  <div class="iris-official-badge" style="background: rgba(165, 180, 252, 0.2); color: #c7d2fe; padding: 4px 12px; border-radius: 999px; display: inline-block; font-weight: 700; font-size: 0.82rem; margin-bottom: 8px;">
    ⚡ URGENȚĂ VITALĂ &bull; TIME IS BRAIN
  </div>
  <p class="iris-official-desc" style="margin-bottom: 12px !important; color: #e0e7ff; font-size: 0.95rem; line-height: 1.55;">
    Protocolul combină într-o singură sesiune scanarea nativă a craniului (excluderea hemoragiei intracraniene și calculul scorului ASPECTS) cu angiografia CT de la arcul aortic la vertex, exportând automat seriile către platforma de inteligență artificială <strong>VizAI</strong> pentru identificarea imediată a ocluziei de vas mare (LVO).
  </p>
  <a href="https://miaradmodalitywiki.powerappsportals.com/CT_BRAIN_ATTACK_CT_HEAD_WO_CTA_H_N" target="_blank" rel="noopener" style="font-weight: 600; color: #a5b4fc; text-decoration: none;">
    Consultați specificațiile originale MIA CT Brain Attack ➔
  </a>
</div>

---

## 1. Justificare Clinică & Ghid IRIS

Conform Ghidului Național de Recomandare a Investigațiilor Imagistice (Ghidul IRIS / Ordinul MS 1342/2012):
- **Indicație:** Deficit neurologic focal cu debut acut (< 24 ore), suspiciune de infarct cerebral ischemic în fereastră terapeutică;
- **Grad de Recomandare:** **Grad A**;
- **Clasă de Doză:** **Clasa 2** (Doză mică, 1 - 3 mSv);
- **Obiectiv Critic:** Excluderea hemoragiei parenchimatoase, decelarea precoce a semnelor de ischemie (hipoatenuare a nucleului lenticular, ștergerea panglicii insulare, semnul arterei cerebrale medii hiperdense) și identificarea stopului circulator pe trunchiurile arteriale mari.

---

## 2. Pregătirea Pacientului & Protocolul Injectorului

| Parametru | Valoare & Instrucțiuni Clinice |
|:----------|:-------------------------------|
| **Statut Alimentar (NPO)** | **Fără repaus alimentar** — urgență medicală de cod roșu. Nu se amână investigația! |
| **Linie Venoasă (IV)** | Canulă intravenoasă **18G** plasată preferențial în plica cotului drept (pentru evitarea artefactelor de influx în trunchiul venos brahiocefalic stâng); |
| **Substanță de Contrast** | Non-ionică, înaltă concentrație (**350 – 370 mg I/mL**, ex. Isovue 370 / Omnipaque 350 / Optiray 350); |
| **Volum Substanță de Contrast** | **100 mL**; |
| **Debit de Injectare** | **4.0 – 5.0 mL/s**; |
| **Saline Flush (Bolus Ser)** | **40 mL ser fiziologic la 4.0 – 5.0 mL/s** (asigură împingerea coloanei de contrast și curățarea venei cave superioare); |
| **Sincronizare Bolus** | Bolus-tracking / SmartPrep cu ROI plasat pe crosa aortei sau artera carotidă comună; prag de declanșare la **100 – 120 HU**. |

---

## 3. Parametri Tehnici de Achiziție & Acoperire Anatomică

### Etapa 1: CT Cranian Nativ (Head Without Contrast)
- **Topogramă / Scout:** Lateral 256 mm;
- **Repere de Scanare:** De la baza craniului (gaura occipitală / C1) până deasupra vertexului;
- **Grosime Secțiune:** 4.0 mm reconstrucție standard cerebrală (Axial 4 mm) + 2.0 mm kernel osos (Axial 2 mm Bone);
- **Reformate:** Coronal 2.0 mm și Sagital 2.0 mm (Standard Brain).

### Etapa 2: Angio-CT Cap & Gât (CTA Head & Neck)
- **Repere de Scanare:** De la nivelul arcului aortic (sub originea arterei subclavii) până deasupra vertexului;
- **Direcție Scanare:** Caudo-cranială (în sensul fluxului arterial);
- **Grosime de Achiziție:** Secțiuni submilimetrice elicoidale (**0.6 – 1.0 mm**);
- **Colimare:** Maximă pentru detectorul scanerului (ex. 64x0.625 mm, 128x0.6 mm).

---

## 4. Reconstrucții & Transmisie Date (PACS & Platforma AI)

| Serie Reformatată | Grosime / Interval | Kernel / Filtru | Fereastră | Destinație |
|:------------------|:-------------------|:----------------|:----------|:-----------|
| **Craniu Nativ Axial** | 4.0 mm / 4.0 mm | Standard Brain | Cerebrum (W:80, L:40) | PACS |
| **Craniu Nativ Os Axial** | 2.0 mm / 2.0 mm | Bone / Osteo | Bone (W:3000, L:500) | PACS |
| **Craniu Nativ Coronal** | 2.0 mm / 2.0 mm | Standard Brain | Cerebrum | PACS |
| **Craniu Nativ Sagital** | 2.0 mm / 2.0 mm | Standard Brain | Cerebrum | PACS |
| **Angio-CT Axial Arc-Vertex** | 1.0 mm / 0.8 mm | Angio Kernel | Angio (W:700, L:200) | PACS |
| **Angio-CT Coronal MIP** | 10.0 mm MIP | Angio Kernel | Angio | PACS |
| **Angio-CT Coronal MIP** | 2.0 mm MIP | Angio Kernel | Angio | PACS |
| **Angio-CT Sagital MIP** | 2.0 mm MIP | Angio Kernel | Angio | PACS |
| **Angio-CT Subțire AI (VizAI)** | 0.6 – 1.0 mm Axial | Angio Kernel | Angio | **VizAI Server** |

> [!IMPORTANT]
> **Fluxul VizAI în MIA Radiology:** Seria axială subțire fără contrast și seria angiografică sunt dirijate direct către serverul de procesare AI. Algoritmul detectează automat ocluziile vasculare proximale (ACI carotidiană internă, ACM segment M1, trunchi bazilar) și trimite alerte securizate pe telefoanele echipei de neuroradiologie intervențională și neurologie de gardă.

---

## 5. Ghid de Interpretare Radiologică & Scor ASPECTS

1. **Excluderea Hemoragiei:** Orice hiperdensitate spontană parenchimatoasă sau în spațiul subarahnoidian contraindică tromboliza intravenoasă;
2. **Scorul ASPECTS (Alberta Stroke Program Early CT Score):**
   - Evaluat pe CT cerebral nativ pe două planuri axiale (la nivelul ganglionilor bazali și la nivelul ventriculilor laterali);
   - Pornind de la 10 puncte, se scade câte 1 punct pentru fiecare arie afectată din cele 10 (C-Caudat, L-Lenticular, IC-Capsulă internă, I-Insulă, M1-M3 la nivelul ganglionilor, M4-M6 la nivel supra-ganglionar);
   - Un scor ASPECTS $\ge 6$ indică parenchim viabil extins și susține decizia de trombectomie mecanică.
3. **Analiza Angiografică CTA:**
   - Localizarea exactă a trombului (LVO);
   - Calitatea circulației colaterale piale leptomeningeale (scorul Tan sau Menon);
   - Morfologia arcului aortic (Tip I, II sau III) și eventualele tortuozități carotidiene esențiale pentru planificarea accesului vascular endovascular.
