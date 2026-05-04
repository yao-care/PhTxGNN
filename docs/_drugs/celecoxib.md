---
layout: default
title: Celecoxib
parent: 僅模型預測 (L5)
nav_order: 67
evidence_level: L5
indication_count: 10
---

# Celecoxib
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

# Celecoxib: From Osteoarthritis & Rheumatoid Arthritis to Inflammatory Spondylopathy

## One-Sentence Summary

Celecoxib is a selective cyclooxygenase-2 (COX-2) inhibitor approved internationally for osteoarthritis, rheumatoid arthritis, and acute pain management, but currently not registered in the Philippines.
The TxGNN model predicts it may be effective for **Inflammatory Spondylopathy** (encompassing ankylosing spondylitis and axial spondyloarthritis), with **multiple completed Phase 3/4 RCTs** and **20 publications** directly supporting this indication.
Among all 10 predicted candidates in this evidence pack, inflammatory spondylopathy is the sole indication reaching L1 evidence level — this is a regulatory gap, not an evidence gap.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Osteoarthritis, Rheumatoid Arthritis, Acute Pain (international approvals; no Philippines registration) |
| Predicted New Indication | Inflammatory Spondylopathy (Ankylosing Spondylitis / Axial Spondyloarthritis) |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this dataset. Based on established pharmacology, however, Celecoxib is a first-generation **selective COX-2 inhibitor (coxib class)** — the first of its kind to enter clinical practice. It selectively targets cyclooxygenase-2, the isoform specifically induced at inflammatory sites, thereby reducing prostaglandin E2 (PGE2) synthesis that drives pain, swelling, and tissue destruction. Because it spares COX-1 (which maintains the gastric mucosal barrier), it carries a substantially better gastrointestinal tolerability profile compared with non-selective NSAIDs. Its efficacy across multiple inflammatory arthritis conditions has been confirmed in hundreds of randomized controlled trials over more than two decades.

Inflammatory spondylopathy — most commonly manifesting as ankylosing spondylitis (AS) or axial spondyloarthritis (axSpA) — is driven by COX-2 overactivation in the sacroiliac joints and spine, with PGE2 fueling synovial inflammation, enthesitis, and the progressive new bone formation (syndesmophyte growth, ankylosis) that causes irreversible disability. The mechanistic fit is exceptionally direct: the pathological driver of AS/axSpA is precisely the enzyme celecoxib targets. This explains both the high TxGNN prediction score and the large body of supporting clinical evidence.

What makes this prediction particularly compelling beyond symptom control is a 2025 prospective study (PMID 39757202, BMB Reports) suggesting that **celecoxib may be the only NSAID capable of inhibiting radiographic bone progression** in spondyloarthritis — an effect potentially independent of its general anti-inflammatory COX-2 activity. If confirmed at scale, this elevates celecoxib from purely symptomatic therapy to a candidate disease-modifying agent in inflammatory spondylopathy, a distinction no other NSAID currently holds.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00648141](https://clinicaltrials.gov/study/NCT00648141) | Phase 3 | Completed | 458 | Landmark RCT: Celecoxib 200 mg QD vs 200 mg BID vs Diclofenac 75 mg SR BID in AS over 12 weeks — established celecoxib's efficacy and optimal dosing profile as a primary AS treatment |
| [NCT02528201](https://clinicaltrials.gov/study/NCT02528201) | Phase 4 | Completed | 330 | Confirmatory 12-week RCT: Celecoxib 200 mg QD vs 400 mg QD vs Diclofenac TID in AS — replicated prior Phase 3 findings and characterized dose–response relationship |
| [NCT00762463](https://clinicaltrials.gov/study/NCT00762463) | Phase 3 | Completed | 240 | Celecoxib vs Diclofenac SR in Chinese AS patients with 6-week double-blind phase plus 6-week extension — supports efficacy in Asian populations directly relevant to the Philippines context |
| [NCT02758782](https://clinicaltrials.gov/study/NCT02758782) | Phase 4 | Completed | 156 | CONSUL trial: Celecoxib + Golimumab vs Golimumab alone over 2 years — directly addresses whether adding NSAID to anti-TNF therapy retards structural spinal progression in AS |
| [NCT01934933](https://clinicaltrials.gov/study/NCT01934933) | Phase 4 | Completed | 150 | Multi-center RCT: Celecoxib 200 mg BID vs Etanercept 50 mg QW vs combination over 54 weeks in active AS — informs combination therapy strategy using MRI SPARCC score endpoints |
| [NCT04115098](https://clinicaltrials.gov/study/NCT04115098) | Phase 2 | Terminated | 42 | N-of-1 trials: selective COX-2 inhibitors vs non-selective NSAIDs in axSpA — compared disease activity, HRQoL, and proteomic biomarkers at individual patient level |
| [NCT03190603](https://clinicaltrials.gov/study/NCT03190603) | Phase 4 | Completed | 12 | MRI-based assessment of NSAID effects on inflammatory lesions in axial SpA — imaging biomarker evidence of NSAID-induced inflammation resolution in sacroiliac joints |
| [NCT05164198](https://clinicaltrials.gov/study/NCT05164198) | Phase 4 | Unknown | 448 | Multicenter study on TNFi dose optimization in stable AS — provides real-world background NSAID use and safety data in a large contemporary cohort |
| [NCT02456363](https://clinicaltrials.gov/study/NCT02456363) | Phase 2 | Unknown | 300 | Registry study of anti-TNF therapy with NSAIDs in AS — real-world safety and usage patterns from clinical practice |
| [NCT03473665](https://clinicaltrials.gov/study/NCT03473665) | Phase 4 | Terminated | 9 | Pilot RCT comparing 4 NSAIDs in axial SpA — terminated early due to insufficient enrollment; provides limited comparative pharmacodynamic data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [39757202](https://pubmed.ncbi.nlm.nih.gov/39757202/) | 2025 | Prospective Clinical Study | BMB Reports | Celecoxib is the **only NSAID** shown to inhibit radiographic bone progression in spondyloarthritis — suggests a unique disease-modifying property beyond general COX-2 inhibition |
| [38228361](https://pubmed.ncbi.nlm.nih.gov/38228361/) | 2024 | RCT Results (CONSUL) | Ann Rheum Dis | CONSUL trial: NSAIDs + Golimumab vs Golimumab alone in r-axSpA over 2 years — primary endpoint not met for structural progression, but celecoxib demonstrated safety alongside biologics |
| [40028763](https://pubmed.ncbi.nlm.nih.gov/40028763/) | 2025 | Comparative Cohort | Scand J Rheumatology | Nationwide cohort study: cardiovascular disease and GI bleeding risk are **comparable** between celecoxib and non-selective NSAIDs specifically in AS patients |
| [36800138](https://pubmed.ncbi.nlm.nih.gov/36800138/) | 2023 | Randomized Controlled Study | Clin Rheumatology | Celecoxib vs imrecoxib in axSpA — both COX-2 inhibitors reduced sacroiliac joint inflammation via bone metabolism and angiogenesis pathway modulation with measurable biomarker changes |
| [40153331](https://pubmed.ncbi.nlm.nih.gov/40153331/) | 2025 | Evidence-based Guidelines | Clin Exp Rheumatology | Expert consensus on NSAIDs across the psoriatic arthritis/SpA spectrum — contextualizes celecoxib's evidence-based role in spondyloarthritis beyond AS alone |
| [28626213](https://pubmed.ncbi.nlm.nih.gov/28626213/) | 2017 | RCT | Med Sci Monitor | Celecoxib vs imrecoxib in axSpA with DKK-1 biomarker assessment at weeks 4 and 12 — mechanistic insight into COX-2 inhibition and Wnt-mediated bone remodeling |
| [22141388](https://pubmed.ncbi.nlm.nih.gov/22141388/) | 2011 | Comprehensive Review | Drugs | Definitive clinical review of celecoxib for OA, RA, and AS — standard reference for dosing, safety profile, and approved indications |
| [17983259](https://pubmed.ncbi.nlm.nih.gov/17983259/) | 2007 | Review | Drugs | Seminal review documenting celecoxib's international approvals for OA, RA, JIA (≥2 years), and AS, with decade-long clinical experience summary |
| [20476924](https://pubmed.ncbi.nlm.nih.gov/20476924/) | 2008 | Review | Expert Rev Clin Immunology | Focused review on celecoxib in ankylosing spondylitis — discusses coxib clinical profile, cardiovascular safety debate, and positioning in AS management |
| [39315555](https://pubmed.ncbi.nlm.nih.gov/39315555/) | 2024 | Prospective Cohort | Reumatismo | Long-term liver (AST, ALT) and renal (creatinine) function in AS patients on continuous NSAID monotherapy — key safety monitoring data directly applicable to long-term use protocols |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Full safety data — including key warnings, contraindications, and drug interaction profile — was not available in this evidence pack (Data Gap DG001). The cardiovascular risk associated with selective COX-2 inhibition (prostacyclin/thromboxane imbalance) and the need for renal function monitoring during chronic use are critical considerations noted in the mechanistic analysis; these must be addressed in a complete safety review before clinical use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 and Phase 4 RCTs — including a 458-patient head-to-head trial against an active comparator (NCT00648141) and a confirmatory 330-patient study (NCT02528201) — confirm celecoxib's efficacy in ankylosing spondylitis and axial spondyloarthritis. Celecoxib holds formal AS indications in the US, EU, Japan, and multiple Asian markets; the absence of Philippines registration is a regulatory gap rather than an evidence gap, and the L1 evidence level justifies prioritizing this for formal regulatory engagement.

**To proceed, the following is needed:**

- **Philippines FDA registration pathway**: Initiate a new drug application or special compassionate use authorization specifically for the inflammatory spondylopathy / ankylosing spondylitis indication, leveraging existing Phase 3 RCT data from the global dossier
- **Complete safety package (Blocking — DG001)**: Obtain full prescribing information including contraindications, boxed warnings (cardiovascular and GI risk), and drug-drug interaction profile before any clinical use; the current dataset contains no safety data
- **Cardiovascular risk mitigation plan**: Pre-treatment screening for cardiovascular risk factors is mandatory; selective COX-2 inhibition shifts the prostacyclin/thromboxane balance and may increase thrombotic event risk, particularly in patients with pre-existing cardiovascular disease
- **Long-term monitoring protocol**: Serum creatinine (renal function), AST/ALT (liver function), and blood pressure assessment at baseline and at regular intervals during chronic therapy
- **MOA data retrieval (DG002)**: Query DrugBank API to retrieve formal mechanism of action documentation for inclusion in regulatory submission
- **Pediatric sub-indication consideration**: If the RF-positive polyarticular JIA indication (Rank 8, L3 evidence) is pursued concurrently, a weight-based dosing protocol (100 mg BID for <25 kg; 200 mg BID for ≥25 kg) and a dedicated pediatric safety monitoring plan must be developed

---

> ⚠️ **Disclaimer**: This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require formal clinical validation before clinical application. All content should be reviewed by qualified medical and regulatory professionals before any decision is made.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

