---
layout: default
title: Codeine
parent: Model Prediction Only (L5)
nav_order: 86
evidence_level: L5
indication_count: 3
monitor_inn: "Codeine"
predicted_indications: ["nasal cavity disease", "trigeminal autonomic cephalalgia", "allergic urticaria"]
last_modified_at: 2026-10-27
description: "Codeine: predicted new indication nasal cavity disease (evidence level L5). Approved use: Not recorded in the local data"
---

# Codeine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **3** 
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

## Codeine: opioid analgesic and antitussive → nasal cavity disease
{: .text-alpha }

## One-Sentence Summary

Codeine is an opioid medicine (a prodrug converted to morphine in the body) that acts on mu-opioid receptors. The TxGNN model predicts it may be relevant to **nasal cavity disease**, with a score of 0.9993. No clinical trials were found, and the only publication is a single case report in which codeine appears as an incidental finding rather than a treatment. The prediction is therefore a model output without direct supporting studies.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | nasal cavity disease |
| TxGNN Prediction Score | 0.9993 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available for this report. Codeine is generally understood as an opioid analgesic and cough suppressant that works mainly through mu-opioid receptor activity after conversion to morphine.

The prediction score is very high, but it does not point to a convincing therapeutic mechanism. Opioid receptor activity and cough suppression offer no plausible disease-modifying role in conditions of the nasal cavity. The score most likely reflects the model's association with related upper-airway conditions rather than a distinct, new mechanism, so this should not be read as a true novel repurposing signal.

The only publication retrieved describes an unusual rhinolith (a nasal stone) that formed around an impacted foreign body, which turned out to be a hardened mixture of codeine and opium. This describes an incidental or adverse event, not a therapeutic effect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17315836](https://pubmed.ncbi.nlm.nih.gov/17315836/) | 2007 | Case report | Ear, Nose, & Throat Journal | A 21-year-old man had a rhinolith formed around a foreign body, which proved to be a hardened codeine and opium mixture; no therapeutic effect described |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0115 | Codeine | Not recorded | Not recorded |

## Safety Considerations

Please refer to the package insert for safety information. The following items come from the data compiled for this report:

- **Drug Interactions**: 100 interactions were found. Those listed include the following.
  - **Major**: alvimopan, bupropion.
  - **Moderate**: atropine, attapulgite, cimetidine, clidinium, dexamethasone, dexfenfluramine, dicyclomine, dolasetron, dronabinol, eliglustat, eluxadoline, fenfluramine, glycerol phenylbutyrate, glycopyrronium, granisetron, hyoscyamine, kaolin, loperamide.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
No clinical trial or study directly examines codeine as a treatment for nasal cavity disease. The single publication is a case report of an incidental finding, and no plausible therapeutic mechanism supports the prediction. The high score alone is not enough to justify further development.

**To proceed, the following is needed:**
- Detailed mechanism of action data.
- Package insert warnings and contraindications from the Philippine regulator.
- Any study showing a benefit of codeine in nasal cavity disease; without it, the prediction should remain at the model-only level.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

