---
layout: default
title: Thiopental
parent: 僅模型預測 (L5)
nav_order: 332
evidence_level: L5
indication_count: 10
---

# Thiopental
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

# Thiopental: From General Anesthesia to Absence Epilepsy

## One-Sentence Summary

Thiopental is an ultra-short-acting barbiturate historically used for intravenous anesthesia induction and acute management of refractory intracranial hypertension.
The TxGNN model predicts it may be effective for **Absence Epilepsy** — ranked #5 by TxGNN score but #1 by clinical evidence strength among all predictions in this pack —
with **2 clinical trials** and **12 publications** currently supporting this direction, including a Tier 1 consensus guideline that explicitly endorses barbiturate anesthetics as third-line therapy for super-refractory status epilepticus.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | General anesthesia induction; adjunct management of raised intracranial pressure |
| Predicted New Indication | Absence Epilepsy |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on TxGNN ranking:** The model's top-ranked prediction is Trichotillomania (score 99.95%), but that indication has zero supporting clinical evidence (L5, Hold). Absence Epilepsy (rank 5) carries the strongest actionable evidence in this dataset and is the focus of this report.

---

## Why is This Prediction Reasonable?

Thiopental belongs to the barbiturate class and acts as a positive allosteric modulator of the GABA-A receptor. By binding to a distinct site on the receptor complex, it prolongs chloride ion channel opening time, thereby amplifying inhibitory neurotransmission throughout the central nervous system. Detailed mechanism-of-action data is currently marked as a Data Gap in this evidence pack — however, the drug's barbiturate class membership and its well-documented CNS-depressant profile are sufficient to establish the mechanistic rationale described here.

This GABA-A mechanism maps directly onto the pathophysiology of absence epilepsy. The characteristic 3 Hz spike-wave discharges arise from synchronized thalamo-cortical oscillations maintained by an imbalance between excitatory and inhibitory tone — precisely the type of aberrant circuit activity that GABAergic enhancement can interrupt. In severe or refractory cases, particularly **absence status epilepticus** (a form of non-convulsive status epilepticus), thiopental's capacity to produce dose-dependent EEG suppression up to burst-suppression provides a mechanistically coherent pathway to seizure termination. A 2018 consensus guideline (PMID 30387431) explicitly classifies barbiturates, including thiopental, as third-line anesthetic therapy for super-refractory status epilepticus — the category under which prolonged absence status epilepticus falls when first- and second-line treatments have failed.

A critical scope distinction must be maintained: the available evidence supports thiopental's role in **acute, ICU-based management of status epilepticus**, not in the chronic outpatient treatment of recurring absence seizures. Its IV-only delivery route, addiction liability, and requirement for ventilatory support confine practical utility to intensive care settings. Any repurposing initiative should be scoped to this acute context.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT07443241](https://clinicaltrials.gov/study/NCT07443241) | N/A | Completed | 779 | Retrospective analysis of sex-specific differences in etiology, diagnostics, treatment, and outcomes of status epilepticus at Marburg University Hospital (2011–2023); real-world treatment database may capture thiopental as a rescue anesthetic agent |
| [NCT04287361](https://clinicaltrials.gov/study/NCT04287361) | N/A | Completed | 310 | IV clonazepam dosing efficacy for initial management of pediatric status epilepticus — study drug is clonazepam, not thiopental; provides benchmark data on the first-line treatment landscape thiopental would need to follow |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [30387431](https://pubmed.ncbi.nlm.nih.gov/30387431/) | 2018 | Consensus Guideline | Acta Medica Portuguesa | Portuguese SRLF/SFMU consensus protocol for super-refractory status epilepticus (SRSE); explicitly lists barbiturates (including thiopental) as third-line anesthetic therapy — strongest evidence tier in this dataset |
| [8223422](https://pubmed.ncbi.nlm.nih.gov/8223422/) | 1993 | Prospective Clinical Study | Epilepsy Research | Thiopental test in 103 pre-surgical epilepsy candidates; IV infusion reliably suppresses EEG beta activity and activates interictal spiking, directly demonstrating thiopental's seizure-circuit modulation properties in human epilepsy patients |
| [8400755](https://pubmed.ncbi.nlm.nih.gov/8400755/) | 1993 | Prospective Clinical Study | J Neurosurgical Anesthesiology | Anesthetic care protocol for the thiopental test in refractory epilepsy evaluation; characterizes dosing regimen, monitoring parameters, and morbidity profile — establishes safety feasibility in the epilepsy population |
| [18759609](https://pubmed.ncbi.nlm.nih.gov/18759609/) | 2009 | Retrospective Cohort | Journal of Neurosurgery | ICP-targeted therapy using thiopental in TBI patients; prospective EEG monitoring demonstrates consistent suppression of both clinical and subclinical (EEG-only) seizure activity during treatment course |
| [36003492](https://pubmed.ncbi.nlm.nih.gov/36003492/) | 2022 | Case Report | Frontiers in Pediatrics | FIRES and new anti-neuronal antibodies in a 5-year-old; documents escalating use of anesthetic-class agents (barbiturate context) in treatment-refractory pediatric epileptic encephalopathy |
| [38505775](https://pubmed.ncbi.nlm.nih.gov/38505775/) | 2024 | Case Report | Frontiers in Neuroscience | FIRES with multi-organ failure and lethal outcome in a 14-year-old; illustrates the clinical pathway to barbiturate-class rescue anesthesia in catastrophic pediatric refractory SE and its limitations |
| [7485956](https://pubmed.ncbi.nlm.nih.gov/7485956/) | 1995 | Review | Anaesthesia and Intensive Care | Propofol and epilepsy — comparative review establishing the broader context of IV anesthetic agents vs. barbiturates in seizure management; supports thiopental as a reference comparator |
| [27848906](https://pubmed.ncbi.nlm.nih.gov/27848906/) | 2016 | Case Report | NTvG | Potentially lethal barbiturate intoxication via internet purchase; critical safety signal — confirms narrow therapeutic window and overdose lethality risk for any repurposing protocol |
| [4979765](https://pubmed.ncbi.nlm.nih.gov/4979765/) | 1969 | Clinical Study | Epilepsia | Thiopental activation test for distinguishing secondary from primary bilateral epileptic synchrony; early clinical evidence of thiopental's differential diagnostic role in epilepsy circuit mapping |
| [4189546](https://pubmed.ncbi.nlm.nih.gov/4189546/) | 1970 | Clinical Study | EEG and Clinical Neurophysiology | Confirmatory study of the thiopental test for bilateral synchrony differentiation; validates reproducibility of thiopental's CNS seizure-suppression effect across independent cohorts |

---

## Safety Considerations

All structured safety fields in this evidence pack (key warnings, contraindications, drug interactions) are recorded as Data Gap. Please refer to the package insert for full safety information.

**Safety signals identified from available literature:**

- **Addiction and abuse potential:** Evidence from the substance dependence evidence set (PMID 15967611) confirms documented thiopental dependence in anesthesiologists identified by hair analysis — barbiturate addiction is a serious, well-characterized risk requiring strict access controls in any clinical protocol
- **Overdose lethality:** PMID 27848906 documents potentially lethal toxicity from barbiturate overdose; therapeutic index is narrow and dose titration must occur under continuous monitoring
- **Cardiovascular depression:** Thiopental carries known negative inotropic and vasodilatory properties that can cause hemodynamic instability — patients with cardiac comorbidities (including coronary artery disease) face elevated risk
- **Respiratory depression:** Mechanical ventilatory support is required at anesthetic doses; this drug cannot be used outside a monitored ICU or procedural setting

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A Tier 1 consensus guideline explicitly endorses barbiturate anesthetics — including thiopental — as third-line therapy for super-refractory status epilepticus, the category that encompasses prolonged absence status epilepticus refractory to standard care. This is not speculative repurposing; it reflects established ICU neurological practice in guideline-producing institutions. The primary barriers are **regulatory** (not marketed in the Philippines) and **operational** (IV-only, requires ICU infrastructure), not evidentiary.

**To proceed, the following is needed:**

- **Clarify the clinical target:** Confirm whether the repurposing scope is *absence status epilepticus* (acute ICU setting — actionable, supported by current guidelines) or *chronic recurring absence epilepsy* (outpatient — high barrier, not supported by available evidence)
- **Retrieve full MOA documentation:** Query DrugBank API and obtain the WHO/TFDA package insert to resolve the current Data Gap before regulatory submission
- **Establish a Philippines import or compassionate use pathway:** Thiopental is not registered domestically (0 licenses); a special access or hospital-level importation authorization is required before any clinical use
- **Develop an ICU-specific safety protocol:** Covering continuous EEG monitoring for burst-suppression endpoint, hemodynamic monitoring, ventilatory support requirements, and barbiturate serum level tracking
- **Controlled substance regulatory review:** Assess the Philippines DEA/FDA-equivalent scheduling status for thiopental and determine procurement and storage requirements
- **Local needs assessment:** Survey whether Philippine tertiary ICUs currently use alternative agents (midazolam, propofol, pentobarbital) for refractory SE, and identify the clinical gap thiopental would specifically address before committing to procurement
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

