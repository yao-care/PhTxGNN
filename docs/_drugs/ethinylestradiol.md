---
layout: default
title: Ethinylestradiol
parent: 僅模型預測 (L5)
nav_order: 131
evidence_level: L5
indication_count: 1
---

# Ethinylestradiol
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

# Ethinylestradiol: From Hormonal Contraception to Zinc, Elevated Plasma

## One-Sentence Summary

Ethinylestradiol is a synthetic estrogen widely used as the estrogenic component of combined oral contraceptive pills; no Philippines regulatory registration data is currently on file.
The TxGNN model predicts it may be effective for **Zinc, Elevated Plasma** (hyperzincemia),
with **0 clinical trials** and **2 observational publications** currently supporting this direction — making the evidence base extremely limited at this time.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Not available from Philippines registration data (commonly used as a synthetic estrogen in oral contraceptives) |
| Predicted New Indication | Zinc, Elevated Plasma |
| TxGNN Prediction Score | 99.63% |
| Evidence Level | L4 (preclinical/mechanistic studies only) |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Ethinylestradiol (EE) is a synthetic 17α-ethinyl derivative of estradiol. Estrogens are known to modulate the expression of zinc-binding proteins — particularly metallothionein and albumin — which regulate zinc distribution between plasma and tissues. Estrogens also influence intestinal zinc absorption and renal zinc reabsorption, both of which can indirectly reduce circulating plasma zinc concentrations. It is on the basis of these known metabolic interactions that the TxGNN model likely identified this association.

However, the evidence supporting this mechanistic link is indirect and historically contextual. The plasma zinc-lowering effect was first observed as an incidental metabolic side effect in women taking oral contraceptives, not as a therapeutic effect deliberately targeted at hyperzincemia. Critically, the foundational animal and human studies involve combination formulations (e.g., norethindrone + mestranol, or Ovulen/Demulen/Enovid-E) rather than ethinylestradiol as an isolated agent. Notably, mestranol is itself a prodrug that is demethylated to ethinylestradiol in vivo, adding one additional degree of indirectness.

In summary, while a pharmacological basis for estrogen's influence on zinc homeostasis exists, the specific, dose-dependent, and clinically actionable therapeutic effect of ethinylestradiol monotherapy on elevated plasma zinc has not been established. The biological plausibility is low-to-moderate; the clinical translation gap is large.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [961877](https://pubmed.ncbi.nlm.nih.gov/961877/) | 1976 | Observational/Cross-sectional | The American Journal of Physiology | Rat study across three dietary zinc levels: mestranol (an EE prodrug) depressed plasma zinc, tibia copper, and magnesium; studied alongside norethindrone as a combination OCP formulation |
| [736629](https://pubmed.ncbi.nlm.nih.gov/736629/) | 1978 | Observational/Cross-sectional | Archives of Gynecology | Human study of four OCP brands (Ovulen-21, Demulen, Enovid-E, Ovral): plasma copper elevated significantly in OCP users; plasma zinc levels remained relatively constant — suggesting OCP use does not reliably lower plasma zinc |

---

## Philippines Market Information

No Philippines FDA registrations on file for Ethinylestradiol. This drug is currently not marketed in the Philippines based on available data.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data including key warnings, contraindications, and drug-drug interactions were not available in this Evidence Pack. Retrieving the full prescribing information from an authoritative source (e.g., FDA Philippines, EMA, or the US FDA label) is strongly recommended before any further evaluation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model assigns a high mathematical score (99.63%), but the underlying evidence does not support clinical translation — the two available publications are 50-year-old observational animal and human studies involving combination OCP products, not ethinylestradiol monotherapy; furthermore, one of those studies (PMID 736629) found that plasma zinc levels remained *relatively constant* in OCP users, directly undermining the prediction's premise.

**To proceed, the following is needed:**

- **Reconfirm the biological direction:** Retrieve and critically appraise all human studies measuring plasma zinc in women on EE-containing contraceptives; resolve the conflicting finding in PMID 736629.
- **Isolate the EE contribution:** Identify any study that isolates EE from progestin co-components to confirm EE alone reduces plasma zinc.
- **Establish clinical context for the target condition:** Determine whether "zinc, elevated plasma" represents a defined clinical syndrome with treatment need, or an incidental laboratory finding.
- **Retrieve MOA data:** Query DrugBank API for ethinylestradiol's full mechanism of action and pharmacokinetic profile to strengthen or refute the mechanistic link.
- **Retrieve safety data:** Download and parse the Philippines FDA or TFDA prescribing information PDF to complete the safety profile (key warnings, contraindications, DDI) before any S1 safety screening can begin.
- **Consider whether the indication is clinically meaningful:** Elevated plasma zinc is rarely a primary treatment target; the therapeutic niche and unmet need should be defined before investing further resources.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

