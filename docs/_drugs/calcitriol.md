---
layout: default
title: Calcitriol
parent: Model Prediction Only (L5)
nav_order: 55
evidence_level: L5
indication_count: 5
monitor_inn: "Calcitriol"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "hereditary hypophosphatemic rickets"]
last_modified_at: 2026-10-27
description: "Calcitriol: predicted new indication obsolete vitamin D deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Calcitriol
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

## Calcitriol: active vitamin D hormone analogue → obsolete vitamin D deficiency
{: .text-alpha }

## One-Sentence Summary

Calcitriol is the active form of vitamin D (1,25-dihydroxyvitamin D3) and is used mainly in disorders of calcium and phosphate metabolism.
The TxGNN model predicts it may be effective for **obsolete vitamin D deficiency**, but **no clinical trials and no publications** in the compiled data directly support this prediction.
The result is a model prediction only and should be treated as a hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | obsolete vitamin D deficiency |
| TxGNN Prediction Score | 0.9996 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, calcitriol is the hormonally active metabolite of vitamin D, so a biological link to vitamin D deficiency is plausible.

However, the disease entry is flagged as obsolete in the ontology, and there are no trials or literature for it. The high score most likely reflects the closeness of the terms in the model's network rather than new evidence. In practice, vitamin D deficiency is usually corrected with native vitamin D (cholecalciferol or ergocalciferol), not with the already-activated hormone, so a real clinical role for calcitriol here is uncertain.

## Philippines Market Information

Local data show one registration (PNF-0066, Calcitriol, single-ingredient). The record is listed with a status of cancelled, and no dosage form or approved indication text is recorded. The overall market status in the local data is "Marketed".

## Safety Considerations

- **Drug Interactions** (100 interactions recorded; main ones shown):
  - **Major:** cholecalciferol, calcifediol, burosumab (additive vitamin D effects, or opposing effects on phosphate handling).
  - **Moderate:** thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone, bendroflumethiazide, benzthiazide), enzyme-inducing anticonvulsants and barbiturates (carbamazepine, fosphenytoin, amobarbital, butabarbital, butalbital), bile-acid sequestrants (cholestyramine, colesevelam, colestipol), aluminum hydroxide, topical calcipotriol, and digoxin/digitoxin.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported by no clinical trials and no publications, so the evidence level is L5. The disease entry is also obsolete, and standard care for vitamin D deficiency already relies on native vitamin D.

**To proceed, the following is needed:**
- Clarify which current disease term replaces the obsolete entry, and whether calcitriol has any role beyond native vitamin D
- Detailed mechanism of action data
- Package insert warnings and contraindications from the Philippine regulator
- Clinical or literature evidence that directly studies calcitriol in this condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

