---
layout: default
title: Neostigmine
parent: Model Prediction Only (L5)
nav_order: 248
evidence_level: L5
indication_count: 7
last_modified_at: 2026-11-12
monitor_inn: "Neostigmine"
predicted_indications: ["autoimmune disease of peripheral nervous system", "disease of receptor activity", "hypersplenism (disease)", "atypical hemolytic-uremic syndrome with B factor anomaly", "bronchitis", "fetal akinesia deformation sequence", "myasthenia, congenital, refractory to acetylcholinesterase inhibitors"]
description: "Neostigmine: predicted new indication Autoimmune disease of peripheral nervous system (evidence level L5). Approved use: Not recorded in the local data"
---

# Neostigmine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Neostigmine: Autoimmune disease of peripheral nervous system
{: .text-alpha }

## One-Sentence Summary

Neostigmine is a cholinesterase inhibitor originally used to treat myasthenia gravis and related neuromuscular junction disorders.
There are currently **0 clinical trials** and **0 publications** specific to this subtype, so support is indirect and rests on the parent myasthenia gravis indication.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Autoimmune disease of peripheral nervous system |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, neostigmine is a reversible acetylcholinesterase inhibitor. It raises acetylcholine levels at the neuromuscular junction, which compensates for the reduced number of available receptors in myasthenia gravis.

Thymic hyperplasia is a common pathological subtype of acetylcholine receptor antibody-positive myasthenia gravis. The mechanism therefore applies directly. This prediction is better described as a subtype of an established use than as a true repurposing target.

No trials or literature were retrieved specifically for this subtype. The rationale is inferred from the parent myasthenia gravis indication.

### Other Predicted Indications (Context)

The model produced other high-scoring predictions, but the evidence for them is weak:

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 3 | Autoimmune disease of peripheral nervous system | 0.9997 | L5 | Literature is mostly myasthenia gravis mechanistic, historical and animal work. The rationale is weak outside myasthenia gravis. |
| 5 | Disease of receptor activity | 0.9996 | L5 | Too broad to act on. |
| 6 | Hypersplenism | 0.9987 | L5 | No mechanistic link found. |
| 7 | Atypical hemolytic-uremic syndrome with B factor anomaly | 0.9983 | L5 | Unrelated mechanism. Likely a TxGNN model (deep learning) artifact. |
| 8 | Bronchitis | 0.9979 | L4 | Increased cholinergic tone may worsen bronchial symptoms. Evidence is anecdotal and outdated. |
| 9 | Fetal akinesia deformation sequence | 0.9972 | L5 | Speculative link, with major safety concerns in fetal use. |
| 10 | Congenital myasthenia refractory to acetylcholinesterase inhibitors | 0.9937 | L5 | Contradicts the disease definition and is likely a false positive. |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was retrieved for the top-ranked indication. The closest supporting items come from the related predictions above:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27854225](https://pubmed.ncbi.nlm.nih.gov/27854225/) | 2016 | Review | J Neuromuscul Dis | Unusual presentations and diagnostic pitfalls of myasthenia gravis. It contains no neostigmine-specific efficacy data. |
| [40544117](https://pubmed.ncbi.nlm.nih.gov/40544117/) | 2025 | Review | Disease-a-Month | Comprehensive review of myasthenia gravis treatment options. |
| [9535308](https://pubmed.ncbi.nlm.nih.gov/9535308/) | 1998 | Case report | Pediatr Neurol | A preterm newborn with transient neonatal myasthenia gravis was treated with neostigmine, exchange transfusions and high-dose IVIG. |
| [23460475](https://pubmed.ncbi.nlm.nih.gov/23460475/) | 2013 | Animal study | Muscle Nerve | Crotamine was compared with neostigmine on neuromuscular transmission in myasthenic rats. |
| [1179220](https://pubmed.ncbi.nlm.nih.gov/1179220/) | 1975 | Animal study | Science | Mice given myasthenic patient immunoglobulin showed decremental responses that neostigmine reversed. |

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Neostigmine | Injection |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Disease associations flagged as potential contraindications** (from knowledge-graph data, not label text): epilepsy, peptic ulcer disease, asthma (including intrinsic and allergic), sudden cardiac arrest, heart conduction disease, peritonitis, hyperthyroidism (including Graves disease and thyrotoxicosis), urinary tract obstruction, and Hirschsprung disease and related syndromes (including Mowat-Wilson syndrome).
- **Drug Interactions**: 47 interactions were found in total. One is rated Major and the rest shown are Moderate.
  - **Major**: Bupropion
  - **Moderate (examples)**: anticholinergics (atropine, hyoscyamine, glycopyrronium, dicyclomine, trospium, methscopolamine, clidinium, mepenzolate), corticosteroids (hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide), aminoglycosides (kanamycin, neomycin, paromomycin), and bowel-preparation agents (picosulfuric acid, sodium sulfate, polyethylene glycol with electrolytes)
- **Literature notes**: acetazolamide has been reported to interact adversely with anticholinesterase drugs at the neuromuscular junction (PMID 6715082).

Package insert warnings and contraindications were not available for this report. Please refer to the package insert for label-based safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction is a subtype of a disease neostigmine already treats, so it adds little as a repurposing opportunity. The other predictions are either weakly supported or likely false positives.

<!-- review:begin ph-lic-20261031-neostigmine-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The top prediction is a subtype of a disease neostigmine already treats, so it adds little as a repurposing opportunity. No trials or literature specific to the subtype exist (L4), and the only Philippines registration is cancelled." Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-10-31). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261031-neostigmine-1 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines. This is currently a blocking gap for safety screening.
- Detailed mechanism of action data (for example, from DrugBank).
- Subtype-specific clinical evidence for thymic hyperplasia-associated myasthenia gravis.
- A review of the Major interaction with bupropion and the disease-level contraindications (epilepsy, asthma, cardiac conduction disease) before any clinical use.

<!-- review:begin ph-lic-20261031-neostigmine-2 -->

> **Review correction (2026-10-31)**: Originally stated: "Subtype-specific clinical evidence for thymic hyperplasia-associated myasthenia gravis. / Clarification of the regulatory pathway, since the only Philippines registration is cancelled and no dosage form or approved indication is recorded." Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-10-31). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261031-neostigmine-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "No trials or literature specific to the subtype exist (L4), and the only Philippines registration is cancelled" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-10-31 | Removed: "Clarification of the regulatory pathway, since the only Philippines registration is cancelled and no dosage form or approved indication is r" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

