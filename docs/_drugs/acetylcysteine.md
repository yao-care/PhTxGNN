---
layout: default
title: Acetylcysteine
parent: Model Prediction Only (L5)
nav_order: 14
evidence_level: L5
indication_count: 10
last_modified_at: 2026-10-15
description: "Acetylcysteine: predicted new indication Thrombotic disease (evidence level L5). Approved use: Bronchitis, paracetamol poisoning, cystic fibrosis, bronchiectasis…"
monitor_inn: "Acetylcysteine"
predicted_indications: ["thrombotic disease", "closed-angle glaucoma", "nasal cavity disease", "dry eye syndrome", "pharyngitis", "acute laryngopharyngitis", "tracheal disease", "transient ischemic attack (disease)", "angle-closure glaucoma"]
---

# Acetylcysteine
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

# Acetylcysteine: From Bronchitis and Paracetamol Poisoning to Thrombotic Disease

## One-Sentence Summary

Acetylcysteine (N-acetylcysteine, NAC) was originally used for respiratory conditions such as bronchitis, cystic fibrosis and bronchiectasis, for paracetamol poisoning, and for amyloidosis.
The TxGNN model predicts it may be effective for **thrombotic disease**, with **7 clinical trials** and **20 publications** compiled for this direction. Only one Phase 3 trial is completed, and its results were not available in the data.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bronchitis, paracetamol poisoning, cystic fibrosis, bronchiectasis, amyloidosis (approved-indication text for the Philippines registration is empty, so the knowledge-graph indications are used) |
| Predicted New Indication | Thrombotic disease |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 (see note below) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold (research question) |

*Evidence level note:* The data compiled for this report grades the lead prediction as L1, but only one Phase 3 trial (NCT03252925) is completed and its results are not available. Under the stated rule (≥2 completed Phase 3 RCTs for L1), L2 is the more defensible grade. NCT03252925 is also not clearly randomized, and the other Phase 2/3 trial (NCT07279610) is single-arm and still ongoing.

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data for acetylcysteine is not available in the compiled data. Based on the supporting literature, NAC is a thiol that can reduce disulfide bonds in ultra-large von Willebrand factor (VWF) multimers. This may lower VWF-platelet binding and microthrombus formation, the central problem in thrombotic thrombocytopenic purpura (TTP) and related thrombotic microangiopathies.

NAC is also an antioxidant that can raise glutathione. This may reduce endothelial oxidative injury and a prothrombotic state, which is also the rationale in the renal-insufficiency trial. Its original uses (mucus thinning, antioxidant detoxification) are different from thrombosis, so the link rests on this thiol and antioxidant chemistry rather than on similarity of the diseases.

Preclinical mouse and baboon TTP models support the mechanism (PMID 28011677). Two 2026 systematic reviews on NAC in TTP have also appeared, though their conclusions were not available in the data.

Other predicted indications were also reviewed. **Dry eye syndrome** has stronger completed-trial support (see the closing section). Most remaining predictions (closed-angle glaucoma, nasal cavity disease, pharyngitis, acute laryngopharyngitis, tracheal disease, transient ischemic attack, laryngotracheitis, angle-closure glaucoma) have little or no clinical evidence and are rated Hold.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | Completed | 170 | NAC in transplant-associated thrombotic microangiopathy (TA-TMA); safety and efficacy study, results not provided |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | Active, not recruiting | 44 | Single-arm multicenter trial of NAC for TA-TMA; no results yet |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | Completed | 40 | Randomized, double-blind, placebo-controlled cross-over trial (RENACTIF) of NAC on the thrombotic phenotype in renal insufficiency |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Early Phase 1 | Completed | 3 | Pilot of IV NAC with plasma exchange in suspected TTP; too small to draw conclusions |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | Unknown | 44 | Dexamethasone plus NAC in newly diagnosed immune thrombocytopenia (indirect relevance) |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Early Phase 1 | Completed | 15 | Atorvastatin plus NAC on platelet count in steroid-resistant or relapsed ITP (indirect) |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | Unknown | 200 | Atorvastatin, NAC and danazol in steroid-resistant or relapsed ITP (indirect) |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41977015](https://pubmed.ncbi.nlm.nih.gov/41977015/) | 2026 | Systematic review | J Clin Med | Systematic review and critical appraisal of NAC therapy in TTP |
| [42338865](https://pubmed.ncbi.nlm.nih.gov/42338865/) | 2026 | Systematic review | Cureus | Systematic review of NAC as adjunctive therapy in TTP |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Cohort study | Ann Hematol | Retrospective study of NAC and in-hospital mortality in acquired TTP; NAC use described as controversial |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Preclinical | Blood | NAC in mouse and baboon TTP models |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Review | Expert Rev Hematol | Repurposed drugs and novel agents in TTP, including NAC |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Review | Blood | Overview of TTP pathophysiology and treatment |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Review | J Clin Med | TTP pathophysiology, diagnosis and management |
| [36410267](https://pubmed.ncbi.nlm.nih.gov/36410267/) | 2022 | Review | J Infect Public Health | NAC in COVID-19, which involves a prothrombotic state |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0003 | Acetylcysteine | Not recorded | Not recorded (status: cancelled) |

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text):** peptic ulcer disease, hypotensive disorder, respiratory failure, asthma, bronchial disease, esophageal varices.
- **Drug Interactions:** 100 interactions were found in total. Among those listed, activated charcoal is Minor and inhaled rapid-acting human insulin is Moderate. The rest (for example mannitol, bupropion, metformin, omeprazole, morphine, prednisone) have no severity rating.

Please refer to the package insert for warnings and label contraindications. The Philippines registration is cancelled and no label text was available.

## Conclusion and Next Steps

**Decision: Hold (research question)**

**Rationale:**
- The prediction score is very high, but the only completed Phase 3 trial has no available results, and the other trials are small, single-arm, ongoing, or indirect (ITP, renal insufficiency). The Philippines registration is cancelled, and no label safety data were available.
- Of the predicted indications, **dry eye syndrome** has stronger supporting evidence. It has a completed Phase 2 trial, two randomized trials of NAC (one in Sjögren's disease dryness, one with chitosan-NAC eye drops), and a rating of "Proceed with Guardrails". It deserves evaluation as a separate candidate, but it would require a topical ophthalmic formulation, and none is registered in the Philippines.

**To proceed, the following is needed:**
- Published results of NCT03252925 and a check of whether it was randomized.
- Results from NCT07279610 and the systematic reviews (PMIDs 41977015, 42338865).
- Detailed mechanism-of-action data from DrugBank.
- Package insert warnings and contraindications (the Philippines registration has been cancelled).
- Dosage-form and route compatibility assessment for the intended indication.
- Safety review of the interaction list, particularly for antithrombotic and antiplatelet co-medication.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

