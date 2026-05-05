---
layout: default
title: Quetiapine
parent: 僅模型預測 (L5)
nav_order: 223
evidence_level: L5
indication_count: 10
---

# Quetiapine
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

# Quetiapine: From Schizophrenia/Bipolar Disorder to Retinal Dystrophy with or without Extraocular Anomalies

## One-Sentence Summary

Quetiapine is a well-established atypical antipsychotic, globally approved for schizophrenia, bipolar disorder, and as an adjunct therapy for major depressive disorder.
The TxGNN model's top-ranked prediction identifies **Retinal Dystrophy with or without Extraocular Anomalies** as a potential new indication,
however **0 clinical trials** and **15 tangentially related publications** (none directly studying this drug-disease pair) currently exist, and the mechanistic rationale is absent.
Quetiapine is not currently registered in the Philippines market.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in Philippines; known global approved uses include schizophrenia, bipolar I/II disorder, and adjunct treatment for major depressive disorder |
| Predicted New Indication | Retinal Dystrophy with or without Extraocular Anomalies |
| TxGNN Prediction Score | 99.57% |
| Evidence Level | L5 (Model prediction only — no direct supporting studies) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacology, Quetiapine is an atypical antipsychotic that primarily antagonises dopamine D2 receptors and serotonin 5-HT2A receptors, with additional binding at histamine H1, adrenergic α1/α2, and muscarinic receptors. These central nervous system receptor interactions underpin its established psychiatric efficacy.

Retinal dystrophy with or without extraocular anomalies is a hereditary retinal degeneration caused by genetic mutations (e.g., RPGR, CRB1, RPGRIP1L) that progressively destroy photoreceptor cells. Its pathophysiology is entirely structural and genetic — not driven by neurotransmitter dysregulation. There is **no known mechanistic intersection** between Quetiapine's D2/5-HT2A receptor pharmacology and the photoreceptor degeneration pathways involved in retinal dystrophy.

More critically, existing literature indicates that prolonged use of antipsychotics — including Quetiapine — may *cause* retinal and lenticular toxicity as an adverse effect (including cataract risk flagged by the EMA). This actively argues against repurposing Quetiapine for any primary ophthalmological indication. The model's high prediction score most likely reflects a spurious knowledge graph path through shared neurological or syndromic comorbidity nodes rather than a genuine pharmacological signal.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The 15 retrieved publications are ophthalmology reviews and case series covering general orbital and ocular pathologies. **None directly investigate Quetiapine as a therapeutic agent for retinal dystrophy.** They are listed below for completeness and transparency:

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38321238](https://pubmed.ncbi.nlm.nih.gov/38321238/) | 2024 | Review | Pediatric Radiology | Imaging features of pediatric ocular pathologies including congenital/developmental lesions and retinopathies |
| [33447730](https://pubmed.ncbi.nlm.nih.gov/33447730/) | 2020 | Review | Therapeutic Advances in Ophthalmology | Eye involvement in inherited metabolic disorders; covers retinal and optic pathway abnormalities |
| [38249493](https://pubmed.ncbi.nlm.nih.gov/38249493/) | 2023 | Review | Taiwan Journal of Ophthalmology | Congenital anomalies of lens shape and associated anterior segment dysgenesis |
| [33806565](https://pubmed.ncbi.nlm.nih.gov/33806565/) | 2021 | Research Article | Int J Molecular Sciences | Optic nerve and retinal abnormalities in congenital fibrosis of extraocular muscles (KIF21A/TUBB3 mutations) |
| [24932988](https://pubmed.ncbi.nlm.nih.gov/24932988/) | 2014 | Research Article | American Journal of Ophthalmology | Unifying pathogenesis theory for maculopathy associated with cavitary optic disc anomalies |
| [7035111](https://pubmed.ncbi.nlm.nih.gov/7035111/) | 1981 | Case Series | Documenta Ophthalmologica | Wagner-Stickler syndrome complex with vitreoretinal degeneration and sensorineural deafness |
| [30747268](https://pubmed.ncbi.nlm.nih.gov/30747268/) | 2019 | Review | Neuroradiology | Neuroradiological evaluation in acute-onset ophthalmoplegia for differential diagnosis |
| [30196776](https://pubmed.ncbi.nlm.nih.gov/30196776/) | 2018 | Review | J Binocular Vision & Ocular Motility | Congenital cranial dysinnervation disorders (CCDDs) and ophthalmoplegia classification |
| [24413161](https://pubmed.ncbi.nlm.nih.gov/24413161/) | 2014 | Case Report | J Neuro-Ophthalmology | Isolated trochlear-oculomotor synkinesis in congenital cranial dysinnervation disorder |
| [20127583](https://pubmed.ncbi.nlm.nih.gov/20127583/) | 2010 | Clinical Pearls | Seminars in Neurology | Systematic history-taking and examination approach for evaluating diplopia |

> ⚠️ **Important**: None of these publications study Quetiapine as a treatment for retinal dystrophy. The literature pool reflects general disease-domain content returned by a broad evidence search, not a drug-disease therapeutic relationship.

---

## Philippines Market Information

Quetiapine is currently **not registered** with the Philippines FDA. No approved products, dosage forms, or indications are on record.

---

## Safety Considerations

Formal Philippines FDA package insert data is not available (no registered product). Based on internationally available safety information for Quetiapine:

- **Ocular Risk**: Long-term use is associated with increased cataract risk (EMA formal warning); this is particularly concerning given the ophthalmological nature of the top predicted indication
- **Metabolic Effects**: Clinically significant risk of weight gain, hyperglycaemia, new-onset diabetes, and dyslipidaemia
- **Cardiovascular**: QTc prolongation risk; postural hypotension
- **CNS Effects**: Sedation, extrapyramidal symptoms, and tardive dyskinesia with prolonged use; neuroleptic malignant syndrome (rare but serious)
- **Black Box Warning** (US FDA): Increased mortality in elderly patients with dementia-related psychosis; suicidality risk in paediatric/young adult populations

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high numerical score (99.57%), but there is no pharmacologically plausible mechanism connecting Quetiapine's receptor profile to the genetic photoreceptor degeneration pathways underlying retinal dystrophy. The retrieved literature provides zero direct evidence, and the drug's known ocular adverse effects (cataract risk, potential retinal toxicity) create a net safety concern rather than a therapeutic opportunity for an ophthalmological indication.

**To proceed with further research, the following would be required:**
- A formal mechanistic hypothesis explaining how D2/5-HT2A receptor antagonism could confer neuroprotection or slow degeneration in retinal tissue
- At least one preclinical study (animal model or cell-based assay) demonstrating a beneficial effect in a retinal dystrophy model
- Comprehensive ocular safety data ruling out retinal or lenticular toxicity in the target patient population
- Philippines FDA regulatory pathway assessment for a new indication filing

---

### 📌 Alternative Prediction Worth Noting: Trichotillomania (Rank 8)

While the top prediction lacks supporting evidence, **Rank 8 — Trichotillomania (Hair-Pulling Disorder)** — presents a meaningfully different profile:

| Item | Content |
|------|---------|
| TxGNN Score | 99.38% |
| Evidence Level | **L4** (case series and pharmacological review) |
| Decision Stage | S1 — Research Question |
| Direct Quetiapine Literature | 7 publications, including clinical overviews and open-label case studies |
| Mechanistic Rationale | Biologically plausible: D2 antagonism reduces dopamine-driven compulsive reward; 5-HT2A antagonism aligns with OCD-spectrum augmentation therapy |

If resources allow for further exploratory analysis, trichotillomania represents a more scientifically grounded candidate for an off-label Quetiapine repurposing investigation — pending a randomised controlled trial to upgrade the evidence level from L4 to L2/L1.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

