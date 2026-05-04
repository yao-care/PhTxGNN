---
layout: default
title: Halothane
parent: 僅模型預測 (L5)
nav_order: 163
evidence_level: L5
indication_count: 6
---

# Halothane
{: .fs-9 }

證據等級: **L5** | 預測適應症: **6** 個
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

# Halothane: From General Anesthesia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Halothane is an inhalational general anesthetic historically used for surgical anesthesia induction and maintenance. The TxGNN model predicts it may be effective for **Manic Bipolar Affective Disorder**, but with **0 clinical trials** and only **5 tangentially related publications** (where halothane served merely as the anesthetic in animal studies of actual bipolar drugs), the evidence base is essentially nonexistent for this repurposing hypothesis.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | General anesthesia (induction and maintenance) |
| Predicted New Indication | Manic Bipolar Affective Disorder |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 (Model prediction only, no actual studies) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the evidence pack. Based on known pharmacology, Halothane is a halogenated hydrocarbon inhalational anesthetic that acts primarily through positive allosteric modulation of GABA-A receptors, along with inhibition of NMDA receptors and modulation of voltage-gated ion channels. These mechanisms produce generalized central nervous system depression, resulting in unconsciousness, amnesia, and immobility during surgical procedures.

The TxGNN model may have identified a signal based on Halothane's GABAergic activity, which could theoretically suppress the hyperexcitability associated with manic states. However, this connection is extremely tenuous. The GABA-A modulation produced by Halothane is a non-specific, general anesthetic effect — it suppresses all neural activity rather than selectively targeting the mood-regulatory circuits (prefrontal cortex, amygdala, striatal dopamine pathways) that are dysregulated in bipolar mania. Effective mood stabilizers such as lithium, valproate, and lamotrigine act through entirely different mechanisms (GSK-3β inhibition, inositol depletion, sodium channel modulation, histone deacetylase inhibition) that Halothane does not share.

Furthermore, Halothane is administered exclusively via inhalation during anesthesia, requires continuous monitoring and ventilatory support, carries significant risks of hepatotoxicity (halothane hepatitis), malignant hyperthermia, and cardiac arrhythmias, and has been largely replaced by safer anesthetics (sevoflurane, desflurane) worldwide. The route of administration and safety profile make it fundamentally incompatible with the chronic, outpatient management required for bipolar disorder. This prediction, while algorithmically high-scoring, lacks clinical plausibility.

## Clinical Trial Evidence

Currently no related clinical trials registered for Halothane in manic bipolar affective disorder, bipolar disorder, or any of the other predicted psychiatric indications.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [29845450](https://pubmed.ncbi.nlm.nih.gov/29845450/) | 2018 | Pharmacological analysis | Cardiovascular Toxicology | Assessed cardiovascular safety margin of **lithium carbonate** (a bipolar drug) in halothane-anesthetized dogs. Halothane served only as the background anesthetic — not as the therapeutic agent. |
| [33136260](https://pubmed.ncbi.nlm.nih.gov/33136260/) | 2021 | Reverse translational analysis | Heart and Vessels | Evaluated cardiovascular adverse events of **lamotrigine** (used for epilepsy/bipolar disorder) in halothane-anesthetized dogs. Again, halothane was the anesthetic model, not the study drug. |
| [835845](https://pubmed.ncbi.nlm.nih.gov/835845/) | 1977 | Drug interaction study | Anesthesiology | Studied effects of **lithium carbonate** on neuromuscular blocking agents in halothane/N₂O-anesthetized dogs. Relevant to anesthesia-lithium drug interactions, not to bipolar treatment. |
| [3019784](https://pubmed.ncbi.nlm.nih.gov/3019784/) | 1986 | Basic research | Federation Proceedings | Examined **lithium's** effects on phosphoinositide metabolism; noted that halothane (as anesthetic) diminished inositol monophosphate accumulation in brain. Suggests halothane suppresses the neural activity signal, not that it has therapeutic relevance. |
| [6126494](https://pubmed.ncbi.nlm.nih.gov/6126494/) | 1982 | Case report / In vitro study | J Clin Psychopharmacology | Case of neuroleptic malignant syndrome with in vitro muscle comparison to malignant hyperthermia. Relates to halothane's known risk of triggering malignant hyperthermia — a safety concern, not a therapeutic signal. |

> **Important Note:** None of these 5 publications study Halothane as a treatment for bipolar disorder. In all cases, Halothane was used as the background anesthetic in animal models, while the actual drugs under investigation were bipolar medications (lithium, lamotrigine). The co-occurrence of "halothane" and "bipolar" in these papers is methodological, not therapeutic.

## Taiwan Market Information

Halothane is currently **not marketed** in Taiwan. There are no active TFDA registrations (0 licenses). Halothane has been largely withdrawn from clinical use globally due to the risk of halothane hepatitis (immune-mediated fulminant hepatic failure) and the availability of safer alternative inhalational anesthetics.

## Safety Considerations

> Please refer to the package insert for safety information. Key TFDA label warnings and contraindications data were not available for this evaluation.

**Known safety concerns from general pharmacological knowledge (not from the evidence pack):**
- **Hepatotoxicity**: Halothane hepatitis — a potentially fatal immune-mediated fulminant hepatic necrosis, particularly with repeated exposure
- **Malignant Hyperthermia**: Halothane is a known trigger in genetically susceptible individuals
- **Cardiac Effects**: Sensitizes the myocardium to catecholamines, increasing risk of arrhythmias
- **Global Market Withdrawal**: Largely replaced by sevoflurane/desflurane due to superior safety profiles

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score (99.82%) is algorithmically high, but lacks any clinical or mechanistic plausibility. Halothane is a general inhalational anesthetic with non-specific CNS depressant effects — it has no selective activity on the pathways involved in bipolar disorder pathology. All 5 retrieved publications merely used halothane as a background anesthetic in animal models studying actual bipolar medications. There are zero clinical trials. The drug is not marketed in Taiwan, has been globally replaced by safer alternatives, and carries serious risks (hepatotoxicity, malignant hyperthermia, cardiac arrhythmias) that make chronic psychiatric use inconceivable. The route of administration (inhalation requiring anesthesia equipment and monitoring) is fundamentally incompatible with outpatient bipolar disorder management.

**This candidate should not be advanced.** To reconsider, the following would be needed:
- Direct evidence of Halothane acting on bipolar-specific molecular targets (GSK-3β, inositol signaling, dopaminergic pathways)
- At least one preclinical study testing Halothane in validated animal models of mania
- A plausible route of administration compatible with chronic psychiatric treatment
- Resolution of the hepatotoxicity and malignant hyperthermia safety concerns

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

