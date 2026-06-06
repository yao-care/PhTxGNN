---
layout: default
title: Tocilizumab
parent: 僅模型預測 (L5)
nav_order: 335
evidence_level: L5
indication_count: 10
---

# Tocilizumab
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

# Tocilizumab: From Rheumatoid Arthritis to Ankylosing Spondylitis

## One-Sentence Summary

Tocilizumab is a humanized anti-interleukin-6 receptor (IL-6R) monoclonal antibody, approved globally for rheumatoid arthritis, systemic and polyarticular juvenile idiopathic arthritis, and giant cell arteritis.
The TxGNN model predicts it may be effective for **Ankylosing Spondylitis (AS)**, with **2 Phase 3 clinical trials directly targeting AS** and **19 publications** currently on record; however, both pivotal trials were **terminated early due to failure to meet primary efficacy endpoints**, making this a **definitively tested-and-failed indication** rather than an unexplored opportunity.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Rheumatoid arthritis (globally approved; not registered in the Philippines) |
| Predicted New Indication | Ankylosing Spondylitis |
| TxGNN Prediction Score | 99.99% |
| Evidence Level | L1 (2 Phase 3 RCTs — both terminated, negative signal) |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, formal mechanism of action data was not retrievable from the local data pipeline. Based on internationally published information, tocilizumab is a recombinant humanized monoclonal antibody that competitively binds both membrane-bound and soluble forms of the IL-6 receptor (IL-6R), blocking downstream JAK1/TYK2 → STAT3 signaling. This effectively suppresses IL-6–driven acute phase responses, osteoclast activation, and T/B lymphocyte differentiation — processes relevant to multiple autoimmune and inflammatory conditions.

Ankylosing spondylitis (AS) shares superficial mechanistic overlap with rheumatoid arthritis: both involve chronic synovial inflammation, elevated CRP/ESR, and IL-6 elevations in serum and synovial fluid. This commonality, combined with tocilizumab's proven efficacy in RA and giant cell arteritis (a systemic vasculitis), provided a plausible rationale for the BUILDER clinical programme. The TxGNN model's high score likely reflects these topological similarities within the knowledge graph linking inflammatory rheumatic diseases.

However, the critical distinction lies in the dominant pathogenic axis: AS is primarily driven by **IL-17A and TNFα** (not IL-6), with the IL-23/IL-17 pathway governing enthesitis and pathological new bone formation. Two dedicated Phase 3 RCTs — BUILDER-1 (NCT01209689, n=113, TNF-refractory patients) and BUILDER-2 (NCT01209702, n=306, NSAID-failed TNF-naïve patients) — were both terminated for insufficient efficacy on primary endpoints (ASAS20/40 response rates). The 2014 publication of their pooled results (PMID 23765873) confirmed that IL-6R blockade does not meaningfully reduce signs and symptoms of AS, establishing the biological hypothesis as falsified for the general AS population.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT01209689](https://clinicaltrials.gov/study/NCT01209689) | Phase 3 | Terminated | 113 | BUILDER-1: Double-blind RCT in TNF-refractory AS. TCZ 8 mg/kg or 4 mg/kg IV q4w vs. placebo for 24 weeks. Terminated — primary efficacy endpoint (ASAS40) not met. Critical negative trial for IL-6 blockade in AS. |
| [NCT01209702](https://clinicaltrials.gov/study/NCT01209702) | Phase 2/3 | Terminated | 306 | BUILDER-2: Seamless Phase 2/3 RCT in NSAID-failed, TNF-naïve AS. TCZ 8 mg/kg IV vs. placebo. Terminated — failed to demonstrate symptom reduction or structural damage inhibition. Confirms IL-6R blockade is insufficient for AS. |
| [NCT02569736](https://clinicaltrials.gov/study/NCT02569736) | N/A | Completed | 60 | Mechanistic study: TCZ effects on T follicular helper cells and B cell maturation in RA patients in vivo and in vitro. Provides immunological mechanistic insight but no clinical efficacy endpoint for AS. |
| [NCT05670301](https://clinicaltrials.gov/study/NCT05670301) | NA | Recruiting | 2,500 | Flemish multi-disease biomarker profiling study (systemic inflammatory diseases). Includes AS; longitudinal cytokine profiling may clarify IL-6 role, but not a TCZ efficacy trial. |
| [NCT01965132](https://clinicaltrials.gov/study/NCT01965132) | N/A | Recruiting | 10,000 | Korean nationwide biologics and targeted DMARD registry covering RA, AS, and PsA. Real-world safety data across agents; not AS-specific TCZ intervention. |
| [NCT05696106](https://clinicaltrials.gov/study/NCT05696106) | N/A | Unknown | 750,000 | Large observational study on incident IMID risk in patients treated with biologics. Provides epidemiological context; no direct TCZ efficacy data in AS. |
| [NCT02925338](https://clinicaltrials.gov/study/NCT02925338) | N/A | Completed | 1,431 | French real-world study of Inflectra (infliximab biosimilar) in RA/SpA. Indirect comparator reference only; not a TCZ study. |
| [NCT07138898](https://clinicaltrials.gov/study/NCT07138898) | Phase 2 | Not Yet Recruiting | 80 | Immunosuppressant management in rheumatology patients undergoing elective shoulder arthroplasty. No direct relevance to AS therapeutic efficacy. |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [23765873](https://pubmed.ncbi.nlm.nih.gov/23765873/) | 2014 | RCT Publication | Ann Rheum Dis | BUILDER-1 and BUILDER-2 pooled results: TCZ failed to achieve significant improvement in AS signs and symptoms at 12 and 24 weeks vs. placebo. Definitive negative evidence for IL-6R blockade in AS. |
| [26986130](https://pubmed.ncbi.nlm.nih.gov/26986130/) | 2016 | Systematic Review | Medicine | Bayesian network meta-analysis of all biologic regimens for AS: TNFα inhibitors and IL-17A inhibitors ranked highest; IL-6 pathway agents absent from recommended therapeutic options. |
| [22452603](https://pubmed.ncbi.nlm.nih.gov/22452603/) | 2012 | Review | Inflamm Allergy Drug Targets | Review of IL-6 antagonism in AS: discusses theoretical rationale, notes IL-6 plays a secondary role relative to TNFα/IL-17; acknowledges limited clinical evidence available at time of writing (prior to BUILDER results). |
| [22450391](https://pubmed.ncbi.nlm.nih.gov/22450391/) | 2012 | Review | Curr Opin Rheumatol | Treatment options for TNF-inhibitor-refractory AS: TCZ discussed as an investigational agent; clinical data then inconclusive. Now superseded by BUILDER negative results. |
| [28413099](https://pubmed.ncbi.nlm.nih.gov/28413099/) | 2017 | Review | Semin Arthritis Rheum | Italian expert board recommendations for second-line biologic choice in AS: IL-6 inhibitors not recommended as standard second-line therapy; IL-17A inhibitors (secukinumab, ixekizumab) preferred. |
| [33981717](https://pubmed.ncbi.nlm.nih.gov/33981717/) | 2021 | Case Report | Front Med | Two AS patients with secondary AA amyloidosis (a severe chronic-inflammation complication) treated successfully with TCZ. Suggests a niche utility for AS complications driven by chronic SAA elevation — not AS disease activity itself. |
| [20959960](https://pubmed.ncbi.nlm.nih.gov/20959960/) | 2011 | Review | Osteoporos Int | Bone effects of biologics in RA and AS: IL-6 pathway relevant to periarticular bone loss; however, TNFα blockers demonstrated superior efficacy in preventing AS-related structural progression. |
| [29290076](https://pubmed.ncbi.nlm.nih.gov/29290076/) | 2018 | Meta-analysis | Clin Rheumatol | Meta-analysis of serious infection risk with biologics in AS/nr-axSpA (RCT-based): safety reference framework for biologic use in spondyloarthritis; TCZ not among agents evaluated for AS specifically. |
| [31852268](https://pubmed.ncbi.nlm.nih.gov/31852268/) | 2020 | Cohort | Expert Rev Clin Immunol | Comparative infection risk between non-biologics, TNF inhibitors, and non-TNF biologics (including TCZ) in inflammatory arthritis: TCZ associated with moderate infection risk, relevant to any future AS safety profiling. |
| [40256995](https://pubmed.ncbi.nlm.nih.gov/40256995/) | 2025 | Guideline | Arthritis Care Res | DMARD recommendations in pregnancy and reproductive health for rheumatic diseases: includes TCZ guidance; important for AS patients of childbearing potential. |

---

## Philippines Market Information

Tocilizumab is currently **not registered** with the Philippines Food and Drug Administration (FDA Philippines). No marketing authorizations are on file.

> **Reference note:** Tocilizumab (Actemra®/RoActemra®, Roche) holds regulatory approvals in the US FDA, EMA (EU), PMDA (Japan), and other major jurisdictions for rheumatoid arthritis, systemic and polyarticular juvenile idiopathic arthritis, giant cell arteritis, and COVID-19–associated cytokine release syndrome. Any Philippines introduction would require a de novo registration application to the FDA Philippines.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Based on globally published prescribing information, the following class effects are well-documented for tocilizumab and are relevant to clinical risk assessment:
>
> - **Serious infections**: Upper respiratory tract infections, pneumonia, opportunistic infections; screening for TB and viral hepatitis required before initiation
> - **Hepatotoxicity**: Transaminase elevations (ALT/AST); baseline and periodic liver function monitoring required
> - **Hematological effects**: Neutropenia and thrombocytopenia; CBC monitoring at baseline, 4–8 weeks, then every 3 months
> - **Lipid changes**: Increases in total cholesterol, LDL, and HDL; cardiovascular risk assessment recommended
> - **Gastrointestinal perforations**: Risk elevated in patients with history of diverticulitis, concurrent NSAIDs, or corticosteroids
> - **Hypersensitivity reactions**: Including anaphylaxis (rare); administer in settings equipped for resuscitation
>
> *Formal Philippines package insert data unavailable due to lack of local registration.*

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN model's 99.99% confidence prediction for tocilizumab in ankylosing spondylitis reflects a biologically plausible but clinically disproven hypothesis. Two dedicated Phase 3 RCTs (BUILDER-1 and BUILDER-2, combined n=419) were both terminated for insufficient efficacy, with published results confirming no meaningful reduction in ASAS response rates. AS pathogenesis is governed primarily by the IL-17A/IL-23/TNFα axis — not IL-6 — making IL-6R blockade an insufficient therapeutic strategy for the general AS population. This is a knowledge-graph topology artefact, not a genuine repurposing opportunity.

**To reconsider this indication, the following would be required:**

- Identification of an AS biomarker subgroup in which IL-6 is the dominant inflammatory driver (e.g., high-IL-6/low-IL-17 phenotype confirmed by prospective biomarker studies)
- Reanalysis of BUILDER-1/BUILDER-2 data for potential responder subgroups (e.g., patients with elevated baseline IL-6, or those with concomitant AA amyloidosis risk)
- New preclinical evidence demonstrating IL-6R blockade efficacy in an IL-17A–independent AS disease model
- Emergence of a specific AS complication subtype (e.g., secondary AA amyloidosis as in PMID 33981717) that justifies a narrowly scoped indication study
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

