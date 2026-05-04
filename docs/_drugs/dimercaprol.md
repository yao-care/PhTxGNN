---
layout: default
title: Dimercaprol
parent: 僅模型預測 (L5)
nav_order: 108
evidence_level: L5
indication_count: 1
---

# Dimercaprol
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

# Dimercaprol: From Heavy Metal Poisoning to Bronchitis

## One-Sentence Summary

Dimercaprol (BAL, British Anti-Lewisite) is a heavy metal chelating agent classically used as an antidote for arsenic, mercury, and lead poisoning.
The TxGNN model predicts it may be effective for **Bronchitis**, with a prediction score of **99.54%**;
however, **no clinically relevant trials** involving Dimercaprol were identified, and the sole supporting literature consists of **a 1963 case report** of mercury inhalation–induced bronchitis — making this an **L5 evidence prediction only**.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Heavy metal poisoning (arsenic, mercury, lead; no Philippines registration on record) |
| Predicted New Indication | Bronchitis |
| TxGNN Prediction Score | 99.54% |
| Evidence Level | L5 — Model prediction only, no actual intervention studies |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Dimercaprol chelates heavy metals — particularly mercury, arsenic, and lead — by forming stable ring complexes with their ions, thereby reducing tissue toxicity. It was originally developed in World War II as a countermeasure to arsenic-based chemical warfare agents (Lewisite) and later extended to clinical heavy metal poisoning management.

The only mechanistically coherent link between Dimercaprol and bronchitis is **mercury vapor inhalation–induced acute bronchitis**: inhaled mercury vapour deposits in airway mucosa, causing direct inflammatory injury, and Dimercaprol could theoretically reduce this injury by chelating mercury from lung tissue. One 1963 case report (PMID 14068440) documents exactly this scenario — two patients with acute bronchitis secondary to mercury inhalation.

Outside this narrow context, Dimercaprol has **no known mechanism** applicable to viral, bacterial, chronic, or allergic bronchitis. The high TxGNN score (0.9954) is assessed in the evidence pack as a **knowledge graph topological false positive**: the model likely traced a Dimercaprol → mercury → pulmonary toxicity path and scored the drug-disease pair highly without reflecting genuine biological activity. This prediction should **not** be interpreted as a clinically actionable repurposing signal.

---

## Clinical Trial Evidence

No clinical trials involving Dimercaprol as an intervention for bronchitis were identified. The 24 trials retrieved by the ClinicalTrials.gov query all study bronchitis/COPD/bronchiolitis obliterans with unrelated drugs or as purely observational cohorts. Representative examples are listed below for transparency, with their relevance grade noted.

| Trial Number | Phase | Status | Enrollment | Notes |
|-------------|-------|--------|-----------|-------|
| [NCT00423137](https://clinicaltrials.gov/study/NCT00423137) | Phase 2 | Completed | 48 | BIBW2948 BS in COPD with chronic bronchitis — unrelated drug |
| [NCT01334892](https://clinicaltrials.gov/study/NCT01334892) | Phase 2/3 | Terminated | 130 | Liposomal ciclosporin A for bronchiolitis obliterans — unrelated drug |
| [NCT01212406](https://clinicaltrials.gov/study/NCT01212406) | Phase 4 | Completed | 100 | Vitamin D to prevent BOS after lung transplant — unrelated drug |
| [NCT00656058](https://clinicaltrials.gov/study/NCT00656058) | Phase 2 | Completed | 25 | Montelukast for bronchiolitis obliterans post-SCT — unrelated drug |
| [NCT01211509](https://clinicaltrials.gov/study/NCT01211509) | Phase 4 | Completed | 30 | Montelukast for BOS after lung transplant — unrelated drug |

> **None of the above trials involve Dimercaprol.** All were retrieved on the basis of the bronchitis disease label alone and represent background noise rather than supporting evidence.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [14068440](https://pubmed.ncbi.nlm.nih.gov/14068440/) | 1963 | Case Report | Am Rev Respir Dis | Two cases of acute bronchitis following mercury vapor inhalation — the only publication directly implicating mercury toxicity as a mechanism linking Dimercaprol to airway disease |
| [2261963](https://pubmed.ncbi.nlm.nih.gov/2261963/) | 1990 | Observational | Eur Respir J | Short-term smoking reduction associated with decreased lower respiratory tract inflammation in 15 heavy smokers — no relation to Dimercaprol |
| [3048217](https://pubmed.ncbi.nlm.nih.gov/3048217/) | 1988 | Review/Case Series | Ann Surg | Obliterative bronchiolitis after cardiopulmonary transplant in 11/30 patients — no relation to Dimercaprol |

> The only publication with any mechanistic relevance to this repurposing hypothesis is PMID 14068440 (1963), which is a 60-year-old case report with no treatment outcome data for Dimercaprol.

---

## Philippines Market Information

Dimercaprol has **no registered products** in the Philippines. No license data is available.

---

## Safety Considerations

No safety data for Dimercaprol was retrieved from the current data sources. Please refer to the full package insert for warnings, contraindications, and precautions before any clinical use. Key areas to review include:

- Known nephrotoxicity and hepatotoxicity at higher doses
- Contraindication in hepatic insufficiency (except arsenic-induced liver damage)
- Painful intramuscular injection route (the only approved route of administration)
- Interaction with iron supplementation (forms toxic complex)

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's high score for Dimercaprol–bronchitis is a likely topological false positive driven by the Dimercaprol → mercury → pulmonary toxicity path in the knowledge graph. The sole mechanistically coherent use case — mercury inhalation–induced acute bronchitis — is extremely rare and supported only by a single 1963 case report. There is no evidence base to support investigation of Dimercaprol for any of the common bronchitis subtypes (viral, bacterial, chronic, or allergic).

**To reconsider, the following would be required:**

- Identification of a plausible non-mercury mechanism by which Dimercaprol modulates airway inflammation (e.g., zinc chelation, NF-κB pathway effects)
- At least one peer-reviewed preclinical study (in vitro or animal model) demonstrating anti-bronchitis activity independent of heavy metal chelation
- A clinical rationale distinguishing the target bronchitis subtype from the general disease category
- Full pharmacokinetic data for pulmonary delivery (Dimercaprol is currently only formulated for IM injection; inhalation or oral bioavailability data are absent)
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

