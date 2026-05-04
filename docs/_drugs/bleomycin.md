---
layout: default
title: Bleomycin
parent: 僅模型預測 (L5)
nav_order: 45
evidence_level: L5
indication_count: 6
---

# Bleomycin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Bleomycin: From Hodgkin's Lymphoma to Reticulum Cell Sarcoma

## One-Sentence Summary

Bleomycin is a glycopeptide antibiotic cytotoxic agent, globally established as a core component of ABVD (Hodgkin's lymphoma) and BEP (germ cell tumour) regimens, though it currently holds **no registered indications in the Philippines**.
The TxGNN model identifies **6 predicted new indications**; the most evidence-supported is **Reticulum Cell Sarcoma** (now classified as Diffuse Large B-Cell Lymphoma, DLBCL), backed by **3 completed Phase 3 RCTs** and **20 publications** including landmark randomised trials.
The remaining 5 predictions range from early investigational (adult astrocytic tumour, primary pulmonary lymphoma) to model-prediction-only, and are summarised in the multi-indication overview below.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hodgkin's lymphoma; germ cell tumours (globally recognised; no Philippines registration) |
| Primary Predicted Indication | Reticulum Cell Sarcoma (Diffuse Large B-Cell Lymphoma) |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Registered |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## All Predicted Indications — Summary

| Rank | Disease | TxGNN Score | Evidence Level | Clinical Trials | Literature | Decision |
|------|---------|-------------|----------------|-----------------|------------|----------|
| 1 | Cauda Equina Neoplasm | 99.30% | L5 | 0 | 3 (all indirect) | Hold |
| 2 | Adult Astrocytic Tumour | 99.28% | L3 | 0 (Phase I/II evidence in literature) | 20 | Research Question |
| **3** | **Reticulum Cell Sarcoma** | **99.14%** | **L1** | **13 (3 completed Phase 3 RCTs)** | **20** | **Proceed with Guardrails** |
| 4 | Primary Pulmonary Lymphoma | 99.10% | L3 | 8 (indirect; Hodgkin's lymphoma trials) | 20 | Research Question |
| 5 | Pulmonary Blastoma | 99.04% | L4 | 0 | 2 (case reports only) | Hold |
| 6 | Well-differentiated Fetal Adenocarcinoma of the Lung | 99.03% | L5 | 0 | 0 | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action (MOA) data for Bleomycin is not available in this evidence pack. Based on established pharmacological knowledge, Bleomycin is a glycopeptide antibiotic that exerts antitumour activity by chelating metal ions (primarily iron) and generating reactive oxygen species, which in turn induce DNA single- and double-strand breaks. This mechanism is most effective in rapidly proliferating cells, particularly during the G₂ and M phases of the cell cycle, making it well-suited for aggressive lymphomas characterised by high proliferative indices.

**Reticulum cell sarcoma** is the obsolete histopathological designation for what is now classified as **Diffuse Large B-Cell Lymphoma (DLBCL)** — the most common aggressive non-Hodgkin's lymphoma worldwide. Bleomycin's DNA-damaging mechanism directly targets the rapid cell division characteristic of DLBCL. Historically, it served as a core component of regimens such as m-BACOD, ProMACE-CytaBOM, CHVmP/BV, and CHOP-Bleo. The earliest direct clinical evidence dates to 1972 (PMID 4109401), when bleomycin monotherapy was administered to 22 reticulum cell sarcoma patients in a marrow-sparing dose protocol, demonstrating objective responses. A landmark CALGB Phase III RCT (PMID 1699653, 1978–1985) directly evaluated the addition of bleomycin to CHOP in 177 patients with diffuse large cell lymphoma, and NCT00005867 enrolled 310 patients in a randomised comparison of PMitCEBO (bleomycin-containing) versus CHOP in good-risk aggressive NHL.

An important clinical caveat: modern standard-of-care for DLBCL is R-CHOP (rituximab + CHOP), which does **not** routinely include bleomycin. This positions bleomycin as a potential option in rituximab-ineligible patients, resource-limited settings where rituximab access is constrained, or in investigational combination strategies, rather than as a first-line replacement. **Bleomycin-induced pneumonitis** remains the principal safety concern and requires mandatory pulmonary function monitoring throughout treatment.

---

## Clinical Trial Evidence — Reticulum Cell Sarcoma

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00005867](https://clinicaltrials.gov/study/NCT00005867) | Phase 3 | Completed | 310 | Largest trial in this set: randomised comparison of CHOP vs PMitCEBO (containing bleomycin) in good-prognosis aggressive NHL; direct comparative efficacy data for a bleomycin-containing regimen vs standard CHOP |
| [NCT00002835](https://clinicaltrials.gov/study/NCT00002835) | Phase 3 | Completed | 116 | Randomised comparison of early intensification vs alternating triple therapy (ATT, bleomycin-containing) in poor-prognosis intermediate-grade / immunoblastic lymphoma; provides long-term efficacy data for bleomycin-containing regimen |
| [NCT00002565](https://clinicaltrials.gov/study/NCT00002565) | Phase 3 | Completed | 61 | Randomised comparison of ATT (bleomycin-containing) vs CHOP in intermediate-grade and immunoblastic NHL (modern DLBCL classification); directly evaluates bleomycin's added value in combination chemotherapy |
| [NCT00057811](https://clinicaltrials.gov/study/NCT00057811) | Phase 2 | Completed | 97 | Rituximab + rasburicase added to bleomycin-containing induction/consolidation in newly diagnosed advanced B-cell leukaemia/lymphoma (paediatric); primarily assesses safety of combination |
| [NCT00002571](https://clinicaltrials.gov/study/NCT00002571) | Phase 2 | Completed | 52 | ProMACE-CytaBOM (bleomycin-containing) + TMP/SMX + AZT + G-CSF in AIDS-related NHL; direct bleomycin use in immunocompromised subgroup; efficacy and toxicity data available |
| [NCT00002524](https://clinicaltrials.gov/study/NCT00002524) | Phase 2 | Completed | 46 | Combination chemotherapy containing bleomycin in AIDS-related lymphoma; efficacy data in HIV-positive subpopulation; limits generalisability to immunocompetent patients |
| [NCT00002657](https://clinicaltrials.gov/study/NCT00002657) | Phase 2 | Completed | 20 | Sequential immunosuppression reduction, interferon-α, and ProMACE-CytaBOM (bleomycin) for post-cardiac-transplant lymphoproliferation; specific transplant subgroup data |
| [NCT00003110](https://clinicaltrials.gov/study/NCT00003110) | Phase 2 | Completed | 5 | 72-hour continuous infusion bleomycin as salvage therapy in both AIDS-related and immunocompetent NHL; only trial directly evaluating bleomycin as a single salvage agent; very small sample |
| [NCT00003815](https://clinicaltrials.gov/study/NCT00003815) | Phase 3 | Unknown | N/A | High-dose chemotherapy/radiotherapy and autologous BMT in high-grade aggressive NHL (Kiel classification, overlapping with reticulum cell sarcoma); bleomycin's role within the combination regimen is not explicitly defined |
| [NCT00983944](https://clinicaltrials.gov/study/NCT00983944) | Phase 2 | Withdrawn | 0 | Comparison of EPOCH-R vs R-VACOP-B (contains bleomycin) for primary mediastinal large B-cell lymphoma; withdrawn prior to any enrolment — no data generated |

---

## Literature Evidence — Reticulum Cell Sarcoma

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [1699653](https://pubmed.ncbi.nlm.nih.gov/1699653/) | 1990 | RCT | Cancer | CALGB 7851: Randomised trial directly evaluating the addition of bleomycin and/or high-dose methotrexate to CHOP in 177 diffuse large cell lymphoma and 97 other intermediate-grade NHL patients; foundational evidence for bleomycin's role in aggressive NHL combination therapy |
| [14962711](https://pubmed.ncbi.nlm.nih.gov/14962711/) | 2004 | Long-term RCT Follow-up | Eur J Cancer | Pooled analysis of 936 patients across 3 EORTC randomised trials; CHVmP/BV (with bleomycin + vincristine) vs CHVmP and ProMACE-MOPP in advanced aggressive NHL; median follow-up 8.7 years with long-term efficacy and toxicity data |
| [4109401](https://pubmed.ncbi.nlm.nih.gov/4109401/) | 1972 | Early Clinical Trial | BMJ | **Earliest direct evidence**: Bleomycin monotherapy in 22 reticulum cell sarcoma patients (+ 54 Hodgkin's, 17 lymphosarcoma); marrow-sparing up to 800 mg total dose; response rates documented in reticulum cell sarcoma specifically |
| [65728](https://pubmed.ncbi.nlm.nih.gov/65728/) | 1977 | Clinical Trial | Med Pediatr Oncol | Randomised comparison of CVP vs ABP (adriamycin + bleomycin + prednisone) in stage IV NHL; 30 evaluable ABP patients; comparable CR rates (50%) with numerically longer CR duration in bleomycin-containing arm (20.5 vs 10.5 months) |
| [7680764](https://pubmed.ncbi.nlm.nih.gov/7680764/) | 1993 | RCT | N Engl J Med | SWOG landmark trial: CHOP vs m-BACOD, ProMACE-CytaBOM, and MACOP-B in advanced NHL; established CHOP's equivalent efficacy to third-generation bleomycin-containing regimens with lower toxic death rate; key context for modern bleomycin positioning |
| [6187214](https://pubmed.ncbi.nlm.nih.gov/6187214/) | 1983 | Case Report (Fatal Toxicity) | Am J Med | Fatal fulminant hyperpyrexia in a lymphoma patient with prior bleomycin exposure without prior reaction; underscores the unpredictability of febrile reactions and the need for vigilance beyond the first administration |
| [37294956](https://pubmed.ncbi.nlm.nih.gov/37294956/) | 2023 | Review | Hematol Oncol | Contemporary management of lymphoma in pregnancy; confirms ABVD (containing bleomycin) is considered safe after the 13th week of pregnancy; provides current risk-benefit context |
| [6205233](https://pubmed.ncbi.nlm.nih.gov/6205233/) | 1984 | Review | Med Clin North Am | Comprehensive review of NHL classification, natural history, staging, and treatment; covers bleomycin-containing combination regimens and their rationale in the era of histological reclassification from "reticulum cell sarcoma" to DLBCL |
| [15934513](https://pubmed.ncbi.nlm.nih.gov/15934513/) | 2005 | Review | Oncology | GELA 20-year experience with Phase II/III studies in aggressive lymphoma/DLBCL; discusses limitations of CHOP and the role of intensified regimens including bleomycin-containing combinations |
| [12967352](https://pubmed.ncbi.nlm.nih.gov/12967352/) | 2003 | Review | Clin Evid | Evidence-based systematic review of NHL management; evaluates the evidence base for bleomycin-containing combination regimens across histological subtypes |

---

## Philippines Market Information

Bleomycin is currently **not registered** in the Philippines. No marketing authorisations are on record in the Philippines FDA database.

| Item | Detail |
|------|--------|
| Market Status | Not Registered (未上市) |
| Total Authorisations | 0 |
| Registration Pathway | A new Drug Registration Application to the Philippines FDA would be required prior to any clinical deployment |
| International Availability | Bleomycin is available in other markets under names such as Blenoxane® (Bristol-Myers Squibb) and various generics; it is included in the WHO Model List of Essential Medicines |

---

## Cytotoxicity

Bleomycin is an antineoplastic glycopeptide antibiotic. This section applies.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic (Glycopeptide antibiotic / DNA strand-break inducer) |
| Myelosuppression Risk | **Low** — Bleomycin is notably marrow-sparing, which is a key pharmacological advantage in combination regimens such as ABVD; routine CBC monitoring is still recommended |
| Emetogenicity Classification | Low |
| Primary Organ Toxicity | **Pulmonary**: Bleomycin-induced pneumonitis and pulmonary fibrosis are dose-dependent and cumulative; risk threshold typically around 300–360 units lifetime cumulative dose; risk substantially increased by age > 60, renal impairment, concurrent G-CSF use, and prior chest irradiation |
| Monitoring Items | Pulmonary function tests (DLCO) before initiation and before each cycle or at regular intervals; renal function (bleomycin is primarily renally eliminated — dose reduction required in renal impairment); cumulative dose tracking across all treatment cycles; temperature monitoring post-infusion (acute hyperpyrexia risk) |
| Handling Protection | Must follow cytotoxic drug handling regulations (PPE, closed-system drug-transfer devices, designated preparation areas) |

---

## Safety Considerations

Formal safety data (package insert warnings and contraindications) were not available in this evidence pack. Based on toxicity data identified in the clinical literature reviewed:

- **Pulmonary toxicity**: Bleomycin-induced pneumonitis and pulmonary fibrosis are the most clinically significant toxicities; risk is amplified by increasing age (PMID 31668826), concurrent granulocyte colony-stimulating factor use, prior chest radiation, and cumulative dose exceeding 300–360 units (PMID 27742539)
- **Hyperpyrexia**: Acute and potentially fatal febrile reactions have been reported, including in patients who previously tolerated bleomycin without incident (PMID 6187214); a test dose is recommended before initiating a full course
- **Drug Interactions**: No DDI data were identified in this review

Please refer to the approved package insert for comprehensive safety information including contraindications and full warning statements.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails** *(primary indication: Reticulum Cell Sarcoma / DLBCL)*

**Rationale:**
The evidence supporting bleomycin in reticulum cell sarcoma (DLBCL) reaches Evidence Level 1 — anchored by at least three completed Phase 3 RCTs and a landmark CALGB randomised trial (PMID 1699653) directly evaluating bleomycin's contribution to CHOP in diffuse large cell lymphoma. However, the modern DLBCL standard-of-care has evolved to R-CHOP (rituximab + CHOP), where bleomycin is no longer routinely included; this means the actionable niche lies specifically in rituximab-ineligible patients, resource-constrained settings, or novel combination strategies rather than as a blanket first-line addition.

**To proceed, the following is needed:**

- **MOA data**: Retrieve complete mechanism of action details from DrugBank API (Data Gap DG002 — currently flagged as High severity)
- **Package insert review**: Download and parse the approved product monograph for formal warnings, contraindications, and dosing guidance (Data Gap DG001 — currently flagged as Blocking)
- **Current treatment context analysis**: Formally assess whether bleomycin-containing regimens offer a meaningful advantage over R-CHOP in the specific target patient population (e.g., rituximab-ineligible, CD20-negative DLBCL)
- **Pulmonary toxicity risk management protocol**: Establish a pre-treatment DLCO baseline monitoring protocol and define cumulative dose limits and stopping rules before any clinical deployment
- **Philippines registration pathway**: Initiate a Drug Registration Application with the Philippines FDA if clinical deployment is planned — no current authorisation exists and this is a prerequisite for lawful use

---

*Summary of decisions for remaining predicted indications:*

| Indication | Decision | Key Reason |
|-----------|----------|------------|
| Adult Astrocytic Tumour | Research Question (L3) | Phase I intratumoral CED trial data exists (PMID 12416544); blood-brain barrier bypass remains a key challenge; no Phase 2/3 data |
| Primary Pulmonary Lymphoma | Research Question (L3) | Indirect evidence from Hodgkin's lymphoma ABVD trials only; elevated bleomycin pulmonary toxicity risk is of particular concern in patients with primary lung involvement |
| Cauda Equina Neoplasm | Hold (L5) | No clinical trials; 3 indirect literature references only; TxGNN high score likely reflects topology-based propagation in the knowledge graph rather than a true mechanistic link |
| Pulmonary Blastoma | Hold (L4) | Only 2 case reports; bleomycin use attributable to germ cell differentiation component (BEP regimen), not to pulmonary blastoma itself |
| Well-differentiated Fetal Adenocarcinoma of the Lung | Hold (L5) | Zero clinical trials and zero literature; no mechanistic basis identified; complete absence of evidence |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

