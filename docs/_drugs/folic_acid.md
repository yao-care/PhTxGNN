---
layout: default
title: Folic Acid
parent: Model Prediction Only (L5)
nav_order: 155
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Folic Acid: predicted new indication Biotin metabolic disease (evidence level L5). Approved use: Vitamin deficiency disorder, folic acid deficiency anemia…"
---

# Folic Acid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Folic Acid: From Vitamin Deficiency and Deficiency Anemias to Biotin Metabolic Disease

## One-Sentence Summary

Folic acid (vitamin B9) was originally used to treat vitamin deficiency disorders and deficiency-related anemias, including folic acid deficiency anemia and iron deficiency anemia.
The TxGNN model predicts it may be effective for **biotin metabolic disease**, but this is a model prediction only, with **0 clinical trials** and **20 publications** (mostly general reviews of B vitamins) that do not directly show it works for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Vitamin deficiency disorder, folic acid deficiency anemia, iron deficiency anemia, hypochromic anemia, deficiency anemia, microcytic anemia (from the knowledge graph; no approved indication text in local registrations) |
| Predicted New Indication | Biotin metabolic disease |
| TxGNN Prediction Score | 99.49% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, folic acid (folate) acts as a coenzyme in one-carbon metabolism. Its efficacy in correcting folate deficiency and related anemias is well established.

Folate and biotin are both B-vitamin cofactors. Their pathways can intersect in methyl-group and amino acid metabolism, which is likely why the network model links them. However, the retrieved literature covers B vitamins in general (vitamin-responsive disorders, B vitamins in diabetes and dermatology). It does not show that folic acid treats biotin metabolic diseases such as biotinidase deficiency or holocarboxylase synthetase deficiency. These disorders are treated with biotin itself, so a direct therapeutic role for folic acid is not established. The very high score reflects network similarity, not clinical proof.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

The data compiled for this report contain 20 publications. Most are reviews of B vitamins in general. Only the most relevant are listed below (no RCTs were found).

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23622402](https://pubmed.ncbi.nlm.nih.gov/23622402/) | 2013 | Review | Handbook of Clinical Neurology | Reviews vitamin-responsive disorders (cobalamin, folate, biotin, B1, E) and inborn errors of vitamin metabolism; biotin disorders are treated with biotin |
| [38203763](https://pubmed.ncbi.nlm.nih.gov/38203763/) | 2024 | Review | International Journal of Molecular Sciences | Vitamin B12 deficiency and the nervous system; notes B12, folate, and biotin share metabolic reactions |
| [7027768](https://pubmed.ncbi.nlm.nih.gov/7027768/) | 1981 | Review | Acta Vitaminologica et Enzymologica | Vitamins in metabolic diseases: malabsorption, metabolism errors, and vitamin-dependent syndromes |
| [41692080](https://pubmed.ncbi.nlm.nih.gov/41692080/) | 2026 | Review | Clinics in Dermatology | B vitamins in cellular metabolism and erythrocyte synthesis |
| [37123774](https://pubmed.ncbi.nlm.nih.gov/37123774/) | 2023 | Review | Cureus | Vitamins and type 2 diabetes; thiamine, pyridoxine, and biotin are lower in people with diabetes |
| [25388747](https://pubmed.ncbi.nlm.nih.gov/25388747/) | 2015 | Review | Endocrine, Metabolic & Immune Disorders Drug Targets | Individual and combined vitamins in type 2 diabetes |
| [14989256](https://pubmed.ncbi.nlm.nih.gov/14989256/) | 2004 | Review | Archives of Biochemistry and Biophysics | Deficiency of B12, folic acid, B6, and other micronutrients can damage DNA; supplements may optimize metabolism |
| [38350491](https://pubmed.ncbi.nlm.nih.gov/38350491/) | 2025 | Cohort | Nutrition Reviews | Micronutrient status in children with severe wasting and/or nutritional edema |
| [13199008](https://pubmed.ncbi.nlm.nih.gov/13199008/) | 1954 | Animal study | Biologica Latina | Combined biotin and folic acid deficiency induced in rats on a purified diet |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0204 | Folic Acid | Not specified | Not specified (registration cancelled) |

## Safety Considerations

- **Contraindications (knowledge graph, not label text)**: The TxGNN knowledge graph links folic acid to many conditions as contraindications. These need verification against the product label before any use. Examples include:
  - Kidney disease, nephrolithiasis, and primary hyperoxaluria
  - Hemolytic anemia, sickle cell anemia, and iron metabolism disorders (hereditary hemochromatosis, hemosiderosis)
  - Wilson disease
  - Diabetes mellitus and diabetic ketoacidosis
  - Bipolar disorder
  - Peptic ulcer disease, ulcerative colitis, and inflammatory bowel disease
  - Hypercalcemia, hyperparathyroidism, and nephrocalcinosis
- **Drug Interactions**: A search found 100 recorded interactions. The only moderate one among the first 20 shown is **pancrelipase**; **sulfasalazine** is minor. The rest are of unknown severity, including metformin, omeprazole, pantoprazole, lansoprazole, glimepiride, acarbose, mesalazine, prednisone, simvastatin, and vancomycin.

Please refer to the package insert for label warnings.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-based only (L5). There are no clinical trials, and the literature does not support folic acid as a treatment for biotin metabolic disease, which is managed with biotin. The only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data and a clear mechanistic rationale for biotin metabolic disease
- Specific evidence (preclinical or clinical) that folic acid benefits biotinidase or holocarboxylase synthetase deficiency, beyond general B-vitamin reviews
- Package insert warnings and contraindications for safety screening, since none are currently available
- Review of the knowledge graph contraindications against label text
- Clarification of the regulatory situation, since the only local registration is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

