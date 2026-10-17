---
layout: default
title: Amlodipine
parent: Model Prediction Only (L5)
nav_order: 25
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Amlodipine: predicted new indication Brain stem infarction (evidence level L5). Approved use: Hypertension, stroke disorder, cerebrovascular disorder…"
monitor_inn: "Amlodipine"
predicted_indications: ["brain stem infarction", "pulmonary hypertension with unclear multifactorial mechanism", "pulmonary hypertension owing to lung disease and/or hypoxia", "malignant hypertensive renal disease", "MRI defined brain infarct", "ABri amyloidosis", "intracerebral hemorrhage"]
---

# Amlodipine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Amlodipine: From Hypertension to Brain Stem Infarction

## One-Sentence Summary

Amlodipine is a calcium channel blocker, originally used for hypertension, stroke-related disorders and Prinzmetal angina.
The TxGNN model's top prediction is **brain stem infarction**, but this one has no supporting trials or publications. The best-supported prediction is **intracerebral hemorrhage**, with **4 clinical trials** (one completed Phase 3) and **10 publications**; the evidence there comes from a combination pill, not amlodipine alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension, stroke disorder, cerebrovascular disorder, cerebral infarction, Prinzmetal angina (from the knowledge graph; the Philippine registration lists no approved indication text) |
| Predicted New Indication | Brain stem infarction (rank 1) |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 for the top prediction (model prediction only) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

For reference, the other predictions scored between 99.78% and 99.91%. The best-supported ones are:

| Predicted Indication | TxGNN Score | Evidence Level | Decision |
|------|------|------|------|
| Intracerebral hemorrhage | 99.79% | L1 (combination pill) | Proceed with Guardrails |
| Cerebral artery occlusion | 99.89% | L2 (weak: terminated trials, preclinical data) | Hold |
| Pulmonary hypertension owing to lung disease and/or hypoxia | 99.91% | L4 | Hold |
| Malignant renovascular hypertension | 99.90% | L4 (case reports) | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Amlodipine is known as an L-type calcium channel blocker. It relaxes vascular smooth muscle and lowers blood pressure, and it is already used for hypertension and stroke prevention.

**Brain stem infarction (rank 1).** The very high score most likely reflects amlodipine's existing cerebrovascular indications (stroke, cerebral infarction). No trials or literature support a brainstem-specific benefit, so this is a model prediction only.

**Intracerebral hemorrhage (best-supported).** Intensive blood pressure control is the key modifiable factor for preventing recurrent hemorrhagic stroke. Amlodipine is a component of the low-dose triple-pill strategy tested in the TRIDENT trial. This is blood pressure management, not a new disease-modifying mechanism, and the effect cannot be attributed to amlodipine alone.

**Cerebral artery occlusion.** Animal stroke models show reduced infarct size with antioxidant and antiapoptotic effects, with additive benefit when combined with atorvastatin. Clinical support is weak.

**Pulmonary hypertension.** Calcium channel blockade could in theory blunt hypoxic pulmonary vasoconstriction. However, vasodilators may worsen ventilation/perfusion mismatch in lung disease, and case reports describe hypoxia and non-cardiogenic pulmonary edema.

## Clinical Trial Evidence

Brain stem infarction, the top prediction, has no related clinical trials registered. The trials below are for **intracerebral hemorrhage** (rank 10) and **cerebral artery occlusion** (rank 6).

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1671 | TRIDENT: low-dose triple-pill blood pressure strategy (includes amlodipine) vs standard care to prevent recurrent stroke after intracerebral hemorrhage. Most direct evidence, but a combination regimen |
| [NCT07458880](https://clinicaltrials.gov/study/NCT07458880) | NA | Recruiting | 140 | Triple antihypertensive medication for blood pressure control after intracerebral hemorrhage; no results yet |
| [NCT00805311](https://clinicaltrials.gov/study/NCT00805311) | Phase 4 | Terminated | 400 | Carotid endarterectomy vs optimal medical treatment in asymptomatic carotid stenosis; amlodipine is not the tested intervention |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | NA | Terminated | 4 | TRIDENT MRI sub-study; too small to inform efficacy |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT cognitive sub-study; no usable outcome data |

## Literature Evidence

No literature is available for brain stem infarction. The publications below relate to the other predicted indications.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [42019018](https://pubmed.ncbi.nlm.nih.gov/42019018/) | 2026 | RCT | N Engl J Med | TRIDENT main results: three low-dose antihypertensives in a single pill after intracerebral hemorrhage (outcome details not available in the compiled data) |
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Trial design paper | Int J Stroke | Rationale and design of TRIDENT; single-pill combination as a secondary prevention strategy |
| [10759437](https://pubmed.ncbi.nlm.nih.gov/10759437/) | 2000 | Randomized crossover study | Eur Respir J | Amlodipine vs placebo on respiratory and pulmonary vascular responses to hypoxia in 14 mountaineers |
| [11282121](https://pubmed.ncbi.nlm.nih.gov/11282121/) | 2001 | Preclinical | Eur J Pharmacol | Amlodipine attenuated pulmonary vascular remodelling in hypoxic rats; prevented entirely when combined with perindopril |
| [21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/) | 2011 | Preclinical | J Neurosci Res | Amlodipine plus atorvastatin gave additive neuroprotection after middle cerebral artery occlusion in rats |
| [17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/) | 2006 | Preclinical | Am J Hypertens | Amlodipine reduced stroke size in ApoE-deficient mice |
| [36856509](https://pubmed.ncbi.nlm.nih.gov/36856509/) | 2023 | Case report | Heart Surg Forum | Amlodipine possibly inhibited hypoxic pulmonary vasoconstriction, causing hypoxia during one-lung ventilation |
| [35261597](https://pubmed.ncbi.nlm.nih.gov/35261597/) | 2022 | Case report | Saudi J Anaesth | Amlodipine overdose complicated by non-cardiogenic pulmonary edema and alveolar hemorrhage (safety signal) |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case report | Ann Pharmacother | Probable amlodipine-induced angioedema in a patient with hemorrhagic stroke |
| [16467664](https://pubmed.ncbi.nlm.nih.gov/16467664/) | 2006 | Case report | J Hypertens | Severe renovascular hypertension in a child (indirect; not specific to amlodipine) |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0017 | Amlodipine | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: liver failure and liver disease, kidney disease, pancreatitis, gallbladder disease, hypothyroidism and myxedema, angioedema (including hereditary and renin-angiotensin-aldosterone system-blocker-induced forms), systemic lupus erythematosus, myopathy and periodic paralysis, potassium deficiency, diabetes mellitus and diabetic ketoacidosis, neutropenia and agranulocytosis, hypotensive disorder, hyperparathyroidism.
- **Drug Interactions**: 100 interactions were identified, and the 20 shown are all of moderate severity. They include corticosteroids (hydrocortisone, betamethasone, budesonide, dexamethasone), aprepitant, acetylsalicylic acid, bupropion, clarithromycin, clotrimazole, SGLT2 inhibitors (canagliflozin, dapagliflozin) and calcium salts (acetate, carbonate, chloride, citrate, gluconate, lactate and others).
- **Case-report signals**: angioedema, and non-cardiogenic pulmonary edema in overdose. In lung disease, vasodilation may worsen oxygenation.

Please also refer to the package insert for label warnings; none were available for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top prediction, brain stem infarction, has no trials or literature and mostly duplicates amlodipine's existing stroke and cerebral infarction indications.
- The only strong clinical signal is for intracerebral hemorrhage (the TRIDENT Phase 3 trial), and it comes from a combination pill, so it cannot be attributed to amlodipine. That indication could be considered for Proceed with Guardrails once the full results are reviewed.
- The only Philippine registration is cancelled, so there is currently no marketed product.

**To proceed, the following is needed:**
- Full TRIDENT results (NEJM 2026) to assess the contribution of amlodipine within the triple pill
- Mechanism of action data and package insert warnings and contraindications
- Confirmation of regulatory status in the Philippines, since the only registration is cancelled
- Direct evidence for brain stem infarction, or a decision to focus on intracerebral hemorrhage
- A safety plan covering angioedema, hypotension, and use in patients with hepatic impairment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

