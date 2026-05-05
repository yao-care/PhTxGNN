---
layout: default
title: Mesalazine
parent: 僅模型預測 (L5)
nav_order: 177
evidence_level: L5
indication_count: 7
---

# Mesalazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

---

# Mesalazine: From Ulcerative Colitis to Congenital Hypotrichosis with Juvenile Macular Dystrophy

## One-Sentence Summary

Mesalazine (5-ASA, mesalamine) is the active anti-inflammatory moiety of sulfasalazine, and is the cornerstone treatment for ulcerative colitis and other forms of inflammatory bowel disease.
The TxGNN model's highest-ranked prediction suggests Mesalazine may be effective for **congenital hypotrichosis with juvenile macular dystrophy**,
yet **no clinical trials** or **published literature** currently support this direction, placing the evidence at **L5 (model prediction only)**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ulcerative colitis / Inflammatory bowel disease (IBD) |
| Predicted New Indication | Congenital Hypotrichosis with Juvenile Macular Dystrophy |
| TxGNN Prediction Score | 99.65% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current evidence pack. Based on well-established pharmacology, Mesalazine (5-aminosalicylic acid, 5-ASA) is produced when sulfasalazine is cleaved by colonic bacteria. It exerts anti-inflammatory effects primarily through inhibition of the NF-κB signalling pathway — thereby suppressing pro-inflammatory cytokines including TNF-α, IL-1β, and IL-6 — and by blocking cyclooxygenase (COX) and lipoxygenase (LOX) pathways to reduce prostaglandin and leukotriene production. Its efficacy in ulcerative colitis and Crohn's disease is well-proven over decades of clinical use.

Congenital hypotrichosis with juvenile macular dystrophy (HJMD) is a rare autosomal recessive disorder caused by mutations in the *CDH3* gene, which encodes P-cadherin. Affected individuals develop sparse hair from birth and progressive macular retinal degeneration leading to early-onset visual impairment. The underlying pathology is fundamentally structural and genetic — P-cadherin dysfunction disrupts cell–cell adhesion in hair follicle stem cells and the retinal pigment epithelium — with no established inflammatory component as a driver of disease.

There is currently no published biological rationale linking Mesalazine's anti-inflammatory mechanism to CDH3 pathway dysfunction or macular degeneration. The high TxGNN prediction score most likely reflects a non-specific overlap of generalised inflammation nodes within the knowledge graph rather than any targeted biological relationship. This pattern is commonly observed for rare orphan diseases in graph-based prediction models, and this result should not be acted upon without first generating basic mechanistic evidence.

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
Despite a very high TxGNN score (99.65%), congenital hypotrichosis with juvenile macular dystrophy is a rare, genetically driven disease with no recognised inflammatory basis, and there is zero preclinical or clinical evidence that Mesalazine — or any anti-inflammatory agent — has any effect on CDH3 dysfunction or macular degeneration in this context.

**To proceed, the following is needed:**
- **Mechanistic feasibility study:** Determine whether NF-κB inhibition or 5-ASA's anti-inflammatory activity has any measurable effect on CDH3 expression, P-cadherin function, or retinal pigment epithelium integrity in cell or animal models
- **Knowledge graph audit:** Clarify which shared nodes are driving the elevated TxGNN score (likely non-specific inflammation hubs); if the link is solely via generic inflammation nodes, biological specificity is insufficient to justify further development
- **Complete MOA and safety documentation:** Full mechanism of action, key warnings, and contraindications for Mesalazine are currently unavailable and must be retrieved before any research initiation
- **Prioritise better-supported predictions:** Two other TxGNN predictions for Mesalazine carry substantially stronger evidence — **Osteoarthritis (L4, 3 publications including a 2024 *Nature Communications* mechanistic study)** and **Rheumatoid Arthritis (L3, 6 trials and 20 publications)** — and warrant evaluation reports of their own before resources are allocated to this L5 prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

