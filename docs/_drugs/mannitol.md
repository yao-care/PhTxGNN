---
layout: default
title: Mannitol
parent: Model Prediction Only (L5)
nav_order: 215
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Mannitol: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Brain edema, intracranial hypertension, ocular hypertension…"
monitor_inn: "Mannitol"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "acute pulmonary heart disease", "exercise-induced malignant hyperthermia", "malignant hyperthermia, susceptibility to", "familial periodic paralysis", "hypokalemic periodic paralysis", "congenital multicore myopathy with external ophthalmoplegia", "moderate multiminicore disease with hand involvement", "nephrogenic diabetes insipidus", "central core myopathy"]
---

# Mannitol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Mannitol: From Intracranial and Ocular Pressure Reduction to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Mannitol is an osmotic agent, originally used for conditions such as brain edema, intracranial hypertension, ocular hypertension and congestive heart failure.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis**,
but there are **0 clinical trials** and only **1 general review** behind this prediction, so it is a model prediction without direct supporting evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Brain edema, intracranial hypertension, ocular hypertension, pseudotumor cerebri, congestive heart failure, cystic fibrosis (the Philippines registration has no indication text) |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, mannitol is an osmotic agent that draws water into the vascular and renal tubular compartments. It is used for conditions where fluid shifts need to be controlled, such as brain edema and raised intracranial or intraocular pressure. In theory, osmotic diuresis could promote free-water excretion.

That theoretical link is weak here. Nephrogenic SIAD is caused by gain-of-function variants in the vasopressin V2 receptor, so the defect sits in the receptor signalling and osmotic diuresis would not correct it. The only retrieved paper is a general review of pitfalls in evaluating hyponatremia. It says nothing about mannitol in this condition. The high TxGNN score is therefore a model output only and should not be read as clinical support.

Other top-ranked predictions are also weak. Most are supportive or indirect associations, and several are mechanistically implausible:
- **Nephrogenic diabetes insipidus** (score 99.70%): osmotic diuresis would likely worsen polyuria and free-water loss, so the prediction is potentially harmful.
- **Malignant hyperthermia, central core myopathy and related myopathies**: the links appear to come from RYR1-related network proximity, and mannitol is a vehicle component of dantrolene formulations. It has no known action on the underlying calcium dysregulation.
- **Hypokalemic periodic paralysis**: mannitol serves as a glucose-free solvent for IV potassium. This is a supportive formulation choice, not disease-modifying treatment.
- **Acute pulmonary heart disease**: only indirect, dated literature exists, and mannitol can transiently expand intravascular volume, which may worsen right heart strain.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26706473](https://pubmed.ncbi.nlm.nih.gov/26706473/) | 2016 | Review | European Journal of Internal Medicine | Describes common pitfalls in evaluating patients with hyponatremia, a condition where wrong diagnosis or treatment can cause serious harm. It does not address mannitol or nephrogenic SIAD treatment. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0299 | Mannitol | Not specified | Not specified (registration status: cancelled) |

## Safety Considerations

The following comes from knowledge-graph disease associations, not from package insert text, and should be confirmed against the official label.

- **Possible contraindicated conditions (knowledge graph)**: anuria, impaired renal function, pulmonary edema, intracranial hemorrhage, liver failure and liver disease, hepatic coma and hepatic encephalopathy, porphyria, thrombocytopenia, neutropenia, agranulocytosis, anemia, and sleep apnea syndromes, among others.
- **Drug interactions**: 100 interactions were identified. Examples include:
  - **Major**: amikacin.
  - **Moderate**: lamivudine, formoterol, salbutamol, arformoterol, benazepril, captopril, carbamazepine, citalopram, canagliflozin, dapagliflozin, desvenlafaxine, cisatracurium, amifostine, bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes, iothalamic acid and diatrizoate.
  - **Minor**: doxycycline.
- Concerns specific to the predicted indication: osmotic diuresis could worsen free-water loss in nephrogenic diabetes insipidus, and volume expansion could strain the right heart in acute pulmonary heart disease.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no clinical trials, the only paper is a general hyponatremia review, and the proposed mechanism does not fit the V2-receptor gain-of-function defect. The Philippines registration is also cancelled, so there is no active local product.

**To proceed, the following is needed:**
- Mechanism of action data for mannitol, to allow a proper mechanistic analysis.
- Package insert warnings and contraindications from the DOH-FDA Philippines, which are required before any safety screening.
- Preclinical or case-level evidence of mannitol's effect in nephrogenic SIAD, or a clear rationale for why osmotic diuresis would help.
- Confirmation of whether any valid mannitol registration or product exists in the Philippines, along with its approved indication and dosage form.
- If the team wants to pursue other predictions, prioritise those with a plausible supportive role (such as hypokalemic periodic paralysis as an IV vehicle) and frame them as formulation questions rather than repurposing of a therapeutic effect.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

