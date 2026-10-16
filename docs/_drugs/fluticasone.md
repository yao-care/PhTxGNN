---
layout: default
title: Fluticasone
parent: Model Prediction Only (L5)
nav_order: 154
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-15
description: "Fluticasone: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available in the compiled data"
monitor_inn: "Fluticasone"
predicted_indications: ["migraine disorder", "Prinzmetal angina", "migraine with brainstem aura"]
---

# Fluticasone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

# Fluticasone: From an Unspecified Original Indication to Migraine Disorder

## One-Sentence Summary

Fluticasone is a glucocorticoid (corticosteroid), but the data compiled for this report do not specify the indication it was approved for in the Philippines.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 clinical trials** and only **1 publication** (a safety-focused review, not evidence of benefit).
This prediction rests on a computational model alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the approved indication text on the registration is empty) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Fluticasone is generally known as a glucocorticoid with anti-inflammatory activity. Because neurogenic inflammation is thought to contribute to migraine, a mechanistic link is conceivable, but the compiled data provide no direct mechanistic or clinical support.

The only publication retrieved (PMID 18681087) is a pharmacovigilance review of neuropsychiatric disturbances reported with intranasal corticosteroids. It addresses safety, not therapeutic benefit. Headache or migraine-like events may appear there as adverse events rather than as an indication.

The high TxGNN score (0.992, rank 5485) reflects a graph-based prediction only and should not be read as clinical evidence.

**Other predicted indications (also model-only, no trials or literature):**
- **Prinzmetal angina** (score 99.19%): Any link to the anti-inflammatory or vascular effects of a corticosteroid is speculative.
- **Migraine with brainstem aura** (score 99.09%): This likely reflects similarity to the parent migraine node in the knowledge graph rather than independent evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18681087](https://pubmed.ncbi.nlm.nih.gov/18681087/) | 2008 | Review | Ann Allergy Asthma Immunol | Review of WHO international pharmacovigilance reports on neuropsychiatric disturbances with intranasal corticosteroids. It concerns safety signals, not efficacy in migraine. |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0203 | Fluticasone | Not specified | Not specified (status: cancelled) |

---

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in total. The main ones with a defined severity level are:
  - **Clarithromycin**: Major
  - **Aprepitant**: Moderate
  - **Insulin human (inhalation, rapid acting)**: Moderate
  - Many other listed interactions have an unclassified severity, including triamcinolone, prednisone, simvastatin, omeprazole, pantoprazole, and morphine.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. There are no clinical trials, and the sole publication is a safety review rather than evidence of benefit. The only Philippine registration is cancelled, and the package insert and mechanism data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Mechanism of action data (for example, from DrugBank) to assess the link to migraine
- A targeted literature search for corticosteroids in migraine, including the 2008 review's relevance to headache as an adverse event versus a treatment effect
- Clarification of the original approved indication and available dosage forms or routes
- Confirmation of the registration status of any current fluticasone products in the Philippines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

