---
layout: default
title: Alprazolam
parent: 僅模型預測 (L5)
nav_order: 19
evidence_level: L5
indication_count: 3
---

# Alprazolam
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Alprazolam: From Anxiety Disorders to Insomnia

## One-Sentence Summary

Alprazolam is a benzodiazepine sedative-hypnotic agent internationally prescribed for anxiety disorders and panic disorder.
The TxGNN model predicts it may be effective for **Insomnia (disease)**, with **7 clinical trials** and **18 publications** currently supporting this direction.
While mechanistic plausibility is strong through GABA-A receptor potentiation, current evidence is largely observational and lacks dedicated large-scale primary insomnia RCTs.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Anxiety disorders, panic disorder (international standard; no Philippines registration on record) |
| Predicted New Indication | Insomnia (disease) |
| TxGNN Prediction Score | 99.81% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not formally recorded in this regulatory dataset. Based on established pharmacology, alprazolam is a triazolobenzodiazepine that acts as a positive allosteric modulator of the GABA-A receptor. By enhancing inhibitory GABAergic neurotransmission across cortical and limbic circuits, it reduces neuronal excitability — the same core mechanism shared by approved hypnotic benzodiazepines such as triazolam and temazepam. In practice, this translates to shortened sleep onset latency and increased total sleep time.

Anxiety and insomnia share overlapping neurobiological substrates: both involve hyperactivation of the amygdala, locus coeruleus, and the hypothalamic-pituitary-adrenal (HPA) axis. Since chronic insomnia frequently co-occurs with anxiety disorders, alprazolam's anxiolytic action may naturally extend to improving sleep continuity in patients with comorbid hyperarousal. Multiple real-world studies confirm that alprazolam is commonly prescribed for sleep disturbances, particularly among the elderly, hemodialysis patients, and post-COVID populations — lending further credibility to the TxGNN prediction.

However, alprazolam's half-life of approximately 11–15 hours is considerably longer than that of benzodiazepines specifically approved as hypnotics, raising concerns about residual morning sedation, next-day cognitive impairment, and physical dependence with repeated dosing. No large placebo-controlled trial has used primary insomnia as the main efficacy endpoint for alprazolam, distinguishing it from agents with formal hypnotic approval. The TxGNN prediction is therefore mechanistically well-founded but clinically constrained by these safety and evidence-level gaps.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02648776](https://clinicaltrials.gov/study/NCT02648776) | N/A (Observational) | Unknown | 1,400 | Large prospective cohort at a Taiwanese academic medical center evaluating risk-benefit profiles of commonly prescribed hypnotics — including alprazolam — in elderly patients with sleep disorders; examines long-term efficacy, safety, pharmacokinetics, and pharmacogenetics |
| [NCT01584440](https://clinicaltrials.gov/study/NCT01584440) | Phase 2 | Completed | 220 | Randomized double-blind placebo-controlled trial of AVP-923 (dextromethorphan/quinidine) for agitation in Alzheimer's disease; benzodiazepine-class sedative-hypnotic context relevant to neuropsychiatric insomnia management |
| [NCT03327506](https://clinicaltrials.gov/study/NCT03327506) | Phase 4 | Unknown | 128 | Randomized trial comparing hypnosis versus alprazolam premedication for perioperative anxiety in laparoscopic gynecological surgery; directly tests alprazolam as a sedating agent, though focused on pre-operative rather than chronic insomnia |
| [NCT00266409](https://clinicaltrials.gov/study/NCT00266409) | Phase 4 | Completed | 418 | Open-label multicenter RCT comparing Niravam™ (alprazolam orally disintegrating tablet) plus SSRI/SNRI versus SSRI/SNRI alone in GAD/panic disorder; anxiety-insomnia overlap provides indirect support for sedative benefit |
| [NCT04572750](https://clinicaltrials.gov/study/NCT04572750) | N/A | Completed | 170 | Electronic self-management intervention to promote benzodiazepine (Xanax/Ativan) cessation in veterans; directly addresses the challenge of long-term BZD use for insomnia and provides evidence on safe tapering strategies |
| [NCT01146600](https://clinicaltrials.gov/study/NCT01146600) | Phase 2 | Completed | 26 | Clarithromycin for central hypersomnia (pathological excessive sleep); represents the mechanistic inverse of insomnia, providing contrast for understanding GABAergic modulation in sleep regulation |
| [NCT01893632](https://clinicaltrials.gov/study/NCT01893632) | Phase 2 | Terminated | 2 | Gabapentin versus benzodiazepines for BZD dependence management; terminated early due to extremely poor enrollment (2 of intended ~60 subjects), highlighting the clinical difficulty of managing chronic benzodiazepine use in the insomnia/anxiety population |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39183410](https://pubmed.ncbi.nlm.nih.gov/39183410/) | 2024 | Observational Study | Medicine | In 116 coronary heart disease patients with insomnia, alprazolam served as the active control; integrative therapy (Du Meridian moxibustion + ear acupuncture) outperformed alprazolam alone on cardiac function and serum neurotransmitter levels, providing direct real-world efficacy data for alprazolam in comorbid insomnia |
| [33403184](https://pubmed.ncbi.nlm.nih.gov/33403184/) | 2020 | Comparative Study | Cureus | Head-to-head comparison of alprazolam versus melatonin for sleep disturbances in end-stage renal disease (ESRD) hemodialysis patients; evaluates subjective/objective sleep quality, daytime sleepiness, and fatigue — the most directly applicable alprazolam insomnia efficacy study in this pack |
| [37801512](https://pubmed.ncbi.nlm.nih.gov/37801512/) | 2023 | Preclinical Study | Aging | Repeated alprazolam administration (24 days) in mice induced mitochondrial dysfunction and attenuated hippocampus-dependent memory consolidation; proteomic analysis identified 439 differentially expressed proteins, mechanistically grounding concerns about cognitive side effects with chronic hypnotic use |
| [36692463](https://pubmed.ncbi.nlm.nih.gov/36692463/) | 2023 | Systematic Review | Acta Pharmaceutica | Meta-analysis of multiple tranquilizers (including benzodiazepines) in elderly patients with chronic non-communicable diseases; identifies safe dose ranges, key adverse effects, and optimal drug selection — directly applicable to prescribing alprazolam for insomnia in older adults |
| [37984023](https://pubmed.ncbi.nlm.nih.gov/37984023/) | 2024 | Epidemiological Study | Value in Health Regional Issues | 10-year predictive model of benzodiazepine prescribing trends for anxiety, insomnia, and mood disorders; documents population-level risks including memory loss, Alzheimer's disease association, physical dependence, and falls in elderly patients |
| [38363887](https://pubmed.ncbi.nlm.nih.gov/38363887/) | 2024 | Cross-sectional Study | Medicine | Survey of insomnia prevalence, severity (ISI scale), and risk factors among COVID-19 survivors (December 2022–February 2023); establishes post-COVID insomnia as a significant, growing unmet medical need |
| [25532388](https://pubmed.ncbi.nlm.nih.gov/25532388/) | 2014 | Real-world Analysis | China Journal of Chinese Materia Medica | Real-world medication use in 1,067 insomnia patients across 20 Chinese hospital information systems; documents high rates of cardiovascular and cerebrovascular comorbidities and prevalent Western medication (including benzodiazepine) prescribing in insomnia |
| [15341891](https://pubmed.ncbi.nlm.nih.gov/15341891/) | 2004 | Observational Study | Sleep Medicine | Analysis of hypnotic prescription patterns in a large managed-care population; documents a decade-long decline in dedicated hypnotic prescribing and the shift toward non-hypnotic medications (including benzodiazepines) as off-label sleep aids |
| [23330992](https://pubmed.ncbi.nlm.nih.gov/23330992/) | 2013 | Review | Expert Opinion on Drug Metabolism & Toxicology | Comprehensive pharmacokinetic review of anxiolytics including alprazolam; discusses elimination half-life, active metabolites, and CYP3A4 interactions — critical for understanding residual morning sedation risk when alprazolam is used as a hypnotic |
| [35041261](https://pubmed.ncbi.nlm.nih.gov/35041261/) | 2022 | RCT | Brain and Behavior | Eszopiclone improves both sleep quality and cognitive function in elderly Alzheimer's patients with sleep disorders; provides a comparative benchmark for non-BZD hypnotic alternatives that could be evaluated alongside alprazolam |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Alprazolam's GABA-A potentiating mechanism is biologically well-suited for insomnia management, and Level 3 observational evidence from real-world populations (hemodialysis patients, coronary heart disease patients with insomnia, elderly cohorts) supports its off-label sedative-hypnotic use; however, the absence of any dedicated primary insomnia RCT, the long half-life raising dependence and residual sedation concerns, and the drug's complete absence from the Philippines market collectively require careful guardrails before any clinical recommendation can be made.

**To proceed, the following is needed:**
- Obtain the full package insert (SPC/PI) to formally document contraindications, black-box warnings, and significant drug interactions, particularly with CYP3A4 inhibitors (e.g., azole antifungals, macrolide antibiotics)
- Identify or commission a prospective, placebo-controlled study with primary insomnia as the primary efficacy endpoint in an appropriate patient population
- Initiate a Philippines FDA (Food and Drug Administration) registration pathway assessment, including determination of applicable drug scheduling (likely Schedule IV controlled substance)
- Develop a risk management and pharmacovigilance plan addressing physical dependence liability, rebound insomnia upon discontinuation, residual morning sedation, and fall risk in elderly patients
- Evaluate CYP3A4 pharmacogenomic variability in Filipino populations to guide dosing recommendations and minimize inter-individual variability in drug exposure
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

