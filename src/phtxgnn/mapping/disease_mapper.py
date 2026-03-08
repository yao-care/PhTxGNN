"""Disease Mapping Module - Filipino/Tagalog disease terms to TxGNN ontology

Note: PNF-EML does not include indication data, so this module is primarily
for future use with news monitoring and other Filipino-language sources.
"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# Filipino/Tagalog disease terms -> English mapping
# Used for news monitoring and Filipino-language sources
DISEASE_DICT = {
    # === Cardiovascular System ===
    "alta presyon": "hypertension",
    "high blood": "hypertension",
    "mataas na presyon ng dugo": "hypertension",
    "baba presyon": "hypotension",
    "sakit sa puso": "heart disease",
    "atake sa puso": "heart attack",
    "atake sa puso": "myocardial infarction",
    "pagpalya ng puso": "heart failure",
    "stroke": "stroke",
    "atake serebral": "stroke",

    # === Respiratory System ===
    "hika": "asthma",
    "asma": "asthma",
    "broncitis": "bronchitis",
    "pulmonya": "pneumonia",
    "ubo": "cough",
    "sipon": "common cold",
    "trangkaso": "influenza",
    "flu": "influenza",
    "tuberculosis": "tuberculosis",
    "tb": "tuberculosis",

    # === Digestive System ===
    "gastritis": "gastritis",
    "ulser": "ulcer",
    "ulser sa tiyan": "gastric ulcer",
    "pagtatae": "diarrhea",
    "constipation": "constipation",
    "tibi": "constipation",
    "almoranas": "hemorrhoids",
    "appendicitis": "appendicitis",
    "hepatitis": "hepatitis",

    # === Nervous System ===
    "sakit ng ulo": "headache",
    "migraine": "migraine",
    "maigraine": "migraine",
    "epilepsy": "epilepsy",
    "seizure": "seizure",
    "kombulsyon": "seizure",
    "parkinsons": "parkinson disease",
    "alzheimers": "alzheimer disease",

    # === Mental Health ===
    "depresyon": "depression",
    "depression": "depression",
    "anxiety": "anxiety disorder",
    "pagkabalisa": "anxiety disorder",
    "schizophrenia": "schizophrenia",
    "bipolar": "bipolar disorder",
    "insomnia": "insomnia",
    "hindi makatulog": "insomnia",

    # === Endocrine System ===
    "diabetes": "diabetes mellitus",
    "diyabetis": "diabetes mellitus",
    "mataas na asukal": "diabetes mellitus",
    "thyroid": "thyroid disease",
    "goiter": "goiter",
    "bosyo": "goiter",

    # === Musculoskeletal System ===
    "arthritis": "arthritis",
    "rayuma": "arthritis",
    "gout": "gout",
    "osteoporosis": "osteoporosis",
    "sakit ng likod": "back pain",
    "sakit ng buto": "bone pain",

    # === Skin Diseases ===
    "eczema": "eczema",
    "eksema": "eczema",
    "psoriasis": "psoriasis",
    "buni": "ringworm",
    "an-an": "tinea versicolor",
    "tagulabay": "herpes zoster",
    "singaw": "mouth ulcer",

    # === Urinary System ===
    "uti": "urinary tract infection",
    "impeksyon sa ihi": "urinary tract infection",
    "kidney stone": "kidney stone",
    "bato sa bato": "kidney stone",
    "kidney failure": "kidney failure",

    # === Eye Diseases ===
    "sore eyes": "conjunctivitis",
    "mata sa mata": "conjunctivitis",
    "glaucoma": "glaucoma",
    "cataract": "cataract",
    "katarata": "cataract",

    # === ENT ===
    "ear infection": "otitis",
    "impeksyon sa tenga": "otitis",
    "tonsillitis": "tonsillitis",
    "sinusitis": "sinusitis",

    # === Infections ===
    "dengue": "dengue",
    "malaria": "malaria",
    "covid": "covid-19",
    "coronavirus": "covid-19",
    "hiv": "hiv infection",
    "aids": "aids",
    "rabies": "rabies",

    # === Allergies ===
    "allergy": "allergy",
    "alerhiya": "allergy",
    "allergic rhinitis": "allergic rhinitis",
    "hay fever": "allergic rhinitis",

    # === Women's Health ===
    "dysmenorrhea": "dysmenorrhea",
    "masakit na regla": "dysmenorrhea",
    "menopause": "menopause",
    "pcos": "polycystic ovary syndrome",

    # === Cancer ===
    "cancer": "cancer",
    "kanser": "cancer",
    "leukemia": "leukemia",
    "breast cancer": "breast cancer",
    "lung cancer": "lung cancer",

    # === General Symptoms ===
    "lagnat": "fever",
    "fever": "fever",
    "sakit": "pain",
    "pain": "pain",
    "pamamaga": "inflammation",
    "impeksyon": "infection",
    "pagkapagod": "fatigue",
    "pagkahilo": "dizziness",
    "pagsusuka": "nausea",
    "pagkasuka": "vomiting",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """Load TxGNN disease vocabulary."""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """Build disease name index (keyword -> (disease_id, disease_name))."""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # Full name
        index[name_upper] = (disease_id, disease_name)

        # Extract keywords (split by space and comma)
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:  # Only keep longer keywords
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """Extract individual indications from indication text.

    Note: PNF-EML does not include indication data, so this function
    is for potential future use with other data sources.
    """
    if not indication_str:
        return []

    # Normalize
    text = indication_str.strip()

    # Split by common separators
    parts = re.split(r"[.;]", text)

    indications = []
    for part in parts:
        # Further split by comma
        sub_parts = re.split(r"[,]", part)
        for sub in sub_parts:
            sub = sub.strip()
            if sub and len(sub) >= 2:
                indications.append(sub)

    return indications


def translate_indication(indication: str) -> List[str]:
    """Translate Filipino indication to English keywords."""
    keywords = []
    indication_lower = indication.lower()

    for local_term, en_term in DISEASE_DICT.items():
        if local_term in indication_lower:
            keywords.append(en_term.upper())

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """Map a single indication to TxGNN diseases.

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # Translate to English keywords
    keywords = translate_indication(indication)

    for kw in keywords:
        # Exact match
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # Partial match
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # Deduplicate and sort by confidence
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]  # Return at most 5 matches


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
    indication_field: str = "indication",
    license_field: str = "license_id",
    brand_field: str = "brand_name",
) -> pd.DataFrame:
    """Map drug indications to TxGNN diseases.

    Note: PNF-EML does not include indication data, so this will return
    an empty DataFrame for PNF data.
    """
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        indication_str = row.get(indication_field, "")
        if not indication_str:
            continue

        # Extract individual indications
        indications = extract_indications(str(indication_str))

        for ind in indications:
            # Translate and map
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "license_id": row.get(license_field, ""),
                        "brand_name": row.get(brand_field, ""),
                        "original_indication": str(indication_str)[:100],
                        "extracted_indication": ind,
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "license_id": row.get(license_field, ""),
                    "brand_name": row.get(brand_field, ""),
                    "original_indication": str(indication_str)[:100],
                    "extracted_indication": ind,
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """Calculate indication mapping statistics."""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
