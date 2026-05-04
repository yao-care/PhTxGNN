---
layout: default
title: Fluticasone
parent: 僅模型預測 (L5)
nav_order: 152
evidence_level: L5
indication_count: 3
---

# Fluticasone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Fluticasone: From Allergic Rhinitis/Asthma to Migraine Disorder

## One-Sentence Summary

Fluticasone is a topical glucocorticoid widely used internationally for allergic rhinitis and asthma, acting primarily through local anti-inflammatory effects with very low systemic bioavailability (<2%). The TxGNN model predicts it may be effective for **Migraine Disorder**, but currently there are **0 clinical trials** and only **1 indirectly related publication** supporting this direction. The evidence is extremely limited, and significant pharmacokinetic barriers exist — this prediction is not currently actionable.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No registered products in the Philippines (internationally: allergic rhinitis, asthma) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 (Model prediction only, no clinical evidence) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action (MOA) data is not available in the evidence pack. Based on known information, Fluticasone is a synthetic glucocorticoid with potent anti-inflammatory properties. It is primarily formulated for topical delivery (intranasal sprays, inhalers, dermal creams) and exerts its effects locally by suppressing inflammatory mediators, inhibiting cytokine release, and reducing immune cell activation at the site of administration.

The theoretical link to migraine disorder rests on the hypothesis that glucocorticoids can suppress neurogenic inflammation — specifically, the release of CGRP (calcitonin gene-related peptide) and activation of the trigeminovascular system, both of which are central to migraine pathophysiology. Systemic corticosteroids such as dexamethasone have indeed been used as adjunctive therapy in acute migraine to reduce recurrence rates, lending some conceptual plausibility to this prediction.

However, **this prediction faces a critical pharmacokinetic barrier**: Fluticasone is designed for local action and has a systemic bioavailability of less than 2%. It cannot achieve the plasma concentrations necessary to influence central nervous system targets relevant to migraine. Unless a fundamentally new formulation (e.g., oral systemic delivery) were developed, the mechanistic link is not pharmacologically viable in its current form. The TxGNN model, being a graph-based prediction system, likely captured the glucocorticoid–anti-inflammatory–neuroinflammation association without accounting for route-of-administration and bioavailability constraints.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Fluticasone in migraine disorder, Prinzmetal angina, or migraine with brainstem aura.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18681087](https://pubmed.ncbi.nlm.nih.gov/18681087/) | 2008 | Safety Review | Ann Allergy Asthma Immunol | WHO pharmacovigilance review of neuropsychiatric disturbances associated with intranasal corticosteroids. Notes that INCs are considered to act locally with minimal systemic effects, but an unexpected cluster of neuropsychiatric adverse event reports was identified. **Not an efficacy study for migraine — focuses on safety signals.** |

> **Note:** This publication does not support the use of Fluticasone for migraine. It is a safety review documenting adverse neuropsychiatric effects of intranasal corticosteroids, and was retrieved due to keyword overlap between corticosteroids and neurological conditions.

---

## Philippines Market Information

Fluticasone has **no registered products** in the Philippines (FDA Philippines). There are no authorization numbers, product names, or locally approved indications to report.

---

## Safety Considerations

> Please refer to the package insert for safety information. No safety data (warnings, contraindications, or drug–drug interactions) was available in the current evidence pack for Fluticasone (DB13867).

---

## Additional Predicted Indications (Lower Priority)

For completeness, the TxGNN model also predicted two additional indications, both rated **L5 / Hold**:

| Rank | Predicted Indication | TxGNN Score | Clinical Trials | Literature | Recommendation |
|------|---------------------|-------------|-----------------|------------|----------------|
| 2 | Prinzmetal Angina | 99.19% | 0 | 0 | Hold |
| 3 | Migraine with Brainstem Aura | 99.09% | 0 | 0 | Hold |

**Prinzmetal Angina**: Variant angina caused by coronary artery spasm. The mechanistic link is extremely weak — coronary spasm is driven by smooth muscle hypercontractility and endothelial dysfunction, not primarily by inflammation. Fluticasone's negligible systemic bioavailability makes this prediction pharmacologically implausible.

**Migraine with Brainstem Aura**: A rare migraine subtype involving reversible brainstem dysfunction. The rationale is even weaker than for general migraine — the pathology is more electrophysiological than inflammatory, Fluticasone cannot cross the blood-brain barrier at meaningful concentrations, and the rarity of this condition would make clinical study impractical.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All three predicted indications are at evidence level L5 — model prediction only, with no supporting clinical trials and no relevant efficacy literature. The single retrieved publication is a safety review, not an efficacy study. Most critically, Fluticasone's pharmacokinetic profile (systemic bioavailability <2%) creates a fundamental barrier to efficacy in systemic/CNS conditions like migraine and angina. The TxGNN prediction, while numerically high-scoring, does not account for route-of-administration constraints, making this a case where the model's graph-level associations do not translate to clinical plausibility.

**To proceed, the following would be needed:**
- Development and characterization of a systemic-delivery formulation of Fluticasone (which would essentially be a new drug product)
- Preclinical evidence demonstrating that Fluticasone at achievable systemic concentrations can modulate CGRP release or trigeminovascular activation
- Mechanism of action (MOA) data gap resolution via DrugBank API query
- FDA Philippines package insert / safety data to complete safety assessment
- Given existing, well-established migraine therapies (triptans, CGRP inhibitors, gepants), the therapeutic niche for a repurposed corticosteroid would need clear differentiation

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

