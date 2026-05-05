---
layout: default
title: Miconazole
parent: 僅模型預測 (L5)
nav_order: 188
evidence_level: L5
indication_count: 1
---

# Miconazole
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

Using `txgnn-pipeline` to confirm context, then generating the evaluation report per the v5 prompt instructions.

---

# Miconazole: From Fungal Infections to Acne

## One-Sentence Summary

Miconazole is a classic imidazole-class antifungal, widely used to treat cutaneous and mucosal fungal infections.
The TxGNN model predicts it may be effective for **acne (disease)**, with **1 clinical trial** (currently suspended) and **4 publications** supporting this direction — including direct in vitro evidence of antibacterial activity against *Cutibacterium acnes*.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Fungal infections (cutaneous / mucosal) |
| Predicted New Indication | Acne (disease) |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L3 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on established pharmacology, Miconazole is an imidazole-class antifungal that inhibits **CYP51 (lanosterol 14α-demethylase)**, blocking ergosterol biosynthesis in fungal cell membranes. Importantly, this antibacterial spectrum extends beyond fungi to certain gram-positive bacteria — including *Cutibacterium acnes* (formerly *Propionibacterium acnes*), the primary bacterial driver of acne vulgaris.

Three mechanistic pathways support this repurposing hypothesis: ① **Direct antibacterial activity** — in vitro data (PMID 20045949) confirm that azole antifungals, including imidazoles such as miconazole, exhibit measurable inhibitory activity against *C. acnes* at clinically relevant MIC values. ② **Malassezia folliculitis overlap** — this condition is frequently misdiagnosed as acne vulgaris, and miconazole is already a standard treatment; this creates a clinically meaningful indirect bridge to the acne indication. ③ **Secondary anti-inflammatory effect** — imidazole-class agents may suppress prostaglandin synthesis, potentially attenuating the inflammatory papules characteristic of acne.

The overall mechanistic linkage is rated **Grade B**: biologically plausible with direct in vitro evidence, but high-quality clinical confirmation is still lacking. The TxGNN prediction score of 99.54% reflects strong graph-level signal, though clinical translation requires further validation.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01244256](https://clinicaltrials.gov/study/NCT01244256) | Phase 2/3 | Suspended | 80 | Evaluated a combination cream (beclomethasone 0.025% + gentamicin 0.1% + antifungal component) for contaminated dermatosis with bilateral symmetrical lesions. Trial was suspended before completion; no efficacy conclusions can be drawn, and the multi-component design prevents isolation of miconazole's individual contribution. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18627330](https://pubmed.ncbi.nlm.nih.gov/18627330/) | 2008 | Review | Expert Opinion on Pharmacotherapy | Reviews miconazole nitrate's multifaceted effects on skin disorders beyond classical antifungal use, highlighting novel therapeutic directions for the imidazole class |
| [15536660](https://pubmed.ncbi.nlm.nih.gov/15536660/) | 2004 | Clinical Assessment (Split-face) | Skin Research and Technology | Split-face clinical assessment of catamenial acne in young women; evaluates a miconazole-containing regimen in the context of cyclically recurrent inflammatory skin changes |
| [8593718](https://pubmed.ncbi.nlm.nih.gov/8593718/) | 1995 | Observational / Case Series | Clinical and Experimental Dermatology | 62 patients with Pityrosporum (Malassezia) folliculitis, frequently misdiagnosed as acne vulgaris; supports the diagnostic overlap rationale and miconazole's established efficacy in this condition |
| [20045949](https://pubmed.ncbi.nlm.nih.gov/20045949/) | 2010 | In vitro Study | Biological & Pharmaceutical Bulletin | Determines in vitro activities of azole antifungals against *Propionibacterium acnes* from acne vulgaris patients; provides the most direct mechanistic link, showing clinically relevant anti-*C. acnes* MIC values for the imidazole class |

---

## Philippines Market Information

Miconazole currently has **no registered products** in the Philippines. There are no FDA Philippines authorization numbers on record, and the drug is classified as **not marketed**. Any clinical use in the Philippines would require a new drug registration submission before commercial adoption.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole registered clinical trial (NCT01244256) was suspended before completion and used a multi-component formulation that cannot isolate miconazole's individual contribution; available literature consists of one review, one small split-face clinical assessment, one observational case series, and one in vitro study — an evidence base insufficient for a repurposing adoption decision, particularly given zero Philippines market registrations and missing safety data.

**To proceed, the following is needed:**
- A dedicated randomized controlled trial evaluating **topical miconazole monotherapy** in confirmed acne vulgaris
- Retrieval of **MOA data from DrugBank** (DG002) to formally document the mechanistic rationale
- **Philippines FDA package insert review** to characterize key warnings and contraindications (DG001)
- **Philippines FDA registration pathway assessment** — a new drug application or bridging strategy will be required prior to any commercialization
- Dose-response and formulation characterization for the acne indication (optimal topical concentration, vehicle, and treatment duration)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

