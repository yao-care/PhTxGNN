---
layout: default
title: Clonidine
parent: Model Prediction Only (L5)
nav_order: 82
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Clonidine: predicted new indication Faciodigitogenital syndrome (evidence level L5). Approved use: Hypertension"
---

# Clonidine
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

# Clonidine: From Hypertension to Faciodigitogenital Syndrome

## One-Sentence Summary

Clonidine is originally used for hypertension, and also for open-angle glaucoma and ADHD according to the knowledge graph used by the model.
The TxGNN model predicts it may be effective for **faciodigitogenital syndrome**, a rare genetic developmental syndrome.
Currently **0 clinical trials** and **0 publications** support this specific prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Hypertension (the Philippines registration has no indication text, so this comes from the knowledge graph, which also lists open-angle glaucoma and ADHD) |
| Predicted New Indication | Faciodigitogenital syndrome |
| TxGNN Prediction Score | 99.999% (model rank 27) |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 currently valid) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the data compiled for this report. Based on known information, clonidine is an alpha-2 adrenergic agonist. It reduces noradrenergic and sympathetic activity, and its efficacy in hypertension and ADHD is established.

The predicted condition is a genetic developmental syndrome. No plausible mechanistic link between alpha-2 adrenergic agonism and this syndrome can be established from the available data. The very high score is therefore a model output that is not backed by any clinical or published evidence. It should be treated as a hypothesis only.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available.

## Philippines Market Information

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0110 | Clonidine (single-ingredient) | Cancelled |

No valid registration currently exists in the Philippines. Dosage form and approved indication are not recorded for this entry.

## Safety Considerations

No package insert warnings or contraindication text could be obtained for this report. Please refer to the package insert for authoritative safety information. The following comes from other sources.

- **Contraindications (knowledge graph, not label text)**: Drug-disease contraindication links in the knowledge graph include:
  - Cardiovascular: myocardial infarction, myocardial ischemia, sudden cardiac arrest, heart conduction disease, hypotensive disorder
  - Metabolic: type 1 and type 2 diabetes mellitus, diabetic ketoacidosis, gout, hypercalcemia, potassium deficiency
  - Organ and other conditions: liver failure, pancreatitis, respiratory failure, anuria, systemic lupus erythematosus, blood coagulation disease, dermatitis
  - Psychiatric: anxiety disorder, dysthymic disorder, neurotic disorder
  
  These links need verification against the official label.
- **Drug Interactions**: The interaction screen found 100 interacting drugs in total. The 20 listed in the data compiled for this report are all rated Moderate. The main groups are:
  - Corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone)
  - Antidiabetic agents (insulins, sulfonylureas such as glimepiride, glipizide and glyburide, and SGLT2 inhibitors such as canagliflozin, dapagliflozin and empagliflozin)
  - CNS-active drugs (morphine, bupropion, dronabinol)

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for faciodigitogenital syndrome has no trials, no literature, and no identifiable mechanistic rationale (L5). The Philippines registration is also cancelled. Pursuing it is not justified at this stage.

Among the other model predictions, **Tourette syndrome** (rank 5, score 99.98%) has by far the strongest support. It has two Phase 4 trials (NCT00370838 completed, n=12; NCT00152750 status unknown, n=32), European guideline recommendation, and a network meta-analysis. The data rate it L1 with "Proceed with Guardrails". The rating should be confirmed against the primary RCT data. If the goal is a practical repurposing candidate, evaluate this indication first. The data rate obesity disorder, migraine and manic bipolar disorder as L3 research questions.

**To proceed, the following is needed:**
- Mechanism of action data from DrugBank
- Package insert warnings and contraindications from DOH-FDA Philippines
- Any biological rationale linking alpha-2 agonism to faciodigitogenital syndrome, followed by a literature search for supporting preclinical or clinical data
- Clarification of the cancelled Philippines registration, and confirmation of available dosage forms if a new indication is pursued
- A re-ranking of the candidate indications, so that Tourette syndrome is evaluated as the primary candidate
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

