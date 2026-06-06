---
layout: default
title: Isosorbide Mononitrate
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 10
---

# Isosorbide Mononitrate
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

Analyzing the Evidence Pack for Isosorbide mononitrate (DB01020) — noting key data points: top prediction is hypertrichosis (L5, zero evidence), Philippines market is unregistered, all safety fields are data gaps, and MOA is unavailable. The most mechanistically coherent prediction is PAH at Rank 10 (L4). Isosorbide mononitrate is a cardiovascular nitrate — **not antineoplastic** — so the Cytotoxicity section will be omitted.

---

# Isosorbide Mononitrate: From Angina Pectoris to Hypertrichosis

## One-Sentence Summary

Isosorbide mononitrate (ISMN) is a long-acting organic nitrate widely used for the prevention of angina pectoris and management of portal hypertension in coronary artery disease. The TxGNN model predicts it may be effective for **Hypertrichosis** (a condition of excessive or abnormal hair growth), yet **0 clinical trials** and **0 publications** currently support this direction. This prediction is grounded solely in a speculative mechanistic analogy to minoxidil and does not reflect any validated clinical or preclinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Angina pectoris / coronary artery disease (from general pharmacological knowledge; no Philippines registration on file) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, isosorbide mononitrate is an organic nitrate; it does not require hepatic biotransformation to a vasoactive metabolite and releases nitric oxide (NO) directly in vascular smooth muscle cells. NO activates soluble guanylate cyclase (sGC), elevates intracellular cyclic GMP (cGMP), and causes smooth muscle relaxation and vasodilation — the basis of its efficacy in angina and portal hypertension.

The TxGNN model's prediction for hypertrichosis most likely follows a knowledge-graph pathway of: ISMN → NO release → microvasculature dilation in the dermis → increased blood flow to the dermal papilla → hair follicle stimulation. This theoretical chain is analogous to minoxidil's mechanism — a potassium channel opener and vasodilator whose unexpected side effect of hypertrichosis directly led to the development of topical Rogaine. The model may have identified this shared "vasodilator → hair follicle perfusion" node in the graph and assigned a high score accordingly.

However, the analogy breaks down on closer inspection. Minoxidil achieves its dermatological effect through targeted topical application with negligible systemic absorption. Systemic ISMN carries well-known risks of generalised vasodilation, orthostatic hypotension, and reflex tachycardia — risks that far outweigh any speculative follicular benefit. More fundamentally, hypertrichosis is a condition of *excessive* hair growth, not hair loss; a vasodilator promoting hair growth would be counterproductive. There are no published clinical trials or preclinical studies examining ISMN in any hair-related disorder, and the Evidence Pack's repurposing rationale explicitly notes the absence of supporting data. The high TxGNN score reflects graph topology, not clinical plausibility.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Isosorbide mononitrate has no registered products with the Philippine FDA. No authorization records are on file, and the drug is classified as **not marketed** in the Philippines.

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Important note:** Key warnings, contraindications, and drug interaction data are all unavailable in the current Evidence Pack. This constitutes a **blocking data gap (DG001)** that prevents formal safety screening (Stage S1). A package insert review from a recognized regulatory authority (FDA Philippines, US FDA, or EMA) is required before any clinical planning proceeds.
>
> Of particular clinical relevance: isosorbide mononitrate, as an organic nitrate, is known to carry an absolute contraindication when co-administered with PDE5 inhibitors (sildenafil, tadalafil, vardenafil) due to the risk of severe hypotension. This is directly relevant to the PAH use case noted below.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top TxGNN-predicted indication, hypertrichosis, is supported by zero clinical trials and zero publications (L5), and the underlying mechanistic hypothesis is directionally inconsistent — ISMN promotes hair growth via vasodilation, whereas hypertrichosis is a disease of *excessive* hair growth requiring suppression, not stimulation. Combined with the complete absence of Philippines market presence and blocking safety data gaps, there is no basis to advance this candidate at this stage.

**Noteworthy secondary finding — Pulmonary Arterial Hypertension (Rank 10, L4):**
Among all 10 predicted indications, **PAH** presents the most scientifically coherent mechanistic rationale. ISMN's NO → sGC → cGMP axis directly overlaps with approved PAH drug mechanisms: riociguat (sGC stimulator) and sildenafil/tadalafil (PDE5 inhibitors) both act on the same pathway. A 2018 preclinical animal study (PMID 29705351) directly demonstrates sGC stimulation efficacy in a monocrotaline-induced PAH rat model, and a medicinal chemistry study (PMID 29377691) designed and tested an ISMN–bardoxolone methyl hybrid compound in PAH rats showing dual pulmonary vasodilation and vascular remodeling inhibition. Despite this, the **absolute contraindication with PDE5 inhibitors** (current PAH first-line therapy) represents a critical clinical barrier that must be resolved before PAH repurposing can be considered.

**To proceed, the following is needed:**

1. **Retrieve safety documentation** — Download and parse the package insert (Philippines FDA, US FDA, or EMA SmPC) to document warnings, contraindications, and drug interactions; this is a **blocking prerequisite** for Stage S1 safety screening
2. **Obtain formal MOA from DrugBank** — Query DrugBank API for DB01020 to populate the mechanism of action and drug category fields (currently a High-severity data gap)
3. **Clarify original registered indication** — Confirm at least one jurisdiction's approved indication to anchor the drug profile and enable mechanistic similarity scoring
4. **Re-evaluate indication ranking** — Consider deprioritising purely L5 hair/hair shaft predictions (Ranks 1–9) in favour of the PAH hypothesis (Rank 10), which has actual mechanistic literature support
5. **PAH feasibility assessment** — If PAH is selected for further development, specifically evaluate: (a) whether an inhalation or other non-systemic delivery route could bypass the PDE5i contraindication barrier, and (b) whether any patient subpopulations are PDE5i-naïve and thus eligible for ISMN co-administration
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

