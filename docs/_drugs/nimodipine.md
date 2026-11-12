---
layout: default
title: Nimodipine
parent: Model Prediction Only (L5)
nav_order: 252
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
description: "Nimodipine: predicted new indication Homozygous familial hypercholesterolemia (evidence level L5). Approved use: Subarachnoid hemorrhage (including acquired aneurysmal subarachnoid h…"
monitor_inn: "Nimodipine"
predicted_indications: ["homozygous familial hypercholesterolemia", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Nimodipine
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

## Nimodipine: From Subarachnoid Hemorrhage to Homozygous Familial Hypercholesterolemia
{: .text-alpha }

## One-Sentence Summary

Nimodipine is a calcium channel blocker originally used for subarachnoid hemorrhage, including aneurysmal subarachnoid hemorrhage.
The TxGNN model predicts it may be effective for **homozygous familial hypercholesterolemia**,
but there are currently **0 clinical trials** and **0 publications** supporting this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Subarachnoid hemorrhage (including acquired aneurysmal subarachnoid hemorrhage) |
| Predicted New Indication | Homozygous familial hypercholesterolemia |
| TxGNN Prediction Score | 0.9929 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Nimodipine is known to be a dihydropyridine L-type calcium channel blocker, and its efficacy in subarachnoid hemorrhage is established. Whether this mechanism applies to homozygous familial hypercholesterolemia is unclear.

The link between the two conditions is weak. Homozygous familial hypercholesterolemia is caused by dysfunction of the LDL receptor pathway. Calcium channel blockers have been explored for possible anti-atherosclerotic or vascular effects, but this does not address that underlying defect. The score of 0.9929 is a model prediction only and has no supporting clinical or literature evidence.

A second prediction, **nephrogenic syndrome of inappropriate antidiuresis** (score 0.9905), has the same limitation. The disease is driven by gain-of-function variants in the vasopressin V2 receptor (AVPR2) or in GNAS, and calcium channel blockade does not clearly target that pathway. Calcium signaling does act downstream in aquaporin-2 regulation, so a loose hypothetical link exists, but it is unsupported. This prediction also has no trials or publications and an L5 evidence level.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Nimodipine | Oral |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications (from knowledge graph, not label text)**: The TxGNN knowledge graph links nimodipine with contraindications in liver disease, gallbladder disease and hypotensive disorder.
- **Drug Interactions**: The interaction query found 100 records in total. The first 20 are listed here.
  - **Major**: Clarithromycin, Dolasetron
  - **Moderate**: Bupropion, Aprepitant, Morphine, Acetylsalicylic acid, Calcium phosphate, Calcium acetate, Calcium carbonate, Calcium chloride, Canagliflozin, Dapagliflozin, Empagliflozin, Cimetidine, Dronabinol, Nabilone, Magnesium sulfate, Kanamycin, Neomycin, Miconazole

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has only a model score (L5), with no clinical trials or publications and no clear mechanistic link to either predicted indication. No label-based safety data are available.

<!-- review:begin ph-lic-20261106-nimodipine-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The only Philippines registration has been cancelled, and no label-based safety data are available." Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-nimodipine-1 -->

**To proceed, the following is needed:**
- Mechanism of action data for nimodipine (for example, from DrugBank)
- Package insert warnings and contraindications from DOH-FDA Philippines
- Preclinical or mechanistic studies testing nimodipine in homozygous familial hypercholesterolemia
- A systematic literature and trial-registry search for the predicted indication
- Clarification of whether a valid local product is available
- Review of the major interactions (clarithromycin, dolasetron) and of the hypotension and liver disease concerns

<!-- review:begin ph-lic-20261106-nimodipine-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Clarification of whether a valid local product is available, since the sole registration is cancelled" Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-nimodipine-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The only Philippines registration has been cancelled, and n" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-06 | Removed: "since the sole registration is cancelled" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

