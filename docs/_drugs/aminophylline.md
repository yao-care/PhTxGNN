---
layout: default
title: Aminophylline
parent: Moderate Evidence (L3-L4)
nav_order: 23
evidence_level: L4
indication_count: 9
last_modified_at: 2026-11-12
description: "Aminophylline: predicted new indication Migraine disorder (evidence level L4). Approved use: Not available"
monitor_inn: "Aminophylline"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "atrophoderma vermiculata", "ulerythema ophryogenesis", "Prinzmetal angina", "pulmonary hypertension", "sciatic neuropathy", "hyperthyroidism", "kyphoscoliotic heart disease"]
---

# Aminophylline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **9** 
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

## Aminophylline: From an Unspecified Original Indication to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Aminophylline is a methylxanthine drug, and the data compiled for this report do not specify its original approved indication in the Philippines.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **no registered clinical trials** and only **4 publications** (one 2023 review, two case reports and one 1964 review), so this is an early-stage research hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the only Philippines license has no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L4 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled records. Based on known pharmacology, aminophylline is a non-selective adenosine receptor antagonist and phosphodiesterase (PDE) inhibitor. It is a methylxanthine, widely known for bronchodilation, and the original indication is not recorded in the data compiled for this report.

Adenosine signalling has been linked to activation of the trigeminovascular system and to pain modulation. A 2023 review proposes that migraine may involve impaired brain energy metabolism with high adenosine levels, and that adenosine antagonism by aminophylline may relieve pain, particularly post-dural headache. A case report of hemiplegic migraine triggered by regadenoson (an adenosine agonist) offers indirect support for adenosine involvement.

This remains a hypothesis. The supporting papers are a narrative review and case reports, with no controlled trials in migraine.

## Clinical Trial Evidence

Currently no related clinical trials registered for migraine disorder.

For reference, among the other predicted indications, only pulmonary hypertension has a registered trial: [NCT01530464](https://clinicaltrials.gov/study/NCT01530464) (Phase 1, completed, 18 healthy volunteers) tested the safety and pharmacokinetics of aminophylline combined with ambrisentan. It provides no efficacy data.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Review | Pain Management | Proposes that migraine involves high adenosine levels and impaired brain energy metabolism; suggests aminophylline, an adenosine antagonist, may relieve pain, especially post-dural headache |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Case report | Journal of Nuclear Cardiology | Hemiplegic migraine triggered by regadenoson (an adenosine agonist); indirectly supports adenosine involvement |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Case report | Canadian Journal of Cardiology | Syndrome X with excessive adenosine effect described as "myocardial migraine"; indirect relevance only |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Review | Aggiornamenti Clinicoterapeutici | Historical review of headaches; no abstract available |

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Aminophylline (theophylline ethylenediamine) | Injection |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction screen. The first 20 reviewed include one **Major** interaction, with **bupropion**. Most others are **Moderate**, including:
  - H2 blockers: famotidine, ranitidine, cimetidine, nizatidine
  - Corticosteroids: hydrocortisone, dexamethasone, betamethasone, triamcinolone, budesonide
  - Antibiotics: doxycycline, tetracycline, minocycline, clarithromycin
  - Bowel preparations: picosulfuric acid, polyethylene glycol with electrolytes, sodium sulfate
  - Others: obeticholic acid, metreleptin

  Lansoprazole is **Minor**.
- **Signals from other predicted indications**: A report in variant (Prinzmetal) angina found that aminophylline termination of dipyridamole stress triggered coronary vasospasm. Methylxanthines can also worsen tachycardia and tremor in thyrotoxicosis. These raise cardiovascular caution for any repurposing use.

Please refer to the package insert for warnings and contraindications, as none were available in the compiled data.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is very high, but the evidence is L4: a plausible adenosine-antagonism mechanism supported only by a narrative review and case reports, with no clinical trials.

<!-- review:begin ph-lic-20261031-aminophylline-1 -->

> **Review correction (2026-10-31)**: Originally stated: "The prediction score is very high, but the evidence is L4: a plausible adenosine-antagonism mechanism supported only by a narrative review and case reports, with no clinical trials. The only Philippines license is cancelled, so there is no currently marketed product, and no label safety data were available." Removed: it said the PNF entries were cancelled, discontinued, or not current, which did not match the PNF data (the Philippine National Formulary as of 2026-10-31). The PNF lists 1 entry for this drug, 1 current; the Quick Overview and the table under Philippines Market Information show the current figures. Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261031-aminophylline-1 -->

**To proceed, the following is needed:**
- Mechanism of action data confirmed from a source such as DrugBank
- Package insert warnings and contraindications from DOH-FDA Philippines
- Controlled clinical studies (at least Phase 2) of aminophylline in migraine or post-dural headache
- A cardiovascular safety assessment, given the vasospasm signal and the major interaction with bupropion
- A decision on the regulatory route

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-10-31 | Removed: "The only Philippines license is cancelled, so there is no currently marketed product, and no label safety data were available" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

