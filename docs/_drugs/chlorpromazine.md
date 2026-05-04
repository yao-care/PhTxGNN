---
layout: default
title: Chlorpromazine
parent: 僅模型預測 (L5)
nav_order: 72
evidence_level: L5
indication_count: 10
---

# Chlorpromazine
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

# Chlorpromazine: From Schizophrenia to Early-Onset Schizophrenia

## One-Sentence Summary

Chlorpromazine is the prototypical first-generation antipsychotic (phenothiazine class), established for treating adult schizophrenia and psychotic disorders through dopamine D2 receptor blockade.
The TxGNN model's most clinically actionable prediction is **Early-Onset Schizophrenia** (disease onset <18 years), with **1 clinical trial** and **8 publications** currently supporting this direction.
The top 9 model-ranked predictions (Ranks 1–9, including retinal dystrophy and various congenital disorders) are assessed as **likely false positive signals** with no supporting evidence and no plausible mechanistic link — they are documented below but excluded from the primary evaluation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia and psychotic disorders (first-generation antipsychotic; well established in global clinical practice) |
| Predicted New Indication | Early-Onset Schizophrenia (highest-evidence actionable prediction among all 10 candidates) |
| TxGNN Prediction Score | 99.47% |
| Evidence Level | L3 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Chlorpromazine is the world's first clinically approved antipsychotic, belonging to the phenothiazine class. Its primary mechanism is potent blockade of dopamine D2 receptors in the mesolimbic pathway, which reduces dopaminergic hyperactivity — the neurochemical core of positive psychotic symptoms (hallucinations, delusions). It also antagonizes histamine H1, muscarinic M1, and alpha-1 adrenergic receptors, contributing to sedation, anticholinergic effects, and orthostatic hypotension respectively. Detailed MOA data from DrugBank was unavailable in this evidence pack (Data Gap DG002); however, Chlorpromazine's pharmacology is extensively characterized in decades of published literature.

Early-onset schizophrenia (EOS, onset before age 18) shares the same core neurobiology as adult-onset disease: mesolimbic D2 hyperactivity, prefrontal-limbic dysconnectivity, and neurodevelopmental deviation. This makes the mechanistic rationale for Chlorpromazine in EOS directly transferable — the molecular target is identical, and the clinical syndrome is diagnostically continuous with the adult form. Chlorpromazine carries L1 evidence across adult schizophrenia RCTs globally, but pediatric/adolescent-specific controlled trials are sparse, bringing EOS-specific evidence to L3. Notably, PMID 18408624 directly reports BDNF genotype-dependent chlorpromazine-induced extrapyramidal syndrome (EPS) in schizophrenia patients, providing direct pharmacological evidence linking this drug to the EOS disease node in the knowledge graph.

**Note on Ranks 1–9 (False Positive Assessment):** The highest TxGNN-scored predictions — retinal dystrophy, CDG with fucosylation defects, X-linked myopia variants, hydranencephaly, polymicrogyria, Charcot-Marie-Tooth 1G, and atypical glycine encephalopathy — all score >99.9% but have zero supporting clinical trials or relevant literature, and none have a plausible mechanistic connection. Chlorpromazine's phenothiazine ring is known to accumulate in retinal pigment epithelium (a documented adverse effect), creating indirect KG node connections to retinal diseases that the model interprets as therapeutic signals. Similarly, its broad CNS receptor profile generates non-specific links to neurological disease nodes. CMT1G warrants a specific safety flag: Chlorpromazine's known neurotoxic potential could worsen demyelinating neuropathy, making it a contraindication rather than a candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT06128408](https://clinicaltrials.gov/study/NCT06128408) | N/A | Unknown | 300 | Observational study characterizing treatment-resistant schizophrenia from illness onset (TRO). Finds that up to 30% of antipsychotic-naive first-episode patients fail to respond to standard antipsychotic treatment from the start, and TRO accounts for ~80% of all treatment-resistant schizophrenia in long-term follow-up. Highly relevant to understanding EOS treatment landscape and antipsychotic selection, though not a direct Chlorpromazine intervention trial. Status requires verification. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18408624](https://pubmed.ncbi.nlm.nih.gov/18408624/) | 2008 | Genetic Association Study | Pharmacogenetics and Genomics | BDNF gene is both a schizophrenia risk factor and directly associated with chlorpromazine-induced extrapyramidal syndrome in Chinese patients — the only study in this pack that directly names Chlorpromazine |
| [17915974](https://pubmed.ncbi.nlm.nih.gov/17915974/) | 2007 | Genetic Association Study | J Clin Psychiatry | AKT1 gene polymorphisms linked to schizophrenia susceptibility and antipsychotic treatment response; AKT1-PI3K pathway intersects D2 receptor signalling relevant to Chlorpromazine pharmacodynamics |
| [10703271](https://pubmed.ncbi.nlm.nih.gov/10703271/) | 1999 | Retrospective Cohort | Soc Psychiatry Psychiatr Epidemiol | Earlier age at schizophrenia onset correlated with higher typical neuroleptic dosage requirements — directly implicates Chlorpromazine-class drugs in EOS dosing considerations |
| [28976410](https://pubmed.ncbi.nlm.nih.gov/28976410/) | 2017 | Cross-sectional / Cohort | Clinical Neuropharmacology | Clinical features of EOS with comorbid OCD; highlights pharmacological complexity in the EOS population that Chlorpromazine prescribing must account for |
| [26916502](https://pubmed.ncbi.nlm.nih.gov/26916502/) | 2016 | Cohort | Acta Neuropsychiatrica | Theory of mind deficits in adolescents with EOS correlate with clinical severity and executive function; provides neurocognitive characterization of the target population |
| [24854724](https://pubmed.ncbi.nlm.nih.gov/24854724/) | 2015 | Cohort | L'Encephale | Neurological soft signs in EOS support the neurodevelopmental model underpinning dopamine-targeted pharmacotherapy |
| [22802957](https://pubmed.ncbi.nlm.nih.gov/22802957/) | 2012 | Case-control / Neuroimaging | PLoS ONE | Temporal gyrus gray matter volume reduction in first-episode EOS; confirms structural neurobiological basis consistent with D2-targeted antipsychotic intervention |
| [24289465](https://pubmed.ncbi.nlm.nih.gov/24289465/) | 2013 | Retrospective Cohort | Psychogeriatrics | Epidemiological comparison of early- vs. late-onset schizophrenia confirms EOS as a clinically distinct subgroup warranting dedicated pharmacotherapy evaluation |

---

## Philippines Market Information

Chlorpromazine is currently **not marketed in the Philippines**. No FDA Philippines authorization records are on file (total registrations: 0). No license table is available.

---

## Safety Considerations

Detailed warnings and contraindications from the Philippine or Taiwan package insert were not available in this evidence pack (Data Gap DG001). Please refer to the package insert for complete safety information.

**Critical safety considerations specific to EOS use (drawn from pharmacological literature):**
- **Extrapyramidal symptoms (EPS):** Chlorpromazine carries high EPS risk compared to second-generation antipsychotics (SGAs); risk may be further elevated in pediatric and adolescent populations. PMID 18408624 documents BDNF genotype-dependent EPS susceptibility.
- **Tardive dyskinesia:** Risk accumulates with duration of exposure; particularly concerning in patients who will require years of antipsychotic treatment beginning in adolescence.
- **Metabolic and cardiac effects:** Weight gain, glucose dysregulation, and QTc prolongation require baseline and ongoing monitoring.
- **Neurotoxicity concern in demyelinating conditions:** As noted for Rank 8 (CMT1G), Chlorpromazine's neurotoxic potential represents a contraindication in any comorbid demyelinating neuropathy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Chlorpromazine's D2 antagonism is mechanistically aligned with early-onset schizophrenia, which shares identical dopaminergic pathophysiology with adult-onset disease; however, the absence of Philippines market registration, limited pediatric-specific trial evidence (L3), and a well-documented EPS burden in young patients necessitate structured risk management before any clinical application.

**To proceed, the following is needed:**

- **Philippines regulatory pathway:** Assess FDA Philippines registration requirements and feasibility; the drug is currently entirely absent from the market
- **Package insert review:** Obtain and parse full TFDA/equivalent package insert to extract contraindications, warnings, and pediatric dosing guidance (Data Gap DG001)
- **MOA documentation:** Complete DrugBank pharmacology data retrieval (Data Gap DG002) to formally document receptor binding profile for regulatory submissions
- **Pediatric safety assessment:** Conduct a systematic review of EPS, tardive dyskinesia, metabolic, and cardiac adverse event rates specifically in patients <18 years treated with Chlorpromazine
- **Comparative effectiveness review:** Evaluate whether SGAs (risperidone, aripiprazole, olanzapine) — which have established pediatric approvals in multiple jurisdictions — offer superior benefit-risk profiles for EOS, as Chlorpromazine may not be a first-line candidate in this population
- **Pediatric-specific RCT identification:** Search for any head-to-head trials of Chlorpromazine versus SGAs in EOS to determine if L3 evidence can be upgraded
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

