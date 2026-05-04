---
layout: default
title: Atropine
parent: 僅模型預測 (L5)
nav_order: 32
evidence_level: L5
indication_count: 2
---

# Atropine
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

# Atropine: From Anticholinergic Applications to Migraine Disorder

## One-Sentence Summary

Atropine is a classic non-selective muscarinic receptor antagonist (anticholinergic drug) with established clinical applications including bradycardia management and organophosphate poisoning antidote, though no Philippines FDA registration is currently on record.
The TxGNN model predicts it may be effective for **Migraine Disorder**, with **0 clinical trials** and **13 publications** currently providing indirect mechanistic support.
Evidence remains exclusively preclinical, and a key mechanistic concern regarding the direction of cholinergic modulation warrants careful scrutiny before any clinical translation is considered.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines FDA registration on record |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Atropine is a non-selective muscarinic receptor antagonist that competitively blocks acetylcholine (ACh) at muscarinic receptors in both the central and peripheral nervous systems. Detailed MOA data from DrugBank was not retrieved in this evaluation cycle (Data Gap DG002); however, atropine's pharmacological class as an anticholinergic agent is universally established. Its clinical versatility — from reversing bradycardia to counteracting organophosphate toxicity — reflects the breadth of muscarinic receptor distribution throughout the body.

The mechanistic case for migraine rests on the role of the parasympathetic autonomic system in headache pathophysiology. Stimulation of the sphenopalatine ganglion (SPG), a major intracranial parasympathetic relay, causes the release of VIP and ACh, which in turn activates meningeal mast cells and induces plasma protein extravasation (neurogenic inflammation) in the dura mater — a well-recognised trigger of migraine pain. By blocking muscarinic receptors, atropine could theoretically interrupt this cascade. Preclinical animal data (PMID 9344563) directly demonstrates that parasympathetic SPG stimulation produces dural plasma extravasation in rats, providing anatomical and pharmacological grounding for this hypothesis. One human clinical observation (PMID 2943405) further documented that systemic atropine markedly reduced attack-related autonomic features (sweating, tearing, nasal secretion) in patients with chronic paroxysmal hemicrania — a headache variant sharing pathophysiological overlap with migraine.

That said, a critical counter-argument emerges from the rank-2 predicted indication (migraine with brainstem aura): the only available study (PMID 31945385) shows that **cholinergic activation** — not blockade — suppresses cortical spreading depression (CSD), which is the electrophysiological substrate of migraine aura. Since atropine is a cholinergic **antagonist**, it could theoretically facilitate rather than suppress CSD. This mechanistic tension does not necessarily negate the rank-1 (migraine disorder) hypothesis, which operates through a different pathway (peripheral SPG-dura axis), but it raises a substantive scientific question that must be resolved before clinical development.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Review | J Appl Toxicol | Anisodamine, a naturally occurring atropine derivative, exhibits the same anticholinergic spectrum with reportedly lower potency and CNS toxicity than atropine, supporting the broader class relevance to cholinergic modulation in neurological applications |
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Preclinical | Eur J Neurosci | Cholinergic system (including muscarinic signalling) modulates meningeal mast cell activity and neurogenic inflammation in a nitroglycerin-induced rat migraine model; most directly relevant mechanistic study linking muscarinic pathways to migraine pathophysiology |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Clinical Observation | Cephalalgia | Systemic atropine markedly reduced attack-related sweating, tearing, and nasal secretion in chronic paroxysmal hemicrania patients; the only in-human evidence directly demonstrating anticholinergic suppression of headache-associated autonomic symptoms |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Preclinical (Animal) | Exp Neurol | Parasympathetic SPG stimulation induces dural plasma protein extravasation in rats; provides direct anatomical and mechanistic rationale for SPG-targeted anticholinergic intervention in migraine |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Preclinical (Animal) | J Pharmacol Exp Ther | Sumatriptan's antinociceptive effect in rodents is partly mediated through the central cholinergic system; cholinergic pathways contribute to pain control mechanisms relevant to migraine |
| [15882801](https://pubmed.ncbi.nlm.nih.gov/15882801/) | 2005 | Preclinical (Animal) | Neurosci Lett | CGRP release from trigeminal neurons involves nicotinic receptor activation; atropine used as muscarinic control, further delineating the cholinergic receptor subtypes relevant to trigeminovascular signalling |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | Preclinical (In vitro) | Br J Pharmacol | Atropine (3 µM) used as a pharmacological tool in a guinea-pig basilar artery model examining antimigraine drug effects on vascular tone; establishes atropine's utility in migraine-relevant vascular pharmacology |
| [1786517](https://pubmed.ncbi.nlm.nih.gov/1786517/) | 1991 | Preclinical (In vitro) | Br J Pharmacol | Ergotamine and dihydroergotamine are potent 5-HT1C receptor agonists in piglet choroid plexus; contextualises the serotonergic receptor pharmacology distinguishable from (but parallel to) the cholinergic mechanisms relevant to atropine |
| [27179636](https://pubmed.ncbi.nlm.nih.gov/27179636/) | 2016 | Case Report | Rev Port Cardiol | Takotsubo syndrome in a 14-year-old following anesthetic procedure involving atropine; highlights cardiovascular safety concerns (tachycardia, catecholamine surge) with systemic atropine use, with direct implications for risk assessment in migraine patients |
| [21252](https://pubmed.ncbi.nlm.nih.gov/21252/) | 1977 | Mechanistic | J Pharm Pharmacol | Early investigation into beta-phenethylamine's mechanism in migraine; provides historical context on monoamine–cholinergic interactions in headache aetiology |

---

## Philippines Market Information

Atropine is currently **not registered** with the Philippines FDA. No active product licenses, authorisation numbers, or approved indications are on record. Any repurposing pathway would require a de novo regulatory filing in the Philippines.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important Note for Migraine Repurposing Context**: Atropine's well-known systemic anticholinergic effects — tachycardia, dry mouth, urinary retention, cycloplegia, and CNS excitation at higher doses — pose particular concerns in migraine patients who may already experience autonomic dysregulation during attacks. Formal safety profiling against Philippines FDA labeling documents and the complete DrugBank safety record is pending (Data Gaps DG001 and DG002). These gaps are classified as **Blocking** and **High** severity respectively, and must be resolved before any progression beyond research-stage evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All available evidence is preclinical or derives from indirect clinical observations (L4), no registered clinical trials exist, a mechanistic concern about the direction of cholinergic modulation in migraine aura (antagonist vs. the expected agonist effect) has not been resolved, and systemic anticholinergic adverse effects present a meaningful safety barrier that cannot be assessed without the missing Philippines FDA labeling data.

**To proceed, the following is needed:**

- **Resolve Data Gap DG001 (Blocking):** Download and parse the Philippines FDA or equivalent package insert for atropine to complete the mandatory S1 safety assessment
- **Resolve Data Gap DG002 (High):** Query DrugBank API to retrieve the full pharmacological MOA, toxicity profile, and drug interaction data
- **Address the mechanistic direction question:** Commission or identify studies that specifically test muscarinic *blockade* (not activation) in validated preclinical migraine models (e.g., SPG stimulation, dural plasma extravasation assay) to confirm or refute efficacy
- **Explore targeted delivery:** Assess whether a localized delivery route (e.g., sphenopalatine ganglion block via intranasal application) could achieve therapeutic anticholinergic effect while limiting systemic adverse events
- **Broaden literature search:** Conduct a targeted search for controlled human studies or prospective case series using atropine or selective muscarinic antagonists (e.g., scopolamine, methscopolamine) specifically in headache disorders before any clinical trial design
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

