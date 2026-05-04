---
layout: default
title: Doxycycline
parent: 僅模型預測 (L5)
nav_order: 118
evidence_level: L5
indication_count: 10
---

# Doxycycline
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

# Doxycycline: From Bacterial Infections to Punctate Epithelial Keratoconjunctivitis

## One-Sentence Summary

Doxycycline is a broad-spectrum tetracycline antibiotic serving as first-line treatment for intracellular bacterial infections including *Chlamydia trachomatis*, *Rickettsia* species, and *Borrelia burgdorferi*.
The TxGNN model predicts it may be effective for **Punctate Epithelial Keratoconjunctivitis**,
with **0 clinical trials** and **1 publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Broad-spectrum bacterial infections (chlamydia, rickettsia, Lyme disease, etc.) — no Philippines registration on file |
| Predicted New Indication | Punctate Epithelial Keratoconjunctivitis |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this Evidence Pack. Based on known information, Doxycycline is a tetracycline-class antibiotic that inhibits bacterial protein synthesis by binding to the 30S ribosomal subunit and blocking aminoacyl-tRNA attachment. This mechanism gives it particular potency against obligate intracellular organisms — notably *Chlamydia trachomatis*, *Rickettsia* spp., and *Borrelia burgdorferi* — that evade many conventional antibiotics.

The mechanistic link to punctate epithelial keratoconjunctivitis centers on *Chlamydia trachomatis* as the shared pathogen. Chlamydial follicular conjunctivitis is a recognized antecedent of punctate epithelial keratitis: the organism invades conjunctival and corneal epithelial cells, triggering an inflammatory cascade that produces characteristic grayish punctate corneal lesions, sometimes with anterior stromal edema. As the WHO-recommended first-line treatment for chlamydial infections, Doxycycline's ability to eliminate the underlying pathogen makes this connection scientifically plausible.

A secondary mechanism may also be relevant: Doxycycline inhibits matrix metalloproteinases (particularly MMP-9), enzymes implicated in corneal stromal degradation during inflammatory keratitis. This host-directed anti-inflammatory property could theoretically limit corneal tissue damage beyond bacterial clearance alone. That said, this prediction largely reflects Doxycycline's **established** role in chlamydial disease rather than a novel repurposing. Systematic clinical validation specifically targeting punctate epithelial keratoconjunctivitis as a primary endpoint is absent.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [1424659](https://pubmed.ncbi.nlm.nih.gov/1424659/) | 1992 | Case Series / Retrospective | *Cornea* | Two patients with *C. trachomatis* follicular conjunctivitis treated with oral tetracycline or doxycycline resolved their follicles, but subsequently developed persistent, recurrent bilateral grayish punctate corneal lesions with fluorescein staining and anterior stromal edema — suggesting post-infectious corneal sequelae may persist or recur despite successful antibiotic clearance of the original infection |

---

## Philippines Market Information

Doxycycline is currently **not registered** with the Philippine FDA (FDA-PH). No product authorization records are on file. This may reflect a regulatory gap rather than safety concerns, as doxycycline is included on the WHO Essential Medicines List and is widely approved in other jurisdictions.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Philippines FDA package insert data (warnings and contraindications) were identified as a blocking data gap (DG001) for this evaluation. Drug interaction data was also unavailable (query returned no results). These gaps must be resolved before any clinical decision-making.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The sole supporting evidence is a single 1992 retrospective case series (n=2, L4), and the identified mechanistic link reflects Doxycycline's already-established efficacy against chlamydial infections rather than a genuine novel repurposing opportunity. No registered clinical trials address punctate epithelial keratoconjunctivitis as a primary endpoint, and both key safety data items (TFDA/FDA-PH package insert warnings and MOA characterization) remain unresolved blocking gaps.

**To proceed, the following is needed:**

- **Safety data (Blocking):** Obtain Philippine FDA package insert PDF and parse warnings, contraindications, and precautions before any safety assessment can proceed
- **MOA data (High priority):** Query DrugBank API for DB00254 to formally characterize mechanism and strengthen or challenge the repurposing rationale
- **Clinical evidence:** Identify or design a prospective clinical study specifically evaluating Doxycycline in punctate epithelial keratoconjunctivitis (chlamydial etiology confirmed by PCR/culture)
- **Patient population definition:** Distinguish chlamydial vs. non-chlamydial (viral, allergic, toxic) etiologies of punctate keratoconjunctivitis, as Doxycycline would only be expected to benefit the infectious subtype
- **Philippines registration pathway:** If clinical evidence is ultimately sufficient, evaluate a supplemental indication filing with FDA-PH given zero current market presence

> **⚠️ Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

