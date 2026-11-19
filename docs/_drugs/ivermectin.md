---
layout: default
title: Ivermectin
parent: Model Prediction Only (L5)
nav_order: 191
evidence_level: L5
indication_count: 9
monitor_inn: "Ivermectin"
predicted_indications: ["vulvovaginal candidiasis", "esophageal candidiasis", "anogenital human papillomavirus infection", "vulvovaginitis", "candida glabrata", "neonatal candidiasis", "congenital candidiasis", "postmenopausal atrophic vaginitis", "candidiasis, invasive"]
last_modified_at: 2026-11-12
description: "Ivermectin: predicted new indication Vulvovaginal candidiasis (evidence level L5). In the Philippines: 1 PNF entry"
---

# Ivermectin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Ivermectin: Antiparasitic (avermectin class) → vulvovaginal candidiasis
{: .text-alpha }

## One-Sentence Summary

Ivermectin is an antiparasitic drug. The TxGNN model predicts it may be relevant for **vulvovaginal candidiasis**, with a score of 0.9995. The data compiled for this report contain **no clinical trials and no publications** that directly study this disease, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Vulvovaginal candidiasis |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Clinical Pharmacology section of the US FDA-approved prescribing information for ivermectin: "In vitro studies using human liver microsomes and recombinant CYP450 enzymes have shown that ivermectin is primarily metabolized by CYP3A4." ([DailyMed: Stromectol (ivermectin) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=681888c9-af79-4b7d-ae80-c3f4f6f1effd), label version 2024-09-20; accessed 2026-11-19.) Ivermectin is generally known as an antiparasitic that acts on glutamate-gated chloride channels in invertebrates. These channels are not present in fungi, so no mechanistic link to *Candida* infection is established.

The high score is a computational prediction only. Several other predictions for this drug are also candidiasis- or vaginitis-related, which suggests the score may reflect proximity among related disease entries in the model rather than a demonstrated antifungal effect. This prediction should be treated as a hypothesis, not as evidence of efficacy.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for vulvovaginal candidiasis.

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Ivermectin | Oral |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: The interaction check returned 100 records, and the main ones are listed below.
  - Moderate: aprepitant, clarithromycin, ethanol, cobicistat, deferasirox, iodide I-123, iodide I-131, dicoumarol, fostamatinib, warfarin, abametapir (topical)
  - Level not classified: omeprazole, lansoprazole, prednisone, prednisolone, ranitidine, famotidine, dexamethasone, ursodeoxycholic acid, heparin

Please refer to the package insert for other safety information (warnings and contraindications).

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or publications, and no plausible antifungal mechanism is identified in the available data. Evidence remains at the model-prediction level (L5).

**To proceed, the following is needed:**
- Mechanism of action data for ivermectin, and evidence of any activity against *Candida* species (e.g. in vitro studies)
- Clinical or preclinical studies directly addressing vulvovaginal candidiasis
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Confirmation of route and dosage form compatibility with the intended use

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Currently, detailed mechanism of action data for this drug is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Stromectol (ivermectin) prescribing information, Merck Sharp & Dohme LLC](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=681888c9-af79-4b7d-ae80-c3f4f6f1effd) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

