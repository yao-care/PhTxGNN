---
layout: default
title: Lynestrenol
parent: 僅模型預測 (L5)
nav_order: 212
evidence_level: L5
indication_count: 5
---

# Lynestrenol
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

# Lynestrenol: From Hormonal Contraception to Migraine with or without Aura

## One-Sentence Summary

Lynestrenol is a synthetic progestogen historically used in hormonal contraception and gynecological disorders (e.g., endometriosis, dysfunctional uterine bleeding), though no registered indication is available in the Philippines evidence pack.
The TxGNN model predicts it may be effective for **Migraine with or without Aura (susceptibility)**, with **0 clinical trials** and **20 publications** (primarily epilepsy-migraine shared-genetics literature) indirectly supporting this direction.
Notably, the closely related indication "migraine disorder" (TxGNN rank #2) carries direct historical evidence: a 1963 case series (PMID 14091721) specifically documented Lynestrenol's prophylactic use for migraine, lending mechanistic plausibility to the overall prediction cluster.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines; no approved indication data in this evidence pack (Lynestrenol is generally recognized as a progestogen for hormonal contraception and gynecological disorders) |
| Predicted New Indication | Migraine with or without Aura, Susceptibility |
| TxGNN Prediction Score | 99.51% |
| Evidence Level | L4 |
| Philippines Market Status | Not marketed (未上市) |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Lynestrenol is not available in this evidence pack. Based on known pharmacology, Lynestrenol is a 19-nortestosterone-derived progestogen that binds progesterone receptors and is partially converted in vivo to norethisterone, its active metabolite. Progestogens modulate neuronal excitability through two relevant pathways: (1) stabilization of estrogen withdrawal — the primary driver of menstrual migraine — and (2) enhancement of GABA-A receptor activity via neurosteroid metabolites that resemble allopregnanolone, thereby raising the cortical excitability threshold.

The TxGNN model's prediction for "migraine with or without aura, susceptibility" is anchored in the well-established genetic and neurophysiological overlap between epilepsy and migraine. Both conditions share ion-channel susceptibility genes (e.g., SCN1A, CACNA1A, SCN8A), and agents capable of stabilizing channel excitability have theoretical cross-indication applicability. The 20 retrieved publications for this rank-1 prediction collectively document this shared biological basis — they do not directly study Lynestrenol, but they define the mechanistic corridor through which the prediction is made.

Direct Lynestrenol–migraine evidence is strongest for the rank-2 indication ("migraine disorder", score 99.49%): PMID 14091721 (1963) reported uncontrolled prophylactic use of Lynestrenol (Orgametril) in migraine patients, and a 2026 comparative review (PMID 41723577) discusses progestogen-containing oral contraceptives in the management of menstrual-cycle-associated migraine and dysmenorrhea. Taken together, the evidence supports a plausible but unconfirmed hormonal mechanism rather than a direct neurological drug effect, and the absolute clinical evidence base remains thin.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

*(Extracted from predicted_indications[0] — "migraine with or without aura, susceptibility to" — ranked by relevance to the epilepsy-migraine shared-susceptibility mechanism)*

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [33856647](https://pubmed.ncbi.nlm.nih.gov/33856647/) | 2021 | Review | Molecular Neurobiology | Epilepsy and migraine share genetic and molecular mechanisms (ion-channel genes, CSD); identifies shared therapeutic targets relevant to progestogen modulation |
| [23294289](https://pubmed.ncbi.nlm.nih.gov/23294289/) | 2013 | Genetic Study | Epilepsia | Demonstrates shared genetic susceptibility between migraine and epilepsy in the EPGP cohort, supporting the knowledge-graph link underlying TxGNN's prediction |
| [17460155](https://pubmed.ncbi.nlm.nih.gov/17460155/) | 2007 | Genetic Linkage Study | Neurology | Maps a locus on chromosome 9q co-segregating with both occipitotemporal epilepsy and migraine with visual aura in a large family |
| [30267335](https://pubmed.ncbi.nlm.nih.gov/30267335/) | 2018 | Meta-analysis | Neurological Sciences | MTHFR C677T polymorphism associated with epilepsy susceptibility; MTHFR variants are also implicated in migraine, reinforcing shared pathways |
| [34575901](https://pubmed.ncbi.nlm.nih.gov/34575901/) | 2021 | Review | Int J Mol Sci | Reviews molecular targets for antiepileptogenesis including ion-channel stabilizers; contextualizes why progesterone-pathway drugs might have relevance |
| [34209535](https://pubmed.ncbi.nlm.nih.gov/34209535/) | 2021 | Review | Int J Mol Sci | Examines bidirectional neuroinflammation-epilepsy relationship; neuroinflammatory pathways are also implicated in migraine chronification |
| [22266888](https://pubmed.ncbi.nlm.nih.gov/22266888/) | 2011 | Review | Seminars in Neurology | Genetics of epilepsy, including ion-channel gene families also relevant to migraine susceptibility |
| [16201993](https://pubmed.ncbi.nlm.nih.gov/16201993/) | 2005 | Review | Epilepsia | GABA-A and glutamate receptor compositional changes drive limbic hyperexcitability; relevant to progestogen-mediated GABA-A upregulation mechanism |
| [28086980](https://pubmed.ncbi.nlm.nih.gov/28086980/) | 2017 | Review | J Neuroinflammation | Neuroinflammation in post-traumatic epileptogenesis; provides mechanistic context for excitability modulation |
| [22938964](https://pubmed.ncbi.nlm.nih.gov/22938964/) | 2012 | Review | Handbook of Clinical Neurology | In vivo and in vitro animal models of epilepsy; foundational reference for understanding seizure threshold modulation |

> **Important caveat**: All publications above address epilepsy or epilepsy-migraine comorbidity — none directly study Lynestrenol. The most relevant direct evidence (PMID [14091721](https://pubmed.ncbi.nlm.nih.gov/14091721/), 1963 Lynestrenol migraine prophylaxis case series) is catalogued under the rank-2 indication "migraine disorder."

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Clinician note**: For progestogens used near migraine populations, a key distinction applies — combined hormonal contraceptives (containing estrogen) are contraindicated in migraine with aura due to increased stroke risk; progestogen-only preparations carry a substantially lower vascular risk profile. This distinction is critical if Lynestrenol is being evaluated for menstrual migraine.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.51%), and a biologically plausible hormonal-neurological mechanism exists, but the evidence base for the primary predicted indication (migraine with or without aura, susceptibility) consists entirely of indirect epilepsy-migraine genetics literature with zero clinical trials. The drug is not registered in the Philippines, and key safety data (package insert warnings, contraindications, MOA) remain unavailable.

**To proceed, the following is needed:**

- **Safety gap (Blocking):** Obtain the Lynestrenol package insert to extract warnings, contraindications, and special population risks before any safety evaluation (DG001)
- **MOA gap (High):** Query DrugBank API to retrieve mechanism of action, pharmacokinetics, and metabolite profile, particularly norethisterone conversion rates (DG002)
- **Evidence deepening:** Conduct a targeted PubMed search for "lynestrenol AND (migraine OR menstrual migraine OR menstrual headache)" to identify any post-1963 clinical data beyond PMID 14091721
- **Indication refinement:** Evaluate whether the rank-2 indication "migraine disorder" (L3 evidence, direct historical use) is a more actionable starting point than rank-1 "susceptibility" (L4, indirect genetics evidence)
- **Regulatory pathway:** Assess requirements for Philippines FDA registration before any clinical development planning
- **Aura safety review:** Confirm whether progestogen-only formulations are safe in migraine-with-aura patients, distinguishing from combined hormonal contraceptive contraindications
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

