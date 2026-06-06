---
layout: default
title: Ketoprofen
parent: 僅模型預測 (L5)
nav_order: 192
evidence_level: L5
indication_count: 10
---

# Ketoprofen
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

Using `txgnn-pipeline` to confirm context. Now generating the evaluation report based on the Evidence Pack.

---

# Ketoprofen: From Anti-inflammatory & Pain Management to Acromesomelic Dysplasia, Hunter-Thompson Type

## One-Sentence Summary

Ketoprofen is a well-established propionic acid-class NSAID, widely used for pain relief, arthritis, and inflammatory conditions through COX-1/COX-2 inhibition.
The TxGNN model predicts it may be effective for **Acromesomelic Dysplasia, Hunter-Thompson Type** — a rare genetic skeletal disorder caused by *GDF5* mutation —
however, **no clinical trials and no published literature** currently support this specific repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Anti-inflammatory, analgesic, arthritis (NSAID; no Philippines FDA registration on record) |
| Predicted New Indication | Acromesomelic Dysplasia, Hunter-Thompson Type |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L5 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacological knowledge, Ketoprofen is a propionic acid-class non-steroidal anti-inflammatory drug (NSAID) that non-selectively inhibits the COX-1 and COX-2 cyclooxygenase enzymes, thereby blocking prostaglandin synthesis and delivering analgesic, antipyretic, and anti-inflammatory effects. Its clinical utility in musculoskeletal pain, rheumatoid arthritis, osteoarthritis, and dysmenorrhea is well-documented in international guidelines.

Acromesomelic dysplasia, Hunter-Thompson type, is a rare autosomal recessive skeletal dysplasia caused by loss-of-function mutations in the *GDF5* gene. The disorder manifests as progressive shortening of the middle and distal limb segments and is fundamentally structural and developmental in nature — not driven by prostaglandin-mediated inflammation. While Ketoprofen's analgesic properties could theoretically provide symptomatic pain relief in affected individuals, it has no capacity to correct the underlying genetic or structural defect.

The high TxGNN score (99.98%) is most likely an artifact of knowledge graph topology: the model propagates signal through shared "skeletal development / cartilage metabolism" nodes common to multiple bone disorders, rather than identifying a specific mechanistic pathway. This prediction should be interpreted with caution and does not imply clinical actionability.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

> **Note on Rank 8 (Spondyloarthropathy):** Although not the top-ranked prediction, the rank 8 indication — *spondyloarthropathy, susceptibility to* — has a meaningfully stronger mechanistic basis. NSAIDs including Ketoprofen are EULAR/ACR guideline-recommended first-line therapy for spondyloarthropathy and reactive arthritis (Fiessinger-Leroy-Reiter syndrome). One supporting review is available (see Literature table below).

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20470931](https://pubmed.ncbi.nlm.nih.gov/20470931/) | 2010 | Review | Ann Dermatol Venereol | Review of reactive arthritis (Fiessinger-Leroy-Reiter syndrome); indirectly supports NSAID use in the spondyloarthropathy spectrum |

---

## Philippines Market Information

Ketoprofen currently holds **no product registrations** with the Philippine FDA. There are no licenses on record, and the drug is classified as not marketed in the Philippines.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Acromesomelic dysplasia, Hunter-Thompson type is a genetic skeletal disorder with no known prostaglandin-driven pathology; Ketoprofen's COX-inhibition mechanism has no established therapeutic link to the root *GDF5* defect. The evidence is purely model-derived (L5) with zero supporting clinical trials or literature, and Ketoprofen has no Philippines regulatory presence — making clinical consideration premature under any interpretation.

**To proceed, the following is needed:**

- **Clarify repurposing intent:** If the goal is symptomatic pain relief rather than disease modification, reclassify the target indication (e.g., musculoskeletal pain in skeletal dysplasia) and re-evaluate under a pain management framework
- **Obtain Philippines FDA registration:** No market authorization exists; regulatory filing is a prerequisite for any clinical pathway
- **Retrieve full MOA data from DrugBank:** Formal pharmacodynamic documentation is required to support mechanistic rationale
- **Retrieve safety data:** Philippines FDA prescribing information and package insert warnings/contraindications are currently unavailable (Data Gap — Blocking severity)
- **Prioritize rank 8 (Spondyloarthropathy) for near-term evaluation:** This indication has a plausible and guideline-supported mechanistic basis for NSAID use, L4 evidence from literature, and represents a more actionable repurposing hypothesis than the top-ranked rare skeletal dysplasia
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

