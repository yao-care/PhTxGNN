---
layout: default
title: Chlorambucil
parent: Model Prediction Only (L5)
nav_order: 71
evidence_level: L5
indication_count: 8
last_modified_at: 2026-10-15
description: "Chlorambucil: predicted new indication Primary pulmonary lymphoma (evidence level L5). Approved use: Hodgkin lymphoma, follicular lymphoma, mature B-cell neoplasms…"
monitor_inn: "Chlorambucil"
predicted_indications: ["pregerminal center chronic lymphocytic leukemia/small lymphocytic lymphoma", "chronic lymphocytic leukemia/small lymphocytic lymphoma with immunoglobulin heavy chain variable-region gene somatic hypermutation", "ALK-positive large B-cell lymphoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "small cell lung carcinoma"]
---

# Chlorambucil
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

## Chlorambucil: From Hodgkin Lymphoma and B-Cell Neoplasms to Primary Pulmonary Lymphoma
{: .text-alpha }

## One-Sentence Summary

Chlorambucil is an alkylating (nitrogen mustard) chemotherapy drug, originally used for Hodgkin lymphoma, follicular lymphoma, other mature B-cell neoplasms, acute lymphoblastic leukaemia and Richter syndrome.
The TxGNN model predicts it may be effective for **primary pulmonary lymphoma** (the highest-ranked prediction with any meaningful literature support).
Currently **no registered clinical trials** and **11 publications** are linked to this prediction, mostly case reports, cohorts and old or indirect studies.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hodgkin lymphoma, follicular lymphoma, mature B-cell neoplasms, acute lymphoblastic leukaemia, Richter syndrome (from the knowledge graph; no approved indication text is available for the Philippines licence) |
| Predicted New Indication | Primary pulmonary lymphoma (the top-ranked prediction, CLL/SLL pre-germinal-centre subtype, is a subtype of an existing indication rather than a true new one) |
| TxGNN Prediction Score | 99.42% (primary pulmonary lymphoma); 99.72% for the top-ranked CLL/SLL subtype |
| Evidence Level | L3 (primary pulmonary lymphoma) |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known information, chlorambucil is a DNA-alkylating nitrogen mustard. Its efficacy in B-cell lymphoproliferative diseases is established, and mechanistically it may be applicable to other B-cell lymphomas.

Primary pulmonary lymphoma is mostly MALT-type marginal zone lymphoma, an indolent B-cell lymphoma. Alkylators such as chlorambucil have a recognised role in such low-grade B-cell lymphomas, which is biologically close to the original indications. A 1987 phase II study of chlorambucil in mixed haematological malignancies reported partial remission in a patient with pseudolymphoma of the lung, and case reports describe patients with pulmonary lymphoma treated with chlorambucil.

Several other high-scoring predictions should be read with caution:
- **CLL/SLL subtypes** (pre-germinal-centre and IGHV-mutated) belong to a disease family where chlorambucil is already used. They are not true repurposing, and the high scores likely reflect proximity to the parent indication.
- **ALK-positive large B-cell lymphoma**, **well-differentiated fetal adenocarcinoma of the lung** and **pulmonary blastoma** have no supporting evidence, and a single low-intensity alkylator is unlikely to be appropriate.
- **Acute lymphoblastic leukaemia** is already among the original indications, and the retrieved literature is indirect.
- **Small cell lung carcinoma** has only old, indirect or preclinical data (see below), and platinum-etoposide regimens have superseded alkylator-based treatment.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Primary pulmonary lymphoma (most relevant items):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3307632](https://pubmed.ncbi.nlm.nih.gov/3307632/) | 1987 | Phase II (mixed haematological malignancies) | Gan to Kagaku Ryoho | Eight patients treated with chlorambucil; partial remission in 2 CLL cases, 1 follicular lymphoma and 1 pulmonary pseudolymphoma. Not specific to pulmonary lymphoma |
| [18603558](https://pubmed.ncbi.nlm.nih.gov/18603558/) | 2008 | Guideline | Haematologica | Italian practice guidelines for primary lung and mediastinal lymphomas |
| [19541720](https://pubmed.ncbi.nlm.nih.gov/19541720/) | 2009 | Cohort | Eur Respir J | Clinical characteristics and prognosis of 63 patients with pulmonary MALT lymphoma |
| [25452791](https://pubmed.ncbi.nlm.nih.gov/25452791/) | 2015 | Case report/Review | Exp Ther Med | Pulmonary MALT lymphoma in a 19-year-old patient, with literature review |
| [36672456](https://pubmed.ncbi.nlm.nih.gov/36672456/) | 2023 | Cohort | Cancers | Long-term ibrutinib vs chlorambucil outcomes (RESONATE-2) in CLL/SLL; indirect evidence |
| [11289295](https://pubmed.ncbi.nlm.nih.gov/11289295/) | 2001 | Case report | Dis Colon Rectum | MALT lymphoma arising in colon and lung; treated with a regimen including chlorambucil |
| [3699123](https://pubmed.ncbi.nlm.nih.gov/3699123/) | 1986 | Case series/Review | Eur J Respir Dis | Primary lung NHL treated with chlorambucil for 5 months |
| [6248988](https://pubmed.ncbi.nlm.nih.gov/6248988/) | 1980 | Case report | Sem Hop | Primary lung lymphosarcoma with clinical remission on continuous chlorambucil over 3 years |

Safety-related items (not efficacy evidence): [9000608](https://pubmed.ncbi.nlm.nih.gov/9000608/) (1997, second malignancies after Hodgkin disease treatment) and [11250989](https://pubmed.ncbi.nlm.nih.gov/11250989/) (2001, lung cancer after Hodgkin disease treatment in relation to therapy).

Small cell lung carcinoma (lower priority, old or preclinical):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [6254684](https://pubmed.ncbi.nlm.nih.gov/6254684/) | 1980 | Phase II (prednimustine) | Cancer Chemother Pharmacol | Prednimustine (a chlorambucil ester) showed no responses in 19 previously treated patients; brief responses in 3 of 9 untreated patients over 70 |
| [688257](https://pubmed.ncbi.nlm.nih.gov/688257/) | 1978 | Randomised comparison | Cancer Treat Rep | Adriamycin plus chlorambucil vs adriamycin plus thiabendazole in non-small cell lung cancer |
| [41025286](https://pubmed.ncbi.nlm.nih.gov/41025286/) | 2026 | Preclinical | Int J Cancer | Chlorambucil-conjugated pyrrole-imidazole polyamide targeting STMN1 in SCLC; a novel construct, not evidence for chlorambucil itself |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0093 | Chlorambucil | Not specified | Not specified (status: cancelled) |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating nitrogen mustard) |
| Myelosuppression Risk | High (the knowledge graph lists neutropenia, thrombocytopenia, leukopenia, anaemia and lymphopenia as contraindication-related conditions) |
| Emetogenicity Classification | Low (oral administration at usual doses); please refer to the package insert |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindication-related conditions (knowledge graph, not label text)**: epilepsy, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, lymphopenia, anaemia, nephrotic syndrome, interstitial lung disease, pulmonary fibrosis, drug-induced liver injury, and acute leukaemias.
- **Drug Interactions** (100 interactions found; main ones shown):
  - Major: deferiprone, samarium (153Sm) lexidronam
  - Moderate: amphotericin B (including lipid, cholesteryl sulfate and liposomal forms), palifermin, strontium chloride Sr-89, mercaptopurine, roflumilast, chloramphenicol
  - Minor: levofloxacin
- **Literature safety signals**: second malignancies (including lung cancer and acute leukaemia) after alkylator-containing treatment for Hodgkin disease; central nervous system toxicity and seizures at high doses.

Please refer to the package insert for the official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only prediction with some supporting data, primary pulmonary lymphoma, rests on case reports, cohorts and one non-specific 1987 phase II study, with no registered trials. The Philippines licence is cancelled and no package insert data is available. The highest-scoring CLL/SLL predictions are subtypes of existing indications, and the others lack supporting evidence.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines
- Mechanism of action data (e.g. from DrugBank)
- Disease-specific clinical evidence for chlorambucil in pulmonary MALT lymphoma, and a comparison against current standard therapy
- Clarification of the regulatory status of the cancelled licence and a plan for product availability
- A safety monitoring plan covering myelosuppression, secondary malignancy risk and drug interactions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

