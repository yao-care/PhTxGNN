---
layout: default
title: Artemether
parent: Model Prediction Only (L5)
nav_order: 30
evidence_level: L5
indication_count: 8
monitor_inn: "Artemether"
predicted_indications: ["acquired angioedema", "angioedema", "hereditary angioedema", "nephrogenic syndrome of inappropriate antidiuresis", "acute contagious conjunctivitis", "scleroderma (disease)", "conjunctivitis", "renin-angiotensin-aldosterone system-blocker-induced angioedema"]
last_modified_at: 2026-11-12
description: "Artemether: predicted new indication acquired angioedema (evidence level L5). Approved use: Not recorded in the local data"
---

# Artemether
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **8** 
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

## Artemether: Artemisinin-class antimalarial → acquired angioedema
{: .text-alpha }

## One-Sentence Summary

Artemether is an artemisinin-class medicine. The TxGNN model predicts it may be relevant to **acquired angioedema**, with a score of 0.9990. There are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

<!-- review:begin ph-lic-20261106-artemether-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Artemether is an artemisinin-class medicine with a licence record in the Philippines." Removed: it conflicted with the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-artemether-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | acquired angioedema |
| TxGNN Prediction Score | 0.9990 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for artemether, so a mechanistic explanation cannot be built from the data compiled for this report.

No mechanistic link to acquired angioedema is established. Artemisinin-class compounds have been reported in preclinical work to have anti-inflammatory or immunomodulatory effects, but nothing in the compiled data supports this for artemether in angioedema. The high score is a computational prediction only, and any biological rationale remains speculative.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Artemether + Lumefantrin | Oral |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Disease-level contraindication signals (model-derived, not from label text)**: long QT syndrome, familial long QT syndrome, torsades de pointes, potassium deficiency disease. These suggest caution with QT prolongation and electrolyte disturbance.
- **Drug Interactions**: 95 interacting drugs were identified. Major interactions include:
  - Clarithromycin
  - Cobicistat
  - Amprenavir
  - Apalutamide
  - Atazanavir
  - Boceprevir

  Moderate interactions include dexamethasone, miconazole, troglitazone, deferasirox, bosentan and brigatinib, among others.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications and no known mechanistic link, so the evidence level is L5. In addition, the QT-related signals and the large number of interactions call for caution before any further work.

**To proceed, the following is needed:**
- Mechanism of action data for artemether
- Package insert warnings and contraindications from the Philippine regulator
- Preclinical or mechanistic studies linking artemether to bradykinin-mediated or other angioedema pathways
- A QT and electrolyte safety assessment for any new-indication population

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "with a licence record in the Philippines" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

