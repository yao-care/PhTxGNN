---
layout: default
title: Flupentixol
parent: 僅模型預測 (L5)
nav_order: 149
evidence_level: L5
indication_count: 9
---

# Flupentixol
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

# Flupentixol: From Psychosis to Retinal Dystrophy with Extraocular Anomalies

## One-Sentence Summary

Flupentixol is a thioxanthene-class typical antipsychotic, used internationally for schizophrenia, psychosis, and depression, and is not registered in the Philippines.
The TxGNN model predicts it may be effective for **Retinal Dystrophy with or without Extraocular Anomalies** with a prediction score of 99.99%;
however, **no clinical trials** exist for this indication, all **15 retrieved publications** are general ophthalmic reviews unrelated to Flupentixol treatment, and evidence analysis strongly suggests this is a **direction-reversed false positive** that warrants no further development.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Psychosis / Schizophrenia (international use; not registered in Philippines) |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacological information, Flupentixol is a thioxanthene-class typical antipsychotic that primarily antagonizes dopamine D1/D2 receptors and serotonin receptors. It is used internationally for schizophrenia, psychosis, and depressive disorders. Its original indication bears no pathophysiological overlap with inherited retinal dystrophies, which are caused by mutations in genes governing photoreceptor structure and function (e.g., *RPGR*, *RPGRIP1*).

> ⚠️ **Direction Reversal Warning — This prediction is highly likely to be a false positive.** Flupentixol is a known cause of drug-induced pigmentary retinopathy as a long-term adverse effect. The mechanism involves D2 receptor blockade in the retinal pigment epithelium (RPE) combined with melanin binding and toxic pigment deposition, resulting in progressive retinal damage rather than therapeutic benefit. The TxGNN knowledge graph most likely captured the "Flupentixol ↔ retinal pigment epithelium ↔ retinal dystrophy" association from adverse event data, and incorrectly reinterpreted this toxicity edge as a therapeutic signal.

This concern is compounded by the complete absence of any disease-specific literature: all 15 retrieved publications are general ophthalmic reviews covering topics such as orbital infections, congenital ptosis, lens anomalies, and extraocular muscle disorders. Not a single study examines Flupentixol as a treatment — or even an investigational candidate — for retinal dystrophy.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

> ⚠️ **None of the following publications examine Flupentixol as a treatment for retinal dystrophy.** They are general ophthalmic references retrieved via co-occurrence search and are listed for transparency only. Their relevance to this repurposing hypothesis is classified as indirect at best.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Differential diagnosis and key imaging features of pediatric ocular pathologies including congenital/developmental lesions |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan J Ophthalmology | Congenital anomalies of lens shape; association with anterior segment dysgenesis and hyperplastic vitreous |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Research Article | Int J Mol Sciences | Optic nerve head and retinal abnormalities in congenital fibrosis of extraocular muscles (CFEOM) caused by KIF21A/TUBB3 mutations |
| [33447730](https://pubmed.ncbi.nlm.nih.gov/33447730/) | 2020 | Review | Ther Adv Ophthalmology | Eye involvement in inherited metabolic disorders; cornea, lens, retina, and extraocular muscle abnormalities |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Review | Neuroradiology | Neuroradiological and clinical features in ophthalmoplegia for differential diagnosis and treatment guidance |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocular Vision Ocular Motility | Congenital cranial dysinnervation disorders (CCDDs) and their various forms of ophthalmoplegia |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Research Article | Am J Ophthalmology | Pathogenesis and treatment of maculopathy associated with cavitary optic disc anomalies |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | J Neuro-Ophthalmology | Isolated case of congenital trochlear-oculomotor synkinesis in a 6-year-old; proposed pathophysiology of CCDDs |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Review/Clinical Pearl | Seminars in Neurology | Systematic history and examination approach to patients presenting with diplopia |
| [19064847](https://pubmed.ncbi.nlm.nih.gov/19064847/) | 2008 | Case Series | Arch Ophthalmology | Clinical features, management, and outcomes in patients with orbital arteriovenous malformations |

---

## Philippines Market Information

Flupentixol has **no market authorization** in the Philippines. No product registrations, approved indications, or dosage form data are available.

---

## Safety Considerations

Please refer to the package insert for complete safety information.

As a thioxanthene-class typical antipsychotic, Flupentixol carries well-established class-level risks that are directly relevant to this repurposing assessment:

- **Drug-induced pigmentary retinopathy**: A documented long-term adverse effect of Flupentixol and related phenothiazine/thioxanthene drugs, caused by toxic pigment deposition in the RPE. This is the probable source of the KG prediction and represents an **active safety concern**, not a therapeutic signal.
- Extrapyramidal symptoms, tardive dyskinesia, and neuroleptic malignant syndrome are additional class-level concerns.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
This prediction is a likely direction-reversed false positive — Flupentixol's documented association with retinal pathology is as a causative toxin (drug-induced pigmentary retinopathy), not as a therapeutic agent. No clinical trials, no disease-specific preclinical studies, and no mechanistic rationale support its use in retinal dystrophy. All 9 predicted indications across this Evidence Pack similarly returned zero clinical trials and zero disease-specific literature, suggesting a systemic model limitation for this drug rather than isolated noise.

**To proceed, the following would be needed:**

- **MOA data retrieval** from DrugBank to formally characterize Flupentixol's receptor pharmacology and rule out any secondary beneficial pathway
- **Adverse event / pharmacovigilance review** to confirm the retinal toxicity signal and document it as a contraindication for this repurposing direction
- **TxGNN knowledge graph audit** to determine whether adverse event edges are being misclassified as therapeutic edges — particularly for drugs in the phenothiazine/thioxanthene class
- **Philippines FDA package insert** (if available from import registrations in neighboring markets) for full safety and contraindication profile
- If further exploration is desired despite this assessment, a formal preclinical study in a validated retinal dystrophy animal model with full safety monitoring would be the minimum required threshold before any clinical consideration

> *This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

