---
layout: default
title: Interferon Alfa
parent: 僅模型預測 (L5)
nav_order: 175
evidence_level: L5
indication_count: 10
---

# Interferon Alfa
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

Using the `txgnn-pipeline` skill to confirm context — this is a PhTxGNN report. Now generating the evaluation report from the Evidence Pack.

---

# Interferon Alfa: From Viral Hepatitis & Oncology to Heart Disease

## One-Sentence Summary

Interferon alfa is a recombinant cytokine with established international use in chronic viral hepatitis (HBV/HCV), select malignancies (melanoma, renal cell carcinoma), and myeloproliferative neoplasms (polycythemia vera) — though it holds **no current registration in the Philippines**.
The TxGNN model predicts it may have therapeutic relevance in **Heart Disease**, supported by **34 clinical trials retrieved** and **20 publications** identified.
However, direct clinical evidence linking Interferon alfa to heart disease treatment is limited and mechanistically contradictory, yielding an **L4 evidence level** and a **Hold** recommendation.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines registration; internationally used for viral hepatitis (HBV/HCV), melanoma, and polycythemia vera |
| Predicted New Indication | Heart Disease |
| TxGNN Prediction Score | 99.999% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacology, Interferon alfa is a type I cytokine that activates innate and adaptive immunity through the canonical IFNAR → JAK1/TYK2 → STAT1/STAT2 → interferon-stimulated gene (ISG) pathway. Its established therapeutic effects span antiviral defence (suppression of HBV/HCV replication), anti-tumour immunomodulation (melanoma, renal cell carcinoma), and reduction of clonal haematopoiesis burden in myeloproliferative neoplasms.

The mechanistic bridge to heart disease is indirect but biologically plausible in two narrow contexts. First, IFN alfa suppresses eosinophil-driven tissue damage: hypereosinophilic syndrome (HES) frequently causes eosinophilic myocarditis with endomyocardial fibrosis, and IFN alfa has documented activity in HES (PMID 17848188, 35470096, 29173361). Second, Erdheim-Chester disease — a rare histiocytosis for which IFN alfa is an established first-line treatment — commonly features cardiac infiltration that can be life-threatening (PMID 34911328). These niche immune-mediated pathways most likely account for the TxGNN model's near-perfect score.

A critical safety counterweight tempers this prediction. PMID 29106401 (King et al., *Nature Medicine*, 2017) demonstrates that IRF3 activation and type I interferon production in macrophages **fuel a fatal inflammatory cascade following myocardial infarction** in animal models. This directly conflicts with any proposed use of IFN alfa in ischaemic or structural heart disease. The prediction is therefore mechanistically plausible only in the sub-population with immune-mediated cardiac disease, and potentially harmful in the far larger population with ischaemic heart disease.

---

## Clinical Trial Evidence

No trials directly investigated Interferon alfa as a treatment for heart disease. The two Grade B trials offer only indirect relevance; all others are Grade C.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00569127](https://clinicaltrials.gov/study/NCT00569127) | Phase 3 | Active, Not Recruiting | 427 | Depot Octreotide + IFN alfa-2b vs Octreotide + Bevacizumab in advanced metastatic carcinoid tumours; carcinoid heart disease (Hedinger syndrome) is a known complication of carcinoid and may appear as a secondary endpoint |
| [NCT05837143](https://clinicaltrials.gov/study/NCT05837143) | Early Phase 1 | Active, Not Recruiting | 12 | AAV9-cTnT-modTERT (JV001) gene therapy for dilated cardiomyopathy; IFN alfa is not the investigational agent but potential IFN-related pathway crosstalk is noted |
| [NCT00002657](https://clinicaltrials.gov/study/NCT00002657) | Phase 2 | Completed | 20 | Reduced immunosuppression, IFN alfa, and ProMACE-CytaBOM for post-cardiac-transplant lymphoproliferation; cardiac transplant setting with IFN alfa as immunomodulator |
| [NCT00072046](https://clinicaltrials.gov/study/NCT00072046) | Phase 3 | Completed | 732 | IFN alfa-2b ± Bevacizumab in advanced renal cell carcinoma; large completed Phase III confirming IFN alfa activity; cardiac outcomes not a primary endpoint |
| [NCT00001379](https://clinicaltrials.gov/study/NCT00001379) | Phase 2 | Completed | 94 | Alpha-interferon in lymphomatoid granulomatosis (LYG), a destructive lymphoproliferative disease that may involve lungs and other organs; IFN alfa as primary agent |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [35007321](https://pubmed.ncbi.nlm.nih.gov/35007321/) | 2022 | RCT Phase 3 | *Blood* | Pegylated IFN-α vs hydroxyurea in high-risk PV/ET: IFN-α reduces thrombotic events by normalising blood counts — indirectly relevant to cardiovascular risk reduction |
| [29173361](https://pubmed.ncbi.nlm.nih.gov/29173361/) | 2017 | Review | *Am J Med Sci* | Eosinophilic myocarditis in HES: systemic treatment (including IFN alfa) is required when eosinophilia causes cardiac infiltration and necrosis |
| [29106401](https://pubmed.ncbi.nlm.nih.gov/29106401/) | 2017 | Translational | *Nature Medicine* | **⚠ Safety signal**: IRF3 and type I IFNs drive lethal macrophage-mediated inflammation after myocardial infarction in mice — major mechanistic concern for ischaemic heart disease |
| [35470096](https://pubmed.ncbi.nlm.nih.gov/35470096/) | 2022 | Review | *J Allergy Clin Immunol Pract* | HES variants and treatment: IFN alfa listed as a cytoreductive option for lymphocytic and idiopathic HES variants with end-organ (cardiac) involvement |
| [33217613](https://pubmed.ncbi.nlm.nih.gov/33217613/) | 2021 | Case Series | *J Allergy Clin Immunol Pract* | SAVI (STING-associated vasculopathy): gain-of-function STING mutations drive type I IFN overproduction causing systemic vasculopathy — illustrates how uncontrolled IFN signalling damages vascular tissue |
| [34911328](https://pubmed.ncbi.nlm.nih.gov/34911328/) | 2021 | Review | *Klin Onkol* | Erdheim-Chester disease: IFN alfa as first-line therapy; cardiac infiltration is a life-threatening feature — one of the strongest indirect cases for IFN alfa in cardiac disease |
| [17848188](https://pubmed.ncbi.nlm.nih.gov/17848188/) | 2007 | Review | *Orphanet J Rare Dis* | Hypereosinophilic syndromes: IFN alfa efficacy in HES-associated eosinophil-driven organ damage including myocardial involvement |
| [30135585](https://pubmed.ncbi.nlm.nih.gov/30135585/) | 2018 | Basic Science | *Nature* | Parkin/PINK1 suppress STING-mediated type I IFN in mitochondrial damage — mechanistic link between mitochondrial stress, IFN signalling, and cardiac-relevant inflammation |
| [39953063](https://pubmed.ncbi.nlm.nih.gov/39953063/) | 2025 | Basic Science | *Nat Commun* | IFN-α-inducible gene Ifi27l2a significantly upregulated in aged microglia after ischaemic stroke — highlights IFN pathway activation in acute ischaemic contexts |
| [37761959](https://pubmed.ncbi.nlm.nih.gov/37761959/) | 2023 | Animal Study | *Genes* | Dp16 (Down syndrome) mouse model: baseline IFN pathway gene expression differences in heart tissue — contextual IFN biology in cardiac gene expression |

---

## Philippines Market Information

Interferon alfa (DrugBank: DB05258) is currently **not registered** in the Philippines. No product authorisations are on record in the regulatory database.

---

## Safety Considerations

No safety data (key warnings, contraindications, or drug interactions) are available in the current Evidence Pack. Based on evidence retrieved in the literature review, the following class-level concerns are relevant to any cardiac repurposing evaluation:

- **Potential harm in ischaemic heart disease**: Type I IFN and IRF3 activation has been shown to amplify post-MI macrophage inflammation and worsen outcomes in preclinical models (PMID 29106401). This constitutes a mechanistic contraindication for the largest sub-population of heart disease patients.
- **IFN-induced autoimmune and vascular effects**: SAVI data (PMID 33217613) illustrates that sustained type I IFN signalling can cause systemic vasculopathy, which is directly adverse in cardiac patients.
- **General IFN alfa class effects** from published literature include: constitutional flu-like syndrome, myelosuppression (neutropenia, thrombocytopenia), neuropsychiatric effects (depression, suicidality), autoimmune thyroiditis, and hepatotoxicity.

Please refer to the package insert for complete safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a near-perfect TxGNN score (99.999%), the predicted indication "heart disease" is too broad to be actionable, and existing mechanistic evidence is **contradictory**: IFN alfa has indirect therapeutic relevance only in immune-mediated cardiac conditions (HES-associated eosinophilic myocarditis, Erdheim-Chester disease with cardiac involvement), while published translational data signals it may be actively harmful in the far more prevalent ischaemic and structural heart disease settings. No direct clinical trial supports this repurposing.

**To proceed, the following is needed:**

- **Disease sub-type refinement**: Narrow the target indication from "heart disease" to a specific immune-mediated cardiac condition — e.g., HES-associated eosinophilic myocarditis or Erdheim-Chester disease with cardiac infiltration — where the mechanistic benefit-risk profile is favourable
- **MOA data from DrugBank**: Detailed mechanism of action to confirm IFN alfa's downstream effects in the cardiac immune microenvironment
- **Full safety review**: Obtain and parse the package insert (international regulatory sources: EMA/US FDA SmPC) for complete warnings, contraindications, and cardiac-specific precautions
- **Drug-drug interaction data**: No DDI data was retrievable; this is a gap for any cardiac population that is typically on multiple medications
- **Focused literature search**: Targeted PubMed search on "interferon alfa" AND ("eosinophilic myocarditis" OR "Erdheim-Chester" OR "carcinoid heart disease") to quantify direct cardiac evidence before any clinical development decision
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

