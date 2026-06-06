---
layout: default
title: Memantine
parent: 僅模型預測 (L5)
nav_order: 220
evidence_level: L5
indication_count: 4
---

# Memantine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Memantine: From Alzheimer's Disease to Pulmonary Hypertension

## One-Sentence Summary

Memantine is a non-competitive NMDA receptor antagonist approved in multiple countries for the treatment of moderate-to-severe Alzheimer's disease and vascular dementia.
The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, with **0 clinical trials** and **2 publications** currently supporting this specific direction.
The overall evidence base for this particular repurposing direction is weak, placing it at evidence level L5 (model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Alzheimer's disease / moderate-to-severe dementia (not registered in Philippines) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacological knowledge, Memantine is a non-competitive, voltage-dependent antagonist of N-methyl-D-aspartate (NMDA) receptors — a subtype of ionotropic glutamate receptor. It blocks pathological, tonic activation of NMDA receptors while largely preserving physiological, phasic receptor activity, which forms the basis of its cognitive benefit in dementia.

The theoretical link to pulmonary hypertension rests on the observation that NMDA receptors are expressed in pulmonary vascular smooth muscle cells. Under this hypothesis, NMDA receptor antagonism could theoretically reduce glutamate-driven vasoconstriction and attenuate vascular remodelling in the pulmonary vasculature. However, this mechanistic pathway is highly indirect and remains entirely speculative — no clinical or preclinical studies have directly tested Memantine in pulmonary arterial hypertension.

The two literature records identified are only tangentially relevant: one covers general NMDA receptor involvement in metabolic and pulmonary injury (PMID 33500723), while the other evaluates MN-08, a nitrate *derivative* of Memantine, in a Phase 1 safety study — not Memantine itself (PMID 41739394). The TxGNN prediction likely reflects topological proximity within the knowledge graph (e.g., shared cardiovascular or vascular biology nodes) rather than direct biological evidence. This direction currently does not meet the threshold for active development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33500723](https://pubmed.ncbi.nlm.nih.gov/33500723/) | 2021 | Basic Research (Metabolism) | *Theranostics* | Examines the glutamate/NMDA receptor axis in acute lung injury and pulmonary arterial hypertension in the context of metabolic regulation; does not directly test Memantine in pulmonary hypertension |
| [41739394](https://pubmed.ncbi.nlm.nih.gov/41739394/) | 2026 | Phase 1 PK/Safety | *Clinical Drug Investigation* | Evaluates MN-08 (a nitrate derivative of Memantine, not Memantine itself) in healthy Chinese volunteers for pulmonary arterial hypertension; results are not directly applicable to Memantine |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high prediction score (99.54%) to Memantine for pulmonary hypertension, but the evidence base is at L5 — no clinical trials and no publications testing Memantine directly in this indication exist. The proposed mechanistic link via pulmonary vascular NMDA receptors is speculative and biologically indirect.

**To proceed, the following is needed:**

- Preclinical (in vitro / animal model) studies directly demonstrating that Memantine reduces pulmonary vascular resistance or attenuates pulmonary vascular remodelling
- Mechanistic confirmation of NMDA receptor expression and functional relevance in human pulmonary artery smooth muscle cells
- Review of the MN-08 (Memantine nitrate derivative) clinical programme for any translatable safety or proof-of-concept signals
- Formal MOA and safety profile data retrieval from DrugBank and the Philippines FDA (FDA-Philippines) package insert

---

> **Note:** Three additional indications were predicted by TxGNN for Memantine. Migraine disorder (rank 2, L2 evidence, "Proceed with Guardrails") carries substantially stronger clinical support, including a completed Phase 3 trial (NCT04698525), a meta-analysis, and multiple systematic reviews. A separate evaluation report for the migraine indication is recommended as the higher-priority development path.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

