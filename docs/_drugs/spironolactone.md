---
layout: default
title: Spironolactone
parent: 僅模型預測 (L5)
nav_order: 313
evidence_level: L5
indication_count: 2
---

# Spironolactone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Spironolactone: From Aldosterone Antagonism to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Spironolactone is a well-established aldosterone receptor antagonist and potassium-sparing diuretic, widely used globally for heart failure, hypertension, and hyperaldosteronism, and recognized for its anti-androgenic properties in conditions such as androgenetic alopecia and hirsutism.
The TxGNN model predicts it may be effective for **Hypotrichosis Simplex of the Scalp**, a rare hereditary hair loss disorder driven by genetic defects in the lysophosphatidic acid signaling pathway.
However, **no clinical trials or published literature** currently support this indication, and the mechanistic rationale is weak.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Spironolactone is an aldosterone receptor antagonist (mineralocorticoid receptor blocker) with well-characterized anti-androgenic activity. By competitively inhibiting dihydrotestosterone (DHT) binding to androgen receptors in hair follicles, it has an established off-label role in androgenetic alopecia, female pattern hair loss, acne, and hirsutism. The TxGNN model likely exploited this recognized hair-follicle connection, extending it through graph-based phenotypic proximity to other conditions in the "hair loss" disease cluster.

However, hypotrichosis simplex of the scalp is a mechanistically distinct condition from androgenetic alopecia. It arises from loss-of-function mutations in *LPAR6* (lysophosphatidic acid receptor 6) or *LIPH* (lipase H), impairing the lysophosphatidic acid (LPA) signaling pathway that is essential for hair follicle morphogenesis. This is a structural developmental defect — not a hormone-dependent or inflammatory process — and there is no established pharmacological intersection between Spironolactone's mineralocorticoid antagonism or androgen receptor blockade and the LPA pathway.

The high TxGNN score (99.26%) most likely reflects graph-topology proximity to other hair-related phenotypes rather than a genuine mechanistic link. Without any supporting trial or literature evidence, and with a mechanistic rationale that is currently unsubstantiated, this prediction should be treated as a hypothesis-generating signal only and not as an actionable repurposing candidate at this stage.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Spironolactone currently has no drug licenses registered with the Philippines FDA and is not marketed in the Philippines. No approved indication text is available from domestic registration records.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This is a pure model-prediction signal (L5 evidence) with zero supporting clinical trials or published literature. The target disease is driven by a genetic defect in the LPA signaling pathway, which has no known overlap with Spironolactone's pharmacological mechanisms; the prediction is most likely an artifact of phenotypic graph proximity rather than a true mechanistic relationship.

**To proceed, the following is needed:**
- Retrieve Spironolactone MOA data from DrugBank to formally characterize whether any secondary mechanisms could intersect with the LPAR6/LIPH pathway
- Conduct a broader literature search for any preclinical or case-report evidence linking aldosterone antagonism or anti-androgen activity to LPA pathway hair disorders
- Obtain Philippines FDA package insert (or equivalent international labeling) to complete safety, contraindication, and drug interaction assessment
- Expert pharmacological review to determine whether the graph-proximity prediction warrants any targeted in vitro mechanistic investigation
- Note: A second TxGNN prediction — **Congenital Hypotrichosis Milia** (score 99.04%, rank 6252) — shares the same evidence gap and mechanistic weakness as the primary prediction and should be evaluated under the same Hold decision pending the above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

