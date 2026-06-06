---
layout: default
title: Tetracaine
parent: 僅模型預測 (L5)
nav_order: 328
evidence_level: L5
indication_count: 9
---

# Tetracaine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Tetracaine: From Local Anesthesia to Acrodermatitis Chronica Atrophicans

## One-Sentence Summary

Tetracaine is an ester-type local anesthetic classically used for surface, spinal, and mucous membrane anesthesia in ophthalmological, dental, and procedural settings.
The TxGNN model predicts it may be effective for **Acrodermatitis Chronica Atrophicans**,
with **0 clinical trials** and **0 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local anesthesia (surface, spinal, and mucous membrane anesthesia) |
| Predicted New Indication | Acrodermatitis Chronica Atrophicans |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, Tetracaine is an ester-type local anesthetic that reversibly blocks voltage-gated sodium channels (Nav), suppressing nerve impulse conduction and producing localized sensory blockade. This mechanism underlies its use across ophthalmology, bronchoscopy pre-medication, spinal anesthesia, and procedural dermatology.

Acrodermatitis chronica atrophicans (ACA) is a late-stage dermatological manifestation of *Borrelia burgdorferi* infection (Lyme disease), characterized by progressive skin atrophy with an inflammatory prodrome that requires antibiotic therapy. The sodium channel-blocking mechanism of Tetracaine has no established pathway relevant to infectious or immune-mediated skin pathology. The TxGNN high score (99.93%) most likely reflects structural clustering of skin-related disease nodes in the knowledge graph rather than a genuine mechanistic connection.

It is worth noting that among all nine predicted indications in this evidence pack, **acne keloid (Rank 5)** carries the strongest clinical evidence: a completed Phase 4 double-blind RCT (NCT02372786, n=30) documented efficacy of a 7% lidocaine/7% tetracaine compound cream for procedural pain control during laser treatment of acne keloidalis nuchae. This is an extension of Tetracaine's established local anesthetic use into a specific procedural context — not disease-modifying repurposing — but represents the most clinically actionable signal in this pack. Additionally, **cauda equina syndrome (Rank 8)** carries a critical reverse signal: all 9 associated publications document tetracaine-induced neurotoxicity following spinal administration, and must be interpreted as a safety warning, not a treatment opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for acrodermatitis chronica atrophicans.

---

## Literature Evidence

Currently no related literature available for acrodermatitis chronica atrophicans.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Reverse Safety Signal — Cauda Equina Syndrome (Rank 8):** Nine published case reports, follow-up studies, and mechanistic reviews consistently document tetracaine-induced cauda equina syndrome following spinal anesthesia. High-concentration intrathecal tetracaine can cause irreversible sodium channel blockade leading to persistent sacral sensory deficits and neurological injury. This pattern represents a known adverse event signal, **not** a repurposing candidate, and should be flagged as a contraindication to intrathecal high-dose administration.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction for acrodermatitis chronica atrophicans (L5, Score 99.93%) is unsupported by any clinical or preclinical evidence, and the mechanistic link between sodium channel blockade and Borrelia-driven late-stage Lyme skin disease is biologically implausible without further investigation. The most credible repurposing signal in this evidence pack — Tetracaine as procedural analgesia in acne keloid laser therapy (Rank 5, L1) — is an application of its existing local anesthetic indication and does not constitute novel disease-modifying repurposing.

**To proceed, the following is needed:**

- **MOA data**: Retrieve full mechanism of action from DrugBank API (DG002; High severity)
- **Safety package**: Download and parse the TFDA/Philippine FDA package insert for warnings and contraindications (DG001; Blocking — required before any S1 safety screening)
- **Philippines regulatory pathway**: Confirm whether any tetracaine-containing combination products (e.g., lidocaine/tetracaine cream) are registered or eligible for expedited review in the Philippines
- **ACA mechanistic hypothesis**: If ACA repurposing is to be seriously explored, preclinical data examining Nav modulation in Borrelia-driven inflammation or neuropathic skin pain would be required as a first step
- **Acne keloid translation**: If pivoting to the Rank 5 acne keloid procedural indication, a regulatory feasibility assessment for the 7% lidocaine/7% tetracaine combination in the Philippine market would be the appropriate next action
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

