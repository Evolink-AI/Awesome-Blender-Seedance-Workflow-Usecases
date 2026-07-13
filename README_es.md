<div align="center">

<a href="https://evolink.ai/cookbook/blender-to-video?utm_source=github&utm_medium=readme&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/images/banner.png" alt="Banner del repositorio de casos de uso de Blender + Seedance" width="760"></a>

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Usar en EvoLink](https://img.shields.io/badge/Use_on-EvoLink-black)](https://evolink.ai/cookbook/blender-to-video?utm_source=github&utm_medium=readme&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=use_on_evolink_badge)
[![MCP + Skill](https://img.shields.io/badge/MCP_%2B_Skill-Cookbook-orange)](https://evolink.ai/cookbook/blender-to-video?utm_source=github&utm_medium=readme&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=mcp_skill_badge)
[![Flujo con agentes](https://img.shields.io/badge/Agent_Workflow-Guide-blue)](https://evolink.ai/cookbook/blender-to-video?utm_source=github&utm_medium=readme&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=agent_workflow_badge)

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

## 🍌 Introducción

Repositorio de casos de uso Blender + Seedance.

**Reunimos flujos reales de Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI y agentes para controlar la generación de video con Seedance.**

La colección actual se deriva de datos X/Twitter proporcionados por el propietario. Cada caso enlaza la publicación original y el perfil del creador.

Empieza por la guía Blender-to-video de EvoLink y usa el inicio rápido que aparece a continuación como referencia local del flujo.

## 📊 Resumen

- **32 casos Blender + Seedance seleccionados** a partir de publicaciones públicas de creadores y de incorporaciones semanales auditadas.
- Cubre control de cámara, previsualización en Blender, bloqueo de varios personajes, coreografía de acción, Blender MCP, bloqueos asistidos por Codex/Claude, referencias FBX/Mixamo, ComfyUI, transferencia de estilo y límites conocidos.
- Cada caso incluye fuente original, atribución al creador, aprendizaje breve, tipo de evidencia y fecha de publicación.
- La lista pública partió de la auditoría de 35 candidatos y ahora incluye 7 incorporaciones semanales auditadas del bucle de actualización recurrente.
- Usa este repositorio para revisar flujos prácticos y luego dirigir a los usuarios a la guía Blender-to-video de EvoLink.

> [!NOTE]
> La colección prioriza evidencia concreta: pasos, referencias de video, uso de agentes/MCP, restricciones reproducibles y límites claros.

<a id="quick-start"></a>
## ⚡ Inicio rápido

Primero prepara el control local de Blender; después instala las skills de EvoLink que llamará tu agente.

### 1. Instala Blender MCP

Sigue la guía oficial de Blender MCP, abre Blender y verifica que tu agente pueda conectarse al servidor Blender MCP antes de generar referencias.

- Configuración oficial: [Configurar Blender MCP](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

### 2. Instala las skills de EvoLink

Instala la skill de generación Seedance y la skill de escalado Topaz en el workspace del agente.

```bash
npm i evolink-seedance
npm i evolink-topaz-video-upscale
```

### 3. [Obtén una clave API](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=readme&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key)

Crea una clave API de EvoLink en tu cuenta y exponla al entorno de ejecución del agente.

```bash
export EVOLINK_API_KEY="<your-evolink-api-key>"
```

### 4. Ejecútalo dentro de tu agente

Cuando MCP, las skills y la clave API estén listos, pide al agente que construya un bloqueo en Blender, exporte el video de referencia, genere con Seedance y escale el clip final si hace falta.

```text
Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.
```

> [!NOTE]
> La página de configuración de Blender MCP es la fuente principal para los detalles de instalación en Blender.

## 📑 Menú

| Sección | Casos |
|---|---|
| [🎥 Control de cámara y previsualización](#camera-control-previs) | Case 1, 2, 3, 4, 5, 29 |
| [🎬 Bloqueo de personajes y acción](#character-action-blocking) | Case 6, 8, 9, 21, 32 |
| [🤖 Blender MCP con agentes](#agentic-blender-mcp) | Case 10, 11, 22, 34 |
| [🧩 Referencias, prompts y correspondencia de múltiples entradas](#reference-prompt-multi-input-mapping) | Case 13, 14, 23, 24, 26, 27, 35 |
| [🛠️ Pipelines y cadenas de herramientas de producción](#production-pipelines-toolchains) | Case 15, 16, 17, 18, 30 |
| [🧪 Límites, pruebas y resolución de problemas](#limits-tests-troubleshooting) | Case 20, 25, 28, 31, 33 |
| [🙏 Agradecimientos](#acknowledge) | Créditos y política de correcciones |

<a id="camera-control-previs"></a>
### 🎥 Control de cámara y previsualización

| Caso | Qué muestra | Tipo |
|---|---|---|
| [Bloqueo de Blender como referencia de movimiento para Seedance](#case-1) | Un flujo de dirección combinado: aplica el método completo de bloqueo en gris del caso original y llévalo al ritmo, la velocidad, el temblor y la coreografía espacial de la previsualización de acción antes de generar con Seedance. | Demo |
| [Bloqueo de cámara con un fotograma inicial de Midjourney](#case-2) | Una receta compacta para una cámara precisa: Blender aporta el movimiento de cámara, Midjourney el fotograma inicial y Seedance sigue la referencia de movimiento. | Demo |
| [Control de cámara en ComfyUI con previsualización de Blender](#case-3) | Un caso de control con ComfyUI que combina la previsualización de Blender con fotogramas de referencia separados, uno vertical y otro invertido, para comprobar la fidelidad al movimiento. | Demo |
| [De la vista previa del viewport a un fotograma inicial realista](#case-4) | Un breve tutorial de previsualización en el viewport: bloquea la escena, exporta la vista previa, convierte el primer fotograma en una imagen realista y proporciona ambas referencias a Seedance. | Demo |
| [Un video de referencia, múltiples mundos](#case-5) | Un caso de variación de estilo y mundo en el que el mismo video de referencia de Blender impulsa distintos mundos generados con Seedance. | Demo |
| [Previsualización de cámara con iPhone sincronizada al diálogo](#case-29) | Usa un pase de cámara de Blender guiado por iPhone y sincronizado con el diálogo, y luego envía esa previs con audio más dos imágenes a Seedance para planificar la toma. | Integration |


<a id="character-action-blocking"></a>
### 🎬 Bloqueo de personajes y acción

| Caso | Qué muestra | Tipo |
|---|---|---|
| [Diálogo de varios personajes con poses coordinadas](#case-6) | Un flujo para planos de diálogo en el que Blender coordina las poses de los personajes y el movimiento de cámara antes de que Seedance genere la escena interpretada. | Demo |
| [Cámara de seguimiento en mano a través del espacio](#case-8) | Un caso de seguimiento con cámara en mano en el que Blender controla el desplazamiento del personaje y Seedance traslada el movimiento áspero de cámara al video final. | Demo |
| [Bloqueo de cámara y personajes para acción táctica](#case-9) | Un caso de bloqueo táctico en el que Blender dirige la órbita de cámara, la elección de lente, las posiciones de cobertura, los momentos de disparo y el movimiento de los personajes antes de generar. | Demo |
| [Previsualización de una emboscada más allá de un simple movimiento de cámara](#case-21) | Un caso de emboscada que muestra cómo la previsualización en Blender resuelve la puesta en escena, el ritmo y el movimiento de cámara antes de que Seedance genere el plano. | Demo |
| [Persecución parkour en azotea con obstáculos](#case-32) | Construye una previs de parkour en Blender con interacciones con obstáculos y beats de evasión cuando Seedance tiende a reducir la acción a una carrera recta. | Demo |


<a id="agentic-blender-mcp"></a>
### 🤖 Blender MCP con agentes

| Caso | Qué muestra | Tipo |
|---|---|---|
| [Flujo de video de referencia con Codex + Blender MCP](#case-10) | Un caso de Blender MCP con agentes en el que Codex crea un mercado 3D sencillo, el movimiento de un gato, el encuadre y una referencia MP4 para Seedance. | Integration |
| [Arquitectura y trabajo de cámara creados con Codex](#case-11) | Un caso para principiantes asistido por Codex en el que la arquitectura y el trabajo de cámara se generan en Blender y luego se prueban como referencia de movimiento para Seedance. | Integration |
| [Previsualización de Blender MCP creada por Claude en minutos](#case-22) | Un caso rápido de previsualización con agentes en el que Claude usa Blender MCP para crear una referencia de plano en dos o tres minutos. | Integration |
| [Skill de Fable migrada a Codex](#case-34) | Haz que un agente construya la skill de video de referencia en Blender, llévala a Codex y comprueba si Seedance puede pulir el movimiento sin usar ningún prompt. | Integration |


<a id="reference-prompt-multi-input-mapping"></a>
### 🧩 Referencias, prompts y correspondencia de múltiples entradas

| Caso | Qué muestra | Tipo |
|---|---|---|
| [Prompt reproducible de Seedance con referencia de Blender](#case-13) | Un caso combinado de reproducibilidad y diagnóstico: la configuración detalla las condiciones del video de referencia y la prueba asociada registra dónde funcionó el control de cámara y ritmo y dónde falló el movimiento de los pies. | Tutorial |
| [Movimiento de Mixamo como referencia de Blender para principiantes](#case-14) | Un caso de fuente de movimiento apto para principiantes: usa movimiento de Mixamo en Blender como base controlable antes de enviar la referencia a Seedance. | Tutorial |
| [Control de referencia solo de posición para una escena más rápida](#case-23) | Un caso de ponderación de referencia: conserva la referencia para las posiciones y deja que el prompt recupere la velocidad y el dinamismo. | Tutorial |
| [Referencia con juguetes físicos en lugar de software 3D](#case-24) | Un caso de referencia física: usa juguetes como referencias rápidas de movimiento y puesta en escena cuando abrir Blender supone demasiado trabajo. | Demo |
| [Control por referencia para una escena específica fallida con prompt](#case-26) | Un recurso de control alternativo: cuando falla la generación solo con prompt, usa una referencia para imponer la escena aunque se reduzca parte del dinamismo. | Demo |
| [Consejos sobre proporciones de personajes y fondos sencillos](#case-27) | Un caso con lista de estabilidad: iguala las proporciones del personaje más allá de la altura y simplifica cualquier fondo que no requiera una alineación precisa. | Tutorial |
| [Mocap de maniquí con fotograma estilizado](#case-35) | Usa una fuente de movimiento rígida de Blender o de un maniquí para fijar el ritmo y luego dirige el estilo final y la tela en Seedance mediante el diseño del fotograma de entrada. | Demo |


<a id="production-pipelines-toolchains"></a>
### 🛠️ Pipelines y cadenas de herramientas de producción

| Caso | Qué muestra | Tipo |
|---|---|---|
| [Stack de Hermes, Krea, ComfyUI y Blender MCP](#case-15) | Un pipeline de agentes con varias herramientas en el que Hermes instala y conecta Krea, ComfyUI, Blender MCP y Seedance para producir referencias visuales y físicas. | Integration |
| [Del viewport de Blender MCP a la transferencia de estilo con Seedance](#case-16) | Un caso del viewport a la transferencia de estilo: Blender MCP controla la cámara y los elementos; después, Seedance y Magnific añaden textura e iluminación. | Integration |
| [De la previsualización de Blender a un render anime con Seedance](#case-17) | Un caso de previsualización 3D a anime que muestra cómo conservar los movimientos de cámara y la acción mientras Seedance cambia el estilo de renderizado. | Integration |
| [Pasada de arcilla FBX con cámara animada mediante Claude](#case-18) | Un flujo de pasada de arcilla FBX en el que Blender importa el movimiento, Claude ayuda a animar por fotogramas clave la cámara y la pasada renderizada se convierte en video de referencia para Seedance. | Integration |
| [Pipeline de referencia de baile orquestado con Fable](#case-30) | Haz que un agente diseñe el personaje, genere el código de coreografía en Blender y entregue la referencia de baile de 15 segundos a Seedance cuando el movimiento por prompt sea demasiado tosco. | Integration |


<a id="limits-tests-troubleshooting"></a>
### 🧪 Límites, pruebas y resolución de problemas

| Caso | Qué muestra | Tipo |
|---|---|---|
| [Bloqueo de Blender solo con referencia y sin fotograma inicial](#case-20) | Una variante sin fotograma inicial que demuestra que el bloqueo de Blender y referencias detalladas del entorno pueden funcionar cuando el flujo no puede apoyarse en una imagen de inicio. | Limit |
| [Refuerzo del prompt con referencia de juguete y ejemplo fallido](#case-25) | Un caso de diagnóstico que muestra por qué los videos de referencia suelen necesitar refuerzo mediante el prompt en lugar de una imitación directa. | Limit |
| [Prueba de estrés de física de telas con Blender y Seedance](#case-28) | Una prueba de estrés de física de telas que muestra dónde puede funcionar Seedance guiado por Blender y dónde los movimientos difíciles aún requieren iteración. | Limit |
| [Corrección de ritmo con fotogramas negros entre poses](#case-31) | Si una referencia tosca de Blender hace que Seedance copie movimientos robóticos entre poses, conserva las poses clave y ennegrece los fotogramas intermedios. | Tutorial |
| [Prueba de desajuste de movimiento en escenas complejas](#case-33) | Trata los renders MCP de escena tosca como una prueba de límites: las escenas complejas de Blender aún pueden desviarse del movimiento previsto incluso tras varias tomas en Seedance. | Limit |



<a id="camera-control-previs-cases"></a>
## 🎥 Control de cámara y previsualización

<a id="case-1"></a>
### Case 1: [Bloqueo de Blender como referencia de movimiento para Seedance](https://x.com/noman23761/status/2071534020014563328) (by [@noman23761](https://x.com/noman23761))

**Un flujo de dirección combinado: aplica el método completo de bloqueo en gris del caso original y llévalo al ritmo, la velocidad, el temblor y la coreografía espacial de la previsualización de acción antes de generar con Seedance.**

- Notas de la fuente: Combinado con el antiguo caso 7; juntas, estas fuentes muestran el flujo completo de bloqueo en gris y la variante de previsualización de acción con ritmo aproximado, velocidad, temblor y coreografía espacial.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case1.mp4)

Tipo: Demo | Fecha: 2026-06-29

---

<a id="case-2"></a>
### Case 2: [Bloqueo de cámara con un fotograma inicial de Midjourney](https://x.com/reidhannaford/status/2069074506849685773) (by [@reidhannaford](https://x.com/reidhannaford))

**Una receta compacta para una cámara precisa: Blender aporta el movimiento de cámara, Midjourney el fotograma inicial y Seedance sigue la referencia de movimiento.**

- Notas de la fuente: La fuente ofrece un flujo claro de tres pasos e indica que el video generado sigue de cerca el movimiento de cámara de Blender.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case2.mp4)

Tipo: Demo | Fecha: 2026-06-22

---

<a id="case-3"></a>
### Case 3: [Control de cámara en ComfyUI con previsualización de Blender](https://x.com/JMSvid/status/2070258132840796579) (by [@JMSvid](https://x.com/JMSvid))

**Un caso de control con ComfyUI que combina la previsualización de Blender con fotogramas de referencia separados, uno vertical y otro invertido, para comprobar la fidelidad al movimiento.**

- Notas de la fuente: El caso resulta útil porque combina la previsualización de Blender con varias referencias fijas dentro de una configuración de control al estilo de ComfyUI.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case3.mp4)

Tipo: Demo | Fecha: 2026-06-25

---

<a id="case-4"></a>
### Case 4: [De la vista previa del viewport a un fotograma inicial realista](https://x.com/DiabloNemesis/status/2070441923706503380) (by [@DiabloNemesis](https://x.com/DiabloNemesis))

**Un breve tutorial de previsualización en el viewport: bloquea la escena, exporta la vista previa, convierte el primer fotograma en una imagen realista y proporciona ambas referencias a Seedance.**

- Notas de la fuente: La publicación presenta un flujo conciso con artefactos concretos: vista previa del viewport, imagen del primer fotograma y video de referencia de Seedance. Se eliminó el contenido multimedia duplicado del caso 29 para que el caso público muestre una sola copia del mismo video.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case4.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case4.mp4)

Tipo: Demo | Fecha: 2026-06-26

---

<a id="case-5"></a>
### Case 5: [Un video de referencia, múltiples mundos](https://x.com/koldo2k/status/2071307945002815967) (by [@koldo2k](https://x.com/koldo2k))

**Un caso de variación de estilo y mundo en el que el mismo video de referencia de Blender impulsa distintos mundos generados con Seedance.**

- Notas de la fuente: La fuente resulta útil porque separa el control del movimiento de la variación de mundo y estilo mediante el mismo video de referencia.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 5](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case5.mp4)

Tipo: Demo | Fecha: 2026-06-28

---


<a id="case-29"></a>
### Case 29: [Previsualización de cámara con iPhone sincronizada al diálogo](https://x.com/CoffeeVectors/status/2076397975853551924) (by [@CoffeeVectors](https://x.com/CoffeeVectors))

**Usa un pase de cámara de Blender guiado por iPhone y sincronizado con el diálogo, y luego envía esa previs con audio más dos imágenes a Seedance para planificar la toma.**

- Notas de la fuente: La fuente usa una cámara de Blender guiada por iPhone y sincronizada con el diálogo, y después envía esa previs con audio a Seedance 2 junto con dos imágenes fijas.
- Vista previa de video:

[![Vista previa de video — Case 29](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case29.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case29.mp4)

Tipo: Integration | Fecha: 2026-07-12

---
<a id="character-action-blocking-cases"></a>
## 🎬 Bloqueo de personajes y acción

<a id="case-6"></a>
### Case 6: [Diálogo de varios personajes con poses coordinadas](https://x.com/reidhannaford/status/2069420552394043625) (by [@reidhannaford](https://x.com/reidhannaford))

**Un flujo para planos de diálogo en el que Blender coordina las poses de los personajes y el movimiento de cámara antes de que Seedance genere la escena interpretada.**

- Notas de la fuente: La fuente añade diálogo entre varios personajes y coordinación de poses, lo que la diferencia de las demostraciones de control de cámara con un solo personaje.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 6](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case6.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case6.mp4)

Tipo: Demo | Fecha: 2026-06-23

---

<a id="case-8"></a>
### Case 8: [Cámara de seguimiento en mano a través del espacio](https://x.com/reidhannaford/status/2070507963429671062) (by [@reidhannaford](https://x.com/reidhannaford))

**Un caso de seguimiento con cámara en mano en el que Blender controla el desplazamiento del personaje y Seedance traslada el movimiento áspero de cámara al video final.**

- Notas de la fuente: La fuente desplaza al personaje por la escena mientras la cámara lo sigue, por lo que resulta útil para planos de movimiento con cámara en mano.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

Vista previa no disponible: el archivo adjunto original de GitHub ya no es accesible públicamente.

Tipo: Demo | Fecha: 2026-06-26

---

<a id="case-9"></a>
### Case 9: [Bloqueo de cámara y personajes para acción táctica](https://x.com/SamJWasserman/status/2070742850095230991) (by [@SamJWasserman](https://x.com/SamJWasserman))

**Un caso de bloqueo táctico en el que Blender dirige la órbita de cámara, la elección de lente, las posiciones de cobertura, los momentos de disparo y el movimiento de los personajes antes de generar.**

- Notas de la fuente: La fuente muestra un bloqueo simultáneo de cámara y personajes, una referencia más sólida que un simple movimiento de cámara.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 9](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case9.mp4)

Tipo: Demo | Fecha: 2026-06-27

---

<a id="case-21"></a>
### Case 21: [Previsualización de una emboscada más allá de un simple movimiento de cámara](https://x.com/reidhannaford/status/2071595581508563168) (by [@reidhannaford](https://x.com/reidhannaford))

**Un caso de emboscada que muestra cómo la previsualización en Blender resuelve la puesta en escena, el ritmo y el movimiento de cámara antes de que Seedance genere el plano.**

- Notas de la fuente: Solicitado como caso 21. Se conservó como ejemplo diferenciado de Reid Hannaford porque lleva el flujo más allá de un simple movimiento de cámara hasta la puesta en escena.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 21](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case21.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case21.mp4)

Tipo: Demo | Fecha: 2026-06-29

---


<a id="case-32"></a>
### Case 32: [Persecución parkour en azotea con obstáculos](https://x.com/moframe2026/status/2075203485604470965) (by [@moframe2026](https://x.com/moframe2026))

**Construye una previs de parkour en Blender con interacciones con obstáculos y beats de evasión cuando Seedance tiende a reducir la acción a una carrera recta.**

- Notas de la fuente: El autor usa una previs de parkour en Blender como referencia de video y dice que Blender fue necesario para añadir obstáculos y flujo de evasión más allá de una simple carrera.
- Vista previa de video:

[![Vista previa de video — Case 32](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case32.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case32.mp4)

Tipo: Demo | Fecha: 2026-07-09

---
<a id="agentic-blender-mcp-cases"></a>
## 🤖 Blender MCP con agentes

<a id="case-10"></a>
### Case 10: [Flujo de video de referencia con Codex + Blender MCP](https://x.com/akiyoshisan/status/2071081230108660199) (by [@akiyoshisan](https://x.com/akiyoshisan))

**Un caso de Blender MCP con agentes en el que Codex crea un mercado 3D sencillo, el movimiento de un gato, el encuadre y una referencia MP4 para Seedance.**

- Notas de la fuente: El autor señala que la prueba se inspiró en otro creador, pero la escena, el movimiento, la cámara y el proceso de exportación descritos pertenecen a su propio experimento.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 10](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case10.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case10.mp4)

Tipo: Integration | Fecha: 2026-06-28

---

<a id="case-11"></a>
### Case 11: [Arquitectura y trabajo de cámara creados con Codex](https://x.com/6_KAKUU/status/2071051063663452374) (by [@6_KAKUU](https://x.com/6_KAKUU))

**Un caso para principiantes asistido por Codex en el que la arquitectura y el trabajo de cámara se generan en Blender y luego se prueban como referencia de movimiento para Seedance.**

- Notas de la fuente: La publicación es valiosa como flujo de Codex para principiantes: el usuario delega en Codex la arquitectura y el trabajo de cámara antes de usar Seedance.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 11](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case11.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case11.mp4)

Tipo: Integration | Fecha: 2026-06-28

---

<a id="case-22"></a>
### Case 22: [Previsualización de Blender MCP creada por Claude en minutos](https://x.com/JoshDaws/status/2071401550845481090) (by [@JoshDaws](https://x.com/JoshDaws))

**Un caso rápido de previsualización con agentes en el que Claude usa Blender MCP para crear una referencia de plano en dos o tres minutos.**

- Notas de la fuente: Solicitado como caso 22. Se conservó porque demuestra velocidad y control mediante agentes en lugar de trabajo manual en Blender.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 22](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case22.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case22.mp4)

Tipo: Integration | Fecha: 2026-06-29

---


<a id="case-34"></a>
### Case 34: [Skill de Fable migrada a Codex](https://x.com/mugi_AI_Art/status/2074259600342163846) (by [@mugi_AI_Art](https://x.com/mugi_AI_Art))

**Haz que un agente construya la skill de video de referencia en Blender, llévala a Codex y comprueba si Seedance puede pulir el movimiento sin usar ningún prompt.**

- Notas de la fuente: El autor hizo que Fable construyera una skill de video de referencia en Blender, la migró a Codex y luego ejecutó una generación en Seedance sin prompt a partir de referencias modeladas de forma tosca.
- Vista previa de video:

[![Vista previa de video — Case 34](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case34.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case34.mp4)

Tipo: Integration | Fecha: 2026-07-06

---
<a id="reference-prompt-multi-input-mapping-cases"></a>
## 🧩 Referencias, prompts y correspondencia de múltiples entradas

<a id="case-13"></a>
### Case 13: [Prompt reproducible de Seedance con referencia de Blender](https://x.com/aidoga_lab/status/2070864815275585913) (by [@aidoga_lab](https://x.com/aidoga_lab))

**Un caso combinado de reproducibilidad y diagnóstico: la configuración detalla las condiciones del video de referencia y la prueba asociada registra dónde funcionó el control de cámara y ritmo y dónde falló el movimiento de los pies.**

- Notas de la fuente: Combinado con el antiguo caso 19; la pareja conserva tanto la configuración reproducible como la nota de limitación sobre el deslizamiento de los pies.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case13.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.mp4)

![Imagen de referencia — Caso 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.jpg)

Tipo: Tutorial | Fecha: 2026-06-27

---

<a id="case-14"></a>
### Case 14: [Movimiento de Mixamo como referencia de Blender para principiantes](https://x.com/tanabe_fragm/status/2070685291183243459) (by [@tanabe_fragm](https://x.com/tanabe_fragm))

**Un caso de fuente de movimiento apto para principiantes: usa movimiento de Mixamo en Blender como base controlable antes de enviar la referencia a Seedance.**

- Notas de la fuente: La fuente resulta útil para principiantes porque identifica Mixamo como una fuente práctica de movimiento para videos de referencia de Blender.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 14](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case14.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case14.mp4)

Tipo: Tutorial | Fecha: 2026-06-27

---

<a id="case-23"></a>
### Case 23: [Control de referencia solo de posición para una escena más rápida](https://x.com/kan_mi_no9/status/2071380621214224403) (by [@kan_mi_no9](https://x.com/kan_mi_no9))

**Un caso de ponderación de referencia: conserva la referencia para las posiciones y deja que el prompt recupere la velocidad y el dinamismo.**

- Notas de la fuente: Solicitado como caso 23. Se conservó junto con la prueba asociada de kan_mi_no9 como una variante diferenciada de control por referencia.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 23](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case23.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case23.mp4)

Tipo: Tutorial | Fecha: 2026-06-28

---

<a id="case-24"></a>
### Case 24: [Referencia con juguetes físicos en lugar de software 3D](https://x.com/gcduncombe/status/2070617538745229546) (by [@gcduncombe](https://x.com/gcduncombe))

**Un caso de referencia física: usa juguetes como referencias rápidas de movimiento y puesta en escena cuando abrir Blender supone demasiado trabajo.**

- Notas de la fuente: Solicitado como caso 24. Se conservó porque amplía la idea del video de referencia más allá de la previsualización realizada solo con software.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 24](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case24.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case24.mp4)

Tipo: Demo | Fecha: 2026-06-26

---

<a id="case-26"></a>
### Case 26: [Control por referencia para una escena específica fallida con prompt](https://x.com/kan_mi_no9/status/2071168235022827587) (by [@kan_mi_no9](https://x.com/kan_mi_no9))

**Un recurso de control alternativo: cuando falla la generación solo con prompt, usa una referencia para imponer la escena aunque se reduzca parte del dinamismo.**

- Notas de la fuente: Solicitado como caso 26. Se conservó como contraparte práctica del posterior caso de variación de kan_mi_no9.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 26](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case26.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case26.mp4)

Tipo: Demo | Fecha: 2026-06-28

---

<a id="case-27"></a>
### Case 27: [Consejos sobre proporciones de personajes y fondos sencillos](https://x.com/craftcapitallab/status/2070512271391068287) (by [@craftcapitallab](https://x.com/craftcapitallab))

**Un caso con lista de estabilidad: iguala las proporciones del personaje más allá de la altura y simplifica cualquier fondo que no requiera una alineación precisa.**

- Notas de la fuente: Solicitado como caso 27. Se conservó porque ofrece consejos de configuración específicos y reutilizables.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 27](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case27.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case27.mp4)

Tipo: Tutorial | Fecha: 2026-06-26

---


<a id="case-35"></a>
### Case 35: [Mocap de maniquí con fotograma estilizado](https://x.com/fatboypink/status/2074087401887039740) (by [@fatboypink](https://x.com/fatboypink))

**Usa una fuente de movimiento rígida de Blender o de un maniquí para fijar el ritmo y luego dirige el estilo final y la tela en Seedance mediante el diseño del fotograma de entrada.**

- Notas de la fuente: El autor dice que un mocap rígido de maniquí marcó el ritmo del movimiento, mientras que el fotograma dibujado a mano siguió empujando a Seedance hacia el estilo y el movimiento de tela deseados.
- Vista previa de video:

[![Vista previa de video — Case 35](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case35.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case35.mp4)

Tipo: Demo | Fecha: 2026-07-06

---
<a id="production-pipelines-toolchains-cases"></a>
## 🛠️ Pipelines y cadenas de herramientas de producción

<a id="case-15"></a>
### Case 15: [Stack de Hermes, Krea, ComfyUI y Blender MCP](https://x.com/SamJWasserman/status/2069656428437225826) (by [@SamJWasserman](https://x.com/SamJWasserman))

**Un pipeline de agentes con varias herramientas en el que Hermes instala y conecta Krea, ComfyUI, Blender MCP y Seedance para producir referencias visuales y físicas.**

- Notas de la fuente: El caso demuestra un stack creativo más amplio creado por agentes, no solo una previsualización manual en Blender.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 15](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case15.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case15.mp4)

Tipo: Integration | Fecha: 2026-06-24

---

<a id="case-16"></a>
### Case 16: [Del viewport de Blender MCP a la transferencia de estilo con Seedance](https://x.com/techhalla/status/2070814203435274715) (by [@techhalla](https://x.com/techhalla))

**Un caso del viewport a la transferencia de estilo: Blender MCP controla la cámara y los elementos; después, Seedance y Magnific añaden textura e iluminación.**

- Notas de la fuente: Esta es la fuente más sólida de techhalla porque explica la animación del viewport y la etapa posterior de estilo e iluminación.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 16](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case16.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case16.mp4)

Tipo: Integration | Fecha: 2026-06-27

---

<a id="case-17"></a>
### Case 17: [De la previsualización de Blender a un render anime con Seedance](https://x.com/restofart/status/2070086939756159368) (by [@restofart](https://x.com/restofart))

**Un caso de previsualización 3D a anime que muestra cómo conservar los movimientos de cámara y la acción mientras Seedance cambia el estilo de renderizado.**

- Notas de la fuente: La fuente presenta directamente el flujo como una previsualización 3D de Blender transformada en un render anime que conserva el movimiento de cámara.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 17](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case17.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case17.mp4)

Tipo: Integration | Fecha: 2026-06-25

---

<a id="case-18"></a>
### Case 18: [Pasada de arcilla FBX con cámara animada mediante Claude](https://x.com/Viggle_PINOC/status/2070183934265012392) (by [@Viggle_PINOC](https://x.com/Viggle_PINOC))

**Un flujo de pasada de arcilla FBX en el que Blender importa el movimiento, Claude ayuda a animar por fotogramas clave la cámara y la pasada renderizada se convierte en video de referencia para Seedance.**

- Notas de la fuente: La fuente ofrece un proceso específico de FBX a pasada de arcilla e incluye la animación de cámara con fotogramas clave antes de exportar la referencia.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 18](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case18.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case18.mp4)

Tipo: Integration | Fecha: 2026-06-25

---


<a id="case-30"></a>
### Case 30: [Pipeline de referencia de baile orquestado con Fable](https://x.com/ryo05m/status/2076284841457521043) (by [@ryo05m](https://x.com/ryo05m))

**Haz que un agente diseñe el personaje, genere el código de coreografía en Blender y entregue la referencia de baile de 15 segundos a Seedance cuando el movimiento por prompt sea demasiado tosco.**

- Notas de la fuente: El autor describe tres pasos: Seedream 5 Pro para el personaje, Blender para un baile de maniquí de 15 segundos y Seedance 2.0 para la referencia final de movimiento y cámara.
- Vista previa de video:

[![Vista previa de video — Case 30](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case30.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case30.mp4)

Tipo: Integration | Fecha: 2026-07-12

---
<a id="limits-tests-troubleshooting-cases"></a>
## 🧪 Límites, pruebas y resolución de problemas

<a id="case-20"></a>
### Case 20: [Bloqueo de Blender solo con referencia y sin fotograma inicial](https://x.com/magneticskiff/status/2070711034793361559) (by [@magneticskiff](https://x.com/magneticskiff))

**Una variante sin fotograma inicial que demuestra que el bloqueo de Blender y referencias detalladas del entorno pueden funcionar cuando el flujo no puede apoyarse en una imagen de inicio.**

- Notas de la fuente: Este caso cubre una variante importante en la que las imágenes de referencia sustituyen la dependencia habitual de un fotograma inicial.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 20](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case20.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case20.mp4)

Tipo: Limit | Fecha: 2026-06-27

---

<a id="case-25"></a>
### Case 25: [Refuerzo del prompt con referencia de juguete y ejemplo fallido](https://x.com/tea_story_hoshi/status/2071002538703479089) (by [@tea_story_hoshi](https://x.com/tea_story_hoshi))

**Un caso de diagnóstico que muestra por qué los videos de referencia suelen necesitar refuerzo mediante el prompt en lugar de una imitación directa.**

- Notas de la fuente: Solicitado como caso 25. Se conservó porque incluye ejemplos que funcionan y una comparación fallida.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 25](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case25.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case25.mp4)

Tipo: Limit | Fecha: 2026-06-27

---

<a id="case-28"></a>
### Case 28: [Prueba de estrés de física de telas con Blender y Seedance](https://x.com/fatboypink/status/2070577334701473800) (by [@fatboypink](https://x.com/fatboypink))

**Una prueba de estrés de física de telas que muestra dónde puede funcionar Seedance guiado por Blender y dónde los movimientos difíciles aún requieren iteración.**

- Notas de la fuente: Solicitado como caso 28. Se conservó como un caso concreto de limitación y prueba de estrés.
- Estado de auditoría: conservado tras la revisión manual de duplicados y originalidad.
- Vista previa de video:

[![Reproducir video de demostración — Caso 28](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case28.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case28.mp4)

Tipo: Limit | Fecha: 2026-06-26

---

<a id="related-repositories"></a>
## 🔗 Repositorios relacionados

- [Explora prompts de Seedance 2.0](https://github.com/Evolink-AI/awesome-seedance-2.0-prompts)
- [Instala la skill de agente Seedance 2](https://github.com/Evolink-AI/seedance2-video-gen-skill-for-openclaw)
- [Explora el flujo GPT Image 2 a Seedance 2](https://github.com/Evolink-AI/GPT-Image-2-Seedance2-Workflow)


<a id="case-31"></a>
### Case 31: [Corrección de ritmo con fotogramas negros entre poses](https://x.com/thechriscooper/status/2076092824102240411) (by [@thechriscooper](https://x.com/thechriscooper))

**Si una referencia tosca de Blender hace que Seedance copie movimientos robóticos entre poses, conserva las poses clave y ennegrece los fotogramas intermedios.**

- Notas de la fuente: El autor explica que Seedance copiaba demasiado literalmente la animación tosca de Blender, mientras que el patrón pose-clave-negro-pose-clave-negro mantuvo el blocking y suavizó el movimiento.
- Vista previa de video:

[![Vista previa de video — Case 31](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case31.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case31.mp4)

Tipo: Tutorial | Fecha: 2026-07-11

---

<a id="case-33"></a>
### Case 33: [Prueba de desajuste de movimiento en escenas complejas](https://x.com/sonicpower1970/status/2074322339391824012) (by [@sonicpower1970](https://x.com/sonicpower1970))

**Trata los renders MCP de escena tosca como una prueba de límites: las escenas complejas de Blender aún pueden desviarse del movimiento previsto incluso tras varias tomas en Seedance.**

- Notas de la fuente: Este seguimiento informa que incluso después de unas cuatro tomas las escenas complejas seguían sin igualar el movimiento previsto en la prueba Claude→Blender→Seedance del autor.
- Vista previa de video:

[![Vista previa de video — Case 33](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case33.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case33.mp4)

Tipo: Limit | Fecha: 2026-07-07

---
<a id="acknowledge"></a>
## 🙏 Agradecimientos

Este repositorio se inspiró en creadores que compartieron públicamente flujos de Blender + Seedance, pruebas, prompts, videos de referencia y notas de producción.

[@noman23761](https://x.com/noman23761), [@reidhannaford](https://x.com/reidhannaford), [@JMSvid](https://x.com/JMSvid), [@DiabloNemesis](https://x.com/DiabloNemesis), [@koldo2k](https://x.com/koldo2k), [@SamJWasserman](https://x.com/SamJWasserman), [@akiyoshisan](https://x.com/akiyoshisan), [@6_KAKUU](https://x.com/6_KAKUU), [@aidoga_lab](https://x.com/aidoga_lab), [@tanabe_fragm](https://x.com/tanabe_fragm), [@techhalla](https://x.com/techhalla), [@restofart](https://x.com/restofart), [@Viggle_PINOC](https://x.com/Viggle_PINOC), [@magneticskiff](https://x.com/magneticskiff), [@JoshDaws](https://x.com/JoshDaws), [@kan_mi_no9](https://x.com/kan_mi_no9), [@gcduncombe](https://x.com/gcduncombe), [@tea_story_hoshi](https://x.com/tea_story_hoshi), [@craftcapitallab](https://x.com/craftcapitallab), [@fatboypink](https://x.com/fatboypink)

*No podemos garantizar que todos los casos estén atribuidos a su creador original. Si es necesario corregir algo, contáctanos y lo actualizaremos.*

¿Tienes un flujo de Blender + Seedance que añadir? [Abre una incidencia de caso de uso](https://github.com/Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases/issues/new?template=use-case.yml) con el [archivo de plantilla de incidencias](.github/ISSUE_TEMPLATE/use-case.yml), o abre una pull request con la [plantilla de PR](.github/PULL_REQUEST_TEMPLATE.md).

[![Gráfico del historial de estrellas](https://api.star-history.com/svg?repos=Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&type=Date)](https://www.star-history.com/#Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&Date)
