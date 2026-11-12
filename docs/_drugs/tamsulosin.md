---
layout: default
title: Tamsulosin
parent: Model Prediction Only (L5)
nav_order: 325
evidence_level: L5
indication_count: 10
last_modified_at: 2026-11-12
description: "Tamsulosin: predicted new indication Ambras type hypertrichosis universalis congenita (evidence level L5). Approved use: Benign prostatic hyperplasia"
monitor_inn: "Tamsulosin"
predicted_indications: ["Ambras type hypertrichosis universalis congenita", "hypertrichosis (disease)", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "hypotrichosis simplex of the scalp", "congenital hypotrichosis milia", "diffuse alopecia areata", "alopecia", "migraine with brainstem aura"]
---

# Tamsulosin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Tamsulosin: From Benign Prostatic Hyperplasia to Ambras Type Hypertrichosis Universalis Congenita
{: .text-alpha }

## One-Sentence Summary

Tamsulosin was originally used to treat benign prostatic hyperplasia (BPH).
The TxGNN model predicts it may be effective for **Ambras type hypertrichosis universalis congenita**, but **0 clinical trials** and **0 publications** currently support this prediction.
The result is a computational prediction only and has no supporting evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Benign prostatic hyperplasia |
| Predicted New Indication | Ambras type hypertrichosis universalis congenita |
| TxGNN Prediction Score | 1.0000 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Tamsulosin is generally known as an alpha-1A/1D adrenergic receptor antagonist. It relaxes smooth muscle in the prostate and bladder neck and is used to relieve urinary symptoms of BPH.

The relationship between the original and predicted indications is weak. Ambras syndrome is a rare genetic disorder of hair growth, linked to chromosomal rearrangements that affect regulation of the *TRPS1* gene. Alpha-1 adrenergic blockade has no established role in this process, so no mechanistic link can be established. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

The other top predictions show the same pattern. They include hypertrichosis, hypotrichosis, alopecia, alopecia areata, hair shaft abnormalities, Dandy-Walker malformation syndromes, dental/periodontal malformation syndromes and migraine with brainstem aura. All are at evidence level L5, with no plausible mechanistic connection and no supporting trials. The two papers retrieved for alopecia do not test tamsulosin (see below).

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

No literature directly supports the top prediction (Ambras type hypertrichosis universalis congenita). The only publications retrieved were for the rank 9 prediction, alopecia, and neither tests tamsulosin:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33175100](https://pubmed.ncbi.nlm.nih.gov/33175100/) | 2021 | Cohort/Pharmacovigilance | JAMA Dermatology | Examines suicidality and psychological adverse events with finasteride, a 5-alpha-reductase inhibitor. It is about finasteride, not tamsulosin. |
| [32826647](https://pubmed.ncbi.nlm.nih.gov/32826647/) | 2021 | Cross-sectional/Observational | Cornea | Studies meibomian gland changes in men with BPH. It does not address alopecia or tamsulosin treatment. |

---

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Tamsulosin | Oral |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

---

## Safety Considerations

- **Contraindications / conditions of concern (from the knowledge graph, not label text)**: multiple system atrophy, postural orthostatic tachycardia syndrome, orthostatic hypotension, liver disease, gallbladder disease, priapism, intraoperative floppy iris syndrome.
- **Drug Interactions**: 100 interactions were identified, and 20 are listed in the data compiled for this report. Most are Moderate. One is Major: **clarithromycin**. Moderate examples include bupropion, aprepitant, morphine, cimetidine, canagliflozin, dapagliflozin, empagliflozin, ertugliflozin, miconazole, clotrimazole, fenfluramine and opium.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction has no supporting clinical trials or literature and no plausible mechanistic link between alpha-1 adrenergic blockade and Ambras syndrome. The evidence level is L5 (model prediction only).

<!-- review:begin ph-lic-20261031-tamsulosin-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The prediction has no supporting clinical trials or literature and no plausible mechanistic link between alpha-1 adrenergic blockade and Ambras syndrome. The only Philippines registration is cancelled." Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-10-31). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261031-tamsulosin-1 -->

**To proceed, the following is needed:**
- Mechanistic evidence, or preclinical data linking alpha-1A/1D blockade to hair follicle biology
- Detailed mechanism of action data (MOA)
- Philippines package insert warnings and contraindications, and confirmation of current registration status
- Evidence of unmet need and a feasible study design, given that Ambras syndrome is a rare genetic disorder
- Review of the other top-ranked predictions, such as hypertrichosis and alopecia, only if new supporting evidence emerges

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The only Philippines registration is cancelled" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

