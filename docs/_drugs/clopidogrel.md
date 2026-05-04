---
layout: default
title: Clopidogrel
parent: 僅模型預測 (L5)
nav_order: 81
evidence_level: L5
indication_count: 8
---

# Clopidogrel
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Clopidogrel: From Cardiovascular Prevention to Migraine with Brainstem Aura

## One-Sentence Summary

Clopidogrel is a well-established thienopyridine antiplatelet agent used to prevent atherothrombotic events including acute coronary syndrome, ischemic stroke, and peripheral arterial disease. The TxGNN model ranks **Migraine with Brainstem Aura** as its top new indication (score 99.44%), with the closely related **Migraine Disorder** ranked second (99.44%), supported collectively by **8 clinical trials** and **20 publications** — including two completed RCTs from the landmark CANOA trial series (JAMA 2015; JAMA Cardiology 2021). The mechanistic case is reinforced by a dual pathway: PFO-mediated microthrombus-triggered cortical spreading depression, and direct P2Y12 receptor blockade on brainstem microglial cells.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Atherothrombotic event prevention (ACS, ischemic stroke, peripheral arterial disease) |
| Predicted New Indication | Migraine with Brainstem Aura |
| TxGNN Prediction Score | 99.44% |
| Evidence Level | L3 (migraine with brainstem aura) / L2 (migraine disorder) |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Research Question |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank was not available for this analysis. Based on established pharmacology, clopidogrel is a thienopyridine that irreversibly and selectively blocks the P2Y12 ADP receptor on platelet surfaces, inhibiting ADP-mediated platelet activation and aggregation. This mechanism underlies all of its approved cardiovascular indications. The P2Y12 receptor is the precise pharmacological target that bridges cardiovascular use to migraine biology.

The mechanistic case for migraine — particularly migraine with *brainstem* aura — runs through two convergent pathways. The primary pathway is vascular-thromboembolic: patent foramen ovale (PFO) and atrial septal defects (ASD) create right-to-left cardiac shunts that allow microthrombi to bypass pulmonary filtration and enter the systemic circulation. These microemboli are hypothesized to trigger cortical spreading depression (CSD), the electrophysiological substrate of migraine aura. In migraine with brainstem aura specifically, dorsal brainstem structures (cerebellum, basilar territory) are the primary aura generators, making microembolic vascular triggers particularly mechanistically relevant. By reducing platelet aggregation, clopidogrel theoretically decreases this microthrombus burden and the frequency of brainstem CSD events.

A second, direct neuroinflammatory mechanism has emerged from preclinical research: P2Y12 receptors are expressed on microglial cells within the trigeminal nucleus caudalis — the brainstem structure that is the central relay for migraine pain processing. ADP-mediated P2Y12 activation in these microglia triggers the RhoA/ROCK inflammatory pathway, amplifying central sensitization and migraine signaling (PMID 31722730). This effect has been confirmed in a nitroglycerin-induced animal migraine model (PMID 34363208). Clopidogrel's P2Y12 blockade may therefore act directly on brainstem pain circuits, independent of peripheral antiplatelet activity — a dual mechanism that uniquely supports this TxGNN prediction.

---

## Clinical Trial Evidence

> **Note:** No clinical trials have been specifically registered for *migraine with brainstem aura* as a distinct diagnostic category (TxGNN Rank #1). The trials below — identified for the closely related *migraine disorder* (TxGNN Rank #2) — constitute the primary clinical evidence base, as migraine with brainstem aura was historically enrolled within broader "migraine with aura" populations in these trials.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00799045](https://clinicaltrials.gov/study/NCT00799045) | Phase 4 | Completed | 220 | **CANOA trial**: Clopidogrel + aspirin vs. aspirin alone after transcatheter ASD closure; primary endpoint is prevention of new-onset migraine — the most directly relevant completed RCT for this repurposing hypothesis |
| [NCT04946734](https://clinicaltrials.gov/study/NCT04946734) | Phase 3 | Active, Not Recruiting | 440 | **SPRING trial**: Multicenter RCT comparing PFO closure vs. drug therapy (antiplatelet regimens included) for migraine relief; positive results would upgrade evidence to L1 |
| [NCT05546320](https://clinicaltrials.gov/study/NCT05546320) | Phase 4 | Unknown | 1,000 | **COMPETE trial**: Large three-arm comparison of anticoagulation vs. antiplatelet (clopidogrel-inclusive) vs. standard migraine preventive therapy in PFO-associated migraine; study design published (PMID 38109984) |
| [NCT02938182](https://clinicaltrials.gov/study/NCT02938182) | Phase 4 | Unknown | 50 | Prospective trial directly evaluating clopidogrel prophylaxis for migraineurs with confirmed right-to-left shunt; tests this repurposing hypothesis directly |
| [NCT00562289](https://clinicaltrials.gov/study/NCT00562289) | Phase 3 | Completed | 664 | PFO closure vs. anticoagulants vs. antiplatelet therapy for stroke recurrence prevention; migraine included as secondary endpoint — large dataset with extractable clopidogrel migraine data |
| [NCT02777359](https://clinicaltrials.gov/study/NCT02777359) | Phase 2 | Unknown | 100 | PFO closure RCT for migraine with aura; clopidogrel is standard post-procedure antiplatelet — supports PFO-migraine mechanistic context |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [26551304](https://pubmed.ncbi.nlm.nih.gov/26551304/) | 2015 | RCT | *JAMA* | **CANOA main results**: Clopidogrel + aspirin significantly reduced incidence of new-onset migraine attacks following transcatheter ASD closure vs. aspirin monotherapy |
| [32965476](https://pubmed.ncbi.nlm.nih.gov/32965476/) | 2021 | RCT | *JAMA Cardiology* | **CANOA 1-year follow-up**: Lower migraine incidence sustained during clopidogrel treatment; partial rebound observed after clopidogrel cessation at 3 months, suggesting drug-dependent effect |
| [39989443](https://pubmed.ncbi.nlm.nih.gov/39989443/) | 2025 | Systematic Review | *Headache* | Comprehensive systematic review of antithrombotic agents — including clopidogrel — as migraine preventive medication; most current synthesis of the field |
| [40144614](https://pubmed.ncbi.nlm.nih.gov/40144614/) | 2025 | Systematic Review | *Indian J Thorac Cardiovasc Surg* | Systematic review of new-onset headache/migraine after transcatheter ASD closure and its management, including antiplatelet strategies |
| [24836213](https://pubmed.ncbi.nlm.nih.gov/24836213/) | 2014 | Pilot RCT | *Cephalalgia* | First pilot randomised controlled trial of clopidogrel as standalone migraine prophylaxis; established proof-of-concept for a dedicated RCT |
| [31722730](https://pubmed.ncbi.nlm.nih.gov/31722730/) | 2019 | Mechanistic Study | *J Neuroinflammation* | P2Y12 receptor on trigeminal nucleus caudalis microglia drives chronic migraine via RhoA/ROCK neuroinflammatory pathway — establishes the brainstem-specific central target |
| [32848048](https://pubmed.ncbi.nlm.nih.gov/32848048/) | 2020 | Cohort | *J Investigative Medicine* | Clopidogrel 75 mg/day added to existing prophylaxis in drug-refractory PFO-associated migraine (56.8% PFO prevalence in cohort); significant reduction in monthly attack frequency |
| [16103551](https://pubmed.ncbi.nlm.nih.gov/16103551/) | 2005 | Prospective Observational | *Heart* | Index observation: clopidogrel reduced migraine with aura after transcatheter PFO/ASD closure — the clinical signal that prompted subsequent RCTs |
| [30478067](https://pubmed.ncbi.nlm.nih.gov/30478067/) | 2018 | Open-label Pilot | *Neurology* | **TRACTOR**: Ticagrelor (P2Y12 inhibitor) for refractory migraine/PFO — confirms P2Y12 inhibitor class effect; prior clinical experience with clopidogrel and prasugrel in PFO-migraine cited |
| [34363208](https://pubmed.ncbi.nlm.nih.gov/34363208/) | 2021 | Animal Study | *Br J Pharmacol* | P2Y12 receptor genetic and pharmacological blockade attenuates nitroglycerin-induced migraine in mice — preclinical mechanistic confirmation at the neuronal level |

---

## Philippines Market Information

Clopidogrel currently has **no registered products** with the Philippine Food and Drug Administration (PFDA). There are no active licenses or marketing authorizations on record in this dataset.

> **Note for Clinical Teams:** Clopidogrel (brand name Plavix® and generics) holds regulatory approval in the United States (FDA), European Union (EMA), Japan (PMDA), Taiwan (TFDA), and most major markets globally. The absence of a Philippine registration entry may reflect a data completeness gap rather than true non-availability. Direct verification against the current PFDA online verification portal is strongly recommended before drawing conclusions about local market access.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Formal safety data extraction from PFDA and DrugBank was not performed for this analysis and is flagged as blocking data gaps (DG001: PFDA package insert warnings/contraindications; DG002: DrugBank MOA and toxicity profile). As a thienopyridine antiplatelet, clopidogrel is known to carry class-specific safety considerations clinically relevant to this repurposing context — including bleeding risk (especially when combined with aspirin), rare thrombotic thrombocytopenic purpura (TTP), and CYP2C19 pharmacogenomic variability that significantly affects active metabolite generation and therefore clinical efficacy. CYP2C19 loss-of-function alleles (\*2, \*3) are substantially more prevalent in Southeast Asian and Filipino populations than in European populations, making genotype-guided dosing particularly important in this context.

---

## Conclusion and Next Steps

**Decision: Research Question (pathway toward Proceed with Guardrails)**

**Rationale:**
Migraine with brainstem aura is a precisely defined ICHD-3 subtype with no dedicated clopidogrel trial to date, warranting a Research Question designation for this specific indication. However, the broader migraine disorder indication (TxGNN Rank #2) achieves L2 evidence and a "Proceed with Guardrails" recommendation, supported by two completed RCTs from the CANOA trial series and a biologically compelling dual P2Y12 mechanism. The two indications share sufficient mechanistic and population overlap that a targeted study in brainstem aura patients with confirmed PFO would efficiently resolve this gap.

**To proceed, the following is needed:**

- Verify current clopidogrel availability and registration status in the Philippines by direct query to the PFDA online drug database
- Obtain and parse the full package insert (SmPC/PIL) for complete warnings, contraindications, and dosage recommendations — this is a **blocking** data gap (DG001) for safety screening entry
- Retrieve the complete DrugBank MOA entry (DB00758) to formally document the mechanism and target profile for regulatory dossier (DG002)
- Await published results from the ongoing **SPRING Phase 3 trial** (NCT04946734, n=440) and **COMPETE trial** (NCT05546320, n=1,000); positive outcomes would upgrade the migraine disorder indication to L1 and materially strengthen the brainstem aura sub-indication
- Design a prospective observational registry specifically targeting patients meeting ICHD-3 criteria for *migraine with brainstem aura* who also have echocardiographically confirmed PFO, to generate a dedicated evidence base for this exact TxGNN-predicted indication
- Conduct a CYP2C19 genotyping feasibility assessment for the target Philippine study population prior to trial design, as high prevalence of CYP2C19 poor metabolizer variants in Southeast Asian populations may require dose adjustment or alternative P2Y12 agent selection
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

