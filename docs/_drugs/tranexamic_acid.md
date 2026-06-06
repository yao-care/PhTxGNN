---
layout: default
title: Tranexamic Acid
parent: 僅模型預測 (L5)
nav_order: 339
evidence_level: L5
indication_count: 1
---

# Tranexamic Acid
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

# Tranexamic Acid: From Hemorrhage Control to Amenorrhea

## One-Sentence Summary

Tranexamic acid is a well-established antifibrinolytic agent used to prevent and treat excessive bleeding in surgical, traumatic, and heavy menstrual bleeding settings.
The TxGNN model predicts it may be effective for **Amenorrhea (Disease)**,
with **0 clinical trials** and **2 publications** currently available — however, mechanistic analysis strongly suggests this prediction is a **false positive** arising from broad clustering of TXA with menstrual-related conditions.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines registration data available |
| Predicted New Indication | Amenorrhea (Disease) |
| TxGNN Prediction Score | 99.19% |
| Evidence Level | L4 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | **Hold** |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank source (data gap). Based on known pharmacology, tranexamic acid (TXA) is an antifibrinolytic agent that competitively blocks the lysine-binding sites on plasminogen, thereby inhibiting fibrinolysis and preventing clot breakdown. The net pharmacological effect is **pro-hemostatic** — it reduces bleeding, not promotes it.

The core problem with this prediction is a **fundamental directional contradiction**: amenorrhea is defined as the absence of menstruation, while TXA's mechanism of action works to reduce or stop bleeding. If TXA were applied in the context of amenorrhea, it would, if anything, reinforce the condition rather than treat it. There is no mechanistic pathway by which inhibiting fibrinolysis would restore menstrual flow.

The high TxGNN score (99.19%) most likely reflects the model broadly clustering TXA within the "menstrual/uterine-related diseases" category — since TXA is legitimately used for heavy menstrual bleeding (menorrhagia), the knowledge graph may have created a spurious association to adjacent gynecological conditions including amenorrhea. The 2 retrieved publications do not directly support TXA as a treatment for amenorrhea; rather, they concern menstrual suppression and management in specific clinical contexts (e.g., hematologic cancer patients), which further illustrates the indirect and incidental nature of the association.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|------------|
| [39043214](https://pubmed.ncbi.nlm.nih.gov/39043214/) | 2024 | Systematic Review / Clinical Guideline | Journal of Oncology Pharmacy Practice | Systematic approach to menses prophylaxis and suppression in pre-menopausal hematologic cancer patients; evaluates agents for managing menstrual bleeding in the context of treatment-associated cytopenias — TXA appears as one of several hemostatic options, not as a treatment for amenorrhea |
| [21701432](https://pubmed.ncbi.nlm.nih.gov/21701432/) | 2011 | Narrative Review | Menopause (New York, N.Y.) | Evidence-based review of pharmacological therapies for abnormal uterine bleeding; covers nonhormonal agents (NSAIDs reducing bleeding 25–35%) and hormonal options — context is managing excessive bleeding, not absent menstruation |

---

## Philippines Market Information

Tranexamic acid currently has no registered products with the Philippine FDA. No authorization data is available.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for tranexamic acid in amenorrhea is mechanistically contradictory — TXA is a hemostatic agent that suppresses bleeding, making it pharmacologically incompatible with treating absent menstruation. No clinical trials support this indication, and the 2 available publications address unrelated clinical contexts (menstrual suppression in oncology patients). The high model score is assessed as a false positive due to broad knowledge-graph clustering with menstrual-related diseases.

**To proceed, the following would be needed:**
- A plausible mechanistic hypothesis explaining how antifibrinolytic activity could restore or induce menstruation (none identified at this time)
- At minimum one hypothesis-generating preclinical or observational study directly linking TXA to amenorrhea treatment (none found)
- Resolution of the data gap on Philippines registration and package insert safety data (DG001), and formal DrugBank MOA retrieval (DG002)
- If the intended clinical question is actually **menorrhagia** (heavy menstrual bleeding) rather than amenorrhea, a re-query against that indication is warranted — TXA has established evidence for menorrhagia and would likely yield a more clinically meaningful prediction
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

