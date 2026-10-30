---
layout: default
title: Topiramate
parent: Model Prediction Only (L5)
nav_order: 341
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
monitor_inn: "Topiramate"
predicted_indications: ["trigeminal nerve neoplasm"]
description: "Topiramate: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Topiramate
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

## Topiramate: Trigeminal nerve neoplasm
{: .text-alpha }

## One-Sentence Summary

Topiramate is an antiseizure medicine originally used for epilepsy (generalized tonic-clonic seizures, partial epilepsy and Lennox-Gastaut syndrome).
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm** with a very high score, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. The prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9970 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From the broader literature, topiramate is a broad-spectrum antiseizure drug acting on voltage-gated sodium channels, GABA-A receptors, AMPA/kainate glutamate receptors, and weakly on carbonic anhydrase. Its efficacy in epilepsy is well established.

There is no known biological link between these actions and the growth of tumors of the trigeminal nerve. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases (such as trigeminal neuralgia) and neurological indications in general, not biological evidence. No mechanistic rationale for this indication can be established from the available data. The score is high, but it should be read as a model signal only.

### Other Predicted Indications (for context)

Several other high-scoring predictions are reflex or rare seizure types, which are much closer to topiramate's original use. None has a registered clinical trial.

| Predicted Indication | Score | Evidence Level | Evidence Summary |
|------|------|------|------|

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available for trigeminal nerve neoplasm.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0493 | Topiramate | Not specified | Not specified (status: valid) |

---

## Safety Considerations

- **Drug Interactions**: The interaction query returned 100 records. Those listed include:
  - **Major**: metformin, and anticholinergic agents (hyoscyamine, atropine, scopolamine, glycopyrronium, clidinium, dicyclomine, mepenzolate, methscopolamine, propantheline, trospium)
  - **Moderate**: pioglitazone, glyburide, morphine, dronabinol, nabilone, phentermine, metoclopramide, phenylbutyric acid, glycerol phenylbutyrate
- **Conditions flagged in the knowledge graph as contraindication-related** (from graph relationships, not label text): anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, liver disease, gallbladder disease, diarrheal disease, ocular hypertension, nephrolithiasis (including the SLC26A1-related form), pyoureter, acute urate nephropathy, acidosis disorder, metabolic acidosis, amnestic disorder, retrograde amnesia.
- **Literature safety signals** (from reports retrieved for related indications): psychotic and manic exacerbation (case reports), cognitive impairment, complications during pregnancy, and adverse reactions in children.

The package insert warnings and contraindications from the Philippines regulator were not available, so please refer to the package insert for authoritative safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score for trigeminal nerve neoplasm is very high (0.9970), but there are no clinical trials, no literature, and no plausible mechanistic link to tumor growth. The evidence is model prediction only (L5). In addition, topiramate is currently marketed in this country, with 1 valid license out of 1.

**To proceed, the following is needed:**
- Mechanism of action data and a biological rationale linking topiramate to trigeminal nerve tumours
- Preclinical or case-level evidence for this indication
- Package insert warnings and contraindications from the Philippines regulator, which are required before safety screening
- Clarification of the cancelled registration status and the available dosage forms and routes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

