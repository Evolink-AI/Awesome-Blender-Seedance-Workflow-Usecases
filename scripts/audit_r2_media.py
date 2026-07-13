#!/usr/bin/env python3
"""Audit uploaded R2 media, poster pairs, and public README usage."""

from __future__ import annotations

import concurrent.futures
import json
import mimetypes
import subprocess
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MEDIA = ROOT / "media"
REPO = "Awesome-Blender-Seedance-Workflow-Usecases"
R2_ROOT = f"https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/{REPO}"
READMES = sorted(ROOT.glob("README*.md"))
VIDEO_SOURCE_MAP = ROOT / "data" / "usecase-video-sources.json"


@dataclass
class Result:
    source: str
    url: str
    status: int
    content_type: str
    error: str = ""


def url_for(path: Path) -> str:
    return f"{R2_ROOT}/{path.relative_to(ROOT).as_posix()}"


def check(url: str, source: str) -> Result:
    request = urllib.request.Request(url, headers={"Range": "bytes=0-0", "User-Agent": "EvoLink-R2-Audit/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return Result(source, url, response.status, response.headers.get_content_type())
    except urllib.error.HTTPError as exc:
        return Result(source, url, exc.code, exc.headers.get_content_type() if exc.headers else "", str(exc))
    except Exception as exc:
        return Result(source, url, 0, "", str(exc))


def probe(video: Path) -> dict:
    command = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height:format=duration",
        "-of",
        "json",
        str(video),
    ]
    payload = json.loads(subprocess.run(command, check=True, capture_output=True, text=True).stdout)
    stream = payload["streams"][0]
    return {
        "width": stream["width"],
        "height": stream["height"],
        "duration": float(payload["format"]["duration"]),
    }


def remote_preview_rows() -> list[dict]:
    payload = json.loads(VIDEO_SOURCE_MAP.read_text(encoding="utf-8"))
    rows = []
    for row in payload["items"]:
        case_label = str(row.get("case_label") or "").strip()
        local_media = row.get("local_media")
        video_url = str(row.get("r2_video_url") or "").strip()
        poster_url = str(row.get("r2_poster_url") or "").strip()
        if not case_label:
            continue
        if not video_url and local_media:
            video_url = f"{R2_ROOT}/{local_media}"
        if not poster_url and (video_url or local_media):
            poster_url = f"{R2_ROOT}/media/posters/{case_label}.jpg"
        if video_url or poster_url:
            rows.append(
                {
                    "case_label": case_label,
                    "video_url": video_url,
                    "poster_url": poster_url,
                    "local_media": local_media,
                }
            )
    return rows


def main() -> None:
    local_files = sorted(
        [path for path in MEDIA.rglob("*") if path.is_file()]
        + [path for path in (ROOT / "images").rglob("*") if path.is_file()]
    )
    readme_text = "\n".join(path.read_text(encoding="utf-8") for path in READMES)
    remote_rows = remote_preview_rows()

    checks: list[tuple[str, str]] = [(str(path.relative_to(ROOT)), url_for(path)) for path in local_files]
    for row in remote_rows:
        if row["video_url"] and row["local_media"] is None:
            checks.append((f"{row['case_label']} remote video", row["video_url"]))
        if row["poster_url"] and not (MEDIA / "posters" / f"{row['case_label']}.jpg").exists():
            checks.append((f"{row['case_label']} remote poster", row["poster_url"]))

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(lambda pair: check(pair[1], pair[0]), checks))
    failures = [result for result in results if result.status not in {200, 206}]

    inventory = [
        "# Media Type Inventory",
        "",
        f"- Generated: {datetime.now(timezone.utc).isoformat()}",
        f"- Repository: `{REPO}`",
        f"- Local files: {len(local_files)}",
        f"- Remote-only preview assets: {len([row for row in remote_rows if row['local_media'] is None and row['video_url']])}",
        "",
        "| Source | Type | Bytes | Public README usage | R2 URL |",
        "|---|---:|---:|---:|---|",
    ]
    for path in local_files:
        rel = path.relative_to(ROOT).as_posix()
        kind = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        inventory.append(f"| `{rel}` | `{kind}` | {path.stat().st_size} | {'yes' if url_for(path) in readme_text else 'no'} | {url_for(path)} |")
    for row in remote_rows:
        if row["local_media"] is None and row["video_url"]:
            inventory.append(f"| `{row['case_label']} (remote video only)` | `video/mp4` | 0 | {'yes' if row['video_url'] in readme_text else 'no'} | {row['video_url']} |")
    (ROOT / "docs" / "media-type-inventory.md").write_text("\n".join(inventory) + "\n", encoding="utf-8")

    audit = [
        "# R2 Upload And Origin Audit",
        "",
        f"- Generated: {datetime.now(timezone.utc).isoformat()}",
        "- Bucket: `image`",
        "- Key prefix: `github-repo-media`",
        f"- Public object prefix: `github-repo-media/{REPO}`",
        f"- Objects checked: {len(results)}",
        f"- Passed: {len(results) - len(failures)}",
        f"- Failed: {len(failures)}",
        f"- Result: `{'PASS' if not failures else 'FAIL'}`",
        "",
        "| Source | Status | Content-Type | R2 URL |",
        "|---|---:|---|---|",
    ]
    for result in results:
        audit.append(f"| `{result.source}` | {result.status} | `{result.content_type}` | {result.url} |")
    (ROOT / "docs" / "r2-upload-report.md").write_text("\n".join(audit) + "\n", encoding="utf-8")

    posters = [
        "# Video Poster Extraction Report",
        "",
        f"- Generated: {datetime.now(timezone.utc).isoformat()}",
        f"- Local videos: {len(list(MEDIA.glob('*.mp4')))}",
        f"- Remote-only videos: {len([row for row in remote_rows if row['local_media'] is None and row['video_url']])}",
        "- Extraction: `ffmpeg -ss 0.5 -frames:v 1 -q:v 3` for local videos; remote-only rows keep their uploaded R2 poster URL.",
        "",
        "| Video | Duration | Dimensions | Poster | Poster bytes |",
        "|---|---:|---:|---|---:|",
    ]
    poster_failures = []
    for video in sorted(MEDIA.glob("*.mp4")):
        poster = MEDIA / "posters" / f"{video.stem}.jpg"
        if not poster.is_file():
            poster_failures.append(video.name)
            continue
        info = probe(video)
        posters.append(
            f"| `{video.relative_to(ROOT).as_posix()}` | {info['duration']:.3f}s | "
            f"{info['width']}x{info['height']} | `{poster.relative_to(ROOT).as_posix()}` | {poster.stat().st_size} |"
        )
    for row in remote_rows:
        if row["local_media"] is None and row["video_url"]:
            posters.append(f"| `{row['case_label']} (remote only)` | remote | remote | `{row['poster_url']}` | remote |")
    posters.insert(6, f"- Result: `{'PASS' if not poster_failures else 'FAIL'}`")
    (ROOT / "docs" / "video-poster-report.md").write_text("\n".join(posters) + "\n", encoding="utf-8")

    if failures or poster_failures:
        raise SystemExit(f"FAIL: origin_failures={len(failures)} poster_failures={len(poster_failures)}")
    print(f"PASS: {len(results)} checked R2 objects and {len(list(MEDIA.glob('*.mp4')))} local video/poster pairs")


if __name__ == "__main__":
    main()
