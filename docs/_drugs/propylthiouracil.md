---
layout: default
title: Propylthiouracil
parent: 僅模型預測 (L5)
nav_order: 186
evidence_level: L5
indication_count: 3
---

# Propylthiouracil
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

# Propylthiouracil: From Hyperthyroidism to Resistance to Thyroid Hormone (THRβ Mutation)

## One-Sentence Summary

Propylthiouracil (PTU) is a thionamide-class antithyroid drug classically used to treat hyperthyroidism and Graves' disease by suppressing thyroid hormone synthesis.
The TxGNN model predicts it may be applicable to **resistance to thyroid hormone due to a mutation in thyroid hormone receptor beta (RTHβ)**,
currently supported by **no registered clinical trials** and **6 publications** — all of which are tier-3 (case reports, animal studies, and basic research).

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperthyroidism / Graves' disease (inferred from pharmacological class; Philippines regulatory record unavailable) |
| Predicted New Indication | Resistance to thyroid hormone due to THRβ mutation (RTHβ) |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 (Preclinical / mechanistic studies only) |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data is not currently available in the evidence pack. Based on established pharmacological knowledge, propylthiouracil (PTU) is a thionamide antithyroid agent that exerts its effect through two main pathways: (1) inhibiting thyroid peroxidase (TPO), thereby blocking the organification of iodide and blocking de novo synthesis of thyroid hormones T3 and T4; and (2) inhibiting peripheral conversion of T4 to the biologically more active T3 by blocking deiodinase activity — an advantage over methimazole that is particularly relevant in acute thyrotoxic states.

RTHβ is a dominantly inherited syndrome caused by point mutations in the *THRB* gene. The mutant THRβ protein acts as a dominant negative, impairing the responsiveness of target tissues to thyroid hormone. Critically, this is a **receptor-level defect**, not a problem of hormone overproduction. Circulating T3/T4 levels may be elevated as a compensatory response to tissue-level insensitivity, with TSH failing to be fully suppressed (particularly at the pituitary level). This makes RTHβ pathophysiologically distinct from classic hyperthyroidism.

There is a theoretical basis for using PTU: by lowering circulating T3/T4 concentrations, it could reduce hormone-driven symptoms in peripheral tissues (e.g., tachycardia, bone loss) where thyrotoxicosis is clinically manifest. However, a critical limitation exists — because the pituitary also harbours the THRβ mutation in most RTHβ cases, reducing T3/T4 does not suppress TSH. Compensatory TSH elevation may further stimulate thyroid growth and potentially promote malignant transformation, as suggested by the animal model evidence (PMID 22919057). The mechanistic link is biologically plausible but subject to significant disease-specific constraints, making this an indirect and potentially harmful application.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for PTU in RTHβ.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [18561095](https://pubmed.ncbi.nlm.nih.gov/18561095/) | 2009 | Case Series / Family Study | Exp Clin Endocrinol Diabetes | Reports a Turkish mother-son pair with RTHβ (P453A THRB mutation); describes clinical presentation and thyroid function test patterns consistent with receptor resistance |
| [14684607](https://pubmed.ncbi.nlm.nih.gov/14684607/) | 2004 | Basic Research | Endocrinology | Mouse knock-in model demonstrating that mutant THRβ (Δ337T) exerts dominant-negative effects in cardiac tissue; establishes mechanistic basis for cardiac involvement in RTHβ |
| [22919057](https://pubmed.ncbi.nlm.nih.gov/22919057/) | 2012 | Animal Study | Endocrinology | Heterozygous Thrb(PV/+) mice with mildly elevated TSH develop asymmetric thyroid carcinoma; raises concern that sustained TSH elevation (as may follow PTU use in RTHβ) drives thyroid tumorigenesis |
| [12201835](https://pubmed.ncbi.nlm.nih.gov/12201835/) | 2002 | Case Report | Clinical Endocrinology | Neonate with RTHβ (M313T) presented with clinical thyrotoxicosis; treated transiently and responded; illustrates the clinical complexity of RTHβ in early life |
| [10724359](https://pubmed.ncbi.nlm.nih.gov/10724359/) | 1999 | Case Report | Endocrine Journal | Thai patient with de novo L330S THRB mutation misdiagnosed as thyrotoxicosis and treated with PTU for 9 months; goiter enlarged despite treatment — a cautionary example of PTU misuse in RTHβ |
| [21909131](https://pubmed.ncbi.nlm.nih.gov/21909131/) | 2012 | Animal Study | Oncogene | Thrb(PV/PV) mouse model demonstrates thyroid hormone activates tumour cell proliferation via PIK3CA pathway; highlights oncogenic risk context in THRB-mutant background |

---

## Philippines Market Information

No registered pharmaceutical licenses for propylthiouracil are currently recorded in the Philippines FDA database.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note for clinical teams:** Although formal safety data was not retrievable in this evidence pack, PTU carries well-documented class-level safety concerns including a **Black Box Warning for severe hepatotoxicity** (including fulminant hepatic failure, particularly in paediatric patients), agranulocytosis, and ANCA-associated vasculitis. These risks are especially relevant given the RTHβ population may include children. Methimazole is generally preferred over PTU in most clinical scenarios; PTU is typically reserved for first trimester of pregnancy or thyroid storm. These risks amplify the caution warranted by the Hold recommendation below.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The mechanistic reasoning for PTU in RTHβ is biologically plausible but fundamentally limited — PTU reduces hormone levels but cannot correct the underlying THRβ receptor defect. The available evidence consists entirely of tier-3 literature (case reports and animal studies), with no clinical trials. One cautionary case report (PMID 10724359) documents actual clinical harm (goiter progression) from inadvertent PTU use in an RTHβ patient, and animal data raise concerns about TSH-driven thyroid tumour promotion following hormone suppression. Together, these findings make this repurposing direction unsuitable for advancement without substantial new evidence.

**To proceed, the following is needed:**
- PTU mechanism of action data retrieved from DrugBank (data gap DG002)
- Philippines FDA prescribing information and full safety/contraindication profile (data gap DG001)
- Prospective clinical data documenting outcomes of PTU use specifically in genetically confirmed RTHβ patients
- Tumour surveillance data in any RTHβ patients exposed to antithyroid agents
- A formal receptor-level mechanistic study assessing whether partial hormone reduction offers net clinical benefit without triggering compensatory TSH overstimulation

---

> **Additional note — Higher-priority indication identified:**
> The second TxGNN-predicted indication, **neonatal thyrotoxicosis** (score 99.40%), carries substantially stronger evidence (Level L2: 1 Phase 3 clinical trial + 20 publications including guidelines, cohort studies, and clinical reviews). PTU's direct mechanistic match to neonatal thyrotoxicosis driven by maternal TRAb transfer is well-established, and the scoring system assigns a *Proceed with Guardrails* recommendation for this indication. If pursuing a PTU repurposing programme in the Philippines, neonatal thyrotoxicosis is recommended as the primary evaluation target over RTHβ.

---

*This report is for research reference purposes only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

