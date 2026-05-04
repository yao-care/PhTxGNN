---
layout: default
title: Cyproterone Acetate
parent: 僅模型預測 (L5)
nav_order: 89
evidence_level: L5
indication_count: 10
---

# Cyproterone Acetate
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

# Cyproterone Acetate: From Hyperandrogenism to Migraine Disorder

## One-Sentence Summary

Cyproterone acetate (CPA) is a synthetic progestogen with potent antiandrogen properties, primarily used to treat hyperandrogenism-related conditions (hirsutism, acne, polycystic ovary syndrome) and prostate cancer. The TxGNN model predicts it may be effective for **Migraine Disorder**, with **0 clinical trials** and **3 publications** currently supporting this direction. Evidence remains at the preclinical/mechanistic level (L4), and the complex, bidirectional nature of progestogen–migraine interactions warrants considerable caution before further development.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hyperandrogenism (hirsutism, acne, PCOS); prostate cancer |
| Predicted New Indication | Migraine Disorder |
| TxGNN Prediction Score | 99.66% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from DrugBank. Based on known pharmacology, cyproterone acetate is a synthetic C21-steroid progestogen with potent antiandrogen activity: it competitively blocks androgen receptors and suppresses gonadotropin (LH/FSH) secretion, thereby reducing ovarian and adrenal androgen production. As a C21-steroid, CPA also interacts with GABA-A receptors and modulates dopaminergic and opioid receptor systems in the central nervous system (Gruber & Huber, 2003) — neurochemical effects that could, in theory, intersect with pain-processing pathways relevant to migraine.

Menstrual migraine is tightly linked to cyclic hormonal fluctuations, particularly the sharp decline in estrogen and progesterone during the late luteal phase. Progestogenic supplementation theoretically stabilises this hormonal environment and could dampen cyclical migraine triggers. An observational study in postmenopausal women (Facchinetti et al., 2002) found that different hormone replacement regimens — including CPA-containing combinations — had meaningfully different effects on migraine frequency, providing indirect evidence that the progestogenic component matters.

However, the progestogen–migraine relationship is bidirectional and individual-dependent: progestogens may either suppress or provoke migraines depending on the formulation, dose, and patient profile. No study has directly tested CPA as a migraine treatment. The high TxGNN score most likely reflects shared hormonal pathway nodes in the knowledge graph rather than direct therapeutic validation, and CPA-specific mechanistic evidence for migraine has not been established.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12390622](https://pubmed.ncbi.nlm.nih.gov/12390622/) | 2002 | Clinical Study (Observational) | *Headache* | Compared three oral HRT regimens (including a CPA-containing scheme) in postmenopausal women; different regimens had differential effects on migraine frequency, indicating that progestogen type influences migraine course |
| [14670648](https://pubmed.ncbi.nlm.nih.gov/14670648/) | 2003 | Review | *Maturitas* | CPA increases dopaminergic responses in striatal tissue and binds opiate receptors independently of its classical antiandrogen effect; as a C21-steroid it activates GABA-A receptors — CNS interactions potentially relevant to migraine pathophysiology |
| [10857213](https://pubmed.ncbi.nlm.nih.gov/10857213/) | 2000 | Observational (Side Effect Report) | *Zentralblatt fur Gynakologie* | Long-term CPA safety data from 2,506 patients (7,971 patient-years) in gynaecological use; provides background safety profile relevant to chronic treatment considerations |

---

## Philippines Market Information

Cyproterone acetate is currently **not registered or marketed in the Philippines**. No product authorizations are on record with the FDA Philippines. Any future use would require full registration proceedings before clinical deployment.

---

## Safety Considerations

Full package insert warnings and contraindications are not yet available. Please refer to the package insert for complete safety information.

> **Critical safety signal from pharmacovigilance literature** (identified across this evidence pack): Multiple cohort and mechanistic studies confirm that CPA-containing oral contraceptives are associated with a **significantly increased risk of venous and arterial thromboembolism**. Key mechanisms include: (1) reduction of protein S levels; (2) increased activated protein C (APC) resistance; (3) elevated thrombin generation potential; (4) suppression of fibrinolytic activity. This has been documented in case reports, cohort studies, and French national pharmacovigilance data (Gourbil et al., 2014; van Vliet et al., 2004; Toorians et al., 2003).
>
> **This thrombotic risk is directly relevant to the top predicted indication**: migraine with aura — and the closely ranked "migraine with brainstem aura" (rank #2) — are independent risk factors for ischaemic stroke. Combining CPA's prothrombotic mechanism with these migraine subtypes would create a **compounded cerebrovascular risk and represents a contraindication**, not a therapeutic opportunity. Similarly, the model's predictions for antithrombin deficiency type 2 (rank #4), heparin cofactor 2 deficiency (rank #5), factor V excess with spontaneous thrombosis (rank #6), and thrombophilia (rank #10) should all be interpreted as **safety-driven false positives** — these likely reflect shared coagulation pathway nodes in the knowledge graph, not treatment signals.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While a hormonal mechanism linking CPA to menstrual migraine is biologically plausible, supporting clinical evidence is entirely absent (zero trials, three indirect publications). More critically, the broader evidence package reveals that CPA carries a well-documented prothrombotic risk profile that is incompatible with several of the high-ranked predicted indications, and requires careful patient selection even for established uses. The top prediction (migraine disorder) cannot advance until the safety profile is fully characterized and migraine subtype screening protocols are defined.

**To proceed, the following is needed:**
- Retrieve complete MOA and drug category data from DrugBank (DB04839) to resolve the current data gap
- Obtain and parse the TFDA (or equivalent Philippine FDA) package insert PDF for full warnings, contraindications, and approved indications
- Conduct a dedicated systematic review focused specifically on progestogen monotherapy (not combined OCP) in menstrual migraine prevention
- Define patient selection criteria that exclude migraine with aura, personal or family history of VTE, and thrombophilic conditions
- Consider prioritising the **amenorrhea indication (rank #8, L3 evidence, "Proceed with Guardrails")** as the near-term development target — it has the strongest mechanistic basis, direct clinical trial data (NCT01103518), and aligns with CPA's established antiandrogen/progestogenic mechanism in hyperandrogenism
- Evaluate regulatory pathway options given that CPA is not currently registered in the Philippines

---

> ⚠️ *This report is for research purposes only and does not constitute medical advice. All drug repurposing candidates identified by TxGNN require clinical validation before any therapeutic application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

