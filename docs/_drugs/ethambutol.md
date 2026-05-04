---
layout: default
title: Ethambutol
parent: 僅模型預測 (L5)
nav_order: 130
evidence_level: L5
indication_count: 5
---

# Ethambutol
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

# Ethambutol: From Tuberculosis to Epiglottitis

## One-Sentence Summary

Ethambutol is a first-line bactericidal antibiotic and a core component of the standard HRZE regimen (isoniazid, rifampicin, pyrazinamide, ethambutol) used for treating tuberculosis.
The TxGNN model predicts it may be effective for **Epiglottitis**, with a prediction score of **99.90%**; however, only **2 case series/review publications** currently support this direction — and mechanistic analysis indicates utility is strictly limited to tuberculosis-related cases of epiglottitis, not common etiologies.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tuberculosis (first-line HRZE regimen) |
| Predicted New Indication | Epiglottitis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this Evidence Pack. Based on established pharmacology, Ethambutol belongs to the antimycobacterial drug class and exerts bacteriostatic/bactericidal effects by inhibiting EmbA/EmbB/EmbC arabinosyltransferases — enzymes unique to mycobacteria — thereby blocking arabinogalactan biosynthesis and destabilising the mycobacterial cell wall. This mechanism is specific to *Mycobacterium tuberculosis* and closely related species.

Epiglottitis caused by *M. tuberculosis* (i.e., supraglottic extension of laryngeal tuberculosis) is an extrapulmonary TB manifestation. In this narrow context, Ethambutol's application falls squarely within its existing TB indication rather than constituting true drug repurposing. The two supporting publications both describe laryngeal tuberculosis series in which the epiglottis was documented as an affected anatomical site, and patients received standard anti-TB regimens including Ethambutol.

Critically, the vast majority of epiglottitis cases are caused by *Haemophilus influenzae* type b, other gram-negative bacteria, or viruses — none of which harbour arabinogalactan in their cell walls. Ethambutol has no pharmacological activity against these pathogens. The high TxGNN score most likely reflects a non-specific graph association between Ethambutol's antimicrobial node and upper airway infection nodes (epiglottitis, laryngitis) in the knowledge graph, rather than a genuine biological rationale for repurposing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [14720571](https://pubmed.ncbi.nlm.nih.gov/14720571/) | 2004 | Case Series / Review | *The Lancet Infectious Diseases* | Reviews laryngeal tuberculosis presentations; the epiglottis is identified as one of the affected structures in laryngeal TB, providing contextual background for TB-related epiglottitis |
| [2806495](https://pubmed.ncbi.nlm.nih.gov/2806495/) | 1989 | Retrospective Case Series | *The European Respiratory Journal* | Reports 41 cases of laryngeal TB (1975–1985); epiglottis was among affected sites (along with vocal cords, false cords, and arytenoid region); patients were routinely treated with isoniazid, rifampicin, and ethambutol |

---

## Philippines Market Information

Ethambutol is currently not registered in the Philippines. No licensed products are on record with the Philippine FDA.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Complete warning, contraindication, and drug interaction data were not available in this Evidence Pack. A known clinical concern for Ethambutol is dose-dependent optic neuropathy (retrobulbar neuritis); baseline and periodic visual acuity monitoring is standard practice during treatment. Patients with renal impairment require dose adjustment due to reduced drug clearance.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Although TxGNN assigns a near-perfect prediction score, mechanistic review reveals that Ethambutol's spectrum of activity is restricted to mycobacterial pathogens. Epiglottitis caused by *M. tuberculosis* is already encompassed within Ethambutol's existing TB indication and does not represent a new repurposing opportunity; for common non-mycobacterial epiglottitis, there is no mechanistic basis or supporting evidence.

**To proceed, the following is needed:**

- **MOA confirmation**: Retrieve full mechanism of action details via DrugBank API (DB00330) to formally document the arabinosyltransferase inhibition target
- **Safety data**: Download and parse the Philippine FDA package insert (or equivalent approved labeling) to capture full warnings, contraindications, and drug interactions — currently all marked as data gaps
- **Epidemiological context**: Assess the local prevalence of TB-related laryngeal/epiglottic disease in the Philippines to determine whether this clinical scenario is relevant in practice
- **Primary registration pathway**: Evaluate whether Ethambutol can be registered in the Philippines for its established TB indication before any repurposing discussion proceeds
- **Alternate indication review**: Consider shifting focus to **Laryngitis (rank 2, L3 evidence)** or **Tuberculous Peritonitis (rank 4, L3 evidence)** — both have stronger mechanistic grounding and more supporting literature within the same TB-treatment paradigm
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

