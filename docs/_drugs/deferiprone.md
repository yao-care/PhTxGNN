---
layout: default
title: Deferiprone
parent: 僅模型預測 (L5)
nav_order: 98
evidence_level: L5
indication_count: 9
---

# Deferiprone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **9** 個
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

# Deferiprone: From Iron Overload to Hepatic Porphyria

## One-Sentence Summary

Deferiprone is an oral iron chelator established for the treatment of transfusional iron overload, particularly in patients who cannot adequately be treated with deferoxamine.
The TxGNN model predicts it may be effective for **Hepatic Porphyria**, with **0 clinical trials** and **2 publications** currently supporting this direction — including one animal study that directly tested deferiprone in a porphyria cutanea tarda murine model.
Evidence is preclinical in nature (L4), and clinical validation is required before any advancement.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Transfusional iron overload (no Taiwan registration found) |
| Predicted New Indication | Hepatic Porphyria |
| TxGNN Prediction Score | 99.20% |
| Evidence Level | L4 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold (Research Question) |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in this evidence pack. Based on known pharmacology, Deferiprone (L1) is a bidentate oral iron chelator that binds free iron (Fe³⁺) in a 3:1 stoichiometric ratio, forming stable hexadentate complexes excreted in the urine. Its oral bioavailability and particularly strong cardiac iron mobilization distinguish it from parenteral chelators such as deferoxamine.

Hepatic porphyria encompasses a family of metabolic disorders in which defects in the heme biosynthesis pathway cause pathological accumulation of porphyrin precursors — most critically in the liver. Critically, free iron (Fe²⁺) participates in Fenton chemistry, generating reactive oxygen species (ROS) that amplify photo-oxidative damage and potentiate porphyrin toxicity in hepatocytes. By reducing the labile iron pool, iron chelation theoretically interrupts this vicious cycle of oxidative stress and porphyrin accumulation.

The mechanistic link is biologically plausible but indirect. It is most directly demonstrated in porphyria cutanea tarda (PCT), the most common hepatic porphyria, where iron overload is a recognised pathogenic co-factor and phlebotomy (iron depletion) is an established first-line treatment. The 2007 murine study in the evidence set (PMID 17854053) directly compared deferiprone-mediated iron chelation against iron-deficient diets in Hfe⁻/⁻ mice, providing the closest available mechanistic bridge to a clinical hypothesis.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Deferiprone × Hepatic Porphyria.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [32678895](https://pubmed.ncbi.nlm.nih.gov/32678895/) | 2020 | Clinical Study / Case Series | *Blood* | Iron chelation rescued hemolytic anemia and skin photosensitivity in congenital erythropoietic porphyria (CEP); demonstrates that reducing iron availability can mitigate porphyrin-driven tissue damage |
| [17854053](https://pubmed.ncbi.nlm.nih.gov/17854053/) | 2007 | Animal Study (Murine Model) | *Hepatology* | Deferiprone (L1) reduced hepatic uroporphyrin accumulation in Hfe⁻/⁻ ALA-fed mice to a degree comparable to iron-deficient diet; directly demonstrates deferiprone's activity in a porphyria cutanea tarda model |

---

## Taiwan Market Information

Deferiprone currently holds **no product registrations** with the Taiwan FDA. There are no licensed products, dosage forms, or approved indications on record. This represents a significant regulatory gap for any clinical or commercial development pathway in Taiwan.

---

## Safety Considerations

Taiwan FDA package insert warnings and contraindications data are not available in this evidence pack (Data Gap: DG001, classified as Blocking severity). Drug interaction data was queried but returned no results.

> Please refer to the official package insert for complete safety information, including the well-established risk of agranulocytosis/neutropenia associated with deferiprone — a class-specific black-box warning requiring mandatory weekly blood count monitoring.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The hepatic porphyria prediction rests on a biologically coherent but indirect mechanistic hypothesis supported only by preclinical and case series data (L4); no clinical trials exist for this specific indication, and the drug lacks any Taiwan regulatory footprint. Additionally, a critical safety data gap (TFDA package insert) remains unresolved and must be addressed before any further evaluation stage.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Obtain and parse the official TFDA package insert PDF to extract warnings, contraindications, and monitoring requirements — this is prerequisite to entering safety pre-screening (S1)
- **Resolve DG002 (High):** Retrieve full mechanism of action data from DrugBank API to complete the mechanistic plausibility analysis
- **Pilot clinical hypothesis:** Conduct a structured literature review specifically for porphyria cutanea tarda + iron chelation (broader than deferiprone alone) to assess whether the mechanistic link warrants a dedicated prospective study
- **Consider secondary indication:** Beta-thalassemia with other manifestations (Rank 8, L3, "Proceed with Guardrails") has stronger existing evidence — if a Taiwan development pathway is sought, this indication may offer a more viable near-term path given deferiprone's well-established role in transfusional iron overload management in thalassemia

> ⚠️ This report is for research reference only and does not constitute medical advice. All repurposing candidates require clinical validation before any application.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

