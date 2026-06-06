---
layout: default
title: Lactulose
parent: 僅模型預測 (L5)
nav_order: 194
evidence_level: L5
indication_count: 8
---

# Lactulose
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

Using `txgnn-pipeline` to guide report generation for this PhTxGNN evidence pack.

---

# Lactulose: From Hepatic Encephalopathy to Acute Urate Nephropathy

## One-Sentence Summary

Lactulose is a non-absorbable disaccharide with well-established use in treating hepatic encephalopathy and constipation, working by acidifying colonic contents and suppressing intestinal ammonia production.
The TxGNN model predicts it may be effective for **Acute Urate Nephropathy**,
however, this prediction is currently supported by **no clinical trials** and **no publications** — mechanistic analysis indicates this is likely a knowledge-graph false positive.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hepatic encephalopathy / Constipation |
| Predicted New Indication | Acute Urate Nephropathy |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacological knowledge, Lactulose is a synthetic non-absorbable disaccharide. It is fermented by colonic bacteria into short-chain organic acids, which lowers the intraluminal pH. This acidification converts ammonia (NH₃) into ammonium ions (NH₄⁺), trapping them in the colon for fecal excretion. Its osmotic effect also accelerates stool transit, further reducing ammonia absorption — the basis for its use in hepatic encephalopathy. As an osmotic laxative, it draws water into the bowel to soften stool.

Acute urate nephropathy (AURN) is a distinct and largely unrelated condition, caused by the precipitation of uric acid crystals within the renal tubules, most commonly following tumor lysis syndrome from cytotoxic chemotherapy. The core pathophysiology involves massive, rapid overproduction of uric acid and its deposition in the kidney. The mechanism driving this disease — uric acid metabolism, xanthine oxidase activity, and renal tubular crystal deposition — has no known pharmacological intersection with Lactulose's gut-based, ammonia-lowering, or osmotic actions.

The TxGNN model assigns a high prediction score (99.89%) to this pairing, but the repurposing rationale in the Evidence Pack explicitly identifies this as a probable false positive, attributable to the spatial proximity of renal disease nodes to Lactulose-associated nodes within the knowledge graph. In the absence of any supporting mechanistic, preclinical, or clinical evidence, this prediction should not be advanced.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Lactulose currently has no product registrations with the Philippine FDA. No license records are available for review.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There is no preclinical or clinical evidence supporting Lactulose in acute urate nephropathy, and the mechanistic analysis strongly indicates this is a knowledge-graph adjacency artifact rather than a genuine therapeutic opportunity. The drug's pharmacological profile (intestinal pH acidification, osmotic laxative action, ammonia trapping) has no demonstrated relevance to uric acid overproduction or renal tubular crystal deposition.

**To proceed, the following is needed:**
- At least one preclinical study (e.g., animal model of tumor lysis syndrome–induced AURN) demonstrating a pharmacological effect of Lactulose on uric acid handling or renal tubular function
- A plausible mechanistic hypothesis linking Lactulose to uric acid metabolism (currently absent)
- Philippine FDA product registration as a prerequisite for any future clinical development pathway
- Detailed MOA data from DrugBank to formally document the mechanism gap
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

