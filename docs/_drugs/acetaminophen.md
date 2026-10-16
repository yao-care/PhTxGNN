---
layout: default
title: Acetaminophen
parent: Model Prediction Only (L5)
nav_order: 12
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-15
description: "Acetaminophen: predicted new indication Migraine with brainstem aura (evidence level L5). Approved use: Migraine disorder, headache disorder, common cold, allergic rhinitis"
monitor_inn: "Acetaminophen"
predicted_indications: ["migraine with brainstem aura"]
---

# Acetaminophen
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Acetaminophen: From Migraine and Headache Disorders to Migraine with Brainstem Aura

## One-Sentence Summary

Acetaminophen (paracetamol) is a widely used analgesic, originally used for headache disorders, migraine, and cold-related symptoms such as allergic rhinitis and common cold.
The TxGNN model predicts it may be effective for **migraine with brainstem aura**, a subtype of migraine.
Currently **0 clinical trials** and **20 publications** (mostly general migraine reviews, none specific to this subtype) are linked to this prediction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Migraine disorder, headache disorder, common cold, allergic rhinitis (from the knowledge graph; no approved indication text in the Philippines record) |
| Predicted New Indication | Migraine with brainstem aura |
| TxGNN Prediction Score | 99.15% |
| Evidence Level | L4 (no registered trials for this subtype; supported only by general migraine literature and mechanistic reasoning) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known information, acetaminophen's analgesic effect is thought to involve central COX inhibition and modulation of serotonergic descending pain pathways. This could plausibly relieve headache pain in any migraine subtype.

Acetaminophen is already used for acute migraine, and migraine with brainstem aura is a clinical subtype of migraine. The very high TxGNN score (0.99) most likely reflects this close relationship between the diseases rather than a distinct mechanism. In other words, this is better read as an extension within the same disease family than as a true new-disease discovery.

No evidence in the compiled data addresses the brainstem aura subtype specifically. The prediction should therefore be treated as a research question, not a confirmed opportunity.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The publications below concern migraine in general. None studies migraine with brainstem aura specifically.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review (guideline-type evidence assessment) | Headache | American Headache Society update of the evidence for acute migraine drug therapies |
| [10321417](https://pubmed.ncbi.nlm.nih.gov/10321417/) | 1999 | Randomized placebo-controlled studies (pooled) | Clinical Therapeutics | Acetaminophen + aspirin + caffeine combination for menstruation-associated migraine, from 3 double-masked trials |
| [11318886](https://pubmed.ncbi.nlm.nih.gov/11318886/) | 2001 | Comparative study | Headache | Isometheptene/dichloralphenazone/acetaminophen combination compared with sumatriptan in mild-to-moderate migraine |
| [38307660](https://pubmed.ncbi.nlm.nih.gov/38307660/) | 2024 | Review | Handbook of Clinical Neurology | Status migrainosus, a complication of migraine with or without aura |
| [30470274](https://pubmed.ncbi.nlm.nih.gov/30470274/) | 2019 | Review | Neurologic Clinics | Headache in pregnancy; acetaminophen described as first-line symptomatic treatment |
| [33525313](https://pubmed.ncbi.nlm.nih.gov/33525313/) | 2021 | Review | Neurology International | Ubrogepant for acute migraine; acetaminophen noted among options for mild-to-moderate attacks |
| [23203776](https://pubmed.ncbi.nlm.nih.gov/23203776/) | 2013 | Review | Current Treatment Options in Neurology | Diagnosis and treatment of familial and sporadic hemiplegic migraine (a rare aura subtype) |
| [16018227](https://pubmed.ncbi.nlm.nih.gov/16018227/) | 2005 | Review | Pediatric Annals | Treatment of pediatric migraine |
| [39493026](https://pubmed.ncbi.nlm.nih.gov/39493026/) | 2024 | Review | Cureus | Abortive and prophylactic migraine therapies in pregnancy |
| [37123778](https://pubmed.ncbi.nlm.nih.gov/37123778/) | 2023 | Review | Cureus | Migraine treatment approach in pregnancy and breastfeeding |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0375 | Paracetamol | Not stated | Not stated (status: cancelled) |

---

## Safety Considerations

- **Contraindications (knowledge-graph associations, not label text)**: The TxGNN knowledge graph links acetaminophen with contraindications in liver failure, liver disease, cirrhosis of the liver, hepatic encephalopathy, hepatic coma, and gallbladder disease.
- **Drug Interactions**: 100 interactions were found in total. The 20 shown in the data are mostly Minor. Moderate-level interactions are with:
  - Activated charcoal
  - Glycerol phenylbutyrate
  - Naltrexone

  Minor-level interactions include anticholinergic agents (atropine, scopolamine, hyoscyamine, dicyclomine, glycopyrronium), H2 blockers (cimetidine, ranitidine), metoclopramide, and liraglutide. Vitamin A and calcitriol are listed with an unknown level.

Please refer to the package insert for full warnings and precautions.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The new indication is a subtype of a condition acetaminophen is already used for, and no trials or subtype-specific studies support it. The high model score mainly reflects disease-family similarity.
- The only Philippines registration is cancelled, so there is no currently valid local product to build on.

**To proceed, the following is needed:**
- Subtype-specific evidence (clinical trials or case series) in migraine with brainstem aura
- Detailed mechanism of action data
- Package insert warnings and contraindications from the Philippines FDA, to enable safety screening
- Confirmation of whether a valid acetaminophen/paracetamol product is currently registered in the Philippines
- Hepatic safety review in light of the liver-related contraindication associations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

