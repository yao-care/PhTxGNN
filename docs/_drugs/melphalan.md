---
layout: default
title: Melphalan
parent: Model Prediction Only (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Melphalan
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

# Melphalan: From Ovarian Cancer to Gonadal Germ Cell Tumor

## One-Sentence Summary

Melphalan is an alkylating chemotherapy drug, originally used for ovarian cancer.
The TxGNN model predicts it may be effective for **gonadal germ cell tumor**,
with **7 clinical trials** and **1 publication** currently linked to this prediction. Most of these trials are small, mixed-population studies in which melphalan is one component of a high-dose regimen.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Ovarian cancer (from the knowledge graph; no approved indication text is available for the local registration) |
| Predicted New Indication | Gonadal germ cell tumor |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 (see note below) |
| Philippines Market Status | Cancelled only (registration cancelled) |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

*Note on evidence level:* The data compiled for this report assign L2 on the basis of one completed Phase 2 trial (NCT00936936, 64 patients). That trial tested a multi-drug regimen and does not isolate melphalan's contribution. It is also a single-arm study, not a randomised controlled trial, so by the strict rule the evidence is weaker than L2.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, melphalan is a DNA-alkylating agent that forms interstrand crosslinks. Its efficacy in ovarian cancer is established, and mechanistically it may be applicable to gonadal germ cell tumors.

Germ cell tumors are highly chemosensitive to DNA-damaging agents. Melphalan has been used in high-dose chemotherapy regimens with autologous stem cell rescue for relapsed or poor-prognosis germ cell tumors. The very high TxGNN score is also consistent with the existing ovarian germ cell tumor labels in the knowledge graph.

Other predictions for ovarian primitive germ cell tumor and female breast carcinoma are supported by small Phase 1/2 studies and case reports. Predictions for choriocarcinoma of ovary, non-epithelial ovarian tumor and several mucinous adenocarcinomas (rectum, colon, gallbladder, cervix, endometrium) rest on the model alone, with no trials or literature found.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | Two cycles of high-dose chemotherapy (gemcitabine, docetaxel, melphalan, carboplatin, then ifosfamide, carboplatin, etoposide) for poor-prognosis relapsed germ-cell tumors; melphalan's specific contribution is not isolated |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Escalating-dose melphalan with autologous stem cell support and amifostine cytoprotection in cancer patients; mixed population |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Eight high-dose chemotherapy regimens with autologous transplant for hematologic malignancy and selected solid tumors; large but heterogeneous |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | Busulfan, melphalan and topotecan with autologous transplant in advanced or recurrent tumors; melphalan effect confounded by the combination |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | Not applicable | Completed | 174 | High-dose chemotherapy with or without total-body irradiation before autologous transplant; germ cell tumors are a small subset |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal melphalan for recurrent neoplastic meningitis; different route and indication |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine as a chemoprotectant with autologous transplant in pediatric solid and brain tumors; supportive-care focus |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Other (mechanistic/endocrine study) | Acta - Unio Internationalis Contra Cancrum | Early study of hormonal and alkylating drugs on pituitary follicle-stimulating function; no abstract available and only indirectly related to germ cell tumor treatment |

Literature is much richer for the lower-ranked prediction of female breast carcinoma (for example high-dose melphalan reviews and a randomised comparison with vinorelbine). It is not listed here because this report focuses on the top-ranked prediction.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0307 | Melphalan | Not specified | Not specified (status: cancelled) |

The only registration found is cancelled, so no valid melphalan product is currently registered in the Philippines according to the data compiled for this report.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (alkylating agent, nitrogen mustard class) |
| Myelosuppression Risk | High (the knowledge graph links melphalan to neutropenia, leukopenia, thrombocytopenia and anemia) |
| Emetogenicity Classification | Please refer to the package insert warnings and precautions |
| Monitoring Items | CBC with differential, liver and renal function |
| Handling Protection | Must follow cytotoxic drug handling regulations |

## Safety Considerations

- **Contraindication/risk signals from the knowledge graph (not label text):** These include kidney disease, thrombocytopenia, anemia (including macrocytic and hemolytic), leukopenia, neutropenia and agranulocytosis (including congenital forms), interstitial lung disease, pulmonary fibrosis, drug-induced liver injury and vasculitis.
- **Drug Interactions:** 100 interactions were identified; the first 20 were reviewed.
  - Moderate: amphotericin B (including lipid complex, cholesteryl sulfate and liposomal forms).
  - Minor: cimetidine, levofloxacin, zinc sulfate and zinc gluconate.
  - Unclassified severity: lansoprazole, omeprazole, pantoprazole, famotidine, dolasetron, granisetron, aspirin, morphine, metformin, vancomycin, prednisone and simvastatin.
- A literature review also notes that alkylating agents such as melphalan carry a high rate of second malignancies, mostly acute leukaemias.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic rationale is plausible and the TxGNN score is very high, but the supporting trials are small and combine melphalan with other agents, so its own benefit cannot be separated out. No melphalan product is currently valid in the Philippines, and the package-insert safety data are missing, which blocks safety screening.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines
- Mechanism of action data (for example from DrugBank)
- Clinical data that isolate melphalan's contribution in germ cell tumors, and a review of established standard regimens for comparison
- Clarification of the cancelled registration (PNF-0307) and a plan for the dosage form and route of any product to be used
- A safety monitoring plan covering severe myelosuppression, renal impairment and pulmonary toxicity
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

