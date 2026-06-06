---
layout: default
title: Melphalan
parent: 僅模型預測 (L5)
nav_order: 219
evidence_level: L5
indication_count: 10
---

# Melphalan
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

# Melphalan: From Multiple Myeloma to Gonadal Germ Cell Tumor

## One-Sentence Summary

Melphalan (L-phenylalanine mustard) is a classic bifunctional DNA alkylating agent belonging to the nitrogen mustard class, with established use in multiple myeloma treatment and as a core ASCT conditioning agent.
The TxGNN model predicts it may be effective for **Gonadal Germ Cell Tumor**, with **8 clinical trials** and **4 publications** currently supporting this direction — including one completed Phase 2 study designed specifically for poor-prognosis relapsed germ cell tumors.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Multiple Myeloma (no Philippines registration data available) |
| Predicted New Indication | Gonadal Germ Cell Tumor |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L2 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not included in this Evidence Pack. Based on established pharmacology, Melphalan is a bifunctional alkylating agent that forms covalent interstrand and intrastrand DNA cross-links, blocking replication and transcription and triggering apoptosis preferentially in rapidly dividing tumor cells. As an amino acid derivative of mechlorethamine (nitrogen mustard), melphalan also exploits the phenylalanine transport system to achieve selective tumor cell uptake in tumors with high amino acid demand.

Gonadal germ cell tumors (GCTs) present a uniquely favorable mechanistic match. They are characterized by high proliferation rates, marked genomic instability (including i(12p) amplification), and functional deficiency in homologous recombination (HR/BRCA pathway), rendering them exquisitely sensitive to DNA cross-linking agents. This is precisely why the BEP regimen (bleomycin + etoposide + cisplatin) achieves cure rates exceeding 80% in good-risk GCT — both cisplatin and melphalan converge on the same DNA interstrand cross-link mechanism. Sarcolysin (the D,L-racemic form of melphalan) was used clinically for testicular seminoma as early as 1956, representing one of the first recorded applications of an alkylating agent to germ cell malignancy.

In the modern HDC/ASCT framework for relapsed or platinum-refractory GCTs, melphalan has been incorporated into salvage conditioning regimens precisely because its mechanism is orthogonal to cisplatin-based resistance. A completed Phase 2 trial (NCT00936936, n=64) directly evaluated a melphalan-containing high-dose combination regimen (gemcitabine + docetaxel + melphalan + carboplatin) for poor-prognosis relapsed GCT, providing the highest-quality direct evidence for this indication.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT00936936](https://clinicaltrials.gov/study/NCT00936936) | Phase 2 | Completed | 64 | Two cycles of HDC for poor-prognosis relapsed GCT: cycle 1 = gemcitabine + docetaxel + **melphalan** + carboplatin; cycle 2 = ifosfamide + carboplatin + etoposide. Most direct Phase 2 evidence for melphalan in this indication. |
| [NCT00003425](https://clinicaltrials.gov/study/NCT00003425) | Phase 1/2 | Completed | 25 | Dose-escalation study of melphalan with autologous pluripotent HSC support and amifostine cytoprotection in high-risk solid tumors, likely including GCT subgroups. |
| [NCT00536601](https://clinicaltrials.gov/study/NCT00536601) | NA | Completed | 174 | Pilot study comparing high-dose chemotherapy regimens ± TBI before ASCT in hematologic malignancies and selected solid tumors; melphalan used as a conditional regimen component. |
| [NCT00060255](https://clinicaltrials.gov/study/NCT00060255) | Phase 2 | Completed | 451 | Eight different high-dose chemotherapy regimens ± radiation before autologous BMT/SCT for hematologic malignancies and selected solid tumors (1991–2013 long-term data). |
| [NCT00638898](https://clinicaltrials.gov/study/NCT00638898) | Phase 1 | Completed | 25 | High-dose busulfan + melphalan + topotecan followed by ASCT in advanced and recurrent solid tumors; completed 2024. |
| [NCT01272817](https://clinicaltrials.gov/study/NCT01272817) | NA | Completed | 36 | Nonmyeloablative allogeneic HSCT using ATG with either melphalan/cladribine or total lymphoid irradiation for a range of malignancies. |
| [NCT00002750](https://clinicaltrials.gov/study/NCT00002750) | Phase 1 | Completed | 6 | Intrathecal melphalan for recurrent neoplastic meningitis; different route and indication, limited relevance to systemic GCT treatment. |
| [NCT00003926](https://clinicaltrials.gov/study/NCT00003926) | Phase 1 | Terminated | 13 | Amifostine cytoprotection study with ASCT for high-risk pediatric solid tumors and brain tumors; terminated early, data value limited. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [13392619](https://pubmed.ncbi.nlm.nih.gov/13392619/) | 1956 | Historical Case Series | Voprosy Onkologii | First published clinical experience using sarcolysin (D,L-melphalan) to treat testicular seminoma and its metastases — foundational precedent for melphalan in gonadal GCT. |
| [4270380](https://pubmed.ncbi.nlm.nih.gov/4270380/) | 1973 | Clinical Review/Series | Oncology | Early clinical series on chemotherapy of testicular germinal tumors, including alkylating agents in the pre-cisplatin era; provides historical context for melphalan's role. |
| [24913](https://pubmed.ncbi.nlm.nih.gov/24913/) | 1977 | Review | Urologic Clinics of North America | Review of seminoma treatment approaches including chemotherapy with alkylating agents; reflects late 1970s standard of care. |
| [14151951](https://pubmed.ncbi.nlm.nih.gov/14151951/) | 1964 | Pharmacological Study | Acta UICC | Investigation of the effects of hormonal and alkylating drugs (including melphalan precursors) on pituitary FSH function in the context of cancer treatment. |

---

## Philippines Market Information

Melphalan currently has **no registered products** with the FDA Philippines. There are 0 active authorizations on record, and the drug's market status is classified as **Not marketed**. Any clinical use in the Philippines would require either compassionate use authorization or import on a case-by-case basis.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Nitrogen mustard / Bifunctional alkylating agent (phenylalanine mustard class) |
| Myelosuppression Risk | **High** — myelosuppression is the dose-limiting toxicity; severe neutropenia, thrombocytopenia, and anemia are expected, particularly at high-dose conditioning regimens (≥140 mg/m²); nadir typically occurs 14–21 days after administration |
| Emetogenicity Classification | Moderate (standard doses); High (high-dose IV regimens used in ASCT conditioning) |
| Monitoring Items | CBC with differential (at minimum weekly during treatment cycles); renal function (melphalan clearance is partially renal-dependent; dose adjustment required); liver function tests; long-term surveillance for secondary AML/MDS (established risk with alkylating agents) |
| Handling Protection | Must follow cytotoxic drug handling regulations — preparation in a certified biological safety cabinet, full PPE (chemotherapy-grade gloves, closed-front gown, eye/face protection); classified as a NIOSH hazardous drug |

---

## Safety Considerations

Please refer to the package insert for safety information. No Philippines-specific safety data is available in this Evidence Pack. Retrieval of the TFDA package insert (warnings and contraindications) is flagged as a **Blocking** data gap that must be resolved before formal safety evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 trial (NCT00936936, n=64) provides direct evidence for melphalan-containing HDC in poor-prognosis relapsed gonadal GCT, supported by a mechanistically coherent basis (GCT HR-pathway deficiency → sensitivity to DNA cross-linking alkylation) and historical clinical use of sarcolysin in testicular seminoma dating to 1956. However, melphalan's role is primarily in the salvage/HDC-ASCT setting rather than first-line therapy, and the Philippines has no existing registration for this drug, requiring careful regulatory navigation.

**To proceed, the following is needed:**
- **MOA data from DrugBank**: Retrieve full mechanism of action to complete the mechanistic link analysis (currently High-severity data gap)
- **Safety data**: Download and parse the TFDA package insert to extract warnings and contraindications — currently a Blocking data gap preventing full S1 safety evaluation
- **DDI profile**: Drug-drug interaction search returned no results; a secondary search with expanded query terms is recommended
- **Route compatibility assessment**: Confirm IV melphalan availability and ASCT infrastructure in the Philippines context before clinical feasibility can be established
- **Subtype stratification**: Clarify whether the target population is testicular vs. ovarian GCT, and whether the intended use is relapsed/refractory (HDC-ASCT) or an alternative first-line role
- **Secondary malignancy risk assessment**: Long-term risk of alkylating agent–induced AML/MDS must be formally evaluated in the treatment plan
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

