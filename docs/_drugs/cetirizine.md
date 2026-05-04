---
layout: default
title: Cetirizine
parent: 僅模型預測 (L5)
nav_order: 68
evidence_level: L5
indication_count: 6
---

# Cetirizine
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

# Cetirizine: From Allergic Rhinitis to Allergic Urticaria

## One-Sentence Summary

Cetirizine is a second-generation, selective histamine H1-receptor antagonist widely used globally for allergic rhinitis and urticaria.
The TxGNN model predicts it may be effective for **Allergic Urticaria**, with **3 clinical trials** and **18 publications** currently supporting this direction.
While this indication is well-established internationally, Cetirizine currently has no Philippines regulatory registration, making formal market entry the primary next step.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Allergic rhinitis / chronic urticaria (globally recognized; no Philippines regulatory record available) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological information, Cetirizine is a selective histamine H1-receptor antagonist and the carboxylated metabolite of hydroxyzine. It competitively blocks peripheral H1 receptors with minimal central nervous system penetration — a key advantage over first-generation antihistamines. Beyond simple receptor blockade, Cetirizine also inhibits eosinophil chemotaxis during the late-phase allergic response, giving it an additional anti-inflammatory dimension that enhances its utility in allergic skin diseases.

Allergic urticaria is primarily driven by IgE-triggered mast cell degranulation, which floods the dermis with histamine, triggering vasodilation and increased vascular permeability — the classic wheal-and-flare reaction. Because H1-receptor activation is the central step in this cascade, the mechanistic link between Cetirizine and allergic urticaria is exceptionally direct. This is not a speculative extrapolation; it is the textbook pharmacological rationale upon which the entire second-generation antihistamine class was developed.

The TxGNN model assigns this prediction a near-perfect score (99.99%), reflecting the strength of this mechanistic relationship in the knowledge graph. US FDA and EMA have already approved Cetirizine for urticaria globally. The Evidence Level is rated L2 rather than L1 because the only identified Phase 3 trial in this pack (NCT02023164) was a feasibility pilot with only 36 patients — designed to test whether a definitive Phase 3 was feasible, not to provide confirmatory efficacy data. The weight of global regulatory approval and published literature nonetheless strongly supports clinical validity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Multicenter parallel-group pilot RCT comparing IV Cetirizine 10 mg vs. IV Diphenhydramine 50 mg for acute urticaria in emergency departments and urgent care settings; primary purpose was to establish feasibility for a subsequent definitive Phase 3 trial, with preliminary safety and efficacy signals |
| [NCT03296358](https://clinicaltrials.gov/study/NCT03296358) | N/A | Completed | 75 | Randomized double-blind trial evaluating short-burst corticosteroid added to standard H1 antihistamine treatment for urticaria; indirectly supports H1 antihistamines (the likely backbone comparator) as the established first-line standard of care |
| [NCT01008592](https://clinicaltrials.gov/study/NCT01008592) | N/A | Terminated | 11 | Investigated the effect of levocetirizine — the active R-enantiomer of cetirizine — on skin inflammatory mediators (histamine, prostaglandin E2, LTB4, cathepsins) in symptomatic dermatographism and chronic idiopathic urticaria; terminated early, providing partial mechanistic data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33030434](https://pubmed.ncbi.nlm.nih.gov/33030434/) | 2021 | Systematic Review | J Investig Allergol Clin Immunol | Critically reviewed evidence for up-dosing second-generation oral antihistamines (including cetirizine) to 4× the licensed dose in chronic spontaneous urticaria; confirms antihistamines as first-line standard, though high-dose evidence relies mainly on expert opinion |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Clinical Trial Series | Allergy | Clinical studies with cetirizine specifically in allergic rhinitis and chronic urticaria; provides direct evidence of cetirizine efficacy in urticarial conditions |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Comprehensive Drug Review | Drugs | Foundational comprehensive review of cetirizine pharmacology; confirms efficacy in chronic urticaria, absence of CNS depression at standard 10 mg dose, and additional anti-inflammatory effects including inhibition of eosinophil chemotaxis |
| [7510611](https://pubmed.ncbi.nlm.nih.gov/7510611/) | 1993 | Drug Review | Drugs | Reappraisal of cetirizine pharmacological properties; confirms effective and well-tolerated treatment for chronic idiopathic urticaria in adults at 10 mg/day |
| [8477125](https://pubmed.ncbi.nlm.nih.gov/8477125/) | 1993 | Drug Review | Ann Pharmacother | Introduction of cetirizine as a nonsedating antihistamine; covers mechanism of action, comparative clinical trials, and adverse effect profile |
| [9951950](https://pubmed.ncbi.nlm.nih.gov/9951950/) | 1999 | Comparative Review | Drugs | Head-to-head comparative review of ten second-generation antihistamines including cetirizine; evaluates sedation, anticholinergic effects, and clinical choice factors for urticaria and allergic rhinitis |
| [41602253](https://pubmed.ncbi.nlm.nih.gov/41602253/) | 2025 | Case Report | Cureus | Case of rebound pruritus and urticaria following cetirizine discontinuation after long-term use in an Asian patient; highlights a clinically relevant safety signal for chronic urticaria management in the Asian population |
| [27110120](https://pubmed.ncbi.nlm.nih.gov/27110120/) | 2016 | Review | Ther Clin Risk Manag | Reviews antihistamine treatment landscape for allergic rhinitis and urticaria; positions cetirizine as an established reference comparator within the second-generation antihistamine class |
| [35593100](https://pubmed.ncbi.nlm.nih.gov/35593100/) | 2022 | Systematic Review | Am J Rhinol Allergy | Systematic review and meta-analysis of RCTs evaluating antihistamines for allergic rhinitis and chronic urticaria; provides class-level quantitative evidence supporting H1 antagonism as the mechanistic basis for urticaria management |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | PK/Comparative Review | Clin Pharmacokinet | Comparative pharmacokinetics and pharmacodynamics of desloratadine, fexofenadine, and levocetirizine (cetirizine's active enantiomer); provides mechanistic context and PK rationale for the cetirizine class in chronic urticaria |

---

## Philippines Market Information

Cetirizine currently has **no active drug registrations** with the Philippines FDA. As of the data cutoff (2026-04-04), the market status is **Not Marketed** with a total of 0 approved licenses on record. There are no product entries to display.

This represents an administrative market gap rather than a scientific one — the drug is globally approved and widely available in most comparable markets.

---

## Safety Considerations

Please refer to the package insert for safety information. No key warnings, contraindications, or drug interaction data were retrievable from the current evidence sources for Cetirizine.

> **Note for review team:** Safety data (TFDA/FDA-approved labeling, warnings, and contraindications) has been identified as a **Blocking data gap** (DG001). The Philippines NDA submission cannot proceed to Stage 1 safety assessment until the approved package insert is obtained and parsed. In addition, a recent 2025 case report (PMID 41602253) flagged rebound pruritus/urticaria upon long-term cetirizine discontinuation in Asian patients — this should be captured in the local risk management plan.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Cetirizine's efficacy for allergic urticaria is mechanistically well-founded and globally validated by FDA and EMA approvals. The Philippines market gap is regulatory in nature — not a signal of insufficient evidence — and can be addressed through standard new drug application pathways using international reference dossiers.

**To proceed, the following is needed:**

- **Resolve Blocking Safety Gap (DG001):** Download and parse the TFDA/FDA/EMA-approved package insert PDF to extract full warnings, contraindications, and drug interaction data before entering Stage 1 safety assessment
- **Confirm MOA documentation (DG002):** Query DrugBank API (DB00341) to formally document mechanism of action for inclusion in regulatory and formulary submissions
- **File Philippines FDA registration:** Submit NDA or abbreviated NDA leveraging existing FDA/EMA approval as reference product; Cetirizine's established international safety profile should support an expedited review pathway
- **Develop rebound urticaria risk communication:** Based on the 2025 case report (PMID 41602253), prepare patient counseling materials specifically addressing discontinuation risk in chronic urticaria patients on long-term therapy — particularly relevant for the Asian patient population
- **Establish local post-marketing surveillance plan** in line with Philippines FDA pharmacovigilance requirements
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

