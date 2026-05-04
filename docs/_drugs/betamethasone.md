---
layout: default
title: Betamethasone
parent: 僅模型預測 (L5)
nav_order: 40
evidence_level: L5
indication_count: 10
---

# Betamethasone
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

# Betamethasone: From Inflammatory/Autoimmune Conditions to Alopecia Areata

## One-Sentence Summary

Betamethasone is a potent synthetic glucocorticoid widely used for its anti-inflammatory and immunosuppressive properties across a broad range of inflammatory and autoimmune conditions.
The TxGNN model predicts it may be effective for **Alopecia Areata**, with **7 clinical trials** and **20 publications** currently supporting this direction — the strongest evidence among all 10 predicted indications in this report.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines FDA registration data available (betamethasone is a well-established glucocorticoid for inflammatory/autoimmune conditions) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Betamethasone is a synthetic glucocorticoid that acts primarily through activation of the glucocorticoid receptor (GR-α). Its core mechanisms include: (1) downregulation of Th1 pro-inflammatory cytokines such as IL-2, IFN-γ, and TNF-α; (2) induction of T-cell apoptosis; (3) upregulation of TGF-β to restore immune privilege microenvironments; and (4) suppression of NF-κB activation. Currently, detailed mechanism of action data from DrugBank is not available in this dataset, but betamethasone's pharmacodynamic profile is well-characterized in the wider literature.

Alopecia areata (AA) is an autoimmune disorder in which CD8+ NKG2D+ T cells breach the hair follicle's immune privilege zone and launch a targeted attack on the follicle. This pathology maps directly onto betamethasone's mechanisms: suppressing T-cell-mediated cytokine cascades, inducing apoptosis of the attacking lymphocytes, and re-establishing the TGF-β-dependent immune privilege environment that protects hair follicles under normal conditions.

What makes this prediction especially robust is the convergence of mechanism with multi-route clinical validation. Topical formulations (dipropionate), intralesional injection (acetonide), and oral mini-pulse regimens have each been studied in controlled trials for AA, and all three routes have demonstrated clinical benefit. This breadth of validated delivery options considerably strengthens the translational case.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT06786689](https://clinicaltrials.gov/study/NCT06786689) | Phase 2 | Completed | 60 | Head-to-head RCT comparing betamethasone oral mini-pulse (BOMP) vs. weekly azathioprine pulse in moderate-to-severe AA; primary betamethasone intervention with full efficacy and safety data |
| [NCT05803070](https://clinicaltrials.gov/study/NCT05803070) | N/A | Unknown | 59 | Topical cetirizine 1% vs. topical betamethasone valerate 0.1% in localized AA; direct head-to-head comparison with betamethasone as the reference standard |
| [NCT06087796](https://clinicaltrials.gov/study/NCT06087796) | Phase 1 | Unknown | 60 | Topical pentoxifylline 2% gel and topical metformin 10% gel vs. topical betamethasone valerate 0.1% cream in patchy AA; betamethasone as active comparator, control-arm data extractable |
| [NCT02350023](https://clinicaltrials.gov/study/NCT02350023) | Phase 4 | Completed | 50 | First head-to-head comparison of topical betamethasone vs. topical latanoprost in localized AA; completed trial with efficacy endpoint data |
| [NCT03535233](https://clinicaltrials.gov/study/NCT03535233) | Phase 4 | Completed | 40 | Combined topical minoxidil 5% + potent topical corticosteroid (including betamethasone-class agents) vs. intralesional triamcinolone in AA; comparative design |
| [NCT04207931](https://clinicaltrials.gov/study/NCT04207931) | Phase 4 | Recruiting | 250 | Multicenter study of Central Centrifugal Cicatricial Alopecia (CCCA) treatment outcomes; different alopecia subtype — indirect class-level reference only |
| [NCT01111981](https://clinicaltrials.gov/study/NCT01111981) | Phase 4 | Unknown | 30 | Clobetasol propionate 0.05% foam in CCCA; different drug and different alopecia subtype — indirect corticosteroid class reference only |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [37870096](https://pubmed.ncbi.nlm.nih.gov/37870096/) | 2023 | Network Meta-analysis | *Cochrane Database of Systematic Reviews* | Comprehensive NMA of all AA treatments including topical and systemic corticosteroids; highest-level evidence synthesis for the field |
| [39393548](https://pubmed.ncbi.nlm.nih.gov/39393548/) | 2025 | RCT | *J Am Acad Dermatol* | Microneedle transdermal delivery of compound betamethasone in AA; demonstrated comparable efficacy to intralesional injection with significantly reduced patient pain |
| [40519428](https://pubmed.ncbi.nlm.nih.gov/40519428/) | 2025 | Prospective Clinical Study | *Cureus* | Oral betamethasone mini-pulse regimen in moderate-to-severe AA; evaluates efficacy, safety, and feasibility of intermittent systemic dosing |
| [38623137](https://pubmed.ncbi.nlm.nih.gov/38623137/) | 2024 | RCT | *Cureus* | Topical betamethasone dipropionate vs. topical minoxidil in AA; direct comparative efficacy trial |
| [34400956](https://pubmed.ncbi.nlm.nih.gov/34400956/) | 2021 | RCT | *Iran J Pharm Res* | Randomized double-blind placebo-controlled trial: oral betamethasone pulse (3 mg/week) vs. methotrexate vs. combination in severe AA (n=36) |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | *Dermatol Pract Concept* | Systematic review of corticosteroid pulse therapy in AA: efficacy rates, relapse patterns, adverse effects profile, and prognostic factors |
| [32594786](https://pubmed.ncbi.nlm.nih.gov/32594786/) | 2022 | RCT | *J Dermatol Treat* | Within-patient randomized controlled trial directly comparing intralesional betamethasone vs. intralesional triamcinolone acetonide in localized AA |
| [36257912](https://pubmed.ncbi.nlm.nih.gov/36257912/) | 2022 | Comparative RCT | *Dermatol Ther* | Six-arm blinded RCT evaluating latanoprost vs. minoxidil vs. betamethasone and combinations in AA (n=108 total, 18 per arm) |
| [36114868](https://pubmed.ncbi.nlm.nih.gov/36114868/) | 2023 | Comparative RCT | *Arch Dermatol Res* | Fractional CO₂ laser alone vs. in combination with betamethasone valerate in AA; clinical and dermoscopic outcome evaluation |
| [26691357](https://pubmed.ncbi.nlm.nih.gov/26691357/) | 2015 | Comparative Study | *J Coll Physicians Surg Pak* | Intralesional triamcinolone acetonide vs. topical betamethasone valerate in localized AA; early controlled comparison supporting topical betamethasone as a standard-of-care reference |

---

## Philippines Market Information

Betamethasone has **no registered products** in the Philippines FDA database based on available data (0 licenses, status: Not Marketed).

> **Important Note:** This likely reflects a data gap rather than true unavailability. Betamethasone is one of the most widely distributed generic corticosteroids globally and is included on the WHO Essential Medicines List. Direct verification with the Philippines FDA (Food and Drug Administration) registry is strongly recommended before drawing regulatory conclusions.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Betamethasone in alopecia areata is supported by a Cochrane Network Meta-analysis, multiple completed RCTs, and a mechanistically coherent immunosuppressive rationale (GR-α activation → T-cell suppression → restoration of follicular immune privilege). The evidence base meets L1 criteria and spans three clinically validated routes of administration, making this a strong repurposing candidate.

**To proceed, the following is needed:**
- Verify Philippines FDA registration status directly with the FDA Philippines registry, as current data showing 0 registrations likely reflects a data coverage gap rather than genuine absence from the market
- Obtain the full betamethasone package insert to document warnings, contraindications, and drug-drug interactions — currently all safety fields are absent from this evidence pack
- Retrieve DrugBank MOA data (DB00443) to formally document the glucocorticoid receptor mechanism for regulatory dossier purposes
- Define the target indication scope: clarify whether to pursue topical (dipropionate for mild/localized AA), intralesional (acetonide for patchy AA), or oral mini-pulse (moderate-to-severe AA), as each route has distinct evidence, safety profiles, and regulatory implications
- Establish a monitoring plan covering: HPA axis suppression (systemic routes), local skin atrophy (topical routes), infection risk, metabolic effects, and adrenal recovery during tapering
- Confirm that any submission pathway accounts for the lack of formal Phase 3 data specifically in the Philippines patient population, and assess whether bridging studies are required by the Philippines FDA
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

