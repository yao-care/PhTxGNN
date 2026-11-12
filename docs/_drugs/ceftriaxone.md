---
layout: default
title: Ceftriaxone
parent: Model Prediction Only (L5)
nav_order: 67
evidence_level: L5
indication_count: 5
monitor_inn: "Ceftriaxone"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "blood group incompatibility", "chronic otitis media"]
last_modified_at: 2026-11-12
description: "Ceftriaxone: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Not recorded in the local data"
---

# Ceftriaxone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ceftriaxone: Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic used against infections such as streptococcal infection, bacterial pneumonia, bacterial meningitis and gonorrhea.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but **no clinical trials** and **no studies of ceftriaxone for this condition** support the prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9939 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. In general, ceftriaxone is a cephalosporin that kills bacteria by blocking cell wall synthesis.

Hyperamylasemia is a laboratory finding, an elevated blood amylase level, rather than an infection. It has many causes, including pancreatic disease and head injury. Ceftriaxone has no known effect on amylase regulation, so no credible mechanistic link was identified. The very high score (0.9939) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The only loosely related item is a small study of ceftriaxone given to prevent infection after a biliary-pancreatic endoscopic procedure. In that setting the antibiotic targets infection, not amylase elevation.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10458061](https://pubmed.ncbi.nlm.nih.gov/10458061/) | 1999 | Clinical study | Bratisl Lek Listy | 30 patients received ceftriaxone 1 g after endoscopic papillosphincterotomy and were compared with 30 who did not. The study concerns infection prophylaxis, not treatment of hyperamylasemia. |
| [7522351](https://pubmed.ncbi.nlm.nih.gov/7522351/) | 1994 | Cohort | South Med J | Of 38 patients with intracranial bleeding, 25 had raised lipase and 17 of those also had raised amylase, without pancreatitis. It describes the condition and does not involve ceftriaxone. |
| [36263834](https://pubmed.ncbi.nlm.nih.gov/36263834/) | 2023 | Case report | Rev Esp Enferm Dig | A Weil syndrome case with upper gastrointestinal bleeding. It provides no evidence that ceftriaxone treats hyperamylasemia. |

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Ceftriaxone (as disodium/sodium salt) | Injection |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

The local record lists no manufacturer or approved indication text.

<!-- review:begin ph-lic-20261106-ceftriaxone-1 -->

> **Review correction (2026-11-06)**: Originally stated: "The local record lists no dosage form, manufacturer or approved indication text." Removed: its description of the Philippine products did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-ceftriaxone-1 -->

## Safety Considerations

Label warnings and contraindications from the package insert are not available in the data compiled for this report.

- **Contraindications recorded in the knowledge graph (not label text)**: liver disease, gallbladder disease, neonatal jaundice, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, hemolytic anemia.
- **Drug interactions** (100 recorded in total; main ones shown):
  - Major: calcium chloride, calcium glucoheptonate, calcium gluconate.
  - Moderate: kanamycin, neomycin, streptomycin, picosulfuric acid.

Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Hyperamylasemia is a laboratory finding, ceftriaxone has no plausible mechanism for correcting it, and no trial or study shows a benefit. The prediction looks like a model artifact. The evidence level is L5.

**To proceed, the following is needed:**
- A clear clinical rationale for treating an elevated amylase, which is a sign rather than a disease.
- Retrieval of the package insert for warnings and contraindications.
- Mechanism of action data from DrugBank.

They would be better candidates for further review.

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "dosage form" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

