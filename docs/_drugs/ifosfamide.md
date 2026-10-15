---
layout: default
title: Ifosfamide
parent: Model Prediction Only (L5)
nav_order: 171
evidence_level: L5
indication_count: 10
---

# Ifosfamide
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Ifosfamide: From Unspecified Original Indication to Female Breast Carcinoma

## One-Sentence Summary

Ifosfamide is an alkylating chemotherapy drug. Its original approved indication is not recorded in the Philippine registration data compiled for this report, and its only Philippine registration is cancelled.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **6 clinical trials** (all early-phase or Phase 2, none confirmatory) and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the compiled data (the registration record has no indication text) |
| Predicted New Indication | Female breast carcinoma |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L2 (Phase 2 and single-arm studies only; no Phase 3 RCT in breast cancer) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold (research question only) |

## Why is This Prediction Reasonable?

Ifosfamide is an alkylating prodrug. Liver enzymes (CYP3A4/CYP2B6) convert it to isophosphoramide mustard, which cross-links DNA and triggers apoptosis in rapidly dividing tumour cells. Detailed mechanism-of-action data were not available in the compiled data, so this description comes from the literature rather than a curated drug record.

Breast carcinoma is a proliferating solid tumour, so a cytotoxic alkylator is mechanistically plausible. Published studies report activity in advanced or metastatic breast cancer. Single-agent response rates range from 7% to 30% in pretreated patients. Combinations with vinorelbine, etoposide, docetaxel, paclitaxel and mitoxantrone have been tested, and one cohort reports use in metaplastic breast cancer.

Ifosfamide is not a standard-of-care breast cancer drug. The evidence is mostly Phase 2 and single-arm studies, and TxGNN's high score should be treated as a hypothesis, not proof of benefit.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00026078](https://clinicaltrials.gov/study/NCT00026078) | Phase 2 | Unknown | 42 | Docetaxel + ifosfamide as first-line therapy in metastatic breast cancer; the most directly relevant trial, but results are unconfirmed |
| [NCT00012311](https://clinicaltrials.gov/study/NCT00012311) | Phase 2 | Unknown | Not reported | Multi-cycle high-dose chemotherapy vs optimized conventional chemotherapy in metastatic breast cancer; ifosfamide's individual contribution cannot be isolated |
| [NCT00006032](https://clinicaltrials.gov/study/NCT00006032) | Phase 2 | Terminated | Not reported | Intensive-dose topotecan, ifosfamide/mesna and etoposide with autologous stem cell rescue; multi-drug design |
| [NCT00002854](https://clinicaltrials.gov/study/NCT00002854) | Phase 1 | Completed | 33 | Sequential high-dose cisplatin, cyclophosphamide, etoposide, ifosfamide, carboplatin and paclitaxel with stem cell support; feasibility data only |
| [NCT00003086](https://clinicaltrials.gov/study/NCT00003086) | Phase 1/2 | Terminated | 12 | Samarium-153 within a double autologous transplant in stage IV breast cancer; ifosfamide is incidental |
| [NCT00020722](https://clinicaltrials.gov/study/NCT00020722) | Phase 2 | Terminated | 7 | Activated T cells after stem cell transplant in stage IV breast cancer; ifosfamide at most part of background conditioning |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14586149](https://pubmed.ncbi.nlm.nih.gov/14586149/) | 2003 | Review | Oncology | Ifosfamide in advanced breast cancer: single-agent response rates of 7–30% in pretreated patients; mesna reduces urotoxicity |
| [8918497](https://pubmed.ncbi.nlm.nih.gov/8918497/) | 1996 | Phase 2 trial | J Clin Oncol | Ifosfamide + vinorelbine as first-line chemotherapy for metastatic breast cancer |
| [11932893](https://pubmed.ncbi.nlm.nih.gov/11932893/) | 2002 | Phase 2 trial | Cancer | Paclitaxel (24-hour infusion) + ifosfamide in anthracycline-resistant metastatic breast carcinoma |
| [8445421](https://pubmed.ncbi.nlm.nih.gov/8445421/) | 1993 | Phase 2 trial | J Clin Oncol | Ifosfamide + mitoxantrone as first-line chemotherapy for metastatic breast cancer |
| [39306877](https://pubmed.ncbi.nlm.nih.gov/39306877/) | 2024 | Cohort | Curr Probl Cancer | Experience with ifosfamide-based first-line chemotherapy in rare metaplastic breast cancer |
| [2112056](https://pubmed.ncbi.nlm.nih.gov/2112056/) | 1990 | Clinical study | Cancer Chemother Pharmacol | Ifosfamide/etoposide with mesna in 44 patients with refractory advanced breast cancer |
| [9226029](https://pubmed.ncbi.nlm.nih.gov/9226029/) | 1997 | Clinical study | Tumori | Ifosfamide + etoposide in previously treated advanced breast cancer |
| [2347057](https://pubmed.ncbi.nlm.nih.gov/2347057/) | 1990 | Clinical study | Cancer Chemother Pharmacol | Ifosfamide substituted for cyclophosphamide in CMF in 25 CMF-resistant breast cancer patients |
| [1390313](https://pubmed.ncbi.nlm.nih.gov/1390313/) | 1992 | Review | Ann Oncol | Use of ifosfamide in breast cancer; about 20% objective response as monotherapy |
| [1720382](https://pubmed.ncbi.nlm.nih.gov/1720382/) | 1991 | Review | Drugs | Ifosfamide/mesna: broad antineoplastic activity, pharmacokinetics and efficacy in cancer |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0242 | Ifosfamide | Not recorded | Not recorded (status: cancelled) |

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (oxazaphosphorine alkylating agent) |
| Myelosuppression Risk | High (myelosuppression is expected; leukopenia, anemia and thrombocytopenia are flagged in the knowledge graph) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, renal function, liver function, electrolytes (including potassium), urinalysis for haematuria, neurological status |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication signals (from a knowledge graph, not label text)**: kidney disease, liver disease, gallbladder disease, thrombocytopenia, anemia, leukopenia, hyperbilirubinemia (including Gilbert syndrome), potassium deficiency, renal tubular acidosis, Fanconi renotubular syndrome and pyoureter. These are model-derived associations and need verification against the official label.
- **Known toxicities from the literature**: nephrotoxicity, neurotoxicity (encephalopathy), hemorrhagic cystitis (mesna uroprotection is routine), myelosuppression, and risk of therapy-related myeloid neoplasms.
- **Drug Interactions**: 100 interactions were found. Those listed are mostly moderate: amphotericin B (including lipid complex), aminoglycosides (kanamycin, neomycin), aprepitant, bupropion, morphine, metoclopramide, dronabinol, nabilone, scopolamine, and sulfonylureas/glinides (chlorpropamide, glimepiride, glipizide, glyburide, tolazamide, acetohexamide, nateglinide, repaglinide). Levofloxacin is minor.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Breast cancer evidence for ifosfamide consists of small Phase 2 and single-arm studies from mostly earlier decades, with no Phase 3 RCT. It is not a standard breast cancer agent, and the only Philippine registration is cancelled. The prediction is a reasonable research question but does not currently justify advancing.

**To proceed, the following is needed:**
- Philippine package insert warnings and contraindications (not available in the data compiled for this report)
- Original indication and dosage form for the cancelled registration, and a current valid registration or import pathway
- Detailed mechanism-of-action data from DrugBank
- Comparative evidence against current standard breast cancer regimens, ideally from randomized trials
- A safety monitoring plan covering renal, neurological, urothelial and haematological toxicity, with mesna support
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

