---
layout: default
title: Fluorouracil
parent: Model Prediction Only (L5)
nav_order: 149
evidence_level: L5
indication_count: 10
monitor_inn: "Fluorouracil"
predicted_indications: ["botryoid-type embryonal rhabdomyosarcoma of the vagina", "rhabdomyosarcoma (disease)", "parameningeal embryonal rhabdomyosarcoma", "embryonal extrahepatic bile duct rhabdomyosarcoma", "prostate embryonal rhabdomyosarcoma", "extrahepatic bile duct rhabdomyosarcoma", "liver sarcoma", "hereditary persistence of fetal hemoglobin-sickle cell disease syndrome", "sickle cell-hemoglobin d disease syndrome", "sickle cell-beta-thalassemia disease syndrome"]
last_modified_at: 2026-10-30
description: "Fluorouracil: predicted new indication Botryoid-type embryonal rhabdomyosarcoma of the vagina (evidence level L5). Approved use: Relations recorded in the knowledge graph (not label-approved): super…"
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

## Fluorouracil: From Gastric and Colorectal Cancer to Botryoid-Type Embryonal Rhabdomyosarcoma of the Vagina
{: .text-alpha }

## One-Sentence Summary

Fluorouracil is a cytotoxic antimetabolite.
The TxGNN model predicts it may be effective for **rhabdomyosarcoma** and related subtypes. No clinical trials have been found, and only **4 publications** (all indirect: older reviews, a cohort of nasopharyngeal carcinoma and one case report) were retrieved for the broader rhabdomyosarcoma entry, so the evidence is very limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Relations recorded in the knowledge graph (not label-approved): superficial basal cell carcinoma, actinic keratosis, colon cancer metastasis, pancreatic adenocarcinoma, gastric cancer. No approved indication text is available in the local licence record. |
| Predicted New Indication | Botryoid-type embryonal rhabdomyosarcoma of the vagina (top-ranked prediction); the broader "rhabdomyosarcoma" entry is also discussed below |
| TxGNN Prediction Score | 0.9975 |
| Evidence Level | L5 (no cited study directly addresses the top-ranked disease; no clinical trials) |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on general pharmacology, fluorouracil is a pyrimidine antimetabolite that inhibits thymidylate synthase and interferes with DNA and RNA synthesis in rapidly dividing cells. That mechanism could plausibly apply to a fast-growing sarcoma.

The very high scores for rhabdomyosarcoma subtypes come from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Standard rhabdomyosarcoma regimens (for example vincristine, dactinomycin, cyclophosphamide) do not centre on fluorouracil, so any role would be unproven.

The same pattern appears in other predictions: several sickle cell syndromes (rank 8–10) share an identical score of 0.9962, which may reflect similarities the model learned between related diseases rather than disease-specific evidence. A fetal-hemoglobin induction rationale is speculative, and fluorouracil's toxicity makes it unattractive for a chronic non-malignant condition.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature was found for the top-ranked disease (botryoid-type embryonal rhabdomyosarcoma of the vagina). The table below shows the publications retrieved for the broader "rhabdomyosarcoma" prediction (rank 2). None is a controlled study of fluorouracil in this disease.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3884137](https://pubmed.ncbi.nlm.nih.gov/3884137/) | 1985 | Review | Cancer | Value of adjuvant chemotherapy for childhood sarcomas, about half of which are rhabdomyosarcomas; general overview |
| [6277228](https://pubmed.ncbi.nlm.nih.gov/6277228/) | 1981 | Review | Ann Acad Med Singapore | Chemotherapy can cure several cancers, including childhood rhabdomyosarcoma; not specific to fluorouracil |
| [3951398](https://pubmed.ncbi.nlm.nih.gov/3951398/) | 1986 | Cohort | Med Pediatr Oncol | Childhood nasopharyngeal carcinoma outcomes; a different disease |
| [42483493](https://pubmed.ncbi.nlm.nih.gov/42483493/) | 2026 | Case report | Case Rep Oncol Med | Young adult with lingual rhabdomyosarcoma; cisplatin plus 5-fluorouracil was followed by disease progression, and a later vincristine/actinomycin D-based regimen was used |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0198 | Fluorouracil | Not specified | Not specified in the licence record |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (fluoropyrimidine antimetabolite) |
| Myelosuppression Risk | Medium to high; the knowledge graph lists thrombocytopenia, neutropenia, leukopenia and agranulocytosis as contraindication-related conditions |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver and renal function, electrolytes; mucosal and gastrointestinal toxicity |
| Handling Protection | Follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication-related conditions (from the knowledge graph, not label text)**: kidney disease, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, leukopenia, diarrhoeal disease, active peptic ulcer disease, pharyngitis, stomatitis, pyoureter and dihydropyrimidine dehydrogenase (DPD) deficiency.
- **Drug Interactions**: 100 interactions were found in total. Moderate-level interactions include metronidazole and tinidazole. Minor-level interactions include cimetidine and levofloxacin. Many others (for example omeprazole, pantoprazole, metformin, morphine) have an unclassified severity level.

Please also refer to the package insert, as no label warnings were available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The predictions rest on model scores alone. The top-ranked disease has no trials or literature, and the literature for broader rhabdomyosarcoma is indirect and does not show a fluorouracil-specific benefit. Fluorouracil is also not part of standard rhabdomyosarcoma therapy and carries significant toxicity.

**To proceed, the following is needed:**
- Package insert warnings, contraindications and approved indications for the Philippine licence (PNF-0198)
- Mechanism of action data
- Disease-specific preclinical or clinical data on fluorouracil in rhabdomyosarcoma subtypes
- A comparison against standard rhabdomyosarcoma regimens
- DPD deficiency screening and a haematological safety monitoring plan if any further study is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

