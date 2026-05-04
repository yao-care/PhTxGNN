---
layout: default
title: Aztreonam
parent: 僅模型預測 (L5)
nav_order: 35
evidence_level: L5
indication_count: 10
---

# Aztreonam
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

# Aztreonam: From Gram-Negative Bacterial Infections to Gonococcal Urethritis

## One-Sentence Summary

Aztreonam is a monobactam β-lactam antibiotic used internationally to treat gram-negative bacterial infections, though it currently holds no market authorization in Taiwan.
The TxGNN model predicts it may be effective for **Gonococcal Urethritis**,
with **1 clinical trial** and **8 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Gram-negative bacterial infections (no Taiwan registration data available) |
| Predicted New Indication | Gonococcal Urethritis |
| TxGNN Prediction Score | 99.59% |
| Evidence Level | L2 |
| Taiwan Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Aztreonam is a synthetic monobactam antibiotic with a monocyclic β-lactam ring — a structure unique among β-lactam antibiotics. Although detailed mechanism of action data was not retrievable in this evidence pack (DrugBank API query gap), the drug's well-established pharmacological class defines it as a PBP3 (penicillin-binding protein 3) inhibitor that blocks gram-negative bacterial cell wall synthesis. Crucially, its monocyclic structure renders it inactive against gram-positive organisms and anaerobes, giving it a spectrum exclusively targeting aerobic gram-negative bacteria.

*Neisseria gonorrhoeae*, the causative agent of gonococcal urethritis, is a gram-negative diplococcus — precisely the category of organism Aztreonam is mechanistically equipped to target. Its PBP3 dependence for cell wall integrity makes it susceptible to Aztreonam's mode of action. Beyond susceptibility, Aztreonam also retains activity against penicillinase-producing *N. gonorrhoeae* (PPNG) strains, which are resistant to conventional penicillin therapy. This is clinically significant, as the CDC has designated antimicrobial-resistant *N. gonorrhoeae* as one of the three most urgent AMR threats nationally.

The repurposing rationale is therefore not merely a computational prediction — it is mechanistically direct and fills a genuine unmet clinical need. As *N. gonorrhoeae* progressively develops resistance to ceftriaxone (the current last-resort first-line agent), Aztreonam represents a pharmacologically sound, evidence-backed reserve option that operates through the same β-lactam-PBP3 pathway with an alternative structural scaffold.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03867734](https://clinicaltrials.gov/study/NCT03867734) | Phase 2/3 | Completed | 32 | Open-label single-arm trial of Aztreonam 2 g IM for pharyngeal *N. gonorrhoeae* infection; designed specifically to evaluate repurposed antibiotics for AMR gonorrhea; conducted at an STI clinic between April–September 2019. Published results available (PMID 33077658). |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [33077658](https://pubmed.ncbi.nlm.nih.gov/33077658/) | 2020 | Prospective Single-arm Clinical Trial | Antimicrobial Agents and Chemotherapy | 2 g IM single-dose Aztreonam for pharyngeal and urogenital gonorrhea; enrolled men at an STI clinic; directly demonstrates clinical utility as a repurposed agent for ceftriaxone-resistant gonorrhea alternatives. |
| [3157346](https://pubmed.ncbi.nlm.nih.gov/3157346/) | 1985 | Comparative Clinical Study | Antimicrobial Agents and Chemotherapy | Aztreonam 1 g IM vs. spectinomycin 2 g IM for uncomplicated gonorrhea; zero treatment failures with either agent across urethral, rectal, and endocervical infection sites. |
| [3095216](https://pubmed.ncbi.nlm.nih.gov/3095216/) | 1986 | Clinical Trial (Historical) | Genitourinary Medicine | Aztreonam 1 g single IM dose cleared *N. gonorrhoeae* at all sites in 61 men and 26 women (one pharyngeal failure in a bisexual male); effective against both penicillin-sensitive and -resistant strains; well tolerated with no adverse effects. |
| [6225808](https://pubmed.ncbi.nlm.nih.gov/6225808/) | 1983 | Clinical Study | Journal of Infectious Diseases | Early evaluation of Aztreonam activity against PPNG; demonstrated efficacy when both penicillin and spectinomycin resistance had emerged, establishing Aztreonam as a viable alternative. |
| [3937450](https://pubmed.ncbi.nlm.nih.gov/3937450/) | 1985 | Epidemiological + Therapeutic Study | Acta Urologica Japonica | One-shot Aztreonam therapy evaluated across 244 clinical *N. gonorrhoeae* isolates in a Japanese cohort; 17.2% PPNG rate documented; assessed both epidemiology and treatment outcomes. |
| [6438364](https://pubmed.ncbi.nlm.nih.gov/6438364/) | 1984 | Clinical Evaluation | Japanese Journal of Antibiotics | 30 male patients with gonococcal urethritis treated with Aztreonam in a Tokyo hospital; bacteriological evaluation of 61 strains including 9 PPNG strains (15%); assessed clinical and microbiological cure rates. |
| [6226596](https://pubmed.ncbi.nlm.nih.gov/6226596/) | 1983 | Clinical Study | Giornale Italiano di Dermatologia e Venereologia | Early Italian clinical evaluation of Aztreonam in acute gonococcal urethritis; one of the earliest reports of monobactam use in gonorrhea. |
| [11406757](https://pubmed.ncbi.nlm.nih.gov/11406757/) | 2001 | Microbiological Surveillance | Journal of Infection and Chemotherapy | Critical resistance surveillance report: documents emergence of cephem- and Aztreonam-high-resistant *N. gonorrhoeae* strains without β-lactamase production; provides important context for monitoring MIC thresholds. |

---

## Taiwan Market Information

Aztreonam currently has **no registered products in Taiwan**. The Taiwan FDA database returned 0 approved licenses, and the drug's market status is **Not Marketed (未上市)**. Any clinical use in Taiwan would require regulatory authorization prior to procurement or formulary inclusion.

---

## Safety Considerations

Please refer to the package insert for safety information. Detailed warnings, contraindications, and drug interaction data were not available in this evidence pack (Taiwan FDA package insert and DrugBank safety queries both returned no data). Retrieving the full prescribing information from the originator product label (e.g., Azactam) is required before proceeding to clinical evaluation.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 2/3 clinical trial (NCT03867734) combined with eight supporting publications — spanning four decades of clinical use from 1983 to 2020, across multiple countries — provides L2-level evidence for Aztreonam's efficacy in gonococcal urethritis. The mechanistic alignment is the strongest possible (★★★★★): Aztreonam's PBP3-inhibiting monobactam mechanism is directly applicable to *N. gonorrhoeae* biology, and the urgent AMR resistance landscape for gonorrhea independently validates the public health imperative for this repurposing direction.

**To proceed, the following is needed:**

- **Unblock DG001** — Download and parse the Taiwan FDA package insert (仿單 PDF) to obtain complete safety warnings and contraindications; this is a blocking data gap for formal safety review
- **Unblock DG002** — Query DrugBank API for complete mechanism of action and pharmacology data to strengthen mechanistic documentation
- **Resistance profile assessment** — Review contemporary Taiwan/Asia-Pacific surveillance data for *N. gonorrhoeae* aztreonam MIC trends, since the 2001 paper (PMID 11406757) already documented high-resistance emergence
- **Route and formulation confirmation** — Confirm availability of parenteral (IM) formulation, as the clinical trials used 1–2 g IM single-dose; no oral aztreonam is currently approved
- **Regulatory feasibility review** — Assess the pathway for Taiwan market authorization, given zero current registrations; consider whether compassionate use or expanded access mechanisms may apply in the interim
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

