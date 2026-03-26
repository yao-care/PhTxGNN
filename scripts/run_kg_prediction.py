#!/usr/bin/env python3
"""Run Knowledge Graph Prediction for PhTxGNN

Uses TxGNN knowledge graph to predict drug repurposing candidates for
Philippine National Formulary (PNF) drugs.

Usage:
    uv run python scripts/run_kg_prediction.py

Prerequisites:
    1. Run process_fda_data.py
    2. Run prepare_external_data.py

Output:
    data/processed/repurposing_candidates.csv
"""

import json
from pathlib import Path

import pandas as pd

from phtxgnn.mapping.drugbank_mapper import (
    build_name_index,
    load_drugbank_vocab,
    map_ingredient_to_drugbank,
)
from phtxgnn.predict.repurposing import (
    build_drug_indication_map,
    load_drug_disease_relations,
)


def load_pnf_drugs(filepath: Path | None = None) -> pd.DataFrame:
    """Load Philippine National Formulary drugs.

    Args:
        filepath: Path to ph_fda_drugs.json

    Returns:
        DataFrame with drug data
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent / "data" / "raw" / "ph_fda_drugs.json"

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Handle both list format and object with "drugs" key
    if isinstance(data, list):
        return pd.DataFrame(data)
    return pd.DataFrame(data.get("drugs", data))


def map_pnf_to_drugbank(pnf_df: pd.DataFrame) -> pd.DataFrame:
    """Map PNF drugs to DrugBank IDs.

    Args:
        pnf_df: PNF drugs DataFrame

    Returns:
        DataFrame with DrugBank mapping results
    """
    drugbank_df = load_drugbank_vocab()
    name_index = build_name_index(drugbank_df)

    results = []
    for _, row in pnf_df.iterrows():
        ingredient = row["ingredient"]

        # Try to map to DrugBank
        drugbank_id = map_ingredient_to_drugbank(ingredient, name_index)
        mapping_source = "drugbank" if drugbank_id else "failed"

        results.append({
            "license_id": row["license_id"],
            "brand_name": row["brand_name"],
            "original_ingredient": row["raw_ingredient"],
            "normalized_ingredient": ingredient,
            "synonyms": "",
            "drugbank_id": drugbank_id,
            "mapping_success": drugbank_id is not None,
            "mapping_source": mapping_source,
        })

    return pd.DataFrame(results)


def find_all_indications(drug_mapping_df: pd.DataFrame) -> pd.DataFrame:
    """Find all TxGNN indications for mapped PNF drugs.

    Since PNF doesn't have indication data, we use TxGNN drug-disease
    relations to find ALL potential indications for each drug.

    Args:
        drug_mapping_df: DrugBank mapping results

    Returns:
        DataFrame with all potential indications
    """
    # Load TxGNN drug-disease relations
    relations_df = load_drug_disease_relations()

    # Build indication map from TxGNN
    kg_drug_map = build_drug_indication_map(relations_df)

    candidates = []
    for _, row in drug_mapping_df.iterrows():
        if not row["mapping_success"]:
            continue

        drug_name = row["normalized_ingredient"]

        # Look up all indications from TxGNN
        kg_diseases = kg_drug_map.get(drug_name, set())

        for disease in kg_diseases:
            candidates.append({
                "license_id": row["license_id"],
                "brand_name": row["brand_name"],
                "ingredient": drug_name,
                "drugbank_id": row["drugbank_id"],
                "potential_indication": disease,
                "source": "TxGNN Knowledge Graph",
            })

    result_df = pd.DataFrame(candidates)

    # Remove duplicates
    if len(result_df) > 0:
        result_df = result_df.drop_duplicates(
            subset=["license_id", "ingredient", "potential_indication"]
        )

    return result_df


def get_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """Calculate mapping statistics.

    Args:
        mapping_df: Mapping results DataFrame

    Returns:
        Statistics dictionary
    """
    total = len(mapping_df)
    mapped = mapping_df["mapping_success"].sum()

    return {
        "total_drugs": total,
        "mapped_drugs": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_drugbank_ids": mapping_df[mapping_df["mapping_success"]]["drugbank_id"].nunique(),
    }


def main():
    print("=" * 60)
    print("PhTxGNN Knowledge Graph Prediction")
    print("=" * 60)
    print()

    base_dir = Path(__file__).parent.parent

    # 1. Load PNF drug data
    print("1. Loading PNF drug data...")
    pnf_df = load_pnf_drugs()
    print(f"   Total drugs: {len(pnf_df)}")

    # 2. DrugBank mapping
    print("\n2. Mapping to DrugBank...")
    drug_mapping = map_pnf_to_drugbank(pnf_df)
    stats = get_mapping_stats(drug_mapping)
    print(f"   Mapped: {stats['mapped_drugs']}/{stats['total_drugs']} ({stats['mapping_rate']:.1%})")
    print(f"   Unique DrugBank IDs: {stats['unique_drugbank_ids']}")

    # Save mapping results
    output_dir = base_dir / "data" / "processed"
    output_dir.mkdir(parents=True, exist_ok=True)
    drug_mapping.to_csv(output_dir / "drug_mapping.csv", index=False)
    print(f"   Saved: {output_dir / 'drug_mapping.csv'}")

    # 3. Find all TxGNN indications
    print("\n3. Finding TxGNN indications...")
    candidates = find_all_indications(drug_mapping)
    print(f"   Total indication pairs: {len(candidates)}")

    if len(candidates) > 0:
        unique_drugs = candidates["ingredient"].nunique()
        unique_diseases = candidates["potential_indication"].nunique()
        print(f"   Unique drugs with indications: {unique_drugs}")
        print(f"   Unique diseases: {unique_diseases}")

        # Top indications
        top_diseases = candidates["potential_indication"].value_counts().head(5)
        print("\n   Top 5 disease indications:")
        for disease, count in top_diseases.items():
            print(f"     - {disease}: {count} drugs")

    # 4. Save results
    print("\n4. Saving results...")
    candidates.to_csv(output_dir / "repurposing_candidates.csv.gz", index=False)
    print(f"   Saved: {output_dir / 'repurposing_candidates.csv.gz'}")

    print()
    print("=" * 60)
    print("Done!")
    print("=" * 60)
    print()
    print("Next step: Generate FHIR resources")
    print("  uv run python scripts/generate_fhir_resources.py")


if __name__ == "__main__":
    main()
