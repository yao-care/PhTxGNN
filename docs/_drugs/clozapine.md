---
layout: default
title: Clozapine
parent: Model Prediction Only (L5)
nav_order: 85
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
description: "Clozapine: predicted new indication Manic bipolar affective disorder (evidence level L5). Approved use: Not available in the Philippines registration data"
monitor_inn: "Clozapine"
predicted_indications: ["manic bipolar affective disorder", "Tourette syndrome", "trichotillomania", "schizophreniform disorder", "bipolar disorder", "major affective disorder", "attention deficit-hyperactivity disorder", "attention deficit hyperactivity disorder, inattentive type", "psychotic disorder", "Malan overgrowth syndrome"]
---

# Clozapine
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

## Clozapine: From Treatment-Resistant Psychosis to Manic Bipolar Affective Disorder
{: .text-alpha }

## One-Sentence Summary

Clozapine is an atypical antipsychotic. The data compiled for this report do not list an approved indication for it in the Philippines, although it is well established for treatment-resistant schizophrenia.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder** (the top-ranked prediction), and the closely related **bipolar disorder** has **13 clinical trials** and **20 publications** supporting this direction. The strongest evidence for bipolar disorder includes a completed Phase 3 placebo-controlled trial and a 2020 meta-analysis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available in the Philippines registration data (the one registration has no indication text) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 0.9995 |
| Evidence Level | L5 for manic bipolar affective disorder (one completed Phase 2 double-blind trial, n=42). The broader bipolar disorder prediction reaches L1. |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails (limited to treatment-refractory patients) |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on known information, clozapine acts on many receptors: D2 and 5-HT2A antagonism, plus broad serotonergic, muscarinic, histaminergic and adrenergic activity. It is the established agent for treatment-resistant schizophrenia and psychosis, and mechanistically it may be applicable to mania.

Mania and psychosis share symptoms such as agitation, impulsivity and psychotic features. A substantial group of manic patients do not respond to, or cannot tolerate, conventional treatment. Clozapine's multi-receptor profile plausibly supports anti-manic and mood-stabilizing effects in this group. A completed Phase 2 double-blind trial and a 2020 systematic review and meta-analysis provide direct clinical support. Most of the evidence comes from treatment-resistant populations, so the finding should not be generalized to all patients.

Other predicted indications are far less supported:
- **Schizophreniform disorder and psychotic disorder:** these are effectively extensions of the core schizophrenia use, so they confirm established use rather than repurposing. Psychotic disorder is supported by 2025 and 2026 RCTs and a 2021 meta-review.
- **Major affective disorder:** evidence is inherited from bipolar and transdiagnostic data, with no unipolar-specific data.
- **Tourette syndrome:** evidence is limited to case reports and a 1998 report, with no registered trials.
- **Trichotillomania, ADHD (including inattentive type) and Malan overgrowth syndrome:** these are model predictions with little or no supporting evidence.

## Clinical Trial Evidence

Trials for manic bipolar affective disorder and the closely related bipolar disorder (the highest-quality evidence is listed first):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00029458](https://clinicaltrials.gov/study/NCT00029458) | Phase 2 | Completed | 42 | Double-blind study of clozapine in treatment-resistant mania |
| [NCT00036582](https://clinicaltrials.gov/study/NCT00036582) | Phase 3 | Completed | 116 | Clozapine vs placebo in treatment-refractory bipolar disorder in children and adolescents |
| [NCT02562287](https://clinicaltrials.gov/study/NCT02562287) | Phase 4 | Unknown | 54 | Clozapine vs olanzapine, quetiapine or risperidone in treatment-resistant bipolar disorder |
| [NCT05603104](https://clinicaltrials.gov/study/NCT05603104) | Phase 3 | Recruiting | 1254 | Intensified pharmacological treatment (including clozapine) after first-line failure in schizophrenia, depression and bipolar depression |
| [NCT04580134](https://clinicaltrials.gov/study/NCT04580134) | Phase 4 | Recruiting | 524 | Randomized, double-blind study of clozapine response in a B-SNIP biotype, spanning psychotic and bipolar disorders |
| [NCT06011460](https://clinicaltrials.gov/study/NCT06011460) | N/A | Enrolling by invitation | 30 | Registry of adverse events during clozapine treatment in bipolar disorder |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | Active, not recruiting | 84 | Pharmacotherapy combined with recovery-oriented programs in treatment-resistant schizophrenia and bipolar disorder |
| [NCT02582736](https://clinicaltrials.gov/study/NCT02582736) | N/A | Completed | 725,489 | Retrospective cohort on atypical antipsychotics and hyperglycemic emergencies (metabolic safety signal) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [32182485](https://pubmed.ncbi.nlm.nih.gov/32182485/) | 2020 | Meta-analysis | J Psychiatr Res | Systematic review and meta-analysis of clozapine efficacy and adverse effects in bipolar disorder |
| [41192460](https://pubmed.ncbi.nlm.nih.gov/41192460/) | 2025 | Cohort / meta-analysis | Lancet Psychiatry | Transdiagnostic effectiveness and safety of clozapine across psychotic, affective and personality disorders |
| [25346322](https://pubmed.ncbi.nlm.nih.gov/25346322/) | 2015 | Systematic review | Bipolar Disord | Efficacy and safety of clozapine for treatment-resistant bipolar disorder |
| [33719158](https://pubmed.ncbi.nlm.nih.gov/33719158/) | 2021 | Review | Bipolar Disord | Overview of current knowledge on clozapine for bipolar disorder and future directions |
| [16432528](https://pubmed.ncbi.nlm.nih.gov/16432528/) | 2006 | Review | Mol Psychiatry | Treatment-resistant bipolar disorder: inadequate response remains common despite many new treatments |
| [31488793](https://pubmed.ncbi.nlm.nih.gov/31488793/) | 2019 | Review | Psychiatr Danub | Clozapine as a promising treatment for suicidality in bipolar disorder |
| [41262335](https://pubmed.ncbi.nlm.nih.gov/41262335/) | 2025 | Modelling study | Drug Des Devel Ther | Clozapine drug interactions and individualized dosing in bipolar disorder |
| [33460070](https://pubmed.ncbi.nlm.nih.gov/33460070/) | 2020 | Review | Acta Psychiatr Scand | Evidence-based treatment options for bipolar mania |
| [10682225](https://pubmed.ncbi.nlm.nih.gov/10682225/) | 2000 | Case series | Clin Neuropharmacol | 36 patients treated with ECT plus clozapine: 67% benefited, adverse reactions in 16.6% |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0114 | Clozapine | Not specified | Not specified (status: valid) |

## Safety Considerations

No package insert warnings or contraindications were available in the data compiled for this report. Please refer to the package insert for label safety information.

- **Contraindication signals from the knowledge graph (not label text):** the TxGNN knowledge graph links clozapine to several conditions, including:
  - Blood disorders: neutropenia, agranulocytosis, leukopenia.
  - Neurological and cerebrovascular conditions: epilepsy, stroke and other cerebrovascular disorders.
  - Heart and circulation: coronary artery disease, sudden cardiac arrest, heart conduction disease, pulmonary embolism, orthostatic hypotension and other hypotensive disorders.
  - Metabolic conditions: diabetes mellitus, diabetic ketoacidosis, hyperglycemia, hyperlipidemia, obesity.
  - Others: liver disease, respiratory failure, angle-closure glaucoma, benign prostatic hyperplasia, paralytic ileus.
- **Safety concerns in the literature:** myocarditis and cardiomyopathy, seizures and metabolic syndrome. A 2025 expert statement also discusses the burden of blood monitoring.
- **Drug interactions:** 100 interactions were recorded. The major-level ones in the data reviewed include bupropion, morphine and potassium citrate. Moderate-level ones include acarbose, famotidine, epinephrine, metformin, pioglitazone, omeprazole, atropine, cimetidine and several anticholinergic and antidiabetic agents.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- For manic bipolar affective disorder alone, the evidence is a single completed Phase 2 trial (n=42) plus a meta-analysis (L2). The broader bipolar disorder indication has a completed Phase 3 placebo-controlled trial (in children and adolescents) and several ongoing trials. Clozapine's risks (agranulocytosis, myocarditis, seizures, metabolic effects) argue for restricting use to treatment-refractory patients.
- Clozapine's only Philippines registration is cancelled, so no product is currently marketed there under this registration.

**To proceed, the following is needed:**
- Verify the regulatory status and approved indications of clozapine in the Philippines, including whether any product is currently valid.
- Obtain the package insert warnings and contraindications from the DOH-FDA Philippines (a blocking gap for safety screening).
- Obtain detailed mechanism of action data.
- Define a mandatory absolute neutrophil count monitoring plan, along with cardiac, seizure and metabolic monitoring.
- Review the 100 documented drug interactions for the likely co-medications in this population.
- Await results from the ongoing Phase 3/4 trials (NCT05603104, NCT04580134) and confirm the findings in adult treatment-refractory mania.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

