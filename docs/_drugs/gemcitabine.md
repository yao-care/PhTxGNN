---
layout: default
title: Gemcitabine
parent: 僅模型預測 (L5)
nav_order: 159
evidence_level: L5
indication_count: 10
---

# Gemcitabine
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

# Gemcitabine: From Pancreatic Cancer to Female Breast Carcinoma

## One-Sentence Summary

Gemcitabine is a cytotoxic nucleoside analog originally developed and widely used for the treatment of pancreatic cancer and other solid tumors. The TxGNN model predicts it may be effective for **Female Breast Carcinoma**, with **50 clinical trials** and **20 publications** currently supporting this direction. Notably, gemcitabine in combination with paclitaxel has already received US FDA approval for metastatic breast cancer, strongly validating this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pancreatic cancer, non-small cell lung cancer, bladder cancer (no Philippines registration data available) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Gemcitabine (2',2'-difluorodeoxycytidine) is a pyrimidine nucleoside antimetabolite that inhibits DNA synthesis by incorporating into the growing DNA strand and causing chain termination. It also inhibits ribonucleotide reductase, depleting intracellular deoxynucleotide pools needed for DNA replication. These mechanisms make it broadly effective against rapidly dividing cells, including breast cancer cells.

The mechanistic rationale for using gemcitabine in breast cancer is well-established. When combined with taxanes (paclitaxel or docetaxel), gemcitabine produces a synergistic dual cytotoxic effect: gemcitabine inhibits DNA repair pathways while taxanes disrupt microtubule function, preventing mitotic division. This non-overlapping mechanism and partially non-overlapping toxicity profile make the combination particularly attractive. The landmark Phase III trial (NCT00006459) demonstrated that gemcitabine plus paclitaxel significantly improved both overall survival and progression-free survival compared with paclitaxel alone in metastatic breast cancer.

The TxGNN prediction score of 99.98% is exceptionally high and is corroborated by the fact that gemcitabine has already received US FDA approval for metastatic breast cancer in combination with paclitaxel (approved 2004). This represents a case where the model's prediction has been independently validated by regulatory approval in another jurisdiction, although the drug is not yet registered in the Philippines for any indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00006459](https://clinicaltrials.gov/study/NCT00006459) | Phase 3 | Completed | N/A | Gemcitabine + Paclitaxel vs Paclitaxel alone in unresectable/metastatic breast cancer. Pivotal trial leading to FDA approval. |
| [NCT00039546](https://clinicaltrials.gov/study/NCT00039546) | Phase 3 | Unknown | N/A | tAnGo trial: evaluating addition of gemcitabine to paclitaxel-containing epirubicin-based adjuvant chemotherapy in ER/PgR-poor early breast cancer. |
| [NCT00561119](https://clinicaltrials.gov/study/NCT00561119) | Phase 3 | Completed | 326 | Maintenance vs observation after 6 cycles of gemcitabine + paclitaxel (GP) as first-line chemotherapy for metastatic/recurrent breast cancer. |
| [NCT00408408](https://clinicaltrials.gov/study/NCT00408408) | Phase 3 | Unknown | 1206 | Neoadjuvant trial evaluating capecitabine or gemcitabine added to docetaxel before AC ± bevacizumab, measuring pathologic complete response (pCR). |
| [NCT00070278](https://clinicaltrials.gov/study/NCT00070278) | Phase 3 | Unknown | 800 | Neoadjuvant sequential EC → Paclitaxel ± Gemcitabine in poor-risk early breast cancer. |
| [NCT00440622](https://clinicaltrials.gov/study/NCT00440622) | Phase 3 | Terminated | 90 | Gemcitabine + Herceptin vs Capecitabine + Herceptin in pretreated HER2+ metastatic breast cancer. |
| [NCT00003540](https://clinicaltrials.gov/study/NCT00003540) | Phase 2 | Completed | 30 | Gemcitabine monotherapy in metastatic breast cancer previously treated with adriamycin and taxol. |
| [NCT00110084](https://clinicaltrials.gov/study/NCT00110084) | Phase 2 | Completed | 50 | Nab-paclitaxel (Abraxane) + gemcitabine in metastatic breast cancer. |
| [NCT02252887](https://clinicaltrials.gov/study/NCT02252887) | Phase 2 | Completed | 45 | Gemcitabine + trastuzumab + pertuzumab in metastatic HER2+ breast cancer after prior pertuzumab-based therapy. |
| [NCT06027268](https://clinicaltrials.gov/study/NCT06027268) | Phase 2 | Active, not recruiting | 36 | Trilaciclib + pembrolizumab + gemcitabine + carboplatin in locally advanced/metastatic triple-negative breast cancer (TNBC). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24175966](https://pubmed.ncbi.nlm.nih.gov/24175966/) | 2014 | Clinical Study | Asia-Pac J Clin Oncol | Phase 3 trial (n=529): gemcitabine-paclitaxel significantly improved OS and PFS vs paclitaxel monotherapy; consistent efficacy between East Asian and global populations. |
| [14754468](https://pubmed.ncbi.nlm.nih.gov/14754468/) | 2004 | Clinical Study | Clin Breast Cancer | Gemcitabine + platinum combinations in patients pretreated with anthracyclines/taxanes; demonstrated non-cross-resistant activity with favorable toxicity profile. |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase I Trial | Breast Cancer Res Treat | Phase I trial of carboplatin + gemcitabine + mifepristone for advanced breast cancer; GR antagonism may enhance chemotherapy-induced apoptosis in GR+ tumors. |
| [12138397](https://pubmed.ncbi.nlm.nih.gov/12138397/) | 2002 | Review | Semin Oncol | Comprehensive review: gemcitabine single-agent ORR 16-37%; in combinations with platinum/taxanes/vinorelbine, ORR up to 68%. |
| [14768404](https://pubmed.ncbi.nlm.nih.gov/14768404/) | 2003 | Review | Oncology | Review of gemcitabine + anthracycline + taxane combinations in advanced breast cancer; favorable activity with manageable toxicity. |
| [15685819](https://pubmed.ncbi.nlm.nih.gov/15685819/) | 2004 | Review | Oncology | Review of gemcitabine + paclitaxel Phase II/III data: 52% ORR (114/221 patients) with established dosing schedules. |
| [15685821](https://pubmed.ncbi.nlm.nih.gov/15685821/) | 2004 | Review | Oncology | Review of gemcitabine + platinum-based chemotherapy in metastatic breast cancer after anthracycline/taxane failure. |
| [12057038](https://pubmed.ncbi.nlm.nih.gov/12057038/) | 2002 | Review | Clin Breast Cancer | Overview of gemcitabine single-agent therapy: unique MOA involving DNA chain termination and self-potentiation via masked chain termination. |
| [38262235](https://pubmed.ncbi.nlm.nih.gov/38262235/) | 2024 | Phase I Study | Gynecol Oncol | MIRV + gemcitabine in FRα+ cancers including TNBC; established MTD and RP2D for the combination. |
| [26372358](https://pubmed.ncbi.nlm.nih.gov/26372358/) | 2016 | Translational | Mol Oncol | Machine learning-derived genomic signatures predicting paclitaxel and gemcitabine resistance in breast cancer; potential for precision medicine. |

---

## Philippines Market Information

Gemcitabine is currently **not registered** in the Philippines. There are no active marketing authorizations on record.

| Item | Status |
|------|------|
| Market Status | Not marketed |
| Total Registrations | 0 |
| Available Dosage Forms | None registered |

---

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic (Antimetabolite — Nucleoside analog / Pyrimidine antagonist) |
| Myelosuppression Risk | High (dose-limiting toxicity; neutropenia, thrombocytopenia, and anemia are common and dose-dependent) |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (weekly during treatment), liver function tests (AST, ALT, bilirubin), renal function (BUN, creatinine), pulmonary function (risk of pneumonitis) |
| Handling Protection | Must follow cytotoxic drug handling regulations; use PPE including gloves, gown, and eye protection during preparation and administration |

---

## Safety Considerations

> Please refer to the package insert for safety information. Local regulatory safety data (package insert warnings, contraindications, and drug-drug interactions) were not available at the time of this evaluation.

**Known general safety concerns for gemcitabine (from international references):**
- **Myelosuppression**: Dose-limiting; requires regular hematologic monitoring
- **Hepatotoxicity**: Transient elevations in transaminases are common; rarely hepatic veno-occlusive disease
- **Pulmonary toxicity**: Dyspnea and interstitial pneumonitis have been reported; discontinue if unexplained dyspnea occurs
- **Hemolytic uremic syndrome (HUS)**: Rare but serious; discontinue permanently if HUS occurs
- **Capillary leak syndrome**: Rare; reported in combination settings

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Gemcitabine's efficacy in breast cancer is supported by the highest level of clinical evidence (L1), including multiple completed Phase III randomized controlled trials. The combination of gemcitabine and paclitaxel has already received US FDA approval for metastatic breast cancer (2004), and the TxGNN prediction score of 99.98% is fully validated by existing clinical data. The primary barrier is the absence of Philippines market registration.

**To proceed, the following is needed:**
- Obtain Philippines FDA registration data or pursue local marketing authorization
- Acquire detailed package insert for safety assessment (key warnings, contraindications, DDI profile)
- Confirm detailed mechanism of action (MOA) documentation from DrugBank
- Establish local safety monitoring protocol aligned with myelosuppression risk management
- Evaluate route compatibility and available dosage forms for Philippines healthcare infrastructure
- Develop prescribing guidelines appropriate for the local population, including dose adjustments for hepatic/renal impairment

---

*Disclaimer: This report is for research purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before clinical application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

