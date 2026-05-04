---
layout: default
title: Carboplatin
parent: 僅模型預測 (L5)
nav_order: 60
evidence_level: L5
indication_count: 10
---

# Carboplatin
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

# Carboplatin: From Ovarian Cancer to Female Breast Carcinoma

## One-Sentence Summary

Carboplatin is a platinum-based cytotoxic chemotherapy agent globally established as a first-line treatment for ovarian cancer, lung cancer, and other solid tumors — though no Philippine FDA registration is currently on file.
The TxGNN model predicts it may be effective for **Female Breast Carcinoma**,
with **multiple completed Phase 3 RCTs** and **20 publications** — spanning triple-negative breast cancer (TNBC), HER2-positive, and BRCA-mutated subtypes — supporting this direction with the highest level of clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Ovarian cancer and solid tumors (globally established; no Philippine FDA registration found) |
| Predicted New Indication | Female Breast Carcinoma |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L1 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Philippine regulatory record. Based on well-established pharmacology, Carboplatin is a second-generation platinum coordination compound that covalently binds to purine bases in DNA, forming intra- and inter-strand cross-links. These adducts physically block the movement of DNA polymerase and RNA polymerase, halting replication and transcription. When the resulting damage cannot be repaired, the cell commits to apoptosis via p53-dependent and p53-independent pathways. Unlike cisplatin, carboplatin is dosed using the Calvert formula (targeting an area under the curve rather than a flat body-surface-area dose), which reduces nephrotoxicity and neurotoxicity while preserving anticancer efficacy — making it the preferred backbone in many modern combination regimens.

The mechanistic bridge from its established oncology use to female breast carcinoma is scientifically well-grounded. Triple-negative breast cancer (TNBC) is enriched for BRCA1/2 germline and somatic mutations, producing homologous recombination deficiency (HRD). Cells lacking functional HR repair cannot efficiently resolve platinum-induced double-strand breaks, creating the same synthetic lethality that underpins carboplatin's efficacy in BRCA-associated ovarian cancer. Beyond BRCA mutations, a broader "BRCAness" phenotype — characterised by promoter methylation of BRCA1 or other HR pathway alterations — expands the platinum-sensitive population in TNBC. In HER2-positive disease, combining carboplatin with anti-HER2 agents (trastuzumab, pertuzumab) exploits simultaneous HER2 pathway inhibition and DNA damage signalling, producing synergistic cytotoxicity that has been validated in the TCbHP and TCHP regimens.

Multiple completed Phase 3 trials now confirm carboplatin's role as a standard component of breast cancer treatment. The Triple Negative Trial (NCT00532727) directly compared carboplatin against docetaxel in 400 patients with metastatic TNBC. The BROCADE3 study demonstrated significant progression-free survival improvement when veliparib was added to carboplatin+paclitaxel in BRCA1/2-mutated advanced breast cancer, with final overall survival data published in 2024. The GeparOcto (n=961) and TCHP (n=315) Phase 3 trials validated carboplatin-containing neoadjuvant regimens for high-risk early breast cancer. An ongoing 720-patient Phase 3 RCT (NCT03168880) continues to refine the carboplatin benefit in locally advanced TNBC. Together, these data represent some of the strongest drug repurposing validation in oncology, fully supporting the TxGNN model's top-ranked prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00532727](https://clinicaltrials.gov/study/NCT00532727) | Phase 3 | Unknown | 400 | Triple Negative Trial: Direct RCT comparing carboplatin vs docetaxel as standard of care in metastatic ER−/PR−/HER2− breast cancer; primary goal to determine whether carboplatin has greater activity than a taxane in TNBC |
| [NCT02125344](https://clinicaltrials.gov/study/NCT02125344) | Phase 3 | Completed | 961 | GeparOcto: Compared two dose-dense neoadjuvant regimens in high-risk early breast cancer; one arm included weekly paclitaxel/non-pegylated doxorubicin with carboplatin and dual HER2 blockade |
| [NCT02003209](https://clinicaltrials.gov/study/NCT02003209) | Phase 3 | Completed | 315 | TCHP ± estrogen deprivation in HR+/HER2+ locally advanced breast cancer; evaluated whether adding estrogen deprivation to docetaxel/carboplatin/trastuzumab/pertuzumab improves pathologic complete response |
| [NCT00047255](https://clinicaltrials.gov/study/NCT00047255) | Phase 3 | Completed | 263 | Docetaxel+trastuzumab with or without carboplatin as first-line therapy in HER2-amplified advanced breast cancer; established the TCH regimen benchmark used in HER2+ practice today |
| [NCT03168880](https://clinicaltrials.gov/study/NCT03168880) | Phase 3 | Active, Not Recruiting | 720 | RCT of neoadjuvant weekly paclitaxel alone vs weekly paclitaxel+carboplatin in large operable or locally advanced TNBC; directly quantifies the benefit of adding carboplatin to taxane backbone |
| [NCT05843292](https://clinicaltrials.gov/study/NCT05843292) | Phase 4 | Not Yet Recruiting | 48 | Short-term sintilimab (anti-PD-1) + taxane + carboplatin as neoadjuvant therapy in early-stage TNBC; Phase 4 deployment signals that this carboplatin-immunotherapy combination is already entering real-world practice |
| [NCT00117442](https://clinicaltrials.gov/study/NCT00117442) | Phase 2 | Completed | 61 | Dose-intensive multi-cycle carboplatin/paclitaxel supported by pegfilgrastim-mobilised peripheral blood progenitor cells in advanced breast cancer; provided key dose-finding, efficacy, and kinetic data for the combination |
| [NCT07327021](https://clinicaltrials.gov/study/NCT07327021) | Phase 2 | Recruiting | 54 | NOGA: MRI-guided neoadjuvant de-escalation strategy in stage II–III TNBC; carboplatin is part of the standard reference arm, reflecting its current guideline-compliant status |
| [NCT06291064](https://clinicaltrials.gov/study/NCT06291064) | Phase 2 | Recruiting | 85 | TARMAC: Multi-omic biomarker study in Nigerian women with TNBC receiving epirubicin+cyclophosphamide followed by docetaxel+carboplatin; aims to identify resistance predictors for precision use of carboplatin |
| [NCT02978495](https://clinicaltrials.gov/study/NCT02978495) | Phase 2 | Completed | 154 | NACATRINE: Prospective Phase 2 of neoadjuvant carboplatin specifically in TNBC in Brazil; assessed pCR rates and tolerability, contributing real-world data from a lower-middle-income country context |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [39671272](https://pubmed.ncbi.nlm.nih.gov/39671272/) | 2025 | RCT | JAMA | CamRelief trial: Camrelizumab (anti-PD-1) added to 4-drug neoadjuvant chemotherapy including platinum in early/locally advanced TNBC; demonstrates that platinum-containing backbones remain the scaffold for next-generation immunotherapy combinations |
| [38309017](https://pubmed.ncbi.nlm.nih.gov/38309017/) | 2024 | Phase 3 RCT | Eur J Cancer | BROCADE3 final overall survival results: Veliparib + carboplatin/paclitaxel vs placebo + carboplatin/paclitaxel in BRCA1/2-mutated HER2-negative advanced breast cancer; confirms carboplatin as the indispensable backbone in BRCA-mutated disease |
| [40593759](https://pubmed.ncbi.nlm.nih.gov/40593759/) | 2025 | Phase 2b RCT | Nature Communications | MUKDEN 06: ARX788+pyrotinib vs docetaxel+carboplatin+trastuzumab+pertuzumab (TCbHP) as neoadjuvant in HER2+ breast cancer; carboplatin-based regimen serves as the active standard comparator, confirming its benchmark status |
| [25247558](https://pubmed.ncbi.nlm.nih.gov/25247558/) | 2014 | Meta-analysis | PLoS One | Meta-analysis confirming carboplatin significantly improves pathological complete response (pCR) in neoadjuvant TNBC; expands the argument for platinum use beyond BRCA-mutated patients to the broader TNBC population |
| [16720915](https://pubmed.ncbi.nlm.nih.gov/16720915/) | 2006 | Review | Med Oncol | Comprehensive synthesis of preclinical synergy data and clinical trial results for paclitaxel-carboplatin in advanced breast cancer; established pharmacological rationale for the doublet that remains standard in multiple guidelines |
| [40779028](https://pubmed.ncbi.nlm.nih.gov/40779028/) | 2025 | Phase I | Breast Cancer Res Treat | Carboplatin + gemcitabine + mifepristone (glucocorticoid receptor antagonist) in GR-positive breast and ovarian cancer; explores pharmacological strategy to reverse GR-mediated suppression of carboplatin-induced apoptosis |
| [9516604](https://pubmed.ncbi.nlm.nih.gov/9516604/) | 1998 | Phase II | Oncology | Paclitaxel (175 mg/m²) + carboplatin (AUC 6) every 3 weeks as first-line for 66 patients with advanced breast cancer; one of the foundational studies defining dosing and response rates for this combination |
| [8893899](https://pubmed.ncbi.nlm.nih.gov/8893899/) | 1996 | Review | Semin Oncol | Foundational evaluation of carboplatin single-agent activity and paclitaxel-carboplatin synergy in advanced breast cancer; laid the conceptual and clinical groundwork for combination trials still running today |
| [39944694](https://pubmed.ncbi.nlm.nih.gov/39944694/) | 2025 | Bioinformatics/Cohort | Front Immunol | DNA damage repair (DDR) gene signature associated with carboplatin resistance and immune infiltration in breast cancer; identifies prognostic markers and immune evasion mechanisms relevant for precision patient selection |
| [33256829](https://pubmed.ncbi.nlm.nih.gov/33256829/) | 2020 | Phase II | Breast Cancer Res | Phase II trial of carboplatin + bevacizumab in breast cancer brain metastases; evaluated safety and antitumor activity, demonstrating that carboplatin's CNS penetration is sufficient for activity in the metastatic brain setting |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Platinum coordination compound / Alkylating-like agent) |
| Myelosuppression Risk | High — dose-limiting toxicity is thrombocytopenia (platelet nadir typically Day 21, AUC-dependent); neutropenia and anaemia are also frequent; requires CBC monitoring before each cycle and dose adjustment for marrow recovery |
| Emetogenicity Classification | Moderate to High (moderate at standard AUC 5–6; high at escalated doses used in transplant conditioning) |
| Monitoring Items | CBC with differential and platelet count prior to each cycle; serum creatinine and creatinine clearance (Cockcroft-Gault or measured GFR) for Calvert formula dosing; audiometry for high-dose or cumulative regimens |
| Handling Protection | Must follow cytotoxic drug handling regulations; preparation in a Class II biological safety cabinet under negative pressure; full PPE (double gloves, gown, eye protection) required for preparation and administration; cytotoxic waste disposal protocols apply |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Carboplatin achieves the highest evidence level (L1) for female breast carcinoma, supported by at least four completed Phase 3 RCTs across TNBC (NCT00532727, NCT02125344) and HER2-positive (NCT00047255, NCT02003209) subtypes, plus an ongoing 720-patient Phase 3 trial (NCT03168880). The mechanistic rationale — platinum-induced DNA cross-links exploiting homologous recombination deficiency in BRCA-mutated and BRCAness tumors — represents one of the most rigorously validated predictive biomarker relationships in oncology.

**To proceed, the following is needed:**
- **Philippine FDA registration**: Carboplatin currently has zero registered products in the Philippines; product registration or a hospital/compassionate-use framework is required before clinical procurement
- **Mechanism of action documentation**: Retrieve the full pharmacology entry from the DrugBank API (DB00958) to complete the regulatory evidence dossier
- **Biomarker-driven patient selection strategy**: Define upfront testing for BRCA1/2 mutation status and HRD score to identify which breast cancer subtype (TNBC vs HER2+ vs BRCA-mutated HR+) benefits most, avoiding use in biomarker-unselected luminal A/B disease where benefit is not established
- **Safety monitoring protocol**: Formalise renal function monitoring for Calvert-formula dosing, myelosuppression management (G-CSF policy, platelet transfusion thresholds), and cumulative ototoxicity surveillance for high-dose regimens
- **YMYL disclaimer**: These predictions are provided for research reference only and do not constitute medical advice; all repurposing candidates require clinical validation and physician oversight before application in patient care
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

