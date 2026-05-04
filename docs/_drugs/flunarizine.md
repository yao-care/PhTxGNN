---
layout: default
title: Flunarizine
parent: 僅模型預測 (L5)
nav_order: 144
evidence_level: L5
indication_count: 1
---

# Flunarizine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Flunarizine: From Vertigo to Migraine Disorder

## One-Sentence Summary

Flunarizine is a selective calcium channel blocker traditionally used globally for the prevention of vertigo and migraine, though it currently holds no registration in the Philippines market.
The TxGNN model predicts it may be effective for **Migraine Disorder** with a high confidence score of 99.12%,
supported by **19 clinical trials** identified in ClinicalTrials.gov, including multiple completed head-to-head randomised controlled trials directly comparing Flunarizine against established first-line prophylactic agents.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Vertigo and migraine prevention (internationally approved; no Philippines registration on record) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.12% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Flunarizine is a selective T-type calcium channel blocker with a well-characterised triple mechanism for migraine prevention. First, it suppresses **Cortical Spreading Depression (CSD)** — the wave of neuronal depolarisation that underlies the migraine aura — by limiting calcium influx that sustains CSD propagation. Second, it reduces hyperexcitability in trigeminal nociceptive neurons, thereby blocking the central sensitisation cascade that amplifies migraine pain. Third, it stabilises cerebral vascular smooth muscle tone, dampening the exaggerated vasoreactivity seen during migraine attacks. Supplementary D2 receptor antagonism and antihistaminergic activity further contribute to headache suppression.

These mechanistic properties align directly with the major pathophysiological targets in migraine — neural hyperexcitability, trigeminovascular activation, and vascular instability — which explains why the TxGNN knowledge-graph model assigns a prediction score of 0.991. The drug is already approved for migraine prophylaxis in numerous markets across Europe, Asia, and Latin America, providing a substantial regulatory and pharmacovigilance track record that reduces the de-novo risk profile.

The primary repurposing opportunity here is therefore a **market-entry play for the Philippines**: Flunarizine represents a low-cost, once-daily oral prophylactic with decades of real-world use, potentially addressing an unmet need in a market where preventive migraine therapy options may be limited by cost or accessibility.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02639598](https://clinicaltrials.gov/study/NCT02639598) | Phase 4 | Completed | 62 | Head-to-head RCT of Flunarizine 10 mg/day vs Topiramate 50 mg/day for chronic migraine prophylaxis; directly evaluates Flunarizine efficacy as a primary intervention |
| [NCT03712917](https://clinicaltrials.gov/study/NCT03712917) | N/A | Completed | 120 | Three-arm parallel trial comparing Greater Occipital Nerve Block, Topiramate, and Flunarizine for episodic migraine prevention; reduction in VAS scores and attack frequency assessed post-treatment |
| [NCT06162819](https://clinicaltrials.gov/study/NCT06162819) | N/A | Unknown | 84 | Randomised comparison of Flunarizine vs Amitriptyline for migraine prophylaxis in a tertiary care setting in Pakistan; primary endpoints are attack frequency and VAS pain score |
| [NCT07354126](https://clinicaltrials.gov/study/NCT07354126) | N/A | Recruiting | 44 | Paediatric RCT comparing Flunarizine vs Propranolol in children aged 8–15 using the PedMIDAS disability scale; extends evidence to an under-studied age group |
| [NCT06499116](https://clinicaltrials.gov/study/NCT06499116) | Phase 4 | Not Yet Recruiting | 460 | PREMI Study: pragmatic multicentre RCT comparing amitriptyline, flunarizine, topiramate, and propranolol as first-line preventive therapy in primary care; largest planned head-to-head comparison |
| [NCT00752466](https://clinicaltrials.gov/study/NCT00752466) | Phase 1 | Completed | 75 | Open-label pharmacokinetic study examining drug–drug interaction between Flunarizine and Topiramate during mono- and combination therapy; directly characterises a clinically relevant co-prescription scenario |
| [NCT04766762](https://clinicaltrials.gov/study/NCT04766762) | N/A | Unknown | 96 | RCT comparing acupuncture (Ying–Wei method) against Flunarizine hydrochloride as active control in migraine without aura; Flunarizine serves as the reference standard, implying established efficacy |
| [NCT07068815](https://clinicaltrials.gov/study/NCT07068815) | Phase 1 | Not Yet Recruiting | 60 | RCT comparing Fu's Subcutaneous Needling (FSN) against Flunarizine hydrochloride in migraine without aura; co-primary endpoints are pain relief and quality-of-life improvement |
| [NCT06753825](https://clinicaltrials.gov/study/NCT06753825) | N/A | Active, Not Recruiting | 60 | Observational study comparing transcutaneous pulsed radiofrequency therapy versus calcium channel blockers (class inclusive of Flunarizine) for childhood migraine; long-term follow-up design |
| [NCT03828539](https://clinicaltrials.gov/study/NCT03828539) | Phase 4 | Completed | 777 | HEART Study: Erenumab vs Topiramate double-blind RCT in episodic and chronic migraine; Flunarizine is listed as a prior prophylactic treatment, providing indirect comparative benchmark data |

---

## Literature Evidence

Currently no related literature available from the PubMed query conducted on 2026-03-09 (result count: 0). This represents a data gap — a supplementary manual search of PubMed using terms such as "flunarizine migraine prophylaxis" is strongly recommended, as published RCTs and meta-analyses for this indication are known to exist in the broader literature.

---

## Philippines Market Information

Flunarizine is **not currently registered** with the FDA Philippines. No drug authorisation records were retrieved.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|------------|-------------------|
| — | — | — | No registrations on file |

A market-entry regulatory submission would be required before commercial use in the Philippines.

---

## Safety Considerations

Detailed local warning and contraindication data (e.g., FDA Philippines package insert) were not available at the time of this report. Based on globally available prescribing information, clinicians should be aware of the following known safety signals associated with Flunarizine:

- **Extrapyramidal side effects**: Flunarizine carries D2 receptor antagonist activity and can cause drug-induced parkinsonism, tardive dyskinesia, or depression, particularly with long-term use or in elderly patients.
- **Sedation and weight gain**: Antihistaminergic properties contribute to somnolence and appetite stimulation; relevant for patient counselling and adherence.
- **Depression risk**: Use should be avoided or carefully monitored in patients with a history of depressive episodes.
- **Drug interactions**: No DDI data was retrieved from the automated query. The Phase 1 pharmacokinetic trial (NCT00752466) suggests a clinically relevant interaction with Topiramate warrants attention.

> Please refer to the full package insert and consult local regulatory guidance for comprehensive safety information before initiating use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Flunarizine has a robust, decades-long global track record as a migraine prophylactic agent with multiple completed RCTs and head-to-head comparisons against established first-line drugs (Topiramate, Propranolol, Amitriptyline). The TxGNN prediction score of 99.12% reflects strong knowledge-graph support, and the mechanistic basis — T-type calcium channel blockade and CSD suppression — directly maps onto migraine pathophysiology. The principal barrier is the absence of Philippines FDA registration, not a lack of evidence.

**To proceed, the following is needed:**

- **Philippines FDA registration pathway assessment**: Determine whether a full New Drug Application or an abbreviated bridging submission is required; gather relevant dossiers from markets where Flunarizine is already approved (e.g., EU, Japan, India).
- **Supplementary PubMed literature review**: Conduct a manual search to retrieve published meta-analyses and systematic reviews on Flunarizine for migraine prophylaxis, as the automated query returned zero results despite known literature existing.
- **Local safety data retrieval**: Download and parse the full package insert (where available from WHO or reference markets) to populate the key warnings, contraindications, and DDI sections before any S1 safety review.
- **Mechanism of action data (MOA)**: Query the DrugBank API for DB04841 to obtain the full structured MOA record, which will strengthen the mechanistic link analysis.
- **Pharmacoeconomic assessment**: Given the migraine prevention landscape in the Philippines, a cost-effectiveness comparison against Topiramate and Propranolol (both likely already registered and generic) should be conducted to define the market positioning rationale.
- **Paediatric strategy**: Monitor the completion of NCT07354126 (Flunarizine vs Propranolol in children aged 8–15) as it may support a paediatric label extension if Philippines registration proceeds.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

