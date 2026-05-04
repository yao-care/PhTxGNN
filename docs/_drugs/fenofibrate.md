---
layout: default
title: Fenofibrate
parent: 僅模型預測 (L5)
nav_order: 137
evidence_level: L5
indication_count: 7
---

# Fenofibrate
{: .fs-9 }

證據等級: **L5** | 預測適應症: **7** 個
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

# Fenofibrate: From Dyslipidemia to Homozygous Familial Hypercholesterolemia

## One-Sentence Summary

Fenofibrate is a peroxisome proliferator-activated receptor alpha (PPARα) agonist belonging to the fibrate class, globally established for the treatment of dyslipidemia and hypertriglyceridemia, though it is not currently registered in the Philippines.
The TxGNN model predicts it may offer adjunctive benefit for **Homozygous Familial Hypercholesterolemia (HoFH)**,
with **1 registered clinical trial** (testing a different agent in the HoFH population) and **11 publications** supporting this research direction — none of which constitute a dedicated Phase 2/3 trial of fenofibrate specifically in HoFH patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Dyslipidemia / Hypertriglyceridemia (globally approved; not registered in Philippines) |
| Predicted New Indication | Homozygous Familial Hypercholesterolemia (HoFH) |
| TxGNN Prediction Score | 99.91% |
| Evidence Level | L3 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in the local regulatory records. Based on published scientific literature, fenofibrate is a PPARα agonist that exerts broad effects on lipid metabolism: it upregulates lipoprotein lipase (LPL) activity to accelerate VLDL and chylomicron clearance, suppresses ApoC-III transcription to reduce hepatic VLDL secretion, induces ApoA-I and ApoA-II expression to raise HDL-C by 10–35%, and shifts the LDL particle distribution toward larger, less atherogenic forms — collectively lowering triglycerides by 20–50% in dyslipidemias.

HoFH is characterised by near-complete loss of LDL receptor function (< 2% residual activity due to homozygous LDLR, ApoB, or PCSK9 mutations), resulting in severely elevated LDL-C from birth and premature atherosclerotic cardiovascular disease. Because fenofibrate's primary LDL-lowering pathway depends on functional LDL receptors, its direct effect on LDL-C in HoFH is expected to be minimal. The prediction is nonetheless mechanistically plausible as an **adjunctive** strategy: fenofibrate can address co-existing hypertriglyceridaemia common in HoFH patients, raise HDL-C to partially compensate for the impaired reverse cholesterol transport pathway, and reduce overall lipid burden alongside first-line agents such as lomitapide, evinacumab, or LDL apheresis.

A 1984 prospective study (PMID 6593751) directly observed fenofibrate in a cohort of type II hyperlipoproteinemia patients that included one HoFH individual, who demonstrated the greatest reduction in total and LDL cholesterol — offering an early, if anecdotal, data point. Furthermore, the pharmacokinetic interaction between fenofibrate and the HoFH-approved agent lomitapide has been formally characterised (PMID 24734312), supporting the feasibility of combination use. The TxGNN model likely captures these mechanistic overlaps within the lipid-disorder knowledge graph; however, the absence of any dedicated HoFH-specific trial for fenofibrate means this remains primarily a research question warranting prospective investigation rather than immediate clinical application.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03510715](https://clinicaltrials.gov/study/NCT03510715) | Phase 3 | Completed | 18 | Evaluated alirocumab (PCSK9 inhibitor, **not fenofibrate**) every 2 weeks in children and adolescents aged 8–17 with HoFH on background treatment; primary endpoint was LDL-C reduction at Week 12. Demonstrates trial feasibility in this ultra-rare orphan population and illustrates the extremely small patient numbers typically available for HoFH studies |

> **Note:** No clinical trials directly testing fenofibrate in HoFH are currently registered on ClinicalTrials.gov. The trial above involves alirocumab and is included solely to characterise the HoFH clinical trial landscape.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [6593751](https://pubmed.ncbi.nlm.nih.gov/6593751/) | 1984 | Prospective Clinical Study | Pharmacological Research Communications | Fenofibrate 300 mg/day for 4–12 months in 22 type II hyperlipoproteinemia patients; total cholesterol fell 22% and LDL-C 24% overall; the single HoFH patient in the cohort showed the greatest reduction, providing the only direct fenofibrate-in-HoFH data point |
| [24734312](https://pubmed.ncbi.nlm.nih.gov/24734312/) | 2014 | PK Interaction Study | Pharmacotherapy | Characterised pharmacokinetic interactions of lomitapide (approved specifically for HoFH) at 10 mg and 60 mg with co-administered fenofibrate; directly relevant for planning combination regimens in HoFH |
| [28437620](https://pubmed.ncbi.nlm.nih.gov/28437620/) | 2017 | Clinical Guideline | Endocrine Practice | AACE/ACE comprehensive dyslipidemia management guidelines; covers fibrate class role in complex dyslipidemias and cardiovascular risk reduction, providing regulatory context for fenofibrate use |
| [37979722](https://pubmed.ncbi.nlm.nih.gov/37979722/) | 2024 | Review | Indian Heart Journal | Comprehensive review of non-statin lipid-lowering drugs; confirms fenofibrate monotherapy is most definitively indicated for fasting TG > 500 mg/dL; positions fenofibrate as adjunct in mixed dyslipidaemia where statin targets cannot be met |
| [24946816](https://pubmed.ncbi.nlm.nih.gov/24946816/) | 2014 | Review | Internal Medicine Journal | Reviews HoFH treatment options including LDL apheresis, lomitapide, and emerging novel therapies; contextualises where adjunctive lipid-modifying agents might fit in the HoFH treatment algorithm |
| [2042836](https://pubmed.ncbi.nlm.nih.gov/2042836/) | 1991 | Review / Clinical Series | Annals of the New York Academy of Sciences | Pharmacological treatment of dyslipidaemic children and adolescents; fenofibrate cited among agents that have successfully reduced lipoprotein concentrations in paediatric familial hypercholesterolaemia |
| [35499807](https://pubmed.ncbi.nlm.nih.gov/35499807/) | 2022 | Review | Current Atherosclerosis Reports | Dyslipidaemia management in pregnancy; discusses the limitations of fibrates and other agents in special populations, relevant to HoFH family planning and genetic counselling contexts |
| [26432726](https://pubmed.ncbi.nlm.nih.gov/26432726/) | 2015 | Review | Indian Heart Journal | Reviews LDL-C reduction strategies including statins and PCSK9 inhibitors; discusses residual cardiovascular risk and the rationale for adjunctive non-statin therapies in severe hypercholesterolaemia |
| [14620392](https://pubmed.ncbi.nlm.nih.gov/14620392/) | 2003 | Review | Pharmacotherapy | Ezetimibe as a selective cholesterol absorption inhibitor; provides comparative context for non-statin adjuncts used alongside fibrates in complex cholesterol management |
| [9129869](https://pubmed.ncbi.nlm.nih.gov/9129869/) | 1997 | Review | Drugs | Atorvastatin pharmacology and therapeutic use in hyperlipidaemia; contextualises statin-based backbone therapy upon which fenofibrate adjunct use in HoFH would be layered |

---

## Philippines Market Information

Fenofibrate is currently **not registered** with the FDA Philippines. There are no product authorisations on record.

> For reference, fenofibrate is approved in multiple major markets — including the United States (TriCor®, Antara®, Fenoglide®), the European Union (Lipanthyl®), Japan, and Taiwan — for dyslipidaemia and hypertriglyceridaemia indications. Any use in the Philippines would currently require a compassionate use or special access pathway pending local registration.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Safety data including key warnings, contraindications, and drug-drug interactions were not available in the current Evidence Pack (TFDA prescribing information not yet retrieved; DDI database query returned no results). Full prescribing information — including the known pharmacokinetic interaction with lomitapide — must be reviewed before any clinical application. Retrieval of the fenofibrate package insert from FDA Philippines, TFDA, or the US FDA is listed as a required next step.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the TxGNN model assigns a very high prediction score (99.91%) to fenofibrate for HoFH — capturing genuine mechanistic overlap in lipid metabolism pathways — HoFH patients have near-complete LDL receptor deficiency, which substantially limits fenofibrate's primary LDL-C-lowering mechanism; furthermore, no dedicated clinical trial has been conducted, the drug is not registered in the Philippines, and critical safety data remain unreviewed.

**To proceed, the following is needed:**

- **Local registration first:** Initiate FDA Philippines product registration for fenofibrate's established dyslipidaemia / hypertriglyceridaemia indication before pursuing any new indication development in country
- **Safety documentation:** Retrieve and review the full fenofibrate package insert (TFDA PDF download or FDA US labelling) for warnings, contraindications, and drug interactions — particularly the lomitapide interaction characterised in PMID 24734312, given lomitapide's role as a first-line HoFH agent
- **Mechanism of action documentation:** Pull complete MOA and DrugBank category data for DB01039 to formally confirm the PPARα agonist classification and support any regulatory submission narrative
- **Clinical feasibility assessment:** Convene a lipidology expert panel to evaluate whether fenofibrate's TG-lowering and HDL-raising effects provide clinically meaningful adjunctive benefit in HoFH patients already receiving lomitapide, evinacumab, or regular LDL apheresis — and whether this benefit justifies a formal study
- **Research protocol design:** If expert consensus supports proceeding, design a prospective observational or small interventional pilot study in HoFH patients on standard-of-care therapy, with pre-specified endpoints including fasting TG, HDL-C, non-HDL-C, ApoB, and cardiovascular event tracking
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

