---
layout: default
title: Halothane
parent: Model Prediction Only (L5)
nav_order: 165
evidence_level: L5
indication_count: 6
---

# Halothane
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **6** 
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

# Halothane: From General Anaesthesia to Manic Bipolar Affective Disorder

## One-Sentence Summary

Halothane is a volatile anaesthetic agent. The data compiled for this report do not record an approved indication for it in the Philippines.
The TxGNN model predicts it may be effective for **manic bipolar affective disorder**, but there are **0 clinical trials** and only **4 publications**, none of which studies halothane as a treatment for this condition. They are preclinical studies that use halothane as an anaesthetic background for lithium or lamotrigine experiments.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the Philippines licence data (halothane is generally known as an inhaled general anaesthetic) |
| Predicted New Indication | Manic bipolar affective disorder |
| TxGNN Prediction Score | 99.82% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. Halothane is a volatile anaesthetic, which is generally understood to enhance GABA-A receptor activity and modulate K2P potassium channels. These actions produce anaesthesia, and there is no established link to an antimanic effect.

The high TxGNN score (0.998) comes from graph-based prediction only. The retrieved publications concern lithium and lamotrigine, with halothane serving only as the anaesthetic used in animal experiments. The prediction most likely reflects network proximity through shared lithium-related anaesthetic interaction nodes, not therapeutic relevance. The mechanistic case for this prediction is therefore weak.

Other predictions in the same list (nephrogenic syndrome of inappropriate antidiuresis, Tourette syndrome, trichotillomania, bipolar disorder, major affective disorder) have similarly high scores but no clinical trial support. Those with literature are likewise indirect.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [835845](https://pubmed.ncbi.nlm.nih.gov/835845/) | 1977 | Review (as classified) | Anesthesiology | Effects of lithium carbonate on five neuromuscular blocking agents in dogs anaesthetised with halothane and N2O |
| [29845450](https://pubmed.ncbi.nlm.nih.gov/29845450/) | 2018 | Preclinical safety analysis | Cardiovascular Toxicology | Cardiovascular safety margin of lithium carbonate assessed in halothane-anaesthetised dogs |
| [3019784](https://pubmed.ncbi.nlm.nih.gov/3019784/) | 1986 | Preclinical | Federation Proceedings | Lithium effects on phosphoinositide metabolism in vivo. Anaesthetics including halothane diminished the lithium-induced brain myo-inositol 1-phosphate elevations |
| [33136260](https://pubmed.ncbi.nlm.nih.gov/33136260/) | 2021 | Preclinical reverse translational analysis | Heart and Vessels | Lamotrigine-induced cardiovascular adverse events assessed in halothane-anaesthetised dogs |

None of these studies tests halothane as a treatment for mania or bipolar disorder.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0224 | Halothane | Not recorded | Not recorded (status: cancelled) |

## Safety Considerations

- **Knowledge-graph contraindication signals** (from drug-disease links in the TxGNN knowledge graph, not from label text): liver disease, gallbladder disease, hypotensive disorder, sudden cardiac arrest, heart conduction disease, malignant hyperthermia of anaesthesia, exercise-induced malignant hyperthermia, pseudotumor cerebri, intracranial hypertension.
- **Drug Interactions**: 100 interactions were identified. Examples of those rated **Major**: epinephrine, dolasetron, cisapride, papaverine, macimorelin. Examples of those rated **Moderate**: famotidine, loperamide, morphine, clarithromycin, levofloxacin, ondansetron, granisetron, promethazine, palonosetron, deferasirox. Metronidazole is rated **Minor**.
- Halothane has been associated with hepatotoxicity concerns, which makes chronic use for a psychiatric indication implausible.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests only on a graph model score. There are no clinical trials, the literature is indirect (halothane appears only as an anaesthetic in lithium and lamotrigine animal studies), and no plausible mechanism links halothane to antimanic effects. The Philippines licence is cancelled, and the safety profile (hepatotoxicity, cardiac and malignant hyperthermia signals) argues against chronic use.

**To proceed, the following is needed:**
- Detailed mechanism of action data and a plausible mechanistic rationale for antimanic effects
- Direct preclinical or clinical evidence of halothane in mood disorders
- Package insert warnings and contraindications (not currently available)
- Clarification of the cancelled Philippines registration and the original approved indication
- A feasibility assessment for any route of administration suitable for a psychiatric indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

