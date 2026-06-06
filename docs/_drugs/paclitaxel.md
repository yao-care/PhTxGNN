---
layout: default
title: Paclitaxel
parent: 僅模型預測 (L5)
nav_order: 266
evidence_level: L5
indication_count: 10
---

# Paclitaxel
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

# Paclitaxel: From Established Global Anticancer Therapy to Female Breast Carcinoma

## One-Sentence Summary

Paclitaxel is a taxane-class cytotoxic agent and one of the most widely used anticancer drugs in the world, serving as a cornerstone chemotherapy backbone across multiple solid tumor indications globally.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma** with a prediction score of **99.995%**,
supported by **multiple completed Phase 3 RCTs** and over **20 clinical publications** directly evaluating paclitaxel in breast cancer across all major subtypes.
Paclitaxel currently has no registered product in the Philippines, making this evaluation relevant to potential market introduction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | No Philippines registration; globally established for ovarian cancer, breast cancer, NSCLC, and Kaposi's sarcoma |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.995% |
| Evidence Level | L1 |
| Philippines Market Status | 未上市 (Not Marketed) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Philippine regulatory data source. Based on known pharmacological information, paclitaxel is a diterpene alkaloid derived from *Taxus* tree species that exerts antitumor activity by **stabilizing polymerized microtubules** against depolymerization. By binding to the β-tubulin subunit of the microtubule, it prevents spindle disassembly during mitosis, arresting cancer cells in the G2/M phase of the cell cycle and ultimately triggering programmed cell death (apoptosis). Additionally, paclitaxel activates tumor-associated macrophages via the TLR4 signaling pathway, which enhances antitumor immune responses—a mechanism that synergizes with emerging checkpoint inhibitor combinations such as atezolizumab and pembrolizumab.

Female breast carcinoma, particularly subtypes with high proliferative indices (elevated Ki67), shows heightened sensitivity to microtubule-targeting agents. Because paclitaxel's mechanism is **receptor-independent**—acting directly on the mitotic machinery rather than through hormone or growth factor receptors—it is active across all major breast cancer subtypes: HER2-positive tumors (combined with trastuzumab/pertuzumab), triple-negative breast cancer (TNBC, the subtype with the fewest targeted options), and hormone receptor-positive tumors where endocrine therapy alone is insufficient for high-risk disease.

Paclitaxel's application in breast cancer is not merely modeled but **globally established**. The landmark CALGB 9344 trial (n=3,677) defined paclitaxel as a cornerstone adjuvant agent in node-positive breast cancer. Subsequent Phase 3 studies—Neo ALTTO, GeparOcto, KEYNOTE-756, and IMpassion130—have refined its role across neoadjuvant, adjuvant, and metastatic settings, including combinations with targeted agents and immunotherapy. The TxGNN score of 99.995% essentially validates this clinical reality, demonstrating the model's ability to capture established pharmacological relationships within its knowledge graph.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00991263](https://clinicaltrials.gov/study/NCT00991263) | N/A | Completed | 3,677 | CALGB 9344 large-scale biomarker extension: evaluated intrinsic breast cancer subtypes and differential paclitaxel benefit in adjuvant setting; identified molecular predictors of response—foundational Phase 3 evidence |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | Adjuvant AC→weekly paclitaxel ± trastuzumab in HER2-low invasive breast cancer; directly evaluates paclitaxel-containing regimen efficacy and survival outcomes |
| [NCT00003088](https://clinicaltrials.gov/study/NCT00003088) | Phase 3 | Completed | 2,005 | Randomized comparison of sequential doxorubicin/paclitaxel/cyclophosphamide vs. concurrent AC→paclitaxel at 14 or 21-day intervals in node-positive Stage II/IIIA breast cancer; established dose-dense scheduling |
| [NCT00433420](https://clinicaltrials.gov/study/NCT00433420) | Phase 3 | Active, Not Recruiting | 2,000 | EC vs. FEC followed by paclitaxel every 3 or 2 weeks with pegfilgrastim in node-positive breast cancer; provides head-to-head regimen and dose-density comparison data |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: compared two dose-intensified neoadjuvant regimens including weekly paclitaxel/liposomal doxorubicin backbone in high-risk early breast cancer |
| [NCT00553358](https://clinicaltrials.gov/study/NCT00553358) | Phase 3 | Completed | 455 | Neo ALTTO: lapatinib, trastuzumab, or both combined with paclitaxel as neoadjuvant therapy in HER2-positive breast cancer; established paclitaxel+dual HER2-blockade as standard backbone |
| [NCT01901146](https://clinicaltrials.gov/study/NCT01901146) | Phase 3 | Completed | 725 | Randomized double-blind comparison of ABP 980 (trastuzumab biosimilar) vs. trastuzumab in HER2-positive early breast cancer using paclitaxel-containing chemotherapy as backbone |
| [NCT07327021](https://clinicaltrials.gov/study/NCT07327021) | Phase 2 | Recruiting | 54 | NOGA: MRI-guided neoadjuvant de-escalation in Stage II–III TNBC with paclitaxel standard arm; evaluates whether response-guided treatment reduction is feasible without compromising outcomes |
| [NCT00709761](https://clinicaltrials.gov/study/NCT00709761) | Phase 2 | Completed | 60 | Weekly nab-paclitaxel plus lapatinib in first/second-line HER2-overexpressing metastatic breast cancer; established clinical activity and tolerability profile of nab-paclitaxel in HER2+ MBC |
| [NCT01131195](https://clinicaltrials.gov/study/NCT01131195) | Phase 3 | Completed | 139 | Bevacizumab + paclitaxel vs. bevacizumab + metronomic cyclophosphamide/capecitabine as first-line therapy in HER2-negative metastatic breast cancer; confirmed paclitaxel+bevacizumab as an active reference arm |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11147586](https://pubmed.ncbi.nlm.nih.gov/11147586/) | 2000 | Phase 2 Clinical Trial | Cancer | Phase II multicenter trial of doxorubicin + paclitaxel combination in metastatic breast carcinoma; assessed response rates and toxicity with attention to prior adjuvant anthracycline exposure |
| [32461977](https://pubmed.ncbi.nlm.nih.gov/32461977/) | 2020 | Phase 2 Cohort | BioMed Research International | Real-world study of epirubicin/cyclophosphamide followed by weekly paclitaxel + trastuzumab as neoadjuvant chemotherapy in HER2-positive breast carcinoma; evaluated pathological complete response rates |
| [9164198](https://pubmed.ncbi.nlm.nih.gov/9164198/) | 1997 | Phase 2 Clinical Trial | J Clin Oncol | ECOG study of biweekly paclitaxel + cisplatin in advanced breast carcinoma; established activity of paclitaxel combination regimens in the metastatic setting |
| [31783552](https://pubmed.ncbi.nlm.nih.gov/31783552/) | 2019 | Review | Biomolecules | Comprehensive review of paclitaxel's mechanistic and clinical effects in breast cancer, covering first-line treatment evidence, resistance mechanisms, and biomarker-guided therapy strategies |
| [39317691](https://pubmed.ncbi.nlm.nih.gov/39317691/) | 2024 | Review | Chemical Biology & Drug Design | Analysis of paclitaxel combination strategies in breast carcinoma and identification of in vivo biomarkers; addresses synergistic drug pairings to overcome acquired resistance |
| [24823476](https://pubmed.ncbi.nlm.nih.gov/24823476/) | 2014 | Genomic Cohort | Nature Communications | Exome sequencing identified TEKT4 germline variations (~10% of breast cancer patients) that enrich in post-treatment tumors and predict paclitaxel resistance through disrupted microtubule stabilization |
| [9282422](https://pubmed.ncbi.nlm.nih.gov/9282422/) | 1997 | Review | Drug and Therapeutics Bulletin | Early regulatory review confirming extended licensure of paclitaxel for metastatic breast carcinoma; established first-line taxane therapy in combination with cisplatin |
| [11745249](https://pubmed.ncbi.nlm.nih.gov/11745249/) | 2001 | Clinical Study | Cancer | Paclitaxel in multimodality treatment for inflammatory breast carcinoma; demonstrated significant clinical activity in this aggressive, locally advanced breast cancer subtype |
| [24068539](https://pubmed.ncbi.nlm.nih.gov/24068539/) | 2013 | Phase I-II | Breast Cancer Research and Treatment | Tipifarnib + sequential weekly paclitaxel and dose-dense AC in HER2-negative locally advanced breast cancer; demonstrated paclitaxel's synergistic role in combination neoadjuvant regimens |
| [39471010](https://pubmed.ncbi.nlm.nih.gov/39471010/) | 2024 | Molecular Docking | Asian Pacific J Cancer Prev | Molecular docking and pharmacokinetic profiling of nab-paclitaxel in HER2-positive breast cancer; confirmed favorable binding affinity and ADMET profile supporting continued clinical development |

---

## Philippines Market Information

Paclitaxel currently has **no registered products with the FDA Philippines** and is classified as **未上市 (Not Marketed)**. The drug is approved internationally by multiple major regulatory agencies:

- **FDA USA**: Approved for metastatic breast cancer, ovarian cancer, NSCLC, AIDS-related Kaposi's sarcoma
- **EMA**: Approved for breast cancer, ovarian cancer, NSCLC, pancreatic cancer (nab-paclitaxel)
- **TFDA (Taiwan)**: Approved for breast cancer, gastric cancer, ovarian cancer, NSCLC

For clinical use in the Philippines, registration through the FDA Philippines or a compassionate/expanded use authorization would be required prior to procurement and administration.

---

## Cytotoxicity

Paclitaxel is a conventional cytotoxic antineoplastic agent (taxane class) and meets criteria for inclusion of this section.

| Item | Content |
|------|------|
| Cytotoxicity Classification | Conventional cytotoxic — Taxane class (microtubule-stabilizing agent) |
| Myelosuppression Risk | High — neutropenia is the primary dose-limiting toxicity; febrile neutropenia occurs in approximately 10–20% of patients with standard q3-week dosing; weekly paclitaxel has a more favorable hematologic profile |
| Emetogenicity Classification | Low to moderate (significantly lower than platinum-based regimens; standard antiemetic prophylaxis typically sufficient) |
| Monitoring Items | Complete blood count (CBC with differential) before each cycle; liver function tests; renal function; peripheral neurological assessment (CIPN scoring tool, e.g., NCI CTCAE); cardiac function monitoring (especially when combined with anthracyclines or trastuzumab) |
| Handling Protection | Must follow cytotoxic drug handling regulations; requires closed-system drug transfer devices (CSTD), appropriate PPE (double gloves, disposable gown, eye protection), and dedicated negative-pressure preparation facilities |

---

## Safety Considerations

Please refer to the package insert for safety information. Formal warnings and contraindications data were not available in the current Evidence Pack (FDA Philippines package insert has not been retrieved). Based on published literature and international regulatory documentation, the following safety signals are clinically significant:

- **Peripheral neuropathy**: Cumulative, dose-dependent chemotherapy-induced peripheral neuropathy (CIPN) is the major non-hematologic dose-limiting toxicity; patients should be screened at each cycle
- **Hypersensitivity reactions**: The Cremophor EL vehicle in conventional paclitaxel formulations carries significant hypersensitivity risk; standard premedication with corticosteroids, H1, and H2 blockers is mandatory; nab-paclitaxel (albumin-bound) formulation substantially reduces this risk
- **Cardiotoxicity**: Subclinical cardiac dysfunction has been documented with taxane-based chemotherapy, particularly in combination with anthracyclines; cardiac monitoring is recommended in long-term follow-up

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Paclitaxel carries Level 1 evidence for female breast carcinoma treatment, validated by multiple landmark Phase 3 RCTs (CALGB 9344, Neo ALTTO, GeparOcto) and decades of global clinical practice. The TxGNN prediction score of 99.995% correctly reflects this established pharmacological reality. The primary barrier in the Philippines is not evidence uncertainty but regulatory registration and clinical infrastructure readiness.

**To proceed, the following is needed:**
- Initiate FDA Philippines product registration application (New Drug Application) or apply for a Special Access Program / compassionate use authorization for urgent oncology need
- Obtain and review complete package insert from TFDA, FDA USA, or EMA for full safety profile (contraindications, DDI, reproductive toxicity)
- Develop a local pharmacovigilance plan covering CIPN monitoring protocols, myelosuppression management guidelines, and hypersensitivity reaction emergency procedures
- Assess cold-chain logistics and cytotoxic drug preparation infrastructure at designated oncology treatment centers
- Conduct health technology assessment (HTA) for cost-effectiveness in the Philippine healthcare context, including comparison with available alternatives
- Define approved oncology center network with trained personnel and cytotoxic handling compliance prior to initial rollout
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

