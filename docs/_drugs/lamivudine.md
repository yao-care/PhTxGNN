---
layout: default
title: Lamivudine
parent: 僅模型預測 (L5)
nav_order: 195
evidence_level: L5
indication_count: 5
---

# Lamivudine
{: .fs-9 }

證據等級: **L5** | 預測適應症: **5** 個
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

Using the `txgnn-pipeline` skill to guide report generation for this evidence pack. Since this skill is not available as a deferred tool, I will proceed directly with the report based on the system prompt instructions.

---

# Lamivudine: From HIV/HBV Antiretroviral to Simian Immunodeficiency Virus Infection

## One-Sentence Summary

Lamivudine (3TC) is a well-established nucleoside reverse transcriptase inhibitor (NRTI) used in the treatment of HIV-1 infection and chronic hepatitis B, though no formal Philippines registration data was captured in this evidence pack.
The TxGNN model's top-ranked prediction is **Simian Immunodeficiency Virus (SIV) infection**, with a prediction score of **99.93%**,
supported by **0 clinical trials** and **20 publications** — all of which are non-human primate animal studies with no direct human clinical application.

> ⚠️ **Critical Note:** All 5 predicted indications in this pack are either non-human animal diseases (SIV, FIV), a rare neurological disorder with zero supporting literature, an obsolete disease ontology term, or a mechanistically mismatched target (HCV). None represents a viable human drug repurposing opportunity in its current form.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 infection and chronic hepatitis B (established clinical use; no Philippines regulatory record captured) |
| Predicted New Indication | Simian immunodeficiency virus infection |
| TxGNN Prediction Score | 99.93% |
| Evidence Level | L4 |
| Philippines Market Status | Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Lamivudine is a cytidine analogue NRTI. Although detailed mechanism of action data was not captured in this evidence pack, Lamivudine's pharmacology is well established: it competitively inhibits HIV-1 reverse transcriptase (RT) and HBV DNA polymerase, acting as a chain terminator after intracellular phosphorylation to its active triphosphate form. Resistance emerges rapidly via the M184V substitution in RT, which is the canonical marker of 3TC resistance.

SIV (simian immunodeficiency virus) is the non-human primate equivalent of HIV, sharing closely homologous RT sequences. This structural similarity fully explains the TxGNN prediction: the M184V resistance mutation has been directly replicated in SIVmac251-infected macaque models under 3TC therapy, confirming that Lamivudine's mechanism is active against SIV reverse transcriptase. Multiple animal studies further demonstrate that Lamivudine, as part of HAART regimens, suppresses SIV viremia and tissue reservoirs in macaques.

However, this prediction carries **no clinical repurposing value for human medicine**. SIV is a disease of non-human primates and does not infect or cause disease in humans. The TxGNN model's high prediction score almost certainly reflects structural proximity between HIV and SIV nodes within the knowledge graph — a biologically accurate relationship, but one without translatable therapeutic significance. The same pattern applies to the second-ranked prediction (feline immunodeficiency virus/FIV), which is similarly a veterinary-only disease. The remaining three predicted indications (a rare neurological disorder with zero evidence, an obsolete ontology term for hyperlipidemia, and chronic HCV — for which Lamivudine has no known direct antiviral mechanism) further confirm that this evidence pack does not identify actionable repurposing targets.

---

## Clinical Trial Evidence

Currently no related clinical trials registered for Lamivudine in simian immunodeficiency virus infection.

---

## Literature Evidence

All 20 retrieved publications are non-human primate animal studies or basic science. None involves human subjects for SIV treatment.

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [19240457](https://pubmed.ncbi.nlm.nih.gov/19240457/) | 2009 | Animal Study | AIDS (London) | ZDV + 3TC + Indinavir post-exposure prophylaxis prevented vaginal SIV transmission in macaques |
| [12021341](https://pubmed.ncbi.nlm.nih.gov/12021341/) | 2002 | Animal/Basic Science | J Virology | M184V RT mutation emerged within 5 weeks in SIVmac251-infected newborn macaques on 3TC therapy — directly mirrors HIV-1 resistance pattern |
| [12502828](https://pubmed.ncbi.nlm.nih.gov/12502828/) | 2003 | Animal/Basic Science | J Virology | Tenofovir selects for M184V reversion in SIV even with concurrent 3TC; evaluated in SIV macaque model |
| [16973590](https://pubmed.ncbi.nlm.nih.gov/16973590/) | 2006 | Animal Study | J Virology | Quadruple ART including 3TC achieved rapid SIV viral decay in cynomolgus macaques; dynamics modelled mathematically |
| [15919889](https://pubmed.ncbi.nlm.nih.gov/15919889/) | 2005 | Animal Study | J Virology | Lamivudine + efavirenz + tenofovir HAART suppressed RT-SHIV plasma viral RNA by >4 log in all 7 treated rhesus macaques |
| [20868521](https://pubmed.ncbi.nlm.nih.gov/20868521/) | 2010 | Animal Study | Retrovirology | Early initiation of HAART (including 3TC) reduced SIV tissue reservoir establishment in macaques; timing-dependent effect |
| [22615988](https://pubmed.ncbi.nlm.nih.gov/22615988/) | 2012 | Animal Study | PLoS One | HAART (including 3TC) impacted SIV infection in male genital tract of macaques; persistent shedding from local reservoirs |
| [14610172](https://pubmed.ncbi.nlm.nih.gov/14610172/) | 2003 | Animal Study | J Virology | Short-term AZT + 3TC + Indinavir HAART initiated 4 h post-SIV exposure altered lymphocyte proliferation kinetics |
| [11689641](https://pubmed.ncbi.nlm.nih.gov/11689641/) | 2001 | Animal Study | J Virology | HAART (with 3TC) reduced SHIV viremia but did not normalize early bone marrow hematopoiesis defect in macaques |
| [15040537](https://pubmed.ncbi.nlm.nih.gov/15040537/) | 2004 | In Vitro | Antiviral Therapy | Comparative susceptibility of HIV-2, SIV (mac251/B670) and SHIV to 16 approved antiretrovirals including Lamivudine; informs PEP guidance |

---

## Philippines Market Information

Lamivudine is currently **not registered** with the Philippines FDA. No authorization records are available in this evidence pack.

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|-------------------|
| — | No registered products found | — | — |

---

## Safety Considerations

Please refer to the package insert for safety information. Philippines FDA package insert data was not captured in this evidence pack, and all key warning and contraindication fields returned no data.

For reference, clinicians should consult internationally recognized prescribing information (e.g., WHO/US FDA label) which documents known NRTI class effects including lactic acidosis, hepatomegaly with steatosis, and exacerbation of hepatitis B upon discontinuation.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
All five TxGNN-predicted indications for Lamivudine lack viable human repurposing value: the top two are non-human animal diseases (SIV in macaques, FIV in domestic cats), the third has zero supporting clinical or preclinical literature in humans, the fourth uses an obsolete ontology term with no modern disease correlate, and the fifth (chronic HCV) is mechanistically incompatible — Lamivudine targets RT/DNA polymerase, not HCV NS5B RNA polymerase. The prediction pipeline appears to have correctly identified Lamivudine's strong RT-inhibitory profile but mapped it predominantly to non-human retroviral disease nodes.

**To move forward, the following steps are recommended:**

- **Re-examine the full TxGNN prediction output** for human-relevant indications that may have ranked below these animal disease predictions (e.g., HIV-associated complications, HBV-related outcomes, LINE-1-driven inflammatory diseases such as Aicardi-Goutières syndrome — where NRTI use has emerging clinical trial support)
- **Filter non-human disease ontology terms** from the TxGNN prediction pipeline output; SIV and FIV nodes should be excluded from human drug repurposing analysis by design
- **Retrieve Philippines FDA registration data** directly from the FDA Philippines official database to confirm whether Lamivudine products are marketed under any approved brand names (Epivir, Zeffix, or fixed-dose combinations such as Combivir, Triumeq, Dovato) which may not have been captured in the current query
- **Obtain the complete package insert** (Philippines or WHO-INN reference label) to populate safety fields currently missing (key warnings, contraindications, DDI profile)
- **Verify original indication data** — the `original_indications` field is empty, which is a data pipeline gap; Lamivudine has WHO Essential Medicine status for HIV and HBV and should have known approved indications recorded
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

