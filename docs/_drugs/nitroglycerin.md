---
layout: default
title: Nitroglycerin
parent: 僅模型預測 (L5)
nav_order: 252
evidence_level: L5
indication_count: 5
---

# Nitroglycerin
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

# Nitroglycerin: From Angina Pectoris to Pulmonary Hypertension

## One-Sentence Summary

Nitroglycerin is a classic organic nitrate vasodilator long established for the treatment of angina pectoris and acute myocardial ischemia. The TxGNN model predicts it may be effective for **Pulmonary Hypertension**, with **multiple completed clinical trials** and **20 publications** currently supporting this direction, including a 2025 RCT in neonates and a dedicated vasoreactivity trial in PAH patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Angina pectoris / acute coronary ischemia (universally established; no Philippines FDA registration on file) |
| Predicted New Indication | Pulmonary Hypertension |
| TxGNN Prediction Score | 99.61% |
| Evidence Level | L2 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Nitroglycerin (NTG) is an organic nitrate that serves as a prodrug for nitric oxide (NO). Upon cellular uptake, it is bioactivated — primarily via mitochondrial aldehyde dehydrogenase (ALDH2) — to release NO, which activates soluble guanylate cyclase (sGC), elevates cyclic GMP (cGMP), and drives relaxation of vascular smooth muscle. This well-characterized cascade (NTG → NO → sGC → cGMP↑ → smooth muscle relaxation → vasodilation) is the same mechanism underpinning its established use in coronary artery spasm. The pulmonary vasculature shares this smooth muscle biology, making the mechanistic bridge to pulmonary hypertension pharmacologically sound.

In pulmonary arterial hypertension (PAH) and related conditions, pathologically elevated pulmonary vascular resistance (PVR) and excessive pulmonary smooth muscle vasoconstriction are central disease drivers. NTG's NO-donating action directly targets this pathophysiology by dilating pulmonary arterial smooth muscle, reducing PVR and mean pulmonary arterial pressure (mPAP), and thereby unloading the right ventricle. The inhaled or nebulized delivery route is particularly advantageous: it achieves preferential pulmonary vasodilation while limiting systemic hypotension, analogous to the selectivity profile of inhaled nitric oxide — but at far lower cost and complexity.

Clinical relevance has been demonstrated across several settings. A 2025 randomized controlled trial (n = 80) confirmed that nebulized NTG improved pulmonary artery pressure and echocardiographic parameters in neonates with persistent pulmonary hypertension (PPHN). A dedicated trial in PAH patients used nebulized NTG as a vasoreactivity testing agent per the 6th World Symposium on PH hemodynamic criteria. Earlier hemodynamic studies in adults with chronic PH showed NTG reduced PVR by approximately 40% and increased cardiac index by 40%. The evidence is most robust in acute and secondary PH settings (post-surgical, neonatal, COPD-associated), where reversible vasoconstriction is dominant, and more limited for WHO Group 1 idiopathic PAH requiring chronic therapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05741229](https://clinicaltrials.gov/study/NCT05741229) | N/A | Completed | 80 | Evaluated nebulized NTG as adjuvant therapy for persistent pulmonary hypertension of the newborn (PPHN); assessed changes in echocardiographic parameters including pulmonary artery pressure, biventricular function, PDA/PFO shunting, and oxygen saturation index |
| [NCT07214129](https://clinicaltrials.gov/study/NCT07214129) | N/A | Completed | 20 | Assessed safety and efficacy of nebulized NTG as a vasoreactive agent in pre-capillary PAH (mPAP >20 mmHg, PVR ≥3 Wood units) per 6th World Symposium diagnostic criteria |
| [NCT04594629](https://clinicaltrials.gov/study/NCT04594629) | Phase 1 | Unknown | 120 | Head-to-head RCT comparing nebulized NTG (2.5–5 mcg/kg/min) versus nebulized epoprostenol (PGI2) for perioperative pulmonary hypertension management in elective valve replacement surgery |
| [NCT03259165](https://clinicaltrials.gov/study/NCT03259165) | Phase 2 | Terminated | 52 | N-FURIOUS trial: compared NTG versus furosemide guided by lung ultrasound for acute heart failure presenting with pulmonary congestion in the ED; provides NTG data in acute pulmonary vascular congestion |
| [NCT06107465](https://clinicaltrials.gov/study/NCT06107465) | Phase 2/3 | Unknown | 60 | Compared high-dose NTG (>100 mcg/min) versus low-dose NTG (<100 mcg/min) in sympathetic crashing acute pulmonary edema (SCAPE); primary endpoints: time to BP resolution, hypoxia correction, and need for mechanical ventilation |
| [NCT00449059](https://clinicaltrials.gov/study/NCT00449059) | Phase 4 | Completed | 20 | Evaluated acute hemodynamic effects of NTG infusion in heart-transplanted patients with cyclosporine-induced hypertension; provides post-transplant PH-adjacent data |
| [NCT01120964](https://clinicaltrials.gov/study/NCT01120964) | Phase 1/2 | Completed | 22 | Randomized double-blind PK/safety trial of IV L-citrulline (a direct NO precursor sharing the same sGC/cGMP pathway) versus placebo in children undergoing cardiopulmonary bypass; supports the NO-pathway mechanism for pediatric PH prevention |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|---------|
| [40888971](https://pubmed.ncbi.nlm.nih.gov/40888971/) | 2025 | RCT | European Journal of Pediatrics | Randomized controlled trial (n = 80) of nebulized NTG in full-term neonates with PPHN; demonstrated significant reduction in pulmonary artery pressure and improvement in echocardiographic and oxygenation parameters |
| [29880427](https://pubmed.ncbi.nlm.nih.gov/29880427/) | 2018 | Comparative RCT | Journal of Cardiothoracic and Vascular Anesthesia | Directly compared dobutamine + NTG versus milrinone in young patients with severe PH undergoing mitral valve replacement; found comparable pulmonary vasodilatory efficacy between the NTG combination and milrinone |
| [39549131](https://pubmed.ncbi.nlm.nih.gov/39549131/) | 2024 | Network Meta-Analysis | Clinical Drug Investigation | NMA of vasodilator therapies for perioperative PH in mitral valve replacement surgery; synthesizes comparative evidence positioning NTG within the pharmacological landscape |
| [34082850](https://pubmed.ncbi.nlm.nih.gov/34082850/) | 2021 | Clinical Study | Cardiology in the Young | Review of inhaled NTG data for acute PAH in children with congenital heart disease; identifies NTG inhalation as a feasible alternative to inhaled nitric oxide in resource-limited settings |
| [16707530](https://pubmed.ncbi.nlm.nih.gov/16707530/) | 2006 | Clinical Study | British Journal of Anaesthesia | Investigated acute effects of inhaled NTG on pulmonary and systemic hemodynamics in children with PAH and congenital heart disease; demonstrated selective pulmonary vasodilation with acceptable systemic effects |
| [6407380](https://pubmed.ncbi.nlm.nih.gov/6407380/) | 1983 | Hemodynamic Study | Annals of Internal Medicine | Foundational human study: NTG administered to 9 patients with chronic PH; cardiac index +40%, stroke volume +40%, PVR −40%, mean PAP decreased; established the core hemodynamic evidence |
| [6423015](https://pubmed.ncbi.nlm.nih.gov/6423015/) | 1984 | Clinical Trial | Bulletin Européen de Physiopathologie Respiratoire | Compared sublingual NTG (1 mg) vs. isosorbide dinitrate in 27 COPD patients with PH during right heart catheterization; only NTG (not ISDN) achieved significant reduction in pulmonary vascular resistance |
| [31425404](https://pubmed.ncbi.nlm.nih.gov/31425404/) | 2020 | Experimental Study | Shock | Compared IV NTG versus novel organic mononitrites for pulmonary vasodilation in a porcine acute PH model; confirmed NTG's efficacy and quantified tolerance development as a long-term limitation |
| [29096811](https://pubmed.ncbi.nlm.nih.gov/29096811/) | 2017 | Review | Journal of the American College of Cardiology | Comprehensive review of NTG and nitrogen oxides in cardiovascular therapeutics; covers NO-mediated vasodilation of capacitance and conductance vessels, including the pulmonary circuit |
| [14508317](https://pubmed.ncbi.nlm.nih.gov/14508317/) | 2003 | Clinical Study | Anesthesiology | Investigated postoperative hemodynamic effects of NTG inhalation in patients with PH undergoing mitral valve replacement; demonstrated improvement in pulmonary hemodynamics in a surgical PH population |

---

## Philippines Market Information

Nitroglycerin currently has **no approved marketing authorizations** with the Philippine FDA. The drug is not commercially available through registered channels in the Philippines. Any clinical use would require regulatory filing, special access, or compassionate use authorization.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** ALDH2 polymorphism (common in East and Southeast Asian populations) is known to reduce NTG bioactivation and attenuate its vasodilatory response. A 2019 pharmacokinetic study in infants with CHD-associated PAH (PMID [31250045](https://pubmed.ncbi.nlm.nih.gov/31250045/)) confirmed this gene–drug interaction. Pharmacogenomic screening should be considered before clinical deployment in Filipino patients.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed RCT (n = 80, 2025) demonstrating efficacy in neonatal PPHN, a dedicated PAH vasoreactivity trial, multiple hemodynamic studies, and a network meta-analysis collectively provide Phase 2-level evidence supporting nebulized NTG as a pulmonary vasodilator. The NO/cGMP mechanism is directly applicable to PH pathophysiology, and inhaled/nebulized delivery addresses the key limitation of systemic hypotension.

**To proceed, the following is needed:**

- **Regulatory pathway**: NTG is unregistered in the Philippines; a regulatory filing or compassionate use/expanded access pathway must be established before clinical deployment
- **Safety dossier**: Obtain full package insert data (key warnings, contraindications, drug interactions) from Philippine FDA or international reference authorities (FDA US, EMA) to complete the safety evaluation blocked by current data gaps
- **MOA documentation**: Formal DrugBank MOA entry retrieval to support mechanistic sections of regulatory submissions
- **Nitrate tolerance protocol**: Long-term use is limited by tolerance development (ALDH2 enzyme downregulation); clinical protocol should specify nitrate-free intervals, dose escalation strategy, or rotation with alternative NO donors
- **ALDH2 pharmacogenomics plan**: Given the documented impact of ALDH2 polymorphism on NTG response in Asian populations, a genotyping or dose-adjustment strategy should be defined for the Filipino patient population
- **Route-of-administration specification**: Clarify target delivery route (nebulized vs. intravenous vs. sublingual) for the specific indication and patient population (neonatal PPHN vs. adult PAH vs. perioperative PH)
- **Bridging study design**: Given that most high-quality evidence is in neonatal PPHN and perioperative settings, a bridging protocol is needed to confirm efficacy and safety in adult idiopathic or WHO Group 1 PAH if that is the intended indication
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

