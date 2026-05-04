---
layout: default
title: Phenobarbital
parent: 僅模型預測 (L5)
nav_order: 173
evidence_level: L5
indication_count: 10
---

# Phenobarbital
{: .fs-9 }

證據等級: **L5** | 預測適應症: **10** 個
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

# Phenobarbital: From Seizures to Trigeminal Nerve Neoplasm

## One-Sentence Summary

Phenobarbital is a long-established barbiturate antiepileptic drug, widely used as a first-line agent for neonatal seizures and general epilepsy management across all age groups.
The TxGNN model predicts it may be effective for **Trigeminal Nerve Neoplasm**, with **0 clinical trials** and **1 loosely related publication** currently supporting this direction.
The mechanistic basis for this specific prediction is indirect and unconvincing — phenobarbital has no known anti-tumor activity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines registration data (globally recognized antiepileptic drug) |
| Predicted New Indication | Trigeminal Nerve Neoplasm |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on widely recognized pharmacological knowledge, phenobarbital is a barbiturate that acts as a positive allosteric modulator of GABA-A receptors, prolonging chloride ion channel opening to produce broad cortical inhibition. This is the foundation of its well-established anticonvulsant properties, including its status as the preferred first-line drug for neonatal seizures in international clinical guidelines (ILAE, 2023).

The connection between phenobarbital and trigeminal nerve neoplasm is mechanistically indirect at best. Tumors affecting the trigeminal nerve can cause secondary seizures or neuropathic pain through nerve compression; phenobarbital's GABA-enhancing effect might theoretically address these secondary symptoms. However, it has no known anti-proliferative, cytotoxic, or anti-tumor mechanism. The core treatment for trigeminal nerve neoplasms remains surgery or radiotherapy — pharmacological GABA modulation plays no role in tumor biology.

The high TxGNN prediction score (0.9996) most likely reflects a knowledge graph traversal path along the lines of "trigeminal nerve → neurological pathway → seizures / neuropathic pain → phenobarbital," which represents significant over-generalization. This interpretation is reinforced by examining the drug's other top-10 predictions, all of which are specific seizure subtypes (orgasm-induced, micturation-induced, eating, thinking, startle, audiogenic, reading seizures), where the mechanistic link to phenobarbital is far more direct and clinically credible.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [9157801](https://pubmed.ncbi.nlm.nih.gov/9157801/) | 1997 | Case Series | *Anales Españoles de Pediatría* | Retrospective review of 14 Sturge-Weber syndrome cases over 25 years; evaluates clinical features, disease course, and treatment response. No direct focus on phenobarbital for trigeminal nerve neoplasm; relevance to predicted indication is peripheral. |

---

## Philippines Market Information

Phenobarbital is **not currently registered** with the Philippines FDA. There are no active product licenses, authorizations, or market approvals on record for any dosage form.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN score (99.96%), this prediction lacks any supporting clinical evidence and is mechanistically implausible — phenobarbital is an antiepileptic drug with GABA-A agonism, not an anti-tumor agent, and its predicted link to trigeminal nerve neoplasm most likely represents a spurious knowledge graph path rather than a genuine therapeutic opportunity.

**To proceed, the following is needed:**
- Clarification of the TxGNN knowledge graph path to understand the specific multi-hop chain driving this prediction
- Structured search for any preclinical data on phenobarbital in neural tumor or neuro-oncology models
- MOA documentation from DrugBank API to formally rule out any indirect anti-tumor pathway
- Philippines FDA package insert retrieval (PDF parsing) to complete safety assessment and fill the blocking data gap on warnings and contraindications
- Registration review for neighboring Southeast Asian markets (e.g., Thailand, Indonesia) to understand regional availability and formulation options should a lower-ranked but more mechanistically credible indication be pursued
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

