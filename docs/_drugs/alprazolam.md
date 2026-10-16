---
layout: default
title: Alprazolam
parent: Moderate Evidence (L3-L4)
nav_order: 20
evidence_level: L4
indication_count: 3
last_modified_at: 2026-10-15
description: "Alprazolam: predicted new indication Insomnia (disease) (evidence level L4). Approved use: Anxiety disorder"
---

# Alprazolam
{: .fs-9 }

Evidence Level: **L4** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Alprazolam: From Anxiety Disorder to Insomnia

## One-Sentence Summary

Alprazolam is a benzodiazepine originally used to treat anxiety disorders, including mixed anxiety and depressive disorder.
The TxGNN model predicts it may be effective for **insomnia**, but there are **0 registered clinical trials** and only **18 publications**, almost none of which directly test alprazolam for insomnia.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorder; mixed anxiety and depressive disorder (from the knowledge graph; no approved indication text is available for the local registration) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known class pharmacology, alprazolam is a benzodiazepine that enhances GABA-A receptor signalling. This produces sedative and anxiolytic effects that could plausibly shorten the time needed to fall asleep. This link rests on general class knowledge, not on supplied data.

Insomnia is also commonly comorbid with anxiety and panic, which are the drug's established uses. This overlap helps explain why the model links the two conditions. However, a high computational score is not clinical proof. No controlled trial of alprazolam for primary insomnia was found.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

The retrieved publications are mostly indirect. Only the first two rows below involve insomnia or alprazolam use in insomnia, and neither is a controlled trial of alprazolam for primary insomnia.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | Retrospective clinical study | Medicine | 116 patients with coronary heart disease and insomnia; alprazolam was the control treatment against moxibustion plus ear acupuncture, so it does not test alprazolam as the intervention of interest |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Meta-analysis | Acta Pharmaceutica | Safety and dosing of tranquilizers in elderly patients with chronic diseases |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opin Drug Metab Toxicol | Pharmacokinetics of anxiolytic drugs |
| [7484706](https://pubmed.ncbi.nlm.nih.gov/7484706/) | 1995 | Review | Am Fam Physician | Overview of panic disorder |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Predictive model | Value Health Reg Issues | Trends and economic burden of benzodiazepine use, including long-term harms such as dependence and falls |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Animal study | Aging | Repeated alprazolam administration caused mitochondrial dysfunction and impaired memory in mice |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Prescription pattern study | Sleep Med | Hypnotic prescribing patterns in a managed-care population |

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0012 | Alprazolam | Not recorded | Not recorded (status: cancelled) |

---

## Safety Considerations

- **Knowledge-graph contraindication signals** (not from label text): anxiety disorder, neurotic disorder, dysthymic disorder, kidney disease, liver disease, gallbladder disease, open-angle and angle-closure glaucoma, obesity disorder, obstructive sleep apnea and other sleep apnea syndromes, congenital central hypoventilation syndrome, and substance-related disorder or substance abuse/dependence.
- **Drug Interactions**: 100 interactions were identified. Examples include:
  - **Major**: morphine, including liposomal morphine (risk of additive central nervous system and respiratory depression)
  - **Moderate**: aprepitant, bupropion, cimetidine, clarithromycin, clotrimazole, dronabinol, eliglustat, glycerol phenylbutyrate, metoclopramide, miconazole
  - **Minor**: several antacids (aluminium hydroxide, calcium carbonate, magnesium salts) and corticosteroids (betamethasone, dexamethasone)
- **Literature-noted risks**: dependence, tolerance, memory impairment, falls in older adults, and difficult discontinuation.

Please also refer to the package insert for full warnings and contraindications.

---

## Other Predicted Indications

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Comment |
|------|------|------|------|------|
| 2 | Benign paroxysmal torticollis of infancy | 99.61% | L5 | No trials or literature. A rare, self-limiting infantile condition; benzodiazepine use in infants is not justified and the prediction is likely a model artifact. Hold. |
| 3 | Agoraphobia | 99.56% | L3 (conservative) | Several older placebo-controlled studies in panic disorder with agoraphobia exist (for example, a 526-patient multicenter trial from 1988). This is closer to an extension of the existing anxiety and panic use than to true repurposing. Research question: verify study designs and check whether it already falls within labeled use. |

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The high TxGNN score (99.81%) is a computational prediction only. There are no registered trials and no controlled study of alprazolam in primary insomnia. The benzodiazepine risks (dependence, tolerance, next-day impairment, and 100 drug interactions including a major one with opioids) weigh against pursuing repurposing now. The product's only Philippine registration is cancelled.

**To proceed, the following is needed:**
- Controlled trial evidence of alprazolam in primary insomnia, or a systematic review comparing it with established hypnotics
- Mechanism of action data (from DrugBank)
- Package insert warnings and contraindications (from DOH-FDA Philippines), which are needed before any safety screening
- Confirmation of a valid Philippine registration, since the only record is cancelled
- A risk assessment for dependence and withdrawal, with a plan for short-term use only
- Separate follow-up on agoraphobia: full-text review of the older panic disorder trials and the 2023 network meta-analysis
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

