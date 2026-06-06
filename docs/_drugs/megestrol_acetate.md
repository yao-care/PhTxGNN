---
layout: default
title: Megestrol Acetate
parent: 僅模型預測 (L5)
nav_order: 218
evidence_level: L5
indication_count: 10
---

# Megestrol Acetate
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

# Megestrol Acetate: From Cancer Cachexia to Uterine Corpus Endometrial Carcinoma

## One-Sentence Summary

Megestrol acetate is a synthetic progestogen used globally for cancer-related cachexia and anorexia, and as a second-line hormone therapy for advanced breast cancer. The TxGNN model predicts it may be effective for **Uterine Corpus Endometrial Carcinoma**, with **3 clinical trials** currently supporting this direction. No published literature was retrieved specifically for this indication pair.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Cancer-related cachexia/anorexia; second-line breast cancer hormone therapy (global use; not registered in the Philippines) |
| Predicted New Indication | Uterine Corpus Endometrial Carcinoma |
| TxGNN Prediction Score | 99.94% |
| Evidence Level | L2 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Megestrol acetate is a potent synthetic progestogen that exerts its anti-tumor effect by binding and activating the progesterone receptor (PR). This competitively blocks estrogen's proliferative signaling in the endometrium, downregulates estrogen receptor (ER) expression, and triggers differentiation and apoptosis in endometrial cancer cells. This is precisely the mechanism exploited in fertility-preserving hormonal treatment for early-stage endometrial carcinoma, and high-dose progestogen therapy (160–320 mg/day) has demonstrated clinical responses in endometrioid adenocarcinoma patients.

Uterine corpus endometrial carcinoma — particularly the endometrioid adenocarcinoma subtype — is a hormone-driven malignancy with characteristically high PR expression. In patients who wish to preserve fertility and whose tumors are confined to the endometrium, progestogen-based therapy represents the internationally accepted approach. Megestrol acetate's receptor-mediated mechanism aligns directly with the biology of this tumor type, making the TxGNN prediction mechanistically sound rather than merely associative.

International clinical guidelines (NCCN, ESMO, JSOG) explicitly list high-dose progestogens — with megestrol acetate as the prototype agent — as the primary therapeutic option for fertility-sparing treatment in Stage IA G1–G2 endometrioid carcinoma. The TxGNN prediction therefore reflects an indication that is already established in multiple international markets, underscoring its clinical plausibility even though it remains unregistered in the Philippines.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00503581](https://clinicaltrials.gov/study/NCT00503581) | Phase 2 | Terminated | 9 | RCT comparing continuous vs. sequential megestrol acetate for endometrial intraepithelial neoplasia and atypical endometrial hyperplasia; directly evaluates megestrol acetate; terminated early due to poor accrual — insufficient statistical power to draw conclusions |
| [NCT00729586](https://clinicaltrials.gov/study/NCT00729586) | Phase 2 | Completed | 73 | Temsirolimus alone vs. temsirolimus + hormonal therapy (including megestrol acetate + tamoxifen) in advanced or recurrent endometrial carcinoma; completed 2017; provides evidence for the hormonal therapy component in combination regimens |
| [NCT04046185](https://clinicaltrials.gov/study/NCT04046185) | Early Phase 1 | Unknown | 60 | PD-1 inhibitor combined with progesterone vs. progesterone alone in early-stage endometrial cancer for fertility preservation; uses progesterone rather than megestrol acetate directly, but the progestogenic mechanism is closely related; limited phase and unknown status reduces evidentiary value |

---

## Literature Evidence

Currently no related literature available.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Hormone therapy (Progestogen class) — receptor-mediated anti-tumor mechanism; not a conventional DNA-damaging cytotoxic agent |
| Myelosuppression Risk | Low — progestogen therapy does not cause clinically significant myelosuppression |
| Emetogenicity Classification | Minimal to low |
| Monitoring Items | Adrenal function (serum cortisol; secondary adrenal suppression reported with long-term high-dose use), fasting blood glucose (risk of glucose intolerance), body weight, clinical signs of thromboembolism |
| Handling Protection | Standard pharmaceutical handling; cytotoxic drug handling precautions not required |

---

## Safety Considerations

Please refer to the package insert for safety information.

Based on published literature referenced in this Evidence Pack:

- **Secondary adrenal suppression**: Long-term high-dose megestrol acetate (≥160 mg/day) has been associated with clinically significant secondary adrenal insufficiency in cancer patients ([PMID 10491532](https://pubmed.ncbi.nlm.nih.gov/10491532/)). Adrenal function monitoring is advisable for treatment courses exceeding 3 months, and dose tapering rather than abrupt discontinuation should be considered.
- **Hemostatic effects / Thromboembolism risk**: High-dose megestrol acetate (160–320 mg/day) has been shown to alter coagulation parameters in gynecologic and breast cancer patients ([PMID 11727356](https://pubmed.ncbi.nlm.nih.gov/11727356/)). Thromboembolism risk should be formally assessed prior to initiation, especially in patients with immobility, prior VTE, or obesity.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Megestrol acetate's progestogenic mechanism directly addresses the hormonal pathophysiology of endometrioid endometrial carcinoma, and international guidelines already recommend it for this indication in other markets. However, the directly available trial evidence within this Evidence Pack is limited — the most relevant Phase 2 RCT (NCT00503581) was terminated with only 9 participants, and no published literature was retrieved for this specific drug–indication pair. The Philippines currently has no registration for this drug, creating an additional regulatory hurdle.

**To proceed, the following is needed:**

- Assess the Philippines FDA (FDA PH) regulatory pathway for importation or compassionate use of a non-registered agent, including whether a drug with established international approvals qualifies for expedited review
- Retrieve the full prescribing information (US FDA or EMA package insert) to complete the safety profile for key warnings and contraindications, which were not available in this Evidence Pack
- Obtain formal MOA and pharmacology data from DrugBank (DB00351) to support mechanistic sections of any regulatory submission
- Review the completed NCT00729586 primary publication to confirm the exact composition of the hormonal therapy arm and extract megestrol-specific efficacy outcomes
- Develop a structured safety monitoring protocol covering adrenal function, glycemic status, and thromboembolism risk for long-term high-dose use (≥160 mg/day)
- **Consider the ovarian cancer indication (Rank 8, Evidence Level L1) as a parallel repurposing target**: a completed Phase 3 RCT ([NCT00005975](https://clinicaltrials.gov/study/NCT00005975), n=288) and multiple Phase 2 studies ([PMID 11593052](https://pubmed.ncbi.nlm.nih.gov/11593052/), [PMID 3099393](https://pubmed.ncbi.nlm.nih.gov/3099393/), [PMID 9856656](https://pubmed.ncbi.nlm.nih.gov/9856656/), [PMID 8080689](https://pubmed.ncbi.nlm.nih.gov/8080689/)) provide substantially stronger direct clinical evidence for megestrol acetate in ovarian cancer and may represent a stronger initial regulatory case
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

