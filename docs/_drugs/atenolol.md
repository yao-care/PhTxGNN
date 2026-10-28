---
layout: default
title: Atenolol
parent: Model Prediction Only (L5)
nav_order: 32
evidence_level: L5
indication_count: 5
monitor_inn: "Atenolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease"]
last_modified_at: 2026-10-23
description: "Atenolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Hypertension, myocardial infarction"
---

# Atenolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Atenolol: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Atenolol is a beta-1 selective blocker whose relations recorded in the knowledge graph include hypertension and myocardial infarction. The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but **no clinical trials and no publications** directly studying this disease were found, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, myocardial infarction (relations recorded in the knowledge graph; the local licence record contains no indication text) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9985 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Atenolol is generally known as a beta-1 selective blocker that lowers blood pressure and reduces renin release. Because both can matter in hypertensive kidney injury, a link to this disease is plausible in principle.

Malignant hypertensive renal disease is a severe kidney complication of very high blood pressure. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

There are important caveats. Malignant hypertension is a hypertensive emergency, usually managed with titratable intravenous drugs, so oral atenolol is not a natural fit. No studies were supplied that test atenolol for this condition.

## Other Predictions Reviewed

All four other predictions are also at Hold. None has a clinical trial.

| Predicted Disease | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|
| Pulmonary hypertension, unclear multifactorial mechanism | 0.9984 | L5 | Computational prediction only. Beta-blockade could in theory harm right ventricular function. |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 0.9984 | L5 | See note below. |
| Braddock syndrome | 0.9980 | L5 | Very rare condition; no plausible mechanistic link found. |
| Chronic pulmonary heart disease | 0.9904 | L5 | See note below. |

**Evidence level note:** The data compiled for this report show L4 for hypoxia-related pulmonary hypertension and chronic pulmonary heart disease. Under the evidence ceiling rule, L4 or higher requires at least one study that directly addresses the predicted disease. The supplied papers for these diseases are animal studies, general beta-blocker reviews, or off-topic items, and none tests atenolol in the disease itself. They are therefore treated as **L5** here.

- **Hypoxia-related pulmonary hypertension:** The animal findings are mixed. Beta-blockade reduced hypoxia-induced right heart hypertrophy in one rat study (PMID 8590992), but another study in rabbits found no inhibition (PMID 6212672).
- **Chronic pulmonary heart disease:** The literature is general beta-blocker and hypertension material. One preclinical paper (PMID 25350545) points to beta-2 signaling, a different receptor subtype from atenolol's beta-1 selectivity.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked indication, malignant hypertensive renal disease, or for the other predicted indications.

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0031 | Atenolol | Not stated | Not stated |

This is a single-ingredient product with valid status. The record contains no indication text, so no approved indication can be confirmed from the local record.

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for label safety information.

- **Relations recorded in the knowledge graph (not label text):** Contraindication relations are recorded for conditions including asthma, atrioventricular block, Raynaud disease, anaphylaxis, diabetes mellitus (including diabetic ketoacidosis), liver failure, pancreatitis, systemic lupus erythematosus, psoriasis, gout, anuria, and several electrolyte or metabolic disorders. These should be checked against the actual label.
- **Drug Interactions:** The interaction search returned 100 records. Those listed include moderate interactions with epinephrine, hydrocortisone, hyoscyamine, bupropion, triamcinolone, morphine, atropine, betamethasone, budesonide, acetohexamide, and calcium salts. Aspirin, aluminum hydroxide, and attapulgite are listed as minor.
- **Disease-specific concern:** Beta-blockers may be unfavorable in pulmonary hypertension because of possible effects on right ventricular function, and cardioselective beta-blocker use in COPD-related disease needs caution.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score (0.9985). There are no clinical trials or publications directly studying atenolol in malignant hypertensive renal disease, so the evidence level is L5. The usual management of this condition with intravenous agents also makes oral atenolol a poor fit.

**To proceed, the following is needed:**
- Mechanism of action data for atenolol
- Package insert warnings and contraindications from the Philippines regulator
- Clinical or observational studies that directly examine atenolol in malignant hypertensive renal disease
- A clinical rationale for how an oral beta-blocker would fit into the care of hypertensive emergencies
- Route and dosage form confirmation, since the local record lists no dosage form
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

