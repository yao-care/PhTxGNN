---
layout: default
title: Paliperidone
parent: 僅模型預測 (L5)
nav_order: 267
evidence_level: L5
indication_count: 10
---

# Paliperidone
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

# Paliperidone: From Schizophrenia to Retinal Dystrophy with Extraocular Anomalies

## One-Sentence Summary

Paliperidone (9-hydroxyrisperidone) is a second-generation antipsychotic approved globally for schizophrenia and schizoaffective disorder, though currently not registered in the Philippines.
The TxGNN model's highest-ranked prediction — **Retinal Dystrophy with or without Extraocular Anomalies** — carries a score of 99.92%, yet lacks mechanistic support and is assessed as a likely model artifact driven by indirect knowledge graph connectivity.
Across all 10 ranked predictions, only **Treatment-Refractory Schizophrenia (rank 10)** demonstrates a coherent pharmacological rationale, backed by **4 clinical trials** and **2 publications**, making it the sole actionable signal in this candidate pack.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Schizophrenia / Schizoaffective Disorder (globally approved; not registered in Philippines) |
| Predicted New Indication (Rank 1) | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.92% |
| Evidence Level | L5 (model prediction only) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Paliperidone is the primary active metabolite of risperidone (9-OH-risperidone). Although detailed MOA data is not present in this evidence pack, Paliperidone is well-established pharmacologically as a D2 dopamine receptor antagonist and 5-HT2A serotonin receptor antagonist, with additional activity at α1-adrenergic and H1-histamine receptors in the central nervous system. This receptor profile underlies its proven efficacy in schizophrenia and schizoaffective disorder across multiple regulatory jurisdictions.

**Regarding ranks 1–9 (retinal dystrophy, X-linked myopias, hydranencephaly, glycosylation disorders, CMT disease, and related conditions):** None of these predictions carry a plausible mechanistic connection to Paliperidone's pharmacology. Retinal dystrophy involves hereditary degeneration of photoreceptors (causative genes include RPGR and PRPF3); X-linked myopias arise from developmental defects in ocular axial growth (MYP1/PRSS56); hydranencephaly is an irreversible structural congenital brain defect — none are addressable through central dopamine or serotonin receptor antagonism. The evidence pack's own mechanistic annotations explicitly state "no plausible mechanistic link" for all nine. High TxGNN scores in this cluster most likely reflect indirect co-morbidity node connections through shared "extraocular anomalies" and "neurodevelopmental disorder" nodes within the knowledge graph, rather than genuine pharmacological signals.

**Regarding rank 10 (treatment-refractory schizophrenia):** This is the only pharmacologically coherent prediction. Paliperidone's D2 antagonism directly engages the same receptor system implicated in schizophrenia pathophysiology. While Clozapine remains the only Level A-evidence treatment for true treatment-refractory schizophrenia (TRS), paliperidone long-acting injectables (PP1M/PP3M) may benefit patients experiencing pseudo-resistance driven by medication non-adherence — a clinically distinct and important subpopulation. The existing trial data, however, is predominantly observational and does not use rigorous TRS definitions (e.g., Kane criteria) as the primary study endpoint.

---

## Clinical Trial Evidence

> **Note:** The top-ranked prediction (Rank 1 – Retinal Dystrophy) has no registered clinical trials. The 15 literature items retrieved for this indication cover general ophthalmic topics (orbital infections, congenital ptosis, lens anomalies, orbital vascular lesions) without any connection to Paliperidone; they are excluded from this report. The table below presents trials for **Rank 10 – Treatment-Refractory Schizophrenia**, the only prediction with registered trial data.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01860781](https://clinicaltrials.gov/study/NCT01860781) | Phase 4 | Completed | 30 | Prospective naturalistic case series evaluating Paliperidone Palmitate in three schizophrenia patient subgroups. Provides real-world safety and efficacy data for PP, but study population is broader schizophrenia rather than strictly defined TRS. |
| [NCT06060886](https://clinicaltrials.gov/study/NCT06060886) | Phase 4 | Unknown | 244 | Multicenter open-label RCT (SchizOMICS) comparing Aripiprazole vs Paliperidone/Risperidone using multi-omics data in first-episode psychosis. Paliperidone serves as a comparator arm; if confirmed, provides indirect safety and efficacy comparison data at adequate sample size. |
| [NCT07047651](https://clinicaltrials.gov/study/NCT07047651) | Phase 4 | Recruiting | 40 | Evaluates pharmacotherapy combined with two recovery-oriented programs (RECOVERYTRSGR for TRS, RECOVERYTRSBDGR for treatment-resistant bipolar disorder). Paliperidone's specific role is not specified in the title; results expected December 2027. |
| [NCT05741502](https://clinicaltrials.gov/study/NCT05741502) | Phase 4 | Terminated | 5 | Compared Clozapine vs non-Clozapine antipsychotics in TRS on inflammatory markers (IL-6 and others). Terminated early with only 5 participants enrolled — data are not statistically meaningful and do not contribute to repurposing decisions. |

---

## Literature Evidence

> **Note:** The table below covers literature for **Rank 10 – Treatment-Refractory Schizophrenia**. No literature was retrieved for ranks 2–9.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31648341](https://pubmed.ncbi.nlm.nih.gov/31648341/) | 2019 | Narrative Review | Actas Españolas de Psiquiatría | Reviews psychopharmacological evidence for schizoaffective disorder; discusses antipsychotic treatments including Paliperidone and highlights the absence of SAD-specific treatment guidelines, reflecting the broader evidence gap in this spectrum. |
| [23364281](https://pubmed.ncbi.nlm.nih.gov/23364281/) | 2013 | Evidence-based Review | Current Opinion in Psychiatry | Systematic review of pharmacological and psychosocial interventions in early-onset schizophrenia spectrum disorders; provides practical dosing, switching, and adverse effect monitoring guidance applicable to Paliperidone prescribing in refractory presentations. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
TxGNN's top 9 predictions for Paliperidone are assessed as knowledge graph artifacts — all involve hereditary structural or metabolic conditions (retinal dystrophies, congenital myopias, brain malformations, glycosylation disorders, peripheral neuropathy) that have no pharmacological interface with central D2/5-HT2A receptor antagonism. The only pharmacologically credible and evidence-backed signal is Treatment-Refractory Schizophrenia (rank 10), which currently sits at evidence level L3 with no Phase 2/3 RCT using strict TRS criteria as the primary endpoint; further research is warranted before any clinical development recommendation can be made.

**To proceed, the following is needed:**
- Resolve blocking data gap DG001: obtain the Philippines FDA (FDA Philippines) package insert to retrieve key warnings and contraindications before any safety screening can proceed
- Resolve high-priority data gap DG002: retrieve Paliperidone MOA data via DrugBank API to complete mechanistic analysis
- For **Treatment-Refractory Schizophrenia (rank 10)**: conduct a targeted systematic literature review using Kane criteria to identify observational cohort studies or retrospective analyses with well-defined TRS populations and quantified Paliperidone outcomes
- Consider designing a prospective registry study comparing PP1M/PP3M outcomes in pseudo-TRS (adherence-driven resistance) vs pharmacologically true TRS as the foundational next research step
- For **ranks 1–9**: no further investigation recommended; predictions are inconsistent with established pharmacology and are attributed to indirect knowledge graph associations rather than genuine drug-disease biology
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

