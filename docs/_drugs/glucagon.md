---
layout: default
title: Glucagon
parent: 僅模型預測 (L5)
nav_order: 160
evidence_level: L5
indication_count: 1
---

# Glucagon
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

# Glucagon: From Hypoglycemia Emergency Treatment to Irritable Bowel Syndrome

## One-Sentence Summary

Glucagon is a peptide hormone traditionally used as an emergency treatment for severe hypoglycemia and as a diagnostic aid to reduce gastrointestinal motility during imaging procedures. The TxGNN model predicts it may be effective for **Irritable Bowel Syndrome (IBS)**, with **11 clinical trials** and **20 publications** currently supporting this direction — most notably, a completed Phase 1/2 trial of ROSE-010 (synthetic human glucagon) directly in IBS-C patients.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Severe hypoglycemia emergency treatment; GI diagnostic imaging aid |
| Predicted New Indication | Irritable Bowel Syndrome (IBS) |
| TxGNN Prediction Score | 99.24% |
| Evidence Level | L2 (1 completed Phase 1/2 RCT directly testing glucagon in IBS) |
| Taiwan Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Glucagon acts through the glucagon receptor to regulate gastrointestinal smooth muscle motility, inhibiting small intestinal peristalsis and delaying gastric emptying. This pharmacological property — which has long been exploited clinically to achieve bowel relaxation during diagnostic imaging — forms the mechanistic bridge to IBS. In IBS patients, disordered gut motility and visceral hypersensitivity are central pathophysiological features, and an agent capable of modulating smooth muscle contractility could directly address spasmodic pain and abnormal transit.

Critically, glucagon belongs to the proglucagon-derived peptide family, which also includes GLP-1 and GLP-2. These related peptides play important roles in intestinal endocrine regulation, gut-brain axis signaling, and visceral pain modulation. ROSE-010, a synthetic analogue of human glucagon that acts as a GLP-1 receptor agonist, has been specifically tested in IBS-C patients and demonstrated promising pain relief effects in a completed Phase 1/2 trial (NCT01056107, n=52). A 2025 systematic review and meta-analysis (PMID 40134805) further consolidates evidence that GLP-1 receptor agonists can inhibit the migrating motor complex and decrease gastrointestinal motility in IBS patients.

While the original mechanism of action annotation is incomplete and requires supplementation from DrugBank, the existing clinical and mechanistic evidence strongly supports the biological plausibility of glucagon (and its derivatives) as a therapeutic approach for IBS, particularly the constipation-predominant subtype (IBS-C).

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT01056107](https://clinicaltrials.gov/study/NCT01056107) | Phase 1/2 | Completed | 52 | **Core evidence.** ROSE-010 (synthetic human glucagon) tested in female IBS-C patients. Hypothesis: delays gastric emptying and enhances gastric accommodation without retarding colonic transit. |
| [NCT04763564](https://clinicaltrials.gov/study/NCT04763564) | Phase 2 | Terminated | 8 | Liraglutide (GLP-1 RA) vs placebo in IPAA patients with chronic high bowel frequency. Terminated early due to recruitment difficulties — negative signal for feasibility. |
| [NCT02731664](https://clinicaltrials.gov/study/NCT02731664) | Phase 1 | Completed | 12 | Investigated GLP-1 inhibitory effect on prandial antro-duodeno-jejunal motility in vivo. Provides pharmacological basis for proglucagon-derived peptides modulating gut motility. |
| [NCT06408610](https://clinicaltrials.gov/study/NCT06408610) | N/A | Completed | 66 | Exercise training effects on gut dysbiosis and GLP-1 in obese IBS patients. Glucagon/GLP-1 measured as biomarker only, not therapeutic intervention. |
| [NCT03256266](https://clinicaltrials.gov/study/NCT03256266) | N/A | Active, not recruiting | 375 | Small intestinal human organoid study evaluating nutrient antigens and therapeutic agents. Basic research, indirect relevance. |
| [NCT06113146](https://clinicaltrials.gov/study/NCT06113146) | N/A | Completed | 41 | Ultra-processed food eating rate effects on metabolic responses. Glucagon measured as metabolic marker only. |
| [NCT04111263](https://clinicaltrials.gov/study/NCT04111263) | N/A | Completed | 33 | Gut microbiota-targeted nutritional intervention for barrier integrity. Related to gut health but not glucagon therapy. |
| [NCT00802971](https://clinicaltrials.gov/study/NCT00802971) | N/A | Completed | 12 | Idiopathic reactive hypoglycemia prevalence and fructo-oligosaccharide supplementation. Indirect relation via glucagon counterregulation. |
| [NCT05249023](https://clinicaltrials.gov/study/NCT05249023) | N/A | Completed | 37 | Butyrate mode of action in human colon, linked to IBS pathophysiology. No direct glucagon relevance. |
| [NCT04230655](https://clinicaltrials.gov/study/NCT04230655) | N/A | Unknown | 110 | Low energy diet vs intragastric balloon in obesity. Background metabolic study. |

> **Note:** Only NCT01056107 (ROSE-010 in IBS-C) constitutes direct evidence for glucagon repurposing in IBS. The remaining trials provide indirect mechanistic or contextual support.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [40134805](https://pubmed.ncbi.nlm.nih.gov/40134805/) | 2025 | Systematic Review & Meta-analysis | Front Endocrinol | GLP-1 RAs improve IBS symptoms; GLP-1 and ROSE-010 inhibit migrating motor complex and decrease GI motility in IBS patients. |
| [35234561](https://pubmed.ncbi.nlm.nih.gov/35234561/) | 2022 | Clinical Trial Report (Post-hoc) | Scand J Gastroenterol | ROSE-010 showed promising pain relief during IBS attacks; cross-analysis identified most suitable subpopulations for treatment. |
| [30444291](https://pubmed.ncbi.nlm.nih.gov/30444291/) | 2019 | Narrative Review | Exp Physiol | L-cells secreting GLP-1 respond to nutrients, microbial factors, and bile acids; explores GLP-1 role in IBS pathophysiology. |
| [28215540](https://pubmed.ncbi.nlm.nih.gov/28215540/) | 2017 | Observational | Clin Res Hepatol Gastroenterol | Decreased serum GLP-1 correlates with abdominal pain in IBS-C patients; GLP-1 receptor expression altered in colon. |
| [31602785](https://pubmed.ncbi.nlm.nih.gov/31602785/) | 2020 | Preclinical | Neurogastroenterol Motil | Exendin-4 (GLP-1 RA) ameliorated GI dysfunction in Wistar Kyoto rat IBS model; supports GLP-1 pathway in IBS. |
| [31311066](https://pubmed.ncbi.nlm.nih.gov/31311066/) | 2019 | Preclinical | Neurogastroenterol Motil | Ghrelin sensitizes colonic neurons to GLP-1 RA exendin-4, implicating postprandial symptom exacerbation mechanism in IBS. |
| [26765585](https://pubmed.ncbi.nlm.nih.gov/26765585/) | 2016 | Review | Expert Opin Investig Drugs | Reviews novel investigational drugs for IBS-C including GLP-1 analogue ROSE-010 as a potential therapeutic agent. |
| [25427821](https://pubmed.ncbi.nlm.nih.gov/25427821/) | 2015 | Preclinical/PoC | Adv Exp Med Biol | Aerosolized GLP-1 delivery for diabetes and IBS; explores alternative administration routes. |
| [38997662](https://pubmed.ncbi.nlm.nih.gov/38997662/) | 2024 | Systematic Review | J Headache Pain | GLP-1 RAs evaluated for headache and pain disorders; highlights GLP-1 role in neuronal pain pathways relevant to visceral pain. |
| [21694813](https://pubmed.ncbi.nlm.nih.gov/21694813/) | 2011 | Review | Ther Adv Gastroenterol | IBS treatment beyond fiber and antispasmodics; discusses emerging therapies including GLP-1 pathway modulation. |

> **Additional literature (not tabled):** 10 more publications including studies on gut-brain-microbiome axis (PMID 30023410), low FODMAP diet effects on GLP-1 in IBS (PMID 40880735), GLP-1 RA prescription patterns in IBS (PMID 40697433), carbohydrate-restricted diet and hormonal changes in IBS (PMID 33450656), serotonin fluctuation in IBS (PMID 32968548), ileal endocrine cells in IBS (PMID 24605036), colonic motility under stress in IBS (PMID 3617051), and gut-brain interactions review (PMID 41480755).

## Taiwan Market Information

Glucagon currently has **no registered products** in Taiwan (TFDA). There are 0 active marketing authorizations.

> To proceed with repurposing in Taiwan, regulatory pathway assessment (e.g., new drug application or clinical trial application) would be required.

## Safety Considerations

> Please refer to the package insert for safety information. Current evidence pack lacks Taiwan TFDA label data (warnings, contraindications, and drug interactions). This is classified as a **Blocking** data gap (DG001) that must be resolved before entering Stage 1 safety evaluation.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although a completed Phase 1/2 trial (ROSE-010, NCT01056107) and a 2025 systematic review provide L2-level evidence supporting glucagon/GLP-1 pathway modulation for IBS, the drug is **not marketed in Taiwan** (0 registrations) and critical safety data (TFDA label warnings, contraindications) remain unresolved Blocking-level gaps. The direct clinical evidence is limited to a single small trial (n=52) using a synthetic glucagon analogue (ROSE-010), not glucagon itself.

**To proceed, the following is needed:**
- **[Blocking] TFDA labeling data**: Download and parse the package insert from the TFDA website to complete safety assessment (DG001)
- **[High] Mechanism of action (MOA)**: Query DrugBank API for complete pharmacological profile of Glucagon (DG002)
- **Regulatory pathway analysis**: Assess feasibility of introducing glucagon in Taiwan, given zero current market presence
- **Distinguish glucagon vs. ROSE-010**: Clarify whether the repurposing target is native glucagon or the synthetic analogue ROSE-010 (a GLP-1 receptor agonist), as their receptor pharmacology and clinical profiles differ significantly
- **Phase 2 efficacy data**: Monitor for larger-scale RCTs specifically testing glucagon (not GLP-1 RAs like liraglutide or semaglutide) in IBS populations
- **IBS subtype specificity**: Current evidence is strongest for IBS-C (constipation-predominant); assess applicability to other subtypes (IBS-D, IBS-M)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

