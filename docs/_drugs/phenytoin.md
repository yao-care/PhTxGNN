---
layout: default
title: Phenytoin
parent: Model Prediction Only (L5)
nav_order: 275
evidence_level: L5
indication_count: 3
last_modified_at: 2026-10-31
monitor_inn: "Phenytoin"
predicted_indications: ["trigeminal nerve neoplasm", "trigeminal neuralgia", "beta-ketothiolase deficiency"]
description: "Phenytoin: predicted new indication Trigeminal nerve neoplasm (evidence level L5). Approved use: Not recorded in the local data"
---

# Phenytoin
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

## Phenytoin: Trigeminal nerve neoplasm
{: .text-alpha }

## One-Sentence Summary

Phenytoin is an established antiseizure medicine, originally used for epilepsy and related seizure conditions.
The TxGNN model predicts it may be effective for **trigeminal nerve neoplasm**, but **no clinical trials** and **no neoplasm-specific publications** support this prediction. The two retrieved papers cover trigeminal neuralgia and Sturge-Weber syndrome, which are different conditions.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Trigeminal nerve neoplasm |
| TxGNN Prediction Score | 0.9999 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available for this drug. Phenytoin is generally known as a voltage-gated sodium channel blocker that suppresses repetitive, high-frequency neuronal firing, and its efficacy in epilepsy is well established.

The link to trigeminal nerve neoplasm is weak. A sodium channel blocker could plausibly relieve neuropathic pain or seizures associated with a tumour near the trigeminal nerve. There is no evidence that phenytoin has anti-tumour activity. The very high score is probably driven by network proximity to **trigeminal neuralgia**, a related nerve-pain condition for which phenytoin has historic use. Treat the prediction as a computational signal, not as support for treating the tumour itself.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17997704](https://pubmed.ncbi.nlm.nih.gov/17997704/) | 2007 | Review | Expert Review of Neurotherapeutics | Overview of medical and surgical treatments for trigeminal neuralgia. It concerns neuralgia, not neoplasm. |
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case series | Anales Españoles de Pediatría | Clinical course and treatment response in 14 children with Sturge-Weber syndrome. It does not address trigeminal nerve neoplasm. |

Neither paper provides direct evidence for phenytoin in trigeminal nerve neoplasm.

## Philippines Market Information

| Authorization Number | Product Name | Status |
|---------|------|------|
| PNF-0384 | Phenytoin | Valid |

This is the only registration, and it is a single-ingredient product. No dosage form or approved indication text is listed. This registration is currently valid (1 valid licence of 1).

## Safety Considerations

- **Contraindications flagged in the knowledge graph.** These come from drug-disease links, not from label text. Phenytoin is linked to contraindication or caution in:
  - Cardiac conditions: long QT syndrome, torsades de pointes, hypotensive disorder.
  - Liver and kidney disease: liver failure, liver disease, hepatic coma and encephalopathy, kidney disease, gallbladder disease.
  - Blood disorders: thrombocytopenia, neutropenia, agranulocytosis.
  - Metabolic conditions: diabetes mellitus, diabetic ketoacidosis, hyperglycemia, porphyria (including inherited porphyria).
  - Autoimmune and respiratory conditions: systemic lupus erythematosus (including the pediatric form), sleep apnea syndromes, congenital central hypoventilation syndrome.
  - Psychiatric conditions: anxiety and neurotic disorders, dysthymic disorder, substance abuse/dependence.
- **Drug interactions.** The interaction screen identified 100 interacting drugs. The 19 shown in the data compiled for this report are mostly moderate. They include acarbose, famotidine, ranitidine, doxycycline, hydrocortisone, dexamethasone, betamethasone, triamcinolone, albiglutide, alogliptin, metformin, pioglitazone, bupropion, aprepitant, morphine, omeprazole, metronidazole, cholecalciferol and calcifediol. Acetylsalicylic acid is a minor interaction.
- **Literature-reported adverse reactions.** The retrieved publications describe phenytoin-associated thrombocytopenia, hyperglycemia and diabetic ketoacidosis, and erythema multiforme in patients receiving cranial radiation (EMPACT syndrome). The EMPACT syndrome is relevant to patients with brain tumours.

Please refer to the package insert for official warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on model output alone (L5). There are no clinical trials and no literature specific to trigeminal nerve neoplasm, and there is no known anti-tumour mechanism. The only registration in the Philippines is cancelled.

**To proceed, the following is needed:**
- Evidence of anti-tumour activity or a clinically meaningful role in trigeminal nerve tumours, such as symptom control or seizure prophylaxis
- Detailed mechanism of action data
- Package insert warnings and contraindications for the Philippines
- A review of the related prediction **trigeminal neuralgia**. It has L3 evidence, including guidelines, reviews, and retrospective cohorts of IV phenytoin for acute exacerbations. It is a more practical research question than the neoplasm prediction, but only as a niche option when oral therapy is not possible.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

