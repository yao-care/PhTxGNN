---
layout: default
title: Ioversol
parent: Model Prediction Only (L5)
nav_order: 181
evidence_level: L5
indication_count: 9
monitor_inn: "Ioversol"
predicted_indications: ["osteoarthritis", "rheumatoid arthritis", "brachyolmia", "hemoglobinopathy", "brachyolmia-amelogenesis imperfecta syndrome", "acromesomelic dysplasia, Hunter-Thompson type", "myosclerosis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "alopecia"]
last_modified_at: 2026-10-30
description: "Ioversol: predicted new indication Osteoarthritis (evidence level L5). Approved use: Not stated in the local registration record"
---

# Ioversol
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

## Ioversol: From an Iodinated Contrast Agent to Osteoarthritis
{: .text-alpha }

## One-Sentence Summary

Ioversol is an iodinated, water-soluble contrast agent used in diagnostic imaging, and it is registered in the Philippines.
The TxGNN model predicts it may be useful for **osteoarthritis**, but there are **0 clinical trials** and **1 publication** in the data compiled for this report, and that publication does not study ioversol as a treatment.
This prediction is a model output without supporting clinical evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the local registration record |
| Predicted New Indication | Osteoarthritis |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Ioversol is a water-soluble iodinated contrast agent. It is used to make blood vessels and tissues visible on X-ray imaging, and it has no known anti-inflammatory or cartilage-protecting activity.

The only linked publication (PMID 38102013, the LipioJoint-1 trial) tested genicular artery embolization for knee osteoarthritis using an ethiodized-oil (Lipiodol) embolic agent. Ioversol was not the therapeutic agent in that study. At most, a contrast agent may be used to visualize the arteries during such a procedure. That is an imaging role, not a treatment effect, and it is not a repurposing signal.

The high TxGNN score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The other predicted diseases (rheumatoid arthritis, brachyolmia, hemoglobinopathy, alopecia and several rare skeletal dysplasias) also have no mechanistic link to ioversol, and none has any supporting clinical trial.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38102013](https://pubmed.ncbi.nlm.nih.gov/38102013/) | 2024 | Single-arm prospective clinical trial | Diagnostic and Interventional Imaging | Assessed the safety and efficacy of transient genicular artery embolization with an ethiodized-oil emulsion for knee osteoarthritis. Ioversol was not the therapeutic agent. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0258 | Ioversol | Not stated | Not stated |

## Safety Considerations

- **Drug Interactions**: The interaction database returned 100 records. The first 20 reviewed include these:
  - **Major**: metformin, amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), mesalazine, balsalazide, olsalazine, sulfasalazine, vancomycin, kanamycin, neomycin, streptomycin and polymyxin B.
  - **Moderate**: mannitol.
  - **Unknown severity**: atropine, famotidine, acetylsalicylic acid, morphine and omeprazole.

  Many of the major interactions involve nephrotoxic drugs or metformin. These should be interpreted with the product's package insert.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only cited study concerns a different embolic agent used for knee osteoarthritis, not ioversol. No clinical trial directly studies ioversol for this disease, and no pharmacological mechanism supports the prediction. The evidence level is therefore L5, based on model prediction alone.

**To proceed, the following is needed:**
- Mechanism of action data for ioversol, and any biological rationale for osteoarthritis
- Direct preclinical or clinical studies of ioversol in osteoarthritis
- Approved indication text and package insert (warnings and contraindications) for the Philippines registration PNF-0258
- Evaluation of route and formulation compatibility, since it is unclear whether an intravascular contrast agent could be given for a joint disease
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

