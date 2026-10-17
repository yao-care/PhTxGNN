---
layout: default
title: Sevoflurane
parent: Model Prediction Only (L5)
nav_order: 311
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Sevoflurane: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not stated in the Philippines licence record (sevoflurane is known as…"
monitor_inn: "Sevoflurane"
predicted_indications: ["Prinzmetal angina", "Tourette syndrome", "fibromyalgia", "tendinitis", "myositis fibrosa", "idiopathic granulomatous myositis", "nephrogenic syndrome of inappropriate antidiuresis", "trichotillomania", "migraine disorder", "inclusion body myositis"]
---

# Sevoflurane
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

# Sevoflurane: From General Anaesthesia to Prinzmetal Angina

## One-Sentence Summary

Sevoflurane is an inhaled general anaesthetic. The data compiled for this report do not list an approved indication for it in the Philippines.
The TxGNN model predicts it may be effective for **Prinzmetal angina**, but there are **0 clinical trials** and **0 publications** for this indication, so the prediction rests on the model score alone.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not stated in the Philippines licence record (sevoflurane is known as an inhaled general anaesthetic) |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Cancelled only (no valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available. Based on general pharmacology, sevoflurane is a volatile anaesthetic. Its anaesthetic effects are generally attributed to modulation of GABA-A and NMDA receptors. Volatile anaesthetics can also relax vascular smooth muscle and affect calcium handling. This is the only speculative link to coronary vasospasm, the cause of Prinzmetal angina.

This link is not supported by the data compiled for this report. Sevoflurane is given by inhalation under controlled medical conditions and is not a practical chronic therapy for a vasospastic condition. The high score (99.78%) most likely reflects relationships in the knowledge graph rather than direct clinical evidence.

## Other Predicted Indications (for reference)

All of the following are rated Hold. None has clinical trial support.

| Rank | Predicted Indication | Score | Evidence Level | Assessment |
|------|------|------|------|------|
| 2 | Tourette syndrome | 99.50% | L5 | Prediction only. Speculative GABA/NMDA rationale. |
| 3 | Fibromyalgia | 99.42% | L4 | One case report on anaesthetic management, not treatment. |
| 4 | Tendinitis | 99.41% | L4 | Nine papers, all about anaesthesia in tendon-related surgery. None tests treatment of the disease. |
| 5 | Myositis fibrosa | 99.41% | L5 | Prediction only. |
| 6 | Idiopathic granulomatous myositis | 99.41% | L5 | Prediction only. The identical score to rank 5 suggests shared graph neighbours. |
| 7 | Nephrogenic syndrome of inappropriate antidiuresis | 99.40% | L5 | Prediction only. No supported link. |
| 8 | Trichotillomania | 99.33% | L5 | Prediction only. Speculative. |
| 9 | Migraine disorder | 99.23% | L4 | One paediatric MRI anaesthesia cohort. The association is likely incidental. |
| 10 | Inclusion body myositis | 99.09% | L4 | One case report on perioperative safety, which is the opposite of a repurposing signal. |

## Clinical Trial Evidence

Currently no related clinical trials registered for Prinzmetal angina or for any of the other top-10 predicted indications.

## Literature Evidence

Currently no related literature available for Prinzmetal angina.

For reference, the literature found for lower-ranked predictions concerns sevoflurane used as an anaesthetic during surgery or procedures, not as a treatment for the disease. Examples:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [26419112](https://pubmed.ncbi.nlm.nih.gov/26419112/) | 2015 | Case report | Masui | Anaesthetic management with sevoflurane in a patient with fibromyalgia. Perioperative care only. |
| [38233786](https://pubmed.ncbi.nlm.nih.gov/38233786/) | 2024 | Comparative trial (likely RCT) | BMC Anesthesiology | Propofol vs sevoflurane for surgical field visibility in arthroscopic rotator cuff repair. Measures anaesthetic technique, not tendinitis treatment. |
| [31852450](https://pubmed.ncbi.nlm.nih.gov/31852450/) | 2019 | Retrospective cohort | BMC Anesthesiology | Ten years of sevoflurane anaesthesia for MRI in children with neuropsychiatric disorders. Not a migraine study. |
| [27247916](https://pubmed.ncbi.nlm.nih.gov/27247916/) | 2016 | Case report | Anesthesiology and Pain Medicine | Anaesthetic considerations in sporadic inclusion body myositis. Concerns perioperative safety. |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0441 | Sevoflurane | Not stated | Not stated (status: cancelled) |

## Safety Considerations

- **Conditions flagged in the knowledge graph (not label text)**: The TxGNN knowledge graph links sevoflurane with contraindication edges to epilepsy, kidney disease, liver disease, gallbladder disease, pyoureter, proteinuria, hypotensive disorder, malignant hyperthermia of anaesthesia, exercise-induced malignant hyperthermia, intracranial hypertension, pseudotumor cerebri, Duchenne muscular dystrophy, Becker muscular dystrophy and muscular dystrophy.
- **Drug Interactions**: 100 interactions were found. The main ones (Major severity) are:
  - Epinephrine
  - Dolasetron
  - Cisapride

  Moderate interactions include famotidine, morphine, ondansetron, palonosetron, clarithromycin, levofloxacin, exenatide, and several laxatives and bowel-preparation agents. Metronidazole is a minor interaction.

Package insert warnings and contraindications were not available. Please refer to the package insert for the full safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction for Prinzmetal angina has no supporting clinical trials or literature (L5). Sevoflurane is an inhaled anaesthetic that is not suited to chronic treatment of this condition. In the Philippines its only registration is cancelled. The same applies to the other nine predicted indications, which lack trials and have only incidental anaesthesia literature.

**To proceed, the following is needed:**
- Mechanism of action data to assess any link to coronary vasospasm
- Preclinical or early clinical evidence of benefit in the predicted indication
- Package insert warnings and contraindications from DOH-FDA Philippines
- An assessment of whether a suitable route and dosage form could exist for a chronic condition
- Clarification of the cancelled registration status and the original approved indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

