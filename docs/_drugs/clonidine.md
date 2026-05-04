---
layout: default
title: Clonidine
parent: 僅模型預測 (L5)
nav_order: 80
evidence_level: L5
indication_count: 10
---

# Clonidine
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

# Clonidine: From Hypertension to Tourette Syndrome

## One-Sentence Summary

Clonidine is a centrally acting α2-adrenergic receptor agonist classically used for hypertension, exerting its effects by suppressing norepinephrine release from the locus coeruleus and modulating prefrontal cortical signaling. Across 10 TxGNN-predicted indications, **Tourette Syndrome (TS)** carries the strongest evidence signal, backed by **3 clinical trials** (including two Phase 4 RCTs) and **19 publications** spanning a 2024 multicenter double-blind placebo-controlled RCT and European clinical practice guidelines. While faciodigitogenital syndrome holds the highest raw TxGNN score (rank #27, ~100%), it has no supporting clinical evidence and is assessed as Hold; Tourette Syndrome (TxGNN rank #382, score 99.98%) is the only indication reaching **L1 evidence** and merits a **Proceed with Guardrails** decision.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hypertension (centrally acting α2-adrenergic agonist) |
| Predicted New Indication | Tourette Syndrome |
| TxGNN Prediction Score | 99.98% (overall rank #382 among all drug-disease pairs) |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Currently, detailed mechanism of action data from DrugBank is unavailable for this report. Based on established clinical pharmacology, however, Clonidine selectively stimulates α2A-adrenergic receptors in the central nervous system. Presynaptically, it inhibits norepinephrine (NE) release from the locus coeruleus (LC), reducing sympathetic outflow throughout the brain. Postsynaptically, it strengthens prefrontal cortical α2A signaling, enhancing working memory and inhibitory control — this dual pathway is commonly referred to as the Arnsten mechanism and underpins Clonidine's utility in attention and impulse-control disorders.

Tourette Syndrome is characterized by dysregulation of the basal ganglia–prefrontal cortex–thalamus circuit, where excessive noradrenergic tone is believed to disinhibit the motor and vocal tic pathways. Clonidine targets this pathology directly: suppressing LC-NE overflow dampens the hyperactivation driving tics, while postsynaptic prefrontal α2A stimulation simultaneously addresses the highly prevalent comorbid ADHD symptoms. This dual action distinguishes Clonidine from dopamine-blocking agents (e.g., haloperidol, aripiprazole) and makes it particularly attractive for the significant subset of TS patients whose impairment stems more from inattention and impulsivity than from tic severity alone.

The clinical evidence base has solidified considerably. The 2022 European Society for the Study of Tourette Syndrome (ESSTS) guidelines formally list Clonidine as a second-line pharmacological option for tic disorders. A 2024 multicenter, randomized, double-blind, placebo-controlled trial (PMID 39258554) directly confirmed the efficacy and tolerability of the Clonidine adhesive patch in TS. A network meta-analysis published in *The Lancet Child & Adolescent Health* (2023, PMID 36528030) provided head-to-head comparative data positioning Clonidine quantitatively among all available pharmacological treatments. A concurrent animal study (2025, PMID 40392363) also revealed an anti-neuroinflammatory mechanism in a TS rat model, suggesting biological pathways beyond direct receptor agonism.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00370838](https://clinicaltrials.gov/study/NCT00370838) | Phase 4 | Completed | 12 | Double-blind, placebo run-in, crossover RCT directly comparing Clonidine vs levetiracetam for tic suppression in children with TS; most targeted and relevant completed trial |
| [NCT00152750](https://clinicaltrials.gov/study/NCT00152750) | Phase 4 | Unknown | 32 | Evaluated whether Clonidine-improved nighttime sleep reduces daytime aggression in children with TS + ADHD; supports Clonidine's role in managing comorbid behavioral symptoms |
| [NCT01172288](https://clinicaltrials.gov/study/NCT01172288) | Phase 2 | Completed | 31 | RCT of N-acetylcysteine vs placebo in TS children; Clonidine and guanfacine referenced as existing standard-of-care alpha-2 agonist treatments, contextualizing Clonidine's established position in the field |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39258554](https://pubmed.ncbi.nlm.nih.gov/39258554/) | 2024 | RCT (Double-blind) | Clinical Neuropharmacology | Multicenter, randomized, double-blind, placebo-controlled trial confirming efficacy and safety of Clonidine adhesive patch in TS — most direct and recent clinical validation |
| [38695046](https://pubmed.ncbi.nlm.nih.gov/38695046/) | 2024 | RCT/Clinical Study | Psychiatry Investigation | Clonidine patch in TS with comorbid ADHD; demonstrates dual benefit for both tic suppression and attentional symptoms |
| [36528030](https://pubmed.ncbi.nlm.nih.gov/36528030/) | 2023 | Network Meta-analysis | The Lancet Child & Adolescent Health | Compared efficacy, tolerability, and acceptability of pharmacological interventions for TS in children and adolescents; positions Clonidine quantitatively against all available agents |
| [34757514](https://pubmed.ncbi.nlm.nih.gov/34757514/) | 2022 | Clinical Guideline | European Child & Adolescent Psychiatry | Updated ESSTS European guidelines for TS pharmacological treatment; formally lists Clonidine as second-line treatment option |
| [40489853](https://pubmed.ncbi.nlm.nih.gov/40489853/) | 2025 | Narrative Review (Phase III/IV) | Medicine | Synthesizes Phase III and IV trials for pharmacological treatment of TS across age groups; provides current regulatory-grade evidence landscape for Clonidine |
| [31061209](https://pubmed.ncbi.nlm.nih.gov/31061209/) | 2019 | Systematic Review | Neurology | Comprehensive systematic review evaluating efficacy and risks of all tic treatments in TS and chronic tic disorders; high-tier independent evidence synthesis |
| [34286606](https://pubmed.ncbi.nlm.nih.gov/34286606/) | 2021 | Systematic Review | Journal of Psychopharmacology | Assessed quality of evidence for pharmacological TS treatment in children and adults; critical appraisal of Clonidine's evidence base including risk of bias |
| [40392363](https://pubmed.ncbi.nlm.nih.gov/40392363/) | 2025 | Animal/Mechanistic Study | Journal of Neuroimmune Pharmacology | Clonidine ameliorates neuroinflammation in a rat TS model via α2 receptor agonism; supports an anti-inflammatory mechanism complementary to noradrenergic modulation |
| [22728760](https://pubmed.ncbi.nlm.nih.gov/22728760/) | 2013 | Review | Neuropharmacology | Comprehensive review of pharmacological treatment for tic disorders and TS; Clonidine discussed as an established, guideline-supported treatment choice |
| [1414629](https://pubmed.ncbi.nlm.nih.gov/1414629/) | 1992 | Clinical Trial | Advances in Neurology | Early foundational clinical trial of Clonidine and clonazepam in TS; established the historical evidence basis for Clonidine's tic-suppressing effect |

---

## Philippines Market Information

Clonidine is currently **not registered** with the Food and Drug Administration of the Philippines (FDA Philippines). No product licenses were found in the regulatory database.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | No registrations found | — | — |

Clonidine is off-patent and available as generic tablets and transdermal patches in multiple other markets (US, EU, Japan, Taiwan). If a repurposing program is pursued in the Philippines, a new drug registration application or compassionate use pathway would be required.

---

## Safety Considerations

Please refer to the package insert for safety information.

No key warnings, contraindications, or drug-drug interaction data were returned in the current evidence pack query. The following data gaps require remediation before clinical use:

- **Key warnings and contraindications**: Philippines FDA package insert not yet retrieved (requires download and parsing of official product labeling from FDA Philippines website)
- **Drug-drug interactions**: DDI query returned no results; formal DDI assessment against co-medications commonly used in TS (antipsychotics, stimulants, SSRIs) is required

Based on the published pharmacological literature, clinicians should be aware that Clonidine is associated with rebound hypertension upon abrupt discontinuation, sedation, bradycardia, and hypotension — particularly relevant in pediatric populations with TS.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Clonidine has reached L1 evidence for Tourette Syndrome, anchored by a 2024 multicenter double-blind RCT and formal inclusion in European clinical guidelines; its noradrenergic mechanism of action directly addresses the established pathophysiology of TS, and it is already in standard clinical use for this indication in multiple jurisdictions.

**To proceed, the following is needed:**

- Retrieve and parse the Philippines FDA (or equivalent originator market) package insert to complete safety labeling review — currently a blocking data gap
- Conduct a formal drug-drug interaction assessment, particularly with antipsychotics (haloperidol, aripiprazole), stimulants (methylphenidate, amphetamine), and benzodiazepines that are co-prescribed in TS
- Confirm availability and feasibility of appropriate formulation: immediate-release tablet (standard for TS) or adhesive patch (validated in 2024 RCT) for importation or local registration
- Establish a pediatric dosing and monitoring protocol, as TS onset is typically ages 5–10 and most evidence is in the pediatric population
- Initiate regulatory pathway assessment at FDA Philippines: new drug registration, compassionate use, or hospital formulary inclusion
- Design a local pharmacovigilance plan, including cardiac monitoring (heart rate, blood pressure) given Clonidine's cardiovascular effects in a population without prior Philippines market authorization
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

