---
layout: default
title: Filgrastim
parent: Model Prediction Only (L5)
nav_order: 142
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Filgrastim: predicted new indication Primary release disorder of platelets (evidence level L5). Approved use: Constitutional neutropenia"
monitor_inn: "Filgrastim"
predicted_indications: ["primary release disorder of platelets", "pseudo-von Willebrand disease", "Glanzmann thrombasthenia", "Scott syndrome", "hemorrhagic disorder due to a constitutional thrombocytopenia", "bleeding diathesis due to a collagen receptor defect", "C1 inhibitor deficiency", "serpinopathy with toxic serpin polymerization", "fetal and neonatal alloimmune thrombocytopenia", "platelet-type bleeding disorder"]
---

# Filgrastim
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

# Filgrastim: From Severe Congenital Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a granulocyte colony-stimulating factor (G-CSF) originally used for neutropenia conditions, including severe congenital neutropenia, constitutional neutropenia, and cyclic hematopoiesis.
The TxGNN model predicts it may be effective for **primary release disorder of platelets**, but this is a graph-based prediction only, with **0 directly supporting clinical trials** and **0 publications**.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Constitutional neutropenia; severe congenital neutropenia; cyclic hematopoiesis; chronic familial neutropenia (from the knowledge graph, not from local label text) |
| Predicted New Indication | Primary release disorder of platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, filgrastim is a G-CSF that acts on the neutrophil lineage through the G-CSF receptor. Its efficacy in neutropenia conditions is the basis of its original indications.

A mechanistic link to platelet secretion or release defects is not established in the data compiled for this report. The very high TxGNN score most likely reflects proximity within the knowledge graph (for example, shared haematological disease neighbours) rather than a demonstrated biological rationale. The other top-ranked predictions (pseudo-von Willebrand disease, Glanzmann thrombasthenia, Scott syndrome and others) are also platelet or bleeding disorders with no known connection to G-CSF signalling, which suggests a systematic pattern in the model rather than disease-specific insight.

## Clinical Trial Evidence

No clinical trials are linked to the top predicted indication. The only trials in the compiled data are linked to a lower-ranked prediction, platelet-type bleeding disorder (rank 10). All are graded C (low relevance): they are stem cell transplantation protocols in haematologic malignancies, where filgrastim is probably supportive care and not the studied intervention.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00296023](https://clinicaltrials.gov/study/NCT00296023) | NA | Completed | 25 | Low-dose allogeneic PBSC transplantation in high-risk low-grade haematologic malignancies |
| [NCT00004232](https://clinicaltrials.gov/study/NCT00004232) | Phase 1 | Completed | Not reported | CD34-enriched stem cell augmentation of bone marrow for allogeneic transplant |
| [NCT00054236](https://clinicaltrials.gov/study/NCT00054236) | Phase 1 | Completed | 55 | Multiple cord blood unit transplantation after non-myeloablative conditioning |
| [NCT00301912](https://clinicaltrials.gov/study/NCT00301912) | Phase 2 | Withdrawn | 0 | Busulfan/fludarabine conditioning before transplant; no participants enrolled |
| [NCT00295997](https://clinicaltrials.gov/study/NCT00295997) | NA | Unknown | 35 | Non-myeloablative matched unrelated donor transplantation |
| [NCT00080925](https://clinicaltrials.gov/study/NCT00080925) | Phase 1 | Completed | 20 | T-cell depleted, reduced-intensity haploidentical transplantation |
| [NCT00004904](https://clinicaltrials.gov/study/NCT00004904) | Phase 1 | Completed | Not reported | T-cell depleted partially matched donor transplantation with CD34 "veto" cells |

None of these trials tests filgrastim for a platelet disorder.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0190 | Filgrastim | Not recorded | Not recorded (status: cancelled) |

## Safety Considerations

- **Drug Interactions**: 100 interactions were found. The ones listed below are all rated Moderate, and the first 20 returned include:
  - Radiopharmaceuticals and radioimmunotherapy: iobenguane (I-131), fludeoxyglucose (18F), ibritumomab tiuxetan, tositumomab, tositumomab (I-131)
  - Cytotoxic and antineoplastic agents: paclitaxel, mercaptopurine, trimetrexate, azacitidine, bendamustine, altretamine, arsenic trioxide, asparaginase *Escherichia coli*
  - Targeted agents and immunotherapies: abemaciclib, acalabrutinib, avapritinib, aldesleukin, alemtuzumab, belantamab mafodotin
  - Other: levamisole

For warnings and contraindications, please refer to the package insert.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction is supported only by a graph-based score, with no relevant clinical trials or literature (Evidence Level L5). No plausible mechanistic link between G-CSF and platelet release defects has been identified. In addition, the only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Mechanism of action data and a credible biological rationale linking G-CSF to platelet function or release
- Preclinical or clinical evidence in platelet function disorders
- Package insert warnings and contraindications from the DOH-FDA Philippines (a blocking gap for safety screening)
- Clarification of the regulatory status and available formulations in the Philippines
- Review of the other predictions, since all of the top-ranked indications currently lack evidence
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

