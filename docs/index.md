---
layout: default
title: Drug Repurposing Predictions — Philippines
nav_order: 1
---

# PhTxGNN Drug Repurposing Reports

Philippine drug repurposing predictions using the TxGNN graph neural network.

{: .warning }
> **Disclaimer**: These predictions are for research purposes only. They do not constitute medical advice and require clinical validation before any clinical application.

<!-- local-home:start（母目錄 .claude/gen_local_home_20261029.py 產生，勿手改）-->
## Philippines: what this site covers

This site publishes reports for **{{ site.data.drug_stats.total_drugs }}** medicines listed in the registration data of [FDA Philippines](https://www.fda.gov.ph/) (Philippines).

Reports by evidence level: L1 {{ site.data.drug_stats.level_counts.L1 }} · L2 {{ site.data.drug_stats.level_counts.L2 }} · L3 {{ site.data.drug_stats.level_counts.L3 }} · L4 {{ site.data.drug_stats.level_counts.L4 }} · L5 {{ site.data.drug_stats.level_counts.L5 }}

### Highest evidence levels on this site

| Medicine | Evidence level |
|---|---|
| [Acetylcysteine](/drugs/acetylcysteine/) | L1 |
| [Dexamethasone](/drugs/dexamethasone/) | L1 |
| [Nepafenac](/drugs/nepafenac/) | L1 |
| [Rifabutin](/drugs/rifabutin/) | L1 |
| [Tegafur](/drugs/tegafur/) | L1 |
| [Chloramphenicol](/drugs/chloramphenicol/) | L1 |
| [Hydrocortisone](/drugs/hydrocortisone/) | L1 |
| [Salmeterol](/drugs/salmeterol/) | L1 |
| [Tiotropium](/drugs/tiotropium/) | L1 |
| [Letrozole](/drugs/letrozole/) | L1 |

### Medicines covered only by this site among the 30 TxGNN sites

| Medicine | Evidence level |
|---|---|
| [Interferon Alfa](/drugs/interferon-alfa/) | L5 |
| [Physostigmine](/drugs/physostigmine/) | N/A |

<!-- local-home:end -->

## Overview

PhTxGNN analyzes drugs from the Philippine National Formulary (PNF) using the TxGNN graph neural network to identify potential new therapeutic uses for existing medications.

### Key Statistics

| Metric | Value |
|--------|-------|
| PNF Drugs Analyzed | 529 |
| DrugBank Mapping Rate | 85.4% |
| Predicted New Indications (known uses excluded) | {{ site.data.site_stats.indications }} |
| Drug Reports | {{ site.data.site_stats.drugs }} |
| Unique Diseases | 880 |

## Data Sources

- **Philippine National Formulary (PNF)**: Essential Medicines List, 8th Edition (2022)
- **TxGNN**: Graph neural network trained on a knowledge graph; predicts drug-disease relationships (known uses already in the graph are excluded)
- **DrugBank**: Drug identifier mapping

## Quick Links

- [FHIR API](/fhir/metadata) - Access predictions via FHIR R4 API
- [SMART App](/smart/launch.html) - Launch SMART on FHIR application

## How It Works

1. **Drug Extraction**: Extract drug names from PNF-EML 2022
2. **DrugBank Mapping**: Map drug names to standard DrugBank identifiers
3. **TxGNN Prediction**: Use the TxGNN graph neural network (score ≥ 0.99) to find potential new indications, excluding known uses
4. **FHIR Export**: Generate FHIR R4 resources for interoperability

## Contact

For questions or feedback, please open an issue on GitHub.

---

*Last updated: {{ site.time | date: "%Y-%m-%d" }}*

---

## About the Developer

This platform is developed and operated by **藥提醒科技有限公司** (yao.care, company registration
number 83620786, 12F, No. 220, Sec. 2, Taiwan Blvd., West Dist., Taichung City, Taiwan).

PhTxGNN is the the Philippines site of the company's "TxGNN Drug Repurposing" product line.
The same system is deployed across 30 countries and regions, each named `{CC}TxGNN`
(JpTxGNN, UsTxGNN, DETxGNN, and so on) at `{cc}txgnn.yao.care`.
Product overview: <https://www.yao.care/medical/txgnn/>.

The TxGNN model itself was developed by the Zitnik Lab at Harvard Medical School and published
in *Nature Medicine*. This platform is the production system 藥提醒科技有限公司 built on top of that
model, covering national drug-registration data integration, deep-learning prediction that excludes uses already recorded in the knowledge graph, PubMed / ClinicalTrials evidence grading, and SMART on FHIR
electronic health record integration.
