<div align="center">

<a href="https://evolink.ai/cookbook/blender-to-video?utm_source=github&utm_medium=banner&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/images/banner.png" alt="Blender + Seedance 유스케이스 저장소 배너" width="760"></a>

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

## 🍌 소개

Blender + Seedance 유스케이스 저장소입니다.

**크리에이터가 Seedance 비디오 생성을 제어하는 데 실제로 사용한 Blender, Blender MCP, 뷰포트, 프리비즈, FBX, Mixamo, ComfyUI 및 에이전트 지원 워크플로를 수집합니다.**

현재 컬렉션은 소유자가 제공한 X/Twitter 데이터에서 선별했습니다. 각 사례는 원본 게시물과 제작자 프로필로 연결됩니다.

먼저 EvoLink Blender-to-video 쿡북을 확인한 다음 아래 빠른 시작을 이 저장소의 워크플로 참고 자료로 활용하세요.

## 📊 개요

- 소유자가 제공한 공개 제작자 게시물 데이터에서 **25개의 Blender + Seedance 사례**를 선별했습니다.
- 카메라 제어, Blender 프리비즈, 다중 캐릭터 블로킹, 액션 안무, Blender MCP, Codex/Claude 지원 블록아웃, FBX/Mixamo 레퍼런스, ComfyUI/스타일 전환, 알려진 한계를 다룹니다.
- 각 사례에는 원본 출처, 제작자 표기, 간결한 핵심 요점, 증거 유형, 게시일이 포함됩니다.
- 공개 목록은 35개 후보 감사에서 시작했고, 지금은 반복 업데이트 루프에서 검증된 주간 추가 7건을 포함합니다.
- 실제 워크플로를 검토한 뒤 설정과 실행은 EvoLink Blender-to-video 쿡북을 이용하세요.

> [!NOTE]
> 이 컬렉션은 과장보다 구체적인 워크플로 근거를 우선합니다. 소스 기반 단계, 레퍼런스 비디오 방식, 에이전트/MCP 활용, 재현 가능한 제약 조건, 명확히 밝힌 한계를 중시합니다.

<a id="quick-start"></a>
## ⚡ 빠른 시작

먼저 로컬 Blender 제어 경로를 설정한 다음 에이전트가 호출할 EvoLink 스킬을 설치합니다.

### 1. Blender MCP 설치

공식 Blender MCP 설정 가이드를 따르고, Blender를 연 뒤 레퍼런스를 만들기 전에 에이전트가 Blender MCP 서버에 연결되는지 확인합니다.

- 공식 설정: [Blender MCP 설정](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

첫 실행 가능한 요청 전에 [API 키 받기](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key)에서 EvoLink 키를 준비하세요.

### 2. EvoLink 스킬 설치

에이전트 워크스페이스에 Seedance 생성 스킬과 Topaz 업스케일링 스킬을 설치합니다.

```bash
npm i evolink-seedance
npm i evolink-topaz-video-upscale
```

### 3. [API 키 받기](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key)

EvoLink 계정에서 API 키를 만들고 에이전트 런타임에서 사용할 수 있도록 설정합니다.

```bash
export EVOLINK_API_KEY="<your-evolink-api-key>"
```

### 4. 에이전트 안에서 실행

MCP, 스킬, API 키가 준비되면 에이전트에게 Blender 블록아웃 제작, 레퍼런스 비디오 내보내기, Seedance 생성, 필요할 경우 최종 클립 업스케일링을 요청합니다.

직접 요청을 보내기 전에 [API 키 받기](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key)에서 키를 확인하세요. 직접 API 폴백이 필요하면 Blender 레퍼런스 워크플로를 `POST https://api.evolink.ai/v1/videos/generations`로 보냅니다.

```bash
curl --request POST \
  --url https://api.evolink.ai/v1/videos/generations \
  --header "Authorization: Bearer ${EVOLINK_API_KEY}" \
  --header 'Content-Type: application/json' \
  --data '{
    "model": "seedance-2.0-reference-to-video",
    "prompt": "Use the Blender blockout video as the motion guide, keep the camera path, and preserve the staged timing.",
    "video_urls": ["https://example.com/blender-blockout.mp4"],
    "image_urls": ["https://example.com/first-frame.jpg"],
    "duration": 5,
    "quality": "720p",
    "aspect_ratio": "16:9",
    "generate_audio": true
  }'
```

이 워크플로를 곧바로 에이전트에 넘길 예정이라면 먼저 같은 키를 [API 키 받기](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key)에서 확인하세요.

```text
Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.
```

> [!NOTE]
> Blender 쪽 설치 세부사항은 Blender MCP 설정 페이지를 기준으로 합니다.

## 📑 메뉴

| 섹션 | 사례 |
|---|---|
| [🎥 카메라 제어와 프리비즈](#camera-control-previs) | Case 1, 2, 3, 4, 5, 29 |
| [🎬 캐릭터와 액션 블로킹](#character-action-blocking) | Case 6, 8, 9, 21, 32 |
| [🤖 에이전트 기반 Blender MCP](#agentic-blender-mcp) | Case 10, 11, 22, 34 |
| [🧩 레퍼런스, 프롬프트 및 다중 입력 매핑](#reference-prompt-multi-input-mapping) | Case 13, 14, 23, 24, 26, 27, 35 |
| [🛠️ 제작 파이프라인과 툴체인](#production-pipelines-toolchains) | Case 15, 16, 17, 18, 30 |
| [🧪 한계, 테스트 및 문제 해결](#limits-tests-troubleshooting) | Case 20, 25, 28, 31, 33 |
| [🙏 감사의 말](#acknowledge) | 크레딧 및 정정 정책 |

<a id="camera-control-previs"></a>
### 🎥 카메라 제어와 프리비즈

| 사례 | 보여주는 것 | Type |
|---|---|---|
| [Seedance 모션 레퍼런스로 사용하는 Blender 블록아웃](#case-1) | 통합 연출 워크플로입니다. 원본 사례의 전체 그레이박스 방식을 사용한 뒤 Seedance 생성 전에 액션 프리비즈의 타이밍, 속도, 흔들림, 공간 안무까지 구체화합니다. | Demo |
| [Midjourney 시작 프레임을 활용한 카메라 블로킹](#case-2) | 정밀 카메라 제어를 위한 간결한 방식입니다. Blender가 카메라 움직임을 제공하고 Midjourney가 시작 프레임을 만들며 Seedance가 모션 레퍼런스를 따릅니다. | Demo |
| [Blender 프리비즈를 활용한 ComfyUI 카메라 제어](#case-3) | Blender 프리비즈에 정방향과 상하 반전 레퍼런스 프레임을 각각 결합해 모션 추종성을 시험한 ComfyUI 제어 사례입니다. | Demo |
| [뷰포트 프리뷰에서 사실적인 시작 프레임으로](#case-4) | 짧은 뷰포트 프리뷰 튜토리얼입니다. 장면을 블록아웃하고 프리뷰를 내보낸 뒤 첫 프레임을 사실적으로 바꾸고 두 레퍼런스를 모두 Seedance에 제공합니다. | Demo |
| [하나의 레퍼런스 비디오로 여러 세계 만들기](#case-5) | 동일한 Blender 레퍼런스 비디오로 Seedance에서 서로 다른 세계를 생성한 스타일·세계 변형 사례입니다. | Demo |
| [대사에 맞춘 iPhone 카메라 프리비즈](#case-29) | iPhone으로 구동한 Blender 카메라 패스를 대사에 맞춘 뒤, 그 오디오 포함 프리비즈와 두 장의 이미지를 Seedance에 넣어 쇼트 계획에 사용합니다. | Integration |


<a id="character-action-blocking"></a>
### 🎬 캐릭터와 액션 블로킹

| 사례 | 보여주는 것 | Type |
|---|---|---|
| [포즈를 맞춘 다중 캐릭터 대화](#case-6) | Seedance가 연기 장면을 생성하기 전에 Blender로 캐릭터 포즈와 카메라 움직임을 맞추는 대화 숏 워크플로입니다. | Demo |
| [공간을 가로지르는 핸드헬드 추적 카메라](#case-8) | Blender로 캐릭터가 공간을 이동하는 방식을 제어하고 Seedance가 거친 카메라 움직임을 최종 비디오에 반영하는 핸드헬드 추적 사례입니다. | Demo |
| [전술 액션을 위한 카메라 및 캐릭터 블로킹](#case-9) | 생성 전에 Blender로 카메라 궤도, 렌즈 선택, 엄폐 위치, 총격 타이밍, 캐릭터 움직임을 연출한 전술 블로킹 사례입니다. | Demo |
| [단순한 카메라 이동을 넘어선 매복 장면 프리비즈](#case-21) | Seedance가 숏을 생성하기 전에 Blender 프리비즈로 장면 구성, 타이밍, 카메라 움직임을 해결하는 매복 장면 사례입니다. | Demo |
| [장애물이 있는 옥상 파쿠르 추격](#case-32) | Seedance가 직선 달리기로 단순화될 때는 장애물 상호작용과 회피 비트를 포함한 Blender 파쿠르 프리비즈를 먼저 만듭니다. | Demo |


<a id="agentic-blender-mcp"></a>
### 🤖 에이전트 기반 Blender MCP

| 사례 | 보여주는 것 | Type |
|---|---|---|
| [Codex + Blender MCP 레퍼런스 비디오 워크플로](#case-10) | Codex가 간단한 3D 시장, 고양이 움직임, 카메라 구도, Seedance용 MP4 레퍼런스를 제작한 에이전트형 Blender MCP 사례입니다. | Integration |
| [Codex로 구축한 건축 및 카메라 워크](#case-11) | Codex의 도움으로 Blender에서 건축과 카메라 워크를 생성한 뒤 Seedance 레퍼런스 모션으로 시험한 초보자 사례입니다. | Integration |
| [Claude로 몇 분 만에 제작한 Blender MCP 프리비즈](#case-22) | Claude가 Blender MCP를 사용해 2~3분 안에 숏 레퍼런스를 제작한 빠른 에이전트형 프리비즈 사례입니다. | Integration |
| [Fable 스킬을 Codex로 이식](#case-34) | 에이전트에게 Blender 레퍼런스 비디오 스킬을 만들게 하고 Codex로 옮긴 뒤, 프롬프트 없이도 Seedance가 움직임을 정리할 수 있는지 확인합니다. | Integration |


<a id="reference-prompt-multi-input-mapping"></a>
### 🧩 레퍼런스, 프롬프트 및 다중 입력 매핑

| 사례 | 보여주는 것 | Type |
|---|---|---|
| [Blender 레퍼런스를 활용한 재현 가능한 Seedance 프롬프트](#case-13) | 재현성과 문제 해결을 통합한 사례입니다. 설정에서 레퍼런스 비디오 조건을 명시하고 짝을 이룬 테스트에서 카메라·리듬 제어가 작동한 부분과 발 움직임이 실패한 부분을 기록합니다. | Tutorial |
| [초보자용 Blender 레퍼런스로 활용하는 Mixamo 모션](#case-14) | 초보자 친화적인 모션 소스 사례입니다. 레퍼런스를 Seedance에 보내기 전에 Blender의 Mixamo 모션을 제어 가능한 움직임 기반으로 사용합니다. | Tutorial |
| [더 빠른 장면을 위한 위치 전용 레퍼런스 제어](#case-23) | 레퍼런스 가중치 조정 사례입니다. 위치 제어에는 레퍼런스를 활용하면서 프롬프트로 속도와 역동성을 회복합니다. | Tutorial |
| [3D 소프트웨어 대신 실물 장난감을 레퍼런스로 활용](#case-24) | 실물 레퍼런스 사례입니다. Blender를 여는 부담이 클 때 장난감을 빠른 모션 및 장면 구성 레퍼런스로 활용합니다. | Demo |
| [프롬프트 생성에 실패한 특정 장면을 위한 레퍼런스 제어](#case-26) | 제어 대안을 보여 주는 사례입니다. 프롬프트만으로 생성에 실패하면 일부 역동성이 줄더라도 레퍼런스를 사용해 장면을 구현합니다. | Demo |
| [캐릭터 비율 및 단순한 배경 팁](#case-27) | 안정성 체크리스트 사례입니다. 키뿐 아니라 캐릭터 전체 비율을 맞추고 정밀한 정렬이 필요 없는 배경은 단순화합니다. | Tutorial |
| [마네킹 모캡과 스타일 프레임 조합](#case-35) | 딱딱한 Blender나 마네킹 모션 소스로 타이밍을 고정하고, 입력 프레임 디자인으로 Seedance의 최종 스타일과 천 움직임을 조정합니다. | Demo |


<a id="production-pipelines-toolchains"></a>
### 🛠️ 제작 파이프라인과 툴체인

| 사례 | 보여주는 것 | Type |
|---|---|---|
| [Hermes, Krea, ComfyUI 및 Blender MCP 스택](#case-15) | Hermes가 Krea, ComfyUI, Blender MCP, Seedance를 설치하고 연결해 이미지 및 실물 레퍼런스를 모두 제작하는 다중 도구 에이전트 파이프라인입니다. | Integration |
| [Blender MCP 뷰포트에서 Seedance로 스타일 전환](#case-16) | 뷰포트에서 스타일 전환으로 이어지는 사례입니다. Blender MCP가 카메라와 요소를 제어하고 Seedance/Magnific이 텍스처와 조명을 추가합니다. | Integration |
| [Blender 프리비즈에서 Seedance 애니메이션 렌더로](#case-17) | Seedance가 렌더 스타일을 바꾸면서도 카메라 움직임과 모션을 유지하는 3D 프리비즈-애니메이션 사례입니다. | Integration |
| [Claude가 키프레임을 설정한 카메라를 활용한 FBX 클레이 패스](#case-18) | Blender가 모션을 가져오고 Claude가 카메라 움직임의 키프레임 설정을 도우며 렌더링한 클레이 패스를 Seedance 레퍼런스 비디오로 사용하는 FBX 워크플로입니다. | Integration |
| [Fable이 짠 댄스 레퍼런스 파이프라인](#case-30) | 프롬프트만으로는 동작이 거칠 때 에이전트에게 캐릭터 설계와 Blender 안무 코드를 맡기고 15초 댄스 레퍼런스를 Seedance에 넘깁니다. | Integration |


<a id="limits-tests-troubleshooting"></a>
### 🧪 한계, 테스트 및 문제 해결

| 사례 | 보여주는 것 | Type |
|---|---|---|
| [시작 프레임 없는 레퍼런스 전용 Blender 블록아웃](#case-20) | 시작 프레임에 의존할 수 없는 워크플로에서도 Blender 블록아웃과 상세한 환경 레퍼런스를 결합하면 작동할 수 있음을 보여 주는 변형 사례입니다. | Limit |
| [장난감 레퍼런스 프롬프트 보강 및 실패 사례](#case-25) | 레퍼런스 비디오를 그대로 모방시키기보다 프롬프트 보강이 필요한 이유를 보여 주는 문제 해결 사례입니다. | Limit |
| [Blender와 Seedance를 활용한 천 물리 스트레스 테스트](#case-28) | Blender로 유도한 Seedance가 작동하는 범위와 어려운 움직임에서는 반복 조정이 필요함을 보여 주는 천 물리 스트레스 테스트입니다. | Limit |
| [블랙 프레임 키프레임 타이밍 보정](#case-31) | 거친 Blender 레퍼런스가 중간 동작까지 로봇처럼 복제되면 키 포즈만 남기고 사이 프레임을 검게 처리합니다. | Tutorial |
| [복잡한 장면에서의 모션 불일치 테스트](#case-33) | 거친 장면 MCP 렌더는 한계 테스트로 봐야 하며, 복잡한 Blender 장면은 여러 번의 Seedance 시도 뒤에도 의도한 움직임에서 벗어날 수 있습니다. | Limit |



<a id="camera-control-previs-cases"></a>
## 🎥 카메라 제어와 프리비즈

<a id="case-1"></a>
### Case 1: [Seedance 모션 레퍼런스로 사용하는 Blender 블록아웃](https://x.com/noman23761/status/2071534020014563328) (작성자: [@noman23761](https://x.com/noman23761))

**통합 연출 워크플로입니다. 원본 사례의 전체 그레이박스 방식을 사용한 뒤 Seedance 생성 전에 액션 프리비즈의 타이밍, 속도, 흔들림, 공간 안무까지 구체화합니다.**

- 소스 메모: 이전 Case 7과 통합했습니다. 두 소스를 함께 보면 전체 그레이박스 워크플로와 대략적인 타이밍, 속도, 흔들림, 공간 안무를 포함한 액션 프리비즈 변형을 확인할 수 있습니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case1.mp4)

Type: Demo | Date: 2026-06-29

---

<a id="case-2"></a>
### Case 2: [Midjourney 시작 프레임을 활용한 카메라 블로킹](https://x.com/reidhannaford/status/2069074506849685773) (작성자: [@reidhannaford](https://x.com/reidhannaford))

**정밀 카메라 제어를 위한 간결한 방식입니다. Blender가 카메라 움직임을 제공하고 Midjourney가 시작 프레임을 만들며 Seedance가 모션 레퍼런스를 따릅니다.**

- 소스 메모: 소스는 명확한 3단계 워크플로를 제시하며 생성된 비디오가 Blender 카메라 움직임을 가깝게 추종했다고 보고합니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case2.mp4)

Type: Demo | Date: 2026-06-22

---

<a id="case-3"></a>
### Case 3: [Blender 프리비즈를 활용한 ComfyUI 카메라 제어](https://x.com/JMSvid/status/2070258132840796579) (작성자: [@JMSvid](https://x.com/JMSvid))

**Blender 프리비즈에 정방향과 상하 반전 레퍼런스 프레임을 각각 결합해 모션 추종성을 시험한 ComfyUI 제어 사례입니다.**

- 소스 메모: ComfyUI 방식의 제어 설정에서 Blender 프리비즈와 여러 정지 이미지 레퍼런스를 결합했다는 점이 유용합니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case3.mp4)

Type: Demo | Date: 2026-06-25

---

<a id="case-4"></a>
### Case 4: [뷰포트 프리뷰에서 사실적인 시작 프레임으로](https://x.com/DiabloNemesis/status/2070441923706503380) (작성자: [@DiabloNemesis](https://x.com/DiabloNemesis))

**짧은 뷰포트 프리뷰 튜토리얼입니다. 장면을 블록아웃하고 프리뷰를 내보낸 뒤 첫 프레임을 사실적으로 바꾸고 두 레퍼런스를 모두 Seedance에 제공합니다.**

- 소스 메모: 게시물은 뷰포트 프리뷰, 첫 프레임 이미지, Seedance 레퍼런스 비디오라는 구체적인 결과물과 함께 간결한 워크플로를 제시합니다. 공개 사례에 동일한 비디오가 한 번만 표시되도록 중복된 Case 29 미디어를 제거했습니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case4.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case4.mp4)

Type: Demo | Date: 2026-06-26

---

<a id="case-5"></a>
### Case 5: [하나의 레퍼런스 비디오로 여러 세계 만들기](https://x.com/koldo2k/status/2071307945002815967) (작성자: [@koldo2k](https://x.com/koldo2k))

**동일한 Blender 레퍼런스 비디오로 Seedance에서 서로 다른 세계를 생성한 스타일·세계 변형 사례입니다.**

- 소스 메모: 동일한 레퍼런스 비디오를 사용하면서 모션 제어와 세계·스타일 변형을 분리했다는 점이 유용합니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 5](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case5.mp4)

Type: Demo | Date: 2026-06-28

---


<a id="case-29"></a>
### Case 29: [대사에 맞춘 iPhone 카메라 프리비즈](https://x.com/CoffeeVectors/status/2076397975853551924) (작성자: [@CoffeeVectors](https://x.com/CoffeeVectors))

**iPhone으로 구동한 Blender 카메라 패스를 대사에 맞춘 뒤, 그 오디오 포함 프리비즈와 두 장의 이미지를 Seedance에 넣어 쇼트 계획에 사용합니다.**

- 소스 메모: 소스는 iPhone으로 구동한 Blender 카메라를 대사에 맞춘 뒤 그 오디오 포함 프리비즈를 두 장의 정지 이미지와 함께 Seedance 2에 전달합니다.
- 비디오 미리보기:

[![비디오 미리보기 — Case 29](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case29.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case29.mp4)

Type: Integration | Date: 2026-07-12

---
<a id="character-action-blocking-cases"></a>
## 🎬 캐릭터와 액션 블로킹

<a id="case-6"></a>
### Case 6: [포즈를 맞춘 다중 캐릭터 대화](https://x.com/reidhannaford/status/2069420552394043625) (작성자: [@reidhannaford](https://x.com/reidhannaford))

**Seedance가 연기 장면을 생성하기 전에 Blender로 캐릭터 포즈와 카메라 움직임을 맞추는 대화 숏 워크플로입니다.**

- 소스 메모: 다중 캐릭터 대화와 포즈 매칭이 추가되어 단일 캐릭터 카메라 제어 데모와 구별됩니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 6](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case6.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case6.mp4)

Type: Demo | Date: 2026-06-23

---

<a id="case-8"></a>
### Case 8: [공간을 가로지르는 핸드헬드 추적 카메라](https://x.com/reidhannaford/status/2070507963429671062) (작성자: [@reidhannaford](https://x.com/reidhannaford))

**Blender로 캐릭터가 공간을 이동하는 방식을 제어하고 Seedance가 거친 카메라 움직임을 최종 비디오에 반영하는 핸드헬드 추적 사례입니다.**

- 소스 메모: 카메라가 따라가는 동안 캐릭터를 장면 안에서 이동시키므로 핸드헬드 이동 숏에 유용합니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

프리뷰를 사용할 수 없습니다. 원본 GitHub 첨부 파일은 더 이상 공개적으로 접근할 수 없습니다.

Type: Demo | Date: 2026-06-26

---

<a id="case-9"></a>
### Case 9: [전술 액션을 위한 카메라 및 캐릭터 블로킹](https://x.com/SamJWasserman/status/2070742850095230991) (작성자: [@SamJWasserman](https://x.com/SamJWasserman))

**생성 전에 Blender로 카메라 궤도, 렌즈 선택, 엄폐 위치, 총격 타이밍, 캐릭터 움직임을 연출한 전술 블로킹 사례입니다.**

- 소스 메모: 카메라와 캐릭터 블로킹을 동시에 보여 주므로 단순한 카메라 전용 레퍼런스보다 강력합니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 9](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case9.mp4)

Type: Demo | Date: 2026-06-27

---

<a id="case-21"></a>
### Case 21: [단순한 카메라 이동을 넘어선 매복 장면 프리비즈](https://x.com/reidhannaford/status/2071595581508563168) (작성자: [@reidhannaford](https://x.com/reidhannaford))

**Seedance가 숏을 생성하기 전에 Blender 프리비즈로 장면 구성, 타이밍, 카메라 움직임을 해결하는 매복 장면 사례입니다.**

- 소스 메모: Case 21로 요청되었습니다. 단순한 카메라 이동을 넘어 장면 구성까지 워크플로를 확장하므로 Reid Hannaford의 별도 사례로 유지했습니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 21](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case21.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case21.mp4)

Type: Demo | Date: 2026-06-29

---


<a id="case-32"></a>
### Case 32: [장애물이 있는 옥상 파쿠르 추격](https://x.com/moframe2026/status/2075203485604470965) (작성자: [@moframe2026](https://x.com/moframe2026))

**Seedance가 직선 달리기로 단순화될 때는 장애물 상호작용과 회피 비트를 포함한 Blender 파쿠르 프리비즈를 먼저 만듭니다.**

- 소스 메모: 작성자는 Blender 파쿠르 프리비즈를 비디오 레퍼런스로 사용했고, 단순한 달리기 이상으로 장애물 활용과 회피 흐름을 넣기 위해 Blender가 필요했다고 말합니다.
- 비디오 미리보기:

[![비디오 미리보기 — Case 32](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case32.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case32.mp4)

Type: Demo | Date: 2026-07-09

---
<a id="agentic-blender-mcp-cases"></a>
## 🤖 에이전트 기반 Blender MCP

<a id="case-10"></a>
### Case 10: [Codex + Blender MCP 레퍼런스 비디오 워크플로](https://x.com/akiyoshisan/status/2071081230108660199) (작성자: [@akiyoshisan](https://x.com/akiyoshisan))

**Codex가 간단한 3D 시장, 고양이 움직임, 카메라 구도, Seedance용 MP4 레퍼런스를 제작한 에이전트형 Blender MCP 사례입니다.**

- 소스 메모: 작성자는 다른 크리에이터에게서 영감을 받았다고 밝혔지만 설명된 장면, 움직임, 카메라, 내보내기 과정은 작성자 본인의 실험입니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 10](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case10.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case10.mp4)

Type: Integration | Date: 2026-06-28

---

<a id="case-11"></a>
### Case 11: [Codex로 구축한 건축 및 카메라 워크](https://x.com/6_KAKUU/status/2071051063663452374) (작성자: [@6_KAKUU](https://x.com/6_KAKUU))

**Codex의 도움으로 Blender에서 건축과 카메라 워크를 생성한 뒤 Seedance 레퍼런스 모션으로 시험한 초보자 사례입니다.**

- 소스 메모: Seedance를 사용하기 전에 건축과 카메라 워크를 Codex에 맡기는 초보자용 Codex 워크플로로서 가치가 있습니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 11](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case11.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case11.mp4)

Type: Integration | Date: 2026-06-28

---

<a id="case-22"></a>
### Case 22: [Claude로 몇 분 만에 제작한 Blender MCP 프리비즈](https://x.com/JoshDaws/status/2071401550845481090) (작성자: [@JoshDaws](https://x.com/JoshDaws))

**Claude가 Blender MCP를 사용해 2~3분 안에 숏 레퍼런스를 제작한 빠른 에이전트형 프리비즈 사례입니다.**

- 소스 메모: Case 22로 요청되었습니다. 수동 Blender 작업보다 속도와 에이전트 제어를 보여 주므로 유지했습니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 22](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case22.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case22.mp4)

Type: Integration | Date: 2026-06-29

---


<a id="case-34"></a>
### Case 34: [Fable 스킬을 Codex로 이식](https://x.com/mugi_AI_Art/status/2074259600342163846) (작성자: [@mugi_AI_Art](https://x.com/mugi_AI_Art))

**에이전트에게 Blender 레퍼런스 비디오 스킬을 만들게 하고 Codex로 옮긴 뒤, 프롬프트 없이도 Seedance가 움직임을 정리할 수 있는지 확인합니다.**

- 소스 메모: 작성자는 Fable이 Blender 레퍼런스 비디오 스킬을 만들게 한 뒤 이를 Codex로 옮기고, 거친 모델 레퍼런스에서 프롬프트 없이 Seedance 생성을 실행했습니다.
- 비디오 미리보기:

[![비디오 미리보기 — Case 34](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case34.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case34.mp4)

Type: Integration | Date: 2026-07-06

---
<a id="reference-prompt-multi-input-mapping-cases"></a>
## 🧩 레퍼런스, 프롬프트 및 다중 입력 매핑

<a id="case-13"></a>
### Case 13: [Blender 레퍼런스를 활용한 재현 가능한 Seedance 프롬프트](https://x.com/aidoga_lab/status/2070864815275585913) (작성자: [@aidoga_lab](https://x.com/aidoga_lab))

**재현성과 문제 해결을 통합한 사례입니다. 설정에서 레퍼런스 비디오 조건을 명시하고 짝을 이룬 테스트에서 카메라·리듬 제어가 작동한 부분과 발 움직임이 실패한 부분을 기록합니다.**

- 소스 메모: 이전 Case 19와 통합했습니다. 두 사례를 함께 유지해 재현 가능한 설정과 발 미끄러짐에 관한 한계 기록을 모두 보존했습니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case13.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.mp4)

![참조 이미지 — Case 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.jpg)

Type: Tutorial | Date: 2026-06-27

---

<a id="case-14"></a>
### Case 14: [초보자용 Blender 레퍼런스로 활용하는 Mixamo 모션](https://x.com/tanabe_fragm/status/2070685291183243459) (작성자: [@tanabe_fragm](https://x.com/tanabe_fragm))

**초보자 친화적인 모션 소스 사례입니다. 레퍼런스를 Seedance에 보내기 전에 Blender의 Mixamo 모션을 제어 가능한 움직임 기반으로 사용합니다.**

- 소스 메모: Blender 레퍼런스 비디오의 실용적인 모션 소스로 Mixamo를 명시하므로 초보자에게 유용합니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 14](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case14.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case14.mp4)

Type: Tutorial | Date: 2026-06-27

---

<a id="case-23"></a>
### Case 23: [더 빠른 장면을 위한 위치 전용 레퍼런스 제어](https://x.com/kan_mi_no9/status/2071380621214224403) (작성자: [@kan_mi_no9](https://x.com/kan_mi_no9))

**레퍼런스 가중치 조정 사례입니다. 위치 제어에는 레퍼런스를 활용하면서 프롬프트로 속도와 역동성을 회복합니다.**

- 소스 메모: Case 23으로 요청되었습니다. 짝을 이루는 kan_mi_no9 테스트와 함께 별도의 레퍼런스 제어 변형으로 유지했습니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 23](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case23.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case23.mp4)

Type: Tutorial | Date: 2026-06-28

---

<a id="case-24"></a>
### Case 24: [3D 소프트웨어 대신 실물 장난감을 레퍼런스로 활용](https://x.com/gcduncombe/status/2070617538745229546) (작성자: [@gcduncombe](https://x.com/gcduncombe))

**실물 레퍼런스 사례입니다. Blender를 여는 부담이 클 때 장난감을 빠른 모션 및 장면 구성 레퍼런스로 활용합니다.**

- 소스 메모: Case 24로 요청되었습니다. 레퍼런스 비디오 개념을 소프트웨어 전용 프리비즈 너머로 확장하므로 유지했습니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 24](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case24.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case24.mp4)

Type: Demo | Date: 2026-06-26

---

<a id="case-26"></a>
### Case 26: [프롬프트 생성에 실패한 특정 장면을 위한 레퍼런스 제어](https://x.com/kan_mi_no9/status/2071168235022827587) (작성자: [@kan_mi_no9](https://x.com/kan_mi_no9))

**제어 대안을 보여 주는 사례입니다. 프롬프트만으로 생성에 실패하면 일부 역동성이 줄더라도 레퍼런스를 사용해 장면을 구현합니다.**

- 소스 메모: Case 26으로 요청되었습니다. 뒤의 kan_mi_no9 변형 사례와 짝을 이루는 실전 사례로 유지했습니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 26](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case26.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case26.mp4)

Type: Demo | Date: 2026-06-28

---

<a id="case-27"></a>
### Case 27: [캐릭터 비율 및 단순한 배경 팁](https://x.com/craftcapitallab/status/2070512271391068287) (작성자: [@craftcapitallab](https://x.com/craftcapitallab))

**안정성 체크리스트 사례입니다. 키뿐 아니라 캐릭터 전체 비율을 맞추고 정밀한 정렬이 필요 없는 배경은 단순화합니다.**

- 소스 메모: Case 27로 요청되었습니다. 구체적이고 재사용 가능한 설정 조언을 제공하므로 유지했습니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 27](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case27.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case27.mp4)

Type: Tutorial | Date: 2026-06-26

---


<a id="case-35"></a>
### Case 35: [마네킹 모캡과 스타일 프레임 조합](https://x.com/fatboypink/status/2074087401887039740) (작성자: [@fatboypink](https://x.com/fatboypink))

**딱딱한 Blender나 마네킹 모션 소스로 타이밍을 고정하고, 입력 프레임 디자인으로 Seedance의 최종 스타일과 천 움직임을 조정합니다.**

- 소스 메모: 작성자는 딱딱한 마네킹 모캡이 움직임 타이밍을 담당했지만 손으로 그린 입력 프레임이 원하는 스타일과 천 움직임을 끝까지 밀어 주었다고 설명합니다.
- 비디오 미리보기:

[![비디오 미리보기 — Case 35](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case35.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case35.mp4)

Type: Demo | Date: 2026-07-06

---
<a id="production-pipelines-toolchains-cases"></a>
## 🛠️ 제작 파이프라인과 툴체인

<a id="case-15"></a>
### Case 15: [Hermes, Krea, ComfyUI 및 Blender MCP 스택](https://x.com/SamJWasserman/status/2069656428437225826) (작성자: [@SamJWasserman](https://x.com/SamJWasserman))

**Hermes가 Krea, ComfyUI, Blender MCP, Seedance를 설치하고 연결해 이미지 및 실물 레퍼런스를 모두 제작하는 다중 도구 에이전트 파이프라인입니다.**

- 소스 메모: 수동 Blender 프리비즈에 그치지 않고 에이전트가 구축한 더 폭넓은 크리에이티브 스택을 보여 줍니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 15](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case15.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case15.mp4)

Type: Integration | Date: 2026-06-24

---

<a id="case-16"></a>
### Case 16: [Blender MCP 뷰포트에서 Seedance로 스타일 전환](https://x.com/techhalla/status/2070814203435274715) (작성자: [@techhalla](https://x.com/techhalla))

**뷰포트에서 스타일 전환으로 이어지는 사례입니다. Blender MCP가 카메라와 요소를 제어하고 Seedance/Magnific이 텍스처와 조명을 추가합니다.**

- 소스 메모: 뷰포트 애니메이션과 후속 스타일·조명 단계를 설명하므로 techhalla 소스 중 근거가 더 강합니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 16](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case16.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case16.mp4)

Type: Integration | Date: 2026-06-27

---

<a id="case-17"></a>
### Case 17: [Blender 프리비즈에서 Seedance 애니메이션 렌더로](https://x.com/restofart/status/2070086939756159368) (작성자: [@restofart](https://x.com/restofart))

**Seedance가 렌더 스타일을 바꾸면서도 카메라 움직임과 모션을 유지하는 3D 프리비즈-애니메이션 사례입니다.**

- 소스 메모: 카메라 움직임을 유지하면서 Blender 3D 프리비즈를 애니메이션 렌더로 변환하는 워크플로라고 소스가 직접 설명합니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 17](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case17.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case17.mp4)

Type: Integration | Date: 2026-06-25

---

<a id="case-18"></a>
### Case 18: [Claude가 키프레임을 설정한 카메라를 활용한 FBX 클레이 패스](https://x.com/Viggle_PINOC/status/2070183934265012392) (작성자: [@Viggle_PINOC](https://x.com/Viggle_PINOC))

**Blender가 모션을 가져오고 Claude가 카메라 움직임의 키프레임 설정을 도우며 렌더링한 클레이 패스를 Seedance 레퍼런스 비디오로 사용하는 FBX 워크플로입니다.**

- 소스 메모: 구체적인 FBX-클레이 패스 과정을 제시하며 레퍼런스 내보내기 전 카메라 키프레임 설정도 포함합니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 18](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case18.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case18.mp4)

Type: Integration | Date: 2026-06-25

---


<a id="case-30"></a>
### Case 30: [Fable이 짠 댄스 레퍼런스 파이프라인](https://x.com/ryo05m/status/2076284841457521043) (작성자: [@ryo05m](https://x.com/ryo05m))

**프롬프트만으로는 동작이 거칠 때 에이전트에게 캐릭터 설계와 Blender 안무 코드를 맡기고 15초 댄스 레퍼런스를 Seedance에 넘깁니다.**

- 소스 메모: 작성자는 Seedream 5 Pro로 캐릭터 설계, Blender로 15초 마네킹 댄스, Seedance 2.0으로 모션과 카메라 레퍼런스를 넣는 3단계를 명시했습니다.
- 비디오 미리보기:

[![비디오 미리보기 — Case 30](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case30.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case30.mp4)

Type: Integration | Date: 2026-07-12

---
<a id="limits-tests-troubleshooting-cases"></a>
## 🧪 한계, 테스트 및 문제 해결

<a id="case-20"></a>
### Case 20: [시작 프레임 없는 레퍼런스 전용 Blender 블록아웃](https://x.com/magneticskiff/status/2070711034793361559) (작성자: [@magneticskiff](https://x.com/magneticskiff))

**시작 프레임에 의존할 수 없는 워크플로에서도 Blender 블록아웃과 상세한 환경 레퍼런스를 결합하면 작동할 수 있음을 보여 주는 변형 사례입니다.**

- 소스 메모: 일반적인 시작 프레임 의존성을 레퍼런스 이미지로 대체하는 중요한 변형을 다룹니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 20](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case20.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case20.mp4)

Type: Limit | Date: 2026-06-27

---

<a id="case-25"></a>
### Case 25: [장난감 레퍼런스 프롬프트 보강 및 실패 사례](https://x.com/tea_story_hoshi/status/2071002538703479089) (작성자: [@tea_story_hoshi](https://x.com/tea_story_hoshi))

**레퍼런스 비디오를 그대로 모방시키기보다 프롬프트 보강이 필요한 이유를 보여 주는 문제 해결 사례입니다.**

- 소스 메모: Case 25로 요청되었습니다. 성공 사례와 실패 비교를 모두 포함하므로 유지했습니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 25](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case25.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case25.mp4)

Type: Limit | Date: 2026-06-27

---

<a id="case-28"></a>
### Case 28: [Blender와 Seedance를 활용한 천 물리 스트레스 테스트](https://x.com/fatboypink/status/2070577334701473800) (작성자: [@fatboypink](https://x.com/fatboypink))

**Blender로 유도한 Seedance가 작동하는 범위와 어려운 움직임에서는 반복 조정이 필요함을 보여 주는 천 물리 스트레스 테스트입니다.**

- 소스 메모: Case 28로 요청되었습니다. 구체적인 한계·스트레스 테스트 사례로 유지했습니다.
- 감사 상태: 중복 및 독창성 수동 검토 후 유지.
- 비디오 미리보기:

[![데모 동영상 재생 — Case 28](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case28.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case28.mp4)

Type: Limit | Date: 2026-06-26

---

<a id="related-repositories"></a>
## 🔗 관련 저장소

- [Seedance 2.0 프롬프트 보기](https://github.com/Evolink-AI/awesome-seedance-2.0-prompts)
- [Seedance 2 에이전트 스킬 설치](https://github.com/Evolink-AI/seedance2-video-gen-skill-for-openclaw)
- [GPT Image 2에서 Seedance 2로 이어지는 워크플로 보기](https://github.com/Evolink-AI/GPT-Image-2-Seedance2-Workflow)


<a id="case-31"></a>
### Case 31: [블랙 프레임 키프레임 타이밍 보정](https://x.com/thechriscooper/status/2076092824102240411) (작성자: [@thechriscooper](https://x.com/thechriscooper))

**거친 Blender 레퍼런스가 중간 동작까지 로봇처럼 복제되면 키 포즈만 남기고 사이 프레임을 검게 처리합니다.**

- 소스 메모: 작성자에 따르면 거친 Blender 애니메이션 전체를 넣으면 Seedance가 어색한 중간 동작까지 그대로 복제했지만, 키프레임-블랙-키프레임 패턴은 블로킹을 유지하면서 움직임을 더 부드럽게 만들었습니다.
- 비디오 미리보기:

[![비디오 미리보기 — Case 31](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case31.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case31.mp4)

Type: Tutorial | Date: 2026-07-11

---

<a id="case-33"></a>
### Case 33: [복잡한 장면에서의 모션 불일치 테스트](https://x.com/sonicpower1970/status/2074322339391824012) (작성자: [@sonicpower1970](https://x.com/sonicpower1970))

**거친 장면 MCP 렌더는 한계 테스트로 봐야 하며, 복잡한 Blender 장면은 여러 번의 Seedance 시도 뒤에도 의도한 움직임에서 벗어날 수 있습니다.**

- 소스 메모: 이 후속 보고는 작성자의 Claude→Blender→Seedance 테스트에서 약 네 번 시도한 뒤에도 복잡한 장면이 의도한 움직임에 맞지 않았다고 말합니다.
- 비디오 미리보기:

[![비디오 미리보기 — Case 33](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case33.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case33.mp4)

Type: Limit | Date: 2026-07-07

---
<a id="acknowledge"></a>
## 🙏 감사의 말

이 저장소는 Blender + Seedance 워크플로, 테스트, 프롬프트, 레퍼런스 비디오, 제작 메모를 공개적으로 공유한 크리에이터들에게서 영감을 받았습니다.

[@noman23761](https://x.com/noman23761), [@reidhannaford](https://x.com/reidhannaford), [@JMSvid](https://x.com/JMSvid), [@DiabloNemesis](https://x.com/DiabloNemesis), [@koldo2k](https://x.com/koldo2k), [@SamJWasserman](https://x.com/SamJWasserman), [@akiyoshisan](https://x.com/akiyoshisan), [@6_KAKUU](https://x.com/6_KAKUU), [@aidoga_lab](https://x.com/aidoga_lab), [@tanabe_fragm](https://x.com/tanabe_fragm), [@techhalla](https://x.com/techhalla), [@restofart](https://x.com/restofart), [@Viggle_PINOC](https://x.com/Viggle_PINOC), [@magneticskiff](https://x.com/magneticskiff), [@JoshDaws](https://x.com/JoshDaws), [@kan_mi_no9](https://x.com/kan_mi_no9), [@gcduncombe](https://x.com/gcduncombe), [@tea_story_hoshi](https://x.com/tea_story_hoshi), [@craftcapitallab](https://x.com/craftcapitallab), [@fatboypink](https://x.com/fatboypink)

*모든 사례가 원작자에게 정확히 귀속되었다고 보장할 수는 없습니다. 정정할 내용이 있다면 연락해 주세요. 업데이트하겠습니다.*

추가할 Blender + Seedance 워크플로가 있나요? [유스케이스 Issue 열기](https://github.com/Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases/issues/new?template=use-case.yml) 시 [Issue 템플릿 파일](.github/ISSUE_TEMPLATE/use-case.yml)을 사용하거나 [PR 템플릿](.github/PULL_REQUEST_TEMPLATE.md)으로 풀 리퀘스트를 열어 주세요.

[![스타 기록 차트](https://api.star-history.com/svg?repos=Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&type=Date)](https://www.star-history.com/#Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&Date)
