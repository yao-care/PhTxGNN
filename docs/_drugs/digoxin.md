---
layout: default
title: Digoxin
parent: 僅模型預測 (L5)
nav_order: 106
evidence_level: L5
indication_count: 6
---

# Digoxin
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

# Digoxin: From Heart Failure / Atrial Fibrillation to Prinzmetal Angina

## One-Sentence Summary

Digoxin is a cardiac glycoside historically used for heart failure and atrial fibrillation (AF) rate control. The TxGNN model predicts it may be effective for **Prinzmetal Angina** (rank 1, score 99.81%), with **0 clinical trials** and **2 publications** currently supporting this direction. Critically, the mechanistic evidence reviewed suggests this prediction is likely a knowledge-graph false positive rather than a genuine repurposing opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure; atrial fibrillation rate control (internationally established; **not registered in the Philippines**) |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Digoxin is a cardiac glycoside that inhibits the Na⁺/K⁺-ATPase pump on myocardial and vascular smooth muscle cells, increasing intracellular calcium concentration, strengthening cardiac contractions (positive inotropy), and slowing atrioventricular conduction through enhanced vagal tone. It is a well-established agent for systolic heart failure and ventricular rate control in atrial fibrillation.

The TxGNN knowledge graph likely generated this high-score prediction by traversing cardiovascular disease nodes — heart failure and angina are closely linked in graph topology (both involve myocardial oxygen supply-demand imbalance). However, the apparent mechanistic link is actually **contradictory** rather than supportive: by inhibiting Na⁺/K⁺-ATPase in vascular smooth muscle, Digoxin elevates intracellular calcium, which could theoretically **precipitate or worsen** coronary vasospasm — the very pathophysiology underlying Prinzmetal angina.

Current cardiology guidelines uniformly recommend calcium channel blockers (amlodipine, diltiazem) and long-acting nitrates as first-line therapy for Prinzmetal angina. Digoxin does not appear in any major guideline for this indication. The high TxGNN rank (99.81%) almost certainly reflects broad cardiovascular node connectivity in the knowledge graph, not a specific biological rationale.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9206110](https://pubmed.ncbi.nlm.nih.gov/9206110/) | 1996 | Clinical Review | Chinese Medical Sciences Journal | Studied 30 angina decubitus patients; primary mechanism was severe coronary obstruction and increased myocardial oxygen consumption; no mention of Digoxin as a treatment option |
| [10736610](https://pubmed.ncbi.nlm.nih.gov/10736610/) | 1999 | Narrative Review | Acta Physiologica et Pharmacologica Bulgarica | Review of circadian rhythms in antihypertensive pharmacotherapy; not directly relevant to Digoxin efficacy in Prinzmetal angina |

> **Note:** Neither publication provides evidence of Digoxin efficacy in Prinzmetal angina. Their retrieval reflects keyword overlap between cardiovascular conditions, not therapeutic relevance.

---

## Philippines Market Information

Digoxin is currently **not registered** in the Philippines. No authorization records exist in the FDA Philippines database. Any future use would require a full new drug registration pathway.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** No DDI data was retrieved in this evidence pack (query status: not found). Digoxin has a well-known narrow therapeutic index and numerous clinically significant drug interactions in published pharmacology literature — a formal DDI review is strongly recommended before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic basis for using Digoxin in Prinzmetal angina is not only unsubstantiated but potentially **directionally harmful** — Digoxin's calcium-promoting effect on vascular smooth muscle may worsen the coronary vasospasm that defines Prinzmetal angina. No clinical trials and only two tangentially related publications exist, neither of which supports this use. All remaining five TxGNN-predicted indications (duodenal obstruction, duodenal ulcer, duodenogastric reflux, ischemic stroke susceptibility, hypoalphalipoproteinemia) carry even weaker evidence (L5) and similarly lack mechanistic rationale, reinforcing the conclusion that the current prediction batch does not identify a viable repurposing opportunity for Digoxin in the Philippines context.

**To proceed, the following is needed:**

- Obtain and review the full package insert (including warnings, contraindications, and narrow therapeutic index guidance) to enable a formal S1 safety assessment
- Conduct a structured DDI review given Digoxin's known interactions with dozens of commonly co-prescribed agents
- Clarify whether Digoxin's vasoconstrictive effect on coronary smooth muscle represents an absolute contraindication in vasospastic angina prior to any clinical hypothesis generation
- Complete a regulatory feasibility assessment for a potential new Philippines registration if a future valid indication is identified
- Re-query TxGNN with a curated cardiovascular disease list to identify candidate indications that are mechanistically aligned (e.g., specific arrhythmias, heart failure subtypes) rather than graph-proximity driven
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

