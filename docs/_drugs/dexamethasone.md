---
layout: default
title: Dexamethasone
parent: 僅模型預測 (L5)
nav_order: 101
evidence_level: L5
indication_count: 10
---

# Dexamethasone
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

# Dexamethasone: From Inflammatory & Autoimmune Conditions to Alopecia Areata

---

## One-Sentence Summary

Dexamethasone is a potent synthetic glucocorticoid widely used for inflammatory conditions, allergic disorders, autoimmune diseases, and as supportive care in oncology.
The TxGNN model predicts it may be effective for **Alopecia Areata**, with **1 RCT**, **1 meta-analysis**, and **20 publications** in total currently supporting this direction.
While no Philippines FDA registrations are currently on file, the clinical literature for this repurposing direction is substantive and mechanistically grounded.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines registration on file; widely established for inflammatory and immune disorders |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Philippines Market Status | Not Marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Alopecia areata (AA) is an autoimmune condition in which autoreactive CD8+ T cells breach and destroy the immune privilege of the hair follicle — a normally protected microenvironment — triggering the characteristic patchy, non-scarring hair loss. This immunological mechanism makes AA a logical target for a broad-spectrum immunosuppressant like dexamethasone. Specifically, dexamethasone is thought to act through three complementary pathways in AA: (1) suppressing T cell activation and blocking the secretion of pro-inflammatory cytokines including IL-2 and IFN-γ that drive perifollicular inflammation; (2) inducing lymphocyte apoptosis to directly deplete the autoreactive T cell pool; and (3) inhibiting NF-κB signaling to reduce the density of inflammatory infiltrate surrounding affected follicles.

The clinical translation of this mechanism is most clearly seen in the **Oral Mini-Pulse (OMP) regimen** — typically 5 mg dexamethasone administered on two consecutive days per week. This pulsed approach is designed to deliver immunosuppression sufficient to arrest the autoimmune attack while substantially reducing the cumulative dose and thus the risk of continuous hypothalamic-pituitary-adrenal (HPA) axis suppression. This is an important advantage over daily corticosteroid regimens and underpins the published clinical evidence summarised below.

Detailed mechanism of action data is not currently available in this Evidence Pack (Data Gap DG002). However, based on well-established glucocorticoid pharmacology and the repurposing rationale derived from the clinical literature, the mechanistic link between dexamethasone and alopecia areata is considered clear and clinically validated. The OMP regimen in particular has been studied in prospective, comparative, and randomised settings across adult and paediatric populations.

---

## Clinical Trial Evidence

> **Important context:** The 13 trials retrieved from ClinicalTrials.gov all involve dexamethasone in an **oncology supportive care role** (chemotherapy premedication, anti-emetic, steroid cover for infusion reactions). None were designed to evaluate dexamethasone as a primary treatment for alopecia areata. The two trials below are presented as the most contextually useful for safety reference purposes. The primary evidence base for this repurposing direction is the literature, not registered trials.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04343560](https://clinicaltrials.gov/study/NCT04343560) | N/A | Completed | 380 | Observational study assessing effects of long-term glucocorticoid exposure (via dexamethasone suppression testing) on bone density, body composition, and fracture risk in patients with mild autonomous cortisol secretion — provides a relevant long-term safety reference for systemic steroid use |
| [NCT02288078](https://clinicaltrials.gov/study/NCT02288078) | Phase 2 | Unknown | 74 | Randomised, placebo-controlled trial of prophylactic oral dexamethasone for fatigue and malaise from regorafenib treatment — evaluates systemic tolerability of oral dexamethasone as primary endpoint; indirect safety reference |

*Remaining 11 retrieved trials use dexamethasone as premedication in chemotherapy regimens and are not directly relevant to alopecia areata treatment.*

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36086930](https://pubmed.ncbi.nlm.nih.gov/36086930/) | 2022 | RCT | Dermatologic Therapy | Randomised open-label study in 30 children with severe AA; compared dexamethasone OMP vs. DPCP contact sensitisation — establishes direct efficacy and safety data for dexamethasone as primary AA treatment in paediatric patients |
| [36070222](https://pubmed.ncbi.nlm.nih.gov/36070222/) | 2022 | Meta-analysis | Dermatologic Therapy | Multi-centre meta-analysis of oral dexamethasone mini-pulse for moderate-to-severe AA (including totalis/universalis subtypes); assessed response rates, relapse, and tolerability across multiple centres in Europe |
| [39042154](https://pubmed.ncbi.nlm.nih.gov/39042154/) | 2024 | Systematic Review / NMA | Archives of Dermatological Research | Network meta-analysis (PRISMA) comparing systemic steroids, oral JAK inhibitors, and contact immunotherapy for severe AA (SALT ≥50%); contextualises dexamethasone relative to newer agents including baricitinib |
| [35330017](https://pubmed.ncbi.nlm.nih.gov/35330017/) | 2022 | Prospective Cohort | Journal of Clinical Medicine | Real-world evidence on dexamethasone mini-pulse OMP in AA patients; assessed effectiveness, adverse effects, and explored predictors of successful response in clinical practice setting |
| [31579982](https://pubmed.ncbi.nlm.nih.gov/31579982/) | 2019 | Retrospective Cohort | Dermatologic Therapy | 73 children with severe AA (>30% scalp involvement); compared 1-day vs. 3-day intravenous dexamethasone pulse regimens monthly combined with topical clobetasol over 6–12 months; >50% regrowth defined as good response |
| [26179196](https://pubmed.ncbi.nlm.nih.gov/26179196/) | 2015 | Longitudinal Cohort | Dermatologic Therapy | Long-term follow-up (median 96 months) of 65 children with severe AA treated with oral dexamethasone pulse; provides durability data well beyond short-term efficacy studies |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Clinical Review | Pediatric Dermatology | Systematic review of dosing regimens for pulse-dose corticosteroid therapy (PDCT) in children with AA; evaluates dosing approaches and associated side effect profiles to guide clinical use |
| [41243342](https://pubmed.ncbi.nlm.nih.gov/41243342/) | 2025 | Case Series | Journal of Dermatological Treatment | Documents durable remission of severe AA with dexamethasone oral mini-pulse in patients ineligible for or lacking access to JAK inhibitors; supports OMP as a viable alternative in resource-limited or contraindicated settings |
| [10535249](https://pubmed.ncbi.nlm.nih.gov/10535249/) | 1999 | Clinical Study | Journal of Dermatology | Early pivotal study of twice-weekly 5 mg oral dexamethasone pulse in 30 patients with extensive AA (mean disease duration 4.2 years); evaluated terminal hair regrowth at minimum 12 weeks of treatment |
| [16707886](https://pubmed.ncbi.nlm.nih.gov/16707886/) | 2006 | Comparative Study | Dermatology (Basel) | Head-to-head comparison of efficacy, relapse rate, and side effects among three systemic corticosteroid modalities for extensive AA; positions dexamethasone OMP within broader corticosteroid treatment landscape |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Philippines FDA registration data and formal package insert warnings were unavailable in this Evidence Pack (Data Gap DG001). Based on the well-established pharmacological profile of systemic corticosteroids, clinicians should be alert to the following class-level risks when using dexamethasone for alopecia areata:
>
> - **HPA axis suppression**: Even OMP regimens carry suppression risk with prolonged use — periodic morning cortisol monitoring is recommended
> - **Metabolic effects**: Hyperglycaemia, weight gain, and dyslipidaemia are dose- and duration-dependent
> - **Immunosuppression**: Increased susceptibility to bacterial, fungal, and opportunistic infections
> - **Bone health**: Risk of osteoporosis and avascular necrosis with long-term use; baseline and periodic DXA scanning is advisable
> - **Paediatric-specific concerns**: Growth suppression is a recognised risk with prolonged corticosteroid exposure in children

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple clinical studies — including a randomised controlled trial in paediatric AA, a multi-centre meta-analysis, a network meta-analysis, and multiple prospective and retrospective cohort studies — directly support the efficacy of oral dexamethasone mini-pulse for alopecia areata. The mechanistic basis is well-established, the OMP dosing strategy provides a practical risk-mitigation approach, and the treatment is particularly relevant in settings where JAK inhibitors are unavailable or contraindicated.

**To proceed, the following is needed:**

- **Philippines FDA (FDA-PH) regulatory gap closure**: Confirm whether any dexamethasone products are registered for inflammatory or autoimmune indications in the Philippines and whether an off-label use pathway applies (Data Gap DG001)
- **Formal safety document review**: Download and parse the TFDA/FDA-PH package insert PDF for approved warnings, contraindications, and drug-drug interactions (Data Gap DG001)
- **MOA documentation**: Query DrugBank API to formally capture mechanism of action data for DB01234 (Data Gap DG002)
- **Clinical safety monitoring plan**: Define HPA axis monitoring schedule, glycaemic surveillance, bone density baseline, and infection risk stratification for the OMP regimen in the Philippine setting
- **Head-to-head positioning against JAK inhibitors**: The 2024 network meta-analysis (PMID 39042154) suggests JAK inhibitors may show superior efficacy for severe AA — a formal health technology assessment comparing dexamethasone OMP vs. baricitinib in the Philippine reimbursement context is recommended
- **Paediatric dosing protocol**: Establish a standardised dosing algorithm for patients under 18 years based on the reviewed literature, given the substantial paediatric evidence base

---

*This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

