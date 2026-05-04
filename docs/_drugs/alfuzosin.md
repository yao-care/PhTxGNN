---
layout: default
title: Alfuzosin
parent: 僅模型預測 (L5)
nav_order: 17
evidence_level: L5
indication_count: 10
---

# Alfuzosin
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

# Alfuzosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita

## One-Sentence Summary

Alfuzosin is a selective alpha-1 adrenergic receptor antagonist, widely used in clinical practice for the management of lower urinary tract symptoms associated with benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, an extremely rare genetic hair overgrowth disorder caused by *TRPS1* gene mutations,
with **0 clinical trials** and **0 publications** currently supporting this direction. This prediction is based entirely on model inference, with no corroborating clinical or experimental evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Benign prostatic hyperplasia (BPH) / lower urinary tract symptoms — no Philippines registration data available |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacological information, Alfuzosin is a selective alpha-1 adrenergic receptor antagonist. It relaxes smooth muscle in the prostate and bladder neck by competitively blocking alpha-1A receptors, thereby relieving outflow obstruction in BPH. Alpha-1 receptors are also expressed in dermal papilla cells of hair follicles and in cutaneous vascular smooth muscle, which may have prompted the TxGNN model to associate Alfuzosin with hair-related disorders.

Ambras syndrome is an extremely rare disorder driven by chromosomal rearrangements affecting the *TRPS1* gene (encoding a GATA-type zinc finger transcription factor), leading to diffuse, excessive hair growth across the entire body and face. The disease mechanism is fundamentally genetic and transcriptional — entirely distinct from the adrenergic signaling pathway through which Alfuzosin exerts its effects.

The mechanistic link between alpha-1 receptor blockade and *TRPS1*-mediated hair follicle dysregulation is considered extremely tenuous. There is no evidence — experimental, preclinical, or clinical — suggesting that Alfuzosin can influence the *TRPS1* regulatory pathway or reverse the abnormal hair follicle proliferation that characterizes Ambras syndrome. At this stage, the high TxGNN score likely reflects structural or topological graph proximity in the knowledge network rather than a biologically actionable connection.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Alfuzosin has no registered products in the Philippines. The drug is currently not marketed and carries no active license authorizations in the Philippine FDA registry.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN confidence score, the mechanistic connection between alpha-1 adrenergic receptor blockade and Ambras syndrome — a monogenic hair overgrowth disorder driven by *TRPS1* transcription factor disruption — is scientifically unsupported, and there is a complete absence of clinical, observational, or preclinical evidence. The drug is additionally unregistered in the Philippines, adding a regulatory barrier before any clinical application could be considered.

**To proceed, the following is needed:**
- Retrieve Alfuzosin mechanism of action data from DrugBank API (currently Data Gap — blocks mechanistic plausibility assessment)
- Obtain Philippines package insert warnings and contraindications (currently Data Gap — blocks safety pre-screening)
- Conduct a targeted literature search examining whether alpha-1 adrenergic signaling has any role in *TRPS1* pathway regulation or hair follicle cycling biology
- If any mechanistic basis emerges, in vitro studies using *TRPS1*-deficient hair follicle models would be required before any clinical hypothesis could be formed
- Philippines drug registration (NDA submission) would need to be pursued as a prerequisite for local clinical development
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

