---
layout: default
title: Dolutegravir
parent: 僅模型預測 (L5)
nav_order: 113
evidence_level: L5
indication_count: 3
---

# Dolutegravir
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

# Dolutegravir: From HIV-1 Infection to Feline Acquired Immunodeficiency Syndrome

## One-Sentence Summary

Dolutegravir (DTG) is a second-generation integrase strand transfer inhibitor (INSTI) established for human HIV-1 treatment, acting by blocking viral DNA integration into the host genome.
The TxGNN model predicts it may be effective for **Feline Acquired Immunodeficiency Syndrome (Feline AIDS)** caused by Feline Immunodeficiency Virus (FIV),
with **5 clinical trials** (all indirect human HIV-1 studies, computationally cross-classified) and **1 direct veterinary publication** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | HIV-1 Infection (antiretroviral therapy; inferred from clinical trial context — no Philippines regulatory record available) |
| Predicted New Indication | Feline Acquired Immunodeficiency Syndrome |
| TxGNN Prediction Score | 99.85% |
| Evidence Level | L4 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available from the DrugBank data pipeline (recorded as a High-severity data gap). However, based on information present within the Evidence Pack, Dolutegravir belongs to the integrase strand transfer inhibitor (INSTI) class of antiretrovirals. DTG inhibits HIV-1 replication by chelating divalent metal ions (Mg²⁺/Mn²⁺) at the active site of the viral integrase enzyme through a diketoacid (DKA) pharmacophore, thereby blocking the strand transfer step of viral DNA integration into the host chromosome. This two-metal-ion chelation mechanism confers a notably high genetic barrier to resistance compared to first-generation INSTIs such as raltegravir and elvitegravir.

Feline Immunodeficiency Virus (FIV), the causative agent of Feline AIDS, belongs to the same *Lentivirus* genus as HIV-1. The FIV integrase shares approximately **40% amino acid sequence similarity** with HIV-1 integrase, with the catalytic core domain — including the conserved DDE motif that coordinates the active-site metal ions — being structurally homologous. This conservation is the primary rationale behind the TxGNN model's prediction: DTG's DKA pharmacophore may engage the FIV integrase active site in a mechanistically analogous manner to its action on HIV-1 integrase.

The prediction gains direct experimental support from a 2023 veterinary pharmacology study (PMID 37112803) which administered DTG-containing combination antiretroviral therapy (cART: DTG 2.5 mg/kg + tenofovir 20 mg/kg + emtricitabine 40 mg/kg) to FIV-infected domestic cats, evaluating both pharmacokinetics and immunophenotypic outcomes. This represents the only directly relevant clinical evidence. Significant knowledge gaps remain, particularly regarding feline-specific pharmacokinetics (protein binding rates, plasma half-life, and CYP metabolism profiles differ substantially between cats and humans), which must be resolved before clinical application.

---

## Clinical Trial Evidence

> ⚠️ **Data Quality Notice**: All 5 trials below are human HIV-1 studies. They were computationally cross-classified under the "feline acquired immunodeficiency syndrome" indication based on mechanistic overlap (shared lentiviral integrase pharmacology), and serve as **indirect mechanistic evidence only**. They do not count toward direct feline clinical trial evidence. No dedicated feline AIDS clinical trials are currently registered on ClinicalTrials.gov.

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT01263015](https://clinicaltrials.gov/study/NCT01263015) | Phase 3 | Completed | 844 | SINGLE trial: DTG 50 mg + ABC/3TC once daily vs. EFV/TDF/FTC (Atripla) in ART-naïve HIV-1 adults over 96 weeks; established DTG non-inferiority and supports integrase inhibition efficacy as a drug class |
| [NCT01227824](https://clinicaltrials.gov/study/NCT01227824) | Phase 3 | Completed | 828 | SPRING-2 trial: DTG 50 mg once daily vs. raltegravir 400 mg twice daily in ART-naïve HIV-1 adults; DTG demonstrated non-inferior antiviral activity with a favourable resistance profile across lentiviral integrase inhibitor class |
| [NCT01231516](https://clinicaltrials.gov/study/NCT01231516) | Phase 3 | Completed | 724 | DTG 50 mg once daily vs. raltegravir in ART-experienced, integrase-naïve HIV-1 adults; confirmed DTG efficacy in the treatment-experienced setting |
| [NCT00951015](https://clinicaltrials.gov/study/NCT00951015) | Phase 2 | Completed | 208 | Phase IIb dose-selection study establishing DTG 50 mg QD as the optimal human dose; provides indirect PK context for future cross-species allometric dose extrapolation |
| [NCT01499199](https://clinicaltrials.gov/study/NCT01499199) | Phase 3 | Completed | 13 | CNS/plasma PK study: DTG 50 mg + ABC/3TC in HIV-1 ART-naïve subjects; CSF/plasma Kp,uu ≈ 0.32, indicating moderate CNS penetration — indirectly relevant to FIV-associated neurological pathology assessment |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37112803](https://pubmed.ncbi.nlm.nih.gov/37112803/) | 2023 | Veterinary Clinical / Observational | *Viruses* | **Only direct feline evidence**: cART regimen (DTG 2.5 mg/kg + tenofovir 20 mg/kg + emtricitabine 40 mg/kg) administered to FIV-infected specific-pathogen-free domestic cats; evaluated pharmacokinetics and CD4/CD8 immunophenotypic changes — critical baseline data for any future feline efficacy trial |

---

## Philippines Market Information

Dolutegravir currently holds **no drug registrations** with the Philippine FDA and is classified as **not marketed** in the Philippines. There are no active authorisation numbers, licensed products, or approved indications on record. Any clinical or veterinary application in the Philippines would require a new drug registration or compassionate use application.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note**: Two blocking data gaps were identified in this Evidence Pack. TFDA package insert warnings and contraindications (DG001, Blocking severity) and DrugBank mechanism of action data (DG002, High severity) were not retrieved. One specific safety signal identified in the mechanistic literature is DTG's known interference with folate (one-carbon) metabolism, associated with elevated neural tube defect risk in periconceptional exposure (Botswana pregnancy cohort data). This is of particular relevance to the rank 3 neurodevelopmental indication assessment (see below).

---

## Additional Predicted Indications

### Rank 2 — Simian Immunodeficiency Virus (SIV) Infection

| Item | Content |
|------|---------|
| TxGNN Score | 99.85% |
| Evidence Level | L3 |
| Recommended Decision | Proceed with Guardrails |

The SIV prediction rests on a mechanistically stronger foundation than the feline AIDS prediction. SIV integrase shares **>60% amino acid sequence similarity** with HIV-1 integrase in the catalytic core domain, and cryo-EM/X-ray structural studies of HIV/SIV intasome complexes (PMID 32506843) have directly confirmed DTG's binding mode is conserved across these viruses. This indication has dual application value: (1) as a translational HIV research model in non-human primates (NHPs), and (2) for conservation veterinary medicine in captive great apes infected with SIVcpz.

**Supporting literature** (up to 10 key publications):

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [30381490](https://pubmed.ncbi.nlm.nih.gov/30381490/) | 2019 | Animal Study (NHP/PK-PD) | *Journal of Virology* | DTG monotherapy in SIV-infected macaques: rapid viral suppression confirmed, but resistance mutations selected under monotherapy pressure; supports use within combination regimens |
| [26150024](https://pubmed.ncbi.nlm.nih.gov/26150024/) | 2016 | Animal Study (NHP/cART) | *AIDS Research and Human Retroviruses* | DTG-containing cART regimens effectively suppress SIVmac239 replication in rhesus macaques to clinically relevant levels; validates NHP model for HIV cure research |
| [36365101](https://pubmed.ncbi.nlm.nih.gov/36365101/) | 2022 | Animal Study (NHP/Longitudinal PK) | *Pharmaceutics* | Long-term PK validation of DTG + TDF + FTC in SIVmac251-infected NHPs; critical pharmacological data confirming drug exposures achievable in the NHP model |
| [32506843](https://pubmed.ncbi.nlm.nih.gov/32506843/) | 2021 | Structural Biology / Mechanistic Review | *The FEBS Journal* | Intasome crystal and cryo-EM structures confirm DTG binding to SIV integrase; mechanistically explains the high genetic barrier to resistance for second-generation INSTIs |
| [26378179](https://pubmed.ncbi.nlm.nih.gov/26378179/) | 2015 | In Vitro Resistance Phenotyping | *Journal of Virology* | SIVmac239 susceptible to DTG; INSTI resistance mutation profiles in SIV mirror HIV-1 patterns, validating SIV as a drug resistance model |
| [28576126](https://pubmed.ncbi.nlm.nih.gov/28576126/) | 2017 | Case Report (Conservation Veterinary) | *Retrovirology* | Successful ART treatment of SIVcpz-induced immunodeficiency in a captive western chimpanzee; proof-of-concept for great ape conservation medicine application |
| [34903055](https://pubmed.ncbi.nlm.nih.gov/34903055/) | 2021 | Animal Study (NHP/CNS Reservoir) | *mBio* | Lentiviral CNS reservoirs persist despite ART across HIV/SIV models; relevant for evaluating DTG CNS penetration adequacy in SIV-infected NHPs |
| [32166319](https://pubmed.ncbi.nlm.nih.gov/32166319/) | 2020 | In Vitro Safety / Metabolic | *Clinical Infectious Diseases* | DTG and raltegravir exhibit proadipogenic and profibrotic effects and induce insulin resistance in human/simian adipose tissue; metabolic safety signal requiring monitoring in long-term NHP use |
| [40093003](https://pubmed.ncbi.nlm.nih.gov/40093003/) | 2025 | Animal Study (NHP/CNS Imaging) | *Frontiers in Immunology* | DTG-containing cART modulates CNS white matter tract deficits in SIV-infected rhesus macaques; provides neuroimaging data relevant to CNS reservoir assessment |
| [28923862](https://pubmed.ncbi.nlm.nih.gov/28923862/) | 2017 | In Vitro / Comparative Pharmacology | *Antimicrobial Agents and Chemotherapy* | Bictegravir and cabotegravir activity against INSTI-resistant SIVmac239; comparative context establishing DTG's position within the INSTI resistance landscape for SIV |

---

### Rank 3 — Neurodevelopmental Disorder with Ataxic Gait, Absent Speech, and Decreased Cortical White Matter

| Item | Content |
|------|---------|
| TxGNN Score | 99.80% |
| Evidence Level | L5 |
| Recommended Decision | Hold |

**This prediction is assessed as a likely computational false positive.** No clinical trials or supporting literature were identified (0/0). The described phenotype — progressive ataxic gait, absent speech, and cortical white matter loss — is characteristic of genetic leukodystrophies (e.g., POLR3-related disorders, mitochondrial leukoencephalopathy) or inborn errors of metabolism, conditions requiring targeted gene- or enzyme-based therapies with no plausible mechanistic link to integrase inhibition.

Furthermore, DTG carries a known **safety signal in this disease context**: documented interference with folate/one-carbon metabolism raises neural tube defect risk and potential neurodevelopmental toxicity. This constitutes a contraindication concern rather than a therapeutic rationale for a CNS developmental disorder. The high TxGNN score (0.9980) in the absence of any experimental support is treated as a model artefact requiring hypothesis-generation studies before further evaluation.

---

## Conclusion and Next Steps

### Primary Indication — Feline Acquired Immunodeficiency Syndrome

**Decision: Hold**

**Rationale:**
The mechanistic basis is plausible (~40% FIV/HIV integrase homology) and is supported by a single 2023 veterinary study, but the overall evidence base (L4) is insufficient for a repurposing decision — no controlled feline efficacy trial exists, and feline-specific PK/safety data is critically absent.

**To proceed, the following is needed:**
- Feline-specific multi-dose PK study to validate the 2.5 mg/kg/day dose from PMID 37112803 and establish appropriate therapeutic drug monitoring thresholds
- Randomised controlled efficacy trial in FIV-positive cats with virological and immunological endpoints
- Long-term feline safety data (hepatotoxicity panel, haematology, neurological monitoring)
- Assessment of veterinary pharmaceutical registration pathway under the Philippine FDA

---

### Secondary Indication — Simian Immunodeficiency Virus Infection

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple NHP animal studies and structural biology evidence (L3) support DTG-containing cART efficacy against SIV, with the mechanistic basis substantially stronger than for the feline indication. The primary application context is translational HIV research and conservation medicine for captive great apes.

**To proceed, the following is needed:**
- Species-specific PK characterisation for great apes (chimpanzee, gorilla) if conservation medicine application is pursued
- Structured compassionate use or research protocol for SIVcpz-infected captive chimpanzees in collaboration with zoo/sanctuary veterinary programmes
- Metabolic safety monitoring plan (lipid panel, fasting glucose, adipose tissue assessment) given the proadipogenic safety signal identified in simian adipose tissue studies (PMID 32166319)
- Resistance monitoring protocol given the documented selection pressure under DTG monotherapy in macaques (PMID 30381490)

---

### General Prerequisites (All Indications)

- **[DG001 — Blocking]** Retrieve TFDA package insert PDF to extract warnings and contraindications; required before S1 safety evaluation can proceed
- **[DG002 — High]** Complete DrugBank API query for formal MOA documentation
- Establish Philippines FDA registration status for the human HIV-1 indication as a regulatory foundation for any veterinary or expanded-use application
- Consider formal veterinary-human bridging pharmacology consultation to define species-appropriate dosing and safety monitoring frameworks
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

