---
layout: default
title: Metoprolol
parent: 僅模型預測 (L5)
nav_order: 185
evidence_level: L5
indication_count: 10
---

# Metoprolol
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

The txgnn-pipeline skill confirms this is within the TxGNN reporting workflow. Proceeding directly to generate the evaluation report following the Drug Repurposing Evaluation Report Prompt (v5) format.

---

# Metoprolol: From Hypertension & Heart Failure to Malignant Hypertensive Renal Disease

## One-Sentence Summary

Metoprolol is a cardioselective β1-adrenergic blocker with well-established use across cardiovascular medicine — including hypertension, angina, heart failure, and post-myocardial infarction management — though no original indication is formally listed in the Philippines regulatory data.
The TxGNN model predicts it may be effective for **Malignant Hypertensive Renal Disease**,
however **no clinical trials** and **no publications** are currently available to directly support this specific direction, leaving the prediction at the lowest evidence tier.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines regulatory data available; globally indicated for hypertension, heart failure, angina, and post-MI management |
| Predicted New Indication | Malignant Hypertensive Renal Disease |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Metoprolol is a cardioselective β1-adrenergic receptor antagonist. It lowers heart rate and cardiac output, reduces myocardial oxygen demand, and — most relevant here — suppresses renin secretion from the juxtaglomerular apparatus of the kidney, where β1 receptors are densely expressed. This renin-suppressing action provides the main theoretical bridge to renal disease: by attenuating RAAS activation and lowering systemic blood pressure, Metoprolol could in principle slow the hypertensive insult that drives malignant hypertensive renal injury.

Malignant hypertensive renal disease is a severe complication of uncontrolled hypertension, characterized by accelerated blood pressure crisis that causes acute renal injury, fibrinoid necrosis of arterioles, and thrombotic microangiopathy. The mechanistic step from a hypertension drug to this renal disease subtype is therefore not unreasonable in concept. However, in clinical practice, beta-blockers are not first-line agents for malignant hypertensive emergencies — calcium channel blockers (e.g., nicardipine, clevidipine), ACE inhibitors, and ARBs are preferred due to their faster, more reliable blood pressure reduction and direct renoprotective properties via the RAAS pathway.

The high TxGNN score (99.91%) most likely reflects the structural proximity between the "malignant hypertensive renal disease" node and the broader hypertension cluster in the knowledge graph — where Metoprolol is strongly represented — rather than a validated direct therapeutic relationship with this specific renal subtype. This is a purely computational prediction and should be interpreted with caution.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Metoprolol has no registered products in the Philippines as of the data cutoff date (May 5, 2026). No authorization numbers, product names, dosage forms, or approved indications are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no clinical trial or published literature directly supporting Metoprolol for malignant hypertensive renal disease, and beta-blockers are not established as standard of care for malignant hypertensive emergencies — where CCBs and RAAS inhibitors are preferred first-line agents with stronger evidence and direct renal-protective profiles.

**To proceed, the following is needed:**
- Retrieve full mechanism of action data (DrugBank API or Philippines package insert PDF)
- Conduct a targeted literature search on β1-selective blockade specifically in malignant hypertensive nephropathy
- Comparative effectiveness analysis against first-line agents (CCBs, ACEIs, ARBs) in this renal subtype
- Safety evaluation for Metoprolol use in patients with acute renal impairment and hypertensive crisis
- Assess Philippines regulatory pathway if supporting evidence is identified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

