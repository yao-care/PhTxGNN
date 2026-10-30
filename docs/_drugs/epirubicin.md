---
layout: default
title: Epirubicin
parent: Model Prediction Only (L5)
nav_order: 128
evidence_level: L5
indication_count: 7
monitor_inn: "Epirubicin"
predicted_indications: ["primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "small cell lung carcinoma", "pulmonary blastoma", "lung mixed small cell and squamous cell carcinoma", "myeloid leukemia", "upper aerodigestive tract neoplasm"]
last_modified_at: 2026-10-30
description: "Epirubicin: predicted new indication primary pulmonary lymphoma (evidence level L5). Approved use: Not recorded in the local data"
---

# Epirubicin
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

## Epirubicin: anthracycline topoisomerase II inhibitor → primary pulmonary lymphoma
{: .text-alpha }

## One-Sentence Summary

Epirubicin is an anthracycline cytotoxic chemotherapy drug that damages DNA and blocks topoisomerase II.
The TxGNN model predicts it may be useful for **primary pulmonary lymphoma**, with a score of 0.9971.
**No clinical trials** are registered for this disease, and the **6 publications** retrieved are general reviews, case reports, or studies of regimens for other lymphomas. The evidence is therefore still at the model-prediction stage.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | primary pulmonary lymphoma |
| TxGNN Prediction Score | 0.9971 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Epirubicin is known as an anthracycline (a doxorubicin epimer) that intercalates into DNA and inhibits topoisomerase II. Drugs of this class are components of several lymphoma regimens, including CHOP-like regimens and the VEBEP regimen used in Hodgkin lymphoma. This gives a plausible class-level link to lymphoma.

The link to primary pulmonary lymphoma is indirect, for three reasons:
- The retrieved literature mostly covers other lymphoma types, such as diffuse large B-cell lymphoma and pleural MALT lymphoma.
- The DLBCL regimens in that literature (R-CHOP, Pola-R-CHP) use doxorubicin, not epirubicin.
- No study in the data shows epirubicin being used or tested in primary pulmonary lymphoma itself.

The high TxGNN score is a computational prediction. It is not backed by direct clinical evidence for this disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [7686469](https://pubmed.ncbi.nlm.nih.gov/7686469/) | 1993 | Review | Drugs | Review of epirubicin pharmacology and its use across cancers; general background, not specific to pulmonary lymphoma |
| [1866500](https://pubmed.ncbi.nlm.nih.gov/1866500/) | 1991 | Case report | Rev Invest Clin | Case of primary non-Hodgkin lymphoma of the lung with pleural effusion; the only retrieved report on the disease itself, with no epirubicin link evident in the available abstract |
| [36237246](https://pubmed.ncbi.nlm.nih.gov/36237246/) | 2022 | Case report | Transl Cancer Res | Misdiagnosed primary MALT lymphoma of the pleura (a related but different site) |
| [39192408](https://pubmed.ncbi.nlm.nih.gov/39192408/) | 2024 | Cohort | Zhongguo Shi Yan Xue Ye Xue Za Zhi | Single-centre retrospective analysis of primary extranodal DLBCL in the rituximab era |
| [10526668](https://pubmed.ncbi.nlm.nih.gov/10526668/) | 1999 | Cohort | Cancer J Sci Am | Pilot study of the intensive VEBEP regimen plus radiotherapy in advanced Hodgkin disease |
| [40728626](https://pubmed.ncbi.nlm.nih.gov/40728626/) | 2025 | Cohort | Ann Hematol | Retrospective study of Pola-R-CHP in 117 DLBCL patients; the regimen contains doxorubicin, not epirubicin |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracycline class) |
| Myelosuppression Risk | High (neutropenia and thrombocytopenia are expected; please refer to the package insert) |
| Emetogenicity Classification | Moderate to high, depending on dose |
| Monitoring Items | CBC with differential, liver and renal function, cardiac function (anthracycline cardiotoxicity) |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Drug Interactions**: Screening returned 100 potential interactions. Those shown in the data include:
  - **Major**: cimetidine, dolasetron.
  - **Moderate**: acarbose, famotidine, pioglitazone, loperamide, bupropion, clarithromycin, levofloxacin, minocycline, naltrexone, palonosetron.
  - **Minor**: metronidazole.

Please refer to the package insert for warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but there are no registered trials. No retrieved study tests epirubicin in primary pulmonary lymphoma, and the related lymphoma literature mainly involves other drugs or other lymphoma types. Evidence therefore rests on model prediction alone (L5).

**To proceed, the following is needed:**
- Detailed mechanism of action data
- A targeted literature review of anthracycline use in primary pulmonary lymphoma, including epirubicin-specific reports
- Package insert warnings and contraindications from the Philippine regulator
- A comparison with current standard lymphoma regimens, weighing cardiotoxicity and myelosuppression
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

