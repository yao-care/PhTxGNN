---
layout: default
title: Iopromide
parent: Model Prediction Only (L5)
nav_order: 180
evidence_level: L5
indication_count: 9
monitor_inn: "Iopromide"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "acromesomelic dysplasia, Hunter-Thompson type", "brachyolmia-amelogenesis imperfecta syndrome", "alopecia", "myosclerosis", "hemoglobinopathy", "pseudoachondroplasia"]
last_modified_at: 2026-10-30
description: "Iopromide: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not stated in the Philippines licence record"
---

# Iopromide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Iopromide: From Radiographic Contrast Imaging to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Iopromide is an iodinated, non-ionic radiographic contrast agent, and it has one registration in the Philippines.
The TxGNN model predicts it may be effective for **osteoarthritis**, but **no clinical trials and no publications** were found to support this prediction.
The prediction rests on a TxGNN model (deep learning) score alone, so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Philippines licence record (the contrast-agent use comes from the drug class, not from licence text) |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9953 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

At present, detailed mechanism of action data is not available. Iopromide belongs to the class of iodinated, non-ionic contrast agents. These agents make tissues visible on X-ray and CT imaging. They are not known to have any anti-inflammatory or cartilage-protecting activity.

No mechanistic link to osteoarthritis has been established. The high score (0.9953) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. It does not reflect pharmacological activity.

The other predicted conditions are rheumatoid arthritis, several rare skeletal dysplasias (brachyolmia, acromesomelic dysplasia Hunter-Thompson type, pseudoachondroplasia), alopecia, myosclerosis and hemoglobinopathy. All of them also have scores ≥ 0.99. None has any trial, publication or plausible mechanism. This suggests the scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence or real therapeutic potential.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0256 | Iopromide | Not stated | Not stated |

This is a single-ingredient product with valid status.

## Safety Considerations

- **Drug Interactions**: The data compiled for this report list 100 interacting drugs in total (20 shown). Most of the listed ones are rated Major. Examples:
  - Metformin
  - Amphotericin B, including its lipid complex, cholesteryl sulfate and liposomal forms
  - Vancomycin
  - Aminoglycosides (kanamycin, neomycin, streptomycin)
  - Polymyxin B
  - Aminosalicylates (mesalazine, balsalazide, olsalazine, sulfasalazine)
  - Mannitol is rated Moderate.
  - Clotrimazole, acetylsalicylic acid, bupropion, dexamethasone and pantoprazole have an unknown severity level.

  Several of the Major interactions involve drugs that can affect the kidneys, so renal function deserves attention. This is a general observation and not a statement from the data.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or publication studies iopromide in osteoarthritis or in any other predicted disease. There is also no plausible mechanism, since iopromide is a diagnostic contrast agent. The evidence is limited to a model score, which places it at level L5.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- Package insert warnings and contraindications from the Philippines FDA, which are currently missing and block safety screening
- Dosage form and approved indication details for licence PNF-0256
- Preclinical or mechanistic studies of iopromide in joint or cartilage models before any clinical consideration
- A check on whether the predictions reflect similarities the TxGNN model (deep learning) learned between related diseases rather than therapeutic effects
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

