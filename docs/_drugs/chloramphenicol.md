---
layout: default
title: Chloramphenicol
parent: Model Prediction Only (L5)
nav_order: 72
evidence_level: L5
indication_count: 8
monitor_inn: "Chloramphenicol"
predicted_indications: ["diffuse scleroderma", "postinfectious vasculitis", "post-bacterial disorder", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "punctate epithelial keratoconjunctivitis"]
last_modified_at: 2026-11-12
description: "Chloramphenicol: predicted new indication Diffuse scleroderma (evidence level L5). Approved use: Not recorded in the local data"
---

# Chloramphenicol
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

## Chloramphenicol: Diffuse scleroderma
{: .text-alpha }

## One-Sentence Summary

Chloramphenicol is an antibacterial drug. The TxGNN model predicts it may be relevant to **diffuse scleroderma** (score 0.9965). However, **no clinical trials** exist and the 4 publications retrieved are laboratory studies, not evidence that the drug works in patients.

<!-- review:begin ph-lic-20261106-chloramphenicol-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Chloramphenicol is an antibacterial drug that is currently registered in the Philippines." Removed: it conflicted with the PNF data (the Philippine National Formulary as of 2026-11-06). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-chloramphenicol-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Diffuse scleroderma |
| TxGNN Prediction Score | 0.9965 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Chloramphenicol is a broad-spectrum antibacterial, and nothing in the data compiled for this report links it to a therapeutic effect in scleroderma.

The four publications retrieved concern collagen gene regulation in scleroderma skin cells (alpha1(I) procollagen promoter activity, Smad3/Sp1/p300 interaction, and TGF-beta signalling). In this type of research, chloramphenicol appears to be used as a laboratory reporter tool (a chloramphenicol acetyltransferase reporter gene), not as a treatment. The high prediction score most likely reflects this literature association rather than a real therapeutic signal.

Overall, the prediction is a model output without a supported biological or clinical rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8702443](https://pubmed.ncbi.nlm.nih.gov/8702443/) | 1996 | Basic research | Arthritis and Rheumatism | Studied how the alpha 1(I) procollagen gene is switched on in skin fibroblasts from patients with recent-onset diffuse systemic sclerosis, including the role of intronic sequences |
| [16319104](https://pubmed.ncbi.nlm.nih.gov/16319104/) | 2006 | Basic research | Rheumatology (Oxford) | Examined TGF-beta/Smad signalling and its role in increased collagen gene expression in scleroderma fibroblasts |
| [9811061](https://pubmed.ncbi.nlm.nih.gov/9811061/) | 1998 | Basic research | Arthritis and Rheumatism | Identified promoter elements and transcription factors behind raised alpha1(I) procollagen expression in systemic sclerosis |
| [11229480](https://pubmed.ncbi.nlm.nih.gov/11229480/) | 2001 | Basic research | Arthritis and Rheumatism | Showed that blocking TGF-beta signalling reduced excess collagen synthesis in scleroderma fibroblasts |

All four are laboratory studies. None tested chloramphenicol as a treatment in patients.

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Chloramphenicol | Oral, Injection |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

The approved indication is not recorded in the local data.

<!-- review:begin ph-lic-20261106-chloramphenicol-2 -->

> **Review correction (2026-11-06)**: Originally stated: "The Philippines licence for single-ingredient chloramphenicol is valid. The approved indication is not recorded in the local data." Removed: it described the products as single-ingredient or combination products in a way that did not match the PNF data (the Philippine National Formulary as of 2026-11-06). Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-chloramphenicol-2 -->

## Safety Considerations

Package insert warnings and contraindications were not available in the data compiled for this report. Please refer to the package insert for full safety information.

**Drug Interactions** (100 interactions were identified; examples shown below):
- **Major:** cisapride, naloxegol
- **Moderate:** aprepitant, balsalazide, metronidazole, budesonide, iron, and several sulfonylurea diabetes drugs (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), as well as repaglinide, saxagliptin, rosuvastatin, simvastatin, eliglustat, naldemedine and nitisinone

**Conditions of concern:** Chloramphenicol is associated with blood-related toxicity. Related records list the following as conditions where use is a concern: anaemia (including aplastic anaemia), neutropenia and agranulocytosis, thrombocytopenia, paroxysmal nocturnal haemoglobinuria, kidney disease, liver disease, gallbladder disease, peripheral neuropathy, optic neuritis and acute intermittent porphyria. These are not taken from the product label and should be checked against it.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone. The only literature is laboratory research in which chloramphenicol is most likely a reporter-assay tool, and there are no clinical trials. With the known blood toxicity of the drug, there is no basis to advance this indication.

**To proceed, the following is needed:**
- Evidence that chloramphenicol itself has an effect on scleroderma, such as preclinical studies using the drug as a test agent
- Mechanism of action data
- Local package insert warnings and contraindications
- A risk-benefit assessment given the haematological toxicity profile

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "that is currently registered in the Philippines" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-06 | Removed: "The Philippines licence for single-ingredient chloramphenicol is valid" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

