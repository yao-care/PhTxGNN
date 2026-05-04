---
layout: default
title: Cytarabine
parent: 僅模型預測 (L5)
nav_order: 90
evidence_level: L5
indication_count: 9
---

# Cytarabine
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

# Cytarabine: From Leukemia to Small Cell Lung Carcinoma

## One-Sentence Summary

Cytarabine (Ara-C) is a pyrimidine nucleoside analog antimetabolite and cornerstone of treatment for hematologic malignancies—most notably acute myeloid leukemia (AML)—for over five decades.
The TxGNN model predicts it may be effective for **Small Cell Lung Carcinoma (SCLC)**, with **3 clinical trials** and **20 publications** identified in support of this direction.
However, the majority of directly relevant clinical evidence dates from 1979–1997 and has been functionally superseded by modern etoposide/platinum-based regimens, making this primarily a historical research signal rather than an immediately actionable repurposing candidate.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute myeloid leukemia (AML) and hematologic malignancies (globally established; not registered in the Philippines) |
| Predicted New Indication | Small Cell Lung Carcinoma |
| TxGNN Prediction Score | 99.78% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on well-established pharmacology, Cytarabine (Ara-C) is a deoxycytidine analog that, once phosphorylated intracellularly to Ara-CTP, competes with endogenous dCTP to inhibit DNA polymerase-α and becomes incorporated into nascent DNA strands, causing chain termination and irreparable double-strand breaks. As an S-phase–specific agent, its cytotoxicity is maximized in rapidly cycling cells—making it theoretically attractive for SCLC, a neuroendocrine tumor notorious for an extremely short doubling time (29–55 days) and near-universal dependence on rapid DNA replication.

From 1979 to 1990, a series of small Phase 2 trials explored Cytarabine—primarily in combination with cyclophosphamide and Adriamycin (PMID 232239), etoposide (PMID 2841844), and cisplatin/vindesine (PMID 2157307)—in both SCLC and NSCLC. In the earliest study (PMID 232239), a 78% combined complete and partial remission rate was achieved with CAV + Ara-C plus thoracic and whole-brain radiotherapy in 20 untreated SCLC patients, though long-term survival data were limited. For relapsed/refractory SCLC, VP-16 combined with infusional Ara-C (PMID 2841844) produced measurable but clinically unsatisfactory responses. In vitro studies using SCLC spheroid models (PMID 2992752) and cell line panels (PMID 1360876) further confirmed biological activity.

Despite this mechanistic plausibility and historical precedent, Cytarabine's role in SCLC has been displaced by the superior efficacy and tolerability of etoposide + platinum doublets (EP/IP), which became the global standard of care from the 1990s onward. The subsequent approvals of atezolizumab (2019) and lurbinectedin (2020) have further narrowed the therapeutic niche available to Ara-C–containing regimens. One remaining context where intrathecal Cytarabine retains historical usage—SCLC-associated leptomeningeal metastases (PMID 6264785)—is not addressed in current formal guidelines and was not captured in the active clinical trial dataset. The TxGNN model's high prediction score most likely reflects the knowledge graph's shared node structure linking SCLC's rapid-proliferation biology to Ara-C's established antineoplastic class rather than a novel biological insight.

---

## Clinical Trial Evidence

> **Important caveat:** All three retrieved trials investigate **intrathecal pemetrexed** for NSCLC leptomeningeal metastases—not Cytarabine for SCLC. Their relevance is conceptual (demonstrating that novel agents can replace standard MTX/Ara-C in intrathecal chemotherapy), not direct. **No active or completed trials evaluating Cytarabine specifically in SCLC are currently registered on ClinicalTrials.gov.**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03101579](https://clinicaltrials.gov/study/NCT03101579) | Phase 1 | Completed | 13 | Intrathecal pemetrexed for recurrent leptomeningeal metastasis from NSCLC; demonstrates feasibility of novel agents beyond standard MTX/Ara-C for intrathecal delivery in lung cancer brain metastases |
| [NCT03507244](https://clinicaltrials.gov/study/NCT03507244) | Phase 1/2 | Completed | 34 | Intrathecal pemetrexed combined with involved-field radiotherapy for solid tumor leptomeningeal metastasis; supports synergistic intrathecal chemotherapy + local RT strategy |
| [NCT00863512](https://clinicaltrials.gov/study/NCT00863512) | Phase 3 | Terminated | 34 | Adjuvant chemotherapy (vinorelbine, cisplatin, docetaxel, gemcitabine, pemetrexed) in early-stage NSCLC after surgery; terminated early with limited enrollment—minimal relevance to Cytarabine in SCLC |

---

## Literature Evidence

Selecting the 10 publications with highest direct relevance to Cytarabine in SCLC or mechanistically related lung cancer contexts (prioritized: Phase 2/direct > in vitro > review):

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [232239](https://pubmed.ncbi.nlm.nih.gov/232239/) | 1979 | Phase 2 | Med Pediatr Oncol | 20 untreated SCLC patients treated with cyclophosphamide + Adriamycin + **Ara-C** (20 mg/m² q12h SC, days 5–9) repeated q28d, plus thoracic/whole-brain RT; 78% CR+PR rate, median survival 49+ weeks for complete responders |
| [6095640](https://pubmed.ncbi.nlm.nih.gov/6095640/) | 1984 | Phase 2 | Am J Clin Oncol | Two simultaneous SCLC studies with **Ara-C** 100 mg/m²/day continuous infusion: (1) monotherapy in 10 heavily pretreated patients—no responses, severe toxicity; (2) Ara-C added to CAV in 25 extensive-stage patients—modest additional benefit with significant myelosuppression |
| [2841844](https://pubmed.ncbi.nlm.nih.gov/2841844/) | 1988 | Phase 2 | Am J Clin Oncol | 17 refractory SCLC patients: **Ara-C** 45 mg/m²/day continuous IV infusion × 72 h + VP-16 as 3 daily IV bolus doses; measurable responses but limited by progressive disease; 3 early deaths from tumor progression |
| [9363869](https://pubmed.ncbi.nlm.nih.gov/9363869/) | 1997 | Randomized | J Clin Oncol | CALGB randomized trial: chemotherapy + radiation ± warfarin in limited-stage SCLC; warfarin did not improve outcomes; provides context that adjunctive manipulation of SCLC chemotherapy regimens yields limited benefit |
| [6264785](https://pubmed.ncbi.nlm.nih.gov/6264785/) | 1981 | Case Series | Am J Med | 60 SCLC patients with cerebral/meningeal metastases; intensive chemotherapy without prophylactic cranial irradiation; 78% response rate; provides historical rationale for **intrathecal Cytarabine** in SCLC meningeal disease |
| [2992752](https://pubmed.ncbi.nlm.nih.gov/2992752/) | 1985 | In Vitro | Cancer | 5 SCLC cell lines grown as 3D spheroids tested against multiple chemotherapeutic agents including **Ara-C**; volume decrease used as activity indicator; confirms pre-clinical cytotoxic activity in SCLC models |
| [1360876](https://pubmed.ncbi.nlm.nih.gov/1360876/) | 1992 | In Vitro | Cancer Chemother Pharmacol | SCLC cell line panel (including 3 MDR variants); sensitivity profiling with doxorubicin, etoposide, vincristine, carmustine; contextualizes cross-resistance patterns relevant to **Ara-C**–containing rescue regimens |
| [2156598](https://pubmed.ncbi.nlm.nih.gov/2156598/) | 1990 | Phase 2 | Cancer | 37 chemo-naive advanced NSCLC patients: high-dose **Ara-C** (3 g/m² over 3 h) + cisplatin 100 mg/m² q3w; 14% overall response rate; Grade IV myelosuppression in 32%; 4 treatment-related deaths—highlights high-dose toxicity risk |
| [2157307](https://pubmed.ncbi.nlm.nih.gov/2157307/) | 1990 | Phase 2 | Tumori | 32 advanced NSCLC patients: cisplatin + vindesine + **Ara-C** 15 mg/m² SC q12h days 1–3 (total 90 mg/m²); 18% response rate (5/28 evaluable); modest activity with manageable toxicity at low Ara-C doses |
| [348088](https://pubmed.ncbi.nlm.nih.gov/348088/) | 1978 | Review | Antibiotics Chemother | Foundational review of Ara-C analogs (cyclocytidine, AAFC, N4-acyl derivatives) with enhanced resistance to cytidine deaminase; pharmacological context for overcoming Ara-C's major metabolic vulnerability in solid tumors |

---

## Philippines Market Information

Cytarabine is **not currently registered with the FDA Philippines**. No product authorizations were identified in the regulatory database.

> Cytarabine is included on the WHO Essential Medicines List and is available in most oncology centers worldwide for hematologic malignancies. The absence of FDA Philippines registration does not preclude hospital pharmacy procurement for established AML/ALL indications through compassionate use or special access pathways; however, any repurposing clinical trial in the Philippines would require formal FDA Philippines authorization and a new drug application or clinical trial exemption.

---

## Cytotoxicity

Cytarabine is a **conventional cytotoxic antineoplastic agent** (nucleoside analog antimetabolite). This section is mandatory given its classification.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Pyrimidine nucleoside analog antimetabolite (S-phase specific) |
| Myelosuppression Risk | **High** — Leukopenia, neutropenia, and thrombocytopenia are dose-limiting; Grade IV myelosuppression in 32% of patients at high-dose regimens (Ara-C 3 g/m², PMID 2156598); standard doses also cause significant cytopenias |
| Emetogenicity Classification | Low to moderate at standard doses; higher with high-dose regimens (>1 g/m²) |
| Monitoring Items | CBC with differential (at minimum weekly during active treatment), platelet count, serum creatinine, liver function tests; neurological assessment (cerebellar function) at high doses |
| Handling Protection | Must be prepared and administered following institutional cytotoxic drug handling regulations — closed-system drug transfer devices (CSTDs), appropriate PPE, dedicated cytotoxic preparation area |

---

## Safety Considerations

Please refer to the package insert for complete safety information. Formal FDA Philippines package insert data was not available in this evidence pack.

Based on clinical study reports contained in the evidence pack, the following toxicity signals have been documented in lung cancer contexts:

- **Severe myelosuppression**: Grade III–IV neutropenia and thrombocytopenia are the principal dose-limiting toxicities; 4 treatment-related deaths reported in one high-dose Ara-C + cisplatin Phase 2 trial (PMID 2156598)
- **Neurotoxicity**: Cerebellar syndrome is an established risk at high doses (≥1–3 g/m²); peripheral neuropathy and encephalopathy also reported
- **Gastrointestinal toxicity**: Nausea, vomiting, mucositis, and diarrhea particularly at high doses; oral mucositis is recognized as a class effect for S-phase–specific DNA synthesis inhibitors (PMID 15548350)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a TxGNN prediction score of 99.78%, the clinical evidence supporting Cytarabine in SCLC consists entirely of small Phase 2 and retrospective studies from 1979–1990 that have been superseded by etoposide/platinum-based standard-of-care regimens. Cytarabine is not registered in the Philippines, no active clinical trials exist for this indication, and no modern preclinical or translational studies have re-examined this combination in the context of current SCLC biology (ASCL1/NeuroD1 subtypes, DLL3 expression, CREBBP mutations).

**To proceed, the following is needed:**

- **Mechanism of action confirmation**: Formal MOA data retrieval from DrugBank (DG002 remediation) to quantify S-phase specificity and its relevance to SCLC proliferative kinetics in molecular subtype-specific models
- **Modern preclinical validation**: Cytotoxicity reassessment in contemporary SCLC cell lines (NCI-H69, NCI-H82, DMS-114) and patient-derived organoids representing current ASCL1-high and NeuroD1-high subtypes
- **Niche identification**: Determine whether intrathecal Cytarabine for SCLC leptomeningeal metastases represents a defensible and specific repurposing niche, given absence of approved intrathecal alternatives
- **Safety package**: Retrieve and review complete Philippines/TFDA package insert warnings and contraindications (DG001 remediation) before any safety classification can be finalized
- **Regulatory pathway assessment**: Evaluate FDA Philippines special access mechanisms if a repurposing pilot study is to be initiated, given zero current market registrations
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

