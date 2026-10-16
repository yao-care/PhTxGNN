---
layout: default
title: Topiramate
parent: Model Prediction Only (L5)
nav_order: 341
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Topiramate: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy with generalized tonic-clonic seizures, partial epilepsy…"
monitor_inn: "Topiramate"
predicted_indications: ["trigeminal nerve neoplasm", "visual epilepsy", "audiogenic seizures", "eating seizures", "micturation-induced seizures", "startle epilepsy", "thinking seizures", "orgasm-induced seizures", "reading seizures"]
---

# Topiramate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

# Topiramate: From Epilepsy to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Topiramate is an antiseizure medicine originally used for epilepsy (generalized tonic-clonic seizures, partial epilepsy and Lennox-Gastaut syndrome).
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm** with a very high score, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction. The prediction rests on model output alone.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy with generalized tonic-clonic seizures, partial epilepsy, Lennox-Gastaut syndrome (from the knowledge graph; no approved-indication text is available in the Philippines registration record) |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.70% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From the broader literature, topiramate is a broad-spectrum antiseizure drug acting on voltage-gated sodium channels, GABA-A receptors, AMPA/kainate glutamate receptors, and weakly on carbonic anhydrase. Its efficacy in epilepsy is well established.

There is no known biological link between these actions and the growth of tumours of the trigeminal nerve. The prediction most likely reflects proximity in the knowledge graph to trigeminal-related conditions (such as trigeminal neuralgia) and to neurological indications in general, rather than a true anti-tumour mechanism. No mechanistic rationale for this indication can be established from the available data. The score is high, but it should be read as a model signal only.

### Other Predicted Indications (for context)

Several other high-scoring predictions are reflex or rare seizure types, which are much closer to topiramate's original use. None has a registered clinical trial.

| Predicted Indication | Score | Evidence Level | Evidence Summary |
|------|------|------|------|
| Visual epilepsy | 99.28% | L4 | General epilepsy reviews and guidelines only; nothing specific to visual-induced seizures |
| Audiogenic seizures | 99.21% | L4 | Preclinical studies in DBA/2 mice and rat models show topiramate protects against sound-induced seizures; no human data |
| Eating seizures | 99.21% | L4 | Retrieved literature is mostly about eating disorders, probably a term-matching artifact |
| Micturition-induced seizures | 99.21% | L4 | Generic epilepsy literature only |
| Startle epilepsy | 99.21% | L5 | No literature |
| Thinking seizures | 99.21% | L4 | Cochrane add-on reviews support use in drug-resistant partial epilepsy, but not this subtype |
| Orgasm-induced seizures | 99.21% | L5 | No literature |
| Reading seizures | 99.09% | L4 | Tangential literature; none on topiramate in reading seizures |

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
| PNF-0493 | Topiramate | Not specified | Not specified (status: cancelled) |

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
The TxGNN score for trigeminal nerve neoplasm is very high (99.70%), but there are no clinical trials, no literature, and no plausible mechanistic link to tumour growth. The evidence is model prediction only (L5). In addition, topiramate currently has no valid registration in the Philippines.

**To proceed, the following is needed:**
- Mechanism of action data and a biological rationale linking topiramate to trigeminal nerve tumours
- Preclinical or case-level evidence for this indication
- Package insert warnings and contraindications from the Philippines regulator, which are required before safety screening
- Clarification of the cancelled registration status and the available dosage forms and routes
- If the aim is to explore reflex seizure indications (for example audiogenic, visual or reading seizures), a separate assessment of those candidates, which are closer to topiramate's established use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

