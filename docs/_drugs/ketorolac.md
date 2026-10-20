---
layout: default
title: Ketorolac
parent: High Evidence (L1-L2)
nav_order: 195
evidence_level: L1
indication_count: 3
last_modified_at: 2026-10-15
description: "Ketorolac: predicted new indication Headache disorder (evidence level L1). Approved use: Atopic, papillary and vernal conjunctivitis"
monitor_inn: "Ketorolac"
predicted_indications: ["headache disorder", "rosacea conjunctivitis", "trigeminal autonomic cephalalgia"]
---

# Ketorolac
{: .fs-9 }

Evidence Level: **L1** | Predicted Indications: **3** 
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

# Ketorolac: From Atopic, Papillary and Vernal Conjunctivitis to Headache Disorder

## One-Sentence Summary

Ketorolac is a non-steroidal anti-inflammatory drug (NSAID). In the knowledge graph its original indications are atopic, papillary and vernal conjunctivitis.
The TxGNN model predicts it may be effective for **headache disorder** (mainly migraine and tension-type headache),
with **16 clinical trials** and **19 publications** currently supporting this direction.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Atopic, papillary and vernal conjunctivitis (from the knowledge graph; no approved indication text is available for the Philippine registration) |
| Predicted New Indication | Headache disorder |
| TxGNN Prediction Score | 99.43% |
| Evidence Level | L1 |
| Philippines Market Status | Cancelled only (no currently valid registration) |
| Number of Registrations | 1 (0 valid, 1 cancelled) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on the known pharmacology of the drug class, ketorolac is a non-selective COX-1/COX-2 inhibitor. By blocking prostaglandin synthesis, it reduces peripheral and central sensitization, neurogenic inflammation and trigeminovascular activation, which drive migraine and tension-type headache pain.

The original ocular indications (atopic, papillary and vernal conjunctivitis) are also prostaglandin-mediated inflammatory conditions. The same anti-inflammatory and analgesic mechanism therefore plausibly extends to headache. Of note, parenteral ketorolac is already used in emergency departments for acute migraine, and several trials and systematic reviews have examined this use.

Two other predictions were also generated but are much weaker. Rosacea conjunctivitis (score 99.40%) has no trials or literature, so it is a computational prediction only (Hold). Trigeminal autonomic cephalalgia (score 99.39%) has only a withdrawn Phase 1 trial with no enrollment and indirect literature (Hold). NSAIDs are generally not established as effective for cluster headache.

## Clinical Trial Evidence

Ten of the 16 registered trials are listed below, with directly relevant ketorolac trials prioritised.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01807234](https://clinicaltrials.gov/study/NCT01807234) | Phase 4 | Completed | 72 | Ketorolac nasal spray vs sumatriptan nasal spray vs placebo for acute migraine |
| [NCT00483717](https://clinicaltrials.gov/study/NCT00483717) | Phase 2 | Completed | 173 | Double-blind, placebo-controlled study of intranasal ketorolac for acute migraine |
| [NCT01011673](https://clinicaltrials.gov/study/NCT01011673) | Phase 4 | Completed | 123 | Metoclopramide/diphenhydramine vs ketorolac alone for tension-type headache |
| [NCT01267864](https://clinicaltrials.gov/study/NCT01267864) | Phase 4 | Completed | 330 | IV valproate vs IV metoclopramide vs IV ketorolac for acute migraine |
| [NCT02358681](https://clinicaltrials.gov/study/NCT02358681) | Phase 3 | Completed | 59 | Intranasal vs intravenous ketorolac for pediatric migraine (non-inferiority) |
| [NCT01596166](https://clinicaltrials.gov/study/NCT01596166) | Phase 4 | Completed | 56 | IV ketorolac plus metoclopramide for pediatric migraine in the emergency department; combination design limits attribution to ketorolac |
| [NCT03221569](https://clinicaltrials.gov/study/NCT03221569) | Phase 4 | Unknown | 60 | Ketamine vs ketorolac for tension-type headache |
| [NCT06083571](https://clinicaltrials.gov/study/NCT06083571) | Phase 2 | Terminated | 41 | Intranasal ketorolac cocktail vs IV ketorolac in pediatric migraine |
| [NCT05641363](https://clinicaltrials.gov/study/NCT05641363) | Phase 3 | Completed | 171 | Three ketorolac doses in children with acute pain (not headache-specific) |
| [NCT06729047](https://clinicaltrials.gov/study/NCT06729047) | Phase 1/2 | Not yet recruiting | 330 | Neostigmine plus atropine vs ketorolac for post-dural puncture headache |

## Literature Evidence

Ten of the 19 publications are listed below, prioritising ketorolac-specific systematic reviews, guidelines and randomized trials.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35138658](https://pubmed.ncbi.nlm.nih.gov/35138658/) | 2022 | Systematic review / meta-analysis | Acad Emerg Med | Evaluates the efficacy of parenteral ketorolac for acute migraine |
| [37849443](https://pubmed.ncbi.nlm.nih.gov/37849443/) | 2024 | Systematic review / meta-analysis | Adv Clin Exp Med | Updated comparison of IV ketorolac vs metoclopramide in adult migraine |
| [23298250](https://pubmed.ncbi.nlm.nih.gov/23298250/) | 2013 | Systematic review | Headache | Reviews RCTs of parenteral ketorolac in acute migraine; notes conflicting evidence |
| [41321235](https://pubmed.ncbi.nlm.nih.gov/41321235/) | 2026 | Guideline | Headache | 2025 American Headache Society update on parenteral drugs for acute migraine in the emergency department |
| [25600718](https://pubmed.ncbi.nlm.nih.gov/25600718/) | 2015 | Guideline / evidence assessment | Headache | American Headache Society assessment of acute migraine pharmacotherapies |
| [24875925](https://pubmed.ncbi.nlm.nih.gov/24875925/) | 2015 | Systematic review / guideline | Cephalalgia | Canadian Headache Society recommendations for migraine pain in emergency settings |
| [24433525](https://pubmed.ncbi.nlm.nih.gov/24433525/) | 2014 | Systematic review | Headache | Parenteral treatment of episodic tension-type headache |
| [35670115](https://pubmed.ncbi.nlm.nih.gov/35670115/) | 2022 | RCT | Headache | IV metoclopramide alone vs with added IV ketorolac in children with migraine in the emergency department |
| [1514724](https://pubmed.ncbi.nlm.nih.gov/1514724/) | 1992 | RCT | Ann Emerg Med | Double-blind trial of IM ketorolac vs meperidine and hydroxyzine for acute migraine |
| [8240554](https://pubmed.ncbi.nlm.nih.gov/8240554/) | 1993 | Observational study | Am J Emerg Med | Patient-rated speed and effectiveness of ketorolac in 23 migraine patients |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0274 | Ketorolac | Not specified | Not specified (registration cancelled) |

## Safety Considerations

- **Disease-related cautions (from the knowledge graph, not label text)**: Ketorolac has contraindication links to the following conditions:
  - Cardiovascular: hypertension, myocardial infarction, stroke, cerebrovascular disorder, heart disease
  - Gastrointestinal: peptic ulcer disease (including active), gastric ulcer, inflammatory bowel disease
  - Other organs: liver disease, gallbladder disease, impaired renal function
  - Bleeding and blood disorders: blood coagulation disease, hemophilia, anemia and hemoglobinopathy
  - Respiratory and metabolic: asthma, diabetes mellitus, diabetic ketoacidosis
  - Other: rheumatoid arthritis, dry eye syndrome
- **Drug Interactions**: 100 interactions were identified. Among those retrieved, the notable one is **acetylsalicylic acid (Major)**. Moderate interactions include corticosteroids (betamethasone, budesonide, dexamethasone, hydrocortisone), sulfonylureas (acetohexamide, chlorpropamide, glimepiride, glipizide, glyburide), exenatide, balsalazide, kanamycin and levofloxacin. Minor interactions include H2 blockers (famotidine, ranitidine, cimetidine) and linaclotide.
- **Lithium**: A case report (PMID 7928331) describes lithium neurotoxicity in a cluster headache patient after ketorolac co-administration. Anticoagulants and other NSAIDs are also of concern.
- **General NSAID risks**: GI bleeding, renal injury, cardiovascular events and platelet inhibition. Parenteral use should be limited to a short course.

Please also refer to the package insert for full warnings and contraindications.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 2 to Phase 4 trials and several systematic reviews and guidelines support ketorolac in acute migraine and tension-type headache. Trials are small, often use combination or comparator designs, and the only registered Philippine license has been cancelled. Safety risks are significant and package insert data are missing.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from DOH-FDA Philippines
- Detailed mechanism of action data (MOA)
- A new or valid Philippine registration, with a defined headache indication, dosage form and route (for example IV/IM or intranasal)
- A short-course dosing limit and screening for the contraindicated conditions and high-risk drug combinations listed above (aspirin, lithium, anticoagulants, other NSAIDs)
- Confirmation of the relative benefit of ketorolac alone, since several trials use combination regimens
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

