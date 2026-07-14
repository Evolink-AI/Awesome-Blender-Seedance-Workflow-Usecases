#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
R2_MEDIA_BASE = "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media"
R2_BANNER_URL = "https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/images/banner.png"
FILES = [
    "README.md",
    "README_es.md",
    "README_pt.md",
    "README_ja.md",
    "README_ko.md",
    "README_de.md",
    "README_fr.md",
    "README_tr.md",
    "README_zh-TW.md",
    "README_zh-CN.md",
    "README_ru.md",
]
EXPECTED_README_CTAS = [
    "https://evolink.ai/cookbook/blender-to-video?utm_source=github&utm_medium=banner&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=readme_banner",
    "https://evolink.ai/cookbook/blender-to-video?utm_source=github&utm_medium=badge&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=model_try",
    "https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=badge&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key",
    "https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key",
]
EXPECTED_ISSUE_CONTACT = "https://evolink.ai?utm_source=github&utm_medium=issue_template&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=contact_link"
UTM_CAMPAIGN = "awesome-blender-seedance-workflow-usecases"
URL_RE = re.compile(r"^https?://")


def fail(msg: str) -> None:
    raise SystemExit(f"FAIL: {msg}")


curated = json.loads((ROOT / "blender-seedance-usecase-curated.json").read_text())
video_sources = json.loads((ROOT / "data" / "usecase-video-sources.json").read_text())
EXPECTED_CASES = len(curated["items"])
if curated["metadata"].get("selected_count") != EXPECTED_CASES:
    fail("curated selected_count does not match README case count")

expected_label_set = {str(item["case"]) for item in curated["items"]}
preview_map = {}
for row in video_sources["items"]:
    case_label = str(row.get("case_label") or "").strip()
    public_case = row.get("public_case")
    usage = str(row.get("usage") or "").strip()
    if not case_label and isinstance(public_case, int):
        case_label = f"case{public_case}"
    if not case_label:
        fail("video source row missing case label")
    local_media = row.get("local_media")
    r2_video_url = str(row.get("r2_video_url") or "").strip()
    r2_poster_url = str(row.get("r2_poster_url") or "").strip()
    if usage in {"standalone_public_case", "weekly_r2_video_only"} and (local_media or r2_video_url):
        preview_map[case_label] = {
            "video_url": r2_video_url or f"{R2_MEDIA_BASE}/{case_label}.mp4",
            "poster_url": r2_poster_url or f"{R2_MEDIA_BASE}/posters/{case_label}.jpg",
        }
    if local_media is not None and local_media and not (ROOT / local_media).exists():
        fail(f"missing video source local media {local_media}")
    attachment = str(row.get("attachment_url") or "").strip()
    if attachment and not URL_RE.search(attachment):
        fail(f"unexpected attachment URL for {case_label}")

for file in FILES:
    p = ROOT / file
    if not p.exists():
        fail(f"missing {file}")
    text = p.read_text()
    if R2_BANNER_URL not in text:
        fail(f"{file} missing configured shared R2 banner")
    anchors = re.findall(r'^<a id="case-([0-9]+)"></a>', text, re.M)
    heads = re.findall(r'^### Case ([0-9]+): \[', text, re.M)
    if len(anchors) != EXPECTED_CASES:
        fail(f"{file} has {len(anchors)} anchors, expected {EXPECTED_CASES}")
    if anchors != heads:
        fail(f"{file} anchors and case headings differ")
    if len(set(anchors)) != len(anchors):
        fail(f"{file} contains duplicate case anchors")
    if set(anchors) != expected_label_set:
        fail(f"{file} anchors do not match curated case labels")
    if "## 📊" not in text or "## ⚡" not in text or "## 📑" not in text or '<a id="related-repositories"></a>' not in text or "## 🙏" not in text:
        fail(f"{file} missing required usecase sections")
    if text.count("| Date: ") + text.count("| Fecha: ") + text.count("| Data: ") + text.count("| Datum: ") + text.count("| Tarih: ") + text.count("| 日期: ") + text.count("| Дата: ") < EXPECTED_CASES:
        fail(f"{file} missing Type/Date metadata lines")
    if ".github/ISSUE_TEMPLATE/use-case.yml" not in text or ".github/PULL_REQUEST_TEMPLATE.md" not in text:
        fail(f"{file} missing issue or PR template links")
    for expected_cta in EXPECTED_README_CTAS:
        if expected_cta not in text:
            fail(f"{file} missing primary CTA link {expected_cta}")
    for url in re.findall(r'https://evolink\.ai[^\s)>"`]+', text):
        if "utm_source=github" not in url or f"utm_campaign={UTM_CAMPAIGN}" not in url:
            fail(f"{file} has EvoLink URL without required README UTM: {url}")
        if not any(medium in url for medium in ("utm_medium=readme", "utm_medium=quickstart", "utm_medium=badge", "utm_medium=banner")):
            fail(f"{file} has EvoLink URL without approved README medium: {url}")
    if re.search(r'^media/[^\s]+$', text, re.M):
        fail(f"{file} still exposes repository-local bare media paths")
    for case_label, urls in preview_map.items():
        if urls["video_url"] not in text:
            fail(f"{file} missing public video URL for {case_label}")
        if urls["poster_url"] not in text:
            fail(f"{file} missing public poster URL for {case_label}")
    if f"{R2_MEDIA_BASE}/case13.jpg" not in text:
        fail(f"{file} missing R2 reference image for case13")

for img in ["images/banner.png"]:
    if not (ROOT / img).exists():
        fail(f"missing {img}")

for required in [
    "LICENSE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "docs/maintenance.md",
    "docs/media-type-inventory.md",
    "docs/r2-upload-report.md",
    "docs/video-poster-report.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/use-case.yml",
    "blender-seedance-usecase-curated.json",
    "data/usecase-video-sources.json",
    "images/banner.png",
]:
    if not (ROOT / required).exists():
        fail(f"missing {required}")

for rel in ["docs/maintenance.md", ".github/ISSUE_TEMPLATE/config.yml", "blender-seedance-usecase-curated.json"]:
    text = (ROOT / rel).read_text()
    for url in re.findall(r'https://evolink\.ai[^\s)>"`]+', text):
        if "utm_source=github" not in url or "utm_medium=" not in url or f"utm_campaign={UTM_CAMPAIGN}" not in url:
            fail(f"{rel} has EvoLink URL without required UTM: {url}")
if EXPECTED_ISSUE_CONTACT not in (ROOT / ".github" / "ISSUE_TEMPLATE" / "config.yml").read_text():
    fail("issue template config missing tracked EvoLink contact URL")

if video_sources["metadata"].get("source_rows") != len(video_sources["items"]):
    fail("video source row count metadata does not match actual rows")
video_labels = [str(row.get("case_label") or "") for row in video_sources["items"]]
if len(set(video_labels)) != len(video_labels):
    fail("video source labels contain duplicates")

media_paths = []
for item in curated["items"]:
    for rel in item.get("local_media", []):
        media_paths.append(rel)
        if not (ROOT / rel).exists():
            fail(f"missing local media {rel}")

print(f"PASS: {len(FILES)} README files, {EXPECTED_CASES} cases each, {len(preview_map)} public video previews per README, {len(media_paths)} tracked local source media files")
