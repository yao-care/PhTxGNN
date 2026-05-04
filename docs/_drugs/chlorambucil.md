---
layout: default
title: Chlorambucil
parent: 僅模型預測 (L5)
nav_order: 69
evidence_level: L5
indication_count: 8
---

# Chlorambucil
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Chlorambucil: From Chronic Lymphocytic Leukemia to Pregerminal Center CLL/SLL

## One-Sentence Summary

Chlorambucil is a nitrogen mustard alkylating agent with a long-established role in treating chronic lymphocytic leukemia (CLL) and related hematologic malignancies, though it currently holds no marketing authorization in the Philippines.
The TxGNN model predicts it may be effective specifically for **Pregerminal Center CLL/SLL** (the IGHV-unmutated, poorer-prognosis molecular subtype), supported by **0 dedicated clinical trials** and **1 review publication** for this subtype — however, extensive broader CLL and lymphoma evidence exists in the global literature across the full prediction set.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Chronic lymphocytic leukemia and non-Hodgkin's lymphoma (established pharmacological use; no Philippines registration on record) |
| Predicted New Indication | Pregerminal Center CLL/SLL (IGHV-unmutated subtype) |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Chlorambucil is a bifunctional nitrogen mustard alkylating agent. Its cytotoxic mechanism involves forming covalent interstrand cross-links within the DNA double helix of lymphocytes, blocking replication and inducing programmed cell death. Because it preferentially accumulates in and targets B-lymphoid tissue, it is especially effective against slowly proliferating, indolent B-cell malignancies. For decades, chlorambucil was the gold-standard first-line treatment for CLL — a role now largely supplanted by BTK inhibitors (ibrutinib, acalabrutinib) and BCL-2 inhibitor-based regimens (venetoclax plus obinutuzumab), as confirmed by landmark Phase 3 trials using chlorambucil as the comparator arm.

Pregerminal center CLL/SLL refers specifically to the **IGHV-unmutated subtype** — B-cell clones that have not undergone somatic hypermutation in the immunoglobulin heavy chain variable region (< 2% IGHV mutation rate). This subtype is biologically distinct from its IGHV-mutated counterpart: it expresses ZAP-70, more frequently harbors adverse genomic features (del[17p], del[11q], TP53 mutation), and carries a significantly worse prognosis. Clinically, approximately 50% of CLL patients carry this subtype. At the cellular level, these pre-germinal center B cells remain susceptible to DNA alkylation in principle — chlorambucil's mechanism of action does not depend on IGHV mutation status.

The TxGNN prediction score of 99.72% reflects strong knowledge-graph connectivity between chlorambucil, B-cell lymphoid malignancies, and CLL molecular biology. However, this should be interpreted carefully: current clinical guidelines have moved decisively toward targeted agents (BTK inhibitors) for IGHV-unmutated CLL given their superior outcomes over chlorambucil-based chemoimmunotherapy. This prediction is therefore best read as a mechanistically plausible association rather than a suggestion of clinical superiority in modern practice. Detailed MOA data was not available in this evidence pack and should be retrieved from DrugBank to complete the mechanistic linkage analysis.

---

## Clinical Trial Evidence

Currently no clinical trials specifically targeting pregerminal center CLL/SLL (IGHV-unmutated subtype) with chlorambucil are registered on ClinicalTrials.gov or ICTRP.

> **Context note:** Multiple completed Phase 3 CLL trials have used chlorambucil as the comparator arm, confirming its established efficacy benchmark in CLL broadly. These include RESONATE-2 (ibrutinib vs. chlorambucil, NCT01722487), CAM307 (alemtuzumab vs. chlorambucil, NCT00046683), and the CLL11 trial (obinutuzumab + chlorambucil). Subgroup analyses from these trials stratified by IGHV mutation status — if available — would be the most direct source of evidence for this specific subtype.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12577769](https://pubmed.ncbi.nlm.nih.gov/12577769/) | 2003 | Review | Ned Tijdschr Geneeskd | One of the first publications identifying two biologically distinct CLL subtypes — the pre-germinal center (IGHV unmutated, ZAP-70+, poorer prognosis) and post-germinal center forms — and arguing for risk-adapted treatment approaches; disease-related morbidity affects ~50% of Stage A patients, with >25% dying of CLL-related causes |

---

## Philippines Market Information

Chlorambucil currently has **no marketing authorization in the Philippines**. No registration records are available. Should clinical use be contemplated, procurement would require special regulatory access pathways, such as a compassionate use application or a special import permit, subject to the approval of the Food and Drug Administration of the Philippines.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Nitrogen mustard / Alkylating agent class (bifunctional DNA cross-linker) |
| Myelosuppression Risk | High — Dose-limiting bone marrow suppression; neutropenia, thrombocytopenia, and anemia are common adverse effects; risk of cumulative and irreversible myelotoxicity with prolonged use; secondary AML and myelodysplastic syndrome (MDS) reported with long-term administration |
| Emetogenicity Classification | Low to moderate |
| Monitoring Items | CBC with differential (at least every 2 weeks during active treatment and at regular intervals thereafter), liver function tests, renal function; monitor for clinical or laboratory signs of secondary malignancies with long-term use |
| Handling Protection | Required — chlorambucil is classified as a Hazardous Drug (NIOSH Group 1 Antineoplastic); handle with appropriate PPE (double gloves, closed-front gown, eye/face protection); avoid skin and mucous membrane contact; prepare in a biological safety cabinet; dispose per cytotoxic waste regulations |

---

## Safety Considerations

No drug interaction data was retrievable from the current evidence pack. Based on the established pharmacological profile of chlorambucil, the following safety considerations apply:

- **Key Warnings**: Irreversible bone marrow suppression (dose-limiting toxicity); secondary malignancies including acute myeloid leukemia (AML) and myelodysplastic syndrome (MDS) with prolonged administration; CNS toxicity including focal and generalized seizures, particularly at high doses; hepatotoxicity (rare but reported).
- **Reproductive Toxicity**: Known teratogen (FDA Pregnancy Category D); causes infertility in both males (azoospermia) and females (premature ovarian failure); patients should be counseled on contraception and fertility preservation before initiating treatment.
- **Special Populations**: Use with extreme caution in patients with prior bone marrow suppression, active infections, or significantly impaired renal/hepatic function. Elderly patients are at higher risk for myelotoxicity.

> For complete contraindication and drug interaction information, the package insert of the specific product must be consulted. Retrieve the TFDA package insert PDF or equivalent to complete the safety dossier.

---

## Additional Predicted Indications — Overview

The TxGNN model generated 8 predictions for chlorambucil in this run. A brief summary is provided for clinical reference:

| Rank | Indication | TxGNN Score | Evidence Level | Recommendation | Notes |
|------|-----------|-------------|----------------|----------------|-------|
| 1 | Pregerminal Center CLL/SLL (IGHV unmutated) | 99.72% | L4 | Hold | Mechanistically plausible; modern treatment has moved to BTK inhibitors |
| 2 | CLL/SLL with IGHV somatic hypermutation (mutated subtype) | 99.72% | L4 | Hold | Better-prognosis subtype; historical chlorambucil response is higher in this group |
| 3 | ALK-positive large B-cell lymphoma | 99.61% | L5 | Hold | Aggressive, ALK-fusion-driven lymphoma; chlorambucil has no specific mechanistic rationale here |
| **4** | **Primary pulmonary lymphoma (MALT type)** | **99.42%** | **L3** | **Proceed with Guardrails** | **Most actionable new indication — clinical practice guidelines (PMID 18603558) explicitly list chlorambucil for extranodal NHL/MALT; Phase II data available** |
| 5 | Well-differentiated fetal adenocarcinoma of the lung | 99.39% | L5 | Hold | Epithelial tumor driven by Wnt/β-catenin; no biological rationale for B-cell-targeted alkylating agent |
| 6 | Pulmonary blastoma | 99.37% | L5 | Hold | Rare biphasic tumor; no mechanistic connection or supporting literature |
| 7 | Acute lymphoblastic leukemia (ALL) | 99.25% | L4 | Research Question | Chlorambucil not part of modern ALL protocols; clinical trial data listed is for CLL (misattribution) |
| 8 | Small cell lung carcinoma (SCLC) | 99.24% | L3 | Research Question | Historical Phase II data + novel 2026 chlorambucil-PIP conjugate study (PMID 41025286) targeting STMN1; warrants monitoring |

> **Highlight — Rank 4 (Primary Pulmonary Lymphoma / MALT):** This is the most clinically compelling "new indication" in the dataset. Pulmonary MALT lymphoma is an indolent low-grade B-cell malignancy — a biological profile highly consistent with chlorambucil's mechanism. Existing Italian hematology guidelines (2008) explicitly include chlorambucil as a treatment option for extranodal NHL including pulmonary MALT. A 1987 Phase II trial (PMID 3307632) confirmed partial remission in lymphoma subtypes. A decision to **Proceed with Guardrails** — requiring histological confirmation, multidisciplinary oncology review, and exclusion of infectious or autoimmune mimics — is justified.

---

## Conclusion and Next Steps

**Decision: Hold** (for Rank 1 — Pregerminal Center CLL/SLL; see Rank 4 for a more actionable pathway)

**Rationale:**
The IGHV-unmutated CLL/SLL subtype is supported by only a single 2003 review publication as direct subtype-specific evidence (L4). While the mechanistic rationale for chlorambucil in B-cell CLL is sound, modern clinical evidence strongly favors BTK inhibitors for this higher-risk subtype, and the drug is not registered in the Philippines. Pursuing this indication as a repurposing priority in the current clinical landscape would require robust justification against available targeted therapies.

**To proceed with any clinical pathway, the following is needed:**

- **MOA data**: Retrieve full mechanism of action from DrugBank (DB00291) to complete mechanistic scoring
- **Philippines package insert**: Download and parse the TFDA (or equivalent) monograph PDF to populate safety warnings and contraindications
- **IGHV-stratified subgroup data**: Extract subgroup analyses from RESONATE-2, CLL11, and CAM307 to quantify chlorambucil's specific response rate in the IGHV-unmutated vs. mutated subtypes
- **Philippines access pathway**: Assess feasibility of compassionate use or special import authorization given zero current registrations
- **Prioritize Rank 4 assessment**: Commission a systematic review of chlorambucil in primary pulmonary MALT lymphoma, where evidence level (L3) and mechanistic alignment are both stronger, for a more actionable repurposing decision

---

> ⚠️ **Disclaimer**: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application. This report should be reviewed by a qualified oncologist and clinical pharmacist before any clinical decision is made.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

