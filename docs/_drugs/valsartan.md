---
layout: default
title: Valsartan
parent: Moderate Evidence (L3-L4)
nav_order: 350
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-15
description: "Valsartan: predicted new indication Malignant hypertensive renal disease (evidence level L4). Approved use: Hypertension (hypertensive disorder)"
---

# Valsartan
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

# Valsartan: From Hypertension to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Valsartan is an angiotensin II receptor blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease** (score 99.97%),
but **no clinical trials** and only **1 indirect preclinical publication** (which does not test valsartan) currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L4 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, valsartan is an angiotensin II type 1 (AT1) receptor blocker. Its efficacy in hypertension is established, and mechanistically it may protect the kidney in severe hypertension through blockade of the renin-angiotensin-aldosterone system (RAAS).

The predicted indication is closely related to the original one. Malignant hypertensive renal disease is kidney damage caused by severe hypertension, so this prediction sits near the labeled use rather than representing a true repurposing signal. The very high TxGNN score is a computational result and does not replace clinical data.

Other predictions from the model are weaker still:
- **Malignant renovascular hypertension** (score 99.97%): strongly angiotensin II-driven, and an animal study (PMID 11560862) shows AT1 blockade prevents lethal malignant hypertension. It is preclinical and it is unclear whether valsartan itself was tested. ARBs also carry a risk of acute kidney injury in bilateral renal artery stenosis.
- **Pulmonary hypertension (two categories)**, **chronic pulmonary heart disease**, **Braddock syndrome** and **Prinzmetal angina**: evidence is model prediction or indirect literature (mostly sacubitril/valsartan, heart failure, or unrelated topics). These are not supported for valsartan alone.

## Clinical Trial Evidence

Currently no related clinical trials registered for the lead prediction, malignant hypertensive renal disease.

For the lower-ranked prediction chronic pulmonary heart disease, one trial was retrieved, but it does not appear to test valsartan:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Exercise and rehabilitation study of vascular function in hypertension; not a valsartan study (relevance grade C) |

## Literature Evidence

For the lead prediction, only one paper was retrieved, and it concerns a different drug:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Preclinical | Pharmacological Research | Avosentan (an endothelin antagonist, not valsartan) protected against hypertensive nephropathy in transgenic rats at doses that did not cause fluid retention |

Selected supporting papers for the second prediction (malignant renovascular hypertension) and other predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11560862](https://pubmed.ncbi.nlm.nih.gov/11560862/) | 2001 | Preclinical (animal) | Circulation | AT1 receptor blockade prevented lethal malignant hypertension, related to kidney inflammation |
| [32552157](https://pubmed.ncbi.nlm.nih.gov/32552157/) | 2020 | Preclinical (animal) | J Am Heart Assoc | Sacubitril/valsartan attenuated right ventricular remodeling in pulmonary hypertension |
| [22377232](https://pubmed.ncbi.nlm.nih.gov/22377232/) | 2012 | Preclinical (animal) | Diabetes Res Clin Pract | Valsartan inhibited the HIF-1α pathway and reduced renal interstitial fibrosis in diabetic rats |
| [34796742](https://pubmed.ncbi.nlm.nih.gov/34796742/) | 2021 | Post hoc RCT analysis | J Am Heart Assoc | Impact of COPD on outcomes in HFpEF patients in PARAGON-HF (sacubitril/valsartan trial) |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0507 | Valsartan | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindications (from the TxGNN knowledge graph, not label text)**: The graph lists, among others, angioedema (including hereditary and RAAS-blocker-induced), liver failure and liver disease, pancreatitis, gallbladder disease, hepatic encephalopathy, anuria, impaired renal function, renal artery obstruction, hypotensive disorder, diabetes mellitus and diabetic ketoacidosis, gout, neutropenia and agranulocytosis, systemic lupus erythematosus, hypercalcemia, hyperparathyroidism, and potassium deficiency.
- **Drug Interactions** (100 interactions found; main ones shown):
  - **Major**: potassium chloride, potassium bicarbonate (risk of hyperkalaemia)
  - **Moderate**: many insulin products, exenatide, hydrocortisone, eluxadoline, polyethylene glycol with electrolytes
- **Indication-specific concern**: ARBs carry a risk of acute kidney injury in bilateral renal artery stenosis, which is relevant for renovascular hypertension.

Please refer to the package insert for further safety information, as label warnings were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction is supported only by a model score and one indirect preclinical paper on a different drug, with no clinical trials (L4). It is also close to valsartan's existing hypertension indication. In addition, valsartan currently has no valid registration in the Philippines (its only record is cancelled), and label safety data are unavailable.

**To proceed, the following is needed:**
- Valsartan-specific clinical or preclinical evidence in malignant hypertensive renal disease
- Confirmation of the current Philippines registration status and a valid product registration
- Package insert warnings and contraindications from DOH-FDA Philippines
- Mechanism of action data (e.g., from DrugBank)
- Renal safety assessment (renal artery stenosis, hyperkalaemia, impaired renal function) for severe hypertension with kidney involvement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

