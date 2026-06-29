# Primary Blender + Seedance Use Cases

Source copy: `data/x-search/blender-seedance/primary-use-case-posts.json`
Count: 35

Only primary original posts are included here. Derivative summaries, reposts, tool aggregators, comments, and watch items are excluded.

## 1. Blender 灰盒预演 + 起始帧 + Seedance motion reference
- URL: https://x.com/noman23761/status/2071534020014563328
- Author: @noman23761
- Tier: `strong`
- Category: `hybrid_previs_camera_control`
- Why: 完整说明从 image model 起始帧、Blender 灰盒场景/相机动画，到 Seedance 参考视频生成的端到端流程。
- Reuse: 可直接改写成“用 Blender blockout 精准导演 AI 镜头”的主 use case。
- Text: Spent months prompting video models and only just figured out what was missing: prompting is describing a shot, you write what you want and hope the model interprets the camera the way you meant. Blocking it out in Blender first is directing it. The workflow is simpler than it sounds. Generate a start frame on an image model. Then in Blender, build the scene with nothing but basic shapes, no modeling, no textures,...

## 2. Blender 运镜参考 + Midjourney 起始帧 + Seedance
- URL: https://x.com/reidhannaford/status/2069074506849685773
- Author: @reidhannaford
- Tier: `strong`
- Category: `hybrid_previs_camera_control`
- Why: 列出 3 步 workflow：Blender block camera、Midjourney start frame、两者送入 Seedance。
- Reuse: 适合做 precision camera control 的基础案例。
- Text: This is wild. Every filmmaker needs to try this hybrid AI workflow for precision camera control: 1) Block out your camera in Blender to create a motion reference and animate the camera move 2) Generate your start frame in Midjourney to match the pose and composition 3) Feed both to Seedance It tracks the move almost exactly. This is the most powerful hybrid pipeline I've tried yet.

## 3. 多角色 + 对话 + 精准运镜
- URL: https://x.com/reidhannaford/status/2069420552394043625
- Author: @reidhannaford
- Tier: `strong`
- Category: `multi_character_dialogue`
- Why: 说明用 Midjourney 起始帧、Blender pose/camera，再交给 Seedance，实现两个一致角色和对话镜头。
- Reuse: 适合做多角色表演/对话场景 use case。
- Text: I'm blown away. This AI filmmaking workflow for precise camera control, multiple characters, and dialogue is insane: 1. Generate a start frame in Midjourney 2. Match the poses in Blender, animate the camera 3. Feed both to Seedance I didn't think this would work. Two consistent characters, solid performances, the move tracked perfectly through the entire beat. Even the soup looks great.

## 4. 基础几何体驱动多角色镜头
- URL: https://x.com/reidhannaford/status/2069783215829569746
- Author: @reidhannaford
- Tier: `strong`
- Category: `multi_character_action`
- Why: 强调 3D 参考不需要精美，只用 basic shapes 也能驱动精确多角色 shot。
- Reuse: 适合做“低成本 3D reference 就够用”的案例。
- Text: This is getting ridiculous. You need to try this AI filmmaking workflow. My Blender reference is embarrassingly simple. You can drive a precise multi-character shot with nothing but basic shapes. 1. Generate a start frame in Midjourney 2. Block out the scene in Blender with boxes, animate the camera 3. Feed both to Seedance This feels like a real unlock. Your 3D reference doesn't need to look good.

## 5. 复杂动作场景编排
- URL: https://x.com/reidhannaford/status/2070145120658137385
- Author: @reidhannaford
- Tier: `strong`
- Category: `action_choreography`
- Why: 明确说明用 Blender basic shapes 编排 action scene，Seedance 负责真实化。
- Reuse: 适合做动作戏/空间调度 use case。
- Text: Ok, this is absurd. You can choreograph a complex action scene in Blender with basic shapes, then let Seedance make it real. You need to try this AI filmmaking workflow: 1. Generate a start frame in Midjourney 2. Block out the action in Blender 3. Feed both to Seedance My Blender reference was just rough timing, camera shake, and spatial choreography, and Seedance tracked the speed, motion, and action way better t...

## 6. 手持跟拍 + 角色绕车运动
- URL: https://x.com/reidhannaford/status/2070507963429671062
- Author: @reidhannaford
- Tier: `strong`
- Category: `handheld_follow_camera`
- Why: 说明在 Blender 中移动角色并做 handheld camera follow，Seedance 跟随运动和质感。
- Reuse: 适合做手持跟拍、角色移动穿越空间的案例。
- Text: The previs workflow is still leveling up! My AI filmmaking process is starting to feel less like wrangling AI and more like animation. Still just cubes in Blender, but now I’m moving the character through space and doing a handheld camera follow. Same basic process: 1. Generate a start frame in Midjourney 2. Block out the scene in Blender, animate the camera 3. Feed both to Seedance Seedance nailed the gritty hand...

## 7. 日本语复现条件 + 完整 prompt
- URL: https://x.com/aidoga_lab/status/2070864815275585913
- Author: @aidoga_lab
- Tier: `strong`
- Category: `replication_prompt`
- Why: 给出 start frame、Blender reference video、Seedance 2.0、5s、以及长 prompt。
- Reuse: 适合做可复现 prompt/source case。
- Text: 再現用に条件を全部置いておきます。 ・スタートフレーム：添付のキャラ画像 ・参照動画：添付のBlender動画 ・モデル：Seedance 2.0 ・尺：5s 使ったプロンプト↓ RReference video 1 defines the camera movement, timing, and the walker's path ONLY — match its trajectory, speed, framing, and the walker's position and facing exactly. The teal figure with pink arms and a purple backpack in the reference is the walker. Do NOT copy the reference's footwork or leg motion: in the reference the ...

## 8. 相机/节奏/移动控制实验与失败点
- URL: https://x.com/aidoga_lab/status/2070864749865398684
- Author: @aidoga_lab
- Tier: `medium`
- Category: `camera_motion_experiment`
- Why: 说明用 Blender 视频控制 Seedance 的 camera/rhythm/subject movement，同时指出 foot sliding 问题。
- Reuse: 适合做 limitations + troubleshooting case。
- Text: AI動画13日目。 Blender動画をSeedanceに参照させて、 カメラの動き・リズム・被写体の移動を制御するやり方にチャレンジしてみました。 結果、 カメラの動き・リズム・移動は、狙い通り制御できた。 でも"足の動き＝仕草"がうまくいかない。 Blender動画の動きをそのまま参照してしまって、自然な歩きにならない。 プロンプトでの制御も、モデル変更（mini→2.0）も試したけど、 どうしても足が滑ってしまう。 Blender動画側が正確な仕草をしてればクリアできる気はしてます。 でも理想は、Blender動画は「カメラ・リズム・移動」だけのリファレンスにして、 仕草はプロンプトに任せる形。 ここがまだ解けてません。 皆さんはどう制御してますか？

## 9. Codex + Blender MCP 生成场景/动作/参照视频
- URL: https://x.com/akiyoshisan/status/2071081230108660199
- Author: @akiyoshisan
- Tier: `strong`
- Category: `agentic_blender_mcp`
- Why: 列出 Blender MCP 连接 Codex、生成猫/市场/屋台、15 秒 motion、camera work、导出 MP4 reference 的完整流程。
- Reuse: 适合做 Agentic Blender MCP + Seedance use case。
- Text: SEIIIRUさんのを参考に、CodexからBlender MCPで試してみました。 投稿をみて、Blenderでもいけそう！と初のMCP繋いでやってみましたが中々難しいっす… ────────────── ▼ 試した内容 ・Blender MCP｜CodexからBlenderへ直接Python実行 ・簡易3Dシーン｜石畳の市場、木製の魚屋台、魚、猫を作成 ・猫モーション｜屋台に向かって歩く、止まる、魚を見る、前足を上げる ・カメラ設計｜猫・屋台・距離感が見える斜め構図で追従 ────────────── ▼ 制作フロー 1. Blender MCPをCodexに接続 2. CodexからBlenderへコード送信 3. 猫・屋台・市場を簡易モデルで生成 4. 15秒の歩きモーションを作成 5. カメラワークを調整 6. 代表フレームで破綻を確認 7. 接触・向き・構図を修正 8. MP4として参照動画を書き出し ────...

## 10. Blender blocking + 多参考图 + 角色锁定 prompt
- URL: https://x.com/AIWarper/status/2069481237308452916
- Author: @AIWarper
- Tier: `strong`
- Category: `prompt_and_reference_mapping`
- Why: 给出 Seedance prompt，把 motion/blocking reference 中的角色映射到指定角色参考图。
- Reuse: 适合做 prompt engineering + character mapping case。
- Text: The TL:DR here is if you are proficient in blocking out animation inside of Blender (or whatever) you can really nail the exact shots you want. Here I attached these 3 ref images + the source video I linked above with this Seedance prompt: "In a retro 1980s anime style, hand-drawn cel animation, set on the sunny city street from the attached environment reference image — tall buildings lined with Japanese signage ...

## 11. FBX 动画导入 Blender 后导出 Seedance reference
- URL: https://x.com/AIWarper/status/2069847776620589430
- Author: @AIWarper
- Tier: `strong`
- Category: `fbx_to_seedance_reference`
- Why: 列出 import FBX、position camera、export animation mp4，且提到 Seedance ref videos 720 max。
- Reuse: 适合做 Mixamo/FBX animation reference pipeline。
- Text: I then just did the following: 1) import the first .fbx into blender 2) position my camera 3) export the animation to .mp4 (720 max res for Seedance ref videos) I did this for each clip, changing the camera angle each time.

## 12. 无动画基础也能做 Seedance ref video
- URL: https://x.com/AIWarper/status/2070162937181065547
- Author: @AIWarper
- Tier: `medium`
- Category: `agentic_blender_mcp`
- Why: 强调不用鼠标点击 Blender、可测试 ref video trend，提示后续 details。
- Reuse: 适合作为 agent-assisted/no-code workflow 候选。
- Text: Want to test the latest Seedance ref video trend but have no clue how to animate? This entire animation was done without a single mouse click in Blender Details below 👇 https://t.co/lWreeqHIDy

## 13. Codex/OPUS + Blender MCP 一句 prompt 做 blockout
- URL: https://x.com/AIWarper/status/2070535586075885912
- Author: @AIWarper
- Tier: `medium`
- Category: `agentic_blender_mcp`
- Why: 说明整个 blockout 可通过单 prompt 约 15 分钟完成，但 Seedance 适配仍有问题。
- Reuse: 适合作为 MCP blockout 能力和问题记录。
- Text: Blender MCP w/ Codex 5.5 or OPUS 4.8 is seriously pretty cracked... This entire block out was one-shot with a single prompt in about 15 minutes. Only problem I am having now is getting Seedance to use it properly 😅 Please feel free to use it and post your results below 👇 https://t.co/IfqFw3DReO

## 14. Blender previz + Comfy + 三输入控制
- URL: https://x.com/JMSvid/status/2070258132840796579
- Author: @JMSvid
- Tier: `strong`
- Category: `comfyui_camera_control`
- Why: 说明用 Blender previz 作为 guide，并配 upright/upside-down reference frames。
- Reuse: 适合做多输入相机控制 case。
- Text: Seedance 2 has insane motion adherence. This was a test to see how far I could push camera control by using a Blender previz as the guide in Comfy. The model had three inputs: - the Blender previz - a reference frame for the upright world - a reference frame for the upside-down https://t.co/LvEE9A3bF9

## 15. Blender viewport 控制 Seedance 场景导演
- URL: https://x.com/KimAkiyama81/status/2070668362229690789
- Author: @KimAkiyama81
- Tier: `medium`
- Category: `viewport_reference`
- Why: 说明 Viewport in Blender gives control for directing scenes in Seedance。
- Reuse: 适合作为 viewport reference 简短案例。
- Text: Using Viewport in Blender gives incredible control for directing scenes in Seedance 2.0! https://t.co/TFOrkiJg6H

## 16. Viewport preview 动画角色
- URL: https://x.com/KimAkiyama81/status/2070266267051667505
- Author: @KimAkiyama81
- Tier: `medium`
- Category: `viewport_reference`
- Why: 说明用 Blender viewport preview 在 Seedance 中 animate character，并提示 process below。
- Reuse: 适合作为 viewport preview 候选。
- Text: You can use Viewport preview in Blender and animate your character in Seedance with it! Sharing process below ⬇️⬇️⬇️ https://t.co/ZC3ny3gHmU

## 17. 土耳其语 Blender + Seedance 导演控制点
- URL: https://x.com/ai_gezgini/status/2070531406237728977
- Author: @ai_gezgini
- Tier: `medium`
- Category: `prompted_camera_direction`
- Why: 列出 camera angle、character pose、motion direction、lighting、depth、lens、composition 等控制项。
- Reuse: 适合提炼为导演参数 checklist。
- Text: Seedance 2.0 ile video üretirken Blender bilenler çok şanslı… 🎬🔥 Çünkü artık olay sadece prompt yazmak değil. Blender’da önce sahneyi kabaca kendin kuruyorsun: → kamera açısı → karakter pozu → hareket yönü → ışık atmosferi → mekan derinliği → lens hissi → kadraj kompozisyonu Blender + Seedance 2.0= Prompt değil, yönetmenlik. Prompt: 👇

## 18. 土耳其语 commando scene prompt case
- URL: https://x.com/ai_gezgini/status/2071529677353615522
- Author: @ai_gezgini
- Tier: `medium`
- Category: `prompted_camera_direction`
- Why: 列出相机看向、角色进入方向、跟随角度、运动方向、景深、最终构图等。
- Reuse: 适合提炼为动作镜头 prompt/control checklist。
- Text: Blender ile komando kadın sahnesi… 🎬 Blender + Seedance 2.0 = yönetmen koltuğu sende. → kamera nereye bakacak → karakter nereden girecek → hangi açıdan takip edilecek → hareket hangi yönde akacak → sahnenin derinliği nasıl olacak → final kadrajı nerede bitecek Bugün Blender bilenler sadece 3D sahne kurmuyor; geleceğin AI video yönetmen adayları gibi çalışıyor. 🎥 Prompt: 👇

## 19. 角色 blocking + 相机 blocking 同时控制
- URL: https://x.com/SamJWasserman/status/2070742850095230991
- Author: @SamJWasserman
- Tier: `strong`
- Category: `character_and_camera_blocking`
- Why: 明确实现 camera orbit、lens choice、gunfire/cover positions/pop-outs，并说 prompt below。
- Reuse: 适合做动作场景 tactical blocking case。
- Text: Finally got this @Blender → Seedance workflow working for not just camera blocking, but character blocking simultaneously. Camera orbit, lens choice, gunfire + cover positions, pop-outs. All directed from pre-vis prior to video generation. Prompt below. Made using @dreamina_ai https://t.co/iLFCabW32W

## 20. Hermes/Krea2/ComfyUI/Blender MCP/Seedance 实验
- URL: https://x.com/SamJWasserman/status/2069656428437225826
- Author: @SamJWasserman
- Tier: `medium`
- Category: `agentic_multitool_pipeline`
- Why: 说明 agent 安装 Krea2、连接 ComfyUI 和 Blender MCP，生成 reference image + physical ref vid 后送 Seedance。
- Reuse: 适合做 multi-agent creative pipeline 候选。
- Text: Wild Experiment. Had my Hermes install @krea_ai 2 on the @NVIDIAAI Dgx Spark and connect it to @ComfyUI. Had Hermes then install @Blender and connect to it via the mcp. I had Hermes make a reference image in Krea2, + Physical ref vid in Blender. I then put all into Seedance 2.0. via @dreamina_ai.

## 21. Blender MCP viewport animation + Seedance/Magnific texture/lighting
- URL: https://x.com/techhalla/status/2070814203435274715
- Author: @techhalla
- Tier: `strong`
- Category: `blender_mcp_style_transfer`
- Why: 说明 adding 3D gives camera/element control，并声称 exactly how I did it。
- Reuse: 适合做 Blender MCP + style transfer 主案例。
- Text: Adding 3D to your animation workflow gives you full control over the camera and every element in the scene. I built this viewport animation in Blender MCP, then took it into Seedance 2.0 in Magnific to add textures and lighting. Here's exactly how I did it 👇 https://t.co/G2Q8IdfFEy

## 22. Seedance 2.0 Pro + Blender viewport style transfer
- URL: https://x.com/techhalla/status/2070832621328732396
- Author: @techhalla
- Tier: `medium`
- Category: `viewport_style_transfer`
- Why: 明确是 viewport style transfer，并指向下方流程。
- Reuse: 适合作为 style transfer 传播帖。
- Text: Seedance 2.0 pro + Blender viewport style transfer below 👇 https://t.co/bcP2Z0h5mC

## 23. Mixamo motion + Blender + Seedance 初学者路径
- URL: https://x.com/tanabe_fragm/status/2070685291183243459
- Author: @tanabe_fragm
- Tier: `medium`
- Category: `mixamo_beginner_workflow`
- Why: 测试 Blender x Seedance，并建议初学者下载 Mixamo motion 导入 Blender。
- Reuse: 适合做 beginner motion-source case。
- Text: 巷で盛り上がっているBlender × Seedance 2.0のワークフローをテスト🎥 この手法だと、確かに細かい動きのコントロールができそう。 ただ、私みたいなBlender素人だと思い通りに動かすのが難しい...😓 次は、Blender MCPを試してみようと思います。 Higgsfieldとかが簡易的なツール（Viewport Preview Referenceという名称）を公開しそうなので、そっちを待つのも手だと思います。 クリエイターさん達はこういうのが作れて本当に凄い❗️と改めて思いました😃 ちなみに、今回のモーションはMixamoというサイトから無料ダウンロードしました。 初心者の方はこういうサービスからモーションをダウンロードしてBlenderにインポートすると早いと思います。

## 24. Codex 生成 Blender 建筑和 camera work 后送 Seedance
- URL: https://x.com/6_KAKUU/status/2071051063663452374
- Author: @6_KAKUU
- Tier: `medium`
- Category: `codex_camera_work`
- Why: 说明 Blender 初学第 3 天，建筑到 camera work 都由 Codex 完成，Seedance 能跟随。
- Reuse: 适合做 Codex-assisted camera work case。
- Text: Blender × Seedance 2.0ってすごいな、本当に追従してくれるんだな。 Blenderインストールして３日目なんですが、建物からカメラワークまでCodex君が全てやってくれました。 ちなみにカメラワークの指示には、少し懐かしさを感じつつある矢印（Arrow）をCodexに対して使ってみた。 https://t.co/q33raf0W4a

## 25. Blender 3D previz → Seedance anime render
- URL: https://x.com/restofart/status/2070086939756159368
- Author: @restofart
- Tier: `medium`
- Category: `anime_previz_render`
- Why: 说明 full camera moves and motion preserved，定位 previz → AI-render pipeline。
- Reuse: 适合作为 anime/render pipeline case。
- Text: Made a 3D previz in Blender, then rendered it as anime with Seedance — all inside Doitong. Full camera moves and motion preserved. This previz → AI-render pipeline is how AI filmmaking beats "prompt and pray." Anyone else building this way? 👇 https://t.co/z0woB9BNFg

## 26. Seedance + Claude + Blender 导航式电影控制
- URL: https://x.com/Flagiuss/status/2071335816190902624
- Author: @Flagiuss
- Tier: `medium`
- Category: `claude_blender_camera_control`
- Why: 强调像 3D environment 一样导航电影以获得 camera/movement/pacing control。
- Reuse: 适合做未来式 camera control 叙事素材。
- Text: Seedance + Claude + Blender A future of AI film making is definitely in ability to navigate within films as if in 3D environments . That can give a lot of camera control, movements control, pacing and much more! Visual direction and finetuning will be mind blowing. #seedance #aivideo #aifilmmaking

## 27. Blender 初学 + agent 辅助 + Seedance reference video 测试
- URL: https://x.com/Ukiyo_il/status/2071098235268071877
- Author: @Ukiyo_il
- Tier: `medium`
- Category: `beginner_agent_reference_video`
- Why: 说明由 agent 辅助做 Blender 参考视频，并测试复杂 HIPHOP dance 进入 Seedance。
- Reuse: 适合作为 beginner/agent-assisted experiment。
- Text: #Blender チャット内で話題だったBlenderを初めて触ってみました！ 操作画面はこんな感じ・・・マジわからにゃい（笑） 普段HANAKOぐらいしか触らないから（笑） これをエージェントに頼んで色々してもらう感じ 色々試してどっかからダウンロードでCodexちゃんに頼んで出来たのが２枚目の動画・・全然改善の余地はある ちょっと難しめのHIPHOPのダンスを渡してみたら・・・全然ダメでした・・３枚目の動画参考 所感は参照動画をseedanceに渡すとそこそこ難しいダンスもしてくれるのでどうだろう？って感じでした！ ・・素人の所感です（笑）

## 28. Viewport preview 导出后进 Seedance
- URL: https://x.com/DiabloNemesis/status/2070441923706503380
- Author: @DiabloNemesis
- Tier: `strong`
- Category: `viewport_preview_to_seedance`
- Why: 明确流程：Blender block out scene、export viewport preview、抽第一帧转真实图、作为 reference 送 Seedance。
- Reuse: 适合做 viewport preview → Seedance 的短教程案例。
- Text: prompting is the old way. this is directing. – block out the scene in blender – export the viewport preview – extract the first frame → turn it into a realistic image in @morphic – drop it into as reference to video – Seedance 2.0 does the rest https://t.co/gg25Iu9VgF

## 29. FBX clay model + Claude keyframe + Seedance refs
- URL: https://x.com/Viggle_PINOC/status/2070183934265012392
- Author: @Viggle_PINOC
- Tier: `strong`
- Category: `fbx_clay_pass_reference`
- Why: 具体 step：Blender 导入 FBX 到 clay model、设置 camera、Claude keyframe camera moves、导出 mp4 给 Seedance refs。
- Reuse: 适合做 FBX/Mixamo 动画参考流程。
- Text: Step 2: Blender Import the FBX onto a clay model, then set your camera. We had Claude keyframe the camera moves, adjusted the angles, and rendered the clay pass. Export to mp4 for Seedance refs. https://t.co/kdZI8bWdi1

## 30. Seedance 角色 + ComfyUI/Claude + Blender/AE 后期
- URL: https://x.com/VengadaS65199/status/2070049247823859770
- Author: @VengadaS65199
- Tier: `medium`
- Category: `hybrid_short_film_pipeline`
- Why: 说明两晚完成创作，Seedance 做角色，ComfyUI 节点由 Claude 辅助，其余在 Blender 和 AE。
- Reuse: 适合做完整短片制作管线候选。
- Text: Pulled two all nighters making this. wrote, animated, edited, did SFX. couldn't sleep with the idea in my head. Seedance 2 for the characters. custom @ComfyUI nodes via Claude for the time-slice. rest in @Blender and AE https://t.co/Xpot8IrVJG

## 31. 不用 start frame 的 Blender blockout reference
- URL: https://x.com/magneticskiff/status/2070711034793361559
- Author: @magneticskiff
- Tier: `medium`
- Category: `no_start_frame_blockout`
- Why: 说明 Seedance + Blender blockout 可以使用 references 而非 starter frames，环境参考有足够细节时效果较好。
- Reuse: 适合做 reference-only variant 候选。
- Text: Seedance + Blender blockout using references, no start frame. I've been messing with the Blender blockout, but for a lot of my own workflow I need to be able to do it using references without starter frames. This works well so far if you're environmental reference has enough discrete details.

## 32. 同一 reference video 生成不同世界
- URL: https://x.com/koldo2k/status/2071307945002815967
- Author: @koldo2k
- Tier: `medium`
- Category: `same_reference_different_worlds`
- Why: 说明用 Blender 控制、Seedance 想象，同一 reference video 生成不同 worlds，并提到 prompt。
- Reuse: 适合做 style/world variation case。
- Text: Control with Blender, imagine with Seedance 2.0 🎬 Same reference video, different worlds. Here's the prompt I used to generate the video. The beginning is always the same only what happens in each scene changes. https://t.co/F5zFzXr6lu

## 33. Mixamo 多角色动作 + Blender storyboard + Seedance
- URL: https://x.com/dave392750/status/2070851042661810551
- Author: @dave392750
- Tier: `medium`
- Category: `mixamo_storyboard_experiment`
- Why: 日文说明 Blender storyboarding、Mixamo 多体动作、Seedance 处理跳跃/动作的实验问题。
- Reuse: 适合做 Mixamo motion complexity/troubleshooting case。
- Text: Blender絵コンテ、もう一作作ってみました。 メイドさんが走る映像ですが、はい最初から嘘が入ってますね^^; 本当はジャンプさせたかったのですが、うまくいかず、そこはSeedanceさんにお任せしました。 今回、Mixamoを動きに合わせて何体も使ったため、そこの収拾に困ることに^^; #capcut生成ai @capcutapp_jp

## 34. Codex MCP 操作 Blender 导出视频给 Seedance
- URL: https://x.com/Toshi_nyaruo_AI/status/2071149652905537541
- Author: @Toshi_nyaruo_AI
- Tier: `medium`
- Category: `codex_blender_mcp_reference`
- Why: 说明用 Codex MCP 直接操作 Blender 并导出视频，初学 2 小时完成。
- Reuse: 适合做 beginner Codex MCP workflow。
- Text: seedance 2.0 & Blender で動画作成💞 CodexのMCPを使ってBlenderを直接操作して、動画の書き出しまで行っています。 Blenderは初めて触っているのですが、起動して2時間弱でここまで来ました。 seedanceに限らず、動画生成AIは狭い空間での描写が苦手なのですが、これで解消できるような気がします。 にしても、Blender のキャラがぁぁ。もっと精進します😇

## 35. 构图 reference + personal/car reference 组合
- URL: https://x.com/Gen_x111x/status/2069803766581526534
- Author: @Gen_x111x
- Tier: `medium`
- Category: `composition_reference_multi_ref`
- Why: 日文说明用 Blender 构图 reference、个人 reference、panda car reference 组合，强调 CG camera instruction 重要。
- Reuse: 适合做 multi-reference composition case。
- Text: 今回のおふざけAIですが Blenderで構図リファレンス と 私のリファレンス と パンダカーのリファレンス をうまいこと組み合わせる作りをしてみました🙏 CGでのカメラワーク指示は非常に重要です。これがないと言うこと聞かないんです そしてseedanceはリファレンス命ですな https://t.co/MQMrxhitOT
