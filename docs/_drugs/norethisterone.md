---
layout: default
title: Norethisterone
parent: 僅模型預測 (L5)
nav_order: 255
evidence_level: L5
indication_count: 1
---

# Norethisterone
{: .fs-9 }

證據等級: **L5** | 預測適應症: **1** 個
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

Using the TxGNN pipeline context to generate the Philippines repurposing evaluation report for Norethisterone.

---

# Norethisterone: From Hormonal Contraception to Amenorrhea

## One-Sentence Summary

Norethisterone is a synthetic progestogen (progestin) with a long clinical history in hormonal contraception and combination hormone therapies for gynecological conditions.
The TxGNN model predicts it may be effective for **Amenorrhea**,
with **8 clinical trials** and **20 publications** currently supporting this direction.

---

## Quick Overview

| Item | Content |
|------|---------|
| Original Indication | Hormonal contraception (established use; no Philippines regulatory record on file) |
| Predicted New Indication | Amenorrhea |
| TxGNN Prediction Score | 99.60% |
| Evidence Level | L3 |
| Philippines Market Status | ✗ Not Marketed |
| Number of Registrations | 0 |
| Recommended Decision | Hold |

---

## Why is This Prediction Reasonable?

Currently, detailed mechanism of action data is not available in this evidence pack. Based on known pharmacological information, Norethisterone is a synthetic progestogen structurally related to 19-nortestosterone. It binds to progesterone receptors in the uterine endometrium, inducing decidualization. When Norethisterone is withdrawn following a treatment course in estrogen-primed patients, the resulting fall in progestogen levels triggers a withdrawal bleed — this is the pharmacological basis of the **progestogen challenge test**, a standard diagnostic and therapeutic intervention for secondary amenorrhea.

The mechanistic connection between Norethisterone and amenorrhea is therefore well-grounded: secondary amenorrhea is frequently caused by relative progesterone deficiency in the setting of adequate estrogen priming, and progestogen supplementation is the established clinical approach. Norethisterone is recognised in international guidelines (e.g., RCOG, WHO) for diagnosing and managing secondary amenorrhea via this withdrawal-bleed mechanism.

An important nuance emerges from the clinical trial evidence, however. In all Phase 3 trials identified, Norethisterone appears as an **add-back therapy** component of GnRH antagonist regimens (e.g., Relugolix + Estradiol + Norethindrone Acetate), where its role is to **prevent** GnRH-induced amenorrhea — not to **treat** pre-existing amenorrhea. The repurposing direction therefore requires careful clarification: the mechanistic rationale points to treating secondary amenorrhea, but the existing trial evidence addresses preventing drug-induced menstrual suppression. These are distinct clinical contexts, and the exact repurposing hypothesis must be defined before proceeding.

---

## Clinical Trial Evidence

| Trial Number | Phase | Status | Enrollment | Key Findings |
|-------------|-------|--------|------------|--------------|
| [NCT03049735](https://clinicaltrials.gov/study/NCT03049735) | Phase 3 | Completed | 388 | LIBERTY 1: Relugolix 40 mg + Estradiol 1 mg + Norethindrone Acetate 0.5 mg vs placebo over 24 weeks for heavy menstrual bleeding associated with uterine fibroids; Norethisterone functions as add-back therapy to prevent GnRH-induced amenorrhea and bone loss |
| [NCT03103087](https://clinicaltrials.gov/study/NCT03103087) | Phase 3 | Completed | 382 | LIBERTY 2: Parallel design to LIBERTY 1; confirms Relugolix combination therapy reduces heavy menstrual bleeding in uterine fibroids; Norethindrone Acetate add-back role consistent across both pivotal studies |
| [NCT03412890](https://clinicaltrials.gov/study/NCT03412890) | Phase 3 | Completed | 477 | LIBERTY Extension: Long-term 28-week open-label extension of LIBERTY 1/2; sustained efficacy of Relugolix combination therapy; menstrual pattern monitoring throughout provides real-world data on progestogen add-back and amenorrhea prevention |
| [NCT03751124](https://clinicaltrials.gov/study/NCT03751124) | Phase 3 | Completed | 229 | Randomised withdrawal study up to 104 weeks; menstrual recovery after Relugolix withdrawal was a key observation endpoint; Norethisterone add-back role informs reversibility of amenorrhea |
| [NCT01817530](https://clinicaltrials.gov/study/NCT01817530) | Phase 2 | Completed | 571 | Elagolix Phase 2b in uterine fibroids with heavy menstrual bleeding; evaluates elagolix alone and with add-back therapy; provides mechanistic evidence for progestogen's role in managing GnRH-related menstrual suppression |
| [NCT01441635](https://clinicaltrials.gov/study/NCT01441635) | Phase 2 | Completed | 271 | Elagolix Phase 2a proof-of-concept; safety and efficacy of elagolix vs placebo for uterine bleeding reduction in premenopausal women; informs the add-back therapy paradigm that includes Norethisterone |
| [NCT05620355](https://clinicaltrials.gov/study/NCT05620355) | Phase 3 | Unknown | 312 | BG2109 (novel GnRH antagonist) alone and with add-back therapy for uterine fibroid-associated heavy menstrual bleeding; Norethisterone add-back role under further characterisation; completion date March 2025, status unconfirmed |
| [NCT06953076](https://clinicaltrials.gov/study/NCT06953076) | N/A | Recruiting | 111 | MySaturn: Observational ultrasound study monitoring fibroid morphology changes during Relugolix + Norethisterone treatment; non-interventional design; provides real-world morphological monitoring data |

---

## Literature Evidence

| PMID | Year | Type | Journal | Key Findings |
|------|------|------|---------|--------------|
| [37863160](https://pubmed.ncbi.nlm.nih.gov/37863160/) | 2024 | RCT Subgroup | Am J Obstet Gynecol | LIBERTY Long-Term Extension subgroup in Black/African American women: Relugolix combination therapy (including norethindrone acetate 0.5 mg) substantially improved fibroid-associated heavy menstrual bleeding over 52 weeks; norethisterone component maintained hormonal stability throughout |
| [38530848](https://pubmed.ncbi.nlm.nih.gov/38530848/) | 2024 | RCT | PLoS One | WHICH trial: norethisterone enanthate (NET-EN) vs DMPA-IM injectable contraceptives in 4,000+ women; menstrual effects including amenorrhea were quantified; NET-EN showed distinct estradiol and bleeding profiles with implications for HIV risk and contraceptive tolerability |
| [37103532](https://pubmed.ncbi.nlm.nih.gov/37103532/) | 2023 | Review | Obstet Gynecol | Oral GnRH antagonists for uterine leiomyomas: comprehensive review of add-back steroid hormone combinations; norethindrone acetate role in preventing hypothalamic suppression sequelae including amenorrhea and bone loss is specifically addressed |
| [23641480](https://pubmed.ncbi.nlm.nih.gov/23641480/) | 2013 | Cochrane Review | Cochrane Database Syst Rev | Combination injectable contraceptives including norethisterone-based formulations: highly effective and reversible; amenorrhea is a recognised and quantified side effect; acceptability data across multiple populations |
| [18843662](https://pubmed.ncbi.nlm.nih.gov/18843662/) | 2008 | Cochrane Review | Cochrane Database Syst Rev | Earlier Cochrane review of combination injectable contraceptives; menstrual pattern changes including amenorrhea discussed as a primary acceptability determinant; norethisterone formulations included |
| [6786825](https://pubmed.ncbi.nlm.nih.gov/6786825/) | 1981 | Clinical Trial | Contraception | Phase I trial of Norethisterone Enanthate (NEN) and Norethisterone Acetate (NET) in 20 fertile Cuban women; preovulatory LH/FSH peaks abolished in all subjects; amenorrhea, spotting and irregular bleeding observed as direct pharmacological effects — earliest direct evidence of norethisterone-induced amenorrhea |
| [2660092](https://pubmed.ncbi.nlm.nih.gov/2660092/) | 1989 | Review | Pediatr Clin North Am | Principles of hormonal contraception including norethisterone-based formulations; pharmacological basis for menstrual regulation relevant to understanding amenorrhea mechanism |
| [3659794](https://pubmed.ncbi.nlm.nih.gov/3659794/) | 1987 | Review | Rev Prat | Progestational contraception: role of progestogens including norethisterone in menstrual regulation; amenorrhea as both mechanism of action and clinical outcome reviewed |
| [12335903](https://pubmed.ncbi.nlm.nih.gov/12335903/) | 1979 | Review | Contracept Fertil Sex | Endometriosis and infertility: early evidence on progestogen therapy in gynecological conditions sharing mechanistic overlap with secondary amenorrhea management |
| [779431](https://pubmed.ncbi.nlm.nih.gov/779431/) | 1976 | Review | Adv Steroid Biochem Pharmacol | Long-acting injectable contraceptives including norethisterone formulations: pharmacological basis of menstrual suppression and amenorrhea induction reviewed; foundational pharmacology reference |

---

## Philippines Market Information

Norethisterone currently has **no registered products** in the Philippines FDA database. There are no authorization numbers, brand names, or approved indications on file. Any clinical development pathway would require a new drug application or registration through standard Philippines FDA channels.

---

## Safety Considerations

Please refer to the package insert for safety information.

---

## Conclusion and Next Steps

**Decision: Hold**

**Rationale:**
While the mechanistic rationale for Norethisterone in amenorrhea is pharmacologically sound — progestogen supplementation can induce withdrawal bleeding in progesterone-deficient secondary amenorrhea — all available Phase 3 clinical trial evidence positions Norethisterone exclusively as an add-back therapy to *prevent* GnRH-induced amenorrhea, not as a primary treatment for amenorrhea itself. Combined with the absence of any Philippines market authorization, the evidence base is insufficient to advance at this stage without first resolving key mechanistic and regulatory questions.

**To proceed, the following is needed:**

- **Clarify the repurposing hypothesis**: confirm whether the target clinical context is (a) progestogen challenge for secondary amenorrhea workup/treatment, or (b) prevention of drug-induced amenorrhea in GnRH-based regimens — these are distinct indications requiring separate evidence strategies
- **Retrieve MOA data** from DrugBank API (DB00717) to formally document progesterone receptor binding pathway and document it in the evidence pack
- **Retrieve safety data** from Philippines FDA–registered equivalent package inserts (Taiwan TFDA or EMA SmPC), particularly regarding thromboembolic risk, estrogen-dependent condition contraindications, and liver function warnings
- **Philippines regulatory pathway assessment**: determine whether a new drug application or a line-extension of a regionally registered product is the appropriate route
- **Targeted literature search**: identify studies specifically evaluating norethisterone monotherapy for secondary amenorrhea (progestogen challenge design) separate from the GnRH add-back context
## Disclaimer

This content is for research purposes only and does not constitute medical advice.
Clinical validation is required before any clinical application.

---

