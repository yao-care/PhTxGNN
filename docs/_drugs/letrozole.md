---
layout: default
title: Letrozole
parent: 僅模型預測 (L5)
nav_order: 199
evidence_level: L5
indication_count: 10
---

# Letrozole
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

# Letrozole: From Aromatase Inhibition to Female Breast Carcinoma

## One-Sentence Summary

Letrozole is a third-generation non-steroidal aromatase inhibitor that suppresses circulating estrogen by more than 99% in postmenopausal women, globally established as the backbone endocrine therapy for hormone receptor-positive breast cancer — though currently unregistered in the Philippines.
The TxGNN model predicts it is highly effective for **Female Breast Carcinoma** with a confidence score of **99.98%**,
supported by **50+ registered clinical trials** and **20+ publications** — including multiple landmark Phase 3 RCTs (BIG 1-98, PALOMA-2, MONALEESA-2) that have cemented it as an international standard of care.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines registration on record; globally approved for HR+/HER2-negative breast cancer |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Letrozole competitively and selectively inhibits CYP19A1 (aromatase), the enzyme that converts adrenal androgens (androstenedione, testosterone) to estrogens (estrone, estradiol) in peripheral tissues and the tumor microenvironment. This results in >99% suppression of circulating estrogen in postmenopausal women — effectively cutting off the primary proliferative signal that drives estrogen receptor-positive (ER+) breast cancer cells. Unlike tamoxifen, which blocks ER binding, Letrozole eliminates the ligand itself, making it particularly potent in settings of high local aromatase activity.

The biological rationale is direct and reinforced by decades of clinical data: ER+ breast cancer cells depend on estrogen-driven ERα transcription to activate growth-promoting genes such as cyclin D1, c-Myc, and IGF-1R. Letrozole's near-complete estrogen depletion arrests this pathway, causing tumour regression in both early and advanced disease. Its established synergy with CDK4/6 inhibitors (palbociclib, ribociclib, abemaciclib) — which block cell-cycle progression downstream of the same ER signalling axis — has made the combination a first-line global standard since 2016.

It is important to note that, while Letrozole is not currently registered in the Philippines, the TxGNN model's prediction of 99.98% essentially recapitulates the overwhelming global consensus. This report therefore serves as an evidence-based argument for market introduction, highlighting both the strength of the existing data package and the key guardrails required before local deployment.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01740427](https://clinicaltrials.gov/study/NCT01740427) | Phase 3 | Completed | 666 | PALOMA-2: Palbociclib + Letrozole vs. Letrozole alone as first-line therapy for postmenopausal ER+/HER2- ABC; Letrozole arm serves as the benchmark for all subsequent first-line CDK4/6i combinations |
| [NCT02338310](https://clinicaltrials.gov/study/NCT02338310) | Phase 3 | Active, not recruiting | 4,486 | TOPIC: Perioperative Letrozole followed by standard adjuvant therapy vs. standard therapy alone; evaluates Ki67 suppression after 2-week AI as an individualised predictor of recurrence-free survival |
| [NCT05163106](https://clinicaltrials.gov/study/NCT05163106) | Phase 2 | Completed | 85 | NEOLETRIB: Ribociclib + Letrozole as neoadjuvant treatment in stage III locally advanced breast cancer; demonstrates feasibility of replacing chemotherapy with CDK4/6i + AI combinations |
| [NCT02600923](https://clinicaltrials.gov/study/NCT02600923) | Phase 3 | Completed | 131 | Palbociclib + Letrozole expanded access for Latin American HR+/HER2- ABC; confirms tolerability and Letrozole-based regimen effectiveness in diverse populations |
| [NCT00291135](https://clinicaltrials.gov/study/NCT00291135) | Phase 2 | Completed | 42 | Six months of Letrozole in high-risk postmenopausal women on HRT; direct assessment of Letrozole single-agent effect on breast tissue biomarkers (Ki67, ER) in a chemoprevention context |
| [NCT02692755](https://clinicaltrials.gov/study/NCT02692755) | Phase 2/3 | Completed | 35 | Palbociclib + Letrozole/Fulvestrant in African American women with HR+/HER2- ABC; prospectively evaluated haematological safety in an under-represented population |
| [NCT00754845](https://clinicaltrials.gov/study/NCT00754845) | Phase 3 | Completed | 1,918 | Extended adjuvant Letrozole vs. placebo after completing 5 years of prior aromatase inhibitor (MA.17 extension); assessed efficacy of prolonged oestrogen suppression |
| [NCT00171704](https://clinicaltrials.gov/study/NCT00171704) | Phase 3 | Completed | 263 | Head-to-head Letrozole vs. Tamoxifen effects on bone mineral density and lipid profiles in adjuvant ER+ early breast cancer; key safety dataset for long-term use |
| [NCT03056755](https://clinicaltrials.gov/study/NCT03056755) | Phase 2 | Completed | 383 | BYLieve: Alpelisib + Letrozole (or Fulvestrant) in PIK3CA-mutated HR+/HER2- ABC after prior CDK4/6i progression; Letrozole as endocrine backbone in PIK3CA-pathway combinations |
| [NCT04553133](https://clinicaltrials.gov/study/NCT04553133) | Phase 2 | Active, not recruiting | 154 | Phase 1/2 dose escalation of PF-07104091 ± Letrozole in advanced breast and ovarian cancers; Letrozole as combination backbone to evaluate novel CDK2 inhibition |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [16382061](https://pubmed.ncbi.nlm.nih.gov/16382061/) | 2005 | RCT Phase 3 (BIG 1-98) | N Engl J Med | Letrozole superior to tamoxifen as adjuvant therapy in postmenopausal ER+ early breast cancer; established Letrozole as the adjuvant aromatase inhibitor reference standard |
| [27959613](https://pubmed.ncbi.nlm.nih.gov/27959613/) | 2016 | RCT Phase 3 (PALOMA-2) | N Engl J Med | Palbociclib + Letrozole significantly prolonged PFS (27.6 vs 14.5 months, HR 0.58) vs. Letrozole alone in first-line HR+/HER2- ABC; confirmed CDK4/6i + Letrozole as global standard |
| [35263519](https://pubmed.ncbi.nlm.nih.gov/35263519/) | 2022 | RCT Phase 3 OS (MONALEESA-2) | N Engl J Med | Ribociclib + Letrozole demonstrated significant overall survival benefit vs. Letrozole alone in HR+/HER2- ABC (median OS 63.9 vs 51.4 months) |
| [29718092](https://pubmed.ncbi.nlm.nih.gov/29718092/) | 2018 | RCT Phase 3 Update (MONALEESA-2) | Ann Oncol | Updated MONALEESA-2: ribociclib + letrozole maintained PFS superiority; exploratory biomarker analyses identified PIK3CA mutation and CCND1/CDK4 pathway features as informative markers |
| [38507751](https://pubmed.ncbi.nlm.nih.gov/38507751/) | 2024 | RCT Phase 3 (NATALEE) | N Engl J Med | Ribociclib + NSAI (letrozole or anastrozole) as adjuvant therapy significantly improved iDFS (HR 0.75) vs. NSAI alone in HR+/HER2- early breast cancer; extends CDK4/6i indication to the curative setting |
| [30475668](https://pubmed.ncbi.nlm.nih.gov/30475668/) | 2019 | RCT Phase 3 Long-term FU (BIG 1-98) | J Clin Oncol | BIG 1-98 12.6-year follow-up: sustained disease-free and overall survival benefit of letrozole vs. tamoxifen in postmenopausal ER+ breast cancer; late recurrence data inform extended therapy strategies |
| [35464999](https://pubmed.ncbi.nlm.nih.gov/35464999/) | 2022 | RCT | Comput Math Methods Med | Sequential tamoxifen → letrozole vs. letrozole monotherapy in breast carcinoma: letrozole arm demonstrated superior efficacy outcomes and comparable safety profile |
| [32683565](https://pubmed.ncbi.nlm.nih.gov/32683565/) | 2020 | RCT Phase 2 OS (PALOMA-1) | Breast Cancer Res Treat | PALOMA-1 OS analysis: palbociclib + letrozole vs. letrozole alone — confirmed PFS benefit (HR 0.488); OS trend favoured combination arm |
| [38729566](https://pubmed.ncbi.nlm.nih.gov/38729566/) | 2024 | RCT Phase 3 OS (MONARCH 3) | Ann Oncol | Abemaciclib + NSAI (including letrozole/anastrozole) as initial therapy for HR+/HER2- ABC: final OS analysis demonstrated significant survival benefit, validating CDK4/6i + aromatase inhibitor as standard first-line |
| [36243120](https://pubmed.ncbi.nlm.nih.gov/36243120/) | 2022 | Review | Life Sci | Comprehensive review of Letrozole pharmacology, toxicology, and therapeutic applications across adjuvant, neoadjuvant, and metastatic breast cancer settings; covers mechanism, PK/PD, and emerging uses |

---

## Philippines Market Information

Letrozole currently has **no registered products** in the Philippines (FDA Philippines). There are zero marketing authorizations, no approved indications, and no licensed dosage forms on record. This is a notable gap given Letrozole's status as a globally approved essential medicine recommended by the WHO, ESMO, NCCN, and ASCO for HR+/HER2-negative breast cancer treatment.

---

## Cytotoxicity

Letrozole is an antineoplastic agent used in breast cancer treatment. It is classified as endocrine/hormonal therapy and is **not** conventional cytotoxic chemotherapy.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Hormonal antineoplastic — non-steroidal aromatase inhibitor (triazole class); targeted endocrine mechanism, not DNA-damaging cytotoxic |
| Myelosuppression Risk | Low — aromatase inhibitors do not suppress bone marrow hematopoiesis; routine CBC monitoring is not required beyond baseline |
| Emetogenicity Classification | Minimal — oral daily tablet; standard antiemetic prophylaxis not indicated |
| Monitoring Items | Bone mineral density (DEXA scan at baseline and annually); lipid profile; liver function tests; arthralgia/myalgia assessment; cardiovascular risk factors in postmenopausal patients |
| Handling Protection | Standard pharmaceutical handling applies; cytotoxic drug handling precautions (closed-system transfer, PPE for hazardous drugs) are **not** required for Letrozole |

---

## Safety Considerations

Detailed Philippines-specific safety labeling is unavailable as Letrozole is not currently registered. Please refer to the international package insert and established clinical safety data for guidance. From the published trial literature, key known adverse effects include musculoskeletal symptoms (arthralgia, myalgia), bone mineral density reduction with long-term use, hot flashes, fatigue, and hypercholesterolaemia.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for Letrozole in female breast carcinoma is among the strongest in oncology — multiple completed Phase 3 RCTs consistently demonstrate superior efficacy over tamoxifen in the adjuvant setting and establish it as the endocrine backbone for CDK4/6 inhibitor combinations. The TxGNN score of 99.98% reflects this global consensus. The critical blocker is the complete absence of Philippines regulatory registration and the identified data gaps in local safety documentation.

**To proceed, the following is needed:**
- **Philippines FDA registration dossier**: Compile the existing international NDA/MAA data package (BIG 1-98, PALOMA-2, MONALEESA-2 as pivotal studies) for submission to the Food and Drug Administration of the Philippines
- **Philippines package insert**: Develop local prescribing information with Philippines-specific pharmacovigilance requirements and YMYL-compliant patient information materials
- **Safety gap remediation**: Obtain full drug interaction database (DDI data gap DG001 remains unresolved); acquire TFDA/PMDA/EMA label warnings and contraindications (DG001/DG002)
- **Bone health management protocol**: Establish baseline and periodic DEXA monitoring guidelines adapted to the Philippines oncology care infrastructure
- **Pharmacoeconomic assessment**: Evaluate cost-effectiveness and affordability within the Philippine Health Insurance Corporation (PhilHealth) reimbursement framework
- **Supply and access planning**: Identify local distributors, confirm oral tablet cold-chain requirements, and assess availability of 2.5 mg tablet formulation

> **Disclaimer**: This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

