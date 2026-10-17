---
layout: default
title: Methylprednisolone
parent: Model Prediction Only (L5)
nav_order: 231
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Methylprednisolone: predicted new indication Alopecia areata (evidence level L5). Approved use: Autoimmune disease, adrenocortical insufficiency…"
monitor_inn: "Methylprednisolone"
predicted_indications: ["alopecia areata", "alopecia mucinosa", "telogen effluvium", "Quinquaud's folliculitis decalvans", "alopecia antibody deficiency", "hereditary hypotrichosis with recurrent skin vesicles", "alopecia-intellectual disability-hypergonadotropic hypogonadism syndrome", "atrichia with papular lesions", "alopecia universalis onychodystrophy vitiligo"]
---

# Methylprednisolone
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

# Methylprednisolone: From Autoimmune and Inflammatory Diseases to Alopecia Areata

## One-Sentence Summary

Methylprednisolone is a corticosteroid originally used for autoimmune diseases, adrenal insufficiency, Crohn disease and acute lymphoblastic leukaemia, among others.
The TxGNN model predicts it may be effective for **alopecia areata**,
with **1 clinical trial** and **20 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Autoimmune disease, adrenocortical insufficiency, Crohn disease and inflammatory bowel disease, acute lymphoblastic leukaemia, among others (no approved indication text is available for the Philippines registration) |
| Predicted New Indication | Alopecia areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 (conservative grading; see below) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, methylprednisolone is a systemic corticosteroid with broad anti-inflammatory and immunosuppressive activity. Its efficacy in autoimmune disease has been established, and mechanistically it may be applicable to alopecia areata.

Alopecia areata is a T-cell-mediated autoimmune disease in which the immune privilege of the hair follicle collapses. High-dose pulse methylprednisolone suppresses T-cell activation and cytokine production, which fits this pathogenesis and overlaps with the drug's existing autoimmune uses.

The other predicted indications in the list are much weaker. Most have no trials or literature, and several (for example atrichia with papular lesions, telogen effluvium and rare genetic hair syndromes) have no plausible corticosteroid-responsive mechanism. Idiopathic steroid-sensitive nephrotic syndrome (L4) is a plausible "research question", since corticosteroids are standard therapy, but prednisone/prednisolone is the established agent there.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Completed | 42 | Oral mega-pulse methylprednisolone in severe, therapy-resistant alopecia areata, using higher doses and more frequent pulses than earlier regimens. Randomisation and control are not confirmed in the available data, and results are not summarised. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32270396](https://pubmed.ncbi.nlm.nih.gov/32270396/) | 2020 | Systematic Review | Dermatology and Therapy | Cyclosporine with or without systemic corticosteroids in alopecia areata, with varied outcomes |
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatology Practical & Conceptual | Efficacy, relapse rates, side effects and prognostic factors of corticosteroid pulse therapy in alopecia areata |
| [28378336](https://pubmed.ncbi.nlm.nih.gov/28378336/) | 2017 | Review | International Journal of Dermatology | Treatment options for alopecia totalis and universalis; no therapy was FDA-approved at the time |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Review | Pediatric Dermatology | Dosing regimens and side effects of pulse corticosteroids in children with alopecia areata |
| [25566921](https://pubmed.ncbi.nlm.nih.gov/25566921/) | 2015 | Clinical study | Indian J Dermatol Venereol Leprol | IV methylprednisolone pulse therapy in severe alopecia areata |
| [9777767](https://pubmed.ncbi.nlm.nih.gov/9777767/) | 1998 | Open prospective study | J Am Acad Dermatol | Single IV methylprednisolone pulse in 45 patients with severe alopecia areata |
| [12746668](https://pubmed.ncbi.nlm.nih.gov/12746668/) | 2003 | Open study | Ann Dermatol Venereol | Monthly IV pulse methylprednisolone in 66 patients with severe alopecia areata |
| [22426909](https://pubmed.ncbi.nlm.nih.gov/22426909/) | 2012 | Clinical study | Saudi Medical Journal | Oral mega-pulse methylprednisolone in severe therapy-resistant alopecia areata |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Retrospective cohort | Dermatologic Therapy | Methylprednisolone alone vs. combined with methotrexate in 26 patients with extensive alopecia areata |
| [25872976](https://pubmed.ncbi.nlm.nih.gov/25872976/) | 2015 | Clinical study | Pediatric Dermatology | High relapse rates despite early IV methylprednisolone pulse therapy in severe childhood alopecia areata |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0321 | Methylprednisolone | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the data compiled for this report. Notable examples:
  - **Major**: bupropion, clarithromycin
  - **Moderate**: antidiabetic agents (metformin, pioglitazone, acarbose, canagliflozin, dapagliflozin, empagliflozin, alogliptin, saxagliptin, albiglutide, dulaglutide, chlorpropamide), amphotericin B, aprepitant, acetylsalicylic acid, and the laxatives bisacodyl and picosulfuric acid
  - **Minor**: zinc sulfate
- **Disease-level cautions (from the knowledge graph, not label text)**: Conditions flagged as contraindication-related include hypertension, congestive heart failure, hyperglycaemia, epilepsy, herpes simplex virus keratitis, measles, urea cycle disorders (carbamoyl phosphate synthetase I deficiency, citrullinemia, hyperargininemia) and pituitary hormone deficiency-related conditions.

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Alopecia areata has a clear immune-mediated rationale, one completed Phase 4 study, and a substantial body of pulse-methylprednisolone literature. Most of it is open-label, retrospective or review-level, and the literature reports high relapse rates, so the evidence is graded L2 conservatively rather than as confirmed Phase 3 RCT-level.
- The only Philippines registration is cancelled, so there is currently no marketed product locally.

**To proceed, the following is needed:**
- Review of the NCT01167946 design and results (randomisation, control arm, response and relapse outcomes)
- Package insert warnings and contraindications, and mechanism of action data
- Confirmation of a currently valid Philippines registration and suitable dosage forms or routes (oral and IV pulse regimens)
- Safety monitoring plan for high-dose pulse use, including blood pressure, glucose, infection risk and interacting drugs (particularly bupropion and clarithromycin)
- Relapse management strategy, and comparison with newer options such as JAK inhibitors where accessible
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

