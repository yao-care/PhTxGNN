---
layout: default
title: Selegiline
parent: Model Prediction Only (L5)
nav_order: 308
evidence_level: L5
indication_count: 4
last_modified_at: 2026-10-31
monitor_inn: "Selegiline"
predicted_indications: ["polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "schizophrenia", "congenital disorder of glycosylation with defective fucosylation", "retinal dystrophy with or without extraocular anomalies"]
description: "Selegiline: predicted new indication Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis (evidence level L5). Approved use: Not recorded in the local data"
---

# Selegiline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **4** 
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

## Selegiline: Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis
{: .text-alpha }

## One-Sentence Summary

Selegiline is an MAO-B inhibitor originally used for Parkinson's disease and depressive disorders.
The TxGNN model predicts it may be effective for **schizophrenia** (the predicted indication with the most supporting evidence among the top candidates), with **1 clinical trial** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis |
| TxGNN Prediction Score | 0.9915 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold (treat as a research question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, selegiline is a selective, irreversible MAO-B inhibitor. By slowing the breakdown of dopamine, it raises dopamine availability, which underlies its use in Parkinson's disease. At higher oral doses (20 mg/day or more) its activity becomes non-selective and also inhibits MAO-A.

Negative symptoms of schizophrenia (such as reduced motivation and emotional blunting) are thought to be linked to low dopamine activity in the prefrontal region. Adding a drug that boosts dopamine to standard antipsychotics is therefore a plausible strategy. Selegiline also has antioxidant and neuroprotective properties and may influence glutamate-related signalling, which could be relevant to cognitive deficits.

This rationale is reasonable but not proven. Published studies have given mixed results, as noted in one of the retrieved articles ("the results are contradictory so far").

Other predictions for this drug were reviewed and are not supported:
- **Polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis** (score 0.9915): a rare, genetically driven brain malformation. There is no plausible mechanism and no trials or literature.
- **Congenital disorder of glycosylation with defective fucosylation** (score 0.9902): MAO-B inhibition has no known link to fucosylation. No trials or literature.
- **Retinal dystrophy** (score 0.9901): only one indirect review on protein aggregation in retinal cells, with no selegiline-specific data (evidence level L4).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00456976](https://clinicaltrials.gov/study/NCT00456976) | Early Phase 1 | Completed | 70 | Randomized, placebo-controlled trial of selegiline added to antipsychotics for negative symptoms in inpatients with chronic schizophrenia. Registry data do not include results. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37087864](https://pubmed.ncbi.nlm.nih.gov/37087864/) | 2023 | Systematic review / Meta-analysis | Eur Neuropsychopharmacol | Appraises oral and transdermal selegiline across psychiatric disorders |
| [15677608](https://pubmed.ncbi.nlm.nih.gov/15677608/) | 2005 | RCT | Am J Psychiatry | Double-blind, placebo-controlled multicenter trial of selegiline augmentation for negative symptoms in outpatients |
| [17972359](https://pubmed.ncbi.nlm.nih.gov/17972359/) | 2008 | RCT | Hum Psychopharmacol | 8-week double-blind trial of selegiline added to risperidone for negative symptoms; earlier results described as contradictory |
| [10587287](https://pubmed.ncbi.nlm.nih.gov/10587287/) | 1999 | RCT | J Clin Psychopharmacol | Double-blind controlled study of deprenyl (selegiline) augmentation in 16 patients with predominantly negative symptoms |
| [8102552](https://pubmed.ncbi.nlm.nih.gov/8102552/) | 1993 | RCT | Biol Psychiatry | Placebo-controlled trial of selegiline 10 mg/day in 33 patients with tardive dyskinesia |
| [8627275](https://pubmed.ncbi.nlm.nih.gov/8627275/) | 1996 | Pilot study (open-label) | J Nerv Ment Dis | Low-dose selegiline (5 mg twice daily) added to antipsychotics in 21 patients with chronic schizophrenia or schizoaffective disorder |
| [17405823](https://pubmed.ncbi.nlm.nih.gov/17405823/) | 2007 | Review | Ann Pharmacother | Evaluates the role of selegiline in negative symptoms of schizophrenia |
| [16930948](https://pubmed.ncbi.nlm.nih.gov/16930948/) | 2006 | Systematic review | Schizophr Res | Pharmacological treatment of primary negative symptoms in schizophrenia |
| [26848926](https://pubmed.ncbi.nlm.nih.gov/26848926/) | 2016 | Systematic review | Cochrane Database Syst Rev | Antioxidant treatments for schizophrenia |
| [29552749](https://pubmed.ncbi.nlm.nih.gov/29552749/) | 2018 | Systematic review | Cochrane Database Syst Rev | Miscellaneous treatments for antipsychotic-induced tardive dyskinesia |

---

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (these come from model-linked drug-disease relationships, not from label text):
  - Psychiatric: psychotic disorder, schizophreniform disorder, schizoaffective disorder, bipolar disorder, major affective disorder, mental disorder
  - Cardiovascular and autonomic: orthostatic hypotension, postural orthostatic tachycardia syndrome, multiple system atrophy, sudden cardiac arrest, heart conduction disease
  - Organ disease: kidney disease, liver disease, gallbladder disease
  - Tumours: phaeochromocytoma, sympathetic paraganglioma, melanoma, and several cancers (adrenal gland, heart, duodenum, small intestine)
  - Movement disorders: tardive dyskinesia, lingual-facial-buccal dyskinesia

  Psychotic and schizophrenia-spectrum disorders appear in this list. This directly conflicts with the proposed new indication and needs careful clinical review.

- **Drug Interactions** (100 interactions recorded; examples from the first 20 shown):
  - **Major**: isometheptene, bupropion, diethylpropion, phentermine, dexfenfluramine
  - **Moderate**: epinephrine, metoclopramide, and several glucose-lowering drugs (insulins, glimepiride, repaglinide, nateglinide, chlorpropamide, acetohexamide)

Please refer to the package insert for further safety information, as label warnings and contraindications were not available.

---

## Conclusion and Next Steps

**Decision: Hold (treat as a research question)**

**Rationale:**
- Schizophrenia has the strongest support among the predictions, with several randomized trials of selegiline for negative symptoms. However, results are mixed, the registered trial is early phase, and no completed Phase 2/3 results are available in the compiled data. The other three predictions have no credible support.

**To proceed, the following is needed:**
- Review the full results of the RCTs (PMIDs 15677608, 17972359, 10587287) and the 2023 meta-analysis (PMID 37087864) to judge the net effect on negative symptoms
- Mechanism of action data (MOA) from DrugBank
- Package insert warnings and contraindications from the DOH-FDA Philippines
- A risk assessment of the psychosis-related contraindication signal and the major drug interactions (especially with antidepressants and sympathomimetics)
- Clarification of the regulatory status and availability of selegiline in the Philippines, since the sole registration is cancelled
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

