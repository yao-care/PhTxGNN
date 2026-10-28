---
layout: default
title: Valproic Acid
parent: Model Prediction Only (L5)
nav_order: 349
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
monitor_inn: "Valproic acid"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia"]
description: "Valproic Acid: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Valproic Acid
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

## Valproic Acid: Trigeminal nerve neoplasm
{: .text-alpha }

## One-Sentence Summary

Valproic acid is an established antiseizure medicine, originally used for epilepsy, manic bipolar affective disorder and absence epilepsy.
The TxGNN model's top-ranked prediction is **trigeminal nerve neoplasm**, but there are **0 clinical trials** and only **1 publication** (a case series on a different condition) behind it.
The more credible repurposing directions are in other seizure-related and neuralgic conditions, noted below.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9997 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 2 of 2) |
| Number of Registrations | 2 (valid: 2) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the compiled data. Based on general knowledge, valproic acid enhances GABA-mediated inhibition, blocks sodium channels and modulates T-type calcium channels. It also inhibits histone deacetylase (HDAC), which is a theoretical antineoplastic mechanism.

For the top-ranked prediction, **trigeminal nerve neoplasm**, no credible mechanistic link is established. The only retrieved paper is a 1997 case series on Sturge-Weber syndrome, which is a different condition. The high TxGNN score is not supported by clinical or preclinical evidence in the data compiled for this report.

Several lower-ranked predictions have more plausible links, because they are close to the original epilepsy indication:
- **Trigeminal neuralgia (rank 3, L4):** older reviews list valproate as a second-line or adjunct anticonvulsant, but the retrieved papers mostly concern carbamazepine.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for any of the ten predicted indications.

---

## Literature Evidence

Literature for the top prediction (trigeminal nerve neoplasm):

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales espanoles de pediatria | Review of 14 Sturge-Weber syndrome cases. This is not a trigeminal nerve neoplasm, so it gives no direct support |

Selected literature for the better-supported alternative predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [20200383](https://pubmed.ncbi.nlm.nih.gov/20200383/) | 2010 | RCT | N Engl J Med | Ethosuximide, valproic acid and lamotrigine compared in childhood absence epilepsy. High quality, but a different syndrome from the predicted ones |
| [30592252](https://pubmed.ncbi.nlm.nih.gov/30592252/) | 2019 | Review | Curr Neuropharmacol | Molecular mechanisms and clinical evidence of valproic acid in epilepsy |
| [29262725](https://pubmed.ncbi.nlm.nih.gov/29262725/) | 2018 | Clinical study | Clin EEG Neurosci | Analysis of whether valproate suppresses the auditory startle reflex in epilepsy patients (startle epilepsy) |
| [6465864](https://pubmed.ncbi.nlm.nih.gov/6465864/) | 1984 | Clinical study | Ann Neurol | Clinical study of 14 startle epilepsy patients; the favorable responses reported in the excerpt were to carbamazepine |
| [2496695](https://pubmed.ncbi.nlm.nih.gov/2496695/) | 1989 | Case report | Pediatr Neurol | Adolescent-onset hyperekplexia that resolved completely with valproic acid |
| [1774173](https://pubmed.ncbi.nlm.nih.gov/1774173/) | 1991 | Review | Headache | Medical management of trigeminal neuralgia; valproic acid is listed among the anticonvulsants reported as efficacious |
| [15246950](https://pubmed.ncbi.nlm.nih.gov/15246950/) | 2004 | Review | Epileptic Disord | Antiepileptic drugs used outside epilepsy; evidence mainly from case series and small trials |
| [33551767](https://pubmed.ncbi.nlm.nih.gov/33551767/) | 2020 | Preclinical | Front Behav Neurosci | Cannabidiol and valproate in the GASH/Sal audiogenic seizure model |
| [38117708](https://pubmed.ncbi.nlm.nih.gov/38117708/) | 2023 | Review | Medicina | Reflex triggers in juvenile myoclonic epilepsy |
| [39786974](https://pubmed.ncbi.nlm.nih.gov/39786974/) | 2025 | Cohort | Future Oncol | Levetiracetam and valproic acid in glioma: antiseizure and potential antineoplastic effects |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0454 | Sodium Valproate | Not recorded | Not recorded (status: valid) |
| PNF-0506 | Valproic Acid | Not recorded | Not recorded (status: valid) |


---

## Safety Considerations

**Contraindications flagged in the knowledge graph** (these come from drug-disease relationship data, not from label text):
- Liver disease, pancreatitis, kidney disease, gallbladder disease
- Thrombocytopenia and other haematologic disease
- Urea cycle disorders: carbamoyl phosphate synthetase I deficiency, citrullinemia, hyperargininemia
- Porphyrias: inherited porphyria, porphyrin metabolism disease, porphyria
- Cognitive disorder, anxiety disorder, neurotic disorder, dysthymic disorder, pyoureter

**Drug Interactions** (100 interactions were found; the first 20 returned are listed):
- **Major:** glycerol phenylbutyrate
- **Moderate:** bupropion, morphine (including liposomal), acetylsalicylic acid, clarithromycin, difenoxin, diphenoxylate, activated charcoal, dronabinol, metoclopramide, nabilone
- **Minor:** cimetidine, esomeprazole, and antacids (magnesium oxide, aluminum hydroxide, calcium carbonate, magaldrate, magnesium carbonate, magnesium hydroxide)

Literature in the compiled data also points to other well-known concerns: teratogenicity in females of reproductive age, hepatotoxicity, hyperammonemic encephalopathy, and an interaction with carbapenem antibiotics. Please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The top-ranked prediction (trigeminal nerve neoplasm) has no clinical trials and no relevant literature, so it sits at L5 (model prediction only). None of the ten predicted indications has a registered trial, and the best-supported one, startle epilepsy (L3), rests on small observational studies and case reports.
- Valproic acid is marketed in the Philippines (2 of 2 licences valid), and the package insert safety data could not be obtained.

**To proceed, the following is needed:**
- Review of the package insert, as safety screening cannot proceed without warnings and contraindications
- Mechanism of action data from DrugBank
- For startle epilepsy, trigeminal neuralgia and reading seizures, a focused literature review or small controlled study, since these have the most plausible links to existing evidence
- For the trigeminal nerve neoplasm prediction, preclinical evidence (for example HDAC-inhibitor activity in relevant tumour models) before any further investment
- A pregnancy-prevention and liver-monitoring plan, given the known risks in women of reproductive age
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

