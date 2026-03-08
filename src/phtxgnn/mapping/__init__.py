"""實體映射模組"""

from .normalizer import normalize_ingredient, extract_ingredients, get_all_synonyms
from .drugbank_mapper import (
    load_drugbank_vocab,
    build_name_index,
    map_ingredient_to_drugbank,
    map_fda_drugs_to_drugbank,
    get_mapping_stats,
)

# Disease mapper is a template file - import after localization
# from .disease_mapper import (...)

__all__ = [
    # Normalizer
    "normalize_ingredient",
    "extract_ingredients",
    "get_all_synonyms",
    # Drug mapping
    "load_drugbank_vocab",
    "build_name_index",
    "map_ingredient_to_drugbank",
    "map_fda_drugs_to_drugbank",
    "get_mapping_stats",
]
