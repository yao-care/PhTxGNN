---
layout: default
title: Dacarbazine
parent: Model Prediction Only (L5)
nav_order: 93
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-31
description: "Dacarbazine: predicted new indication Upper aerodigestive tract neoplasm (evidence level L4). Approved use: Hodgkin lymphoma, metastatic melanoma"
monitor_inn: "Dacarbazine"
predicted_indications: ["upper aerodigestive tract neoplasm"]
---

# Dacarbazine
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

## Dacarbazine: From Hodgkin Lymphoma and Metastatic Melanoma to Upper Aerodigestive Tract Neoplasm
{: .text-alpha }

## One-Sentence Summary

Dacarbazine is an alkylating chemotherapy drug, originally used to treat Hodgkin lymphoma and metastatic melanoma.
The TxGNN model predicts it may be effective for **upper aerodigestive tract neoplasm**,
but **no clinical trials** are registered for this indication, and the **20 publications** compiled for this report offer only indirect, site-based support.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin lymphoma, metastatic melanoma (the Philippines registration record has no approved indication text) |
| Predicted New Indication | Upper aerodigestive tract neoplasm |
| TxGNN Prediction Score | 0.9926 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Dacarbazine is an alkylating agent. It is a prodrug that is activated in the body to MTIC, which methylates DNA and kills dividing tumour cells. Detailed mechanism of action data is not available in the data compiled for this report, so this explanation rests on general knowledge of the drug class.

The link to the predicted indication is indirect and based on anatomical site rather than disease type. Melanoma and Hodgkin lymphoma, the two original indications, can both involve the head and neck or the upper aerodigestive mucosa. Examples in the literature include mucosal melanoma and extranodal Hodgkin lymphoma at head and neck sites. Dacarbazine-containing regimens have also been reported in head and neck-region tumours such as medullary thyroid carcinoma and malignant paraganglioma. These are not true upper aerodigestive tract squamous neoplasms.

The very high TxGNN score is a computational prediction only. No trial or direct clinical study in this indication supports it.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No randomized trial tests dacarbazine in upper aerodigestive tract neoplasm. The most relevant items found are listed below.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41481311](https://pubmed.ncbi.nlm.nih.gov/41481311/) | 2026 | RCT (Phase 3) | JAMA Oncol | Toripalimab vs dacarbazine as first-line therapy in acral melanoma. Dacarbazine is only the comparator, and the population is not the predicted indication. |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | Clinical study | Ann Oncol | Small study of dacarbazine plus 5-FU in advanced medullary thyroid cancer, a head and neck-region neuroendocrine tumour. |
| [31621203](https://pubmed.ncbi.nlm.nih.gov/31621203/) | 2019 | Prospective observational | Cancer Med | Carbon-ion radiotherapy plus dacarbazine, nimustine and vincristine in 21 patients with head and neck mucosal melanoma. |
| [11815960](https://pubmed.ncbi.nlm.nih.gov/11815960/) | 2002 | Preclinical | Cancer | In nude mice with medullary thyroid carcinoma xenografts, dacarbazine was the most effective single agent tested, and it was combined with radioimmunotherapy. |
| [20564093](https://pubmed.ncbi.nlm.nih.gov/20564093/) | 2010 | Cohort | Cancer | Retrospective study of Hodgkin lymphoma at head and neck sites: characteristics and outcomes. |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | Cohort | Ear Nose Throat J | Six patients with head and neck malignant paragangliomas, exploring treatment options. |
| [20138008](https://pubmed.ncbi.nlm.nih.gov/20138008/) | 2010 | Review | Transfus Apher Sci | HIV-associated Hodgkin lymphoma, often with head and neck lymphadenopathy. |
| [12113649](https://pubmed.ncbi.nlm.nih.gov/12113649/) | 2002 | Review | Am J Clin Dermatol | Current management concepts in melanoma. |
| [12845209](https://pubmed.ncbi.nlm.nih.gov/12845209/) | 2003 | Case report | Onkologie | Melanoma with mucosal metastases to the oesophagus, stomach, bladder and tonsil. |
| [29443738](https://pubmed.ncbi.nlm.nih.gov/29443738/) | 2018 | Case report | Medicine | Hodgkin lymphoma of the tonsil misdiagnosed as tonsillar carcinoma. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0125 | Dacarbazine | Not recorded | Not recorded (status: valid) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent) |
| Myelosuppression Risk | High. The knowledge graph lists leukopenia, thrombocytopenia and anaemia as contraindication-related conditions. |
| Emetogenicity Classification | High, based on the usual classification of dacarbazine. Please confirm against the package insert. |
| Monitoring Items | CBC with differential, liver function (including signs of hepatic vein thrombosis) and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Disease-related cautions (knowledge graph, not label text)**: The knowledge graph links dacarbazine with contraindication edges to kidney disease, liver disease, gallbladder disease, pyoureter, thrombocytopenia, anaemia (including macrocytic anaemia), leukopenia, hepatic vein thrombosis and Budd-Chiari syndrome.
- **Drug Interactions**: The query returned 100 interactions in total. The only graded ones among those listed are **Naltrexone (Moderate)** and **Levofloxacin (Minor)**. Many other entries have no assigned severity, including pantoprazole, omeprazole, morphine, metformin, prednisone, simvastatin, vancomycin, aprepitant, ondansetron and palonosetron.

Please refer to the package insert for the official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone. There are no clinical trials in this indication, and the literature only indirectly links dacarbazine to head and neck-region tumours.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines website
- Mechanism of action data from DrugBank
- Disease-specific evidence in upper aerodigestive tract neoplasm, such as preclinical or early clinical studies
- Clarification of which disease subtypes (for example squamous carcinoma versus mucosal melanoma) the prediction covers
- Confirmation of the local regulatory pathway, since the existing registration is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

