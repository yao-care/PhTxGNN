---
layout: default
title: Flutamide
parent: 僅模型預測 (L5)
nav_order: 151
evidence_level: L5
indication_count: 10
---

# Flutamide
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

# Flutamide: From Prostate Cancer to Male Reproductive Organ Cancer

## One-Sentence Summary

Flutamide is a non-steroidal antiandrogen established globally for prostate cancer treatment, operating by competitively blocking the androgen receptor (AR) to suppress androgen-driven tumor growth — though it currently carries **no registration in the Philippines**.
The TxGNN model predicts it may be effective for **Male Reproductive Organ Cancer** (rank 6, score 99.98%), with **over 50 clinical trials** and **20 publications** supporting this direction.
This evidence base — anchored by multiple completed Phase 3 RCTs — qualifies as **Evidence Level L1**, making it the strongest actionable prediction from this analysis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Prostate cancer (established global use; no Philippines registration on record) |
| Predicted New Indication | Male Reproductive Organ Cancer |
| TxGNN Prediction Score | 99.98% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Flutamide is a non-steroidal antiandrogen that acts as a competitive antagonist at the androgen receptor (AR). It prevents testosterone and dihydrotestosterone (DHT) from binding to AR, thereby blocking the downstream gene transcription programs that drive prostate cell proliferation and survival. When combined with a LHRH agonist, Flutamide achieves maximal androgen blockade — reducing PSA levels, shrinking tumor volume, and delaying disease progression. This mechanism is direct and well-characterized (PMID 8252497).

Prostate adenocarcinoma — the dominant cancer within the "male reproductive organ cancer" category — is driven primarily by AR signaling, making AR blockade a cornerstone of its treatment. Flutamide was among the first antiandrogens validated in large Phase 3 trials, both as monotherapy (for potency-sparing treatment in early-stage disease) and as part of combined androgen blockade (CAB) with LHRH agonists in advanced settings. The connection between Flutamide's mechanism and male reproductive organ cancer is therefore direct, biologically sound, and clinically proven.

While second-generation antiandrogens such as enzalutamide and apalutamide have shown superiority in certain settings (e.g., castration-resistant prostate cancer), Flutamide remains a clinically validated and accessible option with decades of safety and efficacy data. Its complete absence from the Philippine market represents a tangible gap in antiandrogen availability, particularly for patients who cannot access or afford newer agents.

> **Note on TxGNN Top-Ranked Prediction**: The model's highest-ranked prediction (rank 1) is "prostate cancer/brain cancer susceptibility" — a genetic predisposition phenotype, not a directly treatable disease entity. This likely reflects ontology-level node proximity in the knowledge graph rather than a genuine therapeutic target. Similarly, rank 2 (fibroma of prostate), rank 3 (Brenner tumor), rank 5 (prostate leiomyoma), and rank 7 (benign prostate phyllodes tumor) all carry L5 evidence (Hold) and represent KG proximity artifacts. The most clinically actionable prediction is **rank 6 (Male Reproductive Organ Cancer)**, which has L1-level evidence and is the focus of this report.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00450463](https://clinicaltrials.gov/study/NCT00450463) | Phase 2 | Completed | 64 | Head-to-head comparison of PROSTVAC/TRICOM vaccine + Flutamide vs. **Flutamide alone** in androgen-insensitive non-metastatic prostate cancer — directly evaluates Flutamide monotherapy efficacy and its combination potential with immunotherapy |
| [NCT00006214](https://clinicaltrials.gov/study/NCT00006214) | Phase 2 | Completed | 63 | **Flutamide as the primary intervention** for chemoprevention in patients with high-grade prostatic intraepithelial neoplasia (HGPIN) — directly evaluates Flutamide's ability to prevent prostate cancer progression from precancerous lesions |
| [NCT02918968](https://clinicaltrials.gov/study/NCT02918968) | Phase 4 | Completed | 206 | Enzalutamide vs. **Flutamide** + ADT in CRPC patients who failed bicalutamide + ADT — head-to-head comparison positioning Flutamide in the contemporary antiandrogen sequence |
| [NCT00002597](https://clinicaltrials.gov/study/NCT00002597) | Phase 3 | Completed | 2,028 | Endocrine therapy (Flutamide + goserelin/leuprolide) as cytoreductive agent prior to RT vs. RT alone in good-prognosis localized prostate cancer — largest trial in dataset, validates ADT before radiotherapy |
| [NCT00936390](https://clinicaltrials.gov/study/NCT00936390) | Phase 3 | Completed | 1,538 | Dose-escalated RT ± short-term androgen deprivation for intermediate-risk prostate cancer — validates role of short-term Flutamide-containing ADT combined with modern radiotherapy |
| [NCT00055731](https://clinicaltrials.gov/study/NCT00055731) | Phase 3 | Completed | 413 | Adjuvant hormonal therapy (including Flutamide) ± docetaxel/estramustine in advanced prostate cancer — evaluates whether adding chemotherapy to Flutamide-based ADT improves outcomes |
| [NCT00288080](https://clinicaltrials.gov/study/NCT00288080) | Phase 3 | Completed | 612 | Androgen suppression + 3DCRT/IMRT vs. same + docetaxel/prednisone for high-risk prostate cancer — Flutamide as the foundation of the androgen suppression arm |
| [NCT00116220](https://clinicaltrials.gov/study/NCT00116220) | Phase 3 | Completed | 206 | External beam RT ± total androgen suppression (including Flutamide) for high-risk localized prostate cancer — confirms necessity of ADT in high-risk disease management |
| [NCT00767286](https://clinicaltrials.gov/study/NCT00767286) | Phase 3 | Completed | N/A | Long-term total androgen suppression post-neoadjuvant cytoreduction and radiotherapy in locally advanced prostate cancer — validates Flutamide-containing ADT duration strategy |
| [NCT00002855](https://clinicaltrials.gov/study/NCT00002855) | Phase 3 | Completed | 306 | Androgen ablation alone vs. combined chemo/hormonal therapy as initial treatment of unresectable/metastatic prostate cancer — tests Flutamide-based ADT as backbone for combination strategies |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8252497](https://pubmed.ncbi.nlm.nih.gov/8252497/) | 1993 | Mechanistic | *Cancer* | Foundational MOA paper: establishes Flutamide as a pure AR antagonist; demonstrates maximal prostate cancer inhibition is achieved by combining LHRH agonist + Flutamide — defines the combined androgen blockade rationale |
| [21751904](https://pubmed.ncbi.nlm.nih.gov/21751904/) | 2011 | RCT | *N Engl J Med* | RTOG 9408 landmark trial: RT + short-term ADT (Flutamide-containing) vs. RT alone — short-term ADT significantly improves 10-year overall survival in localized prostate cancer |
| [8650871](https://pubmed.ncbi.nlm.nih.gov/8650871/) | 1996 | Clinical Study | *Urology* | TRUS-measured prostate volume reduction with Flutamide ± castration in previously untreated prostate cancer — provides objective tumor response data supporting clinical efficacy |
| [11295624](https://pubmed.ncbi.nlm.nih.gov/11295624/) | 2001 | Review | *Urology* | Summarizes the chemoprevention role of Flutamide in high-grade PIN — clinical rationale for using Flutamide to prevent progression from precancerous prostate lesions to frank carcinoma |
| [3367673](https://pubmed.ncbi.nlm.nih.gov/3367673/) | 1988 | Clinical Study | *Med Oncol Tumor Pharmacother* | Flutamide monotherapy in 10 T3M0 prostate cancer patients with potency preservation; 8 metastasis-free tumors remained stable over 3–48 months — demonstrates antiandrogen monotherapy viability |
| [3157927](https://pubmed.ncbi.nlm.nih.gov/3157927/) | 1985 | Clinical Study | *The Prostate* | D-Trp-6-LH-RH microcapsule + Flutamide in Dunning R-3327H rat prostate cancer model — validates combined androgen blockade concept in vivo and supports long-acting formulation development |
| [3071951](https://pubmed.ncbi.nlm.nih.gov/3071951/) | 1988 | Review | *Am J Clin Oncol* | Clinical rationale for combining antiandrogens (Flutamide) with LH-RH analogues in prostate cancer — defines the complete androgen blockade (CAB) framework used in clinical practice for decades |
| [65117](https://pubmed.ncbi.nlm.nih.gov/65117/) | 1976 | Review | *Adv Sex Horm Res* | Foundational antiandrogen review documenting the biological mechanisms of AR blockade, including the early characterization of Flutamide as a non-steroidal antiandrogen |
| [24950779](https://pubmed.ncbi.nlm.nih.gov/24950779/) | 2014 | Translational | *Cancer Prev Res* | Phase II study of Flutamide in women at high-risk for ovarian cancer — androgen ablation reduces serous ovarian tumor burden 24-fold in male mice; identifies AR pathway as a broader cancer target beyond prostate |
| [37919464](https://pubmed.ncbi.nlm.nih.gov/37919464/) | 2023 | In vitro | *Sci Rep* | Ganoderma lucidum polysaccharide sensitizes prostate cancer cells to Flutamide and docetaxel — contemporary combination therapy research demonstrating Flutamide's continued relevance in preclinical models |

---

## Philippines Market Information

Flutamide currently has **no active registrations** with the Philippine FDA. No product licenses, approved dosage forms, or market authorizations are on file (total licenses = 0).

This represents a significant unmet clinical need: prostate cancer patients in the Philippines currently lack access to this well-validated antiandrogen, while multiple internationally approved formulations (oral tablet, 250 mg) have been available in other markets for decades.

---

## Cytotoxicity

Flutamide is used in the treatment of prostate cancer (an antineoplastic context) but is classified as a **non-cytotoxic targeted therapy** — it does not damage DNA or directly kill dividing cells.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Non-cytotoxic targeted therapy — Non-steroidal antiandrogen (AR competitive antagonist); not a conventional cytotoxic or alkylating agent |
| Myelosuppression Risk | Low — AR blockade does not directly suppress hematopoiesis; myelosuppression is not a primary adverse effect of Flutamide |
| Emetogenicity Classification | Low |
| Monitoring Items | Liver function tests (LFTs) at baseline and periodically during therapy — hepatotoxicity (including rare fatal hepatic failure) is the primary safety concern; CBC if used within combination chemotherapy regimens |
| Handling Protection | Standard oral medication handling; special cytotoxic drug handling precautions are not required |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 3 RCTs — including large trials with enrollment exceeding 1,500 patients — confirm the efficacy of Flutamide-containing androgen deprivation therapy in prostate cancer (male reproductive organ cancer), establishing the highest possible evidence level (L1). The drug's complete absence from the Philippine market represents a validated and actionable clinical gap that can be addressed through regulatory registration.

**To proceed, the following is needed:**
- **Safety data gap (Blocking):** Obtain and parse the package insert or international SPC (e.g., from FDA USA or EMA) to complete the safety profile — warnings, contraindications, and hepatotoxicity risk management protocols
- **MOA data gap (High):** Confirm mechanism of action via DrugBank API query (currently flagged as Data Gap)
- **DDI assessment:** Complete a drug-drug interaction screening for Flutamide against common Philippine concomitant medications (e.g., warfarin interaction is clinically significant)
- **Regulatory pathway:** Determine whether Philippine FDA registration can proceed based on international approvals (FDA USA/EMA) or requires local bridging study data
- **Formulary positioning:** Assess whether bicalutamide or newer antiandrogens (enzalutamide, apalutamide) are already registered in the Philippines, to clarify Flutamide's role in the local treatment landscape
- **Cost-effectiveness analysis:** Evaluate patient access, pricing strategy, and supply chain feasibility for oral tablet formulation in the Philippine oncology setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

