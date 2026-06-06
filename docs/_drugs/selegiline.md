---
layout: default
title: Selegiline
parent: 僅模型預測 (L5)
nav_order: 305
evidence_level: L5
indication_count: 4
---

# Selegiline
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Selegiline: From Parkinson's Disease to Schizophrenia

## One-Sentence Summary

Selegiline is an irreversible, selective MAO-B inhibitor primarily approved for Parkinson's disease (oral formulation) and major depressive disorder (transdermal formulation).
The TxGNN model predicts it may be effective as augmentation therapy for **Schizophrenia** (negative symptoms),
with **1 clinical trial** and **20 publications**—including multiple randomized controlled trials and a 2023 systematic meta-analysis—currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Parkinson's disease (oral); Major depressive disorder (transdermal) |
| Predicted New Indication | Schizophrenia (negative symptoms) |
| TxGNN Prediction Score | 99.14% |
| Evidence Level | L2 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Selegiline is an irreversible, selective monoamine oxidase type B (MAO-B) inhibitor. By blocking MAO-B, it reduces the enzymatic catabolism of dopamine, raising dopamine concentrations in the striatum and prefrontal cortex. This mechanism is the foundation of its established efficacy in Parkinson's disease, where dopaminergic depletion drives both motor and non-motor symptoms.

The rationale for selegiline in schizophrenia rests on the **prefrontal hypodopaminergia hypothesis of negative symptoms**: while positive symptoms (hallucinations, delusions) reflect mesolimbic dopamine excess, negative symptoms (blunted affect, alogia, avolition, cognitive slowing) are associated with a deficit of dopaminergic tone in the prefrontal cortex. Conventional antipsychotics act as D2 antagonists and therefore do not address—and may in fact worsen—this prefrontal deficit. A selective MAO-B inhibitor that boosts prefrontal dopamine without broadly activating the mesolimbic system is thus mechanistically well-positioned as an **adjunct**, not a replacement, for antipsychotic therapy.

A secondary, complementary pathway involves oxidative stress. MAO-B catabolizes dopamine while generating hydrogen peroxide as a byproduct. Inhibiting this reaction reduces reactive oxygen species accumulation in neurons, providing antioxidant and anti-apoptotic effects. There is growing evidence that oxidative stress contributes to neuroprogression and grey matter loss in schizophrenia, making selegiline's neuroprotective properties a plausible additional benefit. Clinical studies have specifically tested selegiline as an augmentation agent added to risperidone or other antipsychotics, which aligns with this positioning.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00456976](https://clinicaltrials.gov/study/NCT00456976) | Early Phase 1 | Completed | 70 | Randomized, placebo-controlled trial evaluating selegiline augmentation of antipsychotic medication to reduce negative symptoms in inpatients with chronic schizophrenia; primary endpoint: decrease in negative symptom scores in the selegiline group |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [37087864](https://pubmed.ncbi.nlm.nih.gov/37087864/) | 2023 | Systematic Review + Meta-analysis | European Neuropsychopharmacology | Most comprehensive pooled analysis to date; evaluates selegiline efficacy and safety across psychiatric disorders for both oral and transdermal formulations; synthesizes evidence from multiple RCTs |
| [15677608](https://pubmed.ncbi.nlm.nih.gov/15677608/) | 2005 | RCT (multicenter, double-blind, placebo-controlled) | American Journal of Psychiatry | Pivotal multicenter trial; selegiline augmentation in outpatients with schizophrenia and moderate-to-severe negative symptoms; tests efficacy across multiple sites |
| [17972359](https://pubmed.ncbi.nlm.nih.gov/17972359/) | 2008 | RCT | Human Psychopharmacology | 8-week double-blind RCT of selegiline add-on to risperidone in chronic schizophrenia with prominent negative symptoms; directly tests the clinically relevant augmentation scenario |
| [8627275](https://pubmed.ncbi.nlm.nih.gov/8627275/) | 1996 | RCT | Journal of Nervous and Mental Disease | Pilot study; selegiline 5 mg b.i.d. added to chronic antipsychotic regimens in 21 patients; early positive signal for dopamine-targeted negative symptom improvement |
| [8102552](https://pubmed.ncbi.nlm.nih.gov/8102552/) | 1993 | RCT | Biological Psychiatry | Placebo-controlled trial of selegiline 10 mg/day for neuroleptic-induced tardive dyskinesia; 33 patients; informs selegiline tolerability within antipsychotic-treated schizophrenia populations |
| [17405823](https://pubmed.ncbi.nlm.nih.gov/17405823/) | 2007 | Review | Annals of Pharmacotherapy | Dedicated review evaluating the therapeutic role of selegiline specifically for negative symptoms of schizophrenia; summarizes the pre-2007 evidence base |
| [26848926](https://pubmed.ncbi.nlm.nih.gov/26848926/) | 2016 | Cochrane Review | Cochrane Database of Systematic Reviews | Examines antioxidant treatments for schizophrenia; contextualizes the oxidative stress hypothesis and selegiline's neuroprotective mechanism within the broader evidence for this approach |
| [16930948](https://pubmed.ncbi.nlm.nih.gov/16930948/) | 2006 | Systematic Review | Schizophrenia Research | Systematic review of pharmacological treatments for primary negative symptoms; benchmarks selegiline against other augmentation strategies |
| [10080262](https://pubmed.ncbi.nlm.nih.gov/10080262/) | 1999 | Case Series | Comprehensive Psychiatry | Three DSM-IV schizophrenia patients in a day treatment program showed significant improvement in negative symptoms and overall functioning after selegiline was added to their antipsychotic regimen; no adverse effects observed |
| [7831475](https://pubmed.ncbi.nlm.nih.gov/7831475/) | 1994 | Review | Progress in Neurobiology | Foundational mechanistic review of MAO-B inhibitors in neurological and psychiatric disorders; provides the pharmacological basis for the dopaminergic and neuroprotective rationale |

---

## Philippines Market Information

Selegiline currently has **no registered products in the Philippines**. There are no active marketing authorizations on record with the FDA Philippines for any formulation (oral tablet or transdermal patch). Any clinical use would require a new drug application or compassionate use authorization.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for clinical planning:** Although structured safety data was not retrievable in this evidence pack, selegiline's MAO-B inhibitor class carries well-recognized risks that should be reviewed prior to clinical use: hypertensive crisis at supratherapeutic oral doses (≥20 mg/day, where MAO-A selectivity is lost), serotonin syndrome risk with concomitant serotonergic agents, and tyramine dietary interactions at non-selective doses. These interactions are particularly relevant in a schizophrenia population given polypharmacy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A multicenter double-blind RCT (American Journal of Psychiatry, 2005), a confirmatory RCT with risperidone (2008), and a 2023 systematic meta-analysis provide consistent Phase 2-level evidence that selegiline augmentation meaningfully reduces negative symptoms in schizophrenia—a treatment gap that existing antipsychotics do not address. The mechanistic basis (prefrontal dopamine upregulation via MAO-B inhibition) is coherent and directly maps to the pathophysiology of negative symptoms.

**To proceed, the following is needed:**
- Full safety profile from the TFDA or FDA Philippines package insert, including contraindications, key warnings, and approved dosing range
- Drug-drug interaction assessment with antipsychotics commonly used in the Philippines (particularly risperidone, olanzapine, clozapine) and any co-prescribed serotonergic agents
- Regulatory pathway assessment: FDA Philippines new drug registration or compassionate use framework, given zero current market authorizations
- Definition of the target patient population (chronic schizophrenia with prominent negative symptoms on stable antipsychotic therapy; not acute-phase patients)
- Dose selection rationale: confirm low-dose oral selegiline (5–10 mg/day) remains within selective MAO-B range to avoid dietary tyramine restrictions at clinical doses
- Pharmacovigilance plan for manic switch risk and cardiovascular monitoring in the augmentation setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

