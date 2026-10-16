---
layout: default
title: Sulfacetamide
parent: Model Prediction Only (L5)
nav_order: 321
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sulfacetamide: predicted new indication Postinfectious vasculitis (evidence level L5). Approved use: Acne, seborrheic dermatitis, conjunctivitis, uveitis…"
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

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Sulfacetamide: From Bacterial and Inflammatory Skin/Eye Conditions to Postinfectious Vasculitis

## One-Sentence Summary

Sulfacetamide is a sulfonamide antibacterial, originally used for conditions such as acne, seborrheic dermatitis, conjunctivitis and uveitis.
The TxGNN model predicts it may be effective for **postinfectious vasculitis**, but there are currently **0 clinical trials** and **0 publications** supporting this prediction, so it is a model prediction only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Acne, seborrheic dermatitis, conjunctivitis, uveitis, amebiasis and others (from the knowledge graph; no approved indication text in the Philippines registration) |
| Predicted New Indication | Postinfectious vasculitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the data compiled for this report. Sulfacetamide is generally known as a bacteriostatic sulfonamide that inhibits bacterial dihydropteroate synthase, which explains its use in superficial bacterial infections of the skin and eye.

Postinfectious vasculitis, however, is an immune-mediated process that follows an infection rather than an active bacterial infection itself. Antibacterial activity therefore gives no clear mechanistic rationale. The prediction most likely reflects proximity in the knowledge graph to the drug's infection-related indications, not a demonstrated biological link.

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
| PNF-0464 | Sulfacetamide | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindications (knowledge graph associations, not package insert text):** The graph links sulfacetamide to a broad list of conditions, including:
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

