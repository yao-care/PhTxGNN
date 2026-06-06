---
layout: default
title: Mefenamic Acid
parent: 僅模型預測 (L5)
nav_order: 217
evidence_level: L5
indication_count: 8
---

# Mefenamic Acid
{: .fs-9 }

證據等級: **L5** | 預測適應症: **8** 個
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

# Mefenamic Acid: From Pain and Dysmenorrhea to Rheumatoid Arthritis

## One-Sentence Summary

Mefenamic acid is a fenamate-class NSAID with established analgesic and anti-inflammatory properties, widely used globally for mild-to-moderate pain, dysmenorrhea, and menorrhagia.
The TxGNN model predicts it may be effective for **Rheumatoid Arthritis (RA)**,
with **0 registered clinical trials** and **20 publications** — including 3 directly relevant historical RCTs — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Pain / Dysmenorrhea (fenamate NSAID; no Philippines registration on file) |
| Predicted New Indication | Rheumatoid Arthritis |
| TxGNN Prediction Score | 99.73% |
| Evidence Level | L2 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why Is This Prediction Reasonable?

Detailed mechanism of action data was not available in this evidence package. Based on established pharmacological knowledge, mefenamic acid is a fenamate-class NSAID that inhibits both COX-1 and COX-2 enzymes, reducing prostaglandin synthesis. Crucially, it also **directly antagonizes prostaglandin EP receptors** — a dual mechanism that distinguishes it from most other NSAIDs such as ibuprofen or naproxen, which act only at the synthesis level. This combination suppresses PGE2 both upstream (synthesis) and downstream (receptor signaling).

Rheumatoid arthritis is driven largely by chronic synovial inflammation, where PGE2 plays a central role in perpetuating joint swelling, pain sensitization, and cartilage destruction. The match between mefenamic acid's dual-mechanism and RA's prostaglandin-centric pathophysiology is mechanistically direct. The theoretical advantage over single-mechanism NSAIDs is real, though it has not been tested in modern trials using current RA outcome standards (ACR response criteria, DAS28).

Historical clinical evidence from the 1960s–1970s provides direct support: three double-blind RCTs tested mefenamic acid specifically in RA patients and found efficacy comparable to ibuprofen, sulindac, and flurbiprofen. A 1992 electrophoresis study further demonstrated 75% clinical response rates in 125 RA patients using mefenamic acid-based treatment. While this body of evidence is dated, it is not trivial — it directly addresses the target indication and reflects a real clinical signal that modern trials should revisit.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [373989](https://pubmed.ncbi.nlm.nih.gov/373989/) | 1979 | RCT | Current Medical Research and Opinion | Double-blind crossover (n=24 RA patients): mefenamic acid 1500 mg/day vs sulindac, flurbiprofen, and placebo — all active drugs significantly superior to placebo in pain score, articular index, and morning stiffness duration |
| [330287](https://pubmed.ncbi.nlm.nih.gov/330287/) | 1977 | RCT | J Int Med Research | Randomized double-blind within-patient study (n=40 RA patients): mefenamic acid vs ibuprofen — equivalent analgesic and anti-inflammatory effect; side-effect profiles similar |
| [796645](https://pubmed.ncbi.nlm.nih.gov/796645/) | 1976 | RCT | Med J Australia | Double-blind crossover (mefenamic acid 1500 mg vs ibuprofen 1200 mg, both on background salicylate): mefenamic acid compared favorably; GI side effects mild in both groups |
| [4294443](https://pubmed.ncbi.nlm.nih.gov/4294443/) | 1967 | Clinical Trial | Ann Rheum Dis | Direct clinical investigation of mefenamic acid specifically in rheumatoid arthritis patients |
| [1455792](https://pubmed.ncbi.nlm.nih.gov/1455792/) | 1992 | Clinical Study | Vopr Kurortol | Electrophoresis of mefenamic acid from dimexide solution in 125 RA patients: 75% complete or partial response; reduced pain, corrected immunity markers, suppressed inflammation; best results in low-activity disease |
| [23611159](https://pubmed.ncbi.nlm.nih.gov/23611159/) | 2014 | Formulation Study | Pharm Dev Technol | Triple-concentric time-controlled release mefenamic acid tablet designed specifically for RA: burst release → 2–4 h lag → 8 h controlled release, matching RA morning stiffness chronobiology |
| [16223958](https://pubmed.ncbi.nlm.nih.gov/16223958/) | 2006 | Basic Science | Mol Pharmacol | Epidemiological observation that long-term NSAID use in RA patients reduces Alzheimer's disease risk; mefenamic acid shown to have neuroprotective effects in AD models — secondary finding relevant to RA patient co-morbidity profile |
| [306128](https://pubmed.ncbi.nlm.nih.gov/306128/) | 1978 | Review | Scott Med J | Systematic assessment of mefenamic acid's place in RA therapy; evaluates available evidence base and positions it relative to other NSAIDs of the era |
| [20668](https://pubmed.ncbi.nlm.nih.gov/20668/) | 1977 | Review | Semin Arthritis Rheum | Anti-inflammatory drug class review covering mefenamic acid's mechanism, indications, and role in inflammatory arthritis management |
| [2670397](https://pubmed.ncbi.nlm.nih.gov/2670397/) | 1989 | Review | Clinical Pharmacy | Diclofenac review with NSAID class context; mefenamic acid cited as phenylacetic acid derivative comparator in RA treatment landscape |

---

## Philippines Market Information

No registered products found for mefenamic acid in the Philippines. The drug is not currently marketed or licensed by FDA Philippines as of the data cutoff.

> **Note:** Mefenamic acid (brand name Ponstan) is widely available in other markets including the US, UK, Malaysia, and Taiwan. The absence of Philippines registration represents a regulatory gap, not a safety or efficacy signal.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Safety data (TFDA/FDA-PH warnings, contraindications, DDI profile) was not available in this evidence package. This is flagged as a blocking data gap (DG001) requiring remediation before proceeding to full safety evaluation. As an NSAID, general class-level risks include GI bleeding, renal impairment, and cardiovascular events with prolonged use. A notable drug-specific risk identified in literature: **autoimmune haemolytic anaemia** has been reported in long-term mefenamic acid users (PMID 5676955), and **severe enteropathy with villous atrophy** in prolonged users (PMID 29095288).

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Three double-blind RCTs directly testing mefenamic acid in RA patients, combined with a 125-patient clinical study, provide L2-level evidence for this indication. The dual COX inhibition + direct EP receptor antagonism mechanism maps cleanly onto RA pathophysiology. The absence of Philippines registration and the age of supporting evidence (all pre-1993) require remediation before a regulatory pathway can be defined.

**To proceed, the following is needed:**
- Obtain and review the full package insert (any country registration) for warnings, contraindications, and known DDIs
- Commission or identify a contemporary pharmacovigilance review for the mefenamic acid RA safety profile, including autoimmune haemolytic anaemia risk in long-term use
- Assess feasibility of a modern RA efficacy study (ACR20/50/70, DAS28) — historical RCTs used outcome measures that are no longer standard
- Evaluate regulatory pathway with FDA Philippines for new indication filing or market authorization
- Compare mefenamic acid's role in the context of current RA treatment guidelines (DMARDs as backbone; NSAIDs for symptomatic control only)
- Clarify whether dual PG mechanism provides measurable clinical advantage over currently available NSAIDs in the Philippine formulary
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

