---
layout: default
title: Lidocaine
parent: 僅模型預測 (L5)
nav_order: 207
evidence_level: L5
indication_count: 10
---

# Lidocaine
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

# Lidocaine: From Local Anesthesia to Conjunctival Disorder

## One-Sentence Summary

Lidocaine is a well-established voltage-gated sodium channel (Nav) blocker, widely used internationally as a local anesthetic and antiarrhythmic agent, though it carries no current Philippines registration in this evidence pack.
The TxGNN model predicts it may be effective for **Conjunctival Disorder** — the highest-evidence prediction among 10 candidates —
with **17 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Local anesthetic / ventricular antiarrhythmic (no Philippines registration found) |
| Predicted New Indication | Conjunctival Disorder |
| TxGNN Prediction Score | 99.84% |
| Evidence Level | L1 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Proceed with Guardrails |

> **Note on indication selection:** The TxGNN top-ranked prediction (punctate epithelial keratoconjunctivitis, score 99.99%) has zero supporting evidence (L5). This report features **conjunctival disorder** (rank 6, score 99.84%) because it carries the strongest evidence base (L1, multiple Phase 4 RCTs) and the only actionable recommendation in the prediction set.

---

## Why is This Prediction Reasonable?

Detailed mechanism of action data was not included in this evidence pack. Based on well-established pharmacology, Lidocaine reversibly blocks voltage-gated sodium channels (Nav1.7, Nav1.8) on sensory nerve endings, preventing depolarization and halting pain signal propagation. This is the universal basis of its local anesthetic action. The conjunctiva is richly innervated by trigeminal sensory fibers expressing these same Nav subtypes, making the mechanistic link direct and intuitive: blocking Nav channels on conjunctival nociceptors suppresses pain and potentially dampens neurogenic inflammation during and after tissue manipulation.

The original indication (local anesthesia) and the predicted new indication (conjunctival disorder) are not so much a "jump" as an extension of the same mechanism into a specific anatomical compartment. Multiple Phase 4 RCTs have already validated this in practice — Lidocaine gel and drops are routinely applied to the conjunctival surface for pterygium surgery, peribulbar blocks, and intravitreal injection procedures. The question is therefore not whether Lidocaine works on the conjunctiva, but whether a formalized conjunctival indication should be pursued in the Philippines market.

A second, independent mechanistic strand comes from SUNCT syndrome (Short-lasting Unilateral Neuralgiform headache attacks with Conjunctival injection and Tearing). Multiple prospective studies and a meta-analysis (PMID 33361408) document intravenous Lidocaine aborting acute SUNCT/SUNA attacks — disorders where conjunctival injection and tearing are core diagnostic criteria. This implicates Lidocaine in modulating the trigeminal-autonomic axis driving conjunctival vascular and secretory responses, beyond simple peripheral anesthesia.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|---------|------|------|------|---------|
| [NCT05978687](https://clinicaltrials.gov/study/NCT05978687) | Phase 4 | Completed | 41 | Head-to-head RCT: Lidocaine Ophtesic Gel vs subconjunctival Xylocaine injection for pterygium excision — most direct evidence of topical lidocaine for conjunctival anesthesia |
| [NCT02324166](https://clinicaltrials.gov/study/NCT02324166) | Phase 4 | Unknown | 54 | Cefazolin-Lidocaine solution reducing pain from subconjunctival antibiotic injection in retinal surgery — Lidocaine as primary pain management agent |
| [NCT03397069](https://clinicaltrials.gov/study/NCT03397069) | N/A | Completed | 90 | Midazolam added to Lidocaine peribulbar block for cataract surgery — supports Lidocaine as the primary conjunctival/periocular anesthetic |
| [NCT02150460](https://clinicaltrials.gov/study/NCT02150460) | Phase 4 | Completed | 100 | Single vs double-site peribulbar anaesthesia (Lidocaine-based) for cataract surgery — safety and efficacy of Lidocaine periocular block |
| [NCT03189329](https://clinicaltrials.gov/study/NCT03189329) | Phase 4 | Completed | 66 | Lidocaine vs levobupivacaine in retrobulbar block for vitreoretinal surgery — cerebral oxygenation and cognitive safety monitoring |
| [NCT01087489](https://clinicaltrials.gov/study/NCT01087489) | N/A | Completed | 53 | 4% lidocaine drops vs 3.5% lidocaine HCl gel for intravitreal injection comfort — comparative ophthalmic anesthesia formulations |
| [NCT03480711](https://clinicaltrials.gov/study/NCT03480711) | N/A | Completed | 40 | Modified vs conventional trabeculectomy for POAG — Lidocaine as conjunctival surgical anesthetic |
| [NCT01898728](https://clinicaltrials.gov/study/NCT01898728) | N/A | Completed | 101 | Povidone-iodine conjunctival bacterial reduction: lidocaine gel dilating formulation vs drops — supports safety of Lidocaine gel on conjunctiva |
| [NCT03902925](https://clinicaltrials.gov/study/NCT03902925) | Phase 1/2 | Completed | 56 | Peribulbar vs sub-Tenon + topical jelly anesthesia (includes Lidocaine) for vitreoretinal surgery — pain assessment across anesthetic routes |
| [NCT05925894](https://clinicaltrials.gov/study/NCT05925894) | N/A | Completed | 60 | Intracameral mydriatics in POAG cataract surgery — Lidocaine as standard intraocular anesthetic component |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|-----|------|------|---------|
| [18989343](https://pubmed.ncbi.nlm.nih.gov/18989343/) | 2009 | RCT | Eye (London) | Lidocaine 2% gel vs tetracaine 1% drops for primary pterygium surgery — RCT establishing lidocaine gel efficacy as sole topical anesthetic |
| [15799734](https://pubmed.ncbi.nlm.nih.gov/15799734/) | 2005 | Clinical Study | Acta Ophthalmol Scand | Lidocaine 2% gel in pterygium surgery — confirms effective topical conjunctival anesthesia without injection |
| [16954710](https://pubmed.ncbi.nlm.nih.gov/16954710/) | 2006 | Clinical Study | Ophthalmologica | Viscous lidocaine for postoperative pain relief after pterygium surgery — extends benefit beyond intraoperative anesthesia |
| [33361408](https://pubmed.ncbi.nlm.nih.gov/33361408/) | 2021 | Prospective + Meta-analysis | J Neurol Neurosurg Psychiatry | IV Lidocaine for SUNCT/SUNA — prospective open-label study with single-arm meta-analysis; conjunctival injection/tearing as core diagnostic features that lidocaine resolves |
| [34003160](https://pubmed.ncbi.nlm.nih.gov/34003160/) | 2021 | Review | Neurology India | SUNCT and SUNA update: documents Lidocaine among treatment options for a syndrome defined by conjunctival signs |
| [38415675](https://pubmed.ncbi.nlm.nih.gov/38415675/) | 2024 | Review | Cephalalgia | Most current SUNCT/SUNA review including Lidocaine treatment evidence and mechanism discussion |
| [29720816](https://pubmed.ncbi.nlm.nih.gov/29720816/) | 2018 | Review | Ann Indian Acad Neurol | SUNHA review — summarizes Lidocaine's role in a disorder whose hallmark is conjunctival injection |
| [23330822](https://pubmed.ncbi.nlm.nih.gov/23330822/) | 2013 | Observational | Current Eye Research | Different anesthetics for intravitreal injection pain — evaluates Lidocaine efficacy and tolerability at the conjunctival surface |
| [10696746](https://pubmed.ncbi.nlm.nih.gov/10696746/) | 2000 | Clinical Study | Retina | Topical Lidocaine anesthesia as alternative to peribulbar/retrobulbar block for posterior vitrectomy — supports minimally invasive conjunctival application |
| [37819721](https://pubmed.ncbi.nlm.nih.gov/37819721/) | 2023 | Basic Science | JCI Insight | Nerve-goblet cell association drives allergen passage in conjunctivitis — mechanistic rationale for Nav modulation interrupting conjunctival neuroinflammatory signaling |

---

## Philippines Market Information

Lidocaine currently has **no registered products** in the Philippines (0 active licenses; market status: not marketed). This is almost certainly a data gap rather than a true absence — Lidocaine is one of the most widely used drugs globally and appears on the WHO Essential Medicines List. A targeted search of the Philippine FDA (FDA Philippines) database is strongly recommended before drawing conclusions about local availability.

---

## Safety Considerations

Formal safety data (Philippines FDA package insert warnings, contraindications) was not available in this evidence pack.

**Critical clinical safety note for ophthalmic use:** Chronic or repeated application of topical anesthetics to the corneal surface is a well-recognized clinical contraindication — prolonged exposure impairs corneal epithelial healing and can cause corneal ulceration. Any conjunctival repurposing must be strictly limited to **perioperative or single-procedure use**, not chronic therapeutic dosing.

**For SUNCT/SUNA indication (IV route):** PMID 19250287 documents neuropsychiatric toxicity (75%) and cardiological effects (50%) in all patients receiving IV Lidocaine for headache — requiring cardiac monitoring and specialist oversight.

---

## Conclusion and Next Steps

**Decision: Proceed with Guardrails**

**Rationale:**
Multiple completed Phase 4 RCTs directly establish Lidocaine's safety and efficacy on the conjunctival surface for ophthalmic procedures, and a prospective meta-analysis documents IV Lidocaine's effect on conjunctival symptoms via the trigeminal-autonomic axis. The evidence base for ophthalmic anesthesia applications meets L1 criteria.

**To proceed, the following is needed:**

- **Philippines FDA registration search**: Lidocaine is almost certainly marketed locally under product names not yet captured — manual search of the FDA Philippines database required before any "not available" conclusion
- **MOA documentation**: DrugBank API query for DB00281 to formally document Nav channel subtype specificity and pharmacokinetic profile
- **Indication scoping**: Distinguish two separate evidence tracks — (1) procedural conjunctival anesthesia (strong L1 evidence, low regulatory risk) vs. (2) SUNCT/SUNA treatment with conjunctival symptoms (moderate evidence, requires neurology specialist input and cardiac monitoring infrastructure)
- **Formulation assessment**: Identify which Lidocaine formulations are feasible in the Philippines context (2% gel, 4% drops, injectable) — route compatibility is currently pending
- **Safety file compilation**: Obtain Philippines FDA-equivalent package insert to complete the S1 safety screening that is currently blocked by DG001
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

