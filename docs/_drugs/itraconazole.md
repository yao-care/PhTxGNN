---
layout: default
title: Itraconazole
parent: Model Prediction Only (L5)
nav_order: 190
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Itraconazole: predicted new indication Pneumocystosis (evidence level L4). Approved use: Esophageal candidiasis, candidemia, histoplasmosis, aspergillosis…"
monitor_inn: "Itraconazole"
predicted_indications: ["pneumocystosis"]
---

# Itraconazole
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

## Itraconazole: From Fungal Infections to Pneumocystosis
{: .text-alpha }

## One-Sentence Summary

Itraconazole is an azole antifungal originally used for fungal infections such as candidiasis, histoplasmosis, aspergillosis, blastomycosis and sporotrichosis.
The TxGNN model predicts it may be effective for **pneumocystosis**, but there are currently **0 registered clinical trials** and only indirect literature (**20 publications**, mostly reviews, case reports and general infection studies).
The mechanistic link is weak, so this prediction should be treated with caution.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Esophageal candidiasis, candidemia, histoplasmosis, aspergillosis, blastomycosis, sporotrichosis and other fungal infections (the registration record lists no approved indication text) |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 0.9934 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, itraconazole inhibits fungal lanosterol 14-alpha-demethylase (CYP51), which blocks ergosterol synthesis in the fungal cell membrane. This explains its efficacy across many fungal infections.

The prediction for pneumocystosis is mechanistically doubtful. *Pneumocystis jirovecii* lacks ergosterol in its cell membrane and uses cholesterol instead, so azole antifungals are not expected to work well against it. Standard treatment and prophylaxis (trimethoprim-sulfamethoxazole, atovaquone, pentamidine) act through different pathways.

The high score comes from the TxGNN model (deep learning) and most likely reflects itraconazole's broad antifungal profile and similarities the model learned between related diseases, such as other fungal diseases (e.g., histoplasmosis, aspergillosis), not biological evidence or a true mechanistic link. Literature that mentions both itraconazole and *Pneumocystis* is mostly about broad prophylaxis or co-infection in immunocompromised patients, not about itraconazole treating pneumocystosis itself.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

None of the publications below shows that itraconazole treats pneumocystosis. They cover immunocompromised populations in which *Pneumocystis* and other fungal infections occur together. The most relevant item is the itraconazole prophylaxis trial in HIV patients.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11737382](https://pubmed.ncbi.nlm.nih.gov/11737382/) | 2001 | Phase III RCT (double-blind, placebo-controlled) | HIV Medicine | Itraconazole capsules for preventing deep fungal infections in HIV-infected, immunodeficient patients. Abstract excerpt does not report a pneumocystosis result |
| [26036497](https://pubmed.ncbi.nlm.nih.gov/26036497/) | 2015 | Cohort | Transplantation Proceedings | Invasive fungal infections after kidney transplantation, associated with higher mortality and graft dysfunction |
| [21418688](https://pubmed.ncbi.nlm.nih.gov/21418688/) | 2010 | Review | BMJ Clinical Evidence | Primary and secondary prophylaxis of opportunistic infections in HIV |
| [15250025](https://pubmed.ncbi.nlm.nih.gov/15250025/) | 2004 | Review | Clinical Infectious Diseases | Antimicrobial prophylaxis in febrile neutropenia; trimethoprim-sulfamethoxazole is highly effective against *P. carinii* pneumonia |
| [21973267](https://pubmed.ncbi.nlm.nih.gov/21973267/) | 2011 | Review | Clinical Pharmacokinetics | Penetration of antifungal and other anti-infective agents into pulmonary epithelial lining fluid |
| [8016481](https://pubmed.ncbi.nlm.nih.gov/8016481/) | 1993 | Review | Seminars in Respiratory Infections | Infection after lung transplantation |
| [8397916](https://pubmed.ncbi.nlm.nih.gov/8397916/) | 1993 | Review | Current Clinical Topics in Infectious Diseases | Prophylaxis and treatment of infection in bone marrow transplant recipients |
| [2121456](https://pubmed.ncbi.nlm.nih.gov/2121456/) | 1990 | Review | Drugs | Therapy and prophylaxis of systemic protozoan infections, including *P. carinii* |
| [2233233](https://pubmed.ncbi.nlm.nih.gov/2233233/) | 1990 | Case series | Medicine | Disseminated histoplasmosis in AIDS: clinical findings, diagnosis and treatment |
| [36891307](https://pubmed.ncbi.nlm.nih.gov/36891307/) | 2023 | Case report and review | Frontiers in Immunology | *Talaromyces marneffei* and *P. jirovecii* co-infection in a child with a STAT1 mutation |

---

## Safety Considerations

- **Contraindications (from knowledge-graph drug-disease edges, not label text):** long QT syndrome, torsades de pointes, congestive heart failure and other cardiomyopathies, liver disease and drug-induced liver injury, kidney disease and impaired renal function, chronic obstructive pulmonary disease, peripheral neuropathy, hearing loss, and vision disorders, among others.
- **Drug Interactions (100 interactions found; examples):**
  - **Major:** loperamide, triamcinolone, budesonide
  - **Moderate:** famotidine, ranitidine, omeprazole, rabeprazole, cimetidine, dexamethasone, hydrocortisone, betamethasone, aprepitant, alosetron
  - **Minor:** metformin, pioglitazone, chlorpropamide, amphotericin B

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone: there are no clinical trials, and no study shows itraconazole is effective against pneumocystosis. *Pneumocystis* lacks ergosterol, so the azole mechanism is not expected to work, and established therapies exist. In the Philippines, the only registration is cancelled.

**To proceed, the following is needed:**
- Mechanistic evidence, or preclinical data, showing activity against *Pneumocystis*
- Complete mechanism of action data for itraconazole
- Package insert warnings and contraindications for safety screening
- Clarification of the cancelled registration status and available dosage forms in the Philippines
- Evidence that itraconazole offers any advantage over standard prophylaxis and treatment (trimethoprim-sulfamethoxazole, atovaquone, pentamidine)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

