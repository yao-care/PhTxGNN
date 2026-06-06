---
layout: default
title: Iodixanol
parent: 僅模型預測 (L5)
nav_order: 176
evidence_level: L5
indication_count: 3
---

# Iodixanol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
{: .fs-6 .fw-300 }

---

## 目錄
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## 藥師評估報告

</div>

Using `txgnn-pipeline` for context on report generation standards. Now composing the Iodixanol evaluation report based on the Evidence Pack.

---

# Iodixanol: From Radiographic Contrast Imaging to Osteoarthritis Susceptibility

## One-Sentence Summary

Iodixanol is a non-ionic, iso-osmolar iodinated contrast medium used clinically to enhance radiographic visibility of blood vessels and internal organs during procedures such as CT angiography and cardiac catheterization.
The TxGNN model predicts it may be relevant to **Osteoarthritis Susceptibility**, yet with **0 clinical trials** and **0 supporting literature** for this specific indication, the evidence sits at **L5 (model prediction only)**.
Expert review of the evidence strongly suggests this is a knowledge-graph false positive rather than a genuine repurposing signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Radiographic contrast medium for diagnostic imaging (no local Philippines registration on file) |
| Predicted New Indication | Osteoarthritis Susceptibility |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Iodixanol (brand name Visipaque) is a non-ionic dimeric, iso-osmolar iodinated contrast agent. Its sole pharmacological mechanism is X-ray attenuation via iodine atoms, enhancing vascular and tissue contrast during imaging. It has no known anti-inflammatory, chondroprotective, immunomodulatory, or disease-modifying properties. Mechanism of action data from DrugBank was unavailable for this report and should be formally retrieved; however, the drug class itself makes any arthritis-related mechanism pharmacologically implausible.

"Osteoarthritis susceptibility" is a genetic risk phenotype — it describes an individual's inherited predisposition to develop osteoarthritis, not an active inflammatory or degenerative disease state. There is no biological pathway through which a transiently circulating contrast agent could alter genetic susceptibility to OA.

The most probable explanation for the elevated TxGNN score (99.16%) is a **knowledge-graph false positive**: iodixanol has been extensively co-cited with joint and cartilage research in the context of *diagnostic* CT imaging of cartilage structure. These indirect graph edges (contrast agent → joint imaging → cartilage node → OA node) appear to have created a spurious association that the model interpreted as a therapeutic link. This is a recognized artifact in knowledge-graph-based prediction models when a drug is used as a *tool* (imaging agent) rather than a *therapeutic* in a disease area.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note:** A search of PubMed for Iodixanol + osteoarthritis (the rank-2 indication) did return 7 publications, but all describe iodixanol *as a diagnostic CT contrast agent* to visualize cartilage structure or study solute transport across the osteochondral interface — none evaluate iodixanol as a treatment for osteoarthritis. This further confirms the false-positive diagnosis for the rank-1 indication.

---

## Philippines Market Information

Iodixanol has **no registered product authorizations** with the Philippine FDA. It is not currently marketed in the Philippines.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | No registrations on file | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data (package insert warnings, contraindications, and drug-drug interactions) was not available in this Evidence Pack. Retrieval from the Philippine FDA or manufacturer label is required before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This TxGNN prediction is almost certainly a knowledge-graph false positive. Iodixanol is a purely diagnostic contrast agent with no pharmacological mechanism applicable to osteoarthritis susceptibility (a genetic predisposition phenotype), and zero clinical trial or literature evidence supports a therapeutic role. The high model score reflects spurious co-occurrence in imaging research, not a genuine repurposing opportunity.

**To proceed, the following is needed:**
- Formally retrieve and record iodixanol MOA from DrugBank API to close Data Gap DG002 and confirm absence of any arthritis-relevant pharmacology
- Retrieve Philippine FDA (or originating country) package insert to close Data Gap DG001 and document contraindications/warnings
- Flag this candidate as a **confirmed false positive** in the pipeline and archive with rationale to prevent re-surfacing in future prediction cycles
- Review TxGNN model knowledge-graph edges connecting contrast agents to musculoskeletal disease nodes to reduce similar false-positive rates for other diagnostic agents (e.g., iohexol, iopamidol)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

