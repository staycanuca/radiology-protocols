---
title: CT torace pediatric de rutină — ≥50 kg, vârstă <18 ani
slug: ct-torace-pediatric-peste-50-kg
modality: ct
category: chest
population: pediatric
pediatric_selection:
  basis: weight_kg
  lower_inclusive: 50
  upper_exclusive: null
  age_upper_exclusive_months: 216
  grouping_status: proposed_for_local_review
clinical_status: draft_not_for_clinical_use
author: Ciornă pregătită cu asistență AI — autorul clinic urmează să fie desemnat
last_updated: '2026-09-13'
clinical_indications:
- Întrebare clinică toracică pentru care radiologul confirmă CT de rutină.
position: Decubit dorsal, centrat; brațele ridicate dacă este posibil.
protocol_type: conditional-contrast
contrast:
  agent: De selectat conform indicației și politicii pediatrice locale
tech_params:
  kv: DE CONFIGURAT PE APARAT
  mas: DE CONFIGURAT PE APARAT
  aec: DE CONFIGURAT PE APARAT
  pitch: DE CONFIGURAT PE APARAT
  rotation_time: DE CONFIGURAT PE APARAT
  collimation: DE CONFIGURAT PE APARAT
  slice_thickness: DE CONFIGURAT PE APARAT
  scan_mode: DE CONFIGURAT PE APARAT
series:
- name: Unică; nativ SAU postcontrast, după indicație
  start: Apexuri pulmonare
  end: Baze pulmonare
  delay: DE CONFIGURAT PE APARAT
  thickness: DE CONFIGURAT PE APARAT
recons:
- acquisition: Unică; nativ SAU postcontrast, după indicație
  plane: Axial; MPR după indicație
  kernel: DE CONFIGURAT PE APARAT
  thickness_increment: DE CONFIGURAT PE APARAT
  ir_strength: DE CONFIGURAT PE APARAT
images: []
review_required_fields:
- Confirmarea pragurilor de grupare pentru populația locală
- Model CT, versiune software și preset pediatric validat
- Completarea tech_params și reconstrucțiilor pentru grupă
- Ținte locale de doză și criterii de acceptare a calității
- 'Contrast: selecție, doză, concentrație, debit și întârziere aprobate local'
---

# CT torace pediatric de rutină — ≥50 kg, vârstă <18 ani

!!! warning "Ciornă pentru revizuire — nu se utilizează clinic"
    Pragurile sunt propuneri de organizare. Presetările nu sunt validate pentru un aparat.

## Selectarea grupei

**≥50 kg, vârstă <18 ani.** Limita inferioară este inclusă, cea superioară exclusă. Pentru grupele de greutate se verifică și vârsta sub 18 ani. Greutatea nu înlocuiește evaluarea dimensiunilor pacientului la alegerea tehnicii.

## Planul examinării

Verifică plămânii, mediastinul și pleura. Alegerea contrastului se stabilește înainte de achiziție.

## Înaintea utilizării

Recenzorul completează câmpurile marcate **DE CONFIGURAT PE APARAT**, stabilește pregătirea și măsurile de siguranță locale și rezolvă lista `review_required_fields`. Câmpul `clinical_status` se actualizează numai după revizuire. Nu există valori implicite de adult sau doze de contrast calculate de această ciornă.

## Ilustrație

Imaginea atașată este un exemplu de anatomie/patologie, nu etalon de expunere, normalitate sau potrivire cu grupa. Vârsta/greutatea cazului ilustrat nu trebuie dedusă din grupa acestui dosar.
