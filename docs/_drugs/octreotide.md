---
layout: default
title: Octreotide
parent: Model Prediction Only (L5)
nav_order: 260
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
monitor_inn: "Octreotide"
predicted_indications: ["vulvar inverted follicular keratosis", "seborrheic keratosis"]
description: "Octreotide: predicted new indication Vulvar inverted follicular keratosis (evidence level L5). Approved use: Not recorded in the local data"
---

# Octreotide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Octreotide: Vulvar inverted follicular keratosis
{: .text-alpha }

## One-Sentence Summary

Octreotide is a somatostatin analogue originally used for acromegaly, hyperpituitarism and carcinoid syndrome.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the computational model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 0.9958 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, octreotide is a somatostatin analogue that acts mainly on somatostatin receptors SSTR2 and SSTR5. Its efficacy in acromegaly and carcinoid syndrome is established, but no data compiled for this report connect that pathway to the predicted new indication.

Vulvar inverted follicular keratosis is a benign epithelial lesion. One speculative link would be an antiproliferative effect on keratinocytes through somatostatin receptor signaling, but nothing in the available data supports it. The very high TxGNN score (0.9958) is a computational output only and should not be read as biological validation.

A second prediction, **seborrheic keratosis** (score 0.9955), is also a benign keratinocyte lesion. The two predictions are probably not independent signals. Both scores come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0356 | Octreotide | Not specified | Not specified (status: valid) |

## Safety Considerations

Package insert warnings and contraindications were not available for this report, so please refer to the package insert for safety information.

- **Contraindications / conditions of concern (from knowledge graph, not label text)**: hyperglycemia, diabetes mellitus, diabetic ketoacidosis, hypoglycemia, hypothyroidism (including myxedema and congenital hypothyroidism), liver disease and cirrhosis, gallbladder disease and gallstones (cholelithiasis, cholecystolithiasis, choledocholithiasis), ileus and intestinal obstruction, sudden cardiac arrest, heart conduction disease, kidney failure and uremia, vitamin B12 deficiency.
- **Drug Interactions**: 100 interactions were found, and the 20 shown in the data compiled for this report are all rated Moderate. They are mainly with glucose-lowering drugs, since octreotide can alter blood glucose control:
  - Sulfonylureas and related agents: chlorpropamide, glimepiride
  - Metformin and acarbose
  - DPP-4 inhibitors: alogliptin, linagliptin
  - GLP-1 receptor agonists: albiglutide, dulaglutide, semaglutide
  - SGLT2 inhibitors: canagliflozin, dapagliflozin, empagliflozin
  - Insulins: aspart, degludec, detemir, glargine, glulisine, human isophane, human regular, and inhaled human insulin

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the TxGNN score, with no clinical trials, no literature and no established mechanistic link. The only Philippines registration is cancelled, and safety label data are missing.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank) and a plausible biological link between somatostatin receptor signaling and the benign keratinocyte lesions
- A literature and trial search specific to vulvar inverted follicular keratosis and seborrheic keratosis
- Philippines package insert warnings and contraindications, plus the current registration status and dosage forms
- Route and formulation compatibility assessment (a topical or local route may be relevant for skin lesions, whereas octreotide is conventionally given by injection)
- A glycaemic and gallbladder safety monitoring plan, given the knowledge-graph contraindications and the interactions with antidiabetic drugs
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

