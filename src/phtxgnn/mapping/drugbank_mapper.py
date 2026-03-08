"""DrugBank 映射模組"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd

from .normalizer import extract_ingredients, get_all_synonyms


def load_drugbank_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 DrugBank 詞彙表

    Args:
        filepath: CSV 檔案路徑，預設為 data/external/drugbank_vocab.csv

    Returns:
        DrugBank 詞彙表 DataFrame
    """
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "drugbank_vocab.csv"

    return pd.read_csv(filepath)


def build_name_index(drugbank_df: pd.DataFrame) -> Dict[str, str]:
    """建立名稱索引（名稱 -> DrugBank ID）

    Args:
        drugbank_df: DrugBank 詞彙表

    Returns:
        名稱到 ID 的對照字典
    """
    index = {}

    for _, row in drugbank_df.iterrows():
        name_upper = row["drug_name_upper"]
        drugbank_id = row["drugbank_id"]

        # 完整名稱
        index[name_upper] = drugbank_id

        # 移除常見鹽類後綴，建立別名
        # 例如 "METFORMIN HCL" -> "METFORMIN"
        salt_suffixes = [
            " HCL", " HYDROCHLORIDE", " SODIUM", " POTASSIUM",
            " SULFATE", " SULPHATE", " MALEATE", " ACETATE",
            " CITRATE", " PHOSPHATE", " BROMIDE", " CHLORIDE",
            " TARTRATE", " FUMARATE", " SUCCINATE", " MESYLATE",
            " BESYLATE", " CALCIUM", " MAGNESIUM", " NITRATE",
            " LACTATE", " GLUCONATE", " DISODIUM", " MONOHYDRATE",
            " DIHYDRATE", " TRIHYDRATE", " ANHYDROUS",
            " DIPROPIONATE", " PROPIONATE", " ACETONIDE",
            " VALERATE", " BUTYRATE", " HEXAHYDRATE",
        ]

        for suffix in salt_suffixes:
            if name_upper.endswith(suffix):
                base_name = name_upper[:-len(suffix)].strip()
                if base_name and base_name not in index:
                    index[base_name] = drugbank_id

    # 添加常見同義詞對照
    # 格式：{FDA 成分名稱: DrugBank 名稱}
    synonym_map = {
        # ===== 維生素（通用名 -> DrugBank 化學名）=====
        "NIACINAMIDE": "NICOTINAMIDE",
        "NICOTINIC ACID": "NIACIN",
        # 維生素 B1 (DrugBank: THIAMINE)
        "VITAMIN B1": "THIAMINE",
        "THIAMINE HCL": "THIAMINE",
        "THIAMINE MONONITRATE": "THIAMINE",
        "THIAMINE DISULFIDE": "THIAMINE",
        # 維生素 B2 (DrugBank: RIBOFLAVIN)
        "VITAMIN B2": "RIBOFLAVIN",
        # 維生素 B6 (DrugBank: PYRIDOXINE)
        "VITAMIN B6": "PYRIDOXINE",
        "PYRIDOXINE HCL": "PYRIDOXINE",
        # 維生素 B12 (DrugBank: CYANOCOBALAMIN)
        "VITAMIN B12": "CYANOCOBALAMIN",
        # 維生素 C (DrugBank: ASCORBIC ACID)
        "VITAMIN C": "ASCORBIC ACID",
        # 維生素 E (DrugBank: TOCOPHEROL, ALPHA-TOCOPHEROL ACETATE)
        "VITAMIN E": "TOCOPHEROL",
        "TOCOPHEROL ACETATE": "ALPHA-TOCOPHEROL ACETATE",
        "TOCOPHEROL ACETATE ALPHA DL-": "ALPHA-TOCOPHEROL ACETATE",
        "DL-ALPHA-TOCOPHEROL ACETATE": "ALPHA-TOCOPHEROL ACETATE",
        "ALPHA-TOCOPHEROL": "TOCOPHEROL",
        # 維生素 A (DrugBank: RETINOL)
        "VITAMIN A": "RETINOL",
        "RETINOL PALMITATE": "RETINOL",
        "VITAMIN A PALMITATE": "RETINOL",
        "RETINOIC ACID": "TRETINOIN",
        # 維生素 D
        "VITAMIN D3": "CHOLECALCIFEROL",
        "VITAMIN D2": "ERGOCALCIFEROL",
        # 維生素 K
        "VITAMIN K1": "PHYTONADIONE",
        # 泛酸/維生素 B5 相關
        "PANTOTHENATE CALCIUM": "PANTOTHENIC ACID",
        "CALCIUM PANTOTHENATE": "PANTOTHENIC ACID",
        "CALCIUM PANTOTHENATE TYPE S": "PANTOTHENIC ACID",
        "SODIUM PANTOTHENATE": "PANTOTHENIC ACID",
        "PANTHENOL": "DEXPANTHENOL",
        "PANTHENOL D-": "DEXPANTHENOL",
        "D-PANTHENOL": "DEXPANTHENOL",
        # ===== 常見藥物別名 =====
        "ASPIRIN": "ACETYLSALICYLIC ACID",
        "PARACETAMOL": "ACETAMINOPHEN",
        "ADRENALINE": "EPINEPHRINE",
        "L-ADRENALINE": "EPINEPHRINE",
        "NORADRENALINE": "NOREPINEPHRINE",
        "LIGNOCAINE": "LIDOCAINE",
        "FRUSEMIDE": "FUROSEMIDE",
        "SALBUTAMOL": "ALBUTEROL",
        "GUAIACOL GLYCERYL ETHER": "GUAIFENESIN",
        "GUAIACOL GLYCOLATE": "GUAIFENESIN",
        "GLYCERYL GUAIACOLATE": "GUAIFENESIN",
        "SIMETHICONE": "DIMETHICONE",
        "SIMETICONE": "DIMETHICONE",
        "DL-CHLORPHENIRAMINE MALEATE": "CHLORPHENIRAMINE",
        "CHLORPHENIRAMINE MALEATE": "CHLORPHENIRAMINE",
        "NEOSTIGMINE METHYLSULFATE": "NEOSTIGMINE",
        "ALUMINUM HYDROXIDE DRIED GEL": "ALUMINUM HYDROXIDE",
        "ALUMINIUM HYDROXIDE": "ALUMINUM HYDROXIDE",
        "OXETHAZAINE": "OXETACAINE",
        # ===== 葡萄糖/右旋糖 =====
        "DEXTROSE": "D-GLUCOSE",
        "DEXTROSE MONOHYDRATE": "D-GLUCOSE",
        "DEXTROSE ANHYDROUS": "D-GLUCOSE",
        "DEXTROSE HYDROUS": "D-GLUCOSE",
        "GLUCOSE": "D-GLUCOSE",
        "GLUCOSE MONOHYDRATE": "D-GLUCOSE",
        "GLUCOSE ANHYDROUS": "D-GLUCOSE",
        # ===== L-/D-/DL- 前綴處理 =====
        "L-MENTHOL": "LEVOMENTHOL",
        "MENTHOL": "LEVOMENTHOL",
        "DL-MENTHOL": "RACEMENTHOL",
        "METHIONINE DL-": "METHIONINE",
        "DL-METHIONINE": "METHIONINE",
        "L-METHIONINE": "METHIONINE",
        "LYSINE L- HCL": "LYSINE",
        "L-LYSINE HCL": "LYSINE",
        "L-LYSINE": "LYSINE",
        "ASPARTATE POTASSIUM L-": "ASPARTIC ACID",
        "L-ASPARTATE": "ASPARTIC ACID",
        # ===== 水合物/無水形式 =====
        "CAFFEINE ANHYDROUS": "CAFFEINE",
        "ATORVASTATIN CALCIUM TRIHYDRATE": "ATORVASTATIN",
        "MOSAPRIDE CITRATE DIHYDRATE": "MOSAPRIDE",
        "FORMOTEROL FUMARATE DIHYDRATE": "FORMOTEROL",
        "IRINOTECAN HYDROCHLORIDE TRIHYDRATE": "IRINOTECAN",
        "NILOTINIB HYDROCHLORIDE MONOHYDRATE": "NILOTINIB",
        "SITAGLIPTIN PHOSPHATE MONOHYDRATE": "SITAGLIPTIN",
        "ATROPINE SULFATE MONOHYDRATE": "ATROPINE",
        "ZIPRASIDONE HYDROCHLORIDE MONOHYDRATE": "ZIPRASIDONE",
        "LIDOCAINE HYDROCHLORIDE MONOHYDRATE": "LIDOCAINE",
        "LIDOCAINE HCL MONOHYDRATE": "LIDOCAINE",
        "NALOXONE HCL DIHYDRATE": "NALOXONE",
        "CIPROFLOXACIN HYDROCHLORIDE MONOHYDRATE": "CIPROFLOXACIN",
        "PANTOPRAZOLE SODIUM SESQUIHYDRATE": "PANTOPRAZOLE",
        # ===== 微粒化形式 =====
        "FLUTICASONE PROPIONATE MICRONIZED": "FLUTICASONE",
        "BUDESONIDE MICRONIZED": "BUDESONIDE",
        "FENOFIBRATE MICRONIZED": "FENOFIBRATE",
        "ACETAMINOPHEN MICRONIZED": "ACETAMINOPHEN",
        "PROGESTERONE MICRONIZED": "PROGESTERONE",
        "OLANZAPINE MICRONIZED": "OLANZAPINE",
        # ===== 其他常見變體 =====
        "ACETIC ACID GLACIAL": "ACETIC ACID",
        "ESTRADIOL ETHINYL": "ETHINYL ESTRADIOL",
        "ETHINYLESTRADIOL": "ETHINYL ESTRADIOL",
        "VALPROATE SODIUM": "VALPROIC ACID",
        "SODIUM VALPROATE": "VALPROIC ACID",
        "OLMESARTAN MEDOXOMIL": "OLMESARTAN",
        "METAPROTERENOL SULFATE": "ORCIPRENALINE",
        "METAPROTERENOL": "ORCIPRENALINE",
        "IODOCHLORHYDROXYQUIN": "CLIOQUINOL",
        "UNDECYLENATE ZINC": "UNDECYLENIC ACID",
        "DEXAMETHASONE SODIUM PHOSPHATE": "DEXAMETHASONE",
        "BETAMETHASONE SODIUM PHOSPHATE": "BETAMETHASONE",
        "GLYCYRRHIZINIC ACID": "GLYCYRRHIZIC ACID",
        "GLYCYRRHIZINATE DIPOTASSIUM": "GLYCYRRHIZIC ACID",
        # ===== 抗生素 =====
        "AMOXYCILLIN": "AMOXICILLIN",
        "CEPHRADINE": "CEFRADINE",
        "RIFAMPIN": "RIFAMPICIN",
        "CLAVULANATE POTASSIUM": "CLAVULANIC ACID",
        # ===== 心血管藥物 =====
        "AMLODIPINE BESILATE": "AMLODIPINE",
        "CLOPIDOGREL HYDROGEN SULFATE": "CLOPIDOGREL",
        "BETAHISTINE DIHYDROCHLORIDE": "BETAHISTINE",
        # ===== 抗組織胺 =====
        "CETIRIZINE DIHYDROCHLORIDE": "CETIRIZINE",
        "LEVOCETIRIZINE DIHYDROCHLORIDE": "LEVOCETIRIZINE",
        # ===== 止痛/抗發炎 =====
        "KETOROLAC TROMETHAMINE": "KETOROLAC",
        "DICLOFENAC DIETHYLAMINE": "DICLOFENAC",
        # ===== 局部麻醉劑 =====
        "DIBUCAINE": "CINCHOCAINE",
        "DIBUCAINE HCL": "CINCHOCAINE",
        # ===== 呼吸系統 =====
        "CARBOCYSTEINE": "CARBOCISTEINE",
        "DIPROPHYLLINE": "DYPHYLLINE",
        # ===== 免疫抑制劑 =====
        "CYCLOSPORIN": "CYCLOSPORINE",
        "CICLOSPORIN": "CYCLOSPORINE",
        # ===== 精神科藥物 =====
        "ESCITALOPRAM OXALATE": "ESCITALOPRAM",
        "RIVASTIGMINE HYDROGEN TARTRATE": "RIVASTIGMINE",
        # ===== 消化系統 =====
        "SODIUM RABEPRAZOLE": "RABEPRAZOLE",
        # ===== 抗癲癇/情緒穩定劑 =====
        "DIVALPROEX SODIUM": "VALPROIC ACID",
        # ===== 類固醇 =====
        "CLOBETASOL-17-PROPIONATE": "CLOBETASOL PROPIONATE",
        # ===== 胺基酸/營養補充 =====
        "ARGININE HCL L-": "ARGININE",
        "L- GLUTAMIC ACID": "GLUTAMIC ACID",
        "LYSINE L-": "L-LYSINE",
        "CHOLINE BITARTRATE": "CHOLINE",
        # ===== 通用映射 =====
        "ALCOHOL 95%": "ETHANOL",
        "ALCOHOL": "ETHANOL",
        "DIHYDROERGOTOXINE METHANESULFONATE": "ERGOLOID MESYLATE",
        "DIHYDROXYPROPYL THEOPHYLLINE": "DYPHYLLINE",
        "POTASSIUM PHOSPHATE MONOBASIC": "MONOPOTASSIUM PHOSPHATE",
        "GRAMICIDIN": "GRAMICIDIN D",
        "ALENDRONATE": "ALENDRONIC ACID",
        "CROMOLYN": "CROMOGLICIC ACID",
        "D-GLUCOSAMINE": "GLUCOSAMINE",
        "GENTAMYCIN": "GENTAMICIN",
        "L-CARNITINE": "LEVOCARNITINE",
        "L-CYSTEINE": "CYSTEINE",
        "L-HISTIDINE": "HISTIDINE",
        "PHYTOMENADIONE": "PHYLLOQUINONE",
        "PYRILAMINE": "MEPYRAMINE",
        "TETRAHYDROZOLINE": "TETRYZOLINE",
        "GLYCOPYRROLATE": "GLYCOPYRRONIUM",
        "HYOSCINE": "SCOPOLAMINE",
        "ISOPROTERENOL": "ISOPRENALINE",
        "BENZHEXOL": "TRIHEXYPHENIDYL",
        "BENOXINATE": "OXYBUPROCAINE",
        "CHLORMETHINE": "MECHLORETHAMINE",
        "DOTHIEPIN": "DOSULEPIN",
        "ETILEFRIN": "ETILEFRINE",
        "MEBHYDROLINE": "MEBHYDROLIN",
        "MECLIZINE": "MECLIZINE",
        "METHYLERGONOVINE": "METHYLERGOMETRINE",
        "PRAMOXINE": "PRAMOCAINE",
        "PROCHLORPERAZINE": "PROCHLORPERAZINE",
        "TORSEMIDE": "TORASEMIDE",
        "TRIMEPRAZINE": "ALIMEMAZINE",
        "URSODESOXYCHOLIC": "URSODEOXYCHOLIC ACID",
        "URSODIOL": "URSODEOXYCHOLIC ACID",
        "VALACICLOVIR": "VALACICLOVIR",
        "VALACYCLOVIR": "VALACICLOVIR",
        # ===== 常見化合物 =====
        "CALCIUM": "CALCIUM",
        "MAGNESIUM": "MAGNESIUM",
        "ZINC": "ZINC",
        "IRON": "IRON",
        "COPPER": "COPPER",
        "MANGANESE": "MANGANESE",
        "BIOTIN": "BIOTIN",
        "FOLIC ACID": "FOLIC ACID",
        "INOSITOL": "INOSITOL",
        "CHARCOAL": "ACTIVATED CHARCOAL",
        "CAMPHOR": "CAMPHOR",
        "KAOLIN": "KAOLIN",
        "LACTULOSE": "LACTULOSE",
        "MALTOSE": "MALTOSE",
        "NICOTINE": "NICOTINE",
        "QUININE": "QUININE",
        "WARFARIN": "WARFARIN",
        "IBUPROFEN": "IBUPROFEN",
        "METFORMIN": "METFORMIN",
        "ATROPINE": "ATROPINE",
        "EPINEPHRINE": "EPINEPHRINE",
        "THEOPHYLLINE": "THEOPHYLLINE",
        "CAFFEINE": "CAFFEINE",
        "CODEINE": "CODEINE",
        "MORPHINE": "MORPHINE",
        "ASPIRIN": "ACETYLSALICYLIC ACID",
    }

    for alias, canonical in synonym_map.items():
        if canonical in index and alias not in index:
            index[alias] = index[canonical]

    return index


def map_ingredient_to_drugbank(
    ingredient: str,
    name_index: Dict[str, str],
) -> Optional[str]:
    """將單一成分映射到 DrugBank ID

    映射策略（優先順序）：
    1. 完全匹配
    2. 移除鹽類後綴後匹配
    3. 使用基本名稱匹配

    Args:
        ingredient: 標準化後的成分名稱
        name_index: 名稱索引

    Returns:
        DrugBank ID，若無法映射則回傳 None
    """
    if not ingredient:
        return None

    ingredient = ingredient.upper().strip()

    # 1. 完全匹配
    if ingredient in name_index:
        return name_index[ingredient]

    # 2. 移除台灣 FDA 常見的鹽類後綴
    salt_patterns = [
        r"\s+HCL$", r"\s+HYDROCHLORIDE$", r"\s+SODIUM$",
        r"\s+POTASSIUM$", r"\s+SULFATE$", r"\s+MALEATE$",
        r"\s+ACETATE$", r"\s+CITRATE$", r"\s+PHOSPHATE$",
        r"\s+BROMIDE$", r"\s+CHLORIDE$", r"\s+TARTRATE$",
        r"\s+HBR$", r"\s+HYDROBROMIDE$", r"\s+FUMARATE$",
        r"\s+SUCCINATE$", r"\s+MESYLATE$", r"\s+BESYLATE$",
        r"\s+CALCIUM$", r"\s+MAGNESIUM$", r"\s+NITRATE$",
        r"\s+LACTATE$", r"\s+GLUCONATE$", r"\s+DISODIUM$",
        r"\s+ANHYDROUS$", r"\s+MONOHYDRATE$", r"\s+DIHYDRATE$",
        r"\s+TRIHYDRATE$", r"\s+HEXAHYDRATE$",
        r"\s+DIPROPIONATE$", r"\s+PROPIONATE$", r"\s+ACETONIDE$",
        r"\s+VALERATE$", r"\s+BUTYRATE$", r"\s+MONONITRATE$",
    ]

    base_ingredient = ingredient
    for pattern in salt_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient)

    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    # 2b. 移除 L-/D-/DL- 前綴
    prefix_patterns = [r"^L-", r"^D-", r"^DL-"]
    base_ingredient = ingredient
    for pattern in prefix_patterns:
        base_ingredient = re.sub(pattern, "", base_ingredient)

    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    # 3. 嘗試移除括號內容
    base_ingredient = re.sub(r"\s*\([^)]*\)", "", ingredient).strip()
    if base_ingredient != ingredient and base_ingredient in name_index:
        return name_index[base_ingredient]

    return None


def map_fda_drugs_to_drugbank(
    fda_df: pd.DataFrame,
    drugbank_df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """將台灣 FDA 藥品映射到 DrugBank

    Args:
        fda_df: 台灣 FDA 藥品 DataFrame
        drugbank_df: DrugBank 詞彙表（可選）

    Returns:
        包含映射結果的 DataFrame
    """
    if drugbank_df is None:
        drugbank_df = load_drugbank_vocab()

    # 建立索引
    name_index = build_name_index(drugbank_df)

    results = []

    for _, row in fda_df.iterrows():
        ingredient_str = row.get("主成分略述", "")
        if not ingredient_str:
            continue

        # 提取所有成分及同義詞
        synonyms_data = get_all_synonyms(ingredient_str)

        for main_name, synonyms in synonyms_data:
            # 先嘗試主名稱
            drugbank_id = map_ingredient_to_drugbank(main_name, name_index)

            # 若失敗，嘗試同義詞
            if drugbank_id is None:
                for syn in synonyms:
                    drugbank_id = map_ingredient_to_drugbank(syn, name_index)
                    if drugbank_id:
                        break

            results.append({
                "許可證字號": row["許可證字號"],
                "中文品名": row["中文品名"],
                "原始主成分": ingredient_str,
                "標準化成分": main_name,
                "同義詞": "; ".join(synonyms) if synonyms else "",
                "drugbank_id": drugbank_id,
                "映射成功": drugbank_id is not None,
            })

    return pd.DataFrame(results)


def get_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算映射統計

    Args:
        mapping_df: 映射結果 DataFrame

    Returns:
        統計字典
    """
    total = len(mapping_df)
    success = mapping_df["映射成功"].sum()
    unique_ingredients = mapping_df["標準化成分"].nunique()
    unique_drugbank = mapping_df[mapping_df["映射成功"]]["drugbank_id"].nunique()

    return {
        "total_ingredients": total,
        "mapped_ingredients": int(success),
        "mapping_rate": success / total if total > 0 else 0,
        "unique_ingredients": unique_ingredients,
        "unique_drugbank_ids": unique_drugbank,
    }
