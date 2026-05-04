---
layout: default
title: Chloroquine
parent: 僅模型預測 (L5)
nav_order: 71
evidence_level: L5
indication_count: 4
---

# Chloroquine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

# Chloroquine: From Malaria to RF-Positive Polyarticular Juvenile Idiopathic Arthritis

## One-Sentence Summary

Chloroquine is a classic antimalarial agent and disease-modifying antirheumatic drug (DMARD), historically used to treat malaria and certain autoimmune conditions including rheumatoid arthritis.
The TxGNN model predicts it may be effective for **Rheumatoid Factor-Positive Polyarticular Juvenile Idiopathic Arthritis (RF+ pJIA)**,
with **0 clinical trials** and **2 publications** currently providing indirect supporting evidence for this specific subtype.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malaria (no Philippines registration on file) |
| Predicted New Indication | Rheumatoid factor-positive polyarticular juvenile idiopathic arthritis |
| TxGNN Prediction Score | 99.41% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence package. Based on established pharmacology, chloroquine is a lysosomotropic compound that interferes with endosomal/lysosomal function. Its immune-modulating effects include: (1) inhibition of TLR7/TLR9 innate signaling, which reduces type I interferon and pro-inflammatory cytokine production; (2) impairment of lysosomal acidification, which disrupts MHC class II antigen presentation and downstream T-cell activation; and (3) direct suppression of TNF-α, IL-1β, and IL-6, the core cytokines driving chronic synovitis.

RF-positive polyarticular JIA is the JIA subtype most closely resembling adult seropositive rheumatoid arthritis — both are driven by B-cell autoantibody production (rheumatoid factor), sustained synovial inflammation, and progressive joint destruction. Chloroquine's multi-target immune profile mechanistically overlaps with the pathogenesis of this subtype, which is why the TxGNN model assigns a high prediction score.

It is important to note, however, that the analogue drug hydroxychloroquine (HCQ) — not chloroquine — is more commonly referenced in the JIA literature. No clinical studies directly evaluate chloroquine in RF+ polyarticular JIA specifically. Additionally, the broader evidence pack reveals stronger historical support for chloroquine in the closely related indication of **juvenile chronic polyarthritis** (Evidence Level L3; see PMID 1688268, a comparative trial of chloroquine vs. sulphasalazine in JCA), suggesting the TxGNN model is capturing a mechanistically coherent signal across related arthritis subtypes, even though RF+ pJIA itself lacks direct clinical data.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for this specific indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [24334641](https://pubmed.ncbi.nlm.nih.gov/24334641/) | 2014 | Prospective Observational | The Journal of Rheumatology | Long-term real-world experience with leflunomide in JIA patients; provides context for DMARD use in JIA, but does not directly evaluate chloroquine in this subtype |
| [8627446](https://pubmed.ncbi.nlm.nih.gov/8627446/) | 1996 | Case Report/Series | The Journal of Pediatrics | Two RF+ polyarticular JRA patients developed MTX-induced accelerated nodulosis; nodule progression was arrested by addition of hydroxychloroquine — indirect evidence supporting antimalarial use in this specific JIA subtype |

---

## Philippines Market Information

Chloroquine is currently not registered or marketed in the Philippines. No license records are available in the FDA Philippines database.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked predicted indication (RF+ polyarticular JIA) lacks any direct clinical trial evidence for chloroquine and is supported by only 2 indirectly relevant publications. Furthermore, chloroquine is not registered in the Philippines, creating a significant regulatory barrier before any clinical application could be considered.

**To proceed, the following is needed:**

- **MOA data gap closure**: Retrieve mechanism of action details from DrugBank (DB00608) to support pharmacological plausibility analysis
- **Safety data gap closure**: Download and parse the TFDA package insert PDF to obtain warnings, contraindications, and drug interactions — currently classified as a Blocking data gap
- **Direct clinical evidence**: Identify or commission studies specifically evaluating chloroquine (not only HCQ) in RF+ polyarticular JIA; existing evidence is based on the broader antimalarial class
- **Analogue comparison**: Evaluate whether hydroxychloroquine, which has a comparable mechanism and substantially broader evidence base in JIA, could serve as a more feasible repurposing candidate for this indication
- **Regulatory pathway**: If clinical development is pursued, a Philippines FDA registration strategy for chloroquine must be established prior to any interventional study
- **Cross-indication review**: The related indications in this pack — particularly **juvenile chronic polyarthritis** (L3 evidence, "Proceed with Guardrails") — carry meaningfully stronger direct support for chloroquine and may represent a more actionable starting point for repurposing evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

