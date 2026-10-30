---
layout: default
title: Vancomycin
parent: Model Prediction Only (L5)
nav_order: 351
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Vancomycin: predicted new indication Diffuse scleroderma (evidence level L5). Approved use: Clostridium difficile colitis, staphylococcal infections…"
monitor_inn: "Vancomycin"
predicted_indications: ["diffuse scleroderma", "paratyphoid fever", "salmonellosis", "congenital analbuminemia", "hyperamylasemia", "polyclonal hyperviscosity syndrome", "typhoid fever", "blood group incompatibility", "streptococcal pneumonia", "premalignant hematological system disease"]
---

# Vancomycin
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

## Vancomycin: From Clostridium difficile Colitis and Staphylococcal Infections to Diffuse Scleroderma
{: .text-alpha }

## One-Sentence Summary

Vancomycin is a glycopeptide antibiotic originally used for Gram-positive bacterial infections such as *Clostridium difficile* colitis, staphylococcal infections, and endocarditis.
The TxGNN model predicts it may be effective for **Diffuse Scleroderma**, but there are **0 clinical trials** and only **1 unrelated case report**, so this prediction is most likely a computational artifact.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Clostridium difficile colitis, staphylococcal infections, endocarditis, bacterial arthritis, staphylococcal pneumonia |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. From general pharmacology, vancomycin is a glycopeptide antibiotic that blocks bacterial cell wall synthesis and acts only on Gram-positive bacteria.

Diffuse scleroderma (systemic sclerosis) is an autoimmune disease marked by fibrosis and blood-vessel damage. No plausible antibacterial mechanism links vancomycin to this process. The high TxGNN score (ranked 892nd) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. The one paper retrieved is a case report on erythroderma with sepsis and eosinophilia, which is not about scleroderma.

**Other top predictions were also reviewed:**

| Predicted Indication | TxGNN Score | Assessment |
|------|------|------|
| Paratyphoid fever | 0.9985 | Gram-negative organism, intrinsically resistant to vancomycin; no efficacy evidence |
| Salmonellosis | 0.9981 | Same issue; literature is mostly resistance surveillance |
| Congenital analbuminemia | 0.9979 | No mechanism; no trials or literature |
| Polyclonal hyperviscosity syndrome | 0.9979 | No mechanism; no trials or literature |
| Hyperamylasemia | 0.9979 | A laboratory finding, not a treatable disease target |
| Typhoid fever | 0.9975 | Gram-negative; guideline therapy uses other agents |
| Blood group incompatibility | 0.9963 | No antibacterial target; the one paper is unrelated |
| **Streptococcal pneumonia** | 0.9960 | Only mechanistically credible candidate (L4, "Research Question"), but it overlaps with the existing staphylococcal pneumonia indication, is not a true new use, and has no direct trial evidence |
| Premalignant hematological system disease | 0.9954 | No mechanism; no trials or literature |

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31541072](https://pubmed.ncbi.nlm.nih.gov/31541072/) | 2019 | Case report | The American Journal of Case Reports | A 56-year-old man with diffuse exfoliative rash, sepsis, and eosinophilia (erythroderma). It does not concern scleroderma and gives no evidence for vancomycin in this disease. |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0508 | Vancomycin | Not specified | Not specified (registration valid) |

---

## Safety Considerations

- **Contraindications (from the TxGNN model (deep learning), not label text; these may reflect similarities the model learned between related diseases, not biological evidence)**: kidney disease, pyoureter, neutropenia, agranulocytosis, hearing disorder, auditory system disease.
- **Drug Interactions**: 100 interactions were identified, of which 20 were reviewed. Major-level interactions include:
  - Human immunoglobulin G (intravenous)
  - Human botulinum neurotoxin A/B immune globulin
  - Vibrio cholerae CVD 103-HgR live vaccine

  Moderate-level interactions include nephrotoxic or ototoxic agents (amikacin, amphotericin B, capreomycin, carboplatin, bacitracin), NSAIDs (ketorolac, ibuprofen, diclofenac, celecoxib), and others such as metformin, estradiol, ethinylestradiol, mesalazine, balsalazide, ibandronate, and cholestyramine.

Please also refer to the package insert for full warnings. Label-based warnings were not available in the data compiled for this report.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for diffuse scleroderma rests only on a model score. There is no clinical trial, no relevant literature, and no plausible mechanism. Vancomycin is currently marketed in the Philippines, with 1 valid license out of 1.

**To proceed, the following is needed:**
- A mechanistic rationale connecting vancomycin to systemic sclerosis pathophysiology, if any exists
- Mechanism of action data (MOA) from DrugBank
- Package insert warnings and contraindications from DOH-FDA Philippines
- Clarification of why the registration was cancelled and whether any valid vancomycin product exists locally
- If a repurposing candidate is still wanted, streptococcal pneumonia (resistant pneumococcus) is the only mechanistically credible option. It should be treated as an extension of an existing use, not a novel repurposing, and would need direct clinical evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

