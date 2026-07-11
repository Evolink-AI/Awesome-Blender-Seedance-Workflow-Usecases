#!/usr/bin/env python3
"""Audit public Markdown/HTML links, anchors, UTM parameters, and HTTP status."""

from __future__ import annotations

import concurrent.futures
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"!?\[([^\]]*)\]\(([^)]+)\)")
HTML_LINK = re.compile(r"<(?:a|img)\b[^>]*(?:href|src)=[\"']([^\"']+)[\"']", re.I)
EXPLICIT_ANCHOR = re.compile(r'<a id="([^"]+)"></a>')
HEADING = re.compile(r"^#{1,6}\s+(.+)$", re.M)
URL = re.compile(r"https?://[^\s<>\"')]+")
FILES = sorted(ROOT.glob("README*.md")) + sorted(
    path for path in (ROOT / "docs").glob("*.md") if path.name != "public-surface-link-audit.md"
) + [
    ROOT / "CONTRIBUTING.md", ROOT / "CODE_OF_CONDUCT.md", ROOT / "SECURITY.md"
]
MANUAL_DOMAINS = {"x.com", "twitter.com", "api.star-history.com", "www.star-history.com", "img.shields.io", "projects.blender.org"}


@dataclass
class Check:
    url: str
    status: int
    final_url: str
    content_type: str
    disposition: str
    error: str = ""


def slug(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text).strip().lower()
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    return re.sub(r"[\s-]+", "-", text).strip("-")


def http_check(url: str) -> Check:
    request = urllib.request.Request(url, headers={"Range": "bytes=0-0", "User-Agent": "EvoLink-Link-Audit/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=25) as response:
            return Check(url, response.status, response.geturl(), response.headers.get_content_type(), "pass")
    except urllib.error.HTTPError as exc:
        domain = urllib.parse.urlparse(url).netloc.lower()
        disposition = "manual-external-endpoint" if domain in MANUAL_DOMAINS and exc.code in {401, 403, 429, 500, 502, 503, 504} else "fail"
        return Check(url, exc.code, exc.geturl(), exc.headers.get_content_type() if exc.headers else "", disposition, str(exc))
    except Exception as exc:
        return Check(url, 0, url, "", "fail", str(exc))


def is_critical(url: str) -> bool:
    parsed = urllib.parse.urlparse(url)
    return (
        parsed.netloc == "evolink.ai"
        or parsed.netloc.endswith("r2.dev")
        or (parsed.netloc == "github.com" and parsed.path.startswith("/Evolink-AI/"))
    )


def main() -> None:
    local_errors: list[str] = []
    utm_errors: list[str] = []
    urls: set[str] = set()
    extracted = 0
    for path in FILES:
        if not path.is_file():
            local_errors.append(f"missing public file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        anchors = set(EXPLICIT_ANCHOR.findall(text)) | {slug(value) for value in HEADING.findall(text)}
        targets = [match.group(2).strip() for match in MARKDOWN_LINK.finditer(text)]
        targets += HTML_LINK.findall(text)
        targets += URL.findall(text)
        extracted += len(targets)
        for target in targets:
            target = target.strip("<>").rstrip("`.,;")
            if target.startswith("#"):
                if target[1:] not in anchors:
                    local_errors.append(f"{path.relative_to(ROOT)}: unresolved fragment {target}")
                continue
            if target.startswith(("mailto:", "javascript:")):
                continue
            if target.startswith(("http://", "https://")):
                urls.add(target)
                parsed = urllib.parse.urlparse(target)
                if parsed.netloc == "evolink.ai":
                    params = urllib.parse.parse_qs(parsed.query)
                    required = {"utm_source", "utm_medium", "utm_campaign", "utm_content"}
                    if not required.issubset(params):
                        utm_errors.append(f"{path.relative_to(ROOT)}: EvoLink URL missing UTM fields: {target}")
                continue
            file_target, _, fragment = target.partition("#")
            candidate = (path.parent / urllib.parse.unquote(file_target)).resolve()
            try:
                candidate.relative_to(ROOT)
            except ValueError:
                local_errors.append(f"{path.relative_to(ROOT)}: relative target escapes repository: {target}")
                continue
            if not candidate.exists():
                local_errors.append(f"{path.relative_to(ROOT)}: missing relative target: {target}")
            elif fragment and candidate.suffix.lower() == ".md":
                linked = candidate.read_text(encoding="utf-8")
                linked_anchors = set(EXPLICIT_ANCHOR.findall(linked)) | {slug(value) for value in HEADING.findall(linked)}
                if fragment not in linked_anchors:
                    local_errors.append(f"{path.relative_to(ROOT)}: unresolved linked fragment: {target}")

    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as pool:
        checks = list(pool.map(http_check, sorted(urls)))
    critical_failures = [check for check in checks if check.disposition == "fail" and is_critical(check.url)]
    warnings = [check for check in checks if check.disposition != "pass" and check not in critical_failures]
    p0 = len(local_errors) + len(utm_errors) + len(critical_failures)

    report = [
        "# Public Surface Link Audit",
        "",
        f"- Generated: {datetime.now(timezone.utc).isoformat()}",
        f"- Public files: {len(FILES)}",
        f"- Extracted link occurrences: {extracted}",
        f"- Unique external URLs checked: {len(checks)}",
        f"- Manual/bot-protection warnings: {len(warnings)}",
        f"- P0/P1 failures: {p0}",
        f"- Result: `{'PASS' if p0 == 0 else 'FAIL'}`",
        "",
        "## Local, Fragment, And UTM Findings",
        "",
    ]
    findings = local_errors + utm_errors
    report.extend([f"- {item}" for item in findings] or ["- None."])
    report += ["", "## External Status", "", "| URL | Status | Final URL | Type | Disposition |", "|---|---:|---|---|---|"]
    for check in checks:
        report.append(f"| {check.url} | {check.status} | {check.final_url} | `{check.content_type}` | `{check.disposition}` |")
    report += ["", "## Manual Verification Boundary", "", "X/Twitter, Shields, and Star History 401/403/429 responses are recorded as automation/bot-protection warnings. Source identity is also backed by the committed curated dataset; these warnings do not waive any EvoLink, R2, relative-file, or anchor failure."]
    (ROOT / "docs" / "public-surface-link-audit.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    (ROOT / ".codex" / "link-audit").mkdir(parents=True, exist_ok=True)
    (ROOT / ".codex" / "link-audit" / "latest.json").write_text(
        json.dumps({"checks": [asdict(check) for check in checks], "local_errors": local_errors, "utm_errors": utm_errors}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    if p0:
        raise SystemExit(f"FAIL: local={len(local_errors)} utm={len(utm_errors)} critical_http={len(critical_failures)}")
    print(f"PASS: files={len(FILES)} external={len(checks)} warnings={len(warnings)}")


if __name__ == "__main__":
    main()
