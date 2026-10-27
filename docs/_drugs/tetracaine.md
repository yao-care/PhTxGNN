---
layout: default
title: Tetracaine
parent: Model Prediction Only (L5)
nav_order: 332
evidence_level: L5
indication_count: 9
last_modified_at: 2026-10-15
description: "Tetracaine: predicted new indication Acrodermatitis chronica atrophicans (evidence level L5). Approved use: Dermatitis"
monitor_inn: "Tetracaine"
predicted_indications: ["acrodermatitis chronica atrophicans", "neonatal dermatomyositis", "bronchitis", "secondary interstitial lung disease specific to childhood associated with a connective tissue disease", "acne keloid", "hydroa vacciniforme, familial", "amyopathic dermatomyositis", "cauda equina syndrome", "irritable bowel syndrome"]
---

# Tetracaine
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **9** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Tetracaine: From Dermatitis to Acrodermatitis Chronica Atrophicans
{: .text-alpha }

## One-Sentence Summary

Tetracaine is an ester-type local anaesthetic whose original indication in the knowledge graph is dermatitis.
The TxGNN model predicts it may be effective for **Acrodermatitis Chronica Atrophicans**, but **no clinical trials and no publications** support this prediction, so it rests on the model score alone.
Across the other predicted indications, the only trial and literature found concern procedural anaesthesia or adverse effects, not treatment of disease.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Dermatitis (from the knowledge graph; no approved indication text is available for the Philippines registration) |
| Predicted New Indication | Acrodermatitis chronica atrophicans |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L5 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Tetracaine is known as a topical or ester-type local anaesthetic that blocks sodium channels. Its original indication is dermatitis, and the model likely links it to the new indication through dermatological associations.

On closer inspection, the mechanistic link is weak. Acrodermatitis chronica atrophicans is a late-stage skin infection caused by *Borrelia*. A sodium-channel-blocking anaesthetic has no plausible disease-modifying role in it. The high score is most likely driven by the shared dermatological context in the knowledge graph rather than by a real therapeutic relationship.

The other top-ranked predictions show the same pattern. Neonatal dermatomyositis, amyopathic dermatomyositis, childhood interstitial lung disease and hydroa vacciniforme have no plausible mechanism. For bronchitis and acne keloid, tetracaine provides procedural anaesthesia (for example during bronchoscopy or laser treatment), not treatment of the disease. Irritable bowel syndrome is speculative. For cauda equina syndrome, the literature shows tetracaine as a **cause** of the condition, not a treatment.

---

## Clinical Trial Evidence

No clinical trials are registered for the lead predicted indication (acrodermatitis chronica atrophicans).

For the fifth-ranked prediction, acne keloid, one trial was found. It evaluates procedural pain relief, not efficacy against the disease:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02372786](https://clinicaltrials.gov/study/NCT02372786) | Phase 4 | Completed | 30 | Double-blind RCT comparing 7% lidocaine/7% tetracaine cream with 2.5% lidocaine/2.5% prilocaine cream for pain relief during laser treatment of acne keloidalis nuchae and tattoo removal |

---

## Literature Evidence

No literature is available for the lead predicted indication. The table below lists the most relevant publications found for lower-ranked predictions:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [27377616](https://pubmed.ncbi.nlm.nih.gov/27377616/) | 2017 | RCT (inferred from title) | Br J Dermatol | Lidocaine/tetracaine cream compared with lidocaine/prilocaine cream for anaesthesia during laser treatment of acne keloidalis nuchae and tattoo removal (acne keloid prediction) |
| [9033758](https://pubmed.ncbi.nlm.nih.gov/9033758/) | 1996 | Review | Ann Fr Anesth Reanim | Neurotoxicity of intrathecal agents, including histopathologic spinal lesions (cauda equina syndrome prediction) |
| [10876464](https://pubmed.ncbi.nlm.nih.gov/10876464/) | 2000 | Review | AANA J | Transient neurologic symptoms after spinal anaesthesia (cauda equina syndrome prediction) |
| [30625770](https://pubmed.ncbi.nlm.nih.gov/30625770/) | 2009 | Case report | Korean J Anesthesiol | Cauda equina syndrome after spinal anaesthesia with 0.5% hyperbaric tetracaine plus epinephrine |
| [11685003](https://pubmed.ncbi.nlm.nih.gov/11685003/) | 2001 | Case report | Anesthesiology | Cauda equina syndrome after spinal tetracaine, with 20-year electromyographic follow-up |

The cauda equina publications describe tetracaine as a cause of harm, which is a safety signal and argues against repurposing for that indication.

---

## Philippines Market Information

The data compiled for this report lists one registration, which is cancelled. No dosage form or approved indication text is recorded.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0482 | Tetracaine | Not recorded | Not recorded (status: cancelled) |

---

## Safety Considerations

- **Contraindications (knowledge graph signals, not label text)**: The knowledge graph links tetracaine to caution in epilepsy, kidney disease, liver disease, gallbladder disease, heart and cardiovascular disease (including sudden cardiac arrest and heart conduction disease), respiratory failure, myasthenia gravis and other neuromuscular junction disease, butyrylcholinesterase deficiency, hyperthyroidism (Graves disease, thyrotoxicosis), and several eye conditions (uveitis, iris and ciliary body disease, conjunctivitis, eye infections).
- **Drug Interactions**: 32 interactions were recorded. Major interactions include:
  - Nitrous acid
  - Liposomal bupivacaine

  Moderate interactions include:
  - Other local anaesthetics (lidocaine, benzocaine, cocaine, proparacaine, oxybuprocaine, cinchocaine)
  - Benzodiazepines (alprazolam, chlordiazepoxide, clobazam, clonazepam, clorazepic acid, diazepam, estazolam)
  - Sulfonamides (sulfasalazine, sulfamethoxazole)

  A minor interaction was recorded with hyaluronidase.
- **Neurotoxicity**: Published case reports link spinal tetracaine to cauda equina syndrome. Neonatal use raises concern about systemic absorption and methemoglobinaemia with topical anaesthetics.

Label warnings and contraindications from the Philippine package insert were not available. Please refer to the package insert for the full safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The prediction is supported by model score only (Evidence Level L5). There are no trials or publications for acrodermatitis chronica atrophicans, and there is no plausible mechanism for a sodium channel blocker to treat a *Borrelia* skin infection.
- The only registration in the Philippines is cancelled. None of the other top predictions has a supported therapeutic role, and cauda equina syndrome is a safety signal.

**To proceed, the following is needed:**
- Philippine package insert warnings and contraindications (currently missing and blocking safety screening)
- Mechanism of action data (for example from DrugBank)
- Any clinical or preclinical evidence of therapeutic benefit in the predicted indications, rather than procedural anaesthesia
- Clarification of the regulatory status of the cancelled registration and the available dosage forms and routes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

