---
layout: default
title: Epirubicin
parent: 僅模型預測 (L5)
nav_order: 126
evidence_level: L5
indication_count: 7
---

# Epirubicin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Epirubicin: From Breast Cancer to Primary Pulmonary Lymphoma

## One-Sentence Summary

Epirubicin is an anthracycline antibiotic antineoplastic agent with established international use in breast cancer, gastric/esophageal cancer, and other solid tumors — though it currently holds **no Philippines market registration**.
The TxGNN model's highest-scoring prediction is **Primary Pulmonary Lymphoma** (score 99.71%), with **no clinical trials** and **9 publications** of indirect relevance currently supporting this direction.
Across all 7 predicted indications in this evidence pack, the most clinically actionable findings are for **Small Cell Lung Carcinoma** (11 clinical trials including two Phase III RCTs, 20 publications; L1 evidence) and **Upper Aerodigestive Tract Neoplasm** (20 publications including landmark Phase III RCTs such as the MAGIC Trial; L1 evidence).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines registration; globally established for breast cancer, gastric/esophageal cancer, and other malignancies |
| Predicted New Indication (Rank 1) | Primary Pulmonary Lymphoma |
| TxGNN Prediction Score | 99.71% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## All Predicted Indications at a Glance

| Rank | Disease | TxGNN Score | Evidence Level | Trials | Publications | Decision |
|------|---------|-------------|----------------|--------|-------------|---------|
| 1 | Primary Pulmonary Lymphoma | 99.71% | L4 | 0 | 9 | Hold |
| 2 | Well-differentiated Fetal Adenocarcinoma of the Lung | 99.69% | L5 | 0 | 0 | Hold |
| 3 | **Small Cell Lung Carcinoma** | **99.69%** | **L1** | **11** | **20** | **Proceed with Guardrails** |
| 4 | Pulmonary Blastoma | 99.65% | L4 | 0 | 5 | Hold |
| 5 | Lung Mixed Small Cell and Squamous Cell Carcinoma | 99.17% | L5 | 0 | 0 | Hold |
| 6 | Myeloid Leukemia | 99.07% | L3 | 0 | 20 | Research Question |
| 7 | **Upper Aerodigestive Tract Neoplasm** | **99.06%** | **L1** | 0† | **20** | **Proceed with Guardrails** |

†No ClinicalTrials.gov registrations returned for this disease query; L1 designation is based on Phase III RCT publications (MAGIC Trial, Neo-AEGIS Trial, REAL-2 Trial) in the literature evidence set.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data is not available in this Evidence Pack. Based on established pharmacology, Epirubicin is the 4'-epimer of Doxorubicin — a structural modification that increases its rate of glucuronidation, conferring modestly improved cardiac safety at equivalent doses while preserving antitumor activity. Like other anthracyclines, it intercalates into DNA double strands, stabilizes Topoisomerase II cleavage complexes (inducing irreparable double-strand breaks), and generates reactive oxygen species — collectively arresting DNA replication and transcription in rapidly proliferating cells.

Primary Pulmonary Lymphoma (PPL) most commonly presents as MALT lymphoma (indolent, often amenable to local therapy) or Diffuse Large B-Cell Lymphoma (DLBCL, aggressive, requiring systemic anthracycline-based chemotherapy). For aggressive PPL/DLBCL, Doxorubicin is the anthracycline backbone of the standard R-CHOP regimen. Epirubicin shares the same Topoisomerase II inhibition mechanism and has been substituted for Doxorubicin in established lymphoma regimens — including VEBEP (Vinblastine + Epirubicin + Bleomycin + Etoposide + Prednisone) and MOPPEBVCAD (containing Epidoxirubicin) — demonstrating clinical activity in Hodgkin's lymphoma and non-Hodgkin's lymphoma.

The TxGNN prediction is mechanistically plausible: Epirubicin's cytotoxic activity against lymphoid tumor cells is well-established, and PPL's aggressive subtype (DLBCL) is biologically susceptible to DNA-damaging anthracyclines. However, PPL is a rare, anatomically distinct entity, and no clinical studies have specifically investigated Epirubicin-based regimens at this pulmonary site. The prediction therefore represents a mechanistically coherent hypothesis requiring prospective investigation rather than an immediately actionable clinical finding.

---

## Clinical Trial Evidence

Currently no clinical trials specifically investigating Epirubicin in **Primary Pulmonary Lymphoma** are registered on ClinicalTrials.gov or ICTRP.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [16428496](https://pubmed.ncbi.nlm.nih.gov/16428496/) | 2006 | Clinical Trial | *Clin Cancer Res* | MOPPEBVCAD regimen (containing Epirubicin/Epidoxirubicin) with limited radiotherapy in advanced Hodgkin's lymphoma; 10-year results with late toxicity and second tumor incidence — demonstrates Epirubicin activity in lymphoma regimens |
| [10526668](https://pubmed.ncbi.nlm.nih.gov/10526668/) | 1999 | Clinical Study | *Cancer J Sci Am* | VEBEP (containing Epirubicin) + involved-field radiotherapy in advanced Hodgkin's disease; pilot study evaluating efficacy and toxicity of Epirubicin-based lymphoma combination |
| [7686469](https://pubmed.ncbi.nlm.nih.gov/7686469/) | 1993 | Drug Review | *Drugs* | Comprehensive pharmacodynamic/pharmacokinetic review of Epirubicin; documents equivalent response rates to Doxorubicin in breast cancer and multiple malignancies with improved cardiac safety profile |
| [39192408](https://pubmed.ncbi.nlm.nih.gov/39192408/) | 2024 | Retrospective | *Zhongguo Shi Yan Xue Ye Xue Za Zhi* | Primary extranodal DLBCL clinical features and prognostic factors in the rituximab era; provides disease context for aggressive pulmonary lymphoma management approaches |
| [40728626](https://pubmed.ncbi.nlm.nih.gov/40728626/) | 2025 | Real-world Study | *Ann Hematol* | Pola-R-CHP (anthracycline-based combination) in trial-ineligible first-line DLBCL; improved PFS vs. historical controls in real-world settings including lower-IPI patients |
| [1866500](https://pubmed.ncbi.nlm.nih.gov/1866500/) | 1991 | Case Series | *Rev Invest Clin* | Primary non-Hodgkin's lymphoma with unusual pulmonary involvement and hemorrhagic pleural effusion; electron microscopic diagnosis of lymphoid atypical cells and subsequent chemotherapy management |
| [7525516](https://pubmed.ncbi.nlm.nih.gov/7525516/) | 1994 | Clinical Study | *Int J Radiat Oncol Biol Phys* | Extended-field radiotherapy in favorable stage IA-IIA Hodgkin's disease; long-term results with irradiation-only approach in a subset that would otherwise receive anthracycline-based chemotherapy |
| [36237246](https://pubmed.ncbi.nlm.nih.gov/36237246/) | 2022 | Case Report | *Transl Cancer Res* | First Chinese case of pleural MALT lymphoma; highlights diagnostic pitfalls of rare pulmonary lymphoid malignancies — most similar pathology to PPL in this dataset |
| [8386780](https://pubmed.ncbi.nlm.nih.gov/8386780/) | 1993 | Case Report | *Rinsho Ketsueki* | Malignant lymphoma (lymphoblastic type) developing after small cell lung carcinoma treatment; marked chemotherapy resistance and rapid clinical deterioration |

---

## Philippines Market Information

Epirubicin currently has **no Philippines FDA drug registrations** and is not marketed in the Philippines.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional Cytotoxic — Anthracycline class (Topoisomerase II inhibitor / DNA intercalating agent) |
| Myelosuppression Risk | **High** — neutropenia is the primary dose-limiting toxicity; febrile neutropenia and thrombocytopenia reported across clinical trials; nadir typically at days 10–14 post-infusion with recovery by day 21 |
| Emetogenicity Classification | Moderate to High (consistent with standard IV anthracycline agents at conventional doses ≥90 mg/m²) |
| Monitoring Items | CBC with differential (before each cycle); cardiac function assessment via echocardiogram or MUGA scan (mandatory at baseline and periodically — cumulative dose threshold applies); liver function tests (Epirubicin is primarily hepatically metabolized and biliary-excreted); long-term surveillance for secondary AML/MDS |
| Handling Protection | Must follow cytotoxic drug handling regulations — Epirubicin is a **vesicant** (severe tissue necrosis on extravasation); closed-system drug transfer device (CSTD) required during preparation; full PPE mandatory |

> **Cardiotoxicity Alert:** Epirubicin carries a cumulative dose-dependent risk of irreversible cardiomyopathy. The generally accepted maximum lifetime cumulative dose is **≤900 mg/m²**; this threshold falls significantly lower in patients with prior anthracycline exposure, mediastinal radiation, or pre-existing cardiac disease. Baseline LVEF ≥50% is typically required before initiation.
>
> **Secondary Malignancy Risk:** Epidemiological data from adjuvant breast cancer trials demonstrate a small but measurable excess risk of secondary AML/MDS, particularly at higher cumulative epirubicin doses and when combined with alkylating agents (e.g., cyclophosphamide). This dual role — as both a therapeutic agent and a potential leukemogenic — requires careful risk-benefit assessment, especially for Myeloid Leukemia as a predicted indication (Rank 6).

---

## Safety Considerations

Please refer to the package insert for safety information. (No Philippines package insert data is available in this evidence pack; DDI database query returned no interactions for Epirubicin in the queried database.)

---

## Key Evidence: Small Cell Lung Carcinoma (Rank 3 — Strongest Evidence, L1)

> *This section presents the most clinically actionable finding in this evidence pack.*

**Why is This Prediction Reasonable?**

Epirubicin is a Topoisomerase II inhibitor targeting rapidly proliferating cells. SCLC is characterized by extremely rapid proliferation, near-universal high expression of Topoisomerase II, and high sensitivity to DNA-damaging agents — the same biological properties that make it respond to platinum-etoposide as first-line therapy. The CEV regimen (Cyclophosphamide + Epirubicin + Vincristine) has been evaluated in randomized trials as an alternative to platinum-based therapy since the 1980s, and the EpiTax regimen (Epirubicin + Paclitaxel) has demonstrated real-world activity in the relapsed/refractory setting. This is among the best-supported applications of Epirubicin in thoracic oncology.

### Clinical Trial Evidence (SCLC)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00003606](https://clinicaltrials.gov/study/NCT00003606) | Phase 3 | Completed | 216 | **Core trial**: Cisplatin + Etoposide ± Epirubicin + Cyclophosphamide in extensive-stage SCLC; directly evaluated whether adding Epirubicin to standard platinum doublet improves outcomes |
| [NCT00658580](https://clinicaltrials.gov/study/NCT00658580) | Phase 3 | Completed | 361 | **Largest trial (361 pts)**: Cisplatin-Etoposide vs. Etoposide-based regimen; includes Epirubicin-containing arm — most powered SCLC trial in this dataset |
| [NCT06550518](https://clinicaltrials.gov/study/NCT06550518) | Real-world | Completed | 29 | **EpiTax Study**: Retrospective multicenter study of Epirubicin + Paclitaxel as second-line treatment in relapsed SCLC; specifically evaluates systemic and cerebral (brain metastasis) responses with this Epirubicin-specific combination |
| [NCT03755115](https://clinicaltrials.gov/study/NCT03755115) | Phase 2 | Unknown | 40 | PD-1 antibody SHR-1210 + Epirubicin in extensive SCLC after first-line failure; explores immunotherapy + anthracycline synergy in the relapsed setting |
| [NCT00930891](https://clinicaltrials.gov/study/NCT00930891) | Phase 2/3 | Completed | 143 | Bevacizumab + PCDE (Cisplatin-Cyclophosphamide-Epirubicin-Etoposide) vs. PE in extensive SCLC; Epirubicin as key component of the active combination arm |
| [NCT00011921](https://clinicaltrials.gov/study/NCT00011921) | Phase 3 | Unknown | 430 | High-dose vs. standard-dose chemotherapy in SCLC with stem cell support; largest enrollment in this dataset (430 pts) |
| [NCT01872416](https://clinicaltrials.gov/study/NCT01872416) | Phase 2 | Unknown | 30 | Liposomal Doxorubicin + Ifosfamide in second-line SCLC; uses Doxorubicin (not Epirubicin) but demonstrates anthracycline class activity in relapsed SCLC |
| [NCT00154739](https://clinicaltrials.gov/study/NCT00154739) | Phase 2 | Completed | 86 | Gemcitabine + Cisplatin vs. Gemcitabine + Epirubicin in Stage IIIB/IV NSCLC; indication is NSCLC rather than SCLC — provides Epirubicin safety data in thoracic malignancy |
| [NCT00017186](https://clinicaltrials.gov/study/NCT00017186) | Phase 2 | Completed | 69 | Gemcitabine + Epirubicin in malignant mesothelioma; demonstrates thoracic oncology safety profile for Epirubicin combinations |
| [NCT07016126](https://clinicaltrials.gov/study/NCT07016126) | Phase 3 | Recruiting | 70 | D-BACE + neoadjuvant chemotherapy + Carelizumab in resectable NSCLC; low direct relevance (NSCLC, not SCLC) |

### Key Literature (SCLC)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [7833105](https://pubmed.ncbi.nlm.nih.gov/7833105/) | 1994 | RCT | *Eur J Cancer* | CEV (Cyclophosphamide + **Epirubicin** + Vincristine) vs. PE (Cisplatin + Etoposide) in 139 SCLC patients; head-to-head RCT establishing CEV as an active alternative first-line regimen |
| [21831476](https://pubmed.ncbi.nlm.nih.gov/21831476/) | 2012 | Phase II Trial | *Lung Cancer* | **Epirubicin + Ifosfamide (EI)** as non-cross-resistant second/third-line in relapsed/refractory SCLC; used clinically since 1992 with documented activity |
| [10969446](https://pubmed.ncbi.nlm.nih.gov/10969446/) | 2000 | Phase II Trial | *Chin Med J* | TIEP (Tamoxifen + Ifosfamide + **Epirubicin** + Cisplatin) in extensive-stage SCLC; response rates and toxicity profile reported |
| [36000584](https://pubmed.ncbi.nlm.nih.gov/36000584/) | 2023 | Real-world Study | *Cancer Med* | **EpiTax (Epirubicin + Paclitaxel)** as second-line in ES-SCLC (29 pts); real-world efficacy and safety including specific evaluation of brain metastasis responses |
| [7812705](https://pubmed.ncbi.nlm.nih.gov/7812705/) | 1994 | Prospective Clinical | *Lung Cancer* | CEE (Cyclophosphamide + **Epirubicin** + Etoposide) in 136 untreated SCLC patients; 31% complete response, 49% partial response across limited and extensive disease |
| [15829326](https://pubmed.ncbi.nlm.nih.gov/15829326/) | 2005 | Clinical Study | *Lung Cancer* | Crossover chemotherapy (EP vs. CEV) at SCLC relapse; **CEV** (Epirubicin-containing) showed meaningful second-line efficacy in patients who had received EP as first-line |
| [16622468](https://pubmed.ncbi.nlm.nih.gov/16622468/) | 2006 | Phase I/II | *Br J Cancer* | **Epirubicin + Paclitaxel + Etoposide** triplet in extensive SCLC; Phase I established MTD at Epirubicin 75 mg/m² + Paclitaxel 175 mg/m²; Phase II confirmed antitumor activity |
| [9093707](https://pubmed.ncbi.nlm.nih.gov/9093707/) | 1997 | Phase I/II | *Ann Oncol* | VIP-E (Etoposide + Ifosfamide + Cisplatin + **Epirubicin**) dose-intense therapy in 100 consecutive SCLC patients; feasibility and response outcomes documented |
| [11576714](https://pubmed.ncbi.nlm.nih.gov/11576714/) | 2001 | Review | *Lung Cancer* | Comprehensive review confirming **Epirubicin** as one of the proven effective cytotoxic agents in SCLC alongside Cisplatin, Carboplatin, Etoposide, Cyclophosphamide |
| [12847592](https://pubmed.ncbi.nlm.nih.gov/12847592/) | 2003 | Clinical Study | *Saudi Med J* | Alternating EP and IVE (Ifosfamide + Vincristine + **Epirubicin**) in SCLC; evaluates non-cross-resistant alternating strategy efficacy and toxicity |

---

## Key Evidence: Upper Aerodigestive Tract Neoplasm (Rank 7 — L1 Evidence)

**Why is This Prediction Reasonable?**

Epirubicin is the "E" in the ECF regimen (Epirubicin + Cisplatin + 5-FU), which was established by the landmark MAGIC Phase III RCT as a perioperative standard for resectable gastric/gastroesophageal cancer. The ECF/ECX/EOF/EOX family of triplets — all containing Epirubicin — has formed the backbone of upper aerodigestive tract cancer treatment for two decades in Europe and globally. This is one of Epirubicin's most strongly evidence-supported and internationally recognized oncological applications.

### Key Literature (Upper Aerodigestive Tract Neoplasm)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [16822992](https://pubmed.ncbi.nlm.nih.gov/16822992/) | 2006 | Phase III RCT | *N Engl J Med* | **MAGIC Trial**: Perioperative **ECF** (Epirubicin + Cisplatin + 5-FU) vs. surgery alone in 503 patients with resectable gastroesophageal adenocarcinoma; significant survival benefit (5-year OS 36% vs. 23%) — landmark trial establishing ECF as perioperative standard |
| [18172173](https://pubmed.ncbi.nlm.nih.gov/18172173/) | 2008 | Phase III RCT | *N Engl J Med* | **REAL-2 Trial**: ECF vs. ECX vs. EOF vs. **EOX** (all Epirubicin-containing) in 1,002 patients with advanced esophagogastric cancer; EOX (Epirubicin + Oxaliplatin + Capecitabine) demonstrated non-inferiority, offering an oral fluoropyrimidine alternative |
| [37734399](https://pubmed.ncbi.nlm.nih.gov/37734399/) | 2023 | Phase 3 RCT | *Lancet Gastroenterol Hepatol* | **Neo-AEGIS Trial**: Trimodality therapy vs. perioperative **ECF/EOX** or FLOT in esophageal/GEJ adenocarcinoma; Epirubicin-based regimens used as the perioperative comparator arm |
| [33610734](https://pubmed.ncbi.nlm.nih.gov/33610734/) | 2021 | Phase II RCT | *Ann Oncol* | **FAST Trial**: Zolbetuximab (anti-CLDN18.2) + **EOX** vs. EOX alone in advanced CLDN18.2+ gastric/GEJ cancer; confirms EOX (Epirubicin-containing triplet) as an active backbone for combination strategies |
| [27776843](https://pubmed.ncbi.nlm.nih.gov/27776843/) | 2016 | Phase 2/3 | *Lancet Oncol* | **FLOT4-AIO Phase 2**: FLOT vs. **ECF/ECX** (Epirubicin regimens) in resectable gastric/GEJ cancer; histopathological regression favored FLOT, but ECF/ECX remains established comparator — informs current positioning |
| [10631461](https://pubmed.ncbi.nlm.nih.gov/10631461/) | 1999 | Phase I/II | *Ann Oncol* | **ECU**: Epirubicin + Cisplatin + oral UFT/leucovorin in advanced upper GI cancer; dose-escalation study replacing IV 5-FU with oral UFT — early exploration of Epirubicin triplet modifications |
| [11956251](https://pubmed.ncbi.nlm.nih.gov/11956251/) | 2002 | Review/Editorial | *J Clin Oncol* | ECF in gastric and esophageal cancer: commentary on its superiority to FAMTX and establishment as a practice-changing regimen |
| [25579520](https://pubmed.ncbi.nlm.nih.gov/25579520/) | 2014 | Cohort | *J Cancer Res Ther* | Perioperative **EOX** (Epirubicin + Oxaliplatin + Capecitabine) in resectable locally advanced gastroesophageal cancer; demonstrates "MAGIC-like" outcomes with a more convenient oral fluoropyrimidine |
| [29199662](https://pubmed.ncbi.nlm.nih.gov/29199662/) | 2017 | Phase II | *Indian J Cancer* | **ECF vs. DCF** (Docetaxel + Cisplatin + 5-FU) as first-line in advanced gastric/GEJ cancer; prospective head-to-head comparison of Epirubicin-based vs. taxane-based triplets |
| [16702612](https://pubmed.ncbi.nlm.nih.gov/16702612/) | 2006 | Cohort | *Neth J Med* | **ECC** (Epirubicin + Cisplatin + Capecitabine) in inoperable/metastatic esophagogastric cancer; evaluates oral capecitabine substitution for IV 5-FU in ECF framework |

---

## Conclusion and Next Steps

### Primary Prediction — Primary Pulmonary Lymphoma

**Decision: Hold**

**Rationale:**
Primary Pulmonary Lymphoma is TxGNN's highest-scoring prediction but is supported only by L4-level evidence — indirect lymphoma literature with no PPL-specific clinical trials. The prediction is mechanistically plausible (Epirubicin substitutes for Doxorubicin in anthracycline-based lymphoma regimens), but clinical translation requires PPL-specific data.

**To proceed, the following is needed:**
- Dedicated case series or prospective pilot study of Epirubicin-based regimens in confirmed PPL (particularly DLBCL subtype)
- Direct comparison data vs. Doxorubicin-based R-CHOP (the current standard of care for aggressive PPL)
- Pulmonary pharmacokinetic data to confirm adequate drug distribution to lung lymphoid tissue
- Philippines regulatory pathway: registration or compassionate use import approval (no current Philippines license)

---

### Key Actionable Finding — Small Cell Lung Carcinoma

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase III RCTs directly involving Epirubicin in SCLC (NCT00003606: 216 patients; NCT00658580: 361 patients), combined with multiple Phase II trials and the real-world EpiTax data (NCT06550518), establish L1 evidence for Epirubicin-containing regimens in this indication. The CEV regimen (Cyclophosphamide + Epirubicin + Vincristine) has decades of clinical use in SCLC as a non-platinum alternative.

**To proceed, the following is needed:**
- Philippines regulatory registration or import approval (currently no Philippines license)
- Baseline and periodic cardiac function monitoring (LVEF assessment before initiation and every 2–3 cycles)
- CBC monitoring each cycle (high myelosuppression risk; febrile neutropenia prophylaxis protocol)
- MOA documentation (currently a data gap — required for complete regulatory dossier)
- Positioning assessment relative to current SCLC standards of care (Atezolizumab + Carboplatin + Etoposide first-line; Lurbinectedin / Topotecan second-line)
- Secondary AML/MDS risk disclosure and long-term survivorship monitoring plan

---

### Key Actionable Finding — Upper Aerodigestive Tract Neoplasm

**Decision: Proceed with Guardrails**

**Rationale:**
The ECF regimen is supported by the MAGIC Trial (Phase III RCT, *N Engl J Med* 2006) as a perioperative standard in gastric/gastroesophageal adenocarcinoma, and the REAL-2 Trial (Phase III RCT, *N Engl J Med* 2008) validated ECX/EOX variants. This represents one of Epirubicin's most globally established oncological applications, meeting L1 criteria through Phase III RCT literature.

**To proceed, the following is needed:**
- Philippines regulatory registration or import approval
- MOA documentation (currently a data gap)
- Comparative positioning against the FLOT regimen (Docetaxel + Oxaliplatin + Leucovorin + 5-FU), which now supersedes ECF as the preferred perioperative regimen in Western guidelines based on superior histopathological regression
- Cumulative cardiotoxicity monitoring protocol and dose tracking across treatment cycles
- Local (Philippines/Asia-Pacific) patient population pharmacovigilance plan, given potential differences in drug metabolism and tolerability
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

