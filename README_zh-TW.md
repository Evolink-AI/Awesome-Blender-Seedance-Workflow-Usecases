<div align="center">

<a href="https://evolink.ai/cookbook/blender-to-video?utm_source=github&utm_medium=banner&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/images/banner.png" alt="Blender + Seedance usecase repository banner" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Try Blender Workflow](https://img.shields.io/badge/Try-Blender_Workflow-black)](https://evolink.ai/cookbook/blender-to-video?utm_source=github&utm_medium=badge&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=model_try)
[![Get API Key](https://img.shields.io/badge/Get-API_Key-blue)](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=badge&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key)

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

先從 EvoLink Blender-to-video cookbook 開始，再把下面的 Quick Start 作為倉庫內 workflow 參考。

## 📊 Overview

- **32 個 Blender + Seedance 精選案例**，來自公開創作者貼文和通過審計的每週增量更新。
- 涵蓋相機控制、Blender previs、多角色 blocking、動作編排、Blender MCP、Codex/Claude 輔助 blockout、FBX/Mixamo 參考、ComfyUI/style transfer 和已知限制。
- 每個案例都包含原始來源、創作者署名、簡明 takeaway、證據類型和發布日期。
- 公開列表起點仍是 35 條候選審計，現在額外納入了 recurring update loop 審過的 7 條每週新增案例。
- 這個倉庫用於先展示真實工作流，再把使用者引導到 EvoLink Blender-to-video cookbook。

> [!NOTE]
> 這個集合優先保留具體證據：步驟、參考影片、agent/MCP 用法、可重現條件和明確限制，而不是空泛宣傳。

<a id="quick-start"></a>
## ⚡ Quick Start

先把本地 Blender 控制鏈路搭好，再安裝 agent 會呼叫的 EvoLink skills。

### 1. 安裝 Blender MCP

按照官方 Blender MCP setup 頁面完成配置，開啟 Blender，並在生成參考影片之前確認 agent 能連接到 Blender MCP server。

- 官方 setup: [Blender MCP setup](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

在第一條可執行請求之前，先到 [取得 API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key) 準備好 EvoLink 金鑰。

### 2. 安裝 EvoLink skills

在 agent workspace 裡安裝 Seedance 生成 skill 和 Topaz 影片放大 skill。

```bash
npm i evolink-seedance
npm i evolink-topaz-video-upscale
```

### 3. [取得 API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key)

在 EvoLink 帳號裡建立 API key，然後把它暴露給 agent runtime。

```bash
export EVOLINK_API_KEY="paste_api_key_here"
```

### 4. 在自己的 agent 裡執行

MCP、skills 和 API key 都準備好之後，就可以讓 agent 建立 Blender blockout、匯出參考影片、呼叫 Seedance 生成，並在需要時用 Topaz 放大最終影片。

送出直接請求前，請先到 [取得 API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key) 確認金鑰可用。如果你需要直接 API fallback，可以把 Blender 參考工作流提交到 `POST https://api.evolink.ai/v1/videos/generations`：

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-reference-to-video",
    "prompt": "Use the Blender blockout video as the motion guide, keep the camera path, and preserve the staged timing.",
    "video_urls": ["https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case29.mp4"],
    "image_urls": ["https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case29.jpg"],
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

如果你接下來就要把這套流程交給 agent 跑，先到 [取得 API key](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key) 再確認一次同一把金鑰。

```text
Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.
```

> [!NOTE]
> Blender 側安裝細節以 Blender MCP setup 頁面為準。

## 📑 目錄

| 章節 | 案例 |
|---|---|
| [🎥 Camera Control & Previs / 相機控制與預演](#camera-control-previs) | Case 1, 2, 3, 4, 5, 29 |
| [🎬 Character & Action Blocking / 角色與動作 blocking](#character-action-blocking) | Case 6, 8, 9, 21, 32 |
| [🤖 Agentic Blender MCP / Agent 輔助 Blender MCP](#agentic-blender-mcp) | Case 10, 11, 22, 34 |
| [🧩 Reference, Prompt & Multi-Input Mapping / 參考、prompt 與多輸入映射](#reference-prompt-multi-input-mapping) | Case 13, 14, 23, 24, 26, 27, 35 |
| [🛠️ Production Pipelines & Toolchains / 生產管線與工具鏈](#production-pipelines-toolchains) | Case 15, 16, 17, 18, 30 |
| [🧪 Limits, Tests & Troubleshooting / 限制、測試與排查](#limits-tests-troubleshooting) | Case 20, 25, 28, 31, 33 |
| [🙏 致謝](#acknowledge) | Credits and correction policy |

<a id="camera-control-previs"></a>
### 🎥 Camera Control & Previs / 相機控制與預演

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [Blender 灰盒預演 + 起始幀 + Seedance motion reference](#case-1) | 合并后的導演流程：保留原始灰盒方法，再加入動作預演里的时序、速度、抖動和空间调度，最后交给 Seedance 生成。 | Demo |
| [Blender 运鏡參考 + Midjourney 起始幀 + Seedance](#case-2) | 精确运鏡的三步配方：Blender 负责相机运動，Midjourney 负责起始幀，Seedance 按參考运動生成影片。 | Demo |
| [Blender previz + Comfy + 三輸入控制](#case-3) | ComfyUI 控制案例：Blender previz 搭配 upright/upside-down 參考幀，测試 Seedance 的运動遵循能力。 | Demo |
| [Viewport preview 導出后进 Seedance](#case-4) | Viewport preview 教程：blockout 場景、導出預覽、把首幀轉成真實圖，再把两类參考交给 Seedance。 | Demo |
| [同一 reference video 生成不同世界](#case-5) | 同一參考影片生成不同世界：用同一段 Blender reference 锁定运動，再让 Seedance 改变世界和风格。 | Demo |
| [iPhone 驅動的對話節奏相機預演](#case-29) | 先用 iPhone 驅動 Blender 相機並按對話定節奏，再把帶音訊的預演和兩張圖一起交給 Seedance 做鏡頭規劃。 | Integration |


<a id="character-action-blocking"></a>
### 🎬 Character & Action Blocking / 角色與動作 blocking

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [多角色 + 對話 + 精准运鏡](#case-6) | 多角色對話鏡头：先在 Blender 里匹配角色姿势和相机运動，再让 Seedance 生成表演结果。 | Demo |
| [手持跟拍 + 角色绕车运動](#case-8) | 手持跟拍：Blender 控制角色穿越空间和相机跟随，Seedance 把这种粗粝跟拍感带到最终影片。 | Demo |
| [角色 blocking + 相机 blocking 同时控制](#case-9) | 战术動作 blocking：在生成前用 Blender 规划相机环绕、鏡头、掩体位置、枪火節奏和角色移動。 | Demo |
| [伏击場景 previs + Seedance 動作调度](#case-21) | 伏击場景案例：先用 Blender previs 解决 staging、timing 和 camera movement，再交给 Seedance 生成鏡头。 | Demo |
| [帶障礙互動的屋頂跑酷追逐](#case-32) | 當 Seedance 容易把動作退化成直線奔跑時，可以先用 Blender 跑酷預演補足障礙互動和閃避節奏。 | Demo |


<a id="agentic-blender-mcp"></a>
### 🤖 Agentic Blender MCP / Agent 輔助 Blender MCP

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [Codex + Blender MCP 生成場景/動作/参照影片](#case-10) | Agentic Blender MCP 案例：Codex 生成簡易市場、貓的動作、相机構圖，并導出给 Seedance 的 MP4 參考。 | Integration |
| [Codex 生成 Blender 建筑和 camera work 后送 Seedance](#case-11) | Codex 辅助新手案例：建筑和 camera work 由 Codex 在 Blender 中生成，再测試 Seedance 參考运動。 | Integration |
| [Claude 用 Blender MCP 几分钟生成 previs](#case-22) | 快速 agentic previs 案例：Claude 通过 Blender MCP 在 2-3 分钟内搭出鏡头參考。 | Integration |
| [Fable 技能移植到 Codex 的參考影片流](#case-34) | 可以先讓 agent 產出 Blender 參考影片技能，再移植到 Codex，驗證 Seedance 是否能在零提示詞前提下把動作進一步修順。 | Integration |


<a id="reference-prompt-multi-input-mapping"></a>
### 🧩 Reference, Prompt & Multi-Input Mapping / 參考、prompt 與多輸入映射

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [日本語複現條件 + 完整 prompt](#case-13) | 合并后的複現与排查案例：一條寫清參考影片條件，另一條记录相机/節奏控制有效但脚步動作仍会失败。 | Tutorial |
| [Mixamo motion + Blender + Seedance 初学者路径](#case-14) | 新手运動来源案例：从 Mixamo 拿動作導入 Blender，作为可控运動基础后再送入 Seedance。 | Tutorial |
| [只保留位置关系的參考控制](#case-23) | 參考权重案例：只让參考影片约束位置关系，再用 prompt 补回速度感和動态感。 | Tutorial |
| [用實体玩具替代 3D 软件做參考](#case-24) | 實体參考案例：当不想打开 Blender 时，用玩具快速拍攝运動和 staging 參考。 | Demo |
| [用參考控制修複 prompt 反複失败的場景](#case-26) | 控制兜底案例：prompt-only 反複失败时，用 reference 强制場景成立，即使会损失部分動态。 | Demo |
| [角色比例与簡化背景的稳定性技巧](#case-27) | 稳定性 checklist：角色比例不只看头身，还要匹配手脚体积；无须對齐的背景尽量簡化。 | Tutorial |
| [人偶動捕配合風格化輸入幀](#case-35) | 可以先用偏僵硬的人偶或 Blender 動作源鎖節奏，再透過輸入幀設計把 Seedance 的風格和布料表現拉回來。 | Demo |


<a id="production-pipelines-toolchains"></a>
### 🛠️ Production Pipelines & Toolchains / 生產管線與工具鏈

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [Hermes/Krea2/ComfyUI/Blender MCP/Seedance 實驗](#case-15) | 多工具 agent 管线：Hermes 安装并連接 Krea、ComfyUI、Blender MCP 和 Seedance，生成圖像与物理參考。 | Integration |
| [Blender MCP viewport animation + Seedance/Magnific texture/lighting](#case-16) | Viewport 到风格化案例：Blender MCP 提供相机和元素控制，再用 Seedance/Magnific 加纹理和光照。 | Integration |
| [Blender 3D previz → Seedance anime render](#case-17) | 3D previz 到動画渲染：用 Seedance 改变画面风格，同时保留 Blender 里的相机运動和動作。 | Integration |
| [FBX clay model + Claude keyframe + Seedance refs](#case-18) | FBX clay pass 流程：Blender 導入動作，Claude 辅助关键幀相机，渲染后的 clay pass 成为 Seedance 參考影片。 | Integration |
| [Fable 編排的舞蹈參考影片流水線](#case-30) | 當純提示詞難以描述舞步時，可以讓 agent 負責角色設計和 Blender 編舞程式碼，再把 15 秒舞蹈參考交給 Seedance。 | Integration |


<a id="limits-tests-troubleshooting"></a>
### 🧪 Limits, Tests & Troubleshooting / 限制、測試與排查

| 案例 | 展示內容 | 類型 |
|---|---|---|
| [不用 start frame 的 Blender blockout reference](#case-20) | 无起始幀变体：当不能依赖 starter frame 时，用 Blender blockout 加详细环境參考也能工作。 | Limit |
| [玩具參考 + prompt 补强 + NG 對照](#case-25) | 排查案例：參考影片通常需要 prompt 补强，不能只让模型机械照搬。 | Limit |
| [Blender + Seedance 布料物理压力测試](#case-28) | 布料物理压力测試：Blender-guided Seedance 可用，但複杂运動仍需要多轮迭代。 | Limit |
| [黑幀隔開的關鍵幀節奏修正法](#case-31) | 如果粗糙的 Blender 參考讓 Seedance 連僵硬的中間幀都照搬，就保留關鍵姿勢並把中間幀全部壓成黑幀。 | Tutorial |
| [複雜場景動作失配測試](#case-33) | 把粗場景 MCP 渲染當作限制測試來看：即使反覆多次，複雜 Blender 場景在 Seedance 裡仍可能偏離預期動作。 | Limit |



<a id="camera-control-previs-cases"></a>
## 🎥 Camera Control & Previs / 相機控制與預演

<a id="case-1"></a>
### Case 1: [Blender 灰盒預演 + 起始幀 + Seedance motion reference](https://x.com/noman23761/status/2071534020014563328) (by [@noman23761](https://x.com/noman23761))

**合并后的導演流程：保留原始灰盒方法，再加入動作預演里的时序、速度、抖動和空间调度，最后交给 Seedance 生成。**

- 來源筆記：完整说明从 image model 起始幀、Blender 灰盒場景/相机動画，到 Seedance 參考影片生成的端到端流程。
- 複用角度：可直接改寫成“用 Blender blockout 精准導演 AI 鏡头”的主 use case。
- 影片預覽:

[![播放示範影片 — Case 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case1.mp4)

類型: Demo | 日期: 2026-06-29

---

<a id="case-2"></a>
### Case 2: [Blender 运鏡參考 + Midjourney 起始幀 + Seedance](https://x.com/reidhannaford/status/2069074506849685773) (by [@reidhannaford](https://x.com/reidhannaford))

**精确运鏡的三步配方：Blender 负责相机运動，Midjourney 负责起始幀，Seedance 按參考运動生成影片。**

- 來源筆記：列出 3 步 workflow：Blender block camera、Midjourney start frame、两者送入 Seedance。
- 複用角度：适合做 precision camera control 的基础案例。
- 影片預覽:

[![播放示範影片 — Case 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case2.mp4)

類型: Demo | 日期: 2026-06-22

---

<a id="case-3"></a>
### Case 3: [Blender previz + Comfy + 三輸入控制](https://x.com/JMSvid/status/2070258132840796579) (by [@JMSvid](https://x.com/JMSvid))

**ComfyUI 控制案例：Blender previz 搭配 upright/upside-down 參考幀，测試 Seedance 的运動遵循能力。**

- 來源筆記：说明用 Blender previz 作为 guide，并配 upright/upside-down reference frames。
- 複用角度：适合做多輸入相机控制 case。
- 影片預覽:

[![播放示範影片 — Case 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case3.mp4)

類型: Demo | 日期: 2026-06-25

---

<a id="case-4"></a>
### Case 4: [Viewport preview 導出后进 Seedance](https://x.com/DiabloNemesis/status/2070441923706503380) (by [@DiabloNemesis](https://x.com/DiabloNemesis))

**Viewport preview 教程：blockout 場景、導出預覽、把首幀轉成真實圖，再把两类參考交给 Seedance。**

- 來源筆記：明确流程：Blender block out scene、export viewport preview、抽第一幀轉真實圖、作为 reference 送 Seedance。
- 複用角度：适合做 viewport preview → Seedance 的短教程案例。
- 影片預覽:

[![播放示範影片 — Case 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case4.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case4.mp4)

類型: Demo | 日期: 2026-06-26

---

<a id="case-5"></a>
### Case 5: [同一 reference video 生成不同世界](https://x.com/koldo2k/status/2071307945002815967) (by [@koldo2k](https://x.com/koldo2k))

**同一參考影片生成不同世界：用同一段 Blender reference 锁定运動，再让 Seedance 改变世界和风格。**

- 來源筆記：说明用 Blender 控制、Seedance 想象，同一 reference video 生成不同 worlds，并提到 prompt。
- 複用角度：适合做 style/world variation case。
- 影片預覽:

[![播放示範影片 — Case 5](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case5.mp4)

類型: Demo | 日期: 2026-06-28

---


<a id="case-29"></a>
### Case 29: [iPhone 驅動的對話節奏相機預演](https://x.com/CoffeeVectors/status/2076397975853551924) (by [@CoffeeVectors](https://x.com/CoffeeVectors))

**先用 iPhone 驅動 Blender 相機並按對話定節奏，再把帶音訊的預演和兩張圖一起交給 Seedance 做鏡頭規劃。**

- 來源筆記: 原帖用 iPhone 驅動 Blender 相機並按對話卡節奏，再把帶音訊的預演和兩張靜態圖一起送進 Seedance 2。
- 影片預覽:

[![影片預覽 — Case 29](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case29.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case29.mp4)

類型: Integration | 日期: 2026-07-12

---
<a id="character-action-blocking-cases"></a>
## 🎬 Character & Action Blocking / 角色與動作 blocking

<a id="case-6"></a>
### Case 6: [多角色 + 對話 + 精准运鏡](https://x.com/reidhannaford/status/2069420552394043625) (by [@reidhannaford](https://x.com/reidhannaford))

**多角色對話鏡头：先在 Blender 里匹配角色姿势和相机运動，再让 Seedance 生成表演结果。**

- 來源筆記：说明用 Midjourney 起始幀、Blender pose/camera，再交给 Seedance，實現两個一致角色和對話鏡头。
- 複用角度：适合做多角色表演/對話場景 use case。
- 影片預覽:

[![播放示範影片 — Case 6](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case6.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case6.mp4)

類型: Demo | 日期: 2026-06-23

---

<a id="case-8"></a>
### Case 8: [手持跟拍 + 角色绕车运動](https://x.com/reidhannaford/status/2070507963429671062) (by [@reidhannaford](https://x.com/reidhannaford))

**手持跟拍：Blender 控制角色穿越空间和相机跟随，Seedance 把这种粗粝跟拍感带到最终影片。**

- 來源筆記：说明在 Blender 中移動角色并做 handheld camera follow，Seedance 跟随运動和质感。
- 複用角度：适合做手持跟拍、角色移動穿越空间的案例。
- 影片預覽:

預覽無法使用：原始 GitHub 附件已無法公開存取。

類型: Demo | 日期: 2026-06-26

---

<a id="case-9"></a>
### Case 9: [角色 blocking + 相机 blocking 同时控制](https://x.com/SamJWasserman/status/2070742850095230991) (by [@SamJWasserman](https://x.com/SamJWasserman))

**战术動作 blocking：在生成前用 Blender 规划相机环绕、鏡头、掩体位置、枪火節奏和角色移動。**

- 來源筆記：明确實現 camera orbit、lens choice、gunfire/cover positions/pop-outs，并说 prompt below。
- 複用角度：适合做動作場景 tactical blocking case。
- 影片預覽:

[![播放示範影片 — Case 9](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case9.mp4)

類型: Demo | 日期: 2026-06-27

---

<a id="case-21"></a>
### Case 21: [伏击場景 previs + Seedance 動作调度](https://x.com/reidhannaford/status/2071595581508563168) (by [@reidhannaford](https://x.com/reidhannaford))

**伏击場景案例：先用 Blender previs 解决 staging、timing 和 camera movement，再交给 Seedance 生成鏡头。**

- 來源筆記：明确把 Midjourney 起始圖、Blender blocking/相机動画和 Seedance 組合，用于複杂伏击場景而不只是簡单运鏡。
- 複用角度：适合做複杂場景先解决 staging、timing 和 camera movement，再生成鏡头的案例。
- 影片預覽:

[![播放示範影片 — Case 21](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case21.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case21.mp4)

類型: Demo | 日期: 2026-06-29

---


<a id="case-32"></a>
### Case 32: [帶障礙互動的屋頂跑酷追逐](https://x.com/moframe2026/status/2075203485604470965) (by [@moframe2026](https://x.com/moframe2026))

**當 Seedance 容易把動作退化成直線奔跑時，可以先用 Blender 跑酷預演補足障礙互動和閃避節奏。**

- 來源筆記: 作者把 Blender 跑酷預演當成影片參考，並明確說如果沒有這層參考，動作會更容易塌成單純奔跑。
- 影片預覽:

[![影片預覽 — Case 32](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case32.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case32.mp4)

類型: Demo | 日期: 2026-07-09

---
<a id="agentic-blender-mcp-cases"></a>
## 🤖 Agentic Blender MCP / Agent 輔助 Blender MCP

<a id="case-10"></a>
### Case 10: [Codex + Blender MCP 生成場景/動作/参照影片](https://x.com/akiyoshisan/status/2071081230108660199) (by [@akiyoshisan](https://x.com/akiyoshisan))

**Agentic Blender MCP 案例：Codex 生成簡易市場、貓的動作、相机構圖，并導出给 Seedance 的 MP4 參考。**

- 來源筆記：列出 Blender MCP 連接 Codex、生成貓/市場/屋台、15 秒 motion、camera work、導出 MP4 reference 的完整流程。
- 複用角度：适合做 Agentic Blender MCP + Seedance use case。
- 影片預覽:

[![播放示範影片 — Case 10](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case10.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case10.mp4)

類型: Integration | 日期: 2026-06-28

---

<a id="case-11"></a>
### Case 11: [Codex 生成 Blender 建筑和 camera work 后送 Seedance](https://x.com/6_KAKUU/status/2071051063663452374) (by [@6_KAKUU](https://x.com/6_KAKUU))

**Codex 辅助新手案例：建筑和 camera work 由 Codex 在 Blender 中生成，再测試 Seedance 參考运動。**

- 來源筆記：说明 Blender 初学第 3 天，建筑到 camera work 都由 Codex 完成，Seedance 能跟随。
- 複用角度：适合做 Codex-assisted camera work case。
- 影片預覽:

[![播放示範影片 — Case 11](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case11.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case11.mp4)

類型: Integration | 日期: 2026-06-28

---

<a id="case-22"></a>
### Case 22: [Claude 用 Blender MCP 几分钟生成 previs](https://x.com/JoshDaws/status/2071401550845481090) (by [@JoshDaws](https://x.com/JoshDaws))

**快速 agentic previs 案例：Claude 通过 Blender MCP 在 2-3 分钟内搭出鏡头參考。**

- 來源筆記：说明 Claude 通过 Blender MCP 为鏡头创建 previs，并强调 2-3 分钟完成。
- 複用角度：适合做 agent 快速搭建鏡头預演的短案例。
- 影片預覽:

[![播放示範影片 — Case 22](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case22.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case22.mp4)

類型: Integration | 日期: 2026-06-29

---


<a id="case-34"></a>
### Case 34: [Fable 技能移植到 Codex 的參考影片流](https://x.com/mugi_AI_Art/status/2074259600342163846) (by [@mugi_AI_Art](https://x.com/mugi_AI_Art))

**可以先讓 agent 產出 Blender 參考影片技能，再移植到 Codex，驗證 Seedance 是否能在零提示詞前提下把動作進一步修順。**

- 來源筆記: 作者先讓 Fable 產出 Blender 參考影片技能，再移植進 Codex，並在粗模參考基礎上做了「零提示詞」的 Seedance 生成。
- 影片預覽:

[![影片預覽 — Case 34](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case34.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case34.mp4)

類型: Integration | 日期: 2026-07-06

---
<a id="reference-prompt-multi-input-mapping-cases"></a>
## 🧩 Reference, Prompt & Multi-Input Mapping / 參考、prompt 與多輸入映射

<a id="case-13"></a>
### Case 13: [日本語複現條件 + 完整 prompt](https://x.com/aidoga_lab/status/2070864815275585913) (by [@aidoga_lab](https://x.com/aidoga_lab))

**合并后的複現与排查案例：一條寫清參考影片條件，另一條记录相机/節奏控制有效但脚步動作仍会失败。**

- 來源筆記：给出 start frame、Blender reference video、Seedance 2.0、5s、以及长 prompt。
- 複用角度：适合做可複現 prompt/source case。
- 影片預覽:

[![播放示範影片 — Case 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case13.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.mp4)

![參考圖片 — Case 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.jpg)

類型: Tutorial | 日期: 2026-06-27

---

<a id="case-14"></a>
### Case 14: [Mixamo motion + Blender + Seedance 初学者路径](https://x.com/tanabe_fragm/status/2070685291183243459) (by [@tanabe_fragm](https://x.com/tanabe_fragm))

**新手运動来源案例：从 Mixamo 拿動作導入 Blender，作为可控运動基础后再送入 Seedance。**

- 來源筆記：测試 Blender x Seedance，并建议初学者下载 Mixamo motion 導入 Blender。
- 複用角度：适合做 beginner motion-source case。
- 影片預覽:

[![播放示範影片 — Case 14](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case14.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case14.mp4)

類型: Tutorial | 日期: 2026-06-27

---

<a id="case-23"></a>
### Case 23: [只保留位置关系的參考控制](https://x.com/kan_mi_no9/status/2071380621214224403) (by [@kan_mi_no9](https://x.com/kan_mi_no9))

**參考权重案例：只让參考影片约束位置关系，再用 prompt 补回速度感和動态感。**

- 來源筆記：说明通过调低參考影片對動作的约束、聚焦位置关系，补回 Seedance 的速度感和動态感。
- 複用角度：适合做 reference adherence 调参案例。
- 影片預覽:

[![播放示範影片 — Case 23](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case23.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case23.mp4)

類型: Tutorial | 日期: 2026-06-28

---

<a id="case-24"></a>
### Case 24: [用實体玩具替代 3D 软件做參考](https://x.com/gcduncombe/status/2070617538745229546) (by [@gcduncombe](https://x.com/gcduncombe))

**實体參考案例：当不想打开 Blender 时，用玩具快速拍攝运動和 staging 參考。**

- 來源筆記：提出不打开 3D 软件时也可以用玩具拍攝运動/構圖參考，作为 Blender+AI render 讨论的替代路径。
- 複用角度：适合做 physical previs / toy reference 的轻量替代案例。
- 影片預覽:

[![播放示範影片 — Case 24](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case24.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case24.mp4)

類型: Demo | 日期: 2026-06-26

---

<a id="case-26"></a>
### Case 26: [用參考控制修複 prompt 反複失败的場景](https://x.com/kan_mi_no9/status/2071168235022827587) (by [@kan_mi_no9](https://x.com/kan_mi_no9))

**控制兜底案例：prompt-only 反複失败时，用 reference 强制場景成立，即使会损失部分動态。**

- 來源筆記：说明虽然会损失部分 Seedance 自由运鏡和動态，但在必须得到特定画面的場景里很有用。
- 複用角度：适合做“prompt 失败时用 reference 兜底”的案例。
- 影片預覽:

[![播放示範影片 — Case 26](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case26.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case26.mp4)

類型: Demo | 日期: 2026-06-28

---

<a id="case-27"></a>
### Case 27: [角色比例与簡化背景的稳定性技巧](https://x.com/craftcapitallab/status/2070512271391068287) (by [@craftcapitallab](https://x.com/craftcapitallab))

**稳定性 checklist：角色比例不只看头身，还要匹配手脚体积；无须對齐的背景尽量簡化。**

- 來源筆記：总结了让參考更稳定的具体技巧：figure 不只调头身，还要让手脚体积贴合角色设计；不需要對齐的背景尽量簡单。
- 複用角度：适合做 Blender/參考影片的稳定性 checklist。
- 影片預覽:

[![播放示範影片 — Case 27](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case27.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case27.mp4)

類型: Tutorial | 日期: 2026-06-26

---


<a id="case-35"></a>
### Case 35: [人偶動捕配合風格化輸入幀](https://x.com/fatboypink/status/2074087401887039740) (by [@fatboypink](https://x.com/fatboypink))

**可以先用偏僵硬的人偶或 Blender 動作源鎖節奏，再透過輸入幀設計把 Seedance 的風格和布料表現拉回來。**

- 來源筆記: 作者說動作節奏來自偏僵硬的人偶動捕，但手繪輸入幀依然把最終風格和布料擺動拉回到想要的方向。
- 影片預覽:

[![影片預覽 — Case 35](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case35.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case35.mp4)

類型: Demo | 日期: 2026-07-06

---
<a id="production-pipelines-toolchains-cases"></a>
## 🛠️ Production Pipelines & Toolchains / 生產管線與工具鏈

<a id="case-15"></a>
### Case 15: [Hermes/Krea2/ComfyUI/Blender MCP/Seedance 實驗](https://x.com/SamJWasserman/status/2069656428437225826) (by [@SamJWasserman](https://x.com/SamJWasserman))

**多工具 agent 管线：Hermes 安装并連接 Krea、ComfyUI、Blender MCP 和 Seedance，生成圖像与物理參考。**

- 來源筆記：说明 agent 安装 Krea2、連接 ComfyUI 和 Blender MCP，生成 reference image + physical ref vid 后送 Seedance。
- 複用角度：适合做 multi-agent creative pipeline 候选。
- 影片預覽:

[![播放示範影片 — Case 15](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case15.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case15.mp4)

類型: Integration | 日期: 2026-06-24

---

<a id="case-16"></a>
### Case 16: [Blender MCP viewport animation + Seedance/Magnific texture/lighting](https://x.com/techhalla/status/2070814203435274715) (by [@techhalla](https://x.com/techhalla))

**Viewport 到风格化案例：Blender MCP 提供相机和元素控制，再用 Seedance/Magnific 加纹理和光照。**

- 來源筆記：说明 adding 3D gives camera/element control，并声称 exactly how I did it。
- 複用角度：适合做 Blender MCP + style transfer 主案例。
- 影片預覽:

[![播放示範影片 — Case 16](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case16.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case16.mp4)

類型: Integration | 日期: 2026-06-27

---

<a id="case-17"></a>
### Case 17: [Blender 3D previz → Seedance anime render](https://x.com/restofart/status/2070086939756159368) (by [@restofart](https://x.com/restofart))

**3D previz 到動画渲染：用 Seedance 改变画面风格，同时保留 Blender 里的相机运動和動作。**

- 來源筆記：说明 full camera moves and motion preserved，定位 previz → AI-render pipeline。
- 複用角度：适合作为 anime/render pipeline case。
- 影片預覽:

[![播放示範影片 — Case 17](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case17.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case17.mp4)

類型: Integration | 日期: 2026-06-25

---

<a id="case-18"></a>
### Case 18: [FBX clay model + Claude keyframe + Seedance refs](https://x.com/Viggle_PINOC/status/2070183934265012392) (by [@Viggle_PINOC](https://x.com/Viggle_PINOC))

**FBX clay pass 流程：Blender 導入動作，Claude 辅助关键幀相机，渲染后的 clay pass 成为 Seedance 參考影片。**

- 來源筆記：具体 step：Blender 導入 FBX 到 clay model、设置 camera、Claude keyframe camera moves、導出 mp4 给 Seedance refs。
- 複用角度：适合做 FBX/Mixamo 動画參考流程。
- 影片預覽:

[![播放示範影片 — Case 18](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case18.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case18.mp4)

類型: Integration | 日期: 2026-06-25

---


<a id="case-30"></a>
### Case 30: [Fable 編排的舞蹈參考影片流水線](https://x.com/ryo05m/status/2076284841457521043) (by [@ryo05m](https://x.com/ryo05m))

**當純提示詞難以描述舞步時，可以讓 agent 負責角色設計和 Blender 編舞程式碼，再把 15 秒舞蹈參考交給 Seedance。**

- 來源筆記: 作者明確寫了 3 步：Seedream 5 Pro 做角色、Blender 做 15 秒舞蹈人偶、Seedance 2.0 吃動作和鏡頭參考。
- 影片預覽:

[![影片預覽 — Case 30](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case30.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case30.mp4)

類型: Integration | 日期: 2026-07-12

---
<a id="limits-tests-troubleshooting-cases"></a>
## 🧪 Limits, Tests & Troubleshooting / 限制、測試與排查

<a id="case-20"></a>
### Case 20: [不用 start frame 的 Blender blockout reference](https://x.com/magneticskiff/status/2070711034793361559) (by [@magneticskiff](https://x.com/magneticskiff))

**无起始幀变体：当不能依赖 starter frame 时，用 Blender blockout 加详细环境參考也能工作。**

- 來源筆記：说明 Seedance + Blender blockout 可以使用 references 而非 starter frames，环境參考有足够细節时效果较好。
- 複用角度：适合做 reference-only variant 候选。
- 影片預覽:

[![播放示範影片 — Case 20](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case20.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case20.mp4)

類型: Limit | 日期: 2026-06-27

---

<a id="case-25"></a>
### Case 25: [玩具參考 + prompt 补强 + NG 對照](https://x.com/tea_story_hoshi/status/2071002538703479089) (by [@tea_story_hoshi](https://x.com/tea_story_hoshi))

**排查案例：參考影片通常需要 prompt 补强，不能只让模型机械照搬。**

- 來源筆記：同时给出成功例和 NG 例：解析參考影片并用 prompt 补强会更自然，直接忠實參考则動作和姿势容易僵硬。
- 複用角度：适合做 reference video troubleshooting 与 prompt reinforcement 案例。
- 影片預覽:

[![播放示範影片 — Case 25](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case25.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case25.mp4)

類型: Limit | 日期: 2026-06-27

---

<a id="case-28"></a>
### Case 28: [Blender + Seedance 布料物理压力测試](https://x.com/fatboypink/status/2070577334701473800) (by [@fatboypink](https://x.com/fatboypink))

**布料物理压力测試：Blender-guided Seedance 可用，但複杂运動仍需要多轮迭代。**

- 來源筆記：明确把目标设为测試 Seedance 對 cloth physics 的处理能力，并说明这是较难解决的輸出。
- 複用角度：适合做 cloth physics / complex motion stress test 案例。
- 影片預覽:

[![播放示範影片 — Case 28](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case28.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case28.mp4)

類型: Limit | 日期: 2026-06-26

---

<a id="related-repositories"></a>
## 🔗 相關儲存庫

- [查看 Seedance 2.0 提示詞](https://github.com/Evolink-AI/awesome-seedance-2.0-prompts)
- [安裝 Seedance 2 Agent Skill](https://github.com/Evolink-AI/seedance2-video-gen-skill-for-openclaw)
- [查看 GPT Image 2 到 Seedance 2 工作流程](https://github.com/Evolink-AI/GPT-Image-2-Seedance2-Workflow)


<a id="case-31"></a>
### Case 31: [黑幀隔開的關鍵幀節奏修正法](https://x.com/thechriscooper/status/2076092824102240411) (by [@thechriscooper](https://x.com/thechriscooper))

**如果粗糙的 Blender 參考讓 Seedance 連僵硬的中間幀都照搬，就保留關鍵姿勢並把中間幀全部壓成黑幀。**

- 來源筆記: 作者說 Seedance 會把粗糙 Blender 動畫連同僵硬過渡一起照抄，而「關鍵幀-黑幀-關鍵幀」能保住 blocking 但讓成片更順。
- 影片預覽:

[![影片預覽 — Case 31](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case31.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case31.mp4)

類型: Tutorial | 日期: 2026-07-11

---

<a id="case-33"></a>
### Case 33: [複雜場景動作失配測試](https://x.com/sonicpower1970/status/2074322339391824012) (by [@sonicpower1970](https://x.com/sonicpower1970))

**把粗場景 MCP 渲染當作限制測試來看：即使反覆多次，複雜 Blender 場景在 Seedance 裡仍可能偏離預期動作。**

- 來源筆記: 這條後續測試明確寫到：在作者的 Claude→Blender→Seedance 流程裡，複雜場景試了約四次後，動作仍然對不齊。
- 影片預覽:

[![影片預覽 — Case 33](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case33.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case33.mp4)

類型: Limit | 日期: 2026-07-07

---
<a id="acknowledge"></a>
## 🙏 致謝

感謝所有公開分享 Blender + Seedance 工作流程、測試、提示詞、參考影片和製作筆記的創作者，他們的實踐啟發了這個儲存庫。

[@noman23761](https://x.com/noman23761), [@reidhannaford](https://x.com/reidhannaford), [@JMSvid](https://x.com/JMSvid), [@DiabloNemesis](https://x.com/DiabloNemesis), [@koldo2k](https://x.com/koldo2k), [@SamJWasserman](https://x.com/SamJWasserman), [@akiyoshisan](https://x.com/akiyoshisan), [@6_KAKUU](https://x.com/6_KAKUU), [@aidoga_lab](https://x.com/aidoga_lab), [@tanabe_fragm](https://x.com/tanabe_fragm), [@techhalla](https://x.com/techhalla), [@restofart](https://x.com/restofart), [@Viggle_PINOC](https://x.com/Viggle_PINOC), [@magneticskiff](https://x.com/magneticskiff), [@JoshDaws](https://x.com/JoshDaws), [@kan_mi_no9](https://x.com/kan_mi_no9), [@gcduncombe](https://x.com/gcduncombe), [@tea_story_hoshi](https://x.com/tea_story_hoshi), [@craftcapitallab](https://x.com/craftcapitallab), [@fatboypink](https://x.com/fatboypink)

*我們無法保證每個案例都準確歸屬於最初的創作者。如有需要更正之處，請聯絡我們，我們會及時更新。*

想補充 Blender + Seedance 工作流程？可以[提交 use case issue](https://github.com/Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases/issues/new?template=use-case.yml)，參考 [issue 範本](.github/ISSUE_TEMPLATE/use-case.yml)；也可以使用 [PR 範本](.github/PULL_REQUEST_TEMPLATE.md)提交 pull request。

[![Star History Chart](https://api.star-history.com/svg?repos=Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&type=Date)](https://www.star-history.com/#Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&Date)
