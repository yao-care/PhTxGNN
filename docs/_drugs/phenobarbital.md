---
layout: default
title: Phenobarbital
parent: Model Prediction Only (L5)
nav_order: 273
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Phenobarbital: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy (generalized tonic-clonic and partial seizures), migraine…"
monitor_inn: "Phenobarbital"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
---

# Phenobarbital
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

## Phenobarbital: From Epilepsy to Trigeminal Nerve Neoplasm
{: .text-alpha }

## One-Sentence Summary

Phenobarbital is a long-established anticonvulsant, originally used for epilepsy (including generalized tonic-clonic and partial seizures) and for migraine and headache-type conditions.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but there are **0 clinical trials** and only **1 publication** (a case series on Sturge-Weber syndrome, not on this tumour) behind this prediction.
It rests on model output alone and is not backed by specific evidence.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy (generalized tonic-clonic and partial seizures), migraine, Lennox-Gastaut syndrome. The Philippines licence record contains no indication text, so this comes from the knowledge-graph indication list. |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 (model prediction only) |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Phenobarbital is a barbiturate anticonvulsant, and its efficacy in epilepsy is well established. Its anticonvulsant effect is generally attributed to enhancing GABA-A receptor inhibition.

For trigeminal nerve neoplasm, **no credible mechanistic link was found**. The only retrieved paper concerns Sturge-Weber syndrome, a neurocutaneous disorder with seizures, not trigeminal nerve tumours. At most, phenobarbital could control seizures associated with a tumour or syndrome. That would be symptomatic treatment and not disease-modifying.

The very high TxGNN score appears to reflect proximity in the knowledge graph to epilepsy and other neurological conditions, not a specific therapeutic rationale. The prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | Review of 14 Sturge-Weber syndrome cases over 25 years, covering clinical features, course and treatment response. It does not address trigeminal nerve tumours. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0381 | Phenobarbital | Not stated | Not stated (status: cancelled) |

## Safety Considerations

**Knowledge-graph contraindication signals** (from drug-disease contraindication links in the TxGNN knowledge graph, not from package insert text):
- Liver: liver failure, liver disease, gallbladder disease
- Kidney: kidney disease, pyoureter
- Metabolic and porphyria: inherited porphyria, porphyrin metabolism disease, porphyria, hyperglycemia
- Endocrine: hypothyroidism, myxedema, congenital hypothyroidism
- Respiratory: chronic obstructive pulmonary disease (including severe early onset)
- Cardiovascular and blood: hypertension, hypertensive disorder, thrombocytopenia
- Gastrointestinal: gastric ulcer, peptic ulcer disease, gastritis
- Psychiatric: anxiety disorder, neurotic disorder, dysthymic disorder, insomnia, psychotic disorder, schizophreniform disorder, schizoaffective disorder, mental disorder
- Autoimmune: systemic lupus erythematosus (including paediatric)

**Drug Interactions** (100 interactions found; examples shown):
- **Major**: morphine (including liposomal), eliglustat, naldemedine, naloxegol, rolapitant
- **Moderate**: corticosteroids (hydrocortisone, prednisone, prednisolone, dexamethasone, betamethasone, triamcinolone), doxycycline, metronidazole, bupropion, aprepitant, pioglitazone, dronabinol, cholecalciferol, pyridoxine

Package insert warnings and contraindications for the Philippines were not available. Please refer to the package insert for full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone. There are no clinical trials, and the single retrieved paper does not concern the predicted disease. No mechanistic link to tumour biology was found, and the Philippines registration is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data (e.g., from DrugBank)
- Philippines package insert warnings and contraindications, which are currently missing and block safety screening
- Evidence that phenobarbital has a role in trigeminal nerve neoplasm, beyond symptomatic seizure control
- Clarification of whether a valid Philippines registration exists or would need to be renewed

**Other predictions in the same analysis (all Hold):**
The other nine predicted indications also have no clinical trials. Most are reflex-seizure types, which are extensions of the existing epilepsy indication, so they are not truly new uses.

| Predicted Indication | Evidence Level | Note |
|------|------|------|
| Orgasm-induced seizures | L5 | No literature |
| Micturition-induced seizures | L4 | Generic seizure literature only |
| Eating seizures | L4 | Case reports and animal studies |
| Thinking seizures | L4 | Class-level rationale only |
| Startle epilepsy | L4 | Case-level reports only |
| Audiogenic seizures | L4 | Mostly rodent and veterinary studies |
| Reading seizures | L4 | Non-specific literature |
| Trigeminal neuralgia | L4 | Carbamazepine is the standard drug; phenobarbital would lower its levels as a CYP inducer |
| Beta-ketothiolase deficiency | L5 | No mechanistic link, no literature |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

