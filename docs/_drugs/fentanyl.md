---
layout: default
title: Fentanyl
parent: Model Prediction Only (L5)
nav_order: 140
evidence_level: L5
indication_count: 2
monitor_inn: "Fentanyl"
predicted_indications: ["nephrogenic syndrome of inappropriate antidiuresis", "Tourette syndrome"]
last_modified_at: 2026-10-27
description: "Fentanyl: predicted new indication nephrogenic syndrome of inappropriate antidiuresis (evidence level L5). Approved use: Not recorded in the local data"
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

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Fentanyl: mu-opioid receptor agonist → nephrogenic syndrome of inappropriate antidiuresis
{: .text-alpha }

## One-Sentence Summary

Fentanyl is a potent opioid analgesic that acts on the mu-opioid receptor.
The TxGNN model predicts it may be relevant to **nephrogenic syndrome of inappropriate antidiuresis**, with a score of **0.9946**.
There are currently **no clinical trials** and **no publications** supporting this direction, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nephrogenic syndrome of inappropriate antidiuresis |
| TxGNN Prediction Score | 0.9946 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Fentanyl is known as a mu-opioid receptor agonist, but no established mechanism links it to the signaling that drives this condition.

Nephrogenic syndrome of inappropriate antidiuresis is caused by gain-of-function mutations in the vasopressin V2 receptor gene (AVPR2), and less commonly in GNAS. This leads to excess water retention and low blood sodium. Opioids can increase vasopressin release and cause antidiuresis, which would worsen low sodium rather than treat the condition.

The high score is therefore most likely an artifact of the model, not a true therapeutic signal. The prediction should be treated as a hypothesis only, and the mechanistic rationale is weak.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0188 | Fentanyl | Not recorded | Not recorded |

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for safety information.

- **Drug Interactions**: 100 interacting drugs were identified; the main ones are listed below.
  - **Major**: alvimopan, aprepitant, bupropion, clarithromycin, clotrimazole, dexamethasone, dexfenfluramine, dolasetron, fenfluramine, granisetron, lorcaserin
  - **Moderate**: atropine, cimetidine, clidinium, dicyclomine, dronabinol, eluxadoline, glycerol phenylbutyrate, glycopyrronium, hyoscyamine

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score. No clinical trials or publications exist, and the known pharmacology of opioids (increased vasopressin release and antidiuresis) points in the opposite direction from a benefit in this condition.

**To proceed, the following is needed:**
- Mechanistic evidence linking mu-opioid signaling to V2 receptor or GNAS pathways in the renal collecting duct
- Preclinical studies in relevant models of the disease
- Mechanism of action data for fentanyl from DrugBank
- Philippines package insert warnings and contraindications for safety screening
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

