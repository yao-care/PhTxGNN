---
layout: default
title: Mometasone
parent: Model Prediction Only (L5)
nav_order: 239
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
description: "Mometasone: predicted new indication Primary cutaneous T-cell lymphoma (evidence level L5). Approved use: Not stated in the Philippines registration data"
monitor_inn: "Mometasone"
predicted_indications: ["primary cutaneous T-cell lymphoma"]
---

# Mometasone
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

## Mometasone: From an Unspecified Original Indication to Primary Cutaneous T-Cell Lymphoma
{: .text-alpha }

## One-Sentence Summary

Mometasone is a synthetic corticosteroid. The Philippines registration data compiled for this report do not state its approved indication, although it is known as a topical and intranasal anti-inflammatory agent.
The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma**.
Support is very limited: **0 clinical trials** and **2 publications**, both case reports with no direct evidence for mometasone in this disease.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Philippines registration data |
| Predicted New Indication | Primary cutaneous T-cell lymphoma |
| TxGNN Prediction Score | 0.9936 |
| Evidence Level | L5 |
| Philippines Market Status | Not listed in the Philippine National Formulary (PNF) Essential Medicines List – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data are not available in the data compiled for this report. Pharmacology records show that mometasone acts on the **glucocorticoid receptor (NR3C1)**. It is a potent corticosteroid with anti-inflammatory, immunosuppressive and anti-proliferative effects. It is used intranasally for asthma, allergic rhinitis and nasal polyposis, and topically for allergic skin disorders.

Topical corticosteroids are a recognised skin-directed therapy for early-stage mycosis fungoides, the most common primary cutaneous T-cell lymphoma. Glucocorticoid receptor signalling can suppress T-cell activation and cytokine signalling, so the prediction is biologically plausible.

This reasoning rests on class-level knowledge about topical steroids. The compiled data contain no mometasone-specific clinical evidence in this disease. The prediction is therefore a model output, not a confirmed finding.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case report | Proceedings (Baylor University Medical Center) | Cutaneous pseudolymphoma on the nose did not respond to mometasone and tacrolimus, and was later treated with tapinarof. This is a benign mimic of lymphoma, not a true T-cell lymphoma, and it does not support mometasone's efficacy. |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case report | Journal of Cutaneous Pathology | An 11-year-old boy with CD8+CD56+ cytotoxic-type mycosis fungoides. The report describes the disease and its diagnostic difficulty, and gives no direct evidence on mometasone. |

## Philippines Market Information

<!-- licenses:begin -->

Not listed in the Philippine National Formulary (PNF) Essential Medicines List used for this report.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: The only record is a pharmacology link to the glucocorticoid receptor (its target). It is not a drug-drug interaction with a severity rating.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence is model prediction only (L5). There are no clinical trials, and the two publications are case reports that do not show mometasone efficacy in cutaneous T-cell lymphoma.

<!-- review:begin ph-lic-20261031-mometasone-1 -->

> **Review correction (2026-10-31)**: Originally stated: "There are no clinical trials, and the two publications are case reports that do not show mometasone efficacy in cutaneous T-cell lymphoma. The only Philippines registration is cancelled, and there is no label-based safety information." Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-10-31). The PNF lists 0 entries for this drug, 0 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261031-mometasone-1 -->

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines, so safety screening can begin
- Mechanism-of-action data from DrugBank
- Mometasone-specific clinical or observational data in early-stage mycosis fungoides or other primary cutaneous T-cell lymphoma
- Clarification of the original approved indication and available dosage forms

<!-- review:begin ph-lic-20261106-mometasone-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of the original approved indication and available dosage forms, including whether a valid topical product is registered in the Philippines" Removed: the number or status of PNF entries stated here did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 0 entries for this drug, 0 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-mometasone-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The only Philippines registration is cancelled, and there is no label-based safety information" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-06 | Removed: "including whether a valid topical product is registered in the Philippines" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

