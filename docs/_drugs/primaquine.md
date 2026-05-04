---
layout: default
title: Primaquine
parent: 僅模型預測 (L5)
nav_order: 183
evidence_level: L5
indication_count: 8
---

# Primaquine
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

# Primaquine: From Malaria to Pneumocystis Pneumonia (PCP)

## One-Sentence Summary

Primaquine is the only globally available 8-aminoquinoline antimalarial, licensed since 1952 as the standard treatment for *Plasmodium vivax* radical cure (eliminating dormant liver-stage hypnozoites) and for blocking *P. falciparum* transmission to mosquitoes — yet it remains entirely unregistered in the Philippines.

The TxGNN model identifies **Pneumocystis Pneumonia (PCP / Pneumocystosis)** as a clinically supported new indication, backed by **2 completed randomized controlled trials and 20+ publications at Evidence Level L1**; it simultaneously confirms the established malaria indication with over **50 clinical trials and 20 publications at Evidence Level L1**.

> ⚠️ **Model Signal Caveat**: The four highest TxGNN prediction scores in this dataset all point to myiasis variants (fly-larva infestation, scores 0.9972–0.9975). These are assessed as **knowledge-graph false positives** — myiasis is caused by arthropod larvae with no pharmacological overlap with Primaquine's antiprotozoal mechanism, and zero supporting clinical or preclinical evidence exists. The identical scores across three myiasis subtypes confirm topology-driven artifacts rather than genuine biological signals. This report focuses on the two clinically meaningful L1-supported indications: malaria and pneumocystosis.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Malaria — *P. vivax* radical cure (hypnozoite eradication) and *P. falciparum* gametocytocidal therapy |
| Predicted New Indication | Pneumocystosis (*Pneumocystis jirovecii* Pneumonia, PCP) |
| TxGNN Prediction Score | 99.32% (PCP, rank 2956) · 99.38% (Malaria, rank 4495) |
| Evidence Level | L1 (≥ 2 completed Phase 3 RCTs across both indications) |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Primaquine is metabolized primarily by hepatic CYP2D6 into reactive oxidative intermediates — particularly 5-hydroxyprimaquine and downstream quinone-imine species. These metabolites disrupt mitochondrial electron transport chains and generate intracellular oxidative stress lethal to susceptible organisms. This is the same mechanism that eliminates *P. vivax* hypnozoites in the liver and sterilizes *P. falciparum* gametocytes in the blood — and it forms the mechanistic basis for activity against organisms sharing similar mitochondrial architecture.

*Pneumocystis jirovecii*, despite its phylogenetic reclassification as a fungus, retains a mitochondrial electron transport chain structurally distinct from that of typical pathogenic fungi such as *Candida* or *Aspergillus*, and instead resembles the protozoan-like primitive eukaryote structure targeted by primaquine metabolites. Clinically, the **Clindamycin + Primaquine** combination exploits a synergistic dual mechanism: Clindamycin inhibits *P. jirovecii* ribosomal protein synthesis, while primaquine's oxidative metabolites disrupt mitochondrial respiration — together achieving rapid clearance of both trophozoites and cysts. This combination has been in active clinical use since its foundational in vitro description in 1988 (Queener et al.), and is now formally listed in **ECIL guidelines** as a recognized second-line therapy for PCP in non-HIV haematology patients, and as a standard alternative when TMP-SMX is contraindicated or not tolerated in HIV/AIDS patients.

Regarding malaria: Primaquine's role is well-established beyond any doubt. It remains the **only available drug** capable of clearing *P. vivax* and *P. ovale* hypnozoites (preventing relapse), and the **only potent gametocytocide** for *P. falciparum* (blocking transmission). Its absence from the Philippines formulary represents a critical gap — NCT04222088 documents its active use in Palawan Province, confirming local clinical relevance. The TxGNN model's prediction of malaria at rank 7 effectively serves as a validation signal: the drug belongs in the Philippines antimalarial toolkit.

---

## Clinical Trial Evidence — Malaria (Rank 7 · L1)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT02787070](https://clinicaltrials.gov/study/NCT02787070) | Phase 4 | Completed | 420 | **TRIPI trial** — Randomized controlled trial of Primaquine radical cure for *P. vivax* in Papua, Indonesia; core RCT establishing hypnozoite eradication efficacy |
| [NCT01640574](https://clinicaltrials.gov/study/NCT01640574) | Phase 3 | Completed | 680 | Southeast Asia: randomized comparison of 7-day vs 14-day Primaquine combined with DHP or chloroquine for *P. vivax* radical cure |
| [NCT02216123](https://clinicaltrials.gov/study/NCT02216123) | Phase 3 | Completed | 251 | **DETECTIVE trial** — Double-blind RCT of Tafenoquine vs Primaquine (active comparator) for *P. vivax*, formally establishing Primaquine as the reference standard |
| [NCT01838902](https://clinicaltrials.gov/study/NCT01838902) | Phase 3 | Completed | 467 | Gametocytocidal efficacy of Primaquine in *P. falciparum* asymptomatic carriers in The Gambia; dose-optimization for transmission blocking |
| [NCT05690841](https://clinicaltrials.gov/study/NCT05690841) | Phase 3 | Recruiting | 7,530 | **FLAME trial** — Large cluster-RCT of focal mass drug administration including Primaquine for *P. vivax* elimination in Peru; highest-powered current design |
| [NCT03773536](https://clinicaltrials.gov/study/NCT03773536) | Phase 4 | Completed | 146 | ASAQ + single low-dose Primaquine (0.25 mg/kg) for uncomplicated *P. falciparum* in Zanzibar; confirms transmission-blocking dose in Africa |
| [NCT02434952](https://clinicaltrials.gov/study/NCT02434952) | Phase 4 | Completed | 109 | Low-dose Primaquine (0.25 mg/kg) for *P. falciparum* transmission blocking in symptomatic Cambodians; tolerability and safety |
| [NCT04222088](https://clinicaltrials.gov/study/NCT04222088) | N/A | Completed | 159 | **Philippines-specific (Palawan)** — Antimalarial efficacy trial in Bataraza, Brookes, and Rizal; Primaquine used at 0.75 mg base/kg for *P. vivax* |
| [NCT04864444](https://clinicaltrials.gov/study/NCT04864444) | N/A | Completed | 10,715 | Cluster-RCT of mass drug administration (DHA-PPQ + single low-dose Primaquine) in Senegal for *P. falciparum* seasonal malaria control |
| [NCT05540470](https://clinicaltrials.gov/study/NCT05540470) | N/A | Completed | 1,991 | Real-world *P. vivax* radical cure in highly mobile mining populations across the Guiana Shield; pragmatic implementation evidence |

---

## Clinical Trial Evidence — Pneumocystosis / PCP (Rank 8 · L1)

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---|---|---|---|---|
| [NCT00000640](https://clinicaltrials.gov/study/NCT00000640) | Phase 3 | Completed | 290 | **Core Phase 3 RCT**: Clindamycin/Primaquine vs Dapsone/TMP vs TMP-SMX for mild–moderate PCP in AIDS patients; established Clindamycin/Primaquine as an effective alternative with comparable efficacy |
| [NCT00000717](https://clinicaltrials.gov/study/NCT00000717) | N/A | Completed | 50 | **Pivotal early trial**: Safety and efficacy of Clindamycin + Primaquine for mild–moderate *P. carinii* pneumonia in AIDS patients; 91% clinical response rate reported |
| [NCT07357103](https://clinicaltrials.gov/study/NCT07357103) | Phase 4 | Not Yet Recruiting | 416 | **SPIRIT-PCP Platform** — Modern large-scale adaptive trial positioning second-line PCP therapies (including Clindamycin/Primaquine) for TMP-SMX-intolerant patients; expected to generate high-quality contemporary evidence |
| [NCT04328688](https://clinicaltrials.gov/study/NCT04328688) | N/A | Completed | 30 | PCP treatment comparison after solid organ transplantation; Clindamycin/Primaquine evaluated as second-line alternative in non-HIV immunocompromised setting |
| [NCT06691321](https://clinicaltrials.gov/study/NCT06691321) | N/A | Recruiting | 60 | Caspofungin efficacy for PCP in HIV/AIDS patients; Primaquine-based standard regimen serves as clinical comparator reference |

---

## Literature Evidence — Malaria

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [24499628](https://pubmed.ncbi.nlm.nih.gov/24499628/) | 2013 | Meta-analysis | *Parasites & Vectors* | Systematic review and meta-analysis: artemisinin derivatives + Primaquine block *P. falciparum* transmission to mosquitoes; quantifies gametocytocidal benefit |
| [40813102](https://pubmed.ncbi.nlm.nih.gov/40813102/) | 2025 | Systematic Review | *BMJ Global Health* | Single low-dose Primaquine (SLDPQ) for malaria control in Africa: safety, efficacy, and implementation barriers; latest evidence synthesis |
| [35353968](https://pubmed.ncbi.nlm.nih.gov/35353968/) | 2022 | Clinical Study | *NEJM* | Primaquine and *P. vivax* malaria recurrence in Brazil; clinical cohort documenting efficacy and emerging resistance surveillance |
| [22152065](https://pubmed.ncbi.nlm.nih.gov/22152065/) | 2011 | Review | *Malaria Journal* | Comprehensive update on Primaquine in vivax malaria: efficacy evidence, G6PD hazards, resistance data, and management guidance |
| [25363455](https://pubmed.ncbi.nlm.nih.gov/25363455/) | 2014 | Review | *Malaria Journal* | "Primaquine: the risks and the benefits" — authoritative review covering G6PD hemolysis, dosing, and global policy implications |
| [29672516](https://pubmed.ncbi.nlm.nih.gov/29672516/) | 2018 | Policy Review | *PLoS NTD* | Divergent Primaquine policies across 77 malaria-endemic countries; G6PD testing practice gaps and recommendations |
| [40867022](https://pubmed.ncbi.nlm.nih.gov/40867022/) | 2025 | Pharmacogenomics | *Emerging Infect Dis* | CYP2D6 genotype and Primaquine treatment outcomes in Venezuela; ≈25% intermediate/poor metabolizers with increased vivax recurrence |
| [27039396](https://pubmed.ncbi.nlm.nih.gov/27039396/) | 2016 | Review | *BMC Medicine* | Low-dose Primaquine + ACT for *P. falciparum* transmission reduction: clinical promise vs hemolysis risk framing |
| [28417346](https://pubmed.ncbi.nlm.nih.gov/28417346/) | 2017 | Review | *Bull Soc Pathol Exot* | Role of Primaquine in malaria control and elimination in French-speaking Africa; underutilization analysis and MOA summary |
| [15494911](https://pubmed.ncbi.nlm.nih.gov/15494911/) | 2004 | Review | *Clin Infect Dis* | "Primaquine therapy for malaria" — comprehensive review of 1946–2004 clinical applications; defines spectrum of evidence |

---

## Literature Evidence — Pneumocystosis / PCP

| PMID | Year | Type | Journal | Key Findings |
|---|---|---|---|---|
| [39732393](https://pubmed.ncbi.nlm.nih.gov/39732393/) | 2025 | Systematic Review / Network Meta-analysis | *Clin Microbiol Infect* | Network meta-analysis of all PCP treatment RCTs in HIV patients; quantifies Clindamycin/Primaquine efficacy and safety relative to TMP-SMX and other regimens |
| [27550993](https://pubmed.ncbi.nlm.nih.gov/27550993/) | 2016 | Clinical Guideline (ECIL) | *J Antimicrob Chemother* | ECIL guidelines for PCP in non-HIV haematology patients; Clindamycin + Primaquine formally listed as second-line treatment option |
| [9770152](https://pubmed.ncbi.nlm.nih.gov/9770152/) | 1998 | RCT | *Clin Infect Dis* | **CTN 004**: Multicenter double-blind RCT (n=87) — Clindamycin/Primaquine vs TMP-SMX for AIDS-related PCP; comparable overall efficacy confirmed |
| [2060532](https://pubmed.ncbi.nlm.nih.gov/2060532/) | 1991 | Clinical Trial (Phase 2) | *Eur J Clin Microbiol* | Clindamycin + Primaquine primary treatment for mild–moderate *P. carinii* pneumonia; 91% clinical response in 36 AIDS patients |
| [8086551](https://pubmed.ncbi.nlm.nih.gov/8086551/) | 1994 | Clinical Study | *Clin Infect Dis* | **ACTG 044**: Multi-center study of Clindamycin/Primaquine for mild–moderate PCP; systematic safety and efficacy data |
| [3261959](https://pubmed.ncbi.nlm.nih.gov/3261959/) | 1988 | In vitro / In vivo | *Antimicrob Agents Chemother* | Foundational preclinical study: Clindamycin + Primaquine activity against *P. carinii* in vitro and in animal models; establishes synergistic mechanism |
| [33870843](https://pubmed.ncbi.nlm.nih.gov/33870843/) | 2021 | Review | *Expert Opin Pharmacother* | PCP prevention and treatment overview; Clindamycin/Primaquine positioned as second-line in both HIV and non-HIV immunocompromised populations |
| [36969352](https://pubmed.ncbi.nlm.nih.gov/36969352/) | 2023 | Review | *Avicenna J Med* | PCP management in HIV and non-HIV immunocompromised; discusses rising non-HIV incidence and expanding role of alternative regimens |
| [36160421](https://pubmed.ncbi.nlm.nih.gov/36160421/) | 2022 | Review | *Front Pharmacol* | PCP treatment in G6PD-deficient patients; Primaquine-specific risk assessment and monitoring strategies for co-occurring G6PD deficiency |
| [18971152](https://pubmed.ncbi.nlm.nih.gov/18971152/) | 2008 | Review | *J Formos Med Assoc* | Pneumocystis pneumonia review with Asia-Pacific perspective; regionally relevant for Philippines clinical context |

---

## Philippines Market Information

Primaquine currently has **no registered pharmaceutical products** in the Philippines. The FDA Philippines has issued zero product licenses, and no approved indications, dosage forms, or marketing authorizations exist in the national database.

This absence is clinically significant: Primaquine is designated a **WHO Essential Medicine** (23rd edition), and clinical evidence demonstrates active use in Philippine territory. The trial NCT04222088 specifically documented Primaquine administration at 0.75 mg base/kg for *P. vivax* in Palawan Province (Bataraza, Brookes Point, Rizal municipalities), confirming real-world demand with no formal regulatory framework currently in place.

---

## Safety Considerations

Full package insert warnings and contraindications were not available in the current Evidence Pack. The following safety information is well-established in published literature:

**Key Warnings:**
- **G6PD Deficiency-Induced Hemolytic Anemia**: The most critical safety risk. Primaquine oxidative metabolites cause acute, potentially life-threatening hemolytic anemia in glucose-6-phosphate dehydrogenase (G6PD)-deficient individuals. G6PD gene deficiency frequencies of 3–30% are documented in malaria-endemic Southeast Asian and Pacific populations. Quantitative G6PD testing (e.g., CareStart™ RDT, demonstrated feasible in NCT02876549) is **mandatory** before Primaquine administration under all current WHO guidelines.
- **Methemoglobinemia**: Dose-dependent formation reported, particularly at higher doses; hemoglobin and methemoglobin monitoring required.
- **CYP2D6 Pharmacogenomics and Treatment Failure**: Approximately 25% of patients may be CYP2D6 intermediate or poor metabolizers (PMID 40867022), generating insufficient active metabolite and experiencing *P. vivax* relapse despite full compliance. CYP2D6 genotyping is emerging as a clinical consideration in high-recurrence settings.

**Drug Interactions:**
No DDI data was retrieved for this Evidence Pack. Based on published pharmacology, co-administration with other oxidizing agents (dapsone, sulfonamides, nitrofurantoin) may potentiate hemolytic risk. Quinolone antimalarials (quinine, chloroquine) may interact pharmacokinetically via shared metabolic pathways.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Primaquine holds exceptional, multi-level clinical evidence for two indications directly relevant to the Philippines: (1) **Malaria** — it is the only WHO-recommended drug for *P. vivax* radical cure, with evidence from dozens of Phase 3–4 RCTs across Southeast Asia and documented use in Palawan; (2) **Pneumocystosis (PCP)** — Phase 3 RCT data and multiple clinical guidelines support Clindamycin + Primaquine as a validated second-line regimen for immunocompromised patients intolerant to TMP-SMX. The complete absence of Philippines registration for a WHO Essential Medicine with this evidence base warrants urgent regulatory attention.

**To proceed, the following is needed:**

- **G6PD screening infrastructure**: Implement point-of-care G6PD testing (quantitative RDT) at all malaria treatment facilities and pharmacies before dispensing; train healthcare workers on interpretation and dose-adjustment protocols for deficient patients
- **Full prescribing information**: Obtain and review complete FDA Philippines-equivalent package insert or WHO prescribing information; resolve current data gaps on formal contraindications and approved warnings
- **CYP2D6 pharmacogenomics plan**: Consider population-level CYP2D6 screening or empirical dose-adjustment protocols for *P. vivax* radical cure to address the ≈25% intermediate/poor metabolizer rate identified in regional studies
- **Philippines epidemiology data**: Quantify local G6PD deficiency prevalence in Palawan and other malaria-endemic provinces to calibrate hemolytic risk estimates; review NCT04222088 safety outcomes
- **FDA Philippines registration pathway**: Initiate product registration; Primaquine may qualify for an accelerated or abridged review pathway as a WHO Essential Medicine with established international safety/efficacy data
- **PCP indication strategy**: Define target patient populations (HIV patients with CD4 < 200, solid organ transplant recipients, haematology patients on immunosuppression) and document local PCP epidemiology to support PCP indication registration alongside the primary malaria indication
- **Pharmacovigilance program**: Establish mandatory adverse event reporting for hemolytic events, methemoglobinemia, and treatment failures from first registration date
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

