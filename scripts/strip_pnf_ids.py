"""把 data/ 中間檔裡程式自編的 PNF-xxxx 號碼換成 PNF 品項名稱（2026-11-06，用戶決定；全程不用 AI、不改其他內容）。

舊的 scripts/process_fda_data.py 替手抄的 PNF 品名清單（PNF_DRUGS）逐筆編了「PNF-0001」…「PNF-0529」號碼（PNF 本身沒有這種號碼），
這些號碼一路被抄進 data/raw/ph_fda_drugs.json、data/processed 的對照與預測 CSV、data/collected/tfda、data/evidence_packs、
data/notes、data/txgnn_cache 的舊證據包備份。process_fda_data.py 已改成 license_id＝品名（與 rebuild_licenses_by_ingredient.py
重建後的證據包相同），本支把既有中間檔裡的號碼換回它代表的品名：PNF-NNNN＝PNF_DRUGS[NNNN-1]（號碼就是清單序號，對照是一對一）。
- CSV（含 .csv.gz、.csv.bak_*）：逐格比對（品名可能含逗號，例「Albumin, Human」，用 csv 模組讀寫）。
- 其他文字檔（JSON、Markdown、txt、log、tsv）：直接把號碼換成品名（品名沒有引號、反斜線，JSON 不需跳脫）。
- PDF 等二進位檔不動（檔名的「PNF-EML」「PNF-8th」不是號碼）。
跑完再掃一次，還有號碼就 exit 1（scripts/license_rebuild_run.py 據以停損，不發 Release）。
用法（repo 根目錄）：python3 scripts/strip_pnf_ids.py [--dry-run] [--check]
"""
import csv
import gzip
import importlib.util
import io
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
PNF_ID = re.compile(r"\bPNF-(\d{4})\b")
TEXT_SUFFIX = {".json", ".md", ".txt", ".log", ".tsv", ".yaml", ".yml"}


def pnf_names():
    sp = importlib.util.spec_from_file_location("pfd", ROOT / "scripts/process_fda_data.py")
    m = importlib.util.module_from_spec(sp)
    sp.loader.exec_module(m)
    return list(m.PNF_DRUGS)


def is_csv(p):
    return ".csv" in p.name


def read_bytes(p):
    b = p.read_bytes()
    return gzip.decompress(b) if p.name.endswith(".gz") else b


def write_bytes(p, b):
    p.write_bytes(gzip.compress(b, mtime=0) if p.name.endswith(".gz") else b)


def sub(s, names):
    def f(m):
        i = int(m.group(1))
        if not 1 <= i <= len(names):
            raise ValueError(f"PNF-{m.group(1)} 超出清單範圍（{len(names)} 筆）")
        return names[i - 1]
    return PNF_ID.sub(f, s)


def fix_csv(text, names):
    nl = "\r\n" if "\r\n" in text[:5000] else "\n"
    rows = list(csv.reader(io.StringIO(text, newline="")))
    out = io.StringIO(newline="")
    w = csv.writer(out, lineterminator=nl)
    for r in rows:
        w.writerow([sub(c, names) if "PNF-" in c else c for c in r])
    return out.getvalue()


def targets():
    for p in sorted(DATA.rglob("*")):
        if not p.is_file() or p.is_symlink():
            continue
        if is_csv(p) or p.suffix in TEXT_SUFFIX:
            yield p


def main(argv):
    dry, check_only = "--dry-run" in argv, "--check" in argv
    names = pnf_names()
    files, hits = 0, 0
    for p in targets():
        b = read_bytes(p)
        try:
            t = b.decode("utf-8-sig" if b.startswith(b"\xef\xbb\xbf") else "utf-8")
        except UnicodeDecodeError:
            continue
        n = len(PNF_ID.findall(t))
        if not n:
            continue
        files += 1
        hits += n
        if check_only:
            print(f"  {p.relative_to(ROOT)}：{n}")
            continue
        new = fix_csv(t, names) if is_csv(p) else sub(t, names)
        if not dry:
            enc = new.encode("utf-8")
            write_bytes(p, (b"\xef\xbb\xbf" + enc) if b.startswith(b"\xef\xbb\xbf") else enc)
    if check_only:
        print(f"PNF-xxxx 號碼：{files} 檔、{hits} 處")
        return 1 if hits else 0
    print(f"PNF-xxxx 號碼換成品名：{files} 檔、{hits} 處" + ("（dry-run）" if dry else ""))
    if dry:
        return 0
    left = [p for p in targets() if PNF_ID.search(read_bytes(p).decode("utf-8", "ignore"))]
    if left:
        print("還有號碼：" + ", ".join(str(p.relative_to(ROOT)) for p in left[:20]))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
