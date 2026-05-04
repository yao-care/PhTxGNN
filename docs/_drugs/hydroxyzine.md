---
layout: default
title: Hydroxyzine
parent: 僅模型預測 (L5)
nav_order: 167
evidence_level: L5
indication_count: 5
---

# Hydroxyzine
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

# Hydroxyzine: From Antihistamine/Anxiolytic to Allergic Urticaria

## One-Sentence Summary

Hydroxyzine is a first-generation H1-antihistamine, globally approved for anxiety, pruritus, and urticaria in numerous countries, but currently not marketed in the Philippines.
The TxGNN model predicts it may be effective for **Allergic Urticaria**,
with **1 clinical trial** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Not registered in Philippines (globally approved for: anxiety, pruritus, urticaria) |
| Predicted New Indication | Allergic Urticaria |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Hydroxyzine is a first-generation H1-receptor antagonist (piperazine derivative) that directly blocks histamine-mediated responses, including increased vascular permeability, pruritus, and wheal formation — the hallmark symptoms of allergic urticaria. Although detailed MOA data was not available in this evidence pack, hydroxyzine's mechanism is well-established in global pharmacological literature: it competitively inhibits histamine binding at H1 receptors on smooth muscle, endothelium, and sensory nerve endings, thereby suppressing the immediate allergic reaction cascade.

The relationship between hydroxyzine and allergic urticaria is, in fact, one of the most direct drug–disease relationships in pharmacology. Allergic urticaria is fundamentally a histamine-driven process where mast cell degranulation releases histamine into the skin, causing the characteristic wheals and flares. Hydroxyzine's H1-blocking action directly addresses this core pathophysiology. Notably, cetirizine — hydroxyzine's principal active metabolite — is one of the most widely prescribed second-generation antihistamines for urticaria worldwide, indirectly validating the parent drug's efficacy.

It is worth noting that hydroxyzine is already approved for urticaria in many countries (including the US, EU, Japan, and Taiwan). The TxGNN prediction is therefore essentially confirming a well-established clinical use. The main significance of this finding is for the Philippines market, where hydroxyzine is not currently registered, suggesting a potential regulatory and market opportunity.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT02023164](https://clinicaltrials.gov/study/NCT02023164) | Phase 3 | Completed | 36 | Pilot study comparing IV cetirizine (hydroxyzine's active metabolite) vs. IV diphenhydramine for acute urticaria in emergency settings. Relevance to hydroxyzine is indirect (metabolite relationship) with small sample size. |

> **Note:** While only 1 registered clinical trial was identified through the direct search, the limited trial count reflects the fact that hydroxyzine's efficacy in urticaria is already well-established globally and predates the modern clinical trial registry system. The extensive literature evidence below compensates for this gap.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31582993](https://pubmed.ncbi.nlm.nih.gov/31582993/) | 2019 | Position Statement | Allergy Asthma Clin Immunol | CSACI position statement: Directly names hydroxyzine as a first-generation antihistamine used for urticaria; recommends newer-generation H1-antihistamines as first-line due to better safety profile. |
| [28913986](https://pubmed.ncbi.nlm.nih.gov/28913986/) | 2017 | Review | Allergy Asthma Immunol Res | Chronic spontaneous urticaria treatment begins with antihistamines; hydroxyzine/diphenhydramine historically used up to 4× daily. Omalizumab recommended if high-dose antihistamines fail. |
| [1981354](https://pubmed.ncbi.nlm.nih.gov/1981354/) | 1990 | Systematic Review | Drugs | Cetirizine (carboxylated metabolite of hydroxyzine) is a potent H1-antagonist; effective in chronic urticaria at 10 mg daily with minimal CNS depression. Validates parent drug mechanism. |
| [16278258](https://pubmed.ncbi.nlm.nih.gov/16278258/) | 2005 | Review | Ann Pharmacother | Reviews first- and newer-generation antihistamines for allergic rhinitis and chronic idiopathic urticaria management in pharmacy settings. |
| [22994340](https://pubmed.ncbi.nlm.nih.gov/22994340/) | 2012 | Review | Clin Exp Allergy | Discusses predicting best H1-antihistamine for urticaria patients; compares efficacy of available agents for chronic spontaneous urticaria. |
| [7645679](https://pubmed.ncbi.nlm.nih.gov/7645679/) | 1995 | Clinical Review | Allergy | Clinical studies with cetirizine in allergic rhinitis and chronic urticaria, relevant to hydroxyzine as parent compound. |
| [12113226](https://pubmed.ncbi.nlm.nih.gov/12113226/) | 2002 | Review | Clin Allergy Immunol | H1-antihistamines in children: Level 1 evidence for efficacy in allergic conditions; discusses pediatric urticaria management. |
| [21793329](https://pubmed.ncbi.nlm.nih.gov/21793329/) | 2010 | Observational Study | Chin J Physiol | Open-label multicentre study of levocetirizine for urticaria in Taiwanese patients (n=333); demonstrates regional applicability of hydroxyzine-derived antihistamines. |
| [18336052](https://pubmed.ncbi.nlm.nih.gov/18336052/) | 2008 | PK/PD Review | Clin Pharmacokinet | Comparative pharmacokinetics of second-generation antihistamines (desloratadine, fexofenadine, levocetirizine) in allergic rhinitis and chronic idiopathic urticaria. |
| [11034010](https://pubmed.ncbi.nlm.nih.gov/11034010/) | 2000 | Case Report | J Clin Gastroenterol | Reports cetirizine-induced cholestasis; notes cetirizine (hydroxyzine metabolite) is approved for seasonal/perennial allergic rhinitis and chronic urticaria. Safety signal for metabolite. |

---

## Philippines Market Information

Hydroxyzine currently has **no registered products** in the Philippines (FDA Philippines). There are no authorization records available.

> This represents a potential market entry opportunity if regulatory submission is pursued. Hydroxyzine is widely available in other markets (US, EU, Japan, Taiwan) under various brand names including Atarax® and Vistaril®.

---

## Safety Considerations

> Please refer to the package insert for safety information. Key safety data (warnings, contraindications, drug interactions) were not available in the current evidence pack.

**General pharmacological cautions for hydroxyzine (based on global labelling):**
- First-generation antihistamines are associated with sedation, cognitive impairment, and anticholinergic effects (dry mouth, urinary retention, blurred vision)
- The CSACI position statement (PMID 31582993) notes that first-generation H1-antihistamines including hydroxyzine have been associated with accidents, overdose deaths, and sudden cardiac death
- QT prolongation has been reported; caution with concomitant QT-prolonging medications
- Newer-generation antihistamines (e.g., cetirizine, levocetirizine) are recommended as first-line over hydroxyzine due to superior safety profile

---

## Additional Predicted Indications

The TxGNN model also predicted the following indications for hydroxyzine:

| Rank | Predicted Indication | TxGNN Score | Evidence Level | Recommendation |
|------|---------------------|-------------|----------------|----------------|
| 2 | Rosacea Conjunctivitis | 99.70% | L5 | Hold |
| 3 | Cold Urticaria | 99.66% | L2 | Proceed with Guardrails |
| 4 | Recalcitrant Atopic Dermatitis | 99.36% | L4 | Research Question |
| 5 | IgE Responsiveness, Atopic | 99.27% | L5 | Hold |

**Notable — Cold Urticaria (Rank 3):** This prediction is strongly supported by evidence, including 1 completed Phase 4 clinical trial ([NCT01940393](https://clinicaltrials.gov/study/NCT01940393), n=150) and 20 publications. A head-to-head comparative trial (PMID [6480953](https://pubmed.ncbi.nlm.nih.gov/6480953/)) directly evaluated hydroxyzine against other antihistamines for idiopathic cold urticaria. Cold urticaria is triggered by cold-induced mast cell degranulation releasing histamine, making hydroxyzine's H1-blocking mechanism directly applicable. Another study (PMID [475987](https://pubmed.ncbi.nlm.nih.gov/475987/)) specifically demonstrated hydroxyzine plus cimetidine significantly suppressed cold urticaria erythema (p=0.01).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Hydroxyzine is a well-established H1-antihistamine whose efficacy in allergic urticaria has been validated globally for decades. The TxGNN prediction confirms a clinically proven drug–disease relationship. The primary barrier is not evidence of efficacy but rather the absence of Philippine market registration. The recommendation to proceed "with guardrails" reflects the need to address safety data gaps (package insert warnings, contraindications) and the current global preference shift toward second-generation antihistamines (cetirizine, levocetirizine) with better safety profiles.

**To proceed, the following is needed:**
- Obtain complete package insert data including warnings, contraindications, and drug interactions (from TFDA or FDA reference)
- Detailed mechanism of action documentation from DrugBank
- Regulatory pathway assessment for Philippines FDA registration
- Head-to-head comparison data: hydroxyzine vs. second-generation antihistamines (cetirizine, levocetirizine) for urticaria, to justify positioning of a first-generation agent
- Safety monitoring plan addressing sedation, QT prolongation risk, and anticholinergic effects in the target population
- Consider whether cetirizine (hydroxyzine's active metabolite, with superior safety) would be a more suitable candidate for Philippines market entry
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

