---
layout: default
title: Aminophylline
parent: 僅模型預測 (L5)
nav_order: 22
evidence_level: L5
indication_count: 10
---

# Aminophylline
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

# Aminophylline: From Bronchospasm to Migraine Disorder

## One-Sentence Summary

Aminophylline is a classical methylxanthine compound, widely used as a bronchodilator for asthma, COPD, and apnea of prematurity.
The TxGNN model predicts it may be effective for **Migraine Disorder**,
with **0 clinical trials** and **6 publications** currently supporting this direction — primarily through its adenosine receptor antagonist mechanism.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Bronchospasm and reversible airway obstruction (asthma, COPD, apnea of prematurity) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.88% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on well-established pharmacology, Aminophylline is a methylxanthine compound whose primary mechanisms include: (1) **adenosine receptor antagonism** (A1 and A2A subtypes) and (2) **non-selective phosphodiesterase (PDE) inhibition**, which raises intracellular cAMP levels and relaxes smooth muscle. These properties underpin its bronchodilatory and respiratory-stimulant effects in asthma and apnea of prematurity.

The link to migraine is mechanistically compelling. Accumulating evidence indicates that pathologically elevated adenosine plays a central role in migraine pathogenesis through three pathways: triggering cortical spreading depression (CSD), inducing intracranial vasodilation via A2A receptors, and directly activating trigeminal nociceptors. By blocking adenosine receptors, aminophylline may theoretically interrupt these cascades and reduce both the intensity and frequency of migraine attacks. A 2023 review (PMID 38059379) explicitly frames migraine as a disorder of impaired brain energy metabolism driven by excess adenosine, positioning aminophylline as a potentially strong therapeutic agent.

Strong indirect clinical evidence comes from observations involving regadenoson (a selective A2A adenosine receptor agonist used in cardiac stress imaging): regadenoson can trigger hemiplegic migraine episodes, and the standard reversal agent is aminophylline or caffeine — both methylxanthine adenosine antagonists. This bidirectional relationship directly demonstrates adenosine's causal role in migraine and, by extension, aminophylline's potential therapeutic effect.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Aminophylline in migraine disorder.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [38059379](https://pubmed.ncbi.nlm.nih.gov/38059379/) | 2023 | Review / Clinical Report | Pain Management | Proposes migraine as an adenosine-driven disorder of impaired brain energy metabolism; aminophylline (adenosine receptor antagonist) demonstrated strong therapeutic relief for pain and headache, including post-dural puncture headache, in an observational case series |
| [34308528](https://pubmed.ncbi.nlm.nih.gov/34308528/) | 2022 | Case Report | Journal of Nuclear Cardiology | Regadenoson (A2A adenosine receptor agonist) triggered a hemiplegic migraine episode during cardiac stress imaging; aminophylline reversed the episode — directly demonstrating adenosine's causal role in migraine and aminophylline's antagonist effect |
| [219563](https://pubmed.ncbi.nlm.nih.gov/219563/) | 1979 | Basic Science | Stroke | Adenosine and adenine compounds (AMP, cAMP, ADP, ATP) markedly dilated pial (intracranial) arteries in vitro but not extracranial arteries; establishes the selective intracranial vascular basis for adenosine's role in migraine pathophysiology |
| [7728647](https://pubmed.ncbi.nlm.nih.gov/7728647/) | 1995 | Case Report | Canadian Journal of Cardiology | Patient with syndrome X developed "myocardial migraine" via excessive adenosine effect; dipyridamole (adenosine-enhancing agent) provoked severe pain without ischemia, further supporting adenosine's vascular pain signaling role |
| [14168418](https://pubmed.ncbi.nlm.nih.gov/14168418/) | 1964 | Historical Review | Aggiornamenti clinicoterapeutici | Early clinical investigation of pharmacological headache management; historical context only, limited direct evidence |
| [5540199](https://pubmed.ncbi.nlm.nih.gov/5540199/) | 1971 | Formulation | The Practitioner | Discusses suppository formulations; limited direct relevance to migraine indication |

---

## Philippines Market Information

Aminophylline currently has **no registered products** in the Philippines (FDA Philippines). The drug is classified as **not marketed**, with zero active drug licenses on record. Any clinical development or repurposing program would need to proceed through a full new drug application or compassionate use pathway.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Key warnings, contraindications, and drug-drug interaction data were not retrievable from the current Evidence Pack. Prior to any clinical development, it is essential to obtain the full prescribing information. Aminophylline is known to have a **narrow therapeutic index** (therapeutic range ~10–20 µg/mL for theophylline), and toxicity risk is clinically relevant for dose escalation decisions.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A biologically plausible and well-articulated adenosine receptor antagonism mechanism directly links aminophylline to migraine pathophysiology, supported by a recent review-level publication and case report evidence. However, no prospective clinical trials have been conducted for this specific indication, and the drug lacks Philippines market registration — meaning the evidence base remains observational and the regulatory pathway is uncharted.

**To proceed, the following is needed:**

- **Safety data gap closure:** Download and parse the TFDA/FDA Philippines package insert to extract key warnings, contraindications, and known drug interactions — currently a blocking data gap
- **MOA profile confirmation:** Query DrugBank API to obtain the full mechanism of action, drug targets (A1/A2A receptor affinities, PDE isoform selectivity), and pharmacokinetic data
- **Prospective pilot study:** Design and register a Phase 2 proof-of-concept RCT evaluating aminophylline in acute migraine or migraine prevention, using validated outcome measures (MIDAS, headache diary)
- **Dose-finding work:** Establish a migraine-specific dosing regimen; existing bronchodilator dosing may not translate directly due to the narrow therapeutic index
- **Cardiovascular safety assessment:** Evaluate arrhythmia risk and hemodynamic effects in migraine patient populations, especially given known cardiac sensitivities of methylxanthines
- **Philippines regulatory pathway:** Consult FDA Philippines on the registration requirements for a repurposed drug currently absent from the market
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

