---
layout: default
title: Prednisone
parent: 僅模型預測 (L5)
nav_order: 182
evidence_level: L5
indication_count: 10
---

# Prednisone
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

# Prednisone: From Systemic Inflammatory Conditions to Alopecia Areata

## One-Sentence Summary

Prednisone is a synthetic glucocorticoid with potent anti-inflammatory and immunosuppressive effects, classically used for a wide range of autoimmune, inflammatory, and allergic disorders.
The TxGNN model predicts it may be effective for **Alopecia Areata**,
with **1 directly relevant completed Phase 3 RCT** (NCT02037191) and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Systemic anti-inflammatory and immunosuppressive therapy (autoimmune, inflammatory, and allergic conditions) |
| Predicted New Indication | Alopecia Areata |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L2 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Prednisone is a synthetic glucocorticoid that binds intracellular glucocorticoid receptors to trigger broad anti-inflammatory and immunosuppressive effects. Although detailed MOA data was not retrieved in this evidence pack, prednisone's pharmacology is well established: it inhibits phospholipase A2 (PLA2) to reduce prostaglandin and leukotriene synthesis, suppresses NF-κB to downregulate IL-1β, TNF-α, IL-6, and IFN-γ, curtails IL-2 production to impair CD8⁺ T-cell proliferation, and stabilizes lysosomal membranes to limit collateral tissue damage.

Alopecia areata (AA) is a CD8⁺ T-cell–mediated autoimmune disorder in which autoreactive cytotoxic T cells breach the immune privilege of hair follicles, generating the characteristic perifollicular "swarm of bees" lymphocytic infiltrate. This mechanism maps directly onto prednisone's strengths: suppression of the T-cell–driven cascade can theoretically restore the follicular immune sanctuary and permit hair regrowth. Clinical use of systemic corticosteroids in AA dates back to the 1950s, reflecting longstanding recognition of this mechanistic alignment.

Modern guidelines have shifted toward JAK inhibitors (baricitinib, ritlecitinib) for sustained remission in severe AA owing to more durable responses. However, prednisone remains clinically relevant as acute bridging therapy, as a combination partner with methotrexate — a role directly validated by a 2023 JAMA Dermatology RCT (PMID 36884234) — and for rapid suppression of rapidly progressing disease. The mechanistic basis is solid even if long-term monotherapy is no longer considered optimal.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT02037191](https://clinicaltrials.gov/study/NCT02037191) | Phase 3 | Completed | 90 | Randomized double-blind study evaluating methotrexate vs placebo in severe alopecia areata totalis/universalis, with a secondary treatment arm of methotrexate combined with low-dose prednisone; the most directly relevant trial for prednisone's role in severe AA |
| [NCT03843125](https://clinicaltrials.gov/study/NCT03843125) | Phase 3 | Terminated | 1,147 | Long-term safety and efficacy of baricitinib in AA; prednisone used as rescue or concomitant medication, providing contextual evidence for corticosteroid use in this indication; terminated early — efficacy data require cautious interpretation |
| [NCT05162586](https://clinicaltrials.gov/study/NCT05162586) | Phase 2 | Completed | 456 | Dose-ranging study of enpatoran in SLE/CLE on standard of care; prednisone permitted as background therapy, situating its role within immune-mediated dermatologic disease management |
| [NCT02437890](https://clinicaltrials.gov/study/NCT02437890) | Phase 2 | Completed | 312 | ALX-0061 (anti-IL-6R antibody) in moderate-to-severe SLE; steroid reduction was a prespecified secondary endpoint, highlighting prednisone as the immunosuppressive anchor against which newer biologics are benchmarked |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [36884234](https://pubmed.ncbi.nlm.nih.gov/36884234/) | 2023 | RCT | *JAMA Dermatology* | 2-step double-blind RCT (n=90): methotrexate + low-dose prednisone significantly improved complete hair regrowth rates in alopecia totalis/universalis vs methotrexate alone; strongest current RCT evidence for low-dose prednisone in severe AA |
| [37467740](https://pubmed.ncbi.nlm.nih.gov/37467740/) | 2023 | Case Series | *Clinical and Experimental Dermatology* | 8-case series: combination of baricitinib + low-dose corticosteroids achieved major improvement in very severe AA (SALT ≥95) where baricitinib monotherapy had failed; supports prednisone as a potentiating agent |
| [26735937](https://pubmed.ncbi.nlm.nih.gov/26735937/) | 2016 | Cohort Study | *Dermatology (Basel)* | Methotrexate combined with low-to-moderate dose corticosteroids in severe AA; reports response rates and tolerability supporting the combination regimen |
| [38650498](https://pubmed.ncbi.nlm.nih.gov/38650498/) | 2024 | Real-world Evidence | *Italian Journal of Dermatology and Venereology* | National real-world analysis of hospitalized AA patients in Italy; documents treatment patterns including corticosteroid use, comorbidities, and economic burden |
| [1444509](https://pubmed.ncbi.nlm.nih.gov/1444509/) | 1992 | Review | *Archives of Dermatology* | Comprehensive review of AA therapy covering corticosteroids, DNCB, PUVA, and other modalities; discusses efficacy, safety, and mechanistic underpinnings of prednisone in various AA severity levels |
| [791152](https://pubmed.ncbi.nlm.nih.gov/791152/) | 1976 | Follow-up Study | *Archives of Dermatology* | 18 patients on alternate-day prednisone for AA followed for mean 15 months post-treatment; initial hair regrowth response observed but long-term benefit limited; multiple side effects documented |
| [4571041](https://pubmed.ncbi.nlm.nih.gov/4571041/) | 1973 | Interventional Study | *Archives of Dermatology* | Early immunologic characterization of AA with prednisone treatment; foundational documentation of the immunosuppressive approach in this condition |
| [20804894](https://pubmed.ncbi.nlm.nih.gov/20804894/) | 2010 | Clinical Study | *Annales de Dermatologie et de Vénéréologie* | Evaluated monthly oral pulse prednisone for AA; assessed efficacy and safety of pulsed corticosteroid dosing as an alternative to continuous therapy |
| [8996277](https://pubmed.ncbi.nlm.nih.gov/8996277/) | 1997 | Clinical Study | *Journal of the American Academy of Dermatology* | Systemic cyclosporine + low-dose prednisone in severe chronic AA; clinical and immunopathologic evaluation of the combination approach |
| [23962142](https://pubmed.ncbi.nlm.nih.gov/23962142/) | 2013 | Case Report | *Journal of Cutaneous Pathology* | AA-like diffuse scalp alopecia with prominent follicular mucinosis achieved complete resolution with oral prednisone; illustrates prednisone's efficacy across the AA-spectrum of immune-mediated alopecia |

---

## Philippines Market Information

Prednisone currently has **no registered products** with FDA Philippines (market status: Not Marketed, 0 active licenses). Should this repurposing candidate be advanced, a new drug registration application with FDA Philippines would be required before commercial availability.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
The mechanistic case is compelling — prednisone directly targets the CD8⁺ T-cell–driven immunopathology of alopecia areata — and this is reinforced by a completed Phase 3 RCT (NCT02037191) and a published 2023 JAMA Dermatology RCT (PMID 36884234) demonstrating superior hair regrowth when low-dose prednisone is combined with methotrexate in alopecia totalis/universalis. Evidence level L2 is met. However, the absence of a Philippines market registration, missing formal safety documentation, and the evolving treatment landscape (JAK inhibitors now preferred for severe AA) necessitate guardrails before advancing.

**To proceed, the following is needed:**

- **Regulatory pathway**: Initiate FDA Philippines drug registration for prednisone (currently 0 active licenses)
- **Safety documentation**: Obtain and review the full prescribing information — contraindications, black-box warnings, and drug interactions were not retrievable in this evidence pack
- **DDI assessment**: Full drug-drug interaction profile not available; must be completed before clinical use
- **Target population definition**: Specify intended AA severity stratum (mild patch vs severe/totalis/universalis) and clarify intended role (monotherapy induction, bridging to JAK inhibitor, or combination with methotrexate)
- **Dosing regimen**: Confirm preferred schedule (daily low-dose, alternate-day, or monthly oral pulse) based on available evidence
- **Long-term safety monitoring plan**: Address known corticosteroid risks — HPA axis suppression, metabolic syndrome, osteoporosis, ocular complications, and infection risk — with defined monitoring intervals
- **Positioning vs JAK inhibitors**: Clarify how prednisone fits within current AA treatment algorithms given that baricitinib and ritlecitinib now hold formal regulatory approvals for severe AA
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

