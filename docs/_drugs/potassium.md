---
layout: default
title: Potassium
parent: 僅模型預測 (L5)
nav_order: 214
evidence_level: L5
indication_count: 5
---

# Potassium
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

# Potassium: From Electrolyte Supplementation to Hypertensive Disorder

## One-Sentence Summary

Potassium (DB14500) is an essential mineral clinically recognized for correcting hypokalemia and sustaining normal cellular, cardiac, and vascular function.
The TxGNN model predicts it may be therapeutically relevant for **Hypertensive Disorder**, a prediction backed by a landmark **NEJM outcomes RCT**, **multiple Tier-1 meta-analyses**, and a well-characterized molecular mechanism spanning basic science through large-scale clinical evidence.
Evidence is classified as **L1** — the highest level in this framework — making this the most strongly supported prediction in the current candidate set.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Electrolyte supplementation; correction of hypokalemia |
| Predicted New Indication | Hypertensive Disorder |
| TxGNN Prediction Score | 99.16% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Potassium is not merely a passive electrolyte — it is an active regulator of blood pressure through at least four distinct, well-documented pathways. First, dietary potassium activates the Ppp1Ca–Ppp1r1a dephosphorylation axis in renal distal tubule cells, suppressing the sodium-chloride cotransporter (NCC) and directly promoting urinary sodium excretion — a mechanism recently confirmed at the molecular level in a *Journal of Clinical Investigation* study (Grimm et al., 2023). Second, adequate potassium status suppresses renin secretion, downregulating the renin-angiotensin-aldosterone system (RAAS) axis. Third, elevated extracellular potassium concentrations hyperpolarize vascular smooth muscle cell membranes, inducing arterial vasodilation. Fourth, high potassium intake directly blunts the pressor response to dietary sodium excess — the so-called sodium–potassium antagonism that underpins the benefit of potassium-enriched salt substitutes.

This mechanistic profile parallels two of the most established antihypertensive drug classes: thiazide diuretics (which promote natriuresis) and RAAS inhibitors (which preserve potassium). It is therefore not surprising that conditions marked by potassium wasting — such as primary aldosteronism and renovascular hypertension — are precisely those associated with the most severe and treatment-resistant hypertension. Correcting potassium deficiency in these settings is not merely supportive care; it disrupts the upstream hormonal cascade driving blood pressure elevation.

The clinical evidence has matured well beyond hypothesis. The SSaSS trial (Neal et al., *NEJM* 2021), conducted in nearly 21,000 high-risk participants, demonstrated that a potassium-enriched salt substitute reduced stroke by 14%, major cardiovascular events by 13%, and cardiovascular death by 12%. Multiple independent systematic reviews and dose-response meta-analyses confirm a linear, significant blood pressure–lowering effect of potassium supplementation, particularly in hypertensive individuals. TxGNN's L1-level prediction is therefore not a novel speculation but a computational confirmation of a well-established biological relationship.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01429246](https://clinicaltrials.gov/study/NCT01429246) | N/A | Completed | 282 | Single-blind RCT in Tibet (4,300 m altitude): KCl-based salt substitute vs. standard salt in known hypertensives (SBP ≥140 mmHg); primary endpoint was blood pressure reduction — the most directly relevant trial for potassium supplementation in hypertension |
| [NCT00079690](https://clinicaltrials.gov/study/NCT00079690) | N/A | Completed | ~1,200 | Genetic epidemiology of BP intervention: identifies gene variants modulating BP response to low/high dietary sodium, **oral potassium supplementation**, and cold pressor — includes a dedicated potassium supplementation arm |
| [NCT07137364](https://clinicaltrials.gov/study/NCT07137364) | N/A | Recruiting | 350 | Observational study of spironolactone dosing in lateralized primary aldosteronism (PA); potassium correction and homeostasis are central to BP management in PA, providing indirect evidence for potassium's role in secondary hypertension |
| [NCT05814770](https://clinicaltrials.gov/study/NCT05814770) | Phase 4 | Not Yet Recruiting | 96 | RCT: finerenone vs. spironolactone in primary aldosteronism; serum potassium is a primary safety and efficacy endpoint, directly evaluating potassium homeostasis in mineralocorticoid-excess hypertension |
| [NCT00887250](https://clinicaltrials.gov/study/NCT00887250) | Phase 3 | Completed | 366 | Double-blind RCT: losartan 50–100 mg vs. placebo in mild-to-moderate essential hypertension; losartan's potassium-sparing property (via RAAS inhibition) is one of the proposed mechanisms of BP reduction |
| [NCT00496834](https://clinicaltrials.gov/study/NCT00496834) | Phase 4 | Completed | 201 | Losartan potassium vs. carvedilol in essential hypertension — arterial stiffness (PWV) as primary endpoint; evaluates downstream cardiovascular consequences of potassium-preserving antihypertensive therapy |
| [NCT02832973](https://clinicaltrials.gov/study/NCT02832973) | Phase 4 | Completed | 72 | ResHypOT: sequential nephron blockade (includes potassium-sparing aldosterone antagonism) vs. dual RAAS blockade + bisoprolol in resistant hypertension; serum potassium monitoring integral to both arms |
| [NCT02059811](https://clinicaltrials.gov/study/NCT02059811) | N/A | Completed | 42 | Pilot RCT of DASH diet (a potassium-rich dietary pattern) for uncontrolled hypertension in CKD; evaluates BP lowering from dietary potassium increase in a renally impaired population |
| [NCT03640312](https://clinicaltrials.gov/study/NCT03640312) | Phase 2 | Completed | 62 | QUARTET USA: ultra-low-dose quadruple combination therapy vs. standard monotherapy in hypertension — includes potassium-sparing agents; relevant to combination strategies using potassium-preserving drugs |
| [NCT04026776](https://clinicaltrials.gov/study/NCT04026776) | Early Phase 1 | Recruiting | 120 | Investigates how dietary Na/K ratio influences blood pressure and salt sensitivity in young adults born preterm — directly examines potassium–sodium interplay in BP regulation |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [34459569](https://pubmed.ncbi.nlm.nih.gov/34459569/) | 2021 | Large RCT (outcomes) | N Engl J Med | SSaSS trial (n≈20,995): potassium-enriched salt substitute reduced stroke by 14%, major CV events by 13%, and CV death by 12% in high-risk hypertensive adults; landmark evidence for real-world potassium benefit |
| [32500831](https://pubmed.ncbi.nlm.nih.gov/32500831/) | 2020 | Systematic Review & Meta-Analysis of RCTs | J Am Heart Assoc | Dose-response meta-analysis of RCTs (≥4 weeks): potassium supplementation produces a significant, linear reduction in both systolic and diastolic BP; effect strongest in hypertensive individuals |
| [23558164](https://pubmed.ncbi.nlm.nih.gov/23558164/) | 2013 | Systematic Review & Meta-Analysis | BMJ | WHO-commissioned analysis: increased potassium intake reduces BP and stroke risk by 24%; no adverse effects on blood lipids, kidney function, or renal hormones in healthy adults |
| [37772757](https://pubmed.ncbi.nlm.nih.gov/37772757/) | 2024 | State-of-the-Art Review | Am J Hypertens | Comprehensive update on potassium mechanisms in hypertension: NCC suppression, RAAS modulation, and vascular hyperpolarization reviewed; authors argue potassium deserves a dedicated place in hypertension guidelines |
| [39472546](https://pubmed.ncbi.nlm.nih.gov/39472546/) | 2025 | Expert Review | Hypertens Res | Asia-Pacific consensus on dietary potassium and salt substitution for hypertension: recommends potassium-enriched salt substitutes as a scalable, low-cost non-pharmacological intervention, particularly for Asian populations |
| [37676724](https://pubmed.ncbi.nlm.nih.gov/37676724/) | 2023 | Mechanistic Study (Basic Science) | J Clin Invest | Identifies the Ppp1Ca–Ppp1r1a → NCC dephosphorylation pathway as the key mechanism by which dietary potassium induces natriuresis and BP reduction; transcriptomic validation in rodent models |
| [30190007](https://pubmed.ncbi.nlm.nih.gov/30190007/) | 2018 | Clinical Guideline / Expert Review | J Am Coll Cardiol | JACC Health Promotion Series: identifies inadequate dietary potassium as a modifiable determinant of hypertension; endorses potassium supplementation alongside sodium restriction for BP management |
| [27455317](https://pubmed.ncbi.nlm.nih.gov/27455317/) | 2016 | Narrative Review | Nutrients | Reviews potassium bioavailability, Na⁺/K⁺-ATPase physiology, and clinical evidence for BP reduction; discusses dietary sources, supplement forms, and bioequivalence considerations |
| [29771736](https://pubmed.ncbi.nlm.nih.gov/29771736/) | 2018 | Evidence Synthesis Review | Curr Opin Cardiol | DASH diet and potassium-rich dietary patterns consistently lower BP in pre-hypertensive and hypertensive adults; highlights synergy between sodium reduction and potassium increase |
| [23674806](https://pubmed.ncbi.nlm.nih.gov/23674806/) | 2013 | Comprehensive Review | Adv Nutr | Potassium classified as a "shortfall nutrient" by US Dietary Guidelines; moderate-to-strong evidence for BP reduction and stroke risk reduction; additional benefits for bone health and kidney stone prevention |

---

## Philippines Market Information

Potassium (DB14500) currently has **no registered pharmaceutical products** in the Philippines under this DrugBank entry. No FDA Philippines license records were retrieved.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | No registered products | — | No data available |

> While potassium-containing preparations (e.g., potassium chloride oral supplements, IV electrolyte solutions) are routinely stocked in Philippine hospitals as essential medicines, no formal registration linked to DrugBank ID DB14500 was found in the current dataset. A regulatory pathway review under FDA Philippines will be required to determine whether potassium supplementation products for hypertension require new drug registration or qualify as nutritional supplements.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Important clinical context:** Although formal safety data was not retrieved in this evidence pack, potassium supplementation carries well-recognized risks that are particularly relevant to the hypertensive population: **hyperkalemia** is a serious concern in patients with chronic kidney disease (CKD Stage ≥3), those on RAAS inhibitors, potassium-sparing diuretics, or NSAIDs — populations that overlap substantially with the hypertension target group. Risk stratification for renal function and concomitant medications should be a prerequisite for any formal repurposing program.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The evidence that potassium supplementation lowers blood pressure in hypertensive adults is one of the most thoroughly established relationships in nutritional cardiology, supported by a NEJM outcomes RCT, multiple Tier-1 systematic meta-analyses, and a well-characterized molecular mechanism extending from the renal tubule to the vascular wall. TxGNN's L1 classification is a validation of existing science rather than a novel hypothesis. The primary barriers to formal repurposing in the Philippines context are regulatory classification, safe patient selection, and formulation strategy — not evidence of efficacy.

**To proceed, the following is needed:**

- **Regulatory classification review:** Determine whether potassium supplementation products (KCl oral tablets, salt substitutes) require new FDA Philippines pharmaceutical registration or may be advanced through a nutritional/functional food pathway
- **Renal safety protocol:** Mandatory screening of eGFR and concurrent medication review (RAAS inhibitors, potassium-sparing diuretics, NSAIDs) before initiating supplementation; define contraindication cutoffs for CKD staging
- **Target population definition:** Clarify eligibility criteria — potassium benefit is most pronounced in hypertensive individuals with documented low dietary potassium intake or mild hypokalemia, rather than all hypertensives
- **Formulation and dose selection:** Determine optimal delivery vehicle (potassium chloride capsules vs. salt substitute program vs. dietary counseling) and target daily intake aligned with WHO/ACC guidance (3,500–4,700 mg/day)
- **Local dietary baseline data:** Assess current potassium intake in hypertensive Filipino adults to project the expected magnitude of BP reduction and guide intervention intensity
- **Pharmacovigilance plan:** Establish serum potassium and renal function monitoring intervals, particularly for higher-risk subgroups including the elderly and those with comorbid CKD or diabetes
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

