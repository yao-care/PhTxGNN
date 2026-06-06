---
layout: default
title: Risperidone
parent: 僅模型預測 (L5)
nav_order: 295
evidence_level: L5
indication_count: 6
---

# Risperidone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Risperidone: From Schizophrenia to Major Affective Disorder

> **Note:** This Evidence Pack covers 6 predicted indications (TxGNN ranks 1–6). This report focuses on **Major Affective Disorder** (rank 6 by TxGNN score), which carries the strongest clinical evidence (L1) and the most actionable recommendation. Other predictions — including trichotillomania (L3, 10 publications) and Phelan-McDermid syndrome (L4, 3 publications) — are noted where relevant but not detailed here.

---

## One-Sentence Summary

Risperidone is a second-generation (atypical) antipsychotic, globally established for schizophrenia and bipolar mania, with additional FDA approval for irritability associated with autistic disorder.
The TxGNN model predicts it may be effective for **Major Affective Disorder** (encompassing major depressive disorder and bipolar disorder),
with **36 clinical trials** and **20 publications** supporting this direction — including a pivotal Phase 3 double-blind RCT (NCT00095134, n=630) directly comparing risperidone augmentation versus placebo in antidepressant-refractory MDD.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia (globally approved; not registered in the Philippines) |
| Predicted New Indication | Major Affective Disorder |
| TxGNN Prediction Score | 99.11% |
| Evidence Level | L1 |
| Philippines Market Status | Not registered |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in this Evidence Pack (flagged as data gap DG002, pending DrugBank API retrieval). Based on established pharmacological literature, risperidone is a combined dopamine D2 receptor and serotonin 5-HT2A receptor antagonist. Its atypical antipsychotic profile — distinguishing it from older, purely dopaminergic agents — stems directly from this dual-receptor blockade.

The mechanistic bridge from schizophrenia to major affective disorder is coherent. 5-HT2A antagonism disinhibits prefrontal cortical neurons, enhancing dopamine and norepinephrine release in the prefrontal cortex — a recognized mechanism for augmenting the antidepressant effect of SSRIs and SNRIs in treatment-resistant depression. D2 receptor blockade in the limbic system simultaneously stabilizes dopamine hyperactivity relevant to manic and mixed episodes in bipolar disorder. This dual action positions risperidone as a pharmacologically versatile adjunct across the full spectrum of major affective pathology.

Major affective disorder and schizophrenia share overlapping neurobiological substrates: dysregulation of dopamine-serotonin circuits, frontal-limbic dysconnectivity, and cortico-striato-thalamo-cortical (CSTC) loop dysfunction. TxGNN's knowledge graph model maps these shared molecular and clinical pathways, yielding a high prediction score that is — unusually — already confirmed by a substantial clinical evidence base.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00095134](https://clinicaltrials.gov/study/NCT00095134) | Phase 3 | Completed | 630 | **Pivotal trial**: double-blind RCT comparing adjunctive risperidone vs placebo in MDD patients with sub-optimal antidepressant response; primary evidence for risperidone augmentation in TRD |
| [NCT00044681](https://clinicaltrials.gov/study/NCT00044681) | Phase 3 | Completed | 258 | Risperidone augmentation of SSRI in treatment-resistant depression; also assessed long-term maintenance effect vs placebo augmentation in older and younger adults |
| [NCT00174577](https://clinicaltrials.gov/study/NCT00174577) | Phase 3 | Unknown | 84 | Safety and efficacy of risperidone augmentation in patients with failed or partial response to an adequate antidepressant trial |
| [NCT01282632](https://clinicaltrials.gov/study/NCT01282632) | Phase 1/2 | Completed | 42 | Pilot double-blind head-to-head comparison of risperidone vs olanzapine as add-on to a failed SSRI in treatment-resistant depression |
| [NCT00203723](https://clinicaltrials.gov/study/NCT00203723) | Phase 4 | Terminated | 45 | Risperidone + ECT combination vs ECT alone for treatment-resistant depression; terminated early, partial safety and feasibility data available |
| [NCT00391222](https://clinicaltrials.gov/study/NCT00391222) | Phase 3 | Completed | 585 | Double-blind RCT: risperidone LAI monotherapy vs placebo for prevention of mood episodes in bipolar I disorder; olanzapine active control confirms study validity |
| [NCT00571688](https://clinicaltrials.gov/study/NCT00571688) | Phase 4 | Completed | 50 | Risperidone Consta (biweekly injection) vs treatment-as-usual for prevention of symptomatic relapse and rehospitalization in bipolar patients |
| [NCT00667745](https://clinicaltrials.gov/study/NCT00667745) | Phase 4 | Completed | 283 | Optimized lithium treatment in bipolar disorder (LiTMUS); risperidone used as comparator/combination agent providing indirect comparative effectiveness data |
| [NCT00176202](https://clinicaltrials.gov/study/NCT00176202) | Phase 3 | Completed | 65 | Head-to-head RCT: risperidone vs divalproex sodium in pediatric bipolar disorder, with MRI assessment of affected circuitry pre- and post-treatment |
| [NCT06512220](https://clinicaltrials.gov/study/NCT06512220) | Phase 2 | Recruiting | 12 | 5-HT2A receptor modulation and synaptic density imaging in treatment-resistant depression; risperidone used as 5-HT2A antagonist tool compound, directly strengthening the mechanistic basis for this indication |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [34986373](https://pubmed.ncbi.nlm.nih.gov/34986373/) | 2022 | Systematic Review + NMA | Journal of Affective Disorders | Network meta-analysis comparing multiple augmentation agents for treatment-resistant depression; quantifies risperidone's relative efficacy and discontinuation risk among SGAs |
| [35861202](https://pubmed.ncbi.nlm.nih.gov/35861202/) | 2023 | Systematic Review + Meta-analysis | Journal of Psychopharmacology | Evaluates augmentation and combination strategies for early-stage TRD; confirms ~50% of MDD patients fail first-line antidepressant, supporting the augmentation rationale |
| [34238049](https://pubmed.ncbi.nlm.nih.gov/34238049/) | 2021 | Meta-analysis | Journal of Psychopharmacology | Comparative meta-analysis of antidepressants + SGAs vs esketamine vs lithium in MDD; addresses relative efficacy and tolerability of risperidone-class augmentation |
| [35510505](https://pubmed.ncbi.nlm.nih.gov/35510505/) | 2023 | Systematic Review | Psychological Medicine | Most up-to-date comprehensive meta-analytic assessment of antipsychotics as both monotherapy and adjunctive therapy in MDD |
| [21154393](https://pubmed.ncbi.nlm.nih.gov/21154393/) | 2010 | Systematic Review (Cochrane) | Cochrane Database of Systematic Reviews | Foundational Cochrane review: second-generation antipsychotics for MDD and dysthymia; establishes SGA augmentation as evidence-based strategy |
| [17975181](https://pubmed.ncbi.nlm.nih.gov/17975181/) | 2007 | Randomized Trial | Annals of Internal Medicine | Risperidone for treatment-refractory MDD — key original RCT; published in high-impact general medicine journal, establishing augmentation benefit outside psychiatric specialty literature |
| [25295435](https://pubmed.ncbi.nlm.nih.gov/25295435/) | 2014 | Population-based Study | Journal of Clinical Psychiatry | Nationwide database study comparing aripiprazole, olanzapine, quetiapine, and risperidone augmentation in MDD; real-world effectiveness data across the SGA class |
| [20486830](https://pubmed.ncbi.nlm.nih.gov/20486830/) | 2010 | Review | Expert Opinion on Pharmacotherapy | Risperidone LAI as monotherapy and adjunctive therapy for bipolar I maintenance; addresses adherence benefits and long-term efficacy of long-acting formulation |
| [21189367](https://pubmed.ncbi.nlm.nih.gov/21189367/) | 2011 | Review | Annals of Pharmacotherapy | Focused review of risperidone augmentation specifically for MDD patients failing antidepressant monotherapy; practical clinical guidance |
| [34884874](https://pubmed.ncbi.nlm.nih.gov/34884874/) | 2021 | Comprehensive Review | International Journal of Molecular Sciences | Broad review of pharmacological augmentation in TRD across PubMed, ISI Web, and PsychInfo; identifies risperidone among supported augmentation candidates |

---

## Philippines Market Information

Risperidone is **not currently registered** in the Philippines (0 active licenses on record as of 2026-06-05). Despite being a globally established medication with decades of clinical use and multiple international approvals, no FDA Philippines authorization has been identified in this Evidence Pack. A dedicated regulatory pathway assessment will be required before any clinical development or commercial introduction for the major affective disorder indication.

---

## Safety Considerations

Please refer to the package insert for safety information. Key warnings, contraindications, and drug interaction data were not available in this Evidence Pack (flagged as blocking data gap DG001) and must be retrieved from official Philippines FDA or TFDA prescribing information before any clinical application.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
At least two completed Phase 3 RCTs directly studying risperidone in major affective disorder populations (NCT00095134, n=630; NCT00391222, n=585) qualify this evidence at L1, and multiple Cochrane-quality systematic reviews and network meta-analyses corroborate the SGA augmentation strategy across both unipolar and bipolar spectra. The mechanistic rationale — dual D2/5-HT2A antagonism as antidepressant augmentation — is well-established and biologically coherent.

**To proceed, the following is needed:**
- Retrieve complete MOA documentation from DrugBank API (data gap DG002, severity: High)
- Retrieve Philippines FDA or TFDA package insert for full warnings, contraindications, and DDI profile (data gap DG001, severity: Blocking — required before safety tier assessment)
- Define the specific clinical target: MDD augmentation (NCT00095134 model) vs bipolar I maintenance (NCT00391222 model), as these require distinct monitoring plans
- Develop a Philippines market entry regulatory strategy (no current registrations; pathway from global data dossier needed)
- Assess available formulations (oral vs LAI) for compatibility with target indication and patient population
- Review additional evidence for secondary predictions: trichotillomania (L3, 10 case series/reviews spanning 1997–2025) and Phelan-McDermid syndrome (L4, zebrafish model + case report) may warrant separate targeted assessments

---

*This report is generated for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Data cutoff: 2026-06-05.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

