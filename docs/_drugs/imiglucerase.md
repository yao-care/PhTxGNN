---
layout: default
title: Imiglucerase
parent: 僅模型預測 (L5)
nav_order: 171
evidence_level: L5
indication_count: 5
---

# Imiglucerase
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using the `txgnn-pipeline` skill to guide context. Now generating the evaluation report based on the Evidence Pack.

---

# Imiglucerase: From Gaucher Disease to Hurler Syndrome

## One-Sentence Summary

Imiglucerase (Cerezyme®) is a recombinant form of human glucocerebrosidase, originally approved as enzyme replacement therapy (ERT) for Gaucher disease — the prototypical lysosomal storage disease.
The TxGNN model predicts it may be effective for **Hurler Syndrome (MPS I)**,
with **0 clinical trials** and **2 publications** currently supporting this direction.
However, the mechanistic basis for this prediction is considered weak: the two diseases involve entirely different deficient enzymes, and a dedicated ERT for MPS I already exists.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gaucher disease (glucocerebrosidase deficiency) |
| Predicted New Indication | Hurler Syndrome (Mucopolysaccharidosis Type I) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Imiglucerase is a recombinant analogue of human glucocerebrosidase (encoded by the *GBA* gene). In Gaucher disease, this enzyme is deficient, leading to the accumulation of glucocerebroside in macrophages — particularly in the spleen, liver, and bone marrow. Intravenous infusion of Imiglucerase directly replaces the missing enzyme, clearing the substrate and reversing organ manifestations.

Hurler syndrome, on the other hand, is caused by a deficiency of an entirely different enzyme: **alpha-L-iduronidase** (encoded by *IDUA*). This deficiency leads to the buildup of dermatan sulfate and heparan sulfate — not glucocerebroside. Although both conditions belong to the broader class of lysosomal storage diseases (LSD), the enzymes involved, their substrates, and the resulting pathology are completely distinct. Imiglucerase has no enzymatic activity against the substrates that accumulate in MPS I.

The TxGNN model's high prediction score most likely reflects **graph proximity effects**: in the knowledge graph, both Gaucher disease and Hurler syndrome share the "lysosomal storage disease" node, causing the model to infer a connection through multi-hop path traversal rather than true enzymatic substitutability. This is a known limitation of graph-based predictions for rare disease ERTs. Notably, Hurler syndrome already has an approved ERT — laronidase (Aldurazyme) — making Imiglucerase repurposing in this space biologically implausible and clinically unnecessary.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Imiglucerase in Hurler Syndrome.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20534487](https://pubmed.ncbi.nlm.nih.gov/20534487/) | 2010 | Imaging/Observational | PNAS | PET imaging used to track ERT biodistribution across multiple LSDs including Gaucher disease, Fabry disease, Hurler syndrome, Hunter syndrome, and Pompe disease — describes ERT class effects, not Imiglucerase-specific efficacy in MPS I |
| [21211680](https://pubmed.ncbi.nlm.nih.gov/21211680/) | 2010 | Review | La Revue de médecine interne | Comprehensive review of ERT across lysosomal storage diseases; describes Imiglucerase (Cerezyme®) as the gold standard for Gaucher disease and reviews other approved ERTs for MPS I, Fabry disease, and Pompe disease — does not support Imiglucerase use in Hurler syndrome |

> **Note:** Both publications cover Imiglucerase and Hurler syndrome within the same ERT landscape review, but neither supports the use of Imiglucerase specifically for MPS I. They are included as contextual background, not as evidence of efficacy.

---

## Philippines Market Information

Imiglucerase is not registered in the Philippines. No license records are available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.52%), but this is almost certainly a **graph proximity artifact** rather than a true mechanistic signal. Imiglucerase replaces glucocerebrosidase (*GBA*), while Hurler syndrome requires alpha-L-iduronidase (*IDUA*) — these are different enzymes with different substrates. An approved ERT (laronidase/Aldurazyme) already exists for MPS I, leaving no unmet mechanistic niche for Imiglucerase in this indication.

**To proceed, the following would be needed:**
- A credible biological hypothesis explaining how glucocerebrosidase activity could compensate for alpha-L-iduronidase deficiency (currently none exists)
- Preclinical data (cell or animal model) demonstrating any substrate cross-reactivity or downstream pathway overlap
- Regulatory pathway assessment given that laronidase is already approved for MPS I in major markets
- Philippines FDA registration data and package insert for complete safety profiling

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

