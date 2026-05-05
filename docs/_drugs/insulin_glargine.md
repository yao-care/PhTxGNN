---
layout: default
title: Insulin Glargine
parent: 僅模型預測 (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
---

# Insulin Glargine
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

The txgnn-pipeline skill confirms the context. Now let me generate the evaluation report from the Evidence Pack.

---

# Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis

## One-Sentence Summary

Insulin glargine is a long-acting basal insulin analog established as a cornerstone therapy for glycemic control in Type 1 and Type 2 diabetes mellitus.
The TxGNN model predicts it may be relevant to **Autoimmune Oophoritis**, with **0 clinical trials** and **0 publications** currently supporting this direction — the association is inferred entirely from autoimmune endocrine comorbidity patterns in the knowledge graph, not from direct therapeutic evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Diabetes mellitus (Type 1 & Type 2); no Philippines license record available |
| Predicted New Indication | Autoimmune Oophoritis |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on established pharmacology, insulin glargine is a modified insulin analog with a prolonged, peakless absorption profile (~24 hours), primarily designed to mimic physiological basal insulin secretion and suppress hepatic glucose output in patients with insufficient endogenous insulin production.

Autoimmune oophoritis is an autoantibody-mediated inflammatory destruction of ovarian follicles, frequently encountered not in isolation but as part of **Polyglandular Autoimmune Syndrome Type II (APS-II)** — a clustering of autoimmune endocrine disorders including Type 1 diabetes mellitus (T1DM), Addison's disease, and autoimmune thyroid disease. TxGNN most likely identified this connection by traversing the APS-II comorbidity sub-graph: patients who develop autoimmune oophoritis have elevated rates of T1DM, and T1DM patients routinely receive insulin glargine. The knowledge graph therefore places insulin glargine in close proximity to autoimmune oophoritis through shared patient populations and shared immune targets (anti-GAD65, anti-islet autoantibodies).

However, this is an **indirect, comorbidity-driven association**, not a mechanistic repurposing signal. Insulin glargine acts on insulin receptors to regulate glucose metabolism; it has no known direct effect on ovarian autoimmunity, anti-ovarian antibody titers, or follicular preservation. Any use of insulin glargine in a patient with autoimmune oophoritis would reflect concurrent T1DM management, not treatment of the oophoritis itself.

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
The TxGNN score of 99.88% reflects strong knowledge-graph connectivity through the APS-II comorbidity network — not evidence of therapeutic efficacy for autoimmune oophoritis per se. With zero supporting clinical trials or publications (L5), and no plausible direct mechanism, this prediction does not meet the threshold for active repurposing exploration at this time.

**To proceed, the following is needed:**
- Clarify the clinical question: if the goal is *insulin replacement in APS-II patients who concurrently have T1DM and autoimmune oophoritis*, that is already established practice and requires no repurposing effort
- If the goal is *insulin glargine as a disease-modifying agent for autoimmune oophoritis itself*, a pre-clinical study examining insulin signaling effects on ovarian immune microenvironment would be the minimum first step
- Obtain full MOA data from DrugBank API (DG002) to rule out any immunomodulatory off-target activity
- Obtain Philippines package insert or equivalent label (DG001) to assess contraindications and warnings before any clinical protocol is considered
- Register the drug with FDA Philippines if future clinical use is intended — currently no active registrations exist
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

