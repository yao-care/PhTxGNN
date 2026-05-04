---
layout: default
title: Filgrastim
parent: 僅模型預測 (L5)
nav_order: 140
evidence_level: L5
indication_count: 10
---

# Filgrastim
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

# Filgrastim: From Neutropenia to Primary Release Disorder of Platelets

## One-Sentence Summary

Filgrastim is a recombinant human Granulocyte Colony-Stimulating Factor (G-CSF), primarily used clinically to treat chemotherapy-induced neutropenia and to mobilize hematopoietic stem cells for transplantation.
The TxGNN model predicts it may be effective for **Primary Release Disorder of Platelets**, with **14 clinical trials** and **1 publication** identified in the evidence search — however, none of the trials directly target this indication, and the evidence is largely indirect.
Given the weak mechanistic link and absence of direct clinical data, the current recommendation is **Hold** pending further mechanistic validation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Neutropenia treatment and hematopoietic stem cell mobilization (known pharmacology; no Philippines registration data available) |
| Predicted New Indication | Primary Release Disorder of Platelets |
| TxGNN Prediction Score | 99.998% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Filgrastim is a recombinant G-CSF that primarily stimulates the proliferation and differentiation of neutrophil precursors in the bone marrow, accelerating neutrophil recovery following myelosuppressive chemotherapy. It also plays a well-established role in mobilizing CD34+ hematopoietic stem and progenitor cells into the peripheral blood for collection and transplantation.

The predicted connection to primary release disorder of platelets rests on an indirect theoretical pathway: G-CSF receptors (G-CSFR/CD114) are expressed on megakaryocytes — the precursor cells that give rise to platelets — and stimulation of this receptor may theoretically influence megakaryocyte maturation and, consequently, platelet granule biosynthesis. Primary release disorder of platelets involves defects in dense granule (δ-granule) or alpha-granule (α-granule) secretion, impairing platelet activation upon vascular injury. In principle, if G-CSF can influence the granule content during megakaryopoiesis, it might partially compensate for these secretion defects.

However, this mechanistic hypothesis is highly speculative. The repurposing rationale explicitly notes that G-CSF has no established direct mechanism on platelet granule release function. The high TxGNN prediction score most likely reflects the graph-structural proximity between G-CSF nodes and platelet-related disease nodes in the knowledge graph, rather than true pharmacological relevance. No preclinical studies have yet validated this pathway, making this a model-generated hypothesis requiring experimental confirmation before any clinical translation is considered.

---

## Clinical Trial Evidence

The following trials were identified in the evidence search. All retrieved trials involve Filgrastim in the context of stem cell mobilization or supportive care for hematologic malignancies — none directly study Filgrastim for primary release disorder of platelets.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04047628](https://clinicaltrials.gov/study/NCT04047628) | Phase 3 | Recruiting | 156 | RCT comparing autologous HSCT vs. best available therapy in treatment-resistant relapsing MS; Filgrastim used for stem cell mobilization. Highest-quality trial identified, but not directly relevant to platelet release disorders. |
| [NCT00245037](https://clinicaltrials.gov/study/NCT00245037) | Phase 1/2 | Completed | 147 | Non-myeloablative allogeneic HSCT using busulfan/fludarabine/TBI for hematologic malignancies; Filgrastim as mobilization agent. |
| [NCT00043979](https://clinicaltrials.gov/study/NCT00043979) | Phase 2 | Completed | 60 | Allogeneic/syngeneic blood stem cell transplantation for high-risk pediatric sarcomas; Filgrastim for stem cell mobilization. |
| [NCT01335932](https://clinicaltrials.gov/study/NCT01335932) | Phase 2 | Completed | 160 | RCT of ganciclovir to prevent CMV reactivation in sepsis/trauma-associated respiratory failure; Filgrastim as background supportive therapy. |
| [NCT01503918](https://clinicaltrials.gov/study/NCT01503918) | Phase 2 | Completed | 124 | Antiviral prophylaxis for CMV reactivation in ICU patients; Filgrastim as supportive care. |
| [NCT00923364](https://clinicaltrials.gov/study/NCT00923364) | Phase 2 | Completed | 19 | Reduced-intensity HSCT for patients with GATA2 mutations; Filgrastim for stem cell mobilization. |
| [NCT00076752](https://clinicaltrials.gov/study/NCT00076752) | Phase 2 | Completed | 9 | Intensified lymphodepletion followed by autologous HSCT for severe SLE; Filgrastim for stem cell mobilization. |
| [NCT02646098](https://clinicaltrials.gov/study/NCT02646098) | Phase 2 | Completed | 64 | CD34+ selection vs. unselected autologous SCT in mantle cell and diffuse large B-cell lymphoma. |
| [NCT05436418](https://clinicaltrials.gov/study/NCT05436418) | Phase 1/2 | Recruiting | 260 | Post-transplant cyclophosphamide-based GVHD prophylaxis after reduced-intensity conditioning and PBSCT. |
| [NCT06859424](https://clinicaltrials.gov/study/NCT06859424) | Phase 2 | Recruiting | 358 | Platform protocol investigating PTCy-based GVHD prophylaxis after mismatched unrelated donor PBSCT. |

> ⚠️ **Note:** None of these trials are designed to evaluate Filgrastim as a therapeutic agent for primary release disorder of platelets. Filgrastim appears exclusively as a stem cell mobilization or supportive care agent. These trials do not constitute clinical evidence for the predicted indication.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29770133](https://pubmed.ncbi.nlm.nih.gov/29770133/) | 2018 | Clinical/Observational | Frontiers in Immunology | G-CSF-based peripheral blood stem cell mobilization in healthy allogeneic donors preferentially mobilizes specific lymphocyte subsets; discusses immune modulation potential of G-CSF. Not directly relevant to platelet release disorders. |

---

## Philippines Market Information

Filgrastim is currently **not registered** with the Food and Drug Administration of the Philippines (FDA-Philippines). No marketing authorizations have been identified.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | *No registrations found* | — | — |

---

## Safety Considerations

Formal safety data (warnings and contraindications from the Philippines package insert) is not available in this Evidence Pack.

> Please refer to the package insert for standard safety information.

Nonetheless, mechanistic analysis of the predicted indication landscape has identified the following **indication-specific safety signals** that warrant attention if any clinical exploration is considered:

- **Pseudo-von Willebrand Disease (Rank 2 prediction):** G-CSF has been reported to increase circulating von Willebrand Factor (vWF) concentrations via endothelial cell activation. This could theoretically **exacerbate** pseudo-vWD symptoms (GPIbα gain-of-function mutations causing excess platelet-vWF binding), representing a potential safety hazard rather than a therapeutic benefit.

- **C1 Inhibitor Deficiency / Hereditary Angioedema (Rank 7 prediction):** G-CSF causes large-scale neutrophil mobilization that may activate the contact activation system (Factor XII), potentially accelerating bradykinin generation. Case reports of G-CSF-induced HAE-like episodes exist in the literature. **This indication carries a potential harm signal and should not be pursued.**

- **Serpinopathy with Toxic Serpin Polymerization (Rank 8 prediction):** G-CSF increases neutrophil elastase secretion, while serpins (e.g., alpha-1 antitrypsin) are physiologically designed to inhibit this enzyme. Administration of G-CSF in serpin-deficient states may theoretically **accelerate tissue damage** (e.g., pulmonary emphysema progression).

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All 14 clinical trials retrieved involve Filgrastim exclusively as a stem cell mobilization or supportive care agent in hematologic malignancy contexts; none provide direct therapeutic evidence for primary release disorder of platelets, and the mechanistic hypothesis linking G-CSF to platelet granule secretion is indirect and unvalidated. Furthermore, several of the co-predicted indications carry **active safety concerns**, suggesting that broad exploration in platelet-related disorders requires careful pre-screening.

**To proceed, the following is needed:**

- **MOA validation:** Retrieve full mechanism of action data from DrugBank API (DG002) to confirm whether G-CSF receptor expression on megakaryocytes is sufficient to justify further investigation.
- **Preclinical evidence:** In vitro or animal studies specifically evaluating G-CSF effects on platelet dense granule or alpha-granule secretion are required before any clinical hypothesis can be formed.
- **Philippines regulatory data:** Download and parse the Philippines FDA package insert PDF to obtain local warnings and contraindications (DG001), which is currently a blocking data gap.
- **Safety differentiation:** Conduct a systematic safety analysis to distinguish which platelet disorder subtypes might be safe to study (e.g., constitutional thrombocytopenia where G-CSF's megakaryocyte-stimulating effect is theoretically plausible) from those where G-CSF may be harmful (pseudo-vWD, C1 inhibitor deficiency).
- **Literature deep dive:** Commission a targeted PubMed/EMBASE search combining G-CSF with megakaryocyte function, platelet granule, and dense granule release to identify any unpublished or niche mechanistic studies not captured in this initial evidence pull.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

