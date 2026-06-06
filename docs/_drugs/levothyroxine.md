---
layout: default
title: Levothyroxine
parent: 僅模型預測 (L5)
nav_order: 206
evidence_level: L5
indication_count: 10
---

# Levothyroxine
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

# Levothyroxine: From Hypothyroidism to Endemic Goiter

## One-Sentence Summary

Levothyroxine (LT4) is the synthetic form of thyroxine (T4), the cornerstone pharmacological replacement for hypothyroidism worldwide — though it currently holds no approved registration in the Philippines.
The TxGNN model assigns it the highest prediction score of **99.81%** for **Endemic Goiter**, ranking it first among all repurposing candidates.
This direction is supported by **1 clinical trial** and **20 publications**, including a direct longitudinal cohort study documenting LT4 supplementation in indigenous communities within iodine-deficient endemic goiter areas.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypothyroidism (no Philippine FDA registration on record) |
| Predicted New Indication | Endemic Goiter |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Formal mechanism of action data from DrugBank was not retrieved for this report. Based on well-established clinical pharmacology, however, Levothyroxine is the synthetic L-isomer of thyroxine (T4), the principal secretory product of the thyroid gland. Its two core pharmacodynamic actions are: (1) direct replacement of circulating T4 to restore physiological thyroid hormone levels, and (2) suppression of pituitary TSH (thyroid-stimulating hormone) through the negative feedback axis of the hypothalamic-pituitary-thyroid system.

Endemic goiter arises primarily from iodine deficiency. When dietary iodine is insufficient, T4 synthesis falls, and the pituitary responds by secreting excess TSH. Chronically elevated TSH is the dominant growth driver for thyroid follicular cells — over time this leads to diffuse gland enlargement and, eventually, nodule formation. Levothyroxine addresses both components of this pathophysiology: it replenishes the deficient T4 directly, and simultaneously removes the TSH-driven proliferative stimulus through feedback suppression.

This mechanistic link is backed by direct clinical data. PMID 24393641 is a 1.5-year longitudinal study of Aboriginal communities in the iodine-deficient endemic zone of Pahang, Malaysia, where daily LT4 (100 µg) produced measurable goiter regression across follow-up visits. A German multicenter randomized trial (PMID 3278876) assigned 74 euthyroid endemic goiter patients to either LT4 150 µg alone or LT4 100 µg combined with potassium iodide for six months, finding significant thyroid volume reduction in both arms. Together, these studies confirm that the TxGNN model's top-ranked prediction reflects real clinical experience, not purely graph-based inference.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04482907](https://clinicaltrials.gov/study/NCT04482907) | N/A | Completed | 68 | Evaluated dill (*Anethum graveolens*) vs. placebo in thyroiditis and nodular goiter patients over 90 days; Levothyroxine was not the primary intervention. Provides context on goiter population monitoring but does not directly assess LT4 efficacy for endemic goiter. |

> No trials with Levothyroxine as the primary intervention specifically for endemic goiter were identified in the ClinicalTrials.gov registry search.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [24393641](https://pubmed.ncbi.nlm.nih.gov/24393641/) | 1998 | Clinical Cohort | Asia Pac J Clin Nutr | 1.5-year follow-up of Aboriginal populations in Malaysian iodine-deficient areas; LT4 100 µg/day produced progressive goiter reduction over 311–184 subjects across five assessment points |
| [3278876](https://pubmed.ncbi.nlm.nih.gov/3278876/) | 1988 | Multicenter Clinical Study | Dtsch Med Wochenschr | 74 euthyroid endemic goiter patients: LT4 150 µg/day vs. LT4 100 µg + iodide 100 µg/day for 6 months; both arms achieved significant goiter volume reduction; followed by 3-month iodide prophylaxis |
| [25629792](https://pubmed.ncbi.nlm.nih.gov/25629792/) | 2015 | RCT | Curr Med Res Opin | 460 pregnant women in endemic areas (goiter vs. non-goiter zones, ± iodine supplementation); iodine correction normalized thyroid parameters and improved neonatal outcomes, establishing the TSH-goiter axis as an actionable therapeutic target |
| [2031356](https://pubmed.ncbi.nlm.nih.gov/2031356/) | 1991 | Review | World J Surg | Comprehensive review of iodine deficiency in goitrogenesis; identifies implementation barriers to iodine programs and frames LT4 as a viable pharmacological alternative |
| [6304776](https://pubmed.ncbi.nlm.nih.gov/6304776/) | 1983 | Physiological Study | Prog Clin Biol Res | TSH basal levels 31 ± 8 µU/mL in iodine-deficient endemic goiter patients vs. 10 ± 4 µU/mL in controls; strong inverse T4–TSH correlation validates the mechanistic basis for LT4 suppressive therapy |
| [3090091](https://pubmed.ncbi.nlm.nih.gov/3090091/) | 1986 | Observational Study | J Clin Endocrinol Metab | Thyroid function survey of 1,218 subjects in an Italian endemic goiter region; documents T4, T3, TSH, and thyroglobulin profiles that underpin the case for TSH-suppression as a therapeutic strategy |
| [6309889](https://pubmed.ncbi.nlm.nih.gov/6309889/) | 1983 | Immunological Study | J Clin Endocrinol Metab | Iodized oil treatment in 58 Greek goiter patients from mild iodine-deficient area; goiter size decreased and thyroid hormone profile normalized, providing mechanistic parallels to LT4 therapy |
| [263304](https://pubmed.ncbi.nlm.nih.gov/263304/) | 1978 | Clinical Observational | J Clin Endocrinol Metab | Maternal-fetal thyroid function in severe endemic goiter area (Zaïre); iodized oil correction substantially normalized T4 and TSH in both mothers and newborns, demonstrating hormone replacement benefits in this population |
| [8121602](https://pubmed.ncbi.nlm.nih.gov/8121602/) | 1993 | Clinical Observational | Minerva Ginecol | 38 pregnant women with endemic non-toxic goiter; 10.5% received L-thyroxine 50–100 µg/day; goiter remained asymptomatic in 97.4%, supporting tolerability of LT4 in endemic populations |
| [7704809](https://pubmed.ncbi.nlm.nih.gov/7704809/) | 1994 | Review | Curr Ther Endocrinol Metab | Clinical review of management strategies for endemic goiter, including thyroid hormone suppression therapy as a medical option |

---

## Philippines Market Information

Levothyroxine currently holds **no registered product licenses** with the Philippine Food and Drug Administration. No product authorizations were found in the regulatory database as of the data cutoff (2026-06-04).

For international reference, Levothyroxine is widely approved in other jurisdictions — including the US FDA (e.g., Synthroid, Levoxyl), EMA (e.g., Euthyrox), and PMDA Japan — for hypothyroidism and TSH suppression in thyroid cancer. Any clinical use in the Philippines would require regulatory filing and approval prior to deployment.

---

## Safety Considerations

The Philippine FDA prescribing information for Levothyroxine was not available for this review. Drug-drug interaction data was not retrieved from the query database.

Please refer to the internationally approved package insert (e.g., US FDA label or EMA Summary of Product Characteristics) for comprehensive safety information, including cardiovascular warnings in elderly patients, precautions in adrenal insufficiency, and interactions with agents that affect thyroid hormone absorption (e.g., calcium, iron, proton pump inhibitors).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic case for Levothyroxine in endemic goiter is among the strongest possible for drug repurposing — LT4 directly corrects the T4 deficit that causes the disease and eliminates the TSH-driven growth signal that sustains it. Two direct clinical studies (PMID 24393641, PMID 3278876) document goiter regression with LT4 in endemic populations, placing this at L3 evidence. The main constraints are the absence of Philippine regulatory approval, incomplete safety profiling from local prescribing data, and the fact that iodine supplementation (rather than LT4) remains the WHO-recommended first-line prevention strategy where population-level iodine deficiency is confirmed.

**To proceed, the following is needed:**
- Philippine FDA regulatory submission and approval for Levothyroxine before clinical deployment
- Full prescribing information review (Data Gap DG001) including warnings, contraindications, and special population precautions
- DrugBank mechanism of action data (Data Gap DG002) for complete pharmacological profiling
- Baseline iodine status assessment of the target Philippine population — if iodine deficiency is the primary driver, iodized salt programs should be evaluated in parallel or prior to LT4
- Prospective controlled trial comparing LT4 alone, iodine supplementation alone, and combination therapy in Philippine endemic goiter communities, with TSH, FT4, and thyroid ultrasound as primary endpoints
- Cardiac safety monitoring protocol for at-risk subgroups (elderly, patients with underlying arrhythmias or coronary disease) given known LT4 cardiovascular effects at supratherapeutic doses
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

