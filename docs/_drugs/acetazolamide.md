---
layout: default
title: Acetazolamide
parent: Model Prediction Only (L5)
nav_order: 13
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Acetazolamide: predicted new indication Exercise-induced malignant hyperthermia (evidence level L5). Approved use: Absence epilepsy, congestive heart failure, open-angle glaucoma…"
monitor_inn: "Acetazolamide"
predicted_indications: ["exercise-induced malignant hyperthermia", "hypertrophic cardiomyopathy", "congenital myopathy with excess of thin filaments", "hypertrophic cardiomyopathy due to intensive athletic training", "distal myopathy, Tateyama type", "cirrhotic cardiomyopathy", "cardiomyopathy", "intestinal obstruction", "glycogen storage disease due to acid maltase deficiency, late-onset", "myopathic intestinal pseudoobstruction"]
---

# Acetazolamide
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

## Acetazolamide: From Absence Epilepsy, Glaucoma and Heart Failure to Exercise-Induced Malignant Hyperthermia
{: .text-alpha }

## One-Sentence Summary

Acetazolamide is a carbonic anhydrase inhibitor originally used for absence epilepsy, congestive heart failure, open-angle and angle-closure glaucoma, and altitude sickness.
The TxGNN model predicts it may be effective for **exercise-induced malignant hyperthermia**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction; the result is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Absence epilepsy, congestive heart failure, open-angle glaucoma, angle-closure glaucoma, altitude sickness (the Philippines registration record contains no indication text) |
| Predicted New Indication | Exercise-induced malignant hyperthermia |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, acetazolamide is a carbonic anhydrase inhibitor. It has established use in several conditions, including glaucoma, heart failure and altitude sickness, in which it alters fluid and acid-base balance.

Carbonic anhydrase inhibition could plausibly change acid-base balance and influence muscle excitation-contraction coupling. However, this link is speculative. Malignant hyperthermia is mainly a disorder of ryanodine receptor and calcium handling, and nothing in the data compiled for this report supports a direct mechanistic connection. The very high score (99.95%) reflects model similarity only and should not be read as evidence of efficacy.

Other top-ranked predictions are also unsupported and are not recommended for development. These include hypertrophic cardiomyopathy, cardiomyopathy, cirrhotic cardiomyopathy, intestinal obstruction and myopathic intestinal pseudoobstruction. For the intestinal conditions, the literature points to acetazolamide-induced ileus, which is the opposite of a therapeutic effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

No literature is available for exercise-induced malignant hyperthermia. The closest evidence relates to the second-ranked prediction, hypertrophic cardiomyopathy, and consists only of reviews and a case report. It is shown here for context and does not address the top prediction.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [38806171](https://pubmed.ncbi.nlm.nih.gov/38806171/) | 2025 | Review | ESC Heart Failure | Update on heart failure management; does not address acetazolamide in hypertrophic cardiomyopathy |
| [37169875](https://pubmed.ncbi.nlm.nih.gov/37169875/) | 2023 | Review | Eur Heart J Cardiovasc Pharmacother | Review of new cardiovascular drugs in 2022, including mavacamten for obstructive hypertrophic cardiomyopathy |
| [30279861](https://pubmed.ncbi.nlm.nih.gov/30279861/) | 2018 | Case report | J Cardiol Cases | Acetazolamide treated hypochloremia in an advanced heart failure patient who also had hypertrophic cardiomyopathy |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0002 | Acetazolamide | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindication-related conditions (from the TxGNN knowledge graph, not label text)**: liver failure and liver disease, kidney disease, hematologic disease, gallbladder disease, gout, type 1 and type 2 diabetes mellitus, diabetic ketoacidosis, respiratory failure, renal tubular acidosis, and adrenal insufficiency conditions (including Addison disease and congenital adrenal hyperplasia).
- **Drug Interactions**: 100 interactions were identified. Those listed in the compiled data include:
  - **Major**: acetylsalicylic acid, cisapride.
  - **Moderate**: antidiabetic agents (acarbose, acetohexamide, alogliptin, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, albiglutide), corticosteroids (beclomethasone, betamethasone, dexamethasone), amphotericin B formulations, and laxatives (bisacodyl, castor oil).
  - **Minor**: doxycycline.
- **Case-report safety signals**: acetazolamide-induced adynamic ileus, and non-cardiogenic pulmonary edema after intravenous use. In cirrhosis, there is a theoretical risk of hyperammonemia and encephalopathy. In hypertrophic cardiomyopathy, volume depletion may worsen outflow obstruction.

Please also refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top prediction has no clinical trials and no literature, so it rests on a model score alone (L5). The product also has no currently valid registration in the Philippines, and some lower-ranked predictions carry safety signals.

**To proceed, the following is needed:**
- Mechanism of action data for acetazolamide, and a plausible biological link to malignant hyperthermia
- Preclinical or mechanistic studies supporting the predicted indication
- Package insert warnings and contraindications from the Philippine regulator
- Clarification of the registration status, since the only licence is cancelled and has no dosage form or indication recorded
- A review of the interaction and contraindication profile for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

