---
layout: default
title: Carbetocin
parent: 僅模型預測 (L5)
nav_order: 59
evidence_level: L5
indication_count: 2
---

# Carbetocin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Carbetocin: From Postpartum Hemorrhage to Isotretinoin-Like Syndrome

## One-Sentence Summary

Carbetocin is a synthetic long-acting oxytocin analogue, primarily used to prevent uterine atony and postpartum hemorrhage by activating oxytocin receptors in the myometrium.
The TxGNN model predicts it may be effective for **isotretinoin-like syndrome**, yet **no clinical trials** and **no publications** currently support this direction.
This prediction rests on model output alone (Evidence Level L5), with mechanistic analysis revealing no plausible biological link.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Postpartum hemorrhage prevention (uterine atony) |
| Predicted New Indication | Isotretinoin-Like Syndrome |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Carbetocin is a synthetic, long-acting oxytocin analogue that binds selectively to the G protein-coupled oxytocin receptor (OTR). Upon receptor activation, it triggers the Gq → PLC → IP3/DAG → PKC intracellular cascade, elevating cytosolic calcium and driving uterine smooth muscle contraction — the pharmacological mechanism underlying its clinical use in preventing postpartum hemorrhage after cesarean delivery.

Isotretinoin-like syndrome describes an embryotoxic phenotype caused by excess retinoic acid (13-cis-retinoic acid) exposure. Its molecular basis is entirely distinct: aberrant activation of RAR/RXR nuclear receptors disrupts neural crest cell migration, producing characteristic craniofacial, cardiac, and thymic developmental defects. The receptor systems (GPCR vs. nuclear receptor), downstream effectors (Ca²⁺/PKC vs. gene transcription), and target biology (uterine contractility vs. embryonic organogenesis) have no established points of intersection in the pharmacological literature.

The high TxGNN score (99.15%) most likely reflects indirect statistical co-occurrence between sparse nodes in the knowledge graph, rather than a biologically meaningful repurposing signal. No experimental, mechanistic, or clinical data have been identified to support this predicted indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Carbetocin is not currently registered in the Philippines. No active product licenses were found in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical or preclinical evidence supporting Carbetocin for isotretinoin-like syndrome, and mechanistic analysis reveals a fundamental mismatch between the oxytocin receptor/Ca²⁺ signaling axis and the RAR/RXR-driven retinoic acid teratogenicity pathway. This prediction does not meet the minimum threshold for further investigation.

**To proceed, the following would be needed:**
- A credible biological hypothesis linking OTR activation to retinoic acid signaling or neural crest cell biology
- Preclinical data (in vitro or animal model) demonstrating any effect of oxytocin receptor agonism on retinoic acid-induced toxicity
- Full safety profile including package insert warnings and contraindications (currently unavailable)
- Reconsideration of whether this TxGNN result is a spurious knowledge-graph artefact arising from rare-node proximity, rather than a true repurposing signal

> **Note:** The second-ranked prediction, Goodman syndrome (TxGNN score 99.06%, rank 6178), is similarly unsupported — it involves the RAB23/Sonic Hedgehog/Gli signaling axis, which has no known pharmacological intersection with the oxytocin receptor pathway. Both top predictions share the same L5 / Hold classification and warrant no near-term development resources.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

