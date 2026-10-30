---
layout: default
title: Fosfomycin
parent: Model Prediction Only (L5)
nav_order: 158
evidence_level: L5
indication_count: 8
monitor_inn: "Fosfomycin"
predicted_indications: ["uterine inflammatory disease", "xanthogranulomatous pyelonephritis", "epiglottitis", "urogenital tuberculosis", "laryngitis", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "pyelitis"]
last_modified_at: 2026-10-30
description: "Fosfomycin: predicted new indication Uterine inflammatory disease (evidence level L5). Approved use: Urinary tract infection"
---

# Fosfomycin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Fosfomycin: From Urinary Tract Infection to Uterine Inflammatory Disease
{: .text-alpha }

## One-Sentence Summary

Fosfomycin is an antibiotic. Urinary tract infection is recorded as its original use.
The TxGNN model predicts it may be effective for **uterine inflammatory disease**, but the data compiled for this report contain **no study that directly tests this disease**. The two clinical trials found are general pediatric pharmacokinetic studies, and the one publication concerns cystitis in women taking dienogest, so this is effectively a model-only prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Urinary tract infection (a relation recorded in the knowledge graph; the local licence record contains no approved indication text) |
| Predicted New Indication | Uterine inflammatory disease |
| TxGNN Prediction Score | 0.9998 |
| Evidence Level | L5 (no cited study directly addresses this disease) |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Licences | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. As general background, fosfomycin is a bactericidal antibiotic that inhibits MurA (UDP-N-acetylglucosamine enolpyruvyl transferase). This blocks an early step of bacterial cell-wall (peptidoglycan) synthesis. It is active against many Enterobacterales and some Gram-positive bacteria.

The link to the new indication is an inference. Uterine and pelvic infections can involve organisms such as *E. coli* that fosfomycin covers. Both conditions are infection or inflammation of the genitourinary and pelvic region. However, no direct evidence of efficacy in uterine inflammatory disease was found. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01431326](https://clinicaltrials.gov/study/NCT01431326) | N/A | Completed | 3,520 | Pharmacokinetics of understudied drugs given to children as standard care. It tests no efficacy in uterine inflammatory disease, so the link is indirect at best. |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5,000 | General pharmacokinetic, pharmacodynamic and safety platform for understudied drugs in children and young adults. It has no disease-specific efficacy endpoint. |

Neither trial studies uterine inflammatory disease.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|---------|---------|
| [35653789](https://pubmed.ncbi.nlm.nih.gov/35653789/) | 2022 | Cohort | J Obstet Gynaecol | Prospective study of 145 women after laparoscopic surgery for endometriosis. It compared acute cystitis symptoms and bacteriuria between dienogest and combined oral contraceptives. It does not study fosfomycin treatment of uterine inflammatory disease. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0208 | Fosfomycin | Not stated in the record | Not stated in the record |

This is a single-ingredient product with a valid status. The licence record contains no indication text, so the Philippine approved uses cannot be confirmed from the data compiled for this report.

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** The knowledge graph links fosfomycin with the following diseases as contraindications: kidney disease, pyoureter, *Clostridium difficile* colitis and perinatal necrotizing enterocolitis. These need to be checked against the official label.
- **Drug Interactions (3 found):**
  - Balsalazide: Moderate
  - Picosulfuric acid: Moderate
  - Metoclopramide: Minor

Please refer to the package insert for the full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on the model score and a plausible antibacterial mechanism. No trial or publication directly studies fosfomycin in uterine inflammatory disease, and the pack contains no information on how fosfomycin reaches or acts in uterine tissue. Local label and safety data are also missing.

**To proceed, the following is needed:**
- Direct clinical or microbiological evidence in uterine or pelvic inflammatory infection, including tissue penetration and the causative organisms
- Mechanism of action data from a primary source such as DrugBank
- The Philippine package insert, giving approved indications, dosage forms, warnings and contraindications
- A review of the knowledge-graph contraindication relations (kidney disease and others) against the official label
- Consideration of a better-supported nearby indication, such as pyelitis, which is close to urinary tract infection and has a randomized phase 2/3 trial of IV fosfomycin in complicated UTI and acute pyelonephritis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

