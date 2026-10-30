"""PH（DOH 菲律賓國家處方集 PNF）來源監看：PH 站的本地資料是 PNF（PDF，數年改版一次），FDA Philippines 沒有可批次下載的註冊資料。
用戶 2026-10-30：改成固定抓、發現更新就開 issue。監看 DOH PNF 發布頁的下載檔清單。
（由 _watch_page.py 產生）
抓發布頁上所有 PDF／Excel／Word 下載連結當指紋，跟上次比對；有新增或移除就開 issue（排程 exit 6），頁面不自動改。
"""
import re
import time
from urllib.parse import urljoin

import requests

WATCH = True
PAGES = ['https://www.doh.gov.ph/philippine-national-formulary']
RAW_FILE = "raw/source_watch.json"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"}


def fetch():
    out = []
    for page in PAGES:
        for attempt in range(3):
            try:
                r = requests.get(page, timeout=120, headers=UA)
                r.raise_for_status()
                break
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(20 * (attempt + 1))
        links = sorted({urljoin(r.url, h) for h in re.findall(r'href="([^"]+\.(?:pdf|xlsx?|docx?|zip))"', r.text, re.I)})
        out.append({"page": page, "files": links})
    return out


def validate(new, old):
    return [f"{x['page']} 抓不到任何下載檔連結" for x in new if not x["files"]]


def describe(old, new):
    o = {f for x in old for f in x["files"]}
    n = {f for x in new for f in x["files"]}
    add, rm = sorted(n - o), sorted(o - n)
    return "新增：" + ("、".join(add[:20]) or "無") + "；移除：" + ("、".join(rm[:20]) or "無")


def status_index(new):
    return {}


def record_id(rec):
    return ""


def update(rec, new):
    return False
