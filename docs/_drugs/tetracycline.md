---
layout: default
title: Tetracycline
parent: Moderate Evidence (L3-L4)
nav_order: 333
evidence_level: L4
indication_count: 4
last_modified_at: 2026-10-15
description: "Tetracycline: predicted new indication Punctate epithelial keratoconjunctivitis (evidence level L4). Approved use: Not stated in the Philippines registration record. The knowledge grap…"
monitor_inn: "Tetracycline"
predicted_indications: ["punctate epithelial keratoconjunctivitis", "chronic ethmoidal sinusitis", "chronic rhinosinusitis", "paranasal sinus neoplasm (disease)"]
---

# Tetracycline
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **4** 
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

## Tetracycline: From Bacterial Infections (e.g., Urinary Tract Infection, Acne) to Punctate Epithelial Keratoconjunctivitis
{: .text-alpha }

## One-Sentence Summary

Tetracycline is an antibiotic originally used for a broad range of bacterial infections, including urinary tract infection, bronchitis, acne, pneumonia and gonorrhea.
The TxGNN model predicts it may be effective for **punctate epithelial keratoconjunctivitis**,
but there are **no registered clinical trials** and only **1 publication** (a case report) supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Philippines registration record. The knowledge graph lists urinary tract infection, bronchitis, acne, anthrax, gonorrhea, pharyngitis and pneumonia, among others |
| Predicted New Indication | Punctate epithelial keratoconjunctivitis |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L4 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Based on known information, tetracycline is a broad-spectrum antibiotic whose efficacy in bacterial infections, including chlamydial eye infection (trachoma and inclusion conjunctivitis), is established. Mechanistically it may be applicable to the predicted indication.

Persistent punctate keratitis can follow chlamydial follicular conjunctivitis, so the predicted indication is closely tied to an infection that tetracycline already treats. Tetracyclines are also known to have anti-inflammatory and matrix metalloproteinase (MMP)-inhibiting properties, which gives a plausible second link.

This is largely an extension of existing ocular infection use rather than a distinct repurposing signal. The high TxGNN score rests on one indirect literature item and no trials.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case report/Case series | Cornea | Two patients with chlamydial follicular conjunctivitis were treated with oral tetracycline or doxycycline, and the follicles resolved. Both later developed recurrent bilateral punctate epithelial keratitis, so the keratitis persisted despite the antibiotic treatment. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0483 | Tetracycline | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Drug Interactions**: 100 interactions are recorded in total. Examples of the Major-level ones:
  - Isotretinoin
  - Acitretin
  - Aminolevulinic acid

  Moderate-level examples include ethinylestradiol, amoxicillin, ampicillin, aminophylline, aluminum hydroxide and bismuth subcitrate potassium.
- **Conditions flagged in the knowledge graph (not label text)**: The drug-disease contraindication links include liver failure, liver disease, kidney disease, kidney failure, uremia, epilepsy, diabetes, neutropenia, agranulocytosis, G6PD deficiency, blood coagulation disease and Clostridium difficile colitis. These are model-derived associations and need confirmation against an official label.

Please refer to the package insert for further safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction score is high, but the evidence is a single case report with no trials, and it mainly reflects tetracycline's existing use in chlamydial eye infection. The only Philippines registration is cancelled, which limits practical development.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines (currently missing and blocking safety screening)
- Mechanism of action data (for example, from DrugBank)
- Controlled clinical data on tetracycline for punctate epithelial keratoconjunctivitis
- A review of the Major drug interactions and the knowledge-graph contraindication signals
- Confirmation of whether any valid Philippines registration or ophthalmic formulation exists

## Other Predicted Indications (For Reference)

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Evidence Summary | Recommendation |
|------|------|------|------|------|------|
| 2 | Chronic ethmoidal sinusitis | 99.15% | L4 | One in vitro antibiotic susceptibility survey; no clinical efficacy data | Hold |
| 3 | Chronic rhinosinusitis | 99.15% | L4 | Mostly class-level evidence (doxycycline systematic review and meta-analysis, Cochrane review of antibiotics with low-certainty evidence, an omadacycline case series); no tetracycline-specific trials | Research Question |
| 4 | Paranasal sinus neoplasm | 99.10% | L5 | No trials or literature; computational prediction only | Hold |
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

