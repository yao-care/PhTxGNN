---
layout: default
title: Dextromethorphan
parent: Model Prediction Only (L5)
nav_order: 104
evidence_level: L5
indication_count: 6
last_modified_at: 2026-10-15
description: "Dextromethorphan: predicted new indication Nasal cavity disease (evidence level L5). Approved use: Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold…"
monitor_inn: "Dextromethorphan"
predicted_indications: ["nasal cavity disease", "acute laryngopharyngitis", "faucial diphtheria", "trigeminal autonomic cephalalgia", "cervical disc degenerative disorder", "allergic urticaria"]
---

# Dextromethorphan
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

## Dextromethorphan: From Allergic Rhinitis and Common Cold to Nasal Cavity Disease
{: .text-alpha }

## One-Sentence Summary

Dextromethorphan was originally used for upper respiratory conditions such as allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold and headache disorder.
The TxGNN model predicts it may be effective for **nasal cavity disease**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Allergic rhinitis, vasomotor rhinitis, pharyngitis, common cold, rhinitis, nasopharyngitis, headache disorder (from the knowledge graph; no approved indication text in Philippines registration) |
| Predicted New Indication | Nasal cavity disease |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Dextromethorphan is known as a centrally acting antitussive (NMDA receptor antagonist and sigma-1 agonist). It has no established direct mechanism for treating nasal cavity pathology.

The high score most likely reflects the closeness of "nasal cavity disease" to the drug's existing indications (allergic rhinitis, vasomotor rhinitis, rhinitis) in the knowledge graph. This is essentially an overlap with existing indications rather than true repurposing. Any benefit would probably be symptomatic rather than disease-modifying.

Other predictions follow a similar pattern and are weaker or unsupported:

| Rank | Predicted Indication | Score | Comment |
|------|------|------|------|
| 2 | Acute laryngopharyngitis | 99.98% | Close to existing indications; possible symptomatic cough relief only |
| 3 | Faucial diphtheria | 99.36% | Bacterial toxin-mediated disease; no antibacterial activity, likely graph proximity |
| 4 | Trigeminal autonomic cephalalgia | 99.32% | Plausible but unverified link via NMDA antagonism and central sensitization |
| 5 | Cervical disc degenerative disorder | 99.30% | No clear mechanism; likely model artifact |
| 6 | Allergic urticaria | 99.25% | Not an antihistamine; likely proximity to allergic rhinitis |

All of these are L5 (model prediction only) with a Hold recommendation.

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for label safety information.

- **Contraindication-related conditions (knowledge graph, not label text)**: The knowledge graph links the drug to contraindications in several disease areas, including:
  - Cardiovascular: hypertension, hypotensive disorder, long QT syndrome (including familial), torsades de pointes
  - Hepatic and renal: liver failure, liver disease, kidney disease
  - Respiratory and neurological: epilepsy, COPD, bronchitis
  - Gastrointestinal: gastric ulcer, peptic ulcer disease, inflammatory bowel disease, pancreatitis, gallbladder disease
  - Endocrine and metabolic: diabetes mellitus, diabetic ketoacidosis, hypothyroidism, adrenocortical insufficiency, potassium deficiency
  - Other: thrombocytopenia, benign prostatic hyperplasia

  These should be verified against official labelling.

- **Drug Interactions**: 100 interactions were found. The main ones are:
  - **Major**: dexfenfluramine, fenfluramine, lorcaserin, sibutramine (serotonergic agents); dolasetron, granisetron, ondansetron, palonosetron (5-HT3 antagonists)
  - **Moderate**: bupropion, morphine (including liposomal), opium, cimetidine, dronabinol, nabilone, eliglustat, glycerol phenylbutyrate, mazindol, metoclopramide, phentermine

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but it is not supported by any clinical trials or literature. The prediction mostly overlaps with existing upper respiratory indications, and the only Philippines registration has been cancelled.

**To proceed, the following is needed:**
- Mechanism of action data (MOA) to assess the mechanistic link
- Package insert warnings and contraindications for the Philippines
- Literature and trial search for nasal cavity disease, and for trigeminal autonomic cephalalgia as the most plausible alternative
- Clarification of the cancelled registration status and available dosage forms and routes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

