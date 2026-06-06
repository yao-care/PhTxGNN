---
layout: default
title: Isoxsuprine
parent: 僅模型預測 (L5)
nav_order: 187
evidence_level: L5
indication_count: 10
---

# Isoxsuprine
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

# Isoxsuprine: From Peripheral Vascular Disease to Benign Prostatic Hyperplasia

## One-Sentence Summary

Isoxsuprine is a beta-adrenergic agonist and peripheral vasodilator historically used for peripheral vascular disease and as a tocolytic agent in preterm labor.
The TxGNN model predicts it may be effective for **Benign Prostatic Hyperplasia (BPH)**, ranked #1 with a near-perfect prediction score.
However, **no clinical trials and no supporting literature** currently exist for this indication — the prediction rests entirely on model inference.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Philippines; historically used for peripheral vascular disease and tocolysis |
| Predicted New Indication | Benign Prostatic Hyperplasia (BPH) |
| TxGNN Prediction Score | 99.9999% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on known pharmacological information, Isoxsuprine is a sympathomimetic drug with beta-adrenergic agonist activity. Its primary effect is relaxation of vascular smooth muscle, which historically formed the basis for its use in peripheral vascular disease (e.g., Raynaud's disease, arteriosclerosis obliterans) and as a uterine relaxant in preterm labor.

The theoretical bridge to BPH stems from the premise that beta-adrenergic agonists can relax smooth muscle in the urogenital tract. A functionally analogous mechanism is seen with beta-3 agonists such as mirabegron, which is approved for overactive bladder (OAB). However, Isoxsuprine primarily acts on vascular smooth muscle and has very low selectivity for prostatic or bladder-neck tissue. The mechanistic connection between Isoxsuprine and BPH symptom relief is therefore speculative and structurally weak.

In practice, the TxGNN model prediction for BPH likely reflects network-level proximity in the knowledge graph rather than any established pharmacological pathway. Without preclinical data confirming smooth-muscle relaxation in the lower urinary tract, this prediction cannot be acted upon and should be treated as a hypothesis-generating signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Isoxsuprine in Benign Prostatic Hyperplasia.

---

## Literature Evidence

Currently no related literature available for Isoxsuprine in Benign Prostatic Hyperplasia.

---

## Philippines Market Information

Isoxsuprine currently holds no pharmaceutical registration in the Philippines. No license records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** A data gap exists for both TFDA/FDA-Philippines package insert warnings and formal contraindication data. These must be obtained before any clinical feasibility assessment can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is currently zero clinical or preclinical evidence supporting Isoxsuprine for Benign Prostatic Hyperplasia. The drug is unregistered in the Philippines, mechanism of action data is unavailable, and the proposed pharmacological link to BPH is weak and theoretical. All 10 predicted indications in this pack are rated L5 (model prediction only), making this an early-stage signal that cannot support forward investment without substantial gap-filling.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank API (DG002 — High severity)
- Package insert warnings and contraindications from TFDA or FDA-Philippines (DG001 — Blocking severity)
- At least one preclinical study demonstrating smooth-muscle relaxation activity in lower urinary tract tissue
- Drug interaction profile assessment
- Regulatory feasibility review for Philippines market entry
- Consideration of whether more actionable indications exist within Isoxsuprine's established vascular pharmacology (e.g., peripheral arterial disease, Raynaud's) before pursuing the BPH hypothesis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

