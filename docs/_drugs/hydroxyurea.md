---
layout: default
title: Hydroxyurea
parent: Model Prediction Only (L5)
nav_order: 168
evidence_level: L5
indication_count: 9
monitor_inn: "Hydroxyurea"
predicted_indications: ["female breast carcinoma", "sickle cell-hemoglobin d disease syndrome", "sickle cell-hemoglobin c disease syndrome", "sickle cell-beta-thalassemia disease syndrome", "sickle cell-hemoglobin E disease syndrome", "cervical adenosarcoma", "colon mucinous adenocarcinoma", "rectum mucinous adenocarcinoma", "gallbladder mucinous adenocarcinoma"]
last_modified_at: 2026-10-30
description: "Hydroxyurea: predicted new indication female breast carcinoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Hydroxyurea
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
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

## Hydroxyurea: ribonucleotide reductase inhibitor → female breast carcinoma
{: .text-alpha }

## One-Sentence Summary

Hydroxyurea is an antineoplastic drug that inhibits ribonucleotide reductase and is registered in the Philippines.
The TxGNN model predicts it may be effective for **female breast carcinoma**.
There are **no registered clinical trials** for this disease and **20 publications** were retrieved, but they are mostly preclinical or only indirectly relevant, so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | female breast carcinoma |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Hydroxyurea inhibits ribonucleotide reductase. This depletes the deoxynucleotide (dNTP) pool needed for DNA synthesis and induces replication stress in dividing cells. Detailed mechanism-of-action data are not otherwise available in the data compiled for this report.

Several preclinical papers link replication-stress biology to breast cancer. These include studies of RPA2 hyperphosphorylation and DNA repair, where valproic acid sensitised breast cancer cells to hydroxyurea. They also include work on ATR inhibition in breast and ovarian cancer cell lines. An in-silico paper proposed lipid conjugates of hydroxyurea for breast cancer. This supports biological plausibility, but none of it shows clinical benefit in patients with breast cancer.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No retrieved paper is a clinical study of hydroxyurea in breast cancer. The most relevant items are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38211596](https://pubmed.ncbi.nlm.nih.gov/38211596/) | 2024 | In-silico design | Drug Research | Designed hydroxyurea–lipid conjugates to improve cellular uptake, targeting the PI3K/AKT/mTOR pathway in breast cancer |
| [28837865](https://pubmed.ncbi.nlm.nih.gov/28837865/) | 2017 | Preclinical | DNA Repair | Valproic acid sensitised breast cancer cells to hydroxyurea by inhibiting RPA2 hyperphosphorylation-mediated DNA repair |
| [32795962](https://pubmed.ncbi.nlm.nih.gov/32795962/) | 2020 | Preclinical | DNA Repair | A valproic acid analogue influenced RPA2-mediated DNA repair in breast carcinoma, building on hydroxyurea sensitisation |
| [21730979](https://pubmed.ncbi.nlm.nih.gov/21730979/) | 2011 | Preclinical | Br J Cancer | An ATR inhibitor was evaluated in breast and ovarian cancer cell lines (replication-stress pathway) |
| [37777742](https://pubmed.ncbi.nlm.nih.gov/37777742/) | 2023 | Preclinical | Mol Cancer | EYA4 promotes breast cancer progression through replication stress avoidance |
| [1957839](https://pubmed.ncbi.nlm.nih.gov/1957839/) | 1991 | Phase 1 | Am J Clin Oncol | 5-FU/leucovorin followed by hydroxyurea in 20 patients with advanced gastrointestinal and breast cancer; mixed tumours |
| [1733549](https://pubmed.ncbi.nlm.nih.gov/1733549/) | 1992 | Phase 1/2 | Cancer Chemother Pharmacol | Cisplatin, 5-FU, hydroxyurea and radiotherapy in mixed advanced solid tumours |
| [30159181](https://pubmed.ncbi.nlm.nih.gov/30159181/) | 2018 | Case report | Case Rep Hematol | Breast cancer coexisting with essential thrombocythemia, and the therapeutic challenges involved |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0236 | Hydroxyurea | Not recorded | Not recorded |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (antimetabolite, ribonucleotide reductase inhibitor) |
| Myelosuppression Risk | Please refer to the package insert warnings and precautions |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | Please refer to the package insert warnings and precautions; typically CBC, liver and renal function |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Drug Interactions**: 100 interactions were recorded. The only one with a stated severity is Minor (levofloxacin); the others, such as doxycycline, amphotericin B, hydrocortisone, famotidine, acetylsalicylic acid, pantoprazole, metformin, morphine, omeprazole and simvastatin, have no severity grade.
- **Conditions of concern**: Kidney disease, thrombocytopenia, anemia, macrocytic anemia, leukopenia, pyoureter and cutaneous vasculitis are recorded as contraindication-type concerns. These do not come from label text and need confirmation against the package insert.

Please refer to the package insert for other safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but no clinical trial and no clinical study of hydroxyurea in breast cancer was retrieved. Supporting papers are preclinical, in-silico or only indirectly relevant, so the evidence level is L5.

**To proceed, the following is needed:**
- Clinical data (trials or well-designed observational studies) of hydroxyurea in breast carcinoma
- Package insert warnings and contraindications from the Philippines regulator
- Detailed mechanism-of-action data
- A safety monitoring plan covering myelosuppression, kidney function and the conditions listed above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

