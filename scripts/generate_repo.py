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

CATEGORY_DISPLAY = {
    "en": {
        "camera-control": "Camera Control & Previs",
        "character-action": "Character & Action Blocking",
        "agentic-mcp": "Agentic Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping",
        "production-pipeline": "Production Pipelines & Toolchains",
        "limitations": "Limits, Tests & Troubleshooting",
    },
    "es": {
        "camera-control": "Camera Control & Previs / Control de cámara y previs",
        "character-action": "Character & Action Blocking / Bloqueo de personajes y acción",
        "agentic-mcp": "Agentic Blender MCP / Blender MCP con agentes",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / Referencias, prompts y entradas múltiples",
        "production-pipeline": "Production Pipelines & Toolchains / Pipelines y herramientas de producción",
        "limitations": "Limits, Tests & Troubleshooting / Límites, pruebas y diagnóstico",
    },
    "pt": {
        "camera-control": "Camera Control & Previs / Controle de câmera e previs",
        "character-action": "Character & Action Blocking / Bloqueio de personagens e ação",
        "agentic-mcp": "Agentic Blender MCP / Blender MCP com agentes",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / Referências, prompts e múltiplas entradas",
        "production-pipeline": "Production Pipelines & Toolchains / Pipelines e ferramentas de produção",
        "limitations": "Limits, Tests & Troubleshooting / Limites, testes e diagnóstico",
    },
    "ja": {
        "camera-control": "Camera Control & Previs / カメラ制御とプリビズ",
        "character-action": "Character & Action Blocking / キャラクターとアクションのブロッキング",
        "agentic-mcp": "Agentic Blender MCP / エージェント型 Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / 参照、プロンプト、複数入力の対応付け",
        "production-pipeline": "Production Pipelines & Toolchains / 制作パイプラインとツールチェーン",
        "limitations": "Limits, Tests & Troubleshooting / 制限、検証、トラブルシュート",
    },
    "ko": {
        "camera-control": "Camera Control & Previs / 카메라 제어와 프리비즈",
        "character-action": "Character & Action Blocking / 캐릭터와 액션 블로킹",
        "agentic-mcp": "Agentic Blender MCP / 에이전트 기반 Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / 레퍼런스, 프롬프트, 다중 입력 매핑",
        "production-pipeline": "Production Pipelines & Toolchains / 제작 파이프라인과 툴체인",
        "limitations": "Limits, Tests & Troubleshooting / 한계, 테스트, 문제 해결",
    },
    "de": {
        "camera-control": "Camera Control & Previs / Kamerasteuerung und Previs",
        "character-action": "Character & Action Blocking / Figuren- und Action-Blocking",
        "agentic-mcp": "Agentic Blender MCP / Agentisches Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / Referenzen, Prompts und Multi-Input-Mapping",
        "production-pipeline": "Production Pipelines & Toolchains / Produktionspipelines und Toolchains",
        "limitations": "Limits, Tests & Troubleshooting / Grenzen, Tests und Fehlersuche",
    },
    "fr": {
        "camera-control": "Camera Control & Previs / Contrôle caméra et prévisualisation",
        "character-action": "Character & Action Blocking / Blocking personnages et action",
        "agentic-mcp": "Agentic Blender MCP / Blender MCP avec agents",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / Références, prompts et entrées multiples",
        "production-pipeline": "Production Pipelines & Toolchains / Pipelines et outils de production",
        "limitations": "Limits, Tests & Troubleshooting / Limites, tests et dépannage",
    },
    "tr": {
        "camera-control": "Camera Control & Previs / Kamera kontrolü ve previs",
        "character-action": "Character & Action Blocking / Karakter ve aksiyon blocking",
        "agentic-mcp": "Agentic Blender MCP / Agent destekli Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / Referans, prompt ve çoklu girdi eşleme",
        "production-pipeline": "Production Pipelines & Toolchains / Üretim pipeline'ları ve araç zinciri",
        "limitations": "Limits, Tests & Troubleshooting / Sınırlar, testler ve sorun giderme",
    },
    "zh-CN": {
        "camera-control": "Camera Control & Previs / 相机控制与预演",
        "character-action": "Character & Action Blocking / 角色与动作 blocking",
        "agentic-mcp": "Agentic Blender MCP / Agent 辅助 Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / 参考、prompt 与多输入映射",
        "production-pipeline": "Production Pipelines & Toolchains / 生产管线与工具链",
        "limitations": "Limits, Tests & Troubleshooting / 限制、测试与排查",
    },
    "zh-TW": {
        "camera-control": "Camera Control & Previs / 相機控制與預演",
        "character-action": "Character & Action Blocking / 角色與動作 blocking",
        "agentic-mcp": "Agentic Blender MCP / Agent 輔助 Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / 參考、prompt 與多輸入映射",
        "production-pipeline": "Production Pipelines & Toolchains / 生產管線與工具鏈",
        "limitations": "Limits, Tests & Troubleshooting / 限制、測試與排查",
    },
    "ru": {
        "camera-control": "Camera Control & Previs / Управление камерой и превиз",
        "character-action": "Character & Action Blocking / Блокинг персонажей и экшена",
        "agentic-mcp": "Agentic Blender MCP / Агентный Blender MCP",
        "reference-prompt": "Reference, Prompt & Multi-Input Mapping / Референсы, промпты и multi-input mapping",
        "production-pipeline": "Production Pipelines & Toolchains / Производственные пайплайны и инструменты",
        "limitations": "Limits, Tests & Troubleshooting / Ограничения, тесты и разбор ошибок",
    },
}

OVERVIEW_LINES = {
    "en": [
        "**{count} selected Blender + Seedance cases** from public creator posts in the owner-provided source dataset.",
        "Covers camera control, Blender previs, multi-character blocking, action choreography, Blender MCP, Codex/Claude-assisted blockouts, FBX/Mixamo references, ComfyUI/style transfer, and known limitations.",
        "Each case includes the original source, creator attribution, a concise takeaway, evidence type, and publication date.",
        "The public list was reduced from 35 candidates to 20 primary cases after manual duplicate and originality review.",
        "Use this repo to inspect practical workflows before routing users to the final EvoLink MCP + skill landing page.",
    ],
    "es": [
        "**{count} casos Blender + Seedance seleccionados** a partir de publicaciones públicas de creadores en el dataset proporcionado por el propietario.",
        "Cubre control de cámara, previs en Blender, blocking de varios personajes, coreografía de acción, Blender MCP, blockouts asistidos por Codex/Claude, referencias FBX/Mixamo, ComfyUI/style transfer y límites conocidos.",
        "Cada caso incluye fuente original, atribución al creador, aprendizaje breve, tipo de evidencia y fecha de publicación.",
        "La lista pública se redujo de 35 candidatos a 20 casos primarios tras una revisión manual de duplicados y originalidad.",
        "Usa este repo para revisar workflows prácticos antes de enviar usuarios a la landing final de EvoLink MCP + skill.",
    ],
    "pt": [
        "**{count} casos Blender + Seedance selecionados** a partir de posts públicos de criadores no dataset fornecido pelo proprietário.",
        "Cobre controle de câmera, previs no Blender, blocking de múltiplos personagens, coreografia de ação, Blender MCP, blockouts assistidos por Codex/Claude, referências FBX/Mixamo, ComfyUI/style transfer e limites conhecidos.",
        "Cada caso inclui fonte original, crédito ao criador, resumo acionável, tipo de evidência e data de publicação.",
        "A lista pública foi reduzida de 35 candidatos para 20 casos primários após revisão manual de duplicidade e originalidade.",
        "Use este repo para avaliar workflows práticos antes de direcionar usuários à landing final de EvoLink MCP + skill.",
    ],
    "ja": [
        "**{count} 件の Blender + Seedance ケース** を、所有者提供の公開クリエイター投稿データから選定しました。",
        "カメラ制御、Blender previs、複数キャラクターのブロッキング、アクション設計、Blender MCP、Codex/Claude 支援 blockout、FBX/Mixamo 参照、ComfyUI/style transfer、既知の制限を扱います。",
        "各ケースには元ソース、作者クレジット、短い要点、証拠タイプ、公開日を含めています。",
        "公開リストは、重複とオリジナリティの手動レビュー後に 35 件から 20 件へ絞りました。",
        "最終的な EvoLink MCP + skill landing に誘導する前に、実用 workflow を確認するための repo です。",
    ],
    "ko": [
        "소유자가 제공한 공개 제작자 게시물 데이터에서 **{count}개의 Blender + Seedance 사례**를 선별했습니다.",
        "카메라 제어, Blender 프리비즈, 다중 캐릭터 블로킹, 액션 안무, Blender MCP, Codex/Claude 지원 blockout, FBX/Mixamo 레퍼런스, ComfyUI/style transfer, 알려진 한계를 다룹니다.",
        "각 사례에는 원본 출처, 제작자 표기, 간단한 takeaway, 증거 유형, 게시일이 포함됩니다.",
        "공개 목록은 중복성과 원작성 수동 검토를 거쳐 35개 후보에서 20개 주요 사례로 줄였습니다.",
        "최종 EvoLink MCP + skill 랜딩으로 보내기 전에 실제 workflow를 검토하기 위한 repo입니다.",
    ],
    "de": [
        "**{count} ausgewählte Blender + Seedance Fälle** aus öffentlichen Creator-Posts im vom Owner bereitgestellten Datensatz.",
        "Behandelt Kamerasteuerung, Blender-Previs, Multi-Character-Blocking, Action-Choreografie, Blender MCP, Codex/Claude-gestützte Blockouts, FBX/Mixamo-Referenzen, ComfyUI/style transfer und bekannte Grenzen.",
        "Jeder Fall enthält Originalquelle, Creator-Zuordnung, kompaktes Takeaway, Evidenztyp und Veröffentlichungsdatum.",
        "Die öffentliche Liste wurde nach manueller Prüfung auf Duplikate und Originalität von 35 Kandidaten auf 20 Primärfälle reduziert.",
        "Nutze dieses Repo, um praktische Workflows zu prüfen, bevor Nutzer zur finalen EvoLink MCP + Skill Landingpage geführt werden.",
    ],
    "fr": [
        "**{count} cas Blender + Seedance sélectionnés** depuis des publications publiques de créateurs dans le dataset fourni par le propriétaire.",
        "Couvre contrôle caméra, previs Blender, blocking multi-personnages, chorégraphie d'action, Blender MCP, blockouts assistés par Codex/Claude, références FBX/Mixamo, ComfyUI/style transfer et limites connues.",
        "Chaque cas inclut la source originale, l'attribution créateur, un résumé exploitable, le type de preuve et la date de publication.",
        "La liste publique a été réduite de 35 candidats à 20 cas principaux après revue manuelle des doublons et de l'originalité.",
        "Utilisez ce repo pour examiner des workflows pratiques avant de diriger les utilisateurs vers la landing EvoLink MCP + skill finale.",
    ],
    "tr": [
        "Sahibin sağladığı herkese açık creator postlarından **{count} Blender + Seedance vakası** seçildi.",
        "Kamera kontrolü, Blender previs, çok karakterli blocking, aksiyon koreografisi, Blender MCP, Codex/Claude destekli blockout'lar, FBX/Mixamo referansları, ComfyUI/style transfer ve bilinen sınırları kapsar.",
        "Her vaka orijinal kaynak, creator atfı, kısa takeaway, kanıt tipi ve yayın tarihini içerir.",
        "Herkese açık liste, manuel tekrar ve özgünlük incelemesinden sonra 35 adaydan 20 ana vakaya indirildi.",
        "Bu repo, kullanıcıları final EvoLink MCP + skill landing sayfasına yönlendirmeden önce pratik workflow'ları incelemek içindir.",
    ],
    "zh-CN": [
        "**{count} 个精选 Blender + Seedance 案例**，来自用户提供数据集中公开创作者帖子。",
        "覆盖相机控制、Blender previs、多角色 blocking、动作编排、Blender MCP、Codex/Claude 辅助 blockout、FBX/Mixamo 参考、ComfyUI/style transfer 和已知限制。",
        "每个案例都包含原始来源、创作者署名、简明 takeaway、证据类型和发布日期。",
        "公开列表已经过人工重复与原创性审计，从 35 个候选收敛为 20 个主案例。",
        "这个仓库用于先展示真实工作流，再把用户引导到最终 EvoLink MCP + skill 落地页。",
    ],
    "zh-TW": [
        "**{count} 個精選 Blender + Seedance 案例**，來自使用者提供資料集中公開創作者貼文。",
        "涵蓋相機控制、Blender previs、多角色 blocking、動作編排、Blender MCP、Codex/Claude 輔助 blockout、FBX/Mixamo 參考、ComfyUI/style transfer 和已知限制。",
        "每個案例都包含原始來源、創作者署名、簡明 takeaway、證據類型和發布日期。",
        "公開列表已經過人工重複與原創性審計，從 35 個候選收斂為 20 個主案例。",
        "這個倉庫用於先展示真實工作流，再把使用者引導到最終 EvoLink MCP + skill 落地頁。",
    ],
    "ru": [
        "**{count} отобранных кейсов Blender + Seedance** из публичных постов авторов в датасете владельца.",
        "Охватывает управление камерой, Blender previs, блокинг нескольких персонажей, постановку экшена, Blender MCP, blockout с Codex/Claude, FBX/Mixamo references, ComfyUI/style transfer и известные ограничения.",
        "Каждый кейс содержит исходный пост, автора, краткий вывод, тип доказательства и дату публикации.",
        "Публичный список был сокращен с 35 кандидатов до 20 основных кейсов после ручной проверки дубликатов и оригинальности.",
        "Этот repo помогает изучить реальные workflows перед переходом к финальной landing page EvoLink MCP + skill.",
    ],
}

SELECTED_SOURCE_INDICES = [
    1,
    2,
    3,
    5,
    6,
    7,
    8,
    9,
    10,
    14,
    19,
    20,
    21,
    23,
    24,
    25,
    28,
    29,
    31,
    32,
]

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

EN_TAKEAWAYS = {
    1: "A complete direction workflow: create a start frame, block the shot with gray boxes in Blender, animate only the camera and timing, then use that blockout as Seedance's motion reference.",
    2: "A compact precision-camera recipe: Blender supplies the camera move, Midjourney supplies the start frame, and Seedance follows the motion reference.",
    3: "A dialogue-shot workflow where Blender is used to match character poses and camera motion before Seedance generates the performed scene.",
    5: "An action-previs case showing how rough timing, speed, camera shake, and spatial choreography can be planned in Blender before Seedance renders the shot.",
    6: "A handheld-follow case where Blender controls how a character travels through space and Seedance carries the gritty camera move into the final video.",
    7: "A reproducible prompt case with the start frame, Blender reference video, Seedance version, duration, and movement constraints all spelled out.",
    8: "A limitation case: Blender successfully controls camera, rhythm, and subject path, while natural foot motion still needs better handling.",
    9: "An agentic Blender MCP case where Codex builds a simple 3D market, cat motion, camera framing, and an MP4 reference for Seedance.",
    10: "A reference-mapping case that uses Blender blocking plus multiple character and environment references to tell Seedance which figure should become which character.",
    14: "A ComfyUI control case where Blender previz is combined with separate upright and upside-down reference frames to test motion adherence.",
    19: "A tactical blocking case where Blender directs camera orbit, lens choice, cover positions, gunfire beats, and character movement before generation.",
    20: "A multi-tool agent pipeline where Hermes installs and connects Krea, ComfyUI, Blender MCP, and Seedance to produce both image and physical references.",
    21: "A viewport-to-style-transfer case: Blender MCP provides camera and element control, then Seedance/Magnific add texture and lighting.",
    23: "A beginner-friendly motion-source case: use Mixamo motion in Blender as the controllable movement base before sending the reference to Seedance.",
    24: "A Codex-assisted beginner case where architecture and camera work are generated in Blender and then tested as Seedance reference motion.",
    25: "A 3D-previs-to-anime case showing how camera moves and motion can be preserved while Seedance changes the render style.",
    28: "A short viewport-preview tutorial: block out the scene, export the preview, turn the first frame realistic, then provide both references to Seedance.",
    29: "An FBX clay-pass workflow where Blender imports the motion, Claude helps keyframe camera moves, and the rendered pass becomes Seedance reference video.",
    31: "A no-start-frame variant showing that Blender blockout plus detailed environment references can work when the workflow cannot rely on a starter frame.",
    32: "A style/world-variation case where the same Blender reference video drives different generated worlds in Seedance.",
}

EN_NOTES = {
    1: "The post describes the whole loop from image-model start frame to crude Blender camera blockout and Seedance motion-reference generation.",
    2: "The source gives a clear three-step workflow and reports that the generated video tracks the Blender camera move closely.",
    3: "The source adds multi-character dialogue and pose matching, making it distinct from single-character camera-control demos.",
    5: "The source focuses on action timing, speed, rough camera shake, and spatial choreography rather than only camera path.",
    6: "The source moves the character through the scene while the camera follows, which makes it useful for handheld movement shots.",
    7: "The post includes setup conditions and prompt constraints, so it can be reused as a reproducible reference-video case.",
    8: "This is kept as a troubleshooting case because it names what Blender controlled well and where the motion still failed.",
    9: "The author says the test was inspired by another creator, but the described scene, motion, camera, and export process are their own experiment.",
    10: "The source explains how to pair a blocking reference with multiple still references so Seedance maps the moving figures correctly.",
    14: "The case is useful because it combines Blender previz with multiple still references inside a ComfyUI-style control setup.",
    19: "The source shows simultaneous camera and character blocking, which is stronger than a simple camera-only reference.",
    20: "The case demonstrates a broader agent-built creative stack, not just manual Blender previs.",
    21: "This is the stronger techhalla source because it explains the viewport animation and downstream style/lighting step.",
    23: "The source is useful for beginners because it names Mixamo as a practical motion source for Blender reference videos.",
    24: "The post is valuable as a beginner Codex workflow: the user delegates architecture and camera work to Codex before Seedance.",
    25: "The source directly frames the workflow as Blender 3D previz transformed into an anime render while keeping camera motion.",
    28: "The post gives a concise workflow with concrete artifacts: viewport preview, first-frame image, and Seedance reference video.",
    29: "The source gives a specific FBX-to-clay-pass process and includes camera keyframing before reference export.",
    31: "This case covers an important variant where reference images replace the usual start-frame dependency.",
    32: "The source is useful because it separates motion control from world/style variation using the same reference video.",
}

ZH_TAKEAWAYS = {
    1: "完整导演流程：先做起始帧，再用 Blender 灰盒搭镜头、只动画相机和节奏，最后把 blockout 作为 Seedance motion reference。",
    2: "精确运镜的三步配方：Blender 负责相机运动，Midjourney 负责起始帧，Seedance 按参考运动生成视频。",
    3: "多角色对话镜头：先在 Blender 里匹配角色姿势和相机运动，再让 Seedance 生成表演结果。",
    5: "动作戏预演：用 Blender 规划粗略时序、速度、抖动和空间调度，再交给 Seedance 渲染成片。",
    6: "手持跟拍：Blender 控制角色穿越空间和相机跟随，Seedance 把这种粗粝跟拍感带到最终视频。",
    7: "可复现 prompt 案例：起始帧、Blender 参考视频、Seedance 版本、时长和运动约束都写清楚。",
    8: "限制排查案例：Blender 能控制相机、节奏和移动路径，但自然脚步动作仍然容易出问题。",
    9: "Agentic Blender MCP 案例：Codex 生成简易市场、猫的动作、相机构图，并导出给 Seedance 的 MP4 参考。",
    10: "参考映射案例：用 Blender blocking 加多张角色/环境参考，告诉 Seedance 哪个运动物体对应哪个角色。",
    14: "ComfyUI 控制案例：Blender previz 搭配 upright/upside-down 参考帧，测试 Seedance 的运动遵循能力。",
    19: "战术动作 blocking：在生成前用 Blender 规划相机环绕、镜头、掩体位置、枪火节奏和角色移动。",
    20: "多工具 agent 管线：Hermes 安装并连接 Krea、ComfyUI、Blender MCP 和 Seedance，生成图像与物理参考。",
    21: "Viewport 到风格化案例：Blender MCP 提供相机和元素控制，再用 Seedance/Magnific 加纹理和光照。",
    23: "新手运动来源案例：从 Mixamo 拿动作导入 Blender，作为可控运动基础后再送入 Seedance。",
    24: "Codex 辅助新手案例：建筑和 camera work 由 Codex 在 Blender 中生成，再测试 Seedance 参考运动。",
    25: "3D previz 到动画渲染：用 Seedance 改变画面风格，同时保留 Blender 里的相机运动和动作。",
    28: "Viewport preview 教程：blockout 场景、导出预览、把首帧转成真实图，再把两类参考交给 Seedance。",
    29: "FBX clay pass 流程：Blender 导入动作，Claude 辅助关键帧相机，渲染后的 clay pass 成为 Seedance 参考视频。",
    31: "无起始帧变体：当不能依赖 starter frame 时，用 Blender blockout 加详细环境参考也能工作。",
    32: "同一参考视频生成不同世界：用同一段 Blender reference 锁定运动，再让 Seedance 改变世界和风格。",
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
    if lang == "en":
        return EN_TAKEAWAYS[index]
    if lang in {"zh-CN", "zh-TW"}:
        text = ZH_TAKEAWAYS[index]
        return zh_tw(text) if lang == "zh-TW" else text
    return EN_TAKEAWAYS[index]


def source_notes(item: dict, index: int, lang: str) -> str:
    why = clean(item.get("why_selected_zh", ""))
    reuse = clean(item.get("reuse_angle_zh", ""))
    note = EN_NOTES[index]
    if lang == "zh-CN":
        return f"- {LOCALE[lang]['notes_prefix']}：{why}\n- 复用角度：{reuse}"
    if lang == "zh-TW":
        return f"- {LOCALE[lang]['notes_prefix']}：{zh_tw(why)}\n- 複用角度：{zh_tw(reuse)}"
    return (
        f"- {LOCALE[lang]['notes_prefix']}: {note}\n"
        f"- Audit status: kept after manual duplicate and originality review."
    )


def local_media_links(case_idx: int) -> list[str]:
    media_dir = ROOT / "media" / f"case-{case_idx:02d}"
    if not media_dir.exists():
        return []
    return [str(path.relative_to(ROOT)) for path in sorted(media_dir.iterdir()) if path.is_file()]


def media_notes(case_idx: int, lang: str) -> str:
    links = local_media_links(case_idx)
    if not links:
        return ""
    label = {
        "en": "Local media",
        "es": "Media local",
        "pt": "Mídia local",
        "ja": "ローカルメディア",
        "ko": "로컬 미디어",
        "de": "Lokale Medien",
        "fr": "Médias locaux",
        "tr": "Yerel medya",
        "zh-CN": "本地媒体",
        "zh-TW": "本地媒體",
        "ru": "Локальные медиа",
    }[lang]
    rendered = ", ".join(f"[{Path(path).name}]({path})" for path in links)
    return f"- {label}: {rendered}"


def author_link(item: dict) -> str:
    username = item["author"]["username"]
    return f"https://x.com/{username}"


def curated_records(items: list[dict]) -> list[dict]:
    records = []
    staged = []
    for source_idx in SELECTED_SOURCE_INDICES:
        item = items[source_idx - 1]
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
                "local_media": local_media_links(idx),
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


def category_display(cat: str, lang: str) -> str:
    return CATEGORY_DISPLAY.get(lang, CATEGORY_DISPLAY["en"])[cat]


def render_overview(labels: dict, records: list[dict], lang: str) -> str:
    bullets = "\n".join(f"- {line.format(count=len(records))}" for line in OVERVIEW_LINES[lang])
    return f"""## 📊 Overview

{bullets}

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
        display = category_display(cat, lang)
        lines.append(f"| [{emoji} {display}](#{slug(name)}) | Case {recs[0]['case']}-{recs[-1]['case']} |")
    lines.append(f"| [🙏 {labels['ack']}](#acknowledge) | Credits and correction policy |")
    lines.append("")
    for cat, recs in grouped.items():
        emoji, name = CATEGORY_META[cat]
        display = category_display(cat, lang)
        lines.extend(
            [
                f'<a id="{slug(name)}"></a>',
                f"### {emoji} {display}",
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
        display = category_display(cat, lang)
        chunks.append(f'<a id="{slug(name)}-cases"></a>')
        chunks.append(f"## {emoji} {display}")
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
                    media_notes(idx, lang),
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
        render_overview(labels, records, lang),
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
            - Manual originality audit: `docs/usecase-originality-audit.md`
            - Downloaded public media: `media/case-XX/`

            ## Current State

            - Selected public cases: {len(records)}
            - Candidate pool before audit: 35
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
            - Local media links when the source data exposes media
            - `Type: ... | Date: YYYY-MM-DD`

            Never invent prompts, results, benchmark claims, availability, pricing, or creator attribution.
            Do not re-add removed candidates without updating the audit file.

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
import json
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

curated = json.loads((ROOT / "blender-seedance-usecase-curated.json").read_text())
if curated["metadata"].get("selected_count") != EXPECTED_CASES:
    fail("curated selected_count does not match README case count")

media_paths = []
for item in curated["items"]:
    for rel in item.get("local_media", []):
        media_paths.append(rel)
        if not (ROOT / rel).exists():
            fail(f"missing local media {{rel}}")

for file in FILES:
    text = (ROOT / file).read_text()
    for rel in media_paths:
        if rel not in text:
            fail(f"{{file}} missing local media link {{rel}}")

print(f"PASS: {{len(FILES)}} README files, {{EXPECTED_CASES}} cases each, {{len(media_paths)}} media files linked")
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
            "audit": "docs/usecase-originality-audit.md",
        },
        "items": records,
    }
    (ROOT / "blender-seedance-usecase-curated.json").write_text(json.dumps(curated, ensure_ascii=False, indent=2) + "\n")
    (ROOT / "blender-seedance-usecase-curated.md").write_text(render_curated_md(records))
    write_static_files(records)
    write_verify_script(records)


if __name__ == "__main__":
    main()
