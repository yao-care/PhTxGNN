---
layout: default
title: Artemether
parent: Model Prediction Only (L5)
nav_order: 30
evidence_level: L5
indication_count: 10
---

# Artemether
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

# Artemether: From Antimalarial Use to Acquired Angioedema

## One-Sentence Summary

Artemether is an artemisinin-class antimalarial. The data compiled for this report do not record an approved indication in the Philippines.
The TxGNN model predicts it may be effective for **acquired angioedema**, but **0 clinical trials** and **0 publications** support this prediction, so it rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Philippines license data (antimalarial by drug class) |
| Predicted New Indication | Acquired angioedema |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Artemether belongs to the artemisinin class. Its efficacy in malaria is well established, with the endoperoxide bridge generating reactive radicals inside the parasite.

No mechanistic link to acquired angioedema is established. The high TxGNN score (0.999) is a knowledge-graph prediction only. A speculative rationale could be the anti-inflammatory or immunomodulatory effects reported preclinically for artemisinins. Nothing in the compiled data supports it, and no trials or publications were identified. The prediction should be treated as a hypothesis, not as evidence of benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0026 | Artemether (single-ingredient) | Cancelled |

No dosage form or approved indication text is recorded for this registration. There is currently no valid marketing authorization in the Philippines.

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease edges, not label text): long QT syndrome, familial long QT syndrome, torsades de pointes, and potassium deficiency disease. These point to QT-prolongation risk and need confirmation against the product label.
- **Drug Interactions**: 95 interactions were identified.
  - **Major**: clarithromycin, cobicistat, amprenavir, apalutamide, atazanavir, boceprevir.
  - **Moderate (examples)**: dexamethasone, miconazole, deferasirox, bosentan, brigatinib, fostamatinib.

Please refer to the package insert for label warnings and contraindications, which were not available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Acquired angioedema is supported only by a model prediction (L5), with no trials, no literature, and no plausible documented mechanism. The only Philippines registration is cancelled, and QT-related safety signals exist.

Other predictions in the same data set (*Plasmodium falciparum* malaria and malaria) have L1 evidence from many completed trials and reviews. These reflect established antimalarial use (mostly artemether-lumefantrine) rather than true repurposing. If this drug is pursued, they are the better-supported candidates and should be assessed separately.

**To proceed, the following is needed:**
- Preclinical or mechanistic evidence linking artemether to bradykinin-mediated or acquired angioedema
- Package insert warnings and contraindications, particularly QT-prolongation guidance
- Mechanism of action data from DrugBank
- Clarification of the regulatory status after the cancelled registration, and of any available dosage forms
- A QT and interaction risk assessment for any proposed new-indication population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

