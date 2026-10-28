---
layout: default
title: Finasteride
parent: Model Prediction Only (L5)
nav_order: 143
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-28
description: "Finasteride: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
monitor_inn: "Finasteride"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "familial isolated trichomegaly"]
---

# Finasteride
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Finasteride: From Benign Prostatic Hyperplasia to Ambras type hypertrichosis universalis congenita
{: .text-alpha }

## One-Sentence Summary

Finasteride was originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **hypertrichosis** (the highest-ranked prediction with any literature support), but there are **0 clinical trials** and only **4 indirect publications** (narrative reviews and a methods paper), so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita (top-ranked prediction); hypertrichosis is the best-supported alternative |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 (L4 for hypertrichosis) |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacological knowledge, finasteride is a 5-alpha reductase inhibitor that lowers dihydrotestosterone (DHT). Its efficacy in BPH is established, and it is also used in androgenetic alopecia.

The top-ranked prediction, Ambras type hypertrichosis universalis congenita, is a congenital condition linked to genomic rearrangements affecting TRPS1 regulation. Its hair overgrowth is not clearly androgen-driven, so a mechanistic link is speculative. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Hypertrichosis is by definition androgen-independent hair growth, so a DHT-lowering mechanism has limited rationale. Finasteride is more relevant to hirsutism, which is androgen-dependent. The other predictions are weaker still:

- Malformation syndrome with odontal and/or periodontal component: no clear rationale; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.
- Syndrome with Dandy-Walker malformation: no plausible mechanism, and finasteride's teratogenic concerns (effects on male fetal genital development) argue against developmental-disorder use.
- Isolated genetic hair shaft abnormality: structural defects are generally not DHT-dependent.
- Familial isolated trichomegaly (score 0.9915): no established androgen-dependent mechanism.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The following publications were retrieved for hypertrichosis. None is a trial of finasteride in hypertrichosis, so the evidence is indirect.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12223963](https://pubmed.ncbi.nlm.nih.gov/12223963/) | 2002 | Review | Annales de dermatologie et de venereologie | Hypertrichosis is hair growth in non-androgen-dependent areas; causes include drugs (minoxidil, ciclosporine, diazoxide, glucocorticoids), metabolic, nutritional and paraneoplastic factors. Hormone monitoring is not needed, unlike in hirsutism. |
| [10330884](https://pubmed.ncbi.nlm.nih.gov/10330884/) | 1999 | Review | Therapeutische Umschau | Reviews new treatments for androgenetic alopecia and hirsutism, including oral treatment of male pattern hair loss. |
| [12942187](https://pubmed.ncbi.nlm.nih.gov/12942187/) | 2003 | Review | Der Hautarzt | Notes finasteride for male pattern hair loss and laser-assisted hair removal for hypertrichosis and hirsutism. |
| [12444520](https://pubmed.ncbi.nlm.nih.gov/12444520/) | 2002 | Methods/Technical report | Der Hautarzt | Describes TrichoScan, a digital hair analysis tool for monitoring hair loss and treatment response. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0191 | Finasteride | Not specified | Not specified (registration valid) |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: liver disease and gallbladder disease.
- **Drug Interactions**: 100 potential interactions were identified in the DDI database, but all listed entries have an unclassified severity level. Examples include calcitriol, doxycycline, clotrimazole, dolasetron, dicyclomine, famotidine, acetylsalicylic acid, amoxicillin, bupropion, pantoprazole, glimepiride, metformin, omeprazole, morphine and rosiglitazone. Clinical significance has not been established.
- **Other**: Teratogenic concerns (effects on male fetal genital development) have been noted in relation to developmental-disorder indications.

Please refer to the package insert for further safety information, including key warnings.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN scores are very high, but there are no clinical trials, and the only literature is indirect. Hypertrichosis is androgen-independent, so the DHT-lowering mechanism has limited rationale. The Philippines registration is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- Philippines package insert warnings and contraindications (a blocking gap for safety screening)
- Direct clinical or preclinical evidence of finasteride in hypertrichosis or the other predicted conditions
- Clarification of the current Philippines regulatory status, since the only registration is cancelled
- Review of the ~100 drug interactions for severity, since all are currently unclassified
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

