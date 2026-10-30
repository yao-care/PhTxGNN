---
layout: default
title: Simvastatin
parent: Model Prediction Only (L5)
nav_order: 312
evidence_level: L5
indication_count: 5
last_modified_at: 2026-10-30
monitor_inn: "Simvastatin"
predicted_indications: ["brain stem infarction", "cholesterol-ester transfer protein deficiency", "HIV infectious disease", "ABri amyloidosis", "neurodevelopmental disorder with ataxic gait, absent speech, and decreased cortical white matter"]
description: "Simvastatin: predicted new indication Brain stem infarction (evidence level L5). Approved use: Not recorded in the local data"
---

# Simvastatin
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

## Simvastatin: Brain stem infarction
{: .text-alpha }

## One-Sentence Summary

Simvastatin is a statin (HMG-CoA reductase inhibitor) originally used for lipid disorders such as hypertriglyceridemia and homozygous familial hypercholesterolemia, and for stroke and atherosclerotic disease.
This prediction is on-label or near on-label, so it is better viewed as confirmation of an existing use than as a true repurposing signal.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not recorded in the local data |
| Predicted New Indication | Brain stem infarction |
| TxGNN Prediction Score | 0.9941 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Detailed mechanism-of-action data is not available in the data compiled for this report. Based on known pharmacology, simvastatin inhibits HMG-CoA reductase, which lowers hepatic cholesterol synthesis and upregulates LDL receptors, increasing LDL-C clearance.

Familial hypercholesterolemia is a genetic condition of high LDL-C, and its mechanism fits this action directly. Efficacy depends on residual LDL receptor function, so response in homozygous disease is limited and add-on therapy is often required.

The other predicted indications (ranks 2–8) are much weaker. Examples are brain stem infarction, CETP deficiency, CYP7A1 deficiency, ABri amyloidosis and a rare neurodevelopmental disorder, all with no supporting trials or with only indirect literature. HIV infection appears only through lipid management and drug-interaction studies, not antiviral benefit. Autosomal dominant hypercholesterolemia is essentially the same entity as familial hypercholesterolemia.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00552097](https://clinicaltrials.gov/study/NCT00552097) | Phase 3 | Completed | 720 | ENHANCE: ezetimibe plus high-dose simvastatin vs simvastatin alone on carotid atherosclerosis in heterozygous FH |
| [NCT00129402](https://clinicaltrials.gov/study/NCT00129402) | Phase 3 | Completed | 248 | Ezetimibe co-administered with simvastatin vs simvastatin alone in adolescents with heterozygous FH |
| [NCT01709500](https://clinicaltrials.gov/study/NCT01709500) | Phase 3 | Completed | 249 | Alirocumab vs placebo in heterozygous FH on lipid-modifying therapy; simvastatin's role is background at most |
| [NCT00654446](https://clinicaltrials.gov/study/NCT00654446) | Phase 3 | Completed | 442 | Renal effects of rosuvastatin vs simvastatin in type IIa/IIb dyslipidaemia, including heterozygous FH |
| [NCT03884452](https://clinicaltrials.gov/study/NCT03884452) | Phase 3 | Completed | 50 | Ezetimibe added to atorvastatin or simvastatin in homozygous FH |
| [NCT03885921](https://clinicaltrials.gov/study/NCT03885921) | Phase 3 | Completed | 44 | 24-month open-label safety extension of ezetimibe added to atorvastatin or simvastatin in homozygous FH |
| [NCT03510884](https://clinicaltrials.gov/study/NCT03510884) | Phase 3 | Completed | 153 | Alirocumab vs placebo in children with heterozygous FH; indirect for simvastatin |
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Open-label alirocumab in children with homozygous FH; simvastatin is background at most |
| [NCT01890967](https://clinicaltrials.gov/study/NCT01890967) | Phase 2 | Completed | 527 | Dose-ranging study of LY3015014 in primary hypercholesterolemia on background statins |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [41824590](https://pubmed.ncbi.nlm.nih.gov/41824590/) | 2026 | Guideline | J Am Coll Cardiol | 2026 ACC/AHA dyslipidemia guideline replacing the 2018 cholesterol guideline |
| [41824552](https://pubmed.ncbi.nlm.nih.gov/41824552/) | 2026 | Guideline | Circulation | Same 2026 dyslipidemia guideline, co-published |
| [18376000](https://pubmed.ncbi.nlm.nih.gov/18376000/) | 2008 | Trial report | N Engl J Med | ENHANCE: simvastatin with or without ezetimibe in familial hypercholesterolemia and its effect on atherosclerosis progression |
| [28685504](https://pubmed.ncbi.nlm.nih.gov/28685504/) | 2017 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Statins for children with familial hypercholesterolemia |
| [31696945](https://pubmed.ncbi.nlm.nih.gov/31696945/) | 2019 | Systematic review (Cochrane) | Cochrane Database Syst Rev | Updated review of statins in children with familial hypercholesterolemia |
| [18940534](https://pubmed.ncbi.nlm.nih.gov/18940534/) | 2008 | Clinical study | J Am Coll Cardiol | Efficacy and safety of ezetimibe plus simvastatin in adolescents with heterozygous FH |
| [12908847](https://pubmed.ncbi.nlm.nih.gov/12908847/) | 2003 | Review | Drug Saf | Benefits and risks of simvastatin in familial hypercholesterolaemia |
| [15794711](https://pubmed.ncbi.nlm.nih.gov/15794711/) | 2005 | Review | Expert Opin Drug Saf | Benefit-risk assessment of simvastatin in familial hypercholesterolaemia |
| [2679083](https://pubmed.ncbi.nlm.nih.gov/2679083/) | 1989 | Clinical study | Am J Med | In FH, simvastatin 20 mg lowered LDL-C by 38% and 40 mg by 42% |
| [11383320](https://pubmed.ncbi.nlm.nih.gov/11383320/) | 2001 | Comparative study | Nutr Metab Cardiovasc Dis | Atorvastatin vs simvastatin in heterozygous FH for LDL-C goal attainment |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0443 | Simvastatin | Not specified | Not specified (status: valid) |

## Safety Considerations

- **Disease-related cautions (from the knowledge graph, not label text)**: Listed contraindication or caution associations include liver disease, pancreatitis, gallbladder disease, myopathy and other muscle diseases, rhabdomyolysis, diabetes mellitus and diabetic ketoacidosis, gout, and thrombocytopenia. Other listed associations include blood coagulation disease, peptic ulcer disease, hypotensive disorder, and several cardiac conditions (acute coronary syndrome, coronary artery disease, myocardial infarction).
- **Drug Interactions**: The interaction query returned 100 entries. Major-level interactions include **amiodarone**, **amlodipine** and **fenofibrate**. Moderate-level examples include nifedipine, omeprazole, paclitaxel, zidovudine, aprepitant and ethanol.
- **HIV-related interaction risk**: Simvastatin is a CYP3A4 substrate. Boosted protease inhibitors and cobicistat raise its exposure markedly, and a case report describes myopathy with Genvoya. Rhabdomyolysis has also been reported in an HIV-infected patient.

Please refer to the package insert for label warnings and contraindications, which are not available in the data compiled for this report.

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 trials, including ENHANCE and the adolescent ezetimibe-simvastatin trial, directly evaluate simvastatin in familial hypercholesterolemia, and Cochrane reviews and guidelines support statin use. The indication is essentially on-label. The only Philippine registration is cancelled, and the label safety data is missing. Ranks 2, 3, 5, 7 and 8 have no supporting evidence (Hold), and HIV is a research question limited by interaction risk.

**To proceed, the following is needed:**
- Obtain the package insert from DOH-FDA Philippines to complete warnings and contraindications (a blocking gap for safety screening)
- Obtain detailed mechanism-of-action data from DrugBank
- Confirm the regulatory pathway, since the sole Philippine registration is cancelled, including product, dosage form and approved indication
- Define a monitoring plan for myopathy/rhabdomyolysis and liver function, and an interaction management plan for CYP3A4 inhibitors, amiodarone, amlodipine, fenofibrate and HIV regimens
- Note that the ENHANCE trial found no added atherosclerosis benefit from ezetimibe over simvastatin alone, a point to weigh in regimen choice
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

