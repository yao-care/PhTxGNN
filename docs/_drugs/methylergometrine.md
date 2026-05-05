---
layout: default
title: Methylergometrine
parent: 僅模型預測 (L5)
nav_order: 181
evidence_level: L5
indication_count: 10
---

# Methylergometrine
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

The data-report skill confirms I must work only from the provided JSON data without fabricating values. Since `original_indications` is empty and there are no Philippines licenses, I'll clearly note when drawing on established pharmacological knowledge. The primary repurposing candidate I'll feature is **migraine disorder** (rank #3 in TxGNN), as ranks #1 and #2 are identified as graph artefacts or pharmacologically contraindicated — migraine is the only candidate with genuine clinical literature (L3).

---

# Methylergometrine: From Postpartum Hemorrhage to Migraine Disorder

## One-Sentence Summary

Methylergometrine is an ergot alkaloid used in obstetrics for the prevention and treatment of postpartum hemorrhage by promoting uterine contraction.
The TxGNN model scores **migraine disorder** at **99.84%** (rank #3 overall; selected as the highest-evidence candidate after ranks #1 and #2 were disqualified as graph artefacts or contraindicated),
with **0 clinical trials** and **7 publications** currently supporting this direction — including two studies that directly documented its clinical use in refractory migraine.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Postpartum hemorrhage / uterine atony (obstetric use; no Philippines registration on record) |
| Predicted New Indication | Migraine Disorder (TxGNN rank #3; top evidence-supported candidate) |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data for Methylergometrine is not currently available in this evidence pack. Based on established pharmacology, Methylergometrine is an ergot alkaloid that acts as the **active metabolite of methysergide** — the drug that was the gold standard for migraine prophylaxis for several decades before it was withdrawn due to fibrotic side effects. Both compounds share the same ergoline scaffold and exert their effects primarily through serotonin receptor modulation (5-HT₂A/2C), α-adrenergic agonism, and dopamine receptor interactions in the central and peripheral nervous systems.

The connection to migraine is both mechanistic and historical. The 5-HT₂A/2C pathway is directly implicated in migraine pathophysiology — modulating cortical spreading depression, trigeminal neurovascular activation, and cranial vessel tone. Because Methylergometrine is structurally and pharmacologically one step removed from methysergide, it inherits the same receptor-level rationale that made methysergide effective. Its cranial vasoconstrictive properties also align with the acute-phase mechanism shared by ergotamine, another well-established antimigraine ergot in the same family.

Two small clinical studies (PMID 23432443; PMID 19895705) tested Methylergometrine directly in migraine patients, confirming that this TxGNN prediction reflects real clinical use rather than a purely algorithmic artefact. The remaining literature anchors the broader ergot-antimigraine pharmacological context. Importantly, rank #1 (hypertrichosis) and rank #4 (Ambras type hypertrichosis) are attributed to rare-disease node over-connectivity in the knowledge graph, rank #2 (pulmonary hypertension) is mechanistically contradicted — the drug is expected to worsen that condition — and rank #9 (migraine with brainstem aura) is explicitly contraindicated due to basilar artery spasm risk.

---

## Clinical Trial Evidence

Currently no related clinical trials registered.

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|-------------|
| [23432443](https://pubmed.ncbi.nlm.nih.gov/23432443/) | 2013 | Clinical series / retrospective | *Headache* | Saper & Evans report oral methylergonovine maleate used specifically for refractory migraine and cluster headache prevention — the most direct evidence of clinical use for this indication |
| [19895705](https://pubmed.ncbi.nlm.nih.gov/19895705/) | 2009 | Prospective observational | *Head & Face Medicine* | Pilot open-label study assessed IV methylergonovine in emergency treatment of severe migraine in female patients; preliminary efficacy signal noted |
| [18644039](https://pubmed.ncbi.nlm.nih.gov/18644039/) | 2008 | Historical review | *Cephalalgia* | Traces the synthesis and clinical history of methysergide (parent compound of methylergometrine) in migraine; establishes the 5-HT₂ receptor mechanism as foundational to the entire drug class |
| [10759904](https://pubmed.ncbi.nlm.nih.gov/10759904/) | 2000 | Clinical trial | *Headache* | Baclofen trial in cluster headache; lists methylergonovine maleate among documented prophylactic therapies for cluster headache, supporting its use in the wider headache spectrum |
| [9665056](https://pubmed.ncbi.nlm.nih.gov/9665056/) | 1998 | Pharmacological study | *Circulation* | Compared coronary vasoconstrictor potential across antimigraine ergots including methylergometrine; classifies it within the antimigraine ergot family with significant vasoconstrictive activity — relevant both for efficacy and safety profiling |
| [20419307](https://pubmed.ncbi.nlm.nih.gov/20419307/) | 2011 | Case report | *Archives of Gynecology and Obstetrics* | Postpartum cerebral angiitis case; contextualises methylergometrine's vasospastic potential as a safety signal requiring consideration when using it in migraine |
| [5361033](https://pubmed.ncbi.nlm.nih.gov/5361033/) | 1969 | Clinical study | *Przeglad Lekarski* | Early clinical evaluation of Deseril-retard (methysergide) in idiopathic headache; historical precedent for the drug class in headache management |

---

## Philippines Market Information

Methylergometrine is not currently registered in the Philippines. No authorizations, product listings, or dosage form data are on record (`total_licenses = 0`). Any future clinical use pathway would require a full new drug application to the Philippine FDA.

---

## Safety Considerations

Formal safety data (package insert warnings, contraindications, and drug-drug interaction records) were not retrievable for this evidence pack review. Please refer to the package insert for complete safety information.

The available literature, however, surfaces three critical safety signals that must be considered before any clinical use in migraine:

- **Vasoconstriction and cardiovascular risk**: As an ergot alkaloid, Methylergometrine can cause significant vasospasm including coronary artery constriction (PMID 9665056). Patients with cardiovascular disease, peripheral vascular disease, uncontrolled hypertension, or Raynaud's phenomenon should be excluded.
- **⛔ Pulmonary hypertension — contraindicated**: Two case reports (PMID 26050249, PMID 18277575) document acute pulmonary hypertensive crises following Methylergometrine administration. The drug's α-adrenergic and 5-HT₂ agonism causes pulmonary vasoconstriction — it is expected to **worsen**, not treat, this condition.
- **⛔ Migraine with brainstem aura — contraindicated**: International headache guidelines explicitly advise against vasoconstrictive ergot drugs in this migraine subtype. The risk of basilar artery spasm makes use in migraine with brainstem aura an absolute contraindication.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
Methylergometrine has biologically plausible and historically grounded activity in migraine — it is the active metabolite of methysergide, the historical gold standard for migraine prophylaxis — and at least two small clinical studies demonstrate direct use in refractory migraine patients. However, the total evidence base reaches only L3 (observational studies and retrospective series), with no registered RCTs, incomplete safety documentation, and zero Philippines market presence. The drug's potent vasoconstrictor profile also demands careful patient selection criteria before any broad clinical application.

**To proceed, the following is needed:**

- **Mechanism of action documentation**: Retrieve full MOA from DrugBank API (DB00353) to complete the pharmacological rationale
- **Package insert safety review**: Download and parse Philippines or FDA/EMA package insert for complete warnings, contraindications, and DDI profile
- **Phase 2 RCT design**: A prospective, randomised, placebo-controlled trial evaluating oral methylergonovine maleate in refractory migraine prophylaxis is needed to advance evidence from L3 to L2/L1
- **Patient selection protocol**: Define explicit exclusion criteria — cardiovascular disease, pulmonary hypertension, migraine with brainstem aura, uncontrolled hypertension, pregnancy/postpartum within 6 weeks
- **Philippines registration strategy**: Prepare new drug application to Philippine FDA if Phase 2 evidence is supportive; evaluate compassionate use or expanded access pathways in the interim
- **Comparator benchmarking**: Compare efficacy and safety against current migraine prophylactics (topiramate, valproate, propranolol, CGRP monoclonal antibodies) to establish positioning
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

