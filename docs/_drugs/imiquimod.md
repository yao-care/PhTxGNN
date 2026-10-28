---
layout: default
title: Imiquimod
parent: Model Prediction Only (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
monitor_inn: "Imiquimod"
predicted_indications: ["pre-malignant neoplasm", "benign neoplasm of buccal mucosa", "cervical neuroblastoma", "odontogenic cyst", "benign neoplasm of tongue", "nasopharyngeal teratoma", "cystic neoplasm", "inner ear neoplasm", "neoplasm of major salivary gland", "schwannoma of jugular foramen"]
last_modified_at: 2026-10-28
description: "Imiquimod: predicted new indication pre-malignant neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Imiquimod
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

## Imiquimod: TLR7 agonist (topical immune response modifier) → pre-malignant neoplasm
{: .text-alpha }

## One-Sentence Summary

Imiquimod is a topical immune response modifier that activates the TLR7 pathway.
The TxGNN model predicts it may be effective for **pre-malignant neoplasm**,
with **2 clinical trials** and **9 publications** currently linked to this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | pre-malignant neoplasm |
| TxGNN Prediction Score | 0.9992 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Imiquimod is a Toll-like receptor 7 (TLR7) agonist. It triggers local innate and adaptive immune responses, including release of interferon-alpha, TNF-alpha and IL-12. This immune activation can help clear abnormal epithelial cells. Detailed mechanism-of-action data is not otherwise available in the data compiled for this report.

Pre-malignant lesions such as intraepithelial neoplasias and actinic keratosis are abnormal epithelial growths, many of them HPV-related, that respond to local immune stimulation. The mechanism is therefore plausible for this group of conditions. Evidence beyond actinic keratosis, however, is mixed, and the available Phase 3 data are small.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label study of imiquimod 5% cream, 3 days per week, for actinic keratoses on the head; small and uncontrolled |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | Randomized trial of topical imiquimod in high-grade cervical intraepithelial neoplasia; terminated early with 9 participants, so underpowered |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Review (Cochrane) | Cochrane Database Syst Rev | Interventions for anal canal intraepithelial neoplasia, a pre-malignant HPV-associated condition |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Review (Cochrane) | Cochrane Database Syst Rev | Medical interventions for high-grade vulval intraepithelial neoplasia |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Combined treatments with photodynamic therapy for non-melanoma skin cancer |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Letter | Current management of actinic keratoses, a pre-malignant skin lesion |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topical strategies for non-melanoma skin cancer and precursor lesions, including imiquimod |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case report | Int J STD AIDS | High-grade vulval intra-epithelial neoplasia successfully treated with imiquimod 5% in a renal transplant recipient |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case report | Int J STD AIDS | Bowenoid papulosis of the penis cleared with topical imiquimod 5% |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical | Urol Oncol | TLR7 agonists (TMX-101, TMX-202) in a rat model; TLR7 agonists are used topically for pre-malignant skin lesions |
| [18931984](https://pubmed.ncbi.nlm.nih.gov/18931984/) | 2008 | Other | Hautarzt | Case of actinic porokeratosis imaged by OCT; lesions were resistant to topical treatment |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0245 | Imiquimod | Not recorded | Not recorded |

---

## Safety Considerations

- **Drug Interactions**: 59 potential interactions were identified in the interaction database, but none has a severity level assigned. Examples include pantoprazole, morphine, omeprazole, prednisone, simvastatin, warfarin, clopidogrel, hydroxychloroquine and ibuprofen.
- **Safety signals in the literature**: One case report described malignant conversion of florid oral papillomatosis during imiquimod therapy (relevant to off-label oral use). Another described erythema multiforme in a patient with Gorlin syndrome.

Please refer to the package insert for further safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The two Phase 3 trials that directly address premalignant lesions are small (20 and 9 participants), and one was terminated early. They study actinic keratosis and cervical intraepithelial neoplasia, which are specific premalignant conditions, not "pre-malignant neoplasm" as a whole. No study is therefore sufficient to confirm efficacy across the predicted indication, and the evidence level is set at L2 on the basis of the completed Phase 3 trial. Further evidence is needed before any wider use.

**To proceed, the following is needed:**
- Adequately powered randomized trials in specific premalignant conditions other than actinic keratosis (e.g. cervical, vulvar, anal intraepithelial neoplasia)
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Detailed mechanism-of-action data
- Clarification of dosage form and approved indication for the local licence
- Safety monitoring plan, including attention to photosensitivity and autoimmune conditions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

