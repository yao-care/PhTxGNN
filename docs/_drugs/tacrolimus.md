---
layout: default
title: Tacrolimus
parent: 僅模型預測 (L5)
nav_order: 319
evidence_level: L5
indication_count: 3
---

# Tacrolimus
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

The skill confirms this is a PhTxGNN project (Philippines TxGNN). Proceeding to generate the evaluation report now.

---

# Tacrolimus: From Atopic Dermatitis to Seborrheic Dermatitis

## One-Sentence Summary

Tacrolimus (Protopic®) is a topical calcineurin inhibitor established globally for atopic dermatitis, working by blocking T-cell-driven inflammatory cascades — though it is currently not registered in the Philippines.
The TxGNN model predicts it may be effective for **Seborrheic Dermatitis**, with **2 completed clinical trials** (including a Phase 3 RCT) and **20 publications** supporting this direction.
Evidence strength reaches **L1** — the highest tier — making this one of the strongest repurposing candidates in this analysis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atopic Dermatitis (established global indication; not registered in the Philippines) |
| Predicted New Indication | Seborrheic Dermatitis |
| TxGNN Prediction Score | 99.26% |
| Evidence Level | L1 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Tacrolimus binds to the intracellular immunophilin FKBP12, forming a complex that inhibits calcineurin — the phosphatase responsible for dephosphorylating NFAT (Nuclear Factor of Activated T-cells). By blocking NFAT nuclear translocation, tacrolimus suppresses transcription of key pro-inflammatory cytokines including IL-2, IL-4, and TNF-α. As a topical ointment, it achieves targeted immunomodulation in the skin without the systemic exposure or local side effects (particularly skin atrophy and telangiectasia) that limit long-term use of topical corticosteroids.

Seborrheic dermatitis is a chronic, relapsing inflammatory condition affecting sebaceous-gland-rich areas such as the face and scalp. While colonization by the lipophilic yeast *Malassezia* is the primary environmental trigger, the tissue damage arises from the resulting Th-cell-mediated immune response — the same calcineurin–NFAT pathway that tacrolimus directly inhibits. The mechanistic bridge between atopic dermatitis and seborrheic dermatitis is therefore not superficial: both diseases share the same downstream inflammatory mediator cascade that tacrolimus is designed to block.

There is also a strong clinical rationale specific to seborrheic dermatitis. The face is the most commonly affected site, yet it is also the area most vulnerable to steroid-induced adverse effects with prolonged use. Tacrolimus's steroid-sparing profile makes it uniquely suitable for facial seborrheic dermatitis maintenance — a use case directly supported by the Phase 3 and Phase 4 trials in this evidence pack and by published RCT results in the Journal of the American Academy of Dermatology (2021).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|--------------|
| [NCT02004860](https://clinicaltrials.gov/study/NCT02004860) | Phase 3 | Completed | 120 | Evaluated tacrolimus ointment (Protopic®) for maintenance treatment of severe seborrheic dermatitis on the adult face; assessed capacity to reduce relapse frequency, prolong remission, and reduce dependence on topical steroids. Results published as a multicenter double-blind RCT (Joly et al., JAAD 2021). |
| [NCT01591070](https://clinicaltrials.gov/study/NCT01591070) | Phase 4 | Completed | 104 | Proactive use of 0.1% tacrolimus ointment once or twice weekly in adult facial seborrheic dermatitis; demonstrated that intermittent application can maintain remission and significantly reduce exacerbation incidence in real-world clinical practice. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33010323](https://pubmed.ncbi.nlm.nih.gov/33010323/) | 2021 | Multicenter RCT | J Am Acad Dermatol | Tacrolimus 0.1% vs. ciclopiroxolamine 1% for maintenance of severe facial SD; multicenter, double-blind, randomized design — this is the primary publication of NCT02004860, providing the highest-grade direct evidence for the predicted indication |
| [24171300](https://pubmed.ncbi.nlm.nih.gov/24171300/) | 2013 | Comparative RCT | Ann Parasitol | Head-to-head RCT (n=60) comparing tacrolimus 0.03% cream vs. sertaconazole 2% cream in seborrheic dermatitis; directly evaluates anti-inflammatory vs. antifungal treatment strategies |
| [26512166](https://pubmed.ncbi.nlm.nih.gov/26512166/) | 2015 | Prospective Clinical Trial | Ann Dermatol | Maintenance therapy with 0.1% tacrolimus ointment for facial seborrheic dermatitis; demonstrated feasibility of low-dose intermittent calcineurin inhibitor regimen adapted from atopic dermatitis maintenance protocols |
| [39219446](https://pubmed.ncbi.nlm.nih.gov/39219446/) | 2024 | Cochrane Systematic Review / NMA | Clin Exp Allergy | Network meta-analysis of topical anti-inflammatory treatments for eczema conditions; contextualizes tacrolimus within the current landscape of topical immunomodulators including comparative safety and efficacy |
| [19222250](https://pubmed.ncbi.nlm.nih.gov/19222250/) | 2009 | Review | Am J Clin Dermatol | Comprehensive review of topical calcineurin inhibitors specifically for seborrheic dermatitis; summarizes pathophysiology, safety, and efficacy evidence and supports TCIs as a safe alternative to corticosteroids |
| [27804089](https://pubmed.ncbi.nlm.nih.gov/27804089/) | 2017 | Systematic Review | Am J Clin Dermatol | Systematic review of topical treatments for facial seborrheic dermatitis; positions tacrolimus alongside antifungals and keratolytics as a validated treatment option |
| [12833030](https://pubmed.ncbi.nlm.nih.gov/12833030/) | 2003 | Open Pilot Study | J Am Acad Dermatol | Earliest proof-of-concept study: 18 SD patients treated with 0.1% tacrolimus for 28 days; 61% achieved 100% clearance — established the initial clinical signal for the SD indication |
| [15461548](https://pubmed.ncbi.nlm.nih.gov/15461548/) | 2004 | Review | Expert Opin Pharmacother | Tacrolimus ointment for atopic dermatitis and other inflammatory cutaneous diseases; reviews calcineurin inhibition mechanism and its applicability across multiple inflammatory skin conditions including SD |
| [37067129](https://pubmed.ncbi.nlm.nih.gov/37067129/) | 2023 | Clinical Study | Indian J Dermatol Venereol Leprol | Oral itraconazole (2 days) plus topical tacrolimus vs. topical tacrolimus alone for SD maintenance in Vietnam; evaluates combination strategies in a Southeast Asian real-world setting directly relevant to the Philippines context |
| [19213227](https://pubmed.ncbi.nlm.nih.gov/19213227/) | 2009 | Narrative Review | J Drugs Dermatol | Overview of facial seborrheic dermatitis etiology, epidemiology, and therapeutic horizons; contextualizes the role of calcineurin inhibitors within the evolving SD treatment paradigm |

---

## Philippines Market Information

Tacrolimus is currently **not registered** with the Food and Drug Administration of the Philippines (FDA Philippines). No authorization records are available for any product, dosage form, or indication.

> **Note:** Tacrolimus ointment (Protopic®) is approved in multiple jurisdictions — including the US FDA, EMA, Japan PMDA, and Taiwan TFDA — for atopic dermatitis, and in some countries for seborrheic dermatitis maintenance. A new product registration application to FDA Philippines would be required before any local commercial use.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Formal safety data — including label warnings, contraindications, and drug–drug interaction profiles — are not available in this evidence pack. The TFDA package insert (or equivalent from FDA Philippines-recognized jurisdictions) must be reviewed before proceeding to any clinical or regulatory planning stage.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence base for tacrolimus in seborrheic dermatitis is strong and directly relevant: a completed multicenter Phase 3 RCT (NCT02004860, n=120), a Phase 4 real-world study (NCT01591070, n=104), a published multicenter double-blind RCT in JAAD (2021), and a well-established mechanistic link through calcineurin–NFAT inhibition of Th-cell-driven skin inflammation. However, tacrolimus holds **zero registrations** in the Philippines, making regulatory submission the immediate gating step before any local market development.

**To proceed, the following is needed:**

- **Safety documentation:** Obtain the Protopic® package insert (or EMA/FDA SmPC) to extract warnings, contraindications, and drug–drug interactions; this currently blocks the formal safety screening stage
- **MOA documentation:** Retrieve complete mechanism-of-action data from DrugBank or published pharmacology literature to support the regulatory dossier
- **FDA Philippines registration:** Conduct a regulatory gap analysis and prepare a new product registration (NPR) application, which may incorporate both the established atopic dermatitis indication and the seborrheic dermatitis evidence package
- **Local clinical evidence:** Consider a bridging study or post-market study in Filipino patients, particularly given the Southeast Asian relevance demonstrated by the 2023 Vietnam study (PMID 37067129)
- **Pharmacovigilance plan:** Establish monitoring protocols for known tacrolimus topical risks (application-site burning/stinging, and long-term immunosuppression considerations for sensitive facial skin areas)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

