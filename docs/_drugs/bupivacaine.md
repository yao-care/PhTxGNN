---
layout: default
title: Bupivacaine
parent: Model Prediction Only (L5)
nav_order: 53
evidence_level: L5
indication_count: 4
monitor_inn: "Bupivacaine"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "amyopathic dermatomyositis"]
last_modified_at: 2026-11-20
description: "Bupivacaine: predicted new indication acrodermatitis chronica atrophicans (evidence level L5). In the Philippines: 1 PNF entry"
---

# Bupivacaine
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

## Bupivacaine: local amide anesthetic (sodium channel blocker) → acrodermatitis chronica atrophicans
{: .text-alpha }

## One-Sentence Summary

Bupivacaine is a local anesthetic that blocks voltage-gated sodium channels.
The TxGNN model predicts it may be effective for **acrodermatitis chronica atrophicans**, but **no clinical trials and no publications** currently support this direction, so the prediction rests on the model alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 0.9923 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for bupivacaine: "Local anesthetics block the generation and the conduction of nerve impulses presumably by increasing the threshold for electrical excitation in the nerve, by slowing the propagation of the nerve impulse, and by reducing the rate of rise of the action potential. In general, the progression of anesthesia is related to the diameter, myelination, and conduction velocity of affected nerve fibers." ([DailyMed: Exparel (bupivacaine) prescribing information, Pacira Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bb5a9e59-0f51-11df-8a39-0800200c9a66), label version 2026-11-09; accessed 2026-11-19.) Bupivacaine is generally known as an amide local anesthetic that blocks voltage-gated sodium channels, which produces local numbness and pain relief.

Acrodermatitis chronica atrophicans is the late skin stage of Lyme borreliosis and is treated with antibiotics. A local anesthetic has no plausible role in treating the underlying infection. The high score (0.9923) is a model output only. It may reflect the drug's association with skin conditions, but no trial or publication backs it up. At most, bupivacaine could offer symptomatic or procedural pain relief, not disease modification.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Bupivacaine (as hydrochloride) | Injection |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: The interaction check found 56 interacting drugs. Those with a graded level are Moderate: aprepitant and liposomal morphine. Others, including pantoprazole, omeprazole, lansoprazole, vancomycin, atropine, several corticosteroids (triamcinolone, prednisone, prednisolone, hydrocortisone, dexamethasone), simvastatin, ondansetron, metoclopramide and naloxone, have no graded severity.

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
There are no clinical trials or publications for this disease, and no plausible mechanistic link between a local anesthetic and treatment of the underlying infection. The prediction stays at model level (L5).

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the Philippines regulator
- Mechanism of action data
- Any preclinical or clinical study that directly examines bupivacaine in acrodermatitis chronica atrophicans
- Review of route and formulation compatibility with the intended use

<!-- review:begin log -->

## Review Log

Below is the review log for this page. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-19 | "Detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Exparel (bupivacaine) prescribing information, Pacira Pharmaceuticals, Inc.](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=bb5a9e59-0f51-11df-8a39-0800200c9a66) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

