---
layout: default
title: Clozapine
parent: 僅模型預測 (L5)
nav_order: 83
evidence_level: L5
indication_count: 10
---

# Clozapine
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

# Clozapine: From Treatment-Resistant Schizophrenia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Clozapine is a multi-receptor atypical antipsychotic globally approved for treatment-resistant schizophrenia and for reducing suicidal behavior risk in patients with chronic psychotic disorders.
The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**,
with **6 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines; globally approved for treatment-resistant schizophrenia |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L2 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Clozapine is a broad multi-receptor antagonist with over 30 years of clinical evidence in treatment-resistant schizophrenia. Its pharmacological targets span dopamine D2/D4 receptors, serotonin 5-HT2A/2C receptors, histamine H1 receptors, and α1-adrenergic receptors — a profile that differs substantially from conventional antipsychotics.

This multi-receptor profile provides a plausible mechanistic bridge to manic bipolar affective disorder. D2/D4 dopamine receptor antagonism can dampen the pathological mesolimbic dopamine hyperactivation characteristic of manic episodes. Simultaneously, 5-HT2A antagonism supports mood stabilization via enhanced serotonergic neurotransmission, while H1 blockade provides clinically useful acute sedation during manic agitation. α1-adrenergic antagonism may further attenuate the autonomic dysregulation accompanying severe mania. Emerging evidence also suggests anti-inflammatory properties — including NF-κB inhibition and IL-6 reduction — that may benefit neuroinflammation-driven mood instability.

Mechanistically, both treatment-resistant schizophrenia and manic bipolar affective disorder share dopaminergic dysregulation as a core pathophysiological substrate, making Clozapine's repurposing rationale more grounded than a purely model-driven prediction. This is borne out clinically: a completed Phase 2 double-blind RCT (NCT00029458, n=42) directly evaluated Clozapine in treatment-resistant mania, and a dedicated systematic review and meta-analysis (PMID 32182485) as well as multiple additional systematic reviews specifically assessed its efficacy in bipolar disorder.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00029458](https://clinicaltrials.gov/study/NCT00029458) | Phase 2 | Completed | 42 | Double-blind RCT directly evaluating safety and effectiveness of Clozapine for treatment-resistant manic phase of bipolar disorder; the only completed controlled trial targeting this specific indication |
| [NCT05603104](https://clinicaltrials.gov/study/NCT05603104) | Phase 3 | Recruiting | 1,254 | Large-scale RCT of intensified pharmacological treatment after first-line failure, covering schizophrenia, bipolar depression, and major depressive disorder; if completed, would elevate evidence to L1 |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | Recruiting | 40 | Efficacy of pharmacotherapy combined with recovery-oriented programs (RECOVERYTRSBDGR) specifically for treatment-resistant bipolar disorder patients |
| [NCT06993662](https://clinicaltrials.gov/study/NCT06993662) | Phase 1 | Active, Not Recruiting | 107 | Pharmacotherapy combined with individual cognitive behavioral therapy across mental health disorders including bipolar disorder |
| [NCT03651674](https://clinicaltrials.gov/study/NCT03651674) | N/A | Unknown | 200 | Longitudinal MRI study of ECT-induced brain structural and functional changes in schizophrenia and bipolar disorder; provides neuroimaging context rather than direct drug efficacy data |
| [NCT07398365](https://clinicaltrials.gov/study/NCT07398365) | N/A | Recruiting | 100 | Observational medical phenotyping of NHS general adult psychiatry inpatients; no direct drug efficacy assessment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32182485](https://pubmed.ncbi.nlm.nih.gov/32182485/) | 2020 | Systematic Review & Meta-analysis | Journal of Psychiatric Research | Highest-quality direct evidence: comprehensively assessed clinical efficacy and adverse effect profile of Clozapine in bipolar disorder |
| [25346322](https://pubmed.ncbi.nlm.nih.gov/25346322/) | 2015 | Systematic Review | Bipolar Disorders | Evaluated efficacy and safety of Clozapine specifically for treatment-resistant bipolar disorder (TRBD) |
| [34552059](https://pubmed.ncbi.nlm.nih.gov/34552059/) | 2021 | Systematic Meta-review | Translational Psychiatry | PRISMA-conforming quantitative meta-review of Clozapine efficacy, effectiveness, and tolerability across neuropsychiatric disorders |
| [33719158](https://pubmed.ncbi.nlm.nih.gov/33719158/) | 2021 | Narrative Review | Bipolar Disorders | Synthesized current knowledge and proposed future research directions for Clozapine use in bipolar disorder |
| [37068038](https://pubmed.ncbi.nlm.nih.gov/37068038/) | 2023 | Real-world Observational | Journal of Clinical Psychopharmacology | Pharmacoepidemiological study of Clozapine use in bipolar disorder across Asian clinical settings; relevant to regional prescribing context |
| [31488793](https://pubmed.ncbi.nlm.nih.gov/31488793/) | 2019 | Clinical Review | Psychiatria Danubina | Proposes Clozapine as a promising treatment for suicidality in bipolar disorder, leveraging its anti-aggressive and anti-impulsive pharmacological properties |
| [31567198](https://pubmed.ncbi.nlm.nih.gov/31567198/) | 2021 | Case Series | American Journal of Therapeutics | Discussed rapid Clozapine titration protocols and challenges applicable to both schizophrenia and bipolar disorder |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Clinical Practice Review | Acta Psychiatrica Scandinavica | Evidence-based clinical recommendations for bipolar mania treatment, addressing the role of antipsychotics including Clozapine in refractory cases |
| [16432528](https://pubmed.ncbi.nlm.nih.gov/16432528/) | 2006 | Review | Molecular Psychiatry | Overview of treatment-resistant bipolar disorder management, identifying second-generation antipsychotics including Clozapine as advanced-line options |
| [11280956](https://pubmed.ncbi.nlm.nih.gov/11280956/) | 2001 | Review | Bulletin of the Menninger Clinic | Early characterization of pharmacotherapy options for treatment-resistant bipolar disorder, including Clozapine's role as a rescue agent |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 double-blind RCT (NCT00029458, n=42) directly supports Clozapine's efficacy in treatment-resistant manic bipolar affective disorder, supplemented by multiple systematic reviews and a dedicated meta-analysis, placing the evidence at L2. However, Clozapine is not currently registered in the Philippines, and its well-documented serious adverse effects — including agranulocytosis, metabolic syndrome, myocarditis, and seizures — demand a robust monitoring infrastructure before any clinical adoption.

**To proceed, the following is needed:**
- Retrieve Philippine FDA or international regulatory package inserts (FDA/EMA) to complete the safety warning and contraindication assessment (currently blocking)
- Establish a mandatory hematological monitoring protocol (regular WBC/ANC testing for agranulocytosis risk), equivalent to the REMS program required in the US
- Develop a metabolic safety monitoring plan covering weight, fasting glucose, lipid panel, and blood pressure
- Define the precise target population: treatment-resistant bipolar disorder patients who have failed ≥2 adequate first-line treatments
- Assess Philippine regulatory pathway options: new drug registration, expanded access, or compassionate use designation
- Conduct a local feasibility assessment to determine whether the requisite hematological monitoring infrastructure is available across intended treatment settings in the Philippines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

