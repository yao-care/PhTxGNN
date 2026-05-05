---
layout: default
title: Mometasone
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 1
---

# Mometasone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using the **txgnn-pipeline** skill context to guide the report generation. Now producing the full evaluation report from the Evidence Pack.

---

# Mometasone: From Inflammatory Skin Conditions to Primary Cutaneous T-Cell Lymphoma

## One-Sentence Summary

Mometasone is a high-potency synthetic topical corticosteroid widely used for inflammatory and allergic skin conditions such as atopic dermatitis and allergic rhinitis.
The TxGNN model predicts it may be effective for **primary cutaneous T-cell lymphoma (CTCL)**,
with **0 registered clinical trials** and **2 publications** (both indirect case reports) currently available to support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines FDA registration on file |
| Predicted New Indication | Primary Cutaneous T-Cell Lymphoma (CTCL) |
| TxGNN Prediction Score | 99.36% |
| Evidence Level | L4 — Mechanism-based; no prospective clinical trials |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Philippines regulatory registry. Based on established pharmacology, Mometasone is a high-potency synthetic glucocorticoid that binds and activates the glucocorticoid receptor (GR). This receptor activation is directly relevant to CTCL biology: it induces T-cell apoptosis through downregulation of the anti-apoptotic protein Bcl-2, suppresses pro-inflammatory and pro-tumour cytokines including IL-2, IFN-γ, and TNF-α, and inhibits the proliferation of malignant T-cells. These mechanisms collectively explain why a corticosteroid could theoretically have activity against a T-cell-derived malignancy.

Primary cutaneous T-cell lymphoma — particularly Mycosis Fungoides (MF) at early stages (IA–IIA) — is an indolent lymphoma arising from skin-homing malignant T-cells. The shared immunological architecture between inflammatory T-cell-driven skin disease (the traditional target of corticosteroids) and neoplastic T-cell disease provides a biologically plausible mechanistic bridge. In routine clinical practice, high-potency topical corticosteroids are already used empirically in early-stage MF management, lending real-world credibility to the TxGNN prediction.

The model assigns a very high confidence score of 99.36%, reflecting strong graph-topological proximity between mometasone and CTCL in the drug–disease knowledge graph. However, no prospective clinical trial specifically evaluating mometasone in CTCL has been registered or published to date. The two available publications are indirect case reports in which mometasone appears as a background or failed prior treatment, not as a studied intervention. Formal evidence generation is therefore required before this prediction can be acted upon.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40821495](https://pubmed.ncbi.nlm.nih.gov/40821495/) | 2025 | Case Report | Proceedings (Baylor University Medical Center) | A 62-year-old woman with cutaneous pseudolymphoma (a reactive T-cell process that clinically mimics cutaneous lymphoma) failed prior treatment with mometasone and tacrolimus, then responded to tapinarof. Mometasone was a prior unsuccessful treatment; this is indirect, negative-context evidence. |
| [25442255](https://pubmed.ncbi.nlm.nih.gov/25442255/) | 2015 | Case Report | Journal of Cutaneous Pathology | An 11-year-old boy with a 7-year history of CD8+CD56+ mycosis fungoides (a CTCL subtype) presenting with extensive erythematous patches and plaques. Highlights the diagnostic challenges and management complexity of childhood CTCL. Does not directly evaluate mometasone as a therapy. |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a mechanistically compelling prediction (TxGNN score 99.36%) and known real-world use of topical corticosteroids in early-stage CTCL, the currently available evidence for mometasone specifically consists only of two indirect case reports — neither of which prospectively evaluates mometasone as an active intervention. Mometasone has no Philippines market registration, no clinical trials are on record, and safety data has not been retrieved.

**To proceed, the following is needed:**
- **Clinical evidence:** Identify or initiate a retrospective chart review or prospective pilot study evaluating topical mometasone in early-stage MF (Stage IA–IIA) to generate direct efficacy and safety data
- **Regulatory pathway:** Obtain Philippines FDA market approval or establish a named-patient / compassionate use pathway before any local deployment
- **Safety data retrieval:** Download and parse the official package insert (TFDA, EMA, or FDA-US) to extract labelled warnings, contraindications, and precautions — this is currently a blocking data gap (DG001)
- **MOA documentation:** Query DrugBank API for DB00764 to formally document the mechanism of action and support the mechanistic link analysis (DG002)
- **Expert validation:** Engage a dermatology-oncology specialist to assess the clinical plausibility of mometasone as a repurposing candidate and to determine whether existing real-world use data could support a retrospective study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

