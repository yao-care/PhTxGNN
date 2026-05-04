---
layout: default
title: Efavirenz
parent: 僅模型預測 (L5)
nav_order: 119
evidence_level: L5
indication_count: 3
---

# Efavirenz
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

# Efavirenz: From HIV-1 Infection to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Efavirenz is a non-nucleoside reverse transcriptase inhibitor (NNRTI) established for the treatment of HIV-1 infection, acting by non-competitively blocking the viral reverse transcriptase enzyme. The TxGNN model predicts it may have activity against **Simian Immunodeficiency Virus (SIV) Infection**, supported by **1 clinical trial** (subsequently withdrawn, enrollment 0) and **16 publications**, the majority of which are animal studies conducted in RT-SHIV chimeric macaque models rather than natural SIV disease. The mechanistic bridge to native SIV is structurally weak, placing this prediction in the category of a research model finding rather than an actionable clinical repurposing target.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection (NNRTI class antiviral) |
| Predicted New Indication | Simian Immunodeficiency Virus Infection |
| TxGNN Prediction Score | 99.80% |
| Evidence Level | L3 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why Is This Prediction Reasonable?

Currently, formal mechanism of action data is not recorded in this evidence pack. Based on known pharmacology and the mechanistic analysis embedded in the retrieved evidence, Efavirenz is an NNRTI that specifically occupies the allosteric non-nucleoside inhibitor binding pocket (NNIBP) on HIV-1 reverse transcriptase (RT), preventing RNA-to-DNA transcription required for viral replication. Its potency is tightly coupled to the shape and electrostatic environment of this pocket — a feature that is characteristic of HIV-1 RT but not conserved across all lentiviruses.

Simian immunodeficiency virus (SIV) is phylogenetically related to HIV-1 but encodes its own RT with key differences at the residues (positions corresponding to Y181, Y188, K103 in HIV-1 RT) that define NNRTI sensitivity. Natural SIV strains are therefore largely resistant to NNRTIs including efavirenz. The published evidence for efavirenz–SIV activity relies almost entirely on **RT-SHIV chimeric constructs** — experimental viruses where the SIV genomic backbone carries an HIV-1 RT insert — enabling efavirenz to act via its established HIV-1 RT mechanism in macaque hosts. This is a well-validated animal model for studying HIV therapy but represents a research tool application, not a genuine cross-species indication.

In summary, while the TxGNN knowledge graph captures the biological neighborhood linking HIV-1 therapy nodes to SIV research nodes, the mechanistic connection for efavirenz directly treating natural SIV infection is weak. This prediction is best interpreted as the model detecting efavirenz's utility in **HIV primate model systems**, not as an independent clinical repurposing target for SIV disease.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00863668](https://clinicaltrials.gov/study/NCT00863668) | N/A | Withdrawn | 0 | Investigated HIV RNA decay kinetics using raltegravir (integrase inhibitor) in HIV-infected patients; references SIV macaque comparisons as contextual background, but is entirely unrelated to efavirenz or direct SIV therapy. Withdrawn before any participants enrolled. |

> **Note:** The single retrieved trial was withdrawn with zero enrollment and represents a database ontology mismatch (HIV ↔ SIV cross-tagging). It provides no clinical evidence for efavirenz in SIV infection.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|------|---------|
| [15328115](https://pubmed.ncbi.nlm.nih.gov/15328115/) | 2004 | Animal Study | Antimicrob Agents Chemother | Directly evaluated efavirenz antiviral activity in RT-SHIV–infected rhesus macaques; demonstrated suppression of the chimeric virus, validating RT-SHIV as an NNRTI testing model |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In Vitro | Antiviral Therapy | Screened 16 antiretrovirals against HIV-2, native SIV (mac251, B670), and SHIV strains; efavirenz showed minimal activity against native SIV (no HIV-1 RT) — a critical negative finding for this indication |
| [15564466](https://pubmed.ncbi.nlm.nih.gov/15564466/) | 2004 | In Vitro | J Virology | In vitro characterization of RT-SHIV chimera susceptibility to NNRTIs including efavirenz; established dose-response parameters for this model system |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Animal Study | J Virology | HAART combination (efavirenz + lamivudine + tenofovir) reduced plasma RT-SHIV viral RNA by >4 logs in rhesus macaques; established the NHP HAART model for AIDS research |
| [19195672](https://pubmed.ncbi.nlm.nih.gov/19195672/) | 2009 | Animal Study | Virology | Characterized vaginal transmission of RT-SHIV in Chinese rhesus macaques with persistent viremia; NNRTI activity assessed in a mucosal exposure context |
| [19889213](https://pubmed.ncbi.nlm.nih.gov/19889213/) | 2009 | Animal Study | Retrovirology | Tracked RT-SHIV subpopulation dynamics under short-course efavirenz monotherapy followed by combination ART in pigtail macaques; resistance dynamics characterized |
| [24777106](https://pubmed.ncbi.nlm.nih.gov/24777106/) | 2014 | Animal Study | Antimicrob Agents Chemother | Enhanced 4–5 drug HAART regimens including efavirenz in RT-SHIV macaques; demonstrated improved early viral decay kinetics compared with standard regimens |
| [35856680](https://pubmed.ncbi.nlm.nih.gov/35856680/) | 2022 | Pharmacology / Imaging | Antimicrob Agents Chemother | Mass spectrometry imaging of efavirenz and 5 other ARVs in NHP spleen tissue; mapped spatial relationship between drug distribution, viral RNA, and fibrosis markers in tissue reservoirs |
| [21084490](https://pubmed.ncbi.nlm.nih.gov/21084490/) | 2011 | Molecular | J Virology | Analyzed SIV/HIV-1 RT genetic diversity before, during, and after ART in macaques; efavirenz monotherapy enabled characterization of resistance mutation emergence |
| [22933296](https://pubmed.ncbi.nlm.nih.gov/22933296/) | 2012 | Molecular | J Virology | Ultrasensitive allele-specific PCR detected pre-existing drug-resistant RT variants in RT-SHIV macaques; quantified efavirenz resistance mutation frequency at baseline |

---

## Philippines Market Information

Efavirenz is **not currently registered in the Philippines**. No active drug license records are available (total registrations: 0).

> For reference, Efavirenz is approved by the U.S. FDA (as Sustiva®) and is included in WHO Essential Medicines Lists for HIV/AIDS treatment. A Philippines regulatory application would require submission to the Food and Drug Administration (FDA Philippines) under RA 9711.

---

## Safety Considerations

Please refer to the package insert for complete safety information.

> Safety data (key warnings, contraindications, drug interactions) were not available in the current evidence pack. Clinicians should note that efavirenz is associated with CNS adverse effects (vivid dreams, dizziness, neuropsychiatric events), is a CYP3A4 inducer with significant drug-drug interaction potential, and carries teratogenicity warnings — all warranting formal review before any clinical application.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN prediction for efavirenz in SIV infection reflects its established role in RT-SHIV chimeric animal models — powerful research tools for HIV therapy development — rather than a genuine new clinical indication. The critical in vitro evidence (PMID 15040537) confirms that efavirenz has minimal activity against native SIV strains lacking HIV-1 RT, and the only retrieved clinical trial was withdrawn before enrolling any participants. There is no direct path from this prediction to a human health application.

**Additional Predicted Indications:**

| Rank | Indication | Evidence Level | Decision |
|------|-----------|---------------|---------|
| 2 | Feline Acquired Immunodeficiency Syndrome (FIV) | L4 | Hold |
| 3 | Neurodevelopmental Disorder with Ataxic Gait, Absent Speech, and Decreased Cortical White Matter | L5 | Hold |

The FIV prediction has a biochemical rationale — PMID 38031646 directly compared NNRTIs against FIV-RT vs. HIV-RT — but significant structural divergence at the NNIBP pocket limits efavirenz efficacy against FIV-RT. The neurodevelopmental disorder prediction is purely model-generated (L5) with zero supporting evidence and should not be pursued.

**To proceed with any further evaluation, the following would be needed:**

- Structural crystallography or molecular docking data confirming whether efavirenz can engage native SIV-RT or FIV-RT at the NNIBP
- In vitro efficacy data against unmodified SIV strains (excluding RT-SHIV chimeras)
- Definition of the intended use context — veterinary application (FIV in cats), primate research tool (SIV models), or translational HIV research — each requiring a separate regulatory and ethical pathway
- Philippines FDA registration pathway assessment; no current licenses exist as a starting point
- Complete safety profile documentation (MOA, TFDA label warnings, contraindications, DDI profile) to enable any formal safety stage evaluation
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

