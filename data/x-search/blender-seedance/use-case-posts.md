# Blender + Seedance Use-Case Posts

Source: `/Users/evolink/Desktop/github-repo/awesome-blender-seedance-use-cases/data/x-search/blender-seedance/posts.json`
Full curated: 67 / 171
Primary original use cases: 35

## Selection Criteria
- 必须来自已采集的 blender seedance 近 1 周 posts。
- 必须同时属于 Blender/3D 软件语境和 Seedance 视频生成语境，排除 kitchen blender 等误匹配。
- 优先选择明确分享 workflow、玩法、步骤、prompt、参考视频/viewport/playblast、MCP/agent、ComfyUI 或可转化 use case 的帖子。
- 新增来源角色校验：区分一手原创玩法、原创补充回复、工具/官方聚合、二次转述/转发、趋势解释、待跟踪。
- 主可用列表只保留 source_role=primary_original 且 tier 为 strong/medium 的帖子；转述、复述、纯解释、评论和待跟踪不进入主列表。

## primary_original (35)

### 1. Blender 灰盒预演 + 起始帧 + Seedance motion reference
- URL: https://x.com/noman23761/status/2071534020014563328
- Author: @noman23761
- Tier: `strong`
- Category: `hybrid_previs_camera_control`
- Metrics: likes=0, views=47
- Why: 完整说明从 image model 起始帧、Blender 灰盒场景/相机动画，到 Seedance 参考视频生成的端到端流程。
- Reuse: 可直接改写成“用 Blender blockout 精准导演 AI 镜头”的主 use case。
- Text: Spent months prompting video models and only just figured out what was missing: prompting is describing a shot, you write what you want and hope the model interprets the camera the way you meant. Blocking it out in Blender first is directing it. The workflow is simpler than it sounds. Generate a start frame on an image model. Then in Blender, build the sc...

### 2. Blender 运镜参考 + Midjourney 起始帧 + Seedance
- URL: https://x.com/reidhannaford/status/2069074506849685773
- Author: @reidhannaford
- Tier: `strong`
- Category: `hybrid_previs_camera_control`
- Metrics: likes=1094, views=68790
- Why: 列出 3 步 workflow：Blender block camera、Midjourney start frame、两者送入 Seedance。
- Reuse: 适合做 precision camera control 的基础案例。
- Text: This is wild. Every filmmaker needs to try this hybrid AI workflow for precision camera control: 1) Block out your camera in Blender to create a motion reference and animate the camera move 2) Generate your start frame in Midjourney to match the pose and composition 3) Feed both to Seedance It tracks the move almost exactly. This is the most powerful hybr...

### 3. 多角色 + 对话 + 精准运镜
- URL: https://x.com/reidhannaford/status/2069420552394043625
- Author: @reidhannaford
- Tier: `strong`
- Category: `multi_character_dialogue`
- Metrics: likes=3266, views=204620
- Why: 说明用 Midjourney 起始帧、Blender pose/camera，再交给 Seedance，实现两个一致角色和对话镜头。
- Reuse: 适合做多角色表演/对话场景 use case。
- Text: I'm blown away. This AI filmmaking workflow for precise camera control, multiple characters, and dialogue is insane: 1. Generate a start frame in Midjourney 2. Match the poses in Blender, animate the camera 3. Feed both to Seedance I didn't think this would work. Two consistent characters, solid performances, the move tracked perfectly through the entire ...

### 4. 基础几何体驱动多角色镜头
- URL: https://x.com/reidhannaford/status/2069783215829569746
- Author: @reidhannaford
- Tier: `strong`
- Category: `multi_character_action`
- Metrics: likes=2137, views=219887
- Why: 强调 3D 参考不需要精美，只用 basic shapes 也能驱动精确多角色 shot。
- Reuse: 适合做“低成本 3D reference 就够用”的案例。
- Text: This is getting ridiculous. You need to try this AI filmmaking workflow. My Blender reference is embarrassingly simple. You can drive a precise multi-character shot with nothing but basic shapes. 1. Generate a start frame in Midjourney 2. Block out the scene in Blender with boxes, animate the camera 3. Feed both to Seedance This feels like a real unlock. ...

### 5. 复杂动作场景编排
- URL: https://x.com/reidhannaford/status/2070145120658137385
- Author: @reidhannaford
- Tier: `strong`
- Category: `action_choreography`
- Metrics: likes=4353, views=481743
- Why: 明确说明用 Blender basic shapes 编排 action scene，Seedance 负责真实化。
- Reuse: 适合做动作戏/空间调度 use case。
- Text: Ok, this is absurd. You can choreograph a complex action scene in Blender with basic shapes, then let Seedance make it real. You need to try this AI filmmaking workflow: 1. Generate a start frame in Midjourney 2. Block out the action in Blender 3. Feed both to Seedance My Blender reference was just rough timing, camera shake, and spatial choreography, and...

### 6. 手持跟拍 + 角色绕车运动
- URL: https://x.com/reidhannaford/status/2070507963429671062
- Author: @reidhannaford
- Tier: `strong`
- Category: `handheld_follow_camera`
- Metrics: likes=1276, views=88839
- Why: 说明在 Blender 中移动角色并做 handheld camera follow，Seedance 跟随运动和质感。
- Reuse: 适合做手持跟拍、角色移动穿越空间的案例。
- Text: The previs workflow is still leveling up! My AI filmmaking process is starting to feel less like wrangling AI and more like animation. Still just cubes in Blender, but now I’m moving the character through space and doing a handheld camera follow. Same basic process: 1. Generate a start frame in Midjourney 2. Block out the scene in Blender, animate the cam...

### 7. 日本语复现条件 + 完整 prompt
- URL: https://x.com/aidoga_lab/status/2070864815275585913
- Author: @aidoga_lab
- Tier: `strong`
- Category: `replication_prompt`
- Metrics: likes=3, views=435
- Why: 给出 start frame、Blender reference video、Seedance 2.0、5s、以及长 prompt。
- Reuse: 适合做可复现 prompt/source case。
- Text: 再現用に条件を全部置いておきます。 ・スタートフレーム：添付のキャラ画像 ・参照動画：添付のBlender動画 ・モデル：Seedance 2.0 ・尺：5s 使ったプロンプト↓ RReference video 1 defines the camera movement, timing, and the walker's path ONLY — match its trajectory, speed, framing, and the walker's position and facing exactly. The teal figure with pink arms and a purple backpack in the reference is the walker. Do NOT copy t...

### 8. 相机/节奏/移动控制实验与失败点
- URL: https://x.com/aidoga_lab/status/2070864749865398684
- Author: @aidoga_lab
- Tier: `medium`
- Category: `camera_motion_experiment`
- Metrics: likes=24, views=1239
- Why: 说明用 Blender 视频控制 Seedance 的 camera/rhythm/subject movement，同时指出 foot sliding 问题。
- Reuse: 适合做 limitations + troubleshooting case。
- Text: AI動画13日目。 Blender動画をSeedanceに参照させて、 カメラの動き・リズム・被写体の移動を制御するやり方にチャレンジしてみました。 結果、 カメラの動き・リズム・移動は、狙い通り制御できた。 でも"足の動き＝仕草"がうまくいかない。 Blender動画の動きをそのまま参照してしまって、自然な歩きにならない。 プロンプトでの制御も、モデル変更（mini→2.0）も試したけど、 どうしても足が滑ってしまう。 Blender動画側が正確な仕草をしてればクリアできる気はしてます。 でも理想は、Blender動画は「カメラ・リズム・移動」だけのリファレンスにして、 仕草はプロンプトに任せる形。 ここがまだ解けてません。 皆さんはどう制御してますか？

### 9. Codex + Blender MCP 生成场景/动作/参照视频
- URL: https://x.com/akiyoshisan/status/2071081230108660199
- Author: @akiyoshisan
- Tier: `strong`
- Category: `agentic_blender_mcp`
- Metrics: likes=4, views=1183
- Why: 列出 Blender MCP 连接 Codex、生成猫/市场/屋台、15 秒 motion、camera work、导出 MP4 reference 的完整流程。
- Reuse: 适合做 Agentic Blender MCP + Seedance use case。
- Text: SEIIIRUさんのを参考に、CodexからBlender MCPで試してみました。 投稿をみて、Blenderでもいけそう！と初のMCP繋いでやってみましたが中々難しいっす… ────────────── ▼ 試した内容 ・Blender MCP｜CodexからBlenderへ直接Python実行 ・簡易3Dシーン｜石畳の市場、木製の魚屋台、魚、猫を作成 ・猫モーション｜屋台に向かって歩く、止まる、魚を見る、前足を上げる ・カメラ設計｜猫・屋台・距離感が見える斜め構図で追従 ────────────── ▼ 制作フロー 1. Blender MCPをCodexに接続 2. CodexからBlenderへコード送信 3. 猫・屋台・市場を簡易モデルで生成 4. 15秒の歩きモーションを作成 5. カメラワ...

### 10. Blender blocking + 多参考图 + 角色锁定 prompt
- URL: https://x.com/AIWarper/status/2069481237308452916
- Author: @AIWarper
- Tier: `strong`
- Category: `prompt_and_reference_mapping`
- Metrics: likes=56, views=4188
- Why: 给出 Seedance prompt，把 motion/blocking reference 中的角色映射到指定角色参考图。
- Reuse: 适合做 prompt engineering + character mapping case。
- Text: The TL:DR here is if you are proficient in blocking out animation inside of Blender (or whatever) you can really nail the exact shots you want. Here I attached these 3 ref images + the source video I linked above with this Seedance prompt: "In a retro 1980s anime style, hand-drawn cel animation, set on the sunny city street from the attached environment r...

### 11. FBX 动画导入 Blender 后导出 Seedance reference
- URL: https://x.com/AIWarper/status/2069847776620589430
- Author: @AIWarper
- Tier: `strong`
- Category: `fbx_to_seedance_reference`
- Metrics: likes=10, views=1959
- Why: 列出 import FBX、position camera、export animation mp4，且提到 Seedance ref videos 720 max。
- Reuse: 适合做 Mixamo/FBX animation reference pipeline。
- Text: I then just did the following: 1) import the first .fbx into blender 2) position my camera 3) export the animation to .mp4 (720 max res for Seedance ref videos) I did this for each clip, changing the camera angle each time.

### 12. 无动画基础也能做 Seedance ref video
- URL: https://x.com/AIWarper/status/2070162937181065547
- Author: @AIWarper
- Tier: `medium`
- Category: `agentic_blender_mcp`
- Metrics: likes=469, views=22676
- Why: 强调不用鼠标点击 Blender、可测试 ref video trend，提示后续 details。
- Reuse: 适合作为 agent-assisted/no-code workflow 候选。
- Text: Want to test the latest Seedance ref video trend but have no clue how to animate? This entire animation was done without a single mouse click in Blender Details below 👇 https://t.co/lWreeqHIDy

### 13. Codex/OPUS + Blender MCP 一句 prompt 做 blockout
- URL: https://x.com/AIWarper/status/2070535586075885912
- Author: @AIWarper
- Tier: `medium`
- Category: `agentic_blender_mcp`
- Metrics: likes=252, views=22365
- Why: 说明整个 blockout 可通过单 prompt 约 15 分钟完成，但 Seedance 适配仍有问题。
- Reuse: 适合作为 MCP blockout 能力和问题记录。
- Text: Blender MCP w/ Codex 5.5 or OPUS 4.8 is seriously pretty cracked... This entire block out was one-shot with a single prompt in about 15 minutes. Only problem I am having now is getting Seedance to use it properly 😅 Please feel free to use it and post your results below 👇 https://t.co/IfqFw3DReO

### 14. Blender previz + Comfy + 三输入控制
- URL: https://x.com/JMSvid/status/2070258132840796579
- Author: @JMSvid
- Tier: `strong`
- Category: `comfyui_camera_control`
- Metrics: likes=73, views=3720
- Why: 说明用 Blender previz 作为 guide，并配 upright/upside-down reference frames。
- Reuse: 适合做多输入相机控制 case。
- Text: Seedance 2 has insane motion adherence. This was a test to see how far I could push camera control by using a Blender previz as the guide in Comfy. The model had three inputs: - the Blender previz - a reference frame for the upright world - a reference frame for the upside-down https://t.co/LvEE9A3bF9

### 15. Blender viewport 控制 Seedance 场景导演
- URL: https://x.com/KimAkiyama81/status/2070668362229690789
- Author: @KimAkiyama81
- Tier: `medium`
- Category: `viewport_reference`
- Metrics: likes=6, views=591
- Why: 说明 Viewport in Blender gives control for directing scenes in Seedance。
- Reuse: 适合作为 viewport reference 简短案例。
- Text: Using Viewport in Blender gives incredible control for directing scenes in Seedance 2.0! https://t.co/TFOrkiJg6H

### 16. Viewport preview 动画角色
- URL: https://x.com/KimAkiyama81/status/2070266267051667505
- Author: @KimAkiyama81
- Tier: `medium`
- Category: `viewport_reference`
- Metrics: likes=2, views=154
- Why: 说明用 Blender viewport preview 在 Seedance 中 animate character，并提示 process below。
- Reuse: 适合作为 viewport preview 候选。
- Text: You can use Viewport preview in Blender and animate your character in Seedance with it! Sharing process below ⬇️⬇️⬇️ https://t.co/ZC3ny3gHmU

### 17. 土耳其语 Blender + Seedance 导演控制点
- URL: https://x.com/ai_gezgini/status/2070531406237728977
- Author: @ai_gezgini
- Tier: `medium`
- Category: `prompted_camera_direction`
- Metrics: likes=37, views=3167
- Why: 列出 camera angle、character pose、motion direction、lighting、depth、lens、composition 等控制项。
- Reuse: 适合提炼为导演参数 checklist。
- Text: Seedance 2.0 ile video üretirken Blender bilenler çok şanslı… 🎬🔥 Çünkü artık olay sadece prompt yazmak değil. Blender’da önce sahneyi kabaca kendin kuruyorsun: → kamera açısı → karakter pozu → hareket yönü → ışık atmosferi → mekan derinliği → lens hissi → kadraj kompozisyonu Blender + Seedance 2.0= Prompt değil, yönetmenlik. Prompt: 👇

### 18. 土耳其语 commando scene prompt case
- URL: https://x.com/ai_gezgini/status/2071529677353615522
- Author: @ai_gezgini
- Tier: `medium`
- Category: `prompted_camera_direction`
- Metrics: likes=2, views=433
- Why: 列出相机看向、角色进入方向、跟随角度、运动方向、景深、最终构图等。
- Reuse: 适合提炼为动作镜头 prompt/control checklist。
- Text: Blender ile komando kadın sahnesi… 🎬 Blender + Seedance 2.0 = yönetmen koltuğu sende. → kamera nereye bakacak → karakter nereden girecek → hangi açıdan takip edilecek → hareket hangi yönde akacak → sahnenin derinliği nasıl olacak → final kadrajı nerede bitecek Bugün Blender bilenler sadece 3D sahne kurmuyor; geleceğin AI video yönetmen adayları gibi çalış...

### 19. 角色 blocking + 相机 blocking 同时控制
- URL: https://x.com/SamJWasserman/status/2070742850095230991
- Author: @SamJWasserman
- Tier: `strong`
- Category: `character_and_camera_blocking`
- Metrics: likes=44, views=8117
- Why: 明确实现 camera orbit、lens choice、gunfire/cover positions/pop-outs，并说 prompt below。
- Reuse: 适合做动作场景 tactical blocking case。
- Text: Finally got this @Blender → Seedance workflow working for not just camera blocking, but character blocking simultaneously. Camera orbit, lens choice, gunfire + cover positions, pop-outs. All directed from pre-vis prior to video generation. Prompt below. Made using @dreamina_ai https://t.co/iLFCabW32W

### 20. Hermes/Krea2/ComfyUI/Blender MCP/Seedance 实验
- URL: https://x.com/SamJWasserman/status/2069656428437225826
- Author: @SamJWasserman
- Tier: `medium`
- Category: `agentic_multitool_pipeline`
- Metrics: likes=30, views=1368
- Why: 说明 agent 安装 Krea2、连接 ComfyUI 和 Blender MCP，生成 reference image + physical ref vid 后送 Seedance。
- Reuse: 适合做 multi-agent creative pipeline 候选。
- Text: Wild Experiment. Had my Hermes install @krea_ai 2 on the @NVIDIAAI Dgx Spark and connect it to @ComfyUI. Had Hermes then install @Blender and connect to it via the mcp. I had Hermes make a reference image in Krea2, + Physical ref vid in Blender. I then put all into Seedance 2.0. via @dreamina_ai.

### 21. Blender MCP viewport animation + Seedance/Magnific texture/lighting
- URL: https://x.com/techhalla/status/2070814203435274715
- Author: @techhalla
- Tier: `strong`
- Category: `blender_mcp_style_transfer`
- Metrics: likes=261, views=156578
- Why: 说明 adding 3D gives camera/element control，并声称 exactly how I did it。
- Reuse: 适合做 Blender MCP + style transfer 主案例。
- Text: Adding 3D to your animation workflow gives you full control over the camera and every element in the scene. I built this viewport animation in Blender MCP, then took it into Seedance 2.0 in Magnific to add textures and lighting. Here's exactly how I did it 👇 https://t.co/G2Q8IdfFEy

### 22. Seedance 2.0 Pro + Blender viewport style transfer
- URL: https://x.com/techhalla/status/2070832621328732396
- Author: @techhalla
- Tier: `medium`
- Category: `viewport_style_transfer`
- Metrics: likes=698, views=182967
- Why: 明确是 viewport style transfer，并指向下方流程。
- Reuse: 适合作为 style transfer 传播帖。
- Text: Seedance 2.0 pro + Blender viewport style transfer below 👇 https://t.co/bcP2Z0h5mC

### 23. Mixamo motion + Blender + Seedance 初学者路径
- URL: https://x.com/tanabe_fragm/status/2070685291183243459
- Author: @tanabe_fragm
- Tier: `medium`
- Category: `mixamo_beginner_workflow`
- Metrics: likes=54, views=4865
- Why: 测试 Blender x Seedance，并建议初学者下载 Mixamo motion 导入 Blender。
- Reuse: 适合做 beginner motion-source case。
- Text: 巷で盛り上がっているBlender × Seedance 2.0のワークフローをテスト🎥 この手法だと、確かに細かい動きのコントロールができそう。 ただ、私みたいなBlender素人だと思い通りに動かすのが難しい...😓 次は、Blender MCPを試してみようと思います。 Higgsfieldとかが簡易的なツール（Viewport Preview Referenceという名称）を公開しそうなので、そっちを待つのも手だと思います。 クリエイターさん達はこういうのが作れて本当に凄い❗️と改めて思いました😃 ちなみに、今回のモーションはMixamoというサイトから無料ダウンロードしました。 初心者の方はこういうサービスからモーションをダウンロードしてBlenderにインポートすると早いと思います。

### 24. Codex 生成 Blender 建筑和 camera work 后送 Seedance
- URL: https://x.com/6_KAKUU/status/2071051063663452374
- Author: @6_KAKUU
- Tier: `medium`
- Category: `codex_camera_work`
- Metrics: likes=4, views=169
- Why: 说明 Blender 初学第 3 天，建筑到 camera work 都由 Codex 完成，Seedance 能跟随。
- Reuse: 适合做 Codex-assisted camera work case。
- Text: Blender × Seedance 2.0ってすごいな、本当に追従してくれるんだな。 Blenderインストールして３日目なんですが、建物からカメラワークまでCodex君が全てやってくれました。 ちなみにカメラワークの指示には、少し懐かしさを感じつつある矢印（Arrow）をCodexに対して使ってみた。 https://t.co/q33raf0W4a

### 25. Blender 3D previz → Seedance anime render
- URL: https://x.com/restofart/status/2070086939756159368
- Author: @restofart
- Tier: `medium`
- Category: `anime_previz_render`
- Metrics: likes=0, views=155
- Why: 说明 full camera moves and motion preserved，定位 previz → AI-render pipeline。
- Reuse: 适合作为 anime/render pipeline case。
- Text: Made a 3D previz in Blender, then rendered it as anime with Seedance — all inside Doitong. Full camera moves and motion preserved. This previz → AI-render pipeline is how AI filmmaking beats "prompt and pray." Anyone else building this way? 👇 https://t.co/z0woB9BNFg

### 26. Seedance + Claude + Blender 导航式电影控制
- URL: https://x.com/Flagiuss/status/2071335816190902624
- Author: @Flagiuss
- Tier: `medium`
- Category: `claude_blender_camera_control`
- Metrics: likes=75, views=13137
- Why: 强调像 3D environment 一样导航电影以获得 camera/movement/pacing control。
- Reuse: 适合做未来式 camera control 叙事素材。
- Text: Seedance + Claude + Blender A future of AI film making is definitely in ability to navigate within films as if in 3D environments . That can give a lot of camera control, movements control, pacing and much more! Visual direction and finetuning will be mind blowing. #seedance #aivideo #aifilmmaking

### 27. Blender 初学 + agent 辅助 + Seedance reference video 测试
- URL: https://x.com/Ukiyo_il/status/2071098235268071877
- Author: @Ukiyo_il
- Tier: `medium`
- Category: `beginner_agent_reference_video`
- Metrics: likes=15, views=281
- Why: 说明由 agent 辅助做 Blender 参考视频，并测试复杂 HIPHOP dance 进入 Seedance。
- Reuse: 适合作为 beginner/agent-assisted experiment。
- Text: #Blender チャット内で話題だったBlenderを初めて触ってみました！ 操作画面はこんな感じ・・・マジわからにゃい（笑） 普段HANAKOぐらいしか触らないから（笑） これをエージェントに頼んで色々してもらう感じ 色々試してどっかからダウンロードでCodexちゃんに頼んで出来たのが２枚目の動画・・全然改善の余地はある ちょっと難しめのHIPHOPのダンスを渡してみたら・・・全然ダメでした・・３枚目の動画参考 所感は参照動画をseedanceに渡すとそこそこ難しいダンスもしてくれるのでどうだろう？って感じでした！ ・・素人の所感です（笑）

### 28. Viewport preview 导出后进 Seedance
- URL: https://x.com/DiabloNemesis/status/2070441923706503380
- Author: @DiabloNemesis
- Tier: `strong`
- Category: `viewport_preview_to_seedance`
- Metrics: likes=244, views=10365
- Why: 明确流程：Blender block out scene、export viewport preview、抽第一帧转真实图、作为 reference 送 Seedance。
- Reuse: 适合做 viewport preview → Seedance 的短教程案例。
- Text: prompting is the old way. this is directing. – block out the scene in blender – export the viewport preview – extract the first frame → turn it into a realistic image in @morphic – drop it into as reference to video – Seedance 2.0 does the rest https://t.co/gg25Iu9VgF

### 29. FBX clay model + Claude keyframe + Seedance refs
- URL: https://x.com/Viggle_PINOC/status/2070183934265012392
- Author: @Viggle_PINOC
- Tier: `strong`
- Category: `fbx_clay_pass_reference`
- Metrics: likes=2, views=377
- Why: 具体 step：Blender 导入 FBX 到 clay model、设置 camera、Claude keyframe camera moves、导出 mp4 给 Seedance refs。
- Reuse: 适合做 FBX/Mixamo 动画参考流程。
- Text: Step 2: Blender Import the FBX onto a clay model, then set your camera. We had Claude keyframe the camera moves, adjusted the angles, and rendered the clay pass. Export to mp4 for Seedance refs. https://t.co/kdZI8bWdi1

### 30. Seedance 角色 + ComfyUI/Claude + Blender/AE 后期
- URL: https://x.com/VengadaS65199/status/2070049247823859770
- Author: @VengadaS65199
- Tier: `medium`
- Category: `hybrid_short_film_pipeline`
- Metrics: likes=25, views=2742
- Why: 说明两晚完成创作，Seedance 做角色，ComfyUI 节点由 Claude 辅助，其余在 Blender 和 AE。
- Reuse: 适合做完整短片制作管线候选。
- Text: Pulled two all nighters making this. wrote, animated, edited, did SFX. couldn't sleep with the idea in my head. Seedance 2 for the characters. custom @ComfyUI nodes via Claude for the time-slice. rest in @Blender and AE https://t.co/Xpot8IrVJG

### 31. 不用 start frame 的 Blender blockout reference
- URL: https://x.com/magneticskiff/status/2070711034793361559
- Author: @magneticskiff
- Tier: `medium`
- Category: `no_start_frame_blockout`
- Metrics: likes=1, views=70
- Why: 说明 Seedance + Blender blockout 可以使用 references 而非 starter frames，环境参考有足够细节时效果较好。
- Reuse: 适合做 reference-only variant 候选。
- Text: Seedance + Blender blockout using references, no start frame. I've been messing with the Blender blockout, but for a lot of my own workflow I need to be able to do it using references without starter frames. This works well so far if you're environmental reference has enough discrete details.

### 32. 同一 reference video 生成不同世界
- URL: https://x.com/koldo2k/status/2071307945002815967
- Author: @koldo2k
- Tier: `medium`
- Category: `same_reference_different_worlds`
- Metrics: likes=238, views=13010
- Why: 说明用 Blender 控制、Seedance 想象，同一 reference video 生成不同 worlds，并提到 prompt。
- Reuse: 适合做 style/world variation case。
- Text: Control with Blender, imagine with Seedance 2.0 🎬 Same reference video, different worlds. Here's the prompt I used to generate the video. The beginning is always the same only what happens in each scene changes. https://t.co/F5zFzXr6lu

### 33. Mixamo 多角色动作 + Blender storyboard + Seedance
- URL: https://x.com/dave392750/status/2070851042661810551
- Author: @dave392750
- Tier: `medium`
- Category: `mixamo_storyboard_experiment`
- Metrics: likes=58, views=18475
- Why: 日文说明 Blender storyboarding、Mixamo 多体动作、Seedance 处理跳跃/动作的实验问题。
- Reuse: 适合做 Mixamo motion complexity/troubleshooting case。
- Text: Blender絵コンテ、もう一作作ってみました。 メイドさんが走る映像ですが、はい最初から嘘が入ってますね^^; 本当はジャンプさせたかったのですが、うまくいかず、そこはSeedanceさんにお任せしました。 今回、Mixamoを動きに合わせて何体も使ったため、そこの収拾に困ることに^^; #capcut生成ai @capcutapp_jp

### 34. Codex MCP 操作 Blender 导出视频给 Seedance
- URL: https://x.com/Toshi_nyaruo_AI/status/2071149652905537541
- Author: @Toshi_nyaruo_AI
- Tier: `medium`
- Category: `codex_blender_mcp_reference`
- Metrics: likes=39, views=1700
- Why: 说明用 Codex MCP 直接操作 Blender 并导出视频，初学 2 小时完成。
- Reuse: 适合做 beginner Codex MCP workflow。
- Text: seedance 2.0 & Blender で動画作成💞 CodexのMCPを使ってBlenderを直接操作して、動画の書き出しまで行っています。 Blenderは初めて触っているのですが、起動して2時間弱でここまで来ました。 seedanceに限らず、動画生成AIは狭い空間での描写が苦手なのですが、これで解消できるような気がします。 にしても、Blender のキャラがぁぁ。もっと精進します😇

### 35. 构图 reference + personal/car reference 组合
- URL: https://x.com/Gen_x111x/status/2069803766581526534
- Author: @Gen_x111x
- Tier: `medium`
- Category: `composition_reference_multi_ref`
- Metrics: likes=19, views=970
- Why: 日文说明用 Blender 构图 reference、个人 reference、panda car reference 组合，强调 CG camera instruction 重要。
- Reuse: 适合做 multi-reference composition case。
- Text: 今回のおふざけAIですが Blenderで構図リファレンス と 私のリファレンス と パンダカーのリファレンス をうまいこと組み合わせる作りをしてみました🙏 CGでのカメラワーク指示は非常に重要です。これがないと言うこと聞かないんです そしてseedanceはリファレンス命ですな https://t.co/MQMrxhitOT

## original_supporting_detail (5)

### 1. Viewport playblast 作为 Seedance reference 的教程回复
- URL: https://x.com/reidhannaford/status/2071175948188144061
- Author: @reidhannaford
- Tier: `strong`
- Category: `how_to_reply`
- Derived from: reidhannaford workflow thread
- Metrics: likes=0, views=52
- Why: 给出 Blender 基础、Midjourney first frame、Blender cubes/keyframes、导出 viewport playblast、上传 Seedance 的步骤。
- Reuse: 适合作为 repo 的 practical how-to/source note。
- Text: @Prof_Mcgruff 1. Learn the basics of blender. How to move around the viewport, how to add cubes and objects and move them around. How to add a camera, and use keyframes to animate it over time. Tons of YouTube tutorials on this stuff 2. Use Midjourney to create an image you’re happy with as the first frame in your shot. 3. Back in blender, roughly place c...

### 2. Midjourney + Blender blockout + Seedance 的补充说明
- URL: https://x.com/reidhannaford/status/2069919764563071178
- Author: @reidhannaford
- Tier: `supporting`
- Category: `how_to_reply`
- Derived from: reidhannaford workflow thread
- Metrics: likes=0, views=211
- Why: 用回复形式确认核心流程，并补充 moodboards/profile/prompt 调整。
- Reuse: 可作为主流程的补充证据。
- Text: @EvanDowning Basically just what I wrote in this post above haha! Start frame in Midjourney, blockout in Blender with camera animation, give both to Seedance with a prompt for the action. There’s some additional stuff like how to work with midjourney - I use a custom profile and moodboards and stuff. Check out the previous posts on my account I’ve posted ...

### 3. Seedance 接收 Blender playblast mp4
- URL: https://x.com/reidhannaford/status/2069953631776845893
- Author: @reidhannaford
- Tier: `supporting`
- Category: `technical_detail`
- Derived from: reidhannaford workflow thread
- Metrics: likes=1, views=143
- Why: 确认 Seedance accepts video reference，并使用 start frame image + Blender viewport playblast mp4。
- Reuse: 适合作为 input requirements/asset format 说明。
- Text: @TahirAz08029661 Seedance accepts video reference! So I just uploaded the start frame image, and the video playblast mp4 from Blender.

### 4. Viewport playblast mp4 作为 video reference
- URL: https://x.com/reidhannaford/status/2069787619337097234
- Author: @reidhannaford
- Tier: `supporting`
- Category: `technical_detail`
- Derived from: reidhannaford workflow thread
- Metrics: likes=1, views=120
- Why: 确认 Blender mp4 viewport playblast 可作为 video reference。
- Reuse: 适合作为技术细节引用。
- Text: @John58176513 yeah! It's just an mp4 viewport playblast from blender, added as a video reference. Apparently Seedance 2.5 will be able to work with actual 3D files but we'll see.

### 5. 制作耗时拆解
- URL: https://x.com/reidhannaford/status/2070168175069519888
- Author: @reidhannaford
- Tier: `supporting`
- Category: `production_costing`
- Derived from: reidhannaford workflow thread
- Metrics: likes=2, views=859
- Why: 拆分 start frame、Blender blockout/camera animation、Seedance 多次生成、后期音乐音效耗时。
- Reuse: 适合做 production workflow/time budget 说明。
- Text: @hayden_schwartz Depends on the complexity of the shot but the total is probably something like 5 hours. I spend a decent chunk of time on the start frame, and I've done a lot of upfront work curating my moodboards and style references that do a lot of heavy lifting there. Then the blockout and camera animation in Blender can be simple or difficult depend...

## tool_workflow_aggregator (2)

### 1. 同一 Blender motion 多风格探索
- URL: https://x.com/ComfyUI/status/2070194583343153570
- Author: @ComfyUI
- Tier: `strong`
- Category: `comfyui_style_variation`
- Derived from: AIWarper/reidhannaford/JMSvid clips credited
- Metrics: likes=412, views=21800
- Why: ComfyUI + Seedance 参考图，在保持 motion/camera movement 的同时探索不同 looks。
- Reuse: 适合做 style variation / batch creative direction case。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: One animation. Different visual styles. This workflow uses Seedance 2.0 in ComfyUI with reference images to explore different looks while preserving the same motion and camera movement. In this example, the animation starts with a simple Blender scene, making it easy to compare different creative directions. Featured clips courtesy of @AIWarper, @reidhann...

### 2. Simple Blender animation 到 stylized AI video
- URL: https://x.com/ComfyUI/status/2070522636254560689
- Author: @ComfyUI
- Tier: `strong`
- Category: `comfyui_style_variation`
- Derived from: ComfyUI workflow resource/link
- Metrics: likes=236, views=11841
- Why: 明确 basic 3D motion as guide + reference image look/detail。
- Reuse: 适合做 ComfyUI workflow use case。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: Simple Blender animation → Seedance 2.0 → stylized AI video. This workflow uses basic 3D motion as a guide, then applies the look and detail from a reference image. To try this workflow, link below 👇 https://t.co/QfvT9JJh3n

## derivative_summary (16)

### 1. 中文完整工作流拆解 + prompt 片段
- URL: https://x.com/block0_eth/status/2069650081733570856
- Author: @block0_eth
- Tier: `strong`
- Category: `zh_workflow_breakdown`
- Derived from: reidhannaford hybrid workflow
- Metrics: likes=349, views=15521
- Why: 中文详细拆解 Blender camera blocking、Midjourney start frame、Seedance final video，并给出 prompt 片段。
- Reuse: 适合直接转中文 use case。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: 好莱坞公司老板该睡不着了，ai视频离院线级电影更近了。 这个工作流 是 Blender + Midjourney + Seedance 2.0 的混合（Hybrid）AI视频生成流程， 主要解决目前纯AI视频工具相机运动不精确的问题。 它让创作者能像传统电影一样，先在Blender 3D软件里精确编辑好好相机运动，再用Seedance 2.0生成高质量视频画面。 以下是完整的工作流步骤（以帖子里那个夜市男人走路的例子为例）： 1. Blender 里做相机 Blocking - 用一个简单的低模人物代替真实角色。 - 在 Blender 里精确动画相机运动：跟拍、环绕、推拉、轨道等。 - 导出相机运动参考视频。 2. Midjourney 生成起始帧（Start Frame） - 根据想要的画面风格、人物...

### 2. Hybrid AI workflow 摘要
- URL: https://x.com/RoundtableSpace/status/2069594585647472974
- Author: @RoundtableSpace
- Tier: `medium`
- Category: `hybrid_previs_camera_control`
- Derived from: 2069074506849685773
- Metrics: likes=66, views=47206
- Why: 清晰总结 precision camera control：Blender motion reference + Midjourney start frame + Seedance。
- Reuse: 可作为同类工作流的传播证据。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: Every filmmaker needs to try this hybrid AI workflow for precision camera control. Block out your camera move in Blender to create a motion reference. Generate your start frame in Midjourney to match the pose and composition. Feed both into Seedance. It tracks the move almost exactly. This is one of the most powerful hybrid pipelines out there right now.

### 3. Blender 作为导演 storyboard/shot
- URL: https://x.com/adityarao310/status/2071451152600760635
- Author: @adityarao310
- Tier: `strong`
- Category: `hybrid_previs_camera_control`
- Derived from: reidhannaford/demo being discussed
- Metrics: likes=6, views=501
- Why: 解释 reference frame、Blender placeholder geometry、Seedance render 的职责分离。
- Reuse: 适合做“导演控制 vs prompt hoping”的论证案例。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: Blender has always been the director's storyboard for 3D work. Now it can be the shot itself. The workflow is simple: generate a reference frame in Midjourney, block out your action in Blender using basic placeholder geometry, then feed both into Seedance 2.0. The model takes your rough timing and spatial layout and renders it as a believable live-action ...

### 4. 3D blocking 到 cel-anime sequence
- URL: https://x.com/Genflickmovies/status/2069934537006612759
- Author: @Genflickmovies
- Tier: `medium`
- Category: `anime_previz_render`
- Derived from: Blender-to-Seedance 3D blocking trend / GenFlick promo
- Metrics: likes=8, views=612
- Why: 该帖描述 3D blocking → Seedance → anime sequence，但经复核更像趋势/产品账号转述，不作为一手 use case。
- Reuse: 仅作为二次传播/产品叙事参考；不要作为原创玩法来源。
- Text: This is how movies get made now. Seedance 2.0 turns simple 3D blocking into full cel-anime sequences. No need to hand-draw every frame — just block out your shots in Blender, feed it to Seedance, and watch it transform into a cinematic anime scene. At GenFlick, workflows like this are how we’re building the future of filmmaking. AI isn’t replacing animato...

### 5. 动作场景复述与应用
- URL: https://x.com/Genflickmovies/status/2071384031610945792
- Author: @Genflickmovies
- Tier: `medium`
- Category: `action_choreography`
- Derived from: 2070145120658137385
- Metrics: likes=0, views=66
- Why: 复述复杂 action scene 的 3 步流程，并明确 indie filmmaker action sequence 应用。
- Reuse: 可作为动作戏 workflow 的传播证据。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: This is absurd. 🎬 You can choreograph a complex action scene in Blender with basic shapes, then let Seedance make it real. Reid Hannaford just showed the AI filmmaking workflow: 1️⃣ Generate a start frame in Midjourney 2️⃣ Block out the action in Blender 3️⃣ Feed both to Seedance At GenFlick, we live in this workflow. The difference between describing a s...

### 6. Claude Code + Blender MCP + Mixamo + Seedance
- URL: https://x.com/Genflickmovies/status/2070523006275739680
- Author: @Genflickmovies
- Tier: `medium`
- Category: `agentic_blender_mcp`
- Derived from: AIWarper/Blender MCP no-click trend
- Metrics: likes=0, views=107
- Why: 提出无鼠标 Blender、Mixamo、Seedance 的 10 分钟动画流程。
- Reuse: 适合做 agent-assisted animation workflow 候选。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: Entire Seedance animation done without a single mouse click in Blender. Claude Code + Blender MCP + Mixamo + Seedance. 10 minutes. Zero clicks. Cinema quality. Take it if you need it. https://t.co/5gJPu3mWsB

### 7. Claude + Blender 低成本演出设计图
- URL: https://x.com/taziku_co/status/2071511585324163365
- Author: @taziku_co
- Tier: `medium`
- Category: `claude_blender_low_cost_previs`
- Derived from: Flagiuss / Claude + Blender example
- Metrics: likes=23, views=2841
- Why: 说明不用精细 3D 模型，只用板状人物也可预先决定 camera movement/subject position/flow。
- Reuse: 适合做低成本 previs/control case。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: Seedance + Claude + Blender 作り込んだ3Dモデルではなく、 人物を板として配置しただけのラフな3Dでも、カメラ移動・被写体位置・画面内の流れを先に決められる。 重要なのは、AIに渡すための演出設計図を低コストで作れることだと思う。 Creator：@Flagiuss https://t.co/LC0VsAXe7X

### 8. 日文总结：Midjourney start frame + Blender pose/camera + Seedance
- URL: https://x.com/taziku_co/status/2069635805858214298
- Author: @taziku_co
- Tier: `medium`
- Category: `jp_summary_workflow`
- Derived from: 2069420552394043625 / reidhannaford
- Metrics: likes=140, views=9144
- Why: 总结两角色、对话、camera work 可通过 3D 控制。
- Reuse: 可作为日文市场解释素材。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: 3DはAI動画制作の制御のキーとなる。 この事例では、 ・Midjourneyで開始フレームを作る ・Blenderでポーズとカメラを合わせる ・Seedanceで映像化する という流れで、2人のキャラクター、会話、カメラワークをかなり意図的に扱っています。 via：@reidhannaford https://t.co/THBrDmaUIP

### 9. Blender action choreography → Seedance render
- URL: https://x.com/minchoi/status/2071434710811553945
- Author: @minchoi
- Tier: `medium`
- Category: `action_choreography`
- Derived from: curated list / linked example
- Metrics: likes=22, views=4215
- Why: 简短但直接：rough shapes in Blender became a cinematic action scene。
- Reuse: 适合作为高热度短传播案例。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: 1. Blender action choreography → Seedance render Rough shapes in Blender became a real cinematic action scene. https://t.co/J7bBjcn5lQ

### 10. 日文总结：Midjourney 角色 + Blender camera + Seedance
- URL: https://x.com/Botan_cr/status/2070832324422553711
- Author: @Botan_cr
- Tier: `medium`
- Category: `jp_summary_workflow`
- Derived from: reidhannaford credited
- Metrics: likes=108, views=17908
- Why: 总结 Midjourney 生成角色、Blender 配置和 camera work、Seedance 整合。
- Reuse: 适合做日文市场 explaining post。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: AIフィルムメイキングが、AIによる生成からアニメーション制作へ進化 Midjourneyで生成したキャラをBlenderで配置・カメラワークを組み、Seedanceで統合している。荒々しいハンドヘルドの質感を完璧に再現し、演出の自由度が増えています！ by : reidhannaford氏 https://t.co/SJAao6jCwP

### 11. 中文三步 AI 电影工作流
- URL: https://x.com/mubeitech/status/2070260583367094503
- Author: @mubeitech
- Tier: `strong`
- Category: `zh_workflow_breakdown`
- Derived from: reidhannaford-style three-step demo
- Metrics: likes=8, views=1980
- Why: 中文说明 Midjourney 起始帧、Blender 灰色方块排运动轨迹、Seedance 生成电影画面。
- Reuse: 适合直接转中文 README/use-case。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: AI 视频要进专业剧组，不能只靠嘴说。 导演需要绝对控制，不能跟 AI 玩盲盒。 一种全新的 AI 电影工作流诞生了。 它能把导演在 3D 软件里的“排练”，直接变成电影大片。 过程非常简单： 1. 用 Midjourney 生成一张高精度的起始帧； 2. 在 Blender 里用最简陋的灰色方块，把运动轨迹排出来； 3. 把这两样一起喂给视频模型 Seedance 2.0。 看看这个对比。 上面是 Blender 里极简的灰色预演，下面是 AI 渲染出的电影级公路飞驰镜头，远山和运动模糊完全严丝合缝。 这就是从“玩具”到“生产力工具”的跨越。 AI 终于开始听懂导演的指挥棒了。 https://t.co/Au9ZrQ5EGb

### 12. 中文总结：不是一句话生成，而是可控流水线
- URL: https://x.com/lemondooe/status/2069805496740295073
- Author: @lemondooe
- Tier: `medium`
- Category: `zh_summary_workflow`
- Derived from: general commentary on Midjourney/Blender/Seedance flow
- Metrics: likes=1, views=115
- Why: 概括 Midjourney 出帧、Blender 控镜头、Seedance 做运动的可控 workflow。
- Reuse: 适合做中文定位句/intro 素材。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: AI 电影这个 workflow 有意思。 不是一句话生成视频，而是 Midjourney 出帧、Blender 控镜头、Seedance 做运动。 真正能进生产的 AI，往往不是魔法按钮，是可控流水线。 https://t.co/otbovkpWyq

### 13. Midjourney + Blender + Seedance 一体导演流
- URL: https://x.com/naveedullah600/status/2069443921126772828
- Author: @naveedullah600
- Tier: `medium`
- Category: `directing_not_prompting`
- Derived from: summary/reaction to workflow
- Metrics: likes=1, views=40
- Why: 总结 consistent characters、precise camera moves、dialogue in one workflow。
- Reuse: 适合作为传播型 use case quote。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: AI filmmaking is changing fast. @Midjourney + @Blender + @Seedance can now deliver consistent characters, precise camera moves, and dialogue in one workflow. This feels less like prompting and more like directing. What would you create with it? https://t.co/ozSi60so5l

### 14. Midjourney frames + Blender poses + Seedance
- URL: https://x.com/aiseomastery/status/2069807761714717166
- Author: @aiseomastery
- Tier: `medium`
- Category: `camera_control_dialogue_summary`
- Derived from: headline summary of workflow
- Metrics: likes=0, views=173
- Why: 总结 camera control and dialogue：Midjourney frames、Blender poses、Seedance combine。
- Reuse: 适合做 camera + dialogue workflow 传播证据。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: AI FILMMAKING WORKFLOW NAILS CAMERA CONTROL AND DIALOGUE Midjourney frames, Blender poses, and Seedance combine for two consistent characters. https://t.co/WXKZBLIeT9

### 15. Blender pose/animate 后交 Seedance render
- URL: https://x.com/somi_ai/status/2069602065131966790
- Author: @somi_ai
- Tier: `medium`
- Category: `pose_animate_then_render`
- Derived from: commentary on AI video workflow trend
- Metrics: likes=38, views=4113
- Why: 说明干净镜头和一致角色来自先在 Blender pose/animate，再交给 Seedance render。
- Reuse: 适合做“模型负责填像素，Blender 负责导演”的定位案例。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: AI video still can't take direction. So the people getting clean camera moves and consistent characters do it the old way: pose and animate it in Blender, then feed that to Seedance to render. Midjourney sets the frame, Blender directs, the model just fills in pixels. Pure text-to-video won't beat this until the model can take that direction on its own.

### 16. Midjourney/ChatGPT start frame + Blender block action + Seedance
- URL: https://x.com/MarkAIbuilder/status/2070582870939410936
- Author: @MarkAIbuilder
- Tier: `medium`
- Category: `three_tool_ai_filmmaking_stack`
- Derived from: three-tool stack summary
- Metrics: likes=0, views=80
- Why: 三步总结新 AI filmmaking stack：start frame、Blender basic shapes block action、Seedance real scene。
- Reuse: 适合做简短三工具 stack 案例。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: The new AI filmmaking stack is wild: 1. Midjourney/Chat GPT → start frame 2. Blender → block the action with basic shapes 3. Seedance 2.0 → turns it into a real scene No film school. No crew. Just taste + 3 tools. https://t.co/Q03b73OZqt

## derivative_explainer (5)

### 1. 日本语 Blender x Seedance workflow explainer
- URL: https://x.com/ai_hakase_/status/2071492363256549592
- Author: @ai_hakase_
- Tier: `medium`
- Category: `jp_workflow_explainer`
- Derived from: Japanese explainer/link post
- Metrics: likes=24, views=3184
- Why: 解释用 Blender 控制相机/角色位置、Seedance/Magnific 处理质感和风格。
- Reuse: 适合作为日文市场 workflow 叙事素材。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: 【Blender×Seedance 2.0】AI動画の弱点を克服！3D空間で完全制御する次世代映像制作ワークフロー✨ 👉 https://t.co/CdmhowSv4K 従来のAI動画生成って「プロンプトを入れて、あとは運任せ…🎲」という部分が多かったですよね。それを根本から変える、圧倒的な映像制作手法が登場しました！ おなじみの3Dソフト「Blender」と、最新AIツール「Seedance 2.0 pro」を連携させた、まさに良いとこ取りのハイブリッドワークフローです。 🌟 注目したいポイントがこちら！ ・【動きを完全コントロール】 Blender上でカメラの動きやキャラクターの配置をしっかり決めてからAIに連携（Blender MCPという仕組みで3Dの空間情報を伝達）するため、AI動画特有の「おか...

### 2. 日本语三步混合 workflow
- URL: https://x.com/ai_hakase_/status/2071429951723618582
- Author: @ai_hakase_
- Tier: `medium`
- Category: `jp_workflow_explainer`
- Derived from: Japanese explainer/link post
- Metrics: likes=26, views=2405
- Why: 列出 Midjourney first image、Blender blocking、Seedance input 的三步。
- Reuse: 可复用为日文三步教程结构。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: 【Blender×Seedance】AI動画のガチャ感を克服！空間を「演出」する新世代ハイブリッドワークフロー 👉 https://t.co/Xmga3eeGsf AI動画生成で「キャラクターや物体が溶けてしまう」「思った通りのカメラワークにならない」と悩んだことはありませんか？そんな課題を劇的に解決する、革新的なハイブリッドワークフローが登場しました！✨ 今回の手法は、単にAIにプロンプトを投げて「運任せ」で動画を作るのではなく、クリエイターが意図した通りの動きを完全にコントロールするものです！ 具体的な手順はこちらの3ステップです👇 1️⃣ Midjourneyでベースとなる「最初の1枚（高クオリティな画像）」を生成する 2️⃣ Blenderでざっくりとしたカメラワークや物体の配置、タイミングを設計...

### 3. Claude + Blender 生成 3D 动作/运镜素材
- URL: https://x.com/tkz_aiart/status/2071023469861712294
- Author: @tkz_aiart
- Tier: `medium`
- Category: `claude_blender_reference_video`
- Derived from: Japanese trend explainer
- Metrics: likes=16, views=998
- Why: 日文说明用 Claude 连接 Blender 3D app，制作动作和 camera work，再作为素材读入 Seedance。
- Reuse: 适合做 Claude-assisted Blender reference video 候选。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: じゃじゃん！ 最近の流行りコレ！ 3Dで動きやカメラワークつけて動画生成。 ClaudeにBlenderという3Dアプリ MCG連携できるから、意外と簡単。 できたらSeedanceに素材として読み込めばいい！ https://t.co/PpQGrGfmbf

### 4. 立方体比详细 3D 人偶更适合作运动参考
- URL: https://x.com/ai_hakase_/status/2070976470374056193
- Author: @ai_hakase_
- Tier: `medium`
- Category: `simple_cubes_reference`
- Derived from: Japanese explanatory summary
- Metrics: likes=11, views=1458
- Why: 解释在 Seedance 中简单 cubes 更利于读取 camera/position relation，避免详细人偶限制动作。
- Reuse: 适合做 reference design guideline / limitation insight。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: AI動画生成の常識を覆す！Seedanceでは「詳細な人形」より「立方体」が最強な理由 🚀 AI動画生成ツール「Seedance」での驚きの新常識です！ キャラクターの参照モデルとして「詳細な3D人形」を使うよりも、シンプルな「立方体（ボックス）」を配置する方が、圧倒的にクオリティの高い動画が作れます！ 理由は、3D人形が詳細すぎるとAIが「固定された静止物」と認識し、動きに制限がかかってしまうため。 一方、シンプルな立方体なら、AIがカメラの動きや位置関係だけを読み取り、自由で自然なアクションを生成してくれます。 Blenderで簡単な箱を置いてカメラを動かし、Seedanceに読み込ませるだけの超効率ワークフロー。制作コストを大幅に削減しながら、まるで映画のようなカメラワークを実現できます！ #AI動...

### 5. Blender + Seedance 动画制作手法总结
- URL: https://x.com/aiaicreate/status/2070418984277778909
- Author: @aiaicreate
- Tier: `medium`
- Category: `anime_production_workflow`
- Derived from: news/summary post
- Metrics: likes=26, views=2824
- Why: 总结 Blender 物理/光源/构图与 Seedance finishing 的动画制作方向。
- Reuse: 适合作为 anime production pipeline 背景素材。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: 3DソフトBlenderと動画生成AIの連携によるアニメ制作手法が注目。 表情作成を省き物理演算と光源調整に注力してAIに仕上げを任せるワークフロー。伝統技術とAIの融合への高評価や、個人による高品質アニメ制作の実現に驚く声が多数。 #Seedance #3DCG URLはリプ⬇️ https://t.co/lCjXJbjowX

## supporting_comment (1)

### 1. 基础 cubes 低成本 block camera movement
- URL: https://x.com/aiseomastery/status/2070638985169526904
- Author: @aiseomastery
- Tier: `supporting`
- Category: `low_effort_camera_blocking`
- Derived from: reply validating low-effort camera blocking
- Metrics: likes=2, views=218
- Why: 回复中明确 basic cubes in Blender 用于 block camera movement before Seedance。
- Reuse: 可作为低成本 workflow 的补充证据。
- Text: @reidhannaford Using basic cubes in Blender just to block camera movement before feeding it to Seedance is such a smart low effort workflow

## guideline_commentary (1)

### 1. 需要完整搭建并动画化 3D scene
- URL: https://x.com/renqw5271/status/2070495078712230271
- Author: @renqw5271
- Tier: `medium`
- Category: `full_scene_animation_guideline`
- Derived from: quality guideline/opinion, not a specific shared use case
- Metrics: likes=0, views=62
- Why: 指出不要只搭简单 scene，而要 build out scene 并按目标运动 animate，再 feed dynamic 3D scene into Seedance。
- Reuse: 适合做 quality guideline / advanced workflow note。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: These days everyone's trying to use 3D task-specific scenes to generate videos. But if you're just throwing together a few simple scenes and character actions in Blender, it's not gonna do much for the final video quality. You really need to fully build out the whole scene, then animate that 3D scene based on how you want it to move. Only then can you fee...

## idea_or_speculation (1)

### 1. Tripo/Meshy 3D character → Blender → Seedance reference
- URL: https://x.com/tanabe_fragm/status/2071048943333790047
- Author: @tanabe_fragm
- Tier: `medium`
- Category: `mesh_to_video`
- Derived from: Tripo/Meshy -> Blender -> Seedance idea, not demonstrated
- Metrics: likes=3, views=431
- Why: 提出用 Tripo/Meshy 生成 3D 角色、放进 Blender、给 Seedance 参考视频化的手法。
- Reuse: 适合做 3D character generation pipeline 候选。（注意：该条不是一手玩法分享，主列表中排除，仅作背景/二次传播参考。）
- Text: TripoやMeshyで3Dキャラクターを生成。 そしてBlenderに置いて、それをSeedance 2.0で参照して動画化、という手法もありかも。 ただ、Seedance 2.0の場合はキャラクターシートを渡せばいいだけかも、という気もしますが😅 動画のシチュエーションによって色々な手法を組み合わせ、最適化できるようになりたい😃

## watch_future (1)

### 1. Flick 内测 Blender + Seedance workflow，教程即将发布
- URL: https://x.com/flickartHQ/status/2071295701984976987
- Author: @flickartHQ
- Tier: `watch`
- Category: `future_workflow_tutorial`
- Derived from: tutorial coming soon
- Metrics: likes=23, views=839
- Why: 说明团队在测试 3D modeling + Seedance workflow，但教程尚未发布。
- Reuse: 作为后续跟踪候选，不作为已可复现主案例。
- Text: Blender + Seedance 2.0 is wild! Flick team has been internally testing Blender + Seedance 2.0, along with 3D modeling + Seedance 2.0 workflows, and it’s opening up a whole new way to direct AI shots. Workflow tutorial coming soon. https://t.co/tCwKB0wrU5
