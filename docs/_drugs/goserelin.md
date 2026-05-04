---
layout: default
title: Goserelin
parent: 僅模型預測 (L5)
nav_order: 161
evidence_level: L5
indication_count: 3
---

# Goserelin
{: .fs-9 }

證據等級: **L5** | 預測適應症: **3** 個
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

# Goserelin: From Hormone-Dependent Cancers to Amenorrhea

## One-Sentence Summary

Goserelin is a GnRH (gonadotropin-releasing hormone) agonist widely used internationally for the treatment of hormone-dependent conditions such as prostate cancer, breast cancer, and endometriosis. The TxGNN model predicts it may be effective for **Amenorrhea**, with **7 clinical trials** and **19 publications** currently supporting this direction — notably, inducing amenorrhea is already a well-established pharmacological effect of this drug.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in the Philippines; internationally approved for prostate cancer, breast cancer, endometriosis |
| Predicted New Indication | Amenorrhea (disease) |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

## Why is This Prediction Reasonable?

Goserelin is a synthetic GnRH agonist. When administered continuously (e.g., as a depot injection), it causes downregulation of GnRH receptors in the anterior pituitary gland. This leads to a sustained suppression of luteinizing hormone (LH) and follicle-stimulating hormone (FSH) secretion, which in turn inhibits ovarian estrogen production in women. The direct pharmacological consequence of this hormonal suppression is the induction of amenorrhea — the cessation of menstruation.

This prediction is notable because amenorrhea is not merely a side effect but a **well-characterised and intentionally leveraged pharmacological action** of goserelin. In clinical oncology, goserelin is routinely administered to premenopausal breast cancer patients to achieve ovarian suppression, with amenorrhea serving as the clinical indicator of successful treatment. Multiple Phase 3 trials (e.g., OPTION trial, SWOG S0230) have specifically measured amenorrhea rates as a primary or key secondary endpoint.

Beyond oncology, goserelin-induced amenorrhea has been applied therapeutically in gynaecological conditions such as endometriosis and uterine fibroids, and even explored for managing severe uterine haemorrhage in patients with congenital aplastic anaemia. The mechanistic link between goserelin and amenorrhea is therefore **direct, well-established, and clinically validated** across multiple therapeutic contexts.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00427245](https://clinicaltrials.gov/study/NCT00427245) | Phase 3 | Completed | 400 | OPTION trial: Largest RCT evaluating goserelin for ovarian protection and prevention of early menopause in premenopausal breast cancer patients undergoing chemotherapy. Amenorrhea was a primary endpoint. |
| [NCT00068601](https://clinicaltrials.gov/study/NCT00068601) | Phase 3 | Completed | 257 | SWOG S0230: LHRH analog (goserelin) administered during chemotherapy to reduce ovarian failure in hormone-receptor-negative breast cancer. Demonstrated ovarian protection benefit. |
| [NCT02483767](https://clinicaltrials.gov/study/NCT02483767) | Phase 3 | Completed | 98 | Prospective RCT evaluating GnRH agonist goserelin for preservation of ovarian function during chemotherapy. Amenorrhea incidence was a key outcome measure. |
| [NCT02132390](https://clinicaltrials.gov/study/NCT02132390) | Phase 3 | Unknown | 300 | Adjuvant toremifene ± goserelin in premenopausal HR+ breast cancer, with chemotherapy-induced amenorrhea as a stratification/outcome variable. |
| [NCT03475758](https://clinicaltrials.gov/study/NCT03475758) | Phase 2 | Unknown | 100 | Goserelin for ovarian protection in premenopausal patients receiving cyclophosphamide-containing chemotherapy; menstruation outcome as primary endpoint. |
| [NCT01218581](https://clinicaltrials.gov/study/NCT01218581) | Phase 2/3 | Completed | 32 | RCT comparing aromatase inhibitors vs. GnRH agonists for uterine adenomyosis management; amenorrhea as part of the treatment mechanism. |
| [NCT00488722](https://clinicaltrials.gov/study/NCT00488722) | N/A | Unknown | N/A | Single-arm study of Zoladex 3.6 mg combined with CEF chemotherapy as neo-adjuvant therapy; reversible amenorrhea induced by goserelin was a documented effect. |

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [28472240](https://pubmed.ncbi.nlm.nih.gov/28472240/) | 2017 | Clinical Trial Report | Ann Oncol | OPTION trial results: GnRH agonist during chemotherapy reduced risk of premature ovarian insufficiency in early breast cancer patients. |
| [12488406](https://pubmed.ncbi.nlm.nih.gov/12488406/) | 2002 | RCT | J Clin Oncol | ZEBRA study: Goserelin vs. CMF as adjuvant therapy; goserelin induced reversible amenorrhea with fewer toxic effects than chemotherapy. |
| [14679153](https://pubmed.ncbi.nlm.nih.gov/14679153/) | 2003 | RCT | J Natl Cancer Inst | IBCSG Trial VIII: Chemotherapy followed by goserelin vs. each alone; demonstrated goserelin's role in ovarian suppression and amenorrhea induction. |
| [8513962](https://pubmed.ncbi.nlm.nih.gov/8513962/) | 1993 | RCT | Fertil Steril | Goserelin vs. low-dose OC for endometriosis-related pelvic pain; goserelin effectively induced amenorrhea as therapeutic mechanism. |
| [25187267](https://pubmed.ncbi.nlm.nih.gov/25187267/) | 2015 | Clinical Outcome Study | Cancer Res Treat | Ovarian ablation with goserelin improved survival in premenopausal HR+ breast cancer patients without chemotherapy-induced amenorrhea. |
| [17159194](https://pubmed.ncbi.nlm.nih.gov/17159194/) | 2007 | Comparative Study | J Clin Oncol | IBCSG Trial VIII QOL analysis: Compared amenorrhea rates, hot flashes, and quality of life across chemotherapy, goserelin, and combination arms. |
| [1533675](https://pubmed.ncbi.nlm.nih.gov/1533675/) | 1992 | Review | J R Army Med Corps | Reviewed methods for therapeutic amenorrhea induction; goserelin described as "extremely effective" for this purpose. |
| [12353820](https://pubmed.ncbi.nlm.nih.gov/12353820/) | 2002 | Review | Breast Cancer Res Treat | Overview of LHRH agonists in early breast cancer; goserelin induces reversible ovarian ablation with amenorrhea as the clinical marker. |
| [10730389](https://pubmed.ncbi.nlm.nih.gov/10730389/) | 1999 | Clinical Study | Akush Ginekol | GnRH agonist (Zoladex) used to induce amenorrhea for treating severe uterine haemorrhage in adolescents with congenital aplastic anaemia; bleeding stopped within 2–4 days. |
| [21325445](https://pubmed.ncbi.nlm.nih.gov/21325445/) | 2011 | Long-term Follow-up | Ann Oncol | IBCSG Trial VIII long-term results: Confirmed sustained efficacy of goserelin-based ovarian suppression in premenopausal node-negative breast cancer. |

## Philippines Market Information

Goserelin is currently **not registered** in the Philippines. There are no active marketing authorizations on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| — | — | — | No registrations found |

> **Note:** Goserelin is marketed internationally under the brand name **Zoladex** (AstraZeneca) in subcutaneous depot implant formulations (3.6 mg and 10.8 mg). Philippines registration would be required before any clinical application.

## Cytotoxicity

| Item | Content |
|------|------|
| Cytotoxicity Classification | Hormonal / Endocrine therapy (GnRH agonist) — **not conventional cytotoxic** |
| Myelosuppression Risk | Low (goserelin is not myelosuppressive; it acts via hormonal suppression) |
| Emetogenicity Classification | Minimal (not associated with significant nausea/vomiting) |
| Monitoring Items | Serum estradiol/testosterone levels, bone mineral density (long-term use), lipid profile, blood glucose, menopausal symptoms assessment |
| Handling Protection | Standard handling; does **not** require cytotoxic drug handling precautions |

## Safety Considerations

> Please refer to the package insert for safety information. Detailed TFDA label warnings, contraindications, and drug interaction data are currently unavailable (data gap). International product labels (e.g., FDA, EMA) for Zoladex should be consulted.

**Known class-effect considerations for GnRH agonists (from international labels):**
- **Tumour flare:** Initial transient increase in sex hormones may cause symptom flare in the first 1–2 weeks
- **Bone mineral density:** Prolonged use associated with decreased BMD; duration of therapy should be considered
- **Cardiovascular risk:** QT prolongation and increased cardiovascular risk have been reported with androgen deprivation therapy
- **Injection site reactions:** Local reactions at subcutaneous depot injection site

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Goserelin's ability to induce amenorrhea is a direct, well-characterised pharmacological effect with Level 1 evidence — at least 3 completed Phase 3 RCTs (OPTION, SWOG S0230, and NCT02483767) have demonstrated this effect. The TxGNN prediction (99.99%) aligns perfectly with established clinical evidence. This represents a validated drug-disease relationship rather than a speculative repurposing candidate.

**To proceed, the following is needed:**
- Obtain Philippines FDA (PFDA) regulatory registration for goserelin (Zoladex)
- Secure detailed safety data: package insert warnings, contraindications, and drug-drug interactions from the PFDA or reference regulatory agencies
- Define the specific clinical context for amenorrhea induction (e.g., ovarian protection during chemotherapy, gynaecological conditions, or haematological indications)
- Establish a safety monitoring plan including bone mineral density surveillance for prolonged use
- Confirm route compatibility: subcutaneous depot implant availability and supply chain in the Philippines

---

*Disclaimer: This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

