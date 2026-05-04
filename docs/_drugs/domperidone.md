---
layout: default
title: Domperidone
parent: 僅模型預測 (L5)
nav_order: 114
evidence_level: L5
indication_count: 1
---

# Domperidone
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

# Domperidone: From Antiemetic/Prokinetic to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Domperidone is a peripheral dopamine D2/D3 receptor antagonist widely recognized as an antiemetic and prokinetic agent for nausea, vomiting, and gastroparesis.
The TxGNN model predicts it may be effective for **Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD)**,
however, **no clinical trials or supporting publications** have been identified for this specific repurposing direction, making this a purely model-generated hypothesis at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Antiemetic / prokinetic (nausea, vomiting, gastroparesis) — not currently registered in the Philippines |
| Predicted New Indication | Nephrogenic Syndrome of Inappropriate Antidiuresis (NSIAD) |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L5 — Model prediction only; no clinical or published evidence found |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Domperidone in this context is not available from the Evidence Pack. Based on general pharmacological knowledge, Domperidone is a peripheral dopamine D2 and D3 receptor antagonist that does not readily cross the blood-brain barrier, and is primarily used for its prokinetic and antiemetic effects.

NSIAD is a rare genetic disorder caused by gain-of-function mutations in the *AVPR2* gene, encoding the renal vasopressin V2 receptor. This constitutive V2 receptor activation leads to inappropriate water reabsorption and hyponatremia independent of plasma osmolality. The potential mechanistic link may relate to dopaminergic modulation of renal tubular water transport: dopamine and its receptors (particularly D2-type) have been shown to influence aquaporin-2 (AQP2) trafficking in collecting duct cells, thereby modulating urinary concentration. Blocking these receptors with Domperidone could theoretically influence renal water handling, though whether this would be therapeutic or detrimental in NSIAD remains entirely speculative.

It must be emphasized that the TxGNN model's prediction is based on graph-based relationships in the biomedical knowledge graph, and the mechanistic plausibility has not been validated by any published preclinical or clinical study identified in this data pull. Without confirmed MOA data and supporting evidence, this prediction should be treated as a hypothesis-generation signal only.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Domperidone in Nephrogenic Syndrome of Inappropriate Antidiuresis.

---

## Literature Evidence

Currently no related literature available for Domperidone in Nephrogenic Syndrome of Inappropriate Antidiuresis.

---

## Philippines Market Information

Domperidone currently has **no registered products** with the Philippine FDA (Food and Drug Administration). There are zero active licenses on record, and the drug is classified as **not marketed** in the Philippines.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were retrievable from the current Evidence Pack for this candidate.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is entirely algorithm-generated (L5 evidence level) with no supporting clinical trials, observational studies, or published literature connecting Domperidone to NSIAD. Additionally, MOA data is unavailable, safety data is incomplete, and the drug has no regulatory foothold in the Philippines — making further development premature at this time.

**To proceed, the following is needed:**

- **MOA confirmation**: Retrieve full Domperidone mechanism of action from DrugBank API to assess whether renal dopaminergic pathways plausibly intersect with V2 receptor biology in NSIAD
- **Safety dossier**: Obtain Philippine FDA (or reference agency) package insert to assess key warnings, contraindications, and cardiac safety profile (Domperidone has known QTc prolongation risk that must be evaluated)
- **Targeted literature review**: Conduct manual PubMed search on broader terms (e.g., "dopamine receptor antagonist" + "SIADH OR NSIAD OR V2 receptor OR AQP2") to identify any preclinical mechanistic data
- **Expert consultation**: Engage a nephrologist or endocrinologist to assess biological plausibility before committing further resources
- **Philippines registration pathway**: If evidence emerges, evaluate FDA Philippines requirements for a drug not currently registered in-market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

