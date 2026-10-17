---
layout: default
title: Bromocriptine
parent: Model Prediction Only (L5)
nav_order: 50
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Bromocriptine: predicted new indication Congenital disorder of glycosylation with defective fucosylation (evidence level L5). Approved use: Parkinson disease, hyperprolactinemia, acromegaly"
monitor_inn: "Bromocriptine"
predicted_indications: ["congenital disorder of glycosylation with defective fucosylation", "polymicrogyria, perisylvian, with cerebellar hypoplasia and arthrogryposis", "retinal dystrophy with or without extraocular anomalies", "atypical glycine encephalopathy", "myopia 26, X-linked, female-limited", "hydranencephaly (disease)", "myopia X-linked", "Charcot-Marie-Tooth disease, demyelinating, type 1G", "schizophrenia", "syndromic myopia"]
---

# Bromocriptine
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

# Bromocriptine: From Parkinson Disease and Hyperprolactinemia to Congenital Disorder of Glycosylation with Defective Fucosylation

## One-Sentence Summary

Bromocriptine is a dopamine agonist, originally used for Parkinson disease, hyperprolactinemia, and acromegaly.
The TxGNN model predicts it may be effective for **congenital disorder of glycosylation with defective fucosylation**,
but **no clinical trials and no publications** currently support this prediction. It is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Parkinson disease, hyperprolactinemia, acromegaly (from the knowledge graph; no approved-indication text is available from local registrations) |
| Predicted New Indication | Congenital disorder of glycosylation with defective fucosylation |
| TxGNN Prediction Score | 99.83% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled data. Based on general pharmacology, bromocriptine is a dopamine D2 receptor agonist. Its efficacy in Parkinson disease and hyperprolactinemia is well established.

For this predicted indication, no mechanistic link has been identified. Congenital disorder of glycosylation with defective fucosylation is an inherited metabolic disorder of fucose handling, and dopamine D2 agonism has no known relationship to fucosylation pathways. The high score (99.83%) reflects a pattern found by the model in the knowledge graph, not supporting biological or clinical evidence. This prediction should be treated as a hypothesis only.

**Other high-ranking predictions:** Among the top 10 predictions, a few have limited supporting material, but none reaches clinical-level evidence:
- **Retinal dystrophy** (score 99.82%, L4): one 2024 preclinical study of a three-drug repurposing combination (tamsulosin, metoprolol, bromocriptine) and one 1991 case report (Goldmann-Favre syndrome, cyclosporin A plus bromocriptine). The effect of bromocriptine alone cannot be separated out.
- **Schizophrenia** (score 99.73%, L4): one small open-label Phase 4 trial, which targets metabolic problems (prediabetes) rather than the psychiatric illness itself. A case report also describes bromocriptine-induced schizophrenia, so dopamine agonism may worsen psychosis.
- **Myopia-related conditions** (ranks 5, 7, 10): dopamine is known to influence eye growth in animal models, but there is no bromocriptine-specific evidence.
- The remaining predictions (polymicrogyria, atypical glycine encephalopathy, hydranencephaly, Charcot-Marie-Tooth type 1G) have no plausible mechanistic link.

## Clinical Trial Evidence

Currently no related clinical trials registered for the top-ranked predicted indication.

For reference, the only trial found among the top 10 predictions is for schizophrenia (rank 9):

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03575000](https://clinicaltrials.gov/study/NCT03575000) | Phase 4 | Not yet recruiting | 15 | Open-label pilot of adjunctive bromocriptine for antipsychotic-associated impaired glucose tolerance/insulin resistance in schizophrenia with prediabetes. Tests safety and tolerability; no results yet. |

## Literature Evidence

Currently no related literature available for the top-ranked predicted indication.

For reference, the most relevant publications among the other top 10 predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39009597](https://pubmed.ncbi.nlm.nih.gov/39009597/) | 2024 | Preclinical | Nature Communications | Combination of tamsulosin, metoprolol, and bromocriptine showed mutation-agnostic benefit in preclinical retinopathy models (retinal dystrophy, rank 3) |
| [29342497](https://pubmed.ncbi.nlm.nih.gov/29342497/) | 2018 | Systematic review | Cochrane Database Syst Rev | Catecholaminergic drugs for antipsychotic-induced tardive dyskinesia; no clear evidence of effectiveness (schizophrenia, rank 9) |
| [6574535](https://pubmed.ncbi.nlm.nih.gov/6574535/) | 1983 | Clinical study | Psychiatry Research | Small study (10 patients) of bromocriptine in chronic schizophrenia (schizophrenia, rank 9) |
| [8120934](https://pubmed.ncbi.nlm.nih.gov/8120934/) | 1993 | Case report | J Natl Med Assoc | Schizophrenia developed after starting low-dose bromocriptine and resolved after stopping (safety signal) |
| [1753674](https://pubmed.ncbi.nlm.nih.gov/1753674/) | 1991 | Case report | Klin Monatsbl Augenheilkd | Goldmann-Favre syndrome treated with cyclosporin A and bromocriptine (retinal dystrophy, rank 3) |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0058 | Bromocriptine | Not specified | Not specified (status: cancelled) |

The only registration found is cancelled, so no valid single-ingredient or combination registration is currently on record.

## Safety Considerations

- **Contraindications suggested by the knowledge graph (not label text):** hypertensive disorders, liver disease, gallbladder disease, coronary artery disease, stroke and cerebrovascular disorders, cerebral infarction, and pre-eclampsia (mild, severe, HELLP syndrome).
- **Drug Interactions:** 87 interactions were found. Major interactions include **isometheptene** and **lorcaserin**. Moderate interactions include clarithromycin, metoclopramide, morphine, ethanol, promethazine, lansoprazole, deferasirox, and dronabinol, among others.
- **Psychiatric risk:** a case report describes psychosis triggered by bromocriptine, which is a concern for any use in schizophrenia.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5): there are no trials, no literature, and no plausible mechanism linking dopamine D2 agonism to fucosylation defects. In addition, the only Philippines registration is cancelled, so there is no currently marketed product.

**To proceed, the following is needed:**
- Mechanistic evidence linking bromocriptine to fucosylation or glycosylation pathways (e.g., in vitro or cell-model studies)
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Confirmation of whether any valid bromocriptine registration exists in the Philippines
- If a different indication is preferred, consider re-evaluating retinal dystrophy (preclinical lead) or adjunctive metabolic management in schizophrenia (ongoing Phase 4 trial), after resolving the psychiatric safety question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

