---
layout: default
title: Travoprost
parent: 僅模型預測 (L5)
nav_order: 341
evidence_level: L5
indication_count: 10
---

# Travoprost
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

# Travoprost: From Glaucoma/Ocular Hypertension to Visceral Calciphylaxis

## One-Sentence Summary

Travoprost is a synthetic prostaglandin FP receptor agonist, clinically established for reducing intraocular pressure in glaucoma and ocular hypertension.
The TxGNN model predicts it may be effective for **Visceral Calciphylaxis**;
however, there are currently **0 clinical trials** and **0 publications** directly supporting this direction, and the mechanistic connection is extremely weak — this is a pure model prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Glaucoma / Ocular Hypertension (inferred from clinical evidence; not registered in Philippines) |
| Predicted New Indication | Visceral Calciphylaxis |
| TxGNN Prediction Score | 99.9998% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Travoprost is a synthetic prostaglandin F2α (PGF2α) analogue that selectively activates the FP receptor (prostaglandin F receptor). Its efficacy in lowering intraocular pressure in glaucoma and ocular hypertension has been well established — primarily by increasing uveoscleral aqueous humor outflow — across numerous Phase 3 and Phase 4 clinical trials.

Visceral calciphylaxis is a rare and life-threatening condition characterised by progressive calcification and thrombotic occlusion of small vessels in internal organs, driven by dysregulated calcium-phosphate metabolism and vascular wall inflammation. While prostaglandins broadly participate in vascular tone regulation, inflammation, and angiogenesis, the specific FP receptor agonist pathway activated by travoprost has no established role in the pathophysiology of calciphylaxis. Systemic PGF2α effects are vasoconstrictive — the opposite of the localised vasodilatory response observed in ocular tissue — and the antithrombotic mechanisms most relevant to calciphylaxis (the PGI2/TXA2 axis) are not modulated by FP receptor activation.

This prediction appears to be a topological artifact of the TxGNN knowledge graph, where travoprost may sit in proximity to vascular disease nodes without any causal biological link. No mechanistic rationale connecting this drug to visceral calciphylaxis has been identified, and the model score alone is insufficient to justify clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is zero clinical or preclinical evidence that travoprost has any effect on visceral calciphylaxis, and the mechanistic rationale is implausible given that FP receptor agonism in systemic vessels produces vasoconstriction rather than the vasodilatory or anticalcification effects that would be needed. With L5 evidence and no actionable biological hypothesis, there is no basis for further repurposing development toward this indication.

**To proceed, the following is needed:**
- Basic pharmacological studies establishing FP receptor expression and functional activity in calciphylaxis-relevant vascular tissues
- Mechanistic evidence linking prostaglandin FP signalling to calcium-phosphate dysregulation or small-vessel thrombosis
- Formal MOA documentation retrieved from DrugBank API (currently missing)
- Safety profile data including package insert warnings and contraindications (currently missing)
- Reconsidering whether the broader **vascular disease** indication (TxGNN Rank 5, L4 evidence, 15 trials) merits a separate focused evaluation — as it has a more credible mechanistic anchor (travoprost demonstrably affects retinal and choroidal blood flow per NCT00308945) and substantially more supporting data
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

