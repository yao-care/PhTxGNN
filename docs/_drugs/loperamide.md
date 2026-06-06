---
layout: default
title: Loperamide
parent: 僅模型預測 (L5)
nav_order: 209
evidence_level: L5
indication_count: 10
---

# Loperamide
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

# Loperamide: From Acute Diarrhea to Acute Contagious Conjunctivitis

## One-Sentence Summary

Loperamide is a peripheral μ-opioid receptor agonist widely used as an antidiarrheal agent for acute and chronic diarrhea worldwide.
The TxGNN model predicts it may be effective for **Acute Contagious Conjunctivitis** (score: 99.97%); however, **no clinical trials** and **no supporting literature** currently exist for this indication, and no plausible mechanism of action has been identified.
Across all 10 predicted indications in this report, 7 involve conjunctivitis variants — a pattern strongly suggesting a **knowledge graph artifact** rather than a genuine biological signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Acute diarrhea, chronic diarrhea (based on global pharmacological profile; no Philippines FDA registration on record) |
| Predicted New Indication | Acute Contagious Conjunctivitis |
| TxGNN Prediction Score | 99.97% |
| Evidence Level | L5 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is unavailable in the Evidence Pack. Based on established pharmacology, Loperamide is a peripheral μ-opioid receptor agonist that acts selectively on the gut wall to reduce intestinal motility and fluid/electrolyte secretion. It does not cross the blood-brain barrier at therapeutic doses and is widely used for acute traveler's diarrhea, chronic diarrhea, and IBS-associated loose stools.

The top predicted indication — acute contagious conjunctivitis — is an ocular surface infection entirely unrelated to the gastrointestinal tract. There is no established mechanistic pathway linking peripheral μ-opioid agonism to conjunctival inflammation or microbial containment in the eye. The mechanistic assessment in the Evidence Pack concludes that this prediction "may arise from pseudo-correlations via gut-eye comorbidity nodes in the knowledge graph," which is consistent with the observation that 7 of the 10 predictions in this batch are conjunctivitis variants with identical TxGNN scores (ranks 2897–2899 scoring 0.9964832 each), a hallmark of **batch prediction artifact**.

Gastroduodenitis (Rank 4) is the only indication with a biologically plausible mechanistic link: μ-opioid receptors are distributed throughout the gastrointestinal tract, and reducing intestinal hypermotility and mechanical mucosal stimulation could theoretically benefit gastroduodenal inflammation. This rationale is weak and supported only by one outdated study, but it is not implausible in the way that the ocular predictions are.

---

## All Predicted Indications at a Glance

| Rank | Disease | TxGNN Score | Evidence Level | Decision | Key Issue |
|------|---------|-------------|----------------|----------|-----------|
| 1 | Acute contagious conjunctivitis | 99.97% | L5 | Hold | No mechanistic link; KG artifact suspected |
| 2 | Amebic dysentery | 99.95% | L4 | Hold | **Literature supports a contraindication, not a benefit** |
| 3 | Conjunctivitis | 99.87% | L5 | Hold | Retrieved trials are Azithromycin studies — false positives |
| 4 | Gastroduodenitis | 99.77% | L4 | Research Question | Biologically plausible; one small 1986 study only |
| 5 | Pseudomembranous conjunctivitis | 99.65% | L5 | Hold | No mechanistic link |
| 6 | Serous conjunctivitis (non-viral) | 99.65% | L5 | Hold | KG artifact |
| 7 | Conjunctival folliculosis | 99.65% | L5 | Hold | No mechanistic link |
| 8 | Chronic follicular conjunctivitis | 99.65% | L5 | Hold | KG artifact |
| 9 | Parasitic conjunctivitis | 99.65% | L5 | Hold | No mechanistic link; KG artifact |
| 10 | Angelucci syndrome | 99.63% | L5 | Hold | Loperamide's QT-prolongation risk poses a **cardiac safety concern** |

---

## Clinical Trial Evidence

The 2 trials retrieved were found via disease keyword matching for "conjunctivitis." **Neither trial involves Loperamide.**

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04185402](https://clinicaltrials.gov/study/NCT04185402) | Phase 4 | Completed | 74,920 | Randomized trial of Azithromycin discontinuation vs. continuation for trachoma elimination in Niger — **unrelated to Loperamide; false positive hit** |
| [NCT06289647](https://clinicaltrials.gov/study/NCT06289647) | Phase 4 | Withdrawn | 0 | Azithromycin for trachoma in DRC — **withdrawn with zero enrollment; unrelated to Loperamide** |

> **Note:** Both trials study Azithromycin, not Loperamide. They were retrieved by disease keyword overlap and carry no evidentiary weight for this repurposing assessment.

No clinical trials exist for Loperamide in any of the 10 predicted indications.

---

## Literature Evidence

| PMID | Year | Type | Indication Queried | Key Findings |
|------|------|------|--------------------|--------------|
| [3893119](https://pubmed.ncbi.nlm.nih.gov/3893119/) | 1985 | Review | Amebic dysentery | Reviews non-fluid therapies for acute diarrhea; anti-motility agents noted to reduce stool frequency but raises concerns in infectious/invasive diarrhea contexts |
| [17241255](https://pubmed.ncbi.nlm.nih.gov/17241255/) | 2007 | Case Report | Amebic dysentery | **Safety signal:** Fulminant amoebic colitis following heavy loperamide use — loperamide implicated in progression to toxic megacolon in *Entamoeba histolytica* infection |
| [21174149](https://pubmed.ncbi.nlm.nih.gov/21174149/) | 2011 | Clinical Observation | Amebic dysentery | Documents relapse patterns of intestinal and hepatic amebiasis after treatment; contextually relevant to understanding disease course |
| [3520142](https://pubmed.ncbi.nlm.nih.gov/3520142/) | 1986 | Clinical Study | Gastroduodenitis | Small Soviet-era prospective study examining Imodium (loperamide) in peptic ulcer and chronic gastroduodenitis with functional intestinal disorders; abstract only — no outcomes data available |

> **Critical safety note for amebic dysentery (Rank 2):** The available literature supports a **contraindication**, not a treatment effect. Reducing gut motility in invasive *Entamoeba histolytica* infection promotes pathogen retention and toxin accumulation, with documented progression to fulminant colitis and toxic megacolon. This predicted indication must be flagged as a **safety risk**, not a repurposing opportunity.

---

## Philippines Market Information

Loperamide is **not currently registered** with the Philippine Food and Drug Administration. No product licenses, dosage forms, or approved indications are on record for the Philippines market.

---

## Safety Considerations

Please refer to the package insert for full safety information (Philippines-specific prescribing information was not available for this assessment).

**Model-identified safety signals from this evidence review:**

- **Amebic dysentery (Rank 2):** Published case reports document fulminant amoebic colitis and toxic megacolon associated with loperamide use in invasive enteric infections. Use in acute dysentery caused by invasive pathogens is a recognized contraindication.
- **Angelucci syndrome (Rank 10):** Loperamide is associated with QT-interval prolongation and cardiac arrhythmia at elevated doses. Angelucci syndrome involves a cardiac-conjunctival autonomic reflex; loperamide's cardiac risk profile represents a safety concern in this population, not a therapeutic opportunity.

---

## Conclusion and Next Steps

**Decision: Hold (All 10 Indications)**

**Rationale:**
Seven of the 10 predicted indications are conjunctivitis variants with no mechanistic basis and identically clustered TxGNN scores, providing strong evidence of knowledge graph artifact rather than genuine repurposing signal. The most actionable non-ocular finding — amebic dysentery (Rank 2) — is supported by literature as a **contraindication**. Only gastroduodenitis (Rank 4) has any residual biological plausibility, but evidence is limited to a single decades-old study with no accessible outcomes data. Loperamide is also not registered in the Philippines, adding a regulatory barrier to any clinical development pathway.

**To proceed, the following is needed:**

- Retrieve and parse the Philippine FDA (FDA Philippines) package insert or SmPC for Loperamide to complete the blocking safety gap (DG001)
- Query the DrugBank API to obtain the full mechanism of action, target binding profile, and off-target activity data (DG002)
- Confirm current Philippines OTC/Rx registration status and feasibility of market entry
- Investigate whether the conjunctivitis prediction cluster is a systematic artifact in the PhTxGNN model across other μ-opioid drugs (model validation priority)
- For gastroduodenitis only: conduct a targeted modern literature search (2000–present) in PubMed and Embase before deciding whether to escalate to a formal research question
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

