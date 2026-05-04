---
layout: default
title: Donepezil
parent: 僅模型預測 (L5)
nav_order: 115
evidence_level: L5
indication_count: 8
---

# Donepezil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Donepezil: From Alzheimer's Disease to Psychogenic Movement Disorders

## One-Sentence Summary

Donepezil is a well-established acetylcholinesterase inhibitor (AChEI) widely used in the treatment of Alzheimer's disease. The TxGNN model predicts it may be effective for **Psychogenic Movement Disorders**, though this prediction is currently supported by **0 clinical trials** and **0 publications** — making it a model-level signal only, with no empirical evidence to substantiate the prediction at this stage.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Alzheimer's Disease |
| Predicted New Indication | Psychogenic Movement Disorders |
| TxGNN Prediction Score | 99.23% |
| Evidence Level | L5 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on well-established pharmacological knowledge, Donepezil is a selective and reversible inhibitor of acetylcholinesterase (AChE), the enzyme responsible for breaking down acetylcholine (ACh) in synaptic clefts. By blocking AChE, Donepezil elevates ACh concentrations throughout the central nervous system — particularly in the cortex and hippocampus — which underlies its therapeutic benefit in Alzheimer's disease via the cholinergic hypothesis of cognitive decline.

Psychogenic movement disorders (PMDs), however, represent a fundamentally different pathological process. They are classified as functional neurological disorders (FND), driven by abnormal functional brain connectivity, maladaptive motor predictions, and psychological factors — not by a cholinergic deficit. There is no established biological rationale linking AChEI activity to the core pathophysiology of PMDs.

The notably high TxGNN score (99.23%) is likely an artifact of knowledge graph topology — specifically, "neighbor propagation" effects that associate Donepezil with broad "movement disorder" nodes due to its known roles in Alzheimer's-related motor symptoms, Lewy body dementia, and drug-induced movement side effects. This is a recognized limitation of graph neural network-based models and warrants caution: a high model score does not imply clinical plausibility for this specific indication.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Donepezil in psychogenic movement disorders.

---

## Literature Evidence

Currently no related literature available for Donepezil in psychogenic movement disorders.

---

## Philippines Market Information

Donepezil is currently **not registered** with the Philippine FDA. There are **no approved products** in the Philippine drug registry. Any clinical development or compassionate use of this drug in the Philippines would require new drug registration prior to use.

---

## Safety Considerations

Please refer to the package insert for safety information. Full safety data — including Philippine FDA (FDA Philippines) package insert warnings, contraindications, and drug–drug interaction profiles — were not available in this Evidence Pack and should be retrieved before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial evidence or published literature supporting Donepezil for psychogenic movement disorders, and no established biological mechanism links acetylcholinesterase inhibition to the pathophysiology of functional neurological disorders. The high TxGNN score most likely reflects graph-level noise rather than a genuine pharmacological signal.

**To proceed, the following is needed:**
- Retrieve Donepezil's full mechanism of action data from DrugBank (DB00843) to enable rigorous mechanistic plausibility assessment
- Obtain the Philippine FDA package insert (or equivalent label) to complete the safety evaluation — currently a **blocking data gap**
- Conduct a targeted literature search for cholinergic modulation in functional neurological disorders / psychogenic movement disorders specifically
- Consider re-prioritizing downstream analysis to Rank 8 (**Lingual-Facial-Buccal Dyskinesia**, L3, "Proceed with Guardrails"), which is supported by two Cochrane systematic reviews and has an established cholinergic mechanistic rationale — making it the strongest repurposing candidate in this Evidence Pack
- Philippine FDA drug registration is a prerequisite before any clinical development pathway can be initiated in the Philippines

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

