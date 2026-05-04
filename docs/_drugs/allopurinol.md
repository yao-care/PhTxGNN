---
layout: default
title: Allopurinol
parent: 僅模型預測 (L5)
nav_order: 18
evidence_level: L5
indication_count: 10
---

# Allopurinol
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

# Allopurinol: From Gout/Hyperuricemia to Hepatic Porphyria

## One-Sentence Summary

Allopurinol is a xanthine oxidase (XO) inhibitor widely used in the treatment of gout and hyperuricemia, reducing uric acid production and oxidative stress.
The TxGNN model predicts it may be effective for **Hepatic Porphyria**,
with **0 clinical trials** and **2 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gout and hyperuricemia (xanthine oxidase inhibition) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L4 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on well-established pharmacology, Allopurinol is a xanthine oxidase (XO) inhibitor that blocks the conversion of hypoxanthine and xanthine to uric acid, and reduces reactive oxygen species (ROS) generated as a byproduct of the XO reaction. Its active metabolite, oxypurinol, sustains this inhibition with a longer half-life.

The potential mechanistic link to hepatic porphyria centers on heme biosynthesis regulation. Allopurinol and oxypurinol have been hypothesized to suppress 5-aminolevulinate synthase (ALAS) — the rate-limiting enzyme of heme biosynthesis — either through direct feedback modulation of the hepatic regulatory heme pool or indirectly by reducing XO-derived ROS that can amplify ALAS induction. In acute hepatic porphyria attacks, ALAS is abnormally upregulated due to depletion of the regulatory heme pool; pharmacologically dampening this pathway is a recognized therapeutic target.

A 2019 hypothesis paper (PMID 31443750) proposed that metabolic targeting of hepatic ALAS — via inhibition of heme utilization by tryptophan 2,3-dioxygenase (TDO) — could serve as a novel therapy for acute hepatic porphyrias. This framework partially overlaps with the XO-inhibition pathway. Nevertheless, no clinical trial has directly evaluated Allopurinol in porphyria patients, and the mechanistic connection remains hypothetical pending experimental validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31443750](https://pubmed.ncbi.nlm.nih.gov/31443750/) | 2019 | Hypothesis/Opinion | Medical Hypotheses | Proposes metabolic targeting of liver ALAS via TDO inhibition or tryptophan supplementation as a therapy for acute hepatic porphyrias; discusses regulatory heme pool depletion and secondary ALAS induction as the pathomechanism of acute porphyric attacks |
| [1567472](https://pubmed.ncbi.nlm.nih.gov/1567472/) | 1992 | Animal Study | Biochemical Pharmacology | Demonstrates that carbamazepine exacerbates hepatic porphyria in rats by perturbing haem metabolism; provides a validated screening model for drug–haem interaction, relevant background for evaluating XO inhibitors in the same pathway |

---

## Philippines Market Information

Allopurinol currently has **no registered products** with the Philippine FDA. The drug is not marketed in the Philippines, and no product authorizations are on record.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although the TxGNN model assigns a high prediction score (99.95%) for Allopurinol in hepatic porphyria and a theoretically plausible mechanistic link exists via ALAS/XO inhibition and ROS reduction, the supporting evidence is limited to two Tier 3 studies (one animal study and one hypothesis paper) with no registered clinical trials or human data directly evaluating this indication. The evidence level (L4) and the absence of Philippines market registration together indicate that further foundational work is required before any clinical development steps can be planned.

**To proceed, the following is needed:**
- Retrieve complete MOA data from DrugBank API to formally characterize Allopurinol's relationship with heme biosynthesis enzymes
- Obtain the Philippines FDA (or international) package insert to document full safety profile, contraindications, and key warnings
- Commission a targeted systematic literature review on Allopurinol + ALAS inhibition / porphyria in human or higher-tier preclinical models
- Evaluate whether Allopurinol's known safety risks (e.g., Stevens-Johnson syndrome, allopurinol hypersensitivity syndrome) are acceptable in the hepatic porphyria patient population
- Consider a pilot proof-of-concept preclinical study (e.g., rodent porphyria model) to generate L3/L2 evidence before any human study design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

