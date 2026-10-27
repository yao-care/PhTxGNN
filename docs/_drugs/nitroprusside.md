---
layout: default
title: Nitroprusside
parent: Model Prediction Only (L5)
nav_order: 255
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Nitroprusside: predicted new indication Migraine disorder (evidence level L5). Approved use: Not available"
monitor_inn: "nitroprusside"
predicted_indications: ["migraine disorder", "migraine with brainstem aura", "alopecia", "congenital hypotrichosis milia", "diffuse alopecia areata", "hypotrichosis simplex of the scalp", "migraine with or without aura, susceptibility to", "pulmonary hypertension", "benign prostatic hyperplasia (disease)", "kyphoscoliotic heart disease"]
---

# Nitroprusside
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **10** 
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

## Nitroprusside: From an Unspecified Original Indication to Migraine Disorder
{: .text-alpha }

## One-Sentence Summary

Nitroprusside (sodium nitroprusside) is a nitric oxide (NO) donor and vasodilator. The data compiled for this report do not state a registered indication for it in the Philippines.
The TxGNN model ranks **migraine disorder** as its top prediction, but there are **no registered clinical trials** and only **preclinical and physiology studies** among the 20 publications, and these suggest NO donors tend to *provoke* migraine rather than treat it.
Of the ten predictions, **pulmonary hypertension** has the most plausible mechanism and the most clinical-type data, so it is covered below as an alternative lead.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not available (the Philippines registration has no indication text) |
| Predicted New Indication | Migraine disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L4 (preclinical and mechanism studies only) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the compiled data. Based on known pharmacology, nitroprusside releases nitric oxide, which activates soluble guanylate cyclase and raises cGMP, causing vascular smooth muscle relaxation and vasodilation.

For migraine, the link is mechanistic and diagnostic, not therapeutic. NO and CGRP signalling are central to migraine biology. Human studies used NO-donor and CGRP challenges to compare migraine patients with controls, showing altered vascular smooth muscle and endothelial responses. Nitroprusside is also used as a migraine trigger in animal models. NO donors are known to provoke migraine attacks, so the direction of effect is unfavourable. The very high TxGNN score most likely reflects network proximity through the NO/cGMP and CGRP pathways rather than therapeutic benefit.

The other top predictions are weaker:
- **Migraine with brainstem aura** and **migraine with or without aura, susceptibility to**: supported only by general migraine literature with the same unfavourable direction of effect.
- **Alopecia, congenital hypotrichosis milia, diffuse alopecia areata, hypotrichosis simplex of the scalp, kyphoscoliotic heart disease**: no trials or literature. These are computational outputs only.
- **Benign prostatic hyperplasia**: the NO/cGMP/PDE5 pathway is relevant (PDE5 inhibitors are used), but no study tests nitroprusside, and systemic use is impractical for a chronic condition.
- **Pulmonary hypertension** (Evidence Level L3, "Research Question"): nitroprusside acts on the same NO/cGMP pathway targeted by approved therapies (inhaled NO, PDE5 inhibitors, sGC stimulators). Small perioperative clinical data exist, including inhaled nitroprusside after mitral valve replacement. Systemic use carries risks of hypotension, worsened V/Q matching and cyanide toxicity, so any use would need an inhaled or tightly monitored acute setting.

## Clinical Trial Evidence

Currently no related clinical trials are registered for migraine disorder.

For reference, the one trial listed for the alternative lead, pulmonary hypertension, is only loosely relevant:

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02966665](https://clinicaltrials.gov/study/NCT02966665) | Phase 1 | Recruiting | 420 | Vascular function and exercise rehabilitation in systemic hypertension; nitroprusside likely used only as a vascular probe (low direct relevance) |

## Literature Evidence

The 20 publications for migraine disorder are mostly preclinical, with several human physiology studies. No randomised trials are listed. Selected items:

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [21122149](https://pubmed.ncbi.nlm.nih.gov/21122149/) | 2010 | Cross-sectional | BMC Neurology | Tested endothelial function and NO release in migraine patients |
| [18384419](https://pubmed.ncbi.nlm.nih.gov/18384419/) | 2008 | Case-control physiology | Cephalalgia | Compared skin microvascular responses to CGRP and NO between migraine and control subjects |
| [19528518](https://pubmed.ncbi.nlm.nih.gov/19528518/) | 2009 | Case-control physiology | Neurology | Vascular smooth muscle dysfunction in migraine patients |
| [16396667](https://pubmed.ncbi.nlm.nih.gov/16396667/) | 2006 | Case-control physiology | Cephalalgia | Forearm vascular responses to NO donor (nitroprusside) and CGRP in 10 migraine patients vs 10 controls |
| [39988876](https://pubmed.ncbi.nlm.nih.gov/39988876/) | 2025 | Preclinical (animal) | Cephalalgia | CBD and THC reduced migraine-like behaviours in mouse models, one triggered by nitroprusside |
| [36697259](https://pubmed.ncbi.nlm.nih.gov/36697259/) | 2023 | Preclinical (animal) | J Neurosci | Peroxynitrite contributes to migraine-like responses to an NO donor |
| [11921057](https://pubmed.ncbi.nlm.nih.gov/11921057/) | 2002 | Mechanistic | Annals of Neurology | NO donors (including nitroprusside) increase iNOS expression; NF-kB proposed as a migraine target |
| [24754925](https://pubmed.ncbi.nlm.nih.gov/24754925/) | 2014 | Preclinical (human and rat tissue) | J Headache Pain | Vasodilator responses of meningeal arteries to migraine-related compounds |

The literature shows that nitroprusside is a **migraine research tool and trigger**, not a demonstrated treatment.

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0452 | Sodium Nitroprusside | Not specified | Not specified (status: cancelled) |

## Safety Considerations

- **Drug Interactions**: 58 interactions were identified in total. The 20 shown in the compiled data are all rated Moderate. They include:
  - Corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone, budesonide, prednisolone, prednisone)
  - SGLT2 inhibitors (canagliflozin, dapagliflozin, empagliflozin, ertugliflozin)
  - Opioids (morphine, opium)
  - Cannabinoids (dronabinol, nabilone)
  - Others: bupropion, sapropterin, amifostine, promethazine, iodide I-123
- **Other risks noted in the evidence review**: hypotension, worsened V/Q matching and cyanide toxicity with systemic use.
- **Not retrieved**: package insert warnings and contraindications were not available in the compiled data. Please refer to the package insert for these.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- The migraine prediction rests on indirect preclinical and physiology evidence (L4). NO donors like nitroprusside provoke migraine attacks, so the direction of effect is unfavourable.
- The Philippines registration is cancelled, with no indication or dosage form recorded.
- Pulmonary hypertension is the more credible lead (L3, mechanistically consistent, with small perioperative clinical data), but it needs focused evaluation before any decision.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines (blocking gap for safety screening)
- Mechanism-of-action data from DrugBank
- Original indication and dosage form for the cancelled registration
- For pulmonary hypertension: a focused evidence review of inhaled or tightly monitored perioperative nitroprusside use, including cyanide toxicity and haemodynamic risks
- For migraine: evidence that a therapeutic effect is possible despite the provocation data. Otherwise, deprioritise this indication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

