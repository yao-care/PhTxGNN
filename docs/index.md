---
layout: default
title: Home
nav_order: 1
---

# PhTxGNN Drug Repurposing Reports

Philippine drug repurposing predictions using TxGNN knowledge graph.

{: .warning }
> **Disclaimer**: These predictions are for research purposes only. They do not constitute medical advice and require clinical validation before any clinical application.

## Overview

PhTxGNN analyzes drugs from the Philippine National Formulary (PNF) using the TxGNN knowledge graph to identify potential new therapeutic uses for existing medications.

### Key Statistics

| Metric | Value |
|--------|-------|
| PNF Drugs Analyzed | 529 |
| DrugBank Mapping Rate | 85.4% |
| Drug-Indication Pairs | 3,322 |
| Unique Drugs with Indications | 338 |
| Unique Diseases | 880 |

## Data Sources

- **Philippine National Formulary (PNF)**: Essential Medicines List, 8th Edition (2022)
- **TxGNN Knowledge Graph**: Drug-disease relationship predictions
- **DrugBank**: Drug identifier mapping

## Quick Links

- [FHIR API](/fhir/metadata) - Access predictions via FHIR R4 API
- [SMART App](/smart/launch.html) - Launch SMART on FHIR application

## How It Works

1. **Drug Extraction**: Extract drug names from PNF-EML 2022
2. **DrugBank Mapping**: Map drug names to standard DrugBank identifiers
3. **TxGNN Prediction**: Use knowledge graph to find potential indications
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
model, covering national drug-registration data integration, dual knowledge-graph and
deep-learning prediction, PubMed / ClinicalTrials evidence grading, and SMART on FHIR
electronic health record integration.
