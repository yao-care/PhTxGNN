"""FDA Drug Data Loading and Filtering - Philippine Version"""

import json
from pathlib import Path
from typing import Optional

import pandas as pd
import yaml


def load_field_config() -> dict:
    """Load field mapping configuration."""
    config_path = Path(__file__).parent.parent.parent.parent / "config" / "fields.yaml"
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_fda_drugs(filepath: Optional[Path] = None) -> pd.DataFrame:
    """Load Philippine FDA/PNF drug data.

    Args:
        filepath: JSON file path, defaults to data/raw/ph_fda_drugs.json

    Returns:
        DataFrame containing all drugs

    Raises:
        FileNotFoundError: When data file not found
    """
    config = load_field_config()

    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "raw" / "ph_fda_drugs.json"

    if not filepath.exists():
        raise FileNotFoundError(
            f"Drug data not found: {filepath}\n"
            f"Please follow these steps:\n"
            f"1. Download PNF-EML from DOH website\n"
            f"2. Place it in data/raw/ directory\n"
            f"3. Run: uv run python scripts/process_fda_data.py"
        )

    with open(filepath, "r", encoding=config.get("encoding", "utf-8")) as f:
        data = json.load(f)

    # Handle both list format and object with key
    if isinstance(data, list):
        df = pd.DataFrame(data)
    else:
        df = pd.DataFrame(data.get("drugs", data))

    return df


def filter_active_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """Filter active drugs (exclude withdrawn).

    Args:
        df: Original drug DataFrame

    Returns:
        DataFrame containing only active drugs
    """
    config = load_field_config()
    field_mapping = config["field_mapping"]
    withdrawn_statuses = config.get("withdrawn_statuses", [])

    # Get status field name
    status_field = field_mapping.get("status", "")

    if status_field and status_field in df.columns:
        # Filter non-withdrawn drugs
        active = df[~df[status_field].isin(withdrawn_statuses)].copy()
    else:
        active = df.copy()

    # Filter drugs with ingredients (required for TxGNN)
    ingredients_field = field_mapping.get("ingredients", "")
    if ingredients_field and ingredients_field in df.columns:
        active = active[active[ingredients_field].notna() & (active[ingredients_field] != "")]

    # Reset index
    active = active.reset_index(drop=True)

    return active


def get_drug_summary(df: pd.DataFrame) -> dict:
    """Get drug data summary statistics.

    Args:
        df: Drug DataFrame

    Returns:
        Summary statistics dictionary
    """
    config = load_field_config()
    field_mapping = config["field_mapping"]

    ingredients_field = field_mapping.get("ingredients", "ingredient")
    indication_field = field_mapping.get("indication", "")
    dosage_form_field = field_mapping.get("dosage_form", "")

    summary = {"total_count": len(df)}

    if ingredients_field and ingredients_field in df.columns:
        summary["with_ingredient"] = int(df[ingredients_field].notna().sum())
        summary["unique_ingredients"] = int(df[ingredients_field].nunique())

    if indication_field and indication_field in df.columns:
        summary["with_indication"] = int(df[indication_field].notna().sum())

    if dosage_form_field and dosage_form_field in df.columns:
        summary["dosage_forms"] = df[dosage_form_field].value_counts().to_dict()

    return summary
