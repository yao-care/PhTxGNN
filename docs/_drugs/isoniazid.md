---
layout: default
title: Isoniazid
parent: Model Prediction Only (L5)
nav_order: 186
evidence_level: L5
indication_count: 1
last_modified_at: 2026-10-30
description: "Isoniazid: predicted new indication Conjunctivitis (evidence level L4). Approved use: Pulmonary tuberculosis"
monitor_inn: "Isoniazid"
predicted_indications: ["conjunctivitis"]
---

# Isoniazid
{: .fs-9 }

Evidence Level: **L5** | Predicted Indications: **1** 
{: .fs-6 .fw-300 }

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist" markdown="1">

## Pharmacist Assessment Report

</div>

## Isoniazid: From Pulmonary Tuberculosis to Conjunctivitis
{: .text-alpha }

## One-Sentence Summary

Isoniazid is an antimycobacterial drug originally used to treat pulmonary tuberculosis.
The TxGNN model predicts it may be effective for **conjunctivitis**, but there are **0 registered clinical trials** and only **11 publications** (mostly case reports and reviews), so the evidence is weak and largely indirect.

## Quick Overview

| Item | Content |
|------|------|
| Original Indication | Pulmonary tuberculosis |
| Predicted New Indication | Conjunctivitis |
| TxGNN Prediction Score | 0.9936 |
| Evidence Level | L5 |
| Philippines Market Status | Listed in the Philippine National Formulary (1 of 1) – FDA Philippines registration status is not included in this data |
| Number of Registrations | 1 (valid: 1) |
| Recommended Decision | Hold |

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available. Based on known information, isoniazid is an antimycobacterial agent whose efficacy in tuberculosis is established, and it may be mechanistically applicable to conjunctivitis only in a narrow, infection-related setting.

The model's high score is not directly supported by a mechanism. The literature suggests two indirect links:

1. **Tuberculosis-related eye disease.** Isoniazid's antimycobacterial activity is relevant to ocular disease linked to tuberculosis, such as primary conjunctival TB and phlyctenular keratoconjunctivitis. The latter is a hypersensitivity reaction to mycobacterial antigens, and isoniazid prophylaxis may reduce it.
2. **BCG-associated reactive syndrome.** Isoniazid has been used for reactive arthritis after intravesical BCG therapy, a syndrome in which conjunctivitis can occur.

These links cover infection-related or BCG-related conjunctivitis only. They do not extend to conjunctivitis in general (bacterial, viral, allergic). Several retrieved papers also describe isoniazid or other systemic drugs as *causes* of ocular adverse effects, which points to possible harm rather than benefit.

## Clinical Trial Evidence

Currently no related clinical trials registered.

## Literature Evidence

None of the publications is an RCT. Those most relevant to the predicted indication are listed first.

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [14253168](https://pubmed.ncbi.nlm.nih.gov/14253168/) | 1965 | Observational prophylaxis field study | Am Rev Respir Dis | Isoniazid prophylaxis for phlyctenular keratoconjunctivitis among Eskimos in southwestern Alaska |
| [33607832](https://pubmed.ncbi.nlm.nih.gov/33607832/) | 2021 | Case report + review | Medicine | Pediatric phlyctenular keratoconjunctivitis associated with primary sinonasal tuberculosis |
| [10641112](https://pubmed.ncbi.nlm.nih.gov/10641112/) | 1999 | Case series | Oftalmologia | 28 cases of tuberculous keratoconjunctivitis, 13 of them in children with primary TB |
| [14089390](https://pubmed.ncbi.nlm.nih.gov/14089390/) | 1964 | Case report | Arch Ophthalmol | Primary tuberculosis of the conjunctiva |
| [5103251](https://pubmed.ncbi.nlm.nih.gov/5103251/) | 1971 | Not classified | Ann Ocul | Local use of isoniazid in ocular tuberculosis |
| [10084171](https://pubmed.ncbi.nlm.nih.gov/10084171/) | 1999 | Case report | Rev Rhum (Engl Ed) | Isoniazid useful in refractory arthropathy after intravesical BCG therapy |
| [12226788](https://pubmed.ncbi.nlm.nih.gov/12226788/) | 2002 | Case report | Dtsch Med Wochenschr | Chronic reactive arthritis with conjunctivitis after intravesical BCG |
| [1363080](https://pubmed.ncbi.nlm.nih.gov/1363080/) | 1992 | Review | Optom Clin | Ocular side effects of systemic drugs, including drug-induced conjunctivitis |
| [10084173](https://pubmed.ncbi.nlm.nih.gov/10084173/) | 1999 | Case report + review | Rev Rhum (Engl Ed) | Polyarthritis after intravesical BCG immunotherapy, review of 26 cases |
| [8136810](https://pubmed.ncbi.nlm.nih.gov/8136810/) | 1993 | Case series | Rev Rhum (Ed Fr) | Polyarthritis in 4 patients after intravesical BCG for bladder carcinoma |

## Philippines Market Information

| Authorization Number | Product Name | Dosage Form | Approved Indication |
|---------|------|------|-----------|
| PNF-0264 | Isoniazid (single-ingredient; status: valid) | Not specified | Not specified |

## Safety Considerations

- **Contraindications / risk conditions (from the drug-disease knowledge graph, not label text):** liver failure, acute liver failure, liver disease, hepatitis, gallbladder disease, porphyria (including inherited porphyria and porphyrin metabolism disease), peripheral neuropathy and peripheral nervous system disease, diabetes mellitus, diabetic ketoacidosis, gout, substance abuse/dependence, and slow acetylator status.
- **Drug Interactions:** 100 interactions were identified. Those shown are mostly Moderate in severity:
  - Antidiabetic agents: acarbose, albiglutide, alogliptin, metformin, pioglitazone, canagliflozin, chlorpropamide, dapagliflozin
  - Vitamin D analogues: cholecalciferol, calcifediol, calcitriol
  - Others: metronidazole, budesonide (including nasal), alosetron, picosulfuric acid
  - Minor: corticosteroids (hydrocortisone, triamcinolone, dexamethasone, betamethasone)
- **Ocular adverse effects:** the retrieved literature associates systemic drugs, including isoniazid, with ocular side effects. This is relevant when considering use in eye disease.

Package-insert warnings and contraindications were not available. Please refer to the package insert for label-based safety information.

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
The TxGNN score is very high, but no clinical trials exist and the literature consists of old case reports and reviews that address only tuberculosis- or BCG-related eye disease, not conjunctivitis in general. The Philippines registration is cancelled, and some literature points to ocular harm.

**To proceed, the following is needed:**
- Narrow the hypothesis to a defined subgroup (for example, tuberculosis-associated phlyctenular keratoconjunctivitis) and review it systematically.
- Obtain mechanism of action data to support a mechanistic link.
- Obtain package-insert warnings and contraindications from the DOH-FDA Philippines website.
- Assess whether the available routes of administration are compatible with an ocular indication.
- Clarify the regulatory pathway given that the only registration (PNF-0264) is cancelled.
- Weigh ocular adverse-effect risk, hepatotoxicity and neuropathy risks against any potential benefit.
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

