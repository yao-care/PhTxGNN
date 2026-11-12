---
layout: default
title: Amoxicillin
parent: Model Prediction Only (L5)
nav_order: 26
evidence_level: L5
indication_count: 8
monitor_inn: "Amoxicillin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague"]
last_modified_at: 2026-11-12
description: "Amoxicillin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Bacterial infections (urinary tract infection, otitis media…"
---

# Amoxicillin
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

## Amoxicillin: From Bacterial Infections to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Amoxicillin is a beta-lactam antibiotic whose relations recorded in the knowledge graph include urinary tract infection, otitis media, streptococcal and staphylococcal infections, and bacterial pneumonia. The TxGNN model predicts it may be effective for **hyperamylasemia**, but **no clinical trials and no publications** support this prediction, so it rests on model output alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (urinary tract infection, otitis media, pneumonia, pharyngitis and others), as recorded in the knowledge graph; the local licence record contains no indication text |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9963 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 2) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 2 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Amoxicillin is generally known as a beta-lactam antibiotic that inhibits bacterial cell wall synthesis, and its use is in bacterial infections.

Hyperamylasemia is a biochemical finding with varied non-infectious causes (pancreatic, salivary, renal). No plausible mechanistic link between an antibacterial agent and this condition was identified. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence, and it has no supporting clinical or literature evidence. Other top-ranked predictions (polyclonal hyperviscosity syndrome, congenital analbuminemia, premalignant hematological disease) show the same pattern: high scores, no supporting studies, and no mechanistic rationale.

The one prediction with a biologically plausible antibacterial angle is **septicemic plague** (score 0.9913), but the evidence is limited to animal and in vitro studies, and beta-lactams are not standard first-line therapy for plague.

## Clinical Trial Evidence

Currently no related clinical trials registered for hyperamylasemia.

## Literature Evidence

Currently no related literature available for hyperamylasemia.

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Amoxicillin (as trihydrate) | Oral |
| Co-Amoxiclav (amoxicillin + potassium clavulanate) | Oral |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

The record shows no manufacturer or indication text.

<!-- review:begin ph-lic-20261106-amoxicillin-1 -->

> **Review correction (2026-11-06)**: Originally stated: "This is a single-ingredient product with valid status. The record shows no manufacturer or indication text." Removed: it described the products as single-ingredient or combination products in a way that did not match the PNF data (the Philippine National Formulary as of 2026-11-06). Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-amoxicillin-1 -->

## Safety Considerations

- **Relations recorded in the knowledge graph as contraindications** (not label text): long QT syndrome, torsades de pointes, ventricular tachycardia, liver failure, liver disease, cholestasis, kidney disease, porphyria, Clostridium difficile colitis, myasthenia gravis, osteoporosis, bone fracture, gallbladder disease, infectious mononucleosis, and related conditions. These should be verified against the package insert.
- **Drug Interactions** (100 interactions found; main ones shown):
  - **Major**: Methotrexate; live cholera vaccine (Vibrio cholerae CVD 103-HgR)
  - **Moderate**: Doxycycline, minocycline, demeclocycline, ethinylestradiol, estradiol, anisindione, dicoumarol, mycophenolate mofetil, entecavir, balsalazide, probiotics (Lactobacillus acidophilus, Bifidobacterium longum infantis), indium In-111 oxyquinoline
  - **Minor**: Allopurinol, amiloride, azithromycin, clarithromycin, erythromycin

Package insert warnings and contraindications for the Philippines product were not available. Please refer to the package insert for safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for hyperamylasemia has a high model score but no clinical trials, no literature, and no plausible mechanism. The evidence level is L5. The studies found for other predicted diseases (blood group incompatibility, monoclonal gammopathy, septicemic plague) do not directly show a therapeutic effect of amoxicillin.

**To proceed, the following is needed:**
- Mechanism of action data for amoxicillin
- Package insert warnings and contraindications from the Philippines product, including dosage form and approved indications
- Any clinical or mechanistic evidence linking amoxicillin to hyperamylasemia
- If the antibacterial direction is pursued, septicemic plague could be explored as a research question, but it would require clinical evidence beyond the current animal and in vitro studies

<!-- review:begin ph-lic-20261106-amoxicillin-2 -->

> **Review correction (2026-11-06)**: Originally stated: "Package insert warnings and contraindications from the Philippines product (PNF-xxxx), including dosage form and approved indications" Removed: it conflicted with the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 2 entries for this drug, 2 current; the Quick Overview and the table under Philippines Market Information show the current figures. "PNF-xxxx" stands for a code an earlier version of this site's software assigned to the record; the PNF has no entry numbers, so the code is not shown. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-amoxicillin-2 -->

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "This is a single-ingredient product with valid status" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-06 | Removed: "(PNF-xxxx)" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

