---
layout: default
title: Ertapenem
parent: 僅模型預測 (L5)
nav_order: 127
evidence_level: L5
indication_count: 2
---

# Ertapenem
{: .fs-9 }

證據等級: **L5** | 預測適應症: **2** 個
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

# Ertapenem: From Complicated Intra-Abdominal Infections to Bacterial Arthritis

## One-Sentence Summary

Ertapenem is a broad-spectrum carbapenem antibiotic used to treat complicated bacterial infections including intra-abdominal, skin and soft tissue, respiratory, and urinary tract infections.
The TxGNN model predicts it may be effective for **Bacterial Arthritis**, with **0 registered clinical trials** and **9 publications** currently supporting this direction. A second high-scoring prediction — Staphylococcus aureus infection — carries substantially stronger evidence (8 trials, 20 publications) and is summarised under additional findings.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Complicated intra-abdominal, skin/soft-tissue, respiratory, and urinary tract infections |
| Predicted New Indication | Bacterial Arthritis |
| TxGNN Prediction Score | 99.72% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Ertapenem is a 1β-methyl carbapenem that inhibits bacterial cell wall synthesis by binding preferentially to penicillin-binding proteins (PBP-2 and PBP-3), leading to cell lysis and death. Its antimicrobial spectrum covers methicillin-susceptible *Staphylococcus aureus* (MSSA), *Streptococcus* spp., Enterobacteriaceae (including ESBL-producing strains), and anaerobes — all recognised causative agents of bacterial (septic) arthritis.

Bacterial arthritis typically results from haematogenous spread of these same organisms into the synovial space. Because ertapenem's established indications already target these pathogens at other body sites, extension to joint infections follows logically from its pharmacological profile. Its once-daily dosing schedule is a practical advantage for the prolonged outpatient parenteral antibiotic therapy (OPAT) that bacterial arthritis often requires. A retrospective cohort of 306 OPAT patients (PMID 24709258) identified bone and joint infections as one of the most frequent real-world treatment indications for ertapenem, providing strong clinical plausibility.

Detailed mechanism of action data from DrugBank is not available in this Evidence Pack. Based on published information, ertapenem belongs to the carbapenem class of β-lactam antibiotics; its broad-spectrum efficacy against gram-positive and gram-negative pathogens — the same organisms responsible for bacterial arthritis — makes the TxGNN prediction mechanistically sound.

---

## Clinical Trial Evidence

Currently no clinical trials specifically investigating ertapenem for bacterial arthritis are registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [24709258](https://pubmed.ncbi.nlm.nih.gov/24709258/) | 2014 | Retrospective Cohort | Antimicrobial Agents and Chemotherapy | Among 306 OPAT patients, bone and joint infections were among the most common ertapenem indications; long-term safety and efficacy confirmed |
| [22233826](https://pubmed.ncbi.nlm.nih.gov/22233826/) | 2011 | Case Report | Journal of Chemotherapy | Successful treatment of *Klebsiella pneumoniae* septic wrist arthritis with ertapenem plus levofloxacin |
| [31352398](https://pubmed.ncbi.nlm.nih.gov/31352398/) | 2019 | Case Report | BMJ Case Reports | *Citrobacter koseri* septic arthritis with concomitant osteomyelitis in a diabetic patient successfully treated with ertapenem |
| [37578166](https://pubmed.ncbi.nlm.nih.gov/37578166/) | 2023 | Case Report | Journal of Investigative Medicine High Impact Case Reports | *Prevotella bivia* septic arthritis in an immunocompetent adult; initial misdiagnosis, joint aspiration key to diagnosis, ertapenem-based treatment |
| [31585203](https://pubmed.ncbi.nlm.nih.gov/31585203/) | 2020 | Case Report | Anaerobe | First reported *Clostridium paraputrificum* septic arthritis and osteomyelitis; arthroscopic debridement plus antibiotic coverage highlights need for broad anaerobic spectrum |
| [31220276](https://pubmed.ncbi.nlm.nih.gov/31220276/) | 2019 | Observational Cohort | Journal of Antimicrobial Chemotherapy | Off-label subcutaneous ertapenem used as prolonged suppressive therapy for bone and joint infections when surgery is not feasible; safe and effective in 10 patients |
| [39193962](https://pubmed.ncbi.nlm.nih.gov/39193962/) | 2024 | Observational | Clinical Laboratory | Pathogen distribution and antimicrobial resistance patterns in bone and joint infections among children under four; relevant to susceptibility profiling |
| [38924836](https://pubmed.ncbi.nlm.nih.gov/38924836/) | 2024 | In vitro | Diagnostic Microbiology and Infectious Disease | Auranofin restores ertapenem susceptibility in carbapenem-resistant *E. coli*; potential combination strategy for resistant joint infections |

---

## Additional Finding: Staphylococcus Aureus Infection (TxGNN Rank 2, Score 99.28%)

This indication carries substantially stronger evidence and warrants separate attention.

### Clinical Trials

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|-----------|-------------|
| [NCT04886284](https://clinicaltrials.gov/study/NCT04886284) | Phase 2 | Recruiting | 60 | Randomised trial of cefazolin + ertapenem combination for MSSA bacteremia (CERT sub-study); directly tests ertapenem's role |
| [NCT07148960](https://clinicaltrials.gov/study/NCT07148960) | Phase 4 | Enrolling by Invitation | 300 | SABEDTIO: early dual IV antibiotic therapy vs. monotherapy for *S. aureus* bacteremia; primary endpoint is duration of bacteremia |
| [NCT07376889](https://clinicaltrials.gov/study/NCT07376889) | Phase 4 | Not Yet Recruiting | 2096 | COMBAT-SAB: large RCT testing combination antibiotic therapy vs. single antibiotic for *S. aureus* bacteremia |
| [NCT00366249](https://clinicaltrials.gov/study/NCT00366249) | Phase 3 | Completed | 1061 | Tigecycline vs. ertapenem for diabetic foot infections (includes MSSA); co-primary endpoints not met but ertapenem arm demonstrated efficacy |
| [NCT06634940](https://clinicaltrials.gov/study/NCT06634940) | N/A | Recruiting | 1000 | International surveillance of antimicrobial resistance in cirrhosis-related infections including *S. aureus* |
| [NCT06044272](https://clinicaltrials.gov/study/NCT06044272) | N/A | Completed | 10000 | Retrospective AMR profiles in healthcare facilities; documents ertapenem susceptibility patterns |
| [NCT03218397](https://clinicaltrials.gov/study/NCT03218397) | N/A | Completed | 500 | RAPIDS-GN: rapid susceptibility testing for Gram-negative bacteremia; validates diagnostic stewardship approaches |
| [NCT06174649](https://clinicaltrials.gov/study/NCT06174649) | N/A | Completed | 900 | FAST trial: rapid phenotypic AST for Gram-negative bacteremia; evaluates clinical outcome improvement |

### Literature Evidence (MSSA)

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [31773134](https://pubmed.ncbi.nlm.nih.gov/31773134/) | 2020 | Case Series | Clinical Infectious Diseases | Cefazolin + ertapenem salvage therapy cleared persistent MSSA bacteremia in 11 cases (6 endocarditis); 8 cleared within 24 hours |
| [27572414](https://pubmed.ncbi.nlm.nih.gov/27572414/) | 2016 | Case Series + In vitro/In vivo | Antimicrobial Agents and Chemotherapy | First description of ertapenem + cefazolin synergy; in vitro and murine skin infection model confirmed synergistic activity against MSSA |
| [38946294](https://pubmed.ncbi.nlm.nih.gov/38946294/) | 2024 | Retrospective Cohort | Journal of Antimicrobial Chemotherapy | Carbapenem combination vs. standard of care for persistent MSSA bacteremia; provides comparative outcomes data |
| [40448546](https://pubmed.ncbi.nlm.nih.gov/40448546/) | 2025 | Retrospective Cohort | Journal of Antimicrobial Chemotherapy | Hypoalbuminemia reduces ertapenem efficacy in MSSA bacteremia combination therapy (caution at albumin < 2.5 g/dL) |
| [35493130](https://pubmed.ncbi.nlm.nih.gov/35493130/) | 2022 | In vitro/Translational | Open Forum Infectious Diseases | Ertapenem + cefazolin shows potent activity within staphylococcal biofilms; explains clinical success in endocarditis |
| [34978891](https://pubmed.ncbi.nlm.nih.gov/34978891/) | 2022 | Basic Science | Antimicrobial Agents and Chemotherapy | Ertapenem stimulates IL-1β release from monocytes; immunomodulatory mechanism may partially explain clinical synergy |
| [39777519](https://pubmed.ncbi.nlm.nih.gov/39777519/) | 2025 | In vitro | Journal of Infectious Diseases | Adjunctive carbapenems (ertapenem or meropenem) enhance ceftaroline/vancomycin killing of MRSA |
| [16801442](https://pubmed.ncbi.nlm.nih.gov/16801442/) | 2006 | In vitro + Animal Model | Antimicrobial Agents and Chemotherapy | Linezolid + ertapenem highly synergistic against MRSA in rabbit endocarditis model |
| [15164963](https://pubmed.ncbi.nlm.nih.gov/15164963/) | 2004 | RCT Subgroup | International Journal of Antimicrobial Agents | Ertapenem 1 g daily vs. piperacillin-tazobactam for complicated skin/soft-tissue infections caused by MSSA; comparable clinical cure rates |
| [39230345](https://pubmed.ncbi.nlm.nih.gov/39230345/) | 2025 | Review | AJHP | Comprehensive review of combination treatment options for persistent MSSA bacteremia; positions ertapenem combinations as key strategy |

---

## Philippines Market Information

Ertapenem is currently **not registered** in the Philippines. No regulatory licenses are on file. The drug is marketed globally (e.g., as **Invanz** by Merck/MSD) and approved in multiple jurisdictions including the US FDA, EMA, and Japan PMDA for complicated intra-abdominal, skin, respiratory, urinary, and pelvic infections. Local registration would be required before any formal clinical use in the Philippines.

---

## Safety Considerations

Please refer to the package insert for safety information.

> Key notes from published literature: Patients with hypoalbuminemia (serum albumin < 2.5 g/dL) may experience suboptimal ertapenem exposure due to high protein binding — clinicians should exercise caution when considering combination therapy in this population (PMID 40448546). No drug-drug interaction data was found in the queried database for this Evidence Pack.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple published case reports and a retrospective OPAT cohort confirm ertapenem's real-world use in bacterial/septic arthritis caused by a range of gram-negative and anaerobic organisms, providing reasonable clinical and mechanistic plausibility. No dedicated RCT exists for this specific indication, limiting the evidence to L3. For the related *S. aureus* infection indication, evidence is considerably stronger, including Phase 2–4 RCTs, creating a credible platform for clinical evaluation.

**To proceed, the following is needed:**

- **Philippines FDA registration pathway**: Evaluate compassionate use, importation, or full registration options for Ertapenem (Invanz or equivalent)
- **MOA and safety data**: Retrieve full DrugBank record (DB00303) including key warnings, contraindications, and drug interaction profiles; download package insert from EMA/US FDA
- **Joint PK/PD data**: Confirm adequate synovial fluid penetration to support bacterial arthritis indication
- **Subpopulation safety review**: Assess appropriateness in patients with hypoalbuminemia and renal impairment (ertapenem is renally cleared)
- **Prospective registry or observational study**: Real-world data collection on ertapenem use in septic arthritis in the Philippine context
- **Regulatory gap analysis**: Given that ertapenem is already used off-label for bone and joint infections globally, assess whether a formal indication extension or compassionate-use protocol is the more feasible pathway
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

