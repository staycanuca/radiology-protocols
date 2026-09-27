---
author: MIA Radiology / Imagistică Vasculară
category: vascular
clinical_indications:
- Supraveghere imagistică post-implantare endoproteză aortică abdominală (EVAR) sau toracică (TEVAR)
- Detecția și clasificarea endoleak-urilor (Tip I, II, III, IV, V)
- Monitorizarea diametrului sacului anevrismal rezidual (creștere vs stabilitate vs regresie)
- Evaluarea integrității structurale a endoprotezei (migrare, plicaturare, deconectare modulară, fractură de stent)
- Suspiciune de infecție a grefei vasculare sau tromboză de braț iliac
contrast:
  agent: Substanță de contrast iodată non-ionică (350 - 370 mg I/mL)
  flow_rate: 4.0 mL/s
  roi: Aorta proximală deasupra grefonului (SmartPrep / Bolus tracking)
  timing: 'Protocol trifazic: 1) Nativ; 2) Fază arterială angiografică (CTA); 3) Fază tardivă venoasă la 120-180 secunde'
  trigger: 150 HU prag automat
  volume: 100 - 120 mL contrast + 40 mL ser fiziologic
iris_reference:
  chapter: Sistem Vascular & Torace
  radiation_dose: Clasa 3 (Medie 3 - 10 mSv)
  recommendation_grade: Grad A
last_updated: '2026-09-27'
modality: ct
notes:
  additional_recons: Reconstrucții coronale și sagitale MPR 3x3 mm pentru fiecare fază; reconstrucții MIP 5 mm și 3D VR (Volume Rendering) pentru arborele aortic și brațele iliace.
  nursing: Linie venoasă 18G antecubitală. Verificare antecedente alergice și funcție renală (eGFR).
  rad: >-
    Analiză comparativă obligatorie cu scanările anterioare. Faza nativă diferențiază calcificările dense de extravazarea de contrast. Faza arterială identifică scurgerile cu flux rapid (Tip I și III). Faza tardivă (120-180s) este indispensabilă pentru decelarea endoleak-urilor cu flux lent (Tip II prin artere lombare patente sau arteră mezenterică inferioară).
  tech: Pacient poziționat în decubit dorsal cu brațele ridicate deasupra capului. Acoperire de la apertura toracică superioară (sau deasupra celiacului pentru EVAR) până sub trohanterii mici.
  tips: >-
    Măsurarea diametrului maxim al sacului anevrismal trebuie efectuată strict perpendicular pe axul lung al aortei (pe reconstrucții multiplanare ortogonale, nu pe secțiuni axiale simple).
npo: 4 ore repaus alimentar pentru solide; hidratare orală permisă
position: Decubit dorsal cu brațele ridicate deasupra capului
premedication: Fără premedicație de rutină
protocol_type: vascular
recons:
- acquisition: Faza Nativă (Fără Contrast)
  fov: Aortă toraco-abdominală și pelvis
  kernel: Standard Soft Tissue
  notes: Vizualizarea scheletului metalic, a calcificărilor și a hiperdensităților spontane
  plane: Axial
  thickness_increment: 2.5 mm / 2.5 mm
- acquisition: Faza Arterială Angiografică (CTA)
  fov: Arc aortic / diafragm până sub trohanterii mici
  kernel: Vascular / Soft Tissue
  notes: Evaluarea lumenului patent, a zonelor de ancorare și a endoleak-urilor Tip I / III
  plane: Axial
  thickness_increment: 1.0 - 1.25 mm / 0.8 mm
- acquisition: Faza Arterială Angiografică
  fov: Abdomen și pelvis
  kernel: Vascular
  notes: Reconstrucție MPR coronală
  plane: Coronal
  thickness_increment: 3 mm / 3 mm
- acquisition: Faza Arterială Angiografică
  fov: Abdomen și pelvis
  kernel: Vascular
  notes: Reconstrucție MPR sagitală
  plane: Sagital
  thickness_increment: 3 mm / 3 mm
- acquisition: Faza Venoasă / Tardivă (120 - 180s)
  fov: Sac anevrismal și pelvis
  kernel: Standard Soft Tissue
  notes: Identificarea endoleak-urilor tardive cu flux lent (Tip II)
  plane: Axial
  thickness_increment: 2.5 mm / 2.5 mm
- acquisition: Faza Venoasă / Tardivă
  fov: Abdomen și pelvis
  kernel: Standard Soft Tissue
  notes: Reconstrucție coronală MPR tardivă
  plane: Coronal
  thickness_increment: 3 mm / 3 mm
slug: ct-aorta-endoproteza-evar
sources:
- institution: Medical Imaging Associates (MIA)
  relationship: Adaptare conform protocolului instituțional oficial
  title: 'MIA Modality Wiki: CT CTA Aorta with Endograft'
  url: https://miaradmodalitywiki.powerappsportals.com/CT-Aorta-with-Endograft
  version: '2025'
synonyms:
- Angio-CT Endoproteza EVAR
- CT TEVAR Aorta Toracica
- Supraveghere Endoproteza Aortica
- CT Endoleak Protocol
title: Protocol CT Supraveghere Endoproteză Aortică (EVAR / TEVAR Trifazic)
---

# Protocol CT Supraveghere Endoproteză Aortică (EVAR / TEVAR Trifazic)

Protocol de angiografie tomografică computerizată multifazică dedicat supravegherii post-operatorii a pacienților purtători de endoproteze aortice abdominale (**EVAR**) sau toracice (**TEVAR**), elaborat de **Medical Imaging Associates (MIA Radiology)**.

<div class="iris-official-banner" style="margin-bottom: 24px; background: linear-gradient(135deg, #065f46 0%, #047857 100%); color: #ffffff; padding: 20px 24px; border-radius: 12px; border: 1px solid rgba(167, 243, 208, 0.3);">
  <div class="iris-official-badge" style="background: rgba(167, 243, 208, 0.2); color: #a7f3d0; padding: 4px 12px; border-radius: 999px; display: inline-block; font-weight: 700; font-size: 0.82rem; margin-bottom: 8px;">
    🩸 MONITORIZARE VASCULARĂ &bull; SUPRAVEGHERE EVAR / TEVAR
  </div>
  <p class="iris-official-desc" style="margin-bottom: 12px !important; color: #ecfdf5; font-size: 0.95rem; line-height: 1.55;">
    Detectarea la timp a scurgerilor perigrefon (<em>endoleaks</em>) și prevenirea rupturii tardive de anevrism necesită o explorare strict <strong>trifazică</strong>: scanarea nativă este urmată de faza arterială de mare viteză și obligatoriu de <strong>faza tardivă (120 – 180 secunde)</strong>, singura capabilă să decelaze endoleak-urile cu flux lent de Tip II.
  </p>
  <a href="https://miaradmodalitywiki.powerappsportals.com/CT-Aorta-with-Endograft" target="_blank" rel="noopener" style="font-weight: 600; color: #6ee7b7; text-decoration: none;">
    Consultați specificațiile originale MIA CTA Aorta Endograft ➔
  </a>
</div>

---

## 1. Justificare Clinică & Ghid IRIS

- **Indicație:** Control periodic după reparare endovasculară de anevrism aortic la 1 lună, 6 luni, 12 luni și ulterior anual dacă sacul este stabil; suspiciune de endoleak, creștere a sacului anevrismal sau ischemie acută de membru inferior.
- **Grad de Recomandare:** **Grad A** (standardul de aur în ghidurile internaționale ESVS și SVS).
- **Clasă de Doză:** **Clasa 3** (Doză medie, 3 - 10 mSv).

---

## 2. Protocol de Injectare & Faze de Achiziție

| Parametru | Specificație Tehnică |
|:----------|:---------------------|
| **Cateter IV** | 18G în vena antecubitală |
| **Agent Contrast** | Substanță iodată non-ionică 350 – 370 mg I/mL |
| **Volum & Debit** | 100 – 120 mL la un debit de **4.0 mL/s** |
| **Saline Chaser** | 40 – 50 mL ser fiziologic la 4.0 mL/s |
| **Declanșare Arterială** | Bolus-tracking în aorta proximală deasupra endoprotezei la prag de **150 HU** |
| **Faza Tardivă** | Întârziere fixă de **120 – 180 secunde** post-injectare |

---

## 3. Protocolul Celor Trei Faze de Scanare

```mermaid
flowchart LR
    P1["1. Faza Nativă<br/>(Fără Contrast)"] --> P2["2. Faza Arterială CTA<br/>(Bolus-Tracking 150 HU)"]
    P2 --> P3["3. Faza Tardivă<br/>(120 - 180 Secunde)"]
    
    P1 -.-> D1["Calcificări & Schelet Metalic"]
    P2 -.-> D2["Lumen, Permeabilitate & Endoleak Tip I / III"]
    P3 -.-> D3["Endoleak Tip II cu Flux Lent"]
```

1. **Faza Nativă:** Deasupra trunchiului celiac până la bifurcația femurală. Distinge calcificările parietale preexistente și densitățile spontane de contrastul extravazat în sac.
2. **Faza Arterială:** Vizualizează lumenul vascular, permeabilitatea arterelor renale și a arterelor iliace interne/externe. Evidențiază endoleak-urile cu debit crescut la nivelul manșetelor de etanșare (Tip I) sau defecte de conexiune structurală între componente (Tip III).
3. **Faza Tardivă (120-180s):** Re-scanare centrată pe sacul anevrismal. Detectează acumularea progresivă a contrastului din vasele colaterale retrograd patente (artere lombare, artera mezenterică inferioară) caracteristică endoleak-ului de Tip II.

---

## 4. Clasificarea Radiologică a Endoleak-urilor

| Tip Endoleak | Mecanism Fiziopatologic | Comportament Imagistic CT | Atitudine Terapeutică |
|:-------------|:------------------------|:--------------------------|:----------------------|
| **Tip I** | Defect de etanșare la zona de fixare proximală (IA) sau distală (IB) | Opacifiere imediată în faza arterială în contact direct cu manșeta endoprotezei | **Urgență chirurgicală / endovasculară** (risc mare de ruptură) |
| **Tip II** | Flux retrograd în sac din ramuri colaterale (artere lombare, artera mezenterică inferioară) | Frecvent absent sau discret în faza arterială; **apariție netă în faza tardivă (120-180s)** | Supraveghere; embolizare dacă sacul anevrismal crește $\ge 5$ mm |
| **Tip III** | Defecțiune structurală: deconectare a componentelor modulare (IIIA) sau ruptură de grefă (IIIB) | Jet arterial masiv în sacul anevrismal în faza arterială | **Urgență de reintervenție** prin plasare de manșon suplimentar |
| **Tip IV** | Porozitate tranzitorie a materialului textil al grefei | Încărcare difuză în primele 30 zile postoperator, dispare spontan | Rezoluție spontană post-anticoagulare |
| **Tip V** | Endotensiune (creștere a presiunii și a sacului fără evidențierea unei scurgeri de contrast) | Sac în creștere fără jet decelabil | Monitorizare atentă / conversie chirurgicală |
