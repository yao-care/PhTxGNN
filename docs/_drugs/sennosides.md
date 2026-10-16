---
layout: default
title: Sennosides
parent: Model Prediction Only (L5)
nav_order: 309
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Sennosides: predicted new indication Hypotrichosis simplex of the scalp (evidence level L5). Approved use: Not available in the license data (sennosides are generally known as…"
---

# Sennosides
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Sennosides: From Laxative Use to Hypotrichosis Simplex of the Scalp

## One-Sentence Summary

Sennosides are anthraquinone stimulant laxatives, and the Philippines license data compiled for this report does not list an approved indication.
The TxGNN model predicts they may be effective for **hypotrichosis simplex of the scalp**, with a very high score, but **0 clinical trials** and **0 publications** support this prediction.
It is a computational association only, with no biological or clinical support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the license data (sennosides are generally known as stimulant laxatives) |
| Predicted New Indication | Hypotrichosis simplex of the scalp |
| TxGNN Prediction Score | 99.29% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, sennosides A and B are converted by gut bacteria into rheinanthrone, which acts on the colon to stimulate bowel movement. This is the basis of their use as a laxative.

Hypotrichosis simplex of the scalp is a genetic hair follicle disorder (for example, variants in CDSN, APCDD1 or RPL21). No mechanistic link has been established between a colonic stimulant laxative and hair follicle biology. The high TxGNN score most likely reflects similarity within the knowledge graph rather than a biological rationale.

Other top predictions show the same pattern, with no supporting evidence for any of them:

| Rank | Predicted Indication | TxGNN Score | Note |
|------|------|------|------|
| 2 | Congenital hypotrichosis milia | 99.23% | Rare congenital condition, no plausible mechanism |
| 3 | Diffuse alopecia areata | 99.12% | Autoimmune, T-cell-mediated; sennosides have no known immunomodulatory action and low systemic absorption |
| 4 | Open-angle glaucoma | 99.11% | No link to intraocular pressure or retinal ganglion cell protection |
| 5 | Primary hereditary glaucoma | 99.10% | Genetic outflow defect; no pharmacological rationale |
| 6 | Alopecia | 99.10% | Shared across related hair-loss terms, likely a graph-neighborhood artifact |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0070 | Calcium Sennosides | Not specified | Not specified (status: cancelled) |

## Safety Considerations

Please refer to the package insert for safety information.

No drug-drug interaction records were found in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no clinical trials, no literature and no plausible mechanism. In addition, the only Philippines registration has been cancelled, and its indication and safety information are missing.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank and a plausible biological link to hair follicle or ocular disease
- Preclinical or clinical evidence for any of the predicted indications
- Package insert warnings and contraindications from DOH-FDA Philippines
- Clarification of the cancelled registration status and the approved indication
- Assessment of route and formulation compatibility (an oral laxative versus the routes required for hair or eye conditions)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

