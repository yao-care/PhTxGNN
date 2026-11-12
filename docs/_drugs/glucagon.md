---
layout: default
title: Glucagon
parent: Model Prediction Only (L5)
nav_order: 162
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "Glucagon"
predicted_indications: ["irritable bowel syndrome"]
description: "Glucagon: predicted new indication Irritable bowel syndrome (evidence level L5). Approved use: Not recorded in the local data"
---

# Glucagon
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Glucagon: Irritable bowel syndrome
{: .text-alpha }

## One-Sentence Summary

Glucagon is a pancreatic peptide hormone.
The TxGNN model predicts it may be useful for **irritable bowel syndrome**, but no study found tests glucagon itself in this condition. The **2 clinical trials** and the literature compiled for this report concern GLP-1 and GLP-1 receptor agonists, which are different drugs, so the evidence level is **L5**.

<!-- review:begin ph-lic-20261106-glucagon-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Glucagon is a pancreatic peptide hormone that is registered in the Philippines." Removed: it conflicted with the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-glucagon-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Irritable bowel syndrome |
| TxGNN Prediction Score | 0.9924 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data for glucagon is not available in the data compiled for this report.

Glucagon is known to relax gastrointestinal smooth muscle and is used for this purpose in diagnostic imaging. This gives some plausibility for an effect on gut motility, which is relevant to irritable bowel syndrome. No study provided tests this in IBS patients.

The studies linked to this prediction examine GLP-1 and its analogue ROSE-010. These belong to the same proglucagon-derived peptide family but act on a different receptor (GLP-1 receptor rather than the glucagon receptor). They are class-adjacent evidence only and cannot be counted as evidence for glucagon. The high TxGNN score is a computational prediction and does not replace clinical evidence.

## Clinical Trial Evidence

None of these trials tests glucagon.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | ROSE-010 (a GLP-1 analogue) on gastrointestinal motor function in women with constipation-predominant IBS; a physiological motility study, not a symptom-efficacy trial |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Native GLP-1 versus ROSE-010 on stomach, duodenal and jejunal motility after meals in apparently healthy volunteers; indirect mechanistic support only |

## Literature Evidence

The publications below concern GLP-1 or GLP-1 receptor agonists, or IBS in general. None studies glucagon in IBS.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic Review | Front Endocrinol | GLP-1 receptor agonists and IBS; GLP-1 and ROSE-010 inhibit gut motility in IBS patients |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Systematic Review | J Headache Pain | Role of GLP-1 receptor agonists in headache and pain disorders |
| [40697433](https://pubmed.ncbi.nlm.nih.gov/40697433/) | 2025 | Cohort | Ann Gastroenterol | Prescription and discontinuation patterns of GLP-1 receptor agonists in IBS patients |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Clinical study cross-analysis | Scand J Gastroenterol | Pain relief with ROSE-010 during IBS attacks; exploratory search for the best-suited subpopulation |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Review | Exp Physiol | Possible role of GLP-1 and L-cells in IBS pathophysiology |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Review | Adv Exp Med Biol | Aerosolized GLP-1 for diabetes and IBS |
| [41974246](https://pubmed.ncbi.nlm.nih.gov/41974246/) | 2026 | Review | Clin Gastroenterol Hepatol | Care gaps in IBS and future therapies targeting visceral afferent signalling |

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Glucagon (as hydrochloride) | Injection |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 25 interactions were identified in the interaction screening, all of minor severity. The listed ones include warfarin and a range of beta-blockers (for example atenolol, bisoprolol, carvedilol, metoprolol, propranolol, labetalol and timolol, including ophthalmic forms).

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No study tests glucagon in irritable bowel syndrome. The supporting trials and publications concern GLP-1 and GLP-1 receptor agonists, which are different drugs acting on a different receptor. The prediction therefore rests on the model score alone (evidence level L5).

**To proceed, the following is needed:**
- Direct preclinical or clinical studies of glucagon in irritable bowel syndrome
- Mechanism of action data for glucagon and an analysis of how the glucagon receptor could affect IBS symptoms
- Package insert warnings and contraindications from the Philippines regulator
- Product details for the local registration (dosage form and approved indication)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "that is registered in the Philippines" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

