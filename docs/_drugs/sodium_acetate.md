---
layout: default
title: Sodium Acetate
parent: Model Prediction Only (L5)
nav_order: 314
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
monitor_inn: "Sodium acetate"
predicted_indications: ["congenital prothrombin deficiency", "epiglottitis", "urinary tract infection (disease)", "sclerosing cholangitis", "gonococcal urethritis", "Ureaplasma urethritis", "dyspepsia", "uterine inflammatory disease", "gastroparesis (disease)", "xanthogranulomatous pyelonephritis"]
description: "Sodium Acetate: predicted new indication Congenital prothrombin deficiency (evidence level L5). Approved use: Not recorded in the local data"
---

# Sodium Acetate
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

## Sodium Acetate: Congenital prothrombin deficiency
{: .text-alpha }

## One-Sentence Summary

Sodium acetate is an electrolyte and alkalinizing agent, and no original approved indication is recorded in the Philippines regulatory data compiled for this report.
The TxGNN model predicts it may be effective for **congenital prothrombin deficiency**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
The high score appears to be a TxGNN model (deep learning) artifact rather than a biologically grounded signal.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Congenital prothrombin deficiency |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Sodium acetate is generally understood as an electrolyte and alkalinizing agent: acetate is metabolized to bicarbonate in the body.

No plausible mechanistic link to the predicted indication was identified. Sodium acetate does not affect prothrombin synthesis or coagulation factor II activity. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top-ranked predictions show the same pattern. They include epiglottitis, urinary tract infection, sclerosing cholangitis, Ureaplasma and gonococcal urethritis, dyspepsia, uterine inflammatory disease, gastroparesis and xanthogranulomatous pyelonephritis, all with scores from 0.9946 to 0.9977. None has supporting clinical data for sodium acetate. For dyspepsia and gastroparesis, the retrieved papers mostly use ¹³C-sodium acetate only as a breath-test tracer for measuring gastric emptying, which is not therapeutic evidence.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0447 | Sodium Chloride | Not specified | Not specified (status: valid) |

Its product name is Sodium Chloride, so it may not correspond directly to sodium acetate.

---

## Safety Considerations

- **Disease contraindications from the knowledge graph** (these come from knowledge-graph drug-disease links, not from package insert text): kidney disease, chronic kidney disease, chronic and end-stage renal failure, anuria, nephrolithiasis, nephrocalcinosis, acute urate nephropathy, hypercalcemia, humoral hypercalcemia of malignancy, sarcoidosis, heart disease, cardiovascular disease, atrioventricular block, ventricular fibrillation, digitalis poisoning, hyperkalemic periodic paralysis, hypoaldosteronism, myotonia congenita, phenylketonuria and disorders of phenylalanine metabolism.
- **Drug interactions**: 30 interactions were identified, of which 20 are listed. The listed ones are mostly Moderate or Minor.
  - *Moderate*: tetracyclines (doxycycline, tetracycline, minocycline), salicylates (acetylsalicylic acid, choline salicylate), sympathomimetics and stimulants (ephedrine, pseudoephedrine, amphetamine, dextroamphetamine, benzphetamine) and methenamine.
  - *Minor*: sulfonylureas (chlorpropamide, tolazamide, glipizide, glyburide, acetohexamide, tolbutamide), memantine and methotrexate.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (L5), with no clinical trials or relevant literature, and no plausible mechanism links sodium acetate to prothrombin deficiency. The only Philippines registration is cancelled, so there is no current local product to repurpose. The knowledge-graph contraindications, especially renal and cardiac disease, add further caution.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Mechanism of action data from DrugBank
- Confirmation of the original approved indication and whether the cancelled registration actually corresponds to sodium acetate
- A biologically grounded rationale, or direct preclinical or clinical evidence, for any predicted indication
- Reassessment of the lower-ranked predictions, such as urinary alkalinization in urinary tract infection, if a mechanistic case can be made
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

