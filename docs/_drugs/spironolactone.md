---
layout: default
title: Spironolactone
parent: Model Prediction Only (L5)
nav_order: 317
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-30
monitor_inn: "Spironolactone"
predicted_indications: ["hypotrichosis simplex of the scalp", "congenital hypotrichosis milia"]
description: "Spironolactone: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Not recorded in the local data"
---

# Spironolactone
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

## Spironolactone: Hypotrichosis simplex of the scalp
{: .text-alpha }

## One-Sentence Summary

Spironolactone was originally used to treat hypertension, congestive heart failure and hyperaldosteronism.
The TxGNN model predicts it may be effective for **hypotrichosis simplex of the scalp**,
but the data compiled for this report contain **0 clinical trials** and **0 publications**, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Spironolactone is generally known as an aldosterone (mineralocorticoid receptor) antagonist, and it also has anti-androgen activity: it blocks the androgen receptor and reduces androgen synthesis. This is the basis for its off-label use in female pattern hair loss.

The link to the predicted indication is weak. Hypotrichosis simplex is a genetic hair-loss disorder (for example, variants in CDSN, APCDD1 or RPL21) and is not mainly driven by androgens. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as androgenetic alopecia, not biological evidence, so the mechanistic link should be treated as speculative.

A second prediction, **congenital hypotrichosis milia** (score 0.9904), has the same limitation. It is a rare genetic condition, and there is no evidence that blocking mineralocorticoid or androgen receptors would change its course. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0458 | Spironolactone | Not stated | Not stated (registration status: valid) |

## Safety Considerations

- **Contraindications (from knowledge graph, not label text)**: The TxGNN knowledge graph links spironolactone to contraindications in the following conditions:
  - Kidney disease, anuria
  - Hyperkalaemia-related and electrolyte disorders: potassium deficiency disease, hypercalcaemia, nephrocalcinosis, phosphorus metabolism disease
  - Diabetes mellitus, diabetic ketoacidosis
  - Hepatic coma, hepatic encephalopathy
  - Systemic lupus erythematosus (including paediatric)
  - Pancreatitis, pyoureter
  - Gout, hyperuricaemia
  - Hyperparathyroidism, osteitis fibrosa
  - Neonatal jaundice
- **Drug Interactions**: The interaction query returned 100 records; 20 were available for review. Notable examples:
  - **Major**: loperamide
  - **Moderate**: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide, metformin, bupropion, morphine, bisacodyl, castor oil, dronabinol, exenatide, and the SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - **Minor**: doxycycline, acetylsalicylic acid, fidaxomicin

Package insert warnings and contraindications were not available, so please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only support for this prediction is a high model score. There are no clinical trials or publications, and the mechanistic link is speculative because the target conditions are genetic and not primarily androgen-driven. The only Philippines registration has been cancelled, which further limits near-term feasibility.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Published evidence (case reports, case series or trials) of spironolactone in hypotrichosis simplex or related hereditary hair-loss disorders
- Confirmation of whether a valid registration or an alternative supply route exists in the Philippines
- Assessment of route compatibility (oral versus topical) for a hair-loss indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

