---
layout: default
title: Mercaptopurine
parent: 僅模型預測 (L5)
nav_order: 221
evidence_level: L5
indication_count: 10
---

# Mercaptopurine
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

# Mercaptopurine: From Acute Lymphoblastic Leukemia to Myeloid Leukemia

## One-Sentence Summary

Mercaptopurine (6-MP) is a purine analog antimetabolite established as the global backbone of acute lymphoblastic leukemia (ALL) maintenance therapy for over six decades.
The TxGNN model predicts it may be effective for **Myeloid Leukemia**, with **29 clinical trials** and **20 publications** currently supporting this direction.
Historical RCTs confirm 6-MP's activity in AML induction and APL maintenance, and two active Phase 1/2 trials are now re-evaluating 6-MP in modern AML combination regimens.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute Lymphoblastic Leukemia (ALL) — global standard maintenance therapy |
| Predicted New Indication | Myeloid Leukemia |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is not available in this Evidence Pack. However, based on well-established clinical pharmacology, mercaptopurine is a purine analog that is intracellularly converted to thioguanine nucleotides (TGNs) — the primary active species. TGNs are incorporated into DNA in place of natural purines, blocking DNA replication and triggering cell death. In parallel, 6-MP inhibits de novo purine biosynthesis by suppressing multiple key enzymes (PPAT, ATIC, adenylosuccinate synthetase), depleting the nucleotide pool required for rapid cell division. This dual mechanism is selectively cytotoxic to rapidly proliferating cells such as leukemic blasts.

Both ALL (where 6-MP is the maintenance backbone) and myeloid leukemia share a defining pathological feature: uncontrolled proliferation of immature hematopoietic blast cells that are highly dependent on continuous purine synthesis. While myeloid blasts differ from lymphoid blasts in lineage and surface markers, they are equally vulnerable to antimetabolite-mediated nucleotide depletion. This mechanistic overlap — rather than mere TxGNN structural inference — is supported by decades of real clinical use: 6-MP was historically incorporated into AML induction protocols (JALSG-AML92 RCT in Japan) and remains part of acute promyelocytic leukemia (APL) maintenance regimens worldwide (AIDA, PETHEMA LPA 2005, NCT00003934).

There is currently renewed clinical interest in 6-MP for myeloid disease in a new context: combination with novel agents. NCT05506332 (the ApoAML trial) directly evaluates venetoclax + 6-MP in relapsed/refractory AML based on the hypothesis that purine analog-mediated DNA damage synergizes with Bcl-2 inhibition. NCT06199557 tests 6-MP + valproic acid in AML/high-risk MDS patients unfit for intensive chemotherapy — an underserved population with few effective oral options. These trials position 6-MP not as a standalone legacy drug but as a potential partner in mechanism-based modern combinations.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00003934](https://clinicaltrials.gov/study/NCT00003934) | Phase 3 | Completed | 420 | Randomized APL trial directly comparing tretinoin + combination chemo with or without ATO, followed by **mercaptopurine + methotrexate** maintenance; establishes 6-MP/MTX as the standard APL maintenance backbone |
| [NCT01064557](https://clinicaltrials.gov/study/NCT01064557) | N/A | Unknown | 1,068 | AIDA protocol for APL (1993–2020): evaluates intermittent ATRA vs. **MTX + 6-MP** maintenance in PCR-negative patients; largest APL dataset incorporating 6-MP maintenance |
| [NCT00002701](https://clinicaltrials.gov/study/NCT00002701) | Phase 3 | Unknown | 750 | APL Phase 3: ATRA + Idarubicin induction → intensive consolidation → randomized maintenance including 6-MP; evaluates transplant vs. chemotherapy in PCR-positive patients |
| [NCT00408278](https://clinicaltrials.gov/study/NCT00408278) | Phase 4 | Completed | 300 | PETHEMA LPA 2005: risk-adapted APL protocol with ATRA + anthracycline induction/consolidation, followed by **ATRA + MTX + 6-MP** maintenance; evaluates mitoxantrone reduction in low/intermediate risk |
| [NCT00136084](https://clinicaltrials.gov/study/NCT00136084) | Phase 3 | Completed | 238 | Multi-arm AML trial comparing two cytarabine-based induction regimens in newly diagnosed AML patients; collaborative design with 6-MP as potential maintenance component |
| [NCT00962767](https://clinicaltrials.gov/study/NCT00962767) | Phase 3 | Completed | 168 | Randomized APL trial: gemtuzumab ozogamicin vs. ATRA + chemotherapy (including 6-MP) as post-consolidation maintenance in intermediate/high-risk patients |
| [NCT00465933](https://clinicaltrials.gov/study/NCT00465933) | Phase 4 | Completed | N/A | APL AIDA protocol (1999–2007): ATRA + Idarubicin induction with dose reduction in elderly (≥70 years), **MTX + mercaptopurine** maintenance; also evaluates 6-MP in APL molecular/haematological relapse salvage |
| [NCT00866918](https://clinicaltrials.gov/study/NCT00866918) | Phase 3 | Completed | 106 | Risk-adapted childhood APL trial using ATO during consolidation; standard maintenance phase incorporates 6-MP backbone |
| [NCT06199557](https://clinicaltrials.gov/study/NCT06199557) | Phase 1/2 | Recruiting | 48 | **Active trial directly testing 6-MP + valproic acid in AML/high-risk MDS** patients unfit for standard induction (2024–2029); oral regimen targeting elderly/frail patients |
| [NCT05506332](https://clinicaltrials.gov/study/NCT05506332) | Phase 1 | Recruiting | 10 | **ApoAML trial: directly evaluates venetoclax + 6-MP (purine analog combination) in relapsed/refractory AML** (2022–2026); novel mechanistic rationale combining Bcl-2 inhibition with antimetabolite |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10497848](https://pubmed.ncbi.nlm.nih.gov/10497848/) | 1999 | RCT | Int J Hematology | JALSG-AML92 study: randomized trial of daunorubicin + behenoyl cytarabine + **6-MP** (BHAC-DM) vs. BHAC-DM + etoposide in adult AML; CR ~63%; establishes 6-MP as integral component of Japanese AML induction standard |
| [8174198](https://pubmed.ncbi.nlm.nih.gov/8174198/) | 1994 | RCT | Cancer Chemother Pharmacol | Nationwide Japan randomized trial (n=360): BH-AC·DMP (with **6-MP**) CR 63.7% vs. BH-AC·AMP 53.9%; largest early RCT validating 6-MP-containing regimen in AML; Japan Leukemia Study Group multicenter |
| [26425037](https://pubmed.ncbi.nlm.nih.gov/26425037/) | 2015 | Prospective Cohort | J Korean Med Sci | Oral **6-MP + weekly MTX** maintenance for 2 years in transplant-ineligible AML patients after first CR; demonstrates improved leukemia-free and overall survival vs. no maintenance |
| [9095207](https://pubmed.ncbi.nlm.nih.gov/9095207/) | 1997 | Clinical Trial | Cancer Invest | High-dose continuous IV **6-MP** + intermediate-dose cytarabine in AML first remission (pediatric, n=17); 14/17 patients achieved CR; establishes feasibility of HD 6-MP intensification in AML |
| [1793832](https://pubmed.ncbi.nlm.nih.gov/1793832/) | 1991 | Clinical Trial | Int J Hematology | Intensive individualized induction with behenoyl cytarabine + daunorubicin + **6-MP** in 41 adult AML patients; 71% CR rate; validates 3-drug 6-MP-containing induction |
| [1059498](https://pubmed.ncbi.nlm.nih.gov/1059498/) | 1975 | Clinical Trial | Cancer | 18 children with AML treated with cytarabine + daunorubicin + prednisolone + **mercaptopurine** or thioguanine; 78% initial CR rate, 93% in protocol completers; foundational pediatric AML data |
| [28835099](https://pubmed.ncbi.nlm.nih.gov/28835099/) | 2017 | In Vitro | Biomacromolecules | CD44-targeted glutathione-sensitive hyaluronic acid-**6-MP** prodrug nanoparticles show enhanced cytotoxicity in AML cells vs. free 6-MP; supports novel delivery strategies to overcome bioavailability limitations |
| [24492035](https://pubmed.ncbi.nlm.nih.gov/24492035/) | 2014 | Review | Jpn J Clin Hematology | Japanese review of current AML/APL therapy; contextualizes 6-MP's historical role in APL maintenance within modern ATRA + arsenic trioxide landscape |
| [5220682](https://pubmed.ncbi.nlm.nih.gov/5220682/) | 1966 | Case Series | Minnesota Med | Among the earliest reports of AML treated with **6-MP** + cyclophosphamide; historical documentation of 6-MP cytotoxic activity in myeloid leukemia |
| [265178](https://pubmed.ncbi.nlm.nih.gov/265178/) | 1977 | Case Series | Blood | Three juvenile CML cases showing clinical and hematologic response to sequential subcutaneous cytarabine + oral **mercaptopurine**; demonstrates 6-MP activity in chronic myeloid disease |

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Purine analog / Thiopurine antimetabolite |
| Myelosuppression Risk | **High** — Neutropenia and thrombocytopenia are dose-limiting; risk is substantially amplified in patients with TPMT or NUDT15 loss-of-function variants (NUDT15 c.415C>T carrier frequency ~10–20% in Southeast Asian populations including Filipinos) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential (weekly at treatment initiation, monthly during stable maintenance), liver function tests (ALT, AST, bilirubin — hepatotoxicity is a recognized toxicity), TPMT and NUDT15 genotyping before initiation |
| Handling Protection | Must follow cytotoxic drug handling regulations; wear gloves when handling tablets; do not crush or split; dispose as cytotoxic waste |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials directly incorporating mercaptopurine in myeloid leukemia (especially APL) maintenance regimens, combined with historical RCTs demonstrating 6-MP activity in AML induction, provide sufficient mechanistic and clinical evidence to justify further evaluation. Two active Phase 1/2 trials (NCT05506332, NCT06199557) confirm ongoing scientific interest in 6-MP for AML. However, 6-MP is not registered in the Philippines, package insert safety data is unavailable, and Asian-specific pharmacogenomic risks require mandatory pre-treatment assessment.

**To proceed, the following is needed:**
- Philippines FDA registration or compassionate use pathway assessment
- Full package insert review for complete warnings, contraindications, and drug interactions (including allopurinol — a major 6-MP interaction partner — and azathioprine co-use prohibition)
- Mandatory pre-treatment TPMT and NUDT15 genotyping protocol, with standardized dose-reduction guidelines for Southeast Asian variant carriers (particularly NUDT15 c.415C>T)
- Clear definition of target patient population: APL maintenance (established role), AML unfit for intensive therapy (NCT06199557 context), or relapsed/refractory AML (NCT05506332 context)
- Hepatotoxicity and myelosuppression monitoring plan, with CBC and LFT frequency schedule
- Confirmation of oral formulation (tablet or suspension) availability and supply chain for the Philippines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

