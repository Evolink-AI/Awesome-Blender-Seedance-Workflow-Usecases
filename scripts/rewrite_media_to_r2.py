#!/usr/bin/env python3
"""Rewrite legacy bare media paths in localized READMEs to R2 poster/playback links."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPO = "Awesome-Blender-Seedance-Workflow-Usecases"
R2 = f"https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/{REPO}/media"
FILES = {
    "README.md": ("Play demo video", "Reference image"),
    "README_es.md": ("Reproducir video de demostración", "Imagen de referencia"),
    "README_pt.md": ("Reproduzir vídeo de demonstração", "Imagem de referência"),
    "README_ja.md": ("デモ動画を再生", "参照画像"),
    "README_ko.md": ("데모 동영상 재생", "참조 이미지"),
    "README_de.md": ("Demovideo abspielen", "Referenzbild"),
    "README_fr.md": ("Lire la vidéo de démonstration", "Image de référence"),
    "README_tr.md": ("Demo videosunu oynat", "Referans görseli"),
    "README_zh-TW.md": ("播放示範影片", "參考圖片"),
    "README_zh-CN.md": ("播放演示视频", "参考图像"),
    "README_ru.md": ("Воспроизвести демонстрационное видео", "Референсное изображение"),
}
VIDEO = re.compile(r"^media/(?P<name>case(?P<number>\d+))\.mp4$", re.MULTILINE)
IMAGE = re.compile(r"^media/(?P<name>case(?P<number>\d+))\.(?P<ext>jpg|jpeg|png)$", re.MULTILINE)


def rewrite(path: Path, play_label: str, image_label: str) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")

    def video(match: re.Match[str]) -> str:
        name = match.group("name")
        number = match.group("number")
        return f"[![{play_label} — Case {number}]({R2}/posters/{name}.jpg)]({R2}/{name}.mp4)"

    def image(match: re.Match[str]) -> str:
        name = match.group("name")
        number = match.group("number")
        ext = match.group("ext")
        return f"![{image_label} — Case {number}]({R2}/{name}.{ext})"

    text, videos = VIDEO.subn(video, text)
    text, images = IMAGE.subn(image, text)
    path.write_text(text, encoding="utf-8")
    return videos, images


def main() -> None:
    total_videos = total_images = 0
    for filename, labels in FILES.items():
        videos, images = rewrite(ROOT / filename, *labels)
        total_videos += videos
        total_images += images
        print(f"{filename}: videos={videos} images={images}")
    print(f"PASS: rewritten videos={total_videos} images={total_images}")


if __name__ == "__main__":
    main()
