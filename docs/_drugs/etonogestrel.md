---
layout: default
title: Etonogestrel
parent: 僅模型預測 (L5)
nav_order: 132
evidence_level: L5
indication_count: 5
---

# Etonogestrel
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

# Etonogestrel: From Contraception to Amenorrhea

## One-Sentence Summary

Etonogestrel is a synthetic progestogen delivered via subdermal implant (Implanon/Nexplanon), widely used as a long-acting reversible contraceptive.
The TxGNN model predicts it may be effective for **Amenorrhea**, with **1 clinical trial** and **2 publications** identified — however, this prediction carries a critical causal direction warning.
Available evidence strongly suggests that etonogestrel is a **cause** of amenorrhea in approximately 20% of users, not a treatment for it, raising serious concerns about the validity of this repurposing signal.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Contraception (progestogen subdermal implant; no Philippines registration on record) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the evidence pack. Based on known pharmaceutical information, Etonogestrel is a third-generation synthetic progestogen that works by suppressing ovulation (via LH surge inhibition), thickening cervical mucus, and altering the endometrial lining to prevent implantation. In clinical practice, this endometrial suppression results in amenorrhea in approximately 20% of implant users — making it a well-documented side effect rather than an intended pharmacological target.

**⚠️ Critical Causal Direction Warning:** The high TxGNN prediction score (99.84%) most likely reflects the knowledge graph having learned the strong co-occurrence of "Etonogestrel ↔ amenorrhea" from clinical literature, without distinguishing causal direction. In pharmacological reality, the association runs as: *etonogestrel causes amenorrhea* — not the other way around. The knowledge graph edge between this drug and this disease may have been encoded bidirectionally, leading to a prediction that inverts the true relationship.

While progestogens do have a narrow clinical role in secondary amenorrhea (e.g., the progesterone challenge test uses progesterone to induce withdrawal bleeding as a diagnostic maneuver), etonogestrel is not a standard or evidence-supported treatment for amenorrhea in any guideline. The remaining four predicted indications (ranks 2–5) are all benign breast conditions — fibrocystic disease, apocrine adenosis, blunt duct adenosis, and benign mammary dysplasia — scored identically or near-identically by TxGNN, suggesting a clustering artifact in the knowledge graph's breast-disease node group rather than independent drug-specific predictions.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT04626596](https://clinicaltrials.gov/study/NCT04626596) | Phase 3 | Completed | 498 | Extended-use study evaluating contraceptive efficacy and safety of the ENG implant during years 4 and 5 of use. Amenorrhea is recorded as a secondary safety endpoint (bleeding pattern monitoring), not as a treatment outcome. This trial reinforces that amenorrhea is a consequence of etonogestrel exposure, not a condition being therapeutically addressed. |

> ⚠️ The only identified trial is a contraceptive efficacy study with a relevance grade of C for the amenorrhea repurposing hypothesis. It does not support this indication for drug repurposing.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [10549446](https://pubmed.ncbi.nlm.nih.gov/10549446/) | 1999 | Multi-center RCT | Contraception | Compared single-rod Implanon (ENG) vs six-capsule Norplant over 2–4 years in 200 women; no pregnancies in either group. Documents bleeding patterns including amenorrhea rates as a side-effect measure. Confirms amenorrhea as a pharmacological consequence of ENG implant use. |
| [33430924](https://pubmed.ncbi.nlm.nih.gov/33430924/) | 2021 | Phase 2/3 RCT protocol | Trials | Protocol for BIO101 (a non-etonogestrel compound) in COVID-19 pneumonia prevention. **This record appears entirely unrelated to etonogestrel or amenorrhea** and likely represents a retrieval error in the evidence pipeline. Recommend flagging for pipeline QC review. |

> ⚠️ Neither publication supports etonogestrel as a treatment for amenorrhea. PMID 33430924 is an apparent false positive requiring review.

---

## Philippines Market Information

Etonogestrel currently has **no registered products** with the Philippine FDA. No license authorization data is available for tabulation.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Philippines FDA prescribing information, package insert warnings, contraindications, and drug interaction profiles were not available at the time of this analysis (Data Gap DG001: Blocking severity). Retrieval of the approved prescribing information from the Philippine FDA portal is required before any further evaluation can proceed.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The top-ranked TxGNN prediction (amenorrhea, 99.84%) represents a causal direction artifact — etonogestrel induces amenorrhea as a side effect, not a therapeutic outcome — and none of the identified trials or literature supports its use as an amenorrhea treatment. The drug is not registered in the Philippines, and all five predicted indications remain at L4–L5 evidence levels with a uniform "Hold" recommendation.

**To proceed, the following is needed:**
- **Pipeline QC:** Investigate and correct causal-direction edge encoding in the TxGNN knowledge graph for drug-induced adverse events (etonogestrel → amenorrhea)
- **MOA data retrieval:** Query DrugBank API to fill Data Gap DG002 (High severity) for mechanism of action details
- **Safety data retrieval:** Download and parse Philippine FDA package insert PDF to fill Data Gap DG001 (Blocking severity) before any S1 safety screening
- **Expert pharmacological review:** Assess whether any progestogen receptor activity of etonogestrel could be redirected toward a genuine therapeutic indication not currently represented in the knowledge graph
- **Broader indication screening:** If repurposing exploration is to continue, consider indications outside the current top-5 list that may better represent mechanistically plausible, non-causal-reversal opportunities
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

