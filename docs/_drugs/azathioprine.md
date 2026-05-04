---
layout: default
title: Azathioprine
parent: 僅模型預測 (L5)
nav_order: 33
evidence_level: L5
indication_count: 10
---

# Azathioprine
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

# Azathioprine: From Immunosuppression to Inflammatory Bowel Disease

## One-Sentence Summary

Azathioprine is a thiopurine immunosuppressant internationally recognized as a first-line immunomodulator for autoimmune-mediated diseases; it has **no current Philippines registration** despite a strong global evidence base spanning over 45 years.

The TxGNN model predicts it may be effective for **Inflammatory Bowel Disease (IBD)**, consistent with its established global clinical application, with **50 clinical trials** and **20 publications** currently supporting this direction — making IBD the highest-evidence and most actionable prediction in this analysis.

> **Editorial note on TxGNN rankings**: The top four TxGNN predictions (ranks 1–4: colobomatous microphthalmia-rhizomelic dysplasia syndrome, brachydactyly-syndactyly syndrome, osteoarthritis susceptibility, and WHIM syndrome) carry model scores ≥99.68% but are considered knowledge graph topology false positives — all involve congenital structural malformations or primary immunodeficiency disorders with no mechanistic basis for azathioprine intervention. This report focuses on **IBD (rank 5, score 99.52%)** as the first prediction with genuine biological plausibility and Level 1 clinical evidence.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | No Philippines FDA registration on record |
| Predicted New Indication | Inflammatory Bowel Disease (IBD) |
| TxGNN Prediction Score | 99.52% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

IBD encompasses Crohn's disease and ulcerative colitis — chronic relapsing inflammatory conditions driven by pathological activation of intestinal CD4+ T lymphocytes (Th1 pathway predominant in Crohn's disease; Th2/Th17 in ulcerative colitis). These aberrantly activated cells sustain waves of TNF-α, IL-6, IL-12, IL-23, and IL-17, causing progressive mucosal destruction and epithelial barrier breakdown. Azathioprine is metabolized in vivo to 6-thioguanine nucleotides (6-TGN), which inhibit Rac1 GTPase activation and intercalate into DNA, selectively inducing apoptosis of activated T cells via the Fas/FasL pathway, while simultaneously suppressing IL-2-mediated lymphocyte proliferation — directly targeting the immunological core of IBD pathogenesis.

Although detailed mechanism of action data was not available in this evidence pack, Azathioprine's role in IBD is well-characterized in published literature. It holds a Grade B first-line recommendation in ECCO (European Crohn's and Colitis Organisation) guidelines for maintenance of IBD remission, and has been endorsed by ACG (American College of Gastroenterology) and WHO essential medicines guidelines. Four Cochrane systematic reviews (2007, 2012, 2016, and a 2025 update) have consistently confirmed its efficacy in remission maintenance for both Crohn's disease and ulcerative colitis, establishing it as the benchmark immunomodulator comparator in landmark trials such as SONIC.

The TxGNN score of 99.52% for IBD reflects genuine mechanistic and clinical alignment rather than graph topology artefact — in clear contrast to the top-ranked predictions. A particularly important pharmacogenomic dimension exists for Philippines-context deployment: NUDT15 and TPMT genetic polymorphisms that govern 6-TGN metabolism and leukopenia risk have substantially different allele frequencies in East and Southeast Asian populations compared to Western cohorts, and pre-treatment genotyping is clinically essential before initiating azathioprine in Filipino patients.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT00976690](https://clinicaltrials.gov/study/NCT00976690) | Phase 3 | Completed | 83 | Multicentre RCT directly comparing Azathioprine vs Mesalazine for prevention of postoperative Crohn's disease recurrence — highest-relevance direct evidence |
| [NCT01235689](https://clinicaltrials.gov/study/NCT01235689) | Phase 3 | Completed | 252 | Large multicentre open-label RCT comparing two AZA-containing treatment algorithms for moderate-to-severe Crohn's disease, demonstrating mucosal healing benefit of tight disease control |
| [NCT00094458](https://clinicaltrials.gov/study/NCT00094458) | Phase 3 | Completed | 508 | Landmark three-arm RCT comparing infliximab monotherapy, azathioprine monotherapy, and IFX+AZA combination in immunomodulator/biologic-naïve Crohn's disease patients |
| [NCT00946946](https://clinicaltrials.gov/study/NCT00946946) | Phase 3 | Completed | 78 | Double-blind, double-dummy RCT: AZA vs Mesalazine for clinical relapse prevention in postoperative Crohn's disease with moderate-to-severe endoscopic recurrence |
| [NCT02852694](https://clinicaltrials.gov/study/NCT02852694) | Phase 4 | Completed | 192 | Risk-stratified RCT in paediatric Crohn's disease: AZA/6-MP (low-risk arm) vs Methotrexate vs Adalimumab (high-risk arm) for 1-year steroid-free sustained remission |
| [NCT00546546](https://clinicaltrials.gov/study/NCT00546546) | Phase 4 | Completed | 120 | Pluricentric RCT comparing early immunosuppressant initiation (AZA within 6 months of diagnosis) vs conventional step-up strategy in newly diagnosed Crohn's disease |
| [NCT03189888](https://clinicaltrials.gov/study/NCT03189888) | N/A | Completed | 33 | Prospective multicentre study in steroid-dependent, AZA-intolerant/resistant moderate UC receiving granulocyte-monocyte apheresis; directly confirms AZA's established first-line position in UC |
| [NCT02929706](https://clinicaltrials.gov/study/NCT02929706) | N/A | Unknown | 400 | RCT evaluating NUDT15 genotype-guided thiopurine dose optimisation vs conventional dosing to reduce AZA-induced leukopenia in IBD — critical precision pharmacogenomics safety dataset |
| [NCT04196920](https://clinicaltrials.gov/study/NCT04196920) | N/A | Unknown | 200 | Head-to-head comparison of MTX + anti-TNF vs AZA + anti-TNF combination therapy in chronic IBD; provides direct comparative combination strategy data |
| [NCT00537316](https://clinicaltrials.gov/study/NCT00537316) | Phase 3 | Terminated | 242 | Three-arm double-blind RCT: infliximab monotherapy vs IFX+AZA vs AZA monotherapy in moderate-to-severe active UC; early termination but substantial completed dataset remains informative |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [40013523](https://pubmed.ncbi.nlm.nih.gov/40013523/) | 2025 | Cochrane Systematic Review | Cochrane Database Syst Rev | Updated meta-analysis confirming AZA and 6-MP for maintenance of remission in ulcerative colitis — most current systematic synthesis |
| [39586616](https://pubmed.ncbi.nlm.nih.gov/39586616/) | 2025 | RCT | Gut | ACTIVE trial: top-down infliximab + AZA vs AZA monotherapy in acute severe UC responsive to IV steroids — recent high-quality head-to-head RCT |
| [27192092](https://pubmed.ncbi.nlm.nih.gov/27192092/) | 2016 | Cochrane Systematic Review | Cochrane Database Syst Rev | Cochrane review on AZA/6-MP for UC remission maintenance — cornerstone systematic evidence |
| [22972046](https://pubmed.ncbi.nlm.nih.gov/22972046/) | 2012 | Cochrane Systematic Review | Cochrane Database Syst Rev | Earlier Cochrane synthesis on AZA in UC; part of a consistent longitudinal evidence chain |
| [19392869](https://pubmed.ncbi.nlm.nih.gov/19392869/) | 2009 | Meta-analysis | Aliment Pharmacol Ther | First dedicated meta-analysis confirming AZA/6-MP efficacy specifically in ulcerative colitis |
| [29293971](https://pubmed.ncbi.nlm.nih.gov/29293971/) | 2018 | Review | J Crohn's Colitis | State-of-the-art international expert review of thiopurine treatment in IBD: efficacy, safety, pharmacogenomics, monitoring, and emerging evidence |
| [22072847](https://pubmed.ncbi.nlm.nih.gov/22072847/) | 2011 | Clinical Guideline Review | World J Gastroenterol | Clinical framework for optimising AZA/6-MP dosing using 6-TGN and 6-MMP metabolite monitoring to maximise efficacy and minimise hepatotoxicity |
| [19072367](https://pubmed.ncbi.nlm.nih.gov/19072367/) | 2008 | Molecular Review | Expert Rev Gastroenterol Hepatol | Detailed molecular mechanism of AZA in IBD: 6-TGN synthesis, Rac1 GTPase inhibition, activated T-cell apoptosis, and clinical correlates |
| [37586320](https://pubmed.ncbi.nlm.nih.gov/37586320/) | 2023 | Mechanistic Study | Cell Rep Med | Gut commensal Blautia wexlerae reduces 6-MP bioavailability and drives AZA therapy failure in IBD — microbiome-drug interaction with precision medicine implications |
| [36462311](https://pubmed.ncbi.nlm.nih.gov/36462311/) | 2023 | Pharmacokinetics Study | Biomed Pharmacother | TPMT DNA methylation influences AZA pharmacokinetics in very early onset IBD children — key paediatric dosing precision data, relevant for Asian populations with altered TPMT/NUDT15 frequency |

---

## Philippines Market Information

Azathioprine currently has **no registered products** with the Food and Drug Administration of the Philippines (FDA-Ph). There are no active drug licenses or marketing authorizations on record.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|-------------------|
| — | No registered products found | — | — |

This absence represents a significant clinical access gap. IBD incidence is rising across Southeast Asia including the Philippines, and azathioprine is a low-cost, off-patent, WHO Essential Medicine with over 45 years of validated clinical use globally. Patients in the Philippines who require first-line immunomodulatory maintenance therapy for IBD currently have no formally approved domestic pathway for this drug.

---

## Cytotoxicity

Azathioprine meets the criteria for cytotoxic drug classification: it is a thiopurine antimetabolite originally developed for acute leukemia treatment, and is categorized as an antineoplastic/cytotoxic agent in pharmacological reference databases including DrugBank (Antimetabolites, Antineoplastic Agents). It requires cytotoxic drug handling in healthcare settings.

| Item | Content |
|------|---------|
| Cytotoxicity Classification | Conventional cytotoxic — Antimetabolite (Thiopurine class); originally an antineoplastic agent repositioned as an immunomodulator |
| Myelosuppression Risk | **High** — Leukopenia is the primary dose-limiting toxicity and can be life-threatening. Risk is dramatically elevated in carriers of NUDT15 c.415C>T (common in East/Southeast Asian populations, ~10–15% carrier rate) and TPMT variants. Mandatory CBC monitoring is required |
| Emetogenicity Classification | Low (minimal emetogenic potential at standard immunosuppressive doses) |
| Monitoring Items | CBC with differential (baseline, then every 1–2 weeks for the first month, every 1–3 months thereafter); ALT/AST and serum creatinine at baseline and every 3 months; 6-TGN/6-MMP metabolite levels if therapeutic drug monitoring is available; TPMT/NUDT15 genotyping strongly recommended prior to initiation |
| Handling Protection | Cytotoxic drug handling precautions apply — do not crush or split tablets; use protective gloves; pregnant or trying-to-conceive healthcare workers should avoid direct contact; classify as hazardous drug per applicable national guidelines |

---

## Safety Considerations

Philippines-specific prescribing information is unavailable due to the absence of local registration. The following safety concerns are derived from international published literature:

- **Myelosuppression**: Leukopenia is the most clinically significant and potentially fatal adverse effect. NUDT15 c.415C>T variant — which is significantly more prevalent in Filipino and other Southeast Asian populations than in European populations — confers extreme thiopurine sensitivity at standard doses. Pre-treatment NUDT15 genotyping is strongly recommended before initiating azathioprine in the Philippines.
- **Opportunistic infections**: Immunosuppression increases susceptibility to CMV reactivation, *Clostridioides difficile*, and endemic tropical infections. Pre-treatment screening for tuberculosis, hepatitis B (risk of reactivation), and strongyloidiasis is particularly critical in the Philippine tropical disease context.
- **Lymphoproliferative disease**: Long-term thiopurine use carries a small but measurable increased risk of lymphoma, particularly non-Hodgkin's lymphoma and EBV-associated lymphoproliferative disorders, and is amplified when combined with anti-TNF agents.
- **Hepatotoxicity**: Accumulation of the 6-MMP metabolite is associated with elevated transaminases and, rarely, nodular regenerative hyperplasia; LFT monitoring is mandatory throughout treatment.

Please refer to international prescribing information (EMA SmPC or US FDA prescribing information for IMURAN®/Azasan®) and ECCO/ACG IBD guidelines until a local Philippines registration and formal package insert are established.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Azathioprine has Level 1 evidence for IBD — anchored by multiple completed Phase 3 RCTs, four Cochrane systematic reviews spanning 2007–2025, and ECCO/ACG guideline endorsement as a first-line immunomodulator. The complete absence of Philippines registration is a regulatory and market access gap, not a reflection of insufficient evidence. Given the documented rise of IBD in Southeast Asia and the availability of an affordable, well-characterised therapeutic option, a Philippines registration pathway is strongly justified.

**To proceed, the following is needed:**

- **FDA-Ph registration application**: Prepare a complete dossier referencing established international approvals (EMA, US FDA, or TGA) for the IMURAN®/Azasan® reference product; bioequivalence data for any generic submission
- **Local pharmacogenomic screening protocol**: Develop and validate a TPMT/NUDT15 pre-treatment genotyping pathway suitable for Philippines clinical practice, accounting for the higher NUDT15 c.415C>T allele frequency in East/Southeast Asian populations
- **Mechanism of action documentation**: Complete DrugBank API query for azathioprine MOA (currently unavailable in this evidence pack due to data gap)
- **Drug interaction safety review**: Repeat DDI database query with expanded sources (DrugBank, Liverpool IBD Drug Interactions, Drugs.com) — current query returned zero results, which likely reflects a database access gap rather than true absence of interactions
- **Endemic infection pre-treatment screening guideline**: Develop local clinical protocol for TB (IGRA/TST), HBsAg/HBcAb, and strongyloidiasis screening prior to immunosuppression initiation in the Philippines
- **IBD burden of disease assessment**: Quantify the unmet clinical need and patient population size for IBD in the Philippines to support registration and health technology assessment
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

