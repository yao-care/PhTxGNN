---
layout: default
title: Telmisartan
parent: Model Prediction Only (L5)
nav_order: 328
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
monitor_inn: "Telmisartan"
predicted_indications: ["Prinzmetal angina", "brain stem infarction", "ABri amyloidosis", "cerebral artery occlusion", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "malignant hypertensive renal disease", "intracerebral hemorrhage", "Braddock syndrome"]
description: "Telmisartan: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not recorded in the local data"
---

# Telmisartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Telmisartan: Prinzmetal angina
{: .text-alpha }

## One-Sentence Summary

Telmisartan is an angiotensin receptor blocker, originally used to treat hypertension and to lower stroke risk.
The TxGNN model predicts it may be effective for **Prinzmetal angina** (coronary vasospasm),
but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, telmisartan belongs to the angiotensin II receptor blocker (ARB) class. Its efficacy in hypertension and in reducing cerebrovascular events is established, and it may act on blood vessel tone.

Prinzmetal angina is caused by spasm of the coronary arteries. A plausible link is ARB-mediated vasodilation and improved endothelial function, and telmisartan is also reported to have partial PPARγ activity. However, this link is speculative. No trials or publications were retrieved to show that telmisartan prevents or treats coronary vasospasm. The prediction therefore rests on the model score alone.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0474 (cancelled) | Telmisartan | Not specified | Not specified |


## Safety Considerations

- **Contraindications (knowledge-graph derived, not label text)**: The TxGNN knowledge graph links telmisartan to the following conditions as contraindications. Verify them against the official label.
  - Liver and biliary: liver failure, liver disease, hepatic coma, hepatic encephalopathy, cholestasis (including benign recurrent and familial intrahepatic forms), gallbladder disease, neonatal jaundice
  - Kidney and urinary: kidney disease, anuria, renal artery obstruction, pyoureter, nephrocalcinosis
  - Metabolic and electrolyte: diabetes mellitus, diabetic ketoacidosis, potassium deficiency, hyperuricemia, gout, hypercalcemia, hyperparathyroidism, osteitis fibrosa, phosphorus metabolism disease
  - Other: pancreatitis, systemic lupus erythematosus (including the pediatric form), hypotensive disorder
- **Drug Interactions**: 100 interactions were recorded. The major-severity ones shown are:
  - Potassium citrate (Major)
  - Potassium bicarbonate (Major)

  Moderate-severity examples include:
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin)
  - Insulins and exenatide
  - Aspirin
  - Morphine
  - Bupropion
  - Dronabinol
  - Bowel-preparation agents

For package-insert warnings, please refer to the official label, as none were available in the data compiled.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The Prinzmetal angina prediction has a very high model score but no supporting clinical trials or literature (L5). The only Philippines registration is cancelled, and label-based safety data are missing. There is not enough evidence to advance this candidate.

**To proceed, the following is needed:**
- A systematic literature search on ARBs/telmisartan in coronary vasospasm and Prinzmetal angina, including preclinical and case-level data
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the Philippines regulator
- Confirmation of current regulatory and market availability, since the only registration found is cancelled

**Note on other predicted indications:** Among the lower-ranked predictions, **intracerebral hemorrhage** has the strongest evidence. It rests on the large Phase 3 TRIDENT trial (NCT02699645, n=1671), which tested a low-dose triple-pill combination that includes telmisartan. Its benefit cannot be attributed to telmisartan alone, and the full results should be verified. **Cerebral artery occlusion** has only preclinical support and substantially overlaps with the already-established stroke indication. A separate report on these may be worthwhile.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

