---
layout: default
title: Irbesartan
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 4
---

# Irbesartan
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

Using the `txgnn-pipeline` skill for context on report generation within the TxGNN ecosystem. Now generating the report based on the Evidence Pack.

---

# Irbesartan: From Hypertension to Malignant Renovascular Hypertension

## One-Sentence Summary

Irbesartan is an angiotensin II type 1 (AT1) receptor blocker belonging to the ARB class, widely used in the management of hypertension and hypertensive renal disease.
The TxGNN model predicts it may be effective for **Malignant Renovascular Hypertension**, with a prediction confidence of **99.31%**;
however, **no clinical trials or direct literature** specifically supporting this combination have been identified to date.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension / Hypertensive renal disease (ARB class; no registration found in Philippines) |
| Predicted New Indication | Malignant Renovascular Hypertension |
| TxGNN Prediction Score | 99.31% |
| Evidence Level | L4 (Mechanistic rationale; no clinical studies) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the Evidence Pack. Based on known pharmacological information, Irbesartan is an ARB (angiotensin II receptor blocker) that selectively antagonizes the AT1 receptor, thereby inhibiting the renin-angiotensin-aldosterone system (RAAS). This reduces vasoconstriction, lowers systemic blood pressure, decreases intraglomerular pressure, and suppresses aldosterone release — effects well established in hypertension and diabetic nephropathy.

Malignant renovascular hypertension arises from renal artery stenosis, which triggers intense, sustained RAAS overactivation: reduced renal perfusion drives renin secretion, which in turn elevates angiotensin II and activates AT1 receptors as the primary pressor pathway. Since this is exactly the signaling cascade Irbesartan is designed to block, the mechanistic link is highly plausible. For patients with *unilateral* renal artery stenosis and a normal contralateral kidney, ARB use is considered relatively safe and mechanistically well-founded.

However, a critical safety caveat substantially limits this application: in *bilateral* renal artery stenosis — or unilateral stenosis in a solitary functioning kidney — ARBs (including Irbesartan) dilate the efferent arteriole and thereby dramatically reduce GFR, risking acute kidney injury (AKI). This is a recognized contraindication for the ARB class. The TxGNN model appears to have captured the mechanistic plausibility of RAAS blockade in this disease, but the clinical application requires stringent anatomical subtyping before use can be considered.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Irbesartan in malignant renovascular hypertension.

---

## Literature Evidence

Currently no related literature available directly linking Irbesartan to malignant renovascular hypertension.

---

## Philippines Market Information

Irbesartan is currently **not marketed** in the Philippines. No product registrations were found in the regulatory database (total licenses: 0).

---

## Safety Considerations

No formal safety data (warnings, contraindications, drug interactions) was available in the Evidence Pack for this drug.

Please refer to the package insert for safety information.

> **Mechanistic Safety Flag (from repurposing rationale):** ARBs including Irbesartan are known to carry significant renal risk in the context of bilateral renal artery stenosis or stenosis of a solitary kidney — the very anatomical patterns most associated with renovascular hypertension. Any clinical investigation in this indication must include mandatory pre-treatment imaging (e.g., renal duplex ultrasound or CTA) to exclude bilateral stenosis, along with close renal function monitoring after initiation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the AT1 receptor blockade mechanism of Irbesartan aligns closely with the RAAS-driven pathophysiology of malignant renovascular hypertension, the absence of any clinical trial or published literature evidence — combined with a well-documented class-level contraindication in the most severe anatomical subtype (bilateral stenosis) — makes direct clinical application premature without further evidence generation and patient stratification.

**To proceed, the following is needed:**

- **MOA data:** Obtain complete DrugBank entry for Irbesartan to formally document mechanism and class-level evidence
- **Safety dossier:** Retrieve Philippines FDA package insert (or equivalent approved label) to identify formal contraindications, warnings, and drug interactions
- **Patient stratification framework:** Define eligibility criteria that exclude bilateral renal artery stenosis; imaging protocols must be mandated prior to any ARB initiation in this indication
- **Literature gap-fill:** Conduct targeted searches for ARB class evidence (losartan, valsartan, candesartan) in renovascular hypertension, which may serve as indirect support via class extrapolation
- **Preclinical or pilot data:** Identify any case series or observational data on ARBs in malignant renovascular hypertension to upgrade evidence from L4 to L3 before advancing to clinical feasibility assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

