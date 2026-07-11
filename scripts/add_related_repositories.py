#!/usr/bin/env python3
"""Add the localized Related Repositories section without rebuilding the repository."""

from pathlib import Path

from generate_repo import LANGS, ROOT, render_related


def main() -> None:
    token = '<a id="acknowledge"></a>'
    for lang, filename, _, _ in LANGS:
        path = ROOT / filename
        text = path.read_text(encoding="utf-8")
        if '<a id="related-repositories"></a>' in text:
            print(f"{filename}: already present")
            continue
        if token not in text:
            raise SystemExit(f"missing acknowledge anchor in {filename}")
        path.write_text(text.replace(token, render_related(lang) + "\n\n" + token, 1), encoding="utf-8")
        print(f"{filename}: added")


if __name__ == "__main__":
    main()
