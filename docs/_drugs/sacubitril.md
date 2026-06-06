---
layout: default
title: Sacubitril
parent: 僅模型預測 (L5)
nav_order: 301
evidence_level: L5
indication_count: 5
---

# Sacubitril
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

# Sacubitril: From Heart Failure to Brain Small Vessel Disease 1 with Ocular Anomalies

## One-Sentence Summary

Sacubitril is a neprilysin inhibitor used clinically as the fixed-dose combination Entresto® (sacubitril/valsartan) for heart failure with reduced ejection fraction (HFrEF).
The TxGNN model predicts it may be effective for **brain small vessel disease 1 with or without ocular anomalies**,
with **0 clinical trials** and **18 publications** currently identified — however, none of the publications directly investigate sacubitril as a treatment for this condition.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heart failure with reduced ejection fraction (HFrEF), as Entresto® (sacubitril/valsartan) |
| Predicted New Indication | Brain small vessel disease 1 with or without ocular anomalies |
| TxGNN Prediction Score | 99.58% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available for sacubitril in this evidence pack. Based on established pharmacology, sacubitril is a prodrug converted in vivo to the active neprilysin inhibitor LBQ657. Neprilysin (neutral endopeptidase, NEP) degrades natriuretic peptides including ANP, BNP, and CNP; its inhibition elevates circulating natriuretic peptide levels, resulting in vasodilation, natriuresis, and reduced ventricular remodeling. Clinically, sacubitril is always co-administered with valsartan (an ARB) to counterbalance the renin-angiotensin system activation that would otherwise occur from elevated angiotensin II.

The theoretical link to brain small vessel disease (SVD) is indirect and highly speculative. Elevated ANP/CNP from neprilysin inhibition could, in principle, improve cerebral small vessel endothelial function and offer indirect vascular protection — a pathway conceptually relevant to hemodynamic forms of SVD such as CADASIL. However, "brain small vessel disease 1 with or without ocular anomalies" (associated with COL4A1/COL4A2 mutations) is primarily a **genetic structural disorder** of the vascular extracellular matrix. The ocular anomaly component (anterior segment dysgenesis as seen in Axenfeld-Rieger-type conditions) is a congenital developmental defect arising during embryogenesis.

There is no established mechanistic pathway connecting neprilysin inhibition to correction of collagen IV structural defects or to prevention of congenital ocular malformations. The connection requires at minimum three unsupported inferential steps (neprilysin inhibition → ANP increase → cerebral arteriole remodeling → structural defect attenuation), and the ocular anomaly component has no pharmacological pathway to sacubitril whatsoever. This prediction is best classified as a model-generated hypothesis and warrants no clinical development action at this stage.

---

## Clinical Trial Evidence

No clinical trials investigating Sacubitril for brain small vessel disease 1 with or without ocular anomalies are currently registered.

---

## Literature Evidence

The 18 publications retrieved are reviews and case reports describing congenital ocular anomalies, craniofacial syndromes, and related genetic conditions — none directly study sacubitril as a therapeutic agent for this indication. All relevance assessments remain pending in the evidence pack.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35882526](https://pubmed.ncbi.nlm.nih.gov/35882526/) | 2023 | Review | Journal of Medical Genetics | Axenfeld-Rieger syndrome: anterior segment anomalies with systemic features; distinct subtypes based on causative genes (FOXC1, PITX2) |
| [36926528](https://pubmed.ncbi.nlm.nih.gov/36926528/) | 2023 | Review | Clinical Ophthalmology | ARS current perspectives: FOXC1/PITX2 mutations, neural crest contributions, glaucoma risk in over half of patients |
| [37468646](https://pubmed.ncbi.nlm.nih.gov/37468646/) | 2024 | Review | Pediatric Nephrology | Ocular manifestations of CAKUT-associated genes; retinal expression confirmed for most CAKUT genes |
| [33870948](https://pubmed.ncbi.nlm.nih.gov/33870948/) | 2022 | Review | Journal of Neuro-Ophthalmology | Optic nerve aplasia: rare ocular anomaly with systemic and genetic co-findings |
| [35791156](https://pubmed.ncbi.nlm.nih.gov/35791156/) | 2022 | Review | Indian Journal of Ophthalmology | Fraser syndrome (cryptophthalmos, syndactyly): clinical and orbital anomaly characterization |
| [30182440](https://pubmed.ncbi.nlm.nih.gov/30182440/) | 2018 | Review | Am J Med Genetics Part C | Holoprosencephaly neuropathology: spectrum from aprosencephaly to microforms |
| [22963965](https://pubmed.ncbi.nlm.nih.gov/22963965/) | 2012 | Review | Annales de Dermatologie | Branchio-oculo-facial syndrome (TFAP2A mutations): cutaneous and ocular abnormalities |
| [11581073](https://pubmed.ncbi.nlm.nih.gov/11581073/) | 2001 | Review | Ophthalmology | Renal coloboma syndrome: characterization of ocular features |
| [6782689](https://pubmed.ncbi.nlm.nih.gov/6782689/) | 1981 | Review | Survey of Ophthalmology | Ocular coloboma: spectrum from iris coloboma to anophthalmos; etiological heterogeneity |
| [2237761](https://pubmed.ncbi.nlm.nih.gov/2237761/) | 1990 | Review | Survey of Ophthalmology | Congenital craniofacial anomalies of ophthalmic importance: classification and surgical management principles |

---

## Philippines Market Information

Sacubitril is **not currently registered** with the Philippine FDA. No product licenses — including the combination product Entresto® (sacubitril/valsartan) — are on record. The drug is not commercially available through regulated channels in the Philippines.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Class-level note:** Sacubitril is only administered clinically as the fixed-dose combination with valsartan (Entresto®). Well-established class-level risks include: angioedema (risk significantly elevated if switching from ACE inhibitors — a mandatory 36-hour washout is required), symptomatic hypotension, hyperkalemia, and renal function impairment. Entresto® is contraindicated in pregnancy due to fetal toxicity. Drug interaction data for sacubitril as an isolated compound was not retrievable from the current database query.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite the high TxGNN model score (99.58%), the mechanistic link between sacubitril's neprilysin-inhibition pathway and the pathophysiology of brain small vessel disease 1 — a genetic disorder of collagen IV structural integrity combined with congenital ocular developmental defects — is highly speculative, multi-inferential, and entirely unsupported by preclinical or clinical data. No disease-specific clinical trials or sacubitril-relevant literature exist for this indication.

**To proceed, the following is needed:**

- Preclinical evidence demonstrating neprilysin inhibition has any measurable effect on COL4A1/COL4A2-mediated vascular wall structural pathology
- In vitro or in vivo data linking ANP/CNP pathway upregulation to attenuation of small vessel wall damage in SVD genetic models
- Clarification of whether the prediction target is the vascular hemodynamic component alone (theoretically more tractable) vs. the congenital ocular malformation component (not pharmacologically addressable)
- MOA data retrieval from DrugBank API to fill DG002
- Philippine FDA package insert data to complete safety profile (DG001 — currently Blocking for S1 assessment)

> **Prioritization note:** Among the five predicted indications in this evidence pack, **diabetic nephropathy (Rank 3, L3 evidence, Proceed with Guardrails)** is considerably more actionable — it has 2 registered clinical trials (including a Phase 4 RCT, NCT06501651, n=297) and 17 supporting publications with a clearly established neprilysin-inhibition → natriuretic peptide → renal hemodynamic protection mechanistic pathway. Redirecting development resources toward the diabetic nephropathy indication is recommended.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

