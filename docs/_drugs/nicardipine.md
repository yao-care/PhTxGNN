---
layout: default
title: Nicardipine
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 5
---

# Nicardipine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using the `txgnn-pipeline` skill to orient this task — this is a report-generation step within the TxGNN pipeline for the PhTxGNN (Philippines) project. I'll now generate the evaluation report from the Evidence Pack.

---

# Nicardipine: From Hypertension to Multifactorial Pulmonary Hypertension

## One-Sentence Summary

Nicardipine is a dihydropyridine-type calcium channel blocker (CCB) widely used internationally for hypertension management and hypertensive emergencies; however, it has **no registered product in the Philippines**.
The TxGNN model's top prediction is that it may be effective for **pulmonary hypertension with unclear multifactorial mechanism (WHO Group 5)**, with a prediction score of **99.26%**.
Supporting this direction, there are currently **no registered clinical trials** and **no directly relevant publications**, placing the evidence entirely at model-prediction level.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines registration; internationally used for hypertension and hypertensive emergencies |
| Predicted New Indication | Pulmonary hypertension with unclear multifactorial mechanism (WHO Group 5) |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 (model prediction only, no supporting studies) |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Nicardipine is an L-type voltage-gated calcium channel blocker (CCB) of the dihydropyridine subclass. It acts by blocking calcium influx into vascular smooth muscle cells, producing arterial vasodilation and reducing peripheral vascular resistance — with a more selective vascular profile and less negative inotropic effect than older CCBs.

The theoretical basis for TxGNN's prediction lies in this pulmonary vasodilatory effect. In WHO Group 1 Pulmonary Arterial Hypertension (PAH), roughly 10% of idiopathic cases respond positively to acute vasoreactivity testing (AVT); these patients are candidates for high-dose CCB therapy (nifedipine, diltiazem, amlodipine). Nicardipine, sharing the same class, could theoretically contribute in this narrow, AVT-positive cohort.

However, the predicted indication here is **WHO Group 5 PH** — pulmonary hypertension arising from unclear or multifactorial causes (haematological disorders, systemic disorders, metabolic diseases). CCBs have **no established role** in Group 5 PH, and the pathophysiological pathways diverge fundamentally from Group 1 PAH. The TxGNN model likely arrives at this prediction via indirect connections in the knowledge graph (e.g., shared disease nodes with hypertension), but the clinical extrapolation is speculative. This prediction carries a high risk of graph-level artefact rather than true mechanistic signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for pulmonary hypertension with unclear multifactorial mechanism (WHO Group 5) in combination with Nicardipine.

---

## Literature Evidence

Currently no related literature directly linking Nicardipine to pulmonary hypertension with unclear multifactorial mechanism.

> **Note:** A PubMed search for the rank-2 indication (pulmonary hypertension owing to lung disease and/or hypoxia) returned 20 results, but all retrieved articles address general hypoxia biology (HIF-1α signalling, altitude physiology, cognitive effects of hypoxia, tumour microenvironment) and contain no data on Nicardipine efficacy in pulmonary hypertension. They are not included as supporting evidence.

---

## Philippines Market Information

Nicardipine currently has **no registered products** in the Philippines (data cutoff: 2026-05-05). There are no FDA Philippines authorisation numbers, no approved dosage forms, and no approved indications on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No DDI data was retrieved. Key warnings and contraindications are not available in this Evidence Pack and require retrieval from the official prescribing information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.26%), the evidence base for Nicardipine in WHO Group 5 pulmonary hypertension is entirely absent — no clinical trials, no publications, and no mechanistic studies directly support this indication. The underlying disease group (Group 5 PH) has heterogeneous, poorly characterised aetiology for which CCBs carry no guideline-recommended role; the prediction most likely reflects indirect graph connectivity rather than true therapeutic signal.

**To proceed, the following is needed:**

- **MOA confirmation**: Query DrugBank API (DB00622) to formally document Nicardipine's mechanism of action and target profile
- **Safety data**: Retrieve FDA Philippines or equivalent prescribing information to complete key warnings, contraindications, and drug interaction profile
- **Indication re-evaluation**: Assess whether the more mechanistically coherent target should be **AVT-positive Group 1 PAH** (where CCBs do have a guideline role), rather than Group 5 PH
- **Preclinical evidence search**: A focused literature search using MeSH terms \[nicardipine\] AND \[pulmonary hypertension\] AND \[vasoreactivity\] is warranted before any further development steps
- **Philippines registration pathway**: If evidence were to strengthen, a regulatory pre-consultation with FDA Philippines would be needed, given zero current market presence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

