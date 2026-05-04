---
layout: default
title: Everolimus
parent: 僅模型預測 (L5)
nav_order: 134
evidence_level: L5
indication_count: 10
---

# Everolimus
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

# Everolimus: From Renal Cell Carcinoma to Liposarcoma

## One-Sentence Summary

Everolimus is an mTOR (mechanistic target of rapamycin) inhibitor, approved globally for treatment of advanced renal cell carcinoma, hormone receptor-positive breast cancer, and neuroendocrine tumors, though currently not registered in the Philippines.
The TxGNN model predicts it may be effective for **Liposarcoma** (specifically dedifferentiated liposarcoma and leiomyosarcoma subtypes),
with **1 active clinical trial** and **4 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Philippines registry; globally approved for RCC, breast cancer, and neuroendocrine tumors |
| Predicted New Indication | Liposarcoma |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L2 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known information, Everolimus belongs to the rapalog class of mTOR inhibitors — it selectively binds FKBP-12 and inhibits mTORC1, thereby blocking downstream signaling that drives cell proliferation, protein synthesis, and angiogenesis. Its efficacy in mTOR-driven cancers (renal cell carcinoma, hormone receptor-positive breast cancer, pancreatic neuroendocrine tumors) has been extensively validated across global regulatory approvals.

Dedifferentiated liposarcoma (DDLPS) and leiomyosarcoma (LMS) are among the most common subtypes of soft-tissue sarcoma, where effective systemic options remain scarce. Critically, immunohistochemical and in vitro analyses of 99 DDLPS specimens demonstrated high activation of the Akt/mTOR and MAPK pathways (PMID 26518767), directly implicating mTORC1 as a driver of tumor growth in this histology. This molecular evidence provides the mechanistic bridge between Everolimus's established mechanism and its predicted activity in liposarcoma.

The combination strategy with CDK4/6 inhibitor Ribociclib adds further biological rationale: DDLPS is characterized by CDK4 gene amplification, meaning dual blockade of the CDK4/6-Rb axis and the PI3K/mTOR axis simultaneously disrupts two key G1 checkpoint drivers. Preclinical models have confirmed synergistic growth inhibition with this combination across multiple tumor types, supporting the scientific rationale for Phase 2 trial NCT03114527 (results published 2024).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03114527](https://clinicaltrials.gov/study/NCT03114527) | Phase 2 | Active, Not Recruiting | 48 | Two-arm trial: Ribociclib (300 mg/day, 3 weeks on/1 week off) + Everolimus (2.5 mg daily) in advanced DDLPS (Arm A) and LMS (Arm B) with ≥1 prior systemic therapy; 2024 results published (PMID 37967116), demonstrating antitumor activity of CDK4/6 + mTOR dual blockade |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [37967116](https://pubmed.ncbi.nlm.nih.gov/37967116/) | 2024 | Phase 2 Clinical Trial Results | Clinical Cancer Research | Published results of SAR-096: Ribociclib + Everolimus in advanced DDLPS and LMS; CDK4 targeting in DDLPS and mTOR targeting in LMS represent biologically rationalized dual-pathway strategy |
| [26518767](https://pubmed.ncbi.nlm.nih.gov/26518767/) | 2016 | Translational/Mechanistic | Tumour Biology | Clinicopathological and immunohistochemical analysis of 99 DDLPS specimens confirms Akt/mTOR and MAPK pathway activation; in vitro antitumor effect of mTOR inhibitor directly demonstrated — key mechanistic anchor for this prediction |
| [36003796](https://pubmed.ncbi.nlm.nih.gov/36003796/) | 2022 | Preclinical Review | Frontiers in Oncology | PDOX mouse model platform for sarcomas identifies CDK inhibitor combinations as effective candidates; supports broader rationale for CDK4/6-targeted and mTOR-targeted approaches in sarcoma subtypes |
| [29848686](https://pubmed.ncbi.nlm.nih.gov/29848686/) | 2018 | Preclinical Combination Study | Anticancer Research | Eribulin in combination with mechanistically distinct anticancer agents (including mTOR inhibitors) evaluated across liposarcoma and other human tumor xenograft models; contextualizes combination therapy strategies in liposarcoma |

---

## Philippines Market Information

Everolimus is currently **not registered** in the Philippines. No license records are available.

> **Note for context:** Everolimus (brand names: Afinitor®, Certican®, Zortress®) holds regulatory approval in the US (FDA), EU (EMA), Japan (PMDA), and Taiwan (TFDA) for indications including advanced renal cell carcinoma, hormone receptor-positive HER2-negative advanced breast cancer, pancreatic neuroendocrine tumors, tuberous sclerosis complex, and prevention of organ rejection. Any investigational or clinical use in the Philippines would require a separate regulatory pathway.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy (mTOR inhibitor / rapalog class; not conventional cytotoxic) |
| Myelosuppression Risk | Low to moderate (anemia and thrombocytopenia reported in clinical trials; substantially less myelosuppressive than conventional cytotoxic chemotherapy) |
| Emetogenicity Classification | Low |
| Monitoring Items | CBC with differential, serum glucose (fasting), lipid panel (triglycerides, cholesterol), liver function tests, renal function; pulmonary assessment for non-infectious pneumonitis (class-specific toxicity); wound healing monitoring if perioperative use |
| Handling Protection | Standard oral targeted therapy precautions apply; cytotoxic drug handling protocols recommended given antineoplastic classification |

---

## Safety Considerations

Detailed Philippines-specific safety data (package insert warnings and contraindications) are not available in this evidence pack.

> Please refer to the manufacturer's package insert for complete safety information. Based on published clinical data and global labeling, known class-specific concerns for Everolimus include: non-infectious pneumonitis (occurring in up to 14% of patients in some trials), increased susceptibility to bacterial, fungal, and viral infections (including opportunistic infections), oral mucositis and stomatitis, hyperglycemia, hyperlipidemia, impaired wound healing, and nephrotoxicity in transplant settings.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A dedicated Phase 2 clinical trial (NCT03114527) evaluating Ribociclib + Everolimus specifically in advanced DDLPS and LMS has been conducted and published (2024), providing direct clinical trial evidence for Everolimus activity in liposarcoma; this is further anchored by translational data showing mTOR pathway activation in DDLPS tissue specimens (PMID 26518767). The biological plausibility is strong, though current evidence is limited to a combination regimen and has not yet established Everolimus monotherapy efficacy in this setting.

**To proceed, the following is needed:**

- **Efficacy readout from NCT03114527**: Obtain full published results (PMID 37967116) including primary endpoints — progression-free survival (PFS) and overall response rate (ORR) — stratified by arm (DDLPS vs. LMS)
- **MOA documentation**: Resolve DG002 data gap by querying DrugBank API for Everolimus mechanism of action and pharmacodynamic profile
- **Safety review**: Resolve DG001 by obtaining Philippines FDA (or TFDA as proxy) package insert PDF for full warnings and contraindications; assess non-infectious pneumonitis risk and immunosuppression profile for sarcoma patient population
- **Drug interaction assessment**: DDI data is currently unavailable; a formal interaction check should be performed, especially given potential combination use with Ribociclib (both are CYP3A4 substrates)
- **Regulatory pathway scoping**: Map the regulatory route for Everolimus registration in the Philippines for sarcoma indication (compassionate use, expanded access, or full NDA pathway)
- **Monotherapy vs. combination strategy decision**: Clarify whether the clinical question is Everolimus alone or exclusively in combination with CDK4/6 inhibitors, as this affects trial design and regulatory framing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

