---
layout: default
title: Finasteride
parent: 僅模型預測 (L5)
nav_order: 141
evidence_level: L5
indication_count: 6
---

# Finasteride
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Finasteride: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Finasteride is a 5-alpha reductase inhibitor approved globally for treating benign prostatic hyperplasia (BPH) and androgenetic alopecia, though it holds no current Philippines registration.
The TxGNN model ranks **Ambras Type Hypertrichosis Universalis Congenita** as its top predicted new indication, with a near-perfect score of 99.994%.
However, **zero clinical trials and zero publications** support this specific direction — the evidence level is L5 (model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign prostatic hyperplasia (BPH); androgenetic alopecia (globally recognized; no Philippines registration on record) |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.994% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrievable from this Evidence Pack. Based on established pharmacology, Finasteride is a selective, competitive inhibitor of type II 5-alpha reductase — the enzyme responsible for converting testosterone into dihydrotestosterone (DHT), a more potent androgen. By suppressing DHT levels by approximately 65–70% in plasma and prostate tissue, Finasteride interrupts androgen signaling in DHT-dependent tissues, most notably the prostate and androgen-sensitive hair follicles. This is why it is effective in BPH (where DHT drives prostate enlargement) and androgenetic alopecia (where DHT miniaturizes hair follicles in genetically predisposed individuals).

Ambras Syndrome (Hypertrichosis Universalis Congenita, Ambras type), however, is a fundamentally different biological entity. It results from chromosomal rearrangements at 8q22–q24, leading to near-universal hair overgrowth regardless of androgen status. The pathological mechanism is structural and genetic — not androgen-dependent — meaning that suppressing DHT has no theoretical basis for correcting the underlying follicular dysregulation. Unlike androgenetic alopecia, where DHT is the causal driver, Ambras syndrome hair follicles are not responding to androgen excess or hypersensitivity.

The near-perfect TxGNN score (99.994%) almost certainly reflects a **graph proximity artifact**: Finasteride and Ambras syndrome share "hair follicle" and "hair growth" nodes within the knowledge graph, creating a spuriously high association score despite the absence of mechanistic plausibility. This pattern — high model score, zero supporting evidence, weak mechanistic link — is the hallmark of a false positive in graph-based drug repurposing and warrants a Hold decision rather than further investment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Finasteride holds **no current product authorizations** with the Food and Drug Administration of the Philippines (FDA Philippines). No registered licenses, brand names, or approved indications are on record as of the data cutoff date (2026-04-05).

This is a significant regulatory gap: any future clinical development or marketing application in the Philippines would need to begin from a pre-registration baseline.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Note on data gaps**: This Evidence Pack was generated with two blocking gaps — the Philippines FDA package insert (including warnings and contraindications) and the formal DrugBank mechanism of action record — were not retrieved. A complete safety review cannot be performed until these are resolved. Known class-level safety signals for 5-alpha reductase inhibitors (e.g., sexual dysfunction, teratogenicity in male fetuses, potential mood effects) should be reviewed from the originator label before any clinical consideration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's top-ranked prediction for Finasteride — Ambras Type Hypertrichosis Universalis Congenita — is almost certainly a knowledge graph artifact driven by shared hair-follicle nodes, not a genuine therapeutic signal. The condition is caused by chromosomal rearrangement (8q22–q24), which is structurally and mechanistically incompatible with Finasteride's DHT-suppression mechanism. No clinical trial, published case report, or preclinical study supports this repurposing direction, placing it squarely at evidence level L5.

**To proceed, the following is needed:**

- **Mechanistic justification**: A credible biological hypothesis explaining how DHT reduction could modify a chromosomally-driven hair disorder — none currently exists
- **Any supporting evidence**: At minimum, a published case report or in vitro study demonstrating activity in Ambras syndrome or a closely related model
- **Philippines regulatory pathway**: Finasteride is not registered in the Philippines; a baseline registration (likely for BPH or alopecia) would need to be established before any new indication could be pursued
- **Safety data package**: Retrieve the TFDA or FDA Philippines package insert to complete the warnings, contraindications, and drug interaction review (currently blocking safety assessment)
- **Reassessment of lower-ranked predictions**: Rank 2 (Hypertrichosis, general) has marginally more mechanistic plausibility and some indirect literature, though still rated Hold — this may be a more productive starting point if the hair-loss repurposing angle is of interest
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

