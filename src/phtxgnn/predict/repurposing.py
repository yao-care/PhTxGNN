"""老藥新用預測 - 基於 TxGNN 知識圖譜"""

from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import pandas as pd


def load_drug_disease_relations(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 藥物-疾病關係

    Args:
        filepath: CSV 檔案路徑

    Returns:
        藥物-疾病關係 DataFrame
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "drug_disease_relations.csv"

    return pd.read_csv(filepath)


def build_drug_indication_map(relations_df: pd.DataFrame) -> Dict[str, Set[str]]:
    """建立藥物 -> 適應症集合的映射

    Args:
        relations_df: 藥物-疾病關係 DataFrame

    Returns:
        {drug_name: {disease1, disease2, ...}}
    """
    # 只取 indication 和 off-label use
    indications = relations_df[relations_df["relation"].isin(["indication", "off-label use"])]

    drug_map = {}
    for _, row in indications.iterrows():
        drug = row["x_name"].upper()
        disease = row["y_name"]

        if drug not in drug_map:
            drug_map[drug] = set()
        drug_map[drug].add(disease)

    return drug_map


def find_repurposing_candidates(
    drug_mapping_df: pd.DataFrame,
    indication_mapping_df: pd.DataFrame,
    relations_df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """Find drug repurposing candidates

    Compare current drug indications with TxGNN knowledge graph indications
    to identify potential new indications.

    Args:
        drug_mapping_df: Drug DrugBank mapping results
        indication_mapping_df: Indication disease mapping results
        relations_df: TxGNN drug-disease relations

    Returns:
        Drug repurposing candidates DataFrame
    """
    if relations_df is None:
        relations_df = load_drug_disease_relations()

    # Build TxGNN drug indication map
    kg_drug_map = build_drug_indication_map(relations_df)

    # Column name mapping (support both English and Chinese)
    license_col = "license_id" if "license_id" in drug_mapping_df.columns else "許可證字號"
    ingredient_col = "normalized_ingredient" if "normalized_ingredient" in drug_mapping_df.columns else "標準化成分"
    brand_col = "brand_name" if "brand_name" in drug_mapping_df.columns else "中文品名"

    # Build existing drug indications (vectorized)
    indication_license_col = "license_id" if "license_id" in indication_mapping_df.columns else "許可證字號"
    current_diseases_df = indication_mapping_df[
        indication_mapping_df["disease_name"].notna()
    ][[indication_license_col, "disease_name"]].copy()
    current_diseases_df["disease_lower"] = current_diseases_df["disease_name"].str.lower()
    current_drug_diseases = current_diseases_df.groupby(indication_license_col)["disease_lower"].apply(set).to_dict()

    # Build drug info index (vectorized)
    valid_drugs = drug_mapping_df[drug_mapping_df["drugbank_id"].notna()].copy()

    # Get unique (license_id, ingredient) combinations
    unique_pairs = valid_drugs[[license_col, ingredient_col, brand_col, "drugbank_id"]].drop_duplicates()

    candidates = []

    for _, row in unique_pairs.iterrows():
        license_no = row[license_col]
        drug_name = row[ingredient_col]

        # Query TxGNN for all indications of this drug
        kg_diseases = kg_drug_map.get(drug_name, set())
        if not kg_diseases:
            continue

        # Get current indications
        current_diseases = current_drug_diseases.get(license_no, set())

        # Find potential new indications
        for disease in kg_diseases:
            disease_lower = disease.lower()

            # Quick check if already exists
            is_new = all(
                curr_d not in disease_lower and disease_lower not in curr_d
                for curr_d in current_diseases
            )

            if is_new:
                candidates.append({
                    "license_id": license_no,
                    "brand_name": row[brand_col],
                    "ingredient": drug_name,
                    "drugbank_id": row["drugbank_id"],
                    "potential_indication": disease,
                    "source": "TxGNN Knowledge Graph",
                })

    result_df = pd.DataFrame(candidates)

    # Remove duplicates
    if len(result_df) > 0:
        # First: remove exact duplicates per license
        result_df = result_df.drop_duplicates(
            subset=["license_id", "ingredient", "potential_indication"]
        )

        # Second: for DL prediction efficiency, keep only unique (drugbank_id, disease) pairs
        # This prevents redundant DL predictions for the same drug-disease combination
        # We keep the first occurrence (arbitrary license_id as representative)
        result_df = result_df.drop_duplicates(
            subset=["drugbank_id", "potential_indication"],
            keep="first"
        )

    return result_df


def generate_repurposing_report(candidates_df: pd.DataFrame) -> dict:
    """Generate drug repurposing report statistics

    Args:
        candidates_df: Candidate drugs DataFrame

    Returns:
        Statistics report dictionary
    """
    if len(candidates_df) == 0:
        return {
            "total_candidates": 0,
            "unique_drugs": 0,
            "unique_diseases": 0,
            "top_diseases": [],
            "top_drugs": [],
        }

    # Support both English and Chinese column names
    drug_col = "ingredient" if "ingredient" in candidates_df.columns else "藥物成分"
    indication_col = "potential_indication" if "potential_indication" in candidates_df.columns else "潛在新適應症"

    unique_drugs = candidates_df[drug_col].nunique()
    unique_diseases = candidates_df[indication_col].nunique()

    # Most common potential new indications
    top_diseases = candidates_df[indication_col].value_counts().head(10).to_dict()

    # Drugs with most potential new indications
    drug_counts = candidates_df.groupby(drug_col)[indication_col].nunique()
    top_drugs = drug_counts.sort_values(ascending=False).head(10).to_dict()

    return {
        "total_candidates": len(candidates_df),
        "unique_drugs": unique_drugs,
        "unique_diseases": unique_diseases,
        "top_diseases": top_diseases,
        "top_drugs": top_drugs,
    }
