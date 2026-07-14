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

## 🍌 Введение

Добро пожаловать в репозиторий вариантов использования Blender + Seedance.

**Мы собираем реальные Blender, Blender MCP, область просмотра, превиз, FBX, Mixamo, ComfyUI, а также рабочие процессы с помощью агентов, которые создатели использовали для управления созданием видео Seedance.**

Текущая коллекция составлена на основе исходных данных X/Twitter, предоставленных пользователями. Каждый случай связан с исходным сообщением и профилем создателя.

Начните с кулинарной книги EvoLink Blender по преобразованию видео в видео, а затем используйте приведенный ниже «Быстрый старт» в качестве справочника по рабочему процессу локального репозитория.

## 📊 Обзор

- **32 выбранных кейса Blender + Seedance** из публичных постов авторов и проверенных еженедельных дополнений.
- Охватывает управление камерой, Blender предвидение, многосимвольную блокировку, хореографию действий, Blender MCP, Codex/Claude блокауты, FBX/Mixamo ссылки, ComfyUI/перенос стилей и известные ограничения.
- В каждом случае указываются исходный источник, автор, краткий вывод, тип материала и дата публикации.
- Публичный список начался с аудита 35 кандидатов и теперь включает 7 проверенных еженедельных добавлений из повторяющегося цикла обновления.
- Используйте этот репозиторий для проверки практических рабочих процессов, а затем отправьте пользователей в кулинарную книгу EvoLink Blender для настройки и выполнения.

> [!NOTE]
> Коллекция отдает предпочтение конкретным доказательствам рабочего процесса, а не шумихе: шаги, подтвержденные источниками, методы эталонного видео, использование агента/MCP, воспроизводимые ограничения и четко установленные ограничения.

<a id="quick-start"></a>
## ⚡ Быстрый старт

Сначала настройте локальный путь управления Blender, а затем установите навыки EvoLink, которые будет вызывать ваш агент.

### 1. Установите Blender MCP

Следуйте официальному руководству по настройке Blender MCP, откройте Blender и убедитесь, что ваш агент может подключиться к серверу Blender MCP, прежде чем создавать ссылки.

- Официальная настройка: [Blender MCP настройка](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

### 2. Установите навыки EvoLink

Установите навык генерации Seedance и навык масштабирования Topaz в рабочую область агента.

```bash
npm i evolink-seedance
npm i evolink-topaz-video-upscale
```

### 3. [Получить API-ключ](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key)

Создайте ключ EvoLink API из своей учетной записи, а затем предоставьте его среде выполнения агента.

```bash
export EVOLINK_API_KEY="<your-evolink-api-key>"
```

### 4. Запустите его внутри своего агента

После того, как MCP, навыки и ключ API будут готовы, попросите своего агента создать блокаут Blender, экспортировать эталонное видео, сгенерировать с помощью Seedance и при необходимости повысить масштаб финального клипа.

Перед прямым запросом проверьте ключ через [Получить API-ключ](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key). Если нужен прямой API fallback, отправьте Blender-референсный workflow на `POST https://api.evolink.ai/v1/videos/generations`:

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

Если вы сейчас передаёте этот workflow агенту, сначала проверьте тот же ключ через [Получить API-ключ](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key).

```text
Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.
```

> [!NOTE]
> Страница настройки Blender MCP является источником подробностей установки на стороне Blender.

## 📑 Меню

| Раздел | Дела |
|---|---|
| [🎥 Управление камерой и просмотр](#camera-control-previs) | Case 1, 2, 3, 4, 5, 29 |
| [🎬 Блокировка персонажей и действий](#character-action-blocking) | Case 6, 8, 9, 21, 32 |
| [🤖 Агент Blender MCP](#agentic-blender-mcp) | Case 10, 11, 22, 34 |
| [🧩 Ссылка, подсказка и сопоставление нескольких входов](#reference-prompt-multi-input-mapping) | Case 13, 14, 23, 24, 26, 27, 35 |
| [🛠️ Производственные конвейеры и цепочки инструментов](#production-pipelines-toolchains) | Case 15, 16, 17, 18, 30 |
| [🧪 Ограничения, тесты и устранение неполадок](#limits-tests-troubleshooting) | Case 20, 25, 28, 31, 33 |
| [🙏 Благодарности](#acknowledge) | Авторы и правила исправлений |

<a id="camera-control-previs"></a>
### 🎥 Управление камерой и предварительный просмотр

| Case | Что это показывает | Тип |
|---|---|---|
| [Blender Блокаут как Seedance Ссылка на движение](#case-1) | Рабочий процесс с объединенным направлением: используйте полный метод серого ящика из исходного случая, затем вставьте его в превизуальную синхронизацию действия, скорость, тряску и пространственную хореографию перед созданием Seedance. | Demo |
| [Блокировка камеры с помощью стартового кадра Midjourney](#case-2) | Рецепт компактной точной камеры: Blender обеспечивает движение камеры, Midjourney предоставляет начальный кадр, а Seedance следует за ссылкой на движение. | Demo |
| [ComfyUI Управление камерой с помощью Blender Previs](#case-3) | Контрольный случай ComfyUI, в котором превизуализация Blender объединяется с отдельными вертикальными и перевернутыми опорными кадрами для проверки соблюдения режима движения. | Demo |
| [Предварительный просмотр видового экрана до реалистичного начального кадра](#case-4) | Краткое руководство по предварительному просмотру в окне просмотра: заблокируйте сцену, экспортируйте предварительный просмотр, сделайте первый кадр реалистичным, затем предоставьте обе ссылки на Seedance. | Demo |
| [Один справочный видеоролик, несколько миров](#case-5) | Случай изменения стиля/мира, когда одно и то же эталонное видео Blender управляет разными сгенерированными мирами в Seedance. | Demo |
| [iPhone-превиз камеры в ритме диалога](#case-29) | Используйте проход камеры Blender, управляемый с iPhone и синхронизированный с диалогом, а затем передайте этот превиз со звуком и двумя изображениями в Seedance для планирования кадра. | Integration |


<a id="character-action-blocking"></a>
### 🎬 Блокировка персонажей и действий

| Case | Что это показывает | Тип |
|---|---|---|
| [Диалог нескольких персонажей в одинаковых позах](#case-6) | Рабочий процесс создания диалогов, в котором Blender используется для сопоставления поз персонажей и движения камеры перед тем, как Seedance сгенерирует разыгрываемую сцену. | Demo |
| [Портативная следящая камера в космосе](#case-8) | Случай с портативным слежением, где Blender управляет тем, как персонаж путешествует в пространстве, а Seedance переносит жесткое движение камеры в финальное видео. | Demo |
| [Блокировка камеры и персонажей для тактических действий](#case-9) | Случай тактической блокировки, в котором Blender управляет орбитой камеры, выбором объектива, позициями укрытий, ударами выстрелов и движением персонажа перед генерацией. | Demo |
| [Предварительный просмотр сцены засады, помимо простого движения камеры](#case-21) | Случай со сценой из засады, показывающий, как превиз Blender может определять постановку, время и движение камеры до того, как Seedance сгенерирует кадр. | Demo |
| [Паркур-погоня на крыше с препятствиями](#case-32) | Соберите в Blender паркур-превиз с взаимодействием с препятствиями и уклонениями, если Seedance иначе сводит сцену к прямому бегу. | Demo |


<a id="agentic-blender-mcp"></a>
### 🤖 Агент Blender MCP

| Case | Что это показывает | Тип |
|---|---|---|
| [Codex + Blender MCP Эталонный рабочий процесс видео](#case-10) | Агентический случай Blender MCP, где Codex строит простой рынок 3D, движение кошки, кадрирование камеры и ссылку MP4 для Seedance. | Integration |
| [Codex-Архитектура и операторская работа](#case-11) | Случай для начинающих с помощью Codex, в котором архитектура и операторская работа генерируются в Blender, а затем тестируются как эталонное движение Seedance. | Integration |
| [Claude-Превиз Blender MCP создан за считанные минуты](#case-22) | Случай быстрого агентного превиза, когда Claude использует Blender MCP для создания эталона кадра за две-три минуты. | Integration |
| [Скилл Fable, перенесенный в Codex](#case-34) | Поручите агенту собрать скилл референсного видео для Blender, перенесите его в Codex и проверьте, может ли Seedance доработать движение вообще без prompt-текста. | Integration |


<a id="reference-prompt-multi-input-mapping"></a>
### 🧩 Ссылка, подсказка и сопоставление нескольких входов

| Case | Что это показывает | Тип |
|---|---|---|
| [Воспроизводимая подсказка Seedance со ссылкой на Blender](#case-13) | Объединенный случай воспроизводимости и устранения неполадок: в настройке указываются условия эталонного видео, а в парном тесте фиксируются случаи, когда управление камерой/ритмом сработало, а движение стопы не удалось. | Tutorial |
| [Mixamo Motion для начинающих Blender Справочник](#case-14) | Удобный для новичков случай с источником движения: используйте движение Mixamo в Blender в качестве управляемой базы перемещения перед отправкой ссылки на Seedance. | Tutorial |
| [Управление ссылкой только по положению для более быстрой сцены](#case-23) | Случай взвешивания ссылок: сохраняйте ссылку полезной для позиций, позволяя подсказке восстановить скорость и динамизм. | Tutorial |
| [Физическая ссылка на игрушку вместо программного обеспечения 3D](#case-24) | Случай с физической ссылкой: используйте игрушки в качестве ссылок на быстрое движение и постановку, когда открытие Blender требует слишком больших затрат. | Demo |
| [Управление ссылкой для конкретной сцены с неудачной подсказкой](#case-26) | Резервный вариант управления: если генерация только подсказок не удалась, используйте ссылку для принудительной активации сцены, даже если некоторый динамизм уменьшен. | Demo |
| [Пропорции персонажа и простые советы по фону](#case-27) | Контрольный список стабильности: соблюдайте пропорции символов за пределами высоты и упрощайте любой фон, который не требует точного выравнивания. | Tutorial |
| [Мокап манекена со стилизованным входным кадром](#case-35) | Используйте жесткий источник движения из Blender или от манекена для тайминга, а затем направляйте итоговый стиль и поведение ткани в Seedance через дизайн входного кадра. | Demo |


<a id="production-pipelines-toolchains"></a>
### 🛠️ Производственные конвейеры и цепочки инструментов

| Case | Что это показывает | Тип |
|---|---|---|
| [Hermes, Krea, ComfyUI и Blender MCP Стек](#case-15) | Многоинструментальный конвейер агентов, в котором Hermes устанавливает и подключает Krea, ComfyUI, Blender MCP и Seedance для создания изображений и физических ссылок. | Integration |
| [Blender MCP Окно просмотра для Seedance Перенос стиля](#case-16) | Вариант преобразования области просмотра в стиль: Blender MCP обеспечивает управление камерой и элементами, затем Seedance/Magnific добавляет текстуру и освещение. | Integration |
| [Blender Превиз к аниме Seedance Рендер](#case-17) | Случай 3D-превиз-в-аниме, показывающий, как движется камера и движение можно сохранить, в то время как Seedance меняет стиль рендеринга. | Integration |
| [FBX Clay Pass с камерой в ключевом кадре Claude](#case-18) | Рабочий процесс FBX с пластилиновым проходом, в котором Blender импортирует движение, Claude помогает перемещать ключевой кадр камеры, а визуализированный проход становится эталонным видео Seedance. | Integration |
| [Танцевальный референсный пайплайн от Fable](#case-30) | Когда движение по одному prompt получается слишком грубым, поручите агенту дизайн персонажа и код хореографии Blender, а затем отправьте 15-секундный танцевальный референс в Seedance. | Integration |


<a id="limits-tests-troubleshooting"></a>
### 🧪 Ограничения, тесты и устранение неполадок

| Case | Что это показывает | Тип |
|---|---|---|
| [Только для справки Blender Блокировка без начального кадра](#case-20) | Вариант без начального кадра, показывающий, что блокировка Blender плюс подробные ссылки на среду могут работать, когда рабочий процесс не может полагаться на стартовый кадр. | Limit |
| [Подкрепление подсказки со ссылкой на игрушку и пример NG](#case-25) | Пример устранения неполадок, показывающий, почему эталонные видеоролики часто нуждаются в быстром усилении, а не в грубой имитации. | Limit |
| [Стресс-тест по физике ткани с Blender и Seedance](#case-28) | Стресс-тест физики ткани, показывающий, где Seedance под управлением Blender может работать, но все равно требует итерации для сложных движений. | Limit |
| [Исправление тайминга черными кадрами между ключами](#case-31) | Если грубый Blender-референс заставляет Seedance копировать роботические промежуточные движения, оставьте ключевые позы и затемните кадры между ними. | Tutorial |
| [Тест рассинхрона движения в сложной сцене](#case-33) | Смотрите на MCP-рендер грубой сцены как на тест ограничения: сложные Blender-сцены могут уходить от задуманных движений даже после нескольких прогонов в Seedance. | Limit |



<a id="camera-control-previs-cases"></a>
## 🎥 Управление камерой и предварительный просмотр

<a id="case-1"></a>
### Case 1: [Blender Блокаут как Seedance Ссылка на движение](https://x.com/noman23761/status/2071534020014563328) (от [@noman23761](https://x.com/noman23761))

**Рабочий процесс с объединенным направлением: используйте полный метод серого ящика из исходного случая, затем вставьте его в превизуальную синхронизацию действия, скорость, тряску и пространственную хореографию перед созданием Seedance.**

- Примечания к источнику: объединено с предыдущим случаем 7: вместе эти источники показывают полный рабочий процесс серого ящика и вариант предварительного просмотра действия с приблизительным расчетом времени, скоростью, тряской и пространственной хореографией.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case1.mp4)

Тип: Demo | Дата: 2026-06-29

---

<a id="case-2"></a>
### Case 2: [Блокировка камеры с помощью начального кадра Midjourney](https://x.com/reidhannaford/status/2069074506849685773) (от [@reidhannaford](https://x.com/reidhannaford))

**Рецепт компактной прецизионной камеры: Blender обеспечивает движение камеры, Midjourney предоставляет начальный кадр, а Seedance следует за ссылкой движения.**

- Примечания к источнику: источник дает четкий трехэтапный рабочий процесс и сообщает, что сгенерированное видео отслеживает близкое перемещение камеры Blender.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case2.mp4)

Тип: Demo | Дата: 2026-06-22

---

<a id="case-3"></a>
### Case 3: [ComfyUI Управление камерой с помощью Blender Previs](https://x.com/JMSvid/status/2070258132840796579) (от [@JMSvid](https://x.com/JMSvid))

**Контрольный случай ComfyUI, где превизуализация Blender сочетается с отдельными вертикальными и перевернутыми опорными кадрами для проверки соблюдения режима движения.**

- Примечания к источнику: этот вариант полезен, поскольку он сочетает в себе превизуал Blender с несколькими ссылками на неподвижные изображения внутри настройки управления в стиле ComfyUI.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case3.mp4)

Тип: Demo | Дата: 2026-06-25

---

<a id="case-4"></a>
### Case 4: [Предварительный просмотр видового экрана до реалистичного начального кадра](https://x.com/DiabloNemesis/status/2070441923706503380) (от [@DiabloNemesis](https://x.com/DiabloNemesis))

**Краткое руководство по предварительному просмотру в окне просмотра: заблокируйте сцену, экспортируйте предварительный просмотр, сделайте первый кадр реалистичным, затем предоставьте обе ссылки на Seedance.**

- Примечания к источнику: в посте представлен краткий рабочий процесс с конкретными артефактами: предварительный просмотр области просмотра, изображение первого кадра и эталонное видео Seedance. Дубликат дела 29 был удален, поэтому в общедоступном деле показана только одна копия того же видео.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case4.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case4.mp4)

Тип: Demo | Дата: 2026-06-26

---

<a id="case-5"></a>
### Case 5: [Один эталонный видеоролик, несколько миров](https://x.com/koldo2k/status/2071307945002815967) (от [@koldo2k](https://x.com/koldo2k))

**Случай изменения стиля/мира, когда одно и то же эталонное видео Blender управляет разными сгенерированными мирами в Seedance.**

- Примечания к источнику: источник полезен, поскольку он отделяет управление движением от вариаций мира/стиля с использованием одного и того же эталонного видео.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 5](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case5.mp4)

Тип: Demo | Дата: 2026-06-28

---


<a id="case-29"></a>
### Case 29: [iPhone-превиз камеры в ритме диалога](https://x.com/CoffeeVectors/status/2076397975853551924) (от [@CoffeeVectors](https://x.com/CoffeeVectors))

**Используйте проход камеры Blender, управляемый с iPhone и синхронизированный с диалогом, а затем передайте этот превиз со звуком и двумя изображениями в Seedance для планирования кадра.**

- Примечания к источнику: Источник использует управляемую с iPhone Blender-камеру, синхронизированную с диалогом, и отправляет этот превиз со звуком вместе с двумя статичными изображениями в Seedance 2.
- Предварительный просмотр видео:

[![Предварительный просмотр видео — Case 29](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case29.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case29.mp4)

Тип: Integration | Дата: 2026-07-12

---
<a id="character-action-blocking-cases"></a>
## 🎬 Блокировка персонажей и действий

<a id="case-6"></a>
### Case 6: [Диалог нескольких персонажей в одинаковых позах](https://x.com/reidhannaford/status/2069420552394043625) (от [@reidhannaford](https://x.com/reidhannaford))

**Рабочий процесс создания диалогов, в котором Blender используется для сопоставления поз персонажей и движения камеры перед тем, как Seedance сгенерирует разыгрываемую сцену.**

- Примечания к источнику: источник добавляет многосимвольные диалоги и сопоставление поз, что отличает его от односимвольных демонстраций с управлением камерой.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 6](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case6.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case6.mp4)

Тип: Demo | Дата: 2026-06-23

---

<a id="case-8"></a>
### Case 8: [Портативная следящая камера в космосе](https://x.com/reidhannaford/status/2070507963429671062) (от [@reidhannaford](https://x.com/reidhannaford))

**Случай слежения с рук, когда Blender управляет перемещением персонажа в пространстве, а Seedance переносит жесткое движение камеры в финальное видео.**

- Примечания к источнику: источник перемещает персонажа по сцене, а камера следует за ним, что делает его полезным для съемки движения с рук.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

Предварительный просмотр недоступен: исходное вложение GitHub больше не является общедоступным.

Тип: Demo | Дата: 2026-06-26

---

<a id="case-9"></a>
### Case 9: [Блокировка камеры и персонажей для тактических действий](https://x.com/SamJWasserman/status/2070742850095230991) (автор [@SamJWasserman](https://x.com/SamJWasserman))

**Случай тактической блокировки, когда Blender управляет орбитой камеры, выбором объектива, позициями укрытий, ритмами стрельбы и движением персонажа перед генерацией.**

- Примечания к источнику: источник показывает одновременную блокировку камеры и персонажей, что более эффективно, чем простая ссылка только на камеру.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 9](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case9.mp4)

Тип: Demo | Дата: 2026-06-27

---

<a id="case-21"></a>
### Case 21: [Предварительный просмотр сцены засады, помимо простого движения камеры](https://x.com/reidhannaford/status/2071595581508563168) (от [@reidhannaford](https://x.com/reidhannaford))

**Случай со сценой засады, показывающий, как превиз Blender может определять постановку, синхронизацию и движение камеры до того, как Seedance сгенерирует кадр.**

- Примечания к источнику: Запрошено как случай 21. Сохранено как отдельный пример Рида Ханнафорда, поскольку он выводит рабочий процесс за рамки простого перемещения камеры к постановке сцены.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 21](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case21.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case21.mp4)

Тип: Demo | Дата: 2026-06-29

---


<a id="case-32"></a>
### Case 32: [Паркур-погоня на крыше с препятствиями](https://x.com/moframe2026/status/2075203485604470965) (от [@moframe2026](https://x.com/moframe2026))

**Соберите в Blender паркур-превиз с взаимодействием с препятствиями и уклонениями, если Seedance иначе сводит сцену к прямому бегу.**

- Примечания к источнику: Автор использует Blender-паркур-превиз как видеореференс и пишет, что Blender понадобился, чтобы добавить препятствия и уклонения сверх обычного бега.
- Предварительный просмотр видео:

[![Предварительный просмотр видео — Case 32](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case32.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case32.mp4)

Тип: Demo | Дата: 2026-07-09

---
<a id="agentic-blender-mcp-cases"></a>
## 🤖 Агент Blender MCP

<a id="case-10"></a>
### Case 10: [Codex + Blender MCP Эталонный рабочий процесс видео](https://x.com/akiyoshisan/status/2071081230108660199) (от [@akiyoshisan](https://x.com/akiyoshisan))

**Агентный случай Blender MCP, когда Codex строит простой рынок 3D, движение кошки, кадрирование камеры и ссылку MP4 для Seedance.**

- Примечания к источнику: автор говорит, что тест был вдохновлен другим создателем, но описанная сцена, движение, камера и процесс экспорта являются их собственным экспериментом.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 10](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case10.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case10.mp4)

Тип: Integration | Дата: 2026-06-28

---

<a id="case-11"></a>
### Case 11: [Codex-Встроенная архитектура и операторская работа](https://x.com/6_KAKUU/status/2071051063663452374) (автор [@6_KAKUU](https://x.com/6_KAKUU))

**Случай для начинающих с помощью Codex, в котором архитектура и работа камеры генерируются в Blender, а затем тестируются как эталонное движение Seedance.**

- Примечания к источнику: этот пост ценен для начинающего рабочего процесса Codex: пользователь делегирует работу по архитектуре и камере Codex до Seedance.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 11](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case11.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case11.mp4)

Тип: Integration | Дата: 2026-06-28

---

<a id="case-22"></a>
### Case 22: [Claude-Построенный Blender MCP превиз за считанные минуты](https://x.com/JoshDaws/status/2071401550845481090) (автор [@JoshDaws](https://x.com/JoshDaws))

**Случай быстрого агентного превиза, когда Claude использует Blender MCP для создания эталона кадра за две-три минуты.**

- Примечания к источнику: Запрошен как случай 22. Сохранен, поскольку он демонстрирует скорость и контроль агентов, а не ручную работу Blender.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 22](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case22.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case22.mp4)

Тип: Integration | Дата: 2026-06-29

---


<a id="case-34"></a>
### Case 34: [Скилл Fable, перенесенный в Codex](https://x.com/mugi_AI_Art/status/2074259600342163846) (от [@mugi_AI_Art](https://x.com/mugi_AI_Art))

**Поручите агенту собрать скилл референсного видео для Blender, перенесите его в Codex и проверьте, может ли Seedance доработать движение вообще без prompt-текста.**

- Примечания к источнику: Автор поручил Fable собрать скилл референсного видео для Blender, перенес его в Codex, а затем сделал генерацию Seedance без prompt-текста из грубо смоделированных референсов.
- Предварительный просмотр видео:

[![Предварительный просмотр видео — Case 34](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case34.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case34.mp4)

Тип: Integration | Дата: 2026-07-06

---
<a id="reference-prompt-multi-input-mapping-cases"></a>
## 🧩 Ссылка, подсказка и сопоставление нескольких входов

<a id="case-13"></a>
### Case 13: [Воспроизводимая подсказка Seedance со ссылкой на Blender](https://x.com/aidoga_lab/status/2070864815275585913) (от [@aidoga_lab](https://x.com/aidoga_lab))

**Объединенный случай воспроизводимости и устранения неполадок: в настройке указываются условия эталонного видео, а в парном тесте фиксируются случаи, когда управление камерой/ритмом сработало, а движение стопы не удалось.**

- Примечания к источнику: объединено с предыдущим случаем 19: пара сохраняет как воспроизводимую настройку, так и примечание об ограничении скольжения стопы.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case13.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.mp4)

![Референсное изображение — Case 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.jpg)

Тип: Tutorial | Дата: 2026-06-27

---

<a id="case-14"></a>
### Case 14: [Движение Mixamo как простой референс для Blender](https://x.com/tanabe_fragm/status/2070685291183243459) (от [@tanabe_fragm](https://x.com/tanabe_fragm))

**Удобный для новичков случай с источником движения: используйте движение Mixamo в Blender в качестве управляемой базы перемещения перед отправкой ссылки на Seedance.**

- Примечания к источнику: источник полезен для новичков, поскольку он называет Mixamo практическим источником движения для справочных видеороликов Blender.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 14](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case14.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case14.mp4)

Тип: Tutorial | Дата: 2026-06-27

---

<a id="case-23"></a>
### Case 23: [Управление ссылкой только по положению для более быстрой сцены](https://x.com/kan_mi_no9/status/2071380621214224403) (от [@kan_mi_no9](https://x.com/kan_mi_no9))

**Случай с использованием эталонного взвешивания: сохраняйте привязку полезной для позиций, позволяя подсказке восстановить скорость и динамизм.**

- Примечания к источнику: Запрошен как случай 23. Сохраняется с парным тестом kan_mi_no9 как отдельный вариант эталонного контроля.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 23](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case23.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case23.mp4)

Тип: Tutorial | Дата: 2026-06-28

---

<a id="case-24"></a>
### Case 24: [Физическая ссылка на игрушку вместо программного обеспечения 3D](https://x.com/gcduncombe/status/2070617538745229546) (от [@gcduncombe](https://x.com/gcduncombe))

**Пример физической ссылки: используйте игрушки в качестве ссылок на быстрое движение и постановку, когда открытие Blender требует слишком больших затрат.**

- Примечания к источнику: Запрошено как случай 24. Сохранено, поскольку оно расширяет идею эталонного видео за пределы предварительного просмотра только программного обеспечения.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 24](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case24.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case24.mp4)

Тип: Demo | Дата: 2026-06-26

---

<a id="case-26"></a>
### Case 26: [Управление ссылкой для конкретной неудачной сцены подсказки](https://x.com/kan_mi_no9/status/2071168235022827587) (от [@kan_mi_no9](https://x.com/kan_mi_no9))

**Запасной вариант управления: если генерация только подсказок не удалась, используйте ссылку для форсирования сцены, даже если некоторый динамизм снижен.**

- Примечания к источнику: Запрошено как случай 26. Сохранено как практический аналог более позднего варианта варианта kan_mi_no9.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 26](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case26.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case26.mp4)

Тип: Demo | Дата: 2026-06-28

---

<a id="case-27"></a>
### Case 27: [Пропорции символов и простые советы по фону](https://x.com/craftcapitallab/status/2070512271391068287) (от [@craftcapitallab](https://x.com/craftcapitallab))

**Кейс из контрольного списка стабильности: соблюдайте пропорции символов за пределами высоты и упрощайте любой фон, не требующий точного выравнивания.**

- Примечания к источнику: запрошено как случай 27. Сохранено, поскольку оно предлагает конкретные, многократно используемые советы по настройке.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 27](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case27.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case27.mp4)

Тип: Tutorial | Дата: 2026-06-26

---


<a id="case-35"></a>
### Case 35: [Мокап манекена со стилизованным входным кадром](https://x.com/fatboypink/status/2074087401887039740) (от [@fatboypink](https://x.com/fatboypink))

**Используйте жесткий источник движения из Blender или от манекена для тайминга, а затем направляйте итоговый стиль и поведение ткани в Seedance через дизайн входного кадра.**

- Примечания к источнику: Автор говорит, что жесткий мокап манекена задавал тайминг движения, а нарисованный вручную входной кадр все равно дотянул итог до нужного стиля и поведения ткани.
- Предварительный просмотр видео:

[![Предварительный просмотр видео — Case 35](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case35.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case35.mp4)

Тип: Demo | Дата: 2026-07-06

---
<a id="production-pipelines-toolchains-cases"></a>
## 🛠️ Производственные конвейеры и цепочки инструментов

<a id="case-15"></a>
### Case 15: [Hermes, Krea, ComfyUI и Blender MCP стек](https://x.com/SamJWasserman/status/2069656428437225826) (от [@SamJWasserman](https://x.com/SamJWasserman))

**Мультиинструментальный конвейер агентов, в котором Hermes устанавливает и подключает Krea, ComfyUI, Blender MCP и Seedance для создания изображений и физических ссылок.**

- Примечания к источнику: этот случай демонстрирует более широкий набор креативов, созданных агентом, а не только ручной предварительный просмотр Blender.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 15](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case15.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case15.mp4)

Тип: Integration | Дата: 2026-06-24

---

<a id="case-16"></a>
### Case 16: [Blender MCP Окно просмотра для Seedance Передача стиля](https://x.com/techhalla/status/2070814203435274715) (от [@techhalla](https://x.com/techhalla))

**Перенос области просмотра в стиль: Blender MCP обеспечивает управление камерой и элементами, затем Seedance/Magnific добавляет текстуру и освещение.**

- Примечания к источнику: это более сильный источник techhalla, поскольку он объясняет анимацию области просмотра и последующие этапы стиля/освещения.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 16](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case16.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case16.mp4)

Тип: Integration | Дата: 2026-06-27

---

<a id="case-17"></a>
### Case 17: [Blender Превиз для аниме Seedance рендер](https://x.com/restofart/status/2070086939756159368) (от [@restofart](https://x.com/restofart))

**Кейс 3D-превиз-в-аниме, показывающий, как можно сохранить движение камеры и движение, в то время как Seedance меняет стиль рендеринга.**

- Примечания к источнику: источник непосредственно представляет рабочий процесс в виде превизуализации Blender 3D, преобразованной в рендер аниме, сохраняя при этом движение камеры.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 17](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case17.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case17.mp4)

Тип: Integration | Дата: 2026-06-25

---

<a id="case-18"></a>
### Case 18: [FBX Глиняный проход с Claude-камерой в ключевом кадре](https://x.com/Viggle_PINOC/status/2070183934265012392) (от [@Viggle_PINOC](https://x.com/Viggle_PINOC))

**Рабочий процесс FBX с пластилиновым проходом, в котором Blender импортирует движение, Claude помогает перемещать ключевой кадр камеры, а визуализированный проход становится Seedance эталонным видео.**

- Примечания к источнику: источник описывает конкретный процесс перехода от FBX к глине и включает ключевые кадры камеры перед экспортом ссылок.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 18](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case18.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case18.mp4)

Тип: Integration | Дата: 2026-06-25

---


<a id="case-30"></a>
### Case 30: [Танцевальный референсный пайплайн от Fable](https://x.com/ryo05m/status/2076284841457521043) (от [@ryo05m](https://x.com/ryo05m))

**Когда движение по одному prompt получается слишком грубым, поручите агенту дизайн персонажа и код хореографии Blender, а затем отправьте 15-секундный танцевальный референс в Seedance.**

- Примечания к источнику: Автор явно описывает три шага: Seedream 5 Pro для персонажа, Blender для 15-секундного танца манекена и Seedance 2.0 для референса движения и камеры.
- Предварительный просмотр видео:

[![Предварительный просмотр видео — Case 30](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case30.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case30.mp4)

Тип: Integration | Дата: 2026-07-12

---
<a id="limits-tests-troubleshooting-cases"></a>
## 🧪 Ограничения, тесты и устранение неполадок

<a id="case-20"></a>
### Case 20: [Блокировка Blender только для справки без начального кадра](https://x.com/magneticskiff/status/2070711034793361559) (от [@magneticskiff](https://x.com/magneticskiff))

**Вариант без начального кадра, показывающий, что блокировка Blender плюс подробные ссылки на среду могут работать, когда рабочий процесс не может полагаться на стартовый кадр.**

- Примечания к источнику: этот случай охватывает важный вариант, в котором эталонные изображения заменяют обычную зависимость от начального кадра.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 20](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case20.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case20.mp4)

Тип: Limit | Дата: 2026-06-27

---

<a id="case-25"></a>
### Case 25: [Подкрепление подсказки об игрушке и пример NG](https://x.com/tea_story_hoshi/status/2071002538703479089) (от [@tea_story_hoshi](https://x.com/tea_story_hoshi))

**Пример устранения неполадок, показывающий, почему эталонные видеоролики часто нуждаются в немедленном усилении, а не в грубой имитации.**

- Примечания к источнику: Запрошен как случай 25. Сохранен, поскольку включает как рабочие примеры, так и неудачное сравнение.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 25](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case25.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case25.mp4)

Тип: Limit | Дата: 2026-06-27

---

<a id="case-28"></a>
### Case 28: [Стресс-тест физики ткани с Blender и Seedance](https://x.com/fatboypink/status/2070577334701473800) (от [@fatboypink](https://x.com/fatboypink))

**Стресс-тест физики ткани, показывающий, где Seedance под руководством Blender может работать, но все равно требует итерации для сложных движений.**

- Примечания к источнику: Запрошено как случай 28. Оставлено как случай конкретного ограничения/стресс-теста.
- Статус аудита: сохраняется после ручной проверки дубликатов и оригинальности.
- Предварительный просмотр видео:

[![Воспроизвести демо-видео — Case 28](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case28.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case28.mp4)

Тип: Limit | Дата: 2026-06-26

---

<a id="related-repositories"></a>
## 🔗 Связанные репозитории

- [Посмотреть промпты Seedance 2.0](https://github.com/Evolink-AI/awesome-seedance-2.0-prompts)
- [Установить агентский skill Seedance 2](https://github.com/Evolink-AI/seedance2-video-gen-skill-for-openclaw)
- [Изучить рабочий процесс от GPT Image 2 к Seedance 2](https://github.com/Evolink-AI/GPT-Image-2-Seedance2-Workflow)


<a id="case-31"></a>
### Case 31: [Исправление тайминга черными кадрами между ключами](https://x.com/thechriscooper/status/2076092824102240411) (от [@thechriscooper](https://x.com/thechriscooper))

**Если грубый Blender-референс заставляет Seedance копировать роботические промежуточные движения, оставьте ключевые позы и затемните кадры между ними.**

- Примечания к источнику: Автор говорит, что Seedance слишком буквально копировал грубую Blender-анимацию, тогда как схема ключевой кадр-черный кадр-ключевой кадр сохранила blocking и сделала движение плавнее.
- Предварительный просмотр видео:

[![Предварительный просмотр видео — Case 31](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case31.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case31.mp4)

Тип: Tutorial | Дата: 2026-07-11

---

<a id="case-33"></a>
### Case 33: [Тест рассинхрона движения в сложной сцене](https://x.com/sonicpower1970/status/2074322339391824012) (от [@sonicpower1970](https://x.com/sonicpower1970))

**Смотрите на MCP-рендер грубой сцены как на тест ограничения: сложные Blender-сцены могут уходить от задуманных движений даже после нескольких прогонов в Seedance.**

- Примечания к источнику: Этот последующий пост сообщает, что даже после примерно четырех попыток сложные сцены не совпали с нужным движением в тесте автора Claude→Blender→Seedance.
- Предварительный просмотр видео:

[![Предварительный просмотр видео — Case 33](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case33.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case33.mp4)

Тип: Limit | Дата: 2026-07-07

---
<a id="acknowledge"></a>
## 🙏 Благодарности

Этот репозиторий был вдохновлен создателями, которые публично делились рабочими процессами, тестами, подсказками, справочными видеороликами и производственными заметками Blender + Seedance.

[@noman23761](https://x.com/noman23761), [@reidhannaford](https://x.com/reidhannaford), [@JMSvid](https://x.com/JMSvid), [@DiabloNemesis](https://x.com/DiabloNemesis), [@koldo2k](https://x.com/koldo2k), [@SamJWasserman](https://x.com/SamJWasserman), [@akiyoshisan](https://x.com/akiyoshisan), [@6_KAKUU](https://x.com/6_KAKUU), [@aidoga_lab](https://x.com/aidoga_lab), [@tanabe_fragm](https://x.com/tanabe_fragm), [@techhalla](https://x.com/techhalla), [@restofart](https://x.com/restofart), [@Viggle_PINOC](https://x.com/Viggle_PINOC), [@magneticskiff](https://x.com/magneticskiff), [@JoshDaws](https://x.com/JoshDaws), [@kan_mi_no9](https://x.com/kan_mi_no9), [@gcduncombe](https://x.com/gcduncombe), [@tea_story_hoshi](https://x.com/tea_story_hoshi), [@craftcapitallab](https://x.com/craftcapitallab), [@fatboypink](https://x.com/fatboypink)

*Мы не можем гарантировать, что каждый случай приписан первоначальному создателю. Если что-то необходимо исправить, свяжитесь с нами, и мы обновим это.*

Хотите добавить рабочий процесс Blender + Seedance? [Откройте задачу варианта использования](https://github.com/Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases/issues/new?template=use-case.yml) с помощью [файла шаблона задачи](.github/ISSUE_TEMPLATE/use-case.yml) или откройте запрос на включение с помощью [шаблона PR](.github/PULL_REQUEST_TEMPLATE.md).

[![Карта звездной истории](https://api.star-history.com/svg?repos=Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&type=Date)](https://www.star-history.com/#Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&Date)
