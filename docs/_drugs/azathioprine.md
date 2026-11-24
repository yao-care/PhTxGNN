---
layout: default
title: Azathioprine
parent: Model Prediction Only (L5)
nav_order: 35
evidence_level: L5
indication_count: 7
monitor_inn: "Azathioprine"
predicted_indications: ["colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "WHIM syndrome", "granulomatous disease, chronic, autosomal recessive, 5", "osteoarthritis", "granulomatous disease with defect in neutrophil chemotaxis", "acromesomelic dysplasia, Hunter-Thompson type"]
last_modified_at: 2026-11-24
description: "Azathioprine: predicted new indication colobomatous microphthalmia-rhizomelic dysplasia syndrome (evidence level L5). In the Philippines: 1 PNF entry"
---

# Azathioprine
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

## Azathioprine: purine antimetabolite immunosuppressant → colobomatous microphthalmia-rhizomelic dysplasia syndrome
{: .text-alpha }

## One-Sentence Summary

Azathioprine is an immunosuppressive purine antimetabolite.
The TxGNN model predicts it may be effective for **colobomatous microphthalmia-rhizomelic dysplasia syndrome**, but **no clinical trials and no publications** currently support this prediction, and no mechanistic link has been identified.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | colobomatous microphthalmia-rhizomelic dysplasia syndrome |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

ChEMBL (EMBL-EBI) records the mechanism of action of azathioprine as: Amidophosphoribosyltransferase inhibitor; DNA inhibitor ([ChEMBL CHEMBL1542 (azathioprine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1542), CC BY-SA 3.0; accessed 2026-11-19.) Azathioprine is known as an immunosuppressive purine antimetabolite that inhibits purine synthesis in lymphocytes.

Colobomatous microphthalmia-rhizomelic dysplasia syndrome is a rare developmental malformation syndrome affecting the eye and limbs. Immunosuppression through purine synthesis inhibition has no plausible rationale for treating a developmental condition of this kind. The very high TxGNN score (0.99999 before rounding) is not backed by any trial or publication, and likely reflects an artifact of the model rather than a true therapeutic signal. This prediction should be treated as a computational hypothesis only.

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Azathioprine | Oral |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

Safety data compiled for this report contain no package-insert warnings or contraindications; please refer to the package insert for full safety information.

**Drug Interactions** (100 interactions were found in total; main ones listed):
- **Moderate**: mesalazine, balsalazide, olsalazine, sulfasalazine
- **Minor**: zinc acetate, zinc gluconate, zinc sulfate
- Other interactions with an unclassified severity level include epinephrine, amphotericin B, acetylsalicylic acid, calcitriol, pantoprazole, glimepiride, doxycycline, clotrimazole, morphine, metformin, omeprazole, sucralfate and rosiglitazone.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone: there are no clinical trials or publications for this disease, and the biology of a congenital malformation syndrome does not fit an immunosuppressant. Evidence is at level L5.

**To proceed, the following is needed:**
- Any preclinical or mechanistic evidence linking azathioprine to the pathology of this syndrome
- Detailed mechanism of action data
- Package-insert warnings and contraindications from the Philippine regulator
- A safety assessment in the target population, given azathioprine's myelosuppressive and immunosuppressive effects

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not currently available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [ChEMBL CHEMBL1542 (azathioprine): drug mechanism](https://www.ebi.ac.uk/chembl/explore/compound/CHEMBL1542) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

