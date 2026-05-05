---
layout: default
title: Indacaterol
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
---

# Indacaterol
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

# Indacaterol: From COPD/Asthma to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Indacaterol is a once-daily, ultra-long-acting beta2-adrenoceptor agonist (ultra-LABA) approved in multiple countries for the management of chronic obstructive pulmonary disease (COPD) and asthma, though it carries no registered products in the Philippines.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
with **no clinical trials** and **no publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | COPD / Asthma (approved in multiple countries; no Philippines registration on file) |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on known pharmacology, Indacaterol is an ultra-long-acting β2-adrenoceptor agonist that achieves sustained bronchodilation through a single once-daily inhalation — a profile that distinguishes it from earlier LABAs such as salmeterol or formoterol. Its efficacy in obstructive airway diseases has been validated in numerous Phase 2/3 randomised trials across adult and paediatric populations, and it is currently approved in the EU as a component of triple fixed-dose combinations (IND/GLY/MF, brand name Enerzair® Breezhaler®).

The proposed mechanistic connection to nephrogenic syndrome of inappropriate antidiuresis (NSIAD) is speculative at best. NSIAD is caused by gain-of-function mutations in the V2 vasopressin receptor (AVPR2) gene, resulting in constitutively active, ligand-independent water reabsorption in the renal collecting duct. β2-adrenergic receptors are minimally expressed in renal tubular tissue and may theoretically influence cAMP-mediated signalling cascades that partially overlap with the AVP/V2 pathway. This raises a very distant hypothesis that β2 agonism could attenuate the constitutive over-activation of V2-downstream cAMP signalling — but no pharmacological studies, animal models, or case reports exist to support this.

In practice, the high TxGNN score (99.54%) almost certainly reflects a distant graph-topology association rather than a validated mechanistic connection. NSIAD is a rare orphan disease, and the biological distance between β2-bronchodilation and renal water channel regulation is substantial. This prediction is hypothesis-generating only and should not be pursued without foundational preclinical work.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Indacaterol in nephrogenic syndrome of inappropriate antidiuresis.

---

## Literature Evidence

Currently no related literature available for Indacaterol in nephrogenic syndrome of inappropriate antidiuresis.

---

## Philippines Market Information

Indacaterol currently has no drug product registrations with the Philippine FDA. The product is not available on the Philippine market and has never been licensed locally.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no preclinical or clinical evidence of any kind linking Indacaterol to nephrogenic syndrome of inappropriate antidiuresis. The high TxGNN score derives from a distant knowledge-graph association, not a validated mechanistic or therapeutic signal; proceeding to any development activity at this stage would be premature.

> **Additional context:** The most evidence-supported indication in this TxGNN run is **Bronchial Disease (Rank 7, L1 — Proceed with Guardrails)**, which encompasses asthma management. This is consistent with Indacaterol's already-approved use globally and represents a potential near-term regulatory pathway for the Philippines if local registration is being considered.

**To proceed with the NSIAD hypothesis, the following is needed:**

- Preclinical validation: in vitro studies of β2 agonist effects on AVPR2-mutant renal tubular cell models to determine whether cAMP downstream signalling is modulated
- Pharmacokinetic assessment: confirm whether inhaled Indacaterol achieves any meaningful renal tubular exposure (systemic bioavailability of Indacaterol is low ~40–45%; renal distribution is not characterised)
- MOA documentation: retrieve full DrugBank mechanism of action data (DG002 remediation) to enable formal mechanistic linkage analysis
- Safety/regulatory baseline: obtain Philippines FDA package insert equivalent or WHO-licensed PI to complete S1 safety pre-screening (DG001 remediation; currently blocking)
- Disease expert consultation: engage a nephrologist specialising in NSIAD/rare tubular disorders to assess biological plausibility before investing in wet-lab work

---

*⚠️ This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

