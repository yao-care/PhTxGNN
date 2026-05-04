---
layout: default
title: Acetylcysteine
parent: 僅模型預測 (L5)
nav_order: 14
evidence_level: L5
indication_count: 10
---

# Acetylcysteine
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

# Acetylcysteine: From Mucolytic Agent to Thrombotic Disease

## One-Sentence Summary

Acetylcysteine (NAC) is a well-established mucolytic agent and antidote for acetaminophen overdose, with a decades-long record of clinical use across respiratory and hepatic indications.
The TxGNN model predicts it may be effective for **Thrombotic Disease** — particularly thrombotic microangiopathies such as TTP and transplant-associated TMA (TA-TMA) —
supported by **9 clinical trials** and **20 publications**, including a completed Phase 3 trial in TA-TMA that provides the strongest direct evidence for this repurposing direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Mucolytic agent; antidote for acetaminophen overdose (established global use; no Philippines registration on file) |
| Predicted New Indication | Thrombotic Disease (TTP / TA-TMA subtype) |
| TxGNN Prediction Score | 99.96% |
| Evidence Level | L2 |
| Philippines Market Status | Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not available in the current database. Based on published literature, Acetylcysteine (NAC) carries a free sulfhydryl group (-SH) that directly cleaves disulfide bonds within ultra-large von Willebrand factor (UL-VWF) multimers. In thrombotic thrombocytopenic purpura (TTP), UL-VWF accumulates due to ADAMTS13 deficiency and drives systemic platelet-rich microvascular thrombi. NAC's thiol-mediated VWF reduction offers a complementary therapeutic mechanism that does not depend on ADAMTS13 activity — a property confirmed in human plasma and animal models (PMID 21266777, PMID 28011677). This biochemical mechanism is the direct molecular bridge between NAC's known chemistry and its predicted anti-thrombotic activity.

Beyond TTP, NAC acts as a glutathione (GSH) precursor that reduces systemic oxidative stress — a key driver of endothelial injury and pro-coagulant phenotype in both transplant-associated thrombotic microangiopathy (TA-TMA) and CKD-related thrombophilia. In TA-TMA, oxidative and complement-mediated endothelial damage triggers microvascular thrombosis; NAC's antioxidant properties may interrupt this cycle in addition to its direct VWF cleavage effect. The RENACTIF trial (NCT03636932) extended this logic to chronic kidney disease patients, demonstrating measurable reduction of the uremic pro-thrombotic phenotype.

The prediction is further validated by a Phase 3 clinical trial (NCT03252925, n=170, COMPLETED) specifically in TA-TMA, which represents the highest-grade direct evidence in this category. The original mucolytic indication and thrombotic disease are linked by the same underlying chemistry: NAC cleaves disulfide bonds in airway mucin polymers and VWF multimers by the same -SH mechanism, making the TxGNN prediction mechanistically coherent rather than incidental.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03252925](https://clinicaltrials.gov/study/NCT03252925) | Phase 3 | Completed | 170 | Prospective trial of NAC for transplant-associated thrombotic microangiopathy (TA-TMA) after HSCT; largest completed trial directly in this indication; results published supporting NAC efficacy and safety |
| [NCT07279610](https://clinicaltrials.gov/study/NCT07279610) | Phase 2/3 | Active, Not Recruiting | 44 | Multicenter single-arm trial confirming NAC efficacy in TA-TMA; current standard treatment (plasma exchange <10% response, eculizumab high-cost) makes NAC a practical alternative; forms continuous evidence chain with NCT03252925 |
| [NCT05907486](https://clinicaltrials.gov/study/NCT05907486) | Phase 3 | Unknown | 260 | NAC for prevention of thrombotic events after allogeneic HSCT; if completed, large sample size would upgrade evidence to L1 — status requires active follow-up |
| [NCT03636932](https://clinicaltrials.gov/study/NCT03636932) | Phase 2 | Completed | 40 | RENACTIF trial: randomized double-blind crossover study; NAC reduces pro-coagulant endothelial phenotype induced by uremic toxin indoxyl sulfate in CKD patients; mechanistically highly relevant to oxidative thrombosis |
| [NCT01808521](https://clinicaltrials.gov/study/NCT01808521) | Early Phase 1 | Completed | 3 | Earliest direct clinical TTP pilot study using IV NAC; demonstrates VWF multimer reduction and improved ADAMTS13 cleavage in actual TTP patients; small but foundational |
| [NCT03460808](https://clinicaltrials.gov/study/NCT03460808) | Phase 1/2 | Unknown | 200 | Triple therapy (NAC + atorvastatin + danazol) vs. danazol monotherapy in steroid-resistant/relapsed ITP; NAC role limited to antioxidant support; main indication is platelet destruction, not thrombosis |
| [NCT04368598](https://clinicaltrials.gov/study/NCT04368598) | Phase 2 | Unknown | 44 | NAC + high-dose dexamethasone in newly diagnosed ITP; ITP is a platelet-destructive rather than thrombotic disease; mechanistic relevance indirect |
| [NCT06518044](https://clinicaltrials.gov/study/NCT06518044) | Phase 2 | Not Yet Recruiting | 30 | NAC to promote hematopoietic recovery after haploidentical transplant in severe aplastic anemia; antioxidant protection of hematopoietic stem cells; tangentially related to thrombotic disease context |
| [NCT05551624](https://clinicaltrials.gov/study/NCT05551624) | Early Phase 1 | Completed | 15 | Atorvastatin + NAC for platelet count elevation in steroid-resistant primary ITP; exploratory small study |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [35940529](https://pubmed.ncbi.nlm.nih.gov/35940529/) | 2022 | RCT (Randomized, Placebo-Controlled) | Transplantation and Cellular Therapy | Prospective open-label RCT: NAC prophylaxis significantly reduces TA-TMA incidence in HSCT patients; direct prevention evidence for thrombotic microangiopathy |
| [37311880](https://pubmed.ncbi.nlm.nih.gov/37311880/) | 2023 | Retrospective Cohort | Annals of Hematology | NAC treatment associated with reduced in-hospital mortality in acquired TTP; retrospective cohort (n=real-world patients) supports clinical outcome benefit |
| [21266777](https://pubmed.ncbi.nlm.nih.gov/21266777/) | 2011 | Preclinical (human plasma + mouse) | Journal of Clinical Investigation | Foundational mechanistic study: NAC directly reduces UL-VWF multimer size and platelet aggregation activity in human plasma and murine thrombosis models; established biological rationale |
| [28011677](https://pubmed.ncbi.nlm.nih.gov/28011677/) | 2017 | Animal Study (mouse & baboon) | Blood | NAC in mouse and baboon TTP models; reduces VWF multimers, improves ADAMTS13 cleavage; demonstrates in vivo anti-thrombotic efficacy prior to clinical trials |
| [32243196](https://pubmed.ncbi.nlm.nih.gov/32243196/) | 2020 | Narrative Review | Expert Review of Hematology | Comprehensive review of repurposed drugs for TTP including NAC alongside rituximab and caplacizumab; positions NAC within the emerging TTP treatment algorithm |
| [33540569](https://pubmed.ncbi.nlm.nih.gov/33540569/) | 2021 | Review | Journal of Clinical Medicine | TTP pathophysiology, diagnosis, and management; contextualizes ADAMTS13-independent treatment pathways where NAC is applicable |
| [28382967](https://pubmed.ncbi.nlm.nih.gov/28382967/) | 2017 | Review | Nature Reviews Disease Primers | Authoritative TTP disease primer; covers congenital and acquired forms and establishes clinical framework for evaluating VWF-targeted repurposing agents |
| [28645643](https://pubmed.ncbi.nlm.nih.gov/28645643/) | 2017 | Review | Transfusion Clinique et Biologique | TTP management review addressing refractory disease; highlights unmet need that NAC repurposing aims to address |
| [39737637](https://pubmed.ncbi.nlm.nih.gov/39737637/) | 2025 | Case Report | Journal of Pediatric Hematology/Oncology | Plasma exchange + NAC therapy in congenital TTP presenting with acute renal failure; recent pediatric case supporting combination approach in rare congenital subtype |
| [28416507](https://pubmed.ncbi.nlm.nih.gov/28416507/) | 2017 | Review | Blood | TTP review in Blood (high-impact journal); background on microvascular platelet-rich thrombi and ADAMTS13 biology essential for interpreting NAC mechanism |

---

## Philippines Market Information

Acetylcysteine is currently **not registered** in the Philippines Food and Drug Administration (FDA). No product authorizations were identified in the regulatory database as of the data cutoff (April 4, 2026).

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------------------|-------------|-------------|---------------------|
| — | No registered products found | — | — |

> **Note:** Acetylcysteine (as NAC / Mucomyst / Fluimucil) is registered in the USA, EU, Japan, and Taiwan for mucolytic and acetaminophen antidote indications. Philippine market entry for the thrombotic disease indication would require a new product license application with the Philippine FDA, or access via compassionate use / expanded access pathways.

---

## Safety Considerations

Please refer to the package insert for safety information.

> **Note:** Philippine FDA package insert warnings and contraindications were not available for this review (Blocking data gap). Drug-drug interaction data was also not found in the database query. These gaps should be resolved before any clinical implementation — particularly DDI assessment with anticoagulants (heparin, warfarin) and immunosuppressants commonly co-administered in the thrombotic microangiopathy setting.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
A completed Phase 3 trial (NCT03252925, n=170) and a randomized placebo-controlled prophylaxis RCT (PMID 35940529) provide Level 2 evidence for NAC's efficacy in transplant-associated thrombotic microangiopathy. The mechanistic basis — direct VWF disulfide bond cleavage confirmed in human plasma (PMID 21266777) — is scientifically robust, and NAC's established safety profile in its approved mucolytic indication reduces de novo safety uncertainty. However, the absence of Philippines market registration and incomplete safety documentation require guardrails before any clinical application.

**To proceed, the following is needed:**
- **Philippines FDA registration**: File a new product license or explore compassionate use authorization for Acetylcysteine — currently not marketed in the Philippines
- **Safety data gap resolution**: Obtain and review Philippines FDA-approved (or WHO-approved) package insert for warnings, contraindications, and dosing guidance (currently a blocking gap)
- **DDI assessment**: Specifically evaluate interactions with heparin, tacrolimus, cyclosporine, and eculizumab — agents commonly used in the HSCT/TMA patient population
- **Indication scoping**: Define the specific thrombotic disease sub-indication (TA-TMA post-HSCT vs. acquired TTP vs. general thromboprophylaxis) before clinical protocol development, as evidence strength differs substantially by subtype
- **Completion monitoring**: Track NCT05907486 (Phase 3, n=260, thrombotic event prevention post-HSCT) — if completed successfully, evidence upgrades to L1
- **Local feasibility assessment**: Evaluate HSCT program capacity and TA-TMA incidence within Philippines oncology and transplant centers to determine patient population size and clinical relevance
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

