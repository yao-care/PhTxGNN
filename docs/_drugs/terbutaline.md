---
layout: default
title: Terbutaline
parent: Model Prediction Only (L5)
nav_order: 331
evidence_level: L5
indication_count: 2
last_modified_at: 2026-11-12
monitor_inn: "Terbutaline"
predicted_indications: ["respiratory malformation", "Rienhoff syndrome"]
description: "Terbutaline: predicted new indication Respiratory malformation (evidence level L5). Approved use: Not recorded in the local data"
---

# Terbutaline
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **2** 
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

## Terbutaline: Respiratory malformation
{: .text-alpha }

## One-Sentence Summary

Terbutaline is a beta-2 adrenergic agonist (bronchodilator).
The TxGNN model predicts it may be relevant for **respiratory malformation**, but the supporting evidence is weak: **1 registered clinical trial** (a broad pediatric drug-study platform, not specific to this condition) and **13 publications**, none of which show a treatment benefit for this condition.

<!-- review:begin ph-lic-20261106-terbutaline-1 -->

> **Review correction (2026-11-06)**: Originally stated: "Terbutaline is a beta-2 adrenergic agonist (bronchodilator) that is listed in the Philippines under a single-ingredient registration." Removed: it described the products as single-ingredient or combination products in a way that did not match the PNF data (the Philippine National Formulary as of 2026-11-06). Source: [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/).

<!-- review:end ph-lic-20261106-terbutaline-1 -->

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Respiratory malformation |
| TxGNN Prediction Score | 0.9952 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (PNF entries: 1) – FDA Philippines registration status is not included in this data |
| Number of PNF Entries | 1 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on general pharmacology, terbutaline is a beta-2 agonist, and beta-2 agonism can relax airway smooth muscle and may relieve reversible airflow obstruction or symptoms that accompany structural airway abnormalities.

However, respiratory malformations are structural defects, and bronchodilation does not correct the underlying problem. The publications retrieved are mostly about differential diagnosis (for example, central airway stenosis versus asthma), airway function measurement, or unrelated uses of terbutaline (fetal heart block, autism-related hypotheses, veterinary medicine). None shows a therapeutic benefit of terbutaline for malformation itself. The high TxGNN score most likely reflects closeness to airway-disease concepts in the model's network rather than clinical evidence, so the prediction should be treated as a hypothesis only.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04278404](https://clinicaltrials.gov/study/NCT04278404) | N/A | Recruiting | 5000 | Observational pharmacokinetic and safety study of understudied drugs given to children; not specific to respiratory malformation and provides no efficacy evidence |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [3281307](https://pubmed.ncbi.nlm.nih.gov/3281307/) | 1988 | RCT | Thorax | Subcutaneous adrenaline vs terbutaline in 20 patients with acute severe asthma; not about malformation |
| [1629507](https://pubmed.ncbi.nlm.nih.gov/1629507/) | 1992 | Comparative study (randomized) | J Allergy Clin Immunol | Inhaled budesonide vs terbutaline on airway inflammation in 14 newly diagnosed asthma patients |
| [12061354](https://pubmed.ncbi.nlm.nih.gov/12061354/) | 2002 | Case series | Acta Paediatr | Central airway stenosis in school-aged children, with a focus on distinguishing it from asthma; includes vascular ring anomalies and tracheal stenosis; no terbutaline treatment benefit shown |
| [42303000](https://pubmed.ncbi.nlm.nih.gov/42303000/) | 2026 | Cohort | Respir Med | Long-term treatment of infants with post-infectious bronchiolitis obliterans; evaluates pulmonary function and imaging |
| [19254906](https://pubmed.ncbi.nlm.nih.gov/19254906/) | 2009 | Cohort | Arch Dis Child | Budesonide improved reduced airway conductance in infants with respiratory symptoms |
| [1620986](https://pubmed.ncbi.nlm.nih.gov/1620986/) | 1992 | Observational | Respiration | Inhaled terbutaline reversed abnormal respiratory impedance in chronic bronchitis patients |
| [8327281](https://pubmed.ncbi.nlm.nih.gov/8327281/) | 1993 | Methodological | Pediatr Pulmonol | Flow-volume plot analysis in intubated premature infants before and after terbutaline |
| [11813927](https://pubmed.ncbi.nlm.nih.gov/11813927/) | 2001 | Case series | Cardiol Young | Terbutaline for fetal complete heart block; unrelated to respiratory malformation |
| [19793774](https://pubmed.ncbi.nlm.nih.gov/19793774/) | 2009 | Hypothesis/Review | Toxicol Ind Health | Terbutaline- and mold-associated brain and lung impairments in relation to autism; unrelated |
| [9628312](https://pubmed.ncbi.nlm.nih.gov/9628312/) | 1998 | Case report | Acta Paediatr | Multiple anomalies with hypokalaemic paralysis and partial symptomatic relief with terbutaline; not a respiratory malformation |

## Philippines Market Information

<!-- licenses:begin -->

| PNF entry (active ingredient) | Routes in the PNF |
|------|------|
| Terbutaline (as sulfate) | Oral, Injection, Inhalation, Resp. Soln. |

Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.

<!-- licenses:end -->

## Safety Considerations

- **Conditions listed as contraindications or cautions in the drug-disease relation data:** hypertension and other hypertensive disorders, epilepsy, hyperglycemia, diabetes mellitus and diabetic ketoacidosis, potassium deficiency, hyperthyroidism (including Graves disease and thyrotoxicosis), sudden cardiac arrest, heart conduction disease, myocardial ischemia and coronary artery disease, pulmonary edema, respiratory failure, and placental abruption. These are not taken from label text and should be checked against the package insert.
- **Drug Interactions:** 100 interactions were found in the interaction database. Examples at Moderate level include epinephrine, isometheptene, clarithromycin, famotidine, bisacodyl, and several antidiabetic drugs (acarbose, alogliptin, pioglitazone, canagliflozin, chlorpropamide, albiglutide). Corticosteroids such as hydrocortisone, dexamethasone, budesonide and beclomethasone are Minor.

Please also refer to the package insert for warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The prediction rests on a computational score alone. No trial or publication shows that terbutaline helps respiratory malformation, which is a structural condition that bronchodilation would not be expected to correct.

**To proceed, the following is needed:**
- Studies that directly examine terbutaline in respiratory malformation, or a clear clinical rationale for a symptomatic benefit
- Mechanism of action data
- Package insert warnings and contraindications from the Philippine regulator
- Safety review for cardiovascular, metabolic and potassium-related risks in the target population (including children)

<!-- review:begin log -->

## Review Log

Below is the review log for this page: statements checked against official Philippine National Formulary (PNF) data. Corrections are limited to basic factual statements; model predictions, evidence levels, and conclusions were not rewritten.

| Review date | Item | Action | Source |
|------|------|------|------|
| 2026-11-06 | Removed: "that is listed in the Philippines under a single-ingredient registration" | Corrected | [Philippine National Formulary (DOH)](https://pnf.doh.gov.ph/) |

<!-- review:end log -->

## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

