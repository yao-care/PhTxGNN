---
layout: default
title: Goserelin
parent: Moderate Evidence (L3-L4)
nav_order: 163
evidence_level: L3
indication_count: 3
---

# Goserelin
{: .fs-9 }

Evidence Level: **L3** | Predicted Indications: **3** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Goserelin: From Endometriosis to Amenorrhea

## One-Sentence Summary

Goserelin is a GnRH agonist originally used to treat endometriosis.
The TxGNN model predicts it may be relevant for **Amenorrhea**, with **1 clinical trial** and **16 publications** currently linked to this direction.
However, amenorrhea is largely an expected pharmacological effect of goserelin rather than a disease it treats, so the evidence mostly supports a research question, not a true new indication.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Endometriosis (including endometriosis of uterus) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L3 |
| Philippines Market Status | Cancelled only (no valid registration) |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the data compiled for this report. Based on known pharmacology, goserelin is a GnRH agonist. Continuous exposure desensitizes pituitary GnRH receptors, which lowers LH and FSH and reduces ovarian estradiol production. The result is a reversible, medically induced amenorrhea (ovarian suppression).

This explains why endometriosis, an estrogen-dependent condition, responds to goserelin. It also explains the very high TxGNN score: the model is probably picking up amenorrhea as a pharmacodynamic effect of the drug, not as a treatable disease.

The repurposing framing is therefore ambiguous. Deliberately inducing amenorrhea (for example, for heavy bleeding, or for ovarian protection during chemotherapy) is mechanistically plausible. Treating pathological amenorrhea would be counterproductive, because goserelin suppresses the very hormones that are already lacking.

Two further predictions, renal hypoplasia and bilateral renal hypoplasia (scores about 99.1%), have no plausible mechanistic link, no trials and no literature. They are most likely knowledge-graph artifacts and are not pursued here.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | Unknown | 300 | Adjuvant toremifene with or without goserelin in premenopausal women with hormone receptor-positive stage I-IIIA breast cancer, with or without chemotherapy-induced amenorrhoea. The primary endpoint is oncologic, not amenorrhea, and no results are available. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | J Clin Oncol | Goserelin vs CMF as adjuvant therapy in premenopausal node-positive breast cancer (ZIPP/ZEBRA study) |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | J Natl Cancer Inst | IBCSG Trial VIII: chemotherapy followed by goserelin vs either alone in node-negative breast cancer |
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | RCT (secondary analysis) | J Clin Oncol | Impact of chemotherapy and/or goserelin on amenorrhea, hot flashes and quality of life |
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Review/Meta-analysis | Ann Oncol | OPTION trial: GnRH agonist during chemotherapy to reduce the risk of premature ovarian insufficiency |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J R Army Med Corps | Induction of amenorrhoea; goserelin as an effective option compared with continuous oral contraceptives |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Review | Breast Cancer Res Treat | LHRH agonists in early breast cancer; reversible ovarian ablation |
| [12734855](https://pubmed.ncbi.nlm.nih.gov/12734855/) | 2003 | Review | Br J Surg | Ovarian ablation in adjuvant treatment of premenopausal breast cancer |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Retrospective cohort | Cancer Res Treat | Goserelin ovarian ablation improved survival in stage II/III HR-positive breast cancer without chemotherapy-induced amenorrhea |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | Clinical study | Fertil Steril | Goserelin vs low-dose oral contraceptive for endometriosis-related pelvic pain |
| [16889194](https://pubmed.ncbi.nlm.nih.gov/16889194/) | 2006 | Clinical study | Akush Ginekol | Zoladex (goserelin 3.6 mg every 28 days for 6 months) in 112 patients with pelvic endometriosis |

Most of this literature concerns breast cancer and endometriosis, with amenorrhea appearing as an effect of treatment rather than as the condition being treated.

---

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0222 | Goserelin | Not specified | Not specified (status: cancelled) |

---

## Safety Considerations

- **Disease-level cautions (from the knowledge graph, not label text)**: Goserelin is linked to contraindication or caution signals in hypertension, hyperglycemia, diabetes mellitus, diabetic ketoacidosis, hypercalcemia, nephrocalcinosis, phosphorus metabolism disorders, obesity, and urinary tract obstruction.
- **Drug Interactions**: 100 interactions were identified. One is Major: **dolasetron**. Most others are Moderate and cluster in these groups:
  - Antidiabetic agents: acarbose, alogliptin, albiglutide, canagliflozin, chlorpropamide, dapagliflozin, dulaglutide, empagliflozin, glimepiride, linagliptin, metformin, saxagliptin
  - Laxatives and bowel preparations: bisacodyl, picosulfuric acid, polyethylene glycol with electrolytes
  - Other agents: famotidine, loperamide, clarithromycin, palonosetron

Please refer to the package insert for warnings and formal contraindications.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The only related trial is a breast cancer study where amenorrhea is not the target, and the literature mainly describes amenorrhea as a pharmacological effect of ovarian suppression. The high TxGNN score likely reflects this association. In addition, goserelin has no valid registration in the Philippines (the single registration is cancelled).

**To proceed, the following is needed:**
- A clear definition of the intended use (induced amenorrhea, for example for heavy bleeding or fertility protection, versus treatment of pathological amenorrhea)
- Mechanism of action data and package insert safety information (warnings and contraindications)
- Clarification of regulatory status in the Philippines, since the only registration is cancelled
- Prospective clinical evidence with amenorrhea or ovarian protection as a defined endpoint
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

