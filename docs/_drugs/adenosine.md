---
layout: default
title: Adenosine
parent: 僅模型預測 (L5)
nav_order: 15
evidence_level: L5
indication_count: 2
---

# Adenosine
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

# Adenosine: From Supraventricular Tachycardia to Catecholaminergic Polymorphic Ventricular Tachycardia

---

## One-Sentence Summary

Adenosine is a naturally occurring purine nucleoside clinically established for terminating paroxysmal supraventricular tachycardia (PSVT) via rapid AV nodal blockade, though it currently holds no Philippines market authorization.
The TxGNN model's highest-ranked prediction ("obsolete bundle branch block", Rank 1) was set aside as it corresponds to a retired disease ontology term with no current clinical classification; the substantive evaluation focuses on **Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT)** (Rank 2, score 99.42%), a rare life-threatening inherited arrhythmia.
This repurposing direction is supported by **1 Phase 2a clinical trial** (testing a related A1 receptor agonist) and **13 publications** spanning mechanistic, preclinical, and clinical observation evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines; clinically established internationally for PSVT termination |
| Predicted New Indication | Catecholaminergic Polymorphic Ventricular Tachycardia (CPVT) |
| TxGNN Prediction Score | 99.42% *(Rank 2; Rank 1 discarded — "obsolete bundle branch block" is a retired disease ontology term, not a valid clinical target)* |
| Evidence Level | L4 (Preclinical/mechanistic studies + 1 early-phase exploratory trial with a related compound) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Adenosine acts primarily on cardiac A1 adenosine receptors, activating inhibitory Gi proteins that suppress adenylyl cyclase. The resulting drop in intracellular cAMP reduces protein kinase A (PKA) activity, which in turn decreases phosphorylation of the cardiac ryanodine receptor (RyR2) at key regulatory sites (Ser2808, Ser2814)—reducing spontaneous sarcoplasmic reticulum (SR) calcium leak. Additionally, adenosine exerts direct anti-adrenergic effects that antagonize the downstream consequences of catecholamine surge, and its short-acting AV nodal suppression is a well-established electrophysiological tool in clinical cardiology.

CPVT is caused precisely by dysregulated RyR2 or calsequestrin-2 function: inherited mutations allow pathological SR calcium leak under sympathetic stimulation (exercise, emotional stress), triggering fatal ventricular arrhythmias in structurally normal hearts. Adenosine's suppression of the cAMP–PKA–RyR2 phosphorylation axis directly counters CPVT's core pathomechanism. Biochemical evidence (PMID 23747301) further shows that ATP—rapidly dephosphorylated to adenosine in vivo—directly binds the RyR2 central domain (approximately residues 2000–2500), the exact region where the majority of CPVT-causative mutations cluster, providing molecular-level plausibility beyond the receptor-signaling cascade.

Two independent lines of translational evidence reinforce this rationale. First, a selective A1 adenosine receptor agonist (AGP100) is currently enrolling in a Phase 2a CPVT trial (NCT07263139), providing indirect but mechanistically on-target proof-of-concept for the adenosine–A1R–cAMP axis as a CPVT therapeutic strategy. Second, a published case report (PMID 18313614) documents that intravenous ATP successfully terminated bidirectional ventricular tachycardia in a pediatric CPVT patient, representing the first direct clinical observation linking an adenosine-class molecule to acute CPVT arrhythmia management.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT07263139](https://clinicaltrials.gov/study/NCT07263139) | Phase 2a | Recruiting | 10 | AGP100 (selective A1 adenosine receptor agonist, not adenosine itself) evaluated for safety, tolerability, and exploratory efficacy in adult CPVT patients. The trial directly validates the adenosine–A1R axis as a CPVT therapeutic target, providing high-relevance class-effect evidence in support of adenosine repurposing. Study started January 2026; completion expected June 2027. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18313614](https://pubmed.ncbi.nlm.nih.gov/18313614/) | 2008 | Case Report | *Heart Rhythm* | ATP (adenosine precursor) terminated bidirectional ventricular tachycardia in a pediatric CPVT patient — the most direct clinical observation linking adenosine-class molecules to acute CPVT arrhythmia termination. |
| [23747301](https://pubmed.ncbi.nlm.nih.gov/23747301/) | 2013 | Basic Science | *Biochim Biophys Acta* | ATP directly binds the RyR2 central domain (aa ~2000–2500), the precise mutation hotspot region for CPVT (R2474S, P2328S, N2386I, etc.), providing in vitro mechanistic support for an adenosine/ATP–RyR2 molecular interaction. |
| [40165484](https://pubmed.ncbi.nlm.nih.gov/40165484/) | 2025 | Review / Consensus | *Europace* | ESC/HRS/APHRS/LAHRS joint clinical consensus statement on pharmacological provocation testing in cardiac electrophysiology; contextualizes adenosine's diagnostic and therapeutic roles in inherited arrhythmia syndromes including CPVT. |
| [38776406](https://pubmed.ncbi.nlm.nih.gov/38776406/) | 2024 | Basic Science | *Cardiovascular Research* | PDE2A/PDE4B gene therapy prevents HF and arrhythmias in mice via improved subcellular cAMP compartmentation; reinforces the cAMP–PKA–RyR2 axis as a central, tractable target in arrhythmia settings overlapping with CPVT pathophysiology. |
| [41691612](https://pubmed.ncbi.nlm.nih.gov/41691612/) | 2026 | Basic Science | *J Physiol* | Human cardiac–neural microtissues reveal CPVT is also a disease of the sympathetic neuron; adenosine's anti-adrenergic properties may provide dual protection by modulating both cardiomyocyte and sympathetic nerve components of CPVT. |
| [21699856](https://pubmed.ncbi.nlm.nih.gov/21699856/) | 2011 | Clinical Observation | *Heart Rhythm* | Postpacing abnormal repolarization documented in CPVT with RyR2 mutation; supports the value of electrophysiological provocation protocols in which adenosine is a standard pharmacological agent. |
| [30209242](https://pubmed.ncbi.nlm.nih.gov/30209242/) | 2018 | Basic Science | *Science Translational Medicine* | SR calcium leak via RyR2 selectively drives arrhythmia (not heart failure progression) in murine models; validates RyR2 stabilization as an antiarrhythmic target directly downstream of adenosine's cAMP-lowering action. |
| [35577932](https://pubmed.ncbi.nlm.nih.gov/35577932/) | 2022 | Basic Science | *Communications Biology* | TECRL deficiency causes aberrant mitochondrial function and CPVT-like arrhythmias; expands the CPVT disease model landscape and underscores the need for multi-mechanistic therapeutic approaches. |
| [23858002](https://pubmed.ncbi.nlm.nih.gov/23858002/) | 2013 | Basic Science | *J General Physiology* | Calsequestrin regulation of single cardiac RyR2 in normal and CPVT pathological conditions; clarifies luminal Ca²⁺ regulation as a key modulator of the same release pathway targeted by adenosine. |
| [39148245](https://pubmed.ncbi.nlm.nih.gov/39148245/) | 2024 | Review | *Paediatric Anaesthesia* | Clinical practice guide on pediatric arrhythmias for anesthesiologists; includes CPVT management context and notes adenosine as the standard first-line agent for SVT, supporting perioperative relevance in CPVT patients. |

---

## Philippines Market Information

Adenosine currently holds **no market authorization in the Philippines** (0 registered products across all dosage forms and routes of administration).

> For reference, adenosine is approved and in routine clinical use in many other jurisdictions (United States, European Union, and others) primarily for acute PSVT termination and pharmacological cardiac stress testing. Any investigational use in the Philippines would require a separate regulatory pathway (e.g., compassionate use or clinical trial authorization).

---

## Safety Considerations

Please refer to the package insert for safety information.

> ⚠️ **Data Gap Notice:** Philippines-specific prescribing information (package insert warnings and contraindications) was not available in this evidence pack. This is classified as a **blocking data gap (DG001)** that must be resolved before any formal safety pre-evaluation can proceed. No drug–drug interaction data was identified in the current evidence review.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Adenosine's mechanistic connection to CPVT pathophysiology is biologically well-grounded—the cAMP–PKA–RyR2 axis, direct ATP–RyR2 binding, and anti-adrenergic effects all converge on CPVT's core pathomechanism—and is bolstered by a direct case observation and an ongoing A1R agonist trial. However, the available evidence concerns class-effect molecules (ATP, AGP100), not adenosine itself; the lone clinical trial is early-stage (Phase 2a, n=10) and tests a different compound; and there is no Philippines regulatory pathway currently in place. The overall evidence remains at L4, making clinical translation premature without further groundwork.

**To proceed, the following is needed:**

- **Regulatory pathway**: Establish Philippines FDA registration or import authorization for investigational use; adenosine is not currently marketed in the Philippines
- **Safety data (Blocking — DG001)**: Obtain and review Philippines-specific package insert warnings and contraindications before any safety pre-evaluation
- **MOA documentation (High — DG002)**: Formally document adenosine's mechanism of action from DrugBank or peer-reviewed sources
- **Drug–drug interaction profile**: No DDI data was identified; a formal DDI review is required, particularly for co-administration with antiarrhythmic agents (β-blockers, flecainide) commonly used in CPVT
- **Formulation strategy**: Adenosine has an extremely short plasma half-life (~10 seconds IV); chronic CPVT management would require a novel delivery approach (e.g., slow-release formulation or use of a selective, orally bioavailable A1R agonist such as AGP100)
- **Direct adenosine evidence**: Design or identify a prospective protocol specifically evaluating adenosine (not just adenosine receptor agonists) in a CPVT-relevant efficacy endpoint, building on the AGP100 trial design and the ATP case report as scientific precedent
- **Await AGP100 Phase 2a results (NCT07263139)**: Results from this trial (expected 2027) will substantially strengthen or weaken the case for adenosine in CPVT, and should be a formal go/no-go decision trigger
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

