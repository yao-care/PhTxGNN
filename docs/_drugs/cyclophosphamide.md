---
layout: default
title: Cyclophosphamide
parent: 僅模型預測 (L5)
nav_order: 87
evidence_level: L5
indication_count: 5
---

# Cyclophosphamide
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Cyclophosphamide: From Alkylating Chemotherapy to Myeloid Leukemia

## One-Sentence Summary

Cyclophosphamide is a well-established nitrogen mustard alkylating agent used globally in oncology and immunosuppression, though it currently holds no registered indication in the Philippines.
The TxGNN model predicts it may be effective for **Myeloid Leukemia**,
with **multiple Phase 2/3 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines registration; globally used as alkylating chemotherapy for cancers and autoimmune conditions |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L1 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack (listed as a high-severity data gap). Based on established pharmacology, Cyclophosphamide is a nitrogen mustard alkylating agent that works by crosslinking DNA strands — both inter-strand and intra-strand — thereby blocking DNA replication and triggering apoptosis in rapidly dividing cells. This mechanism is particularly effective against high-proliferation malignancies such as leukemia, where tumor cells divide continuously.

Cyclophosphamide plays a central role in myeloid leukemia treatment through two mechanistically distinct strategies. First, as a **myeloablative conditioning agent** prior to allogeneic hematopoietic stem cell transplantation (allo-HSCT), it is combined with busulfan (BuCy regimen) or total-body irradiation (TBI/Cy) to eradicate residual leukemia and permit donor engraftment — this is a globally accepted standard approach for AML patients proceeding to transplant. Second, as **post-transplant cyclophosphamide (PTCy)**, administered on Day +3 and +4 after transplantation, it has emerged as a highly effective and widely adopted GvHD prophylaxis strategy, particularly in haploidentical HSCT settings, demonstrating favorable relapse-free survival outcomes in both adult and pediatric AML cohorts.

The TxGNN model's high-confidence prediction of 99.47% reflects this robust, multi-faceted linkage between cyclophosphamide's known biology and its established clinical role across the myeloid leukemia treatment spectrum. The drug's dual capacity — direct leukemia cell kill at high doses and immune modulation at lower doses — provides a compelling mechanistic foundation for continued and expanded application in myeloid leukemia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT06098313](https://clinicaltrials.gov/study/NCT06098313) | Phase 2 | Active, not recruiting | 113 | Evaluates post-transplant cyclophosphamide (PTCy) with myeloablative or reduced-intensity conditioning for allo-HCT in higher-risk MDS and secondary AML; primary endpoint is GvHD-free, relapse-free survival |
| [NCT07132684](https://clinicaltrials.gov/study/NCT07132684) | Phase 3 | Recruiting | 240 | Multicenter randomized comparison of Venetoclax+Azacitidine (VA) vs Daunorubicin/Idarubicin+Cytarabine (D/IA) as induction regimens in elderly (ages 55–75) AML patients fit for intensive chemotherapy |
| [NCT00002798](https://clinicaltrials.gov/study/NCT00002798) | Phase 3 | Completed | 880 | Landmark randomized trial comparing multiple chemotherapy regimens with or without bone marrow transplantation in children with untreated AML or MDS |
| [NCT00002945](https://clinicaltrials.gov/study/NCT00002945) | Phase 3 | Completed | 61 | High-dose cytarabine+idarubicin induction followed by high-dose etoposide+**cyclophosphamide** intensification, ASCT, and IL-2 immunomodulation for previously untreated de novo and secondary adult myeloid leukemia |
| [NCT00005898](https://clinicaltrials.gov/study/NCT00005898) | Phase 1/2 | Completed | 30 | TBI + **Cyclophosphamide** + Fludarabine + ATG conditioning followed by HLA non-identical T-cell depleted HCT; assessed engraftment probability and GvHD incidence in AML/Fanconi's anemia |
| [NCT00134004](https://clinicaltrials.gov/study/NCT00134004) | Phase 2 | Completed | 210 | Fludarabine + **cyclophosphamide**-based non-myeloablative conditioning followed by partially HLA-mismatched bone marrow transplantation for hematologic malignancies including AML |
| [NCT01370213](https://clinicaltrials.gov/study/NCT01370213) | Phase 2 | Completed | 25 | NK cell-based non-myeloablative haploidentical transplantation for high-risk acute myeloid diseases; cyclophosphamide as part of conditioning; assessed leukemia-free neutrophil engraftment at Day +28 |
| [NCT03417154](https://clinicaltrials.gov/study/NCT03417154) | Phase 2 | Completed | 12 | Nivolumab + low-dose oral **cyclophosphamide** combination for relapsed/refractory AML and higher-risk MDS in patients not eligible for or declining HSCT; included randomized pilot sub-study |
| [NCT06802315](https://clinicaltrials.gov/study/NCT06802315) | Phase 2 | Recruiting | 38 | Intensity-modulated total marrow irradiation (IM-TMI, 9 Gy) + Fludarabine/Busulfan (FluBu4) + post-transplant **cyclophosphamide** (Day +3/+4) for high-risk AML, CML, and MDS allo-HSCT |
| [NCT01010217](https://clinicaltrials.gov/study/NCT01010217) | Phase 2 | Completed | 176 | Three-arm study comparing haploidentical, 1-antigen mismatched, and matched unrelated donor transplantation using T-cell replete allograft with high-dose post-transplant **cyclophosphamide** for hematologic malignancies |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40434956](https://pubmed.ncbi.nlm.nih.gov/40434956/) | 2025 | RCT | Future Oncology | Compares BuCy vs FluBu myeloablative conditioning for allo-HSCT in AML; FluBu shows similar efficacy with potentially lower toxicity profile |
| [35955881](https://pubmed.ncbi.nlm.nih.gov/35955881/) | 2022 | Prospective | Int J Mol Sci | PTCy after matched sibling and unrelated donor HSCT in pediatric AML; improved GvHD and relapse-free survival, supporting PTCy beyond haploidentical settings |
| [38499049](https://pubmed.ncbi.nlm.nih.gov/38499049/) | 2024 | Prospective Phase 2 | Transplant Immunology | Cladribine + BuCy as intensive conditioning prior to allo-HSCT for relapsed/refractory AML; demonstrated feasibility and preliminary efficacy |
| [25345651](https://pubmed.ncbi.nlm.nih.gov/25345651/) | 2015 | Prospective Phase 2 | Am J Hematol | Cy/Flu non-myeloablative allotransplant vs myeloablative allotransplant for 165 AML patients in remission; comparable event-free and overall survival at median 61-month follow-up |
| [39939431](https://pubmed.ncbi.nlm.nih.gov/39939431/) | 2025 | Retrospective Cohort | Bone Marrow Transplantation | EBMT registry analysis of 1,823 AML patients in CR1 receiving PTCy-based HSCT; myeloablative conditioning superior in adverse-risk cytogenetics |
| [40437709](https://pubmed.ncbi.nlm.nih.gov/40437709/) | 2025 | Retrospective Cohort | Eur J Haematol | RIC vs MAC conditioning in AML (<65 years) with ATG + PTCy + cyclosporine prophylaxis; MAC associated with lower relapse risk |
| [38466265](https://pubmed.ncbi.nlm.nih.gov/38466265/) | 2024 | Retrospective Cohort | Cytotherapy | Prognostic factors in haploidentical HSCT with PTCy for AML; PTCy provides effective GvHD suppression; disease status at transplant is the dominant prognostic factor |
| [40905088](https://pubmed.ncbi.nlm.nih.gov/40905088/) | 2026 | Retrospective Cohort | Haematologica | 217 AML patients in CR receiving MAC allo-HCT + PTCy-based GvHD prophylaxis; 2-year OS 77%, EFS 72%; adverse-risk patients had significantly worse outcomes |
| [33325761](https://pubmed.ncbi.nlm.nih.gov/33325761/) | 2021 | Retrospective Case Series | Leukemia & Lymphoma | High-dose cyclophosphamide (60 mg/kg) for cytoreduction in AML with hyperleukocytosis or leukostasis (WBC ≥50×10⁹/L); 41% response rate with acceptable safety |
| [29039989](https://pubmed.ncbi.nlm.nih.gov/29039989/) | 2017 | Case Series | Pediatr Hematol Oncol | Clofarabine + cyclophosphamide + etoposide for relapsed/refractory childhood and adolescent AML (n=17); 41% overall response rate (4 CR, 1 CRi, 2 PR) |

---

## Philippines Market Information

Cyclophosphamide currently has **no registered product authorizations** in the Philippines. The drug is classified as **Not Marketed**, with zero product licenses on record in the Philippines FDA database. Any clinical use would require evaluation through the Philippines FDA's compassionate special permit or importation pathway for unregistered drugs.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Nitrogen mustard alkylating agent |
| Myelosuppression Risk | **High** — Neutropenia, thrombocytopenia, and anemia are dose-limiting toxicities; nadir typically occurs 10–14 days after administration |
| Emetogenicity Classification | **Moderate to High** — Dose-dependent; single doses >1,500 mg/m² are highly emetogenic; standard doses are moderately emetogenic |
| Monitoring Items | CBC with differential (at least weekly during treatment), liver function tests, renal function (serum creatinine, BUN), urinalysis and urine dipstick for hematuria (hemorrhagic cystitis monitoring) |
| Handling Protection | Must follow cytotoxic drug handling regulations; high-dose regimens (≥1,000 mg/m²) require co-administration of **mesna** and aggressive IV hydration to prevent hemorrhagic cystitis |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important:** Key warnings, contraindications, and drug interaction data were identified as blocking and high-severity data gaps in this evidence pack. Based on established pharmacology, critical known risks include: **hemorrhagic cystitis** (requiring mesna and hydration at high doses), **severe myelosuppression** (infection and bleeding risk), **secondary malignancies** (therapy-related AML with long-term use), and **gonadotoxicity** (infertility risk, particularly in young patients). A formal safety review using the complete product package insert is required before any clinical decision.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence supporting cyclophosphamide in myeloid leukemia is exceptionally strong (Evidence Level L1), with multiple completed Phase 3 trials — including an 880-patient landmark pediatric AML trial (NCT00002798) — and extensive Phase 2 evidence across HSCT conditioning (BuCy), post-transplant GvHD prophylaxis (PTCy), and direct cytoreduction settings. The TxGNN prediction score of 99.47% accurately reflects this well-established, mechanistically coherent evidence base. However, the drug is currently unregistered in the Philippines and critical safety documentation is absent from the evidence pack, warranting guardrails before any clinical pathway is initiated.

**To proceed, the following is needed:**
- **Safety documentation (Blocking):** Download and analyze the complete package insert/SmPC to document key warnings, contraindications, and drug-drug interactions — currently a blocking data gap that prevents safety pre-screening
- **Philippines regulatory pathway:** Evaluate the Philippines FDA compassionate special permit or importation pathway for an unregistered drug; confirm availability of mesna for hemorrhagic cystitis prevention
- **MOA documentation (High priority):** Obtain formal mechanism of action data from the DrugBank API to complete the mechanistic linkage analysis
- **Patient population definition:** Specify the target AML subgroup (de novo vs. secondary AML; age bracket; cytogenetic/molecular risk category: favorable, intermediate, or adverse) to align with the appropriate evidence base
- **Institutional capacity assessment:** Confirm availability of HSCT infrastructure, supportive care (G-CSF, blood products, antimicrobial prophylaxis), and therapeutic drug monitoring for busulfan if BuCy conditioning is considered
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

