<div align="center">

<a href="https://evolink.ai/cookbook/blender-to-video?utm_source=github&utm_medium=banner&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/images/banner.png" alt="Bannière du dépôt de cas d’usage Blender + Seedance" width="760"></a>

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

Dépôt de cas d'usage Blender + Seedance.

**Nous réunissons des flux de travail réels avec Blender, Blender MCP, viewport, prévisualisation, FBX, Mixamo, ComfyUI et agents pour contrôler la génération vidéo Seedance.**

La collection actuelle vient des données X/Twitter fournies par le propriétaire. Chaque cas renvoie vers la source et le profil du créateur.

Commencez par le guide Blender-to-video d'EvoLink, puis utilisez le démarrage rapide ci-dessous comme référence locale du flux de travail.

## 📊 Vue d’ensemble

- **39 cas Blender + Seedance sélectionnés** à partir de publications publiques de créateurs et d’ajouts hebdomadaires audités.
- Couvre le contrôle caméra, la prévisualisation Blender, le blocking multi-personnages, la chorégraphie d'action, Blender MCP, les blockings assistés par Codex/Claude, les références FBX/Mixamo, ComfyUI, le transfert de style et les limites connues.
- Chaque cas inclut la source originale, l'attribution créateur, un résumé exploitable, le type de preuve et la date de publication.
- La liste publique est partie de l’audit de 35 candidats et inclut maintenant 14 ajouts hebdomadaires audités issus de la boucle de mise à jour récurrente.
- Utilisez ce dépôt pour examiner des flux de travail pratiques, puis diriger les utilisateurs vers le guide Blender-to-video d'EvoLink.

> [!NOTE]
> La collection privilégie les preuves concrètes: étapes, vidéos de référence, usage agent/MCP, contraintes reproductibles et limites explicites.

<a id="quick-start"></a>
## ⚡ Démarrage rapide

Configurez d'abord le contrôle local de Blender, puis installez les skills EvoLink que votre agent appellera.

### 1. Installer Blender MCP

Suivez le guide officiel Blender MCP, ouvrez Blender et vérifiez que votre agent peut se connecter au serveur Blender MCP avant de générer des références.

- Configuration officielle : [Configurer Blender MCP](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

Avant la première requête exécutable, récupérez votre clé EvoLink via [Obtenir une clé API](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key).

### 2. Installer les skills EvoLink

Installez la skill de génération Seedance et la skill d'upscale Topaz dans le workspace de l'agent.

```bash
npm i evolink-seedance
npm i evolink-topaz-video-upscale
```

### 3. [Obtenir une clé API](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key)

Créez une clé API EvoLink depuis votre compte, puis exposez-la à l’environnement d’exécution de l'agent.

```bash
export EVOLINK_API_KEY="paste_api_key_here"
```

### 4. Lancer dans votre agent

Une fois MCP, les skills et la clé API prêts, demandez à l'agent de créer un blocking Blender, d'exporter la vidéo de référence, de générer avec Seedance et d'agrandir le clip final si nécessaire.

Avant d’envoyer une requête directe, vérifiez votre clé via [Obtenir une clé API](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key). Si vous avez besoin d’un repli API direct, envoyez le workflow de référence Blender à `POST https://api.evolink.ai/v1/videos/generations` :

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

Si vous allez confier ce workflow à un agent, vérifiez d’abord la même clé via [Obtenir une clé API](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key).

```text
Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.
```

> [!NOTE]
> La page de configuration Blender MCP reste la source de vérité pour les détails d'installation côté Blender.

## 📑 Menu

| Section | Cas |
|---|---|
| [🎥 Contrôle caméra et prévisualisation](#camera-control-previs) | Case 1, 2, 3, 4, 5, 29, 37, 42 |
| [🎬 Blocking des personnages et de l’action](#character-action-blocking) | Case 6, 8, 9, 21, 32, 38, 39 |
| [🤖 Blender MCP avec agents](#agentic-blender-mcp) | Case 10, 11, 22, 34, 40 |
| [🧩 Références, prompts et correspondance des entrées multiples](#reference-prompt-multi-input-mapping) | Case 13, 14, 23, 24, 26, 27, 35, 36 |
| [🛠️ Pipelines et chaînes d’outils de production](#production-pipelines-toolchains) | Case 15, 16, 17, 18, 30 |
| [🧪 Limites, tests et dépannage](#limits-tests-troubleshooting) | Case 20, 25, 28, 31, 33, 41 |
| [🙏 Remerciements](#acknowledge) | Crédits et politique de correction |

<a id="camera-control-previs"></a>
### 🎥 Contrôle caméra et prévisualisation

| Cas | Ce que cela montre | Type |
|---|---|---|
| [Blocking Blender comme référence de mouvement pour Seedance](#case-1) | Un workflow de réalisation fusionné : appliquez toute la méthode de gray box du cas d’origine, puis poussez-la vers le rythme, la vitesse, les secousses et la chorégraphie spatiale d’une prévisualisation d’action avant la génération Seedance. | Demo |
| [Blocking caméra avec une image de départ Midjourney](#case-2) | Une recette compacte pour une caméra précise : Blender fournit le mouvement caméra, Midjourney l’image de départ et Seedance suit la référence de mouvement. | Demo |
| [Contrôle caméra dans ComfyUI avec prévisualisation Blender](#case-3) | Un cas de contrôle ComfyUI où la prévisualisation Blender est combinée à deux images de référence distinctes, l’une à l’endroit et l’autre à l’envers, afin de tester la fidélité au mouvement. | Demo |
| [De l’aperçu du viewport à une image de départ réaliste](#case-4) | Un court tutoriel d’aperçu du viewport : bloquez la scène, exportez l’aperçu, rendez la première image réaliste, puis fournissez les deux références à Seedance. | Demo |
| [Une vidéo de référence, plusieurs univers](#case-5) | Un cas de variation de style et d’univers où la même vidéo de référence Blender pilote différents mondes générés dans Seedance. | Demo |
| [Prévis caméra sur iPhone calée sur le dialogue](#case-29) | Utilisez un passage caméra Blender piloté par iPhone et calé sur le dialogue, puis envoyez cette prévis avec audio et deux images à Seedance pour préparer le plan. | Integration |
| [Test de focus et de profondeur vers Seedance](#case-37) | Testez d’abord les changements de focus et la profondeur dans Blender, puis utilisez un rendu viewport et une fiche personnage pour vérifier si Seedance garde ce langage de caméra. | Evaluation |
| [Workflow ComfyUI d’animation caméra dans Blender](#case-42) | Animez d’abord la caméra dans Blender, puis donnez cette référence de mouvement à Seedance quand le cadrage précis compte plus qu’une estimation par prompt. | Tutorial |


<a id="character-action-blocking"></a>
### 🎬 Blocking des personnages et de l’action

| Cas | Ce que cela montre | Type |
|---|---|---|
| [Dialogue à plusieurs personnages avec poses concordantes](#case-6) | Un workflow de plan dialogué où Blender sert à faire correspondre les poses des personnages et le mouvement caméra avant que Seedance ne génère la scène jouée. | Demo |
| [Caméra portée suivant un personnage dans l’espace](#case-8) | Un cas de suivi en caméra portée où Blender contrôle le déplacement du personnage dans l’espace et Seedance transpose le mouvement caméra brut dans la vidéo finale. | Demo |
| [Blocking caméra et personnages pour une action tactique](#case-9) | Un cas de blocking tactique où Blender dirige l’orbite caméra, le choix de l’objectif, les positions à couvert, les temps de tir et les déplacements des personnages avant la génération. | Demo |
| [Prévisualisation d’une embuscade au-delà d’un simple mouvement de caméra](#case-21) | Un cas d’embuscade montrant comment la prévisualisation Blender peut résoudre la mise en scène, le rythme et le mouvement caméra avant que Seedance ne génère le plan. | Demo |
| [Chasse parkour sur les toits avec obstacles](#case-32) | Construisez une prévis de parkour Blender avec interactions d’obstacles et beats d’évitement lorsque Seedance réduit sinon l’action à une simple course. | Demo |
| [Benchmark de transfert d’action à 16 caméras](#case-38) | Pour une scène d’action complexe, laissez Blender fixer les caméras et les coupes, puis mesurez ce que Seedance conserve réellement de ce plan. | Benchmark |
| [Plan orbital à huit personnages avec Video REF](#case-39) | Lorsqu’un long plan orbital doit garder plusieurs personnages cohérents, utilisez d’abord une previs légère dans Blender comme Video REF pour Seedance. | Demo |


<a id="agentic-blender-mcp"></a>
### 🤖 Blender MCP avec agents

| Cas | Ce que cela montre | Type |
|---|---|---|
| [Workflow de vidéo de référence avec Codex + Blender MCP](#case-10) | Un cas de Blender MCP piloté par agent où Codex crée un marché 3D simple, le mouvement d’un chat, le cadrage et une référence MP4 pour Seedance. | Integration |
| [Architecture et travail caméra créés par Codex](#case-11) | Un cas pour débutants assisté par Codex où l’architecture et le travail caméra sont générés dans Blender, puis testés comme référence de mouvement pour Seedance. | Integration |
| [Prévisualisation Blender MCP créée par Claude en quelques minutes](#case-22) | Un cas rapide de prévisualisation par agent où Claude utilise Blender MCP pour créer une référence de plan en deux à trois minutes. | Integration |
| [Skill Fable portée dans Codex](#case-34) | Demandez à un agent de créer la skill de vidéo de référence Blender, portez-la dans Codex et vérifiez si Seedance peut lisser le mouvement sans aucun prompt. | Integration |
| [Workflow de référence au modèle brut avec ClaudeCode](#case-40) | Laissez ClaudeCode, via Blender MCP, construire d’abord un modèle brut et un mouvement de caméra, puis réutilisez cette référence dans Seedance pour une scène plus ciblée qu’un simple prompt. | Integration |


<a id="reference-prompt-multi-input-mapping"></a>
### 🧩 Références, prompts et correspondance des entrées multiples

| Cas | Ce que cela montre | Type |
|---|---|---|
| [Prompt Seedance reproductible avec référence Blender](#case-13) | Un cas fusionné de reproductibilité et de dépannage : la configuration détaille les conditions de la vidéo de référence, tandis que le test associé indique où le contrôle caméra et rythme a fonctionné et où le mouvement des pieds a échoué. | Tutorial |
| [Mouvement Mixamo comme référence Blender pour débutants](#case-14) | Un cas de source de mouvement adapté aux débutants : utilisez un mouvement Mixamo dans Blender comme base contrôlable avant d’envoyer la référence à Seedance. | Tutorial |
| [Contrôle de référence limité aux positions pour une scène plus rapide](#case-23) | Un cas de pondération de référence : conservez la référence pour les positions tout en laissant le prompt rétablir vitesse et dynamisme. | Tutorial |
| [Jouets physiques comme référence à la place d’un logiciel 3D](#case-24) | Un cas de référence physique : utilisez des jouets comme références rapides de mouvement et de mise en scène lorsque lancer Blender représente trop de travail. | Demo |
| [Contrôle par référence pour une scène précise où le prompt a échoué](#case-26) | Une solution de repli pour le contrôle : lorsque la génération par prompt seul échoue, utilisez une référence pour imposer la scène, même si cela réduit légèrement le dynamisme. | Demo |
| [Conseils sur les proportions des personnages et les arrière-plans simples](#case-27) | Un cas sous forme de checklist de stabilité : faites correspondre les proportions du personnage au-delà de sa taille et simplifiez tout arrière-plan ne nécessitant pas d’alignement précis. | Tutorial |
| [Mocap de mannequin avec image stylisée](#case-35) | Utilisez une source de mouvement raide issue de Blender ou d’un mannequin pour fixer le timing, puis guidez le style final et le comportement du tissu dans Seedance grâce à l’image d’entrée. | Demo |
| [Espace 3D balisé pour contrôler personnage et caméra](#case-36) | Placez dans Blender des marqueurs de position et d’orientation, puis transmettez cette référence à Seedance pour garder personnage, regard et caméra ancrés dans l’espace 3D. | Integration |


<a id="production-pipelines-toolchains"></a>
### 🛠️ Pipelines et chaînes d’outils de production

| Cas | Ce que cela montre | Type |
|---|---|---|
| [Stack Hermes, Krea, ComfyUI et Blender MCP](#case-15) | Un pipeline multi-outils piloté par agent où Hermes installe et connecte Krea, ComfyUI, Blender MCP et Seedance pour produire des références visuelles et physiques. | Integration |
| [Du viewport Blender MCP au transfert de style avec Seedance](#case-16) | Un cas du viewport au transfert de style : Blender MCP contrôle la caméra et les éléments, puis Seedance et Magnific ajoutent textures et éclairage. | Integration |
| [De la prévisualisation Blender au rendu anime avec Seedance](#case-17) | Un cas de prévisualisation 3D vers anime montrant comment préserver mouvements caméra et animation pendant que Seedance modifie le style de rendu. | Integration |
| [Clay pass FBX avec caméra animée par Claude](#case-18) | Un workflow de clay pass FBX où Blender importe le mouvement, Claude aide à poser les images clés de caméra et la passe rendue devient la vidéo de référence de Seedance. | Integration |
| [Pipeline de référence de danse orchestré par Fable](#case-30) | Faites concevoir le personnage par un agent, générer le code de chorégraphie Blender, puis transmettre la référence de danse de 15 secondes à Seedance quand le mouvement guidé par prompt reste trop grossier. | Integration |


<a id="limits-tests-troubleshooting"></a>
### 🧪 Limites, tests et dépannage

| Cas | Ce que cela montre | Type |
|---|---|---|
| [Blocking Blender avec référence seule, sans image de départ](#case-20) | Une variante sans image de départ montrant qu’un blocking Blender accompagné de références détaillées de l’environnement peut fonctionner quand le workflow ne peut pas s’appuyer sur une image initiale. | Limit |
| [Renforcement du prompt avec un jouet de référence et exemple d’échec](#case-25) | Un cas de dépannage montrant pourquoi les vidéos de référence nécessitent souvent un renforcement par le prompt plutôt qu’une imitation brute. | Limit |
| [Test de résistance de physique des tissus avec Blender et Seedance](#case-28) | Un test de résistance de physique des tissus montrant où Seedance guidé par Blender fonctionne, tout en nécessitant encore des itérations pour les mouvements difficiles. | Limit |
| [Correction de timing avec des frames noires entre poses](#case-31) | Quand une référence Blender brute pousse Seedance à copier des intervalles robotiques, conservez les poses clés et noircissez les frames intermédiaires. | Tutorial |
| [Test de décalage de mouvement sur scène complexe](#case-33) | Traitez les rendus MCP de scène brute comme un test de limite : des scènes Blender complexes peuvent encore dériver du mouvement voulu même après plusieurs prises Seedance. | Limit |
| [Des blocs proxy simples battent la 3D détaillée](#case-41) | Si une géométrie Blender trop détaillée laisse trop de rendu CG dans l’image finale, ramenez personnages et accessoires à des blocs proxy simples afin que Seedance lise le layout plutôt que l’apparence. | Limit |



<a id="camera-control-previs-cases"></a>
## 🎥 Contrôle caméra et prévisualisation

<a id="case-1"></a>
### Case 1: [Blocking Blender comme référence de mouvement pour Seedance](https://x.com/noman23761/status/2071534020014563328) (by [@noman23761](https://x.com/noman23761))

**Un workflow de réalisation fusionné : appliquez toute la méthode de gray box du cas d’origine, puis poussez-la vers le rythme, la vitesse, les secousses et la chorégraphie spatiale d’une prévisualisation d’action avant la génération Seedance.**

- Notes de source: Fusionné avec l’ancien cas 7 : ensemble, ces sources montrent le workflow complet de gray box et sa variante de prévisualisation d’action avec rythme approximatif, vitesse, secousses et chorégraphie spatiale.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case1.mp4)

Type: Demo | Date: 2026-06-29

---

<a id="case-2"></a>
### Case 2: [Blocking caméra avec une image de départ Midjourney](https://x.com/reidhannaford/status/2069074506849685773) (by [@reidhannaford](https://x.com/reidhannaford))

**Une recette compacte pour une caméra précise : Blender fournit le mouvement caméra, Midjourney l’image de départ et Seedance suit la référence de mouvement.**

- Notes de source: La source présente un workflow clair en trois étapes et indique que la vidéo générée suit fidèlement le mouvement caméra de Blender.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case2.mp4)

Type: Demo | Date: 2026-06-22

---

<a id="case-3"></a>
### Case 3: [Contrôle caméra dans ComfyUI avec prévisualisation Blender](https://x.com/JMSvid/status/2070258132840796579) (by [@JMSvid](https://x.com/JMSvid))

**Un cas de contrôle ComfyUI où la prévisualisation Blender est combinée à deux images de référence distinctes, l’une à l’endroit et l’autre à l’envers, afin de tester la fidélité au mouvement.**

- Notes de source: Ce cas est utile car il combine une prévisualisation Blender et plusieurs références fixes dans une configuration de contrôle de type ComfyUI.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case3.mp4)

Type: Demo | Date: 2026-06-25

---

<a id="case-4"></a>
### Case 4: [De l’aperçu du viewport à une image de départ réaliste](https://x.com/DiabloNemesis/status/2070441923706503380) (by [@DiabloNemesis](https://x.com/DiabloNemesis))

**Un court tutoriel d’aperçu du viewport : bloquez la scène, exportez l’aperçu, rendez la première image réaliste, puis fournissez les deux références à Seedance.**

- Notes de source: La publication décrit un workflow concis avec des éléments concrets : aperçu du viewport, image de la première frame et vidéo de référence Seedance. Le média dupliqué du cas 29 a été retiré afin que le cas public n’affiche qu’une seule copie de la même vidéo.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case4.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case4.mp4)

Type: Demo | Date: 2026-06-26

---

<a id="case-5"></a>
### Case 5: [Une vidéo de référence, plusieurs univers](https://x.com/koldo2k/status/2071307945002815967) (by [@koldo2k](https://x.com/koldo2k))

**Un cas de variation de style et d’univers où la même vidéo de référence Blender pilote différents mondes générés dans Seedance.**

- Notes de source: La source est utile car elle sépare le contrôle du mouvement des variations d’univers et de style à partir de la même vidéo de référence.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 5](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case5.mp4)

Type: Demo | Date: 2026-06-28

---


<a id="case-29"></a>
### Case 29: [Prévis caméra sur iPhone calée sur le dialogue](https://x.com/CoffeeVectors/status/2076397975853551924) (by [@CoffeeVectors](https://x.com/CoffeeVectors))

**Utilisez un passage caméra Blender piloté par iPhone et calé sur le dialogue, puis envoyez cette prévis avec audio et deux images à Seedance pour préparer le plan.**

- Notes de source: La source utilise un passage caméra Blender piloté par iPhone et synchronisé sur le dialogue, puis envoie cette prévis avec audio à Seedance 2 avec deux images fixes.
- Aperçu vidéo:

[![Aperçu vidéo — Case 29](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case29.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case29.mp4)

Type: Integration | Date: 2026-07-12

---
<a id="case-37"></a>
### Case 37: [Test de focus et de profondeur vers Seedance](https://x.com/ObsceneSelene/status/2078025128672436354) (by [@ObsceneSelene](https://x.com/ObsceneSelene))

**Testez d’abord les changements de focus et la profondeur dans Blender, puis utilisez un rendu viewport et une fiche personnage pour vérifier si Seedance garde ce langage de caméra.**

- Notes de source: L’auteur vérifie si les changements de focus d’une scène Blender survivent dans Seedance et dit que le rendu viewport plus la fiche personnage ont conservé la profondeur voulue.
- Aperçu vidéo:

[![Aperçu vidéo — Case 37](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case37.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case37.mp4)

Type: Evaluation | Date: 2026-07-17

---
<a id="case-42"></a>
### Case 42: [Workflow ComfyUI d’animation caméra dans Blender](https://x.com/ComfyUI/status/2076746530258919858) (by [@ComfyUI](https://x.com/ComfyUI))

**Animez d’abord la caméra dans Blender, puis donnez cette référence de mouvement à Seedance quand le cadrage précis compte plus qu’une estimation par prompt.**

- Notes de source: Le post officiel de ComfyUI dit que les keyframes de caméra dans Blender peuvent définir mouvement, rotation et cadrage avant que Seedance ne produise la vidéo finale.
- Aperçu vidéo:

[![Aperçu vidéo — Case 42](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case42.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case42.mp4)

Type: Tutorial | Date: 2026-07-13

---
<a id="character-action-blocking-cases"></a>
## 🎬 Blocking des personnages et de l’action

<a id="case-6"></a>
### Case 6: [Dialogue à plusieurs personnages avec poses concordantes](https://x.com/reidhannaford/status/2069420552394043625) (by [@reidhannaford](https://x.com/reidhannaford))

**Un workflow de plan dialogué où Blender sert à faire correspondre les poses des personnages et le mouvement caméra avant que Seedance ne génère la scène jouée.**

- Notes de source: La source ajoute un dialogue à plusieurs personnages et la correspondance des poses, ce qui la distingue des démonstrations de contrôle caméra à un seul personnage.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 6](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case6.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case6.mp4)

Type: Demo | Date: 2026-06-23

---

<a id="case-8"></a>
### Case 8: [Caméra portée suivant un personnage dans l’espace](https://x.com/reidhannaford/status/2070507963429671062) (by [@reidhannaford](https://x.com/reidhannaford))

**Un cas de suivi en caméra portée où Blender contrôle le déplacement du personnage dans l’espace et Seedance transpose le mouvement caméra brut dans la vidéo finale.**

- Notes de source: La source déplace le personnage dans la scène tandis que la caméra le suit, ce qui la rend utile pour les plans en mouvement à caméra portée.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

Aperçu indisponible : la pièce jointe GitHub d’origine n’est plus accessible publiquement.

Type: Demo | Date: 2026-06-26

---

<a id="case-9"></a>
### Case 9: [Blocking caméra et personnages pour une action tactique](https://x.com/SamJWasserman/status/2070742850095230991) (by [@SamJWasserman](https://x.com/SamJWasserman))

**Un cas de blocking tactique où Blender dirige l’orbite caméra, le choix de l’objectif, les positions à couvert, les temps de tir et les déplacements des personnages avant la génération.**

- Notes de source: La source montre un blocking simultané de la caméra et des personnages, plus riche qu’une simple référence limitée au mouvement caméra.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 9](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case9.mp4)

Type: Demo | Date: 2026-06-27

---

<a id="case-21"></a>
### Case 21: [Prévisualisation d’une embuscade au-delà d’un simple mouvement de caméra](https://x.com/reidhannaford/status/2071595581508563168) (by [@reidhannaford](https://x.com/reidhannaford))

**Un cas d’embuscade montrant comment la prévisualisation Blender peut résoudre la mise en scène, le rythme et le mouvement caméra avant que Seedance ne génère le plan.**

- Notes de source: Demandé comme cas 21. Conservé comme exemple distinct de Reid Hannaford, car il fait évoluer le workflow d’un simple mouvement caméra vers une véritable mise en scène.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 21](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case21.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case21.mp4)

Type: Demo | Date: 2026-06-29

---


<a id="case-32"></a>
### Case 32: [Chasse parkour sur les toits avec obstacles](https://x.com/moframe2026/status/2075203485604470965) (by [@moframe2026](https://x.com/moframe2026))

**Construisez une prévis de parkour Blender avec interactions d’obstacles et beats d’évitement lorsque Seedance réduit sinon l’action à une simple course.**

- Notes de source: L’auteur utilise une prévis de parkour Blender comme référence vidéo et dit que Blender était nécessaire pour ajouter des obstacles et un flux d’évitement au-delà d’une simple course.
- Aperçu vidéo:

[![Aperçu vidéo — Case 32](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case32.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case32.mp4)

Type: Demo | Date: 2026-07-09

---
<a id="case-38"></a>
### Case 38: [Benchmark de transfert d’action à 16 caméras](https://x.com/nemopi/status/2077741477565010406) (by [@nemopi](https://x.com/nemopi))

**Pour une scène d’action complexe, laissez Blender fixer les caméras et les coupes, puis mesurez ce que Seedance conserve réellement de ce plan.**

- Notes de source: Le côté Blender est réduit à un bloc repère de taille et 16 coupes rapides ; le post indique qu’environ 73 pour cent des coupes prévues tombent à plus ou moins 0,6 seconde.
- Aperçu vidéo:

[![Aperçu vidéo — Case 38](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case38.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case38.mp4)

Type: Benchmark | Date: 2026-07-16

---
<a id="case-39"></a>
### Case 39: [Plan orbital à huit personnages avec Video REF](https://x.com/moframe2026/status/2077343109349007376) (by [@moframe2026](https://x.com/moframe2026))

**Lorsqu’un long plan orbital doit garder plusieurs personnages cohérents, utilisez d’abord une previs légère dans Blender comme Video REF pour Seedance.**

- Notes de source: L’auteur utilise une previs légère de Blender comme Video REF pour un plan orbital de 15 secondes et dit que la prise non retenue a gardé les huit personnages cohérents jusqu’au bout.
- Aperçu vidéo:

[![Aperçu vidéo — Case 39](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case39.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case39.mp4)

Type: Demo | Date: 2026-07-15

---
<a id="agentic-blender-mcp-cases"></a>
## 🤖 Blender MCP avec agents

<a id="case-10"></a>
### Case 10: [Workflow de vidéo de référence avec Codex + Blender MCP](https://x.com/akiyoshisan/status/2071081230108660199) (by [@akiyoshisan](https://x.com/akiyoshisan))

**Un cas de Blender MCP piloté par agent où Codex crée un marché 3D simple, le mouvement d’un chat, le cadrage et une référence MP4 pour Seedance.**

- Notes de source: L’auteur précise que le test a été inspiré par un autre créateur, mais que la scène, le mouvement, la caméra et le processus d’export décrits relèvent de sa propre expérience.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 10](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case10.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case10.mp4)

Type: Integration | Date: 2026-06-28

---

<a id="case-11"></a>
### Case 11: [Architecture et travail caméra créés par Codex](https://x.com/6_KAKUU/status/2071051063663452374) (by [@6_KAKUU](https://x.com/6_KAKUU))

**Un cas pour débutants assisté par Codex où l’architecture et le travail caméra sont générés dans Blender, puis testés comme référence de mouvement pour Seedance.**

- Notes de source: La publication est précieuse comme workflow Codex pour débutants : l’utilisateur délègue à Codex l’architecture et le travail caméra avant Seedance.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 11](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case11.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case11.mp4)

Type: Integration | Date: 2026-06-28

---

<a id="case-22"></a>
### Case 22: [Prévisualisation Blender MCP créée par Claude en quelques minutes](https://x.com/JoshDaws/status/2071401550845481090) (by [@JoshDaws](https://x.com/JoshDaws))

**Un cas rapide de prévisualisation par agent où Claude utilise Blender MCP pour créer une référence de plan en deux à trois minutes.**

- Notes de source: Demandé comme cas 22. Conservé parce qu’il démontre la rapidité et le contrôle par agent plutôt qu’un travail manuel dans Blender.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 22](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case22.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case22.mp4)

Type: Integration | Date: 2026-06-29

---


<a id="case-34"></a>
### Case 34: [Skill Fable portée dans Codex](https://x.com/mugi_AI_Art/status/2074259600342163846) (by [@mugi_AI_Art](https://x.com/mugi_AI_Art))

**Demandez à un agent de créer la skill de vidéo de référence Blender, portez-la dans Codex et vérifiez si Seedance peut lisser le mouvement sans aucun prompt.**

- Notes de source: L’auteur a fait créer par Fable une skill de vidéo de référence Blender, l’a portée dans Codex, puis a lancé une génération Seedance sans prompt à partir de références modélisées grossièrement.
- Aperçu vidéo:

[![Aperçu vidéo — Case 34](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case34.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case34.mp4)

Type: Integration | Date: 2026-07-06

---
<a id="case-40"></a>
### Case 40: [Workflow de référence au modèle brut avec ClaudeCode](https://x.com/Ryota110034/status/2077289164694057203) (by [@Ryota110034](https://x.com/Ryota110034))

**Laissez ClaudeCode, via Blender MCP, construire d’abord un modèle brut et un mouvement de caméra, puis réutilisez cette référence dans Seedance pour une scène plus ciblée qu’un simple prompt.**

- Notes de source: L’auteur relie ClaudeCode à Blender MCP, construit un modèle brut avec son passage caméra, puis réutilise cette référence dans Seedance pour guider la génération.
- Aperçu vidéo:

[![Aperçu vidéo — Case 40](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case40.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case40.mp4)

Type: Integration | Date: 2026-07-15

---
<a id="reference-prompt-multi-input-mapping-cases"></a>
## 🧩 Références, prompts et correspondance des entrées multiples

<a id="case-13"></a>
### Case 13: [Prompt Seedance reproductible avec référence Blender](https://x.com/aidoga_lab/status/2070864815275585913) (by [@aidoga_lab](https://x.com/aidoga_lab))

**Un cas fusionné de reproductibilité et de dépannage : la configuration détaille les conditions de la vidéo de référence, tandis que le test associé indique où le contrôle caméra et rythme a fonctionné et où le mouvement des pieds a échoué.**

- Notes de source: Fusionné avec l’ancien cas 19 : la paire conserve à la fois la configuration reproductible et la remarque sur la limite liée au glissement des pieds.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case13.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.mp4)

![Image de référence — Cas 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.jpg)

Type: Tutorial | Date: 2026-06-27

---

<a id="case-14"></a>
### Case 14: [Mouvement Mixamo comme référence Blender pour débutants](https://x.com/tanabe_fragm/status/2070685291183243459) (by [@tanabe_fragm](https://x.com/tanabe_fragm))

**Un cas de source de mouvement adapté aux débutants : utilisez un mouvement Mixamo dans Blender comme base contrôlable avant d’envoyer la référence à Seedance.**

- Notes de source: La source est utile aux débutants car elle présente Mixamo comme une source de mouvement pratique pour les vidéos de référence Blender.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 14](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case14.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case14.mp4)

Type: Tutorial | Date: 2026-06-27

---

<a id="case-23"></a>
### Case 23: [Contrôle de référence limité aux positions pour une scène plus rapide](https://x.com/kan_mi_no9/status/2071380621214224403) (by [@kan_mi_no9](https://x.com/kan_mi_no9))

**Un cas de pondération de référence : conservez la référence pour les positions tout en laissant le prompt rétablir vitesse et dynamisme.**

- Notes de source: Demandé comme cas 23. Conservé avec le test associé de kan_mi_no9 comme variante distincte du contrôle par référence.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 23](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case23.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case23.mp4)

Type: Tutorial | Date: 2026-06-28

---

<a id="case-24"></a>
### Case 24: [Jouets physiques comme référence à la place d’un logiciel 3D](https://x.com/gcduncombe/status/2070617538745229546) (by [@gcduncombe](https://x.com/gcduncombe))

**Un cas de référence physique : utilisez des jouets comme références rapides de mouvement et de mise en scène lorsque lancer Blender représente trop de travail.**

- Notes de source: Demandé comme cas 24. Conservé parce qu’il étend l’idée de vidéo de référence au-delà des prévisualisations réalisées uniquement par logiciel.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 24](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case24.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case24.mp4)

Type: Demo | Date: 2026-06-26

---

<a id="case-26"></a>
### Case 26: [Contrôle par référence pour une scène précise où le prompt a échoué](https://x.com/kan_mi_no9/status/2071168235022827587) (by [@kan_mi_no9](https://x.com/kan_mi_no9))

**Une solution de repli pour le contrôle : lorsque la génération par prompt seul échoue, utilisez une référence pour imposer la scène, même si cela réduit légèrement le dynamisme.**

- Notes de source: Demandé comme cas 26. Conservé comme pendant pratique du cas ultérieur de variation de kan_mi_no9.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 26](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case26.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case26.mp4)

Type: Demo | Date: 2026-06-28

---

<a id="case-27"></a>
### Case 27: [Conseils sur les proportions des personnages et les arrière-plans simples](https://x.com/craftcapitallab/status/2070512271391068287) (by [@craftcapitallab](https://x.com/craftcapitallab))

**Un cas sous forme de checklist de stabilité : faites correspondre les proportions du personnage au-delà de sa taille et simplifiez tout arrière-plan ne nécessitant pas d’alignement précis.**

- Notes de source: Demandé comme cas 27. Conservé parce qu’il propose des conseils de configuration précis et réutilisables.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 27](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case27.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case27.mp4)

Type: Tutorial | Date: 2026-06-26

---


<a id="case-35"></a>
### Case 35: [Mocap de mannequin avec image stylisée](https://x.com/fatboypink/status/2074087401887039740) (by [@fatboypink](https://x.com/fatboypink))

**Utilisez une source de mouvement raide issue de Blender ou d’un mannequin pour fixer le timing, puis guidez le style final et le comportement du tissu dans Seedance grâce à l’image d’entrée.**

- Notes de source: L’auteur dit qu’un mocap de mannequin raide a fourni le timing, tandis que l’image d’entrée dessinée à la main a quand même poussé Seedance vers le style et le mouvement de tissu visés.
- Aperçu vidéo:

[![Aperçu vidéo — Case 35](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case35.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case35.mp4)

Type: Demo | Date: 2026-07-06

---
<a id="case-36"></a>
### Case 36: [Espace 3D balisé pour contrôler personnage et caméra](https://x.com/ryo05m/status/2078311133245804623) (by [@ryo05m](https://x.com/ryo05m))

**Placez dans Blender des marqueurs de position et d’orientation, puis transmettez cette référence à Seedance pour garder personnage, regard et caméra ancrés dans l’espace 3D.**

- Notes de source: L’auteur construit une scène Blender avec Fable 5, place des marqueurs de position et d’orientation, puis utilise cette référence dans Seedance pour lier personnage, direction et caméra au même espace.
- Aperçu vidéo:

[![Aperçu vidéo — Case 36](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case36.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case36.mp4)

Type: Integration | Date: 2026-07-18

---
<a id="production-pipelines-toolchains-cases"></a>
## 🛠️ Pipelines et chaînes d’outils de production

<a id="case-15"></a>
### Case 15: [Stack Hermes, Krea, ComfyUI et Blender MCP](https://x.com/SamJWasserman/status/2069656428437225826) (by [@SamJWasserman](https://x.com/SamJWasserman))

**Un pipeline multi-outils piloté par agent où Hermes installe et connecte Krea, ComfyUI, Blender MCP et Seedance pour produire des références visuelles et physiques.**

- Notes de source: Ce cas illustre un stack créatif plus large construit par agent, et non une simple prévisualisation manuelle dans Blender.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 15](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case15.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case15.mp4)

Type: Integration | Date: 2026-06-24

---

<a id="case-16"></a>
### Case 16: [Du viewport Blender MCP au transfert de style avec Seedance](https://x.com/techhalla/status/2070814203435274715) (by [@techhalla](https://x.com/techhalla))

**Un cas du viewport au transfert de style : Blender MCP contrôle la caméra et les éléments, puis Seedance et Magnific ajoutent textures et éclairage.**

- Notes de source: Il s’agit de la source techhalla la plus solide, car elle explique l’animation du viewport et l’étape suivante de style et d’éclairage.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 16](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case16.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case16.mp4)

Type: Integration | Date: 2026-06-27

---

<a id="case-17"></a>
### Case 17: [De la prévisualisation Blender au rendu anime avec Seedance](https://x.com/restofart/status/2070086939756159368) (by [@restofart](https://x.com/restofart))

**Un cas de prévisualisation 3D vers anime montrant comment préserver mouvements caméra et animation pendant que Seedance modifie le style de rendu.**

- Notes de source: La source présente directement le workflow comme une prévisualisation 3D Blender transformée en rendu anime tout en conservant le mouvement caméra.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 17](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case17.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case17.mp4)

Type: Integration | Date: 2026-06-25

---

<a id="case-18"></a>
### Case 18: [Clay pass FBX avec caméra animée par Claude](https://x.com/Viggle_PINOC/status/2070183934265012392) (by [@Viggle_PINOC](https://x.com/Viggle_PINOC))

**Un workflow de clay pass FBX où Blender importe le mouvement, Claude aide à poser les images clés de caméra et la passe rendue devient la vidéo de référence de Seedance.**

- Notes de source: La source décrit un processus précis de FBX vers clay pass et comprend l’animation par images clés de la caméra avant l’export de la référence.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 18](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case18.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case18.mp4)

Type: Integration | Date: 2026-06-25

---


<a id="case-30"></a>
### Case 30: [Pipeline de référence de danse orchestré par Fable](https://x.com/ryo05m/status/2076284841457521043) (by [@ryo05m](https://x.com/ryo05m))

**Faites concevoir le personnage par un agent, générer le code de chorégraphie Blender, puis transmettre la référence de danse de 15 secondes à Seedance quand le mouvement guidé par prompt reste trop grossier.**

- Notes de source: L’auteur décrit trois étapes : Seedream 5 Pro pour le personnage, Blender pour une danse de mannequin de 15 secondes et Seedance 2.0 pour la référence de mouvement et de caméra.
- Aperçu vidéo:

[![Aperçu vidéo — Case 30](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case30.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case30.mp4)

Type: Integration | Date: 2026-07-12

---
<a id="limits-tests-troubleshooting-cases"></a>
## 🧪 Limites, tests et dépannage

<a id="case-20"></a>
### Case 20: [Blocking Blender avec référence seule, sans image de départ](https://x.com/magneticskiff/status/2070711034793361559) (by [@magneticskiff](https://x.com/magneticskiff))

**Une variante sans image de départ montrant qu’un blocking Blender accompagné de références détaillées de l’environnement peut fonctionner quand le workflow ne peut pas s’appuyer sur une image initiale.**

- Notes de source: Ce cas couvre une variante importante où des images de référence remplacent la dépendance habituelle à une image de départ.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 20](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case20.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case20.mp4)

Type: Limit | Date: 2026-06-27

---

<a id="case-25"></a>
### Case 25: [Renforcement du prompt avec un jouet de référence et exemple d’échec](https://x.com/tea_story_hoshi/status/2071002538703479089) (by [@tea_story_hoshi](https://x.com/tea_story_hoshi))

**Un cas de dépannage montrant pourquoi les vidéos de référence nécessitent souvent un renforcement par le prompt plutôt qu’une imitation brute.**

- Notes de source: Demandé comme cas 25. Conservé parce qu’il comprend à la fois des exemples réussis et une comparaison ayant échoué.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 25](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case25.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case25.mp4)

Type: Limit | Date: 2026-06-27

---

<a id="case-28"></a>
### Case 28: [Test de résistance de physique des tissus avec Blender et Seedance](https://x.com/fatboypink/status/2070577334701473800) (by [@fatboypink](https://x.com/fatboypink))

**Un test de résistance de physique des tissus montrant où Seedance guidé par Blender fonctionne, tout en nécessitant encore des itérations pour les mouvements difficiles.**

- Notes de source: Demandé comme cas 28. Conservé comme cas concret de limite et de test de résistance.
- Statut de l’audit : conservé après vérification manuelle des doublons et de l’originalité.
- Aperçu vidéo:

[![Lire la vidéo de démonstration — Cas 28](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case28.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case28.mp4)

Type: Limit | Date: 2026-06-26

---

<a id="related-repositories"></a>
## 🔗 Dépôts associés

- [Voir les prompts Seedance 2.0](https://github.com/Evolink-AI/awesome-seedance-2.0-prompts)
- [Installer le skill agent Seedance 2](https://github.com/Evolink-AI/seedance2-video-gen-skill-for-openclaw)
- [Explorer le workflow GPT Image 2 vers Seedance 2](https://github.com/Evolink-AI/GPT-Image-2-Seedance2-Workflow)


<a id="case-31"></a>
### Case 31: [Correction de timing avec des frames noires entre poses](https://x.com/thechriscooper/status/2076092824102240411) (by [@thechriscooper](https://x.com/thechriscooper))

**Quand une référence Blender brute pousse Seedance à copier des intervalles robotiques, conservez les poses clés et noircissez les frames intermédiaires.**

- Notes de source: L’auteur explique que Seedance copiait trop littéralement l’animation Blender brute, alors que le motif pose clé-noir-pose clé-noir gardait le blocking tout en lissant le mouvement.
- Aperçu vidéo:

[![Aperçu vidéo — Case 31](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case31.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case31.mp4)

Type: Tutorial | Date: 2026-07-11

---

<a id="case-33"></a>
### Case 33: [Test de décalage de mouvement sur scène complexe](https://x.com/sonicpower1970/status/2074322339391824012) (by [@sonicpower1970](https://x.com/sonicpower1970))

**Traitez les rendus MCP de scène brute comme un test de limite : des scènes Blender complexes peuvent encore dériver du mouvement voulu même après plusieurs prises Seedance.**

- Notes de source: Cette suite indique qu’après environ quatre essais, des scènes complexes ne correspondaient toujours pas au mouvement visé dans le test Claude→Blender→Seedance de l’auteur.
- Aperçu vidéo:

[![Aperçu vidéo — Case 33](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case33.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case33.mp4)

Type: Limit | Date: 2026-07-07

---
<a id="case-41"></a>
### Case 41: [Des blocs proxy simples battent la 3D détaillée](https://x.com/nemopi/status/2076877244832837890) (by [@nemopi](https://x.com/nemopi))

**Si une géométrie Blender trop détaillée laisse trop de rendu CG dans l’image finale, ramenez personnages et accessoires à des blocs proxy simples afin que Seedance lise le layout plutôt que l’apparence.**

- Notes de source: L’auteur explique que des mains et accessoires détaillés laissaient des éléments trop CG, tandis que des blocs proxy simples gardaient bien mieux le rendu 2D avec la même structure à 15 caméras.
- Aperçu vidéo:

[![Aperçu vidéo — Case 41](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case41.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case41.mp4)

Type: Limit | Date: 2026-07-14

---
<a id="acknowledge"></a>
## 🙏 Remerciements

Ce dépôt a été inspiré par des créateurs ayant partagé publiquement des flux de travail Blender + Seedance, des tests, des prompts, des vidéos de référence et des notes de production.

[@noman23761](https://x.com/noman23761), [@reidhannaford](https://x.com/reidhannaford), [@JMSvid](https://x.com/JMSvid), [@DiabloNemesis](https://x.com/DiabloNemesis), [@koldo2k](https://x.com/koldo2k), [@SamJWasserman](https://x.com/SamJWasserman), [@akiyoshisan](https://x.com/akiyoshisan), [@6_KAKUU](https://x.com/6_KAKUU), [@aidoga_lab](https://x.com/aidoga_lab), [@tanabe_fragm](https://x.com/tanabe_fragm), [@techhalla](https://x.com/techhalla), [@restofart](https://x.com/restofart), [@Viggle_PINOC](https://x.com/Viggle_PINOC), [@magneticskiff](https://x.com/magneticskiff), [@JoshDaws](https://x.com/JoshDaws), [@kan_mi_no9](https://x.com/kan_mi_no9), [@gcduncombe](https://x.com/gcduncombe), [@tea_story_hoshi](https://x.com/tea_story_hoshi), [@craftcapitallab](https://x.com/craftcapitallab), [@fatboypink](https://x.com/fatboypink)

*Nous ne pouvons pas garantir que chaque cas soit attribué à son créateur d’origine. Si une correction est nécessaire, contactez-nous et nous le mettrons à jour.*

Vous souhaitez ajouter un workflow Blender + Seedance ? [Ouvrez une issue de cas d’usage](https://github.com/Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases/issues/new?template=use-case.yml) avec le [fichier modèle d’issue](.github/ISSUE_TEMPLATE/use-case.yml), ou ouvrez une pull request avec le [modèle de PR](.github/PULL_REQUEST_TEMPLATE.md).

[![Graphique de l’historique des étoiles](https://api.star-history.com/svg?repos=Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&type=Date)](https://www.star-history.com/#Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&Date)
