---
layout: default
title: Streptokinase
parent: Model Prediction Only (L5)
nav_order: 318
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
monitor_inn: "Streptokinase"
predicted_indications: ["Prinzmetal angina", "hemoglobinopathy", "peripheral vascular disease", "peripheral arterial disease", "partial deletion of the short arm of chromosome 16"]
description: "Streptokinase: predicted new indication Prinzmetal angina (evidence level L5). Approved use: Not recorded in the local data"
---

# Streptokinase
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **5** 
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

## Streptokinase: Prinzmetal angina
{: .text-alpha }

## One-Sentence Summary

Streptokinase is a clot-dissolving (thrombolytic) enzyme. The original indication is not recorded in the data compiled for this report, and the single Philippines registration has no indication text.
Myocardial infarction is already an established, guideline-recognised use of streptokinase, so this is not a true repurposing case.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Prinzmetal angina |
| TxGNN Prediction Score | 0.9980 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, streptokinase forms a complex with plasminogen. The complex converts plasminogen to plasmin, which breaks down fibrin in blood clots. In acute myocardial infarction, this can dissolve the clot blocking a coronary artery and restore blood flow.

Myocardial infarction is the classic use of streptokinase. Large trials (such as ISIS-2 and GISSI, described in the literature below) showed a survival benefit. The high model score therefore reflects an existing therapeutic use rather than a new discovery.

Several other predictions follow the same logic but have weaker support:
- **Coronary thrombosis** (L1) overlaps heavily with MI.
- **Peripheral vascular and arterial disease** (L3) rely on local clot lysis, but streptokinase has largely been replaced by other agents.
- **MI subtypes** (septal, posterolateral, posteroinferior) should be assessed under the parent MI indication.
- **Prinzmetal angina, hemoglobinopathy and partial deletion of the short arm of chromosome 16** have no credible mechanistic link and are on hold.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00000507](https://clinicaltrials.gov/study/NCT00000507) | Phase 3 | Completed | Not reported | Intravenous streptokinase in acute MI, to see whether early use limits myocardial damage |
| [NCT00000503](https://clinicaltrials.gov/study/NCT00000503) | Phase 3 | Completed | Not reported | Non-surgical reperfusion (thrombolysis) and its effect on infarct size in acute MI |
| [NCT00627809](https://clinicaltrials.gov/study/NCT00627809) | Phase 4 | Completed | 53 | Low-dose intracoronary streptokinase added to primary PCI in STEMI, assessing infarct size and left ventricular volumes |
| [NCT01305226](https://clinicaltrials.gov/study/NCT01305226) | Phase 3 | Completed | 120 | Recombinant staphylokinase (THR-100) vs streptokinase in acute MI; streptokinase is the comparator |
| [NCT02182011](https://clinicaltrials.gov/study/NCT02182011) | Phase 3 | Completed | 49 | Procoagulant effect of tenecteplase, alteplase and streptokinase in acute MI |
| [NCT03677466](https://clinicaltrials.gov/study/NCT03677466) | N/A | Completed | 60 | Intramyocardial haemorrhage in STEMI with different reperfusion strategies (pharmaco-invasive vs primary PCI) |
| [NCT02893280](https://clinicaltrials.gov/study/NCT02893280) | N/A | Withdrawn | 0 | Sri Lanka acute coronary syndrome audit project; no efficacy data |

Only three of these trials directly test streptokinase in MI, and two of them have no reported enrollment. The remaining trials either use streptokinase as a comparator or address related questions.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [10572811](https://pubmed.ncbi.nlm.nih.gov/10572811/) | 1999 | Meta-analysis | J Accid Emerg Med | Compared outcomes of accelerated alteplase (t-PA) and streptokinase in acute MI |
| [2146913](https://pubmed.ncbi.nlm.nih.gov/2146913/) | 1990 | Meta-analysis | Ann Intern Med | Effect of intravenous streptokinase on early mortality by infarct location (anterior vs inferior) |
| [481511](https://pubmed.ncbi.nlm.nih.gov/481511/) | 1979 | Controlled trial | N Engl J Med | European trial in 315 medium- and high-risk patients; 24-hour streptokinase infusion gave significantly lower six-month mortality than glucose |
| [2191849](https://pubmed.ncbi.nlm.nih.gov/2191849/) | 1990 | Review | Drugs | Major trials (GISSI, ISIS-2, ISAM; over 30,000 patients) show intravenous streptokinase improves survival in acute MI |
| [8130384](https://pubmed.ncbi.nlm.nih.gov/8130384/) | 1994 | Review | Drugs & Aging | Streptokinase confers a survival benefit in older MI patients; ISIS-2 showed a 5-week absolute mortality reduction |
| [3312370](https://pubmed.ncbi.nlm.nih.gov/3312370/) | 1987 | Review | J Am Coll Cardiol | Review of randomised trials of intracoronary and intravenous streptokinase in acute MI |
| [3396164](https://pubmed.ncbi.nlm.nih.gov/3396164/) | 1988 | Trial analysis | Circulation | Western Washington trial: streptokinase gave a higher infarct-artery patency rate (68.5%) than standard therapy |
| [10163575](https://pubmed.ncbi.nlm.nih.gov/10163575/) | 1996 | Economic review | PharmacoEconomics | Streptokinase is as efficacious as alteplase given as a 3-hour infusion, and the less costly option |
| [9339259](https://pubmed.ncbi.nlm.nih.gov/9339259/) | 1997 | Review | Arch Mal Coeur Vaiss | Streptokinase is immunogenic and induces antibodies, which can limit re-administration |
| [10454969](https://pubmed.ncbi.nlm.nih.gov/10454969/) | 1999 | Review | Eur Heart J | Editorial arguing against continued use of streptokinase ("never again") |

The evidence is mostly older reviews and trial reports. There are no recent head-to-head trials against current standard care, such as primary PCI or fibrin-specific agents.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0459 | Streptokinase | Not recorded | Not recorded (registration status: valid) |


---

## Safety Considerations

**Drug Interactions** (100 interactions were identified; the main ones are shown):
- **Major**: apixaban, betrixaban, bivalirudin, abciximab, acalabrutinib, avapritinib, deferasirox, ibritumomab tiuxetan, tositumomab (I-131). Most of these raise bleeding risk.
- **Moderate**: acetylsalicylic acid, ibuprofen, ketorolac, celecoxib, topical diclofenac, aminocaproic acid, omega-3 fatty acids, ginger, fenfluramine, sibutramine.

**Class-level cautions from the literature and prediction notes:**
- Bleeding risk, including intracranial haemorrhage.
- Neutralising anti-streptokinase antibodies after prior exposure or streptococcal infection, which limit re-administration.
- Hypotension and allergic reactions.
- Reports of post-infarction ventricular septal rupture and haemorrhagic infarction in streptokinase-treated patients.

Please refer to the package insert for label warnings and contraindications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
- Streptokinase has a long-established evidence base in acute MI, including large randomised trials and meta-analyses, and the same applies to coronary thrombosis.
- Streptokinase is already a recognised MI treatment, so this is a confirmation of an existing use rather than a new repurposing finding. Fibrin-specific agents and primary PCI are preferred in many settings, and the only Philippines registration is cancelled.

**To proceed, the following is needed:**
- Confirm whether any streptokinase product is currently available or can be registered in the Philippines.
- Obtain the package insert warnings and contraindications.
- Obtain mechanism-of-action data from DrugBank.
- Confirm the original indication from the registration or DrugBank record.
- Compare against current guideline-preferred reperfusion options (primary PCI and fibrin-specific thrombolytics).
- Define a bleeding-risk and antibody/re-exposure screening plan.
- Handle the other predictions as follows:
  - Peripheral vascular and arterial disease: research questions only, to be assessed together.
  - MI subtypes (septal, posterolateral, posteroinferior): evaluate under the parent MI indication.
  - Prinzmetal angina, hemoglobinopathy and chromosome 16 partial deletion: hold, with no support for further work.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

