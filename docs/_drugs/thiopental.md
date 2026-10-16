---
layout: default
title: Thiopental
parent: Model Prediction Only (L5)
nav_order: 336
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Thiopental: predicted new indication Trichotillomania (evidence level L5). Approved use: Epilepsy, pseudotumor cerebri, intracranial hypertension"
---

# Thiopental
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

# Thiopental: From Epilepsy and Intracranial Hypertension to Trichotillomania

## One-Sentence Summary

Thiopental is a barbiturate, originally associated with epilepsy, pseudotumor cerebri and intracranial hypertension.
The TxGNN model predicts it may be effective for **trichotillomania**, but there are **0 clinical trials** and **0 publications** supporting this prediction, so it rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Epilepsy, pseudotumor cerebri, intracranial hypertension (from the knowledge graph; no approved indication text is available for the local registration) |
| Predicted New Indication | Trichotillomania |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Thiopental is a barbiturate, a class known to enhance GABA-A receptor signaling, and it is linked to epilepsy and raised intracranial pressure in the knowledge graph.

The link to trichotillomania, a compulsive hair-pulling disorder, is speculative. One could argue that GABAergic modulation might dampen compulsive or impulsive circuitry, but no trial or publication supports this for thiopental. The prediction score is very high (rank 627 among model outputs), but a high score alone does not establish a plausible therapeutic effect. The drug's registration in the Philippines has also been cancelled.

### Other Predicted Indications (for reference)

Other high-scoring predictions were also reviewed. None has trial evidence.

| Rank | Predicted Indication | Score | Evidence Level | Comment |
|---|---|---|---|---|
| 2 | Frontal lobe epilepsy | 99.95% | L4 | Only indirect literature (thiopental test in epilepsy surgery work-up, case reports where steroids or surgery, not thiopental, were the successful treatments) |
| 3 | Prinzmetal angina | 99.94% | L5 | No evidence; cardiovascular depressant effects argue against benefit |
| 4 | Migraine disorder | 99.94% | L5 | The only paper retrieved concerns a plant extract, not thiopental |
| 5 | Absence epilepsy | 99.91% | L4 | Literature is mostly about status epilepticus; barbiturate anesthetics are not standard care for absence seizures |
| 6 | Tourette syndrome | 99.90% | L5 | No evidence |
| 7 | Migraine with brainstem aura | 99.90% | L5 | The only paper concerns metoprolol, not thiopental |
| 8 | Bundle branch block (obsolete term) | 99.90% | L5 | Likely an ontology mapping issue |
| 9 | Substance abuse/dependence | 99.89% | L4 | Papers describe barbiturate dependence and misuse, which is a safety signal rather than a therapeutic one |
| 10 | Nephrogenic syndrome of inappropriate antidiuresis | 99.85% | L5 | No plausible mechanism |

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

Currently no related literature available for trichotillomania.

For reference, the most relevant literature for the second-ranked prediction, frontal lobe epilepsy, is indirect:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8223422](https://pubmed.ncbi.nlm.nih.gov/8223422/) | 1993 | Cohort | Epilepsy Res | Thiopental test in 103 epilepsy surgery candidates, using EEG changes to localize focal dysfunction (a diagnostic use, not a treatment) |
| [18759609](https://pubmed.ncbi.nlm.nih.gov/18759609/) | 2009 | Cohort | J Neurosurg | EEG seizure activity in head-injury patients treated with an ICP-targeted protocol |
| [9805996](https://pubmed.ncbi.nlm.nih.gov/9805996/) | 1998 | Case report | Rinsho Shinkeigaku | Severe frontal-origin status epilepticus treated with corticosteroids |
| [12446223](https://pubmed.ncbi.nlm.nih.gov/12446223/) | 2002 | Case report | Epileptic Disord | Epilepsy surgery for status epilepticus caused by cortical dysplasia in an infant |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0486 | Thiopental | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Contraindications (from knowledge graph associations, not label text)**: Disease associations flagged in the knowledge graph include:
  - Kidney and liver disease, kidney failure, uremia, gallbladder disease
  - Asthma (including intrinsic and allergic asthma)
  - Hypotensive disorder
  - Anemia
  - Adrenal insufficiency (Addison disease, congenital adrenal hyperplasia and related disorders)
  - Myasthenia gravis and neuromuscular junction disease
  - Variegate porphyria and acute intermittent porphyria
  - Hypothyroidism and myxedema
- **Drug Interactions**: 45 interactions were identified in total. Major interactions include **ethanol** and **warfarin**. Moderate interactions include morphine, codeine, hydrocodone, dextromethorphan, dronabinol, nabilone, cetirizine, doxycycline, methylene blue, nitisinone, and radioactive iodide (I-123 and I-131). Minor interactions include cimetidine, promethazine, pyridoxine, and sulfasalazine.
- **Misuse potential**: The literature describes barbiturate tolerance, physical dependence, and overdose risk.

Please refer to the package insert for full warnings and contraindications, as label-based safety data were not available.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for trichotillomania is based only on a model score, with no clinical trials or publications (Evidence Level L5). The mechanism is speculative, safety data from the label are missing, and the Philippines registration is cancelled. Thiopental is also an injectable anesthetic-class barbiturate with significant safety constraints, which makes it a poor fit for a chronic behavioral disorder.

**To proceed, the following is needed:**
- Mechanism of action data to assess whether any link to trichotillomania is credible
- Package insert warnings and contraindications from the DOH-FDA Philippines
- Any preclinical or clinical evidence for thiopental in trichotillomania
- Review of whether a barbiturate anesthetic is a practical candidate for this condition, including route of administration, dosing, and risk-benefit
- Clarification of the cancelled registration status and whether any product is available locally
- Consideration of better-supported alternatives, such as the epilepsy-related predictions, which already have indirect literature
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

