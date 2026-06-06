---
layout: default
title: Tramadol
parent: 僅模型預測 (L5)
nav_order: 338
evidence_level: L5
indication_count: 10
---

# Tramadol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Tramadol: From Pain Management to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Tramadol is a centrally-acting analgesic widely used for managing moderate to moderately severe pain, operating via dual mechanisms of μ-opioid receptor agonism and monoamine reuptake inhibition.
The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type**, a rare congenital skeletal disorder caused by CDMP1/GDF5 gene mutations.
Currently, there are **no clinical trials** and **no publications** directly supporting this repurposing direction, placing the evidence at Level 5 (model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain management (moderate to moderately severe pain) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Tramadol is a centrally-acting analgesic with two complementary mechanisms: (1) agonism at the μ-opioid receptor, producing direct analgesic effects, and (2) inhibition of serotonin and norepinephrine reuptake, which enhances descending pain pathway modulation. This dual action distinguishes Tramadol from conventional opioids and gives it a broader pain-control profile.

Acromesomelic Dysplasia, Hunter-Thompson Type is a rare autosomal recessive skeletal dysplasia driven by loss-of-function mutations in CDMP1/GDF5, a gene encoding a bone morphogenetic protein central to limb cartilage and joint development. There is no established mechanistic bridge between Tramadol's opioidergic/monoaminergic pathways and the GDF5/BMP signaling cascade that governs skeletogenesis. Tramadol does not interact with growth factor receptors, chondrocyte differentiation pathways, or connective tissue remodeling processes at any known target.

The high TxGNN score (99.99%) most likely reflects an **indirect knowledge graph connection** — a pain → skeletal node pathway arising from co-morbid pain phenotypes in bone dysplasia patients — rather than a genuine disease-modifying repurposing signal. This is a recognized artifact in graph-based prediction models, where pain is a highly connected hub node. The prediction should be interpreted as hypothesis-generating only, not as actionable pharmacological evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a near-perfect TxGNN prediction score, all evidence pathways return empty — no clinical trials, no literature, and no mechanistic rationale connecting Tramadol to the underlying GDF5/BMP signaling defect in this congenital skeletal disorder. The high score is most plausibly a knowledge graph artifact (pain hub co-occurrence) rather than a true repurposing signal.

**To proceed, the following is needed:**
- Retrieve Tramadol's full MOA data from DrugBank (DB00193) to confirm or rule out any off-target skeletal effects
- Complete the safety profile: obtain Philippines FDA (or TFDA) package insert warnings and contraindications to enable S1 safety screening
- Conduct a targeted literature search for Tramadol in skeletal dysplasia or BMP/GDF5 pathway modulation
- Consider re-prioritizing analysis to **Rank 7 — Juvenile Idiopathic Arthritis (L4 evidence)**, which has 2 associated literature records and a clinically coherent pain-management rationale, making it the most actionable candidate in this Evidence Pack for further evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

