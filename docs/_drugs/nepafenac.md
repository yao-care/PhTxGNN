---
layout: default
title: Nepafenac
parent: 僅模型預測 (L5)
nav_order: 201
evidence_level: L5
indication_count: 10
---

# Nepafenac
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

# Nepafenac: From Cataract Surgery Inflammation to Broader Eye Disease Treatment

## One-Sentence Summary

Nepafenac is a topical ophthalmic NSAID prodrug used globally for the prevention and treatment of pain and inflammation following cataract surgery.
The TxGNN model predicts it may be effective for the broader category of **Eye Disease** — including diabetic macular edema, posterior segment inflammatory disorders, and related conditions —
with **41 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Post-cataract surgery ocular pain and inflammation (globally approved; no Philippines registration on file) |
| Predicted New Indication | Eye Disease |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L1 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nepafenac is an ophthalmic prodrug that, after topical instillation, penetrates the cornea and is rapidly hydrolyzed by intraocular esterases into its active metabolite **amfenac**. Amfenac is a potent, time-dependent inhibitor of both COX-1 and COX-2 enzymes — reducing intraocular prostaglandin synthesis (particularly PGE2) and thereby suppressing ocular inflammation, preventing cystoid macular edema (CME), and controlling post-surgical pain. A defining pharmacokinetic feature is that nepafenac can penetrate all the way to the posterior segment of the eye (vitreous and retina), as directly confirmed by studies measuring drug and metabolite concentrations in vitreous humor (PMID 26474497; NCT03597867). This makes it unusual among topical NSAIDs.

The same COX/PGE2 inflammatory pathway implicated in post-cataract inflammation also drives a wide range of other ocular conditions: diabetic retinopathy, diabetic macular edema, uveitic macular edema, inflammation after laser procedures (laser peripheral iridotomy, pan-retinal photocoagulation), epiretinal membrane surgery, and vitreoretinal diseases. Clinical evidence already exists for many of these extended uses: NCT01853072 enrolled 881 diabetic cataract patients, NCT00782717 specifically targeted diabetic retinopathy patients, and NCT00801905 studied nepafenac for macular thickening after pan-retinal photocoagulation.

In this case, the TxGNN prediction is less about discovering a truly novel indication and more about formalizing a recognized pharmacological breadth. The mechanistic rationale is well-grounded, posterior segment penetration is pharmacokinetically confirmed, and the clinical trial portfolio already covers multiple sub-categories within the broad "eye disease" label. The model score of 99.85% reflects the strength of the drug–disease network connections across the ophthalmic disease cluster.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01853072](https://clinicaltrials.gov/study/NCT01853072) | Phase 3 | Completed | 881 | Pivotal double-blind, vehicle-controlled RCT in diabetic cataract surgery patients; demonstrated superiority of Nepafenac 0.3% once daily over vehicle for post-surgical clinical outcomes |
| [NCT01109173](https://clinicaltrials.gov/study/NCT01109173) | Phase 3 | Completed | 2120 | Largest Phase 3 study in this indication; evaluated safety and efficacy of Nepafenac 0.3% for prevention and treatment of ocular inflammation and pain after cataract surgery |
| [NCT01872611](https://clinicaltrials.gov/study/NCT01872611) | Phase 3 | Completed | 819 | Confirmatory double-blind, vehicle-controlled RCT in diabetic cataract patients; corroborates NCT01853072 findings with independent cohort |
| [NCT00405730](https://clinicaltrials.gov/study/NCT00405730) | Phase 3 | Completed | 227 | European Phase 3 RCT comparing Nepafenac 0.1% vs Ketorolac 0.5% vs placebo for ocular inflammation/pain after cataract extraction with IOL implantation |
| [NCT03597867](https://clinicaltrials.gov/study/NCT03597867) | Phase 3 | Completed | 104 | Directly measured vitreous NSAID concentrations and PGE2 levels post-topical dosing in vitrectomy patients; confirmed meaningful posterior segment penetration of Nepafenac 0.3% |
| [NCT01395069](https://clinicaltrials.gov/study/NCT01395069) | Phase 4 | Completed | 162 | Three-arm RCT (Nepafenac vs Ketorolac vs placebo) for CME prophylaxis after phacoemulsification; provides head-to-head relative efficacy data |
| [NCT00494494](https://clinicaltrials.gov/study/NCT00494494) | Phase 4 | Completed | 82 | Evaluated Nepafenac 0.1% for prevention of post-operative CME after uncomplicated cataract surgery using OCT quantification |
| [NCT01318499](https://clinicaltrials.gov/study/NCT01318499) | Phase 2 | Completed | 1342 | Dose-ranging study comparing Nepafenac 0.3% vs 0.1% vs vehicle; established pharmacodynamic basis for once-daily 0.3% dosing regimen |
| [NCT02752646](https://clinicaltrials.gov/study/NCT02752646) | N/A | Completed | 200 | Tolerability and toxicity comparison of Nepafenac 0.3% vs Ketorolac 0.5% in cataract surgery patients; large-sample safety characterization with no efficacy endpoint |
| [NCT01847638](https://clinicaltrials.gov/study/NCT01847638) | N/A | Completed | 50 | Head-to-head comparison of Bromfenac 0.07% QD vs Nepafenac 0.3% QD post-cataract; assessed inflammation, visual acuity, and macular thickness outcomes |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39936354](https://pubmed.ncbi.nlm.nih.gov/39936354/) | 2025 | Systematic Review | European Journal of Ophthalmology | Meta-analysis of RCTs: Nepafenac added to steroids significantly reduces foveal thickness and total macular volume, and improves best-corrected visual acuity after cataract surgery |
| [34120417](https://pubmed.ncbi.nlm.nih.gov/34120417/) | 2021 | RCT | Korean Journal of Ophthalmology | Nepafenac 0.1% vs prednisolone 1% for post-operative inflammation in micro-incisional cataract surgery; comparable efficacy, suggesting NSAID monotherapy viability |
| [32672612](https://pubmed.ncbi.nlm.nih.gov/32672612/) | 2020 | RCT | Ophthalmology Glaucoma | Nepafenac 0.1% vs prednisolone acetate 1% for controlling inflammation after laser peripheral iridotomy; non-inferior efficacy with a steroid-sparing advantage |
| [35196591](https://pubmed.ncbi.nlm.nih.gov/35196591/) | 2022 | RCT | Ophthalmology Glaucoma | Nepafenac 0.1% vs bromfenac 0.09% for inflammation after laser peripheral iridotomy; both effective with comparable safety, extends evidence beyond cataract surgery |
| [30284393](https://pubmed.ncbi.nlm.nih.gov/30284393/) | 2018 | RCT | Acta Ophthalmologica | Nepafenac vs preservative-free diclofenac for post-cataract surgery management; compared clinical efficacy and tolerability of two potent topical NSAIDs |
| [26474497](https://pubmed.ncbi.nlm.nih.gov/26474497/) | 2016 | PK Study | Experimental Eye Research | Demonstrated measurable distribution of topical nepafenac and active metabolite amfenac to posterior eye segment; key PK foundation for posterior segment indications |
| [34210237](https://pubmed.ncbi.nlm.nih.gov/34210237/) | 2022 | Review | Clinical & Experimental Optometry | Comprehensive review of nepafenac in cataract surgery: high ocular penetration, CME risk reduction, pain control, favorable safety and tolerability profile |
| [17259381](https://pubmed.ncbi.nlm.nih.gov/17259381/) | 2007 | Preclinical Study | Diabetes | Topical nepafenac inhibits diabetes-induced retinal microvascular disease in animal models; validates the COX pathway's role in early diabetic retinopathy and supports posterior-segment use |
| [29199864](https://pubmed.ncbi.nlm.nih.gov/29199864/) | 2018 | Prospective Study | Current Eye Research | Confirmed intracameral safety of nepafenac and efficacy in inhibiting prostaglandin synthesis during phacoemulsification surgery |
| [16466612](https://pubmed.ncbi.nlm.nih.gov/16466612/) | 2006 | Expert Review | Current Medical Research and Opinion | Expert review of nepafenac's unique posterior segment ocular permeation and early evidence for retinal anti-inflammatory efficacy beyond the anterior segment |

---

## Philippines Market Information

Nepafenac currently has **no registered products** with the Philippine FDA. There are no authorized licenses to list.

> ⚠️ As an unregistered drug, any clinical use in the Philippines would require special authorization — such as a **Compassionate Special Permit (CSP)** issued by the FDA Philippines, or a new full product registration application. The drug is marketed in the United States (NEVANAC® 0.1%, ILEVRO™ 0.3% — Alcon Laboratories) and Europe, which may support a local registration dossier.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Formal safety data (key warnings, contraindications, and drug-drug interactions specific to the Philippines) were not available in this evidence pack. Clinicians should consult the official prescribing information for **NEVANAC® (nepafenac ophthalmic suspension 0.1%)** or **ILEVRO™ (nepafenac ophthalmic suspension 0.3%)** before use. As a class effect of topical ophthalmic NSAIDs, clinicians should be aware of potential risks including corneal adverse events (thinning, melting, perforation) with prolonged use, delayed wound healing, and possible interaction with topical prostaglandin analog glaucoma medications.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
At least four completed Phase 3 RCTs (including pivotal studies with 800–2,100 enrollees) and a 2025 systematic review with meta-analysis provide L1-grade evidence for nepafenac's efficacy in ocular inflammation and macular edema prevention — the core pathophysiological features shared across the predicted "eye disease" category. The mechanistic basis (COX-1/COX-2 inhibition with confirmed posterior segment penetration) is robust and well-characterized. The primary barrier to Philippine use is the absence of local product registration rather than any fundamental evidence gap.

**To proceed, the following is needed:**
- Retrieve and review the complete prescribing information (NEVANAC® / ILEVRO™) to document all warnings, contraindications, precautions, and drug interactions for the safety dossier
- Define the specific target indication within "eye disease" (e.g., post-cataract CME prevention, diabetic macular edema) to focus the Philippine FDA registration strategy
- Initiate a Philippine FDA product registration application, or apply for a Compassionate Special Permit (CSP) for near-term clinical access
- Establish a local pharmacovigilance and adverse event reporting plan aligned with Philippine FDA regulations
- Conduct a health-economic assessment for the primary target Philippine patient population (e.g., diabetic patients undergoing cataract surgery)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

