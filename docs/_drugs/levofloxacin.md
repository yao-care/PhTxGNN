---
layout: default
title: Levofloxacin
parent: Model Prediction Only (L5)
nav_order: 206
evidence_level: L5
indication_count: 9
last_modified_at: 2026-11-20
monitor_inn: "Levofloxacin"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "congenital hematological disorder"]
description: "Levofloxacin: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). In the Philippines: 1 PNF entry"
---

# Levofloxacin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Levofloxacin: Punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Levofloxacin is a fluoroquinolone antibacterial. The TxGNN model predicts it may be useful for **punctate epithelial keratoconjunctivitis**, with a score of 0.9992. Evidence is very thin: **no clinical trials** and **1 publication**, an outbreak report on a different cause of keratoconjunctivitis (microsporidia).

<!-- review:begin ph-lic-20261106-levofloxacin-2 -->

> **Review correction (2026-11-24)**: Originally stated: "Levofloxacin is a fluoroquinolone antibacterial that is registered in the Philippines." Removed: it conflicted with the PNF data (the Philippine National Formulary as of 2026-11-06). The Quick Overview and the PNF entry table under Philippines Market Information show the current number of PNF entries. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-levofloxacin-2 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action and Microbiology sections of the US FDA-approved prescribing information for levofloxacin: "Levofloxacin is a member of the fluoroquinolone class of antibacterial agents. […] Levofloxacin is the L-isomer of the racemate, ofloxacin, a quinolone antimicrobial agent. The antibacterial activity of ofloxacin resides primarily in the L-isomer. The mechanism of action of levofloxacin and other fluoroquinolone antimicrobials involves inhibition of bacterial topoisomerase IV and DNA gyrase (both of which are type II topoisomerases), enzymes required for DNA replication, transcription, repair and recombination." ([DailyMed: levofloxacin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=814450ae-439e-4a5d-8c60-9b21b6f14be5), label version 2026-11-05; accessed 2026-11-19.) In general, levofloxacin is a fluoroquinolone that inhibits bacterial DNA gyrase and topoisomerase IV, so activity on the ocular surface against bacterial pathogens is plausible.

The link to punctate epithelial keratoconjunctivitis is weak, however. The only linked paper describes an outbreak of microsporidial keratoconjunctivitis. Microsporidia are not bacteria, and fluoroquinolones have no established activity against them. The paper does not test levofloxacin as a treatment. The high model score therefore is not backed by clinical data, and the prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [30055152](https://pubmed.ncbi.nlm.nih.gov/30055152/) | 2018 | Outbreak report | American Journal of Ophthalmology | Outbreak of microsporidial keratoconjunctivitis linked to contaminated swimming pool water in Taiwan; does not evaluate levofloxacin as a treatment |

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Levofloxacin | Oral, Injection, Eye Drops |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: Interaction screening returned 100 records. Major-level interactions in the listed results include **tramadol** and **hydrocortisone**. Many others are moderate, for example metformin, pioglitazone, ibuprofen, ketorolac, famotidine, salbutamol and formoterol. Minor ones include paclitaxel, aldesleukin and altretamine.

For warnings and contraindications, please refer to the package insert, as label-based safety text is not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a high model score but no clinical trials, and its only publication concerns a microsporidial outbreak, an organism fluoroquinolones are not known to treat. No cited study directly tests levofloxacin in this disease, so the evidence level is L5.

**To proceed, the following is needed:**
- Studies directly testing levofloxacin in punctate epithelial keratoconjunctivitis, with the causative agent defined (bacterial, viral, or non-infectious)
- Mechanism of action data and a review of the package insert warnings and contraindications
- Confirmation of ophthalmic formulations and approved indications in the local licence records

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "Levofloxacin's only Philippines registration is cancelled, and label safety data could not be obtained" | No longer present after the report was regenerated (2026-11-12: the report was regenerated in 2026-11 and no longer contains this statement; was: Corrected (revised 2026-11-24; earlier version kept in the record)) | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-24 | Removed: "that is registered in the Philippines" | Corrected (revised 2026-11-24; earlier version kept in the record) | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: levofloxacin prescribing information, PD-Rx Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=814450ae-439e-4a5d-8c60-9b21b6f14be5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

