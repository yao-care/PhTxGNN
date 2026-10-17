---
layout: default
title: Heparin
parent: Moderate Evidence (L3-L4)
nav_order: 166
evidence_level: L4
indication_count: 2
last_modified_at: 2026-10-15
description: "Heparin: predicted new indication Thrombophilia due to protein C deficiency, autosomal recessive (evidence level L4). Approved use: Pulmonary embolism, disseminated intravascular coagulation…"
monitor_inn: "Heparin"
predicted_indications: ["thrombophilia due to protein C deficiency, autosomal recessive", "primary release disorder of platelets"]
---

# Heparin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **2** 
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

# Heparin: From Pulmonary Embolism to Thrombophilia due to Protein C Deficiency (Autosomal Recessive)

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
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L4 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, heparin potentiates antithrombin and thereby inhibits thrombin and factor Xa. This could offset the hypercoagulable state caused by absent protein C activity.

The new indication is closely related to the original ones. Severe (homozygous) protein C deficiency is a classic cause of purpura fulminans, which is already among heparin's original indications. This makes the prediction biologically plausible.

Caution is needed. The very high TxGNN score is a computational result and likely reflects how close this disease sits to purpura fulminans in the knowledge graph. Standard care for severe congenital protein C deficiency is protein C concentrate or fresh frozen plasma, with anticoagulation as an adjunct. This is background knowledge, not evidence from the data compiled here.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for this indication.

---

## Philippines Market Information

Heparin has one registration on record (PNF-0225, single-ingredient product), and it is **cancelled**. No dosage form, manufacturer or approved indication text is available. There is no currently valid registration in the Philippines.

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
The prediction is mechanistically plausible and close to heparin's existing use in purpura fulminans, but no trials or publications address this specific disease. The evidence is limited to a model score and reasoning (L4). Heparin also has no valid registration in the Philippines, and label safety data is missing.

**To proceed, the following is needed:**
- Targeted literature review of heparin or other anticoagulants in severe congenital protein C deficiency, compared with protein C concentrate or plasma
- Mechanism of action data (MOA) from DrugBank
- Package insert warnings and contraindications from DOH-FDA Philippines
- Clarification of regulatory status, since the only registration is cancelled
- Clinical expert review of dosing, bleeding risk and monitoring in this population

---

## Appendix: Second-Ranked Prediction (Not Recommended)

The model's second prediction, **primary release disorder of platelets** (score 99.06%, evidence level L5, decision **Hold**), has no credible mechanistic rationale. These are bleeding-tendency platelet function defects, and heparin is an anticoagulant that raises bleeding risk. It can also cause platelet-related harm such as heparin-induced thrombocytopenia. The 20 retrieved publications are loosely related to coagulation, HIT, cirrhosis and cancer-associated thrombosis, and none addresses heparin treatment of this condition. The high score is probably an artifact of graph proximity to platelet and coagulation terms. This prediction is not recommended for further pursuit.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

