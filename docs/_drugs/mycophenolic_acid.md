---
layout: default
title: Mycophenolic Acid
parent: 僅模型預測 (L5)
nav_order: 197
evidence_level: L5
indication_count: 10
---

# Mycophenolic Acid
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

Using the `txgnn-pipeline` skill as context for this TxGNN drug repurposing report. Now generating the evaluation report based on the Evidence Pack.

---

# Mycophenolic Acid: From Organ Transplant Rejection Prevention to Hemoglobinopathy

## One-Sentence Summary

Mycophenolic acid (MPA) is the active metabolite of mycophenolate mofetil (MMF), an established immunosuppressant used globally to prevent rejection in solid organ transplant recipients and to treat autoimmune conditions such as lupus nephritis — though it currently has no Philippines regulatory registration.
The TxGNN model predicts it may be effective for **Hemoglobinopathy** (encompassing sickle cell disease and thalassemia major),
with **27 clinical trials** and **9 publications** supporting its role as GVHD prophylaxis enabling curative hematopoietic stem cell transplantation for these conditions.

---

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Organ transplant rejection prevention (renal, cardiac, hepatic allografts) and lupus nephritis — not registered in Philippines |
| Predicted New Indication | Hemoglobinopathy (sickle cell disease, thalassemia major) |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L2 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Mycophenolic acid (MPA) is the active metabolite of mycophenolate mofetil (MMF). Formal mechanism of action data is not available from the Philippines regulatory record; however, based on published evidence, MPA acts as a selective, non-competitive inhibitor of inosine monophosphate dehydrogenase (IMPDH) — specifically the type II isoform (IMPDH2) predominantly expressed in activated lymphocytes. Because T and B lymphocytes rely almost entirely on the de novo purine synthesis pathway for proliferation (rather than salvage pathways), IMPDH inhibition selectively suppresses lymphocyte expansion without substantially affecting other cell types. This mechanism was characterised in foundational in vitro work as early as 1991 (PMID 1826793) and underpins MPA's established role in all transplant immunosuppression settings.

In the context of hemoglobinopathy, allogeneic hematopoietic stem cell transplantation (allo-HSCT) is the only curative therapy for sickle cell disease and thalassemia major. The critical barriers to cure are graft-versus-host disease (GVHD) and graft rejection. MMF is used as a core component of GVHD prophylaxis regimens: by selectively suppressing donor and recipient lymphocyte proliferation, it stabilises mixed chimerism — the coexistence of donor and host hematopoietic cells — which ultimately allows functional replacement of the defective erythropoiesis. A 2023 publication directly reports "Immunosuppression Boost with MMF for Mixed Chimerism in Thalassemia Transplants" (*Transplantation and Cellular Therapy*, PMID 36372358), providing direct mechanistic and clinical confirmation of this link.

The connection between MPA's established transplant immunosuppression role and hemoglobinopathy HSCT is therefore mechanistically coherent and clinically intuitive: the same lymphocyte-suppressive mechanism that prevents solid organ rejection is equally applicable to preventing GVHD following HSCT for hemoglobinopathy. Active clinical adoption is confirmed by a 2025 population pharmacokinetic dosing guideline specifically addressing MMF in pediatric thalassemia patients undergoing HSCT (PMID 39891881).

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT04009525](https://clinicaltrials.gov/study/NCT04009525) | Phase 4 | Completed | 823 | Multicenter prospective study of allo-HSCT efficacy in thalassemia major; MMF is a core GVHD prophylaxis component in the standard regimen |
| [NCT02342145](https://clinicaltrials.gov/study/NCT02342145) | Phase 4 | Completed | 205 | Multicenter RCT evaluating basiliximab for acute GVHD prevention in unrelated allo-HSCT for thalassemia major; MMF used as core background immunosuppression |
| [NCT03263559](https://clinicaltrials.gov/study/NCT03263559) | Phase 2 | Completed | 95 | Phase II multicenter trial of haploidentical BMT for symptomatic sickle cell disease; assessed engraftment and toxicity in paediatric and adult patients |
| [NCT00919503](https://clinicaltrials.gov/study/NCT00919503) | Phase 2 | Completed | 98 | Treosulfan + fludarabine preparative regimen for nonmalignant disorders including hemoglobinopathies; MMF incorporated as post-transplant immunosuppression |
| [NCT01050855](https://clinicaltrials.gov/study/NCT01050855) | Phase 2 | Active, not recruiting | 75 | Phase II RIC pilot study for non-malignant diseases including hemoglobinopathies; bone marrow or cord blood as stem cell source |
| [NCT06872333](https://clinicaltrials.gov/study/NCT06872333) | Phase 2 | Recruiting | 62 | Open-label Phase II trial of allo-HSCT for high-risk hemoglobinopathies and red cell transfusion-dependent disorders; currently enrolling |
| [NCT03121001](https://clinicaltrials.gov/study/NCT03121001) | Phase 2 | Recruiting | 50 | HLA-haploidentical HSCT with low-dose TBI for clinically aggressive sickle cell disease; MMF included in GVHD prophylaxis protocol |
| [NCT02867800](https://clinicaltrials.gov/study/NCT02867800) | Phase 1 | Completed | 24 | Abatacept added to standard GVHD prophylaxis (calcineurin inhibitor + methotrexate) after HSCT for paediatric sickle cell disease; MMF used as comparator background therapy |
| [NCT04644016](https://clinicaltrials.gov/study/NCT04644016) | Phase 2 | Recruiting | 31 | Cord blood transplantation for life-threatening non-malignant hematologic disorders without matched related donors; assessing 1-year treatment-related mortality |
| [NCT01917708](https://clinicaltrials.gov/study/NCT01917708) | Phase 1 | Completed | 10 | Tolerability of abatacept combined with cyclosporine and mycophenolate mofetil as GVHD prophylaxis in children receiving unrelated donor HSCT for serious non-malignant diseases |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [39891881](https://pubmed.ncbi.nlm.nih.gov/39891881/) | 2025 | Clinical Dosing Guideline | Eur J Drug Metab Pharmacokinet | Population PK model and dosing recommendations for MMF in paediatric thalassemia patients undergoing HSCT; fills a critical gap in off-label dosing |
| [36372358](https://pubmed.ncbi.nlm.nih.gov/36372358/) | 2023 | Retrospective Cohort | Transplant Cell Ther | MMF immunosuppression boost for declining mixed chimerism in thalassemia transplants; directly demonstrates MMF's role in sustaining donor engraftment |
| [29061531](https://pubmed.ncbi.nlm.nih.gov/29061531/) | 2018 | Retrospective Cohort | Biol Blood Marrow Transplant | Unrelated donor HSCT for severe sickle cell disease with myeloablative busulfan/fludarabine/ATG regimen; tacrolimus and MMF used for GVHD prophylaxis |
| [28578010](https://pubmed.ncbi.nlm.nih.gov/28578010/) | 2017 | Prospective Cohort | Biol Blood Marrow Transplant | Unrelated cord blood transplantation with RIC for sickle cell disease; addition of thiotepa improved engraftment rates |
| [26860634](https://pubmed.ncbi.nlm.nih.gov/26860634/) | 2016 | Retrospective Cohort | Biol Blood Marrow Transplant | Alternative-donor HSCT with post-transplant cyclophosphamide for nonmalignant paediatric disorders including hemoglobinopathies and immunodeficiencies |
| [18940682](https://pubmed.ncbi.nlm.nih.gov/18940682/) | 2008 | Prospective Cohort | Biol Blood Marrow Transplant | Stable long-term donor engraftment following RIC-HCT from HLA-matched sibling donors for high-risk sickle cell disease |
| [17454192](https://pubmed.ncbi.nlm.nih.gov/17454192/) | 2007 | Retrospective Cohort | Hematology | Pure red cell aplasia incidence, risk factors, and management after major ABO-incompatible allo-HSCT; provides relevant post-HSCT safety context |
| [17180133](https://pubmed.ncbi.nlm.nih.gov/17180133/) | 2007 | Case Report | J Perinatol | Neonatal anaemia and hydrops fetalis following maternal MMF use during pregnancy; important teratogenicity safety signal |
| [15126382](https://pubmed.ncbi.nlm.nih.gov/15126382/) | 2004 | Review | Genetics | Historical perspective on genetics of hemoglobinopathies and lessons from genetics-medicine interface |

---

## Philippines Market Information

Mycophenolic acid (including its prodrug mycophenolate mofetil, CellCept® / Myfortic®) currently has **no registered products** in the Philippines FDA database, with zero license authorizations on record.

> For clinical use in Philippine transplant centres, procurement would require an Import License (pursuant to RA 9711 and its IRR) or a hospital-based compassionate/expanded access application submitted to the Philippines FDA. Prescribers should consult the international package insert (Roche CellCept® or Novartis Myfortic®) for complete prescribing information in the interim.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
MMF/MPA has an established, mechanistically well-supported role as GVHD prophylaxis in allo-HSCT for hemoglobinopathy, backed by multiple completed Phase 2 and Phase 4 trials — including an 823-patient multicenter prospective study in thalassemia major and a completed Phase 2 haploidentical BMT trial in sickle cell disease — plus a dedicated 2025 clinical dosing guideline. The evidence base is sufficient to support proceeding, provided that regulatory and safety safeguards appropriate to an unregistered drug in the Philippines are put in place.

**To proceed, the following is needed:**
- Apply for Philippines FDA import license or compassionate use approval before clinical administration
- Obtain complete international prescribing information (CellCept® / Myfortic® package insert) to establish local safety protocols covering contraindications, warnings, and major drug interactions
- Establish a therapeutic drug monitoring (TDM) protocol for MPA AUC-guided dosing, with particular attention to paediatric thalassemia patients based on the 2025 population PK model
- Confirm drug compatibility with locally available HSCT conditioning agents (tacrolimus, cyclosporine, fludarabine, busulfan) and verify local DDI data
- Seek ethics committee approval at the designated Philippine transplant centre before initiating any protocol incorporating MMF as GVHD prophylaxis
- Implement a pharmacovigilance reporting framework for adverse events in Philippine patients receiving off-label MMF in the HSCT setting
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

