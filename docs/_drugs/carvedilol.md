---
layout: default
title: Carvedilol
parent: 僅模型預測 (L5)
nav_order: 61
evidence_level: L5
indication_count: 5
---

# Carvedilol
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

# Carvedilol: From Hypertension / Heart Failure to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Carvedilol is a non-selective β1/β2-adrenergic blocker with additional α1-adrenergic blocking activity, conventionally used for systemic hypertension and chronic heart failure.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**, with **0 clinical trials** and **0 publications** currently providing direct evidence for this specific repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; Chronic Heart Failure (no Philippines registration data on file) |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.55% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data is not available in this Evidence Pack. Based on information embedded in the repurposing rationale, Carvedilol exerts its effects through combined β1/β2 and α1-adrenergic receptor blockade. The β-blocking component reduces heart rate and cardiac output, while the α1-blocking component lowers peripheral vascular resistance — together producing a sustained reduction in systemic blood pressure. An additional pharmacological property is suppression of renin release from the juxtaglomerular apparatus via β1-blockade, which attenuates activation of the renin–angiotensin–aldosterone system (RAAS).

Malignant hypertensive renal disease is an end-organ complication of severely uncontrolled hypertension, characterised by fibrinoid necrosis of small renal arterioles, thrombotic microangiopathy, and rapidly progressive renal impairment. The theoretical mechanistic bridge is plausible: reducing systemic blood pressure and renal perfusion pressure through dual adrenergic blockade, combined with RAAS suppression, could in principle slow progressive glomerular injury. Both the cardiovascular and renal damage in this condition share a common upstream driver — catecholamine excess and RAAS over-activation — which Carvedilol addresses pharmacologically.

However, the mechanistic link remains theoretical. Malignant hypertensive renal disease is a high-acuity clinical emergency typically managed with intravenous antihypertensives and RAAS inhibitors as first-line therapy. No randomised or observational study has directly evaluated Carvedilol in this specific condition. The TxGNN score of 99.55% (ranked 3,602 among all candidate disease associations) most likely reflects knowledge-graph structural proximity rather than independently validated biological evidence, and should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Carvedilol is currently **not registered** with the FDA Philippines. No product licenses, approved indications, or dosage form records are on file.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Philippines FDA package insert data (warnings, contraindications) was identified as a blocking data gap in this Evidence Pack. Safety evaluation cannot be completed without this information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for Carvedilol in malignant hypertensive renal disease is currently limited to mechanistic reasoning only (L4 — no clinical trials, no supporting publications). Additionally, the use of β-blockers in certain renal hypertensive states carries recognised safety concerns (e.g., potential worsening of renal perfusion in bilateral renal artery stenosis), and the package insert data needed for a formal safety screening are not yet available for the Philippines market.

**To proceed, the following is needed:**

- **Philippines FDA package insert** — obtain warnings, contraindications, and dosing guidance for renal impairment (currently a blocking data gap)
- **Formal MOA documentation** — confirm β/α-adrenergic receptor pharmacology via DrugBank API query
- **Targeted literature search** — systematic search for Carvedilol or third-generation β-blockers in hypertensive nephropathy or malignant hypertension case series
- **Preclinical evidence review** — assess whether any animal models of malignant hypertension have evaluated Carvedilol
- **Philippines registration pathway** — if evidence is strengthened, evaluate regulatory feasibility given current zero-registration status
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

