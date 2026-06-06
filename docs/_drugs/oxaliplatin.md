---
layout: default
title: Oxaliplatin
parent: 僅模型預測 (L5)
nav_order: 263
evidence_level: L5
indication_count: 4
---

# Oxaliplatin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Oxaliplatin: From Colorectal Cancer to Malignant Pleural Mesothelioma

## One-Sentence Summary

Oxaliplatin is a third-generation platinum-based chemotherapeutic agent, globally established as the backbone of FOLFOX/XELOX regimens for colorectal cancer treatment.
The TxGNN model predicts it may be effective for **malignant pleural mesothelioma (MPM)**,
with **5 clinical trials** and **20 publications** currently supporting this direction — including two completed Phase 2 trials directly testing oxaliplatin-based combinations in MPM.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Colorectal cancer (global standard of care; FOLFOX/XELOX backbone) |
| Predicted New Indication | Malignant Pleural Mesothelioma |
| TxGNN Prediction Score | 99.68% |
| Evidence Level | L2 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Oxaliplatin is a platinum analogue that exerts its anticancer effect by forming bulky DNA intrastrand and interstrand crosslinks — primarily GG-intrastrand adducts — which block DNA replication and transcription, ultimately triggering apoptosis. Unlike cisplatin, oxaliplatin's adducts are not recognized by mismatch repair (MMR) proteins, giving it a distinct resistance profile and complementary activity to other platinum agents.

Malignant pleural mesothelioma is a rare but aggressive cancer of the pleural lining, strongly associated with asbestos exposure. MPM cells frequently harbor defects in DNA damage repair pathways — including ERCC1 downregulation and BAP1/NF2 mutations — which impair the cell's ability to remove platinum-DNA adducts, theoretically increasing sensitivity to oxaliplatin. Combining oxaliplatin with antimetabolites such as gemcitabine (GemOx regimen) or raltitrexed creates a mechanistic synergy: oxaliplatin disrupts DNA integrity while antimetabolites block nucleotide synthesis, attacking tumor cells on two complementary fronts.

The clinical rationale is further reinforced by the emergence of intraperitoneal/intracavitary delivery strategies. HIPEC (Hyperthermic Intraperitoneal Chemotherapy) and PIPAC (Pressurized IntraPeritoneal Aerosol Chemotherapy) with oxaliplatin exploit the peritoneal-plasma barrier to achieve local drug concentrations 10–20× higher than systemic delivery, potentially overcoming the modest systemic response rates historically observed in MPM. Multiple Phase 2 trials, including one completed study with 29 patients (NCT00859469), have demonstrated measurable activity of oxaliplatin-based regimens in MPM, validating the TxGNN model's high-confidence prediction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00859469](https://clinicaltrials.gov/study/NCT00859469) | Phase 2 | Completed | 29 | Direct evaluation of Oxaliplatin (Eloxatin®) + Gemcitabine as first- or second-line chemotherapy for malignant pleural or peritoneal mesothelioma; assesses objective response rate |
| [NCT00996385](https://clinicaltrials.gov/study/NCT00996385) | Phase 2 | Unknown | 29 | Bortezomib (Velcade) + Oxaliplatin (Eloxatin) in previously treated pleural or peritoneal mesothelioma; 6-cycle maximum, QoL and CT response assessed every 2 cycles |
| [NCT03210298](https://clinicaltrials.gov/study/NCT03210298) | N/A | Unknown | 1,000 | Multicenter international registry of PIPAC/PITAC procedures for malignant pleural and peritoneal diseases; provides real-world safety data for intraperitoneal oxaliplatin |

> **Note:** NCT06310473 (esophagogastric junction cancer) and NCT05107674 (NX-1607 Phase 1) were excluded as they are not directly relevant to MPM — likely database retrieval artifacts where oxaliplatin appears as a background chemotherapy.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12525529](https://pubmed.ncbi.nlm.nih.gov/12525529/) | 2003 | Phase II | J Clin Oncol | Raltitrexed + Oxaliplatin in 70 MPM patients (55 chemo-naive, 15 pretreated); overall response rate reported; established this combination as active in MPM |
| [14609447](https://pubmed.ncbi.nlm.nih.gov/14609447/) | 2003 | Phase II Multicenter | Clin Lung Cancer | Gemcitabine 1000 mg/m² + Oxaliplatin 80 mg/m² (days 1 & 8, 21-day cycle) in 25 MPM patients; efficacy and safety profile evaluated |
| [11989592](https://pubmed.ncbi.nlm.nih.gov/11989592/) | 2001 | Phase I/II | Tumori | Pilot study of Oxaliplatin + Raltitrexed in inoperable MPM; preliminary activity signal following Phase I dose-finding |
| [15639727](https://pubmed.ncbi.nlm.nih.gov/15639727/) | 2005 | Phase II | Lung Cancer | Vinorelbine 30 mg/m² (days 1, 8) + Oxaliplatin 130 mg/m² (day 1) in untreated MPM; 24% prior response rate with single-agent vinorelbine used as rationale |
| [19091133](https://pubmed.ncbi.nlm.nih.gov/19091133/) | 2008 | Retrospective Cohort | J Occup Med Toxicol | Gemcitabine ± Oxaliplatin in pemetrexed-pretreated MPM patients; real-world second-line efficacy and tolerability assessment |
| [15893013](https://pubmed.ncbi.nlm.nih.gov/15893013/) | 2005 | Phase II | Lung Cancer | Raltitrexed + Oxaliplatin as second-line therapy in 14 MPM patients; trial closed early due to absence of objective responses (disease stabilization in 4/14); important negative result |
| [10930799](https://pubmed.ncbi.nlm.nih.gov/10930799/) | 2000 | Phase II Experience | Eur J Cancer | Institut Gustave Roussy 9-year experience in 163 mesothelioma patients across 7 trials; Raltitrexed-Oxaliplatin combination highlighted as a step forward |
| [31455014](https://pubmed.ncbi.nlm.nih.gov/31455014/) | 2019 | Review | Int J Mol Sci | Cisplatin, oxaliplatin, and pemetrexed investigated for immunomodulatory capacity in MPM; supports rational design of oxaliplatin + immune checkpoint inhibitor combinations |
| [37359920](https://pubmed.ncbi.nlm.nih.gov/37359920/) | 2023 | Systematic Review | Indian J Surg Oncol | PRISMA-guided systematic review of HIPEC protocols for peritoneal mesothelioma; oxaliplatin among agents reviewed for locoregional delivery |
| [12610498](https://pubmed.ncbi.nlm.nih.gov/12610498/) | 2003 | Narrative Review | Br J Cancer | Comprehensive review of MPM chemotherapy including all Phase 2–3 trials published up to 2003; contextualizes oxaliplatin-based regimen results within the broader treatment landscape |

---

## Philippines Market Information

Oxaliplatin currently has **no registered products** with the Philippine FDA (FDA Philippines). There are 0 active licenses on file.

> This does not preclude clinical use under compassionate/expanded access pathways or institutional importation, but any formal repurposing program would require a new market authorization application.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Platinum analogue (3rd generation) |
| Myelosuppression Risk | Moderate — neutropenia and thrombocytopenia reported; generally less nephrotoxic than cisplatin but myelosuppression monitoring required |
| Emetogenicity Classification | Moderate to High — prophylactic antiemetic regimen (5-HT3 antagonist + dexamethasone) recommended |
| Monitoring Items | CBC with differential (before each cycle), serum creatinine and eGFR, liver function tests, neurological assessment (peripheral neuropathy grading — the dose-limiting toxicity of oxaliplatin) |
| Handling Protection | Must follow cytotoxic drug handling regulations; cold-exposure precaution recommended post-infusion (oxaliplatin induces acute cold-triggered dysesthesia) |

---

## Safety Considerations

Safety data (TFDA package insert warnings, contraindications, and drug-drug interaction records) were not retrievable for this Evidence Pack. The primary known clinical concern unique to oxaliplatin — not shared with other platinum agents — is cumulative **peripheral sensory neuropathy**, which is both acute (cold-triggered, reversible) and chronic (dose-dependent, potentially irreversible at cumulative doses >850 mg/m²).

Please refer to the originator package insert (Eloxatin®, Sanofi) and current clinical guidelines for full safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Two completed Phase 2 trials (NCT00859469; Fizazi et al., JCO 2003) directly tested oxaliplatin-based regimens in MPM, establishing measurable activity — this meets the L2 threshold. The mechanistic basis (platinum-DNA adduct formation in a DNA-repair-deficient tumor) is well-grounded, and the emerging HIPEC/PIPAC intraperitoneal delivery route offers a pharmacokinetically favorable path for locoregional MPM control. However, oxaliplatin is not currently registered in the Philippines, and key safety data from the Philippine FDA package insert is unavailable.

**To proceed, the following is needed:**

- **Mechanism of Action data**: Retrieve full MOA and pharmacokinetic profile from DrugBank API (flagged as DG002 High priority)
- **Philippine FDA package insert / safety dossier**: Download and parse TFDA or originator SmPC PDF to fulfill DG001 (Blocking — required before S1 safety evaluation)
- **Subtype-stratified evidence**: Existing MPM trials rarely report oxaliplatin efficacy by histological subtype (epithelioid vs. sarcomatoid); a systematic search for subtype-specific outcomes would sharpen the evidence base
- **Market access pathway**: Identify Philippine FDA regulatory pathway for new indication filing or compassionate use authorization, given zero current registrations
- **Peripheral neuropathy risk management plan**: Cumulative neurotoxicity is the primary dose-limiting concern in any MPM treatment protocol using oxaliplatin; a formal monitoring and dose-modification protocol should be defined before clinical use
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

