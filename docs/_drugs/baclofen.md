---
layout: default
title: Baclofen
parent: 僅模型預測 (L5)
nav_order: 37
evidence_level: L5
indication_count: 2
---

# Baclofen
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Baclofen: From Spasticity to Attention Deficit-Hyperactivity Disorder

## One-Sentence Summary

Baclofen is a GABA-B receptor agonist classically used for the treatment of spasticity in neurological conditions. The TxGNN model predicts it may be effective for **Attention Deficit-Hyperactivity Disorder (ADHD)** (Rank #1; score: 99.32%), with **0 clinical trials** and **10 publications** providing only indirect mechanistic support; and secondarily for **Nicotine Dependence** (Rank #2; score: 99.19%), which carries stronger evidence with **3 Phase 2 clinical trials** and **20 publications**. These two predictions differ substantially in evidence maturity and should be evaluated independently.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Spasticity (Baclofen not registered in the Philippines) |
| Predicted New Indication | Attention Deficit-Hyperactivity Disorder (ADHD) |
| TxGNN Prediction Score | 99.32% |
| Evidence Level | L4 (Preclinical / mechanistic studies only) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from this evidence pack. Based on established pharmacological knowledge, Baclofen is a selective GABA-B receptor agonist. It acts on pre- and post-synaptic GABA-B receptors in the central nervous system, suppressing neuronal excitability and inhibiting the release of excitatory neurotransmitters — including dopamine — particularly within the mesolimbic pathways.

The theoretical connection to ADHD rests on Baclofen's ability to dampen excessive dopaminergic tone in the ventral tegmental area (VTA) and modulate frontal-striatal circuits that govern attention, impulse control, and executive function — pathways consistently implicated in ADHD pathophysiology. The repurposing rationale from this evidence pack describes this as "highly speculative" with no direct neuroimaging or pharmacological human studies yet supporting it. Critically, conventional ADHD treatments (stimulants such as methylphenidate) work by *enhancing* dopaminergic and noradrenergic signalling, which is mechanistically the opposite of what Baclofen does; this raises a flag about potential worsening of attentional symptoms.

The most concrete indirect evidence comes from Baclofen's documented use in Tourette Syndrome — a neurodevelopmental disorder with up to 60% ADHD comorbidity — where baclofen has been used for tic suppression. The TxGNN knowledge graph model likely captured these shared neurodevelopmental substrates when generating this prediction, rather than direct pharmacological evidence for ADHD per se.

---

## Clinical Trial Evidence

Currently no related clinical trials are registered for Baclofen in ADHD.

---

## Literature Evidence (ADHD)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35345730](https://pubmed.ncbi.nlm.nih.gov/35345730/) | 2022 | Systematic Review | Cureus | Reviews behavioural interventions, antipsychotics, and alpha agonists for tics in Tourette's; ADHD is a primary comorbidity; no direct Baclofen-ADHD assessment |
| [26366961](https://pubmed.ncbi.nlm.nih.gov/26366961/) | 2015 | Review | Clin Neuropharmacology | Mood stabilisers in paediatric autism spectrum disorders with ADHD-like behavioural problems; contextual background for neurodevelopmental pharmacotherapy |
| [24295630](https://pubmed.ncbi.nlm.nih.gov/24295630/) | 2013 | Review | Int Rev Neurobiology | Emerging Tourette treatments including pipeline agents; ADHD comorbidity management reviewed; highlights unmet clinical need |
| [10342599](https://pubmed.ncbi.nlm.nih.gov/10342599/) | 1999 | Review | J Child Neurology | 450 Tourette patients treated with baclofen and botulinum toxin; baclofen used in a ADHD-comorbid population; only indirect evidence for Baclofen-ADHD |
| [21300040](https://pubmed.ncbi.nlm.nih.gov/21300040/) | 2011 | Animal Study | Brain Research | EEG responses to GABA-B agonists (including baclofen) in spontaneously hypertensive rat (SHR) ADHD model; provides mechanistic background for GABAergic modulation in ADHD-like circuits |
| [24062084](https://pubmed.ncbi.nlm.nih.gov/24062084/) | 2014 | Animal Study | Psychopharmacology | Guanfacine (α2A agonist) reduces impulsive decision-making via ventral hippocampus; contextually relevant — highlights GABAergic vs. noradrenergic approaches to impulsivity |
| [24496320](https://pubmed.ncbi.nlm.nih.gov/24496320/) | 2014 | Animal Study | Neuropsychopharmacology | Anterior cingulate cortex and basolateral amygdala contributions to effortful decision-making deficits in ADHD-like models; no direct Baclofen testing |
| [24103016](https://pubmed.ncbi.nlm.nih.gov/24103016/) | 2013 | Animal Study | Eur J Neuroscience | Habenula regulates monoaminergic neurotransmission and social play in rats; mechanistic background for GABAergic modulation of reward and attention circuits |
| [11393328](https://pubmed.ncbi.nlm.nih.gov/11393328/) | 2001 | Review | Paediatric Drugs | Tourette syndrome management; clonidine as first-line agent; Baclofen listed as a used option for tic suppression in patients with ADHD comorbidity |
| [30122296](https://pubmed.ncbi.nlm.nih.gov/30122296/) | 2019 | Review | L'Encephale | Off-label methylphenidate use in adult ADHD; highlights the persistent gap in approved treatments and the practice of framed off-label prescribing |

---

## Additional Predicted Indication: Nicotine Dependence (Rank #2)

> This second prediction carries substantially stronger evidence than ADHD and is presented here for completeness. TxGNN score: **99.19%** | Evidence Level: **L2** | Decision Stage: **Research Question**

**Mechanistic rationale:** Baclofen acts on GABA-B receptors in the VTA to inhibit dopamine neuron firing, thereby attenuating the nicotine-induced surge in mesolimbic dopamine — the core neurobiological reward signal driving nicotine addiction. This mechanism has been directly demonstrated in multiple animal studies and parallels Baclofen's evidence base in alcohol use disorder (AUD), where it is approved in France. The GABAergic reward-attenuation mechanism appears transdiagnostic across substance use disorders.

### Clinical Trial Evidence (Nicotine Dependence)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT01821560](https://clinicaltrials.gov/study/NCT01821560) | Phase 2 | **Completed** | 44 | Used perfusion fMRI to examine Baclofen's effects on brain and behavioural responses to smoking cues in cigarette smokers; only completed trial — highest direct relevance for efficacy signals |
| [NCT00257894](https://clinicaltrials.gov/study/NCT00257894) | Phase 2 | Terminated | 41 | Assessed Baclofen's effect on smoking urge, withdrawal, and reinforcement in moderate-to-heavy smokers; terminated after 41 enrolments (reason unreported); safety and preliminary data may be available |
| [NCT01228994](https://clinicaltrials.gov/study/NCT01228994) | Phase 2 | Terminated | 6 | Tested the GABAergic hypothesis of nicotine dependence; terminated very early (only 6 subjects), limiting statistical validity; conceptual proof-of-concept value only |

### Literature Evidence (Nicotine Dependence)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24553576](https://pubmed.ncbi.nlm.nih.gov/24553576/) | 2014 | Animal Study | Psychopharmacology | Baclofen attenuates nicotine rewarding properties and withdrawal manifestations in rodents; supports direct pharmacological mechanism |
| [18682277](https://pubmed.ncbi.nlm.nih.gov/18682277/) | 2008 | Animal Study | Neuroscience Letters | Baclofen (3 mg/kg) reduces nicotine-induced conditioned place preference and discriminative effects in rats; provides dose-effect data for mechanistic understanding |
| [19250803](https://pubmed.ncbi.nlm.nih.gov/19250803/) | 2009 | Animal Study | Eur Neuropsychopharmacology | Baclofen prevents drug-induced reinstatement of nicotine-seeking behaviour and nicotine place preference in rodents; directly relevant relapse prevention data |
| [23500668](https://pubmed.ncbi.nlm.nih.gov/23500668/) | 2013 | Animal Study | Prog Neuropsychopharmacol Biol Psychiatry | Baclofen prevents mecamylamine-precipitated nicotine withdrawal; α4β2 nicotinic receptor density modulated; elucidates receptor-level withdrawal mechanism |
| [25868070](https://pubmed.ncbi.nlm.nih.gov/25868070/) | 2015 | Conference Abstract (Pilot RCT) | Neuropsychopharmacology | Baclofen as pharmacotherapy for concurrent alcohol and nicotine dependence; double-blind, placebo-controlled randomised pilot; dual substance use design |
| [24971600](https://pubmed.ncbi.nlm.nih.gov/24971600/) | 2015 | Review | Neuropharmacology | GABA-B receptors as therapeutic targets for substance use disorders; positive allosteric modulators discussed; comprehensive preclinical evidence summary |
| [29250815](https://pubmed.ncbi.nlm.nih.gov/29250815/) | 2018 | Review | Pharmacotherapy | Current and emerging pharmacotherapies for tobacco cessation; Baclofen discussed in context of GABAergic approaches; NRT limitations highlighted |
| [17338593](https://pubmed.ncbi.nlm.nih.gov/17338593/) | 2007 | Review | CNS Drugs | Pharmacotherapy of dual substance abuse (alcohol + nicotine); single-drug therapies reviewed; Baclofen relevant for co-occurring dependence |
| [38555115](https://pubmed.ncbi.nlm.nih.gov/38555115/) | 2024 | Review (Drug Repurposing) | Int Rev Neurobiology | Repurposing drugs for alcohol use disorder; Baclofen listed among approved AUD medications in France; shared GABAergic mechanism with nicotine reinforcement suppression |
| [28919445](https://pubmed.ncbi.nlm.nih.gov/28919445/) | 2018 | Review | Prog Neuropsychopharmacol Biol Psychiatry | Cognitive effects of addictolytic medications including Baclofen; relevant for assessing cognitive risk-benefit profile in nicotine cessation treatment |

---

## Philippines Market Information

Baclofen is **not currently registered in the Philippines**. There are no active licenses on record with the Food and Drug Administration of the Philippines (FDA Philippines).

> **Note for decision-makers:** Before any clinical or research use in the Philippines, a product registration application would be required. Baclofen is available as a generic in many international markets (oral tablets 10 mg, 25 mg; intrathecal formulation). Its regulatory status in other jurisdictions (e.g., EMA-approved in the EU for spasticity; approved in France for alcohol use disorder under specific conditions) could support a bridging application strategy.

---

## Safety Considerations

No key warnings, contraindications, or drug interaction data are available in this evidence pack for the Philippines market.

> Please refer to the package insert and approved prescribing information from reference regulatory agencies (EMA, US FDA) for safety information. Known class-level concerns with Baclofen include: CNS depression, sedation, respiratory depression at high doses, abrupt withdrawal syndrome (potentially fatal — gradual dose tapering required), and particular caution in renal impairment (primary renal excretion).

---

## Conclusion and Next Steps

### Primary Prediction — ADHD

**Decision: Hold**

**Rationale:**
The ADHD prediction is mechanistically speculative and rests entirely on indirect evidence from Tourette syndrome and animal circuit models. No clinical trials have tested Baclofen directly for ADHD, and the direction of pharmacological action (dopamine suppression) is theoretically inconsistent with established ADHD treatment principles (dopamine/noradrenaline enhancement). The TxGNN model likely detected shared neurodevelopmental signatures rather than direct therapeutic applicability.

**To proceed, the following is needed:**
- A dedicated mechanistic hypothesis paper or preclinical study directly testing Baclofen in validated ADHD animal models (e.g., SHR rats, dopamine transporter knock-down models)
- Neuroimaging or pharmacodynamic data in human subjects with ADHD assessing GABAergic modulation of prefrontal circuits
- Safety profile review specifically addressing whether GABA-B agonism worsens attentional performance

---

### Secondary Prediction — Nicotine Dependence

**Decision: Proceed with Guardrails**

**Rationale:**
Nicotine dependence has a clear and well-supported mechanistic rationale (GABA-B–mediated attenuation of mesolimbic dopamine reward), confirmed preclinical data across multiple animal paradigms, and one completed Phase 2 clinical trial (NCT01821560, n=44). The two terminated trials reflect feasibility and recruitment challenges rather than safety signals. This prediction is further supported by Baclofen's approved use in alcohol use disorder in France, pointing to a transdiagnostic GABAergic mechanism across addictive disorders.

**To proceed, the following is needed:**
- Full results from NCT01821560 (fMRI + behavioural outcomes) should be obtained and reviewed
- A feasibility study scoping Philippines-specific tobacco cessation need and patient population
- Pharmacokinetic data for the oral formulation in Asian populations (CYP profile considerations)
- A regulatory pathway assessment: Baclofen is not registered in the Philippines, so a Phase 2 investigator-initiated trial would require both product registration and ethics approval
- Safety monitoring plan addressing sedation, withdrawal risk, and renal function in a nicotine-dependent population

---

*⚠️ Disclaimer: This report is for research reference only and does not constitute medical advice. All drug repurposing candidates require clinical validation before therapeutic application. Data cutoff: 2026-04-04.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

