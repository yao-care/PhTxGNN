---
layout: default
title: Methylphenidate
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 4
---

# Methylphenidate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **4** 個
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

The `txgnn-pipeline` skill is focused on technical pipeline management and doesn't override the report-generation instructions already defined. Proceeding to generate the evaluation report based on the Evidence Pack.

---

# Methylphenidate: From ADHD to Specific Developmental Disorder

## One-Sentence Summary

Methylphenidate (commonly known as Ritalin) is a central nervous system stimulant widely established for treating Attention-Deficit/Hyperactivity Disorder (ADHD), acting by blocking dopamine and norepinephrine reuptake transporters to enhance prefrontal cortical function.
The TxGNN model predicts it may be effective for **Specific Developmental Disorder**, with **16 clinical trials** and **18 publications** currently supporting this direction.

> **Note on prediction ranking**: This Evidence Pack contains 4 TxGNN predictions. Ranks 1 (faciodigitogenital syndrome) and 2 (chondromyxoid fibroma) each scored L5 with zero supporting evidence and are explicitly flagged in the repurposing rationale as likely model artifacts — the mechanistic links are implausible. This report focuses on **Rank 3: Specific Developmental Disorder**, which carries the strongest evidence base (L2) and the most actionable recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ADHD — globally established clinical use; Methylphenidate holds no Philippines regulatory registration |
| Predicted New Indication | Specific Developmental Disorder |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Philippines Market Status | Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Formal mechanism of action data from DrugBank was not retrieved for this report. Based on published pharmacological literature, however, methylphenidate acts primarily by blocking the dopamine transporter (DAT) and norepinephrine transporter (NET), increasing synaptic availability of both neurotransmitters in the prefrontal cortex (PFC). This strengthens attentional control networks, working memory, and executive function — all functions governed by the fronto-striatal-cerebellar circuitry.

Specific developmental disorders — including childhood apraxia of speech (CAS, ICD-10 F80.0), developmental dyslexia (F81.0), and developmental coordination disorder (F82) — share a core pathophysiological feature: disrupted basal ganglia–prefrontal cortex circuits involved in motor sequence learning, language processing, and procedural learning. These circuits overlap substantially with those implicated in ADHD. Apraxia of speech in particular involves dopaminergic basal ganglia motor-sequence pathways, providing a direct mechanistic hypothesis for why methylphenidate may confer benefit beyond ADHD alone.

Crucially, this is not merely theoretical: a completed Phase 2 double-blind RCT (NCT05185583) directly tested methylphenidate against placebo for speech intelligibility in children with childhood apraxia of speech. The high co-occurrence of ADHD with specific developmental disorders further supports shared neurobiological vulnerabilities that methylphenidate's DAT/NET mechanism may simultaneously address.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT05185583](https://clinicaltrials.gov/study/NCT05185583) | Phase 2 | Completed | 18 | Double-blind, placebo-controlled crossover RCT directly testing MPH for speech intelligibility in children aged 6–12 with childhood apraxia of speech (CAS); the single most directly relevant trial in this pack |
| [NCT05974241](https://clinicaltrials.gov/study/NCT05974241) | Phase 4 | Completed | 36 | Crossover study comparing MPH and aripiprazole for irritability and emotion dysregulation in ADHD children; characterises clinical profiles that overlap with co-morbid developmental disorders |
| [NCT01470261](https://clinicaltrials.gov/study/NCT01470261) | N/A | Completed | 1,398 | ADDUCE project — large 2-year observational study examining MPH adverse effects on growth, neurological, psychiatric, and cardiovascular systems in children and adults with ADHD; key long-term safety reference |
| [NCT01363544](https://clinicaltrials.gov/study/NCT01363544) | Phase 2/3 | Completed | 112 | RCT comparing exercise and neurofeedback to pharmacological treatment (MPH) in ADHD children; evaluates neurocognitive and EEG-based cortical regulation outcomes, relevant to developmental circuit overlap |
| [NCT04647500](https://clinicaltrials.gov/study/NCT04647500) | N/A | Completed | 45 | Dual-tracer PET study examining how MPH modulates the dopaminergic and noradrenergic systems in individuals with 22q11.2 deletion syndrome — a neurogenetic condition with 35–45% ADHD comorbidity and atypical brain development |
| [NCT05916339](https://clinicaltrials.gov/study/NCT05916339) | Phase 4 | Recruiting | 500 | Pragmatic SMART trial comparing MPH vs. amphetamine for ADHD in children and adolescents with autism spectrum disorder; findings will inform treatment across overlapping neurodevelopmental diagnoses |
| [NCT02167048](https://clinicaltrials.gov/study/NCT02167048) | Phase 1/2 | Active, not recruiting | 52 | Crossover study comparing low vs. standard psychostimulant doses on executive functions (working memory, selective attention, cognitive flexibility) in ADHD children aged 6–18 |
| [NCT07024303](https://clinicaltrials.gov/study/NCT07024303) | Early Phase 1 | Not yet recruiting | 20 | Study comparing medication (including MPH) and behavioural treatment for challenging behaviour in children and adolescents with autism; uses direct observation within natural contexts |
| [NCT05669170](https://clinicaltrials.gov/study/NCT05669170) | Phase 2 | Not yet recruiting | 60 | Safety and efficacy of MPH for apathy in Veterans with Parkinson's disease; explores dopaminergic mechanisms underpinning motivation and goal-directed behaviour — a relevant mechanistic analogy |
| [NCT01554046](https://clinicaltrials.gov/study/NCT01554046) | N/A | Completed | 40 | Investigates familial treatment response to Ritalin IR in ADHD, examining both symptom improvement and side-effect profiles across family members — provides real-world tolerability data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [41128391](https://pubmed.ncbi.nlm.nih.gov/41128391/) | 2026 | Controlled pharmacological study | Psychiatry and Clinical Neurosciences | Longitudinal PET study in adult ADHD demonstrating that extended-release MPH distinctly modulates DAT and NET binding; directly characterises the transporter mechanism underlying MPH's clinical effects |
| [40527386](https://pubmed.ncbi.nlm.nih.gov/40527386/) | 2025 | Longitudinal cohort | Progress in Neuro-Psychopharmacology & Biological Psychiatry | MPH exposure has age-dependent effects on brain structure (n=89 ADHD vs. 91 controls); demonstrates treatment-associated neuroplasticity changes relevant to developmental brain interventions |
| [33012168](https://pubmed.ncbi.nlm.nih.gov/33012168/) | 2021 | Review | Clinical EEG and Neuroscience | QEEG review covering ADHD and learning disabilities; supports personalized medicine — EEG biomarkers can distinguish neurodevelopmental subtypes and predict differential MPH response |
| [22923783](https://pubmed.ncbi.nlm.nih.gov/22923783/) | 2015 | Review | Journal of Attention Disorders | Comprehensive review of MPH cellular and molecular mechanisms in adult vs. juvenile brain; addresses developmental consequences of treatment directly relevant to paediatric developmental disorder use |
| [19627998](https://pubmed.ncbi.nlm.nih.gov/19627998/) | 2009 | Review | Neuropharmacology | Foundational review of ADHD neurobiology — fronto-striatal circuitry, dopaminergic and noradrenergic pathways, and genetic architecture; establishes the mechanistic basis for circuit-level overlap with developmental disorders |
| [8719499](https://pubmed.ncbi.nlm.nih.gov/8719499/) | 1996 | Cross-sectional | Clinical EEG | QEEG-based discriminant functions distinguished children with **specific developmental learning disorders** from ADD/ADHD and normal controls with high accuracy; QEEG also predicted MPH vs. dextroamphetamine treatment response — directly supports the target indication |
| [20483462](https://pubmed.ncbi.nlm.nih.gov/20483462/) | 2010 | Observational/EEG | Psychiatry Research | EEG coherence differences identified between good and poor MPH responders in ADHD children; supports biomarker-guided treatment selection for neurodevelopmental conditions |
| [36688969](https://pubmed.ncbi.nlm.nih.gov/36688969/) | 2024 | Interventional | European Child & Adolescent Psychiatry | First objective study of MPH and physiotherapy effects on graphomotor/handwriting movements in ADHD children — directly relevant to the motor developmental disorder dimension |
| [25989180](https://pubmed.ncbi.nlm.nih.gov/25989180/) | 2015 | Pharmacogenetic study | Genes, Brain, and Behavior | LPHN3 gene variants predict both ADHD susceptibility and MPH treatment response; supports a precision-medicine approach for neurodevelopmental conditions sharing this genetic architecture |
| [11990715](https://pubmed.ncbi.nlm.nih.gov/11990715/) | 2002 | Animal model | Behavioural Pharmacology | SHRSP rats validated as an animal model of developmental disorder; MPH normalised hyperactivity, emotional, and cognitive deficits — providing preclinical mechanistic support for the repurposing hypothesis |

---

## Philippines Market Information

Methylphenidate currently has **no registered products** in the Philippines (total licences: 0, market status: 未上市). No product table can be generated.

As a Schedule II–equivalent controlled psychostimulant in most jurisdictions, any future Philippines registration would require a controlled substance clearance from the Philippine Drug Enforcement Agency (PDEA) in addition to standard Philippine FDA (Food and Drug Administration) registration — a dual-track regulatory pathway not required for most repurposing candidates.

---

## Safety Considerations

Please refer to the package insert for safety information. No formal warnings, contraindications, or drug interaction data were retrievable for this report.

Based on drug class knowledge, the following areas warrant particular attention before any clinical or regulatory action:

- **Controlled substance classification**: Methylphenidate's Schedule II status in most countries reflects its stimulant abuse potential. Philippine PDEA classification must be confirmed before any registration effort begins.
- **Cardiovascular monitoring**: Standard precaution for CNS stimulants; required in patients with pre-existing cardiac conditions.
- **Paediatric growth monitoring**: The ADDUCE observational study (NCT01470261, n=1,398) was specifically designed to track long-term effects on growth — directly relevant to a paediatric developmental disorder indication.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2 double-blind RCT (NCT05185583) directly tested methylphenidate in children with childhood apraxia of speech — a specific developmental disorder — providing L2-level evidence. The fronto-striatal mechanistic overlap between ADHD and specific developmental disorders is well-grounded in neuroscience. However, the pivotal trial enrolled only 18 participants, the drug is not registered in the Philippines, and its controlled substance status adds a non-trivial regulatory hurdle.

**To proceed, the following is needed:**

- Obtain full package insert (DrugBank and/or TFDA source) to document MOA, warnings, and contraindications formally
- Confirm Philippine PDEA Schedule classification for methylphenidate and understand the controlled substance registration pathway at Philippine FDA
- Obtain and review the full publication of NCT05185583 results (Phase 2 apraxia of speech RCT) once available
- Commission a systematic review of methylphenidate evidence across specific developmental disorder subtypes (F80–F83) to quantify the full evidence base
- Design a larger confirmatory study — or identify an existing investigator-initiated trial — targeting Philippine paediatric populations with specific developmental disorders
- Prepare a benefit-risk summary that accounts for the abuse-potential profile when submitting to regulatory bodies
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

