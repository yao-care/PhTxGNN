"""依成分重建後，把藥物頁「## Philippines Market Information」段落的表換成程式產生的 PNF 品項表（2026-11-06，用戶核准；全程不用 AI）。

前置：scripts/rebuild_licenses_by_ingredient.py 已重建 data/bundles（PNF-EML 2022 品項，依成分，含複方）。
PH 站的本地資料是菲律賓國家處方集（PNF），不是 FDA Philippines 的藥品註冊：
- 段落裡的第一張表（原表頭「Authorization Number | Product Name | Dosage Form | Approved Indication」，第一欄是程式編的 PNF-xxxx，
  PNF 本身沒有這種號碼）換成「| PNF entry (active ingredient) | Routes in the PNF |」，表後註明來源是 PNF；最多列 20 筆。
- 正文裡剩下的號碼一併拿掉（號碼是程式編的；把號碼說成許可證／註冊的句子由 tools/txgnn/.claude/delete_license_sentences.py 先刪）：
  「(PNF-0018)」整個括號、下一步條目句尾的「for licence PNF-0071」「of PNF-0174」，以及「(PNF-0075, Carbamazepine, single-ingredient)」
  這類描述舊紀錄（號碼、無劑型、無適應症）的整句；拿掉後還留著號碼，scripts/license_rebuild_run.py 會停損。
- 概覽表裡另外手寫的「Number of Approvals」列（把 PNF 品項寫成許可／註冊張數；程式產生的是「Number of PNF Entries」列）整列拿掉。
- 概覽表有「Philippines Market Status」列、卻沒有「Number of PNF Entries」列的頁，在狀態列下面補一列（值＝PNF 品項數）。
- 新資料沒有任何品項時拿掉表，改一句「Not listed in the Philippine National Formulary (PNF) Essential Medicines List used for this report.」
- 段落裡沒有表的頁（舊頁只有文字、或矛盾句刪完只剩標題）：在標題下補程式產生的表與來源句（沒有品項時補「Not listed …」句，已有就不重複）；表以外的文字只動號碼括號（2026-11-06 第三輪）。
程式區塊標記（2026-11-12 起，本站查核機制，比照 UsTxGNN）：程式產生的表格（連同表下的 SHOW／SOURCE 句，或 NONE_LINE）前後各一行
「<!-- licenses:begin -->」「<!-- licenses:end -->」（前後空行），讓查核紀錄、刪句工具與 gate 分得出哪些字是程式寫的；
區塊內容由 block_for 決定（重排、補標記、快照共用）；--mark-existing 只替表頭＝HEAD 的現有程式表補標記、不改內容；
carry_block 給 sync_notes_to_docs.py 重寫整頁時移植舊頁的程式區塊；program_rows 給 scripts/build_license_snapshot.py。
gate（scripts/check_seo_docs.py）依 snapshots/ph_licenses.json.gz 檢查程式表（src/phtxgnn/regulatory/licenses.py）。
用法（repo 根目錄）：python3 scripts/sync_license_tables.py [--dry-run] [--mark-existing] [頁 ...]
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEC = "## Philippines Market Information"
HEAD = ["| PNF entry (active ingredient) | Routes in the PNF |", "|------|------|"]
NONE_LINE = "Not listed in the Philippine National Formulary (PNF) Essential Medicines List used for this report."
SOURCE = ("Source: Philippine National Formulary (PNF) Essential Medicines List, 8th Edition (as of 2 November 2022). "
          "PNF entries are formulary listings, not FDA Philippines registrations; FDA Philippines registration status is not included in this data.")
SHOW = "Showing {n} of {m} PNF entries."
SHOW_RX = re.compile(r"^Showing \d+ of \d+ PNF entries\.( .*)?$")
PART_NOTE = "Only part of the licence list is held in the data; the list may be incomplete."
MAX_ROWS = 20
BEGIN = "<!-- licenses:begin -->"
END = "<!-- licenses:end -->"
ID_PAREN = re.compile(r"\s*\((?:(?:licen[cs]e|registration|authori[sz]ation)\s+(?:no\.?|number)\s*)?PNF-\d{4}\)", re.I)
# 下一步條目句尾的號碼：「… for licence PNF-0071」「… for the Philippines registration PNF-0258」「… of PNF-0174」「… for PNF-0187」
ID_TAIL = re.compile(r"\s+(?:for|of)\s+(?:the\s+)?(?:(?:Philippines?|Philippine|local)\s+)?(?:(?:licen[cs]e|registration|authori[sz]ation)\s+)?PNF-\d{4}(?=[.,;]|$)", re.I)
# 描述舊紀錄的整句（號碼＋品名／單方／無劑型無適應症）
ID_SENT = re.compile(r"[^.\n]*\bPNF-\d{4}\b[^.\n]*\.(?:\s+(?:It has no|It carries no|The data compiled for this report carry no|No dosage form|Its dosage form|Dosage form)[^.\n]*\.)?")
APPROVALS_ROW = re.compile(r"^\| Number of approvals \|.*\|\s*$", re.I)


def cell(x, n=120):
    t = re.sub(r"\s+", " ", str(x or "").replace("|", "/")).strip()
    return t if len(t) <= n else t[:n - 1].rstrip() + "…"


def table_rows(recs):
    seen, rows = set(), []
    for r in recs:
        k = r.get("license_id")
        if not k or k in seen:
            continue
        seen.add(k)
        rows.append(f"| {cell(k)} | {cell(r.get('dosage_form') or 'Not stated', 60)} |")
    return rows


STATUS_LABEL, COUNT_LABEL = "| Philippines Market Status |", "| Number of PNF Entries |"


def ensure_count_row(lines, recs, partial):
    if any(l.startswith(COUNT_LABEL) for l in lines):
        return lines
    for i, l in enumerate(lines):
        if l.startswith(STATUS_LABEL):
            n = len({r.get("license_id") for r in recs if r.get("license_id")})
            return lines[:i + 1] + [f"{COUNT_LABEL} {('at least ' if partial else '')}{n} |"] + lines[i + 1:]
    return lines


def strip_ids(lines, log):
    out = []
    for l in lines:
        if APPROVALS_ROW.match(l):
            log.append(("PNF張數列", l, ""))
            continue
        n = ID_TAIL.sub("", ID_PAREN.sub("", l))
        if re.search(r"PNF-\d{4}", n) and not l.startswith("|"):
            n = re.sub(r"\s{2,}", " ", ID_SENT.sub("", n)).strip()
        if n != l:
            log.append(("PNF號碼", l, n))
            if not n.strip(" -*"):
                continue
        out.append(n)
    return out


def block_for(recs):
    """程式區塊的內容（不含標記）：表＋表下的 SHOW／SOURCE 句；沒有任何品項時是 NONE_LINE 一句"""
    rows = table_rows(recs)
    if not rows:
        return [NONE_LINE]
    return HEAD + rows[:MAX_ROWS] + [""] + ([SHOW.format(n=MAX_ROWS, m=len(rows)) + " " + SOURCE] if len(rows) > MAX_ROWS else [SOURCE])


def strip_marks(lines):
    return [l for l in lines if l.strip() not in (BEGIN, END)]


def wrap(block):
    return [BEGIN, ""] + block + ["", END]


def program_rows(tf, fc=None):
    """快照用：(程式表的列, 表下的程式文字)；沒有任何品項時 ([], None)"""
    blk = block_for(tf.get("records") or [])
    if blk == [NONE_LINE]:
        return [], None
    return [l for l in blk[2:] if l.startswith("|")], [l for l in blk if l.strip() and not l.startswith("|")]


def _bounds(lines):
    a = lines.index(SEC) + 1
    return a, next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))


def _is_prog_text(l):
    s = l.strip()
    return bool(SHOW_RX.match(s)) or s == SOURCE


def mark_existing(lines):
    """表頭＝HEAD 的現有程式表（連同緊接的 SHOW／SOURCE 句）或 NONE_LINE 補上標記，內容一字不改"""
    if BEGIN in lines or SEC not in lines:
        return lines
    a, b = _bounds(lines)
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        if NONE_LINE in lines[a:b]:
            k = lines.index(NONE_LINE, a)
            return lines[:k] + wrap([NONE_LINE]) + lines[k + 1:]
        return lines
    x = y = tb[0]
    if lines[x].strip() != HEAD[0]:
        return lines
    while y + 1 < b and lines[y + 1].startswith("|"):
        y += 1
    blk, k = lines[x:y + 1], y + 1
    while k < b and not lines[k].strip():
        k += 1
    if k < b and _is_prog_text(lines[k]):
        blk, y = blk + ["", lines[k]], k
    return lines[:x] + wrap(blk) + lines[y + 1:]


def carry_block(old_text, new_text):
    """sync_notes_to_docs.py 重寫整頁時用：舊頁的程式區塊移植到新頁的市場段落，取代新頁模型寫的第一張表（連同表下程式文字）；
    新頁段落沒有表時接在標題下。舊頁沒有程式區塊就原樣回傳新頁。"""
    old = old_text.replace("\r\n", "\n").split("\n")
    if BEGIN not in old or END not in old:
        return new_text
    blk = old[old.index(BEGIN):old.index(END) + 1]
    lines = strip_marks(new_text.split("\n"))
    if SEC not in lines:
        return new_text
    a, b = _bounds(lines)
    tb = [k for k in range(a, b) if lines[k].startswith("|")]
    if not tb:
        out = lines[:a] + [""] + blk + [""] + lines[a:]
    else:
        x = y = tb[0]
        while y + 1 < b and lines[y + 1].startswith("|"):
            y += 1
        rest = [l for l in lines[y + 1:b] if not _is_prog_text(l)]
        out = lines[:x] + blk + rest + lines[b:]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(out))


def process(text, recs, partial=False, log=None):
    log = [] if log is None else log
    lines = strip_ids(ensure_count_row(strip_marks(text.split("\n")), recs, partial), log)
    if SEC in lines:
        a = lines.index(SEC) + 1
        b = next((k for k in range(a, len(lines)) if lines[k].startswith("## ")), len(lines))
        tb = [k for k in range(a, b) if lines[k].startswith("|")]
        if not tb:
            rows = table_rows(recs)
            if rows or not any(l.strip() == NONE_LINE for l in lines[a:b]):
                lines = lines[:a] + [""] + wrap(block_for(recs)) + [""] + lines[a:]
            elif NONE_LINE in lines[a:b]:  # 已有 NONE_LINE：補標記（不重複加句）
                k = lines.index(NONE_LINE, a)
                lines = lines[:k] + wrap([NONE_LINE]) + lines[k + 1:]
        else:
            x, y = tb[0], tb[0]
            while y + 1 < b and lines[y + 1].startswith("|"):
                y += 1
            rest = [l for l in lines[y + 1:b] if not SHOW_RX.match(l.strip()) and l.strip() != SOURCE and (partial or l.strip() != PART_NOTE)]
            lines = lines[:x] + wrap(block_for(recs)) + [""] + rest + lines[b:]
            if lines[x - 1].strip():
                lines.insert(x, "")
    t2 = re.sub(r"\n{3,}", "\n\n", "\n".join(lines))
    return t2 if t2 != text else None


def run(only=None, dry=False, log_path=None):
    """only：要處理的頁名集合（None＝全部）；回傳改到的頁名。log_path：號碼／張數列的刪改附加到刪句清單（tsv）"""
    changed, rows = [], []
    for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
        if only and page.stem not in only:
            continue
        bf = ROOT / "data/bundles" / page.stem / "drug_bundle.json"
        if not bf.exists():
            bf = ROOT / "data/bundles" / page.stem.replace("-", "_") / "drug_bundle.json"
        if not bf.exists():
            continue
        raw = page.read_bytes().decode("utf-8")
        if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
            continue
        crlf = "\r\n" in raw[:500]
        reg = json.loads(bf.read_text(encoding="utf-8")).get("tfda") or {}
        recs = reg.get("records") or []
        lg = []
        new = process(raw.replace("\r\n", "\n"), recs, int(reg.get("total_matches") or 0) > len(recs), lg)
        rows += [f"{page.stem}\t{r}\t{o}\t{'拿掉程式編的 PNF-xxxx 號碼（PNF 沒有這種號碼）' + ('；留下：' + n if n else '；整句是描述舊紀錄') if r == 'PNF號碼' else '手寫的許可張數列；程式產生的是 Number of PNF Entries 列'}" for r, o, n in lg]
        if new is None:
            continue
        changed.append(page.stem)
        if not dry:
            page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
    if log_path and rows and not dry:
        with open(log_path, "a", encoding="utf-8") as f:
            f.write("\n".join(rows) + "\n")
    return changed


def main(argv):
    if "--mark-existing" in argv:
        n = 0
        for page in sorted((ROOT / "docs/_drugs").glob("*.md")):
            raw = page.read_bytes().decode("utf-8")
            if "layout: id_redirect" in raw[:3000] or 'http-equiv="refresh"' in raw[:3000]:
                continue
            crlf = "\r\n" in raw[:500]
            t = raw.replace("\r\n", "\n")
            new = re.sub(r"\n{3,}", "\n\n", "\n".join(mark_existing(t.split("\n"))))
            if BEGIN in new and BEGIN not in t:  # 只寫入真的補了標記的頁
                n += 1
                if "--dry-run" not in argv:
                    page.write_bytes((new.replace("\n", "\r\n") if crlf else new).encode("utf-8"))
        print(f"程式區塊標記：補上 {n} 頁")
        return
    lp = argv[argv.index("--log") + 1] if "--log" in argv else None
    only = {a for a in argv if not a.startswith("--") and a != lp}
    print(f"許可證表改 {len(run(only or None, '--dry-run' in argv, lp))} 頁")


if __name__ == "__main__":
    main(sys.argv[1:])
