#!/usr/bin/env python3
"""Check public copy against the user-supplied literal redline terms; not approval."""
import argparse
import json
from pathlib import Path
import re
import sys
import unicodedata


def normalize(text):
    return "".join(c for c in unicodedata.normalize("NFKC", text).casefold()
                   if c.isalnum() or c == "%")


def check(text, rules):
    compact, lines = [], []
    for number, line in enumerate(text.splitlines(), 1):
        part = normalize(line)
        compact.extend(part)
        lines.extend([number] * len(part))
    compact = "".join(compact)
    hits = []
    for category, terms in rules.items():
        for term in terms:
            needle = normalize(term)
            for match in re.finditer(re.escape(needle), compact):
                hits.append({"line": lines[match.start()], "category": category, "term": term})
    for match in re.finditer(r"(?<![0-9])1[3-9][0-9]{9}(?![0-9])", compact):
        hits.append({"line": lines[match.start()], "category": "疑似联系方式", "term": "疑似手机号码"})
    return hits


def main():
    parser = argparse.ArgumentParser(description="仅检查公开文本固定词；不检查图片声音，不作审核通过判断。")
    parser.add_argument("files", nargs="+", type=Path, help="公开文案文本；不要传入Skill规则或内部审核记录")
    args = parser.parse_args()
    rules = json.loads((Path(__file__).resolve().parents[1] / "assets/redline-terms.json").read_text(encoding="utf-8"))
    results = []
    try:
        for path in args.files:
            results.append({"file": str(path), "hits": check(path.read_text(encoding="utf-8"), rules)})
    except (OSError, UnicodeError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps({"results": results, "scope": "固定词文字初查；语义、画面、声音与人工审核需另做"}, ensure_ascii=False, indent=2))
    return 1 if any(r["hits"] for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
