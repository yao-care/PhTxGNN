---
layout: default
title: Calcitriol
parent: Model Prediction Only (L5)
nav_order: 55
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-15
description: "Calcitriol: predicted new indication Obsolete vitamin D deficiency (evidence level L5). Approved use: Hypercalcemia disease, nephrocalcinosis…"
monitor_inn: "Calcitriol"
predicted_indications: ["obsolete vitamin D deficiency", "renal tubular acidosis", "familial isolated hypoparathyroidism due to impaired PTH secretion", "acromesomelic dysplasia, Campailla Martinelli type", "craniofacial conodysplasia", "Dahlberg-Borer-Newcomer syndrome", "hereditary hypophosphatemic rickets"]
---

# Calcitriol
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

# Calcitriol: From Hypercalcemia and Mineral Metabolism Disorders to Vitamin D Deficiency (Obsolete Disease Entry)

## One-Sentence Summary

Calcitriol is the active form of vitamin D. In the knowledge graph it is linked to disorders of calcium and phosphorus metabolism, hypoparathyroidism and renal osteodystrophy.
The TxGNN model predicts it may be effective for **"obsolete vitamin D deficiency"**, but there are **0 clinical trials** and **0 publications** for this prediction. The score reflects model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypercalcemia disease, nephrocalcinosis, phosphorus metabolism disease, hypophosphatemia, hypoparathyroidism, renal osteodystrophy (from the knowledge graph; the local registration lists no indication text) |
| Predicted New Indication | Obsolete vitamin D deficiency |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Calcitriol is the hormonally active form of vitamin D (1,25-dihydroxyvitamin D3). It regulates calcium and phosphate balance, and it is already used in conditions of disturbed mineral metabolism. A biological link to vitamin D deficiency is therefore plausible.

However, the predicted disease entry is flagged as **obsolete** in the disease ontology. There are no trials or publications for it. The very high score most likely reflects closeness between related terms in the knowledge graph, not new clinical evidence. In practice, vitamin D deficiency is usually treated with native vitamin D (cholecalciferol or ergocalciferol), not calcitriol. This prediction should not be read as a new therapeutic opportunity.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0066 | Calcitriol (single-ingredient) | Cancelled |

The record has no dosage form, manufacturer or approved indication text. There is no currently valid calcitriol registration in the Philippines.

## Safety Considerations

- **Disease associations flagged as contraindications in the knowledge graph** (these come from the model's knowledge graph, not from label text): kidney disease, pyoureter, sarcoidosis, hypercalcemia, nephrocalcinosis, phosphorus metabolism disease, nephrolithiasis (including the SLC26A1-related form), acute urate nephropathy, hyperphosphatemia, hypervitaminosis and arteriosclerosis obliterans.
- **Drug Interactions** (100 interactions were recorded; the main ones are listed):
  - **Major:** cholecalciferol, calcifediol (additive vitamin D effects and risk of hypercalcemia) and burosumab.
  - **Moderate:**
    - Thiazide diuretics (hydrochlorothiazide, chlorothiazide, chlorthalidone, bendroflumethiazide, benzthiazide).
    - Enzyme-inducing anticonvulsants and barbiturates (carbamazepine, fosphenytoin, amobarbital, butabarbital, butalbital).
    - Bile acid sequestrants (cholestyramine, colesevelam, colestipol).
    - Digoxin and digitoxin.
    - Aluminum hydroxide.
    - Topical calcipotriol.

For full warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction has no trials or publications behind it (evidence level L5). The target disease entry is obsolete, and calcitriol has no valid registration in the Philippines.
- Among the other predictions compiled for this drug, **hereditary hypophosphatemic rickets** has the strongest support (evidence level L2). It has one completed Early Phase 1 trial (n=16), one Phase 4 dose-comparison trial (n=100, status unknown) and multiple reviews and guidelines. However, calcitriol plus phosphate is already standard therapy there, so it is better viewed as clinical optimization than as new repurposing.

**To proceed, the following is needed:**
- Clarification of the disease mapping, replacing the obsolete entry with a current vitamin D deficiency or related disease term
- Mechanism of action data
- Package insert warnings and contraindications
- Clarification of why the Philippines registration was cancelled and whether a valid registration exists
- If pursuing the better-supported rickets direction: dosing and safety data (nephrocalcinosis, hypercalciuria) and a comparison with burosumab
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

