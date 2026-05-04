---
layout: default
title: Docetaxel
parent: 僅模型預測 (L5)
nav_order: 112
evidence_level: L5
indication_count: 10
---

# Docetaxel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Docetaxel: From Solid Tumor Chemotherapy to Female Breast Carcinoma

## One-Sentence Summary

Docetaxel (Taxotere) is a taxane-class antineoplastic agent with global regulatory approvals for multiple solid tumors, including breast cancer, non-small cell lung cancer, and prostate cancer, but is currently not registered in the Philippines.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma** as the top-ranked indication,
with **multiple completed Phase 3 clinical trials** and **20 publications** fully supporting this direction — a finding consistent with its internationally established standard-of-care role in breast oncology.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | None on record in the Philippines; globally approved for breast cancer, NSCLC, prostate cancer, gastric cancer, and head & neck cancer |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 (≥5 completed Phase 3 RCTs identified) |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Docetaxel is a semisynthetic taxane derived from the European yew tree (*Taxus baccata*). Its mechanism of action centers on **stabilizing polymerized microtubules** by binding to the β-tubulin subunit and preventing their disassembly. This results in mitotic arrest at the G2/M phase of the cell cycle, disruption of the mitotic spindle apparatus, and ultimately apoptotic cell death. Compared to paclitaxel — the first taxane to reach clinical use — docetaxel has approximately two-fold higher binding affinity for tubulin and superior intracellular accumulation, which contributes to its greater potency in several tumor models.

Breast cancer, particularly HER2-positive and triple-negative subtypes (TNBC), is characterized by high cellular proliferation rates. Rapidly dividing cancer cells are especially vulnerable to agents that disrupt mitotic machinery, which explains why docetaxel demonstrates activity across all major breast cancer subtypes and treatment settings: as first-line therapy in metastatic disease (alone or in combination with trastuzumab, bevacizumab, or carboplatin), as neoadjuvant therapy to downstage locally advanced tumors prior to surgery, and as adjuvant therapy to reduce recurrence risk in node-positive and high-risk early breast cancer.

The TxGNN model's top prediction of female breast carcinoma for docetaxel — with a score of 99.90% — is mechanistically and clinically well-grounded. The drug already holds regulatory approvals for breast cancer from the FDA (USA), EMA (Europe), and PMDA (Japan). In the Philippines context, where docetaxel is not currently registered, this prediction highlights an actionable market access gap rather than a novel repurposing hypothesis: the evidence is mature and extensive, and the primary challenge is local regulatory registration.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00333775](https://clinicaltrials.gov/study/NCT00333775) | Phase 3 | Completed | 736 | Bevacizumab (2 dose levels) + docetaxel vs. docetaxel + placebo as 1st-line treatment in HER2-negative metastatic/locally recurrent breast cancer; pivotal efficacy and safety study |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | Adjuvant TC×6 or AC→T/P ± trastuzumab in node-positive or high-risk, HER2-low early breast cancer; largest adjuvant taxane trial in this population |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | Completed | 263 | Docetaxel + trastuzumab (TH) vs. docetaxel + carboplatin + trastuzumab (TCH) as 1st-line in HER2-amplified advanced breast cancer; established TCH as a standard-of-care regimen |
| [NCT00129935](https://clinicaltrials.gov/study/NCT00129935) | Phase 3 | Completed | 1,384 | EC→docetaxel vs. ET→capecitabine as adjuvant therapy in HER2-negative, node-positive breast cancer; directly compared two docetaxel-containing strategies |
| [NCT00004125](https://clinicaltrials.gov/study/NCT00004125) | Phase 3 | Completed | N/A | AC followed by weekly paclitaxel or weekly docetaxel in axillary node-positive (stage II/IIIA) breast cancer; compared scheduling strategies |
| [NCT01564056](https://clinicaltrials.gov/study/NCT01564056) | Phase 3 | Active, Not Recruiting | 1,989 | Adjuvant chemotherapy + endocrine therapy vs. endocrine therapy alone in elderly (>70 years) ER+/HER2- breast cancer stratified by Genomic Grade; evaluating survival benefit of adding chemotherapy |
| [NCT00532727](https://clinicaltrials.gov/study/NCT00532727) | Phase 3 | Unknown | 400 | Triple Negative Trial: carboplatin vs. docetaxel monotherapy in ER-/PR-/HER2- metastatic or recurrent locally advanced breast cancer; direct head-to-head comparison in TNBC |
| [NCT01503905](https://clinicaltrials.gov/study/NCT01503905) | N/A | Unknown | 600 | Docetaxel + epirubicin (DE) vs. docetaxel + epirubicin + cyclophosphamide (DEC) as neoadjuvant in operable premenopausal breast cancer; multicentre randomized design |
| [NCT00464646](https://clinicaltrials.gov/study/NCT00464646) | Phase 2 | Completed | 105 | EC→docetaxel + trastuzumab + bevacizumab as neoadjuvant/adjuvant in HER2+ locally advanced breast cancer; evaluated cardiac function impact of adding bevacizumab |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Phase 2 | Recruiting | 85 | EC→docetaxel + carboplatin in Nigerian women with TNBC; assesses pathological complete response (pCR) and identifies blood biomarkers of chemotherapy resistance |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28398846](https://pubmed.ncbi.nlm.nih.gov/28398846/) | 2017 | RCT | J Clin Oncol | ABC Trials (3 studies): TC×6 was not superior to standard TaxAC (TAC6, AC→T, or AC→P) in early breast cancer adjuvant setting; established TC as a reasonable non-anthracycline alternative |
| [7595719](https://pubmed.ncbi.nlm.nih.gov/7595719/) | 1995 | Review | J Clin Oncol | Comprehensive review of docetaxel's preclinical pharmacology and early clinical activity in solid tumors including breast cancer; foundational reference for the drug's development |
| [12868800](https://pubmed.ncbi.nlm.nih.gov/12868800/) | 2003 | Review | Breast Cancer Res Treat | Docetaxel-anthracycline combination regimens in metastatic breast cancer; synthesized Phase II/III evidence for doxorubicin and epirubicin combinations |
| [26874836](https://pubmed.ncbi.nlm.nih.gov/26874836/) | 2017 | Cohort | Breast Cancer (Tokyo) | HER-TC (docetaxel + cyclophosphamide + trastuzumab) as neoadjuvant in HER2+ breast cancer; evaluated pCR rates stratified by hormone receptor status |
| [19755993](https://pubmed.ncbi.nlm.nih.gov/19755993/) | 2009 | Correlative | Br J Cancer | Microarray gene expression profiling to identify predictors of pathological complete response (pCR) to trastuzumab-docetaxel treatment in HER2+ breast carcinoma |
| [15316749](https://pubmed.ncbi.nlm.nih.gov/15316749/) | 2004 | Phase 2 | Cancer Chemother Pharmacol | Docetaxel + high-dose epirubicin as neoadjuvant in locally advanced breast cancer; pCR rate as primary endpoint in a clinically meaningful population |
| [15585076](https://pubmed.ncbi.nlm.nih.gov/15585076/) | 2004 | Phase 2 | Clin Breast Cancer | Docetaxel + cisplatin (both 70 mg/m²) as neoadjuvant in breast tumors ≥5 cm; evaluated pCR before radical mastectomy |
| [12599222](https://pubmed.ncbi.nlm.nih.gov/12599222/) | 2003 | Phase 2 | Cancer | Capecitabine + docetaxel + epirubicin (TEX) as first-line therapy in locally advanced/metastatic breast carcinoma; assessed anti-tumor activity and tolerability |
| [19856651](https://pubmed.ncbi.nlm.nih.gov/19856651/) | 2009 | Phase 2 | Tumori | Weekly docetaxel + gemcitabine combination in anthracycline-pretreated metastatic breast cancer; dose-finding study preserving quality of life |
| [27997437](https://pubmed.ncbi.nlm.nih.gov/27997437/) | 2017 | Retrospective | Anti-Cancer Drugs | Adjuvant docetaxel-based chemotherapy and incidence of breast cancer-related lymphedema; characterized fluid retention and edema as key safety considerations |

---

## Philippines Market Information

Docetaxel is currently **not registered** with the Philippine Food and Drug Administration (FDA-PH). No approved pharmaceutical products were identified in the local registry (0 license records). Patients requiring docetaxel in the Philippines would currently need to access it through a special/compassionate use permit or through regulated importation pathways under FDA-PH authorization.

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (semisynthetic, microtubule-stabilizing agent; not targeted therapy, not immunotherapy) |
| Myelosuppression Risk | **High** — Neutropenia is the dose-limiting toxicity; febrile neutropenia occurs in approximately 10–15% of patients on standard 3-weekly regimens; G-CSF (filgrastim or pegfilgrastim) prophylaxis is strongly recommended per ASCO/ESMO guidelines |
| Emetogenicity Classification | **Low to moderate** (per MASCC/ESMO classification; antiemetic premedication is primarily directed at hypersensitivity and fluid retention prevention with 3-day corticosteroid premedication) |
| Monitoring Items | CBC with differential (before each cycle; consider day-8 nadir check in first cycle), liver function tests (ALT, AST, total bilirubin, alkaline phosphatase — dose reduction or contraindication if elevated), renal function, peripheral neuropathy assessment (CIPN grading scale), body weight and edema grading (cumulative fluid retention), cardiac function (LVEF monitoring when combined with trastuzumab or anthracyclines) |
| Handling Protection | Must follow cytotoxic drug handling regulations — closed-system drug transfer devices (CSTD) required during preparation; PPE including chemotherapy-rated gloves, gown, and eye protection; dedicated negative-pressure preparation area; cytotoxic waste segregation and disposal per institutional policy |

---

## Safety Considerations

Complete local safety data (Philippine FDA package insert, TFDA warnings, contraindications) is not yet available for this review (see Data Gap DG001). Based on globally available clinical information:

- **Key Warnings**: Severe hypersensitivity reactions may occur — **mandatory 3-day corticosteroid premedication** (e.g., oral dexamethasone starting the day before infusion) is required to reduce the risk and severity of fluid retention and hypersensitivity. Patients with elevated hepatic bilirubin or transaminases >1.5× ULN combined with alkaline phosphatase >2.5× ULN are at significantly increased risk of treatment-related mortality and should generally not receive docetaxel.
- **Known Toxicities**: Myelosuppression (dose-limiting; neutropenia most common), cumulative fluid retention and peripheral edema, alopecia (universal and reversible), peripheral sensory neuropathy (cumulative with repeated cycles), nail disorders, asthenia, mucositis, and diarrhea.

Please retrieve the complete warnings, contraindications, and drug interaction data from the official package insert before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Docetaxel has the highest tier of global clinical evidence (L1: ≥5 completed Phase 3 RCTs) for female breast carcinoma, confirming efficacy across all major subtypes and treatment settings — metastatic, neoadjuvant, and adjuvant. The TxGNN prediction score of 99.90% is the top-ranked indication among all predictions. The primary barrier to clinical use in the Philippines is the **absence of local regulatory registration**, not a lack of clinical evidence. Global approvals from the FDA (USA), EMA (Europe), and PMDA (Japan) provide a robust foundation for a Philippines registration application.

**To proceed, the following is needed:**
- Submission of a local drug registration dossier to the Philippine FDA (FDA-PH), leveraging reference-listed drug status from FDA/EMA-approved dossiers
- Retrieval of complete package insert data (DG001: TFDA/FDA package insert PDF) for full warnings, contraindications, and dosing guidance
- Retrieval of MOA and pharmacological data via DrugBank API (DG002) to formally complete the mechanistic analysis section
- Development of a local pharmacovigilance and risk management plan aligned with Philippines FDA regulatory requirements
- Confirmation of G-CSF (filgrastim/pegfilgrastim) availability in the local formulary, given the high febrile neutropenia risk requiring prophylaxis
- Assessment of cold-chain storage and reconstitution infrastructure for docetaxel supply chain management in the Philippines
- Conduct a PhilHealth reimbursement and formulary inclusion analysis to ensure sustainable patient access for breast cancer chemotherapy protocols
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

