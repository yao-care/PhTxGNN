---
layout: default
title: Fentanyl
parent: Model Prediction Only (L5)
nav_order: 140
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Fentanyl: predicted new indication Nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not stated in the registration data"
---

# Fentanyl
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Fentanyl: From an Unspecified Original Indication to Nephrogenic Syndrome of Inappropriate Antidiuresis

## One-Sentence Summary

Fentanyl is a potent mu-opioid receptor agonist. The Philippines registration data compiled for this report does not state an approved indication.
The TxGNN model predicts it may be effective for **nephrogenic syndrome of inappropriate antidiuresis (NSIAD)**,
but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the registration data |
| Predicted New Indication | Nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 99.46% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Fentanyl is generally known as a mu-opioid receptor agonist used for strong analgesia, but the registration record here lists no approved indication.

The proposed link to NSIAD is weak. NSIAD is caused by gain-of-function mutations in the vasopressin V2 receptor gene (AVPR2), and less commonly in GNAS. No established mechanism connects mu-opioid agonism to V2 receptor signaling in the renal collecting duct. Opioids can increase vasopressin release and cause antidiuresis, which would tend to worsen the hyponatraemia seen in NSIAD rather than treat it.

The high prediction score is therefore most likely an artifact of the knowledge graph rather than a true therapeutic signal.

The second-ranked prediction, **Tourette syndrome** (score 99.05%), also has no trials or literature. Its rationale is speculative and indirect (opioid modulation of cortico-striatal circuits). Fentanyl's risks of respiratory depression, dependence and abuse make it a poor fit for a chronic neurodevelopmental condition that already has established treatments.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0188 | Fentanyl | Not stated | Not stated (status: cancelled) |

## Safety Considerations

- **Disease contraindications (knowledge-graph based, not label text)**: The knowledge graph lists contraindication links with the following conditions, among others:
  - Cardiovascular: hypertension, hypotensive disorder, orthostatic hypotension, long QT syndrome, torsades de pointes
  - Respiratory: COPD, asthma
  - Liver, kidney and gastrointestinal: liver failure and liver disease, kidney disease, pancreatitis, gallbladder disease, inflammatory bowel disease
  - Neurological and psychiatric: multiple system atrophy, basal ganglia disease, anxiety disorder, substance abuse/dependence
  - Others: benign prostatic hyperplasia, potassium deficiency disease

  These come from a computational knowledge graph and should be verified against the official label.
- **Drug Interactions**: 100 interactions were found. Examples of **Major** interactions include:
  - Alvimopan
  - Aprepitant
  - Bupropion
  - Clarithromycin
  - Clotrimazole
  - Dexamethasone
  - Dolasetron
  - Granisetron
  - Fenfluramine / Dexfenfluramine
  - Lorcaserin

  Examples of **Moderate** interactions include atropine, cimetidine, dicyclomine, glycopyrronium, hyoscyamine and eluxadoline.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction relies only on a model score, with no clinical trials or literature, and no plausible mechanistic link. The Philippines registration is cancelled, so no valid local license exists. Fentanyl's safety profile (respiratory depression, dependence, abuse potential) makes the benefit-risk balance unfavorable without supporting evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines
- Mechanism of action data (for example from DrugBank)
- Any preclinical or clinical evidence linking mu-opioid agonism to V2 receptor or renal water handling in NSIAD
- Clarification of the cancelled registration status and the original approved indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

