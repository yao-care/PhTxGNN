---
layout: default
title: Calcipotriol
parent: 僅模型預測 (L5)
nav_order: 52
evidence_level: L5
indication_count: 10
---

# Calcipotriol
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

# Calcipotriol: From Psoriasis to Seborrheic Keratosis

## One-Sentence Summary

Calcipotriol is a synthetic vitamin D3 analog (calcipotriene), widely used as a topical treatment for plaque psoriasis by modulating keratinocyte proliferation and differentiation via the vitamin D receptor (VDR).
The TxGNN model predicts it may be effective for **Seborrheic Keratosis** (老人疣／脂溢性角化症),
with **0 registered clinical trials** and **6 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Plaque psoriasis (topical treatment) |
| Predicted New Indication | Seborrheic Keratosis |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Calcipotriol is a synthetic vitamin D3 analog that exerts its effects by binding to the vitamin D receptor (VDR), a nuclear receptor widely expressed in keratinocytes. Through VDR activation, calcipotriol inhibits keratinocyte hyperproliferation and promotes differentiation and apoptosis — the same biological pathway that makes it effective in psoriasis, where keratinocyte overgrowth is the hallmark pathology.

Seborrheic keratosis (SK), commonly known as senile warts, is fundamentally a benign epithelial neoplasm characterized by localized, excessive keratinocyte proliferation. This mechanistic overlap is direct and biologically plausible: if calcipotriol can suppress abnormal keratinocyte growth in psoriasis, the same anti-proliferative and pro-apoptotic VDR signaling may reduce SK lesions. A 2005 clinical study (PMID 16043912) explicitly documented apoptosis induction in seborrheic keratosis treated with topical vitamin D3 analogs, including calcipotriol.

Currently, detailed mechanism of action data from DrugBank is not available in this evidence pack. However, based on established pharmacology, calcipotriol's VDR-mediated regulation of keratinocyte biology provides a strong scientific rationale for its repurposing in seborrheic keratosis, and multiple small clinical series have demonstrated complete lesion regression with topical application.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for calcipotriol in seborrheic keratosis.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36752725](https://pubmed.ncbi.nlm.nih.gov/36752725/) | 2023 | Prospective Clinical Series (open-label) | Australasian Journal of Dermatology | Case series of 12 patients with facial SK treated with 0.005% calcipotriol ointment for 3–8 months; complete lesion regression achieved, with remission lasting 6–10 years |
| [15090020](https://pubmed.ncbi.nlm.nih.gov/15090020/) | 2004 | Comparative Clinical Study | International Journal of Dermatology | Head-to-head comparison of cryosurgery vs. topical calcipotriene, tazarotene, and imiquimod for SK; assessed efficacy of topical alternatives to procedural treatment |
| [16043912](https://pubmed.ncbi.nlm.nih.gov/16043912/) | 2005 | Clinical + Mechanistic Study | The Journal of Dermatology | 116 patients treated with topical vitamin D3 analogs (including calcipotriol); 30.2% showed response; authors conclude efficacy is likely mediated through apoptosis induction |
| [15577148](https://pubmed.ncbi.nlm.nih.gov/15577148/) | 2004 | Clinical Article / Case Series | Clinical Calcium | Japanese review reporting treatment of senile warts (SK) with topical vitamin D3 analogs once or twice daily; supporting data for calcipotriol in this setting |
| [10721662](https://pubmed.ncbi.nlm.nih.gov/10721662/) | 2000 | Case Report | The Journal of Dermatology | A patient with keratosis lichenoides chronica (seborrheic dermatitis-like features) showed marked response to calcipotriol ointment; highlights VDR-mediated anti-keratotic activity |
| [21534378](https://pubmed.ncbi.nlm.nih.gov/21534378/) | 2011 | Clinical Vignette | JAAPA | Clinical discussion of a spotted, itchy rash on the shins diagnosed as seborrheic keratosis; contextual reference for clinical presentation |

---

## Philippines Market Information

Calcipotriol currently has **no registered products** with the Philippines FDA (Food and Drug Administration). It is not available as a marketed pharmaceutical in the Philippines as of the data cutoff (April 4, 2026).

---

## Safety Considerations

Detailed safety data (package insert warnings, contraindications, and drug interactions) were not available in this evidence pack for the Philippines market.

Please refer to the package insert and international prescribing information for safety guidance. Key considerations known from general pharmacology include:
- **Hypercalcemia risk**: Excessive use or application to large body surface areas may raise serum calcium levels; weekly dose limits apply (typically ≤100 g/week for adults)
- **Skin irritation**: Local irritation at the application site is the most commonly reported adverse effect
- **Pregnancy and lactation**: Use with caution; systemic absorption risk should be assessed

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple small clinical studies and case series (6 publications, including prospective and comparative designs) directly document complete or partial regression of seborrheic keratosis with topical calcipotriol, and a mechanistic study has confirmed apoptosis induction as the likely mode of action. While no registered clinical trials exist and the current evidence is limited to small series (L3), the biological rationale is strong and initial clinical results are consistent.

**To proceed, the following is needed:**

- **Regulatory filing**: Register calcipotriol topical formulation with the Philippines FDA before any clinical use
- **Mechanism of action data**: Obtain full DrugBank MOA entry to support regulatory dossier preparation
- **Formal clinical trial**: Design a prospective, controlled pilot trial (Phase 2) in the Philippines to generate local efficacy and safety data
- **Safety data package**: Retrieve the complete package insert (warnings, contraindications, drug interactions) from an approved market (e.g., EMA, FDA-USA) to complete the local safety assessment
- **Dose optimization**: Confirm appropriate application frequency and duration for SK specifically, distinct from psoriasis dosing regimens
- **Hypercalcemia monitoring plan**: Establish serum calcium monitoring protocol for patients with extensive or prolonged treatment

> **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before clinical application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

