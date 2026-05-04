---
layout: default
title: Etoposide
parent: 僅模型預測 (L5)
nav_order: 133
evidence_level: L5
indication_count: 10
---

# Etoposide
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

# Etoposide: From Germ Cell Tumors & Lymphomas to Well-Differentiated Fetal Adenocarcinoma of the Lung

## One-Sentence Summary

Etoposide is a well-established cytotoxic chemotherapy agent belonging to the epipodophyllotoxin class, with globally recognized use in germ cell tumors, lymphomas, and small cell lung cancer (SCLC), though it currently holds no registered indication in the Philippines.
The TxGNN model predicts it may be effective for **Well-Differentiated Fetal Adenocarcinoma of the Lung (WDFACL)**,
with **0 registered clinical trials** and **1 case report/review publication** currently available to support this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines FDA registration (established global use: germ cell tumors, lymphomas, SCLC) |
| Predicted New Indication | Well-Differentiated Fetal Adenocarcinoma of the Lung |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not directly available in this evidence pack. Based on established pharmacological knowledge, Etoposide is a Topoisomerase IIα (Topo IIα) inhibitor that stabilizes the Topo IIα–DNA cleavage complex, causing DNA double-strand breaks and cell cycle arrest in the G2/M phase, ultimately triggering apoptosis in rapidly proliferating cells. Tumor cells exhibiting high Topo IIα expression—including many embryonic and fetal tumor types—are theoretically more susceptible to Etoposide-mediated cytotoxicity.

Well-Differentiated Fetal Adenocarcinoma of the Lung (WDFACL) is an extremely rare, low-grade primary lung malignancy within the pulmonary blastoma spectrum. It is pathologically defined by fetal-type glandular epithelium resembling embryonic lung tissue at approximately 10–16 weeks of gestation. Because WDFACL shares embryonic cellular characteristics with classic biphasic pulmonary blastoma and pleuropulmonary blastoma (PPB), Etoposide's ability to target Topo IIα in embryonically differentiated proliferating cells provides a plausible mechanistic rationale for cross-applicability. Etoposide-containing regimens (e.g., BEP, carboplatin/etoposide, CCNU-vincristine-VP16-cyclophosphamide) have appeared in individual case reports of classic biphasic pulmonary blastoma, lending indirect analogical support.

However, no clinical trials or prospective studies have directly evaluated Etoposide in WDFACL. The sole publication retrieved in this evidence pack involves classic biphasic pulmonary blastoma—a histologically related but distinct entity—and did not document Etoposide as the primary agent. The extreme rarity of WDFACL (estimated at far below 0.5% of primary lung malignancies) renders dedicated prospective trials essentially infeasible, and any clinical consideration would require careful extrapolation from related pulmonary blastoma spectrum entities.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for well-differentiated fetal adenocarcinoma of the lung.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33107372](https://pubmed.ncbi.nlm.nih.gov/33107372/) | 2020 | Case Report / Review | The Journal of International Medical Research | Describes a case of classic biphasic pulmonary blastoma — a spectrum entity closely related to WDFACL — in which the patient underwent right upper lobe resection followed by nedaplatin + paclitaxel adjuvant chemotherapy; upon disease recurrence, further treatment was administered. Authors emphasize the complete absence of standard treatment guidelines for pulmonary blastoma due to its extreme rarity, and review existing chemotherapy experiences in the literature. |

---

## Philippines Market Information

Etoposide currently holds **no registered product licenses** with the Philippines FDA (total registrations: 0, market status: Not Marketed). No authorization records are available for this drug in the Philippines.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Epipodophyllotoxin class (Topoisomerase IIα inhibitor) |
| Myelosuppression Risk | High — neutropenia and thrombocytopenia are the primary dose-limiting toxicities; leukocyte and platelet nadir typically occurs at days 7–14 post-administration |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | Complete blood count with differential (CBC-D), platelet count, liver function tests (ALT, AST, bilirubin), renal function (serum creatinine), serum albumin (affects protein binding and free drug exposure) |
| Handling Protection | Required — must be handled per cytotoxic drug handling regulations (gloves, protective gown, closed-system transfer, safe disposal of waste) |

---

## Safety Considerations

Please refer to the package insert for safety information. Formal safety data including Philippines FDA package insert warnings, contraindications, and drug-drug interaction profiles were not available in this evidence pack.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a high TxGNN prediction score (99.94%), the clinical evidence base for Etoposide in well-differentiated fetal adenocarcinoma of the lung is limited to a single case report on a related histological entity—classic biphasic pulmonary blastoma—without documented Etoposide use. The absence of any registered clinical trials and the extreme rarity of WDFACL place this repurposing hypothesis firmly at a preclinical/mechanistic level (L4), warranting deferral pending further evidence.

**Note on Broader Evidence Landscape:** While WDFACL (rank 1) holds a marginally higher TxGNN score, lower-ranked predicted indications in this evidence pack carry substantially stronger clinical evidence — particularly **Ewing sarcoma (rank 4, L1)** and **rhabdomyosarcoma (rank 6, L1)**, both of which have multiple completed Phase 3 RCTs directly validating Etoposide-containing regimens. These indications may be more actionable repurposing candidates and warrant separate dedicated evaluation reports.

**To proceed with the WDFACL hypothesis, the following is needed:**
- Mechanism of action (MOA) and target expression data from DrugBank API (data gap DG002)
- Philippines FDA safety data: package insert warnings, contraindications, and full drug interaction profile (data gap DG001)
- Systematic literature review of the complete pulmonary blastoma spectrum to identify all cases where Etoposide-containing regimens were employed, including pleuropulmonary blastoma and classic biphasic pulmonary blastoma subgroups
- Topo IIα expression profiling in WDFACL tumor samples as a predictive biomarker
- Expert consultation with thoracic oncologists regarding off-label use of Etoposide-based regimens in pulmonary blastoma spectrum tumors
- If single-institution case series data accumulate, consideration of a multi-histology basket trial design encompassing related rare pulmonary embryonal malignancies

---

> ⚠️ **Disclaimer:** This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before any clinical application. All therapeutic decisions should be based on formal clinical evidence and regulatory approval.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

