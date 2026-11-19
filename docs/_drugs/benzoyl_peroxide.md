---
layout: default
title: Benzoyl Peroxide
parent: Model Prediction Only (L5)
nav_order: 41
evidence_level: L5
indication_count: 4
monitor_inn: "Benzoyl peroxide"
predicted_indications: ["vulvar inverted follicular keratosis", "2-hydroxyethyl methacrylate sensitization", "acrodermatitis chronica atrophicans", "acne keloid"]
last_modified_at: 2026-11-12
description: "Benzoyl Peroxide: predicted new indication vulvar inverted follicular keratosis (evidence level L5). In the Philippines: 1 PNF entry"
---

# Benzoyl Peroxide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Benzoyl Peroxide: Topical keratolytic and antibacterial agent → vulvar inverted follicular keratosis
{: .text-alpha }

## One-Sentence Summary

Benzoyl peroxide is a topical agent with keratolytic, comedolytic and antibacterial effects.
The TxGNN model predicts it may be effective for **vulvar inverted follicular keratosis**, but the prediction rests on the model alone: **no clinical trials and no publications** were found for this condition.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | vulvar inverted follicular keratosis |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for benzoyl peroxide: "Benzoyl peroxide is an oxidizing agent with bactericidal and keratolytic effects but the precise mechanism of action in the treatment of rosacea is unknown." ([DailyMed: Epsolay (benzoyl peroxide) prescribing information, Mayne Pharma Commercial LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=641981e6-460b-44dd-8146-306c47e5367c), label version 2025-08-11; accessed 2026-11-19.) Benzoyl peroxide is known for keratolytic, comedolytic and antimicrobial effects, which could plausibly act on follicular keratinization.

Inverted follicular keratosis is a benign follicular-derived lesion that is related to seborrheic keratosis, a skin condition for which benzoyl peroxide is also used. This relatedness is the likely basis of the model's signal. However, no clinical or mechanistic data support the use of benzoyl peroxide at the vulvar site. The vulvar mucosa is also sensitive to irritation, which raises a safety concern for a product known to cause local irritation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Benzoyl Peroxide | Gel |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Disease associations flagged as contraindications (not from label text)**: Photosensitivity disease, photoparoxysmal response, kidney disease, diabetes mellitus, diabetic ketoacidosis, inflammatory bowel disease (including Crohn disease and ulcerative colitis), exfoliative dermatitis, dermatitis, skin atrophy, telangiectasis, hereditary hemorrhagic telangiectasia, peripheral vascular disease, adrenocortical insufficiency, anogenital human papillomavirus infection and common wart. These come from model-derived data and should be checked against the package insert.
- **Local tolerability**: Vulvar mucosa is sensitive to irritation, so use at this site raises a specific concern.

No drug interaction records were found. Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has a very high model score, but no clinical trials or publications address vulvar inverted follicular keratosis, so the evidence level is L5. Mucosal irritation at the vulvar site adds a safety concern.

**To proceed, the following is needed:**
- Direct clinical or histopathological evidence for benzoyl peroxide in inverted follicular keratosis
- Mechanism of action data
- Package insert warnings and contraindications from the Philippine regulator
- Assessment of vulvar mucosal tolerability and a suitable formulation

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data is not available" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Epsolay (benzoyl peroxide) prescribing information, Mayne Pharma Commercial LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=641981e6-460b-44dd-8146-306c47e5367c) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

