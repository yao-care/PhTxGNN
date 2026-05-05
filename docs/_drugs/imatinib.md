---
layout: default
title: Imatinib
parent: 僅模型預測 (L5)
nav_order: 170
evidence_level: L5
indication_count: 10
---

# Imatinib
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

The txgnn-pipeline skill confirms this is a standard TxGNN report-generation task. Proceeding with the Evidence Pack now.

---

# Imatinib: From CML / GIST to Heart Fibrosarcoma

## One-Sentence Summary

Imatinib is a first-in-class small-molecule tyrosine kinase inhibitor (TKI) originally developed and globally approved for chronic myeloid leukaemia (CML) and gastrointestinal stromal tumours (GIST), targeting BCR-ABL, c-KIT, and PDGFR kinases.
The TxGNN model places **heart fibrosarcoma** as its top-ranked novel prediction (score: 99.94%), currently supported by **0 clinical trials** and **1 publication** — a mechanistically plausible but evidence-poor signal.
Notably, the second-ranked prediction — **fibroblastic neoplasm (DFSP)** — carries Level 2 evidence and existing FDA/EMA approvals, and represents a more immediately actionable repurposing pathway for the Philippines.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic Myeloid Leukaemia (CML) / Gastrointestinal Stromal Tumour (GIST) |
| Predicted New Indication | Heart Fibrosarcoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not formally available in this evidence pack. Based on published literature embedded in the evidence, Imatinib (Gleevec/Glivec, Novartis) is a potent small-molecule inhibitor of three receptor tyrosine kinases: BCR-ABL (the constitutively active kinase driving CML), c-KIT (the primary oncogenic driver in GIST), and PDGFR-α/β (platelet-derived growth factor receptors). This multi-target profile has been clinically validated across haematological malignancies and solid tumours, and provides the mechanistic foundation for exploring activity wherever these kinases are pathologically activated.

Heart fibrosarcoma is an ultra-rare primary cardiac malignancy, accounting for fewer than 5% of all primary cardiac malignant tumours. The proposed mechanistic link to Imatinib rests on the hypothesis that cardiac fibrosarcoma cells may express PDGFR-β — the same kinase targeted in dermatofibrosarcoma protuberans (DFSP), where Imatinib's IC₅₀ is approximately 0.1 nM. This is an extrapolation from better-characterised PDGFR-driven fibrosarcomas. No PDGFR expression data specific to heart fibrosarcoma has been published, and no clinical experience with Imatinib in this tumour entity exists.

The TxGNN model's high prediction score most likely reflects the model learning the general Imatinib–fibrosarcoma–PDGFR relationship from training data and generalising it across anatomical sites. Without biomarker-driven patient selection (e.g., confirmed PDGFR+ expression on tumour biopsy), this prediction cannot be translated to clinical practice. It is best treated as a hypothesis requiring prospective validation.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for heart fibrosarcoma.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18623899](https://pubmed.ncbi.nlm.nih.gov/18623899/) | 2008 | Editorial / Commentary | Prescrire International | Reviews Imatinib's expanding approved indications (CML, Ph+ALL, GIST). Notes superior haematological response rate vs chemotherapy in a 55-patient Ph+ALL trial. **No heart fibrosarcoma-specific data.** |

---

## Philippines Market Information

Imatinib currently has **no registered products** with the FDA Philippines. There are no active FR-number licenses on record for this drug. Any use in the Philippines would require importation under a compassionate special permit or individual patient access program.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Tyrosine kinase inhibitor (BCR-ABL / c-KIT / PDGFR class); not a conventional cytotoxic |
| Myelosuppression Risk | Moderate — neutropenia, thrombocytopenia, and anaemia are commonly reported, particularly in CML patients; severity is dose-dependent |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (weekly × 4 weeks, then monthly), liver function (ALT/AST/bilirubin), renal function, body weight and fluid balance (risk of peripheral oedema and pleural/pericardial effusion) |
| Handling Protection | Standard oral cytotoxic precautions apply; tablets should not be crushed or split without PPE; avoid inhalation of powder |

---

## Safety Considerations

Please refer to the package insert for safety information. No Philippines-specific label data or DDI records are available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold** *(for heart fibrosarcoma as the primary indication)*

**Rationale:**
Heart fibrosarcoma is an ultra-rare malignancy with zero registered clinical trials and only one tangentially related publication. The mechanistic link is entirely inferential, and the TxGNN high score reflects model generalisation from PDGFR-driven fibrosarcoma data rather than any disease-specific evidence. Proceeding without biomarker confirmation and a formal case series would not meet minimum evidentiary standards for clinical development.

---

**⚠ Higher-Priority Finding in This Evidence Pack**

The **#2-ranked prediction — fibroblastic neoplasm / Dermatofibrosarcoma Protuberans (DFSP)** — carries substantially stronger evidence and warrants immediate follow-up:

- **Evidence level L2**: One completed Phase 2 trial (NCT00085475, n=17), supported by the 2024 EADO European Clinical Practice Guideline (PMID 39904126) and multiple systematic reviews confirming Imatinib's role in unresectable/metastatic DFSP
- **Regulatory precedent**: Imatinib is already FDA- and EMA-approved for unresectable/metastatic DFSP based on the COL1A1-PDGFB fusion protein mechanism
- **Philippines gap**: Imatinib has zero registrations in the Philippines — this represents a direct regulatory filing opportunity

---

**To proceed on heart fibrosarcoma, the following is needed:**
- PDGFR-α/β immunohistochemistry (IHC) profiling from cardiac fibrosarcoma tumour specimens
- Compassionate-use case data or enrolment in a multi-centre rare cardiac tumour registry
- Cardiac oncology specialist consultation, given extreme rarity and the complexity of surgical and multimodal management

**To pursue fibroblastic neoplasm / DFSP (recommended priority action):**
- Initiate Philippines FDA registration filing, leveraging the FDA and EMA DFSP-approved label as regulatory precedent
- Engage dermatology and surgical oncology centres in the Philippines for patient identification (DFSP incidence ~1–4 per million/year)
- Reference 2024 EADO DFSP Guideline ([PMID 39904126](https://pubmed.ncbi.nlm.nih.gov/39904126/)) and NCCN Soft Tissue Sarcoma Guidelines for clinical protocols
- Obtain Imatinib mechanism of action and full safety data via DrugBank API (DrugBank ID: DB00619) to complete a full S1 safety assessment before submission
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

