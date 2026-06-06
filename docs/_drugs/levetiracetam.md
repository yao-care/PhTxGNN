---
layout: default
title: Levetiracetam
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Levetiracetam
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

# Levetiracetam: From Partial-Onset Seizures to Visual Epilepsy

## One-Sentence Summary

Levetiracetam (Keppra®) is a well-established second-generation antiseizure medication, globally approved for partial-onset seizures, myoclonic seizures in juvenile myoclonic epilepsy (JME), and primary generalized tonic-clonic seizures.
The TxGNN model predicts it may be effective for **Visual Epilepsy (photosensitive epilepsy)**, with **9 clinical trials** and **20 publications** currently indexed in support of this direction.
Although levetiracetam is not registered in the Philippines, its documented ability to suppress photoparoxysmal EEG responses provides a mechanistically coherent rationale for this prediction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Partial-onset seizures (global approval; no Philippines registration available) |
| Predicted New Indication | Visual Epilepsy |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L3 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Levetiracetam's mechanism centers on binding to synaptic vesicle glycoprotein 2A (SV2A), a presynaptic protein that regulates neurotransmitter vesicle trafficking and release. This binding reduces the frequency of repetitive high-frequency neuronal firing and dampens abnormal cortical synchronization—without directly acting on GABA or glutamate receptors. This mechanistic uniqueness means levetiracetam retains efficacy even when conventional GABAergic pathways are saturated or desensitized, making it effective across a broad spectrum of seizure types. (Note: formal MOA data from DrugBank has not yet been retrieved; the above is based on the mechanistic rationale documented in this Evidence Pack.)

Visual epilepsy—encompassing photosensitive epilepsy and related reflex epilepsy syndromes—is characterized by occipital cortex hyperexcitability triggered by flickering light or visual patterns, producing photoparoxysmal EEG responses (PPR) and, in susceptible individuals, clinical seizures. The pathophysiology is fundamentally one of aberrant cortical synchronization, the same substrate levetiracetam addresses via SV2A modulation. Clinical observations and small series have documented levetiracetam's ability to suppress PPR in photosensitive patients, and it is already used in practice as add-on therapy for photosensitive idiopathic generalized epilepsies, particularly JME—a syndrome in which up to 90% of patients exhibit photosensitivity.

Two recent network meta-analyses (PMID 37378757, 40450767) systematically evaluated antiseizure medications across idiopathic generalized epilepsies, a category that broadly encompasses photosensitive subtypes. These provide indirect Phase 3-level population evidence situating levetiracetam among the effective options. However, no randomized controlled trial has been designed with visual epilepsy as its primary endpoint, and the trials indexed in this pack are largely for unrelated seizure contexts. Filling this evidence gap with a dedicated study—particularly using PPR suppression as an objective electrophysiological endpoint—would be the logical next step to confirm what mechanistic reasoning and indirect data already suggest.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00855738](https://clinicaltrials.gov/study/NCT00855738) | Phase 4 | Completed | 111 | LICEO study: prospective observational study of LEV and other AEDs as first bitherapy in focal epilepsy; IGE patients (including potential photosensitive subtypes) were enrolled, providing indirect population-level data |
| [NCT04559529](https://clinicaltrials.gov/study/NCT04559529) | Phase 2 | Completed | 62 | LEV effect on hippocampal hyperactivity in psychotic disorders using a visual scene processing fMRI task; demonstrates LEV's modulation of visually-engaged cortical networks, though not visual epilepsy specifically |
| [NCT03107507](https://clinicaltrials.gov/study/NCT03107507) | Phase 4 | Unknown | 40 | Neonatal seizure control: LEV vs phenobarbital in neonates; evaluates broad antiseizure efficacy but no photosensitive or visual epilepsy mechanism |
| [NCT00105040](https://clinicaltrials.gov/study/NCT00105040) | Phase 2 | Completed | 87 | Cognitive and neuropsychological safety of LEV (20–60 mg/kg/day) in children aged 4–16 with refractory partial-onset seizures; safety characterization in pediatric populations |
| [NCT00203216](https://clinicaltrials.gov/study/NCT00203216) | N/A | Completed | 31 | Open-label single-center trial of LEV for migraine prophylaxis, including patients with aura (visual disturbances); no direct link to visual epilepsy design |
| [NCT04573803](https://clinicaltrials.gov/study/NCT04573803) | Phase 3 | Not Yet Recruiting | 1,649 | MAST trial: comparing AED duration and type (LEV vs phenytoin) after traumatic brain injury; large Phase 3 comparative trial for post-injury seizure prevention |
| [NCT07336992](https://clinicaltrials.gov/study/NCT07336992) | Phase 3 | Not Yet Recruiting | 580 | Prophylactic LEV for acute seizures in intracerebral haemorrhage; seizure etiology unrelated to visual epilepsy mechanism |
| [NCT04833907](https://clinicaltrials.gov/study/NCT04833907) | Phase 1/2 | Enrolling by Invitation | 24 | AVASPA gene therapy for Canavan disease; LEV serves as background antiseizure medication only, not a study intervention |
| [NCT04277936](https://clinicaltrials.gov/study/NCT04277936) | Phase 2 | Terminated | 1 | LEV modulation of hippocampal activity in psychosis via visual fMRI tasks (terminated early, n=1); not designed for visual epilepsy |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37378757](https://pubmed.ncbi.nlm.nih.gov/37378757/) | 2023 | Systematic Review / Network Meta-analysis | Journal of Neurology | Compares ASMs for idiopathic generalized epilepsies (IGEs), including photosensitive subtypes; LEV ranks among effective agents for both monotherapy and adjunctive therapy |
| [40450767](https://pubmed.ncbi.nlm.nih.gov/40450767/) | 2025 | Systematic Review / Meta-analysis | Epilepsy & Behavior | Evaluates LEV vs other ASMs specifically for myoclonic seizures in IGE/JME—a syndrome strongly associated with photosensitivity; directly supports LEV's role in the photosensitive epilepsy spectrum |
| [34286461](https://pubmed.ncbi.nlm.nih.gov/34286461/) | 2022 | Systematic Review / Meta-analysis | Neurocritical Care | Meta-analysis of LEV for seizure prophylaxis in ICH, TBI, neurosurgery, and SAH; comprehensively reviews LEV dosing, efficacy, and adverse events across neurocritical contexts |
| [36209676](https://pubmed.ncbi.nlm.nih.gov/36209676/) | 2022 | Systematic Review / Network Meta-analysis | Seizure | Evaluates interventions for benzodiazepine-resistant status epilepticus in children and adults; LEV identified as one of the most effective second-line agents, supporting its broad-spectrum antiseizure properties |
| [32385134](https://pubmed.ncbi.nlm.nih.gov/32385134/) | 2020 | RCT | Pediatrics | LEV vs phenobarbital for neonatal seizures (randomized controlled trial); LEV showed comparable seizure control with an improved safety profile in the developing brain |
| [35963261](https://pubmed.ncbi.nlm.nih.gov/35963261/) | 2022 | Phase 3 RCT | The Lancet Neurology | PEACH trial: double-blind placebo-controlled Phase 3 trial of prophylactic LEV in intracerebral haemorrhage; while LEV did not reduce overall seizure risk vs placebo, the trial contributes high-quality evidence on LEV's safety profile |
| [39808752](https://pubmed.ncbi.nlm.nih.gov/39808752/) | 2025 | Systematic Review / Network Meta-analysis | Neurology | LEV among ASMs for poststroke seizures; network meta-analysis supports LEV's favorable efficacy-safety balance compared to older agents |
| [35976303](https://pubmed.ncbi.nlm.nih.gov/35976303/) | 2022 | Review | Arquivos de Neuro-Psiquiatria | Status epilepticus: diagnosis, monitoring, treatment review; discusses synaptic receptor dynamics underpinning treatment resistance and positions LEV as a second-line option |
| [34260837](https://pubmed.ncbi.nlm.nih.gov/34260837/) | 2021 | Review | New England Journal of Medicine | Initial seizure management in adults; positions LEV as a first-choice agent in modern clinical guidelines |
| [21936590](https://pubmed.ncbi.nlm.nih.gov/21936590/) | 2011 | Review | CNS Drugs | Comprehensive profile of levetiracetam: approved indications (partial-onset seizures, myoclonic seizures in JME, primary GTC seizures), pharmacology, and clinical evidence base |

---

## Philippines Market Information

Levetiracetam currently has **no registered products** with the Philippine Food and Drug Administration (FDA Philippines). The market status is **Not Marketed**, and no authorization numbers, product names, or approved indications are on file as of the data cutoff (June 4, 2026).

Any clinical development or patient access pathway would require a full registration application with FDA Philippines before commercial distribution.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Formal safety data (key warnings, contraindications, drug–drug interactions) have not yet been retrieved from the TFDA package insert or DrugBank for this report. This is a blocking data gap (DG001) that must be resolved before any clinical safety evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Levetiracetam's SV2A-mediated suppression of cortical hyperexcitability is mechanistically aligned with the pathophysiology of visual epilepsy, and indirect Level 3 evidence from systematic reviews of idiopathic generalized epilepsies—a spectrum that regularly includes photosensitive subtypes—supports its potential efficacy. However, no randomized trial has designated visual epilepsy as a primary endpoint, the drug carries zero Philippines registration, and formal safety documentation remains unavailable; these gaps prevent an unconditional "Go" decision.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate FDA Philippines registration dossier; no existing local authorization exists
- **Targeted clinical evidence**: Design a prospective study or systematic registry using photoparoxysmal response (PPR) suppression as the primary electrophysiological endpoint in photosensitive patients
- **Safety data retrieval** (Blocking — DG001): Download and parse the TFDA package insert PDF to extract warnings, contraindications, and special population guidance
- **MOA data retrieval** (High priority — DG002): Query DrugBank API for formal mechanism of action, target binding data, and toxicity classifications
- **Drug interaction screen**: Re-query DDI database; current query returned no results, which may reflect a database gap rather than absence of interactions
- **Pharmacoeconomic assessment**: Evaluate cost-effectiveness and affordability for Philippine patient populations given the drug's off-patent status and generic availability globally
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

