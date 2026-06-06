---
layout: default
title: Ketorolac
parent: 僅模型預測 (L5)
nav_order: 193
evidence_level: L5
indication_count: 3
---

# Ketorolac
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

The txgnn-pipeline skill is focused on model training and deployment. This task is report generation, which is fully governed by the system prompt instructions. Proceeding directly to write the report.

---

# Ketorolac: From Acute Pain to Headache Disorder

## One-Sentence Summary

Ketorolac is a potent parenteral non-steroidal anti-inflammatory drug (NSAID), widely used in clinical practice for the short-term management of moderate to severe acute pain.
The TxGNN model predicts it may be effective for **Headache Disorder** (encompassing migraine and tension-type headache), with **36 clinical trials** and **19 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines (no approved indication on record) |
| Predicted New Indication | Headache Disorder |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L1 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on known pharmacological information, Ketorolac is a COX-1/COX-2 inhibitor belonging to the pyrrolo-pyrrole NSAID class. It works by blocking cyclooxygenase enzymes, which reduces the synthesis of prostaglandins — key chemical messengers involved in pain sensitization, inflammation, and vasodilation.

Prostaglandins play a central role in the pathophysiology of both migraine and tension-type headache. In migraine, prostaglandin E2 (PGE2) activates and sensitizes trigeminal nociceptors, contributing to the characteristic unilateral throbbing pain and associated photophobia and phonophobia. Ketorolac's potent inhibition of prostaglandin synthesis — combined with its parenteral availability for rapid-onset delivery — makes it mechanistically well-suited for aborting acute headache attacks, particularly in emergency department settings where oral medications cannot be used.

Clinically, Ketorolac has been deployed as a first-line or comparator agent for acute migraine and tension-type headache since the early 1990s. Its inclusion as the active "standard care" arm in multiple Phase 3 and Phase 4 randomized trials confirms its de facto role in headache management, giving the TxGNN prediction strong empirical grounding beyond model scoring alone.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01267864](https://clinicaltrials.gov/study/NCT01267864) | Phase 4 | Completed | 330 | Head-to-head RCT comparing IV valproate, IV metoclopramide, and IV ketorolac for acute migraine in the ED |
| [NCT01011673](https://clinicaltrials.gov/study/NCT01011673) | Phase 4 | Completed | 123 | Ketorolac vs metoclopramide/diphenhydramine for acute tension-type headache in the ED |
| [NCT01596166](https://clinicaltrials.gov/study/NCT01596166) | Phase 4 | Completed | 56 | IV ketorolac + metoclopramide combination for pediatric migraine in the emergency department |
| [NCT02358681](https://clinicaltrials.gov/study/NCT02358681) | Phase 3 | Completed | 59 | Non-inferiority trial of intranasal vs IV ketorolac for acute migraine in children |
| [NCT00483717](https://clinicaltrials.gov/study/NCT00483717) | Phase 2 | Completed | 173 | Double-blind placebo-controlled study of intranasal ketorolac for acute migraine — safety and efficacy |
| [NCT01807234](https://clinicaltrials.gov/study/NCT01807234) | Phase 4 | Completed | 72 | Ketorolac nasal spray vs sumatriptan nasal spray vs placebo for acute migraine abortive therapy |
| [NCT03081416](https://clinicaltrials.gov/study/NCT03081416) | Phase 3 | Completed | 80 | THINK Trial: intranasal ketamine vs standard care (ketorolac) for acute headache in the ED |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Sub-dissociative ketamine vs ketorolac for acute tension-type headache in the ED |
| [NCT02664116](https://clinicaltrials.gov/study/NCT02664116) | Phase 4 | Unknown | 40 | IM ketorolac vs oral diclofenac potassium powder (Cambia) for acute severe migraine |
| [NCT05983354](https://clinicaltrials.gov/study/NCT05983354) | NA | Unknown | 55 | Pilot RCT comparing oral vs parenteral ketorolac + metoclopramide for acute migraine in the ED |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35138658](https://pubmed.ncbi.nlm.nih.gov/35138658/) | 2022 | Meta-analysis | Acad Emerg Med | Systematic review and meta-analysis confirming efficacy of parenteral ketorolac in treating acute migraine headache |
| [39674934](https://pubmed.ncbi.nlm.nih.gov/39674934/) | 2025 | Meta-analysis | Ann Emerg Med | Bayesian network meta-analysis ranking the relative effectiveness and safety of pharmacologic therapies for migraine in the ED |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | 2025 AHS guideline update on parenteral pharmacotherapies for acute migraine management in the ED — includes ketorolac recommendations |
| [35670115](https://pubmed.ncbi.nlm.nih.gov/35670115/) | 2022 | RCT | Headache | Randomized trial assessing efficacy and safety of IV metoclopramide alone vs with add-on IV ketorolac for pediatric migraine in the ED |
| [30783794](https://pubmed.ncbi.nlm.nih.gov/30783794/) | 2019 | RCT | Neurol Sci | Prospective double-blind RCT comparing ketorolac 30 mg, dexamethasone, metoclopramide, and chlorpromazine IV for migraine pain relief and recurrence prevention |
| [1514724](https://pubmed.ncbi.nlm.nih.gov/1514724/) | 1992 | RCT | Ann Emerg Med | Landmark early RCT: IM ketorolac vs meperidine/hydroxyzine for acute migraine in the ED |
| [37849443](https://pubmed.ncbi.nlm.nih.gov/37849443/) | 2024 | Meta-analysis | Adv Clin Exp Med | Updated systematic review and meta-analysis comparing IV ketorolac vs IV metoclopramide in adult migraine patients |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Review | Headache | American Headache Society updated evidence assessment of pharmacological therapies for acute migraine, including ketorolac |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Review | Cephalalgia | Canadian Headache Society systematic review and recommendations on migraine pain management in emergency settings |
| [37291500](https://pubmed.ncbi.nlm.nih.gov/37291500/) | 2023 | Meta-analysis | BMC Neurol | Network meta-analysis of randomized controlled trials comparing metoclopramide and other antimigraine drugs (including ketorolac) for acute attacks |

---

## Philippines Market Information

Ketorolac is currently **not registered** in the Philippines. No product authorizations were found in the regulatory database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** A notable drug interaction has been documented in the literature (PMID [7928331](https://pubmed.ncbi.nlm.nih.gov/7928331/)): co-administration of ketorolac with lithium (used in cluster headache prophylaxis) has been associated with lithium neurotoxicity. Clinicians should exercise caution when using ketorolac in patients on lithium therapy.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 and Phase 4 RCTs, corroborated by recent meta-analyses and 2025–2026 clinical practice guidelines from major headache societies, establish ketorolac as an evidence-based treatment for acute headache disorders. This is one of the highest-confidence TxGNN predictions reviewable — the clinical evidence substantially predates and independently validates the model output. The primary barrier to Philippines deployment is the absence of local registration, not a lack of efficacy evidence.

**To proceed, the following is needed:**
- **Philippines FDA Registration**: Submit a product registration dossier (no licenses currently on record); identify a local marketing authorization holder or distributor
- **Package Insert Review**: Obtain and parse the full package insert to document black-box warnings, contraindications (e.g., renal impairment, peri-operative CABG use, active peptic ulcer disease), and duration-of-use restrictions (ketorolac is typically limited to ≤5 days in most regulatory labels due to cumulative GI and renal toxicity risk)
- **Formulation Decision**: Confirm target route of administration — parenteral (IV/IM) formulations carry the strongest evidence base; intranasal formulations (e.g., Sprix®) show promise but with a smaller evidence body
- **Drug Interaction Screening**: Establish a pharmacovigilance protocol for high-risk combinations, particularly with lithium, anticoagulants, and other NSAIDs
- **Risk Management Plan**: Define appropriate patient selection criteria, monitoring parameters (renal function, GI symptoms), and maximum treatment duration for local prescribing guidelines
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

