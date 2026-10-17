---
layout: default
title: Fluorouracil
parent: Model Prediction Only (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Fluorouracil: predicted new indication Rhabdomyosarcoma (evidence level L5). Approved use: Superficial multifocal basal cell carcinoma, actinic keratosis…"
monitor_inn: "Fluorouracil"
predicted_indications: ["botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "liver sarcoma", "sickle cell-hemoglobin c disease syndrome", "sickle cell-hemoglobin E disease syndrome", "sickle cell-hemoglobin d disease syndrome"]
---

# Fluorouracil
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

# Fluorouracil: From Skin Conditions and Gastrointestinal Cancers to Rhabdomyosarcoma

## One-Sentence Summary

Fluorouracil is an antimetabolite chemotherapy drug, originally used for skin conditions such as superficial basal cell carcinoma and actinic keratosis, and for gastrointestinal cancers such as gastric, pancreatic and colon cancer.
The TxGNN model predicts it may be effective for **rhabdomyosarcoma**, with **0 clinical trials** and **4 publications** (mostly old, indirect or single case reports) currently supporting this direction.
This is a model prediction with very weak direct evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Superficial multifocal basal cell carcinoma, actinic keratosis, gastric cancer, pancreatic adenocarcinoma, colon cancer metastasis (from the knowledge graph; no approved-indication text is available for the Philippine registration) |
| Predicted New Indication | Rhabdomyosarcoma (the top-ranked prediction is botryoid-type embryonal rhabdomyosarcoma of the vagina) |
| TxGNN Prediction Score | 99.75% (top-ranked prediction); 99.74% for rhabdomyosarcoma (disease) |
| Evidence Level | L5 for the top-ranked prediction; L4 for rhabdomyosarcoma (disease) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general knowledge, fluorouracil is a thymidylate synthase inhibitor and antimetabolite. It disrupts DNA synthesis in rapidly dividing cells, and its efficacy in gastrointestinal and skin cancers is well established. Mechanistically, it could plausibly act on a highly proliferative sarcoma.

The prediction is likely driven by the structure of the knowledge graph, where fluorouracil sits close to many tumour types. However, standard rhabdomyosarcoma regimens (such as vincristine, actinomycin D and cyclophosphamide) do not rely on fluorouracil. No study isolates a fluorouracil contribution in this disease. For the biliary rhabdomyosarcoma prediction, the link may partly reflect fluorouracil use in biliary tract carcinoma, which is a different disease.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Four publications were retrieved for rhabdomyosarcoma (disease). None provides direct evidence for fluorouracil, and full-text review is needed.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Review / clinical series | Cancer | Adjuvant chemotherapy in childhood sarcomas, including rhabdomyosarcoma; role of fluorouracil not isolated |
| [42483493](https://pubmed.ncbi.nlm.nih.gov/42483493/) | 2026 | Case report | Case Reports in Oncological Medicine | Young adult with lingual rhabdomyosarcoma; disease progressed on cisplatin plus 5-fluorouracil, and a later vincristine/actinomycin D-based regimen followed |
| [6277228](https://pubmed.ncbi.nlm.nih.gov/6277228/) | 1981 | Review | Annals of the Academy of Medicine, Singapore | General review of curable cancers with chemotherapy, mentioning rhabdomyosarcoma among childhood cancers |
| [3951398](https://pubmed.ncbi.nlm.nih.gov/3951398/) | 1986 | Retrospective case series | Medical and Pediatric Oncology | Pediatric nasopharyngeal carcinoma; low relevance to rhabdomyosarcoma |

The single case report suggests fluorouracil-containing therapy did not control the disease in that patient.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0198 | Fluorouracil | Not specified | Not specified (status: cancelled) |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Medium to high; the knowledge graph lists neutropenia, leukopenia, thrombocytopenia and agranulocytosis as contraindication-related conditions |
| Emetogenicity Classification | Low to medium |
| Monitoring Items | Complete blood count with differential, liver and renal function, electrolytes, and mucositis and diarrhoea assessment |
| Handling Protection | Must follow cytotoxic drug handling regulations |

---

## Safety Considerations

- **Contraindications / cautions (from the knowledge graph, not label text)**: kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, diarrhoeal disease, active peptic ulcer disease, pharyngitis, stomatitis, and dihydropyrimidine dehydrogenase (DPD) deficiency.
- **Drug Interactions**: 100 interactions were found. The main ones with a stated severity are **Moderate** with metronidazole and tinidazole, and **Minor** with cimetidine and levofloxacin. Many others have unknown severity (for example omeprazole, pantoprazole, metformin and morphine).
- For package insert warnings, please refer to the product label, as label-based warnings and contraindications were not available.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by model scores, with no registered clinical trials and no direct literature for fluorouracil in rhabdomyosarcoma. Standard treatment uses other agents, fluorouracil is cytotoxic and myelosuppressive, and the only Philippine registration is cancelled.

**To proceed, the following is needed:**
- Full-text review of the retrieved literature to clarify the role of fluorouracil
- Preclinical or retrospective data on fluorouracil activity in rhabdomyosarcoma, compared against standard regimens
- Detailed mechanism of action data
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Clarification of the cancelled registration status and available dosage forms and routes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

