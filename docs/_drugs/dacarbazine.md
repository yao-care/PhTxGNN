---
layout: default
title: Dacarbazine
parent: 僅模型預測 (L5)
nav_order: 91
evidence_level: L5
indication_count: 1
---

# Dacarbazine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

# Dacarbazine: From Melanoma to Upper Aerodigestive Tract Neoplasm

## One-Sentence Summary

Dacarbazine (DTIC) is a triazene alkylating agent classically used in the treatment of melanoma, Hodgkin lymphoma, and soft tissue sarcomas. The TxGNN model predicts it may be effective for **upper aerodigestive tract neoplasm** (score: 99.26%), with **1 analog clinical trial** and **20 publications** currently identified to support this direction. However, direct clinical evidence for Dacarbazine itself in this indication is essentially absent, and the available trial studied a structurally related analog (Temozolomide) that was terminated early due to limited efficacy.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Melanoma, Hodgkin lymphoma, soft tissue sarcoma |
| Predicted New Indication | Upper Aerodigestive Tract Neoplasm |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, formal mechanism of action data from DrugBank is not available. Based on known pharmacology, Dacarbazine is a triazene alkylating agent that requires hepatic bioactivation via CYP1A1/CYP1A2 enzymes to generate its active metabolite, MTIC (5-(3-methyltriazen-1-yl)imidazole-4-carboxamide). MTIC methylates DNA at the O6-guanine position, causing mismatch repair (MMR) failure and triggering cancer cell apoptosis. This mechanism is identical to that of Temozolomide — both drugs converge on the same active intermediate — making existing Temozolomide clinical data structurally relevant as indirect (analog) evidence for Dacarbazine.

Upper aerodigestive tract tumors, including head and neck squamous cell carcinomas (HNSCC), neuroendocrine tumors (medullary thyroid carcinoma, paraganglioma, esthesioneuroblastoma), and rare vascular malignancies (angiosarcoma), represent a biologically heterogeneous group that is theoretically susceptible to DNA alkylation due to rapid proliferation. Notably, small case series have documented direct use of Dacarbazine-containing regimens (CYVADIC, Dacarbazine + 5-FU) in head and neck angiosarcoma and medullary thyroid carcinoma, providing limited but direct precedent.

The critical mechanistic limitation, however, lies in MGMT (O6-methylguanine-DNA methyltransferase) expression. Most HNSCC tumors demonstrate robust MGMT activity, which efficiently repairs O6-guanine alkylation damage and confers resistance to this drug class. The Phase 2 trial of Temozolomide (NCT00423150) — which enrolled only patients with confirmed MGMT promoter methylation — was terminated early, and its published results confirmed limited efficacy in this enriched population. This outcome strongly suggests that unselected HNSCC patients would respond poorly, and that MGMT biomarker screening would be essential to identify any potentially responsive subgroup.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00423150](https://clinicaltrials.gov/study/NCT00423150) | Phase 2 | Terminated | 86 | Evaluated **Temozolomide** (structural analog of Dacarbazine, shared MTIC metabolite) in MGMT promoter-methylated patients with advanced aerodigestive tract cancers (head & neck, esophageal, NSCLC) and colorectal cancer. Published results (PMID 23443801, 2013) confirmed limited efficacy — the likely reason for early termination. This constitutes **analog indirect evidence** for Dacarbazine; results cannot be directly extrapolated. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [23443801](https://pubmed.ncbi.nlm.nih.gov/23443801/) | 2013 | Phase 2 Study | *Mol Cancer Ther* | Temozolomide in MGMT-methylated aerodigestive tract and colorectal cancers; limited response rates confirm MGMT methylation as necessary but insufficient predictor — key analog evidence for Dacarbazine |
| [7826911](https://pubmed.ncbi.nlm.nih.gov/7826911/) | 1994 | Clinical Study | *Ann Oncol* | **Direct Dacarbazine evidence**: Dacarbazine + 5-FU combination in advanced medullary thyroid carcinoma (neuroendocrine tumor of the upper aerodigestive region); modest activity reported |
| [8346929](https://pubmed.ncbi.nlm.nih.gov/8346929/) | 1993 | Case Series | *Gan To Kagaku Ryoho* | CYVADIC regimen (including DTIC/Dacarbazine) used in head and neck angiosarcoma; documents direct Dacarbazine use in a rare upper aerodigestive malignancy |
| [20564093](https://pubmed.ncbi.nlm.nih.gov/20564093/) | 2010 | Retrospective Cohort | *Cancer* | Hodgkin lymphoma involving extranodal and nodal head and neck sites; ABVD (containing Dacarbazine) is the standard regimen — supports Dacarbazine activity in head/neck lymphomatous disease |
| [20138008](https://pubmed.ncbi.nlm.nih.gov/20138008/) | 2010 | Review | *Transfus Apher Sci* | Hodgkin lymphoma in HIV-infected patients; head and neck involvement predominant; ABVD (Dacarbazine-containing) discussed as treatment backbone |
| [34654328](https://pubmed.ncbi.nlm.nih.gov/34654328/) | 2024 | Case Series | *Ear Nose Throat J* | Six malignant head and neck paragangliomas reviewed for clinicopathological features, gene mutations, and treatment outcomes; highlights chemotherapy context for rare neuroendocrine upper aerodigestive tumors |
| [11163509](https://pubmed.ncbi.nlm.nih.gov/11163509/) | 2001 | Retrospective Case Series | *Int J Radiat Oncol* | Radiotherapy outcomes in esthesioneuroblastoma (rare malignant intranasal tumor); establishes multimodal management context for rare upper aerodigestive tract malignancies |
| [20627492](https://pubmed.ncbi.nlm.nih.gov/20627492/) | 2010 | Review | *Clin Oncol* | Comprehensive review of medullary thyroid carcinoma, including Dacarbazine-based chemotherapy regimens for advanced/refractory disease |
| [39570323](https://pubmed.ncbi.nlm.nih.gov/39570323/) | 2025 | In vitro / Preclinical | *Endocrine* | Doxorubizen (structural hybrid of doxorubicin and temozolomide) tested in anaplastic thyroid cancer cell lines; demonstrates ongoing interest in MTIC-based DNA alkylation for aggressive thyroid malignancies |
| [12113649](https://pubmed.ncbi.nlm.nih.gov/12113649/) | 2002 | Review | *Am J Clin Dermatol* | Melanoma management review; contextualizes Dacarbazine as the established single-agent alkylating standard — mechanistic reference for extrapolation to other epithelial tumors |

---

## Philippines Market Information

Dacarbazine is currently **not registered or marketed in the Philippines**. No product licenses have been identified in the regulatory database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No registered products found |

For clinical access, international importation or hospital-based compassionate use/special access programs would be required prior to any investigational or standard-of-care use.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Triazene alkylating agent (shares MTIC metabolite with Temozolomide) |
| Myelosuppression Risk | High — leukopenia and thrombocytopenia are dose-limiting toxicities; nadir typically occurs at 3–4 weeks post-administration |
| Emetogenicity Classification | High — Dacarbazine is classified as a highly emetogenic agent; prophylactic antiemetic regimen (5-HT₃ antagonist + NK1 receptor antagonist + dexamethasone) is mandatory |
| Monitoring Items | CBC with differential (baseline and at nadir), liver function tests (ALT, AST, bilirubin — hepatotoxicity risk), renal function (creatinine, BUN), infusion site assessment (vesicant/irritant potential) |
| Handling Protection | Classified as a hazardous drug — must comply with cytotoxic handling regulations: closed-system drug transfer devices (CSTD), biological safety cabinet preparation, PPE (double gloves, gown, eye protection), and dedicated waste disposal |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gap Notice**: Formal TFDA/FDA Philippines package insert warnings, contraindications, and drug interaction data were not retrieved in this evidence pack. Acquisition of the official prescribing information is classified as a **Blocking** data gap (DG001) that must be resolved before any safety assessment can be completed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score (99.26%) and mechanistic plausibility exists through shared MTIC-mediated DNA alkylation, the only identified clinical trial studied an analog drug (Temozolomide) that was terminated early due to limited efficacy. The high MGMT expression characteristic of most upper aerodigestive tract tumors represents a fundamental pharmacological barrier, and direct clinical evidence for Dacarbazine itself in this indication is absent.

**To proceed, the following is needed:**

- **Resolve Blocking data gap (DG001)**: Retrieve the official Dacarbazine prescribing information (TFDA, EMA, or FDA) to extract confirmed warnings, contraindications, and drug interactions — required before any S1 safety evaluation
- **Resolve High data gap (DG002)**: Query DrugBank (DB00851) for full MOA, molecular targets, pharmacokinetics, and enzyme interaction data
- **Identify direct Dacarbazine evidence**: Conduct a targeted literature search for clinical studies specifically using Dacarbazine (not Temozolomide) in head, neck, or upper aerodigestive tract tumors beyond the two small case series identified here
- **MGMT landscape analysis**: Review MGMT promoter methylation frequency in upper aerodigestive tract neoplasm subtypes to identify which histologies may harbor a dacarbazine-sensitive subpopulation
- **Regulatory feasibility assessment**: Clarify the registration and special access pathway for Dacarbazine in the Philippines given its current non-marketed status
- **Subtype specificity**: Distinguish between HNSCC (likely resistant) and neuroendocrine subtypes (medullary thyroid carcinoma, paraganglioma, esthesioneuroblastoma) where Dacarbazine-containing regimens have existing precedent and may warrant a separate, more favorable evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

