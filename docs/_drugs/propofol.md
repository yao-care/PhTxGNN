---
layout: default
title: Propofol
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 5
---

# Propofol
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

# Propofol: From General Anesthesia to Migraine Disorder

## One-Sentence Summary

Propofol is a widely used intravenous general anesthetic, primarily administered for the induction and maintenance of anesthesia in surgical and procedural settings. The TxGNN model predicts it may be effective for **Migraine Disorder** — specifically as an abortive (acute-terminating) therapy — with **5 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | General anesthesia (induction and maintenance of anaesthesia) |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L2 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not retrieved from DrugBank in this query cycle. Based on well-established pharmacological knowledge, Propofol (2,6-diisopropylphenol) is a non-barbiturate intravenous sedative-hypnotic agent whose primary mechanism involves potentiation of GABA-A receptor activity, leading to dose-dependent suppression of neuronal excitability. Crucially, at **sub-anesthetic (low) doses**, this GABAergic enhancement can suppress central sensitization without causing loss of consciousness — making it a pharmacologically tractable candidate for pain modulation outside the operating room.

The mechanistic connection to migraine is biologically plausible. Propofol has been demonstrated to inhibit **cortical spreading depression (CSD)** — the neurophysiological event underlying migraine aura and a key initiator of the trigeminovascular pain cascade. Through GABA-A potentiation, it also directly dampens activity in the **trigeminovascular pathway** (specifically the trigeminal nucleus caudalis), which is the primary pain relay in migraine pathophysiology. These dual actions — CSD suppression and trigeminal inhibition — provide a mechanistic rationale that extends beyond its anesthetic use.

General anesthesia and migraine are linked by a common neurophysiological thread: both involve the modulation of neuronal hyperexcitability in the central nervous system. Anecdotal clinical observations from the late 1990s noted that propofol, given at sub-anesthetic infusion rates, could terminate refractory migraine attacks in outpatient headache clinics. This clinical signal sparked a series of controlled investigations — predominantly in emergency department settings — that have since produced multiple RCTs and systematic reviews, lending sufficient evidence to consider this a legitimate repurposing candidate.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01604785](https://clinicaltrials.gov/study/NCT01604785) | Phase 2/3 | Completed | 74 | Sub-anesthetic propofol for abortive therapy of pediatric migraine in the ED; designed to compare propofol against standard treatments, building on a positive institutional retrospective series |
| [NCT02485418](https://clinicaltrials.gov/study/NCT02485418) | Not specified | Completed | 40 | Prospective study of low-dose IV propofol infusion for pediatric migraine; evaluated efficacy, safe dosing limits, and duration of effect in children and adolescents |
| [NCT02492295](https://clinicaltrials.gov/study/NCT02492295) | Not specified | Terminated | 12 | Low-dose propofol for severe refractory adult migraine in the ED; terminated early due to insufficient enrollment — safety signals were observed, but efficacy conclusions cannot be drawn |
| [NCT03789370](https://clinicaltrials.gov/study/NCT03789370) | Not specified | Unknown | 130 | Propofol vs. sevoflurane for anaesthesia maintenance; investigated whether propofol reduces postoperative headache frequency, indirectly supporting its protective effect in migraine-prone patients |
| [NCT02443220](https://clinicaltrials.gov/study/NCT02443220) | Not applicable | Completed | 315 | Electroacupuncture analgesia in off-pump cardiac surgery; propofol used as anaesthetic agent, not as a migraine intervention — limited relevance to repurposing question |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Clinical Guideline | *Headache* | 2025 American Headache Society guideline update on parenteral pharmacotherapies for acute migraine in the ED; provides current evidence-based positioning of propofol among available IV agents |
| [31621134](https://pubmed.ncbi.nlm.nih.gov/31621134/) | 2020 | Systematic Review | *Academic Emergency Medicine* | Systematic review evaluating safety and efficacy of propofol for acute migraine in the ED; consolidates evidence from both outpatient and inpatient settings |
| [39364614](https://pubmed.ncbi.nlm.nih.gov/39364614/) | 2024 | Systematic Review & Network Analysis | *Headache* | Network meta-analysis comparing parenteral agents for reducing relapse after severe acute migraine ED presentations; includes propofol among comparators |
| [35402989](https://pubmed.ncbi.nlm.nih.gov/35402989/) | 2022 | RCT | *Archives of Academic Emergency Medicine* | Double-blind RCT comparing propofol+granisetron vs. propofol+metoclopramide for symptom management of acute migraine; evaluated pain relief and adverse events |
| [35573713](https://pubmed.ncbi.nlm.nih.gov/35573713/) | 2022 | RCT | *Archives of Academic Emergency Medicine* | RCT comparing sumatriptan+propofol combination vs. sumatriptan alone for acute migraine in the ED; assessed whether propofol adds benefit over standard triptan therapy |
| [29456086](https://pubmed.ncbi.nlm.nih.gov/29456086/) | 2018 | RCT | *Journal of Emergency Medicine* | Prospective randomised trial of low-dose propofol for pediatric migraine in the ED; reported a favorable side effect profile and potential reduction in ED length of stay |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Systematic Review | *Cephalalgia* | Canadian Headache Society systematic review on migraine treatment in emergency settings; addresses evidence-practice gaps and discusses propofol's role |
| [27454834](https://pubmed.ncbi.nlm.nih.gov/27454834/) | 2016 | Review | *Expert Review of Neurotherapeutics* | Comprehensive drug profile of propofol for super-refractory migraine at sub-anesthetic doses; covers pharmacology, dosing, and clinical evidence |
| [32638172](https://pubmed.ncbi.nlm.nih.gov/32638172/) | 2020 | Review | *Current Pain and Headache Reports* | Review of IV migraine management in children and adolescents; covers propofol among other parenteral agents, noting limitations of current paediatric evidence |
| [10759925](https://pubmed.ncbi.nlm.nih.gov/10759925/) | 2000 | Observational | *Headache* | Landmark early report on propofol's unique effectiveness for intractable migraine at sub-anesthetic doses in an outpatient headache clinic; the foundational clinical observation that prompted subsequent controlled trials |

---

## Philippines Market Information

Propofol (DrugBank ID: DB00818) currently has **no registered products in the Philippines**. There are no active pharmaceutical licenses or market authorizations on record for this drug under the Philippine FDA registration system.

> **Note:** This does not necessarily mean propofol is clinically unavailable in the Philippines — it may be imported or available through institutional procurement — but it does mean no formal domestic registration exists in the current dataset. Regulatory pathway clarification is required before any repurposing programme is initiated.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Data Gap Notice:** Key warnings, contraindications, and drug-drug interaction data were not retrieved in this query cycle. Per the Evidence Pack meta-data:
> - **DG001 (Blocking):** Package insert warnings and contraindications have not been obtained. This gap must be resolved before S1 safety screening can proceed.
> - **DG002 (High):** Full MOA documentation from DrugBank is pending. This affects mechanistic plausibility analysis.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2/3 RCT (NCT01604785, n=74), two additional completed prospective studies in paediatric populations, and a growing body of RCTs and systematic reviews in adult ED settings consistently demonstrate that sub-anesthetic propofol can effectively terminate acute and refractory migraine attacks. The 2025 American Headache Society guideline update (PMID 41321235) further situates propofol within the current evidence landscape for parenteral migraine therapy. The mechanistic rationale — GABA-A potentiation suppressing cortical spreading depression and trigeminovascular activation — is biologically coherent, and the evidence quality justifies advancing to a structured feasibility assessment rather than immediate shelving.

**To proceed, the following is needed:**

- **Resolve DG001 (Blocking):** Obtain and review the full package insert (preferably from a jurisdiction where propofol is registered) to extract key warnings, contraindications, and special population restrictions before S1 safety screening
- **Resolve DG002 (High):** Complete DrugBank MOA data retrieval to formalise the mechanistic link narrative
- **DDI profile:** Manual review of propofol's known interactions (particularly with CNS depressants, opioids, benzodiazepines, and antiemetics commonly co-administered in migraine management)
- **Philippines regulatory pathway:** Determine whether propofol can be accessed through existing hospital procurement, parallel import, or compassionate use frameworks — and what registration steps would be required for a new indication claim
- **Route of administration constraint:** Propofol requires IV access, continuous monitoring, and resuscitation equipment; repurposing use must be explicitly scoped to **in-hospital or emergency department settings**, not outpatient or community use
- **Paediatric vs. adult strategy:** Clarify whether the initial programme targets paediatric refractory migraine (where the most direct RCT evidence exists) or adult ED migraine — each has different regulatory and operational implications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

