---
layout: default
title: Telmisartan
parent: 僅模型預測 (L5)
nav_order: 324
evidence_level: L5
indication_count: 10
---

# Telmisartan
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

# Telmisartan: From Hypertension to Prinzmetal Angina

## One-Sentence Summary

Telmisartan is an angiotensin II type 1 receptor blocker (ARB) widely established for hypertension management globally, though it is not currently registered in the Philippines.
The TxGNN model predicts it may have therapeutic potential for **Prinzmetal Angina** (variant angina caused by coronary artery spasm),
however this prediction rests on model inference alone, with **no clinical trials or publications** identified to support this specific application.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Philippines; globally established for Hypertension |
| Predicted New Indication | Prinzmetal Angina |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, telmisartan is an angiotensin II type 1 receptor (AT1R) blocker. By competitively inhibiting AT1R, telmisartan reduces angiotensin II–mediated vasoconstriction and aldosterone secretion. Its vasodilatory and potential anti-inflammatory properties form the theoretical basis for this TxGNN prediction.

Prinzmetal angina (variant angina) is characterised by episodic coronary artery spasm causing transient myocardial ischaemia, typically occurring at rest rather than with exertion. The theoretical rationale is that AT1R blockade could attenuate angiotensin II–mediated coronary vasoconstriction. However, the dominant drivers of Prinzmetal angina are α-adrenergic hyperactivity, endothelin-1 elevation, and thromboxane A2 (TXA2)–induced smooth muscle contraction — pathways largely independent of the renin-angiotensin system. The mechanistic connection between AT1R blockade and Prinzmetal angina is therefore considered weak.

Given the complete absence of clinical or preclinical evidence linking telmisartan to Prinzmetal angina, this prediction most likely reflects network proximity within the TxGNN knowledge graph rather than a pharmacologically established relationship.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Telmisartan is not currently registered in the Philippines. No product authorisations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.98%), the mechanistic link between AT1R blockade and Prinzmetal angina is weak — the primary disease drivers (α-adrenergic overactivity, endothelin-1, TXA2) are not principal targets of telmisartan — and no clinical or preclinical evidence supports this specific repurposing direction.

**To proceed, the following is needed:**
- Preclinical studies specifically examining telmisartan's effect on coronary artery spasm models
- Mechanistic studies characterising the role of angiotensin II in Prinzmetal angina pathophysiology
- MOA documentation and Philippines/TFDA package insert data to enable safety profiling
- Philippines regulatory registration pathway assessment before any clinical use

---

> **Broader Evidence Note — Higher-Priority Indication Identified**
>
> Among all 10 TxGNN-predicted indications in this evaluation, **intracerebral hemorrhage** (Rank 9, TxGNN score 99.93%) carries substantially stronger evidence:
>
> - A completed **Phase 3 RCT** (TRIDENT; [NCT02699645](https://clinicaltrials.gov/study/NCT02699645), n = 1,671) tested a telmisartan 80 mg–based triple combination pill for secondary prevention of recurrent intracerebral haemorrhage.
> - **Evidence Level: L2** | **Recommendation: Proceed with Guardrails**
> - Supporting animal studies consistently demonstrate AT1R blockade reduces ICH-related neuronal apoptosis, cerebral vasospasm, and neuroinflammation (e.g., PMID [17538008](https://pubmed.ncbi.nlm.nih.gov/17538008/), PMID [27078703](https://pubmed.ncbi.nlm.nih.gov/27078703/)).
>
> **This indication warrants priority consideration** for a dedicated full evaluation report.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

