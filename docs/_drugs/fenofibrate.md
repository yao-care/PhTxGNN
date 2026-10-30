---
layout: default
title: Fenofibrate
parent: Model Prediction Only (L5)
nav_order: 139
evidence_level: L5
indication_count: 1
monitor_inn: "Fenofibrate"
predicted_indications: ["cholesterol-ester transfer protein deficiency"]
last_modified_at: 2026-10-30
description: "Fenofibrate: predicted new indication Cholesterol-ester transfer protein deficiency (evidence level L5). Approved use: Hypertriglyceridemia, hyperlipidemia…"
---

# Fenofibrate
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

## Fenofibrate: From Hypertriglyceridemia to Cholesterol-Ester Transfer Protein Deficiency
{: .text-alpha }

## One-Sentence Summary

Fenofibrate is a lipid-lowering drug whose relations recorded in the knowledge graph cover hypertriglyceridemia and several forms of hyperlipidemia.
The TxGNN model predicts it may be relevant to **cholesterol-ester transfer protein (CETP) deficiency**, but there are **0 clinical trials** and only **3 publications** (all preclinical or mechanistic, none studying CETP deficiency in patients) behind this prediction.
The evidence is weak, and the prediction is a computational signal rather than a validated treatment rationale.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertriglyceridemia, hyperlipidemia, familial hyperlipidemia and related conditions (relations recorded in the knowledge graph; the local licence record has no indication text) |
| Predicted New Indication | Cholesterol-ester transfer protein deficiency |
| TxGNN Prediction Score | 0.9961 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Fenofibrate is generally known as a PPARα agonist that lowers triglycerides and raises HDL cholesterol, and the retrieved literature is consistent with this role in HDL metabolism.

CETP deficiency is a genetic condition marked by very high HDL cholesterol and impaired transfer of cholesteryl esters between lipoproteins. The retrieved studies link PPARα agonism to HDL metabolism (for example, induction of the phospholipid transfer protein gene and HDL enlargement in mice) and to combined effects with CETP inhibition in transgenic mice. This connection is biologically plausible but indirect.

There is also a reasoning problem: fenofibrate would further raise HDL cholesterol, which is not an obvious therapeutic goal in a condition that already shows elevated HDL cholesterol. The high score most likely reflects shared lipid-metabolism nodes in the network rather than a validated treatment rationale. No cited study directly examines this disease, so the evidence level is capped at L5.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20332533](https://pubmed.ncbi.nlm.nih.gov/20332533/) | 2010 | Preclinical (transgenic mice) | J Cardiovasc Pharmacol Ther | The CETP inhibitor torcetrapib and the PPARα agonist fenofibrate were tested in mice expressing human ApoB-100 and CETP to see how they affect lipid profiles. |
| [11342537](https://pubmed.ncbi.nlm.nih.gov/11342537/) | 2001 | Mechanistic (mice) | J Biol Chem | Fenofibrate induces the phospholipid transfer protein gene, which accounts for HDL enlargement in treated mice. |
| [30271349](https://pubmed.ncbi.nlm.nih.gov/30271349/) | 2018 | Mechanistic | Front Physiol | Plasma HDL cholesterol did not correlate with fecal cholesterol excretion or efflux capacity, suggesting HDL function matters more than HDL level. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0187 | Fenofibrate | Not stated | Not stated in the record |

## Safety Considerations

No package insert warnings or contraindications were available in the data compiled for this report. Please refer to the package insert for safety information.

- **Relations recorded in the knowledge graph (not label text)**: the knowledge graph links fenofibrate with contraindication to liver failure and liver disease, pancreatitis, gallbladder disease and gallstones (cholelithiasis), myopathy and rhabdomyolysis, impaired renal function, thrombocytopenia, anemia, and several blood-cell disorders (leukopenia, agranulocytosis, neutropenia and its congenital forms). These need confirmation against the approved label.
- **Drug Interactions**: 100 interactions were identified; the 20 listed are all of moderate level. They include sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), many insulin products (human, aspart, degludec, detemir, glargine, glulisine, lispro and others), esomeprazole, and chenodeoxycholic acid. Blood glucose monitoring is relevant when combined with antidiabetic drugs.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trials and no study directly addressing CETP deficiency exist; the three publications are preclinical or mechanistic. The high TxGNN score is not supported by a clear therapeutic rationale, since fenofibrate would raise HDL cholesterol that is already high in this condition.

**To proceed, the following is needed:**
- Evidence that studies CETP deficiency directly (patient data or a disease-relevant model)
- A clear rationale for the therapeutic goal, given the already elevated HDL cholesterol
- Mechanism of action data
- Package insert warnings and contraindications from the Philippine FDA, including the dosage form and approved indication for PNF-0187
- Review of the knowledge-graph contraindication signals against the label
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

