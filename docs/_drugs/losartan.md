---
layout: default
title: Losartan
parent: Model Prediction Only (L5)
nav_order: 213
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Losartan: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertensive disorder, hypertension, diabetic nephropathy"
monitor_inn: "Losartan"
predicted_indications: ["malignant hypertensive renal disease", "malignant renovascular hypertension", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "Prinzmetal angina", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies"]
---

# Losartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Losartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Losartan is an angiotensin II receptor blocker, originally used for hypertension and diabetic nephropathy.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease**,
but the evidence is thin: **0 clinical trials** and **1 publication** (a preclinical animal study) are available, and the indication largely overlaps with losartan's existing uses.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertensive disorder, hypertension, diabetic nephropathy |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, losartan is an angiotensin II type 1 (AT1) receptor blocker, its efficacy in hypertension and diabetic nephropathy is established, and mechanistically it may be applicable to malignant hypertensive renal disease.

Angiotensin II and NF-κB signaling drive kidney injury in malignant hypertensive nephrosclerosis. Blocking the AT1 receptor is therefore a plausible way to reduce that damage. The only supporting study is a rat model (PMID 30809002).

This prediction is not a true repurposing signal. Malignant hypertensive renal disease is closely related to hypertension and nephropathy, which losartan already treats. It is essentially an extension of the existing indication.

Other predictions in the list have even weaker support. For malignant renovascular hypertension there is only one case report and a rodent methods chapter. For pulmonary hypertension due to lung disease or hypoxia, the retrieved studies are mostly indirect or preclinical. For brain small vessel disease 1, the rationale is indirect and drawn from related conditions such as Marfan syndrome. Braddock syndrome, Prinzmetal angina and the familial hematuria-retinal arteriolar tortuosity syndrome have no supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30809002](https://pubmed.ncbi.nlm.nih.gov/30809002/) | 2019 | Preclinical animal model | Hypertension Research | In a rat model of malignant hypertensive nephrosclerosis, angiotensin II and the NF-κB system were implicated in kidney injury. Losartan was not tested in this study. |

## Philippines Market Information

The only registration on record (PNF-0296, single-ingredient losartan) has been cancelled. No dosage form or approved indication text is available, and there is no currently valid registration.

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: Conditions linked to contraindication or caution include impaired renal function, anuria, renal artery obstruction, hypotensive disorder, potassium deficiency, hypercalcemia, diabetes mellitus, diabetic ketoacidosis, liver disease, hepatic encephalopathy, pancreatitis, gallbladder disease, gout, systemic lupus erythematosus and neonatal jaundice. These need confirmation against the official package insert.
- **Drug Interactions**: The interaction query returned 100 interactions in total. Major interactions include:
  - Potassium citrate
  - Potassium bicarbonate

  Moderate interactions include:
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide)
  - Acetylsalicylic acid
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin)
  - Insulins (aspart, glargine, human isophane)
  - Morphine
  - Bupropion
  - Aprepitant
  - Dronabinol

  Potassium-containing products warrant particular attention because of hyperkalaemia risk.
- Bilateral renal artery stenosis is also a recognized safety concern with ARBs, which is relevant to the renovascular hypertension prediction.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the evidence is model prediction plus a single animal study (L5). The indication also overlaps with losartan's existing uses. There is no valid Philippine registration, and the package insert safety data has not been obtained.

**To proceed, the following is needed:**
- Obtain the package insert and safety data from the DOH-FDA Philippines, since this gap currently blocks safety screening
- Add detailed mechanism of action data (for example from DrugBank)
- Find human clinical evidence in malignant hypertensive nephropathy, or confirm whether the indication is already covered by the existing hypertension and nephropathy indications
- Clarify the regulatory status in the Philippines, given the cancelled registration
- Consider the brain small vessel disease and pulmonary hypertension predictions only as research questions, as they are supported by indirect evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

