---
layout: default
title: Epirubicin
parent: Moderate Evidence (L3-L4)
nav_order: 128
evidence_level: L4
indication_count: 7
last_modified_at: 2026-10-15
description: "Epirubicin: predicted new indication Primary pulmonary lymphoma (evidence level L4). Approved use: Breast carcinoma / breast neoplasm"
monitor_inn: "Epirubicin"
predicted_indications: ["primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "small cell lung carcinoma", "pulmonary blastoma", "lung mixed small cell and squamous cell carcinoma", "myeloid leukemia", "upper aerodigestive tract neoplasm"]
---

# Epirubicin
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **7** 
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

## Epirubicin: From Breast Carcinoma to Primary Pulmonary Lymphoma
{: .text-alpha }

## One-Sentence Summary

Epirubicin is an anthracycline chemotherapy drug, originally used to treat breast carcinoma.
The TxGNN model predicts it may be effective for **primary pulmonary lymphoma**, but there are **0 registered clinical trials** and only **6 publications** (reviews, case reports and retrospective studies, none specific to epirubicin in this disease), so the evidence is weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Breast carcinoma / breast neoplasm |
| Predicted New Indication | Primary pulmonary lymphoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, epirubicin is an anthracycline, a class that inhibits topoisomerase II and intercalates into DNA. Its efficacy in breast carcinoma has been established, and mechanistically it may be applicable to lymphoma.

Anthracyclines are components of several established lymphoma regimens, such as CHOP-like regimens and the VEBEP regimen used in Hodgkin's disease. This gives a plausible class-level link between epirubicin and lymphoma, including lymphoma arising in the lung.

However, the link is indirect. The retrieved literature on DLBCL regimens (R-CHOP, Pola-R-CHP) involves doxorubicin, not epirubicin. The high TxGNN score is a computational prediction and is not backed by direct clinical evidence in this indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7686469](https://pubmed.ncbi.nlm.nih.gov/7686469/) | 1993 | Review | Drugs | General review of epirubicin's pharmacology and use in cancer chemotherapy. Reports efficacy equivalent to doxorubicin in breast and lung cancers, with no lymphoma-specific data in the available text. |
| [40728626](https://pubmed.ncbi.nlm.nih.gov/40728626/) | 2025 | Cohort | Annals of Hematology | Retrospective study of 117 DLBCL patients given first-line Pola-R-CHP (a doxorubicin-containing regimen). Examines efficacy and safety in lower-risk or trial-ineligible patients. |
| [39192408](https://pubmed.ncbi.nlm.nih.gov/39192408/) | 2024 | Cohort | Zhongguo Shi Yan Xue Ye Xue Za Zhi | Single-center retrospective analysis of clinical features and prognostic factors in primary extranodal DLBCL in the rituximab era. |
| [10526668](https://pubmed.ncbi.nlm.nih.gov/10526668/) | 1999 | Cohort | The Cancer Journal from Scientific American | Pilot study of the intensive VEBEP regimen plus involved-field radiotherapy in advanced Hodgkin's disease. |
| [36237246](https://pubmed.ncbi.nlm.nih.gov/36237246/) | 2022 | Case report | Translational Cancer Research | Case of primary MALT lymphoma of the pleura that was misdiagnosed; diagnostic focus, not treatment with epirubicin. |
| [1866500](https://pubmed.ncbi.nlm.nih.gov/1866500/) | 1991 | Case report | Revista de Investigacion Clinica | Case of primary non-Hodgkin's lymphoma of the lung with pleural effusion. |

None of these studies shows a treatment benefit of epirubicin in primary pulmonary lymphoma.

## Philippines Market Information

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0170 | Epirubicin | Cancelled |

The only registration is cancelled, so no valid epirubicin registration currently exists in the Philippines. Dosage form and approved indication details are not available.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline class, topoisomerase II inhibitor) |
| Myelosuppression Risk | High (the knowledge-graph contraindications include neutropenia, thrombocytopenia and agranulocytosis) |
| Emetogenicity Classification | Moderate to high (typical for anthracycline chemotherapy; confirm against the package insert) |
| Monitoring Items | CBC with differential, liver and renal function, cardiac function (e.g., LVEF/echocardiography), cumulative anthracycline dose |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication signals (from a drug-disease knowledge graph, not from label text)**: liver failure, liver disease, kidney disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, hemoglobinopathy, stomatitis, pyoureter, and a group of cardiac conditions (myocardial infarction, coronary thrombosis, cardiomyopathy including hypertrophic cardiomyopathy, endomyocardial fibrosis, myocardial disorder, heart conduction disease, sudden cardiac arrest).
- **Drug Interactions**: 100 interactions were found in total. The two classified as **Major** among those reviewed are **cimetidine** and **dolasetron**. Examples of **Moderate** interactions include clarithromycin, levofloxacin, bupropion, famotidine, pioglitazone, loperamide, palonosetron and naltrexone.
- For warnings and label-based contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests mainly on the model score and a class-level link between anthracyclines and lymphoma. There are no registered trials, the available literature does not examine epirubicin in this disease, and the only Philippines registration is cancelled. Given epirubicin's cardiotoxicity and myelosuppression, and the existing doxorubicin-based lymphoma standards, the benefit-risk case is not yet supported.

**To proceed, the following is needed:**
- Disease-specific clinical evidence for epirubicin in primary pulmonary lymphoma (prospective or well-documented retrospective studies)
- A comparison with doxorubicin-based regimens already standard for lymphoma
- Detailed mechanism of action data
- Package insert warnings and contraindications from the Philippine FDA
- Clarification of the cancelled registration status and product availability
- A cardiac and hematologic safety monitoring plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

