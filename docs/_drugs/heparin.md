---
layout: default
title: Heparin
parent: Model Prediction Only (L5)
nav_order: 166
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Heparin: predicted new indication Thrombophilia due to protein C deficiency, autosomal recessive (evidence level L5). Approved use: Pulmonary embolism, disseminated intravascular coagulation…"
monitor_inn: "Heparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets"]
---

# Heparin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Heparin: From Pulmonary Embolism to Thrombophilia due to Protein C Deficiency, Autosomal Recessive
{: .text-alpha }

## One-Sentence Summary

Heparin is an anticoagulant originally used for pulmonary embolism, disseminated intravascular coagulation and purpura fulminans.
The TxGNN model predicts it may be effective for **thrombophilia due to protein C deficiency, autosomal recessive**,
but currently there are **0 clinical trials** and **0 publications** supporting this specific prediction. It rests on model prediction and mechanistic reasoning only.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, disseminated intravascular coagulation, purpura fulminans, acquired purpura fulminans |
| Predicted New Indication | Thrombophilia due to protein C deficiency, autosomal recessive |
| TxGNN Prediction Score | 0.9929 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, heparin potentiates antithrombin and thereby inhibits thrombin and factor Xa. This could offset the hypercoagulable state caused by absent protein C activity.

The new indication is closely related to the original ones. Severe (homozygous) protein C deficiency is a classic cause of purpura fulminans, which is already among heparin's original indications. This makes the prediction biologically plausible.

Caution is needed. The very high TxGNN score is a computational result from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Standard care for severe congenital protein C deficiency is protein C concentrate or fresh frozen plasma, with anticoagulation as an adjunct. This is background knowledge, not evidence from the data compiled here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for this indication.

---

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Heparin (unfractionated) (as sodium salt) | Injection |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

No manufacturer or approved indication text is available.

<!-- review:begin ph-lic-20261106-heparin-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Heparin has one registration on record (PNF-xxxx, single-ingredient product), and it is **valid**. No dosage form, manufacturer or approved indication text is available. There is 1 currently valid registration of 1 in the Philippines." Removed: the number or status of PNF entries stated here did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. "PNF-xxxx" stands for a code an earlier version of this site's software assigned to the record; the PNF has no entry numbers, so the code is not shown. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-heparin-2 -->

---

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

Additional signals from the knowledge graph (these are drug-disease relationships, not label text):

- **Contraindication-related conditions** include: heparin-induced thrombocytopenia, thrombocytopenia, hemophilia and other blood coagulation diseases, antithrombin III deficiency, Glanzmann thrombasthenia and qualitative platelet defects, intracranial and intracerebral hemorrhage, placental abruption, active peptic ulcer disease, ulcerative colitis and inflammatory bowel disease, liver failure, biliary tract disease and obstructive jaundice, infective endocarditis, osteoporosis, and retinal disease (including diabetic and hypertensive retinopathy).
- **Drug interactions** (100 total found; examples shown):
  - Moderate: acetylsalicylic acid, sulfonylureas and glinides (glimepiride, glipizide, glyburide, chlorpropamide, tolazamide, tolbutamide, acetohexamide, repaglinide, nateglinide), fenfluramine, dexfenfluramine, sibutramine.
  - Unknown severity: levocarnitine, mannitol, calcitriol, vitamin A, pantoprazole, mesalazine, doxycycline.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is mechanistically plausible and close to heparin's existing use in purpura fulminans, but no trials or publications address this specific disease. The evidence is limited to a model score and reasoning (L4). Label safety data is missing.

<!-- review:begin ph-lic-20261106-heparin-3 -->

> **Review correction (2026-11-06)**: Originally stated: "Heparin has 1 valid registration of 1 in the Philippines, but label safety data is missing." Removed: the number or status of PNF entries stated here did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-heparin-3 -->

**To proceed, the following is needed:**
- Targeted literature review of heparin or other anticoagulants in severe congenital protein C deficiency, compared with protein C concentrate or plasma
- Mechanism of action data (MOA) from DrugBank
- Package insert warnings and contraindications from DOH-FDA Philippines
- Clinical expert review of dosing, bleeding risk and monitoring in this population

<!-- review:begin ph-lic-20261031-heparin-1 -->

> **Review correction (2026-10-31)**: Originally stated: "Package insert warnings and contraindications from DOH-FDA Philippines / Clarification of regulatory status, since the only registration is cancelled" Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-10-31). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261031-heparin-1 -->

---

## Appendix: Second-Ranked Prediction (Not Recommended)

The model's second prediction, **primary release disorder of platelets** (score 0.9906, evidence level L5, decision **Hold**), has no credible mechanistic rationale. These are bleeding-tendency platelet function defects, and heparin is an anticoagulant that raises bleeding risk. It can also cause platelet-related harm such as heparin-induced thrombocytopenia. The 20 retrieved publications are loosely related to coagulation, HIT, cirrhosis and cancer-associated thrombosis, and none addresses heparin treatment of this condition. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. This prediction is not recommended for further pursuit.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "Clarification of regulatory status, since the only registration is cancelled" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-06 | Removed: "Heparin has one registration on record (PNF-xxxx, single-ingredient product), and it is **valid**. dosage form, There is 1 currently valid r" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-06 | Removed: "Heparin has 1 valid registration of 1 in the Philippines, but l" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

