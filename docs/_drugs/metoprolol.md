---
layout: default
title: Metoprolol
parent: Model Prediction Only (L5)
nav_order: 233
evidence_level: L5
indication_count: 6
monitor_inn: "Metoprolol"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "Braddock syndrome", "chronic pulmonary heart disease", "trichotillomania"]
last_modified_at: 2026-10-28
description: "Metoprolol: predicted new indication Malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Metoprolol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Metoprolol: Malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Metoprolol is a beta-1 selective blocker whose relations recorded in the knowledge graph cover hypertension, acute coronary syndrome and myocardial infarction.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but **no clinical trials and no publications** directly study this disease, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9991 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Metoprolol is a beta-1 selective blocker. Such drugs lower heart rate, cardiac output and renin release, which is why they are used in hypertension.

Malignant hypertensive renal disease is a kidney complication of severe hypertension, so a link to a blood-pressure-lowering drug is biologically plausible. However, this is essentially an extension of the hypertension relation already recorded in the knowledge graph. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No study of metoprolol in malignant hypertensive nephropathy was found.

Other predictions in the list are weaker still. For pulmonary hypertension, beta-blockers are generally used with caution because of the risk of reduced cardiac output and right ventricular function. For Braddock syndrome and trichotillomania, no mechanistic rationale can be established from the data.

## Clinical Trial Evidence

Currently no related clinical trials registered for malignant hypertensive renal disease.

For context, trials were found only for a different predicted condition (chronic pulmonary heart disease), and they concern metoprolol in patients with COPD, not this disease:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02587351](https://clinicaltrials.gov/study/NCT02587351) | Phase 3 | Terminated | 532 | Metoprolol to prevent COPD exacerbations; no benefit, with more exacerbations requiring hospitalisation |
| [NCT06825728](https://clinicaltrials.gov/study/NCT06825728) | Phase 4 | Not yet recruiting | 311 | Metoprolol in heart failure with reduced ejection fraction and COPD |
| [NCT00384566](https://clinicaltrials.gov/study/NCT00384566) | Phase 4 | Withdrawn | 0 | Carvedilol vs metoprolol respiratory effects in heart failure; no data |

## Literature Evidence

Currently no related literature available for malignant hypertensive renal disease.

Selected publications on metoprolol in COPD with heart disease (another predicted condition, shown only as background on respiratory safety):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38762800](https://pubmed.ncbi.nlm.nih.gov/38762800/) | 2024 | RCT | JAMA | Bisoprolol in COPD; notes that metoprolol did not reduce exacerbations and increased hospital admissions |
| [38587241](https://pubmed.ncbi.nlm.nih.gov/38587241/) | 2024 | RCT | N Engl J Med | Beta-blockers after myocardial infarction with preserved ejection fraction |
| [32000982](https://pubmed.ncbi.nlm.nih.gov/32000982/) | 2020 | Cohort | Am J Cardiol | Metoprolol vs carvedilol in older patients with heart failure, COPD, diabetes and renal failure |
| [26844454](https://pubmed.ncbi.nlm.nih.gov/26844454/) | 2016 | Cohort | Medicine | Beta-blocker survival effects in coexisting heart failure and COPD (Taiwan database) |
| [14520486](https://pubmed.ncbi.nlm.nih.gov/14520486/) | 2003 | Study | Heart Vessels | Metoprolol appeared safe in coronary artery disease patients with COPD |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0323 | Metoprolol | Not stated | Not stated |

The licence record contains no indication text, so no approved use is confirmed from local label data.

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: contraindication links include diabetes mellitus and diabetic ketoacidosis, liver disease, pancreatitis, gallbladder disease, systemic lupus erythematosus, psoriasis, gout, myasthenia gravis, phaeochromocytoma, hypotensive disorder, anxiety and related disorders, and several metabolic conditions (potassium deficiency, hypercalcaemia, hyperparathyroidism). These need checking against the official label.
- **Drug Interactions**: 100 interactions were found. Most listed are Moderate, including epinephrine, corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), bupropion, morphine, cimetidine, canagliflozin, dapagliflozin, chlorpropamide, and anticholinergics (atropine, hyoscyamine, glycopyrronium). Minor ones include acetylsalicylic acid and magnesium oxide.
- **Respiratory safety**: the terminated BLOCK COPD trial raised concern about COPD exacerbations in patients without a cardiac indication.

Please refer to the package insert for official warnings and contraindications, which were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for malignant hypertensive renal disease has no supporting trials or publications, so the evidence level is L5. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The other predictions are also unsupported, except chronic pulmonary heart disease, where only indirect COPD data exist and some are negative.

**To proceed, the following is needed:**
- Studies of metoprolol specifically in malignant hypertensive nephropathy
- Mechanism of action data
- Package insert warnings and contraindications from the Philippines FDA, and the approved indication text for licence PNF-0323
- Dosage form and route information for the Philippine product
- A review of the knowledge-graph contraindication relations against the label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

