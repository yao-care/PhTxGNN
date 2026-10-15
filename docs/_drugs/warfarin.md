---
layout: default
title: Warfarin
parent: Model Prediction Only (L5)
nav_order: 359
evidence_level: L5
indication_count: 7
---

# Warfarin
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **7** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Pharmacist Assessment Report

</div>

# Warfarin: From Thrombotic Disease to Thrombophilia

## One-Sentence Summary

Warfarin is an oral anticoagulant (vitamin K antagonist), originally used to treat pulmonary embolism, thrombotic disease and intracranial embolism.
The TxGNN model predicts it may be effective for **Thrombophilia** (a state of increased clotting tendency), with **1 clinical trial** and **20 publications** currently supporting this direction.
Most of the evidence consists of reviews and case reports, and the new indication is very close to warfarin's existing uses, so it is not a truly novel repurposing.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary embolism, thrombotic disease, intracranial embolism (from the knowledge graph; no approved indication text is available for the local registration) |
| Predicted New Indication | Thrombophilia (the top-ranked prediction by TxGNN score is heparin cofactor 2 deficiency, but thrombophilia has the strongest supporting evidence and is the focus of this report) |
| TxGNN Prediction Score | 99.75% (thrombophilia); 99.87% for the top-ranked prediction, heparin cofactor 2 deficiency |
| Evidence Level | L2 (one Phase 3 trial, but status unknown and not a direct warfarin-versus-control comparison; the data compilation conservatively rates it below L1) |
| Philippines Market Status | Cancelled only |
| Number of Registrations | 1 (cancelled) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Detailed mechanism of action data is not currently available. From known pharmacology, warfarin is a vitamin K antagonist. It reduces the synthesis of clotting factors II, VII, IX and X, which lowers the tendency of blood to clot. Its efficacy in venous thromboembolism and other thrombotic disease is well established, and mechanistically it may be applicable to inherited or acquired thrombophilia.

Thrombophilia is a state in which the blood clots too readily, so the original and predicted indications are closely related. Long-term anticoagulation to prevent recurrent venous thromboembolism is already standard practice for many patients with thrombophilia. This prediction therefore mostly confirms an existing clinical use rather than revealing a new one.

The other predictions are weaker. Heparin cofactor II deficiency and antithrombin deficiency type 2 are supported only by case reports. Factor V excess is supported by model prediction alone. Rheumatoid arthritis, fibrocystic breast disease and benign mammary dysplasia appear to be artifacts of drug-interaction co-occurrence, with no therapeutic rationale.

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT00895505](https://clinicaltrials.gov/study/NCT00895505) | Phase 3 | Unknown | 300 | Tests whether D-dimer testing can tailor the duration of oral anticoagulation after an unprovoked deep vein thrombosis (randomized, controlled). It evaluates a guidance strategy, not warfarin itself in thrombophilia. |

For the other predicted indications, there are no relevant trials of warfarin as a treatment. The four Phase 1 trials listed under rheumatoid arthritis are drug-interaction studies in which warfarin was only a probe substrate.

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [33141212](https://pubmed.ncbi.nlm.nih.gov/33141212/) | 2020 | Review | JAMA | Diagnosis and treatment of lower-limb venous thromboembolism; recurrence rates of 20-36% over 10 years |
| [39233011](https://pubmed.ncbi.nlm.nih.gov/39233011/) | 2024 | Review | J Thromb Haemost | ISTH communication on direct oral anticoagulants for secondary VTE prevention in severe thrombophilia; evidence is limited to cohort and single-centre studies |
| [39244017](https://pubmed.ncbi.nlm.nih.gov/39244017/) | 2024 | Review | Presse Med | Impact of thrombophilia on VTE management; factor V Leiden and prothrombin mutations are not clearly linked to recurrence |
| [32214817](https://pubmed.ncbi.nlm.nih.gov/32214817/) | 2020 | Cohort | Vasc Health Risk Manag | Prevalence and outcomes of thrombophilia in acute pulmonary embolism |
| [12871277](https://pubmed.ncbi.nlm.nih.gov/12871277/) | 2003 | Review | J Thromb Haemost | Management of thrombophilia; uncertainty about how test results should guide prolonged anticoagulation |
| [15706484](https://pubmed.ncbi.nlm.nih.gov/15706484/) | 2005 | Review | Semin Thromb Hemost | Inherited thrombophilia should not change the intensity of anticoagulant therapy |
| [7607583](https://pubmed.ncbi.nlm.nih.gov/7607583/) | 1995 | Case report | Haemostasis | Severe protein S deficiency; thrombosis not fully prevented by warfarin plus adjusted-dose heparin |
| [10718793](https://pubmed.ncbi.nlm.nih.gov/10718793/) | 2000 | Other | Br J Surg | Warfarin-induced skin necrosis is a rare complication (0.01-0.1%) |
| [3046272](https://pubmed.ncbi.nlm.nih.gov/3046272/) | 1988 | Other | Am Fam Physician | In cancer-associated coagulopathy (Trousseau's syndrome), heparin is preferred and warfarin does not seem beneficial |
| [14633797](https://pubmed.ncbi.nlm.nih.gov/14633797/) | 2003 | Other | Hematology Am Soc Hematol Educ Program | Diagnosis and treatment of thrombotic disorders |

Literature for other predicted indications is limited to case reports (for example heparin cofactor II deficiency, PMID 2214444, and antithrombin type IIB deficiency, PMID 29582922).

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0523 | Warfarin | Not stated | Not stated (registration status: cancelled) |

## Cytotoxicity

Not applicable. Warfarin is not an antineoplastic drug, so this section is omitted.

## Safety Considerations

- **Contraindications (from the knowledge graph, not label text)**: Hypertension, liver failure and liver disease, gallbladder disease, congestive heart failure, hypothyroidism, nephrotic syndrome, impaired renal function, psychotic and other mental disorders, connective tissue disease, bone and cartilage disease, substance abuse or dependence, blood coagulation disease, hyperlipidemia, anemia, cholestasis, chronic diarrheal disease.
- **Drug Interactions**: 100 interactions were found in total. Notable examples:
  - **Major**: acetylsalicylic acid (aspirin), metronidazole.
  - **Moderate**: ranitidine, rabeprazole, doxycycline, metformin, amoxicillin, bupropion, aprepitant, mesalazine, chenodeoxycholic acid, and corticosteroids (hydrocortisone, dexamethasone, betamethasone, budesonide, triamcinolone).
  - **Minor**: acarbose, albiglutide, ascorbic acid.
- **Other safety signals from the literature**: Warfarin-induced skin necrosis is rare. Danazol and leflunomide have been reported to increase warfarin's anticoagulant effect and require dose adjustment.

Please refer to the package insert for label warnings and contraindications.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
- Thrombophilia is essentially an extension of warfarin's existing anticoagulant use, so the prediction is plausible but not novel. The only Phase 3 trial has unknown status and tests a D-dimer-guided strategy rather than warfarin itself, and the literature is mostly reviews and case reports. In the Philippines, the only registration is cancelled, so the drug is not currently marketed under it.

**To proceed, the following is needed:**
- Package insert warnings and contraindications from the DOH-FDA Philippines (currently missing and a blocking gap for safety screening)
- Detailed mechanism of action data (for example from DrugBank)
- Clarification of why the Philippines registration was cancelled and whether another warfarin product is currently available
- Direct comparative evidence (warfarin versus control or versus direct oral anticoagulants) in specific thrombophilia subtypes
- A safety monitoring plan (INR monitoring, interaction management) for the intended population
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

