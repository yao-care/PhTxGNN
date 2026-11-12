---
layout: default
title: Chlorambucil
parent: Model Prediction Only (L5)
nav_order: 71
evidence_level: L5
indication_count: 5
monitor_inn: "Chlorambucil"
predicted_indications: ["ALK-positive large B-cell lymphoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "small cell lung carcinoma"]
last_modified_at: 2026-11-12
description: "Chlorambucil: predicted new indication ALK-positive large B-cell lymphoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Chlorambucil
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

## Chlorambucil: ALK-positive large B-cell lymphoma
{: .text-alpha }

## One-Sentence Summary

Chlorambucil is an alkylating anticancer drug.
The TxGNN model's top prediction is **CLL/SLL with somatic hypermutation of the immunoglobulin heavy chain variable-region gene (IGHV)**, with a very high score. **No clinical trials and no publications** directly study this subtype, so the prediction rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | ALK-positive large B-cell lymphoma |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, chlorambucil is an alkylating agent that cross-links DNA and damages rapidly dividing cancer cells.

The TxGNN model (deep learning) scores chlorambucil against other mature B-cell neoplasms. CLL/SLL is a closely related B-cell malignancy, and the IGHV-mutated form is a molecular subset of it. The high score therefore comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. No trial or publication was found for the subtype itself, so the plausibility is mechanistic and indirect only.

Other predictions in the list are weaker or off-target. The pre-germinal-center CLL/SLL subtype has only one 2003 narrative review, which gives no subtype-specific efficacy data. Primary pulmonary lymphoma has the most literature, mainly case reports, cohorts and guidelines, but it is a different disease from the top-ranked prediction.

## Clinical Trial Evidence

Currently no related clinical trials registered for the predicted disease.

## Literature Evidence

Currently no related literature available for the predicted disease.

Literature exists only for lower-ranked predictions (for example, primary pulmonary lymphoma and small cell lung carcinoma). This is mostly case reports, old phase II studies and preclinical work, and it does not address the top-ranked indication.

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Chlorambucil | Oral |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High. The knowledge graph lists neutropenia, thrombocytopenia, leukopenia, anemia and agranulocytosis as contraindication-type relations. |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Complete blood count with differential, liver function, renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph lists the following as contraindication-type relations. These are not confirmed by Philippine label text.
  - Blood-related conditions: thrombocytopenia, neutropenia, agranulocytosis, leukopenia, lymphopenia, anemia, acute leukemias
  - Organ-related conditions: interstitial lung disease, pulmonary fibrosis, drug-induced liver injury, nephrotic syndrome, epilepsy
- **Drug Interactions:** 100 interactions were found. Examples of those rated **Major** are deferiprone and samarium (153Sm) lexidronam. **Moderate** examples are amphotericin B (several formulations), mercaptopurine, roflumilast, chloramphenicol, palifermin and strontium-89 chloride. Several others (such as warfarin, prednisone and omeprazole) have an unknown severity rating.
- **Other safety signals in the literature:** Second malignancies after Hodgkin disease treatment, and dose-limiting central nervous system toxicity (seizures) at high doses.

Package insert warnings and contraindications for the Philippine product are not available. Please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score for IGHV-mutated CLL/SLL is not backed by any trial or publication on this subtype, so the evidence level is L5. Chlorambucil carries significant myelosuppression risk.

<!-- review:begin ph-lic-20261106-chlorambucil-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Chlorambucil carries significant myelosuppression risk, and the Philippine licence record has no indication or safety text." Removed: it conflicted with the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-chlorambucil-1 -->

**To proceed, the following is needed:**
- Subtype-specific clinical data on chlorambucil in IGHV-mutated CLL/SLL, including comparison with current standard therapies
- Detailed mechanism of action data
- Philippine package insert with approved indication, warnings and contraindications
- A safety monitoring plan covering blood counts and the interaction risks identified above

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "and the Philippine licence record has no indication or safety text" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

