---
layout: default
title: Dipyridamole
parent: Model Prediction Only (L5)
nav_order: 112
evidence_level: L5
indication_count: 6
monitor_inn: "Dipyridamole"
predicted_indications: ["sick sinus syndrome 2, autosomal dominant", "sarcoglycanopathy", "Wildervanck syndrome", "macrocephaly, dysmorphic facies, and psychomotor retardation", "lateral sinus thrombosis", "cavernous sinus thrombosis"]
last_modified_at: 2026-11-12
description: "Dipyridamole: predicted new indication Sick sinus syndrome 2, autosomal dominant (evidence level L5). In the Philippines: 1 PNF entry"
---

# Dipyridamole
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

## Dipyridamole: Sick sinus syndrome 2, autosomal dominant
{: .text-alpha }

## One-Sentence Summary

Dipyridamole is an antiplatelet medicine that is marketed in the Philippines. The TxGNN model predicts it may be useful for **sick sinus syndrome 2, autosomal dominant**, but the data compiled for this report contain **no clinical trials and no publications** on this disease. The prediction rests on the model score alone, and a plausible mechanism is lacking.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Sick sinus syndrome 2, autosomal dominant |
| TxGNN Prediction Score | 0.9989 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for dipyridamole: "Dipyridamole inhibits the uptake of adenosine into platelets, endothelial cells and erythrocytes in vitro and in vivo; the inhibition occurs in a dose-dependent manner at therapeutic concentrations (0.5 to 1.9 mcg/mL). This inhibition results in an increase in local concentrations of adenosine which acts on the platelet A 2 -receptor thereby stimulating platelet adenylate cyclase and increasing platelet cyclic-3',5'-adenosine monophosphate (cAMP) levels." ([DailyMed: dipyridamole prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=226099e2-70bb-4b9b-bb52-c20fbca2aec5), label version 2026-04-29; accessed 2026-11-19.) Dipyridamole is generally known as an antiplatelet agent that raises local adenosine levels.

The predicted disease is an inherited disorder of the heart's pacemaker, linked to HCN4-related channel dysfunction. Dipyridamole's antiplatelet and adenosine-related actions do not address that underlying channel problem. Higher adenosine levels could in theory slow heart rate or conduction, which could worsen bradyarrhythmia. No mechanistic rationale supports this prediction, and the high score is a computational output only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

<!-- review:begin ph-lic-20261106-dipyridamole-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The Philippines has one valid single-ingredient licence for dipyridamole." Removed: the number or status of PNF entries stated here did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-dipyridamole-1 -->

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Dipyridamole | Oral |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: The interaction screen returned 100 interacting drugs in total. Those rated Moderate are **dexfenfluramine, sibutramine and fenfluramine**. Others, such as acetylsalicylic acid, cimetidine, morphine, metformin and omeprazole, appear without a severity rating.
- **Disease-specific concern**: Because dipyridamole can raise adenosine levels, any use in a patient with a rhythm disorder involving slow heart rate would need careful cardiac assessment.

Please refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting trials or publications (evidence level L5) and no plausible mechanism. There is also a theoretical risk that adenosine-related effects could worsen slow heart rhythms.

**To proceed, the following is needed:**
- Mechanism of action data for dipyridamole, and a mechanistic review of its effects on pacemaker-cell and HCN4 channel function
- Preclinical or case-level evidence showing any benefit in this disease
- Package insert warnings and contraindications from the Philippine regulator, to complete the safety review
- Cardiac safety assessment, with attention to bradyarrhythmia risk

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The Philippines has one valid single-ingredient licence for dipyridamole" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available for this drug in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: dipyridamole prescribing information, REMEDYREPACK INC.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=226099e2-70bb-4b9b-bb52-c20fbca2aec5) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

