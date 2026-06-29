<div align="center">

<a href="#conversion-path-pending"><img src="images/zh-tw.png" alt="Blender + Seedance usecase repository banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Use on EvoLink](https://img.shields.io/badge/Use_on-EvoLink-black)](#conversion-path-pending)
[![MCP + Skill](https://img.shields.io/badge/MCP_%2B_Skill-Pending-orange)](#conversion-path-pending)
[![Agent Workflow](https://img.shields.io/badge/Agent_Workflow-Pending-blue)](#conversion-path-pending)

[![English](https://img.shields.io/badge/English-111111)](README.md)
[![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md)
[![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md)
[![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md)
[![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md)
[![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md)
[![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md)
[![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md)
[![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md)
[![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md)
[![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

## 🍌 Introduction

Blender + Seedance 使用案例倉庫。

**這裡收集真實的 Blender、Blender MCP、viewport、previs、FBX、Mixamo、ComfyUI 和 agent 輔助工作流，用來控制 Seedance 影片生成。**

目前集合來自使用者提供的 X/Twitter 精選資料。每個案例都連結到原帖和創作者主頁。

主落地頁暫缺。預期轉化路徑是安裝 MCP、安裝 EvoLink skill、儲值，然後在 Agent 裡使用。

## 📊 Overview

- **35 selected Blender + Seedance cases** from public creator posts in the owner-provided source dataset.
- Covers camera control, Blender previs, multi-character blocking, action choreography, Blender MCP, Codex/Claude-assisted blockouts, FBX/Mixamo references, ComfyUI/style transfer, and known limitations.
- Each case includes the original source, creator attribution, a concise takeaway, evidence type, and publication date.
- Use this repo to inspect practical workflows before routing users to the final EvoLink MCP + skill landing page.

> [!NOTE]
> 這個集合優先保留具體證據：步驟、參考影片、agent/MCP 用法、可重現條件和明確限制，而不是空泛宣傳。

<a id="-quick-api-access"></a>
## ⚡ 快速 API 入口

在最終落地頁提供之前，這裡記錄 Seedance reference-to-video 的預期模型路徑。

```bash
curl --request POST \
  --url https://direct.evolink.ai/v1/messages \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '
{
  "model": "seedance-2.0-reference-to-video",
  "max_tokens": 1024,
  "messages": [
    {
      "role": "user",
      "content": "Plan a Blender reference-video workflow for a Seedance shot."
    }
  ]
}
'
```

<a id="conversion-path-pending"></a>
## 🚧 轉化路徑待補齊

最終落地頁仍待補齊。把倉庫標記為 release-ready 之前，需要把這一節替換成最終 CTA。

## 📑 目錄

| 章節 | 案例 |
|---|---|
| [🎥 Camera Control & Previs](#camera-control-previs) | Case 1-8 |
| [🎬 Character & Action Blocking](#character-action-blocking) | Case 9-13 |
| [🤖 Agentic Blender MCP](#agentic-blender-mcp) | Case 14-19 |
| [🧩 Reference, Prompt & Multi-Input Mapping](#reference-prompt-multi-input-mapping) | Case 20-26 |
| [🛠️ Production Pipelines & Toolchains](#production-pipelines-toolchains) | Case 27-32 |
| [🧪 Limits, Tests & Troubleshooting](#limits-tests-troubleshooting) | Case 33-35 |
| [🙏 致謝](#acknowledge) | Credits and correction policy |

### [🎥 Camera Control & Previs](#camera-control-previs)

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [Blender 灰盒預演 + 起始幀 + Seedance motion reference](#case-1) | 用這個案例來把「Blender 灰盒預演 + 起始幀 + Seedance motion reference」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Demo |
| [Blender 运鏡參考 + Midjourney 起始幀 + Seedance](#case-2) | 用這個案例來把「Blender 运鏡參考 + Midjourney 起始幀 + Seedance」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Demo |
| [Blender previz + Comfy + 三輸入控制](#case-3) | 用這個案例來把「Blender previz + Comfy + 三輸入控制」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Demo |
| [Blender viewport 控制 Seedance 場景導演](#case-4) | 用這個案例來把「Blender viewport 控制 Seedance 場景導演」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Demo |
| [Viewport preview 動画角色](#case-5) | 用這個案例來把「Viewport preview 動画角色」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Demo |
| [Seedance + Claude + Blender 導航式电影控制](#case-6) | 用這個案例來把「Seedance + Claude + Blender 導航式电影控制」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Demo |
| [Viewport preview 導出后进 Seedance](#case-7) | 用這個案例來把「Viewport preview 導出后进 Seedance」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Demo |
| [同一 reference video 生成不同世界](#case-8) | 用這個案例來把「同一 reference video 生成不同世界」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Demo |

### [🎬 Character & Action Blocking](#character-action-blocking)

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [多角色 + 對話 + 精准运鏡](#case-9) | 用這個案例來把「多角色 + 對話 + 精准运鏡」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Demo |
| [基础几何体驱動多角色鏡头](#case-10) | 用這個案例來把「基础几何体驱動多角色鏡头」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Demo |
| [複杂動作場景编排](#case-11) | 用這個案例來把「複杂動作場景编排」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Demo |
| [手持跟拍 + 角色绕车运動](#case-12) | 用這個案例來把「手持跟拍 + 角色绕车运動」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Demo |
| [角色 blocking + 相机 blocking 同时控制](#case-13) | 用這個案例來把「角色 blocking + 相机 blocking 同时控制」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Demo |

### [🤖 Agentic Blender MCP](#agentic-blender-mcp)

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [Codex + Blender MCP 生成場景/動作/参照影片](#case-14) | 用這個案例來把「Codex + Blender MCP 生成場景/動作/参照影片」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Integration |
| [无動画基础也能做 Seedance ref video](#case-15) | 用這個案例來把「无動画基础也能做 Seedance ref video」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Integration |
| [Codex/OPUS + Blender MCP 一句 prompt 做 blockout](#case-16) | 用這個案例來把「Codex/OPUS + Blender MCP 一句 prompt 做 blockout」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Integration |
| [Codex 生成 Blender 建筑和 camera work 后送 Seedance](#case-17) | 用這個案例來把「Codex 生成 Blender 建筑和 camera work 后送 Seedance」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Integration |
| [Blender 初学 + agent 辅助 + Seedance reference video 测試](#case-18) | 用這個案例來把「Blender 初学 + agent 辅助 + Seedance reference video 测試」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Integration |
| [Codex MCP 操作 Blender 導出影片给 Seedance](#case-19) | 用這個案例來把「Codex MCP 操作 Blender 導出影片给 Seedance」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Integration |

### [🧩 Reference, Prompt & Multi-Input Mapping](#reference-prompt-multi-input-mapping)

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [日本語複現條件 + 完整 prompt](#case-20) | 用這個案例來把「日本語複現條件 + 完整 prompt」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Tutorial |
| [Blender blocking + 多參考圖 + 角色锁定 prompt](#case-21) | 用這個案例來把「Blender blocking + 多參考圖 + 角色锁定 prompt」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Tutorial |
| [FBX 動画導入 Blender 后導出 Seedance reference](#case-22) | 用這個案例來把「FBX 動画導入 Blender 后導出 Seedance reference」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Tutorial |
| [土耳其語 Blender + Seedance 導演控制点](#case-23) | 用這個案例來把「土耳其語 Blender + Seedance 導演控制点」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Tutorial |
| [土耳其語 commando scene prompt case](#case-24) | 用這個案例來把「土耳其語 commando scene prompt case」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Tutorial |
| [Mixamo motion + Blender + Seedance 初学者路径](#case-25) | 用這個案例來把「Mixamo motion + Blender + Seedance 初学者路径」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Tutorial |
| [構圖 reference + personal/car reference 組合](#case-26) | 用這個案例來把「構圖 reference + personal/car reference 組合」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Tutorial |

### [🛠️ Production Pipelines & Toolchains](#production-pipelines-toolchains)

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [Hermes/Krea2/ComfyUI/Blender MCP/Seedance 實驗](#case-27) | 用這個案例來把「Hermes/Krea2/ComfyUI/Blender MCP/Seedance 實驗」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Integration |
| [Blender MCP viewport animation + Seedance/Magnific texture/lighting](#case-28) | 用這個案例來把「Blender MCP viewport animation + Seedance/Magnific texture/lighting」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Integration |
| [Seedance 2.0 Pro + Blender viewport style transfer](#case-29) | 用這個案例來把「Seedance 2.0 Pro + Blender viewport style transfer」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Integration |
| [Blender 3D previz → Seedance anime render](#case-30) | 用這個案例來把「Blender 3D previz → Seedance anime render」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Integration |
| [FBX clay model + Claude keyframe + Seedance refs](#case-31) | 用這個案例來把「FBX clay model + Claude keyframe + Seedance refs」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Integration |
| [Seedance 角色 + ComfyUI/Claude + Blender/AE 后期](#case-32) | 用這個案例來把「Seedance 角色 + ComfyUI/Claude + Blender/AE 后期」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Integration |

### [🧪 Limits, Tests & Troubleshooting](#limits-tests-troubleshooting)

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [相机/節奏/移動控制實驗与失败点](#case-33) | 用這個案例來把「相机/節奏/移動控制實驗与失败点」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Limit |
| [不用 start frame 的 Blender blockout reference](#case-34) | 用這個案例來把「不用 start frame 的 Blender blockout reference」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Limit |
| [Mixamo 多角色動作 + Blender storyboard + Seedance](#case-35) | 用這個案例來把「Mixamo 多角色動作 + Blender storyboard + Seedance」改造成 Blender 参考视频驱动的 Seedance 工作流。 | Limit |

## 🎥 Camera Control & Previs

<a id="case-1"></a>
### Case 1: [Blender 灰盒預演 + 起始幀 + Seedance motion reference](https://x.com/noman23761/status/2071534020014563328) (by [@noman23761](https://x.com/noman23761))

**用這個案例來把「Blender 灰盒預演 + 起始幀 + Seedance motion reference」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：完整说明从 image model 起始幀、Blender 灰盒場景/相机動画，到 Seedance 參考影片生成的端到端流程。
- 複用角度：可直接改寫成“用 Blender blockout 精准導演 AI 鏡头”的主 use case。

類型: Demo | 日期: 2026-06-29

---

<a id="case-2"></a>
### Case 2: [Blender 运鏡參考 + Midjourney 起始幀 + Seedance](https://x.com/reidhannaford/status/2069074506849685773) (by [@reidhannaford](https://x.com/reidhannaford))

**用這個案例來把「Blender 运鏡參考 + Midjourney 起始幀 + Seedance」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：列出 3 步 workflow：Blender block camera、Midjourney start frame、两者送入 Seedance。
- 複用角度：适合做 precision camera control 的基础案例。

類型: Demo | 日期: 2026-06-22

---

<a id="case-3"></a>
### Case 3: [Blender previz + Comfy + 三輸入控制](https://x.com/JMSvid/status/2070258132840796579) (by [@JMSvid](https://x.com/JMSvid))

**用這個案例來把「Blender previz + Comfy + 三輸入控制」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明用 Blender previz 作为 guide，并配 upright/upside-down reference frames。
- 複用角度：适合做多輸入相机控制 case。

類型: Demo | 日期: 2026-06-25

---

<a id="case-4"></a>
### Case 4: [Blender viewport 控制 Seedance 場景導演](https://x.com/KimAkiyama81/status/2070668362229690789) (by [@KimAkiyama81](https://x.com/KimAkiyama81))

**用這個案例來把「Blender viewport 控制 Seedance 場景導演」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明 Viewport in Blender gives control for directing scenes in Seedance。
- 複用角度：适合作为 viewport reference 簡短案例。

類型: Demo | 日期: 2026-06-27

---

<a id="case-5"></a>
### Case 5: [Viewport preview 動画角色](https://x.com/KimAkiyama81/status/2070266267051667505) (by [@KimAkiyama81](https://x.com/KimAkiyama81))

**用這個案例來把「Viewport preview 動画角色」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明用 Blender viewport preview 在 Seedance 中 animate character，并提示 process below。
- 複用角度：适合作为 viewport preview 候选。

類型: Demo | 日期: 2026-06-25

---

<a id="case-6"></a>
### Case 6: [Seedance + Claude + Blender 導航式电影控制](https://x.com/Flagiuss/status/2071335816190902624) (by [@Flagiuss](https://x.com/Flagiuss))

**用這個案例來把「Seedance + Claude + Blender 導航式电影控制」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：强调像 3D environment 一样導航电影以获得 camera/movement/pacing control。
- 複用角度：适合做未来式 camera control 叙事素材。

類型: Demo | 日期: 2026-06-28

---

<a id="case-7"></a>
### Case 7: [Viewport preview 導出后进 Seedance](https://x.com/DiabloNemesis/status/2070441923706503380) (by [@DiabloNemesis](https://x.com/DiabloNemesis))

**用這個案例來把「Viewport preview 導出后进 Seedance」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：明确流程：Blender block out scene、export viewport preview、抽第一幀轉真實圖、作为 reference 送 Seedance。
- 複用角度：适合做 viewport preview → Seedance 的短教程案例。

類型: Demo | 日期: 2026-06-26

---

<a id="case-8"></a>
### Case 8: [同一 reference video 生成不同世界](https://x.com/koldo2k/status/2071307945002815967) (by [@koldo2k](https://x.com/koldo2k))

**用這個案例來把「同一 reference video 生成不同世界」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明用 Blender 控制、Seedance 想象，同一 reference video 生成不同 worlds，并提到 prompt。
- 複用角度：适合做 style/world variation case。

類型: Demo | 日期: 2026-06-28

---

## 🎬 Character & Action Blocking

<a id="case-9"></a>
### Case 9: [多角色 + 對話 + 精准运鏡](https://x.com/reidhannaford/status/2069420552394043625) (by [@reidhannaford](https://x.com/reidhannaford))

**用這個案例來把「多角色 + 對話 + 精准运鏡」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明用 Midjourney 起始幀、Blender pose/camera，再交给 Seedance，實現两個一致角色和對話鏡头。
- 複用角度：适合做多角色表演/對話場景 use case。

類型: Demo | 日期: 2026-06-23

---

<a id="case-10"></a>
### Case 10: [基础几何体驱動多角色鏡头](https://x.com/reidhannaford/status/2069783215829569746) (by [@reidhannaford](https://x.com/reidhannaford))

**用這個案例來把「基础几何体驱動多角色鏡头」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：强调 3D 參考不需要精美，只用 basic shapes 也能驱動精确多角色 shot。
- 複用角度：适合做“低成本 3D reference 就够用”的案例。

類型: Demo | 日期: 2026-06-24

---

<a id="case-11"></a>
### Case 11: [複杂動作場景编排](https://x.com/reidhannaford/status/2070145120658137385) (by [@reidhannaford](https://x.com/reidhannaford))

**用這個案例來把「複杂動作場景编排」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：明确说明用 Blender basic shapes 编排 action scene，Seedance 负责真實化。
- 複用角度：适合做動作戏/空间调度 use case。

類型: Demo | 日期: 2026-06-25

---

<a id="case-12"></a>
### Case 12: [手持跟拍 + 角色绕车运動](https://x.com/reidhannaford/status/2070507963429671062) (by [@reidhannaford](https://x.com/reidhannaford))

**用這個案例來把「手持跟拍 + 角色绕车运動」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明在 Blender 中移動角色并做 handheld camera follow，Seedance 跟随运動和质感。
- 複用角度：适合做手持跟拍、角色移動穿越空间的案例。

類型: Demo | 日期: 2026-06-26

---

<a id="case-13"></a>
### Case 13: [角色 blocking + 相机 blocking 同时控制](https://x.com/SamJWasserman/status/2070742850095230991) (by [@SamJWasserman](https://x.com/SamJWasserman))

**用這個案例來把「角色 blocking + 相机 blocking 同时控制」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：明确實現 camera orbit、lens choice、gunfire/cover positions/pop-outs，并说 prompt below。
- 複用角度：适合做動作場景 tactical blocking case。

類型: Demo | 日期: 2026-06-27

---

## 🤖 Agentic Blender MCP

<a id="case-14"></a>
### Case 14: [Codex + Blender MCP 生成場景/動作/参照影片](https://x.com/akiyoshisan/status/2071081230108660199) (by [@akiyoshisan](https://x.com/akiyoshisan))

**用這個案例來把「Codex + Blender MCP 生成場景/動作/参照影片」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：列出 Blender MCP 連接 Codex、生成貓/市場/屋台、15 秒 motion、camera work、導出 MP4 reference 的完整流程。
- 複用角度：适合做 Agentic Blender MCP + Seedance use case。

類型: Integration | 日期: 2026-06-28

---

<a id="case-15"></a>
### Case 15: [无動画基础也能做 Seedance ref video](https://x.com/AIWarper/status/2070162937181065547) (by [@AIWarper](https://x.com/AIWarper))

**用這個案例來把「无動画基础也能做 Seedance ref video」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：强调不用鼠标点击 Blender、可测試 ref video trend，提示后续 details。
- 複用角度：适合作为 agent-assisted/no-code workflow 候选。

類型: Integration | 日期: 2026-06-25

---

<a id="case-16"></a>
### Case 16: [Codex/OPUS + Blender MCP 一句 prompt 做 blockout](https://x.com/AIWarper/status/2070535586075885912) (by [@AIWarper](https://x.com/AIWarper))

**用這個案例來把「Codex/OPUS + Blender MCP 一句 prompt 做 blockout」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明整個 blockout 可通过单 prompt 约 15 分钟完成，但 Seedance 适配仍有問題。
- 複用角度：适合作为 MCP blockout 能力和問題记录。

類型: Integration | 日期: 2026-06-26

---

<a id="case-17"></a>
### Case 17: [Codex 生成 Blender 建筑和 camera work 后送 Seedance](https://x.com/6_KAKUU/status/2071051063663452374) (by [@6_KAKUU](https://x.com/6_KAKUU))

**用這個案例來把「Codex 生成 Blender 建筑和 camera work 后送 Seedance」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明 Blender 初学第 3 天，建筑到 camera work 都由 Codex 完成，Seedance 能跟随。
- 複用角度：适合做 Codex-assisted camera work case。

類型: Integration | 日期: 2026-06-28

---

<a id="case-18"></a>
### Case 18: [Blender 初学 + agent 辅助 + Seedance reference video 测試](https://x.com/Ukiyo_il/status/2071098235268071877) (by [@Ukiyo_il](https://x.com/Ukiyo_il))

**用這個案例來把「Blender 初学 + agent 辅助 + Seedance reference video 测試」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明由 agent 辅助做 Blender 參考影片，并测試複杂 HIPHOP dance 进入 Seedance。
- 複用角度：适合作为 beginner/agent-assisted experiment。

類型: Integration | 日期: 2026-06-28

---

<a id="case-19"></a>
### Case 19: [Codex MCP 操作 Blender 導出影片给 Seedance](https://x.com/Toshi_nyaruo_AI/status/2071149652905537541) (by [@Toshi_nyaruo_AI](https://x.com/Toshi_nyaruo_AI))

**用這個案例來把「Codex MCP 操作 Blender 導出影片给 Seedance」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明用 Codex MCP 直接操作 Blender 并導出影片，初学 2 小时完成。
- 複用角度：适合做 beginner Codex MCP workflow。

類型: Integration | 日期: 2026-06-28

---

## 🧩 Reference, Prompt & Multi-Input Mapping

<a id="case-20"></a>
### Case 20: [日本語複現條件 + 完整 prompt](https://x.com/aidoga_lab/status/2070864815275585913) (by [@aidoga_lab](https://x.com/aidoga_lab))

**用這個案例來把「日本語複現條件 + 完整 prompt」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：给出 start frame、Blender reference video、Seedance 2.0、5s、以及长 prompt。
- 複用角度：适合做可複現 prompt/source case。

類型: Tutorial | 日期: 2026-06-27

---

<a id="case-21"></a>
### Case 21: [Blender blocking + 多參考圖 + 角色锁定 prompt](https://x.com/AIWarper/status/2069481237308452916) (by [@AIWarper](https://x.com/AIWarper))

**用這個案例來把「Blender blocking + 多參考圖 + 角色锁定 prompt」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：给出 Seedance prompt，把 motion/blocking reference 中的角色映射到指定角色參考圖。
- 複用角度：适合做 prompt engineering + character mapping case。

類型: Tutorial | 日期: 2026-06-23

---

<a id="case-22"></a>
### Case 22: [FBX 動画導入 Blender 后導出 Seedance reference](https://x.com/AIWarper/status/2069847776620589430) (by [@AIWarper](https://x.com/AIWarper))

**用這個案例來把「FBX 動画導入 Blender 后導出 Seedance reference」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：列出 import FBX、position camera、export animation mp4，且提到 Seedance ref videos 720 max。
- 複用角度：适合做 Mixamo/FBX animation reference pipeline。

類型: Tutorial | 日期: 2026-06-24

---

<a id="case-23"></a>
### Case 23: [土耳其語 Blender + Seedance 導演控制点](https://x.com/ai_gezgini/status/2070531406237728977) (by [@ai_gezgini](https://x.com/ai_gezgini))

**用這個案例來把「土耳其語 Blender + Seedance 導演控制点」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：列出 camera angle、character pose、motion direction、lighting、depth、lens、composition 等控制项。
- 複用角度：适合提炼为導演参数 checklist。

類型: Tutorial | 日期: 2026-06-26

---

<a id="case-24"></a>
### Case 24: [土耳其語 commando scene prompt case](https://x.com/ai_gezgini/status/2071529677353615522) (by [@ai_gezgini](https://x.com/ai_gezgini))

**用這個案例來把「土耳其語 commando scene prompt case」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：列出相机看向、角色进入方向、跟随角度、运動方向、景深、最终構圖等。
- 複用角度：适合提炼为動作鏡头 prompt/control checklist。

類型: Tutorial | 日期: 2026-06-29

---

<a id="case-25"></a>
### Case 25: [Mixamo motion + Blender + Seedance 初学者路径](https://x.com/tanabe_fragm/status/2070685291183243459) (by [@tanabe_fragm](https://x.com/tanabe_fragm))

**用這個案例來把「Mixamo motion + Blender + Seedance 初学者路径」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：测試 Blender x Seedance，并建议初学者下载 Mixamo motion 導入 Blender。
- 複用角度：适合做 beginner motion-source case。

類型: Tutorial | 日期: 2026-06-27

---

<a id="case-26"></a>
### Case 26: [構圖 reference + personal/car reference 組合](https://x.com/Gen_x111x/status/2069803766581526534) (by [@Gen_x111x](https://x.com/Gen_x111x))

**用這個案例來把「構圖 reference + personal/car reference 組合」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：日文说明用 Blender 構圖 reference、個人 reference、panda car reference 組合，强调 CG camera instruction 重要。
- 複用角度：适合做 multi-reference composition case。

類型: Tutorial | 日期: 2026-06-24

---

## 🛠️ Production Pipelines & Toolchains

<a id="case-27"></a>
### Case 27: [Hermes/Krea2/ComfyUI/Blender MCP/Seedance 實驗](https://x.com/SamJWasserman/status/2069656428437225826) (by [@SamJWasserman](https://x.com/SamJWasserman))

**用這個案例來把「Hermes/Krea2/ComfyUI/Blender MCP/Seedance 實驗」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明 agent 安装 Krea2、連接 ComfyUI 和 Blender MCP，生成 reference image + physical ref vid 后送 Seedance。
- 複用角度：适合做 multi-agent creative pipeline 候选。

類型: Integration | 日期: 2026-06-24

---

<a id="case-28"></a>
### Case 28: [Blender MCP viewport animation + Seedance/Magnific texture/lighting](https://x.com/techhalla/status/2070814203435274715) (by [@techhalla](https://x.com/techhalla))

**用這個案例來把「Blender MCP viewport animation + Seedance/Magnific texture/lighting」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明 adding 3D gives camera/element control，并声称 exactly how I did it。
- 複用角度：适合做 Blender MCP + style transfer 主案例。

類型: Integration | 日期: 2026-06-27

---

<a id="case-29"></a>
### Case 29: [Seedance 2.0 Pro + Blender viewport style transfer](https://x.com/techhalla/status/2070832621328732396) (by [@techhalla](https://x.com/techhalla))

**用這個案例來把「Seedance 2.0 Pro + Blender viewport style transfer」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：明确是 viewport style transfer，并指向下方流程。
- 複用角度：适合作为 style transfer 传播帖。

類型: Integration | 日期: 2026-06-27

---

<a id="case-30"></a>
### Case 30: [Blender 3D previz → Seedance anime render](https://x.com/restofart/status/2070086939756159368) (by [@restofart](https://x.com/restofart))

**用這個案例來把「Blender 3D previz → Seedance anime render」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明 full camera moves and motion preserved，定位 previz → AI-render pipeline。
- 複用角度：适合作为 anime/render pipeline case。

類型: Integration | 日期: 2026-06-25

---

<a id="case-31"></a>
### Case 31: [FBX clay model + Claude keyframe + Seedance refs](https://x.com/Viggle_PINOC/status/2070183934265012392) (by [@Viggle_PINOC](https://x.com/Viggle_PINOC))

**用這個案例來把「FBX clay model + Claude keyframe + Seedance refs」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：具体 step：Blender 導入 FBX 到 clay model、设置 camera、Claude keyframe camera moves、導出 mp4 给 Seedance refs。
- 複用角度：适合做 FBX/Mixamo 動画參考流程。

類型: Integration | 日期: 2026-06-25

---

<a id="case-32"></a>
### Case 32: [Seedance 角色 + ComfyUI/Claude + Blender/AE 后期](https://x.com/VengadaS65199/status/2070049247823859770) (by [@VengadaS65199](https://x.com/VengadaS65199))

**用這個案例來把「Seedance 角色 + ComfyUI/Claude + Blender/AE 后期」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明两晚完成创作，Seedance 做角色，ComfyUI 節点由 Claude 辅助，其余在 Blender 和 AE。
- 複用角度：适合做完整短片制作管线候选。

類型: Integration | 日期: 2026-06-25

---

## 🧪 Limits, Tests & Troubleshooting

<a id="case-33"></a>
### Case 33: [相机/節奏/移動控制實驗与失败点](https://x.com/aidoga_lab/status/2070864749865398684) (by [@aidoga_lab](https://x.com/aidoga_lab))

**用這個案例來把「相机/節奏/移動控制實驗与失败点」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明用 Blender 影片控制 Seedance 的 camera/rhythm/subject movement，同时指出 foot sliding 問題。
- 複用角度：适合做 limitations + troubleshooting case。

類型: Limit | 日期: 2026-06-27

---

<a id="case-34"></a>
### Case 34: [不用 start frame 的 Blender blockout reference](https://x.com/magneticskiff/status/2070711034793361559) (by [@magneticskiff](https://x.com/magneticskiff))

**用這個案例來把「不用 start frame 的 Blender blockout reference」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：说明 Seedance + Blender blockout 可以使用 references 而非 starter frames，环境參考有足够细節时效果较好。
- 複用角度：适合做 reference-only variant 候选。

類型: Limit | 日期: 2026-06-27

---

<a id="case-35"></a>
### Case 35: [Mixamo 多角色動作 + Blender storyboard + Seedance](https://x.com/dave392750/status/2070851042661810551) (by [@dave392750](https://x.com/dave392750))

**用這個案例來把「Mixamo 多角色動作 + Blender storyboard + Seedance」改造成 Blender 参考视频驱动的 Seedance 工作流。**

- 來源筆記：日文说明 Blender storyboarding、Mixamo 多体動作、Seedance 处理跳跃/動作的實驗問題。
- 複用角度：适合做 Mixamo motion complexity/troubleshooting case。

類型: Limit | 日期: 2026-06-27

---

<a id="acknowledge"></a>
## 🙏 致謝

This repository was inspired by creators who publicly shared Blender + Seedance workflows, tests, prompts, reference videos, and production notes.

- [@noman23761](https://x.com/noman23761)
- [@reidhannaford](https://x.com/reidhannaford)
- [@JMSvid](https://x.com/JMSvid)
- [@KimAkiyama81](https://x.com/KimAkiyama81)
- [@Flagiuss](https://x.com/Flagiuss)
- [@DiabloNemesis](https://x.com/DiabloNemesis)
- [@koldo2k](https://x.com/koldo2k)
- [@SamJWasserman](https://x.com/SamJWasserman)
- [@akiyoshisan](https://x.com/akiyoshisan)
- [@AIWarper](https://x.com/AIWarper)
- [@6_KAKUU](https://x.com/6_KAKUU)
- [@Ukiyo_il](https://x.com/Ukiyo_il)
- [@Toshi_nyaruo_AI](https://x.com/Toshi_nyaruo_AI)
- [@aidoga_lab](https://x.com/aidoga_lab)
- [@ai_gezgini](https://x.com/ai_gezgini)
- [@tanabe_fragm](https://x.com/tanabe_fragm)
- [@Gen_x111x](https://x.com/Gen_x111x)
- [@techhalla](https://x.com/techhalla)
- [@restofart](https://x.com/restofart)
- [@Viggle_PINOC](https://x.com/Viggle_PINOC)
- [@VengadaS65199](https://x.com/VengadaS65199)
- [@magneticskiff](https://x.com/magneticskiff)
- [@dave392750](https://x.com/dave392750)

*We cannot guarantee that every case is attributed to the original creator. If anything needs to be corrected, please contact us and we will update it.*

If you have more interesting usage cases to share, open an issue or pull request and help expand the EvoLink usecase library.

[![Star History Chart](https://api.star-history.com/svg?repos=cheercheung/Awesome-Blender-Seedance-Workflow-Usecases&type=Date)](https://www.star-history.com/#cheercheung/Awesome-Blender-Seedance-Workflow-Usecases&Date)

