---
layout: default
title: Amlodipine
parent: 僅模型預測 (L5)
nav_order: 24
evidence_level: L5
indication_count: 10
---

# Amlodipine
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

# Amlodipine: From Hypertension to Brain Stem Infarction

## One-Sentence Summary

Amlodipine is a long-acting dihydropyridine calcium channel blocker (CCB) with globally established use in hypertension and chronic stable angina, though no Philippines registration data is currently available.
The TxGNN model predicts it may be effective for **brain stem infarction** (highest-ranked prediction, score 99.94%), with **10 cerebrovascular and hypertensive disease indications** predicted across the full evaluation.
While the top-ranked prediction has **no direct clinical or literature support (L5)**, the closely related indication of **intracerebral hemorrhage (rank 10)** has **1 completed Phase 3 RCT** (TRIDENT, n=1,671) and **8 publications**, representing the strongest actionable candidate in this multi-indication pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension; Chronic Stable Angina (globally established; not registered in Philippines per current dataset) |
| Predicted New Indication (Rank 1) | Brain Stem Infarction |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L5 (Rank 1 — Brain Stem Infarction) / L2 (Rank 10 — Intracerebral Hemorrhage) |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Rank 1) / Proceed with Guardrails (Rank 10 — Intracerebral Hemorrhage) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current Evidence Pack. Based on established pharmacological knowledge, Amlodipine is a long-acting L-type calcium channel blocker that reduces vascular smooth muscle contraction by blocking voltage-gated calcium channels, resulting in systemic vasodilation and sustained blood pressure reduction. Its half-life of approximately 35–50 hours provides stable 24-hour hemodynamic control with minimal reflex tachycardia — a pharmacokinetic profile particularly well-suited to cerebrovascular secondary prevention.

All 10 TxGNN-predicted indications fall within the cerebrovascular and hypertensive disease spectrum, which is directly mechanistically connected to Amlodipine's established use. Brain stem infarction, cerebral artery occlusion, MRI-defined brain infarct, and intracerebral hemorrhage are all strongly linked to uncontrolled hypertension. Sustained CCB therapy reduces cerebral small vessel wall pressure, attenuates atherosclerotic progression, and lowers lacunar infarct formation risk — providing a coherent biological rationale for the high TxGNN scores observed across this cluster.

For ischemic indications specifically (brain stem infarction, cerebral artery occlusion), preclinical animal studies using Amlodipine directly have demonstrated additional neuroprotective mechanisms: inhibition of neuronal L-type calcium channel overactivation following ischemia-reperfusion, anti-apoptotic and anti-autophagic effects, and antioxidative properties — with synergistic effects observed in combination with atorvastatin. The most clinically validated indication in this pack is **intracerebral hemorrhage**: the TRIDENT Phase 3 trial (n=1,671, completed) tested a fixed-dose triple combination pill that included a CCB/Amlodipine component for ICH secondary prevention, providing the strongest direct evidence for a CCB role in this disease spectrum.

---

## Predicted Indications — Full Landscape

| Rank | Disease | TxGNN Score | Evidence Level | Recommendation |
|------|---------|-------------|----------------|----------------|
| 1 | Brain Stem Infarction | 99.94% | L5 | Hold |
| 2 | PH — Unclear Multifactorial Mechanism | 99.91% | L5 | Hold |
| 3 | PH — Lung Disease / Hypoxia | 99.91% | L5 | Hold |
| 4 | Malignant Hypertensive Renal Disease | 99.90% | L5 | Hold |
| 5 | Malignant Renovascular Hypertension | 99.90% | L4 | Research Question |
| 6 | Cerebral Artery Occlusion | 99.89% | L4 | Research Question |
| 7 | Braddock Syndrome | 99.88% | L5 | Hold |
| 8 | MRI-Defined Brain Infarct | 99.86% | L4 | Research Question |
| 9 | ABri Amyloidosis | 99.84% | L5 | Hold |
| **10** | **Intracerebral Hemorrhage** | **99.79%** | **L2** | **Proceed with Guardrails** |

---

## Clinical Trial Evidence

### Intracerebral Hemorrhage (Rank 10 — Strongest Clinical Evidence)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02699645](https://clinicaltrials.gov/study/NCT02699645) | Phase 3 | Completed | 1,671 | TRIDENT: Multicentre, double-blinded, placebo-controlled RCT testing a fixed-dose triple-pill BP-lowering strategy (including CCB/Amlodipine) on top of standard care for secondary prevention of recurrent stroke in patients with a history of intracerebral haemorrhage |
| [NCT00134160](https://clinicaltrials.gov/study/NCT00134160) | Phase 4 | Completed | 1,000 | CASE-J: High-dose ARB monotherapy vs ARB + CCB (Amlodipine) in Japanese elderly high-risk hypertensives; comparison of cardiovascular event incidence including stroke |
| [NCT03264352](https://clinicaltrials.gov/study/NCT03264352) | Phase 4 | Recruiting | 11,414 | IPAD: Antihypertensive therapy (may include Amlodipine) in adults with T2D and high-normal BP; cardiovascular and cerebrovascular events as secondary endpoints |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT Cognitive Sub-Study: early termination with n=1, no valid data |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Terminated | 4 | TRIDENT MRI Sub-Study: early termination with n=4, no valid data |

### Cerebral Artery Occlusion (Rank 6 — Strongest Amlodipine-Specific Preclinical Evidence)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03015311](https://clinicaltrials.gov/study/NCT03015311) | N/A | Unknown | 8,000 | STEP: Intensive (<130 mmHg) vs standard (<150 mmHg) SBP control in elderly hypertensives aged 60–80; Amlodipine likely part of intervention arm; MRI brain infarct a potential imaging sub-endpoint |
| [NCT02850081](https://clinicaltrials.gov/study/NCT02850081) | Phase 3 | Completed | 31 | Statin neuroprotection pre-carotid endarterectomy; not testing Amlodipine directly; small sample |
| [NCT03785067](https://clinicaltrials.gov/study/NCT03785067) | Phase 3 | Terminated | 1 | TRIDENT Cognitive Sub-Study; early termination, no valid data |
| [NCT03783754](https://clinicaltrials.gov/study/NCT03783754) | N/A | Terminated | 4 | TRIDENT MRI Sub-Study; early termination, no valid data |
| [NCT00805311](https://clinicaltrials.gov/study/NCT00805311) | Phase 4 | Terminated | 400 | CEA vs optimal medical therapy for asymptomatic high-grade carotid stenosis; early termination, not Amlodipine-specific |

---

## Literature Evidence

### Cerebral Artery Occlusion (Rank 6 — Direct Amlodipine Animal Studies)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21538457](https://pubmed.ncbi.nlm.nih.gov/21538457/) | 2011 | Preclinical (Animal) | J Neuroscience Research | Amlodipine + atorvastatin exert anti-apoptotic and anti-autophagic neuroprotection after transient MCAO in Zucker metabolic syndrome rats; combination therapy superior to monotherapy |
| [20971084](https://pubmed.ncbi.nlm.nih.gov/20971084/) | 2011 | Preclinical (Animal) | Brain Research | Synergistic reduction of infarct volume with amlodipine + atorvastatin vs either drug alone after 90-min tMCAO in Zucker rats |
| [21276424](https://pubmed.ncbi.nlm.nih.gov/21276424/) | 2011 | Preclinical (Animal) | Brain Research | Amlodipine + atorvastatin combination reduces ischemic stroke damage with physical and serum parameter improvements in metabolic syndrome rat model |
| [17070425](https://pubmed.ncbi.nlm.nih.gov/17070425/) | 2006 | Preclinical (Animal) | Am J Hypertension | Amlodipine (L-type CCB) reduces stroke size after focal brain ischemia in ApoE-deficient mice |
| [17904110](https://pubmed.ncbi.nlm.nih.gov/17904110/) | 2007 | Preclinical (Animal) | Brain Research | CCBs with antioxidative properties prevent neuronal damage after transient focal ischemia in rats; antioxidative mechanism implicated |

### Intracerebral Hemorrhage (Rank 10)

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34994269](https://pubmed.ncbi.nlm.nih.gov/34994269/) | 2022 | Protocol/Design | Int J Stroke | TRIDENT trial rationale and design: single-pill CCB-containing combination for ICH secondary prevention; provides mechanistic basis for triple-pill BP-lowering strategy |
| [14717341](https://pubmed.ncbi.nlm.nih.gov/14717341/) | 2003 | RCT Protocol | Hypertension Res | CASE-J design paper: ARB vs ARB+CCB in high-risk Japanese hypertensives; cardiovascular event reduction framework |
| [23053838](https://pubmed.ncbi.nlm.nih.gov/23053838/) | 2013 | Review | Neurological Sciences | Comparison of antihypertensive agents (including CCBs) in acute ICH management; sympathetic overactivity and intracranial pressure as key pathological targets |
| [3154329](https://pubmed.ncbi.nlm.nih.gov/3154329/) | 1988 | Review | Cardiovascular Drugs Ther | Comprehensive review of CCB antihypertensive mechanisms; vascular myocyte calcium overload hypothesis as rationale for first-choice therapy in severe hypertension |
| [17077518](https://pubmed.ncbi.nlm.nih.gov/17077518/) | 2006 | Preclinical | Biol Pharm Bull | Dihydropyridine CCB (benidipine) improves cerebral blood flow autoregulation in spontaneously hypertensive rats; class-level evidence relevant to Amlodipine |
| [19299323](https://pubmed.ncbi.nlm.nih.gov/19299323/) | 2009 | Case Report (AE) | Ann Pharmacotherapy | Probable Amlodipine-induced angioedema in a patient with right thalamic hemorrhagic stroke — adverse event signal relevant to ICH population |
| [26698202](https://pubmed.ncbi.nlm.nih.gov/26698202/) | 2015 | Case Report | BMJ Case Reports | PRES after rapid antihypertensive withdrawal (including Amlodipine) post-bariatric surgery in a patient with prior ICH; highlights risks of abrupt CCB discontinuation |
| [37489780](https://pubmed.ncbi.nlm.nih.gov/37489780/) | 2024 | Case Report | Current Drug Safety | Tizanidine-induced hypotension in stroke patients on antihypertensive regimens; drug interaction signal relevant to ICH survivors on CCBs |

---

## Philippines Market Information

Amlodipine is currently **not registered** in the Philippines market based on available data. No active pharmaceutical licenses were found in the regulatory dataset (0 registrations). This likely reflects a data gap rather than true market absence, as Amlodipine is one of the most widely prescribed antihypertensives globally and is included on the WHO Essential Medicines List. A supplementary query to the FDA Philippines (Food and Drug Administration of the Philippines) is recommended to confirm current market authorization status.

---

## Safety Considerations

Please refer to the package insert for safety information.

> No key warnings, contraindications, or drug interaction data are available in the current Evidence Pack. Full safety review should be completed by retrieving the FDA Philippines-approved prescribing information before any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold (Rank 1 — Brain Stem Infarction) / Proceed with Guardrails (Rank 10 — Intracerebral Hemorrhage)**

**Rationale:**
The top TxGNN prediction (brain stem infarction, 99.94%) is currently supported by model prediction only — no clinical trials or literature validate this specific repurposing hypothesis, warranting a Hold pending further mechanistic and clinical data. However, the closely related indication of intracerebral hemorrhage (rank 10) benefits from the completed Phase 3 TRIDENT trial (n=1,671), which directly tested a CCB-containing triple pill for secondary prevention of recurrent stroke after ICH, providing sufficient L2 evidence to justify advancing with appropriate safeguards. The mechanistic hypothesis is coherent across all 10 predicted indications, as the entire cluster maps to hypertension-driven cerebrovascular pathology — Amlodipine's core pharmacological domain.

**To proceed (for Intracerebral Hemorrhage):**
- Obtain TRIDENT primary endpoint publication and confirm CCB arm-specific effect size
- Verify Philippines FDA registration status and regulatory pathway for ICH indication
- Retrieve full mechanism of action (MOA) data from DrugBank (DG002 data gap resolution)
- Obtain Philippines-approved prescribing information to complete safety assessment (DG001 data gap — currently Blocking)
- Assess oral formulation availability in Philippines and route compatibility for ICH secondary prevention population
- For brain stem infarction (rank 1): initiate targeted literature review and consider designing a preclinical validation study before escalating evidence level above L5
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

