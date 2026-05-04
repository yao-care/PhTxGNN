---
layout: default
title: Ciprofloxacin
parent: 僅模型預測 (L5)
nav_order: 73
evidence_level: L5
indication_count: 10
---

# Ciprofloxacin
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

# Ciprofloxacin: From Bacterial Infections to Diffuse Scleroderma

## One-Sentence Summary

Ciprofloxacin is a broad-spectrum fluoroquinolone antibiotic, widely used to treat bacterial infections including urinary tract infections, respiratory tract infections, and septicemia.
The TxGNN model predicts it may have potential utility for **Diffuse Scleroderma**, with **0 registered clinical trials** and **2 publications** currently supporting this direction.
Evidence remains at an early exploratory stage, and this prediction should be considered a research question requiring further validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bacterial infections (urinary tract, respiratory, gastrointestinal, and systemic) |
| Predicted New Indication | Diffuse Scleroderma |
| TxGNN Prediction Score | 99.87% |
| Evidence Level | L4 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ciprofloxacin is a fluoroquinolone antibiotic that exerts bactericidal effects by inhibiting two critical bacterial enzymes — DNA gyrase (topoisomerase II, GyrA subunit) and topoisomerase IV (ParC subunit) — causing irreparable double-strand DNA breaks in bacteria. While its primary role is antimicrobial, there is emerging in vitro evidence suggesting secondary anti-fibrotic properties that are structurally independent of its antibacterial mechanism.

The mechanistic rationale for scleroderma operates through two distinct pathways. The first is **direct anti-fibrotic activity**: in vitro experiments show that ciprofloxacin can suppress fibroblast proliferation and inhibit TGF-β-driven collagen synthesis, a core driver of scleroderma progression. The second is **indirect benefit through treating Small Intestinal Bacterial Overgrowth (SIBO)**: systemic sclerosis patients frequently develop gut dysmotility, leading to SIBO; by reducing microbial overgrowth, ciprofloxacin may dampen downstream immune activation and pro-fibrotic signaling in the gut-skin axis.

It must be noted clearly that both proposed mechanisms are **indirect interventions** — neither directly targets the primary pathogenesis of scleroderma, which is driven by autoimmune vasculopathy and progressive fibrosis. The biological plausibility is hypothesis-generating at this stage. The TxGNN model's high prediction score likely reflects shared knowledge graph pathways around fibrosis and connective tissue disease nodes, but this has not been confirmed in adequately powered clinical studies.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Ciprofloxacin in Diffuse Scleroderma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [20507401](https://pubmed.ncbi.nlm.nih.gov/20507401/) | 2010 | Pilot RCT | The Journal of Dermatology | A controlled, double-blind randomized pilot trial evaluating oral ciprofloxacin as an antifibrotic agent in scleroderma patients. Assessed whether ciprofloxacin reduces severity of skin fibrosis; results were preliminary with a small sample size. |
| [7728404](https://pubmed.ncbi.nlm.nih.gov/7728404/) | 1995 | Clinical Observation | British Journal of Rheumatology | Investigated small bowel bacterial overgrowth (SIBO) in 24 systemic sclerosis patients with malabsorption symptoms. Treatment with antibiotics including ciprofloxacin was assessed; supports the SIBO-indirect mechanism pathway rather than direct anti-scleroderma efficacy. |

---

## Philippines Market Information

Ciprofloxacin currently has **no registered licenses** with the Philippine FDA (Food and Drug Administration). It is not an approved marketed product in the Philippines at this time.

---

## Safety Considerations

Please refer to the package insert for complete safety information. Key safety considerations known from the broader literature include:

- **Black Box Warning (FDA, 2016)**: Ciprofloxacin carries a US FDA black box warning for peripheral neuropathy (potentially permanent), tendinitis and tendon rupture, central nervous system effects, and exacerbation of myasthenia gravis. These warnings are particularly relevant given that scleroderma patients may already have underlying neuropathic or musculoskeletal complications.
- **Drug Interactions**: Full DDI profile was not available in the current data set. Fluoroquinolones are known to interact with QT-prolonging agents, antacids (reduced absorption), and anticoagulants such as warfarin. A formal DDI review should be conducted before any clinical use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence for ciprofloxacin in diffuse scleroderma is limited to one small pilot RCT and one indirect observational study (SIBO context), placing this candidate firmly at the preclinical/early exploratory stage (L4). With no registered clinical trials and a mechanistic rationale that is indirect, the evidence base is insufficient to justify clinical translation at this time.

**To proceed, the following is needed:**
- Retrieve and review the full results of PMID 20507401 (the 2010 pilot RCT) to assess effect size, sample size, and primary endpoint outcomes.
- Conduct dedicated in vitro and in vivo studies to confirm anti-fibrotic activity of ciprofloxacin at clinically achievable plasma concentrations.
- Obtain complete MOA data from DrugBank (currently listed as data gap) to better characterize ciprofloxacin's off-target pharmacology.
- Clarify whether SIBO-mediated pathway or direct anti-fibrotic pathway is the primary hypothesized mechanism before designing any proof-of-concept study.
- Review the Philippine FDA registration pathway: as the drug is currently not marketed locally, regulatory strategy (new indication filing vs. compassionate use) must be defined.
- Conduct a formal safety review with a focus on the black box warning profile, particularly peripheral neuropathy risk in a patient population with potential pre-existing neuropathic features.

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any therapeutic application. Results generated by the TxGNN computational model must be interpreted in the context of supporting clinical and biological evidence.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

