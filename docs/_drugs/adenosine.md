---
layout: default
title: Adenosine
parent: Model Prediction Only (L5)
nav_order: 16
evidence_level: L5
indication_count: 1
monitor_inn: "Adenosine"
predicted_indications: ["obsolete bundle branch block"]
last_modified_at: 2026-10-27
description: "Adenosine: predicted new indication obsolete bundle branch block (evidence level L5). Approved use: Not recorded in the local data"
---

# Adenosine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

## Adenosine: A1 receptor agonist (antiarrhythmic) → obsolete bundle branch block
{: .text-alpha }

## One-Sentence Summary

Adenosine is an antiarrhythmic drug that acts on cardiac adenosine receptors.
The TxGNN model predicts it may be relevant to **obsolete bundle branch block**, but **no clinical trials and no publications** were found to support this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | obsolete bundle branch block |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, adenosine acts on A1 receptors in the atrioventricular (AV) node and slows conduction there.

This mechanism does not plausibly treat a bundle branch conduction defect. Adenosine is used diagnostically to unmask conduction abnormalities, and AV nodal blockade could worsen conduction disease. "Obsolete bundle branch block" is also a deprecated ontology term rather than a distinct clinical entity, so the high score (0.9994) is most likely an artifact of term mapping rather than a true therapeutic signal.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0006 | Adenosine | Not recorded | Not recorded |

This single-ingredient record is marked as cancelled in the licence data, although the overall market status is listed as marketed.

## Safety Considerations

- **Drug Interactions**: 100 interactions were found in total. Major-level interactions include:
  - Cisapride
  - Dolasetron
  - Papaverine

  Moderate-level interactions include famotidine, clarithromycin, granisetron, levofloxacin, ondansetron and palonosetron.

Please also refer to the package insert for warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a model score, with no trials or publications. The predicted condition is a deprecated term, and adenosine's AV-nodal slowing could worsen conduction disease.

**To proceed, the following is needed:**
- Confirmation of which current, clinically defined conduction disorder the predicted term maps to
- Mechanism of action data
- Package insert warnings and contraindications from DOH-FDA Philippines
- Any direct preclinical or clinical evidence in the predicted condition
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

