---
layout: default
title: Ranitidine
parent: 僅模型預測 (L5)
nav_order: 191
evidence_level: L5
indication_count: 10
---

# Ranitidine
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

# Ranitidine: From Gastric Acid Hypersecretion to Active Peptic Ulcer Disease

## One-Sentence Summary

Ranitidine is a well-established histamine H2-receptor antagonist historically used globally for gastric acid-related conditions, but it currently holds no registered product license in the Philippines.
The TxGNN model predicts it may be effective for **Active Peptic Ulcer Disease**,
with **1 clinical trial** and **19 publications** currently supporting this direction.

> **Interpretive note**: This prediction represents a pharmacological **validation** of ranitidine's historically primary indication rather than a novel repurposing finding. The high score reflects the strength of the mechanistic signal within the knowledge graph. Global market availability has been severely impacted since 2020 due to NDMA contamination findings.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not registered in the Philippines (no license data on file) |
| Predicted New Indication | Active Peptic Ulcer Disease |
| TxGNN Prediction Score | 99.89% |
| Evidence Level | L1 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Ranitidine is a selective, competitive histamine H2-receptor antagonist. Although detailed MOA data is not available in the current dataset, extensive published literature confirms its mechanism: ranitidine blocks H2 receptors on gastric parietal cells, inhibiting both basal and stimulated gastric acid secretion and reducing nocturnal acid output by approximately 70%. The resulting elevation of intragastric pH creates a favorable microenvironment for ulcer healing — a well-characterised, direct pharmacological pathway requiring no inferential leaps.

The connection between ranitidine and active peptic ulcer disease is one of the most thoroughly established relationships in gastroenterology. Before proton pump inhibitors (PPIs) became the dominant standard of care, ranitidine (Zantac) was among the most widely prescribed drugs worldwide, with its primary regulatory approval covering short-term treatment of active duodenal and gastric ulcers. Pivotal RCTs published from the early 1980s onward (PMID 3909374, PMID 2877570, PMID 1863945) documented duodenal ulcer healing rates exceeding 90% at 4–8 weeks and demonstrated that maintenance therapy significantly reduced 12-month relapse rates.

The high TxGNN prediction score (99.89%) therefore reflects the robustness of the pharmacological signal within the knowledge graph — the H2 receptor → parietal cell → acid suppression → ulcer healing pathway is a direct, high-confidence node relationship — rather than an unexpected or speculative repurposing discovery. This is a case where the model performs as a validation tool, and its output is consistent with decades of clinical evidence.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00930670](https://clinicaltrials.gov/study/NCT00930670) | Phase 4 | Completed | 320 | Investigated whether PPIs and statins interfere with clopidogrel antiplatelet effects in post-PCI patients on dual antiplatelet therapy. Ranitidine was not the primary investigational drug, and this trial provides no direct efficacy data for ranitidine in active PUD. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [3909374](https://pubmed.ncbi.nlm.nih.gov/3909374/) | 1985 | RCT | Scand J Gastroenterol | Ranitidine 300 mg/day in 151 patients (duodenal, prepyloric, and gastric ulcers): healing rates of 91% for duodenal ulcer at 4 weeks. Maintenance therapy (100–150 mg nightly) significantly delayed 1-year relapse vs placebo. |
| [2877570](https://pubmed.ncbi.nlm.nih.gov/2877570/) | 1986 | RCT | Am J Med | Large multicenter double-blind international trial (n=1,031; 68 investigators in 19 countries): famotidine vs ranitidine in endoscopically confirmed active duodenal ulcer — equivalent healing efficacy established across a large, diverse population. |
| [3104657](https://pubmed.ncbi.nlm.nih.gov/3104657/) | 1986 | RCT | Klinische Wochenschrift | Rioprostil (prostaglandin E1 analogue) vs ranitidine 300 mg nightly in duodenal ulcer healing; ranitidine served as the efficacy comparator benchmark. Discusses acid suppression depth and gastrin elevation as trade-offs. |
| [1863945](https://pubmed.ncbi.nlm.nih.gov/1863945/) | 1991 | RCT | Clin Ther | Multicenter double-blind trial (n=160): famotidine 40 mg vs ranitidine 300 mg nightly for active duodenal ulcer. Healing confirmed endoscopically at 8 weeks: 94% (famotidine) vs 80% (ranitidine); 6-month maintenance data provided. |
| [2491360](https://pubmed.ncbi.nlm.nih.gov/2491360/) | 1989 | RCT | J Gastroenterol Hepatol | Omeprazole (10 mg or 20 mg QD) vs ranitidine (150 mg BID) in active duodenal ulcer (n=270) with weekly endoscopy. Ranitidine as active comparator; prospective collection of 46 potential prognostic factors for healing. |
| [6317325](https://pubmed.ncbi.nlm.nih.gov/6317325/) | 1983 | Drug Review | Drug Intell Clin Pharm | Early FDA-approval narrative review: ranitidine is 4–10× more potent than cimetidine on a molar basis. Summarises clinical trial evidence supporting approval for short-term treatment of active duodenal ulcer and gastric hypersecretory conditions. |
| [6317740](https://pubmed.ncbi.nlm.nih.gov/6317740/) | 1983 | Drug Review | J Clin Gastroenterol | Comparative pharmacodynamics and pharmacokinetics of ranitidine vs cimetidine. Ranitidine 6–8× more potent for gastric acid suppression; longer duration of action; clinical significance of differences outlined. |
| [1976583](https://pubmed.ncbi.nlm.nih.gov/1976583/) | 1990 | Review | Hepato-gastroenterology | Comprehensive review: inhibition of nocturnal and 24-hour intragastric acidity is the key factor predicting ulcer healing. Compares H2 blockers including ranitidine and famotidine on pH control, pepsin inhibition, and healing outcomes. |
| [12751338](https://pubmed.ncbi.nlm.nih.gov/12751338/) | 2003 | Clinical Trial | São Paulo Med J | Ranitidine bismuth citrate + clarithromycin 7-day regimen for H. pylori eradication in Brazilian peptic ulcer patients. Supports ranitidine-based combination therapy as a valid H. pylori treatment platform. |
| [18493408](https://pubmed.ncbi.nlm.nih.gov/18493408/) | 1996 | Clinical Study | Diagn Ther Endosc | Prospective endoscopic study of PUD during Ramadan fasting (n=23): ranitidine 150 mg BID at meal breaks maintained ulcer healing in adherent patients; non-adherent patients showed deterioration. Real-world dosing compliance data. |

---

## Philippines Market Information

Ranitidine has **no registered products** with the Philippine Food and Drug Administration (FDA Philippines). There are currently **0 active drug licenses** on file for this compound.

This absence of Philippines registration is consistent with the global market situation: between 2019 and 2020, regulatory agencies including the US FDA, EMA, and Health Canada identified unacceptable levels of N-nitrosodimethylamine (NDMA) — a probable human carcinogen — in ranitidine formulations. This led to voluntary recalls by manufacturers worldwide and the withdrawal of ranitidine from most major regulated markets. As a result, ranitidine cannot currently be assessed for the Philippines market in the same way as an active, registered compound.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Critical regulatory context**: Ranitidine-containing products were recalled globally in 2020 following detection of NDMA contamination above the acceptable daily intake (ADI) threshold. Any future clinical consideration would require verification of an NDMA-free or NDMA-below-ADI formulation from a certified manufacturer, followed by regulatory re-submission. Package insert warnings, contraindications, and drug interaction data are not available in the current dataset and must be obtained from the original labelling documentation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite an extensively documented evidence base confirming ranitidine's efficacy in active peptic ulcer disease (L1 — multiple large completed Phase 3 RCTs), the drug is not registered in the Philippines and was subject to global market withdrawal due to NDMA contamination. In the current landscape, PPIs (omeprazole, esomeprazole, pantoprazole) have largely superseded H2 blockers as first-line therapy, further reducing the urgency of ranitidine re-entry. Proceeding requires resolution of both formulation safety and regulatory standing before any clinical pathway can be mapped.

**To proceed, the following is needed:**

- **Formulation safety confirmation**: Certified NDMA-free or NDMA-below-ADI ranitidine formulation from an approved manufacturer, verified by validated analytical methods
- **Complete safety documentation**: Package insert warnings, contraindications, and comprehensive drug-drug interaction data (all currently unavailable in this dataset)
- **Mechanism of action documentation**: Full MOA description from DrugBank or equivalent source for inclusion in the regulatory dossier
- **Philippines FDA regulatory strategy**: Assessment of the re-registration pathway under FDA Philippines requirements, including whether a new NDA or abbreviated submission applies
- **Comparative effectiveness analysis**: Updated head-to-head comparison vs current Philippines standard of care (PPI-based regimens and H. pylori eradication protocols) to establish clinical positioning
- **H. pylori co-therapy evaluation**: Given that H. pylori eradication is now the definitive treatment for most peptic ulcers, clarify whether ranitidine bismuth citrate formulations (which have a distinct regulatory history) offer any pathway advantage
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

