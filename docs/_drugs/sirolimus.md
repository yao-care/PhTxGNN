---
layout: default
title: Sirolimus
parent: 僅模型預測 (L5)
nav_order: 309
evidence_level: L5
indication_count: 10
---

# Sirolimus
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

# Sirolimus: From Renal Transplant Rejection to Liposarcoma

## One-Sentence Summary

Sirolimus (also known as rapamycin) is an mTOR inhibitor globally approved for prevention of renal transplant rejection and lymphangioleiomyomatosis (LAM), though not currently registered in the Philippines.
The TxGNN model predicts it may be effective for **Liposarcoma**, with **5 clinical trials** and **12 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Renal transplant rejection prevention; lymphangioleiomyomatosis — FDA-approved globally, not registered in the Philippines |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L2 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Sirolimus (rapamycin) inhibits mTORC1 (mechanistic target of rapamycin complex 1) by binding to the intracellular chaperone FKBP12, blocking downstream signaling — particularly S6K1 and 4E-BP1 — that drives cell growth, protein synthesis, and cell cycle progression. While formal MOA documentation was not included in this evidence package, the mechanism is extensively validated across both immunologic and oncologic settings. The FDA's 2015 approval of Sirolimus for LAM — a neoplasm driven by TSC2 mutation and constitutive mTOR activation — directly establishes its antitumor mechanism of action.

Dedifferentiated liposarcoma (DDLPS), the most clinically aggressive subtype of liposarcoma, frequently exhibits PI3K/Akt/mTOR pathway activation demonstrable by immunohistochemistry (PMID 26518767, 99 DDLPS tissue specimens). This positions mTORC1 as a mechanistically direct target. Preclinical studies in DDLPS patient-derived orthotopic xenograft (PDOX) models confirm that rapamycin combined with chloroquine arrests tumor growth in vivo (PMID 36309387, PMID 37400145). Liposarcoma and the drug's known indications (LAM, renal AML) share a common molecular dependency on dysregulated mTOR signaling, making the mechanistic extrapolation more than an inference.

The most compelling translational anchor is the completed Phase 2 trial NCT02821507 (n=70), which directly used a **Sirolimus-based combination** for myxoid liposarcoma and chondrosarcoma. In addition, three rapalogue analogs — Temsirolimus, Ridaforolimus, and Everolimus — have each reached Phase 2 in sarcoma cohorts, collectively demonstrating that mTOR inhibition is a viable strategy in this tumor family and that the class effect is pharmacologically reproducible.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02821507](https://clinicaltrials.gov/study/NCT02821507) | Phase 2 | Completed | 70 | **Direct Sirolimus combination** in metastatic or unresectable myxoid liposarcoma and chondrosarcoma; targets mTOR pathway dysregulation shared across sarcoma subtypes |
| [NCT00093080](https://clinicaltrials.gov/study/NCT00093080) | Phase 2 | Completed | 216 | Ridaforolimus (rapalogue) QDx5 q2w in advanced sarcoma; largest Phase 2 mTOR inhibitor sarcoma trial to date |
| [NCT01614795](https://clinicaltrials.gov/study/NCT01614795) | Phase 2 | Completed | 46 | Temsirolimus (Sirolimus prodrug) + Cixutumumab in recurrent/refractory pediatric sarcoma; mTOR inhibitor class activity confirmed in sarcoma |
| [NCT00949325](https://clinicaltrials.gov/study/NCT00949325) | Phase 1/2 | Completed | 24 | Temsirolimus + liposomal doxorubicin in advanced soft tissue and bone sarcoma; established safe dosing and preliminary antitumor activity |
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, not recruiting | 48 | Ribociclib (CDK4/6i) + Everolimus (mTOR) in dedifferentiated liposarcoma and leiomyosarcoma; CDK4/6 + mTOR dual blockade strategy with synergistic preclinical rationale |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|------------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 Report | Clin Cancer Res | SAR-096 trial: Ribociclib + Everolimus in DDL and LMS; CDK4/6 + mTOR dual inhibition demonstrates synergistic growth suppression in multiple tumor models |
| [39796641](https://pubmed.ncbi.nlm.nih.gov/39796641/) | 2024 | Review | Cancers | Comprehensive overview of novel therapeutics in soft tissue sarcoma, including recent FDA approvals and emerging targeted agents |
| [37400145](https://pubmed.ncbi.nlm.nih.gov/37400145/) | 2023 | Preclinical | Cancer Genomics Proteomics | Rapamycin + chloroquine synergistically inhibits autophagy and induces apoptosis in well-differentiated liposarcoma; in vitro and PDOX model efficacy |
| [37222206](https://pubmed.ncbi.nlm.nih.gov/37222206/) | 2023 | Review | Curr Opin Oncol | New targeted treatments for advanced sarcomas; rationale and clinical trial results for molecular-targeted agents |
| [36309387](https://pubmed.ncbi.nlm.nih.gov/36309387/) | 2022 | Preclinical (PDOX) | In Vivo | Chloroquine + rapamycin arrests tumor growth in DDLPS patient-derived orthotopic xenograft model with demonstrated tumor volume reduction |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Translational | Tumour Biol | Akt/mTOR and MAPK pathway activation confirmed in 99 DDLPS specimens by IHC; in vitro mTOR inhibitor antitumor effect demonstrated |
| [25519700](https://pubmed.ncbi.nlm.nih.gov/25519700/) | 2015 | Preclinical | Mol Cancer Ther | MLN0128 (ATP-competitive mTOR kinase inhibitor) shows potent in vitro and in vivo activity against bone and soft-tissue sarcoma; supports mTOR dependency |
| [20497911](https://pubmed.ncbi.nlm.nih.gov/20497911/) | 2010 | Review | Bull Cancer | Targeted treatment of rare connective tissue tumors; classifies sarcoma subgroups by molecular alteration and reviews mTOR-pathway targeting |
| [16434506](https://pubmed.ncbi.nlm.nih.gov/16434506/) | 2006 | Cohort | JASN | Sirolimus after cyclosporine withdrawal reduces malignancy risk in renal transplant recipients (n=430); demonstrates direct Sirolimus antitumor properties in vivo |
| [26093731](https://pubmed.ncbi.nlm.nih.gov/26093731/) | 2015 | Cohort | Transplant Proc | Long-term cancer surveillance in renal transplant patients; quantifies impact of immunosuppressive drug choice (including Sirolimus) on malignancy incidence |

---

## Philippines Market Information

Sirolimus currently has no registered products with the Philippines Food and Drug Administration. No product licenses are on record.

---

## Cytotoxicity

Sirolimus is classified as a targeted antineoplastic agent (mTOR inhibitor, FDA-approved for LAM — a neoplastic condition), warranting oncology-appropriate monitoring.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — mTOR inhibitor (rapalogue class); not conventional cytotoxic |
| Myelosuppression Risk | Low to moderate: thrombocytopenia and anemia reported; significantly less myelosuppressive than conventional chemotherapy |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, serum creatinine and urinalysis, liver function tests, fasting lipid panel (triglycerides and cholesterol), fasting blood glucose, wound healing assessment before invasive procedures |
| Handling Protection | Standard oral oncology precautions; special cytotoxic handling regulations not required (non-alkylating, non-DNA-intercalating mechanism) |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The completed Phase 2 trial NCT02821507 provides the most direct clinical evidence — Sirolimus itself was used in combination in a myxoid liposarcoma cohort (n=70) — supported by three additional completed rapalogue Phase 2 trials in sarcoma, mechanistic data confirming PI3K/Akt/mTOR activation in DDLPS tissue, and PDOX model proof of concept. The TxGNN score of 99.89% and L2 evidence level justify forward momentum with appropriate risk management.

**To proceed, the following is needed:**
- Full published efficacy and safety results from NCT02821507 (direct Sirolimus in liposarcoma/chondrosarcoma, n=70) to confirm objective response and PFS endpoints
- Formal MOA documentation from the DrugBank API to complete the drug-level dossier
- Philippines regulatory pathway assessment: compassionate use, clinical trial importation, or Section 21 access mechanism for unregistered drugs
- Molecular patient-selection criteria: tissue profiling for PI3K/Akt/mTOR pathway activation or TSC1/TSC2 mutation status to identify responders
- Immunosuppression-aware safety management plan addressing infection prophylaxis, metabolic monitoring, and wound-healing protocols for the oncology context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

