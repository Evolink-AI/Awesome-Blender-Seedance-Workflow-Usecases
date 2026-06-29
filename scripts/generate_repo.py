#!/usr/bin/env python3
"""Generate the Blender + Seedance usecase repository surface from curated data."""

from __future__ import annotations

import json
import re
import textwrap
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data" / "primary-use-case-posts.json"
REPO = "Awesome-Blender-Seedance-Workflow-Usecases"
OWNER = "cheercheung"
MODEL = "Blender + Seedance"
MODEL_ID = "seedance-2.0-reference-to-video"
CTA_ANCHOR = "#conversion-path-pending"

LANGS = [
    ("en", "README.md", "English", "images/en.png"),
    ("es", "README_es.md", "Español", "images/es.png"),
    ("pt", "README_pt.md", "Português", "images/pt.png"),
    ("ja", "README_ja.md", "日本語", "images/ja.png"),
    ("ko", "README_ko.md", "한국어", "images/ko.png"),
    ("de", "README_de.md", "Deutsch", "images/de.png"),
    ("fr", "README_fr.md", "Français", "images/fr.png"),
    ("tr", "README_tr.md", "Türkçe", "images/tr.png"),
    ("zh-TW", "README_zh-TW.md", "繁體中文", "images/zh-tw.png"),
    ("zh-CN", "README_zh-CN.md", "简体中文", "images/zh.png"),
    ("ru", "README_ru.md", "Русский", "images/ru.png"),
]

LANG_BADGES = """[![English](https://img.shields.io/badge/English-111111)](README.md)
[![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md)
[![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md)
[![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md)
[![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md)
[![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md)
[![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md)
[![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md)
[![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md)
[![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)"""

CATEGORY_META = {
    "camera-control": ("🎥", "Camera Control & Previs"),
    "character-action": ("🎬", "Character & Action Blocking"),
    "agentic-mcp": ("🤖", "Agentic Blender MCP"),
    "reference-prompt": ("🧩", "Reference, Prompt & Multi-Input Mapping"),
    "production-pipeline": ("🛠️", "Production Pipelines & Toolchains"),
    "limitations": ("🧪", "Limits, Tests & Troubleshooting"),
}

CATEGORY_FOR_CASE = {
    1: "camera-control",
    2: "camera-control",
    3: "character-action",
    4: "character-action",
    5: "character-action",
    6: "character-action",
    7: "reference-prompt",
    8: "limitations",
    9: "agentic-mcp",
    10: "reference-prompt",
    11: "reference-prompt",
    12: "agentic-mcp",
    13: "agentic-mcp",
    14: "camera-control",
    15: "camera-control",
    16: "camera-control",
    17: "reference-prompt",
    18: "reference-prompt",
    19: "character-action",
    20: "production-pipeline",
    21: "production-pipeline",
    22: "production-pipeline",
    23: "reference-prompt",
    24: "agentic-mcp",
    25: "production-pipeline",
    26: "camera-control",
    27: "agentic-mcp",
    28: "camera-control",
    29: "production-pipeline",
    30: "production-pipeline",
    31: "limitations",
    32: "camera-control",
    33: "limitations",
    34: "agentic-mcp",
    35: "reference-prompt",
}

EN_TITLES = {
    1: "Blender Blockout as Seedance Motion Reference",
    2: "Camera Blocking with Midjourney Start Frame",
    3: "Multi-Character Dialogue with Matched Poses",
    4: "Basic Shapes for Multi-Character Shots",
    5: "Action Choreography from Rough Blender Timing",
    6: "Handheld Follow Camera through Space",
    7: "Reproducible Seedance Prompt with Blender Reference",
    8: "Camera Rhythm Control and Foot-Sliding Limits",
    9: "Codex + Blender MCP Reference Video Workflow",
    10: "Character Mapping from Blocking and Reference Images",
    11: "FBX Animation Export as Seedance Reference",
    12: "No-Click Blender Animation with Agent Assistance",
    13: "One-Prompt Blender MCP Blockout",
    14: "ComfyUI Camera Control with Blender Previs",
    15: "Blender Viewport as Scene Direction",
    16: "Viewport Preview for Character Animation",
    17: "Director Checklist for Camera and Lens Control",
    18: "Action Shot Direction with Blender Camera Planning",
    19: "Camera and Character Blocking for Tactical Action",
    20: "Hermes, Krea, ComfyUI and Blender MCP Stack",
    21: "Blender MCP Viewport to Seedance Style Transfer",
    22: "Seedance Pro Viewport Style Transfer",
    23: "Mixamo Motion as Beginner Blender Reference",
    24: "Codex-Built Architecture and Camera Work",
    25: "Blender Previz to Anime Seedance Render",
    26: "Navigable AI Filmmaking with Claude and Blender",
    27: "Beginner Agent-Assisted HIPHOP Reference Test",
    28: "Viewport Preview to Realistic Start Frame",
    29: "FBX Clay Pass with Claude-Keyframed Camera",
    30: "Two-Night Hybrid Short Film Pipeline",
    31: "Reference-Only Blender Blockout without Start Frame",
    32: "One Reference Video, Multiple Worlds",
    33: "Mixamo Multi-Character Storyboard Experiment",
    34: "Codex MCP Direct Blender Export",
    35: "Composition Reference with Person and Vehicle Refs",
}

TYPE_FOR_CATEGORY = {
    "camera-control": "Demo",
    "character-action": "Demo",
    "agentic-mcp": "Integration",
    "reference-prompt": "Tutorial",
    "production-pipeline": "Integration",
    "limitations": "Limit",
}

LOCALE = {
    "en": {
        "intro": "Welcome to the Blender + Seedance usecase repository.",
        "value": "We collect real-world Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI, and agent-assisted workflows that creators used to control Seedance video generation.",
        "source": "The current collection is curated from user-provided X/Twitter source data. Each case links to the original post and creator profile.",
        "cta": "Primary landing page is pending. The intended conversion path is MCP install, EvoLink skill install, recharge, then run inside an agent.",
        "overview_note": "The collection favors concrete workflow evidence over hype: source-backed steps, reference-video methods, agent/MCP usage, reproducible constraints, and clearly stated limits.",
        "quick": "Quick API Access",
        "quick_text": "For repository scaffolding, this section records the expected Seedance reference-to-video model path. Replace the pending landing link once the owner provides the final page.",
        "pending": "Conversion Path Pending",
        "pending_body": "The final landing page is still pending. This draft records the intended path: MCP installation, EvoLink skill installation, recharge, and agent usage. Replace this section with the final CTA before calling the repository release-ready.",
        "menu": "Menu",
        "ack": "Acknowledge",
        "what": "What it shows",
        "case": "Case",
        "type": "Type",
        "date": "Date",
        "section": "Section",
        "cases": "Cases",
        "takeaway_prefix": "Use this case to",
        "notes_prefix": "Source notes",
    },
    "es": {
        "intro": "Repositorio de casos de uso Blender + Seedance.",
        "value": "Reunimos flujos reales de Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI y agentes para controlar la generación de video con Seedance.",
        "source": "La colección actual se deriva de datos X/Twitter proporcionados por el propietario. Cada caso enlaza la publicación original y el perfil del creador.",
        "cta": "La landing principal está pendiente; la ruta prevista es instalar MCP, instalar la skill de EvoLink, recargar y usarla dentro de un agente.",
        "overview_note": "La colección prioriza evidencia concreta: pasos, referencias de video, uso de agentes/MCP, restricciones reproducibles y límites claros.",
        "quick": "Acceso rápido a API",
        "quick_text": "Esta sección conserva la ruta esperada del modelo Seedance reference-to-video hasta que exista la landing final.",
        "pending": "Ruta de conversión pendiente",
        "pending_body": "La landing final sigue pendiente. Sustituye esta sección por el CTA final antes de marcar el repositorio como listo para release.",
        "menu": "Menú",
        "ack": "Agradecimientos",
        "what": "Qué muestra",
        "case": "Caso",
        "type": "Tipo",
        "date": "Fecha",
        "section": "Sección",
        "cases": "Casos",
        "takeaway_prefix": "Usa este caso para",
        "notes_prefix": "Notas de la fuente",
    },
    "pt": {
        "intro": "Repositório de casos de uso Blender + Seedance.",
        "value": "Reunimos fluxos reais com Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI e agentes para controlar a geração de vídeo no Seedance.",
        "source": "A coleção vem dos dados X/Twitter fornecidos pelo proprietário. Cada caso aponta para o post original e o criador.",
        "cta": "A landing principal está pendente; a rota prevista é instalar MCP, instalar a skill EvoLink, recarregar e usar no agente.",
        "overview_note": "A coleção prioriza evidência concreta: passos, vídeos de referência, uso de agente/MCP, restrições reproduzíveis e limites claros.",
        "quick": "Acesso rápido à API",
        "quick_text": "Esta seção registra o caminho esperado do modelo Seedance reference-to-video até a landing final existir.",
        "pending": "Caminho de conversão pendente",
        "pending_body": "A landing final ainda está pendente. Substitua esta seção pelo CTA final antes de marcar o repositório como pronto para release.",
        "menu": "Menu",
        "ack": "Agradecimentos",
        "what": "O que mostra",
        "case": "Caso",
        "type": "Tipo",
        "date": "Data",
        "section": "Seção",
        "cases": "Casos",
        "takeaway_prefix": "Use este caso para",
        "notes_prefix": "Notas da fonte",
    },
    "ja": {
        "intro": "Blender + Seedance のユースケース集です。",
        "value": "Blender、Blender MCP、viewport、previs、FBX、Mixamo、ComfyUI、agent 支援で Seedance 動画生成を制御する実例を集めています。",
        "source": "現在のコレクションは、所有者提供の X/Twitter データから整理されています。各ケースは元投稿と作者プロフィールにリンクします。",
        "cta": "主要ランディングページは未確定です。想定経路は MCP 導入、EvoLink skill 導入、チャージ、agent 内での利用です。",
        "overview_note": "このコレクションは宣伝よりも具体的な証拠を優先します。手順、参照動画、agent/MCP 利用、再現条件、明確な制限を重視します。",
        "quick": "API クイックアクセス",
        "quick_text": "最終 landing が提供されるまで、ここには Seedance reference-to-video の想定モデル経路を記録します。",
        "pending": "コンバージョン経路は未確定",
        "pending_body": "最終 landing はまだ未確定です。release-ready と呼ぶ前に、この節を最終 CTA に置き換えてください。",
        "menu": "メニュー",
        "ack": "謝辞",
        "what": "内容",
        "case": "ケース",
        "type": "Type",
        "date": "Date",
        "section": "セクション",
        "cases": "ケース",
        "takeaway_prefix": "このケースは次に使えます:",
        "notes_prefix": "ソースメモ",
    },
    "ko": {
        "intro": "Blender + Seedance 유스케이스 저장소입니다.",
        "value": "Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI, agent 기반 워크플로로 Seedance 비디오 생성을 제어한 실제 사례를 모았습니다.",
        "source": "현재 컬렉션은 소유자가 제공한 X/Twitter 데이터에서 선별했습니다. 각 사례는 원본 게시물과 제작자 프로필로 연결됩니다.",
        "cta": "주요 랜딩 페이지는 아직 미정입니다. 예정 경로는 MCP 설치, EvoLink skill 설치, 충전, agent 안에서 사용입니다.",
        "overview_note": "이 컬렉션은 과장보다 구체적 근거를 우선합니다: 단계, reference video, agent/MCP 사용, 재현 조건, 명확한 한계.",
        "quick": "API 빠른 접근",
        "quick_text": "최종 landing 이 제공되기 전까지 Seedance reference-to-video 모델 경로를 기록합니다.",
        "pending": "전환 경로 대기 중",
        "pending_body": "최종 landing 은 아직 미정입니다. release-ready 로 표시하기 전에 이 섹션을 최종 CTA 로 교체하세요.",
        "menu": "메뉴",
        "ack": "감사의 말",
        "what": "보여주는 것",
        "case": "사례",
        "type": "Type",
        "date": "Date",
        "section": "섹션",
        "cases": "사례",
        "takeaway_prefix": "이 사례를 활용해",
        "notes_prefix": "소스 메모",
    },
    "de": {
        "intro": "Usecase-Repository für Blender + Seedance.",
        "value": "Wir sammeln reale Workflows mit Blender, Blender MCP, Viewport, Previs, FBX, Mixamo, ComfyUI und Agentensteuerung für Seedance-Videogenerierung.",
        "source": "Die aktuelle Sammlung stammt aus vom Owner bereitgestellten X/Twitter-Daten. Jeder Fall verlinkt Quelle und Creator-Profil.",
        "cta": "Die primäre Landingpage fehlt noch; der geplante Pfad ist MCP installieren, EvoLink Skill installieren, aufladen und im Agenten nutzen.",
        "overview_note": "Die Sammlung bevorzugt konkrete Evidenz: Schritte, Referenzvideos, Agent/MCP-Nutzung, reproduzierbare Bedingungen und klare Grenzen.",
        "quick": "Schneller API-Zugang",
        "quick_text": "Bis zur finalen Landingpage dokumentiert dieser Abschnitt den erwarteten Seedance reference-to-video Modellpfad.",
        "pending": "Conversion-Pfad ausstehend",
        "pending_body": "Die finale Landingpage steht noch aus. Ersetze diesen Abschnitt durch den finalen CTA, bevor das Repository als release-ready gilt.",
        "menu": "Menü",
        "ack": "Danksagung",
        "what": "Was es zeigt",
        "case": "Fall",
        "type": "Typ",
        "date": "Datum",
        "section": "Abschnitt",
        "cases": "Fälle",
        "takeaway_prefix": "Nutze diesen Fall, um",
        "notes_prefix": "Quellnotizen",
    },
    "fr": {
        "intro": "Dépôt de cas d'usage Blender + Seedance.",
        "value": "Nous réunissons des workflows réels avec Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI et agents pour contrôler la génération vidéo Seedance.",
        "source": "La collection actuelle vient des données X/Twitter fournies par le propriétaire. Chaque cas renvoie vers la source et le profil du créateur.",
        "cta": "La landing principale est en attente; le chemin prévu est installer MCP, installer la skill EvoLink, recharger, puis utiliser dans un agent.",
        "overview_note": "La collection privilégie les preuves concrètes: étapes, vidéos de référence, usage agent/MCP, contraintes reproductibles et limites explicites.",
        "quick": "Accès API rapide",
        "quick_text": "Cette section conserve le chemin attendu du modèle Seedance reference-to-video jusqu'à la landing finale.",
        "pending": "Chemin de conversion en attente",
        "pending_body": "La landing finale est encore en attente. Remplacez cette section par le CTA final avant de qualifier le dépôt de release-ready.",
        "menu": "Menu",
        "ack": "Remerciements",
        "what": "Ce que cela montre",
        "case": "Cas",
        "type": "Type",
        "date": "Date",
        "section": "Section",
        "cases": "Cas",
        "takeaway_prefix": "Utilisez ce cas pour",
        "notes_prefix": "Notes de source",
    },
    "tr": {
        "intro": "Blender + Seedance kullanım örnekleri deposu.",
        "value": "Seedance video üretimini kontrol etmek için Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI ve agent destekli gerçek iş akışlarını topluyoruz.",
        "source": "Mevcut koleksiyon, sahibin sağladığı X/Twitter verilerinden seçildi. Her vaka orijinal gönderiye ve yaratıcı profiline bağlanır.",
        "cta": "Ana landing sayfası beklemede; hedef yol MCP kurulumu, EvoLink skill kurulumu, bakiye yükleme ve agent içinde kullanımdır.",
        "overview_note": "Koleksiyon abartı yerine somut kanıtı öne çıkarır: adımlar, referans videolar, agent/MCP kullanımı, yeniden üretilebilir koşullar ve net sınırlar.",
        "quick": "Hızlı API erişimi",
        "quick_text": "Final landing gelene kadar bu bölüm Seedance reference-to-video model yolunu kaydeder.",
        "pending": "Dönüşüm yolu beklemede",
        "pending_body": "Final landing sayfası hâlâ beklemede. Depoyu release-ready saymadan önce bu bölümü final CTA ile değiştirin.",
        "menu": "Menü",
        "ack": "Teşekkür",
        "what": "Ne gösteriyor",
        "case": "Vaka",
        "type": "Tür",
        "date": "Tarih",
        "section": "Bölüm",
        "cases": "Vakalar",
        "takeaway_prefix": "Bu vakayı şunun için kullanın:",
        "notes_prefix": "Kaynak notları",
    },
    "zh-CN": {
        "intro": "Blender + Seedance 使用案例仓库。",
        "value": "这里收集真实的 Blender、Blender MCP、viewport、previs、FBX、Mixamo、ComfyUI 和 agent 辅助工作流，用来控制 Seedance 视频生成。",
        "source": "当前集合来自用户提供的 X/Twitter 精选数据。每个案例都链接到原帖和创作者主页。",
        "cta": "主落地页暂缺。预期转化路径是安装 MCP、安装 EvoLink skill、充值，然后在 Agent 里使用。",
        "overview_note": "这个集合优先保留具体证据：步骤、参考视频、agent/MCP 用法、可复现条件和明确限制，而不是空泛宣传。",
        "quick": "快速 API 入口",
        "quick_text": "在最终落地页提供之前，这里记录 Seedance reference-to-video 的预期模型路径。",
        "pending": "转化路径待补齐",
        "pending_body": "最终落地页仍待补齐。把仓库标记为 release-ready 之前，需要把这一节替换成最终 CTA。",
        "menu": "目录",
        "ack": "致谢",
        "what": "展示内容",
        "case": "案例",
        "type": "类型",
        "date": "日期",
        "section": "章节",
        "cases": "案例",
        "takeaway_prefix": "用这个案例来",
        "notes_prefix": "来源笔记",
    },
    "zh-TW": {
        "intro": "Blender + Seedance 使用案例倉庫。",
        "value": "這裡收集真實的 Blender、Blender MCP、viewport、previs、FBX、Mixamo、ComfyUI 和 agent 輔助工作流，用來控制 Seedance 影片生成。",
        "source": "目前集合來自使用者提供的 X/Twitter 精選資料。每個案例都連結到原帖和創作者主頁。",
        "cta": "主落地頁暫缺。預期轉化路徑是安裝 MCP、安裝 EvoLink skill、儲值，然後在 Agent 裡使用。",
        "overview_note": "這個集合優先保留具體證據：步驟、參考影片、agent/MCP 用法、可重現條件和明確限制，而不是空泛宣傳。",
        "quick": "快速 API 入口",
        "quick_text": "在最終落地頁提供之前，這裡記錄 Seedance reference-to-video 的預期模型路徑。",
        "pending": "轉化路徑待補齊",
        "pending_body": "最終落地頁仍待補齊。把倉庫標記為 release-ready 之前，需要把這一節替換成最終 CTA。",
        "menu": "目錄",
        "ack": "致謝",
        "what": "展示內容",
        "case": "案例",
        "type": "類型",
        "date": "日期",
        "section": "章節",
        "cases": "案例",
        "takeaway_prefix": "用這個案例來",
        "notes_prefix": "來源筆記",
    },
    "ru": {
        "intro": "Репозиторий use cases Blender + Seedance.",
        "value": "Мы собираем реальные workflow с Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI и агентами для управления генерацией видео Seedance.",
        "source": "Текущая коллекция основана на X/Twitter данных, предоставленных владельцем. Каждый кейс ведет к исходному посту и профилю автора.",
        "cta": "Основная landing page ожидается; планируемый путь: установить MCP, установить EvoLink skill, пополнить баланс и использовать внутри агента.",
        "overview_note": "Коллекция ставит конкретные доказательства выше хайпа: шаги, reference video, agent/MCP, воспроизводимые условия и явные ограничения.",
        "quick": "Быстрый доступ к API",
        "quick_text": "До финальной landing page этот раздел фиксирует ожидаемый путь модели Seedance reference-to-video.",
        "pending": "Путь конверсии ожидается",
        "pending_body": "Финальная landing page пока ожидается. Замените этот раздел финальным CTA перед статусом release-ready.",
        "menu": "Меню",
        "ack": "Благодарности",
        "what": "Что показывает",
        "case": "Кейс",
        "type": "Тип",
        "date": "Дата",
        "section": "Раздел",
        "cases": "Кейсы",
        "takeaway_prefix": "Используйте этот кейс, чтобы",
        "notes_prefix": "Заметки источника",
    },
}


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def date_only(value: str) -> str:
    return value[:10]


def zh_tw(text: str) -> str:
    replacements = {
        "预": "預",
        "帧": "幀",
        "参考": "參考",
        "视频": "影片",
        "导": "導",
        "现": "現",
        "复": "複",
        "语": "語",
        "条": "條",
        "输": "輸",
        "个": "個",
        "对": "對",
        "话": "話",
        "镜": "鏡",
        "场": "場",
        "实": "實",
        "际": "際",
        "验": "驗",
        "发": "發",
        "动": "動",
        "节": "節",
        "问": "問",
        "题": "題",
        "连": "連",
        "试": "試",
        "猫": "貓",
        "鱼": "魚",
        "简": "簡",
        "写": "寫",
        "图": "圖",
        "摄": "攝",
        "览": "覽",
        "转": "轉",
        "构": "構",
        "组": "組",
    }
    for src, dst in replacements.items():
        text = text.replace(src, dst)
    return text


def local_case_title(item: dict, index: int, lang: str) -> str:
    if lang == "zh-CN":
        return item.get("use_case_title_zh") or EN_TITLES[index]
    if lang == "zh-TW":
        return zh_tw(item.get("use_case_title_zh") or EN_TITLES[index])
    return EN_TITLES[index]


def usage_takeaway(item: dict, index: int, lang: str) -> str:
    title = local_case_title(item, index, lang)
    if lang == "en":
        return f"Use this case to adapt {title.lower()} into a Blender-guided Seedance workflow."
    if lang in {"zh-CN", "zh-TW"}:
        verb = LOCALE[lang]["takeaway_prefix"]
        return f"{verb}把「{title}」改造成 Blender 参考视频驱动的 Seedance 工作流。"
    prefix = LOCALE[lang]["takeaway_prefix"]
    return f"{prefix} adapt '{title}' into a Blender-guided Seedance workflow."


def source_notes(item: dict, index: int, lang: str) -> str:
    why = clean(item.get("why_selected_zh", ""))
    reuse = clean(item.get("reuse_angle_zh", ""))
    source_text = clean(item.get("text", ""))
    short_source = source_text[:260].rsplit(" ", 1)[0] + ("..." if len(source_text) > 260 else "")
    if lang == "zh-CN":
        return f"- {LOCALE[lang]['notes_prefix']}：{why}\n- 复用角度：{reuse}"
    if lang == "zh-TW":
        return f"- {LOCALE[lang]['notes_prefix']}：{zh_tw(why)}\n- 複用角度：{zh_tw(reuse)}"
    return (
        f"- {LOCALE[lang]['notes_prefix']}: curated because the source describes a concrete Blender + Seedance workflow rather than a generic showcase.\n"
        f"- Reuse angle: {reuse}\n"
        f"- Context summary: {short_source}"
    )


def author_link(item: dict) -> str:
    username = item["author"]["username"]
    return f"https://x.com/{username}"


def curated_records(items: list[dict]) -> list[dict]:
    records = []
    staged = []
    for source_idx, item in enumerate(items, 1):
        cat = CATEGORY_FOR_CASE[source_idx]
        staged.append((cat, source_idx, item))
    order = {cat: pos for pos, cat in enumerate(CATEGORY_META)}
    staged.sort(key=lambda entry: (order[entry[0]], entry[1]))
    for idx, (cat, source_idx, item) in enumerate(staged, 1):
        records.append(
            {
                "case": idx,
                "source_index": source_idx,
                "id": item["id"],
                "url": item["url"],
                "author": f"@{item['author']['username']}",
                "author_url": author_link(item),
                "date": date_only(item["created_at_iso"]),
                "category": cat,
                "category_name": CATEGORY_META[cat][1],
                "title": EN_TITLES[source_idx],
                "title_zh": item.get("use_case_title_zh"),
                "evidence_type": TYPE_FOR_CATEGORY[cat],
                "quality_tier": item.get("tier"),
                "source_role": item.get("source_role"),
                "why_selected_zh": item.get("why_selected_zh"),
                "reuse_angle_zh": item.get("reuse_angle_zh"),
                "source_text": item.get("text"),
            }
        )
    return records


def render_badges(img_path: str) -> str:
    return f"""<div align="center">

<a href="{CTA_ANCHOR}"><img src="{img_path}" alt="Blender + Seedance usecase repository banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Use on EvoLink](https://img.shields.io/badge/Use_on-EvoLink-black)]({CTA_ANCHOR})
[![MCP + Skill](https://img.shields.io/badge/MCP_%2B_Skill-Pending-orange)]({CTA_ANCHOR})
[![Agent Workflow](https://img.shields.io/badge/Agent_Workflow-Pending-blue)]({CTA_ANCHOR})

{LANG_BADGES}

</div>"""


def render_intro(labels: dict) -> str:
    return f"""## 🍌 Introduction

{labels["intro"]}

**{labels["value"]}**

{labels["source"]}

{labels["cta"]}"""


def render_overview(labels: dict, records: list[dict]) -> str:
    return f"""## 📊 Overview

- **{len(records)} selected Blender + Seedance cases** from public creator posts in the owner-provided source dataset.
- Covers camera control, Blender previs, multi-character blocking, action choreography, Blender MCP, Codex/Claude-assisted blockouts, FBX/Mixamo references, ComfyUI/style transfer, and known limitations.
- Each case includes the original source, creator attribution, a concise takeaway, evidence type, and publication date.
- Use this repo to inspect practical workflows before routing users to the final EvoLink MCP + skill landing page.

> [!NOTE]
> {labels["overview_note"]}"""


def render_quick(labels: dict) -> str:
    return f"""<a id="-quick-api-access"></a>
## ⚡ {labels["quick"]}

{labels["quick_text"]}

```bash
curl --request POST \\
  --url https://direct.evolink.ai/v1/messages \\
  --header 'Authorization: Bearer <token>' \\
  --header 'Content-Type: application/json' \\
  --data '
{{
  "model": "{MODEL_ID}",
  "max_tokens": 1024,
  "messages": [
    {{
      "role": "user",
      "content": "Plan a Blender reference-video workflow for a Seedance shot."
    }}
  ]
}}
'
```

<a id="conversion-path-pending"></a>
## 🚧 {labels["pending"]}

{labels["pending_body"]}"""


def grouped_records(records: list[dict]) -> dict[str, list[dict]]:
    grouped = defaultdict(list)
    for record in records:
        grouped[record["category"]].append(record)
    return dict(grouped)


def render_menu(labels: dict, records: list[dict], lang: str) -> str:
    grouped = grouped_records(records)
    lines = [
        f"## 📑 {labels['menu']}",
        "",
        f"| {labels['section']} | {labels['cases']} |",
        "|---|---|",
    ]
    for cat, recs in grouped.items():
        emoji, name = CATEGORY_META[cat]
        lines.append(f"| [{emoji} {name}](#{slug(name)}) | Case {recs[0]['case']}-{recs[-1]['case']} |")
    lines.append(f"| [🙏 {labels['ack']}](#acknowledge) | Credits and correction policy |")
    lines.append("")
    for cat, recs in grouped.items():
        emoji, name = CATEGORY_META[cat]
        lines.extend(
            [
                f"### [{emoji} {name}](#{slug(name)})",
                "",
                f"| {labels['case']} | {labels['what']} | {labels['type']} |",
                "|---|---|---|",
            ]
        )
        for rec in recs:
            item = source_items()[rec["source_index"] - 1]
            title = local_case_title(item, rec["source_index"], lang)
            lines.append(f"| [{title}](#case-{rec['case']}) | {usage_takeaway(item, rec['source_index'], lang).strip('*')} | {rec['evidence_type']} |")
        lines.append("")
    return "\n".join(lines).rstrip()


_SOURCE_ITEMS_CACHE = None


def source_items() -> list[dict]:
    global _SOURCE_ITEMS_CACHE
    if _SOURCE_ITEMS_CACHE is None:
        _SOURCE_ITEMS_CACHE = json.loads(SOURCE.read_text())["items"]
    return _SOURCE_ITEMS_CACHE


def render_cases(labels: dict, items: list[dict], lang: str) -> str:
    grouped = grouped_records(curated_records(items))
    chunks = []
    for cat, recs in grouped.items():
        emoji, name = CATEGORY_META[cat]
        chunks.append(f"## {emoji} {name}")
        chunks.append("")
        for rec in recs:
            idx = rec["case"]
            source_idx = rec["source_index"]
            item = items[source_idx - 1]
            title = local_case_title(item, source_idx, lang)
            author = item["author"]["username"]
            chunks.extend(
                [
                    f'<a id="case-{idx}"></a>',
                    f"### Case {idx}: [{title}]({item['url']}) (by [@{author}]({author_link(item)}))",
                    "",
                    f"**{usage_takeaway(item, source_idx, lang)}**",
                    "",
                    source_notes(item, source_idx, lang),
                    "",
                    f"{labels['type']}: {rec['evidence_type']} | {labels['date']}: {rec['date']}",
                    "",
                    "---",
                    "",
                ]
            )
    return "\n".join(chunks).rstrip()


def render_ack(labels: dict, records: list[dict]) -> str:
    creators = []
    seen = set()
    for record in records:
        if record["author"] not in seen:
            seen.add(record["author"])
            creators.append(f"- [{record['author']}]({record['author_url']})")
    return f"""<a id="acknowledge"></a>
## 🙏 {labels["ack"]}

This repository was inspired by creators who publicly shared Blender + Seedance workflows, tests, prompts, reference videos, and production notes.

{chr(10).join(creators)}

*We cannot guarantee that every case is attributed to the original creator. If anything needs to be corrected, please contact us and we will update it.*

If you have more interesting usage cases to share, open an issue or pull request and help expand the EvoLink usecase library.

[![Star History Chart](https://api.star-history.com/svg?repos={OWNER}/{REPO}&type=Date)](https://www.star-history.com/#{OWNER}/{REPO}&Date)"""


def render_readme(lang: str, filename: str, img_path: str, items: list[dict], records: list[dict]) -> str:
    labels = LOCALE[lang]
    parts = [
        render_badges(img_path),
        render_intro(labels),
        render_overview(labels, records),
        render_quick(labels),
        render_menu(labels, records, lang),
        render_cases(labels, items, lang),
        render_ack(labels, records),
        "",
    ]
    return "\n\n".join(parts)


def render_curated_md(records: list[dict]) -> str:
    lines = [
        "# Blender + Seedance Curated Use Cases",
        "",
        f"Generated: {datetime.utcnow().replace(microsecond=0).isoformat()}Z",
        f"Cases: {len(records)}",
        "",
        "| Case | Title | Source | Author | Category | Type | Date |",
        "|---|---|---|---|---|---|---|",
    ]
    for record in records:
        lines.append(
            f"| {record['case']} | {record['title']} | [source]({record['url']}) | [{record['author']}]({record['author_url']}) | {record['category_name']} | {record['evidence_type']} | {record['date']} |"
        )
    lines.append("")
    return "\n".join(lines)


def write_banner(path: Path, lang_name: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (1520, 760), "#111827")
    draw = ImageDraw.Draw(img)
    for y in range(760):
        r = int(17 + y * 0.05)
        g = int(24 + y * 0.04)
        b = int(39 + y * 0.08)
        draw.line((0, y, 1520, y), fill=(r, g, b))
    draw.rectangle((86, 86, 1434, 674), outline="#38bdf8", width=4)
    draw.rectangle((116, 116, 1404, 644), outline="#f97316", width=2)
    try:
        font_big = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 78)
        font_mid = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 40)
        font_small = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", 30)
    except Exception:
        font_big = font_mid = font_small = ImageFont.load_default()
    draw.text((150, 205), "Blender + Seedance", fill="#f8fafc", font=font_big)
    draw.text((154, 315), "Curated use cases for agent-guided video workflows", fill="#bae6fd", font=font_mid)
    draw.text((154, 395), f"{lang_name} edition · MCP · Skill · Agent workflow", fill="#fed7aa", font=font_small)
    draw.text((154, 505), "Previs · Viewport · FBX · Mixamo · ComfyUI · Blender MCP", fill="#e5e7eb", font=font_small)
    img.save(path)


def write_static_files(records: list[dict]) -> None:
    (ROOT / ".gitignore").write_text(
        "\n".join(
            [
                ".DS_Store",
                "__pycache__/",
                "*.pyc",
                ".env",
                ".env.*",
                "node_modules/",
                ".codex/",
                "data/x-search/raw/",
                "data/x-search/*/raw/",
                "",
            ]
        )
    )
    (ROOT / "LICENSE").write_text(
        textwrap.dedent(
            """\
            Creative Commons Attribution 4.0 International

            This repository contains curated summaries and links to public source posts.
            Source posts, images, videos, trademarks, and creator materials remain owned by their respective creators.

            You are free to share and adapt this curated repository content with attribution to EvoLink and the original source creators where applicable.
            """
        )
    )
    (ROOT / "CONTRIBUTING.md").write_text(
        textwrap.dedent(
            """\
            # Contributing

            Contributions should add source-backed Blender + Seedance cases only.

            Required metadata:

            - Original source URL
            - Creator handle and profile URL
            - Publication date when available
            - Evidence type: Demo, Tutorial, Evaluation, Integration, Benchmark, or Limit
            - A concise usage takeaway
            - Source-grounded notes without invented prompts or results

            Do not add raw private exports, unpublished media, or copied long post text.
            """
        )
    )
    (ROOT / "docs" / "maintenance.md").write_text(
        textwrap.dedent(
            f"""\
            # Maintenance

            ## Source of Truth

            - Public curated source: `blender-seedance-usecase-curated.json`
            - Human-readable curated source: `blender-seedance-usecase-curated.md`
            - Owner-provided input: `data/primary-use-case-posts.json`

            ## Current State

            - Selected public cases: {len(records)}
            - Primary CTA: pending owner-provided landing page
            - Public push: not approved
            - GitHub repository creation: not approved; push target approved after local verification

            ## Case Rules

            Each public case must include:

            - Stable `<a id="case-x"></a>` anchor
            - Source-linked `### Case X` heading
            - Creator attribution
            - Bold usage takeaway
            - Source-grounded notes
            - `Type: ... | Date: YYYY-MM-DD`

            Never invent prompts, results, benchmark claims, availability, pricing, or creator attribution.

            ## Validation

            ```bash
            python3 scripts/verify_repo.py
            git diff --check
            ```

            ## Release Blockers

            Replace `#conversion-path-pending` with the final landing page before claiming release-ready. The landing page should explain MCP installation, EvoLink skill installation, recharge, and agent usage.
            """
        )
    )
    (ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md").write_text(
        textwrap.dedent(
            """\
            ## Source-backed case checklist

            - [ ] Original source URL is included.
            - [ ] Creator profile is included.
            - [ ] Date is present or explicitly unavailable.
            - [ ] Evidence type is one of Demo, Tutorial, Evaluation, Integration, Benchmark, or Limit.
            - [ ] No prompt, result, benchmark, price, or API claim is invented.

            ## Localization checklist

            - [ ] All 11 README files keep the same case count.
            - [ ] All case anchors remain `#case-x`.
            - [ ] Source URLs and creator URLs match the English source.

            ## Validation

            - [ ] `python3 scripts/verify_repo.py`
            - [ ] `git diff --check`
            """
        )
    )


def write_verify_script(records: list[dict]) -> None:
    script = f'''#!/usr/bin/env python3
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FILES = {[filename for _, filename, _, _ in LANGS]!r}
EXPECTED_CASES = {len(records)}
EXPECTED_IMAGES = {[img for _, _, _, img in LANGS]!r}

def fail(msg):
    raise SystemExit(f"FAIL: {{msg}}")

for file in FILES:
    p = ROOT / file
    if not p.exists():
        fail(f"missing {{file}}")
    text = p.read_text()
    anchors = re.findall(r'^<a id="case-([0-9]+)"></a>', text, re.M)
    heads = re.findall(r'^### Case ([0-9]+): \\[', text, re.M)
    if len(anchors) != EXPECTED_CASES:
        fail(f"{{file}} has {{len(anchors)}} anchors, expected {{EXPECTED_CASES}}")
    if anchors != heads:
        fail(f"{{file}} anchors and case headings differ")
    if anchors != [str(i) for i in range(1, EXPECTED_CASES + 1)]:
        fail(f"{{file}} anchors are not contiguous")
    if "## 📊" not in text or "## ⚡" not in text or "## 📑" not in text or "## 🙏" not in text:
        fail(f"{{file}} missing required usecase sections")
    if text.count("| Date: ") + text.count("| Fecha: ") + text.count("| Data: ") + text.count("| Datum: ") + text.count("| Tarih: ") + text.count("| 日期: ") + text.count("| Дата: ") < EXPECTED_CASES:
        fail(f"{{file}} missing Type/Date metadata lines")

for img in EXPECTED_IMAGES:
    if not (ROOT / img).exists():
        fail(f"missing {{img}}")

for required in ["LICENSE", "CONTRIBUTING.md", "docs/maintenance.md", ".github/PULL_REQUEST_TEMPLATE.md", "blender-seedance-usecase-curated.json", "blender-seedance-usecase-curated.md"]:
    if not (ROOT / required).exists():
        fail(f"missing {{required}}")

print(f"PASS: {{len(FILES)}} README files, {{EXPECTED_CASES}} cases each, required assets present")
'''
    path = ROOT / "scripts" / "verify_repo.py"
    path.write_text(script)
    path.chmod(0o755)


def main() -> None:
    data = json.loads(SOURCE.read_text())
    items = data["items"]
    records = curated_records(items)
    for _, _, lang_name, img in LANGS:
        write_banner(ROOT / img, lang_name)
    for lang, filename, _, img in LANGS:
        (ROOT / filename).write_text(render_readme(lang, filename, img, items, records))
    curated = {
        "metadata": {
            "generated_at": datetime.utcnow().replace(microsecond=0).isoformat() + "Z",
            "source": str(SOURCE.relative_to(ROOT)),
            "repo": REPO,
            "selected_count": len(records),
            "tier_counts": dict(Counter(record["quality_tier"] for record in records)),
            "category_counts": dict(Counter(record["category"] for record in records)),
            "cta_status": "pending owner-provided landing page",
            "publication_status": "local scaffold; push to cheercheung/Awesome-Blender-Seedance-Workflow-Usecases approved after local verification; no remote creation approved",
        },
        "items": records,
    }
    (ROOT / "blender-seedance-usecase-curated.json").write_text(json.dumps(curated, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "blender-seedance-usecase-curated.md").write_text(render_curated_md(records))
    write_static_files(records)
    write_verify_script(records)


if __name__ == "__main__":
    main()
