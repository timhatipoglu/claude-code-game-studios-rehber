#!/usr/bin/env python3
"""Claude Code Game Studios'un ajan ve skill boyutlarını ölçer.

Kullanım:  python3 olcum.py
Yalnız Python 3 standart kütüphanesi gerekir; GitHub'dan dosyaları okur, hiçbir şey yazmaz.
Token tahmini kabadır: karakter / 4 (İngilizce metin için).
"""
import collections
import json
import re
import urllib.request
from concurrent.futures import ThreadPoolExecutor

REPO = "Donchitos/Claude-Code-Game-Studios"
RAW = f"https://raw.githubusercontent.com/{REPO}/main/"


def al(yol):
    return yol, urllib.request.urlopen(RAW + yol, timeout=20).read().decode("utf-8", "replace")


def ayir(metin):
    m = re.match(r"---\n(.*?)\n---\n?(.*)", metin, re.S)
    baslik, govde = (m.group(1), m.group(2)) if m else ("", metin)

    def alan(ad):
        e = re.search(rf"^{ad}:\s*(.*)$", baslik, re.M)
        return e.group(1).strip().strip('"') if e else ""

    return alan, govde


def tok(karakter):
    return f"≈ {round(karakter / 4 / 1000, 1)} bin token"


ag = json.load(urllib.request.urlopen(f"https://api.github.com/repos/{REPO}/git/trees/main?recursive=1", timeout=20))["tree"]
ajanlar = [x["path"] for x in ag if re.match(r"\.claude/agents/[^/]+\.md$", x["path"])]
skiller = [x["path"] for x in ag if re.match(r"\.claude/skills/[^/]+/SKILL\.md$", x["path"])]
with ThreadPoolExecutor(6) as ex:
    A = dict(ex.map(al, ajanlar))
    S = dict(ex.map(al, skiller))
    ex_claude = al("CLAUDE.md")[1]

print(f"== {REPO} ==")
a_model = collections.Counter(ayir(t)[0]("model") or "-" for t in A.values())
a_acik = sum(len(ayir(t)[0]("description")) for t in A.values())
a_govde = sorted((len(ayir(t)[1]), p.split("/")[-1][:-3]) for p, t in A.items())
print(f"\nAJAN: {len(A)} adet, model dağılımı {dict(a_model)}")
print(f"  açıklamalar (oturum başında): {a_acik} karakter, {tok(a_acik)}")
print(f"  en büyük gövde (yalnız o ajan çalışınca): {a_govde[-1][0]} karakter, {tok(a_govde[-1][0])} ({a_govde[-1][1]})")

s_model = collections.Counter(ayir(t)[0]("model") or "-" for t in S.values())
s_kapali = sum(1 for t in S.values() if ayir(t)[0]("disable-model-invocation") == "true")
s_acik = sum(len(ayir(t)[0]("description")) + len(p.split("/")[-2]) for p, t in S.items())
s_govde = sorted((len(ayir(t)[1]), p.split("/")[-2]) for p, t in S.items())
medyan = s_govde[len(s_govde) // 2][0]
print(f"\nSKILL: {len(S)} adet, model dağılımı {dict(s_model)}, açıklaması bağlama girmeyen (disable-model-invocation): {s_kapali}")
print(f"  ad + açıklama (oturum başında): {s_acik} karakter, {tok(s_acik)}")
print(f"  gövde medyan (yalnız skill çağrılınca, sonra konuşmada kalır): {medyan} karakter, {tok(medyan)}")
print(f"  en büyük gövde: {s_govde[-1][0]} karakter, {tok(s_govde[-1][0])} ({s_govde[-1][1]})")

print(f"\nCLAUDE.md: {len(ex_claude)} karakter, {tok(len(ex_claude))}")
print(f"\nOturum başında toplam (ajan + skill açıklamaları + CLAUDE.md): {tok(a_acik + s_acik + len(ex_claude))}")
