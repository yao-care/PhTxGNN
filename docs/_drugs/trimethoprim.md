---
layout: default
title: Trimethoprim
parent: Model Prediction Only (L5)
nav_order: 346
evidence_level: L5
indication_count: 1
last_modified_at: 2026-11-12
monitor_inn: "Trimethoprim"
predicted_indications: ["punctate epithelial keratoconjunctivitis"]
description: "Trimethoprim: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Trimethoprim
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Trimethoprim: Punctate epithelial keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Trimethoprim is an antibacterial drug originally used for urinary tract infections, ear infections, pneumocystosis, shigellosis and several forms of conjunctivitis.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**, but there are currently **0 clinical trials** and **0 publications** specific to this condition, so the prediction is a computational signal only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 0.9957 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on general pharmacological knowledge, trimethoprim is an antibacterial agent that is understood to inhibit bacterial dihydrofolate reductase. Its efficacy in bacterial infections, including bacterial conjunctivitis, is established, and the model likely links it to the new indication because of this closeness to its existing eye indications.

The high score (0.9957) most likely reflects network proximity to trimethoprim's existing ocular indications (conjunctivitis, acute contagious conjunctivitis, blepharoconjunctivitis). However, punctate epithelial keratoconjunctivitis is often viral (for example adenoviral) or non-infectious. An antibacterial drug would not be expected to act on a viral cause. No mechanistic link can be verified with the data compiled for this report.

## Clinical Trial Evidence

Currently no related clinical trials registered for punctate epithelial keratoconjunctivitis.

## Literature Evidence

No literature was found for the top predicted indication. The second-ranked prediction, conjunctivitis, is already an original indication of trimethoprim, so it is not a true repurposing candidate. The most relevant publications found for it are listed below for context.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [19043945](https://pubmed.ncbi.nlm.nih.gov/19043945/) | 2008 | Comparative clinical study (design not confirmed) | J Pediatr Ophthalmol Strabismus | Compared speed of clinical efficacy of polymyxin B/trimethoprim eye drops with 0.5% moxifloxacin in bacterial conjunctivitis |
| [6204534](https://pubmed.ncbi.nlm.nih.gov/6204534/) | 1984 | Clinical evaluation | Am J Ophthalmol | Evaluated efficacy and safety of trimethoprim combined with sulfacetamide and polymyxin B, or with polymyxin B alone, in bacterial conjunctivitis or blepharitis |
| [2418736](https://pubmed.ncbi.nlm.nih.gov/2418736/) | 1985 | Clinical study | Ann Ophthalmol | Trimethoprim-polymyxin B was clinically and bacteriologically effective in surface ocular bacterial infections |
| [8595639](https://pubmed.ncbi.nlm.nih.gov/8595639/) | 1995 | Survey | Clin Ther | Survey of children with acute bacterial conjunctivitis treated with trimethoprim-polymyxin B eye drops |
| [16491721](https://pubmed.ncbi.nlm.nih.gov/16491721/) | 2006 | Review | J Pediatr Ophthalmol Strabismus | Guidance on controlling contagious bacterial conjunctivitis |
| [20084257](https://pubmed.ncbi.nlm.nih.gov/20084257/) | 2001 | Review | Paediatr Child Health | Etiology, clinical features and management of acute infectious conjunctivitis in children |
| [30007329](https://pubmed.ncbi.nlm.nih.gov/30007329/) | 2018 | Systematic review/meta-analysis | J Pediatric Infect Dis Soc | Antibiotic treatments for neonatal chlamydial conjunctivitis, including trimethoprim; relevance to trimethoprim unclear |

Many other retrieved publications were off-target (cat-scratch disease, veterinary studies, Stevens-Johnson syndrome, a Nocardia case report) and are not listed.

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Cotrimoxazole (sulfamethoxazole + trimethoprim) | Oral, Injection |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

No package insert warnings or contraindications are available; please refer to the package insert for safety information. The following items come from drug-disease relationships in the knowledge graph, not from label text.

- **Possible disease-related contraindications (knowledge graph)**: porphyria (including inherited porphyria and porphyrin metabolism disease), kidney disease, liver disease, gallbladder disease, pyoureter, thrombocytopenia, neutropenia, agranulocytosis, G6PD deficiency, folic acid deficiency anemia, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, glycogen storage disease, cystinuria, galactosemia.
- **Drug Interactions**: 100 interactions were identified; the main ones are listed below.
  - **Major**: potassium citrate, potassium bicarbonate, potassium chloride, potassium gluconate (the potassium salts carry a risk of raised potassium).
  - **Moderate**: metformin, pioglitazone, rosiglitazone, repaglinide, balsalazide, picosulfuric acid, sapropterin.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for punctate epithelial keratoconjunctivitis rests on the model score alone, with no trials or literature, and the likely viral or non-infectious cause makes an antibacterial mechanism implausible. Label safety data are missing.

<!-- review:begin ph-lic-20261106-trimethoprim-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The local registration is cancelled, with no indication text or dosage form on record, and label safety data are missing." Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-trimethoprim-1 -->

**To proceed, the following is needed:**
- Mechanism of action data for trimethoprim
- Evidence that bacterial infection contributes to punctate epithelial keratoconjunctivitis, or clinical data in this condition
- Package insert warnings and contraindications, to complete the safety screening
- Confirmation of an available ophthalmic formulation and its route compatibility
- Review of the 2008 and 1984 ophthalmic studies for design and outcomes, to confirm that they are controlled studies

<!-- review:begin ph-lic-20261106-trimethoprim-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Confirmation of an available ophthalmic formulation and its route compatibility, given the cancelled local registration" Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-trimethoprim-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "The local registration is cancelled, with no indication text or dosage form on record, and l" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-06 | Removed: "given the cancelled local registration" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

