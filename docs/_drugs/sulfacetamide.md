---
layout: default
title: Sulfacetamide
parent: Model Prediction Only (L5)
nav_order: 321
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-30
monitor_inn: "Sulfacetamide"
predicted_indications: ["postinfectious vasculitis", "post-bacterial disorder", "otitis externa", "post-infectious syndrome", "infective urethral stricture", "Chagas cardiomyopathy", "infection-related hemolytic uremic syndrome", "punctate epithelial keratoconjunctivitis", "exposure keratitis", "parasitic eyelid infestation"]
description: "Sulfacetamide: predicted new indication Postinfectious vasculitis (evidence level L5). Approved use: Not recorded in the local data"
---

# Sulfacetamide
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

## Sulfacetamide: Postinfectious vasculitis
{: .text-alpha }

## One-Sentence Summary

Sulfacetamide is a sulfonamide antibacterial, originally used for conditions such as acne, seborrheic dermatitis, conjunctivitis and uveitis.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Sulfacetamide is generally known as a bacteriostatic sulfonamide that inhibits bacterial dihydropteroate synthase, which explains its use in superficial bacterial infections of the skin and eye.

Postinfectious vasculitis, however, is an immune-mediated process that follows an infection rather than an active bacterial infection itself. Antibacterial activity therefore gives no clear mechanistic rationale. The score comes from the TxGNN model (deep learning) and may reflect similarities the model learned between related diseases, not biological evidence.

Other lower-ranked predictions show the same pattern. Several are post-infectious or vague categories (post-bacterial disorder, post-infectious syndrome). Otitis externa and punctate epithelial keratoconjunctivitis are plausible by analogy to topical antibacterial use, but have no supporting evidence. For infection-related hemolytic uremic syndrome, antibiotics are generally not recommended, which is a potential concern rather than a rationale.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

For the top-ranked prediction (postinfectious vasculitis), currently no related literature is available.

For lower-ranked predictions, two papers were retrieved. Neither supports efficacy for the predicted indication:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3157322](https://pubmed.ncbi.nlm.nih.gov/3157322/) | 1985 | Case report (adverse event) | American Journal of Ophthalmology | An 8-year-old boy developed erythema multiforme major after topical sodium sulfacetamide for conjunctivitis. This is a safety signal, not evidence of benefit (linked to the exposure keratitis prediction). |
| [18561612](https://pubmed.ncbi.nlm.nih.gov/18561612/) | 2007 | Review/Observational | Annales Academiae Medicae Stetinensis | Describes Demodex as a cause of chronic marginal blepharitis. Sulfacetamide does not appear to have been evaluated (linked to the parasitic eyelid infestation prediction). |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0464 | Sulfacetamide | Not specified | Not specified (status: valid) |

## Safety Considerations

- **Contraindications (associations listed in the data source, not package insert text):** The data source lists sulfacetamide alongside a broad list of conditions, including:
  - Metabolic and blood disorders: G6PD deficiency, porphyria, hematologic disease, diabetes mellitus, diabetic ketoacidosis, hyperthyroidism
  - Organ disease: kidney disease, liver disease, gallbladder disease, heart disease, coronary artery disease, hypertension
  - Eye conditions: open-angle and angle-closure glaucoma, ocular hypertension, herpes simplex virus keratitis
  - Skin and other conditions: dermatitis, exanthem, benign prostatic hyperplasia
  
  These should be verified against an authoritative label.
- **Adverse event signal:** A published case report (PMID 3157322) describes erythema multiforme major after topical sulfacetamide use in a child.
- **Drug interactions:** No interaction records were found.

Please refer to the package insert for full warnings and precautions.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by the model score, with no clinical trials or literature, and no clear mechanistic link between an antibacterial sulfonamide and an immune-mediated condition. The Philippines registration is cancelled, and package insert safety information is unavailable.

**To proceed, the following is needed:**
- Mechanism of action data (for example from DrugBank) to assess any biological link to vasculitis
- Package insert warnings and contraindications from the DOH-FDA Philippines
- A literature and trial search specific to sulfacetamide and postinfectious vasculitis
- Clarification of the market status, since the only registration is cancelled, and of the available dosage forms and routes
- If any further work is pursued, a review of the more clinically plausible ocular and otic predictions (for example otitis externa, punctate epithelial keratoconjunctivitis), with attention to the erythema multiforme safety signal
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

