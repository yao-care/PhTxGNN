---
layout: default
title: Etoposide
parent: Model Prediction Only (L5)
nav_order: 135
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Etoposide: predicted new indication well-differentiated fetal adenocarcinoma of the lung (evidence level L5). Approved use: Small cell lung carcinoma, testicular cancer and germ cell tumors"
monitor_inn: "Etoposide"
predicted_indications: ["well-differentiated fetal adenocarcinoma of the lung", "primary pulmonary lymphoma", "pulmonary blastoma", "Ewing sarcoma", "botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "embryonal extrahepatic bile duct rhabdomyosarcoma", "parameningeal embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma"]
---

# Etoposide
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

## Etoposide: From Small Cell Lung Carcinoma and Germ Cell Tumors to Well-Differentiated Fetal Adenocarcinoma of the Lung
{: .text-alpha }

## One-Sentence Summary

Etoposide is a chemotherapy drug originally used for small cell lung carcinoma and testicular germ cell tumours (including seminoma, yolk sac tumour and teratoma).
The TxGNN model's top-ranked predictions are lung-related rare tumours, but the best-supported prediction is **Ewing sarcoma**, with **34 clinical trials** and **20 publications** (including several randomised phase 3 trials), followed by **rhabdomyosarcoma** with **14 clinical trials** and **20 publications**.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Small cell lung carcinoma, testicular cancer and germ cell tumours (the approved indication text for the Philippines registration is blank) |
| Predicted New Indication | Ewing sarcoma (best-supported); the highest-ranked prediction by score is well-differentiated fetal adenocarcinoma of the lung |
| TxGNN Prediction Score | 0.9994 (well-differentiated fetal adenocarcinoma of the lung) |
| Evidence Level | L5 (Ewing sarcoma and rhabdomyosarcoma); L3–L5 for the other candidates |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails (Ewing sarcoma, rhabdomyosarcoma); Hold for the remaining candidates |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Etoposide is generally known as a topoisomerase II inhibitor that causes DNA strand breaks in rapidly dividing cells. Its efficacy in small cell lung carcinoma and germ cell tumours is established, and mechanistically it may be applicable to other fast-growing, chemosensitive tumours.

The data compiled for this report contains ten predictions. They fall into three groups:

- **Ewing sarcoma and rhabdomyosarcoma (strong support):** Etoposide, combined with ifosfamide, is a standard component of multi-agent regimens for these paediatric and young-adult sarcomas. A randomised trial in the *New England Journal of Medicine* (2003) showed that adding ifosfamide and etoposide to standard chemotherapy improved outcomes in Ewing sarcoma. For rhabdomyosarcoma, ifosfamide/etoposide was reported to be superior to vincristine/melphalan in metastatic disease. These are combination regimens, so etoposide's individual contribution cannot be isolated.
- **Pulmonary blastoma (limited support):** Etoposide, usually with platinum agents, appears only in case reports and small series. There are no prospective trials.
- **Other candidates (very weak support):** Well-differentiated fetal adenocarcinoma of the lung, primary pulmonary lymphoma, and rare rhabdomyosarcoma subtypes (vaginal botryoid, parameningeal, prostate, bile duct) rest on indirect literature or the model score alone.

---

## Clinical Trial Evidence

**Ewing sarcoma** (34 trials retrieved; the most relevant are shown)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002516](https://clinicaltrials.gov/study/NCT00002516) | Phase 3 | Unknown | N/A | EICESS 92: randomised comparison of chemotherapy regimens plus surgery/radiotherapy in Ewing sarcoma |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1200 | EURO-E.W.I.N.G.99: chemotherapy with or without radiotherapy, surgery or stem cell support |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | Interval-compressed chemotherapy in Ewing sarcoma and related tumours |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | Adding vincristine-topotecan-cyclophosphamide to standard five-drug chemotherapy (including etoposide) in non-metastatic Ewing sarcoma |
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Dose intensification in non-metastatic Ewing sarcoma |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, not recruiting | 312 | Ganitumab added to multi-agent chemotherapy (including etoposide) in metastatic Ewing sarcoma |
| [NCT00002466](https://clinicaltrials.gov/study/NCT00002466) | Phase 2 | Completed | N/A | Combination chemotherapy including etoposide and ifosfamide, then resection and radiotherapy, in peripheral PNET/Ewing sarcoma |
| [NCT02727387](https://clinicaltrials.gov/study/NCT02727387) | Phase 2 | Completed | 155 | High-dose chemotherapy, radiotherapy and maintenance therapy in metastatic Ewing sarcoma |
| [NCT01864109](https://clinicaltrials.gov/study/NCT01864109) | Phase 2 | Active, not recruiting | 83 | Irinotecan and temozolomide added to high-dose alkylator-based chemotherapy in newly diagnosed Ewing sarcoma |
| [NCT07194044](https://clinicaltrials.gov/study/NCT07194044) | Phase 1 | Recruiting | 15 | Schedule-enhancement approach in widely metastatic Ewing sarcoma |

**Rhabdomyosarcoma** (14 trials retrieved; the most relevant are shown)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003052](https://clinicaltrials.gov/study/NCT00003052) | Phase 3 | Completed | 340 | Etoposide + ifosfamide + doxorubicin with or without regional hyperthermia in high-risk adult soft tissue sarcoma |
| [NCT00025363](https://clinicaltrials.gov/study/NCT00025363) | Phase 2 | Completed | 150 | Irinotecan schedules in relapsed rhabdomyosarcoma; etoposide's role is indirect |
| [NCT00025441](https://clinicaltrials.gov/study/NCT00025441) | Phase 2 | Completed | N/A | MMT 98: combination chemotherapy in metastatic rhabdomyosarcoma |
| [NCT00788125](https://clinicaltrials.gov/study/NCT00788125) | Phase 1/2 | Terminated | 7 | Dasatinib with ifosfamide, carboplatin and etoposide; very small |

Pulmonary blastoma, primary pulmonary lymphoma, and the other predicted indications have no registered clinical trials.

---

## Literature Evidence

**Ewing sarcoma**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | RCT | N Engl J Med | Adding ifosfamide and etoposide to standard chemotherapy in newly diagnosed Ewing sarcoma/PNET of bone |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | RCT (Phase 3) | Lancet | EE2012: comparison of two chemotherapy regimens in newly diagnosed Ewing sarcoma |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | RCT | J Clin Oncol | Interval-compressed chemotherapy (alternating VDC and ifosfamide/etoposide) in localised Ewing sarcoma |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | RCT (Phase 3) | J Clin Oncol | Ganitumab with interval-compressed chemotherapy in metastatic Ewing sarcoma |
| [39713774](https://pubmed.ncbi.nlm.nih.gov/39713774/) | 2024 | Retrospective study | Sarcoma | Oral etoposide in 33 adolescent and adult patients with relapsed or refractory Ewing sarcoma |
| [37403815](https://pubmed.ncbi.nlm.nih.gov/37403815/) | 2023 | Consensus | Cancer | National Ewing Sarcoma Tumor Board recommendations for management |

**Rhabdomyosarcoma**

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11846301](https://pubmed.ncbi.nlm.nih.gov/11846301/) | 2001 | Clinical study | J Pediatr Hematol Oncol | Ifosfamide/etoposide superior to vincristine/melphalan in metastatic rhabdomyosarcoma |
| [26503200](https://pubmed.ncbi.nlm.nih.gov/26503200/) | 2016 | Clinical trial | J Clin Oncol | Dose-compressed ifosfamide/etoposide and VDC cycles in high-risk rhabdomyosarcoma (COG) |
| [9849484](https://pubmed.ncbi.nlm.nih.gov/9849484/) | 1998 | Clinical trial | Eur J Cancer | Alternating VDC and etoposide/ifosfamide in intermediate-risk rhabdomyosarcoma |

**Pulmonary blastoma** (case reports and reviews only)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | Case report/Review | J Int Med Res | Classic biphasic pulmonary blastoma; no standard treatment guidelines |
| [9452262](https://pubmed.ncbi.nlm.nih.gov/9452262/) | 1998 | Case report/Review | Cancer | Seven-year remission and review of chemotherapy experience |
| [11955657](https://pubmed.ncbi.nlm.nih.gov/11955657/) | 2002 | Case report/Review | Lung Cancer | Radiosensitive tumour; cisplatin plus etoposide added afterwards without further regression |

Literature for the other candidates (primary pulmonary lymphoma, vaginal botryoid rhabdomyosarcoma, parameningeal and prostate rhabdomyosarcoma) is indirect or limited to single case reports and reviews. Nothing was retrieved for well-differentiated fetal adenocarcinoma of the lung beyond the pulmonary blastoma report, or for the bile duct rhabdomyosarcoma entities.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0181 | Etoposide | Not specified | Not specified (status: valid) |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (topoisomerase II inhibitor) |
| Myelosuppression Risk | High (the knowledge graph lists thrombocytopenia, neutropenia, leukopenia, agranulocytosis and anaemia as contraindication-related conditions) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Disease-related cautions (from the knowledge graph, not label text):** thrombocytopenia, neutropenia, agranulocytosis, anaemia, macrocytic anaemia, leukopenia, interstitial lung disease, pulmonary fibrosis, impaired renal function, acidosis/metabolic acidosis, and drug-induced liver injury.
- **Drug Interactions:** 100 interactions were found. Moderate-level ones include aprepitant, rolapitant, metronidazole, tinidazole, eliglustat, rosuvastatin and simvastatin. Levofloxacin is rated minor. Many others have an unrated ("Unknown") level, including cimetidine, pantoprazole, amphotericin B, doxycycline and morphine.
- **Package-insert warnings and contraindications:** not available in the data compiled for this report. Please refer to the package insert.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** (Ewing sarcoma and rhabdomyosarcoma); **Hold** for pulmonary blastoma, primary pulmonary lymphoma, well-differentiated fetal adenocarcinoma of the lung, and the rare rhabdomyosarcoma subtypes.

**Rationale:**
- Ewing sarcoma and rhabdomyosarcoma are supported by multiple randomised phase 3 trials and publications in which etoposide is a core component of combination regimens. However, this evidence is for combinations, not etoposide alone, and these are likely already established uses in oncology rather than new discoveries.
- The highest-scoring predictions (lung blastoma-type tumours and pulmonary lymphoma) have only case reports or indirect evidence. The Philippines registration is cancelled, so there is currently no marketed product.

**To proceed, the following is needed:**
- Re-registration or an alternative supply route in the Philippines, since the only licence is cancelled.
- Package insert warnings and contraindications from DOH-FDA Philippines (safety screening cannot move forward without them).
- Mechanism of action data from DrugBank.
- Use only within established risk-stratified combination protocols, with myelosuppression and secondary malignancy monitoring.
- For the Hold candidates, prospective or at least systematic evidence before any further consideration.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

