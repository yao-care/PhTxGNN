---
layout: default
title: Rabeprazole
parent: Model Prediction Only (L5)
nav_order: 290
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Rabeprazole: predicted new indication Smouldering systemic mastocytosis (evidence level L5). Approved use: Peptic ulcer disease, gastroesophageal reflux disease…"
monitor_inn: "Rabeprazole"
predicted_indications: ["lymphoadenopathic mastocytosis with eosinophilia"]
---

# Rabeprazole
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

# Rabeprazole: From Peptic Ulcer Disease to Smouldering Systemic Mastocytosis

## One-Sentence Summary

Rabeprazole is a proton pump inhibitor, originally used for acid-related conditions such as peptic ulcer disease, gastroesophageal reflux disease and Zollinger-Ellison syndrome.
The TxGNN model predicts it may be effective for **Smouldering Systemic Mastocytosis**,
but currently there are **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Peptic ulcer disease, gastroesophageal reflux disease, and related acid-related conditions (the Philippines registration record has no indication text) |
| Predicted New Indication | Smouldering systemic mastocytosis |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (registration cancelled) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, rabeprazole is a proton pump inhibitor (acid-suppressing drug). Its efficacy in acid-related disorders is established, and the knowledge graph already lists systemic mastocytosis and mastocytosis among its indications.

Smouldering systemic mastocytosis is a subtype of systemic mastocytosis. The high TxGNN score (0.994) most likely reflects this shared disease relationship rather than new biological evidence. In mastocytosis, mast cells release excess histamine, which can drive gastric acid hypersecretion. Rabeprazole could plausibly help control these acid-related symptoms.

This benefit would be symptomatic only. There is no indication that rabeprazole affects the underlying clonal mast cell disease. No independent mechanistic evidence is available.

A second prediction, lymphoadenopathic mastocytosis with eosinophilia (score 99.35%), follows the same logic. It also has no trials or literature, and any benefit would be limited to acid suppression.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0413 | Rabeprazole | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Knowledge graph contraindication associations** (not from label text): liver disease, gallbladder disease, osteoporosis, postmenopausal osteoporosis, bone fracture.
- **Drug Interactions**: The interaction screen returned 100 records. The first 20 reviewed include:
  - **Major**: acalabrutinib, atazanavir
  - **Moderate**: for example amikacin, amphotericin B (including its lipid formulations), amphetamine, apalutamide, aprepitant, armodafinil, bosutinib, and the thiazides bendroflumethiazide and benzthiazide
  - **Minor**: acetylsalicylic acid, axitinib

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature (Evidence Level L5). Any plausible benefit is limited to symptomatic acid suppression, not treatment of the disease itself. The only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines (currently a blocking gap)
- Detailed mechanism of action data (e.g., from DrugBank)
- Clinical or observational evidence of rabeprazole use in smouldering systemic mastocytosis
- Clarification of the current market and registration status in the Philippines, and of available dosage forms and routes
- Review of the interaction profile (including the major interactions with acalabrutinib and atazanavir) and of the bone and liver-related associations for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

