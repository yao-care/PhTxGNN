"""正文 PNF 品項張數的程式改寫（2026-11-24 建，用戶決定「正文張數自動改寫」；做法移植 KrTxGNN／MyTxGNN，英文句型照 InTxGNN 同名檔改成本站口徑）。

正文裡「one single-ingredient record」「N PNF entries」「N registrations」「All N licences are valid」這類張數敘述，
由程式依許可證快照（snapshots/ph_licenses.json.gz 的 facts）改寫，資料更新後跟著改，不逐筆寫查核紀錄
（同 Kr／My／Tw：程式改寫的張數敘述是程式產生的正文）。

本站的「許可證」是菲律賓國家處方集（PNF）Essential Medicines List 的品項（一個成分或複方一筆，記給藥途徑），
不是 FDA Philippines 註冊；PNF 本身沒有有效／註銷狀態，事實層 total＝品項數、valid＝total、cancelled＝0（只講筆數）；
single_total／valid_single＝單一成分品項（證據包 kind＝single）。PNF 沒有品項號碼，舊頁上程式自編的 PNF-xxxx 由
scripts/sync_license_tables.py 拿掉、查核框遮成「PNF-xxxx」（scripts/apply_drug_reviews.py 的 PNF_ID），這支不碰號碼。

只改「句型明確、數字確定是本藥 PNF 品項張數」的地方，其餘一律不動：
  - 句子要有許可字樣（licence／license、authorization、registration、listing、PNF、formulary；
    products／records／entries 要同句有 Philippine／PNF／formulary／local data／single-ingredient／for this drug 等本地資料字樣），
    且沒有試驗、文獻、病人、劑量、年份、適應症、交互作用等字樣（NOT_LICENSE）。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、front matter、「Conclusion／Next Steps」段的待辦條目；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）。
  - 整句不動（skipped）：有保留（at least、partial、may、about…）、講證據包或查詢（found、returned、identified…）、相對數
    （other、further、remaining、also、including…）、劑型、複方、品牌名子集、其他國家、過去式；講表格顯示筆數（display）；
    事實層 partial 或總數 0 的頁整頁不動。
角色：「X of Y」的 Y＝總數、X 看後面的狀態字（valid／marketed→有效；cancelled→註銷）；
  「N valid …」有效；「N licences are valid」有效；「N (entries|records|registrations…)」總數；名詞前有 single-ingredient 時是單方（不改寫）。
讀法：沒有限定詞的總數接受 total、valid。數字已等於任一合理讀法就不動；要改時只在各讀法結果唯一時才改，否則 ambiguous。
不改、列出（要改請寫查核紀錄）：單方張數跟事實不符（single）、原數字 0（zero-premise）、新數字 0（zero-result）、1 跟非 1 之間的改動或 both
  （英文單複數與動詞要跟著改，grammar）、句子說「all／both … valid／single-ingredient」而跟事實不符（premise）。
"""
from __future__ import annotations

import re

SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z*\[(>-])")
WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10,
         "eleven": 11, "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
         "eighteen": 18, "nineteen": 19, "twenty": 20, "both": 2}
W_OUT = {v: k for k, v in WORDS.items() if k != "both"}
NUM = re.compile(r"(?<![\w.,/$-])(\d{1,4}|" + "|".join(sorted(WORDS, key=len, reverse=True)) + r")(?![\w%/-]|\.\d|,\d)", re.I)
NOUN = r"(?:licen[cs]es?|authori[sz]ations?|registrations?|listings?|products?|records?|entries|entry)"
LICENSE = re.compile(r"licen[cs]e|authori[sz]ation|registration|\blistings?\b|\bPNF\b|formulary", re.I)
PRODUCT_CTX = re.compile(r"\bproducts?\b|\brecords?\b|\bentr(?:y|ies)\b", re.I)
LOCAL_CTX = re.compile(r"Philippine|\bPNF\b|formulary|local (?:data|record)|single[- ]ingredient|for this drug|\bvalid\b|\bmarketed\b|\blisted\b", re.I)
NOT_LICENSE = re.compile(r"\btrials?\b|\bstud(?:y|ies)\b|patients?|participants|subjects|PMID|NCT\d|publications?|articles?|\bcases?\b|"
                         r"%|\byears?\b|\bmonths?\b|\bweeks?\b|\bdays?\b|\bdos(?:e|es|ing)\b|\bscore|\bphase\b|indications?|adverse|"
                         r"interactions?|PubMed|ClinicalTrials|\b(?:19|20)\d\d\b|knowledge graph|predict", re.I)
HEDGED = re.compile(r"at least|\bpartial|\bmay\b|\bmight\b|approximately|\babout\b|\baround\b|\bover\b|more than|\bup to\b|nearly|roughly|"
                    r"\bsome\b|several|\bmany\b|\bmost\b|further|\bother\b|\bothers\b|another|additional|remaining|\brest\b|\balso\b|"
                    r"includ|\bamong\b|of which|e\.g\.|for example|such as|combination|combined|\bcombo|named|\bbrands?\b|under the|"
                    r"manufactur|generic|\bplus\b|/|"
                    r"tablet|capsule|inject|solution|suspension|cream|ointment|\bgel\b|patch|spray|inhal|drops|syrup|powder|suppositor|"
                    r"lozenge|\boral\b|topical|intravenous|ophthalmic|nasal|strengths?\b|\bmg\b|\bmcg\b|\bmL\b|"
                    r"evidence pack|\bquer(?:y|ied)|search|retriev|returned|\bfound\b|identified|located|matched|"
                    r"veterinar|\bUS\b|\bU\.S\.|United States|\bFDA\b|\bEMA\b|Europe|other countries|worldwide|"
                    r"\bwas\b|\bwere\b|\bhad\b|used to|formerly|previously|historical", re.I)
BRAND = re.compile(r"\b(?!PNF\b|NCT\b|FDA\b)[A-Z][A-Z0-9-]{3,}\b")  # 大寫品名（APO-…、LIPITOR）：講品牌子集
DISPLAY = re.compile(r"\bshown\b|\bshowing\b|\bshows?\b|\blisted (?:above|below|here)\b|\btable\b|\bthe list\b|\babove\b|\bbelow\b|"
                     r"\bfirst (?:five|\d+)\b|\bexamples?\b|\bselection\b|\bthese are\b|\bfollowing\b|\bhere\b", re.I)
VALID = r"(?:valid|marketed|active)"
CANC = r"(?:cancel+ed|revoked|withdrawn|discontinued)"
NM = r"(?:dormant)"
SINGLE = r"(?:single[- ]ingredient|single[- ]entity|single[- ]agent|mono-?component)"
ADJ_WORD = r"(?:valid|currently valid|marketed|currently marketed|active|current|cancel+ed|discontinued|dormant|" + SINGLE + \
           r"|Philippine|PNF|distinct|separate|registered|approved|listed|recorded|drug|product|unique|individual)"
ADJ = r"(?:" + ADJ_WORD + r"\s+)*"
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)
TODO_SEC = re.compile(r"Conclusion|Next Steps|Recommend|To proceed|Action", re.I)


def _val(tok):
    t = tok.lower()
    return int(t) if t.isdigit() else WORDS[t]


def _fmt(tok, v):
    if tok.isdigit() or v not in W_OUT:
        return str(v)
    w = W_OUT[v]
    return w.capitalize() if tok[:1].isupper() else w


def _np(right):
    """數字後面的名詞片語：回 (形容詞字串, 名詞片語結束位置) 或 None"""
    m = re.match(r"\s+(" + ADJ + r")" + NOUN + r"\b", right, re.I)
    return (m.group(1), m.end()) if m else None


def _status(text):
    if re.search(CANC, text, re.I):
        return "cancelled"
    if re.search(NM, text, re.I):
        return "nm"
    if re.search(VALID, text, re.I):
        return "valid"
    return None


def _role(s, a, b):
    """回 (角色, single) 或 None。角色：total／valid／cancelled／nm"""
    left, right = s[max(0, a - 60):a], s[b:b + 100]
    # 「X of Y」的 Y
    if re.search(r"\b(?:of|out of)\s+(?:the\s+|these\s+|its\s+|all\s+)?$", left, re.I):
        pre = re.sub(r"\b(?:of|out of)\s+(?:the\s+|these\s+|its\s+|all\s+)?$", "", left, flags=re.I)
        if not pre.strip() or re.search(r"[,;(]\s*$", pre):  # 句首「Of the 14 DINs, 11 are valid」
            np = _np(right)
            return ("total", bool(re.search(SINGLE, np[0], re.I))) if np else None
        if re.search(r"(\d+|" + "|".join(WORDS) + r")\s+(?:" + ADJ + NOUN + r"\s+)?$", pre, re.I):
            np = _np(right)
            return ("total", bool(np and re.search(SINGLE, np[0], re.I))) if np or re.match(r"\s*[,;.)]|\s+(?:are|is)\b", right) else None
        return None
    # 「X of Y …」的 X：看後面的狀態字
    m = re.match(r"\s+(?:of|out of)\s+(?:the\s+|these\s+|its\s+)?\S+\s+(" + ADJ + r")(?:" + NOUN + r")?\s*(?:\([^)]*\)\s*)?"
                 r"(?:(?:are|is|remain\w*|currently|still|now)\s+){1,3}(" + VALID + "|" + CANC + "|" + NM + r")", right, re.I)
    if m:
        return _status(m.group(2)), bool(re.search(SINGLE, m.group(1), re.I))
    if re.match(r"\s+(?:of|out of)\s+", right, re.I):
        return None
    np = _np(right)
    if np:
        adj, end = np
        single = bool(re.search(SINGLE, adj, re.I))
        st = _status(adj)
        if st:
            return st, single
        tail = right[end:end + 50]
        mm = re.match(r"\s*(?:\([^)]*\)\s*)?(?:(?:are|is|remain\w*)\s+)(?:(?:all|both|currently|still|now)\s+)*(" + VALID + "|" + CANC + "|" + NM + r")\b", tail, re.I)
        if mm and not re.search(r"\b(?:all|both|the)\s*$", left, re.I):
            return _status(mm.group(1)), single
        return "total", single
    # 「…; 8 are valid」「Of the 9 licences, 8 are valid」
    mm = re.match(r"\s+(?:of them\s+)?(?:are|is|remain\w*)\s+(?:(?:currently|still|now)\s+)*(" + VALID + "|" + CANC + "|" + NM + r")\b", right, re.I)
    if mm and re.search(LICENSE, s[:a]):
        return _status(mm.group(1)), None  # single 不明
    return None


def _readings(role, single, f, explicit):
    t, v, c = f.get("total"), f.get("valid") or 0, f.get("cancelled") or 0
    nm = f.get("not_marketed") or 0
    vs, st = f.get("valid_single"), f.get("single_total")
    if single:
        if vs is None or st is None:
            return set(), None
        if role == "valid":
            ok = {vs} | ({st} if c == 0 else set())
            return ok, (vs if nm == 0 else None)
        if role == "total":
            ok = {st} if explicit else {st, vs}
            return ok, (st if explicit or st == vs else None)
        return set(), None
    if role == "cancelled":
        return {c}, c
    if role == "nm":
        return {nm}, nm
    if role == "valid":
        return {v, v + nm}, (v if nm == 0 else None)
    if explicit:
        return {t}, t
    return {t, v, v + nm}, (t if t == v else None)


def _premise_ok(sent, f):
    lo = sent.lower()
    t, v, c, nm = f.get("total"), f.get("valid") or 0, f.get("cancelled") or 0, f.get("not_marketed") or 0
    if re.search(r"\b(all|both|every|each)\b[^.;]{0,60}\b(valid|active)\b", lo) and c:
        return False
    if re.search(r"\b(all|both|every|each)\b[^.;]{0,60}\bmarketed\b", lo) and (c or nm):
        return False
    if re.search(r"\b(all|both|every|each)\b[^.;]{0,60}" + SINGLE, lo) and f.get("single_total") != t:
        return False
    if re.search(r"\b(?:none|no|nothing)\b[^.;]{0,40}" + CANC, lo) and c:
        return False
    if re.search(r"\b(the only|the sole|a single|only one)\b", lo):
        return False
    return True


def rewrite_sentence(sent, f):
    """回傳 (新句子, 跳過理由或 None)。"""
    if not NUM.search(sent):
        return sent, None
    if not LICENSE.search(sent) and not (PRODUCT_CTX.search(sent) and LOCAL_CTX.search(sent)):
        return sent, None
    found = [(m, _role(sent, m.start(), m.end())) for m in NUM.finditer(sent)]
    found = [(m, r) for m, r in found if r]
    if not found:
        return sent, None
    if NOT_LICENSE.search(sent):
        return sent, None
    _plain = re.sub(r"\[[^\]]*\]\([^)]*\)", "", sent)
    if HEDGED.search(_plain) or BRAND.search(_plain):
        return sent, "hedged/subset"
    if any(r[1] is None for _, r in found) and re.search(SINGLE, sent, re.I):
        return sent, "hedged/subset"  # 「…, 8 are valid」而句子另講單方：分不清是哪個數
    explicit = any(r[0] in ("valid", "cancelled", "nm") for _, r in found) or \
        bool(re.search(r"\b(?:all|both)\b[^.;]{0,60}\b(?:valid|marketed|active|" + CANC[3:-1] + r")\b", sent, re.I))
    if DISPLAY.search(sent):  # 講表格顯示筆數：不改；數字跟事實對不上時列出（reason＝display）
        bad = any(_val(m.group(1)) not in _readings(r[0], r[1], f, explicit)[0] for m, r in found)
        return sent, ("display" if bad else "display-ok")
    subs = []
    for m, (role, single) in found:
        old = _val(m.group(1))
        ok, v = _readings(role, single, f, explicit)
        if not ok:
            return sent, "hedged/subset"
        if old in ok:
            continue
        if single:  # 單方張數不改寫（本站 2026-11-06 慣例是刪「single-ingredient」字樣；checker total_x 以總數比），列出
            return sent, "single"
        if v is None:
            return sent, "ambiguous"
        if old == 0:
            return sent, "zero-premise"
        if v == 0:
            return sent, "zero-result"
        if m.group(1).lower() == "both" or (old == 1) != (v == 1):
            return sent, "grammar"
        subs.append((m, v))
    if not subs:
        return sent, None
    if not _premise_ok(sent, f):
        return sent, "premise"
    out, pos = [], 0
    for m, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(_fmt(m.group(1), v))
        pos = m.end(1)
    out.append(sent[pos:])
    return "".join(out), None


def _line(ln, f, protect, skipped):
    if ln.startswith(("|", "#", "{:", "<")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if not held and any(a != b for a, b in zip(parts, new)):
        # 同一行別句說「none … cancelled」「all … valid」而跟事實不符（數字改了、前提沒改會前後矛盾）：整行不動、列出
        for s in parts:
            if s in new and re.search(r"cancel|valid|marketed|" + SINGLE, s, re.I) and not _premise_ok(s, f) and not NUM.search(s):
                skipped.append(("premise", s.strip()))
                held = True
    if held:  # 同一行有句子判斷不了：整行不動
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格、待辦條目不動。"""
    skipped = []
    if not facts or facts.get("partial") or not facts.get("total"):
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines, todo = [], False
    for ln in body.split("\n"):
        if ln.startswith("## "):
            todo = bool(TODO_SEC.search(ln))
        if "\x00" in ln or (todo and re.match(r"\s*(?:[-*+]|\d+\.)\s", ln)):
            lines.append(ln)
        else:
            lines.append(_line(ln, facts, protect, skipped))
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
