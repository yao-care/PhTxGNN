---
layout: default
title: Flucytosine
parent: Model Prediction Only (L5)
nav_order: 145
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Flucytosine: predicted new indication bone Paget disease (evidence level L5). Approved use: Not stated in the Philippines registration data"
---

# Flucytosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Flucytosine: From Fungal Infection to Bone Paget Disease

## One-Sentence Summary

Flucytosine is an antifungal prodrug. Fungal cytosine deaminase converts it to 5-fluorouracil, which interferes with fungal RNA and DNA synthesis.
The TxGNN model predicts it may be effective for **bone Paget disease**, but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Philippines registration data |
| Predicted New Indication | bone Paget disease |
| TxGNN Prediction Score | 99.04% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, flucytosine is an antifungal prodrug: fungal cytosine deaminase converts it to 5-fluorouracil (5-FU), which disrupts fungal RNA and DNA synthesis.

Paget disease of bone is a disorder of excessive, disorganized osteoclast-driven bone remodelling. SQSTM1 mutations and possibly viral contributions have been proposed in its development. No direct link between flucytosine's mechanism and this process can be established from the available data. The high score may reflect indirect knowledge-graph associations, such as shared neighbours among 5-FU or other pyrimidine analogues, rather than biological plausibility.

Bisphosphonates are already well-established treatment for Paget disease, so the unmet need for a repurposed agent is low. Flucytosine's toxicity (bone marrow suppression, hepatotoxicity, and accumulation in kidney impairment) and its 85 recorded drug interactions also weigh against repurposing without supporting evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0193 | Flucytosine | Not stated | Not stated (status: cancelled) |

The only registration is cancelled, so there is currently no valid marketed product in the Philippines.

## Safety Considerations

- **Disease associations flagged in the knowledge graph** (derived from drug-disease contraindication edges, not from package insert text): kidney disease, liver disease, gallbladder disease, pyoureter, potassium deficiency disease, thrombocytopenia, leukopenia, agranulocytosis, neutropenia (including several congenital and constitutional forms), and aplastic anaemia. The pattern points mainly to bone marrow suppression, liver injury and renal impairment.
- **Drug Interactions**: 85 interactions were recorded. Examples:
  - **Major**: Deferiprone
  - **Moderate**: Amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms), aminoglycosides (kanamycin, neomycin, streptomycin), vancomycin, polymyxin B, bacitracin, pentamidine, ibuprofen, deferasirox, mesalazine, balsalazide, olsalazine, sulfasalazine, iobenguane (I-131), and strontium-89 chloride

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no clinical trials or publications, and no mechanistic link to Paget disease can be supported. Established alternatives exist, the drug has significant toxicity, and its only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data (e.g. from DrugBank) and a plausible biological link to Paget disease pathophysiology
- Preclinical or other supporting evidence for bone Paget disease
- Package insert warnings and contraindications from DOH-FDA Philippines
- Clarification of the original approved indication and of the cancelled registration status
- A risk-benefit assessment against bisphosphonates, including a marrow, liver and renal monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

