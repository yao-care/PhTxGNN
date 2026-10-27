---
layout: default
title: Baclofen
parent: Model Prediction Only (L5)
nav_order: 39
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Baclofen: predicted new indication Attention deficit-hyperactivity disorder (evidence level L5). Approved use: Not recorded in the Philippines registration data"
monitor_inn: "Baclofen"
predicted_indications: ["attention deficit-hyperactivity disorder", "nicotine dependence"]
---

# Baclofen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Baclofen: From Its Registered Use to Attention Deficit-Hyperactivity Disorder
{: .text-alpha }

## One-Sentence Summary

Baclofen is a GABA-B receptor agonist whose registered indication is not recorded in the data compiled for this report.
The TxGNN model predicts it may be effective for **attention deficit-hyperactivity disorder (ADHD)**, but there are **0 clinical trials** and **9 publications**, none of which test baclofen in ADHD.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Philippines registration data |
| Predicted New Indication | Attention deficit-hyperactivity disorder |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L5 (model prediction only) |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Baclofen is known as a GABA-B receptor agonist. In principle, this could modulate the dopamine and glutamate circuits involved in impulsivity and tics.

The link to ADHD is speculative. The retrieved literature covers Tourette syndrome treatment (ADHD is a common comorbidity there), rodent studies of impulsivity and decision-making, and methylphenidate prescribing. None of it tests baclofen in ADHD. Despite the very high model score (0.993), the prediction rests on adjacent conditions and preclinical models rather than direct evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications below evaluates baclofen for ADHD. Only PMID 10342599 involves baclofen, and it concerns tic disorders.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Clinical report | J Child Neurol | 450 patients with tics/Tourette syndrome treated with baclofen/botulinum toxin type A and rated on the Yale Global Tic Severity Scale; not an ADHD study |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatr Drugs | Tourette syndrome characteristics and management, including comorbid psychiatric conditions |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | Int Rev Neurobiol | Emerging Tourette syndrome treatments; ADHD noted as a common comorbidity |
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Review/Meta-analysis | Cureus | Behavioural, antipsychotic and alpha-agonist treatments for tics; no baclofen-ADHD data evident |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Clinical practice report | L'Encephale | Supervised off-label methylphenidate prescribing in adult ADHD; baclofen not studied |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Preclinical (rat) | Brain Res | EEG effects of neurotransmitter agonists in an ADHD rat model (spontaneously hypertensive) versus an epilepsy model |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Preclinical (rodent) | Psychopharmacology | Guanfacine (α2A agonist) in the ventral hippocampus reduces impulsive decision-making |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | Preclinical (rodent) | Neuropsychopharmacology | Roles of the anterior cingulate cortex and basolateral amygdala in effort-based decisions |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | Preclinical (rodent) | Eur J Neurosci | Habenula function in social play behaviour in rats |

## Philippines Market Information

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0039 | Baclofen | Cancelled |

Dosage form and approved indication text are not recorded for this registration. No valid single-ingredient or combination registrations currently exist.

## Safety Considerations

Package insert warnings and contraindications were not available. Please refer to the package insert for safety information.

- **Contraindication signals from the knowledge graph** (drug-disease edges in the TxGNN knowledge graph, not label text): epilepsy, kidney disease, psychotic disorders (including schizophrenia, schizophreniform and schizoaffective disorders), mental disorder, stroke and cerebrovascular disorders, cerebral infarction, autonomic nervous system disease (including autonomic dysreflexia and Horner syndrome), pyoureter, and disease of the neck of the urinary bladder.
- **Drug Interactions**: 100 interactions were recorded. The main ones are:
  - Major: morphine, liposomal morphine.
  - Moderate: dronabinol, metoclopramide, nabilone, opium, sibutramine, difenoxin, diphenoxylate.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but there are no clinical trials and no literature testing baclofen in ADHD. Evidence is model prediction only (L5), the mechanistic link is speculative, and the only Philippines registration is cancelled. For comparison, the second-ranked prediction, nicotine dependence (score 99.19%), has Phase 2 trials and preclinical support (evidence L2), and may be a more promising direction for this drug.

**To proceed, the following is needed:**
- Mechanism-of-action data and a stronger rationale linking GABA-B agonism to ADHD pathophysiology
- Any clinical or well-designed preclinical study of baclofen in ADHD
- The package insert, to establish the registered indication, warnings and contraindications
- Clarification of why the Philippines registration was cancelled, and of the regulatory pathway if development proceeds
- A safety review for neuropsychiatric populations, given the knowledge-graph contraindication signals (psychotic disorders, epilepsy) and the interaction with opioids
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

