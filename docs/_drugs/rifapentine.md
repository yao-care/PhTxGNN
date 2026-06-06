---
layout: default
title: Rifapentine
parent: 僅模型預測 (L5)
nav_order: 292
evidence_level: L5
indication_count: 10
---

# Rifapentine
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

# Rifapentine: From Tuberculosis to Leprosy

## One-Sentence Summary

Rifapentine is a rifamycin-class antibiotic used for the treatment of active tuberculosis and prevention of latent tuberculosis infection (LTBI), particularly in combination regimens such as 3HP (weekly rifapentine + isoniazid × 12 weeks).
The TxGNN model predicts it may be effective for **Leprosy (Hansen's disease)**, with **0 registered clinical trials** and **20 publications** — including a landmark 2023 NEJM randomised trial — currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Tuberculosis (active disease and latent infection prevention) |
| Predicted New Indication | Leprosy |
| TxGNN Prediction Score | 99.77% |
| Evidence Level | L1 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available from DrugBank for this report. Based on known class-level pharmacology, rifapentine is a semisynthetic rifamycin antibiotic. Like rifampicin, its bactericidal activity is believed to result from inhibition of bacterial DNA-dependent RNA polymerase (RNAP), blocking transcription and leading to cell death. Rifapentine distinguishes itself from rifampicin through a substantially longer half-life (approximately 14–18 hours versus 2–3 hours for rifampicin), which enables once-weekly or even single-dose prophylaxis dosing — a property highly relevant to leprosy control programmes in low-resource, endemic settings.

Both tuberculosis (*Mycobacterium tuberculosis*) and leprosy (*Mycobacterium leprae*) are mycobacterial diseases, sharing key biological vulnerabilities to rifamycin-class antibiotics. Rifampicin has been a backbone of WHO leprosy multidrug therapy (MDT) since the 1980s, providing strong mechanistic precedent for rifapentine's potential in this indication. Studies in murine footpad models have confirmed that rifapentine demonstrates bactericidal activity against *M. leprae* that is at least comparable to — and in some assays superior to — rifampicin (PMID 10991891, PMID 30207440). The emergence of rifampicin-resistant *M. leprae* strains further elevates interest in alternative rifamycins as replacement agents (PMID 29071280).

Critically, a 2023 NEJM randomised trial (PMID 37195940) directly tested single-dose rifapentine in household contacts of leprosy patients, demonstrating that its greater bactericidal potency in preclinical models translates to a clinically meaningful prevention signal. A 2025 systematic review (PMID 40278757) further contextualises rifapentine within the WHO "Towards Zero Leprosy" chemoprophylaxis strategy. Taken together, the biological rationale is strong and the clinical evidence base is maturing.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for rifapentine + leprosy on ClinicalTrials.gov. Published clinical evidence is captured in the literature section below.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37195940](https://pubmed.ncbi.nlm.nih.gov/37195940/) | 2023 | RCT | N Engl J Med | Single-dose rifapentine in household contacts of leprosy patients; rifapentine showed greater bactericidal activity against *M. leprae* than rifampicin in murine models; provides direct clinical effectiveness data for leprosy post-exposure prophylaxis |
| [40278757](https://pubmed.ncbi.nlm.nih.gov/40278757/) | 2025 | Review | Trop Med Infect Dis | Systematic review of rifamycin-based post-exposure chemoprophylaxis for leprosy; contextualises rifapentine within WHO "Towards Zero Leprosy" strategy following the landmark COLEP study (57% reduction in incidence) |
| [38440733](https://pubmed.ncbi.nlm.nih.gov/38440733/) | 2024 | Review | Front Immunol | Comprehensive review of leprosy treatment, prevention, and immune response; highlights stable incidence despite MDT and emergence of rifampicin-resistant strains as drivers for exploring alternative rifamycins |
| [11201894](https://pubmed.ncbi.nlm.nih.gov/11201894/) | 2000 | Animal Study | Lepr Rev | Rifapentine-moxifloxacin-minocycline (PMM) combination for leprosy; compared bactericidal activities against *M. leprae* in mouse footpad system; PMM suitable for monthly supervised administration |
| [10991891](https://pubmed.ncbi.nlm.nih.gov/10991891/) | 2000 | Animal Study | Antimicrob Agents Chemother | Bactericidal activities of rifapentine, HMR 3647, and moxifloxacin vs *M. leprae* in mice; rifapentine activity compared to rifampicin under single-dose and multi-dose conditions |
| [32936818](https://pubmed.ncbi.nlm.nih.gov/32936818/) | 2020 | Animal Study | PLoS Negl Trop Dis | PEP efficacy of rifapentine and other agents in susceptible-subclinical murine leprosy model; supports selecting drugs for clinical PEP trials |
| [30207440](https://pubmed.ncbi.nlm.nih.gov/30207440/) | 2016 | Animal Study | Indian J Leprosy | Rifapentine combinations tested in murine model of rifampicin-resistant leprosy; RPT + clarithromycin + minocycline showed activity as alternative to current MDT |
| [29071280](https://pubmed.ncbi.nlm.nih.gov/29071280/) | 2017 | Computational | Mol Biol Res Commun | Molecular simulation comparing rifabutin and rifapentine as substitutes for rifampicin in drug-resistant leprosy; findings relevant to programme managers considering alternative rifamycins |
| [37385746](https://pubmed.ncbi.nlm.nih.gov/37385746/) | 2023 | Protocol | BMJ Open | COMBINE trial protocol: population-wide screening + mass drug administration (including rifapentine) for leprosy control in Kiribati hot-spot; evaluates universal prevention vs contact-limited chemoprophylaxis |
| [37907954](https://pubmed.ncbi.nlm.nih.gov/37907954/) | 2023 | Review | Parasites Vectors | Pipeline review for NTD drugs including leprosy; rifapentine identified among off-label anti-infective drugs with Phase ≥2 data applicable to neglected tropical disease control |

---

## Philippines Market Information

Rifapentine is **not currently registered** in the Philippines. There are no FDA Philippines (Food and Drug Administration of the Philippines) authorisations on record.

| Item | Details |
|------|---------|
| Market Status | Not marketed |
| Total Registrations | 0 |
| Note | Any use would require Special Access Route (SAR) or Compassionate Special Permit application to FDA Philippines |

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note on drug interactions**: While formal DDI data was not retrieved in this evidence pack, rifapentine is known to be a potent inducer of CYP3A4 and CYP2B6 enzymes. This is clinically significant when co-administered with antiretroviral drugs (relevant to the HIV/TB co-infection context), calcium channel blockers, and other CYP3A4-metabolised medications. Prescribers managing leprosy patients on concurrent medications should review interaction profiles carefully before use.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A 2023 NEJM randomised trial directly tested single-dose rifapentine in household contacts of leprosy patients, and multiple preclinical studies confirm bactericidal activity against *Mycobacterium leprae* that equals or exceeds rifampicin — the current MDT backbone. The biological rationale is robust (shared mycobacterial target, established rifamycin class activity in leprosy), and the WHO "Towards Zero Leprosy" strategy explicitly includes rifamycin-based chemoprophylaxis as a prevention pillar.

**To proceed, the following is needed:**

- **Philippines regulatory access**: Rifapentine is not registered locally; a Special Access Route (SAR) or Compassionate Special Permit application to FDA Philippines is required before clinical use
- **Mechanism of action data**: Obtain full DrugBank MOA entry for package insert-level documentation
- **TFDA package insert review**: Download and parse safety warnings, contraindications, and special population guidance (the Blocking data gap DG001) to enable full safety screening
- **Drug interaction assessment**: Evaluate rifapentine's CYP3A4/2B6 induction profile against any concurrent medications in target patients (particularly in HIV-coinfected individuals or patients on calcium channel blockers used for leprosy-related neuropathic complications)
- **Resistance monitoring plan**: Given documented rifampicin-resistant *M. leprae* strains, a cross-resistance assessment and local susceptibility surveillance plan should accompany any new rifapentine deployment
- **Dosing protocol for leprosy**: Confirm whether single-dose (post-exposure prophylaxis) or multi-dose regimen (active disease) is the target; each requires distinct evidence review and regulatory framing
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

