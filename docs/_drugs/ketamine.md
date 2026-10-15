---
layout: default
title: Ketamine
parent: Model Prediction Only (L5)
nav_order: 192
evidence_level: L5
indication_count: 1
---

# Ketamine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
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

# Ketamine: From an Unspecified Original Indication to Headache Disorder

## One-Sentence Summary

Ketamine is an NMDA receptor antagonist whose original approved indication is not recorded in the Philippine registration data compiled for this report.
The TxGNN model predicts it may be effective for **headache disorder**,
with **9 clinical trials** and **20 publications** currently supporting this direction, including 2 completed Phase 3/4 randomized trials in the emergency department.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the registration data |
| Predicted New Indication | Headache disorder |
| TxGNN Prediction Score | 99.33% |
| Evidence Level | L1 (see note below) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 |
| Recommended Decision | Hold |

*Note on the evidence level:* The L1 label comes from the data compiled for this report. Strictly, the completed Phase 3 trial (THINK, n=80) is the only one at that phase, and no outcome data were provided. Under the stated rules (≥2 completed Phase 3 RCTs), the level is arguably closer to L2 or lower. Treat L1 with caution.

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the compiled data. Based on general pharmacology, ketamine blocks NMDA-type glutamate receptors. Glutamate signaling and central sensitization contribute to migraine, cluster headache, and chronic headache pain, so NMDA blockade offers a plausible analgesic and anti-sensitization mechanism.

Ketamine also affects cortical spreading depression and pain-pathway modulation, including trigeminal nociceptive processing. This adds biological plausibility. The very high TxGNN score (0.993) fits this picture. The link rests on general pharmacology rather than a curated mechanism, and the original indication is unknown, so the relationship between old and new indications cannot be assessed.

"Headache disorder" is a broad category. It covers acute migraine in the emergency department, tension-type headache, cluster headache, and chronic or refractory headache. Evidence differs by subtype.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | THINK trial: intranasal sub-dissociative ketamine vs standard care for primary headache in the ED (single-blind, placebo-controlled). Outcome data not provided. |
| [NCT05306899](https://clinicaltrials.gov/study/NCT05306899) | Phase 3 | Recruiting | 56 | KetHead: multicenter placebo-controlled RCT of high-dose IV ketamine (1 mg/kg/h for 6 hours) in chronic daily headache. No results yet. |
| [NCT02657031](https://clinicaltrials.gov/study/NCT02657031) | Phase 4 | Completed | 54 | CHECK trial: low-dose ketamine vs prochlorperazine (Compazine) for headache in the ED. Small sample. |
| [NCT02697071](https://clinicaltrials.gov/study/NCT02697071) | Not specified | Completed | 34 | Randomized placebo-controlled trial of sub-dissociative ketamine for acute migraine in the ED. |
| [NCT04814381](https://clinicaltrials.gov/study/NCT04814381) | Phase 4 | Completed | 93 | Single ketamine infusion combined with magnesium sulfate in refractory chronic cluster headache. Combination design obscures ketamine's own effect. |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Ketamine vs ketorolac for acute tension-type headache in the ED. Status unknown. |
| [NCT04179266](https://clinicaltrials.gov/study/NCT04179266) | Phase 1/2 | Completed | 23 | Proof-of-concept of intranasal ketamine spray in chronic cluster headache. Exploratory. |
| [NCT04860713](https://clinicaltrials.gov/study/NCT04860713) | Phase 4 | Completed | 5 | Oral ketamine plus aspirin vs rimegepant in ED headache. Too small to inform efficacy. |
| [NCT02403687](https://clinicaltrials.gov/study/NCT02403687) | Not specified | Completed | 300 | PACE study: observational study of topical NSAIDs for pain. Relevance to ketamine in headache unclear. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | American Headache Society update on parenteral drug treatment of acute migraine in the ED. |
| [34919214](https://pubmed.ncbi.nlm.nih.gov/34919214/) | 2022 | Review | Drugs | Drug treatment of cluster headache, covering acute and preventive therapy. |
| [34806767](https://pubmed.ncbi.nlm.nih.gov/34806767/) | 2021 | Review | Headache | Second-line injectable options for ED migraine when first-line drugs fail. |
| [36310189](https://pubmed.ncbi.nlm.nih.gov/36310189/) | 2023 | Systematic review / meta-analysis | Journal of Neurology | Preventive treatments for refractory chronic cluster headache. |
| [35356451](https://pubmed.ncbi.nlm.nih.gov/35356451/) | 2022 | Retrospective cohort | Frontiers in Neurology | Efficacy, duration, and safety of IV lidocaine and ketamine infusions for inpatient headache disorders. |
| [33610431](https://pubmed.ncbi.nlm.nih.gov/33610431/) | 2021 | Systematic review | Neurophysiologie Clinique | Ketamine and cortical spreading depolarization, a mechanism linked to migraine aura. |
| [38870050](https://pubmed.ncbi.nlm.nih.gov/38870050/) | 2024 | Review | Expert Review of Neurotherapeutics | Ketamine mentioned as a possible adjuvant in trigeminal neuralgia. |
| [37806714](https://pubmed.ncbi.nlm.nih.gov/37806714/) | 2023 | Review | Progress in Brain Research | Bidirectional link between migraine and treatment-resistant depression. |
| [40062461](https://pubmed.ncbi.nlm.nih.gov/40062461/) | 2025 | Review | Current Opinion in Neurology | Persistent aura without infarction. |
| [35416105](https://pubmed.ncbi.nlm.nih.gov/35416105/) | 2022 | Review | Expert Opinion on Drug Safety | Long-term safety of ketamine and esketamine in depression (relevant to safety, not headache efficacy). |

Several other retrieved papers concern ketamine in depression or alcohol use disorder and do not address headache directly.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0271 | Ketamine | Not recorded | Not recorded (status: cancelled) |

## Safety Considerations

- **Contraindications suggested by the knowledge graph** (drug-disease links from a model knowledge graph, not from label text): hypertension and hypertensive disorders, stroke and cerebrovascular disorders, cerebral infarction, myocardial infarction, myocardial ischemia and coronary artery disease, coronary thrombosis, intracranial hypertension and pseudotumor cerebri, ocular hypertension, respiratory failure, hyperthyroidism (thyrotoxicosis, Graves disease), delirium, substance abuse/dependence, and hemoglobinopathy.
- **Drug Interactions**: The interaction query returned 100 entries. The main ones listed are:
  - Moderate: morphine (including liposomal), diphenoxylate, opium, dronabinol, nabilone, metoclopramide, sibutramine, phentermine, ephedrine, fenfluramine, isometheptene, topical epinephrine.
  - Unknown severity: atropine, amphotericin B, famotidine, omeprazole, potassium chloride, ondansetron, ursodeoxycholic acid.

Package insert warnings and contraindications were not available, so please refer to the package insert for label safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The biological rationale is plausible, and the ED trials directly test ketamine in headache. However, no efficacy results were provided, the trials are small, the only Phase 3 trial of note is complete without reported outcomes, and the other is still recruiting.
- The only Philippine registration is cancelled, with no recorded indication or dosage form. No label safety information is available, and the knowledge graph flags many cardiovascular and cerebrovascular contraindications, which matter for headache patients.

**To proceed, the following is needed:**
- Published results from THINK (NCT03081416), CHECK (NCT02657031), and the placebo-controlled migraine trial (NCT02697071), plus the KetHead outcomes when available.
- A clearer target headache subtype (acute ED migraine, cluster headache, or chronic daily headache).
- The Philippine package insert (warnings and contraindications) and a curated mechanism of action.
- Clarification of the regulatory pathway, since the only registration is cancelled, and a review of the controlled-substance status and available routes (IV, intranasal).
- A safety plan for patients with cardiovascular, cerebrovascular, or substance-use risk factors, and an interaction-management plan for opioids and sympathomimetics.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

