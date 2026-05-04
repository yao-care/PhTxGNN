---
layout: default
title: Clofazimine
parent: 僅模型預測 (L5)
nav_order: 77
evidence_level: L5
indication_count: 3
---

# Clofazimine
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

# Clofazimine: From Leprosy/Drug-Resistant Tuberculosis to Pneumocystosis

## One-Sentence Summary

Clofazimine is a riminophenazine antibiotic used in the WHO multidrug therapy (MDT) regimen for leprosy and, more recently, in treatment regimens for drug-resistant tuberculosis (DR-TB). The TxGNN model predicts it may be effective for **Pneumocystosis** (Pneumocystis jirovecii pneumonia, PCP), with **1 clinical trial** and **4 publications** currently identified — however, the evidence is largely indirect, and the high prediction score most likely reflects shared epidemiological context in immunocompromised patients rather than direct pharmacological activity against Pneumocystis.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Leprosy (WHO MDT); Drug-resistant tuberculosis |
| Predicted New Indication | Pneumocystosis |
| TxGNN Prediction Score | 99.90% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the Evidence Pack. Based on known pharmacology, Clofazimine is a riminophenazine compound with broad antimicrobial activity. Its primary mechanism involves generating reactive oxygen species (ROS) and disrupting microbial cell membranes — properties that have been proposed to theoretically interfere with the metabolism of Pneumocystis jirovecii. This mechanistic rationale, however, remains entirely hypothetical; no dedicated in vitro or in vivo study has directly tested Clofazimine against P. jirovecii.

The more plausible explanation for the TxGNN model's high score (0.999) is epidemiological co-occurrence rather than pharmacological specificity. Both Pneumocystis jirovecii pneumonia (PCP) and Mycobacterium avium complex (MAC) infection are classic opportunistic infections in severely immunocompromised patients, particularly those with AIDS and CD4 counts below 100/mm³. Clofazimine is well-established for MAC prophylaxis and treatment in this population, and patients receiving Clofazimine for MAC frequently have concurrent or prior PCP — creating a strong statistical association in the knowledge graph without implying direct therapeutic activity against Pneumocystis.

Until dedicated preclinical studies demonstrate that Clofazimine inhibits P. jirovecii, the mechanistic link between this drug and pneumocystosis remains speculative. The existing standard of care for PCP (trimethoprim-sulfamethoxazole) is highly effective, further limiting the near-term clinical rationale for this repurposing direction.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00002058](https://clinicaltrials.gov/study/NCT00002058) | NA | Completed | N/A | Randomized controlled prophylaxis study evaluating Clofazimine to prevent disseminated MAC infection in HIV patients; subjects had prior Pneumocystis carinii pneumonia or CD4 ≤ 100/mm³. The trial targets MAC prevention, not pneumocystosis treatment. The subject inclusion criterion (prior PCP episode) demonstrates co-occurrence but provides no efficacy data for Clofazimine against Pneumocystis. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [8501340](https://pubmed.ncbi.nlm.nih.gov/8501340/) | 1993 | Clinical Study (Prophylaxis) | J Infect Dis | Randomized prospective trial of Clofazimine 50 mg/day for MAC prophylaxis in 110 HIV patients; eligibility required a prior PCP episode or CD4 ≤ 100/mm³. Confirms PCP–MAC co-occurrence in AIDS patients; Clofazimine was used for MAC, with no assessment of anti-PCP efficacy. |
| [2714863](https://pubmed.ncbi.nlm.nih.gov/2714863/) | 1989 | Case Report | Infection | AIDS patient with concurrent M. kansasii lung disease and PCP; treated with isoniazid, ethambutol, Clofazimine, and ciprofloxacin (for mycobacterial disease) plus TMP-SMX (for PCP). Clinical recovery occurred; Clofazimine's role was antimycobacterial, not anti-Pneumocystis. |
| [6299154](https://pubmed.ncbi.nlm.nih.gov/6299154/) | 1983 | Case Report | Ann Intern Med | Early AIDS case report of a hemophiliac patient presenting with PCP followed by disseminated M. avium-intracellulare. Describes co-occurrence of both infections; no Clofazimine therapy was reported in this case. |
| [11363899](https://pubmed.ncbi.nlm.nih.gov/11363899/) | 1996 | Review | PI Perspective | Opportunistic infections update covering PCP, MAC, and other AIDS-defining illnesses; documents disease context and treatment landscape without providing specific efficacy data for Clofazimine against Pneumocystis. |

---

## Philippines Market Information

Clofazimine currently has **no registered drug products** in the Philippines. There are no active FDA-Philippines authorizations on record.

> Note: Clofazimine is included in the WHO Model List of Essential Medicines and is available through the WHO Global Drug Facility primarily for leprosy elimination programs. Access in the Philippines would require sourcing through WHO/PNLA leprosy program channels or compassionate use provisions.

---

## Safety Considerations

Please refer to the package insert for safety information.

> All safety fields (key warnings, contraindications, and drug interaction data) were not available in the current Evidence Pack. Clofazimine is known from published pharmacology to carry risks including skin discoloration (orange-brown pigmentation), gastrointestinal adverse effects, and QTc prolongation — the latter being clinically significant when used in combination regimens. These should be confirmed from the official prescribing information before any use.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Despite a very high TxGNN model score (99.90%), the available evidence does not support direct clinical or preclinical efficacy of Clofazimine against Pneumocystis jirovecii. The single identified clinical trial targets MAC infection (not PCP), the literature reflects co-occurrence of these opportunistic infections in AIDS patients rather than any anti-Pneumocystis effect, and there is no mechanism-of-action data available to support a direct pharmacological link. An effective standard of care (TMP-SMX) already exists for PCP, further reducing the unmet need for this repurposing direction.

**To proceed, the following is needed:**

- **In vitro susceptibility testing**: Direct measurement of Clofazimine activity against P. jirovecii in cell-based or animal models
- **Mechanistic data**: Formal MOA profile from DrugBank or published pharmacology to assess whether Clofazimine's ROS-generating activity can plausibly target Pneumocystis
- **Clinical unmet need assessment**: Identification of patient subpopulations (e.g., TMP-SMX-intolerant or refractory cases) where a new treatment option would be meaningful
- **Safety data gap remediation**: Retrieval of Philippines FDA prescribing information and full contraindication/DDI profile, particularly QTc risk in immunocompromised patients
- **KG signal audit**: Investigation of whether the high TxGNN score is driven by direct drug–disease edges or by indirect epidemiological co-occurrence via immunocompromised host nodes, to determine whether model prediction is mechanistically meaningful
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

