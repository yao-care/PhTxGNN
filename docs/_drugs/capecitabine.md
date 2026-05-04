---
layout: default
title: Capecitabine
parent: 僅模型預測 (L5)
nav_order: 55
evidence_level: L5
indication_count: 10
---

# Capecitabine
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

# Capecitabine: From Colorectal Cancer to Gastric Tubular Adenocarcinoma

## One-Sentence Summary

Capecitabine is an oral fluoropyrimidine prodrug established globally as first-line chemotherapy for colorectal and breast cancer, functioning through tumor-selective enzymatic conversion to active 5-fluorouracil (5-FU) by thymidine phosphorylase (TP) preferentially overexpressed in tumor tissue.
This multi-indication TxGNN evaluation covers 10 gastric cancer subtypes; the clinically most actionable prediction is **Gastric Tubular Adenocarcinoma** (L1 evidence), supported by **20 publications** including multiple completed Phase 3 landmark RCTs (CLASSIC, CheckMate 649, KEYNOTE-859, RESOLVE, ORIENT-16, GLOW) — the highest TxGNN-ranked prediction (GAPPS, score 99.94%) carries only model-level evidence (L5, Hold).
Capecitabine is currently **not registered in the Philippines**, making regulatory authorization the critical prerequisite before any clinical application.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Colorectal cancer and breast cancer (global approval; not registered in the Philippines) |
| Predicted New Indication | Gastric Tubular Adenocarcinoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Capecitabine is an oral fluoropyrimidine carbamate prodrug designed for tumor-selective activation. After oral absorption, hepatic carboxylesterase converts it to 5′-deoxy-5-fluorocytidine (5′-DFCR), which cytidine deaminase subsequently converts to 5′-deoxy-5-fluorouridine (5′-DFUR). The final and rate-limiting step is catalyzed by thymidine phosphorylase (TP), which is characteristically overexpressed in many tumor tissues compared to adjacent healthy tissue, generating active 5-fluorouracil (5-FU) preferentially at the tumor site. Active 5-FU then inhibits thymidylate synthase (TS), blocking de novo synthesis of thymidylate (dTMP) required for DNA replication, and is also misincorporated into RNA, further disrupting tumor cell protein synthesis. *Note: Formal DrugBank MOA documentation was not retrieved in this evaluation (Data Gap DG002); the above reflects established published pharmacology.*

Gastric tubular adenocarcinoma corresponds to the Lauren intestinal subtype — the predominant histological form of gastric cancer, accounting for approximately 50–60% of all cases and typically arising in the distal stomach. These tumors characteristically exhibit **high TP expression and relatively low TS expression**, creating precisely the biological environment that maximizes Capecitabine's tumor-selective activation advantage over intravenous 5-FU. The mechanistic compatibility between this subtype and fluoropyrimidine therapy is paralleled by colorectal cancer, where CAPOX (Capecitabine + Oxaliplatin) is also a cornerstone regimen. At the translational level, the MALAT1-miRNA regulatory network controls TYMS-encoded TS expression and directly modulates 5-FU-based chemotherapy sensitivity (PMID 35922756), providing molecular-level support for patient stratification.

The clinical evidence base is exceptionally mature. The landmark CLASSIC trial (PMID 22226517, Phase 3 RCT, n=1,035) established CAPOX adjuvant chemotherapy as standard of care after D2 gastrectomy, improving 3-year disease-free survival from 59% to 74% (HR 0.56). Capecitabine's role has since been reinforced by its adoption as the universal chemotherapy backbone in every major Phase 3 immunotherapy combination trial in gastric/GEJ adenocarcinoma: CheckMate 649 (nivolumab), KEYNOTE-859 (pembrolizumab), ORIENT-16 (sintilimab), GLOW/SPOTLIGHT (zolbetuximab), and RATIONALE-305 (tislelizumab). This near-universal adoption across diverse sponsor organizations and patient populations constitutes the strongest possible external validation of Capecitabine's central, non-replaceable role in gastric tubular adenocarcinoma management.

---

## Clinical Trial Evidence

No ClinicalTrials.gov registrations are specifically designated for gastric tubular adenocarcinoma in isolation. The following trials from the closely related gastric cardia, gastric body, and signet ring cell adenocarcinoma predictions **directly test Capecitabine-containing regimens** and are highly representative of the broader gastric adenocarcinoma spectrum:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT00040859](https://clinicaltrials.gov/study/NCT00040859) | Phase 2 | Completed | 48 | CAPOX (Oxaliplatin + Capecitabine) as first-line treatment of measurable metastatic adenocarcinoma of the esophagus, GEJ, and gastric cardia; ORR 45% (95% CI 30–60%) — highest direct relevance for CAPOX in gastric cardia/GEJ |
| [NCT03653507](https://clinicaltrials.gov/study/NCT03653507) | Phase 3 | Active, not recruiting | 507 | SPOTLIGHT trial: Zolbetuximab + CAPOX vs. placebo + CAPOX as first-line treatment of CLDN18.2+/HER2-negative gastric/GEJ adenocarcinoma; CAPOX serves as the pivotal control backbone |
| [NCT06901531](https://clinicaltrials.gov/study/NCT06901531) | Phase 3 | Recruiting | 500 | Zolbetuximab + Pembrolizumab + CAPOX triple combination vs. Zolbetuximab + CAPOX in CLDN18.2+/HER2-neg/PD-L1+ gastric/GEJ cancer; next-generation combination platform |
| [NCT00374036](https://clinicaltrials.gov/study/NCT00374036) | Phase 3 | Completed | 416 | Polychemotherapy sequence strategies for metastatic or locally advanced gastric/cardia adenocarcinoma; large-scale Phase 3 evidence for gastric cancer chemotherapy strategy |
| [NCT00938470](https://clinicaltrials.gov/study/NCT00938470) | Phase 2 | Completed | 73 | Randomized extended neoadjuvant therapy for locally advanced esophageal/GEJ/gastric cardia adenocarcinoma: docetaxel + oxaliplatin + capecitabine vs. fluorouracil + oxaliplatin + radiation |
| [NCT06238752](https://clinicaltrials.gov/study/NCT06238752) | Phase 2 | Completed | 33 | Apatinib + Tislelizumab + CAPOX first-line for HER2-negative advanced gastric/GEJ cancer including signet ring cell subtype and peritoneal metastasis; demonstrates CAPOX feasibility in high-risk subgroups |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [22226517](https://pubmed.ncbi.nlm.nih.gov/22226517/) | 2012 | Phase 3 RCT | *Lancet* | **CLASSIC trial**: CAPOX adjuvant chemotherapy after D2 gastrectomy for Stage II–IIIB gastric cancer improves 3-year DFS (74% vs. 59%, HR 0.56, n=1,035); milestone evidence establishing Capecitabine in gastric cancer |
| [34102137](https://pubmed.ncbi.nlm.nih.gov/34102137/) | 2021 | Phase 3 RCT | *Lancet* | **CheckMate 649**: Nivolumab + CAPOX vs. CAPOX alone first-line for HER2-negative advanced gastric/GEJ/esophageal adenocarcinoma; confirms CAPOX as international standard-of-care backbone |
| [30982686](https://pubmed.ncbi.nlm.nih.gov/30982686/) | 2019 | Phase 3 RCT | *Lancet* | **FLOT4**: Perioperative FLOT vs. ECX/ECF (capecitabine-containing arm) for resectable gastric/GEJ adenocarcinoma; FLOT superiority established with CAPOX as active comparator |
| [34252374](https://pubmed.ncbi.nlm.nih.gov/34252374/) | 2021 | Phase 3 RCT | *Lancet Oncology* | **RESOLVE trial**: Perioperative/postoperative SOX vs. postoperative CAPOX after D2 gastrectomy; CAPOX confirmed as effective comparator confirming non-inferiority of both approaches |
| [37524953](https://pubmed.ncbi.nlm.nih.gov/37524953/) | 2023 | Phase 3 RCT | *Nature Medicine* | **GLOW trial**: Zolbetuximab + CAPOX vs. placebo + CAPOX in CLDN18.2+ gastric/GEJ adenocarcinoma; PFS and OS improvement — CAPOX is the backbone of a positive pivotal trial |
| [37875143](https://pubmed.ncbi.nlm.nih.gov/37875143/) | 2023 | Phase 3 RCT | *Lancet Oncology* | **KEYNOTE-859**: Pembrolizumab + CAPOX vs. placebo + CAPOX for HER2-negative advanced gastric/GEJ adenocarcinoma; OS benefit confirmed across PD-L1 CPS subgroups |
| [38806195](https://pubmed.ncbi.nlm.nih.gov/38806195/) | 2024 | Phase 3 RCT | *BMJ* | **RATIONALE-305**: Tislelizumab + CAPOX vs. placebo + CAPOX first-line for advanced gastric/GEJ adenocarcinoma; validates CAPOX across Asia-Pacific populations |
| [38051328](https://pubmed.ncbi.nlm.nih.gov/38051328/) | 2023 | Phase 3 RCT | *JAMA* | **ORIENT-16**: Sintilimab + CAPOX vs. placebo + CAPOX for unresectable gastric/GEJ cancer; OS and PFS benefits particularly relevant for Asian patient populations including Philippines |
| [20728210](https://pubmed.ncbi.nlm.nih.gov/20728210/) | 2010 | Phase 3 RCT | *Lancet* | **ToGA trial**: Trastuzumab + chemotherapy (capecitabine/cisplatin arm) vs. chemotherapy alone in HER2+ advanced gastric/GEJ cancer; foundational capecitabine combination trial |
| [35922756](https://pubmed.ncbi.nlm.nih.gov/35922756/) | 2022 | Basic Science | *Molecular Medicine* | MALAT1-miRNA network regulates TYMS-encoded thymidylate synthase expression, affecting 5-FU-based chemotherapy sensitivity; mechanistic framework for Capecitabine patient stratification in gastric cancer |

---

## Philippines Market Information

Capecitabine is currently **not registered** with the Food and Drug Administration of the Philippines. No marketing authorizations are on file.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | (No registrations on file) | — | — |

A full marketing authorization application (MAA/NDA) submission to the FDA Philippines is required before Capecitabine can be clinically prescribed in the Philippines. Reference product: Xeloda® (Roche), globally approved for colorectal cancer (adjuvant, metastatic) and metastatic breast cancer.

---

## Cytotoxicity

Capecitabine meets antineoplastic criteria: it is a cytotoxic agent (fluoropyrimidine class) with original oncology indications and direct DNA synthesis disruption via 5-FU.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Oral fluoropyrimidine prodrug (tumor-selective 5-FU generator) |
| Myelosuppression Risk | Low to moderate (neutropenia incidence lower than IV 5-FU; lymphocytopenia and anemia may occur; significant thrombocytopenia uncommon as monotherapy) |
| Emetogenicity Classification | Low (oral administration; mild nausea more common than vomiting; classified as minimal-to-low emetogenic risk per MASCC/ESMO/ASCO antiemetic guidelines) |
| Monitoring Items | CBC with differential (baseline + Day 1 of each cycle); serum creatinine and creatinine clearance (CrCl) — mandatory for dosing: 25% dose reduction if CrCl 30–50 mL/min, contraindicated if CrCl <30 mL/min; liver function tests (AST, ALT, total bilirubin); hand-foot syndrome (HFS/PPES) grading at each clinical visit; INR if co-administered with warfarin (critical DDI) |
| Handling Protection | Institutional cytotoxic drug handling procedures required; gloves mandatory for dispensing and administration; tablets must not be crushed by unprotected caregivers; preparation staff require cytotoxic safety certification |

---

## Safety Considerations

Detailed Philippines-specific or TFDA safety data (local package insert warnings, contraindications, and drug-drug interaction profile) was not available in this evaluation. Please refer to the complete international package insert (EMA SmPC or FDA Prescribing Information for Xeloda®) for full safety information.

Based on published clinical literature and global pharmacovigilance:

- **Hand-foot syndrome (HFS/Palmar-Plantar Erythrodysesthesia)**: The most characteristic dose-limiting toxicity of Capecitabine; Grade 3 HFS requires mandatory dose reduction (25%); preventive measures (urea-based emollients, sun avoidance) should begin at cycle 1.
- **Renal function dependency**: Capecitabine clearance is directly proportional to renal function; CrCl-based dose adjustment is mandatory at treatment initiation and reassessed before each cycle in high-risk patients.
- **DPD deficiency risk**: Complete dihydropyrimidine dehydrogenase (DPD) deficiency causes life-threatening 5-FU accumulation; DPYD gene testing (or phenotyping via uracil breath test) is recommended in European guidelines before first administration.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for Capecitabine (as the CAPOX backbone) in gastric tubular adenocarcinoma satisfies L1 criteria — anchored by the landmark CLASSIC Phase 3 RCT (n=1,035) and further reinforced by its universal adoption as the control-arm chemotherapy in six subsequent Phase 3 pivotal trials by independent international sponsors — making the clinical evidence essentially unequivocal. The primary barriers to implementation in the Philippines are regulatory (no local registration) and safety data access, not scientific uncertainty about efficacy.

**To proceed, the following is needed:**
- **Regulatory authorization** (Critical): File marketing authorization application with FDA Philippines for Capecitabine; no clinical use is permissible until approval is granted
- **Safety data gap remediation** (Blocking — DG001): Download and systematically review TFDA or EMA package insert for complete warnings, contraindications, and drug-drug interaction profile
- **MOA documentation** (High — DG002): Query DrugBank API to retrieve formal mechanism of action and pharmacokinetic data for database completeness
- **DPYD/DPD screening protocol**: Establish institutional policy for pre-treatment DPYD genotyping aligned with international guidelines
- **Renal function monitoring plan**: Implement CrCl-based dose adjustment algorithm and schedule into prescribing workflow
- **HFS management guideline**: Develop institutional HFS grading scale, dose modification table, and patient education materials before first prescription

> **Multi-indication context**: Among the 10 TxGNN-predicted gastric cancer subtypes evaluated, 4 carry a **Hold** recommendation (L5 evidence): GAPPS (Rank 1), Microinvasive Gastric Cancer (Rank 4), EBV-Associated Gastric Carcinoma (Rank 9), and Malignant Gastric Granular Cell Tumor (Rank 10). These should not be pursued for clinical application without dedicated prospective study. The **Proceed with Guardrails** recommendation applies to: Gastric Tubular Adenocarcinoma (L1), Gastric Body Carcinoma (L1), Signet Ring Cell Gastric Adenocarcinoma (L2), and Gastric Cardia Adenocarcinoma (L2).
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

