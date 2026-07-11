#!/usr/bin/env python3
"""Generate the authoritative public case inventory from curated data."""

import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "blender-seedance-usecase-curated.json"
OUT = ROOT / "docs" / "official-case-inventory.md"


def main() -> None:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    items = payload["items"]
    lines = [
        "# Official Case Inventory",
        "",
        f"- Generated: {datetime.now(timezone.utc).isoformat()}",
        f"- Source of truth: `{DATA.name}`",
        f"- Public cases: {len(items)}",
        "- Numbering policy: recorded legacy namespace; new cases append contiguously from Case 29",
        "",
        "| Case | Category | Type | Date | Creator | Source | Media |",
        "|---:|---|---|---|---|---|---|",
    ]
    for item in items:
        media = ", ".join(f"`{value}`" for value in item.get("local_media", [])) or "none"
        lines.append(
            f"| {item['case']} | `{item['category']}` | {item['evidence_type']} | {item['date']} | "
            f"[{item['author']}]({item['author_url']}) | [Open source]({item['url']}) | {media} |"
        )
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"PASS: {len(items)} cases -> {OUT}")


if __name__ == "__main__":
    main()
