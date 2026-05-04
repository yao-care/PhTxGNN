---
layout: default
title: Bromocriptine
parent: 僅模型預測 (L5)
nav_order: 48
evidence_level: L5
indication_count: 10
---

# Bromocriptine
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

# Bromocriptine: From Parkinson's Disease & Hyperprolactinemia to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

Bromocriptine is a semisynthetic ergot alkaloid and dopamine D2/D3 receptor agonist with well-established global uses in Parkinson's disease, hyperprolactinemia, acromegaly, and type 2 diabetes (Cycloset formulation).
The TxGNN model predicts it may be effective for **congenital disorder of glycosylation with defective fucosylation** as its top-ranked new indication (score 99.83%), yet currently there are **no clinical trials** and **no publications** specifically supporting this direction.
Across all 10 predicted indications, evidence is uniformly sparse — the highest data density is found for schizophrenia-adjacent applications (3 clinical trials, 20 publications), though even these carry significant mechanistic safety concerns.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease, hyperprolactinemia (no Philippines registration on file) |
| Predicted New Indication | Congenital disorder of glycosylation with defective fucosylation |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not currently available in this evidence pack. Based on established pharmacology, bromocriptine acts primarily as a dopamine D2 and D3 receptor agonist with partial D1 activity and serotonin 5-HT2C receptor agonism. It suppresses prolactin secretion through pituitary D2 receptors, activates nigrostriatal dopaminergic pathways (providing symptomatic relief in Parkinson's disease), and modulates hypothalamic circadian rhythm signaling — the mechanism underlying its FDA-approved Cycloset formulation for type 2 diabetes.

Congenital disorder of glycosylation with defective fucosylation (CDG-IIc, also known as leukocyte adhesion deficiency type II) is caused by loss-of-function mutations in *SLC35C1*, the gene encoding the GDP-fucose transporter in the Golgi apparatus. Defective N-glycan fucosylation leads to recurrent life-threatening infections, severe intellectual disability, and growth failure. The disease mechanism is entirely upstream of — and biologically disconnected from — the dopaminergic neurotransmitter system.

The TxGNN high prediction score (0.9983) is most plausibly a knowledge graph artifact: rare disease nodes tend to cluster in network proximity even when no true pharmacological relationship exists. No known biological pathway connects D2/D3 receptor agonism to GDP-fucose transport, fucosyltransferase activity, or Golgi glycosylation machinery. This prediction is currently considered biologically implausible, and the mechanistic rationale analysis in the evidence pack concurs with this assessment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for congenital disorder of glycosylation with defective fucosylation.

---

## Literature Evidence

Currently no related literature available for this specific indication.

---

## Philippines Market Information

Bromocriptine has **no product registrations** with the Philippine FDA. No authorizations, dosage forms, or approved indications were found in the regulatory database. Any future clinical application in the Philippines would require a full registration process before use.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important note for reviewers:** One case report (PMID [8120934](https://pubmed.ncbi.nlm.nih.gov/8120934/)) documents bromocriptine-induced psychosis, consistent with the drug's dopamine agonist mechanism. This is a relevant safety signal if any repurposing attempt targets neuropsychiatric indications. Additionally, given that bromocriptine is a dopamine D2 agonist, its use in patients concurrently taking D2 antagonists (antipsychotics, metoclopramide, domperidone) would represent a pharmacodynamic antagonism interaction of clinical significance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite achieving the highest TxGNN rank in this evidence pack, the prediction linking bromocriptine to congenital glycosylation disorders lacks any biological plausibility, supporting clinical trials, or published literature — placing it firmly at evidence level L5. The absence of Philippine market registration adds a further regulatory barrier to any clinical application.

**To proceed, the following is needed:**

- **MOA documentation:** Retrieve the full DrugBank entry and any available Philippines or international package inserts to formally document the mechanism of action before reassessment.
- **Biological plausibility review:** An independent expert in glycobiology should evaluate whether any indirect pathway (e.g., D2 receptor modulation of vesicular trafficking, which shares some Golgi machinery) could theoretically connect bromocriptine to fucosylation. Current scientific consensus does not support this.
- **Portfolio-level prioritization:** Among the 10 predicted indications in this pack, the schizophrenia-adjacent applications (particularly managing antipsychotic-induced hyperprolactinemia and metabolic dysregulation — NCT03575000) represent the highest evidence density (L3), but carry a critical mechanistic safety concern: bromocriptine as a D2 agonist may exacerbate positive psychotic symptoms. Any such investigation requires concurrent antipsychotic coverage and careful patient selection.
- **Regulatory pathway:** Philippine FDA registration (via Certificate of Product Registration) must be obtained before any local clinical trial or compassionate use program can proceed.
- **Rare disease strategy:** If the goal is to identify bromocriptine opportunities in rare diseases, the retinal dystrophy indication (rank 3) has the most scientifically credible rationale — retinal dopaminergic amacrine cells express D4 receptors with known neuroprotective functions, and one 2024 preclinical study (PMID [39009597](https://pubmed.ncbi.nlm.nih.gov/39009597/)) directly tested bromocriptine in a retinopathy model with positive results. This warrants a dedicated evidence assessment as a separate candidate report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

