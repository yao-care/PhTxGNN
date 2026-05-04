---
layout: default
title: Fusidic Acid
parent: 僅模型預測 (L5)
nav_order: 157
evidence_level: L5
indication_count: 10
---

# Fusidic Acid
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

# Fusidic Acid: From Bacterial Infections to Exposure Keratitis

## One-Sentence Summary

Fusidic acid is a bacteriostatic antibiotic known internationally for treating staphylococcal skin and eye infections.
The TxGNN model predicts it may be effective for **Exposure Keratitis**,
but with **0 clinical trials** and only **1 tangentially related publication**, the evidence supporting this specific repurposing direction remains extremely limited.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Bacterial infections (no Philippines-registered indication on file) |
| Predicted New Indication | Exposure Keratitis |
| TxGNN Prediction Score | 99.95% |
| Evidence Level | L5 — Model prediction only, no direct clinical studies |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Fusidic acid is a steroidal antibiotic derived from the fungus *Fusidium coccineum*. It works by inhibiting bacterial protein synthesis — specifically, it prevents the turnover of elongation factor G (EF-G) from the ribosome, effectively halting translation. It has potent activity against Gram-positive organisms, particularly *Staphylococcus aureus* (including many MRSA strains), and is widely used internationally in topical formulations (creams, ointments, eye drops) for skin and ocular surface infections.

Exposure keratitis is a corneal condition arising when the eye's surface is inadequately protected — for example, due to incomplete eyelid closure (lagophthalmos) — leading to desiccation, epithelial breakdown, and secondary bacterial infection. The corneal epithelial defect in exposure keratitis creates a vulnerability to bacterial colonisation, particularly by staphylococcal species. Since fusidic acid ophthalmic preparations (e.g., Fucithalmic viscous eye drops) are already widely used in many countries for bacterial conjunctivitis and blepharitis, the prediction that it could play a role in managing the infectious component of exposure keratitis has a plausible pharmacological basis.

However, it is important to emphasise that exposure keratitis is fundamentally a mechanical/protective problem (eyelid dysfunction), and antibiotic therapy addresses only the secondary infection risk, not the root cause. The TxGNN prediction likely captures the association between fusidic acid's ocular antibacterial activity and the infectious complications of exposure keratitis, rather than suggesting it as a primary treatment. This context should be considered when interpreting the high prediction score.

## Clinical Trial Evidence

Currently no related clinical trials registered for the specific combination of fusidic acid and exposure keratitis.

> **Note:** While no trials directly address this indication, fusidic acid has been studied in other ocular infection contexts. The absence of trials for this specific pairing reflects the niche nature of exposure keratitis rather than a lack of interest in fusidic acid's ophthalmic use.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [31246677](https://pubmed.ncbi.nlm.nih.gov/31246677/) | 2019 | Case Series | Cornea | Largest case series of Tsukamurella-associated ophthalmic infections, describing clinical spectrum, risk factors, and treatment outcomes — tangentially relevant to ocular surface infection management |

> **Note:** The single retrieved publication is only indirectly related to the fusidic acid–exposure keratitis pairing. It addresses ophthalmic infections broadly rather than fusidic acid's role in exposure keratitis specifically.

## Philippines Market Information

Fusidic acid currently has **no registered pharmaceutical products** in the Philippines. There are no FDA Philippines authorisations on record.

> To advance this candidate in the Philippines, regulatory pathway assessment and import/registration feasibility would need to be evaluated.

## Other Predicted Indications (Summary)

The TxGNN model also predicted the following indications for fusidic acid. These are presented for completeness:

| Rank | Predicted Indication | TxGNN Score | Clinical Trials | Publications | Evidence Level |
|------|---------------------|-------------|-----------------|--------------|---------------|
| 1 | Exposure keratitis | 99.95% | 0 | 1 | L5 |
| 2 | Non-human animal disease | 99.86% | 0 | 0 | L5 |
| 3 | Otitis externa | 99.84% | 0 | 6 | L4 |
| 4 | Postinfectious vasculitis | 99.83% | 0 | 0 | L5 |
| 5 | Post-bacterial disorder | 99.82% | 2 | 0 | L3 |
| 6 | Post-infectious syndrome | 99.82% | 0 | 0 | L5 |
| 7 | Infective urethral stricture | 99.81% | 0 | 0 | L5 |
| 8 | Chagas cardiomyopathy | 99.80% | 0 | 0 | L5 |
| 9 | Infection-related hemolytic uremic syndrome | 99.79% | 0 | 0 | L5 |
| 10 | Parasitic eyelid infestation | 99.65% | 0 | 0 | L5 |

> **Notable:** The rank 3 indication **otitis externa** has the most literature support (6 publications) and aligns well with fusidic acid's known antibacterial spectrum. The rank 5 indication **post-bacterial disorder** has 2 clinical trials (including a completed Phase 3 trial of oral sodium fusidate for ABSSSI — [NCT02570490](https://clinicaltrials.gov/study/NCT02570490)). These may warrant separate evaluation.

## Safety Considerations

> Please refer to the package insert for safety information. No Philippines-specific safety data (warnings, contraindications, or drug interactions) is currently available in this evidence pack.
>
> **Generally known safety profile of fusidic acid (from international sources):**
> - Topical: Generally well tolerated; may cause local irritation, stinging, or allergic reactions
> - Systemic (oral/IV): Hepatotoxicity (reversible jaundice), gastrointestinal disturbance; requires liver function monitoring
> - Drug interaction: Potent inhibitor of CYP3A4 and OATP1B1 — significant interactions with statins (risk of rhabdomyolysis), ciclosporin, HIV protease inhibitors, and ritonavir-boosted regimens

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction score is high (99.95%), but there is essentially no direct clinical evidence supporting fusidic acid's use specifically for exposure keratitis. The single retrieved publication is only tangentially related. Furthermore, fusidic acid has no registered products in the Philippines, creating an additional regulatory barrier. While the mechanistic rationale (antibacterial protection of compromised corneal surface) is sound, exposure keratitis is primarily a mechanical problem requiring eyelid management, and antibiotics serve only an adjunctive role.

**To proceed, the following is needed:**
- Detailed mechanism of action confirmation via DrugBank API (currently a data gap)
- FDA Philippines package insert / safety data (labelled as a blocking data gap)
- Literature review of fusidic acid ophthalmic preparations in corneal infection prevention
- Assessment of alternative predicted indications with stronger evidence (particularly **otitis externa** with 6 publications, and **post-bacterial disorder** with a completed Phase 3 trial)
- Regulatory pathway assessment for introducing fusidic acid products in the Philippines market

---

*This report is for research reference only and does not constitute medical advice. Drug repurposing candidates require clinical validation before application.*
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

