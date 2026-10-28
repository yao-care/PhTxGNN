---
layout: default
title: Losartan
parent: Model Prediction Only (L5)
nav_order: 213
evidence_level: L5
indication_count: 7
monitor_inn: "Losartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "Prinzmetal angina", "autosomal dominant familial hematuria-retinal arteriolar tortuosity-contractures syndrome", "brain small vessel disease 1 with or without ocular anomalies"]
last_modified_at: 2026-10-27
description: "Losartan: predicted new indication malignant hypertensive renal disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Losartan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Losartan: Angiotensin II receptor blocker → malignant hypertensive renal disease
{: .text-alpha }

## One-Sentence Summary

Losartan is an angiotensin II receptor blocker (AT1 antagonist) used in the Philippines as a single-ingredient product.
The TxGNN model predicts it may be useful for **malignant hypertensive renal disease**, but the data compiled for this report contain **0 clinical trials** and **1 publication** (a preclinical animal model study) for this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9973 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, losartan blocks the angiotensin II type 1 (AT1) receptor.

The one publication found (PMID 30809002) describes angiotensin II and the NF-κB system as drivers of kidney injury in a rat model of malignant hypertensive nephrosclerosis. This makes AT1 receptor blockade mechanistically plausible. However, it is a single animal-model study that does not test losartan in this disease, so it is not direct evidence.

The disease also overlaps closely with hypertension and kidney-protection uses already associated with this drug, so this prediction is not a strong signal of a truly new use.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30809002](https://pubmed.ncbi.nlm.nih.gov/30809002/) | 2019 | Preclinical animal model | Hypertension Research | Angiotensin II and the NF-κB system contribute to kidney injury in a rat model of malignant hypertensive nephrosclerosis (uninephrectomy plus salt overload) |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0296 | Losartan | Not recorded | Not recorded in the local data |

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 recorded interactions. Those listed as Major include **potassium citrate** and **potassium bicarbonate** (risk of raised blood potassium). Many others are rated Moderate, including corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone), SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin), insulins, aspirin and morphine.

Please refer to the package insert for warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high, but no clinical trial exists and the only publication is a preclinical animal study that does not test losartan directly. The disease also largely overlaps with hypertension and kidney uses already linked to this drug, so it adds little as a new use.

**To proceed, the following is needed:**
- Clinical or observational studies of losartan in malignant hypertensive kidney disease
- Mechanism of action data and package insert warnings and contraindications
- Review of the local licence status and the approved indication text
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

