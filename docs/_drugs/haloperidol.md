---
layout: default
title: Haloperidol
parent: 僅模型預測 (L5)
nav_order: 162
evidence_level: L5
indication_count: 10
---

# Haloperidol
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

# Haloperidol: From Antipsychotic Use to Manic Bipolar Affective Disorder

## One-Sentence Summary

Haloperidol is a classic first-generation (typical) antipsychotic, globally recognized for treating schizophrenia, acute psychosis, and Tourette syndrome.
The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder** (rank 10, score 99.83%),
with **9 clinical trials** and **20 publications** providing robust support — notably including multiple completed Phase 3 RCTs where haloperidol served as an active comparator, yielding direct efficacy data.

> ⚠️ **Note:** Haloperidol is currently **not registered** in the Philippines. The top 9 TxGNN-ranked predictions (ranks 1–9) involve ultra-rare congenital/genetic disorders with **no clinical evidence** (L5), and are all recommended as **Hold**. This report focuses on rank 10 — manic bipolar affective disorder — which is the only prediction with actionable clinical evidence.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in the Philippines. Globally approved for schizophrenia, acute psychosis, and Tourette syndrome |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L1 (≥2 completed Phase 3 RCTs) |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## All TxGNN Predicted Indications Summary

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|---------------|----------------|
| 1 | Congenital disorder of glycosylation with defective fucosylation | 99.91% | L5 | Hold |
| 2 | Retinal dystrophy with or without extraocular anomalies | 99.91% | L5 | Hold |
| 3 | Hydranencephaly | 99.90% | L5 | Hold |
| 4 | Myopia, X-linked | 99.89% | L5 | Hold |
| 5 | Charcot-Marie-Tooth disease, demyelinating, type 1G | 99.89% | L5 | Hold |
| 6 | Myopia 26, X-linked, female-limited | 99.89% | L5 | Hold |
| 7 | Syndromic myopia | 99.88% | L5 | Hold |
| 8 | Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis | 99.88% | L5 | Hold |
| 9 | Atypical glycine encephalopathy | 99.87% | L5 | Hold |
| **10** | **Manic Bipolar Affective Disorder** | **99.83%** | **L1** | **Proceed with Guardrails** |

> Ranks 1–9 involve ultra-rare genetic or congenital conditions with no mechanistic rationale for haloperidol's D2 antagonism. Several predictions (ranks 4, 6, 7) may actually be **contraindicated** — D2 antagonism in the retina could worsen myopia progression. Rank 5 (CMT1G) raises safety concerns as antipsychotics may exacerbate peripheral neuropathy. Only rank 10 has a sound mechanistic basis and clinical evidence.

---

## Why is This Prediction Reasonable?

Haloperidol is a butyrophenone-class dopamine D2 receptor antagonist. Its primary mechanism involves potent blockade of D2 receptors in the mesolimbic and mesocortical dopamine pathways. This dopaminergic antagonism directly addresses the hyperdopaminergic state that underlies the core pathophysiology of acute mania — including euphoria, grandiosity, psychomotor agitation, and psychotic features.

Manic episodes in bipolar I disorder are characterized by excessive dopaminergic activity in the mesolimbic system. Haloperidol's high-affinity D2 blockade rapidly reduces this overactivation, making it mechanistically well-suited for acute mania management. In clinical practice, haloperidol has been used for treating acute mania for decades, often serving as the "gold standard" active comparator in clinical trials of newer atypical antipsychotics (risperidone, olanzapine, aripiprazole) for bipolar mania.

It is important to note that this prediction essentially validates a **well-established clinical use** rather than identifying a novel repurposing opportunity. Haloperidol is already approved for bipolar mania in numerous regulatory jurisdictions worldwide (e.g., FDA, EMA). The TxGNN model's ability to independently recover this known indication serves as a positive control demonstrating the model's validity for this drug. However, since haloperidol is not currently registered in the Philippines, there may be a regulatory pathway opportunity if local market need exists.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00253162](https://clinicaltrials.gov/study/NCT00253162) | Phase 3 | Completed | 439 | Risperidone vs Haloperidol vs Placebo in manic episodes of bipolar I disorder; haloperidol as active comparator over 12 weeks demonstrating sustained efficacy |
| [NCT00253149](https://clinicaltrials.gov/study/NCT00253149) | Phase 3 | Completed | 158 | Risperidone vs Haloperidol as add-on to mood stabilizers for bipolar mania treatment |
| [NCT00129220](https://clinicaltrials.gov/study/NCT00129220) | Phase 3 | Completed | 224 | Olanzapine vs Haloperidol vs Placebo in manic/mixed episodes of bipolar I disorder; head-to-head comparison design |
| [NCT00097266](https://clinicaltrials.gov/study/NCT00097266) | Phase 3 | Completed | 615 | Aripiprazole monotherapy vs Haloperidol (active control) for acute mania over 12 weeks; largest trial in dataset |
| [NCT00126009](https://clinicaltrials.gov/study/NCT00126009) | Phase 2 | Completed | 120 | Valproate-Amisulpride vs Valproate-Haloperidol (5–15 mg/day) combination therapy in manic episodes over 3 months |
| [NCT04327843](https://clinicaltrials.gov/study/NCT04327843) | Phase 3 | Completed | 22 | Long-acting injectable antipsychotics combined with behavioral program for chronic psychotic disorders including bipolar disorder in Tanzania |
| [NCT00767715](https://clinicaltrials.gov/study/NCT00767715) | Phase 4 | Terminated | 11 | Olanzapine vs conventional antipsychotics (including haloperidol) in acute mania in Sweden; terminated due to poor enrollment |
| [NCT03541031](https://clinicaltrials.gov/study/NCT03541031) | N/A | Unknown | 120 | Micronutrient supplementation as adjunctive treatment for bipolar disorder |
| [NCT06049953](https://clinicaltrials.gov/study/NCT06049953) | N/A | Recruiting | 200 | Observational study on developmental effects of antenatal antipsychotic exposure in pregnant individuals with severe mental illness |

> **Summary:** 4 completed Phase 3 RCTs directly include haloperidol as an active comparator arm, collectively enrolling over 1,400 patients. This exceeds the L1 threshold (≥2 completed Phase 3 RCTs) with strong confidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34642461](https://pubmed.ncbi.nlm.nih.gov/34642461/) | 2022 | Systematic Review / NMA | Molecular Psychiatry | Comprehensive network meta-analysis comparing pharmacological treatments for acute bipolar mania from all available RCTs; positions haloperidol among effective interventions |
| [22134043](https://pubmed.ncbi.nlm.nih.gov/22134043/) | 2012 | RCT | Journal of Affective Disorders | Randomized double-blind trial of olanzapine vs haloperidol vs placebo in Japanese bipolar I patients with manic/mixed episodes; first Asian population-specific data |
| [3312180](https://pubmed.ncbi.nlm.nih.gov/3312180/) | 1987 | RCT | J Clinical Psychiatry | Double-blind trial comparing clonazepam with haloperidol in acutely manic patients; demonstrated haloperidol's established efficacy as benchmark |
| [369472](https://pubmed.ncbi.nlm.nih.gov/369472/) | 1979 | RCT | Archives of General Psychiatry | Controlled trial of lithium + haloperidol vs placebo + haloperidol in schizoaffective disorder; showed additive benefit of combination therapy |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Clinical Review | Acta Psychiatrica Scandinavica | Evidence-based review of mania treatment options; includes haloperidol as a recommended option among mood stabilizers and antipsychotics |
| [22070611](https://pubmed.ncbi.nlm.nih.gov/22070611/) | 2012 | Review | CNS Neuroscience & Therapeutics | Reviews treatment of refractory bipolar disorder; recommends adding haloperidol to lithium/valproate partial responders |
| [36789916](https://pubmed.ncbi.nlm.nih.gov/36789916/) | 2023 | Comparative Analysis | BMJ Mental Health | Comparison of antipsychotic dose equivalents between acute mania and schizophrenia; provides dosing guidance for haloperidol in mania |
| [15147609](https://pubmed.ncbi.nlm.nih.gov/15147609/) | 2004 | HTA / Systematic Review | Health Technology Assessment | Systematic review and economic evaluation of treatments for bipolar mania; haloperidol included as comparator across multiple analyses |
| [18344731](https://pubmed.ncbi.nlm.nih.gov/18344731/) | 2008 | Systematic Review | J Clinical Psychopharmacology | Systematic comparison of antipsychotic-induced EPS in bipolar disorder vs schizophrenia; important safety data for haloperidol use in mania |
| [10343182](https://pubmed.ncbi.nlm.nih.gov/10343182/) | 1999 | Mechanism Study | Neuropsychobiology | Lithium and haloperidol differentially affect Gαs protein levels in bipolar patients; provides mechanistic insight into haloperidol's action in bipolar disorder |

---

## Philippines Market Information

Haloperidol is **not currently registered** in the Philippines. No FDA Philippines authorizations were found.

| Item | Status |
|------|------|
| Market Status | Not marketed |
| Total Registrations | 0 |
| Available Dosage Forms | None registered |

> Haloperidol is widely available globally and appears on the WHO Model List of Essential Medicines. Its absence from the Philippines market may represent a registration gap rather than a safety/efficacy concern.

---

## Safety Considerations

> Please refer to the package insert for safety information.

Detailed safety data (warnings, contraindications, drug interactions) were not available in the current evidence pack. Based on haloperidol's well-established global safety profile, key considerations include:

- **Extrapyramidal Symptoms (EPS):** Haloperidol has a high incidence of acute dystonia, akathisia, parkinsonism, and tardive dyskinesia — particularly relevant in bipolar patients who may require long-term maintenance
- **QTc Prolongation:** Risk of Torsades de Pointes, especially with IV administration or at higher doses
- **Neuroleptic Malignant Syndrome (NMS):** Rare but life-threatening; requires immediate discontinuation
- **Black Box Warning (US FDA):** Increased mortality in elderly patients with dementia-related psychosis
- **Metabolic Effects:** Lower metabolic risk compared to atypical antipsychotics, but monitoring still recommended

> ⚠️ **Data Gap:** Philippine-specific prescribing information, local package insert warnings, and DDI data require supplementation from FDA Philippines or the manufacturer.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Haloperidol's efficacy in acute bipolar mania is supported by multiple completed Phase 3 RCTs (L1 evidence) and decades of global clinical experience. The D2 antagonism mechanism directly addresses manic pathophysiology. This is effectively a **validated known indication** rather than a novel repurposing discovery, which serves as a positive control for the TxGNN model's predictive capability. However, the drug is currently not registered in the Philippines, presenting a potential market access opportunity.

**The top 9 TxGNN predictions (ranks 1–9) are all recommended as Hold** due to:
- All are ultra-rare congenital/genetic disorders with no clinical evidence (L5)
- No mechanistic rationale for D2 antagonism in these conditions
- Several predictions may be contraindicated (myopia variants, CMT1G)

**To proceed, the following is needed:**
- **Regulatory pathway assessment** for haloperidol registration in the Philippines
- **Detailed MOA data** from DrugBank to support formal documentation
- **Philippine-specific package insert** with local warnings and contraindications
- **Drug-drug interaction database** query to populate DDI safety profile
- **Comparative cost-effectiveness analysis** against atypical antipsychotics (risperidone, olanzapine) already available in the Philippines for bipolar mania
- **EPS monitoring protocol** given haloperidol's higher EPS burden compared to atypical alternatives

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*

*Data cutoff: 2026-04-05 | Evidence Pack version: v4 | Candidate ID: TW-DB00502-multi*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

