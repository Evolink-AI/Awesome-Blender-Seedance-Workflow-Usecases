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

## 🍌 Einführung

Willkommen im Usecase-Repository Blender + Seedance.

**Wir sammeln reale Blender, Blender MCP, Viewport, Previs, FBX, Mixamo, ComfyUI und agentengestützte Workflows, die Ersteller zur Steuerung der Seedance-Videogenerierung verwendet haben.**

Die aktuelle Sammlung wird aus vom Benutzer bereitgestellten X/Twitter-Quelldaten zusammengestellt. Jeder Fall verlinkt auf den ursprünglichen Beitrag und das Erstellerprofil.

Beginnen Sie mit dem EvoLink Blender-zu-Video-Kochbuch und verwenden Sie dann den Schnellstart unten als Repository-lokale Workflow-Referenz.

## 📊 Übersicht

- **32 ausgewählte Blender- + Seedance-Fälle** aus öffentlichen Creator-Posts und geprüften wiederkehrenden Wochen-Updates.
- Behandelt Kamerasteuerung, Blender Previs, Multi-Character-Blocking, Action-Choreografie, Blender MCP, Codex/Claude-unterstützte Blockouts, FBX/Mixamo-Referenzen, ComfyUI/Style-Transfer und bekannte Einschränkungen.
- Jeder Fall enthält die Originalquelle, die Nennung des Urhebers, eine prägnante Zusammenfassung, die Art des Beweismittels und das Veröffentlichungsdatum.
- Die öffentliche Liste begann mit der Prüfung von 35 Kandidaten und enthält jetzt 7 auditiert hinzugefügte Wochenfälle aus dem wiederkehrenden Update-Loop.
- Verwenden Sie dieses Repo, um praktische Arbeitsabläufe zu überprüfen, und senden Sie Benutzer dann zur Einrichtung und Ausführung an das EvoLink Blender-to-Video-Kochbuch.

> [!NOTE]
> Die Sammlung bevorzugt konkrete Workflow-Beweise gegenüber Hype: quellengestützte Schritte, Referenzvideomethoden, Agenten-/MCP-Nutzung, reproduzierbare Einschränkungen und klar festgelegte Grenzen.

<a id="quick-start"></a>
## ⚡ Schnellstart

Richten Sie zuerst den lokalen Blender-Steuerungspfad ein und installieren Sie dann die EvoLink-Skills, die Ihr Agent aufrufen wird.

### 1. Blender MCP installieren

Befolgen Sie die offizielle Blender MCP-Einrichtungsanleitung, öffnen Sie Blender und stellen Sie sicher, dass Ihr Agent eine Verbindung zum Blender MCP-Server herstellen kann, bevor Sie Referenzen generieren.

- Offizielles Setup: [Blender MCP Setup](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

Holen Sie Ihren EvoLink-Schlüssel vor der ersten ausführbaren Anfrage unter [API-Schlüssel abrufen](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key).

### 2. Installieren Sie EvoLink-Skills

Installieren Sie den Seedance-Generierungsskill und den Topaz-Upscaling-Skill im Agentenarbeitsbereich.

```bash
npm i evolink-seedance
npm i evolink-topaz-video-upscale
```

### 3. [API-Schlüssel abrufen](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key)

Erstellen Sie einen EvoLink API-Schlüssel aus Ihrem Konto und stellen Sie ihn dann der Agent-Laufzeit zur Verfügung.

```bash
export EVOLINK_API_KEY="<your-evolink-api-key>"
```

### 4. Führen Sie es in Ihrem Agenten aus

Nachdem MCP, Skills und API-Schlüssel bereit sind, bitten Sie Ihren Agenten, einen Blender-Blockout zu erstellen, das Referenzvideo zu exportieren, mit Seedance zu generieren und den fertigen Clip bei Bedarf hochzuskalieren.

Bevor Sie eine direkte Anfrage senden, prüfen Sie Ihren Schlüssel unter [API-Schlüssel abrufen](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key). Wenn Sie einen direkten API-Fallback benötigen, senden Sie den Blender-Referenz-Workflow an `POST https://api.evolink.ai/v1/videos/generations`:

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

Wenn Sie den Workflow gleich an einen Agenten übergeben, prüfen Sie denselben Schlüssel zuerst unter [API-Schlüssel abrufen](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key).

```text
Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.
```

> [!NOTE]
> Die Blender MCP-Setup-Seite ist die Quelle der Wahrheit für Installationsdetails auf der Blender-Seite.

## 📑 Menü

| Abschnitt | Fälle |
|---|---|
| [🎥 Kamerasteuerung und Vorschau](#camera-control-previs) | Case 1, 2, 3, 4, 5, 29 |
| [🎬 Zeichen- und Aktionsblockierung](#character-action-blocking) | Case 6, 8, 9, 21, 32 |
| [🤖 Agent Blender MCP](#agentic-blender-mcp) | Case 10, 11, 22, 34 |
| [🧩 Referenz, Eingabeaufforderung und Zuordnung mehrerer Eingaben](#reference-prompt-multi-input-mapping) | Case 13, 14, 23, 24, 26, 27, 35 |
| [🛠️ Produktionspipelines und Toolchains](#production-pipelines-toolchains) | Case 15, 16, 17, 18, 30 |
| [🧪 Einschränkungen, Tests und Fehlerbehebung](#limits-tests-troubleshooting) | Case 20, 25, 28, 31, 33 |
| [🙏 Danksagung](#acknowledge) | Urheberangaben und Korrekturrichtlinie |

<a id="camera-control-previs"></a>
### 🎥 Kamerasteuerung & Previs

| Case | Was der Fall zeigt | Typ |
|---|---|---|
| [Blender Blockout als Seedance Bewegungsreferenz](#case-1) | Ein zusammengeführter Regie-Workflow: Verwenden Sie die vollständige Gray-Box-Methode aus dem Originalfall und übertragen Sie sie dann vor der Seedance-Generierung auf Action-Previs-Timing, Geschwindigkeit, Shake und räumliche Choreografie. | Demo |
| [Kamerablockierung mit Midjourney Startbild](#case-2) | Ein kompaktes Präzisionskamera-Rezept: Blender liefert die Kamerabewegung, Midjourney liefert das Startbild und Seedance folgt der Bewegungsreferenz. | Demo |
| [ComfyUI Kamerasteuerung mit Blender Previs](#case-3) | Ein ComfyUI-Kontrollfall, bei dem Blender-Vorviz mit separaten aufrechten und umgedrehten Referenzrahmen kombiniert wird, um die Bewegungseinhaltung zu testen. | Demo |
| [Ansichtsfenstervorschau auf realistischen Startrahmen](#case-4) | Ein kurzes Tutorial zur Ansichtsfenstervorschau: Blockieren Sie die Szene, exportieren Sie die Vorschau, machen Sie das erste Bild realistisch und stellen Sie dann beide Verweise auf Seedance bereit. | Demo |
| [Ein Referenzvideo, mehrere Welten](#case-5) | Ein Stil-/Weltvariationsfall, bei dem dasselbe Blender-Referenzvideo verschiedene generierte Welten in Seedance antreibt. | Demo |
| [Mit Dialog getaktete iPhone-Kameraprevis](#case-29) | Verwenden Sie einen per iPhone gesteuerten Blender-Kameradurchlauf, der auf den Dialog getaktet ist, und geben Sie diese audioführende Previs plus zwei Bilder an Seedance weiter, um die Einstellung zu planen. | Integration |


<a id="character-action-blocking"></a>
### 🎬 Zeichen- und Aktionsblockierung

| Case | Was der Fall zeigt | Typ |
|---|---|---|
| [Dialog mit mehreren Charakteren und passenden Posen](#case-6) | Ein Dialogaufnahme-Workflow, bei dem Blender verwendet wird, um Charakterposen und Kamerabewegungen abzugleichen, bevor Seedance die ausgeführte Szene generiert. | Demo |
| [Handkamera durch den Weltraum verfolgen](#case-8) | Ein Handheld-Verfolgungsfall, bei dem Blender steuert, wie sich eine Figur durch den Raum bewegt, und Seedance die grobe Kamerabewegung in das endgültige Video überträgt. | Demo |
| [Kamera- und Zeichenblockierung für taktische Aktionen](#case-9) | Ein taktischer Blockierungsfall, bei dem Blender Kameraorbit, Objektivwahl, Deckungspositionen, Schüsse und Charakterbewegungen vor der Generierung steuert. | Demo |
| [Hinterhalt-Szenenvorschau über eine einfache Kamerabewegung hinaus](#case-21) | Ein Fall einer Hinterhaltsszene, der zeigt, wie Blender previs Inszenierung, Timing und Kamerabewegung klären kann, bevor Seedance die Aufnahme erzeugt. | Demo |
| [Parkour-Dachjagd mit Hindernissen](#case-32) | Bauen Sie eine Blender-Parkour-Previs mit Hindernisinteraktionen und Ausweichbeats, wenn Seedance die Aktion sonst auf gerades Laufen reduziert. | Demo |


<a id="agentic-blender-mcp"></a>
### 🤖 Agent Blender MCP

| Case | Was der Fall zeigt | Typ |
|---|---|---|
| [Codex + Blender MCP Referenzvideo-Workflow](#case-10) | Ein Agenten-Blender MCP-Fall, in dem Codex einen einfachen 3D-Markt, Katzenbewegung, Kameraeinstellung und eine MP4-Referenz für Seedance aufbaut. | Integration |
| [Codex-Gebaute Architektur und Kameraarbeit](#case-11) | Ein von Codex unterstützter Einsteigerfall, bei dem Architektur und Kameraführung in Blender generiert und dann als Seedance-Referenzbewegung getestet werden. | Integration |
| [Claude-Erstellt Blender MCP Vorschau in Minuten](#case-22) | Ein schneller Agent-Previs-Fall, bei dem Claude Blender MCP verwendet, um in zwei bis drei Minuten eine Schussreferenz zu erstellen. | Integration |
| [Fable-Skill in Codex portiert](#case-34) | Lassen Sie einen Agenten die Blender-Referenzvideo-Skill bauen, portieren Sie sie nach Codex und testen Sie, ob Seedance die Bewegung ohne Prompttext glätten kann. | Integration |


<a id="reference-prompt-multi-input-mapping"></a>
### 🧩 Referenz, Eingabeaufforderung und Zuordnung mehrerer Eingaben

| Case | Was der Fall zeigt | Typ |
|---|---|---|
| [Reproduzierbare Seedance-Eingabeaufforderung mit Blender-Referenz](#case-13) | Ein kombinierter Fall von Reproduzierbarkeit und Fehlerbehebung: Der Aufbau beschreibt die Referenzvideobedingungen, während der gepaarte Test aufzeichnet, wo die Kamera-/Rhythmussteuerung funktionierte und die Fußbewegung fehlschlug. | Tutorial |
| [Mixamo Bewegung als Anfänger Blender Referenz](#case-14) | Ein anfängerfreundlicher Bewegungsquellenfall: Verwenden Sie die Mixamo-Bewegung in Blender als steuerbare Bewegungsbasis, bevor Sie die Referenz an Seedance senden. | Tutorial |
| [Nur Positions-Referenzsteuerung für eine schnellere Szene](#case-23) | Ein Referenzgewichtungsfall: Halten Sie die Referenz für Positionen nützlich, während Sie der Eingabeaufforderung ermöglichen, Geschwindigkeit und Dynamik wiederherzustellen. | Tutorial |
| [Physische Spielzeugreferenz anstelle von 3D Software](#case-24) | Ein Fall mit physischen Referenzen: Verwenden Sie Spielzeuge als schnelle Bewegungs- und Inszenierungsreferenzen, wenn das Öffnen von Blender zu viel Aufwand bedeutet. | Demo |
| [Referenzsteuerung für eine bestimmte fehlgeschlagene Eingabeaufforderungsszene](#case-26) | Ein Kontroll-Fallback-Fall: Wenn die Generierung nur einer Eingabeaufforderung fehlschlägt, verwenden Sie einen Verweis, um die Szene zu erzwingen, auch wenn die Dynamik etwas reduziert ist. | Demo |
| [Tipps zu Zeichenproportionen und einfachen Hintergründen](#case-27) | Ein Beispiel für eine Stabilitäts-Checkliste: Passen Sie die Proportionen der Zeichen über die Höhe hinaus an und vereinfachen Sie jeden Hintergrund, der keine präzise Ausrichtung erfordert. | Tutorial |
| [Mannequin-Mocap mit stilisiertem Eingabebild](#case-35) | Verwenden Sie eine steife Blender- oder Mannequin-Bewegungsquelle für das Timing und steuern Sie dann Stil und Stoffverhalten in Seedance über das Design des Eingabebilds. | Demo |


<a id="production-pipelines-toolchains"></a>
### 🛠️ Produktionspipelines und Toolchains

| Case | Was der Fall zeigt | Typ |
|---|---|---|
| [Hermes, Krea, ComfyUI und Blender MCP Stapel](#case-15) | Eine Multi-Tool-Agent-Pipeline, in der Hermes Krea, ComfyUI, Blender MCP und Seedance installiert und verbindet, um sowohl Bild- als auch physische Referenzen zu erstellen. | Integration |
| [Blender MCP Ansichtsfenster zu Seedance Stilübertragung](#case-16) | Ein Ansichtsfenster-zu-Stil-Transfergetriebe: Blender MCP bietet Kamera- und Elementsteuerung, dann Seedance/Magnific fügen Textur und Beleuchtung hinzu. | Integration |
| [Blender Vorschau zum Anime Seedance Render](#case-17) | Ein 3D-Previs-to-Anime-Fall, der zeigt, wie Kamerabewegungen und Bewegung erhalten bleiben können, während Seedance den Renderstil ändert. | Integration |
| [FBX Clay Pass mit Claude-Keyframe-Kamera](#case-18) | Ein FBX-Clay-Pass-Workflow, bei dem Blender die Bewegung importiert, Claude Keyframe-Kamerabewegungen unterstützt und der gerenderte Durchgang zum Seedance-Referenzvideo wird. | Integration |
| [Von Fable orchestrierte Tanz-Referenzpipeline](#case-30) | Lassen Sie einen Agenten die Figur entwerfen, den Blender-Choreografiecode erzeugen und die 15-Sekunden-Tanzreferenz an Seedance übergeben, wenn Prompt-only-Bewegung zu grob bleibt. | Integration |


<a id="limits-tests-troubleshooting"></a>
### 🧪 Einschränkungen, Tests und Fehlerbehebung

| Case | Was der Fall zeigt | Typ |
|---|---|---|
| [Nur Referenz Blender Blockout ohne Startrahmen](#case-20) | Eine Variante ohne Start-Frame, die zeigt, dass Blender-Blockout plus detaillierte Umgebungsreferenzen funktionieren können, wenn der Workflow nicht auf einen Starter-Frame zurückgreifen kann. | Limit |
| [Spielzeugreferenz-Eingabeaufforderungsverstärkung und NG-Beispiel](#case-25) | Ein Fall zur Fehlerbehebung, der zeigt, warum Referenzvideos oft einer sofortigen Verstärkung statt einer bloßen Nachahmung bedürfen. | Limit |
| [Stoffphysik-Stresstest mit Blender und Seedance](#case-28) | Ein Stoffphysik-Stresstest, der zeigt, wo Blender-geführtes Seedance funktionieren kann, aber für schwierige Bewegungen noch eine Iteration erfordert. | Limit |
| [Schwarze Frames zwischen Keyframes als Timing-Fix](#case-31) | Wenn eine grobe Blender-Referenz dazu führt, dass Seedance robotische Zwischenbewegungen kopiert, behalten Sie nur die Schlüsselposen und schwärzen die Frames dazwischen. | Tutorial |
| [Test auf Bewegungsabweichung in komplexen Szenen](#case-33) | Behandeln Sie MCP-Rohszenen-Render als Grenztest: Komplexe Blender-Szenen können selbst nach mehreren Seedance-Durchläufen noch von der beabsichtigten Bewegung abweichen. | Limit |



<a id="camera-control-previs-cases"></a>
## 🎥 Kamerasteuerung & Previs

<a id="case-1"></a>
### Case 1: [Blender Blockout als Seedance Bewegungsreferenz](https://x.com/noman23761/status/2071534020014563328) (von [@noman23761](https://x.com/noman23761))

**Ein Arbeitsablauf mit zusammengeführter Regie: Verwenden Sie die vollständige Gray-Box-Methode aus dem Originalfall und übertragen Sie sie dann vor der Seedance-Generierung auf Action-Previs-Timing, Geschwindigkeit, Shake und räumliche Choreografie.**

- Quellenhinweise: Zusammengeführt mit früherem Fall 7: Zusammen zeigen diese Quellen den vollständigen Gray-Box-Workflow und die Action-Previs-Variante mit grobem Timing, Geschwindigkeit, Verwackelung und räumlicher Choreografie.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case1.mp4)

Typ: Demo | Datum: 2026-06-29

---

<a id="case-2"></a>
### Case 2: [Kamerablockierung mit Midjourney Startbild](https://x.com/reidhannaford/status/2069074506849685773) (durch [@reidhannaford](https://x.com/reidhannaford))

**Ein kompaktes Präzisionskamera-Rezept: Blender liefert die Kamerabewegung, Midjourney liefert das Startbild und Seedance folgt der Bewegungsreferenz.**

- Hinweise zur Quelle: Die Quelle gibt einen klaren dreistufigen Arbeitsablauf an und berichtet, dass das generierte Video die Bewegung der Blender-Kamera genau verfolgt.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case2.mp4)

Typ: Demo | Datum: 2026-06-22

---

<a id="case-3"></a>
### Case 3: [ComfyUI Kamerasteuerung mit Blender Previs](https://x.com/JMSvid/status/2070258132840796579) (von [@JMSvid](https://x.com/JMSvid))

**Ein ComfyUI-Kontrollfall, bei dem Blender-Vorviz mit separaten aufrechten und umgedrehten Referenzrahmen kombiniert wird, um die Bewegungseinhaltung zu testen.**

- Quellenhinweise: Der Fall ist nützlich, weil er Blender Previz mit mehreren Standbildreferenzen innerhalb eines ComfyUI-artigen Steuerungsaufbaus kombiniert.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case3.mp4)

Typ: Demo | Datum: 2026-06-25

---

<a id="case-4"></a>
### Case 4: [Ansichtsfenstervorschau auf realistischen Startrahmen](https://x.com/DiabloNemesis/status/2070441923706503380) (von [@DiabloNemesis](https://x.com/DiabloNemesis))

**Ein kurzes Tutorial zur Ansichtsfenstervorschau: Blockieren Sie die Szene, exportieren Sie die Vorschau, machen Sie das erste Bild realistisch und stellen Sie dann beide Verweise auf Seedance bereit.**

- Quellenhinweise: Der Beitrag bietet einen prägnanten Arbeitsablauf mit konkreten Artefakten: Ansichtsfenstervorschau, erstes Bild und Seedance Referenzvideo. Das Duplikat des Fall-29-Mediums wurde entfernt, sodass im öffentlichen Fall nur eine Kopie desselben Videos angezeigt wird.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case4.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case4.mp4)

Typ: Demo | Datum: 2026-06-26

---

<a id="case-5"></a>
### Case 5: [Ein Referenzvideo, mehrere Welten](https://x.com/koldo2k/status/2071307945002815967) (von [@koldo2k](https://x.com/koldo2k))

**Ein Fall einer Stil-/Weltvariation, bei dem dasselbe Blender-Referenzvideo verschiedene generierte Welten in Seedance antreibt.**

- Hinweise zur Quelle: Die Quelle ist nützlich, da sie die Bewegungssteuerung von der Welt-/Stilvariation unter Verwendung desselben Referenzvideos trennt.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 5](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case5.mp4)

Typ: Demo | Datum: 2026-06-28

---


<a id="case-29"></a>
### Case 29: [Mit Dialog getaktete iPhone-Kameraprevis](https://x.com/CoffeeVectors/status/2076397975853551924) (von [@CoffeeVectors](https://x.com/CoffeeVectors))

**Verwenden Sie einen per iPhone gesteuerten Blender-Kameradurchlauf, der auf den Dialog getaktet ist, und geben Sie diese audioführende Previs plus zwei Bilder an Seedance weiter, um die Einstellung zu planen.**

- Quellenhinweise: Die Quelle verwendet eine per iPhone gesteuerte Blender-Kamera, die auf den Dialog getaktet ist, und schickt diese Previs mit Audio zusammen mit zwei Standbildern an Seedance 2.
- Videovorschau:

[![Videovorschau — Case 29](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case29.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case29.mp4)

Typ: Integration | Datum: 2026-07-12

---
<a id="character-action-blocking-cases"></a>
## 🎬 Zeichen- und Aktionsblockierung

<a id="case-6"></a>
### Case 6: [Dialog mit mehreren Charakteren und passenden Posen](https://x.com/reidhannaford/status/2069420552394043625) (von [@reidhannaford](https://x.com/reidhannaford))

**Ein Dialogaufnahme-Workflow, bei dem Blender verwendet wird, um Charakterposen und Kamerabewegungen abzugleichen, bevor Seedance die ausgeführte Szene generiert.**

- Hinweise zur Quelle: Die Quelle fügt Dialoge mit mehreren Charakteren und Posenabgleich hinzu, wodurch sie sich von Demos zur Kamerasteuerung mit nur einem Charakter unterscheidet.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 6](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case6.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case6.mp4)

Typ: Demo | Datum: 2026-06-23

---

<a id="case-8"></a>
### Case 8: [Handkamera durch den Weltraum verfolgen](https://x.com/reidhannaford/status/2070507963429671062) (von [@reidhannaford](https://x.com/reidhannaford))

**Ein Handheld-Verfolgungsfall, bei dem Blender steuert, wie sich ein Charakter durch den Raum bewegt, und Seedance die grobe Kamerabewegung in das endgültige Video überträgt.**

- Hinweise zur Quelle: Die Quelle bewegt die Figur durch die Szene, während die Kamera ihr folgt, was sie für Bewegungsaufnahmen aus der Hand nützlich macht.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

Vorschau nicht verfügbar: Der ursprüngliche GitHub-Anhang ist nicht mehr öffentlich zugänglich.

Typ: Demo | Datum: 2026-06-26

---

<a id="case-9"></a>
### Case 9: [Kamera- und Zeichenblockierung für taktische Aktionen](https://x.com/SamJWasserman/status/2070742850095230991) (von [@SamJWasserman](https://x.com/SamJWasserman))

**Ein taktischer Blockierungsfall, bei dem Blender Kameraorbit, Objektivwahl, Deckungspositionen, Schüsse und Charakterbewegungen vor der Generierung steuert.**

- Hinweise zur Quelle: Die Quelle zeigt eine gleichzeitige Kamera- und Zeichenblockierung, die stärker ist als eine einfache Nur-Kamera-Referenz.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 9](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case9.mp4)

Typ: Demo | Datum: 2026-06-27

---

<a id="case-21"></a>
### Case 21: [Hinterhalt-Szenenvorschau über eine einfache Kamerabewegung hinaus](https://x.com/reidhannaford/status/2071595581508563168) (von [@reidhannaford](https://x.com/reidhannaford))

**Ein Fall einer Hinterhaltsszene, der zeigt, wie Blender previs Inszenierung, Timing und Kamerabewegung klären kann, bevor Seedance die Aufnahme erzeugt.**

- Quellenanmerkungen: Angefordert als Fall 21. Wird als eindeutiges Reid Hannaford-Beispiel beibehalten, da es den Arbeitsablauf über eine einfache Kamerabewegung hinaus in die Szeneninszenierung verlagert.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 21](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case21.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case21.mp4)

Typ: Demo | Datum: 2026-06-29

---


<a id="case-32"></a>
### Case 32: [Parkour-Dachjagd mit Hindernissen](https://x.com/moframe2026/status/2075203485604470965) (von [@moframe2026](https://x.com/moframe2026))

**Bauen Sie eine Blender-Parkour-Previs mit Hindernisinteraktionen und Ausweichbeats, wenn Seedance die Aktion sonst auf gerades Laufen reduziert.**

- Quellenhinweise: Der Autor verwendet eine Blender-Parkour-Previs als Videoreferenz und sagt, Blender sei nötig gewesen, um Hindernisnutzung und Ausweichfluss über reines Laufen hinaus hinzuzufügen.
- Videovorschau:

[![Videovorschau — Case 32](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case32.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case32.mp4)

Typ: Demo | Datum: 2026-07-09

---
<a id="agentic-blender-mcp-cases"></a>
## 🤖 Agent Blender MCP

<a id="case-10"></a>
### Case 10: [Codex + Blender MCP Referenzvideo-Workflow](https://x.com/akiyoshisan/status/2071081230108660199) (von [@akiyoshisan](https://x.com/akiyoshisan))

**Ein Agenten-Blender MCP-Fall, in dem Codex einen einfachen 3D-Markt, Katzenbewegung, Kameraeinstellung und eine MP4-Referenz für Seedance aufbaut.**

- Quellenhinweise: Der Autor gibt an, dass der Test von einem anderen Ersteller inspiriert wurde, aber die beschriebene Szene, Bewegung, Kamera und der Exportvorgang sind ihr eigenes Experiment.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 10](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case10.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case10.mp4)

Typ: Integration | Datum: 2026-06-28

---

<a id="case-11"></a>
### Case 11: [Codex-Gebaute Architektur und Kameraführung](https://x.com/6_KAKUU/status/2071051063663452374) (von [@6_KAKUU](https://x.com/6_KAKUU))

**Ein Codex-unterstützter Einsteigerfall, bei dem Architektur und Kameraführung in Blender generiert und dann als Seedance-Referenzbewegung getestet werden.**

- Quellenhinweise: Der Beitrag ist als Anfänger wertvoll. Codex-Workflow: Der Benutzer delegiert Architektur und Kameraarbeit an Codex vor Seedance.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 11](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case11.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case11.mp4)

Typ: Integration | Datum: 2026-06-28

---

<a id="case-22"></a>
### Case 22: [Mit Claude erstellte Blender-MCP-Previs in Minuten](https://x.com/JoshDaws/status/2071401550845481090) (von [@JoshDaws](https://x.com/JoshDaws))

**Ein schneller Agent-Previs-Fall, bei dem Claude Blender MCP verwendet, um in zwei bis drei Minuten eine Schussreferenz zu erstellen.**

- Quellenhinweise: Angefordert als Fall 22. Behalten, da es sich eher um Geschwindigkeit und Agentenkontrolle als um manuelle Blender Arbeit handelt.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 22](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case22.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case22.mp4)

Typ: Integration | Datum: 2026-06-29

---


<a id="case-34"></a>
### Case 34: [Fable-Skill in Codex portiert](https://x.com/mugi_AI_Art/status/2074259600342163846) (von [@mugi_AI_Art](https://x.com/mugi_AI_Art))

**Lassen Sie einen Agenten die Blender-Referenzvideo-Skill bauen, portieren Sie sie nach Codex und testen Sie, ob Seedance die Bewegung ohne Prompttext glätten kann.**

- Quellenhinweise: Der Autor ließ Fable eine Blender-Referenzvideo-Skill bauen, portierte sie nach Codex und führte dann aus grob modellierten Referenzen eine Seedance-Generierung ohne Prompt aus.
- Videovorschau:

[![Videovorschau — Case 34](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case34.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case34.mp4)

Typ: Integration | Datum: 2026-07-06

---
<a id="reference-prompt-multi-input-mapping-cases"></a>
## 🧩 Referenz, Eingabeaufforderung und Zuordnung mehrerer Eingaben

<a id="case-13"></a>
### Case 13: [Reproduzierbare Seedance-Eingabeaufforderung mit Blender-Referenz](https://x.com/aidoga_lab/status/2070864815275585913) (von [@aidoga_lab](https://x.com/aidoga_lab))

**Ein kombinierter Fall von Reproduzierbarkeit und Fehlerbehebung: Der Aufbau beschreibt die Bedingungen des Referenzvideos, während der gepaarte Test aufzeichnet, wo die Kamera-/Rhythmussteuerung funktionierte und die Fußbewegung fehlschlug.**

- Quellenhinweise: Zusammengeführt mit früherem Fall 19: Das Paar behält sowohl den reproduzierbaren Aufbau als auch den Einschränkungshinweis zum Fußgleiten bei.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case13.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.mp4)

![Referenzbild — Case 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.jpg)

Typ: Tutorial | Datum: 2026-06-27

---

<a id="case-14"></a>
### Case 14: [Mixamo Bewegung als Anfänger Blender Referenz](https://x.com/tanabe_fragm/status/2070685291183243459) (von [@tanabe_fragm](https://x.com/tanabe_fragm))

**Ein anfängerfreundlicher Bewegungsquellenfall: Verwenden Sie die Mixamo-Bewegung in Blender als steuerbare Bewegungsbasis, bevor Sie die Referenz an Seedance senden.**

- Hinweise zur Quelle: Die Quelle ist für Anfänger nützlich, da sie Mixamo als praktische Bewegungsquelle für Blender-Referenzvideos nennt.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 14](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case14.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case14.mp4)

Typ: Tutorial | Datum: 2026-06-27

---

<a id="case-23"></a>
### Case 23: [Nur Positions-Referenzsteuerung für eine schnellere Szene](https://x.com/kan_mi_no9/status/2071380621214224403) (von [@kan_mi_no9](https://x.com/kan_mi_no9))

**Ein Fall der Referenzgewichtung: Halten Sie die Referenz für Positionen nützlich, während die Eingabeaufforderung wieder an Geschwindigkeit und Dynamik gewinnt.**

- Quellenhinweise: Angefordert als Fall 23. Behalten mit dem gepaarten kan_mi_no9-Test als eindeutige Referenz-Kontroll-Variante.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 23](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case23.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case23.mp4)

Typ: Tutorial | Datum: 2026-06-28

---

<a id="case-24"></a>
### Case 24: [Physische Spielzeugreferenz anstelle von 3D Software](https://x.com/gcduncombe/status/2070617538745229546) (von [@gcduncombe](https://x.com/gcduncombe))

**Ein Fall mit physischen Referenzen: Verwenden Sie Spielzeuge als schnelle Bewegungs- und Inszenierungsreferenzen, wenn das Öffnen von Blender zu viel Aufwand verursacht.**

- Quellenhinweise: Angefordert als Fall 24. Behalten, da es die Idee des Referenzvideos über reine Software-Previs hinaus erweitert.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 24](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case24.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case24.mp4)

Typ: Demo | Datum: 2026-06-26

---

<a id="case-26"></a>
### Case 26: [Referenzsteuerung für eine bestimmte fehlgeschlagene Eingabeaufforderungsszene](https://x.com/kan_mi_no9/status/2071168235022827587) (von [@kan_mi_no9](https://x.com/kan_mi_no9))

**Ein Kontroll-Fallback-Fall: Wenn die Nur-Prompt-Generierung fehlschlägt, verwenden Sie einen Verweis, um die Szene zu erzwingen, auch wenn die Dynamik etwas reduziert ist.**

- Quellenhinweise: Angefordert als Fall 26. Wird als praktisches Gegenstück zum späteren Fall der Variante kan_mi_no9 beibehalten.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 26](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case26.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case26.mp4)

Typ: Demo | Datum: 2026-06-28

---

<a id="case-27"></a>
### Case 27: [Tipps zu Zeichenproportionen und einfachen Hintergrund](https://x.com/craftcapitallab/status/2070512271391068287) (von [@craftcapitallab](https://x.com/craftcapitallab))

**Ein Beispiel für eine Stabilitäts-Checkliste: Passen Sie die Proportionen der Zeichen über die Höhe hinaus an und vereinfachen Sie jeden Hintergrund, der keine präzise Ausrichtung erfordert.**

- Quellenhinweise: Angefordert als Fall 27. Behalten, da es spezifische, wiederverwendbare Einrichtungshinweise bietet.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 27](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case27.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case27.mp4)

Typ: Tutorial | Datum: 2026-06-26

---


<a id="case-35"></a>
### Case 35: [Mannequin-Mocap mit stilisiertem Eingabebild](https://x.com/fatboypink/status/2074087401887039740) (von [@fatboypink](https://x.com/fatboypink))

**Verwenden Sie eine steife Blender- oder Mannequin-Bewegungsquelle für das Timing und steuern Sie dann Stil und Stoffverhalten in Seedance über das Design des Eingabebilds.**

- Quellenhinweise: Der Autor sagt, ein steifes Mannequin-Mocap habe das Bewegungstiming geliefert, während das handgezeichnete Eingabebild Seedance trotzdem zum gewünschten Stil und Stoffverhalten geführt habe.
- Videovorschau:

[![Videovorschau — Case 35](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case35.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case35.mp4)

Typ: Demo | Datum: 2026-07-06

---
<a id="production-pipelines-toolchains-cases"></a>
## 🛠️ Produktionspipelines und Toolchains

<a id="case-15"></a>
### Case 15: [Hermes, Krea, ComfyUI und Blender MCP Stack](https://x.com/SamJWasserman/status/2069656428437225826) (von [@SamJWasserman](https://x.com/SamJWasserman))

**Eine Multi-Tool-Agent-Pipeline, in der Hermes Krea, ComfyUI, Blender MCP und Seedance installiert und verbindet, um sowohl Bild- als auch physische Referenzen zu erstellen.**

- Quellenhinweise: Der Fall zeigt einen breiteren, von Agenten erstellten Kreativ-Stack, nicht nur manuelle Blender previs.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 15](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case15.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case15.mp4)

Typ: Integration | Datum: 2026-06-24

---

<a id="case-16"></a>
### Case 16: [Vom Blender-MCP-Viewport zum Seedance-Stiltransfer](https://x.com/techhalla/status/2070814203435274715) (von [@techhalla](https://x.com/techhalla))

**Ein Übertragungsfall vom Ansichtsfenster zum Stil: Blender MCP bietet Kamera- und Elementsteuerung, dann fügt Seedance/Magnific Textur und Beleuchtung hinzu.**

- Quellenhinweise: Dies ist die stärkere Techhalla-Quelle, da sie die Ansichtsfensteranimation und den nachgelagerten Stil-/Beleuchtungsschritt erklärt.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 16](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case16.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case16.mp4)

Typ: Integration | Datum: 2026-06-27

---

<a id="case-17"></a>
### Case 17: [Von Blender-Previs zum Anime-Render mit Seedance](https://x.com/restofart/status/2070086939756159368) (von [@restofart](https://x.com/restofart))

**Ein 3D-Previs-to-Anime-Fall, der zeigt, wie Kamerabewegungen und Bewegung erhalten bleiben können, während Seedance den Renderstil ändert.**

- Hinweise zur Quelle: Die Quelle umrahmt den Workflow direkt als Blender 3D, das vorab in ein Anime-Rendering umgewandelt wurde, während die Kamerabewegung beibehalten wurde.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 17](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case17.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case17.mp4)

Typ: Integration | Datum: 2026-06-25

---

<a id="case-18"></a>
### Case 18: [FBX Clay Pass mit Claude-Keyframe-Kamera](https://x.com/Viggle_PINOC/status/2070183934265012392) (von [@Viggle_PINOC](https://x.com/Viggle_PINOC))

**Ein FBX-Clay-Pass-Workflow, bei dem Blender die Bewegung importiert, Claude Keyframe-Kamerabewegungen unterstützt und der gerenderte Durchgang zum Seedance-Referenzvideo wird.**

- Quellenhinweise: Die Quelle gibt einen spezifischen FBX-to-Clay-Pass-Prozess an und beinhaltet Kamera-Keyframing vor dem Referenzexport.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 18](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case18.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case18.mp4)

Typ: Integration | Datum: 2026-06-25

---


<a id="case-30"></a>
### Case 30: [Von Fable orchestrierte Tanz-Referenzpipeline](https://x.com/ryo05m/status/2076284841457521043) (von [@ryo05m](https://x.com/ryo05m))

**Lassen Sie einen Agenten die Figur entwerfen, den Blender-Choreografiecode erzeugen und die 15-Sekunden-Tanzreferenz an Seedance übergeben, wenn Prompt-only-Bewegung zu grob bleibt.**

- Quellenhinweise: Der Autor beschreibt drei Schritte: Seedream 5 Pro für das Charakterdesign, Blender für einen 15-sekündigen Mannequin-Tanz und Seedance 2.0 für die Bewegungs- und Kamerareferenz.
- Videovorschau:

[![Videovorschau — Case 30](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case30.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case30.mp4)

Typ: Integration | Datum: 2026-07-12

---
<a id="limits-tests-troubleshooting-cases"></a>
## 🧪 Einschränkungen, Tests und Fehlerbehebung

<a id="case-20"></a>
### Case 20: [Nur Referenz Blender Blockout ohne Startrahmen](https://x.com/magneticskiff/status/2070711034793361559) (von [@magneticskiff](https://x.com/magneticskiff))

**Eine Variante ohne Start-Frame, die zeigt, dass Blender-Blockout plus detaillierte Umgebungsreferenzen funktionieren können, wenn der Workflow nicht auf einen Starter-Frame zurückgreifen kann.**

- Quellenhinweise: In diesem Fall geht es um eine wichtige Variante, bei der Referenzbilder die übliche Start-Frame-Abhängigkeit ersetzen.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 20](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case20.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case20.mp4)

Typ: Limit | Datum: 2026-06-27

---

<a id="case-25"></a>
### Case 25: [Spielzeugreferenz-Eingabeaufforderungsverstärkung und NG-Beispiel](https://x.com/tea_story_hoshi/status/2071002538703479089) (von [@tea_story_hoshi](https://x.com/tea_story_hoshi))

**Ein Fall zur Fehlerbehebung, der zeigt, warum Referenzvideos oft einer sofortigen Verstärkung statt einer bloßen Nachahmung bedürfen.**

- Quellenhinweise: Angefordert als Fall 25. Behalten, da es sowohl Arbeitsbeispiele als auch einen fehlgeschlagenen Vergleich enthält.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 25](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case25.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case25.mp4)

Typ: Limit | Datum: 2026-06-27

---

<a id="case-28"></a>
### Case 28: [Stoffphysik-Stresstest mit Blender und Seedance](https://x.com/fatboypink/status/2070577334701473800) (von [@fatboypink](https://x.com/fatboypink))

**Ein stoffphysikalischer Belastungstest, der zeigt, wo Blender-gesteuertes Seedance funktionieren kann, aber für schwierige Bewegungen noch eine Iteration erfordert.**

- Quellenangaben: Angefordert als Fall 28. Wird als konkreter Einschränkungs-/Stresstest-Fall beibehalten.
- Audit-Status: Wird nach manueller Duplikat- und Originalitätsprüfung beibehalten.
- Videovorschau:

[![Demovideo abspielen — Case 28](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case28.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case28.mp4)

Typ: Limit | Datum: 2026-06-26

---

<a id="related-repositories"></a>
## 🔗 Verwandte Repositories

- [Seedance-2.0-Prompts ansehen](https://github.com/Evolink-AI/awesome-seedance-2.0-prompts)
- [Seedance-2-Agent-Skill installieren](https://github.com/Evolink-AI/seedance2-video-gen-skill-for-openclaw)
- [Workflow von GPT Image 2 zu Seedance 2 erkunden](https://github.com/Evolink-AI/GPT-Image-2-Seedance2-Workflow)


<a id="case-31"></a>
### Case 31: [Schwarze Frames zwischen Keyframes als Timing-Fix](https://x.com/thechriscooper/status/2076092824102240411) (von [@thechriscooper](https://x.com/thechriscooper))

**Wenn eine grobe Blender-Referenz dazu führt, dass Seedance robotische Zwischenbewegungen kopiert, behalten Sie nur die Schlüsselposen und schwärzen die Frames dazwischen.**

- Quellenhinweise: Der Autor sagt, Seedance habe die grobe Blender-Animation zu wörtlich übernommen, während das Muster Keyframe-Schwarz-Keyframe-Schwarz das Blocking erhielt und die Bewegung glättete.
- Videovorschau:

[![Videovorschau — Case 31](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case31.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case31.mp4)

Typ: Tutorial | Datum: 2026-07-11

---

<a id="case-33"></a>
### Case 33: [Test auf Bewegungsabweichung in komplexen Szenen](https://x.com/sonicpower1970/status/2074322339391824012) (von [@sonicpower1970](https://x.com/sonicpower1970))

**Behandeln Sie MCP-Rohszenen-Render als Grenztest: Komplexe Blender-Szenen können selbst nach mehreren Seedance-Durchläufen noch von der beabsichtigten Bewegung abweichen.**

- Quellenhinweise: Dieser Folgebeitrag berichtet, dass selbst nach etwa vier Versuchen komplexe Szenen in der Claude→Blender→Seedance-Prüfung des Autors die beabsichtigte Bewegung nicht trafen.
- Videovorschau:

[![Videovorschau — Case 33](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case33.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case33.mp4)

Typ: Limit | Datum: 2026-07-07

---
<a id="acknowledge"></a>
## 🙏 Danksagung

Dieses Repository wurde von Erstellern inspiriert, die Blender + Seedance-Workflows, Tests, Eingabeaufforderungen, Referenzvideos und Produktionsnotizen öffentlich geteilt haben.

[@noman23761](https://x.com/noman23761), [@reidhannaford](https://x.com/reidhannaford), [@JMSvid](https://x.com/JMSvid), [@DiabloNemesis](https://x.com/DiabloNemesis), [@koldo2k](https://x.com/koldo2k), [@SamJWasserman](https://x.com/SamJWasserman), [@akiyoshisan](https://x.com/akiyoshisan), [@6_KAKUU](https://x.com/6_KAKUU), [@aidoga_lab](https://x.com/aidoga_lab), [@tanabe_fragm](https://x.com/tanabe_fragm), [@techhalla](https://x.com/techhalla), [@restofart](https://x.com/restofart), [@Viggle_PINOC](https://x.com/Viggle_PINOC), [@magneticskiff](https://x.com/magneticskiff), [@JoshDaws](https://x.com/JoshDaws), [@kan_mi_no9](https://x.com/kan_mi_no9), [@gcduncombe](https://x.com/gcduncombe), [@tea_story_hoshi](https://x.com/tea_story_hoshi), [@craftcapitallab](https://x.com/craftcapitallab), [@fatboypink](https://x.com/fatboypink)

*Wir können nicht garantieren, dass jeder Fall dem ursprünglichen Ersteller zugeordnet wird. Wenn etwas korrigiert werden muss, kontaktieren Sie uns bitte und wir werden es aktualisieren.*

Möchten Sie einen Blender + Seedance-Workflow hinzufügen? [Eröffnen Sie ein Use-Case-Issue](https://github.com/Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases/issues/new?template=use-case.yml) mithilfe der [Issue-Vorlage](.github/ISSUE_TEMPLATE/use-case.yml), oder öffnen Sie einen Pull Request mit der [PR-Vorlage](.github/PULL_REQUEST_TEMPLATE.md).

[![Sterngeschichte-Diagramm](https://api.star-history.com/svg?repos=Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&type=Date)](https://www.star-history.com/#Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&Date)
