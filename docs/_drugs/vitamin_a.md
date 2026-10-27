---
layout: default
title: Vitamin A
parent: Model Prediction Only (L5)
nav_order: 358
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Vitamin A: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Vitamin deficiency disorder"
monitor_inn: "Vitamin A"
predicted_indications: ["congenital prothrombin deficiency", "biotin metabolic disease", "non-syndromic esophageal malformation", "injury", "cell proliferation disorder", "florid cemento-osseous dysplasia", "perinatal disease", "segmental odontomaxillary dysplasia", "disease by subcellular system affected", "radiation or chemically induced disorder"]
---

# Vitamin A
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

## Vitamin A: From Vitamin A Deficiency to Congenital Prothrombin Deficiency
{: .text-alpha }

## One-Sentence Summary

Vitamin A is a fat-soluble vitamin originally used to treat vitamin deficiency disorders, including vitamin A deficiency.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but **no clinical trials and no publications** currently support this prediction, so it is a model-only signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin deficiency disorder; vitamin A deficiency |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Vitamin A (retinol) is an essential nutrient. Its efficacy in correcting vitamin A deficiency is well established. Its active metabolite, retinoic acid, signals through nuclear receptors and regulates gene expression.

The TxGNN score is very high (99.97%), but it is a graph-based association only. The prediction is hard to justify mechanistically:

- Prothrombin (factor II) synthesis depends on vitamin K-dependent gamma-carboxylation. Vitamin A has no established role in this pathway.
- Congenital prothrombin deficiency is a genetic (F2) defect. A vitamin supplement is not expected to correct it.

The high score should therefore be treated as a hypothesis-generating signal, not a therapeutic rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0516 | Vitamin A | Cancelled |

The only registration is a single-ingredient product that has been cancelled. No dosage form or approved indication text is on record.

---

## Safety Considerations

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for safety information.

- **Knowledge-graph contraindication signals** (from a drug-disease graph, not label text): kidney disease, liver disease, gallbladder disease, peptic ulcer disease, sarcoidosis, hypercalcemia, nephrocalcinosis, nephrolithiasis, sickle cell anemia, hemolytic anemia, hereditary hemochromatosis and other iron metabolism disorders, Wilson disease, primary hyperoxaluria, hyperphosphatemia, inflammatory bowel disease and ulcerative colitis, gastroenteritis, hypervitaminosis, and arteriosclerosis obliterans.
- **Drug interactions:** 68 interactions were identified in total. The main ones are:
  - **Major:** other retinoids (isotretinoin, acitretin, tretinoin) and tetracycline-class antibiotics (tetracycline, doxycycline, minocycline, oxytetracycline, demeclocycline, omadacycline, eravacycline, sarecycline).
  - **Moderate:** bexarotene, bile acid sequestrants (cholestyramine, colesevelam, colestipol), sevelamer, and selpercatinib.
  - **Minor:** orlistat.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a model score. No trials or publications support it, and there is no plausible mechanistic link to the vitamin K-dependent prothrombin pathway. The only Philippine registration is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological hypothesis linking vitamin A to prothrombin deficiency
- Package insert warnings and contraindications for safety screening
- Any preclinical or clinical signal in prothrombin deficiency
- Confirmation of whether a valid vitamin A product is available in the Philippines

**Note on other predictions for this drug:**
Two lower-ranked predictions have more supporting evidence and may deserve a separate review:
- **Perinatal disease (score 99.63%):** The evidence level is L1. Multiple Cochrane meta-analyses of vitamin A supplementation in very low birth weight infants support it, for reducing bronchopulmonary dysplasia and related morbidity. The benefit is modest, and dose and route matter. A large malaria-in-pregnancy trial (NCT01115478) also exists but is a different perinatal setting. This is the strongest candidate (Proceed with Guardrails).
- **Injury (score 99.69%):** The evidence level is L2. Reviews on wound healing support it, and two neonatal trials (NCT02102711, NCT01203488) address lung injury in preterm infants. Safety signals include bone fracture risk and liver toxicity at high doses.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

