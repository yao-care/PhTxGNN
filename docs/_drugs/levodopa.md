---
layout: default
title: Levodopa
parent: Model Prediction Only (L5)
nav_order: 205
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Levodopa: predicted new indication Rasmussen subacute encephalitis (evidence level L5). Approved use: Parkinson disease and related parkinsonian disorders"
monitor_inn: "Levodopa"
predicted_indications: ["Rasmussen subacute encephalitis"]
---

# Levodopa
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

## Levodopa: From Parkinson Disease to Rasmussen Subacute Encephalitis
{: .text-alpha }

## One-Sentence Summary

Levodopa is a dopamine precursor originally used to treat Parkinson disease and related parkinsonian disorders.
The TxGNN model predicts it may be effective for **Rasmussen subacute encephalitis**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease and related parkinsonian disorders |
| Predicted New Indication | Rasmussen subacute encephalitis |
| TxGNN Prediction Score | 0.9906 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, levodopa is a dopamine precursor that replaces missing dopamine in parkinsonian disorders. Its efficacy in Parkinson disease is well established.

Rasmussen encephalitis is a rare, chronic, unilateral inflammatory brain disease, probably T-cell mediated. It causes intractable focal seizures and progressive hemispheric atrophy. The only possible link to levodopa is that both conditions involve movement-related features. For example, hemiparkinsonism-hemiatrophy syndrome is among levodopa's listed indications, and Rasmussen encephalitis causes progressive hemiparesis and hemispheric atrophy.

This link is speculative. Levodopa would not be expected to treat the inflammatory or seizure-generating processes of the disease. At most, dopaminergic therapy could be considered for symptomatic movement features, and this has not been studied. The high prediction score is a computational output without clinical corroboration.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0286 | Levodopa | Not specified | Not specified (registration valid) |

## Safety Considerations

- **Contraindications (from TxGNN model associations, not package insert text)**: The TxGNN model (deep learning) links levodopa to the following conditions as contraindications; these associations may reflect similarities the model learned between related diseases, not biological evidence:
  - **Cardiovascular:** myocardial infarction, coronary thrombosis, sudden cardiac arrest, heart conduction disease, orthostatic hypotension, postural orthostatic tachycardia syndrome
  - **Neurological and psychiatric:** epilepsy, drug-induced dyskinesia, multiple system atrophy, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder, anxiety disorder, neurotic disorder, dysthymic disorder
  - **Eye:** open-angle glaucoma, angle-closure glaucoma
  - **Gastrointestinal, hepatic and renal:** gastric ulcer, peptic ulcer disease, diarrheal disease, liver disease, gallbladder disease, kidney disease, pyoureter
  - **Metabolic, blood and skin:** diabetes mellitus, diabetic ketoacidosis, hemoglobinopathy, melanoma

  Epilepsy is particularly relevant to the predicted indication, since Rasmussen encephalitis presents with intractable seizures.

- **Drug Interactions**: The data compiled for this report list 100 interactions in total. The first 20 returned are all Moderate or Minor severity:
  - **Moderate:** epinephrine, ephedrine, bupropion, metronidazole, pyridoxine, iron, metoclopramide, and anticholinergics (methscopolamine, hyoscyamine, atropine, glycopyrronium, clidinium, dicyclomine, mepenzolate)
  - **Minor:** antacids (aluminum hydroxide, calcium carbonate, magaldrate, and magnesium carbonate, hydroxide and oxide)

Package insert warnings and contraindications were not available; please refer to the package insert for authoritative safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a high model score. There are no clinical trials or publications, and no plausible mechanism is evident. Levodopa would not be expected to address the inflammatory and epileptogenic basis of Rasmussen encephalitis. Its only Philippines registration is cancelled, and epilepsy appears among its knowledge-graph contraindications.

**To proceed, the following is needed:**
- Mechanism of action data and a mechanistic rationale for Rasmussen encephalitis
- Preclinical or case-level evidence of benefit
- Package insert warnings and contraindications, to complete safety screening
- Review of the cancelled registration and available dosage forms and routes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

