---
layout: default
title: Tamsulosin
parent: 僅模型預測 (L5)
nav_order: 321
evidence_level: L5
indication_count: 10
---

# Tamsulosin
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

# Tamsulosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Tamsulosin is a selective alpha-1 adrenergic receptor antagonist widely used in clinical practice for the treatment of benign prostatic hyperplasia (BPH) and associated lower urinary tract symptoms.
The TxGNN model predicts it may be effective for **Ambras Type Hypertrichosis Universalis Congenita**, an ultra-rare congenital hair overgrowth disorder.
Currently, there are **0 clinical trials** and **0 publications** directly supporting this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign Prostatic Hyperplasia / Lower Urinary Tract Symptoms |
| Predicted New Indication | Ambras Type Hypertrichosis Universalis Congenita |
| TxGNN Prediction Score | 99.996% |
| Evidence Level | L5 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on established pharmacological knowledge, Tamsulosin is a selective alpha-1 adrenergic receptor antagonist with preferential affinity for the ADRA1A and ADRA1D subtypes. Its proven clinical utility lies in relaxing smooth muscle in the prostate gland and bladder neck, thereby relieving urinary outflow obstruction in men with BPH. It is not an immunomodulator, cytotoxic agent, or hormone-modifying drug.

Ambras syndrome (OMIM 145701) is a congenital disorder caused by a deletion at chromosomal locus 8q23.3 involving the *TRPS1* transcription factor gene, resulting in universal hypertrichosis with abnormal hair follicle development and characteristic facial dysmorphism. The pathophysiology is entirely genetic and developmental in origin — driven by transcription factor dysfunction affecting ectodermal and follicular morphogenesis — rather than by adrenergic receptor signaling. Although alpha-1 adrenergic receptors (ADRA1A) have been detected at low expression levels in dermal papilla cells of hair follicles, no evidence exists that alpha-1 receptor blockade can influence the genetically determined follicular overgrowth in Ambras syndrome.

The extremely high TxGNN score (99.996%) most likely reflects a topological false positive arising from the model's knowledge graph structure, where hair disorder nodes cluster in proximity to shared drug-target nodes and propagate high prediction scores without valid biological grounding. The same pattern repeats across the top 10 predictions, which are dominated by rare hair and follicular disorders (ranks 1–9) with no mechanistic link to alpha-1 adrenergic antagonism. This systematic clustering strongly suggests graph neighborhood bias rather than genuine pharmacological opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Tamsulosin in Ambras type hypertrichosis universalis congenita.

---

## Literature Evidence

Currently no related literature available for Tamsulosin in Ambras type hypertrichosis universalis congenita.

---

## Philippines Market Information

Tamsulosin currently has no registered product with the Philippines FDA. No authorization records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All top 10 TxGNN predictions for Tamsulosin are rated L5 (model prediction only, no supporting studies), and the highest-ranked indication — Ambras Type Hypertrichosis Universalis Congenita — has no mechanistic plausibility, no clinical trials, and no supporting literature; the prediction pattern across all 10 indications is consistent with knowledge graph topological bias rather than genuine repurposing signal.

**To proceed, the following is needed:**
- Retrieve MOA data from DrugBank (ADRA1A/ADRA1D selectivity, receptor binding kinetics) to enable mechanistic plausibility analysis
- Obtain Philippines FDA package insert PDF to complete safety profiling (warnings, contraindications, drug interactions)
- Request TxGNN team to review knowledge graph edge weighting for hair disorder nodes to assess and correct potential false-positive clustering
- Consider redirecting repurposing evaluation to biologically grounded candidates where alpha-1 antagonism has independent mechanistic rationale — such as ureteral stone expulsion therapy, PTSD-related sleep disturbances (prazosin class effect), or hypertensive urgency — which may yield higher-yield L3–L4 evidence upon targeted literature search
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

