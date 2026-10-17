---
layout: default
title: Imiquimod
parent: Model Prediction Only (L5)
nav_order: 174
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Imiquimod: predicted new indication Pre-malignant neoplasm (evidence level L5). Approved use: Common wart, anogenital HPV infection…"
monitor_inn: "Imiquimod"
predicted_indications: ["benign neoplasm of buccal mucosa", "cervical neuroblastoma", "odontogenic cyst", "benign neoplasm of tongue", "nasopharyngeal teratoma", "cystic neoplasm", "inner ear neoplasm", "neoplasm of major salivary gland", "schwannoma of jugular foramen"]
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

# Imiquimod: From Common Wart and Actinic Keratosis to Pre-malignant Neoplasm

## One-Sentence Summary

Imiquimod is a topical immune response modifier, originally used for skin and HPV-related conditions such as common warts, anogenital HPV infection, superficial basal cell carcinoma, and actinic keratosis.
The TxGNN model predicts it may be effective for **pre-malignant neoplasm**,
with **2 clinical trials** and **9 publications** currently supporting this direction. Both trials are small, and the evidence outside actinic keratosis is limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Common wart, anogenital HPV infection, superficial multifocal basal cell carcinoma, actinic keratosis, and other skin conditions (the Philippines registration record contains no indication text) |
| Predicted New Indication | Pre-malignant neoplasm |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L1 per the scoring record, but see the note below |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Proceed with Guardrails |

**Note on evidence level:** The scoring record assigns L1. However, the two Phase 3 trials found are small (n=20 and n=9). One is an uncontrolled open-label study and the other was terminated early. Under strict application of the level definitions (at least 2 completed Phase 3 RCTs), this would be closer to L2–L3. Treat the L1 label with caution.

## Why is This Prediction Reasonable?

Imiquimod is a Toll-like receptor 7 (TLR7) agonist. It stimulates local innate and adaptive immune responses, including interferon-alpha, TNF-alpha, and IL-12. This immune activation helps the body clear abnormal epithelial cells and HPV-infected tissue.

Actinic keratosis is itself a classic pre-malignant skin lesion, and imiquimod is already used for it. Extending to other pre-malignant lesions, such as cervical, vulvar, and anal intraepithelial neoplasia, is therefore a plausible step. These are often HPV-related, as are several of imiquimod's original indications. Evidence outside actinic keratosis is mixed, and the available Phase 3 data are small.

Detailed mechanism-of-action data from DrugBank are currently not available. The description above is based on the known pharmacology of imiquimod.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00175643](https://clinicaltrials.gov/study/NCT00175643) | Phase 3 | Completed | 20 | Open-label study of imiquimod 5% cream, 3 days per week, for actinic keratoses on the head. It aimed to assess the duration of effect. Small and uncontrolled, and it overlaps with the existing indication. |
| [NCT02329171](https://clinicaltrials.gov/study/NCT02329171) | Phase 3 | Terminated | 9 | Randomized trial of topical imiquimod for high-grade cervical intraepithelial neoplasia, as an alternative to surgical excision. Terminated with only 9 participants, so it cannot support an efficacy conclusion. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [23235673](https://pubmed.ncbi.nlm.nih.gov/23235673/) | 2012 | Review (Cochrane) | Cochrane Database Syst Rev | Interventions for anal canal intraepithelial neoplasia, a HPV-associated pre-malignant condition |
| [21491403](https://pubmed.ncbi.nlm.nih.gov/21491403/) | 2011 | Review (Cochrane) | Cochrane Database Syst Rev | Medical interventions for high-grade vulval intraepithelial neoplasia |
| [26516853](https://pubmed.ncbi.nlm.nih.gov/26516853/) | 2015 | Review | Int J Mol Sci | Combined treatments with photodynamic therapy for non-melanoma skin cancer |
| [15584683](https://pubmed.ncbi.nlm.nih.gov/15584683/) | 2004 | Review | Semin Cutan Med Surg | Topical strategies for non-melanoma skin cancer and precursor lesions, including imiquimod |
| [20505896](https://pubmed.ncbi.nlm.nih.gov/20505896/) | 2010 | Review | Skin Therapy Lett | Current management of actinic keratoses, a pre-malignant lesion that can progress to squamous cell carcinoma |
| [30284955](https://pubmed.ncbi.nlm.nih.gov/30284955/) | 2019 | Case report | Int J STD AIDS | Successful imiquimod 5% treatment of high-grade vulval intraepithelial neoplasia in a renal transplant recipient |
| [15601490](https://pubmed.ncbi.nlm.nih.gov/15601490/) | 2004 | Case report | Int J STD AIDS | Clearance of penile bowenoid papulosis with imiquimod 5% cream |
| [29500135](https://pubmed.ncbi.nlm.nih.gov/29500135/) | 2018 | Preclinical | Urol Oncol | Pharmacokinetics of TLR7 agonists in a rat model for bladder cancer |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0245 | Imiquimod | Not specified | Not specified (status: cancelled) |

The only registration is cancelled, so there is currently no valid registered imiquimod product in the Philippines.

## Safety Considerations

- **Disease-level contraindication signals (knowledge graph, not label text):** photoparoxysmal response, photosensitivity disease, autoimmune disease, graft versus host disease, and sunburn.
- **Drug Interactions:** 59 potential interactions were identified in the DDI database, but none has a severity rating. Examples include pantoprazole, omeprazole, prednisone, prednisolone, warfarin, clopidogrel, simvastatin, and hydroxychloroquine. Their clinical significance cannot be judged from the available data.
- **Off-label oral use:** A case report described malignant conversion of florid oral papillomatosis during imiquimod therapy, a concern for use on oral mucosa.

Please refer to the package insert for key warnings and formal contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Imiquimod already has an established role in actinic keratosis and HPV-related skin disease, and the mechanism plausibly extends to other pre-malignant lesions. However, the supporting trials are very small, one was terminated early, and the Philippine registration is cancelled.

**To proceed, the following is needed:**
- Larger, adequately powered randomized trials in specific pre-malignant indications (for example, high-grade cervical, vulvar, or anal intraepithelial neoplasia)
- Narrowing the broad "pre-malignant neoplasm" label to defined diseases and a defined topical route
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Clarification of regulatory status, since the only registration is cancelled
- Detailed mechanism-of-action data
- Review of the photosensitivity and autoimmune/graft-versus-host contraindication signals, and severity grading of the drug interactions

**Other predicted indications:** Benign neoplasm of buccal mucosa and odontogenic cyst have only preclinical, review, and case-report evidence (L4, research questions). The remaining predictions (cervical neuroblastoma, benign tongue neoplasm, nasopharyngeal teratoma, cystic neoplasm, inner ear neoplasm, major salivary gland neoplasm, jugular foramen schwannoma) have no meaningful supporting evidence and should be held.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

