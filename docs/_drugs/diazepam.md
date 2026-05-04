---
layout: default
title: Diazepam
parent: 僅模型預測 (L5)
nav_order: 103
evidence_level: L5
indication_count: 10
---

# Diazepam
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

# Diazepam: From Anxiety and Seizure Disorders to Insomnia

## One-Sentence Summary

Diazepam is a classic benzodiazepine historically prescribed for anxiety disorders, seizures, muscle spasms, and alcohol withdrawal management. The TxGNN model predicts it may be effective for **Insomnia**, with **5 graded clinical trials** and **7 key publications** directly supporting this pharmacological direction — though the current clinical literature largely focuses on managing benzodiazepine *discontinuation* rather than developing new therapeutic uses. Given diazepam's well-established short-term hypnotic mechanism, this prediction is pharmacologically grounded, but carries significant long-term safety risks that necessitate strict clinical guardrails.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines market authorization; no approved indication data available |
| Predicted New Indication | Insomnia |
| TxGNN Prediction Score | 99.99997% |
| Evidence Level | L2 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the regulatory database. Based on known pharmacological information, Diazepam is a benzodiazepine — a class that acts as a positive allosteric modulator of GABA-A receptors. By binding to the benzodiazepine recognition site on GABA-A receptors, diazepam increases the frequency of chloride ion channel opening in response to endogenous GABA, enhancing central inhibitory neurotransmission. This is the basis of its well-recognized sedative, anxiolytic, anticonvulsant, and muscle-relaxant effects.

The mechanistic connection to insomnia is direct and robust. Diazepam shortens sleep latency (time to fall asleep) and reduces nocturnal awakenings by dampening arousal-promoting neural circuits — precisely the two core deficits in insomnia. This is not a novel hypothesis: clinical trials from the 1980s already compared diazepam head-to-head against other hypnotics (e.g., PMID 6113175), and current prescribing guidelines acknowledge benzodiazepines as a pharmacological option for short-term insomnia. A 2024 review in *Bioorganic Chemistry* (PMID 39581171) explicitly identifies diazepam as a prototypical GABA-A modulator with clinical applications in insomnia.

However, the repurposing context carries an important mechanistic paradox. Long-term diazepam use suppresses REM sleep and slow-wave sleep, causing non-restorative sleep and potentially worsening the underlying disorder. A 2022 *Nature Neuroscience* study (PMID 35228700) demonstrated that chronic diazepam exposure induces microglial spine engulfment and cognitive impairment in mice via TSPO. This dual nature — effective short-term hypnotic, harmful long-term sleep disruptor — explains why contemporary clinical research is dominated by trials on how to *safely discontinue* benzodiazepines in insomnia patients, rather than validating new uses.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02831894](https://clinicaltrials.gov/study/NCT02831894) | Phase 2 | Completed | 74 | Evaluated tapering pace for benzodiazepine/Z-drug discontinuation in insomnia; confirms that >65% of hypnotic-prescribed patients use the drugs for >1 year, and >30% for >5 years — directly establishing the clinical footprint of this drug class in chronic insomnia |
| [NCT04050176](https://clinicaltrials.gov/study/NCT04050176) | Phase 3 | Active, Not Recruiting | 260 | RCT comparing blinded vs open-label benzodiazepine tapering combined with CBT-I for insomnia; validates benzodiazepine receptor agonist use in chronic insomnia and tests structured discontinuation strategies |
| [NCT04751851](https://clinicaltrials.gov/study/NCT04751851) | Randomized Trial | Completed | 128 | Assessed Acceptance and Commitment Therapy for benzodiazepine withdrawal in adults with hypnotic-dependent insomnia; explicitly targets "hypnotic-dependent insomnia" as the study population |
| [NCT03461042](https://clinicaltrials.gov/study/NCT03461042) | Phase 4 | Completed | 17 | Double-blind placebo-controlled RCT examining ramelteon co-administration to facilitate benzodiazepine dose reduction in chronic insomnia patients |
| [NCT03687086](https://clinicaltrials.gov/study/NCT03687086) | Observational Intervention | Completed | 188 | Novel mechanism-targeted program to help older adults discontinue sleep medications; study population comprised chronic benzodiazepine/hypnotic users with insomnia |
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | Observational | Unknown | 1,400 | Taiwanese academic medical center cohort studying prescribing patterns, efficacy, safety, pharmacokinetics, and pharmacogenetics of hypnotics (including benzodiazepines) in elderly insomnia patients — most geographically relevant to Philippines context |
| [NCT02281175](https://clinicaltrials.gov/study/NCT02281175) | Randomized Trial | Completed | 114 | PASSE-65+ psychosocial intervention for gradual benzodiazepine weaning in older adults; notes BZDs are "widely used to treat anxiety, insomnia, and depression" with serious long-term adverse effect concerns |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [6113175](https://pubmed.ncbi.nlm.nih.gov/6113175/) | 1981 | RCT | J Int Med Res | Head-to-head double-blind RCT (n=100): lormetazepam 1mg vs **diazepam 5mg** in insomnia over 7 days; lormetazepam showed superior sleep onset and duration, but both drugs demonstrated clinically meaningful hypnotic activity — directly validates diazepam's efficacy in sleep disorders |
| [39581171](https://pubmed.ncbi.nlm.nih.gov/39581171/) | 2024 | Review | Bioorganic Chemistry | Comprehensive review of small-molecule GABA-A receptor modulators for neurological disorders; explicitly identifies **diazepam** as a well-known positive allosteric modulator with established clinical applications in insomnia, while noting side effects of sedation and dependence |
| [7525193](https://pubmed.ncbi.nlm.nih.gov/7525193/) | 1994 | Clinical Guideline | Drugs | Evidence-based guidelines for rational benzodiazepine use; identifies insomnia as a primary indication for the class, recommending short-term or intermittent use for transient insomnia and emphasizing risks of tolerance and dependence with prolonged treatment |
| [7595266](https://pubmed.ncbi.nlm.nih.gov/7595266/) | 1995 | Review | J Fam Pract | Systematic review of 10 clinical trials on benzodiazepine therapy for insomnia in community-dwelling elderly; documents sleep laboratory benefit but highlights absence of long-term effectiveness and increased injury risk data |
| [40570297](https://pubmed.ncbi.nlm.nih.gov/40570297/) | 2025 | Review | Sleep | Studied effects of chronic BZD/BZRA use on sleep macroarchitecture in older adults with insomnia; demonstrates that chronic use disrupts NREM slow oscillations and spindle coupling — mechanistically explains why long-term diazepam causes non-restorative sleep |
| [35228700](https://pubmed.ncbi.nlm.nih.gov/35228700/) | 2022 | Preclinical Study | Nature Neuroscience | Long-term **diazepam** treatment impairs structural plasticity of dendritic spines, causes microglial spine engulfment, and produces cognitive impairment in mice via TSPO; critical safety evidence for chronic use in insomnia patients |
| [6114852](https://pubmed.ncbi.nlm.nih.gov/6114852/) | 1981 | Review | Drugs | Comparative pharmacological review of triazolam vs longer-acting benzodiazepines (including **diazepam**) for insomnia; argues that longer half-life of diazepam makes it less suitable as a hypnotic than shorter-acting agents, informing formulation strategy for this indication |

---

## Philippines Market Information

Diazepam has no current market authorization in the Philippines. No drug license records are available.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | No registered products | — | Not currently authorized in the Philippines |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** TFDA package insert warnings, contraindications, and drug-drug interaction data were not retrievable at the time of this report (Data Gap: DG001, severity: Blocking). Obtaining this information is a prerequisite before proceeding to any safety evaluation stage.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Diazepam's GABA-A receptor mechanism directly and plausibly addresses the neurobiological basis of insomnia, and its short-term hypnotic efficacy is supported by historical RCT data and clinical guideline endorsement for transient insomnia. However, the drug is not registered in the Philippines, critical safety data (package insert warnings, contraindications, drug interactions) remain unavailable, and the contemporary clinical consensus increasingly favors discontinuing benzodiazepines in insomnia due to dependence risk and sleep architecture disruption — meaning repurposing scope must be tightly constrained to short-term, guideline-aligned use in clearly defined patient subgroups.

**To proceed, the following is needed:**

- **Retrieve FDA Philippines / TFDA package insert** for complete warnings, contraindications, and drug interaction data — this is a blocking prerequisite (DG001) for any formal safety evaluation
- **Obtain DrugBank MOA data** (DG002) to complete the mechanistic rationale section and support regulatory submission
- **Define the precise target population**: short-term insomnia only (e.g., ≤4 weeks), excluding elderly patients, individuals with history of substance abuse, respiratory compromise, and concurrent CNS depressant use
- **Establish Philippines regulatory pathway**: determine whether a new Drug Registration Application (DRA) with FDA Philippines is required, or whether compassionate use or existing regional market authorization (e.g., from neighboring markets) can be referenced
- **Design a risk mitigation protocol**: minimum effective dose, maximum treatment duration cap, structured tapering schedule, patient monitoring plan for tolerance and dependence indicators
- **Conduct a drug-drug interaction review** specific to common co-prescriptions in the Philippines insomnia population (e.g., antihypertensives, antidepressants, opioid analgesics)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

