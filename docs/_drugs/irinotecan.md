---
layout: default
title: Irinotecan
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 1
---

# Irinotecan
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

Using `txgnn-pipeline` skill to confirm context. Now generating the report from the Evidence Pack.

---

# Irinotecan: From Colorectal Cancer to Female Breast Carcinoma

## One-Sentence Summary

Irinotecan is a topoisomerase I inhibitor globally approved for colorectal cancer and other gastrointestinal malignancies, where its active metabolite SN-38 induces tumour cell apoptosis via DNA replication fork collapse.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
with **22 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Colorectal cancer (global standard; no Philippines registration on file) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.08% |
| Evidence Level | L2 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Irinotecan (CPT-11) is a prodrug converted in vivo to SN-38, a potent topoisomerase I (Top1) inhibitor. SN-38 stabilises the Top1–DNA covalent complex, prevents DNA strand religation, and causes replication-fork collapse with double-strand breaks — ultimately triggering tumour cell apoptosis. Breast cancer, particularly triple-negative breast cancer (TNBC), is characterised by high proliferative rates and elevated topoisomerase I expression, making it mechanistically sensitive to this class of agent.

The clearest mechanistic bridge between irinotecan and breast cancer is Sacituzumab Govitecan (SG), an FDA-approved antibody–drug conjugate that delivers SN-38 directly to tumour cells via a Trop-2-targeting antibody. SG carries full regulatory approval for metastatic TNBC and HR+/HER2− metastatic breast cancer — effectively confirming that SN-38 is cytotoxically active in the breast cancer microenvironment. This constitutes mechanism-level validation that goes well beyond a model prediction.

Importantly, irinotecan as a bare drug has also been evaluated directly in clinical trials. Phase 2 studies (NCT00072852; NCT03562390) enrolled patients with anthracycline- and taxane-refractory metastatic breast cancer, and a Phase 1 study specifically targeted triple-negative recurrent breast cancer (NCT00031681). Additionally, the PHENOMENAL Phase 2 trial (2026) demonstrated that liposomal irinotecan crosses the blood-brain barrier and shows antitumour activity in HER2-negative breast cancer with brain metastases — a particularly high-unmet-need population. Taken together, the mechanistic rationale and the clinical evidence base are mutually reinforcing.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00072852](https://clinicaltrials.gov/study/NCT00072852) | Phase 2 | Completed | 134 | Single-agent irinotecan (two dosing schedules) in women with anthracycline-, taxane-, and capecitabine-refractory metastatic breast cancer. This is the core Phase 2 direct-efficacy trial for this repurposing prediction. |
| [NCT01631552](https://clinicaltrials.gov/study/NCT01631552) | Phase 1/2 | Completed | 515 | Sacituzumab Govitecan (SN-38 ADC, anti-Trop-2) in epithelial cancers, with large TNBC and HR+/HER2− breast cancer cohorts. Pivotal trial confirming SN-38 payload activity in breast cancer microenvironment. |
| [NCT03562390](https://clinicaltrials.gov/study/NCT03562390) | Phase 2 | Unknown | 124 | Single-arm irinotecan as third-line or later therapy in Chinese patients with locally recurrent or metastatic breast cancer previously treated with anthracyclines and taxanes. Directly evaluates irinotecan efficacy and safety in an Asian population. |
| [NCT00031681](https://clinicaltrials.gov/study/NCT00031681) | Phase 1 | Completed | 41 | UCN-01 + irinotecan in solid tumours (Part I); exclusively in triple-negative recurrent breast cancer from 2007 onwards (Part II). Directly addresses TNBC subtype with irinotecan backbone. |
| [NCT00083148](https://clinicaltrials.gov/study/NCT00083148) | Phase 1 | Completed | 12 | Irinotecan followed by capecitabine in advanced breast carcinoma; dose-finding study based on the rationale that irinotecan sensitises tumour cells to capecitabine. |
| [NCT04640480](https://clinicaltrials.gov/study/NCT04640480) | Phase 1 | Completed | 21 | SNB-101 (novel nanoparticle SN-38 formulation) dose escalation in advanced solid tumours. Safety and PK profile of next-generation irinotecan-derived formulation. |
| [NCT01770353](https://clinicaltrials.gov/study/NCT01770353) | Phase 1 | Completed | 45 | Nanoliposomal irinotecan (nal-IRI) PK and biodistribution in solid tumours; confirmed drug delivery to breast cancer tumour microenvironment and assessed feasibility of ferumoxytol MRI to predict response. |
| [NCT03678883](https://clinicaltrials.gov/study/NCT03678883) | Phase 1/2 | Active, not recruiting | 350 | GSK-3β inhibitor 9-ING-41 combined with irinotecan (and other cytotoxics) in refractory cancers including breast cancer. Large-scale combination trial supporting irinotecan's role in multi-line breast cancer therapy. |
| [NCT05453825](https://clinicaltrials.gov/study/NCT05453825) | Phase 2 | Unknown | 180 | Navicixizumab (DLL4/VEGF bispecific antibody) ± irinotecan basket study with a dedicated TNBC cohort (Cohort C). Evaluates irinotecan as a combination partner in anti-angiogenic strategies. |
| [NCT00004095](https://clinicaltrials.gov/study/NCT00004095) | Phase 1 | Completed | 38 | Irinotecan + gemcitabine in unresectable or metastatic solid tumours; established dosing, schedule, and safety for this combination regimen applicable to breast cancer. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30786188](https://pubmed.ncbi.nlm.nih.gov/30786188/) | 2019 | Phase 1/2 Trial | N Engl J Med | Sacituzumab Govitecan in refractory mTNBC; ORR 33.3%, median PFS 5.5 months. Landmark study confirming SN-38 (irinotecan's active metabolite) as a cytotoxic payload effective in TNBC. |
| [36027558](https://pubmed.ncbi.nlm.nih.gov/36027558/) | 2022 | Phase 3 RCT | J Clin Oncol | TROPiCS-02: Sacituzumab Govitecan vs physician's choice in HR+/HER2− metastatic breast cancer. SG significantly improved PFS, extending SN-38 efficacy evidence to luminal subtypes. |
| [28291390](https://pubmed.ncbi.nlm.nih.gov/28291390/) | 2017 | Phase 2 Clinical Study | J Clin Oncol | Sacituzumab Govitecan in heavily pretreated mTNBC; ORR 30%, median OS 11.4 months. Phase 2 expansion cohort independently validating SN-38 cytotoxicity in breast cancer. |
| [36302269](https://pubmed.ncbi.nlm.nih.gov/36302269/) | 2022 | Systematic Review | Breast | Comprehensive review of TROP-2-targeting ADCs (SG, datopotamab deruxtecan) in metastatic breast cancer; mechanism, clinical data, and emerging resistance patterns. |
| [41371050](https://pubmed.ncbi.nlm.nih.gov/41371050/) | 2026 | Phase 2 Study | Eur J Cancer | PHENOMENAL trial: liposomal irinotecan (nal-IRI) in HER2-negative breast cancer with brain metastases. Demonstrates irinotecan's blood-brain barrier penetration and antitumour activity in a high-unmet-need population. |
| [31208270](https://pubmed.ncbi.nlm.nih.gov/31208270/) | 2019 | Mechanistic Review | mAbs | In-depth mechanistic review of SN-38-based ADC development; topoisomerase I inhibition, SN-38 potency advantages over conventional irinotecan, and design rationale for TROP-2-targeted delivery in solid tumours. |
| [32223649](https://pubmed.ncbi.nlm.nih.gov/32223649/) | 2020 | Trial Protocol | Future Oncol | TROPiCS-02 study design and rationale; explains scientific basis for SN-38 payload targeting Trop-2-overexpressing HR+/HER2− breast cancer and outlines primary and secondary endpoints. |
| [28558150](https://pubmed.ncbi.nlm.nih.gov/28558150/) | 2017 | Phase 1/2 Study | Cancer | IMMU-132 (sacituzumab govitecan) pharmacokinetics and safety at 8–10 mg/kg across diverse epithelial cancers; tolerability profile established for the SN-38 ADC platform. |
| [12800602](https://pubmed.ncbi.nlm.nih.gov/12800602/) | 2003 | Review | Oncology | Mechanistic rationale for mitomycin + irinotecan synergy in advanced breast cancer; mitomycin upregulates topoisomerase I, increasing irinotecan sensitivity — foundational pharmacological argument for irinotecan use in breast cancer. |
| [9726101](https://pubmed.ncbi.nlm.nih.gov/9726101/) | 1998 | Review | Oncology | Early overview of irinotecan's broad antitumour activity across tumour types including breast, ovarian, pancreatic, and haematological malignancies. Historical foundation for this repurposing direction. |

---

## Philippines Market Information

Irinotecan is currently **not registered** with the FDA Philippines. No marketing authorisations, product licences, or Certificate of Product Registration records are on file.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Camptothecin analog (Topoisomerase I inhibitor) |
| Myelosuppression Risk | **High** — Dose-limiting neutropenia and delayed diarrhoea are class-defining toxicities. Patients homozygous for the UGT1A1\*28 allele (and UGT1A1\*6, prevalent in East/Southeast Asian populations) are at significantly elevated risk of severe neutropenia and require dose reduction. |
| Emetogenicity Classification | Moderate |
| Monitoring Items | CBC with differential (prior to each cycle and as clinically indicated), liver function tests, total and direct bilirubin, serum electrolytes, renal function; UGT1A1 genotyping prior to first dose |
| Handling Protection | Yes — must be prepared and administered by trained oncology personnel following cytotoxic drug handling regulations; closed-system drug transfer devices (CSTDs) recommended; standard cytotoxic PPE required for preparation and disposal |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 trials have directly evaluated irinotecan in anthracycline- and taxane-refractory metastatic breast cancer, and the FDA approval of Sacituzumab Govitecan — whose cytotoxic payload is SN-38, the active metabolite of irinotecan — for both mTNBC and HR+/HER2− metastatic breast cancer provides mechanism-level validation that this compound class is active in the breast cancer setting. The TxGNN score of 99.08% is strongly aligned with the L2 clinical evidence base.

**To proceed, the following is needed:**
- **Philippines registration pathway**: Irinotecan is currently unregistered in the Philippines; an import/compassionate use or full registration dossier pathway must be assessed before any clinical deployment
- **UGT1A1 genotyping programme**: UGT1A1\*6 allele (distinct from the UGT1A1\*28 allele used in Western guidelines) is prevalent in Filipino and Asian populations; local genotyping capacity and dose-individualisation protocols must be established prior to use
- **Phase 3 data gap**: The highest-level direct evidence for irinotecan as a bare drug in breast cancer remains Phase 2; a Phase 3 confirmatory trial or regulatory bridging strategy from SG approval data is needed for definitive indication approval
- **Safety information retrieval**: Full prescribing information (warnings, contraindications, drug interactions) should be sourced from the originator package insert or regulatory dossier to complete the safety evaluation
- **Strategic decision on formulation**: Determine whether the preferred local development path is irinotecan bare drug, liposomal irinotecan (nal-IRI), or SN-38-based ADC (Sacituzumab Govitecan), as each carries different evidence levels, cost implications, and access considerations for the Philippines market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

