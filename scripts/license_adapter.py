"""PH（菲律賓國家處方集 PNF）來源監看，給 license_refresh_20261029.py 用（2026-10-30）。

PH 站的本地資料是 PNF（衛生部藥劑處出版、數年改版、期間以公告追加品項），FDA Philippines 沒有可批次下載的註冊資料。
用戶 2026-10-30：改成固定抓、發現更新就開 issue。衛生部網站（doh.gov.ph）擋 GitHub runner（403），
改看 PhilHealth 公告頁（PNF 改版與追加品項都由 PhilHealth 公告轉發，例 PA2024-0026、PA2025-0013）：
抓今年與去年的公告清單，只取標題含 Formulary／PNF／Essential Medicines 的公告當指紋；有新增就開 issue，頁面不自動改。
"""
import re
import time
from urllib.parse import urljoin

import requests

WATCH = True
RAW_FILE = "raw/pnf_watch.json"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"}
KEY = re.compile(r"formulary|\bPNF\b|PNDF|essential medicine|medicines? list|drug list|list of (?:drugs|medicines)", re.I)  # 公告頁只列各年最新 10 則，新公告會在最上面


def fetch():
    y = int(time.strftime("%Y"))
    out = []
    for year in (y - 1, y):
        url = f"https://www.philhealth.gov.ph/advisories/{year}/"
        for attempt in range(3):
            try:
                r = requests.get(url, timeout=120, headers=UA)
                if r.status_code == 404:
                    break
                r.raise_for_status()
                for href, title in re.findall(r'<a href="([^"]+\.pdf)"[^>]*>([^<]+)</a>', r.text):
                    if KEY.search(title):
                        out.append({"pdf": urljoin(url, href), "title": " ".join(title.split())})
                break
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(20 * (attempt + 1))
    return sorted(out, key=lambda x: x["pdf"])


def validate(new, old):
    return []  # 這一年可能剛好沒有 PNF 公告，0 筆也正常


def describe(old, new):
    o = {x["pdf"] for x in old}
    add = [f"{x['title']}（{x['pdf']}）" for x in new if x["pdf"] not in o]
    return "PhilHealth 新的處方集相關公告：" + ("；".join(add[:10]) or "無（只有移除）")


def status_index(new):
    return {}


def record_id(rec):
    return ""


def update(rec, new):
    return False
