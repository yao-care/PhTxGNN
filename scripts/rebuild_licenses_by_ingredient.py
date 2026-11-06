"""PH 依成分重建證據包的「本地資料」紀錄（2026-11-06，用戶核准；全程不用 AI；做法比照 Za／Us／Sg／Eu／Uk／NZ）。

PH 站的本地資料是菲律賓國家處方集（Philippine National Formulary，PNF）基本藥物清單，不是 FDA Philippines 的藥品註冊；
這裡只依成分重建「列在 PNF 的品項」，頁面上一律寫成「列在 PNF」、不含 FDA Philippines 註冊狀態（check_drug_page.SOURCE_STATUS／NO_CENTRAL）。
舊資料（scripts/process_fda_data.py）是一份手抄的品名清單，每個品名配一個程式編的「PNF-0001」號碼；PNF 本身沒有這種號碼，
重建後不再用：紀錄的 license_id 就是 PNF 上的品項名稱（去掉腳註標記），頁面上不顯示號碼欄。

1. 來源：data/raw/PNF-EML_2022.pdf（衛生部藥劑處 PNF Essential Medicines List，8th Edition，as of 2 November 2022；
   在本站 data Release 裡，與 process_fda_data.py 用的同一版）。用 pdftotext -layout 轉文字，依版面解析「Active Ingredient」欄的品項：
   第 0 欄起頭、右欄有用法標記（Oral:、Inj.:、Inhalation: …）的行是新品項；品名換行（上一行以 + / , ( 或 and/of/for… 結尾、括號沒閉合、
   第 0 欄小寫或括號開頭、或沒有用法標記）接回品名；「X (see Y)」是參照，不是品項；FAQ 之後不收。
2. 比對：品名拿掉腳註（(1, 2)、(A1)、(B)）、「*Reserve Antimicrobial」、學名方括號，主名依「+」拆成成分；括號裡寫的複方成分
   （Co-Amoxiclav (amoxicillin + potassium clavulanate)）與別名（Ascorbic Acid (vitamin C)）也當成分鍵，「(as …)」是鹽類說明、不算。
   成分去掉鹽類／水合物字樣、英美名統一，與頁的 drug.inn 同樣處理，有效成分相同就收（含複方）。
3. 寫回證據包 tfda：records＝全部比對到的 PNF 品項（單方在前），total_matches＝品項數；原紀錄整批換掉。比對結果是空的、但原紀錄有
   品名 → 不改這個證據包、列進報告（疑似比對漏掉，要人看）。
用法（repo 根目錄）：python3 scripts/rebuild_licenses_by_ingredient.py [--dry-run] [--report out.tsv] [頁 ...]
"""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "data/bundles"
PDF = ROOT / "data/raw/PNF-EML_2022.pdf"
SOURCE = "Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022)"
# 查過 PNF-EML 2022 全文都沒有的成分（舊的手抄清單有，但 PNF 沒有這個品項）：比對落空時照實寫成不在 PNF
CONFIRMED_EMPTY = {"mometasone": "PNF-EML 2022 全文查無 mometasone", "sodium_acetate": "PNF-EML 2022 全文查無 sodium acetate（舊紀錄誤配 Sodium Chloride）"}
# PNF 把幾個成分寫在同一個品名裡、沒有用「+」分開的品項
ENTRY_COMPONENTS = {"Vitamin B1 B6 B12": ["thiamine", "pyridoxine", "cyanocobalamin"]}

SALT = (r"hydrochloride|dihydrochloride|hcl|hydrobromide|besilate|besylate|camsylate|maleate|mesilate|mesylate|tartrate|bitartrate|fumarate|"
        r"succinate|citrate|acetate|diacetate|propionate|dipropionate|valerate|butyrate|phosphate|sulfate|sulphate|nitrate|lactate|gluconate|"
        r"palmitate|sodium|disodium|potassium|calcium|magnesium|bromide|chloride|iodide|tosilate|tosylate|pamoate|embonate|stearate|"
        r"mandelate|xinafoate|furoate|hyclate|trometamol|tromethamol|tromethamine|meglumine|olamine|erbumine|benzathine|esilate|isethionate|"
        r"oxalate|dihydrogen|hydrogen|decanoate|enanthate|cipionate|undecanoate|pivalate|axetil|cilexetil|medoxomil|dimesylate|"
        r"butylbromide|hippurate|acetonide|hexacetonide|carbonate|monohydrate|dihydrate|trihydrate|heptahydrate|hemihydrate|anhydrous|hydrate|base|salt")
SALT_RX = re.compile(r"\b(" + SALT + r")\b")
CANON = [(r"\bparacetamol\b", "acetaminophen"), (r"\bciclosporin\b", "cyclosporine"), (r"\bfrusemide\b", "furosemide"),
         (r"\badrenaline\b", "epinephrine"), (r"\bnoradrenaline\b", "norepinephrine"), (r"\bsalbutamol\b", "albuterol"),
         (r"\bglibenclamide\b", "glyburide"), (r"\blignocaine\b", "lidocaine"), (r"\brifampin\b", "rifampicin"),
         (r"\bacetylsalicylic acid\b", "aspirin"), (r"\bcolecalciferol\b", "cholecalciferol"), (r"\baluminium\b", "aluminum"),
         (r"\bsimethicone\b", "simeticone"), (r"\bthyroxine\b", "levothyroxine"), (r"\bhyoscine\b", "scopolamine"),
         (r"\bphenobarbitone\b", "phenobarbital"), (r"\bglyceryl trinitrate\b", "nitroglycerin"), (r"\boestr", "estr"), (r"\bsulph", "sulf"),
         (r"\bcyclosporin\b", "cyclosporine"), (r"\bamoxycillin\b", "amoxicillin"), (r"\bcephalexin\b", "cefalexin"),
         (r"\baciclovir\b", "acyclovir"), (r"\bchlortalidone\b", "chlorthalidone"), (r"\bindometacin\b", "indomethacin"),
         (r"\bmeclozine\b", "meclizine"), (r"\bphytomenadione\b", "phylloquinone"), (r"\bphytonadione\b", "phylloquinone"),
         (r"\bhydroxycarbamide\b", "hydroxyurea"), (r"\bnicotinic acid\b", "niacin"), (r"\bpolyethylene glycol\b", "macrogol"),
         (r"\bdextrose\b", "glucose"), (r"\bchlorpheniramine\b", "chlorphenamine"), (r"\bethinyl estradiol\b", "ethinylestradiol"),
         # 2026-11-06 實測（PNF 的寫法）：拼字錯誤、維生素別名、異構寫法
         (r"\banastrazole\b", "anastrozole"), (r"\bfusidate\b", "fusidic acid"), (r"\bfusidic acid acid\b", "fusidic acid"),
         (r"\bisosorbide 5 mononitrate\b", "isosorbide mononitrate"), (r"\bhepatitis a inactivated vaccine\b", "hepatitis a vaccine"),
         (r"\bvitamin b1\b", "thiamine"), (r"\bvitamin b6\b", "pyridoxine"), (r"\bvitamin b12\b", "cyanocobalamin"),
         (r"\bvitamin c\b", "ascorbic acid"), (r"\bvitamin a\b", "retinol"), (r"\bvitamin d3\b", "cholecalciferol"),
         (r"\bvitamin k1\b", "phylloquinone"), (r"\bvalproate\b", "valproic acid")]


def norm(x):
    t = str(x or "").lower().replace("‐", "-")
    while re.search(r"\([^()]*\)|\[[^\[\]]*\]", t):
        t = re.sub(r"\([^()]*\)|\[[^\[\]]*\]", " ", t)
    t = " ".join(re.sub(r"[^a-z0-9]+", " ", t).split())
    for a, b in CANON:
        t = re.sub(a, b, t)
    return " ".join(t.split())


def base(t):
    t = re.sub(r"^(l|d|dl)\s+(?=[a-z]{3})", "", t)
    t = re.sub(r"\s+\d+[a-z]?$", "", t)  # Dextran 70、Interferon Alfa 2B
    return " ".join(SALT_RX.sub(" ", t).split()) or t


# ---- PNF 版面解析 ----
ROUTE=re.compile(r"^([A-Z][A-Za-z. /]{1,30}?):")
NOTROUTE={"Composition","Volume","Concentration","Protein","Carbohydrate","Calories","Electrolytes","Lipid"}
CONT_END=re.compile(r"([+/,(‐-]|\b(for|of|and|with|or|in))$", re.I)
def unbalanced(s): return s.count("(")>s.count(")")
def route_of(t):
    r=ROUTE.match(t)
    return r.group(1) if r and r.group(1) not in NOTROUTE and not r.group(1).startswith("Each") else None
def parse(txt):
    ents=[];cur=None;started=False;prev_name=False;xref=False
    for raw in open(txt,encoding="utf-8"):
        line=raw.rstrip("\n").replace("\f","")
        if re.match(r"^\s*Active Ingredient",line): started=True; prev_name=False; continue
        if not started: continue
        if re.match(r"^\s*FREQUENTLY ASKED QUESTIONS",line): break
        if not line.strip() or re.match(r"^\s*(Pharmaceutical Forms|Route of Administration)",line) or re.fullmatch(r"\s*\d+\s*",line):
            prev_name=False; continue
        if line.startswith(" "):
            t=line.strip()
            if cur: cur["text"].append(t); rt=route_of(t); rt and cur["routes"].append(rt)
            prev_name=False; continue
        m=re.match(r"^(\S.*?)(?:\s{2,}(.*))?$",line)
        left,right=m.group(1).strip(),(m.group(2) or "").strip()
        rt=route_of(right)
        if xref:  # 參照（X (see Y)）跨行的後半
            xref=unbalanced(left) if not left.count(")") else False
            if right and cur: cur["text"].append(right); rt and cur["routes"].append(rt)
            continue
        if "(see" in left:
            if cur and prev_name and not cur["text"] and not cur["routes"]:
                ents.remove(cur); cur=ents[-1] if ents else None  # 參照的前半行被當成品項
            xref=unbalanced(left)
            if right and cur: cur["text"].append(right); rt and cur["routes"].append(rt)
            prev_name=False; continue
        if left in ("OR", "or"):
            continue
        if cur and (left[0] in "(" or left[0].islower() or left.count(")") > left.count("(")):  # 跨頁的品名後半（「2)」「(Ringer's Lactate)」）
            cur["name"] += " " + left
            if right: cur["text"].append(right)
            if rt: cur["routes"].append(rt)
            prev_name = True
            continue
        nm=cur["name"].rstrip() if cur else ""
        joiner=cur is not None and prev_name and (bool(CONT_END.search(nm)) or unbalanced(nm))
        if rt:
            cont=joiner
        else:
            # 沒有用法標記的第 0 欄行接在品名行後面＝品名換行；上一行品名已經以「)」或「*Reserve Antimicrobial」收尾時是新品項（Hemodialysis Solution）
            cont=cur is not None and prev_name and not re.search(r"(\)|Antimicrobial)$", nm)
        if cont:
            cur["name"]+=" "+left
        else:
            cur={"name":left,"routes":[],"text":[]};ents.append(cur)
        if right: cur["text"].append(right)
        if rt: cur["routes"].append(rt)
        prev_name=True
    return ents


FOOT = re.compile(r"\s*\((?:\d|A\d|B)(?:\s*,\s*(?:\d|A\d|B))*(?:\)|$)")
RESERVE = re.compile(r"\s*\(?\s*(?:Inj\.\s*-\s*)?\*\s*Reserve Anti\w+\)?", re.I)
ROUTE_NAME = {"Inj.": "Injection", "Inj": "Injection", "MDI": "Inhalation (MDI)", "DPI": "Inhalation (DPI)"}


def clean_name(n):
    n = re.sub(r"\s*●\s*", " ", n)
    n = RESERVE.sub("", FOOT.sub("", n))
    return " ".join(n.split()).strip(" ,")


def keys_of(name):
    """回傳（成分鍵集合, 成分數）"""
    main = norm(name)
    comps = [base(x.strip()) for x in re.split(r"[+/]", re.sub(r"\([^()]*\)|\[[^\]]*\]", " ", name.replace("‐", "-")))]
    comps = list(dict.fromkeys(c for c in (base(norm(x)) for x in comps) if len(c) >= 3))
    if name in ENTRY_COMPONENTS:
        comps = ENTRY_COMPONENTS[name]
    keys = set(comps) | {re.sub(r"\s+(disoproxil|alafenamide)\b", "", c) for c in comps}  # Tenofovir disoproxil fumarate：頁是 tenofovir 時也收
    if len(comps) == 1 and not SALT_RX.sub(" ", norm(name)).strip():
        keys.add(norm(name).split()[0])  # 整個品名都是鹽類字（Magnesium Sulfate、Sodium Chloride）：頁是陽離子（magnesium）時也收
    for par in re.findall(r"\(([^()]*)\)", name):
        p = par.strip()
        if re.match(r"(?i)as |for |equivalent|types?\b|recombinant|to be used|see\b|\d", p):
            continue
        parts = re.split(r"\+", p) if "+" in p else re.split(r",|/", p)
        sub = [base(norm(x)) for x in parts]
        sub = [s for s in sub if len(s) >= 3]
        if "+" in p and len(sub) > 1:
            comps = sub
        keys |= set(sub)
    return keys, max(len(comps), 1), main


def load_pnf():
    if not PDF.exists():
        raise SystemExit(f"找不到 {PDF}（先還原 data Release）")
    txt = ROOT / "data/raw/PNF-EML_2022.txt"
    subprocess.run(["pdftotext", "-layout", str(PDF), str(txt)], check=True)
    ents = parse(txt)
    txt.unlink()
    if len(ents) < 550:
        raise SystemExit(f"PNF 只解析出 {len(ents)} 個品項，疑似版面改變")
    out = {}
    for e in ents:
        name = clean_name(e["name"])
        if not name:
            continue
        k, n, _ = keys_of(name)
        routes = list(dict.fromkeys(ROUTE_NAME.get(r, r) for r in e["routes"]))
        out.setdefault(name, {"keys": set(), "n": n, "routes": []})
        out[name]["keys"] |= k
        out[name]["routes"] = list(dict.fromkeys(out[name]["routes"] + routes))
    return out


def main(argv):
    dry = "--dry-run" in argv
    rep = argv[argv.index("--report") + 1] if "--report" in argv else None
    only = [a for a in argv if not a.startswith("--") and a != rep]
    pnf = load_pnf()
    by_key = {}
    for name, e in pnf.items():
        for k in e["keys"]:
            by_key.setdefault(k, set()).add(name)
    out, held, n_changed, n_found, n_empty = [], [], 0, 0, 0
    for f in sorted(BUNDLES.glob("*/drug_bundle.json")):
        page = f.parent.name
        if only and page not in only:
            continue
        b = json.loads(f.read_text(encoding="utf-8"))
        reg = b.get("tfda") or {}
        inn = (b.get("drug") or {}).get("inn") or page.replace("_", " ")
        key = base(norm(inn))
        hit = set(by_key.get(key, set())) if len(key) >= 3 else set()
        old = sorted({str(x.get("brand_name_en") or x.get("license_id") or "").strip() for x in reg.get("records") or []} - {""})
        if not hit and old and page not in CONFIRMED_EMPTY:
            held.append(page)
            out.append(f"{page}\t{key}\t{reg.get('total_matches')}\t{len(old)}\t-\tHELD\t{';'.join(old[:10])}\t")
            continue
        recs = []
        for name in sorted(hit, key=lambda k: (pnf[k]["n"] > 1, k.lower())):
            recs.append({"license_id": name, "brand_name_zh": name, "brand_name_en": name, "ingredients": name, "indication": "",
                         "dosage_form": ", ".join(pnf[name]["routes"]), "manufacturer": "", "license_holder": "", "approval_date": "",
                         "expiry_date": "", "status": "", "kind": "single" if pnf[name]["n"] == 1 else "combo",
                         "source": SOURCE + " (formulary list; not FDA Philippines registrations)"})
        new = dict(reg, found=bool(recs), records=recs, total_matches=len(recs),
                   rebuilt="2026-11-06 by ingredient (Philippine National Formulary, PNF-EML 2022)")
        new_ids = [x["license_id"] for x in recs]
        out.append(f"{page}\t{key}\t{reg.get('total_matches')}\t{len(old)}\t{len(new_ids)}\t-\t{';'.join(old[:10])}\t{';'.join(new_ids[:10])}")
        n_found += bool(recs)
        n_empty += not recs
        if new != reg:
            n_changed += 1
            b["tfda"] = new
            if not dry:
                f.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding="utf-8")
    if rep:
        Path(rep).write_text("page\tmatch\told_total_matches\told_records\tnew_records\t-\told_names\tnew_entries\n" + "\n".join(out) + "\n",
                             encoding="utf-8")
    print(f"PNF {len(pnf)} 個品項；改 {n_changed} 個證據包（有紀錄 {n_found}、查無 {n_empty}、比對落空但原紀錄有品名而保留 {len(held)}）")
    if held:
        print("保留（要人看）：" + ", ".join(held[:60]))


if __name__ == "__main__":
    main(sys.argv[1:])
