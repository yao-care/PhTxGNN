---
layout: default
title: Valsartan
parent: Moderate Evidence (L3-L4)
nav_order: 350
evidence_level: L4
indication_count: 6
last_modified_at: 2026-11-20
description: "Valsartan: predicted new indication Malignant hypertensive renal disease (evidence level L4). Approved use: Hypertension (hypertensive disorder)"
monitor_inn: "Valsartan"
predicted_indications: ["malignant hypertensive renal disease", "pulmonary hypertension owing to lung disease and/or hypoxia", "pulmonary hypertension with unclear multifactorial mechanism", "Braddock syndrome", "chronic pulmonary heart disease", "Prinzmetal angina"]
---

# Valsartan
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **6** 
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

## Valsartan: From Hypertension to Malignant Hypertensive Renal Disease
{: .text-alpha }

## One-Sentence Summary

Valsartan is an angiotensin II receptor blocker, originally used to treat hypertension.
The TxGNN model predicts it may be effective for **malignant hypertensive renal disease** (score 0.9997),
but **no clinical trials** and only **1 indirect preclinical publication** (which does not test valsartan) currently support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (hypertensive disorder) |
| Predicted New Indication | Malignant hypertensive renal disease |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L4 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 3) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 3 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

According to the Mechanism of Action section of the US FDA-approved prescribing information for valsartan: "Angiotensin II is formed from angiotensin I in a reaction catalyzed by angiotensin-converting enzyme (ACE, kininase II). Angiotensin II is the principal pressor agent of the renin-angiotensin system, with effects that include vasoconstriction, stimulation of synthesis and release of aldosterone, cardiac stimulation, and renal reabsorption of sodium. […] Diovan (valsartan) blocks the vasoconstrictor and aldosterone-secreting effects of angiotensin II by selectively blocking the binding of angiotensin II to the AT 1 receptor in many tissues, such as vascular smooth muscle and the adrenal gland." ([DailyMed: Diovan (valsartan) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ddba454-f3e6-43c2-a7a6-58365d297213), label version 2026-08-11; accessed 2026-11-19.) Based on known pharmacology, valsartan is an angiotensin II type 1 (AT1) receptor blocker. Its efficacy in hypertension is established, and mechanistically it may protect the kidney in severe hypertension through blockade of the renin-angiotensin-aldosterone system (RAAS).

The predicted indication is closely related to the original one. Malignant hypertensive renal disease is kidney damage caused by severe hypertension, so this prediction sits near the labeled use rather than representing a true repurposing signal. The very high TxGNN score is a computational result and does not replace clinical data.

Other predictions from the model are weaker still:
- **Pulmonary hypertension (two categories)**, **chronic pulmonary heart disease**, **Braddock syndrome** and **Prinzmetal angina**: evidence is model prediction or indirect literature (mostly sacubitril/valsartan, heart failure, or unrelated topics). These are not supported for valsartan alone.

## Clinical Trial Evidence

Currently no related clinical trials registered for the lead prediction, malignant hypertensive renal disease.

For the lower-ranked prediction chronic pulmonary heart disease, one trial was retrieved, but it does not appear to test valsartan:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Exercise and rehabilitation study of vascular function in hypertension; not a valsartan study (relevance grade C) |

## Literature Evidence

For the lead prediction, only one paper was retrieved, and it concerns a different drug:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [24368192](https://pubmed.ncbi.nlm.nih.gov/24368192/) | 2014 | Preclinical | Pharmacological Research | Avosentan (an endothelin antagonist, not valsartan) protected against hypertensive nephropathy in transgenic rats at doses that did not cause fluid retention |

Selected supporting papers for the predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [11560862](https://pubmed.ncbi.nlm.nih.gov/11560862/) | 2001 | Preclinical (animal) | Circulation | AT1 receptor blockade prevented lethal malignant hypertension, related to kidney inflammation |
| [32552157](https://pubmed.ncbi.nlm.nih.gov/32552157/) | 2020 | Preclinical (animal) | J Am Heart Assoc | Sacubitril/valsartan attenuated right ventricular remodeling in pulmonary hypertension |
| [22377232](https://pubmed.ncbi.nlm.nih.gov/22377232/) | 2012 | Preclinical (animal) | Diabetes Res Clin Pract | Valsartan inhibited the HIF-1α pathway and reduced renal interstitial fibrosis in diabetic rats |
| [34796742](https://pubmed.ncbi.nlm.nih.gov/34796742/) | 2021 | Post hoc RCT analysis | J Am Heart Assoc | Impact of COPD on outcomes in HFpEF patients in PARAGON-HF (sacubitril/valsartan trial) |

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Valsartan | Oral |
| Sacubitril/Valsartan | Oral |
| Valsartan + Hydrochlorothiazide | Oral |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Contraindications (from the TxGNN knowledge graph, not label text)**: The graph lists, among others, angioedema (including hereditary and RAAS-blocker-induced), liver failure and liver disease, pancreatitis, gallbladder disease, hepatic encephalopathy, anuria, impaired renal function, renal artery obstruction, hypotensive disorder, diabetes mellitus and diabetic ketoacidosis, gout, neutropenia and agranulocytosis, systemic lupus erythematosus, hypercalcemia, hyperparathyroidism, and potassium deficiency.
- **Drug Interactions** (100 interactions found; main ones shown):
  - **Major**: potassium chloride, potassium bicarbonate (risk of hyperkalaemia)
  - **Moderate**: many insulin products, exenatide, hydrocortisone, eluxadoline, polyethylene glycol with electrolytes
- **Indication-specific concern**: ARBs carry a risk of acute kidney injury in bilateral renal artery stenosis, which is relevant for renovascular hypertension.

Please refer to the package insert for further safety information, as label warnings were not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The lead prediction is supported only by a model score and one indirect preclinical paper on a different drug, with no clinical trials (L4). It is also close to valsartan's existing hypertension indication. In addition, label safety data are unavailable.

<!-- review:begin ph-lic-20261106-valsartan-1 -->

> **Review correction (2026-11-24)**: Originally stated: "In addition, valsartan is currently marketed in the Philippines (1 valid license of 1), and label safety data are unavailable." Removed: the number or status of PNF entries stated here did not match the PNF data (the Philippine National Formulary as of 2026-11-06). The Quick Overview and the PNF entry table under Philippines Market Information show the current number of PNF entries. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-valsartan-1 -->

**To proceed, the following is needed:**
- Valsartan-specific clinical or preclinical evidence in malignant hypertensive renal disease
- Confirmation of the current Philippines registration status and a valid product registration
- Package insert warnings and contraindications from DOH-FDA Philippines
- Mechanism of action data (e.g., from DrugBank)
- Renal safety assessment (renal artery stenosis, hyperkalaemia, impaired renal function) for severe hypertension with kidney involvement

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten. A statement that mechanism-of-action data were not available was replaced with an excerpt from the cited official prescribing information or database.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-24 | Removed: "valsartan is currently marketed in the Philippines (1 valid license of 1), and" | Corrected (revised 2026-11-24; earlier version kept in the record) | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |
| 2026-11-19 | "Currently, detailed mechanism of action data is not available in the data compiled for this report" replaced with a sourced mechanism-of-action statement | Statement that mechanism-of-action data were not available replaced with a sourced excerpt | [DailyMed: Diovan (valsartan) prescribing information, Novartis Pharmaceuticals Corporation](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=5ddba454-f3e6-43c2-a7a6-58365d297213) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

