---
layout: default
title: Salicylic Acid
parent: Model Prediction Only (L5)
nav_order: 306
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Salicylic Acid: predicted new indication Papillary conjunctivitis (evidence level L5). Approved use: Tinea pedis, synovitis, tenosynovitis, rheumatoid arthritis…"
monitor_inn: "Salicylic acid"
predicted_indications: ["papillary conjunctivitis", "colobomatous microphthalmia-rhizomelic dysplasia syndrome", "brachydactyly-syndactyly syndrome", "brachyolmia-amelogenesis imperfecta syndrome", "rosacea conjunctivitis", "acromesomelic dysplasia, Hunter-Thompson type", "pseudoachondroplasia", "myosclerosis", "brachyolmia", "spondyloarthropathy, susceptibility to"]
---

# Salicylic Acid
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

# Salicylic Acid: From Superficial Skin and Inflammatory Conditions to Papillary Conjunctivitis

## One-Sentence Summary

Salicylic acid is a long-established keratolytic and anti-inflammatory agent, used for conditions such as acne, tinea infections, seborrheic dermatitis, rheumatoid arthritis and allergic rhinitis.
The TxGNN model predicts it may be effective for **papillary conjunctivitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on computational prediction alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Tinea pedis, synovitis, tenosynovitis, rheumatoid arthritis, allergic rhinitis, acne, seborrheic dermatitis and others (from the knowledge graph; no approved indication text in the Philippines registration) |
| Predicted New Indication | Papillary conjunctivitis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on known information, salicylic acid has keratolytic, anti-inflammatory and antimicrobial properties. It is proposed to act through COX inhibition, but no public bioactivity data confirm this at a specific target. Its pharmacology record lists ASIC3 as a related target.

Salicylic acid is already used in allergic and inflammatory conditions such as allergic rhinitis, and in inflammatory skin conditions. Papillary conjunctivitis is an allergic or inflammatory disease of the ocular surface, so there is a loose conceptual link.

This link is speculative. No clinical or literature evidence supports it, and applying salicylic acid directly to the eye carries a real risk of irritation or corneal injury. The high score is a computational result only.

**Other top-ranked predictions** (all L5, all Hold):

| Rank | Predicted Disease | Score | Assessment |
|---|---|---|---|
| 2 | Colobomatous microphthalmia-rhizomelic dysplasia syndrome | 99.78% | No plausible mechanistic link; developmental genetic disorder |
| 3 | Brachydactyly-syndactyly syndrome | 99.73% | No plausible link; likely a graph artifact |
| 4 | Brachyolmia-amelogenesis imperfecta syndrome | 99.55% | No plausible link |
| 5 | Rosacea conjunctivitis | 99.53% | Weak, indirect link via inflammatory skin disease; speculative, with ocular safety concerns |
| 6 | Acromesomelic dysplasia, Hunter-Thompson type | 99.52% | No plausible link |
| 7 | Pseudoachondroplasia | 99.51% | No plausible link; at most tangential joint pain relevance |
| 8 | Myosclerosis | 99.49% | Weak, loose thematic link to musculoskeletal inflammation |
| 9 | Brachyolmia | 99.44% | No plausible link |
| 10 | Spondyloarthropathy, susceptibility to | 99.34% | Moderate class-level plausibility (NSAID-type symptom relief); no salicylic acid-specific evidence |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0434 | Salicylic Acid | Not specified | Not specified (status: cancelled) |

## Safety Considerations

Please refer to the package insert for safety information.

One item with data: the pharmacology record lists ASIC3 as an interacting target of salicylic acid. This is a target-level association rather than a drug-drug interaction with a graded severity. Direct ocular application raises a theoretical risk of irritation or corneal injury, as noted in the mechanistic assessment.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for papillary conjunctivitis has no supporting clinical trials or literature (evidence level L5). The only Philippines registration is cancelled, and the mechanistic link is speculative with ocular safety concerns. Most other top predictions are rare genetic disorders with no plausible biological link.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Philippines regulator (currently missing, and blocking safety screening)
- Mechanism of action data (for example, from DrugBank)
- Preclinical or literature evidence on salicylic acid in allergic or inflammatory ocular surface disease
- Ocular tolerability and safety assessment, plus a feasible ophthalmic formulation and route
- Clarification of the market status, since the only registration is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

