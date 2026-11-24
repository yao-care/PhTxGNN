---
layout: default
title: Doxycycline
parent: Model Prediction Only (L5)
nav_order: 120
evidence_level: L5
indication_count: 10
monitor_inn: "Doxycycline"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "otitis externa", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "exposure keratitis", "chronic gingivitis"]
last_modified_at: 2026-11-20
description: "Doxycycline: predicted new indication punctate epithelial keratoconjunctivitis (evidence level L5). In the Philippines: 1 PNF entry"
---

# Doxycycline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Doxycycline: tetracycline-class antibiotic → punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Doxycycline is a tetracycline-class antibiotic. The TxGNN model predicts it may be useful for **punctate epithelial keratoconjunctivitis**. Support is very limited: **0 clinical trials** and **1 publication** (a 1992 case report) are currently linked to this prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for doxycycline: "Doxycycline inhibits bacterial protein synthesis by binding to the 30S ribosomal subunit. Doxycycline has bacteriostatic activity against a broad range of Gram-positive and Gram-negative bacteria." ([DailyMed: Doxycyclate Hyclate (doxycycline hyclate) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4dc319c1-b7ef-40e4-9e66-fb24cfdefea8), label version 2026-07-09; accessed 2026-11-19.) Doxycycline belongs to the tetracycline class and is active against *Chlamydia trachomatis*. It is also reported to have anti-inflammatory and matrix metalloproteinase (MMP)-inhibiting effects. Mechanistically, these properties could plausibly help with ocular surface inflammation.

The single supporting paper, from 1992, describes two patients who developed punctate epithelial keratitis after chlamydial follicular conjunctivitis. Both had first been treated with oral tetracycline or doxycycline, and the follicles resolved. The keratitis then recurred. This is an observation about the disease course, **not** a study showing that doxycycline treats it. The mechanistic link therefore remains hypothetical.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case report | Cornea | Two patients developed recurrent, bilateral punctate corneal epithelial lesions after chlamydial follicular conjunctivitis. The conjunctivitis had been treated with oral tetracycline or doxycycline. It describes the disease course, not a doxycycline treatment effect. |

## Philippines Market Information

<!-- review:begin ph-lic-20261106-doxycycline-1 -->

> **Review correction (2026-11-24)**: Originally stated: "The market status recorded in the local data is "Marketed". The detailed licence list is generated separately by the site program and is not reproduced here." Removed: its description of the Philippine products did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The Quick Overview and the PNF entry table under Philippines Market Information show the current number of PNF entries. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-doxycycline-1 -->

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Doxycycline | Oral |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: The interaction search returned 100 records, and the first 20 were reviewed. Interactions rated **Major** include:
  - Isotretinoin
  - Acitretin
  - Aminolevulinic acid

  Many others are rated Moderate or Minor. Examples are aluminium hydroxide, aminophylline, amoxicillin and ampicillin (Moderate), and acetazolamide and amiloride (Minor).
- **Conditions flagged for caution** (relations recorded in the compiled data, not label text): Clostridium difficile colitis, perinatal necrotizing enterocolitis, and dyskinesia of the oesophagus.

Package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is high (0.9994), but the only supporting evidence is one 1992 case report that does not test doxycycline as a treatment. No clinical trials exist, so efficacy in this condition is unsupported.

**To proceed, the following is needed:**
- Controlled clinical studies of doxycycline (for example, ocular or low-dose oral use) in punctate epithelial keratoconjunctivitis
- Mechanism-of-action data and a review of ocular surface anti-inflammatory evidence
- Package insert warnings and contraindications from the Philippines FDA
- A route and formulation assessment (oral versus ocular)
- A safety plan covering the major drug interactions and antimicrobial resistance

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "The market status recorded in the local data is "Marketed". The detailed licence list is generated separately by the site program and is not" | Corrected (revised 2026-11-24; earlier version kept in the record) | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-19 | "Detailed mechanism-of-action data for doxycycline are not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Doxycyclate Hyclate (doxycycline hyclate) prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=4dc319c1-b7ef-40e4-9e66-fb24cfdefea8) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

