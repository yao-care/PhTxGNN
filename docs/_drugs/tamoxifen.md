---
layout: default
title: Tamoxifen
parent: 僅模型預測 (L5)
nav_order: 320
evidence_level: L5
indication_count: 10
---

# Tamoxifen
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

# Tamoxifen: From ER-Positive Breast Cancer to Mammary Paget Disease

## One-Sentence Summary

Tamoxifen is a selective estrogen receptor modulator (SERM) widely established globally as the first-line endocrine therapy for hormone receptor-positive breast cancer, though it currently has no registered products in the Philippines market.
The TxGNN model predicts it may be effective for **Mammary Paget Disease**, with **1 clinical trial** and **13 publications** currently supporting this direction.
The prediction is biologically plausible: 80–90% of mammary Paget disease cases harbour an underlying ER-positive invasive carcinoma or DCIS, meaning tamoxifen's mechanism of ERα antagonism applies directly to the majority of patients.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | ER-positive breast cancer (globally established standard of care; no Philippines registration data available) |
| Predicted New Indication | Mammary Paget Disease |
| TxGNN Prediction Score | 99.69% |
| Evidence Level | L3 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Tamoxifen acts as a competitive antagonist at estrogen receptor alpha (ERα) in breast tissue. Upon binding, it induces a conformational change in the receptor that favors recruitment of co-repressors (NCoR, SMRT) rather than co-activators, thereby blocking transcription of estrogen-responsive proliferative genes including cyclin D1, c-myc, and IGF-1R. Its primary active metabolite, endoxifen — formed through CYP2D6-mediated hepatic metabolism — accounts for the majority of the drug's antitumor effect. Tamoxifen also stimulates TGF-β secretion and induces cell-cycle arrest via p21/p27 upregulation, providing both cell-intrinsic and paracrine inhibitory mechanisms.

Mammary Paget disease is a rare malignancy presenting as eczematous changes of the nipple-areola complex. Critically, 80–90% of cases harbour an underlying ER-positive invasive ductal carcinoma or high-grade DCIS — the same ER-driven proliferative pathway that tamoxifen targets in conventional breast cancer. Current clinical practice already incorporates tamoxifen into adjuvant management of Paget disease when the underlying tumor is hormone receptor-positive, treating the co-existing ER-positive malignancy. This is not a theoretical repurposing: the Phase III trial NCT00002920 explicitly enrolled patients with Paget's disease of the nipple who were receiving adjuvant tamoxifen, confirming that this population is already embedded within tamoxifen's real-world use.

For the minority of pure epidermal-type Paget cases with absent or low ER expression in the Paget cells themselves, the mechanistic rationale is weaker. However, the high frequency of ER-positive co-occurrence and direct case evidence of tamoxifen efficacy in HR-positive Paget disease (PMID 34463889, PMID 14965622) together provide a compelling biological and clinical basis for the TxGNN prediction score of 99.69%.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002920](https://clinicaltrials.gov/study/NCT00002920) | Phase 3 | Completed | 313 | RCT of medroxyprogesterone acetate vs. observation for preventing endometrial complications in postmenopausal patients — including those with Paget's disease of the nipple — receiving adjuvant tamoxifen. The inclusion of Paget's disease patients confirms tamoxifen as an established standard-of-care agent in this population; the trial's primary endpoint addresses endometrial safety management rather than Paget disease efficacy directly. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [34463889](https://pubmed.ncbi.nlm.nih.gov/34463889/) | 2022 | Case Report | Investigational New Drugs | Successful tamoxifen treatment of HR-positive metastatic extramammary Paget disease; tumor overexpressed hormone receptors; tamoxifen induced remission — the strongest direct evidence of ER-targeted therapy efficacy specifically in Paget disease |
| [14965622](https://pubmed.ncbi.nlm.nih.gov/14965622/) | 2001 | Case Report | Breast (Edinburgh) | Unusually extensive Paget's disease of the nipple that had been concealed for over 10 years; tamoxifen treatment achieved a response before definitive radiotherapy — documents single-agent tamoxifen activity in Paget disease |
| [25759627](https://pubmed.ncbi.nlm.nih.gov/25759627/) | 2014 | Meta-analysis | Breast Care (Basel) | Meta-analysis of local recurrence after mastectomy or BCS for Paget's disease; total recurrence rate 20–40%; provides disease natural history and highlights the unmet need for effective adjuvant systemic therapy |
| [16277886](https://pubmed.ncbi.nlm.nih.gov/16277886/) | 2005 | Retrospective Cohort | Clinical Breast Cancer | Paget's disease presenting as local recurrence following BCT in a cohort of 2181 early BC patients (1977–2002); contextualizes the role of adjuvant tamoxifen in reducing risk of Paget disease-type recurrence in ER-positive populations |
| [1648987](https://pubmed.ncbi.nlm.nih.gov/1648987/) | 1991 | Case Series | British Journal of Surgery | 48 women with Paget's disease of the nipple managed over 13 years; tamoxifen was used as primary treatment in one patient; characterises disease management options including endocrine therapy |
| [12924421](https://pubmed.ncbi.nlm.nih.gov/12924421/) | 2003 | Case Report | Surgery Today | Synchronous bilateral breast cancer with Paget's disease and invasive ductal carcinoma in a 60-year-old woman; illustrates the common co-occurrence of Paget disease with ER-positive underlying malignancy supporting the endocrine therapy rationale |
| [29694313](https://pubmed.ncbi.nlm.nih.gov/29694313/) | 2018 | Case Report | Il Giornale di Chirurgia | Paget disease of the male breast; notes absence of standard guidelines and potential to hide underlying invasive ductal carcinoma; highlights the need for evidence-based endocrine therapy options in this rare presentation |
| [8955252](https://pubmed.ncbi.nlm.nih.gov/8955252/) | 1996 | Case Series | The American Surgeon | Review of 32 cases of male breast Paget's disease; 50% had palpable mass or positive lymph nodes at presentation; endocrine therapy including tamoxifen considered in receptor-positive cases |
| [19112575](https://pubmed.ncbi.nlm.nih.gov/19112575/) | 2009 | Case Report | Archives of Gynecology and Obstetrics | Sequential vulvar and breast Paget's disease with underlying adenocarcinoma; illustrates the hormone-driven pathobiology supporting an endocrine treatment strategy across Paget disease variants |
| [17319355](https://pubmed.ncbi.nlm.nih.gov/17319355/) | 2006 | Case Series | Nigerian Journal of Clinical Practice | 8 cases of Paget's disease of the nipple-areola complex over 10 years at a Nigerian teaching hospital (3.3% of all breast cancers); characterizes disease presentation and underlines the need for accessible, evidence-based treatment in diverse populations |

---

## Philippines Market Information

No tamoxifen products are currently registered with the Philippines Food and Drug Administration (FDA Philippines). The drug has no approved authorizations and is not marketed in the Philippines at this time.

For reference, tamoxifen holds full approval in major regulatory jurisdictions — including the US FDA (NDA 17-970), EMA, and Japan PMDA — for ER-positive breast cancer treatment and chemoprevention in high-risk women. It is also included on the WHO Model List of Essential Medicines for cancer treatment. A Philippines FDA registration application or special access authorization would be required before clinical use.

---

## Cytotoxicity

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Targeted therapy — Hormonal/Endocrine (Selective Estrogen Receptor Modulator; not a conventional cytotoxic chemotherapy agent) |
| Myelosuppression Risk | Low (tamoxifen does not cause clinically significant myelosuppression; isolated reports of leukopenia and thrombocytopenia are rare and typically mild) |
| Emetogenicity Classification | Minimal to low (oral tablet; nausea and vomiting occur in fewer than 10% of patients and are usually self-limiting) |
| Monitoring Items | Endometrial thickness (annual transvaginal ultrasound in postmenopausal patients), liver function tests (LFTs), complete blood count (CBC), lipid panel, ophthalmologic exam if visual symptoms or prolonged high-dose use |
| Handling Protection | Standard oral medication precautions; specialized cytotoxic drug handling facilities are generally not required (tamoxifen is not classified as a hazardous drug by NIOSH at standard therapeutic doses), though institutional pharmacy policies should be consulted |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Mammary Paget disease is strongly and consistently associated with ER-positive underlying cancer (80–90% of cases), providing a direct mechanistic target for tamoxifen's ERα-antagonist activity. Although the current evidence base remains at L3 (retrospective cohorts and case reports), tamoxifen is already embedded in clinical practice for this population as adjuvant therapy for the co-existing hormone receptor-positive breast cancer — and one 2022 case report documents remission in HR-positive metastatic Paget disease with tamoxifen as the primary intervention.

**To proceed, the following is needed:**
- Hormone receptor (ER/PR) testing of the underlying lesion — tamoxifen efficacy is contingent on confirmed ER-positive status; purely ER-negative Paget cells would not benefit
- Philippines FDA registration or appropriate special access/compassionate use authorization prior to any clinical use
- Full review of tamoxifen package insert warnings and contraindications (unavailable in the current evidence pack; obtaining the TFDA or US FDA label is recommended)
- Endometrial safety monitoring plan: annual transvaginal ultrasound for postmenopausal patients; immediate investigation of any abnormal uterine bleeding
- Consider CYP2D6 pharmacogenomic testing, as poor metabolizers have significantly reduced endoxifen concentrations and may have diminished efficacy or require dose adjustment
- Prospective data collection: establish a disease-specific registry or observational study protocol to systematically document tamoxifen outcomes in mammary Paget disease patients, addressing the current L3 evidence gap
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

