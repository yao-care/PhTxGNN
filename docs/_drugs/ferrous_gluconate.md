---
layout: default
title: Ferrous Gluconate
parent: Model Prediction Only (L5)
nav_order: 141
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-28
description: "Ferrous Gluconate: predicted new indication Plummer-Vinson syndrome (evidence level L4). Approved use: Iron deficiency anemia (also anemia of prematurity, hypochromic…"
monitor_inn: "Ferrous gluconate"
predicted_indications: ["Plummer-Vinson syndrome", "vitamin B12- and folate-independent constitutional megaloblastic anemia", "non-syndromic esophageal malformation", "biotin metabolic disease", "vitamin deficiency disorder"]
---

# Ferrous Gluconate
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Ferrous Gluconate: From Iron Deficiency Anemia to Plummer-Vinson Syndrome
{: .text-alpha }

## One-Sentence Summary

Ferrous gluconate is an iron supplement originally used to treat iron deficiency anemia and related anemias.
The TxGNN model predicts it may be effective for **Plummer-Vinson syndrome**, but there are currently **no clinical trials and no publications** supporting this specific prediction.
The prediction largely reflects an extension of the existing anemia indication rather than a truly new use.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Iron deficiency anemia (also anemia of prematurity, hypochromic, deficiency and microcytic anemia) |
| Predicted New Indication | Plummer-Vinson syndrome |
| TxGNN Prediction Score | 0.9994 |
| Evidence Level | L5 |
| Philippines Market Status | Marketed (valid licenses: 1 of 1) |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not currently available. Based on known information, ferrous gluconate is an oral iron salt that replenishes body iron stores. Its efficacy in iron deficiency anemia is well established, and mechanistically it may be applicable to Plummer-Vinson syndrome.

Plummer-Vinson syndrome (sideropenic dysphagia) is characterized by iron deficiency anemia, esophageal webs and difficulty swallowing. Iron repletion is the established standard treatment and can resolve both the anemia and the dysphagia. The drug's original indication therefore overlaps directly with the core pathophysiology of this syndrome, so the high TxGNN score likely reflects this shared mechanism rather than a new therapeutic use.

Support is indirect (mechanistic and guideline-based) only, since no trials or literature were compiled for this report.

### Other Predictions Reviewed

| Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|
| Vitamin B12- and folate-independent constitutional megaloblastic anemia | 0.9994 | L5 | Pathway unclear; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Hold |
| Non-syndromic esophageal malformation | 0.9967 | L5 | Structural defect iron would not be expected to correct; likely linked via esophageal webs. Hold |
| Biotin metabolic disease | 0.9942 | L5 | No plausible mechanism; the score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence. Hold |
| Vitamin deficiency disorder | 0.9917 | L5 | One small pilot trial (iron and FGF23 in hypophosphatemic rickets); hypothesis-generating only |

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Plummer-Vinson syndrome.

For the lower-ranked prediction "vitamin deficiency disorder", one trial was found:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02233322](https://clinicaltrials.gov/study/NCT02233322) | Not applicable | Completed | 8 | Pilot study of iron therapy in autosomal dominant hypophosphatemic rickets, testing whether iron lowers elevated FGF23 and corrects low phosphate. Small and indirect evidence only. |

---

## Safety Considerations

- **Disease contraindications (from the knowledge graph, not label text)**: peptic ulcer disease, hereditary hemochromatosis, hemosiderosis, iron metabolism disease, Wilson disease, ulcerative colitis, inflammatory bowel disease, hemolytic anemia, gastroenteritis.
- **Drug Interactions**: 80 interactions were identified. Most are Moderate, with some Minor. Main ones include:
  - Proton pump inhibitors (omeprazole, esomeprazole, lansoprazole, dexlansoprazole, pantoprazole, rabeprazole), which may reduce iron absorption
  - Antacids and minerals (calcium carbonate, magnesium oxide, aluminum hydroxide, magaldrate)
  - Tetracyclines (doxycycline, tetracycline, minocycline) and levofloxacin
  - Pancrelipase, sodium sulfate and triethylenetetramine
  - Minor: cimetidine, zinc sulfate and zinc acetate

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The leading prediction (Plummer-Vinson syndrome) is biologically sound but is essentially covered by the existing iron deficiency anemia use, with no trials or literature to support it as a distinct repurposing opportunity. The only registered Philippines license is cancelled, and label safety data is unavailable.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines
- Detailed mechanism of action data
- Literature review of iron therapy in Plummer-Vinson syndrome (case series and guidelines)
- Clarification of the current Philippines market status and whether a valid product is available
- Review of the knowledge-graph contraindications (e.g., inflammatory bowel disease, hemochromatosis) for the target population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

