---
layout: default
title: Methotrexate
parent: 僅模型預測 (L5)
nav_order: 179
evidence_level: L5
indication_count: 10
---

# Methotrexate
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

The system prompt defines my role precisely as a drug repurposing report writer for this Evidence Pack — this is a subagent execution context. Proceeding directly with report generation.

---

# Methotrexate: From Oncology & Autoimmune Diseases to Pulmonary Blastoma

## One-Sentence Summary

Methotrexate is a globally established antifolate antimetabolite with decades of proven use across multiple cancers (leukemia, lymphoma, osteosarcoma) and autoimmune diseases (rheumatoid arthritis, psoriasis), though it currently holds no marketing registration in the Philippines.
The TxGNN model predicts it may be effective for **Pulmonary Blastoma**, achieving a prediction score of **99.45%**, yet this direction is currently supported by **no clinical trials** and **no published literature**.
This remains a computational model-only prediction without corroborating clinical or preclinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines; globally established for leukemia, lymphoma, osteosarcoma, rheumatoid arthritis, and psoriasis |
| Predicted New Indication | Pulmonary Blastoma |
| TxGNN Prediction Score | 99.45% |
| Evidence Level | L5 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data for Methotrexate was not retrieved in this Evidence Pack. Based on established pharmacological knowledge, Methotrexate acts as a competitive inhibitor of dihydrofolate reductase (DHFR), blocking the conversion of dihydrofolate to tetrahydrofolate. This disrupts the de novo biosynthesis of purines and thymidylate, effectively halting DNA replication in rapidly proliferating cells. This mechanism underpins its broad antitumor activity across diverse cancer types and its anti-inflammatory efficacy at lower doses via adenosine-dependent immunomodulation.

Pulmonary blastoma is a rare biphasic lung malignancy containing both epithelial and mesenchymal components that histologically resemble fetal lung tissue at 16–18 weeks of gestation. In principle, MTX's DHFR inhibition could exert antiproliferative effects on the rapidly cycling embryonal-type tumor cells present in this tumor. The TxGNN knowledge graph score of 0.9945 reflects indirect connections between broad-spectrum antitumor agents and rare lung malignancies captured during model training.

However, pulmonary blastoma is an exceedingly rare disease (annual incidence <1 per million), and no preclinical studies or clinical trials have specifically investigated MTX in this setting. The high prediction score reflects pattern recognition within the knowledge graph — an indirect association — rather than a direct biological or clinical signal. This prediction should be interpreted with caution and is best treated as a hypothesis-generating output.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Methotrexate in Pulmonary Blastoma.

---

## Literature Evidence

Currently no related literature available for Methotrexate in Pulmonary Blastoma.

---

## Philippines Market Information

Methotrexate is currently not registered with the Food and Drug Administration (FDA) Philippines. No marketing authorizations, product licenses, or approved indications are on record. This means there is no established local regulatory pathway or approved labeling to reference for this drug in the Philippines context.

---

## Cytotoxicity

Methotrexate is a conventional cytotoxic chemotherapeutic agent (folate antagonist class) with well-documented antineoplastic activity.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Antifolate / Folate antagonist (not a targeted therapy or immunotherapy) |
| Myelosuppression Risk | High — Bone marrow suppression is dose-dependent and cumulative; leukopenia, neutropenia, thrombocytopenia, and anemia are well-documented, particularly at intermediate-to-high doses (≥100 mg/m²) |
| Emetogenicity Classification | Low to moderate — Low emetogenic potential at standard doses; increases to moderate at high-dose regimens (≥500 mg/m²) |
| Monitoring Items | CBC with differential (weekly during induction, then periodically), serum creatinine and BUN (MTX is renally cleared; nephrotoxicity delays elimination), liver function tests (ALT, AST, albumin, bilirubin), serum MTX levels with leucovorin rescue timing (mandatory for high-dose protocols), mucositis surveillance |
| Handling Protection | Must follow cytotoxic drug handling regulations (classified as a NIOSH Hazardous Drug, Group 1); double-glove PPE, closed-system drug transfer devices (CSTD), and biosafety cabinet preparation are required |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Pulmonary blastoma is an extremely rare malignancy (incidence <1/million/year) with zero published clinical or preclinical evidence supporting Methotrexate use; the high TxGNN score of 99.45% reflects indirect knowledge graph associations rather than any direct mechanistic or clinical signal specific to this disease.

**To proceed, the following is needed:**
- **Preclinical studies**: In vitro cytotoxicity testing of MTX against pulmonary blastoma cell lines; in vivo xenograft efficacy evaluation
- **Mechanistic characterization**: Confirm DHFR expression levels and folate pathway dependency in pulmonary blastoma tumor biology (comparative to sensitive tumor types)
- **Safety data retrieval**: Obtain and review the full package insert (DHFR inhibitor class warnings, contraindications, key drug-drug interactions) from DrugBank API or WHO source documents
- **Philippines regulatory pathway**: Assess FDA Philippines registration requirements and feasibility for a drug with no current local authorization
- **Rare tumor network linkage**: Given the disease rarity, consider engagement with international rare lung tumor registries or basket trial frameworks (e.g., NCI-MATCH, TAPISTRY) rather than a standalone disease-specific trial design

> **Research Note for Context:** While pulmonary blastoma (rank 1) is the top-scored TxGNN prediction, two other predicted indications carry substantially stronger clinical evidence — **Primary Pulmonary Lymphoma** (rank 2, L3 evidence, 12 trials, 20 publications) and **Hodgkin's Lymphoma** (rank 5, L2 evidence, recommendation: *Proceed with Guardrails*) — both supported by HD-MTX containing regimens with published Phase II/III data. These may represent more actionable repurposing targets if the research team wishes to pursue the Philippines drug access agenda for Methotrexate.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

