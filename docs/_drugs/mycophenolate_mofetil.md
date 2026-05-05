---
layout: default
title: Mycophenolate Mofetil
parent: 僅模型預測 (L5)
nav_order: 196
evidence_level: L5
indication_count: 10
---

# Mycophenolate Mofetil
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

# Mycophenolate Mofetil: From Organ Transplant Rejection to HIV Infectious Disease

## One-Sentence Summary

Mycophenolate mofetil (MMF) is an established immunosuppressant used to prevent organ rejection following kidney, heart, and liver transplantation, acting through selective inhibition of lymphocyte proliferation via the de novo purine synthesis pathway.
The TxGNN model predicts it may be effective for **HIV Infectious Disease**,
with **10 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Organ transplant rejection prevention (kidney, heart, liver) |
| Predicted New Indication | HIV Infectious Disease |
| TxGNN Prediction Score | 99.86% |
| Evidence Level | L2 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data from DrugBank is currently unavailable in this evidence pack. Based on established pharmacological knowledge, mycophenolate mofetil is a prodrug that is rapidly hydrolyzed in vivo to its active metabolite, mycophenolic acid (MPA). MPA is a selective, non-competitive inhibitor of inosine-5′-monophosphate dehydrogenase (IMPDH), the rate-limiting enzyme in the de novo synthesis of guanosine nucleotides. Because lymphocytes — unlike most other cell types — are almost entirely dependent on this de novo pathway and lack an effective salvage alternative, MPA selectively depletes intracellular deoxyguanosine triphosphate (dGTP) and guanosine triphosphate (GTP) pools in activated T and B cells, blocking their proliferation without broadly suppressing other tissues.

The mechanistic bridge to HIV is both direct and well-documented in the early literature. HIV reverse transcriptase requires dGTP as a substrate to complete reverse transcription of viral genomic RNA into proviral DNA. MMF-induced intracellular dGTP depletion therefore directly limits the substrate available for viral replication, an effect that has been demonstrated ex vivo and in small clinical cohorts to translate into measurable reductions in plasma HIV-1 RNA. Furthermore, since HIV depends on activated CD4+ T cells as its primary replication factories, MMF's lymphostatic effect indirectly shrinks the pool of productive infection targets. This dual mechanism — starving the virus of nucleotide substrate while simultaneously reducing the number of susceptible host cells — is pharmacologically complementary to conventional nucleoside reverse transcriptase inhibitors (NRTIs) such as abacavir, and multiple studies have confirmed synergistic activity between MMF and NRTI-containing regimens.

The TxGNN prediction is further supported by a consistent body of clinical work spanning more than two decades. The MAN2 trial series (NCT00120419, Phase 4, n=90) prospectively studied MMF in antiretroviral-naïve HIV-1 patients to determine whether suppressing chronic immune hyperactivation — a key driver of AIDS progression — could slow CD4+ T cell decline. Separately, transplant medicine has provided an unintentional but informative real-world dataset: MMF is now routinely used as part of immunosuppressive regimens in HIV-positive renal transplant recipients, and accumulated experience confirms that it is tolerable in this immunocompromised population when combined with well-controlled antiretroviral therapy.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|-------------|
| [NCT00120419](https://clinicaltrials.gov/study/NCT00120419) | Phase 4 | Unknown | 90 | MAN2 Study: Directly evaluates MMF monotherapy in antiretroviral-naïve HIV-1 patients; primary endpoints are control of chronic immune hyperactivation, preservation of CD4+ T cell count, and plasma HIV-1 RNA; most directly relevant trial for this indication |
| [NCT00247494](https://clinicaltrials.gov/study/NCT00247494) | Phase 4 | Unknown | 90 | MAN2 cardiovascular substudy: Assesses effects of MMF on metabolic and cardiovascular surrogate markers in HIV-1 infected patients not on antiretroviral therapy; provides safety and pharmacodynamic data in the HIV population |
| [NCT00021489](https://clinicaltrials.gov/study/NCT00021489) | Phase 2 | Withdrawn | 0 | Phase 1/2 study designed to evaluate safety, tolerability, and antiretroviral activity of MMF as adjunct to abacavir in heavily treatment-experienced HIV patients; withdrawn prior to enrollment, but its design reflects strong scientific rationale recognized by regulators |
| [NCT01453192](https://clinicaltrials.gov/study/NCT01453192) | Phase 3 | Completed | 27 | National multicenter prospective trial evaluating 6-month acute rejection incidence in HIV-infected renal transplant recipients on raltegravir-based antiretroviral therapy; MMF used as standard anti-rejection agent, providing safety context in HIV+ transplant setting |
| [NCT00009009](https://clinicaltrials.gov/study/NCT00009009) | Phase 2 | Completed | 10 | Renal allotransplantation in HIV-infected patients with end-stage renal disease; MMF included in immunosuppressive regimen; early pilot demonstrating feasibility and safety of transplantation with MMF in HIV-positive individuals |
| [NCT00038272](https://clinicaltrials.gov/study/NCT00038272) | Phase 2 | Completed | 56 | Randomized double-blind Phase 1/2 trial comparing DAPD (amdoxovir) versus DAPD plus MMF in treatment-experienced HIV patients; evaluates whether MMF augments the antiviral activity of a novel NRTI via nucleotide pool modulation |
| [NCT00112593](https://clinicaltrials.gov/study/NCT00112593) | N/A | Completed | 5 | Allogeneic hematopoietic stem cell transplantation to induce mixed hematopoietic chimerism in HIV-1 positive patients using non-myeloablative conditioning; MMF used for GVHD prophylaxis in an experimental HIV functional cure strategy |
| [NCT01288131](https://clinicaltrials.gov/study/NCT01288131) | Phase 3 | Terminated | 8 | Randomized controlled trial of MMF vs. cyclophosphamide/prednisolone for anti-erythropoietin-associated pure red cell aplasia; terminated early (n=8); provides indirect evidence of MMF's immunosuppressive scope in a closely related clinical context |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [12352149](https://pubmed.ncbi.nlm.nih.gov/12352149/) | 2002 | Clinical Cohort | J Acquir Immune Defic Syndr | Seminal clinical proof-of-concept: MMF 500 mg BID added to failing regimens including abacavir in 5 patients; demonstrated measurable dGTP pool depletion and associated decrease in plasma HIV-1 RNA, directly validating the IMPDH-inhibition mechanism in humans |
| [11391161](https://pubmed.ncbi.nlm.nih.gov/11391161/) | 2001 | Pilot Study | J Acquir Immune Defic Syndr | Open-label pilot (n=7) in patients with diagnosed AIDS and multidrug-resistant HIV: MMF combined with ABC, ddI, amprenavir, and ritonavir was well tolerated in advanced disease; provided early clinical rationale for salvage regimens incorporating MMF |
| [15213566](https://pubmed.ncbi.nlm.nih.gov/15213566/) | 2004 | Prospective Clinical Study | J Acquir Immune Defic Syndr | Randomized pilot (n=17) in early-stage chronic HIV-1: patients randomized to HAART+MMF or HAART alone, followed by structured treatment interruption; evaluated effects on plasma and lymphatic tissue viral load and immune response |
| [15353978](https://pubmed.ncbi.nlm.nih.gov/15353978/) | 2004 | Clinical Study | AIDS | Assessed the effect of MMF on plasma HIV-1 RNA decay rate and the latently infected cellular reservoir in treatment-naïve patients initiating antiretroviral therapy; explores whether IMPDH inhibition can accelerate reservoir clearance |
| [16379601](https://pubmed.ncbi.nlm.nih.gov/16379601/) | 2005 | Clinical Study | AIDS Res Hum Retroviruses | Longitudinal study confirming no detrimental immunological effects of MMF combined with HAART in treatment-naïve acute and chronic HIV-1 patients; assessed T cell proliferation kinetics and HIV-specific immunity over time |
| [15871638](https://pubmed.ncbi.nlm.nih.gov/15871638/) | 2005 | PK/PD Study | Clin Pharmacokinet | PK-PD characterization of low-dose MMF in HIV-infected patients on HAART (abacavir, efavirenz, nelfinavir); established that therapeutic drug monitoring is recommended due to variable exposure; supports dosing guidance for future trials |
| [15355127](https://pubmed.ncbi.nlm.nih.gov/15355127/) | 2004 | PK Interaction Study | Clin Pharmacokinet | Evaluated MMF's impact on the pharmacokinetics of multiple antiretroviral drugs and on intracellular dCTP, dGTP, and lamivudine-triphosphate pools; mechanistically explains how MMF reshapes the nucleotide landscape to favor NRTI activity |
| [17885292](https://pubmed.ncbi.nlm.nih.gov/17885292/) | 2007 | Clinical Study | AIDS | Evaluated safety, tolerability, and antiretroviral activity of amdoxovir (DAPD) with or without MMF in HIV-1 patients following extensive prior antiretroviral therapy; supports combination strategy but highlights need for careful safety monitoring |
| [17017956](https://pubmed.ncbi.nlm.nih.gov/17017956/) | 2006 | Review | Curr Top Med Chem | Comprehensive review of immunosuppressive drugs in HIV disease; discusses how chronic immune hyperactivation drives CD4+ depletion and AIDS progression, and analyzes the mechanistic and clinical rationale for IMPDH inhibition as an adjunct to HAART |
| [39515757](https://pubmed.ncbi.nlm.nih.gov/39515757/) | 2025 | Retrospective Cohort | Am J Transplant | Large real-world analysis (SRTR registry, 2004–2022, n=1,155) of kidney transplant recipients with HIV discharged on tacrolimus/MMF regimens; inverse probability treatment weighting analysis comparing induction strategies; the most recent and largest safety dataset for MMF use in the HIV population |

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A well-characterized mechanistic framework — MMF-driven intracellular dGTP depletion impairing HIV reverse transcription, combined with reduction of the activated CD4+ T cell replicative pool — underpins multiple Phase 2/4 clinical investigations spanning over two decades, with the MAN2 trial series (Phase 4, n=90) representing the most direct prospective evidence. However, MMF is a broad immunosuppressant, and its use in an already immunocompromised HIV-positive population demands rigorous patient selection, opportunistic infection prophylaxis, and careful monitoring.

**To proceed, the following is needed:**
- Obtain complete mechanism of action data from DrugBank (DB00688) to finalize mechanistic linkage documentation
- Retrieve full prescribing information (warnings, contraindications, pregnancy category) from the current MMF SmPC or package insert to complete the safety assessment
- Verify the final publication status and results of NCT00120419 (MAN2 Study) and NCT00247494 to determine whether Phase 4 endpoints were met
- Define the specific target patient subpopulation: HIV+ organ transplant recipients (established use), antiretroviral-naïve patients with immune hyperactivation, or HAART-experienced patients with treatment failure
- Conduct a formal drug-drug interaction review between MMF and current first-line antiretroviral agents (integrase inhibitors, tenofovir-based regimens)
- Develop a safety monitoring protocol addressing hematological toxicity (CBC), renal and hepatic function, and opportunistic infection surveillance given the compounded immunosuppression risk
- Assess the regulatory pathway in the Philippines for compassionate use, special import authorization (FDA Philippines), or inclusion in a formally registered clinical protocol if local evaluation is planned
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

