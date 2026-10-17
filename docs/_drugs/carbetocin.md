---
layout: default
title: Carbetocin
parent: Model Prediction Only (L5)
nav_order: 61
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Carbetocin: predicted new indication Isotretinoin-like syndrome (evidence level L5). Approved use: Prader-Willi syndrome, Noonan syndrome"
monitor_inn: "Carbetocin"
predicted_indications: ["isotretinoin-like syndrome", "Goodman syndrome"]
---

# Carbetocin
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

# Carbetocin: From Prader-Willi Syndrome and Noonan Syndrome to Isotretinoin-like Syndrome

## One-Sentence Summary

Carbetocin is a long-acting oxytocin analogue. In the knowledge graph used for this report it is linked to Prader-Willi syndrome and Noonan syndrome, and its pharmacology data describe use in preventing postpartum haemorrhage due to uterine atony.
The TxGNN model predicts it may be effective for **isotretinoin-like syndrome**, but **no clinical trials and no publications** currently support this direction.
This is a model-only prediction and should be treated as hypothesis-generating.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Prader-Willi syndrome, Noonan syndrome (knowledge-graph indications; no approved indication text on the Philippines registration) |
| Predicted New Indication | Isotretinoin-like syndrome |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on the pharmacology data compiled for this report, carbetocin is a peptide oxytocin analogue that acts on the oxytocin receptor (OXTR). An intranasal formulation has been under development for Prader-Willi syndrome, intended to reduce the extreme hunger that leads to hyperphagia.

The original indications (Prader-Willi syndrome and Noonan syndrome) are developmental syndromes. This suggests the prediction may reflect shared neighbours in the knowledge graph. However, isotretinoin-like syndrome is a teratogenic embryopathy associated with disruption of the retinoic acid pathway. No biological pathway connecting oxytocin receptor agonism to this phenotype can be established from the available data.

The prediction rests only on the high model score. It has no trial or literature backing, so its plausibility should be regarded as low until a mechanistic rationale is shown.

A second predicted indication, **Goodman syndrome** (score 99.06%), is a rare craniofacial and limb malformation disorder. It also has no supporting trials or literature, and oxytocin-based therapy would not be expected to correct a structural congenital malformation. It is likewise rated L5 / Hold.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0076 | Carbetocin | Not specified | Not specified (registration status: cancelled) |

---

## Safety Considerations

- **Drug Interactions**: The interaction query completed, but it returned only a pharmacology target record (oxytocin receptor, OXTR, human) and no drug-drug interactions with a defined severity level.

Please refer to the package insert for further safety information, including warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction relies only on a model score. There are no clinical trials or publications, the mechanism of action is unavailable, and no biological link between oxytocin receptor agonism and isotretinoin-like embryopathy can be established. The only Philippines registration is cancelled, and the safety information from the package insert is missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines (a blocking gap for safety screening)
- Detailed mechanism of action data from DrugBank
- A plausible biological rationale linking oxytocin receptor agonism to the predicted indication
- Any preclinical or clinical evidence for the predicted indication
- Clarification of the cancelled registration status and the available dosage forms and routes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

