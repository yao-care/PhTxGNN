---
layout: default
title: Atropine
parent: Model Prediction Only (L5)
nav_order: 34
evidence_level: L5
indication_count: 2
last_modified_at: 2026-10-15
description: "Atropine: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available"
---

# Atropine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

# Atropine: From an Unspecified Original Indication to Migraine Disorder

## One-Sentence Summary

Atropine is a muscarinic anticholinergic drug. Its original approved indication is not recorded in the Philippines registration data compiled for this report.
The TxGNN model predicts it may be effective for **migraine disorder**, but there are **0 clinical trials** and only **11 publications** (mostly preclinical, case reports, or off-topic). This prediction is a computational hypothesis only.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the single registration has no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.56% |
| Evidence Level | L4 (preclinical and mechanistic studies only) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Atropine is a non-selective muscarinic acetylcholine receptor antagonist. Preclinical studies suggest cholinergic signalling may play a role in migraine. These include meningeal mast cell-mediated cholinergic modulation of neurogenic inflammation (rat model, 2024), plasma protein extravasation in rat dura mater after parasympathetic sphenopalatine ganglion stimulation (1997), and central cholinergic involvement in antinociception in rodents (1996). In a small observational study of chronic paroxysmal hemicrania, systemic atropine reduced attack-related sweating, tearing, and nasal secretion, which shows autonomic involvement in headache syndromes.

However, **no direct clinical evidence shows that atropine treats or prevents migraine**. Several retrieved papers are off-topic or are adverse-event case reports (botulinum-induced dropped head syndrome, topiramate-related eye effects, stunned myocardium after anaesthesia). The very high TxGNN score is a computational prediction and does not replace clinical data.

The second prediction, migraine with brainstem aura (score 99.42%, evidence level L5), is mechanistically ambiguous. One mouse study found that muscarinic receptor activation *inhibits* cortical spreading depression, so a muscarinic antagonist like atropine might have neutral or even opposing effects. This prediction is not supported by the current evidence.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [17186568](https://pubmed.ncbi.nlm.nih.gov/17186568/) | 2007 | Review | J Appl Toxicol | Anisodamine, an atropine derivative, is a non-specific cholinergic antagonist, less potent and less toxic than atropine |
| [36485173](https://pubmed.ncbi.nlm.nih.gov/36485173/) | 2024 | Preclinical | Eur J Neurosci | Meningeal mast cell-mediated cholinergic modulation of neurogenic inflammation in a rat migraine model |
| [2943405](https://pubmed.ncbi.nlm.nih.gov/2943405/) | 1986 | Case series | Cephalalgia | In 4 patients with chronic paroxysmal hemicrania, systemic atropine markedly reduced attack-related sweating, tearing, and nasal secretion |
| [9344563](https://pubmed.ncbi.nlm.nih.gov/9344563/) | 1997 | Preclinical (animal) | Exp Neurol | Parasympathetic sphenopalatine ganglion stimulation induced dural plasma protein extravasation in rats |
| [8930196](https://pubmed.ncbi.nlm.nih.gov/8930196/) | 1996 | Preclinical (animal) | J Pharmacol Exp Ther | The central cholinergic system contributes to sumatriptan-induced antinociception in rodents |
| [10193781](https://pubmed.ncbi.nlm.nih.gov/10193781/) | 1999 | Preclinical (in vitro) | Br J Pharmacol | Migraine-related drugs inhibited nicotine-evoked relaxation of guinea-pig basilar artery (atropine present as a background agent) |
| [1786517](https://pubmed.ncbi.nlm.nih.gov/1786517/) | 1991 | Preclinical (in vitro/animal) | Br J Pharmacol | Ergotamine and dihydroergotamine are potent 5-HT1C agonists (not directly about atropine) |
| [40590589](https://pubmed.ncbi.nlm.nih.gov/40590589/) | 2024 | Case report | Pain Med Case Rep | Botulinum toxin-induced dropped head syndrome in chronic migraine (off-topic) |
| [18091300](https://pubmed.ncbi.nlm.nih.gov/18091300/) | 2007 | Case report | Optom Vis Sci | Topiramate-linked raised intraocular pressure and myopic shift (off-topic) |
| [18604026](https://pubmed.ncbi.nlm.nih.gov/18604026/) | 2007 | Case report | Kathmandu Univ Med J | Topiramate-induced bilateral angle-closure glaucoma (off-topic) |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0034 | Atropine | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Drug Interactions**: 100 interactions were identified in the interaction screening. Most of those listed are of moderate severity, and a few are minor.
  - Anticholinergic or antimuscarinic agents (additive effects): hyoscyamine, aclidinium, amitriptyline, chlorpheniramine, acrivastine, phenyltoloxamine
  - Opioids and CNS depressants: fentanyl, alfentanil, codeine, dihydrocodeine, tramadol, ethanol
  - Others: botulinum toxin type A, acetylcholine, galantamine, amantadine, loperamide, acebutolol
  - Minor: acetaminophen, hydrochlorothiazide

Please refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The evidence consists only of preclinical mechanistic studies, small observational reports, and off-topic papers. There are no clinical trials in migraine. The only Philippines registration is cancelled, and no label-based safety data are available.

**To proceed, the following is needed:**
- Clinical evidence in migraine patients, such as pilot or exploratory trials
- Clarification of the mechanistic direction (muscarinic blockade vs. activation), especially for aura-related migraine
- A confirmed original indication and the package insert (warnings and contraindications) from the DOH-FDA Philippines
- Detailed mechanism of action data
- An assessment of whether a valid marketed product and a suitable route of administration exist in the Philippines
- A safety evaluation of anticholinergic burden, including the interactions above
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

