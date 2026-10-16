---
layout: default
title: Atenolol
parent: Moderate Evidence (L3-L4)
nav_order: 32
evidence_level: L4
indication_count: 9
last_modified_at: 2026-10-15
description: "Atenolol: predicted new indication Posteroinferior myocardial infarction (evidence level L4). Approved use: Hypertension, myocardial infarction"
monitor_inn: "Atenolol"
predicted_indications: ["posteroinferior myocardial infarction", "posterolateral myocardial infarction", "malignant renovascular hypertension", "malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "septal myocardial infarction", "Braddock syndrome", "chronic pulmonary heart disease"]
---

# Atenolol
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

# Atenolol: From Hypertension and Myocardial Infarction to Posteroinferior Myocardial Infarction

## One-Sentence Summary

Atenolol is a beta-blocker originally used to treat hypertension and myocardial infarction.
The TxGNN model predicts it may be effective for **posteroinferior myocardial infarction**,
but this is a sub-type of an existing indication, and there are currently **0 clinical trials** and only **1 indirect publication** supporting the prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, myocardial infarction (from the knowledge graph; the Philippines registration has no indication text) |
| Predicted New Indication | Posteroinferior myocardial infarction |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, atenolol is a cardioselective (beta-1) blocker, its efficacy in hypertension and myocardial infarction is established, and mechanistically it may be applicable to infarct sub-types.

Beta-1 blockade lowers heart rate, myocardial oxygen demand and arrhythmic risk, which is plausible for an infarct in any location. Posteroinferior myocardial infarction is an anatomical sub-type of myocardial infarction, which is already an original indication. This is therefore not true repurposing. The high score most likely reflects the closeness of this term to the parent MI term in the knowledge graph, and not independent evidence.

Other top predictions follow a similar pattern. Posterolateral and septal myocardial infarction, as well as malignant renovascular hypertension and malignant hypertensive renal disease, are sub-types of approved indications. The predictions for pulmonary hypertension and chronic pulmonary heart disease are mechanistically weak. Preclinical data suggest beta-2 receptor-dependent protection in hypoxic pulmonary vasoconstriction, which argues against a benefit from beta-1 blockade, and beta-blockers are generally cautioned against in pulmonary hypertension with right ventricular dysfunction.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3901170](https://pubmed.ncbi.nlm.nih.gov/3901170/) | 1985 | Crossover RCT (small, single-blind) | La Revue de medecine interne | Compared the anti-ischaemic activity of atenolol (200 mg) and diltiazem (240 mg) in 23 patients 4 weeks after a postero-inferior or anterior MI, using exercise testing. Indirect evidence, not specific to posteroinferior MI. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0031 | Atenolol | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: The knowledge graph links atenolol to contraindications in the following groups:
  - Respiratory and allergic: asthma (including intrinsic and allergic asthma), anaphylaxis
  - Cardiovascular: atrioventricular block, Raynaud disease
  - Metabolic and endocrine: type 1 and type 2 diabetes mellitus, diabetic ketoacidosis, gout and hyperuricaemia, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease, potassium deficiency disease
  - Other: liver failure, anuria, pancreatitis, systemic lupus erythematosus (including paediatric), psoriasis and parapsoriasis, anxiety, neurotic and dysthymic disorders
- **Drug Interactions**: 100 interactions were identified. The ones listed in the data compiled for this report are mostly Moderate. Examples include epinephrine, hydrocortisone and other corticosteroids (betamethasone, budesonide, triamcinolone), morphine, bupropion, atropine, hyoscyamine, acetohexamide, and calcium salts. Minor interactions include acetylsalicylic acid, aluminium hydroxide and attapulgite.
- **Renal consideration**: Atenolol is renally cleared and needs dose adjustment in renal impairment.

Package insert warnings and contraindications could not be retrieved. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Posteroinferior myocardial infarction falls within the already established indication of myocardial infarction, so the prediction adds little new value. The only supporting paper is a small 1985 study that gives indirect evidence, there are no clinical trials, and the Philippines registration is cancelled with no valid product on the market.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank)
- Clarification of whether the cancelled registration PNF-0031 can be reinstated or a new registration is required
- Review of the contraindication list (asthma, diabetes, atrioventricular block) against the target population
- Clinical guideline review to confirm whether location-specific MI evidence adds anything beyond the existing MI indication
- For the pulmonary hypertension and cor pulmonale predictions, a separate safety and mechanistic review before further consideration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

