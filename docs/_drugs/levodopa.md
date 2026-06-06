---
layout: default
title: Levodopa
parent: 僅模型預測 (L5)
nav_order: 203
evidence_level: L5
indication_count: 1
---

# Levodopa
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Levodopa: From Parkinson's Disease to Rasmussen Subacute Encephalitis

## One-Sentence Summary

Levodopa is a dopamine precursor and the foundational pharmacological treatment for Parkinson's disease, restoring central dopamine levels by crossing the blood-brain barrier and undergoing enzymatic conversion.
The TxGNN model predicts it may be effective for **Rasmussen Subacute Encephalitis**, a rare progressive autoimmune encephalitis defined by treatment-resistant focal epilepsy.
Currently, **no clinical trials** and **no publications** specifically support this repurposing direction, placing the evidence at the lowest tier (L5 — model prediction only).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (established clinical use; no Philippines registration on record) |
| Predicted New Indication | Rasmussen Subacute Encephalitis |
| TxGNN Prediction Score | 99.06% |
| Evidence Level | L5 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from current data sources. Based on established pharmacology, Levodopa (L-3,4-dihydroxyphenylalanine) is a dopamine precursor that crosses the blood-brain barrier and is converted to dopamine (DA) by DOPA decarboxylase. This central dopamine replenishment is the basis of its efficacy in Parkinson's disease.

The TxGNN model identifies three potential indirect mechanistic pathways connecting Levodopa to Rasmussen Subacute Encephalitis. First, dopamine can bind D1/D5 receptors on T cells, potentially suppressing Th17 differentiation and downregulating pro-inflammatory cytokines including IL-17 and TNF-α. Second, dopaminergic signaling may shift microglial polarization from M1 (pro-inflammatory) toward M2 (anti-inflammatory) phenotype, potentially moderating the neuroinflammatory cascade central to Rasmussen pathology. Third, the dopaminergic system has known functional interactions with NMDA/AMPA receptor regulation, and Rasmussen encephalitis is associated with anti-GluR3 (AMPA-type) autoantibodies.

These mechanistic links are, however, highly indirect and none have been validated clinically for this indication. Crucially, the high TxGNN score (99.06%) reflects knowledge graph topological similarity rather than a confirmed biological pathway. A significant safety concern also runs counter to this repurposing hypothesis: Levodopa has been reported to provoke myoclonus and may worsen certain seizure types in neurological contexts, directly conflicting with Rasmussen's hallmark symptom of refractory focal epilepsy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Levodopa has no registered products in the Philippines as of the data cut-off (2026-06-04). The drug is not marketed in the Philippines under any authorization on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinical Safety Flag**: The repurposing rationale identifies a direct conflict requiring attention before any further evaluation: Levodopa has been reported to induce myoclonus and may aggravate certain seizure types in some neurological settings. Because refractory focal epilepsy is the defining clinical feature of Rasmussen encephalitis, this potential adverse effect constitutes a primary safety concern that must be addressed with preclinical evidence before this candidate can advance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is supported exclusively by knowledge graph topology, with zero corroborating clinical trials or published literature. More critically, Levodopa's potential to worsen seizure activity in neurological contexts creates a direct and unresolved safety conflict with Rasmussen encephalitis, a condition whose core morbidity is intractable epilepsy.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) from DrugBank or primary literature to confirm or refute the indirect immunomodulatory pathway hypothesis
- Preclinical evidence (animal models or in vitro studies) demonstrating dopaminergic modulation of Rasmussen-type autoimmune neuroinflammation
- Dedicated seizure safety review: systematic evidence that Levodopa does not worsen focal cortical seizures or myoclonus at therapeutic doses
- Screening of published case reports or case series for any incidental observations of Levodopa use in autoimmune or inflammatory encephalitis patients
- Philippines FDA regulatory pathway scoping, conditional on preclinical findings reaching L4 evidence or above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

