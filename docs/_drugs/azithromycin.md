---
layout: default
title: Azithromycin
parent: Model Prediction Only (L5)
nav_order: 36
evidence_level: L5
indication_count: 10
monitor_inn: "Azithromycin"
predicted_indications: ["hyperamylasemia", "polyclonal hyperviscosity syndrome", "congenital analbuminemia", "punctate epithelial keratoconjunctivitis", "blood group incompatibility", "premalignant hematological system disease", "monoclonal gammopathy", "hematological disease associated with an acquired peripheral neuropathy", "septicemic plague", "congenital hematological disorder"]
last_modified_at: 2026-10-28
description: "Azithromycin: predicted new indication Hyperamylasemia (evidence level L5). Approved use: Not stated in the local licence record. The TxGNN model (deep learning) score may reflect similarities the model learned between related diseases, not biological evidence…"
---

# Azithromycin
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

## Azithromycin: From Bacterial Infections to Hyperamylasemia
{: .text-alpha }

## One-Sentence Summary

Azithromycin is a macrolide antibiotic whose recorded uses in the knowledge graph are bacterial infections such as streptococcal and staphylococcal infections, bacterial pneumonia, conjunctivitis and chancroid.
The TxGNN model gives its top prediction as **hyperamylasemia**, but **no clinical trials and no publications** support this prediction.
The best-supported repurposing directions in the data compiled for this report are in other diseases, such as congenital hematological disorders (sickle cell disease), but those studies are indirect or were withdrawn.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the local licence record. The knowledge graph records streptococcal infection, bacterial pneumonia, staphylococcal infection, conjunctivitis, chancroid and others (relations recorded in the knowledge graph, not approved indications) |
| Predicted New Indication | Hyperamylasemia |
| TxGNN Prediction Score | 0.9981 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Number of Approvals | 1 registration (single-ingredient) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Azithromycin is a macrolide antibiotic. No plausible mechanism connecting it to a reduction in serum amylase is supported by the data compiled for this report.

The high score (0.9981) comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Without any trial or publication on hyperamylasemia, the prediction cannot be considered mechanistically supported, so the evidence level is L5.

Other predicted indications offer more biological plausibility, although none has direct clinical support:
- **Congenital hematological disorder (sickle cell disease):** azithromycin has anti-inflammatory and immunomodulatory actions and may reduce respiratory infections that trigger acute chest syndrome. Two relevant trials were withdrawn with zero enrollment.
- **Monoclonal gammopathy:** one preclinical study showed macrolides block autophagy flux and sensitize myeloma cells to bortezomib.
- **Septicemic plague:** one in vitro study showed azithromycin had poor activity against *Yersinia pestis* strains.
- **Punctate epithelial keratoconjunctivitis:** the only paper is a diagnostic case report that does not test azithromycin.

## Clinical Trial Evidence

Currently no related clinical trials are registered for hyperamylasemia.

For reference, trials found under the lower-ranked prediction "congenital hematological disorder" are listed below. They do not support the top prediction.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02960503](https://clinicaltrials.gov/study/NCT02960503) | Phase 1/2 | Withdrawn | 0 | Macrolide therapy to improve FEV1 in adults with sickle cell disease; no data generated |
| [NCT02630394](https://clinicaltrials.gov/study/NCT02630394) | Phase 1 | Withdrawn | 0 | Pilot of azithromycin prophylaxis for acute chest syndrome in sickle cell disease; no data generated |
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5000 | General pharmacokinetics and safety study of understudied drugs in children; not specific to this indication |

## Literature Evidence

Currently no related literature is available for hyperamylasemia.

For reference, selected publications from lower-ranked predictions are below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26408070](https://pubmed.ncbi.nlm.nih.gov/26408070/) | 2015 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Antibiotics for preventing lower respiratory tract infections in high-risk children; indirect support for sickle cell disease |
| [23546223](https://pubmed.ncbi.nlm.nih.gov/23546223/) | 2013 | Preclinical study | Int J Oncol | Macrolides including azithromycin block autophagy flux and enhance bortezomib cytotoxicity in myeloma cell lines |
| [8540736](https://pubmed.ncbi.nlm.nih.gov/8540736/) | 1995 | In vitro study | Antimicrob Agents Chemother | Azithromycin showed poor activity against 78 *Yersinia pestis* strains |
| [12698575](https://pubmed.ncbi.nlm.nih.gov/12698575/) | 2002 | Preclinical study | Antibiot Khimioter | Azithromycin was highly active in experimental brucellosis |
| [32826651](https://pubmed.ncbi.nlm.nih.gov/32826651/) | 2021 | Case report | Cornea | Diagnosis of microsporidial keratoconjunctivitis; does not show azithromycin efficacy |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0036 | Azithromycin | Not specified | Not specified |

The record shows one valid single-ingredient registration. Approved indication text is not available in the local record.

## Safety Considerations

- **Relations recorded in the knowledge graph (not label text):** azithromycin has contraindication links to long QT syndrome, familial long QT syndrome, torsades de pointes, liver disease, gallbladder disease, *Clostridium difficile* colitis, perinatal necrotizing enterocolitis, myasthenia gravis, neuromuscular junction disease, and hearing and auditory system disorders.
- **Drug Interactions:** 100 interactions were found. Those listed include the following.
  - **Major:** cisapride, dolasetron (both relate to QT-prolongation risk).
  - **Moderate:** famotidine, loperamide, clarithromycin, levofloxacin, granisetron, aluminum hydroxide, magnesium-containing antacids, balsalazide, and several laxatives (bisacodyl, castor oil, glycerin, lactitol, lactulose).
  - **Minor:** amoxicillin, metronidazole.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction, hyperamylasemia, rests only on a score from the TxGNN model (deep learning), which may reflect similarities the model learned between related diseases, not biological evidence, with no trials, no publications and no supported mechanism. The strongest alternative direction (sickle cell disease) has only withdrawn trials and indirect evidence. Safety signals, especially QT prolongation, add to the need for caution.

**To proceed, the following is needed:**
- Mechanism of action data and a plausible biological link to the predicted disease
- Package insert warnings and contraindications from the Philippines FDA
- Any clinical or observational data on azithromycin and serum amylase
- If the sickle cell disease direction is pursued, a new adequately powered trial with a cardiac (QT) safety plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

