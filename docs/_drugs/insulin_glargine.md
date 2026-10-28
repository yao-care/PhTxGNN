---
layout: default
title: Insulin Glargine
parent: Model Prediction Only (L5)
nav_order: 176
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Insulin Glargine: predicted new indication Autoimmune oophoritis (evidence level L5). Approved use: Type 2 diabetes mellitus, type 1 diabetes mellitus…"
monitor_inn: "Insulin glargine"
predicted_indications: ["autoimmune oophoritis", "thiamine-responsive dysfunction syndrome", "classic stiff person syndrome", "focal stiff limb syndrome", "opsismodysplasia", "pancreatic agenesis", "drug-induced localized lipodystrophy", "centrifugal lipodystrophy", "pressure-induced localized lipoatrophy", "idiopathic localized lipodystrophy"]
---

# Insulin Glargine
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

## Insulin Glargine: From Diabetes Mellitus to Autoimmune Oophoritis
{: .text-alpha }

## One-Sentence Summary

Insulin glargine is a long-acting basal insulin analog, originally used to treat type 1 and type 2 diabetes mellitus and diabetic ketoacidosis.
The TxGNN model predicts it may be effective for **autoimmune oophoritis**, but there are currently **0 clinical trials** and **0 publications** supporting this specific prediction.
The score comes from the model alone, so the evidence is very weak.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Type 2 diabetes mellitus, type 1 diabetes mellitus, diabetic ketoacidosis (approved indication text is not available for the Philippines registration) |
| Predicted New Indication | Autoimmune oophoritis |
| TxGNN Prediction Score | 0.9988 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, insulin glargine is a long-acting basal insulin analog whose efficacy in diabetes mellitus is well established.

For autoimmune oophoritis, there is no clear mechanistic link. This condition is an immune-mediated injury of the ovary, and insulin glargine has no known immunomodulatory action in this setting. The high score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, such as autoimmune polyglandular syndromes in which diabetes also occurs, not biological evidence.

The model's other top predictions show the same pattern. Most are linked to insulin only through comorbid diabetes or autoimmunity (thiamine-responsive dysfunction syndrome, stiff person syndrome, focal stiff limb syndrome). Others are linked through insulin-related signaling (opsismodysplasia). Several localized lipodystrophies are in fact known adverse effects of insulin injection, so they are safety concerns rather than repurposing opportunities. Pancreatic agenesis (rank 6) is mechanistically coherent, since it causes insulin-deficient diabetes. However, insulin replacement there is essentially the same as the existing diabetes use, not a new indication.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For autoimmune oophoritis, currently no related literature is available.

The only literature retrieved among the top predictions relates to pancreatic agenesis (rank 6) and is indirect. None of it addresses insulin glargine in that condition directly:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12150359](https://pubmed.ncbi.nlm.nih.gov/12150359/) | 2002 | Review | J Am Pharm Assoc | Review of insulin therapy use and initiation in type 2 diabetes |
| [19322513](https://pubmed.ncbi.nlm.nih.gov/19322513/) | 2009 | Review | Acta Diabetol | Secondary diabetes associated with endocrine diseases such as acromegaly and Cushing syndrome |
| [32871938](https://pubmed.ncbi.nlm.nih.gov/32871938/) | 2020 | Case report | Medicine | First reported MODY5 case treated with a GLP-1 receptor agonist |
| [25818213](https://pubmed.ncbi.nlm.nih.gov/25818213/) | 2015 | Veterinary cohort | J Vet Intern Med | Pancreatic enzymes and ultrasound findings in diabetic cats (non-human) |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0250 | Insulin Glargine | Not specified | Not specified (status: valid) |

The only registration is valid, so a valid registration currently exists in the Philippines.

## Safety Considerations

- **Drug Interactions**: The interaction query found 100 interacting drugs, mostly of moderate severity. Examples:
  - Other glucose-lowering drugs: metformin, pioglitazone, alogliptin, albiglutide
  - Beta-agonists and sympathomimetics: salbutamol, formoterol, epinephrine, phenylephrine, pseudoephedrine
  - Beta-blocker: acebutolol
  - Corticosteroids: hydrocortisone
  - Hormones: estradiol, ethinylestradiol
  - Others: acetazolamide, hydrochlorothiazide, doxycycline, alpelisib, ethanol
  - Topical corticosteroids such as hydrocortisone (topical) and alclometasone (topical) are minor.
- **Injection-site lipodystrophy**: Several predicted conditions (localized lipodystrophy and lipoatrophy) are known adverse effects of repeated insulin injection at the same site. Insulin glargine is more likely a cause than a treatment for these.

Please refer to the package insert for other warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for autoimmune oophoritis rests on a model score alone (L5), with no trials, no literature and no plausible mechanism. In the Philippines, the only registration is cancelled.

**To proceed, the following is needed:**
- Mechanistic evidence that insulin glargine affects autoimmune ovarian injury, and any clinical or preclinical data in this condition
- Detailed mechanism of action data (MOA)
- Package insert warnings and contraindications from the Philippines FDA
- Clarification of the cancelled registration status and a valid local authorization, if use is planned
- If a new indication is pursued, a better-supported prediction. Pancreatic agenesis is coherent but overlaps with the existing use. The lipodystrophy predictions should be treated as safety signals.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

