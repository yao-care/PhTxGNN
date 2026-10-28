---
layout: default
title: Mitoxantrone
parent: Model Prediction Only (L5)
nav_order: 238
evidence_level: L5
indication_count: 7
last_modified_at: 2026-10-28
monitor_inn: "Mitoxantrone"
predicted_indications: ["upper aerodigestive tract neoplasm", "small cell lung carcinoma", "primary pulmonary lymphoma", "well-differentiated fetal adenocarcinoma of the lung", "pulmonary blastoma", "head and neck cancer", "bladder exstrophy-epispadias-cloacal exstrophy complex"]
description: "Mitoxantrone: predicted new indication Upper aerodigestive tract neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Mitoxantrone
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

## Mitoxantrone: Upper aerodigestive tract neoplasm
{: .text-alpha }

## One-Sentence Summary

Mitoxantrone is an anthracenedione chemotherapy agent, originally used for acute myeloid leukemia.
The TxGNN model predicts it may be effective for **head and neck cancer** (the best-supported of eight predictions, selected because it has the strongest clinical evidence rather than the highest score),
with **6 clinical trials** and **20 publications** currently supporting this direction. Most of the direct clinical evidence concerns the liposomal formulation and is still early-phase.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Upper aerodigestive tract neoplasm |
| TxGNN Prediction Score | 0.9978 |
| Evidence Level | L5 (nominal; see note below) |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

*Note on the evidence level:* L1 formally reflects the existence of a Phase III randomized trial. That trial has not started recruiting and has no results. In practice, the direct evidence is closer to early-phase (Phase Ib/II) data, so the L1 label overstates the strength of the evidence.

---

## Why is This Prediction Reasonable?

Mitoxantrone is a topoisomerase II inhibitor and DNA intercalator. It damages the DNA of rapidly dividing tumor cells. Detailed mechanism-of-action data were not available in the data compiled for this report, but this class-level mechanism is well established for the drug and is consistent with the literature reviewed.

Mitoxantrone is already used in a malignancy of blood-forming cells (acute myeloid leukemia). Its cytotoxic action is not limited to one tumor type. Squamous and salivary gland tumors of the head and neck are proliferating solid tumors, so a DNA-damaging agent is mechanistically plausible there.

The clinical record is mixed. Historic Phase II studies of conventional mitoxantrone in head and neck carcinoma and adenoid cystic carcinoma showed limited activity; for example, a Southwest Oncology Group study reported one partial response among 22 evaluable patients. More recent work is stronger and centers on the **liposomal formulation**: a completed Phase Ib study (NCT04902027, n=45) and a 2025 publication on liposomal mitoxantrone in recurrent or metastatic head and neck squamous cell carcinoma. Conventional mitoxantrone is not the agent being developed for this use.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04902027](https://clinicaltrials.gov/study/NCT04902027) | Phase 1 (Ib) | Completed | 45 | Single-arm study of liposomal mitoxantrone in recurrent/metastatic head and neck cancer; safety and efficacy evaluation |
| [NCT05717764](https://clinicaltrials.gov/study/NCT05717764) | Phase 3 | Not yet recruiting | 500 | Randomized trial of liposomal mitoxantrone plus capecitabine vs capecitabine alone in recurrent/metastatic nasopharyngeal carcinoma after platinum failure |
| [NCT06472713](https://clinicaltrials.gov/study/NCT06472713) | Phase 2 | Recruiting | 32 | Single-arm study of liposomal mitoxantrone plus PD-1 blockade in previously treated recurrent/metastatic nasopharyngeal carcinoma |
| [NCT06892431](https://clinicaltrials.gov/study/NCT06892431) | Phase 2 | Not yet recruiting | 150 | JMT101 plus liposomal mitoxantrone in nasopharyngeal cancer after at least two prior lines |
| [NCT07070479](https://clinicaltrials.gov/study/NCT07070479) | Phase 2 | Recruiting | 208 | Bayesian adaptive trial in PD-1-resistant nasopharyngeal carcinoma; one arm is liposomal mitoxantrone plus anti-PD-1 antibody |
| [NCT07354698](https://clinicaltrials.gov/study/NCT07354698) | Phase 4 | Not yet recruiting | 114 | Mitoxantrone used as a lymphatic tracer in transoral robotic thyroid cancer surgery (an imaging use, not antitumor therapy) |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39952083](https://pubmed.ncbi.nlm.nih.gov/39952083/) | 2025 | Clinical study (Phase 1b) | Oral Oncology | Liposomal mitoxantrone (PLM60) tested for safety and efficacy in recurrent/metastatic head and neck squamous cell carcinoma |
| [1650529](https://pubmed.ncbi.nlm.nih.gov/1650529/) | 1991 | Phase II trial | Am J Clin Oncol | 19 patients with incurable head and neck carcinoma; dose adjusted by leukocyte nadir |
| [8922205](https://pubmed.ncbi.nlm.nih.gov/8922205/) | 1996 | Phase II trial | Ann Oncol | EORTC study of mitoxantrone in adenoid cystic carcinoma of the head and neck |
| [6511239](https://pubmed.ncbi.nlm.nih.gov/6511239/) | 1984 | Phase II trial | Invest New Drugs | Mitoxantrone every 3 weeks in advanced head and neck cancer |
| [11290867](https://pubmed.ncbi.nlm.nih.gov/11290867/) | 2001 | Phase II trial | Anti-Cancer Drugs | Ifosfamide plus mitoxantrone in recurrent/metastatic squamous cell carcinoma of the head and neck |
| [12045460](https://pubmed.ncbi.nlm.nih.gov/12045460/) | 2002 | Phase II study | Anti-Cancer Drugs | Mitoxantrone plus cisplatin in salivary gland malignancies (14 patients) |
| [6511243](https://pubmed.ncbi.nlm.nih.gov/6511243/) | 1984 | Phase II trial | Invest New Drugs | Southwest Oncology Group study: one partial response in 22 evaluable patients; leukopenia and thrombocytopenia were the main toxicities; no significant antitumor activity |
| [2345066](https://pubmed.ncbi.nlm.nih.gov/2345066/) | 1990 | Phase II trial | Invest New Drugs | 20 patients with advanced squamous cell carcinoma; one partial remission |
| [34659878](https://pubmed.ncbi.nlm.nih.gov/34659878/) | 2021 | Review | Am J Cancer Res | Systemic therapies for salivary gland adenoid cystic carcinoma |
| [31324333](https://pubmed.ncbi.nlm.nih.gov/31324333/) | 2019 | Systematic review | Bull Cancer | Systemic treatments for metastatic or recurrent adenoid cystic carcinoma of the head and neck |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0328 | Mitoxantrone | Not recorded | Not recorded (status: valid) |

The only registration is cancelled, so no mitoxantrone product is currently marketed in the Philippines.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (anthracenedione, topoisomerase II inhibitor) |
| Myelosuppression Risk | High (leukopenia and thrombocytopenia are the main toxicities reported in the head and neck studies) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential, liver function, cardiac function (cardiotoxicity is a known concern for this class), renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

Please refer to the package insert warnings and precautions for full details.

---

## Safety Considerations

- These need confirmation against the product label.
- **Drug Interactions:** 100 interactions were found. The more notable ones are:
  - **Major:** dolasetron
  - **Moderate:** clarithromycin, eliglustat, rolapitant
  - **Minor:** levofloxacin
  - Many other interactions have an unclassified severity.

Please refer to the package insert for official warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Head and neck cancer has the strongest evidence among the eight predictions: a completed Phase Ib study, a 2025 publication, and an upcoming Phase III trial in nasopharyngeal carcinoma. However, the efficacy evidence is still early-phase, historic Phase II results with conventional mitoxantrone were modest, the recent data apply to the liposomal formulation, and the only Philippine registration is cancelled. Treat this as a research question rather than a ready-to-implement indication.

**To proceed, the following is needed:**
- Results from the Phase III trial NCT05717764 and the Phase II trials in nasopharyngeal carcinoma
- Clarification of whether the liposomal formulation is available or registrable in the Philippines (the cancelled registration covers a conventional product only)
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Detailed mechanism of action data
- A cardiac and hematologic safety monitoring plan, especially for patients with liver disease, heart failure, or low blood counts
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

