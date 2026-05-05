---
layout: default
title: Methylprednisolone
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 10
---

# Methylprednisolone
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

Using `txgnn-pipeline` skill to guide the report generation. Now producing the full evaluation report based on the Evidence Pack.

---

# Methylprednisolone: From Inflammatory/Autoimmune Conditions to Alopecia Areata

## One-Sentence Summary

Methylprednisolone is a potent synthetic glucocorticoid used broadly for its anti-inflammatory and immunosuppressive effects across a wide range of autoimmune and inflammatory conditions. The TxGNN model predicts it may be effective for **Alopecia Areata (AA)**, with **18 clinical trials** and **20 publications** retrieved in support of this direction — many of which directly evaluate methylprednisolone pulse therapy in AA patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines registration data available (drug not registered in the Philippines) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Methylprednisolone is a synthetic glucocorticoid that binds the glucocorticoid receptor (GR) and suppresses the NF-κB signalling pathway. This reduces production of pro-inflammatory cytokines — including IL-2, IL-4, IFN-γ, and TNF-α — and directly inhibits CD4⁺ and CD8⁺ T cell activation and proliferation. The net effect is broad immunosuppression with potent anti-inflammatory activity.

Alopecia Areata is an organ-specific autoimmune disease in which CD8⁺ NKG2D⁺ T cells breach the immune privilege of the hair follicle, triggering inflammatory infiltration and arresting the hair growth cycle. The pathological mechanism is directly driven by T cell activation and the cytokine milieu methylprednisolone is designed to suppress. This mechanistic alignment explains why corticosteroids — and methylprednisolone in particular — have been used in clinical practice for decades as a systemic treatment option for moderate-to-severe and therapy-resistant AA.

In practice, methylprednisolone is administered as "pulse therapy" (high-dose intravenous bolus or oral mega-pulse regimens) to achieve peak immunosuppression while limiting cumulative steroid toxicity. Multiple retrospective cohorts, open prospective studies, systematic reviews, and at least one completed Phase 4 trial (NCT01167946) document this approach in severe AA, including alopecia totalis and alopecia universalis. The TxGNN prediction is therefore mechanistically sound and supported by an established body of clinical evidence.

---

## Clinical Trial Evidence

> **Note:** Many of the 18 retrieved trials are about systemic lupus erythematosus (SLE) — a condition where alopecia is a common symptom — rather than alopecia areata specifically. The table below prioritises the trials most directly relevant to methylprednisolone or corticosteroids in alopecia areata.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01167946](https://clinicaltrials.gov/study/NCT01167946) | Phase 4 | Completed | 42 | Oral mega-pulse methylprednisolone in severe, therapy-resistant alopecia areata (including totalis and universalis subtypes). Evaluated higher doses and more frequent pulses than conventional protocols. |
| [NCT01017510](https://clinicaltrials.gov/study/NCT01017510) | Phase N/A | Unknown | 20 | Compared DERMOJET (needle-free) vs. conventional syringe for intralesional corticosteroid injection in alopecia areata. Addresses delivery method for lesion-directed steroid therapy. |
| [NCT07101471](https://clinicaltrials.gov/study/NCT07101471) | N/A | Completed | 296 | Observational safety and effectiveness study of tofacitinib in alopecia, with some participants receiving adjuvant prednisolone. Provides real-world data on steroid co-administration in alopecia. |
| [NCT05162586](https://clinicaltrials.gov/study/NCT05162586) | Phase 2 | Completed | 456 | Dose-ranging study of enpatoran in SLE and cutaneous lupus; standard-of-care background included corticosteroids. Provides disease-context and endpoint data for autoimmune hair-loss conditions. |
| [NCT06759519](https://clinicaltrials.gov/study/NCT06759519) | N/A | Completed | 621 | Multicentre retrospective-prospective observational study of active moderate-to-severe SLE in Russia. Real-world treatment patterns likely include corticosteroid use. |
| [NCT04835441](https://clinicaltrials.gov/study/NCT04835441) | Phase 2 | Completed | 76 | Acazicolcept (ALPN-101) in moderate-to-severe SLE; background steroid use documented. Indirect relevance as autoimmune disease context. |
| [NCT03843125](https://clinicaltrials.gov/study/NCT03843125) | Phase 3 | Terminated | 1,147 | Long-term baricitinib (JAK inhibitor) in SLE. Terminated. Illustrates the therapeutic landscape in autoimmune disease where steroids serve as backbone therapy. |
| [NCT03616964](https://clinicaltrials.gov/study/NCT03616964) | Phase 3 | Completed | 778 | Baricitinib vs. placebo in SLE; corticosteroid background therapy documented. Contextual data on steroid use patterns. |
| [NCT04582136](https://clinicaltrials.gov/study/NCT04582136) | Phase 3 | Active, not recruiting | 146 | Sirolimus added to standard therapy (including corticosteroids) in active SLE. Background methylprednisolone use likely documented. |
| [NCT02031822](https://clinicaltrials.gov/study/NCT02031822) | Phase N/A | Completed | 40 | Ultrasound-guided greater occipital nerve steroid injection for refractory primary headache. Demonstrates corticosteroid administration techniques relevant to nerve block contexts. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [37992355](https://pubmed.ncbi.nlm.nih.gov/37992355/) | 2023 | Review | Dermatology Practical & Conceptual | Comprehensive review of corticosteroid pulse therapy in AA: summarises efficacy, relapse rates, adverse effects, and prognostic factors across multiple pulse regimens. |
| [35986630](https://pubmed.ncbi.nlm.nih.gov/35986630/) | 2022 | Retrospective Cohort | Dermatologic Therapy | Directly compared methylprednisolone (MP) alone vs. MP + methotrexate in 26 patients with extensive AA; evaluated whether combination is superior to MP monotherapy. |
| [32270396](https://pubmed.ncbi.nlm.nih.gov/32270396/) | 2020 | Systematic Review | Dermatology and Therapy | Systematic review of cyclosporine with and without systemic corticosteroids in AA; quantifies outcomes for corticosteroid-containing regimens. |
| [25566921](https://pubmed.ncbi.nlm.nih.gov/25566921/) | 2015 | Clinical Study | Indian J Dermatol Venereol Leprol | IV methylprednisolone pulse in severe AA; evaluated response rates and durability in therapy-resistant cases. |
| [18608727](https://pubmed.ncbi.nlm.nih.gov/18608727/) | 2008 | Clinical Study | J Dermatological Treatment | Combination of cyclosporine and methylprednisolone in severe chronic AA; addresses the high recurrence after cyclosporine monotherapy by adding MP. |
| [30745958](https://pubmed.ncbi.nlm.nih.gov/30745958/) | 2019 | Clinical Study | Open Access Macedonian J Medical Sciences | Vietnamese experience with methotrexate + mini-pulse methylprednisolone in severe AA totalis/universalis; demonstrates efficacy in a resource-limited setting. |
| [22426909](https://pubmed.ncbi.nlm.nih.gov/22426909/) | 2012 | Clinical Study | Saudi Medical Journal | Intensive oral mega-pulse methylprednisolone regimen in severe forms of AA; evaluated higher doses and more frequent pulses than prior protocols. |
| [36865845](https://pubmed.ncbi.nlm.nih.gov/36865845/) | 2022 | Retrospective Study + Review | Indian Journal of Dermatology | Examined sex-based differences in AA outcomes following steroid pulse therapy; identifies prognostic subgroups for response. |
| [36461625](https://pubmed.ncbi.nlm.nih.gov/36461625/) | 2023 | Clinical Review | Pediatric Dermatology | Reviewed pulse-dose corticosteroid therapy dosing in children with AA; highlights dosing regimen variability and associated side effects in the paediatric population. |
| [9777767](https://pubmed.ncbi.nlm.nih.gov/9777777/) | 1998 | Prospective Study | J American Academy of Dermatology | Open prospective study of 45 patients receiving IV methylprednisolone pulse for severe AA; evaluated benefit in patients with ongoing hair loss of < 12 months' duration. |

---

## Philippines Market Information

Methylprednisolone is **not currently registered** in the Philippines Food and Drug Administration (FDA) database. No active licenses were retrieved.

| Item | Detail |
|------|--------|
| Registration Status | No active Philippines FDA registrations found |
| Total Licenses | 0 |

> ⚠️ This data gap should be verified directly with the Philippines FDA (FDA.gov.ph) before drawing conclusions, as methylprednisolone is a globally available generic medicine and may be marketed under brand names or as a hospital-use product not captured in this query.

---

## Safety Considerations

Detailed safety data (package insert warnings, contraindications, and drug interactions) for the Philippines market were not available in this dataset.

Please refer to the package insert for safety information.

> As a general clinical note, methylprednisolone pulse therapy carries established risks including transient hyperglycaemia, hypertension, insomnia, mood disturbance, hypothalamic-pituitary-adrenal (HPA) axis suppression, and in high cumulative doses, avascular necrosis, osteoporosis, and opportunistic infection. Patient selection and monitoring protocols are critical when using this regimen for AA.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Methylprednisolone pulse therapy has a mechanistically coherent basis for use in alopecia areata (T cell-mediated immune privilege collapse), and this is supported by a substantial body of retrospective cohort data, multiple clinical studies, systematic reviews, and a completed Phase 4 trial (NCT01167946). The evidence is sufficient to justify clinical consideration, but the absence of large, placebo-controlled RCTs and the Philippines regulatory gap require structured safeguards before wider adoption.

**To proceed, the following is needed:**

- **Philippines regulatory verification**: Confirm whether methylprednisolone is marketed locally under any brand or hospital formulary listing via direct FDA Philippines enquiry
- **Package insert and safety data**: Obtain and review the full prescribing information to complete S1 safety screening (currently a blocking data gap)
- **Mechanism of action documentation**: Retrieve full DrugBank MOA entry for methylprednisolone to strengthen the mechanistic rationale section
- **Clinician validation**: Confirm clinical feasibility with a dermatologist or clinical pharmacist experienced in AA management in the Philippines context
- **Relapse monitoring protocol**: Any application of methylprednisolone pulse in AA should include a defined relapse-monitoring plan, as high relapse rates post-treatment are well-documented (see PMID 25872976)
- **Special population assessment**: Paediatric dosing considerations require separate review (PMID 36461625) before any paediatric application
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

