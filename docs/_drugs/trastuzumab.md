---
layout: default
title: Trastuzumab
parent: 僅模型預測 (L5)
nav_order: 340
evidence_level: L5
indication_count: 10
---

# Trastuzumab
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

# Trastuzumab: From HER2-Positive Breast Cancer to Progesterone Receptor-Positive Breast Cancer

## One-Sentence Summary

Trastuzumab (Herceptin) is an internationally established humanized monoclonal antibody targeting HER2, approved for the treatment of HER2-overexpressing breast cancer and gastric/gastroesophageal junction cancer across multiple major regulatory jurisdictions.
The TxGNN model predicts it may be specifically effective for **Progesterone Receptor-Positive (PR+) Breast Cancer**,
with **36 registered clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HER2-positive breast cancer; HER2-positive gastric/gastroesophageal junction cancer (international approval; not registered in the Philippines) |
| Predicted New Indication | Progesterone Receptor-Positive Breast Cancer |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L1 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Trastuzumab is a humanized IgG1 monoclonal antibody that targets extracellular domain IV of HER2 (ErbB2), blocking HER2-HER3 dimerization and suppressing downstream PI3K/AKT proliferative signaling. In parallel, trastuzumab recruits natural killer cells via its Fc region to trigger antibody-dependent cell-mediated cytotoxicity (ADCC), directly eliminating HER2-overexpressing tumor cells through immune engagement.

Among PR-positive breast cancers, approximately 15–20% co-overexpress HER2, forming what is clinically recognized as the HR+/HER2+ or "triple-positive" molecular subtype (ER+/PR+/HER2+). This subtype poses a unique biological challenge: HER2 activation can transcriptionally suppress PR expression through phosphorylation of ER-coactivators, while residual PR and ER signaling may attenuate HER2-targeted therapy sensitivity by sustaining alternative survival pathways. A 2024 preclinical study (PMID 38034484) directly demonstrated that the combination of progesterone and estradiol reverses trastuzumab's inhibitory effect on BT474 triple-positive breast cancer cells, mechanistically explaining why this subtype requires tailored co-targeting strategies.

The TxGNN prediction is further supported by established clinical trial data. The Phase II trial NCT00134680 enrolled patients with ErbB2+/PR+/ER+ metastatic breast cancer receiving letrozole plus trastuzumab — precisely the target population described here — and demonstrated clinical activity. The Phase III RCT NCT01275677 (n=3,270) enrolled node-positive HER2+ patients, a substantial fraction of whom were PR+, providing direct population-level evidence. The WSG-TP-II trial additionally compared endocrine therapy combined with trastuzumab and pertuzumab against de-escalated chemotherapy specifically in the HR+/HER2+ early breast cancer setting, further validating the mechanistic convergence of HER2 blockade and hormone receptor modulation in PR+ disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00134680](https://clinicaltrials.gov/study/NCT00134680) | Phase 2 | Completed | 33 | Letrozole 2.5 mg/day + trastuzumab weekly in ErbB2+/PR+/ER+ metastatic BC — the most directly targeted trial for this indication; evaluated the anti-tumor efficacy and tolerability of combining HER2 blockade with aromatase inhibition in the exact PR+/HER2+ population |
| [NCT01275677](https://clinicaltrials.gov/study/NCT01275677) | Phase 3 | Completed | 3,270 | Large RCT of adjuvant chemotherapy alone vs. chemotherapy + trastuzumab in node-positive or high-risk HER2-low/HER2+ invasive BC; encompasses PR+ subpopulation and establishes trastuzumab's adjuvant benefit in HER2-overexpressing disease |
| [NCT00005970](https://clinicaltrials.gov/study/NCT00005970) | Phase 3 | Completed | 3,436 | AC followed by weekly paclitaxel with or without trastuzumab as adjuvant treatment in HER2-overexpressing breast cancer; landmark trial demonstrating OS and DFS benefit of trastuzumab in the HER2+ population, including HR+ subgroups |
| [NCT00667251](https://clinicaltrials.gov/study/NCT00667251) | Phase 3 | Completed | 652 | Taxane-based chemotherapy plus lapatinib vs. taxane plus trastuzumab as first-line therapy in HER2+ metastatic BC; directly compared two HER2-targeted strategies and defined trastuzumab as the preferred HER2 agent in this setting |
| [NCT04629846](https://clinicaltrials.gov/study/NCT04629846) | Phase 3 | Completed | 517 | Pertuzumab biosimilar QL1209 vs. reference pertuzumab, each combined with trastuzumab + docetaxel in HER2+ early or locally advanced BC; validates trastuzumab efficacy consistency as backbone therapy |
| [NCT03726879](https://clinicaltrials.gov/study/NCT03726879) | Phase 3 | Completed | 454 | IMpassion050: atezolizumab or placebo combined with neoadjuvant AC followed by paclitaxel + trastuzumab + pertuzumab in early HER2+ BC; assessed whether immune checkpoint inhibition adds benefit to the HER2-blockade backbone |
| [NCT04886531](https://clinicaltrials.gov/study/NCT04886531) | Phase 2 | Recruiting | 30 | Neratinib + aromatase inhibitor + trastuzumab for 24 weeks as neoadjuvant therapy in ER+/HER2+ cancer; chemotherapy-free approach combining HER2 and endocrine co-targeting, directly relevant to the PR+ context |
| [NCT02152943](https://clinicaltrials.gov/study/NCT02152943) | Phase 1 | Completed | 37 | Everolimus + letrozole + trastuzumab in HR+/HER2+ advanced BC or other solid tumors; explored triple-pathway inhibition (mTOR + ER + HER2) to overcome resistance mechanisms prevalent in PR+/HER2+ disease |
| [NCT04334330](https://clinicaltrials.gov/study/NCT04334330) | Phase 2 | Unknown | 34 | Palbociclib + trastuzumab + pyrotinib + fulvestrant in ER/PR+/HER2+ BC with brain metastases; evaluates quadruple-targeted approach for the PR+/HER2+ subtype in a CNS disease setting |
| [NCT01785420](https://clinicaltrials.gov/study/NCT01785420) | Phase 3 | Recruiting | 1,100 | Double-blind RCT of short-duration preoperative trastuzumab vs. placebo in HER2/erbB2-positive operable BC; explores early biological effects of trastuzumab including immune activation (ADCC) prior to definitive surgery |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [31410192](https://pubmed.ncbi.nlm.nih.gov/31410192/) | 2019 | Translational Cohort | Theranostics | Multi-omics landscape analysis (n=32,056 SEER + 4 clinical cohorts) of ER+/PR+/HER2+ triple-positive breast cancer; characterized trastuzumab responsiveness and molecular features unique to this subtype — most directly relevant paper for this repurposing prediction |
| [37166817](https://pubmed.ncbi.nlm.nih.gov/37166817/) | 2023 | RCT | JAMA Oncology | WSG-TP-II trial: prospective comparison of endocrine therapy + trastuzumab + pertuzumab vs. de-escalated chemotherapy as neoadjuvant treatment in HR+/HER2+ early BC; first prospective head-to-head evaluation of chemotherapy-free HER2 + endocrine strategy in PR+ disease |
| [32353342](https://pubmed.ncbi.nlm.nih.gov/32353342/) | 2020 | Phase 2 RCT | Lancet Oncology | monarcHER: abemaciclib + trastuzumab ± fulvestrant vs. standard chemotherapy + trastuzumab in HR+/HER2+ advanced BC; demonstrated superior PFS with CDK4/6 inhibition combined with trastuzumab-based endocrine therapy, supporting chemotherapy-free strategies in PR+ subtype |
| [34983437](https://pubmed.ncbi.nlm.nih.gov/34983437/) | 2022 | Retrospective | BMC Cancer | Single-center retrospective study of trastuzumab + fulvestrant combination in HR+/HER2+ advanced BC; provided real-world evidence for the anti-HER2 plus selective estrogen receptor degrader approach applicable to PR+ patients |
| [38034484](https://pubmed.ncbi.nlm.nih.gov/38034484/) | 2024 | Preclinical | Oncology Letters | Progesterone + estradiol combination reverses trastuzumab's anti-proliferative effect in BT474 triple-positive BC cells; mechanistic evidence for PR-HER2 pathway crosstalk and its implications for optimizing trastuzumab therapy in PR+ disease |
| [27179402](https://pubmed.ncbi.nlm.nih.gov/27179402/) | 2016 | Phase 2 RCT | Lancet Oncology | NeoSphere 5-year analysis: neoadjuvant pertuzumab + trastuzumab + docetaxel vs. controls in locally advanced or early HER2+ BC; 5-year PFS and DFS data confirming durability of dual HER2 blockade benefit |
| [26874901](https://pubmed.ncbi.nlm.nih.gov/26874901/) | 2016 | Phase 3 RCT | Lancet Oncology | ExteNET: 12 months of neratinib after trastuzumab-based adjuvant therapy in HER2+ early BC (n=2,840); HR+ subgroup derived greater benefit from extended HER2 blockade, underscoring the importance of PR/ER status in HER2-targeted therapy optimization |
| [40339592](https://pubmed.ncbi.nlm.nih.gov/40339592/) | 2025 | Phase 2a | Lancet Oncology | Zanidatamab (HER2 bispecific antibody) + palbociclib + fulvestrant in previously treated HR+/HER2+ metastatic BC; antitumor activity in PR+ subset provides contemporary proof-of-concept for combined HER2 + CDK4/6 + endocrine strategy |
| [35640077](https://pubmed.ncbi.nlm.nih.gov/35640077/) | 2022 | Guidelines | JCO | ASCO guideline update on systemic therapy for HER2+ advanced breast cancer; contextualizes trastuzumab's role across hormone receptor subgroups (including PR+) and provides evidence-based treatment sequencing recommendations |
| [28945833](https://pubmed.ncbi.nlm.nih.gov/28945833/) | 2017 | Phase 2 RCT | Annals of Oncology | WSG-ADAPT HER2+/HR- trial: 12 weeks of neoadjuvant dual blockade (trastuzumab + pertuzumab ± paclitaxel) with pCR as primary endpoint; provided molecular stratification insights distinguishing HR- from HR+ (including PR+) HER2+ subtype responses |

---

## Philippines Market Information

Trastuzumab currently has **no registered products** with the Philippine FDA. The drug has not been approved or marketed in the Philippines as of the data cutoff date.

For international reference, trastuzumab (originator product Herceptin®, Roche/Genentech) holds regulatory approval in:
- **USA (FDA)**: HER2-overexpressing breast cancer (adjuvant and metastatic); HER2-overexpressing metastatic gastric/GEJ adenocarcinoma
- **EU (EMA)**: Early and metastatic HER2+ breast cancer; HER2+ metastatic gastric cancer
- **Japan (PMDA)**: HER2+ breast cancer; HER2+ gastric cancer

Multiple biosimilar products (e.g., QL1701, HD201, SB3) have also received approvals in various jurisdictions, potentially offering a more accessible market entry pathway.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Humanized anti-HER2 IgG1 monoclonal antibody; not a conventional cytotoxic agent |
| Myelosuppression Risk | Low (trastuzumab monotherapy rarely causes significant myelosuppression; mild neutropenia reported when combined with cytotoxic chemotherapy) |
| Emetogenicity Classification | Low |
| Monitoring Items | Left ventricular ejection fraction (LVEF) before initiation and at regular intervals during treatment (cardiac toxicity is the primary concern); CBC with differential when combined with chemotherapy; liver and renal function |
| Handling Protection | Standard biologic/monoclonal antibody handling protocols; not classified as a hazardous cytotoxic drug by NIOSH; institutional policies for biologic agent preparation and administration apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** TFDA-approved prescribing information (or EMA/FDA SmPC) download is recommended to complete the baseline safety assessment for this candidate. Known class-level concerns include cardiotoxicity (symptomatic and asymptomatic LVEF decline), infusion-related reactions, and embryo-fetal toxicity; these should be reviewed before clinical application planning.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Trastuzumab already carries L1-level clinical evidence across multiple completed Phase III RCTs in HER2-positive breast cancer populations that encompass PR+ patients; dedicated studies in the HR+/HER2+ (triple-positive) molecular subtype directly validate both the biological rationale and clinical benefit of HER2 blockade in PR-expressing disease. The TxGNN score of 99.90% and independent mechanistic evidence of PR-HER2 pathway crosstalk together support advancing this prediction to a structured clinical evaluation.

**To proceed, the following is needed:**

- **Safety baseline**: Obtain TFDA, EMA, or FDA package insert/SmPC to fulfill drug-level safety screening (key warnings, contraindications, and teratogenicity data)
- **MOA documentation**: Complete DrugBank API query to formally capture trastuzumab mechanism of action for regulatory submission preparation
- **Philippines regulatory pathway**: Initiate FDA Philippines registration planning; consider biosimilar entry strategy given lower access barriers
- **Patient stratification algorithm**: Define HER2 IHC/FISH and PR testing protocol to identify the PR+/HER2+ target population
- **Cardiac monitoring protocol**: Establish LVEF baseline measurement and serial monitoring schedule before and during therapy
- **Combination strategy planning**: Define the optimal co-treatment framework — aromatase inhibitor, fulvestrant, pertuzumab, or CDK4/6 inhibitor — based on metastatic vs. early-stage setting
- **Drug interaction review**: Assess DDI profile when combined with endocrine agents and other targeted therapies planned for the PR+/HER2+ regimen
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

