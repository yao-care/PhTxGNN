---
layout: default
title: Varenicline
parent: Model Prediction Only (L5)
nav_order: 352
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "Varenicline"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "congenital hypotrichosis milia", "hypotrichosis simplex of the scalp", "diffuse alopecia areata", "alopecia", "open-angle glaucoma", "primary hereditary glaucoma", "headache disorder", "pulmonary hypertension"]
description: "Varenicline: predicted new indication Migraine disorder (evidence level L5). Approved use: Not recorded in the local data"
---

# Varenicline
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

## Varenicline: Migraine disorder
{: .text-alpha }

## One-Sentence Summary

Varenicline is a nicotinic receptor drug, and its original indication is not recorded in the Philippines registration data compiled for this report.
The TxGNN model predicts it may be effective for **migraine disorder**, but this is a model prediction only, with **0 clinical trials** and **1 publication** (a cardiac arrest case report that is a safety signal, not efficacy evidence).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Varenicline is a partial agonist of the α4β2 nicotinic acetylcholine receptor and a full agonist of the α7 receptor. Nicotinic cholinergic signalling has been loosely linked to pain modulation and cortical excitability, which is the only plausible bridge to migraine.

The compiled data provide no direct mechanistic or clinical evidence for this link. The very high TxGNN score (0.9992) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Related predictions such as migraine with brainstem aura rest on the same indirect hypothesis, and the many alopecia and hypotrichosis predictions suggest the score may partly reflect similarities the model learned between related diseases rather than real biology.

Detailed mechanism-of-action data from DrugBank were not available for this report. The mechanism described above comes from the analysis of the prediction itself and should be verified.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19585710](https://pubmed.ncbi.nlm.nih.gov/19585710/) | 2009 | Case report | Therapie | Cardiac arrest reported in a patient taking varenicline. This is a safety signal, not evidence of efficacy in migraine. |

For the broader "headache disorder" prediction, 13 publications were retrieved, mostly on smoking cessation and other substance use. They mainly show headache as an adverse event, including a case of bath-related headache induced by varenicline ([23175211](https://pubmed.ncbi.nlm.nih.gov/23175211/)). They do not support efficacy against headache.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0509 | Varenicline | Not recorded | Not recorded (status: valid) |

---

## Safety Considerations

- **Disease-level contraindication signals (from the TxGNN knowledge graph, not label text)**: anxiety disorder, neurotic disorder, dysthymic disorder, bipolar disorder, major affective disorder, substance abuse/dependence, schizophrenia, acute coronary syndrome, peripheral vascular disease, intermittent vascular claudication, peripheral arterial disease.
- **Drug Interactions**: 100 interactions were found. The only graded entry among those shown is cimetidine (Minor). The others shown, including phentermine, metformin, glimepiride, rosiglitazone, simvastatin, morphine, prednisone, epinephrine and several proton pump inhibitors, are of unknown severity.
- **Case-report signals**: cardiac arrest, and headache as an adverse reaction.

Please refer to the package insert for label warnings and contraindications, which were not available for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is model-only (L5), with no clinical trials and no efficacy literature for migraine.

**To proceed, the following is needed:**
- Mechanistic and preclinical evidence linking nicotinic receptor activity to migraine
- Package insert warnings and contraindications from DOH-FDA Philippines
- Detailed mechanism-of-action data from DrugBank
- Confirmation of the original approved indication and the reason the registration was cancelled
- A review of cardiovascular and psychiatric safety in the target migraine population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

