---
layout: default
title: Lamotrigine
parent: Model Prediction Only (L5)
nav_order: 198
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Lamotrigine: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Epilepsy, partial epilepsy, Lennox-Gastaut syndrome"
monitor_inn: "Lamotrigine"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "micturation-induced seizures", "audiogenic seizures", "thinking seizures", "orgasm-induced seizures", "eating seizures", "reading seizures"]
---

# Lamotrigine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Lamotrigine: From Epilepsy to Trigeminal Nerve Neoplasm (Top-Ranked Prediction), with Trigeminal Neuralgia as the Best-Supported Candidate

## One-Sentence Summary

Lamotrigine is an antiseizure medicine, originally used for epilepsy, partial epilepsy and Lennox-Gastaut syndrome.
The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm**, but the linked literature concerns trigeminal neuralgia rather than tumours, so this prediction is not supported by real evidence.
The best-supported candidate in the list is **trigeminal neuralgia**, with **2 completed clinical trials** and **19 publications** (small trials, plus guideline and review mentions).

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy, partial epilepsy, Lennox-Gastaut syndrome (the licence record has no approved indication text) |
| Predicted New Indication | Trigeminal nerve neoplasm (rank 1); trigeminal neuralgia (rank 2) is the best-supported candidate |
| TxGNN Prediction Score | 99.97% (trigeminal nerve neoplasm); 99.89% (trigeminal neuralgia) |
| Evidence Level | L5 for trigeminal nerve neoplasm; L2 for trigeminal neuralgia |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold for trigeminal nerve neoplasm; Proceed with Guardrails for trigeminal neuralgia as a research question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, lamotrigine blocks voltage-gated sodium channels and reduces glutamate release, which calms abnormal, hyperexcitable nerve firing in epilepsy.

**Trigeminal nerve neoplasm:** This prediction is probably an artefact. The two linked publications are about trigeminal neuralgia (a general treatment review and a Gamma Knife case report), not tumour treatment. There is no evidence of anti-tumour activity. The score likely reflects closeness to trigeminal neuralgia in the knowledge graph.

**Trigeminal neuralgia:** The case is plausible. The condition involves ectopic, paroxysmal nerve discharges, and the first-line drugs (carbamazepine, oxcarbazepine) work through the same sodium-channel mechanism. Guidelines and reviews list lamotrigine as an add-on or second-line option.

**Other predicted indications:** Several lower-ranked predictions are rare reflex seizure types (micturition-, startle-, audiogenic-, thinking-, orgasm-, eating- and reading-induced seizures). They are mechanistically close to lamotrigine's original use. Evidence for them is indirect, apart from startle-induced seizures, which have small clinical case series (see below).

---

## Clinical Trial Evidence

Trials for trigeminal neuralgia (rank 2). No clinical trials were found for the other predicted indications.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00913107](https://clinicaltrials.gov/study/NCT00913107) | Phase 2/3 | Completed | 21 | Lamotrigine vs carbamazepine (standard of care) in trigeminal neuralgia; efficacy and safety comparison. Results not summarised in the data compiled. |
| [NCT00203229](https://clinicaltrials.gov/study/NCT00203229) | Not specified | Completed | 20 | Double-blind, placebo-controlled add-on study of lamotrigine in trigeminal neuralgia; looked at side effects and reduction of attacks. Results not summarised in the data compiled. |

---

## Literature Evidence

Trigeminal neuralgia (rank 2), highest-priority items:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [37892981](https://pubmed.ncbi.nlm.nih.gov/37892981/) | 2023 | Systematic review | Biomedicines | Umbrella review of drug therapies for trigeminal neuralgia, covering efficacy and side effects |
| [30860637](https://pubmed.ncbi.nlm.nih.gov/30860637/) | 2019 | Guideline | Eur J Neurol | European Academy of Neurology recommendations for managing trigeminal neuralgia |
| [34108244](https://pubmed.ncbi.nlm.nih.gov/34108244/) | 2021 | Review | Pract Neurol | Practical guide to diagnosis and medical/surgical treatment |
| [31908187](https://pubmed.ncbi.nlm.nih.gov/31908187/) | 2020 | Review | Mol Pain | Pathophysiology and pharmacological treatments |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Rev Neurother | Carbamazepine/oxcarbazepine remain effective but limited by side effects; newer anticonvulsants are possible alternatives |
| [38246671](https://pubmed.ncbi.nlm.nih.gov/38246671/) | 2024 | Review | No Shinkei Geka | Lamotrigine is used off-label in Japan and described as effective, though less so than carbamazepine |

Other indications (limited, mostly indirect):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10512780](https://pubmed.ncbi.nlm.nih.gov/10512780/) | 1999 | Case series | Seizure | Startle-induced seizures: add-on lamotrigine used in four consecutive patients |
| [21896426](https://pubmed.ncbi.nlm.nih.gov/21896426/) | 2011 | Case series | Epileptic Disord | Six patients on add-on lamotrigine; seizure control greatly improved in three |
| [26876275](https://pubmed.ncbi.nlm.nih.gov/26876275/) | 2017 | Preclinical (animal) | Epilepsy Behav | Lamotrigine tested in a genetic audiogenic seizure hamster model |
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Rev Neurother | Linked to trigeminal nerve neoplasm, but concerns trigeminal neuralgia treatment, not tumours |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0278 | Lamotrigine | Not recorded | Not recorded (status: cancelled) |

---

## Safety Considerations

- **Contraindications flagged in the knowledge graph (not label text):** anxiety disorder, neurotic disorder, dysthymic disorder, liver disease, gallbladder disease, thrombocytopenia, neutropenia, agranulocytosis, anaemia (including macrocytic and aplastic anaemia), pancytopenia, and non-infectious meningitis. These should be verified against the package insert.
- **Drug Interactions:** 100 interactions were found in total. Moderate-level ones include morphine (including liposomal), opium, dronabinol, nabilone, metoclopramide and orlistat. Metformin is minor. Many others are of unknown severity (e.g. omeprazole, pantoprazole, lansoprazole, doxycycline, vancomycin).

Package insert warnings and contraindications were not available. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold (trigeminal nerve neoplasm); Proceed with Guardrails (trigeminal neuralgia, as a research question)**

**Rationale:**
- The top-ranked prediction, trigeminal nerve neoplasm, has no supporting evidence, and the literature relates to neuralgia rather than tumours. It should not be pursued.
- For trigeminal neuralgia, there are two small completed trials (n=20 and n=21) and guideline/review support as an add-on or second-line agent. This is promising but not definitive. Startle-induced seizures have small case series. Other reflex seizure predictions have only indirect or animal evidence.
- Lamotrigine has no currently valid registration in the Philippines (its single registration is cancelled), which is a practical barrier.

**To proceed, the following is needed:**
- Published results of NCT00913107 and NCT00203229, to confirm efficacy
- A larger randomised trial in trigeminal neuralgia
- Package insert warnings and contraindications, and a mechanism of action record
- Clarification of the regulatory route, given the cancelled registration
- A review of the knowledge-graph contraindications (blood disorders, liver disease) and the interaction profile before any use in a new population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

