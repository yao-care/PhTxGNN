---
layout: default
title: Doxorubicin
parent: 僅模型預測 (L5)
nav_order: 117
evidence_level: L5
indication_count: 10
---

# Doxorubicin
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

# Doxorubicin: From Established Antineoplastic Agent to Ewing Sarcoma

## One-Sentence Summary

Doxorubicin is a globally established anthracycline cytotoxic agent recognized as a backbone treatment across breast cancer, acute leukemias, lymphomas, and multiple solid tumors — though it currently holds no registration in the Philippines.
The TxGNN model predicts it may be effective for **Ewing Sarcoma** with near-perfect confidence (99.90%), a prediction powerfully validated by **multiple completed Phase III RCTs** and **20 publications** that already position doxorubicin at the heart of international standard-of-care protocols for this disease.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines; globally established for breast cancer, acute leukemias, lymphomas, and multiple solid tumors |
| Predicted New Indication | Ewing Sarcoma |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this evidence pack. Based on established pharmacological knowledge, doxorubicin is an anthracycline antibiotic that intercalates into DNA and inhibits Topoisomerase IIα (Topo IIα), triggering DNA double-strand breaks and apoptosis. It also generates reactive oxygen species (ROS) that amplify cellular damage. These mechanisms are most potent in rapidly dividing cells that express high levels of Topo IIα — precisely the biological profile of Ewing sarcoma cells.

Ewing sarcoma is driven by the EWSR1-FLI1 (or related EWSR1-ETS) chromosomal fusion, which promotes aggressive proliferation and genomic instability. This renders the tumor cells exquisitely sensitive to DNA-damaging agents such as doxorubicin. The convergence of Topo IIα overexpression, high proliferative index, and impaired DNA repair pathways in Ewing sarcoma cells provides a compelling mechanistic basis for doxorubicin's activity.

Critically, this prediction reflects evidence confirmation rather than a novel hypothesis: doxorubicin is already embedded in the internationally recognized first-line VDC/IE regimen (Vincristine, Doxorubicin, Cyclophosphamide alternating with Ifosfamide, Etoposide), established through multiple large-scale Phase III trials including AEWS0031, EURO-EWING 99, and EE2012. The TxGNN score of 99.90% and L1 classification reflect the overwhelming clinical consensus on doxorubicin's centrality in curing Ewing sarcoma.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02063022](https://clinicaltrials.gov/study/NCT02063022) | Phase 3 | Completed | 278 | Randomized Phase III comparing standard vs. dose-intensive VDC/IE in non-metastatic Ewing sarcoma; directly evaluates doxorubicin dose intensification as the pivotal strategic variable |
| [NCT00006734](https://clinicaltrials.gov/study/NCT00006734) | Phase 3 | Completed | 587 | Randomized Phase III trial of interval-compressed chemotherapy schedules for Ewing sarcoma and PNET; doxorubicin is a central component of the VDC backbone evaluated |
| [NCT01231906](https://clinicaltrials.gov/study/NCT01231906) | Phase 3 | Completed | 642 | COG AEWS1031: Randomized Phase III adding VTC to standard VDC/IE in non-metastatic Ewing sarcoma; doxorubicin-containing VDC serves as the established standard-of-care control |
| [NCT02306161](https://clinicaltrials.gov/study/NCT02306161) | Phase 3 | Active, Not Recruiting | 312 | COG AEWS1221: Randomized Phase III evaluating IGF-1R antibody ganitumab added to interval-compressed VDC/IE chemotherapy in newly diagnosed metastatic Ewing sarcoma |
| [NCT06820957](https://clinicaltrials.gov/study/NCT06820957) | Phase 2/3 | Active, Not Recruiting | 437 | Randomized trial of VIrR + VDC/IE vs. VDC/IE alone for newly diagnosed metastatic Ewing sarcoma; confirms the ongoing central role of doxorubicin (as part of VDC) in current trials |
| [NCT00002643](https://clinicaltrials.gov/study/NCT00002643) | Phase 2 | Completed | 130 | Pediatric Oncology Group: High-intensity doxorubicin-containing chemotherapy with growth factor support for newly diagnosed metastatic Ewing sarcoma; direct evidence in the highest-risk subgroup |
| [NCT03011528](https://clinicaltrials.gov/study/NCT03011528) | Phase 2 | Completed | 45 | CombinaiR3: First-line doxorubicin-based combination regimen for Ewing sarcoma with primary extrapulmonary metastases; directly evaluates doxorubicin efficacy in this high-risk subgroup |
| [NCT03277924](https://clinicaltrials.gov/study/NCT03277924) | Phase 1/2 | Completed | 197 | International multicenter trial evaluating immunotherapy (sunitinib/nivolumab) combined with doxorubicin-containing chemotherapy for advanced soft tissue and bone sarcomas including Ewing sarcoma |
| [NCT00001209](https://clinicaltrials.gov/study/NCT00001209) | Phase 1 | Completed | 120 | Foundational NIH pilot study of VAC (Vincristine, Adriamycin/Doxorubicin, Cyclophosphamide) alternating with ifosfamide/VP-16 for Ewing sarcoma; early evidence establishing doxorubicin's role |
| [NCT00020566](https://clinicaltrials.gov/study/NCT00020566) | Phase 3 | Unknown | 1,200 | EURO-E.W.I.N.G.99: Large European randomized Phase III studying combination chemotherapy (including doxorubicin) with or without high-dose consolidation in Ewing sarcoma across multiple countries |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12594313](https://pubmed.ncbi.nlm.nih.gov/12594313/) | 2003 | Phase III RCT | N Engl J Med | Landmark trial showing that adding ifosfamide/etoposide to standard doxorubicin-containing chemotherapy significantly improved survival in Ewing sarcoma; established the modern VDC/IE regimen as standard of care |
| [23091096](https://pubmed.ncbi.nlm.nih.gov/23091096/) | 2012 | Phase III RCT | J Clin Oncol | AEWS0031: Interval compression of doxorubicin-based VDC/IE improved event-free survival in localized Ewing sarcoma; confirmed doxorubicin dose intensity as a critical prognostic determinant |
| [36522207](https://pubmed.ncbi.nlm.nih.gov/36522207/) | 2022 | Phase III RCT | Lancet | EE2012: Head-to-head randomized comparison of European (doxorubicin-based) vs. US VDC/IE regimens in newly diagnosed Ewing sarcoma across multiple countries; directly addresses doxorubicin's role vs. alternatives |
| [36669140](https://pubmed.ncbi.nlm.nih.gov/36669140/) | 2023 | Phase III RCT | J Clin Oncol | AEWS1221: Ganitumab (IGF-1R antibody) added to interval-compressed VDC/IE in metastatic Ewing sarcoma; doxorubicin is the pharmacological backbone of this Phase III trial in the highest-risk setting |
| [35427190](https://pubmed.ncbi.nlm.nih.gov/35427190/) | 2022 | Phase III RCT | J Clin Oncol | Ewing 2008R3: 12-country Phase III trial of high-dose treosulfan/melphalan consolidation vs. standard therapy in high-risk Ewing sarcoma; doxorubicin forms the induction platform |
| [31952545](https://pubmed.ncbi.nlm.nih.gov/31952545/) | 2020 | Phase III RCT | Trials | EURO EWING 2012: International randomized trial protocol comparing doxorubicin-based and alternative induction/consolidation regimens; provides framework for evaluating doxorubicin's comparative contribution |
| [37651654](https://pubmed.ncbi.nlm.nih.gov/37651654/) | 2023 | Phase III RCT (Follow-up) | J Clin Oncol | Long-term outcomes from AEWS0031: 10+ year follow-up of interval-compressed doxorubicin-based VDC/IE; confirms durable benefit and long-term tolerability of doxorubicin-containing regimens |
| [20152770](https://pubmed.ncbi.nlm.nih.gov/20152770/) | 2010 | Review | Lancet Oncol | Comprehensive review of Ewing sarcoma management; documents improvement from <10% survival before chemotherapy to ~75% for localized disease with modern doxorubicin-based multidrug regimens |
| [26304893](https://pubmed.ncbi.nlm.nih.gov/26304893/) | 2015 | Review | J Clin Oncol | "Ewing Sarcoma: Current Management and Future Approaches" — authoritative summary of risk-adapted doxorubicin-containing chemotherapy as the international standard, and unmet needs in metastatic disease |
| [1833556](https://pubmed.ncbi.nlm.nih.gov/1833556/) | 1991 | Dose-Intensity Analysis | J Natl Cancer Inst | Foundational dose-intensity analysis showing doxorubicin dose intensity most closely correlates with favorable outcomes across Ewing sarcoma trials; established the rationale for doxorubicin as the key active agent in combination regimens |

---

## Philippines Market Information

Doxorubicin currently has **no registered products** in the Philippines. The drug is classified as "Not Marketed" with zero active license authorizations on file with FDA Philippines.

Given the absence of local registration, clinical access to doxorubicin for Ewing sarcoma treatment would require formal pathways such as special importation authorization, compassionate use programs, or hospital-based procurement under applicable FDA Philippines regulations.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Anthracycline class (DNA intercalator / Topoisomerase IIα inhibitor) |
| Myelosuppression Risk | High — Neutropenia and thrombocytopenia are dose-limiting toxicities; nadir typically at days 10–14 post-dose, recovery by approximately day 21 |
| Emetogenicity Classification | Moderate to High (dose-dependent; bolus doxorubicin ≥60 mg/m² classified as high emetic risk per MASCC/ASCO guidelines) |
| Monitoring Items | CBC with differential (before each cycle), liver function tests (hepatic metabolism), renal function, baseline LVEF / echocardiogram and periodic cardiac reassessment, serum troponin, cumulative lifetime anthracycline dose tracking (maximum ~450–550 mg/m²) |
| Handling Protection | Must follow cytotoxic drug handling regulations — preparation in biological safety cabinet with closed-system drug transfer devices (CSTDs), double-glove and gown, eye and face protection; dedicated hazardous waste disposal per institutional cytotoxic protocols |

---

## Safety Considerations

Please refer to the package insert for complete safety information, as detailed local warning and contraindication data are not available in this evidence pack.

The following safety signals are universally recognized for doxorubicin and are critical for clinical planning:

- **Cardiotoxicity**: Cumulative dose-dependent cardiomyopathy is doxorubicin's most serious long-term risk. Cardiac function (LVEF) must be monitored at baseline and at intervals throughout therapy. Pediatric patients face particular long-term risk.
- **Vesicant hazard**: Doxorubicin is a potent vesicant; extravasation causes severe tissue necrosis. Central venous access is strongly recommended for all administrations.
- **Therapy-related secondary malignancy**: Long-term risk of secondary AML (therapy-related) is associated with Topoisomerase II inhibitor exposure, particularly relevant for pediatric Ewing sarcoma survivors.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Doxorubicin is not a repurposing candidate in the conventional sense — it is the internationally established, Phase III–validated cornerstone of Ewing sarcoma chemotherapy. The TxGNN model's 99.90% prediction score and L1 evidence classification reflect the exceptional strength of existing evidence. The primary barrier is a local market access gap: doxorubicin is not registered in the Philippines, meaning patients cannot access it through standard channels despite overwhelming global clinical evidence supporting its use.

**To proceed, the following is needed:**
- **Regulatory pathway**: Initiate a special importation or compassionate use authorization process through FDA Philippines; evaluate eligibility under the Philippine Generics Act and FDA Circular frameworks for unlicensed essential medicines
- **Protocol alignment**: Adopt an evidence-based institutional chemotherapy protocol aligned with AEWS0031 / EURO-EWING 99 / EE2012 standards for consistent and safe local implementation
- **Cardiac monitoring program**: Establish baseline LVEF echocardiography and periodic cardiac reassessment protocol; consider cardioprotection with dexrazoxane for pediatric patients at risk for high cumulative anthracycline exposure
- **Cumulative dose registry**: Implement a patient-level lifetime anthracycline dose tracking system to prevent cardiotoxicity from dose accumulation across treatment courses
- **MOA documentation**: Obtain complete mechanism of action data via DrugBank API (DB00997) to address the existing data gap and support future regulatory filings
- **Supply chain planning**: Identify reliable importation sources and ensure cold-chain storage infrastructure for doxorubicin availability at treating institutions
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

