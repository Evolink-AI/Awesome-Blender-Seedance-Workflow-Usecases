#!/usr/bin/env python3
"""Audit localized README case coverage and visible translation parity."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "docs" / "localization-audit.md"
LOCALES = ["de", "es", "fr", "ja", "ko", "pt", "ru", "tr", "zh-CN", "zh-TW"]
CASE_RE = re.compile(
    r'^### Case (?P<number>\d+): \[(?P<title>.+?)\]\([^\n]+\).*?\n\n\*\*(?P<takeaway>.+?)\*\*',
    re.MULTILINE | re.DOTALL,
)


def cases(path: Path) -> dict[int, tuple[str, str]]:
    text = path.read_text(encoding="utf-8")
    return {
        int(match.group("number")): (match.group("title").strip(), match.group("takeaway").strip())
        for match in CASE_RE.finditer(text)
    }


def main() -> int:
    english = cases(ROOT / "README.md")
    failures: list[str] = []
    rows: list[str] = []
    forbidden = [
        "Preview unavailable",
        "Audit status:",
        "Source notes:",
        "Have a Blender + Seedance workflow to add?",
    ]

    for locale in LOCALES:
        path = ROOT / f"README_{locale}.md"
        localized = cases(path)
        missing = sorted(set(english) - set(localized))
        same_titles = sorted(n for n in english if n in localized and english[n][0] == localized[n][0])
        same_takeaways = sorted(n for n in english if n in localized and english[n][1] == localized[n][1])
        text = path.read_text(encoding="utf-8")
        leaked = [phrase for phrase in forbidden if phrase in text]
        status = "PASS" if not (missing or same_titles or same_takeaways or leaked) else "FAIL"
        rows.append(
            f"| `{locale}` | {len(localized)} | {len(same_titles)} | {len(same_takeaways)} | "
            f"{', '.join(leaked) if leaked else 'none'} | {status} |"
        )
        if missing:
            failures.append(f"{locale}: missing cases {missing}")
        if same_titles:
            failures.append(f"{locale}: untranslated titles {same_titles}")
        if same_takeaways:
            failures.append(f"{locale}: untranslated takeaways {same_takeaways}")
        if leaked:
            failures.append(f"{locale}: English UI text remains: {', '.join(leaked)}")

    lines = [
        "# Localization Audit",
        "",
        f"- English case count: {len(english)}",
        f"- Localized README count: {len(LOCALES)}",
        f"- Status: {'PASS' if not failures else 'FAIL'}",
        "",
        "| Locale | Cases | Exact English titles | Exact English takeaways | English UI leaks | Status |",
        "|---|---:|---:|---:|---|---|",
        *rows,
        "",
        "## Findings",
        "",
        *(f"- {item}" for item in failures),
    ]
    if not failures:
        lines.append("- All 10 localized READMEs contain every case and translate the audited visible fields.")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{'PASS' if not failures else 'FAIL'}: {REPORT}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
