---
layout: default
title: Ceftriaxone
parent: Model Prediction Only (L5)
nav_order: 67
evidence_level: L5
indication_count: 7
monitor_inn: "Ceftriaxone"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "infectious otitis media", "blood group incompatibility", "suppurative otitis media", "chronic otitis media"]
last_modified_at: 2026-10-30
description: "Ceftriaxone: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Bacterial infections . The local licence record has no indication text"
---

# Ceftriaxone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
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

## Ceftriaxone: From Bacterial Infections to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Ceftriaxone is a third-generation cephalosporin antibiotic used against infections such as streptococcal infection, bacterial pneumonia, bacterial meningitis and gonorrhea.
The TxGNN model predicts it may be effective for **hyperamylasemia**, but **no clinical trials** and **no studies of ceftriaxone for this condition** support the prediction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (relations recorded in the knowledge graph, e.g. streptococcal infection, bacterial pneumonia, bacterial meningitis, gonorrhea). The local licence record has no indication text. |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9939 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
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

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0089 | Ceftriaxone | Valid, single-ingredient |

The local record lists no dosage form, manufacturer or approved indication text.

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

Note: other predictions in the same data, such as infectious otitis media, are far more biologically plausible and fit ceftriaxone's established antibacterial role. They would be better candidates for further review.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

