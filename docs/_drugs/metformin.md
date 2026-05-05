---
layout: default
title: Metformin
parent: 僅模型預測 (L5)
nav_order: 178
evidence_level: L5
indication_count: 5
---

# Metformin
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

Using the `txgnn-pipeline` skill confirmed context. Now generating the report from the Evidence Pack:

---

# Metformin: From Type 2 Diabetes to Focal Stiff Limb Syndrome

## One-Sentence Summary

Metformin is a biguanide antidiabetic agent and the most widely prescribed first-line therapy for type 2 diabetes mellitus worldwide.
The TxGNN model predicts it may be effective for **Focal Stiff Limb Syndrome**, a rare autoimmune neurological condition;
however, **no clinical trials** and **no published literature** currently support this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Type 2 diabetes mellitus (first-line biguanide antidiabetic) |
| Predicted New Indication | Focal Stiff Limb Syndrome |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Metformin is a biguanide compound whose primary mechanism involves activation of AMP-activated protein kinase (AMPK). Through this pathway, it suppresses hepatic glucose production and improves peripheral insulin sensitivity—the basis for its decades-long efficacy in type 2 diabetes. Crucially, AMPK activation also inhibits mTORC1 signaling, which carries downstream immunomodulatory consequences: mTOR suppression shifts the Treg/Th17 immune balance and attenuates NF-κB-driven pro-inflammatory responses. This broader immunological footprint is likely what the TxGNN model is detecting.

Focal stiff limb syndrome is a localized variant of stiff person syndrome (SPS), a rare autoimmune neurological disorder in which anti-GAD65 (glutamic acid decarboxylase 65) or anti-amphiphysin antibodies impair GABAergic interneuron function, producing involuntary rigidity confined to one or a few limbs. The theoretical bridge is that metformin's AMPK→mTORC1 immunomodulation could in principle reduce autoantibody-driven neuronal inhibition by reshaping the aberrant immune response.

In practice, however, this link is highly indirect. Metformin does not act on GAD65 autoantibodies, the GABA system, or the spinal interneuron circuitry that is the actual site of pathology. Established treatments—diazepam, baclofen, IVIG, and rituximab—address the condition far more specifically. No preclinical or clinical work has explored this hypothesis. The TxGNN signal is best interpreted as a bioinformatic lead requiring biological plausibility validation before any clinical consideration.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

Currently no related literature available.

---

## Philippines Market Information

Metformin carries **zero product authorizations** with the Philippine FDA at the time of this report. No registration table can be generated. This is notable given that metformin is one of the most widely registered drugs globally; the absence from the Philippine registry warrants independent verification before drawing conclusions about local availability.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **⚠️ Cross-indication safety signal identified in this Evidence Pack:**
> Among the top-5 predicted indications, **thiamine-responsive dysfunction syndrome (TRMA, rank 4)** raises a specific and serious safety concern: metformin inhibits mitochondrial respiratory chain Complex I and has been documented to reduce thiamine absorption—potentially via competitive interference at SLC19A2/SLC19A3 transporters. TRMA patients carry loss-of-function mutations in SLC19A2, meaning any further impairment of thiamine transport by metformin could be hazardous. This finding does not directly affect the focal stiff limb syndrome assessment, but it should inform the overall repurposing risk profile for metformin across rare diseases.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Evidence level L5 means this is a computational prediction only—there are no clinical trials, observational data, or published literature connecting metformin to focal stiff limb syndrome. The mechanistic rationale (AMPK immunomodulation vs. anti-GAD65 autoimmunity) is too indirect to justify advancing without foundational preclinical validation, especially when well-established targeted therapies already exist for this indication.

**To proceed, the following is needed:**
- Retrieve metformin's full mechanism of action from DrugBank (DB00331) to confirm the AMPK→Treg/Th17 axis detail
- Verify Philippine FDA registration status for metformin directly via the FDA Philippines eRegistration portal
- Conduct a targeted literature search for metformin in stiff person syndrome models or anti-GAD65 autoimmune contexts (broader than the focal limb variant)
- Evaluate preclinical evidence of AMPK activation on GABAergic interneuron function or autoantibody suppression before any clinical hypothesis generation
- Resolve the thiamine safety concern (DG001/DG002 data gaps) before applying metformin in any mitochondrial or transporter-related rare disease context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

