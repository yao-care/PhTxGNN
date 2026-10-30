---
layout: default
title: Allopurinol
parent: Model Prediction Only (L5)
nav_order: 19
evidence_level: L5
indication_count: 10
monitor_inn: "Allopurinol"
predicted_indications: ["hepatic porphyria", "hepatopulmonary syndrome", "idiopathic copper-associated cirrhosis", "hepatoportal sclerosis", "primitive portal vein thrombosis", "early-onset familial noncirrhotic portal hypertension", "disorder of phenylalanine metabolism", "immune-mediated necrotizing myopathy", "antisynthetase syndrome", "idiopathic eosinophilic myositis"]
last_modified_at: 2026-10-30
description: "Allopurinol: predicted new indication Hepatic porphyria (evidence level L5). Approved use: Gout, hyperuricemia and acute urate nephropathy"
---

# Allopurinol
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

## Allopurinol: From Gout to Hepatic Porphyria
{: .text-alpha }

## One-Sentence Summary

Allopurinol is a xanthine oxidase inhibitor whose relations recorded in the knowledge graph include gout, hyperuricemia and acute urate nephropathy.
The TxGNN model predicts it may be relevant to **hepatic porphyria**, but **no clinical trials** and only **2 hypothesis-level or off-target publications** are available, so the prediction rests on the model score alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Gout, hyperuricemia and acute urate nephropathy (relations recorded in the knowledge graph; the local licence record contains no indication text) |
| Predicted New Indication | Hepatic porphyria |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Allopurinol is generally known as a xanthine oxidase inhibitor used to lower uric acid. This general background is not drawn from the compiled data.

The link to hepatic porphyria is weak and may even point in the opposite direction. Allopurinol has been reported to have porphyrinogenic effects in experimental models, possibly through interaction with hepatic heme biosynthesis (ALAS1 regulation). The two retrieved papers do not show a therapeutic benefit. One is a hypothesis paper proposing to target 5-aminolevulinate synthase in acute hepatic porphyrias. The other is a rat study of carbamazepine, a different drug.

The high TxGNN score is a model prediction only. It could reflect an association with adverse heme effects rather than benefit. Other predicted diseases, such as hepatopulmonary syndrome and several portal or hepatic disorders, share an identical score of 0.9994. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Review | Medical Hypotheses | Proposes metabolic targeting of liver 5-aminolevulinate synthase, using tryptophan or inhibiting heme use by tryptophan 2,3-dioxygenase, as a therapy for acute hepatic porphyrias. It does not study allopurinol. |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal study | Biochemical Pharmacology | Low-dose carbamazepine worsened heme metabolism changes in rat liver, relevant to porphyria exacerbation. It is a different drug. |

No clinical trials are currently registered for this prediction. Neither paper directly studies allopurinol in hepatic porphyria, so the evidence level is capped at L5.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0011 | Allopurinol | Not stated | Not stated |

The record lists 1 single-ingredient registration with valid status. The list is complete.

---

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text)**: Contraindication relations are recorded for liver disease, gallbladder disease, impaired renal function, hypersensitivity vasculitis, cutaneous leukocytoclastic angiitis, allergic cutaneous vasculitis and anti-glomerular basement membrane disease.
- **Drug Interactions**: 100 interactions were found in the DDI database. Moderate-level interactions include:
  - aluminum hydroxide
  - attapulgite
  - kaolin
  - magaldrate
  - sucralfate

  Minor-level interactions include amoxicillin and chlorpropamide. Several others, such as metformin, omeprazole, glimepiride and morphine, are of unknown severity.
- **Disease-specific concern**: The retrieved rationale notes that allopurinol may be a concern in porphyria. For other predicted diseases it notes rare hypersensitivity reactions (such as DRESS) and reports of myopathy.

Please refer to the package insert for the full warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No trial or publication directly studies allopurinol in hepatic porphyria, and the available literature suggests possible harm rather than benefit. The other nine predicted diseases also have no direct supporting evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Philippine regulator
- Mechanism of action data
- Clinical or mechanistic evidence on allopurinol's effect on heme biosynthesis and porphyria, including safety in porphyria patients
- Expert review of whether the score reflects an adverse association rather than a therapeutic one
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

