---
layout: default
title: Midazolam
parent: 僅模型預測 (L5)
nav_order: 189
evidence_level: L5
indication_count: 1
---

# Midazolam
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

Using the `txgnn-pipeline` skill for context, and now generating the evaluation report from the Evidence Pack.

---

# Midazolam: From Procedural Sedation to Insomnia

## One-Sentence Summary

Midazolam is a short-acting benzodiazepine widely used for procedural sedation, anesthesia premedication, and acute seizure management.
The TxGNN model predicts it may be effective for **Insomnia**, with **1 completed Phase 4 RCT**, **multiple recruiting trials**, and **4 historical RCTs in the literature** supporting this direction.
However, its ultra-short half-life (1.5–2.5 hours) limits its clinical utility to sleep-onset insomnia, and it is currently not registered in the Philippines.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Procedural sedation / anesthesia premedication |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.74% |
| Evidence Level | L2 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

While the formal mechanism of action field has a data gap in the current Evidence Pack, the pharmacological basis is well established: midazolam is a **positive allosteric modulator of the GABA-A receptor** (benzodiazepine class). By binding to the benzodiazepine site on GABA-A receptors, it enhances GABAergic inhibitory neurotransmission and increases chloride ion influx, producing dose-dependent sedation, anxiolysis, and hypnotic effects. This is the **same mechanism** shared by all approved benzodiazepine hypnotics — flurazepam, triazolam, temazepam — making the TxGNN prediction pharmacologically sound.

The critical pharmacokinetic limitation is midazolam's extremely short half-life (1.5–2.5 hours). This makes it well-suited for **sleep-onset insomnia** (difficulty falling asleep) but poorly suited for **sleep-maintenance insomnia** (frequent awakenings, early-morning awakening), where a longer-acting agent is needed. Historical clinical trials from 1981–1990 directly demonstrated that oral midazolam (10–30 mg) was effective for sleep induction in hospitalized patients with secondary insomnia, with better tolerability than barbiturate combinations and no residual hangover effect.

Multiple perioperative RCTs have further compared midazolam head-to-head against dexmedetomidine on objective sleep quality outcomes (including polysomnography), consistently confirming that midazolam affects sleep architecture. Taken together, the mechanistic rationale and the volume of historical evidence strongly support the TxGNN prediction — the question is whether midazolam's narrow pharmacokinetic window and its dependence liability represent an acceptable clinical trade-off given that modern alternatives (non-benzodiazepine receptor agonists, orexin antagonists) now exist.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT02142595](https://clinicaltrials.gov/study/NCT02142595) | Phase 4 | Completed | 111 | Direct RCT comparing midazolam vs. dexmedetomidine on postoperative sleep quality in TURP patients; the most directly relevant completed trial |
| [NCT06407518](https://clinicaltrials.gov/study/NCT06407518) | N/A | Recruiting | 280 | Prospective double-blind RCT evaluating preoperative oral midazolam specifically in patients with sleep disturbance or anxiety undergoing colorectal cancer surgery; directly targets a sleep-disturbed population |
| [NCT04149626](https://clinicaltrials.gov/study/NCT04149626) | Phase 2 | Unknown | 60 | Compares dexmedetomidine vs. midazolam vs. remifentanil for sedation in orthopedic surgery; sleep quality included as a secondary outcome endpoint |
| [NCT05606315](https://clinicaltrials.gov/study/NCT05606315) | Phase 4 | Unknown | 285 | Remimazolam (same benzodiazepine receptor class) for ICU sedation in mechanically ventilated patients; provides class-level pharmacodynamic and safety data applicable to midazolam |
| [NCT01050699](https://clinicaltrials.gov/study/NCT01050699) | Phase 4 | Completed | 90 | Compares dexmedetomidine vs. standard sedation (including midazolam) on sleep and inflammatory cytokines in critically ill ALI/ARDS patients |
| [NCT01791296](https://clinicaltrials.gov/study/NCT01791296) | Phase 4 | Completed | 100 | Sleep protocol pilot RCT in ICU (2 sites); assesses feasibility, safety, and effect of nocturnal dexmedetomidine vs. standard benzodiazepine sedation on sleep outcomes |
| [NCT01966315](https://clinicaltrials.gov/study/NCT01966315) | N/A | Terminated | 5 | 24-hour polysomnography comparison of dexmedetomidine vs. midazolam on sleep quality and delirium incidence in ICU; terminated early due to low enrollment |
| [NCT00826553](https://clinicaltrials.gov/study/NCT00826553) | Phase 1 | Terminated | 6 | Polysomnographic assessment of GABA agonists (including midazolam) vs. α2 agonists on sleep stages and total sleep time; terminated early, but provides mechanistic sleep architecture data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [6138072](https://pubmed.ncbi.nlm.nih.gov/6138072/) | 1983 | RCT | Br J Clin Pharmacol | Double-blind RCT of midazolam 15 mg vs. Vesparax in 30 female insomnia patients (secondary to neuromuscular disease); midazolam was effective and better tolerated, with no hangover effect unlike the barbiturate comparator |
| [2229461](https://pubmed.ncbi.nlm.nih.gov/2229461/) | 1990 | Multicenter RCT | J Clin Psychopharmacol | Multicenter RCT (executive summary) of midazolam vs. flurazepam over 14 days in chronic insomnia; measured sleep quality, daytime performance, and plasma levels |
| [2121802](https://pubmed.ncbi.nlm.nih.gov/2121802/) | 1990 | RCT | J Clin Psychopharmacol | Randomized, double-blind, parallel-groups, multicenter study of midazolam vs. flurazepam in chronic insomnia; heterogeneous patient sample reflecting real-world benzodiazepine use; evaluated sleep, mood, and performance |
| [6120704](https://pubmed.ncbi.nlm.nih.gov/6120704/) | 1981 | Phase 2 RCT | Arzneimittel-Forschung | Dose-finding study of oral midazolam 10–30 mg in 75 hospitalized patients with mild-to-moderate insomnia secondary to musculoskeletal/neurological disorders; established optimal dose range for sleep induction |
| [2883820](https://pubmed.ncbi.nlm.nih.gov/2883820/) | 1986 | Clinical Review | Acta Psychiatr Scand Suppl | Review of benzodiazepine hypnotics including midazolam; discusses differential indications by insomnia subtype, pharmacokinetics, and dosing strategies |
| [36615100](https://pubmed.ncbi.nlm.nih.gov/36615100/) | 2022 | RCT (indirect) | J Clin Med | Pilot RCT comparing lemborexant vs. benzodiazepine for insomnia in high-risk pancreato-biliary patients post-endoscopy; highlights increased delirium risk with benzodiazepines — directly relevant to midazolam's safety profile in this indication |
| [21396773](https://pubmed.ncbi.nlm.nih.gov/21396773/) | 2011 | Animal Study | Pain | GABAergic neurons in the cingulate cortex are part of the neurobiological substrate for homeostatic sleep regulation; sciatic nerve ligation increased wakefulness and decreased NREM sleep — supports GABA-A as a mechanistic target for insomnia treatment |

---

## Safety Considerations

> Complete safety data (key warnings, contraindications, drug-drug interactions) is not available in the current Evidence Pack. Please refer to the official package insert for full safety information.

> **Important class-level concerns to address before proceeding:**
> - **Respiratory depression**: Dose-dependent, particularly with concomitant opioids or CNS depressants
> - **Dependence and tolerance**: Chronic use carries risk of physiological dependence — a critical consideration for an insomnia indication
> - **Next-day residual effects**: Less of a concern vs. long-acting benzodiazepines given short half-life, but individual variability exists
> - **CYP3A4 interactions**: Midazolam is a sensitive CYP3A4 substrate; inhibitors (e.g., azole antifungals, macrolides) can dramatically increase plasma levels

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The pharmacological rationale is strong and multiple historical RCTs (1981–1990) directly support midazolam's efficacy for sleep-onset insomnia; however, the drug is not registered in the Philippines (0 licenses), a complete safety profile is unavailable, midazolam's ultra-short half-life constrains its utility to a narrow insomnia subtype, and modern alternatives with more favorable safety profiles (non-benzodiazepine receptor agonists, orexin antagonists) have largely superseded benzodiazepines in insomnia treatment guidelines.

**To proceed, the following is needed:**

- **Safety data retrieval**: Download and parse the prescribing information PDF to obtain full warnings, contraindications, and DDI profile — especially CYP3A4 interactions and CNS depressant combinations
- **Regulatory pathway assessment**: Determine whether an oral formulation of midazolam is currently available or approvable in the Philippines, and identify the applicable regulatory pathway for a new indication
- **Formulation feasibility check**: Confirm that an oral dosage form (tablet or solution) suitable for outpatient insomnia use is either already registered or can be developed — IV/IM formulations are impractical for this indication
- **Comparative effectiveness review**: Conduct a systematic review positioning midazolam against current first-line insomnia agents (CBT-I, eszopiclone, zolpidem, lemborexant, suvorexant) within Philippine clinical practice guidelines
- **Benefit–risk assessment**: Formally weigh hypnotic efficacy against dependence liability, rebound insomnia risk, and the availability of safer alternatives before any clinical development decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

