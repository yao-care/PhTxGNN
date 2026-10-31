---
layout: default
title: Methylergometrine
parent: Model Prediction Only (L5)
nav_order: 229
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-31
description: "Methylergometrine: predicted new indication hypertrichosis (disease) (evidence level L5). Approved use: Not available"
monitor_inn: "Methylergometrine"
predicted_indications: ["hypertrichosis (disease)", "pulmonary hypertension", "migraine disorder", "Ambras type hypertrichosis universalis congenita", "malformation syndrome with odontal and/or periodontal component", "syndrome with a Dandy-Walker malformation as major feature", "isolated genetic hair shaft abnormality", "kyphoscoliotic heart disease", "migraine with brainstem aura", "nephrogenic syndrome of inappropriate antidiuresis"]
---

# Methylergometrine
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

## Methylergometrine: From Uterotonic Use (Original Indication Not Recorded) to hypertrichosis (disease)
{: .text-alpha }

## One-Sentence Summary

Methylergometrine is an ergot-derived agent with uterotonic activity. Its original approved indication is not recorded in the local registration data compiled for this report.
The TxGNN model predicts it may be effective for **hypertrichosis**, but there are **0 clinical trials** and **0 publications** supporting this prediction.
Evidence is limited to a computational prediction, and the top-ranked prediction has no identified mechanistic rationale.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the only registration has no indication text) |
| Predicted New Indication | Hypertrichosis |
| TxGNN Prediction Score | 0.9987 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, methylergometrine is an ergot-derived serotonergic, adrenergic and dopaminergic agent with uterotonic activity.

No known pathway links it to hair growth regulation. The high TxGNN score reflects network-based proximity only, and no trials or literature support it. The prediction is therefore not mechanistically supported at this stage.

Other predictions for this drug point the same way:

- **Pulmonary hypertension (rank 2):** Ergot alkaloids act on 5-HT2B receptors, and this activity is associated with pulmonary arterial hypertension and valvulopathy. This suggests potential harm rather than benefit.
- **Migraine disorder (rank 3):** This is the only prediction with some indirect literature. The ergot class link is plausible, but there is no direct evidence for methylergometrine itself.
- **Other predictions (ranks 4-10):** These include rare genetic or malformation conditions and have no plausible mechanism or evidence.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

For hypertrichosis, there is currently no related literature available.

For reference, the following two publications were retrieved for the third-ranked prediction, migraine disorder. They are indirect and do not support the hypertrichosis prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18644039](https://pubmed.ncbi.nlm.nih.gov/18644039/) | 2008 | Review | Cephalalgia | History of methysergide (synthesized from lysergic acid) in migraine, linked to the serotonin and vasodilation theories of migraine |
| [9665056](https://pubmed.ncbi.nlm.nih.gov/9665056/) | 1998 | Review | Circulation | Compared coronary vasoconstrictor potential of antimigraine drugs, including methysergide and its metabolite methylergometrine, because ergotamine and sumatriptan can cause angina-like symptoms |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0319 | Methylergometrine | Not recorded | Not recorded (status: valid) |

---

## Safety Considerations

- **Contraindication signals from the knowledge graph** (drug-disease contraindication links, not package insert text): hypertension and hypertensive disorders, epilepsy, kidney disease, liver disease, gallbladder disease, pyoureter, stroke and cerebrovascular disorders, cerebral infarction, arteriosclerosis obliterans, and HELLP syndrome.
- **Drug Interactions:** 92 interactions were identified, and the 20 listed in the compiled data include these main ones:
  - **Major:** isometheptene, epinephrine (including ophthalmic and topical forms), ephedrine (including nasal), lorcaserin, clarithromycin
  - **Moderate:** doxycycline, tetracycline, minocycline, aprepitant, dexamethasone, cimetidine, clotrimazole, miconazole, eluxadoline, glycerol phenylbutyrate, metreleptin, troglitazone
- **Class-related concerns:** Ergot vasoconstriction and 5-HT2B agonism raise concerns about ischemia, valvulopathy and fibrosis. These are particularly relevant for the cardiac, pulmonary hypertension and migraine-with-brainstem-aura predictions.

Package insert warnings and contraindications were not available, so please refer to the package insert for full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a model score alone (Evidence Level L5), with no trials, no literature and no plausible mechanism for hypertrichosis.

**To proceed, the following is needed:**
- The mechanism of action data for methylergometrine, to test whether any link to the predicted disease exists
- The approved indication and package insert warnings and contraindications from the Philippines registration
- Preclinical or clinical evidence for the predicted indication; migraine is the only prediction with indirect supporting literature, but a safety review of its vasoconstrictive risk would come first
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

