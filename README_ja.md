<div align="center">

<a href="https://evolink.ai/cookbook/blender-to-video?utm_source=github&utm_medium=banner&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/images/banner.png" alt="Blender + Seedanceユースケースリポジトリのバナー" width="760"></a>

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

## 🍌 はじめに

Blender + Seedanceのユースケース集です。

**クリエイターがSeedance動画生成を制御するために実際に使った、Blender、Blender MCP、ビューポート、プリビズ、FBX、Mixamo、ComfyUI、エージェント支援のワークフローを収集しています。**

現在のコレクションは、所有者提供のX/Twitterソースデータから選定されています。各事例には元の投稿とクリエイターのプロフィールへのリンクがあります。

まずEvoLinkのBlender-to-videoクックブックを確認し、次に以下のクイックスタートをこのリポジトリ内のワークフロー参照として利用してください。

## 📊 概要

- **Blender + Seedanceの選定事例25件**を、所有者提供のソースデータセットに含まれる公開クリエイター投稿から選定しました。
- カメラ制御、Blenderプリビズ、複数キャラクターのブロッキング、アクションの振り付け、Blender MCP、Codex／Claude支援のブロックアウト、FBX／Mixamo参照、ComfyUI／スタイル変換、既知の制限を扱います。
- 各事例には、元ソース、クリエイター表記、簡潔な要点、証拠タイプ、公開日が含まれます。
- 公開リストは35件の候補監査から始まり、現在は定期更新ループで監査済みの週次追加7件を含みます。
- このリポジトリで実践的なワークフローを確認し、セットアップと実行にはEvoLinkのBlender-to-videoクックブックを利用してください。

> [!NOTE]
> このコレクションは宣伝よりも具体的なワークフロー証拠を重視します。ソースに基づく手順、参照動画の手法、エージェント／MCPの利用、再現可能な制約、明記された制限を優先します。

<a id="quick-start"></a>
## ⚡ クイックスタート

最初にローカルのBlender制御経路を設定し、その後エージェントが呼び出すEvoLinkスキルをインストールします。

### 1. Blender MCPをインストール

公式のBlender MCPセットアップガイドに従ってBlenderを開き、参照を生成する前にエージェントがBlender MCPサーバーへ接続できることを確認します。

- 公式セットアップ：[Blender MCPセットアップ](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

### 2. EvoLinkスキルをインストール

エージェントのワークスペースにSeedance生成スキルとTopazアップスケーリングスキルをインストールします。

```bash
npm i evolink-seedance
npm i evolink-topaz-video-upscale
```

### 3. [APIキーを取得](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=readme&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key)

EvoLinkアカウントでAPIキーを作成し、エージェントのランタイムで利用できるようにします。

```bash
export EVOLINK_API_KEY="<your-evolink-api-key>"
```

### 4. エージェント内で実行

MCP、スキル、APIキーの準備ができたら、エージェントにBlenderブロックアウトの作成、参照動画の書き出し、Seedanceでの生成、必要に応じた最終クリップのTopazアップスケーリングを依頼します。

直接リクエストを送る前に、[APIキーを取得](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=readme&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key) でキーを確認してください。直接 API のフォールバックが必要な場合は、Blender 参照ワークフローを `POST https://api.evolink.ai/v1/videos/generations` に送信します。

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

```text
Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.
```

> [!NOTE]
> Blender側のインストール詳細については、Blender MCPセットアップページを唯一の正確な情報源としてください。

## 📑 メニュー

| セクション | ケース |
|---|---|
| [🎥 カメラ制御とプリビズ](#camera-control-previs) | Case 1, 2, 3, 4, 5, 29 |
| [🎬 キャラクターとアクションのブロッキング](#character-action-blocking) | Case 6, 8, 9, 21, 32 |
| [🤖 エージェント型Blender MCP](#agentic-blender-mcp) | Case 10, 11, 22, 34 |
| [🧩 参照、プロンプト、複数入力の対応付け](#reference-prompt-multi-input-mapping) | Case 13, 14, 23, 24, 26, 27, 35 |
| [🛠️ 制作パイプラインとツールチェーン](#production-pipelines-toolchains) | Case 15, 16, 17, 18, 30 |
| [🧪 制限、検証、トラブルシューティング](#limits-tests-troubleshooting) | Case 20, 25, 28, 31, 33 |
| [🙏 謝辞](#acknowledge) | クレジットと訂正ポリシー |

<a id="camera-control-previs"></a>
### 🎥 カメラ制御とプリビズ

| ケース | 内容 | Type |
|---|---|---|
| [Seedanceのモーション参照として使うBlenderブロックアウト](#case-1) | 統合型の演出ワークフローです。元事例の完全なグレーボックス手法を使い、Seedanceで生成する前に、アクションプリビズのタイミング、速度、揺れ、空間的な振り付けまで作り込みます。 | Demo |
| [Midjourneyの開始フレームを使ったカメラブロッキング](#case-2) | 精密なカメラ制御の簡潔なレシピです。Blenderでカメラ移動を作り、Midjourneyで開始フレームを用意し、Seedanceにモーション参照を追従させます。 | Demo |
| [Blenderプリビズを使ったComfyUIカメラ制御](#case-3) | Blenderプリビズに正位置と上下反転の参照フレームを別々に組み合わせ、動きへの追従性を検証するComfyUI制御事例です。 | Demo |
| [ビューポートプレビューからリアルな開始フレームへ](#case-4) | 短いビューポートプレビューのチュートリアルです。シーンをブロックアウトし、プレビューを書き出し、最初のフレームをリアルにしてから、両方の参照をSeedanceに渡します。 | Demo |
| [1本の参照動画から複数の世界を生成](#case-5) | 同じBlender参照動画を使って、Seedanceで異なる世界観を生成するスタイル／世界観バリエーションの事例です。 | Demo |
| [会話に同期したiPhoneカメラのプリビズ](#case-29) | iPhoneで駆動したBlenderカメラパスを会話に合わせ、その音声付きプリビズと2枚の画像をSeedanceに渡してショット設計に使います。 | Integration |


<a id="character-action-blocking"></a>
### 🎬 キャラクターとアクションのブロッキング

| ケース | 内容 | Type |
|---|---|---|
| [ポーズを合わせた複数キャラクターの対話](#case-6) | Seedanceで演技シーンを生成する前に、Blenderでキャラクターのポーズとカメラ移動を合わせる対話ショットのワークフローです。 | Demo |
| [空間を移動するハンドヘルド追従カメラ](#case-8) | Blenderでキャラクターの空間移動を制御し、Seedanceが荒々しいカメラワークを最終動画に引き継ぐハンドヘルド追従の事例です。 | Demo |
| [タクティカルアクション向けのカメラとキャラクターのブロッキング](#case-9) | 生成前にBlenderでカメラの旋回、レンズ選択、遮蔽物の位置、銃撃のタイミング、キャラクター移動を演出するタクティカルブロッキングの事例です。 | Demo |
| [単純なカメラ移動を超えた待ち伏せシーンのプリビズ](#case-21) | Seedanceでショットを生成する前に、Blenderプリビズでステージング、タイミング、カメラ移動を解決できることを示す待ち伏せシーンの事例です。 | Demo |
| [障害物付き屋上パルクールチェイス](#case-32) | Seedanceが直線的な走りに寄りやすいときは、障害物とのやり取りや回避ビートを含むBlenderパルクールプリビズを先に作ります。 | Demo |


<a id="agentic-blender-mcp"></a>
### 🤖 エージェント型Blender MCP

| ケース | 内容 | Type |
|---|---|---|
| [Codex + Blender MCPによる参照動画ワークフロー](#case-10) | Codexが簡単な3D市場、猫の動き、カメラ構図、Seedance用のMP4参照を構築するエージェント型Blender MCPの事例です。 | Integration |
| [Codexで構築する建築とカメラワーク](#case-11) | Codexの支援でBlender内に建築とカメラワークを生成し、Seedanceの参照モーションとして検証する初心者向け事例です。 | Integration |
| [Claudeで数分以内に作るBlender MCPプリビズ](#case-22) | ClaudeがBlender MCPを使い、2〜3分でショット参照を構築する高速なエージェント型プリビズの事例です。 | Integration |
| [FableスキルをCodexへ移植](#case-34) | エージェントにBlender参照動画スキルを作らせてCodexへ移植し、プロンプトなしでSeedanceが動きを整えられるか試します。 | Integration |


<a id="reference-prompt-multi-input-mapping"></a>
### 🧩 参照、プロンプト、複数入力の対応付け

| ケース | 内容 | Type |
|---|---|---|
| [Blender参照を使った再現可能なSeedanceプロンプト](#case-13) | 再現性とトラブルシューティングを統合した事例です。セットアップで参照動画の条件を明示し、対になる検証でカメラ／リズム制御が成功した点と足の動きが失敗した点を記録しています。 | Tutorial |
| [初心者向けBlender参照としてのMixamoモーション](#case-14) | 初心者向けのモーションソース事例です。参照をSeedanceに送る前に、Blender内のMixamoモーションを制御可能な動きの土台として使います。 | Tutorial |
| [高速なシーンのための位置限定参照制御](#case-23) | 参照の重み付け事例です。位置合わせには参照を活かしつつ、プロンプトで速度と躍動感を取り戻します。 | Tutorial |
| [3Dソフトウェアの代わりに実物のおもちゃを参照](#case-24) | 物理参照の事例です。Blenderを開く負担が大きい場合に、おもちゃを素早い動きとステージングの参照として使います。 | Demo |
| [プロンプトで失敗した特定シーンの参照制御](#case-26) | 制御の代替策を示す事例です。プロンプトだけの生成に失敗したら、多少の躍動感を犠牲にしても参照を使ってシーンを成立させます。 | Demo |
| [キャラクター比率とシンプルな背景のヒント](#case-27) | 安定性チェックリストの事例です。身長だけでなくキャラクター全体の比率を合わせ、厳密な位置合わせが不要な背景は簡略化します。 | Tutorial |
| [マネキンモーキャプとスタイル入力フレーム](#case-35) | 硬いBlenderやマネキンの動きソースでタイミングを固定しつつ、入力フレーム設計でSeedanceの最終スタイルと布の挙動を誘導します。 | Demo |


<a id="production-pipelines-toolchains"></a>
### 🛠️ 制作パイプラインとツールチェーン

| ケース | 内容 | Type |
|---|---|---|
| [Hermes、Krea、ComfyUI、Blender MCPのスタック](#case-15) | HermesがKrea、ComfyUI、Blender MCP、Seedanceをインストールして接続し、画像参照と物理参照の両方を作るマルチツール型エージェントパイプラインです。 | Integration |
| [Blender MCPビューポートからSeedanceへのスタイル変換](#case-16) | ビューポートからスタイル変換へ進む事例です。Blender MCPでカメラと要素を制御し、Seedance／Magnificでテクスチャとライティングを加えます。 | Integration |
| [BlenderプリビズからSeedanceのアニメ調レンダーへ](#case-17) | Seedanceでレンダースタイルを変えながら、カメラ移動とモーションを維持できることを示す3Dプリビズからアニメへの事例です。 | Integration |
| [Claudeでキーフレーム設定したカメラを使うFBXクレイパス](#case-18) | Blenderでモーションを読み込み、Claudeがカメラ移動のキーフレーム設定を支援し、レンダリングしたクレイパスをSeedance参照動画にするFBXワークフローです。 | Integration |
| [Fableが組んだダンス参照パイプライン](#case-30) | プロンプトだけでは粗い動きになりやすいとき、エージェントにキャラ設計とBlender振付コードを任せ、15秒のダンス参照をSeedanceへ渡します。 | Integration |


<a id="limits-tests-troubleshooting"></a>
### 🧪 制限、検証、トラブルシューティング

| ケース | 内容 | Type |
|---|---|---|
| [開始フレームなしの参照専用Blenderブロックアウト](#case-20) | 開始フレームを利用できないワークフローでも、Blenderブロックアウトと詳細な環境参照を組み合わせれば機能することを示す、開始フレームなしのバリエーションです。 | Limit |
| [おもちゃ参照のプロンプト補強とNG例](#case-25) | 参照動画をそのまま模倣させるのではなく、プロンプトによる補強が必要になる理由を示すトラブルシューティング事例です。 | Limit |
| [BlenderとSeedanceによる布物理のストレステスト](#case-28) | Blenderで誘導したSeedanceが機能する範囲と、難しい動きでは反復調整が必要なことを示す布物理のストレステストです。 | Limit |
| [黒フレームでつなぐキーフレーム補正](#case-31) | 荒いBlender参照の中割りまでSeedanceが機械的に真似するときは、キーポーズだけ残して間を黒フレームにします。 | Tutorial |
| [複雑シーンでのモーション不一致テスト](#case-33) | ラフシーンのMCPレンダーは制約テストとして扱うべきで、複雑なBlenderシーンは複数回のSeedance試行でも意図した動きからずれることがあります。 | Limit |



<a id="camera-control-previs-cases"></a>
## 🎥 カメラ制御とプリビズ

<a id="case-1"></a>
### Case 1: [Seedanceのモーション参照として使うBlenderブロックアウト](https://x.com/noman23761/status/2071534020014563328)（作者：[@noman23761](https://x.com/noman23761))

**統合型の演出ワークフローです。元事例の完全なグレーボックス手法を使い、Seedanceで生成する前に、アクションプリビズのタイミング、速度、揺れ、空間的な振り付けまで作り込みます。**

- ソースメモ: 旧Case 7と統合しました。両ソースを合わせることで、完全なグレーボックスワークフローと、概略のタイミング、速度、揺れ、空間的な振り付けを含むアクションプリビズのバリエーションを確認できます。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case1.mp4)

Type: Demo | Date: 2026-06-29

---

<a id="case-2"></a>
### Case 2: [Midjourneyの開始フレームを使ったカメラブロッキング](https://x.com/reidhannaford/status/2069074506849685773)（作者：[@reidhannaford](https://x.com/reidhannaford))

**精密なカメラ制御の簡潔なレシピです。Blenderでカメラ移動を作り、Midjourneyで開始フレームを用意し、Seedanceにモーション参照を追従させます。**

- ソースメモ: ソースには明確な3段階のワークフローが示され、生成動画がBlenderのカメラ移動に正確に追従したと報告されています。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case2.mp4)

Type: Demo | Date: 2026-06-22

---

<a id="case-3"></a>
### Case 3: [Blenderプリビズを使ったComfyUIカメラ制御](https://x.com/JMSvid/status/2070258132840796579)（作者：[@JMSvid](https://x.com/JMSvid))

**Blenderプリビズに正位置と上下反転の参照フレームを別々に組み合わせ、動きへの追従性を検証するComfyUI制御事例です。**

- ソースメモ: ComfyUI形式の制御セットアップ内でBlenderプリビズと複数の静止画参照を組み合わせている点が有用です。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case3.mp4)

Type: Demo | Date: 2026-06-25

---

<a id="case-4"></a>
### Case 4: [ビューポートプレビューからリアルな開始フレームへ](https://x.com/DiabloNemesis/status/2070441923706503380)（作者：[@DiabloNemesis](https://x.com/DiabloNemesis))

**短いビューポートプレビューのチュートリアルです。シーンをブロックアウトし、プレビューを書き出し、最初のフレームをリアルにしてから、両方の参照をSeedanceに渡します。**

- ソースメモ: 投稿には、ビューポートプレビュー、最初のフレーム画像、Seedance参照動画という具体的な成果物を伴う簡潔なワークフローがあります。公開事例に同じ動画が1つだけ表示されるよう、重複していたCase 29のメディアは削除しました。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case4.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case4.mp4)

Type: Demo | Date: 2026-06-26

---

<a id="case-5"></a>
### Case 5: [1本の参照動画から複数の世界を生成](https://x.com/koldo2k/status/2071307945002815967)（作者：[@koldo2k](https://x.com/koldo2k))

**同じBlender参照動画を使って、Seedanceで異なる世界観を生成するスタイル／世界観バリエーションの事例です。**

- ソースメモ: 同じ参照動画を使いながら、モーション制御と世界観／スタイルの変化を分離している点が有用です。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 5](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case5.mp4)

Type: Demo | Date: 2026-06-28

---


<a id="case-29"></a>
### Case 29: [会話に同期したiPhoneカメラのプリビズ](https://x.com/CoffeeVectors/status/2076397975853551924) （作者：[@CoffeeVectors](https://x.com/CoffeeVectors)）

**iPhoneで駆動したBlenderカメラパスを会話に合わせ、その音声付きプリビズと2枚の画像をSeedanceに渡してショット設計に使います。**

- ソースメモ: ソースでは、iPhoneで駆動したBlenderカメラを会話に合わせ、その音声付きプリビズを2枚の静止画と一緒にSeedance 2へ渡しています。
- 動画プレビュー:

[![動画プレビュー — Case 29](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case29.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case29.mp4)

Type: Integration | Date: 2026-07-12

---
<a id="character-action-blocking-cases"></a>
## 🎬 キャラクターとアクションのブロッキング

<a id="case-6"></a>
### Case 6: [ポーズを合わせた複数キャラクターの対話](https://x.com/reidhannaford/status/2069420552394043625)（作者：[@reidhannaford](https://x.com/reidhannaford))

**Seedanceで演技シーンを生成する前に、Blenderでキャラクターのポーズとカメラ移動を合わせる対話ショットのワークフローです。**

- ソースメモ: 複数キャラクターの対話とポーズ合わせが加わっており、単一キャラクターのカメラ制御デモとは異なります。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 6](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case6.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case6.mp4)

Type: Demo | Date: 2026-06-23

---

<a id="case-8"></a>
### Case 8: [空間を移動するハンドヘルド追従カメラ](https://x.com/reidhannaford/status/2070507963429671062)（作者：[@reidhannaford](https://x.com/reidhannaford))

**Blenderでキャラクターの空間移動を制御し、Seedanceが荒々しいカメラワークを最終動画に引き継ぐハンドヘルド追従の事例です。**

- ソースメモ: カメラが追従しながらキャラクターをシーン内で移動させるため、ハンドヘルド移動ショットの参考になります。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

プレビューを利用できません。元のGitHub添付ファイルは現在公開されていません。

Type: Demo | Date: 2026-06-26

---

<a id="case-9"></a>
### Case 9: [タクティカルアクション向けのカメラとキャラクターのブロッキング](https://x.com/SamJWasserman/status/2070742850095230991)（作者：[@SamJWasserman](https://x.com/SamJWasserman))

**生成前にBlenderでカメラの旋回、レンズ選択、遮蔽物の位置、銃撃のタイミング、キャラクター移動を演出するタクティカルブロッキングの事例です。**

- ソースメモ: カメラとキャラクターのブロッキングを同時に示しており、単純なカメラ専用参照よりも実践的です。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 9](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case9.mp4)

Type: Demo | Date: 2026-06-27

---

<a id="case-21"></a>
### Case 21: [単純なカメラ移動を超えた待ち伏せシーンのプリビズ](https://x.com/reidhannaford/status/2071595581508563168)（作者：[@reidhannaford](https://x.com/reidhannaford))

**Seedanceでショットを生成する前に、Blenderプリビズでステージング、タイミング、カメラ移動を解決できることを示す待ち伏せシーンの事例です。**

- ソースメモ: Case 21として依頼されました。単純なカメラ移動からシーンのステージングまでワークフローを発展させているため、Reid Hannafordの独立した事例として採用しました。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 21](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case21.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case21.mp4)

Type: Demo | Date: 2026-06-29

---


<a id="case-32"></a>
### Case 32: [障害物付き屋上パルクールチェイス](https://x.com/moframe2026/status/2075203485604470965) （作者：[@moframe2026](https://x.com/moframe2026)）

**Seedanceが直線的な走りに寄りやすいときは、障害物とのやり取りや回避ビートを含むBlenderパルクールプリビズを先に作ります。**

- ソースメモ: 作者はBlender製のパルクールプリビズを動画参照に使い、単なる走りではなく障害物利用と回避の流れを補うためにBlenderが必要だったと書いています。
- 動画プレビュー:

[![動画プレビュー — Case 32](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case32.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case32.mp4)

Type: Demo | Date: 2026-07-09

---
<a id="agentic-blender-mcp-cases"></a>
## 🤖 エージェント型Blender MCP

<a id="case-10"></a>
### Case 10: [Codex + Blender MCPによる参照動画ワークフロー](https://x.com/akiyoshisan/status/2071081230108660199)（作者：[@akiyoshisan](https://x.com/akiyoshisan))

**Codexが簡単な3D市場、猫の動き、カメラ構図、Seedance用のMP4参照を構築するエージェント型Blender MCPの事例です。**

- ソースメモ: 作者は別のクリエイターから着想を得たと述べていますが、説明されているシーン、動き、カメラ、書き出し工程は作者自身の実験です。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 10](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case10.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case10.mp4)

Type: Integration | Date: 2026-06-28

---

<a id="case-11"></a>
### Case 11: [Codexで構築する建築とカメラワーク](https://x.com/6_KAKUU/status/2071051063663452374)（作者：[@6_KAKUU](https://x.com/6_KAKUU))

**Codexの支援でBlender内に建築とカメラワークを生成し、Seedanceの参照モーションとして検証する初心者向け事例です。**

- ソースメモ: Seedanceを使う前に建築とカメラワークをCodexへ任せる、初心者向けCodexワークフローとして価値があります。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 11](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case11.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case11.mp4)

Type: Integration | Date: 2026-06-28

---

<a id="case-22"></a>
### Case 22: [Claudeで数分以内に作るBlender MCPプリビズ](https://x.com/JoshDaws/status/2071401550845481090)（作者：[@JoshDaws](https://x.com/JoshDaws))

**ClaudeがBlender MCPを使い、2〜3分でショット参照を構築する高速なエージェント型プリビズの事例です。**

- ソースメモ: Case 22として依頼されました。手作業のBlender操作ではなく、速度とエージェント制御を示しているため採用しました。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 22](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case22.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case22.mp4)

Type: Integration | Date: 2026-06-29

---


<a id="case-34"></a>
### Case 34: [FableスキルをCodexへ移植](https://x.com/mugi_AI_Art/status/2074259600342163846) （作者：[@mugi_AI_Art](https://x.com/mugi_AI_Art)）

**エージェントにBlender参照動画スキルを作らせてCodexへ移植し、プロンプトなしでSeedanceが動きを整えられるか試します。**

- ソースメモ: 作者はFableにBlender参照動画スキルを作らせてCodexへ移植し、ラフモデリングの参照からプロンプトなしでSeedance生成を行っています。
- 動画プレビュー:

[![動画プレビュー — Case 34](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case34.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case34.mp4)

Type: Integration | Date: 2026-07-06

---
<a id="reference-prompt-multi-input-mapping-cases"></a>
## 🧩 参照、プロンプト、複数入力の対応付け

<a id="case-13"></a>
### Case 13: [Blender参照を使った再現可能なSeedanceプロンプト](https://x.com/aidoga_lab/status/2070864815275585913)（作者：[@aidoga_lab](https://x.com/aidoga_lab))

**再現性とトラブルシューティングを統合した事例です。セットアップで参照動画の条件を明示し、対になる検証でカメラ／リズム制御が成功した点と足の動きが失敗した点を記録しています。**

- ソースメモ: 旧Case 19と統合しました。この組み合わせにより、再現可能なセットアップと足滑りに関する制限の記録を両方残しています。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case13.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.mp4)

![参照画像 — Case 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.jpg)

Type: Tutorial | Date: 2026-06-27

---

<a id="case-14"></a>
### Case 14: [初心者向けBlender参照としてのMixamoモーション](https://x.com/tanabe_fragm/status/2070685291183243459)（作者：[@tanabe_fragm](https://x.com/tanabe_fragm))

**初心者向けのモーションソース事例です。参照をSeedanceに送る前に、Blender内のMixamoモーションを制御可能な動きの土台として使います。**

- ソースメモ: Blender参照動画の実用的なモーションソースとしてMixamoを明示しているため、初心者に有用です。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 14](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case14.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case14.mp4)

Type: Tutorial | Date: 2026-06-27

---

<a id="case-23"></a>
### Case 23: [高速なシーンのための位置限定参照制御](https://x.com/kan_mi_no9/status/2071380621214224403)（作者：[@kan_mi_no9](https://x.com/kan_mi_no9))

**参照の重み付け事例です。位置合わせには参照を活かしつつ、プロンプトで速度と躍動感を取り戻します。**

- ソースメモ: Case 23として依頼されました。対になるkan_mi_no9の検証と併せ、独立した参照制御のバリエーションとして採用しました。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 23](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case23.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case23.mp4)

Type: Tutorial | Date: 2026-06-28

---

<a id="case-24"></a>
### Case 24: [3Dソフトウェアの代わりに実物のおもちゃを参照](https://x.com/gcduncombe/status/2070617538745229546)（作者：[@gcduncombe](https://x.com/gcduncombe))

**物理参照の事例です。Blenderを開く負担が大きい場合に、おもちゃを素早い動きとステージングの参照として使います。**

- ソースメモ: Case 24として依頼されました。参照動画の考え方をソフトウェアだけのプリビズから拡張しているため採用しました。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 24](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case24.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case24.mp4)

Type: Demo | Date: 2026-06-26

---

<a id="case-26"></a>
### Case 26: [プロンプトで失敗した特定シーンの参照制御](https://x.com/kan_mi_no9/status/2071168235022827587)（作者：[@kan_mi_no9](https://x.com/kan_mi_no9))

**制御の代替策を示す事例です。プロンプトだけの生成に失敗したら、多少の躍動感を犠牲にしても参照を使ってシーンを成立させます。**

- ソースメモ: Case 26として依頼されました。後に続くkan_mi_no9のバリエーション事例と対になる実践例として採用しました。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 26](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case26.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case26.mp4)

Type: Demo | Date: 2026-06-28

---

<a id="case-27"></a>
### Case 27: [キャラクター比率とシンプルな背景のヒント](https://x.com/craftcapitallab/status/2070512271391068287)（作者：[@craftcapitallab](https://x.com/craftcapitallab))

**安定性チェックリストの事例です。身長だけでなくキャラクター全体の比率を合わせ、厳密な位置合わせが不要な背景は簡略化します。**

- ソースメモ: Case 27として依頼されました。具体的で再利用可能なセットアップの助言があるため採用しました。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 27](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case27.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case27.mp4)

Type: Tutorial | Date: 2026-06-26

---


<a id="case-35"></a>
### Case 35: [マネキンモーキャプとスタイル入力フレーム](https://x.com/fatboypink/status/2074087401887039740) （作者：[@fatboypink](https://x.com/fatboypink)）

**硬いBlenderやマネキンの動きソースでタイミングを固定しつつ、入力フレーム設計でSeedanceの最終スタイルと布の挙動を誘導します。**

- ソースメモ: 作者は、硬いマネキン由来のモーションがタイミングを担当しつつ、手描きの入力フレームが狙ったスタイルと布の動きを引き戻したと説明しています。
- 動画プレビュー:

[![動画プレビュー — Case 35](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case35.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case35.mp4)

Type: Demo | Date: 2026-07-06

---
<a id="production-pipelines-toolchains-cases"></a>
## 🛠️ 制作パイプラインとツールチェーン

<a id="case-15"></a>
### Case 15: [Hermes、Krea、ComfyUI、Blender MCPのスタック](https://x.com/SamJWasserman/status/2069656428437225826)（作者：[@SamJWasserman](https://x.com/SamJWasserman))

**HermesがKrea、ComfyUI、Blender MCP、Seedanceをインストールして接続し、画像参照と物理参照の両方を作るマルチツール型エージェントパイプラインです。**

- ソースメモ: 手作業のBlenderプリビズだけでなく、エージェントが構築するより広範なクリエイティブスタックを示しています。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 15](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case15.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case15.mp4)

Type: Integration | Date: 2026-06-24

---

<a id="case-16"></a>
### Case 16: [Blender MCPビューポートからSeedanceへのスタイル変換](https://x.com/techhalla/status/2070814203435274715)（作者：[@techhalla](https://x.com/techhalla))

**ビューポートからスタイル変換へ進む事例です。Blender MCPでカメラと要素を制御し、Seedance／Magnificでテクスチャとライティングを加えます。**

- ソースメモ: ビューポートアニメーションと後段のスタイル／ライティング工程を説明しているため、techhallaのソースの中でも根拠がより明確です。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 16](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case16.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case16.mp4)

Type: Integration | Date: 2026-06-27

---

<a id="case-17"></a>
### Case 17: [BlenderプリビズからSeedanceのアニメ調レンダーへ](https://x.com/restofart/status/2070086939756159368)（作者：[@restofart](https://x.com/restofart))

**Seedanceでレンダースタイルを変えながら、カメラ移動とモーションを維持できることを示す3Dプリビズからアニメへの事例です。**

- ソースメモ: カメラ移動を維持しながらBlenderの3Dプリビズをアニメ調レンダーへ変換するワークフローとして、ソースに明示されています。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 17](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case17.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case17.mp4)

Type: Integration | Date: 2026-06-25

---

<a id="case-18"></a>
### Case 18: [Claudeでキーフレーム設定したカメラを使うFBXクレイパス](https://x.com/Viggle_PINOC/status/2070183934265012392)（作者：[@Viggle_PINOC](https://x.com/Viggle_PINOC))

**Blenderでモーションを読み込み、Claudeがカメラ移動のキーフレーム設定を支援し、レンダリングしたクレイパスをSeedance参照動画にするFBXワークフローです。**

- ソースメモ: 具体的なFBXからクレイパスへの工程が示され、参照を書き出す前のカメラキーフレーム設定も含まれています。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 18](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case18.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case18.mp4)

Type: Integration | Date: 2026-06-25

---


<a id="case-30"></a>
### Case 30: [Fableが組んだダンス参照パイプライン](https://x.com/ryo05m/status/2076284841457521043) （作者：[@ryo05m](https://x.com/ryo05m)）

**プロンプトだけでは粗い動きになりやすいとき、エージェントにキャラ設計とBlender振付コードを任せ、15秒のダンス参照をSeedanceへ渡します。**

- ソースメモ: 作者は、Seedream 5 Proでキャラ設計、Blenderで15秒のマネキンダンス、Seedance 2.0で動きとカメラ参照という3段階を明記しています。
- 動画プレビュー:

[![動画プレビュー — Case 30](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case30.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case30.mp4)

Type: Integration | Date: 2026-07-12

---
<a id="limits-tests-troubleshooting-cases"></a>
## 🧪 制限、検証、トラブルシューティング

<a id="case-20"></a>
### Case 20: [開始フレームなしの参照専用Blenderブロックアウト](https://x.com/magneticskiff/status/2070711034793361559)（作者：[@magneticskiff](https://x.com/magneticskiff))

**開始フレームを利用できないワークフローでも、Blenderブロックアウトと詳細な環境参照を組み合わせれば機能することを示す、開始フレームなしのバリエーションです。**

- ソースメモ: 通常の開始フレームへの依存を参照画像で置き換える重要なバリエーションを扱っています。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 20](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case20.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case20.mp4)

Type: Limit | Date: 2026-06-27

---

<a id="case-25"></a>
### Case 25: [おもちゃ参照のプロンプト補強とNG例](https://x.com/tea_story_hoshi/status/2071002538703479089)（作者：[@tea_story_hoshi](https://x.com/tea_story_hoshi))

**参照動画をそのまま模倣させるのではなく、プロンプトによる補強が必要になる理由を示すトラブルシューティング事例です。**

- ソースメモ: Case 25として依頼されました。成功例と失敗した比較の両方が含まれるため採用しました。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 25](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case25.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case25.mp4)

Type: Limit | Date: 2026-06-27

---

<a id="case-28"></a>
### Case 28: [BlenderとSeedanceによる布物理のストレステスト](https://x.com/fatboypink/status/2070577334701473800)（作者：[@fatboypink](https://x.com/fatboypink))

**Blenderで誘導したSeedanceが機能する範囲と、難しい動きでは反復調整が必要なことを示す布物理のストレステストです。**

- ソースメモ: Case 28として依頼されました。具体的な制限／ストレステスト事例として採用しました。
- 監査状況：手動による重複および独自性レビュー後に採用。
- 動画プレビュー:

[![デモ動画を再生 — Case 28](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case28.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case28.mp4)

Type: Limit | Date: 2026-06-26

---

<a id="related-repositories"></a>
## 🔗 関連リポジトリ

- [Seedance 2.0のプロンプトを見る](https://github.com/Evolink-AI/awesome-seedance-2.0-prompts)
- [Seedance 2 エージェントスキルをインストール](https://github.com/Evolink-AI/seedance2-video-gen-skill-for-openclaw)
- [GPT Image 2 から Seedance 2 のワークフローを見る](https://github.com/Evolink-AI/GPT-Image-2-Seedance2-Workflow)


<a id="case-31"></a>
### Case 31: [黒フレームでつなぐキーフレーム補正](https://x.com/thechriscooper/status/2076092824102240411) （作者：[@thechriscooper](https://x.com/thechriscooper)）

**荒いBlender参照の中割りまでSeedanceが機械的に真似するときは、キーポーズだけ残して間を黒フレームにします。**

- ソースメモ: 作者によると、荒いBlenderアニメーション全体をそのまま渡すとSeedanceがぎこちない中割りまで複製しましたが、キーフレームと黒フレームを交互にするとブロッキングを保ったまま動きが滑らかになりました。
- 動画プレビュー:

[![動画プレビュー — Case 31](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case31.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case31.mp4)

Type: Tutorial | Date: 2026-07-11

---

<a id="case-33"></a>
### Case 33: [複雑シーンでのモーション不一致テスト](https://x.com/sonicpower1970/status/2074322339391824012) （作者：[@sonicpower1970](https://x.com/sonicpower1970)）

**ラフシーンのMCPレンダーは制約テストとして扱うべきで、複雑なBlenderシーンは複数回のSeedance試行でも意図した動きからずれることがあります。**

- ソースメモ: この続報では、作者のClaude→Blender→Seedanceテストにおいて、およそ4テイク試しても複雑なシーンでは意図した動きに合わなかったと報告しています。
- 動画プレビュー:

[![動画プレビュー — Case 33](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case33.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case33.mp4)

Type: Limit | Date: 2026-07-07

---
<a id="acknowledge"></a>
## 🙏 謝辞

このリポジトリは、Blender + Seedanceのワークフロー、検証、プロンプト、参照動画、制作メモを公開したクリエイターの皆様から着想を得ています。

[@noman23761](https://x.com/noman23761), [@reidhannaford](https://x.com/reidhannaford), [@JMSvid](https://x.com/JMSvid), [@DiabloNemesis](https://x.com/DiabloNemesis), [@koldo2k](https://x.com/koldo2k), [@SamJWasserman](https://x.com/SamJWasserman), [@akiyoshisan](https://x.com/akiyoshisan), [@6_KAKUU](https://x.com/6_KAKUU), [@aidoga_lab](https://x.com/aidoga_lab), [@tanabe_fragm](https://x.com/tanabe_fragm), [@techhalla](https://x.com/techhalla), [@restofart](https://x.com/restofart), [@Viggle_PINOC](https://x.com/Viggle_PINOC), [@magneticskiff](https://x.com/magneticskiff), [@JoshDaws](https://x.com/JoshDaws), [@kan_mi_no9](https://x.com/kan_mi_no9), [@gcduncombe](https://x.com/gcduncombe), [@tea_story_hoshi](https://x.com/tea_story_hoshi), [@craftcapitallab](https://x.com/craftcapitallab), [@fatboypink](https://x.com/fatboypink)

*すべての事例が元のクリエイターへ正しく帰属していることを保証するものではありません。訂正が必要な場合はご連絡ください。内容を更新します。*

追加したいBlender + Seedanceワークフローがありますか？ [ユースケースIssueを作成](https://github.com/Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases/issues/new?template=use-case.yml)する際は[Issueテンプレートファイル](.github/ISSUE_TEMPLATE/use-case.yml)を使用するか、[PRテンプレート](.github/PULL_REQUEST_TEMPLATE.md)を使ってプルリクエストを作成してください。

[![スター履歴チャート](https://api.star-history.com/svg?repos=Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&type=Date)](https://www.star-history.com/#Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&Date)
