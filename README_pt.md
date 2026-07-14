<div align="center">

<a href="https://evolink.ai/cookbook/blender-to-video?utm_source=github&utm_medium=banner&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=readme_banner"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/images/banner.png" alt="Banner do repositório de casos de uso de Blender + Seedance" width="760"></a>

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

## 🍌 Introdução

Repositório de casos de uso Blender + Seedance.

**Reunimos fluxos reais com Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI e agentes para controlar a geração de vídeo no Seedance.**

A coleção vem dos dados X/Twitter fornecidos pelo proprietário. Cada caso aponta para o post original e o criador.

Comece pelo guia Blender-to-video da EvoLink e use o início rápido abaixo como referência local do fluxo.

## 📊 Visão geral

- **32 casos Blender + Seedance selecionados** a partir de posts públicos de criadores e de adições semanais auditadas.
- Cobre controle de câmera, previsualização no Blender, bloqueio de múltiplos personagens, coreografia de ação, Blender MCP, bloqueios assistidos por Codex/Claude, referências FBX/Mixamo, ComfyUI, transferência de estilo e limites conhecidos.
- Cada caso inclui fonte original, crédito ao criador, resumo acionável, tipo de evidência e data de publicação.
- A lista pública começou na auditoria de 35 candidatos e agora inclui 7 adições semanais auditadas do loop recorrente de atualização.
- Use este repositório para avaliar fluxos práticos e depois direcionar usuários ao guia Blender-to-video da EvoLink.

> [!NOTE]
> A coleção prioriza evidência concreta: passos, vídeos de referência, uso de agente/MCP, restrições reproduzíveis e limites claros.

<a id="quick-start"></a>
## ⚡ Início rápido

Configure primeiro o controle local do Blender; depois instale as skills EvoLink que o agente vai chamar.

### 1. Instale o Blender MCP

Siga o guia oficial de configuração do Blender MCP, abra o Blender e confirme que o agente consegue se conectar ao servidor Blender MCP antes de gerar referências.

- Configuração oficial: [Configurar Blender MCP](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

Antes da primeira solicitação executável, obtenha sua chave EvoLink em [Obtenha uma chave de API](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key).

### 2. Instale as skills EvoLink

Instale a skill de geração Seedance e a skill de upscale Topaz no workspace do agente.

```bash
npm i evolink-seedance
npm i evolink-topaz-video-upscale
```

### 3. [Obtenha uma chave de API](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key)

Crie uma chave de API da EvoLink na sua conta e exponha essa chave ao ambiente de execução do agente.

```bash
export EVOLINK_API_KEY="<your-evolink-api-key>"
```

### 4. Execute dentro do seu agente

Com MCP, skills e a chave de API prontos, peça ao agente para criar um bloqueio no Blender, exportar o vídeo de referência, gerar com Seedance e ampliar o resultado quando necessário.

Antes de enviar uma solicitação direta, confirme sua chave em [Obtenha uma chave de API](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key). Se precisar de um fallback direto de API, envie o workflow de referência do Blender para `POST https://api.evolink.ai/v1/videos/generations`:

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

Se você vai entregar este workflow a um agente agora, confirme primeiro a mesma chave em [Obtenha uma chave de API](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key).

```text
Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.
```

> [!NOTE]
> A página de configuração do Blender MCP é a fonte principal para os detalhes de instalação no Blender.

## 📑 Menu

| Seção | Casos |
|---|---|
| [🎥 Controle de câmera e previsualização](#camera-control-previs) | Case 1, 2, 3, 4, 5, 29 |
| [🎬 Bloqueio de personagens e ação](#character-action-blocking) | Case 6, 8, 9, 21, 32 |
| [🤖 Blender MCP com agentes](#agentic-blender-mcp) | Case 10, 11, 22, 34 |
| [🧩 Referências, prompts e mapeamento de múltiplas entradas](#reference-prompt-multi-input-mapping) | Case 13, 14, 23, 24, 26, 27, 35 |
| [🛠️ Pipelines e cadeias de ferramentas de produção](#production-pipelines-toolchains) | Case 15, 16, 17, 18, 30 |
| [🧪 Limites, testes e solução de problemas](#limits-tests-troubleshooting) | Case 20, 25, 28, 31, 33 |
| [🙏 Agradecimentos](#acknowledge) | Créditos e política de correções |

<a id="camera-control-previs"></a>
### 🎥 Controle de câmera e previsualização

| Caso | O que mostra | Tipo |
|---|---|---|
| [Blockout do Blender como referência de movimento para o Seedance](#case-1) | Um fluxo de direção combinado: use todo o método de gray box do caso original e leve-o ao timing, à velocidade, ao tremor e à coreografia espacial da previs de ação antes da geração no Seedance. | Demo |
| [Bloqueio de câmera com quadro inicial do Midjourney](#case-2) | Uma receita compacta de câmera precisa: o Blender fornece o movimento de câmera, o Midjourney fornece o quadro inicial e o Seedance segue a referência de movimento. | Demo |
| [Controle de câmera no ComfyUI com previs do Blender](#case-3) | Um caso de controle no ComfyUI em que a previs do Blender é combinada com quadros de referência separados, um normal e outro invertido, para testar a fidelidade ao movimento. | Demo |
| [Da prévia do viewport a um quadro inicial realista](#case-4) | Um tutorial curto de prévia no viewport: faça o blockout da cena, exporte a prévia, torne o primeiro quadro realista e forneça as duas referências ao Seedance. | Demo |
| [Um vídeo de referência, vários mundos](#case-5) | Um caso de variação de estilo e mundo em que o mesmo vídeo de referência do Blender conduz diferentes mundos gerados no Seedance. | Demo |
| [Previs de câmera com iPhone sincronizada ao diálogo](#case-29) | Use um passe de câmera do Blender guiado por iPhone e sincronizado com o diálogo, depois envie essa previs com áudio e duas imagens para o Seedance planejar a tomada. | Integration |


<a id="character-action-blocking"></a>
### 🎬 Bloqueio de personagens e ação

| Caso | O que mostra | Tipo |
|---|---|---|
| [Diálogo com vários personagens e poses correspondentes](#case-6) | Um fluxo para cenas de diálogo em que o Blender é usado para alinhar as poses dos personagens e o movimento da câmera antes de o Seedance gerar a cena encenada. | Demo |
| [Câmera de acompanhamento portátil através do espaço](#case-8) | Um caso de acompanhamento com câmera na mão em que o Blender controla o deslocamento do personagem e o Seedance leva o movimento de câmera áspero ao vídeo final. | Demo |
| [Bloqueio de câmera e personagens para ação tática](#case-9) | Um caso de bloqueio tático em que o Blender dirige a órbita da câmera, a escolha da lente, as posições de cobertura, os momentos de disparo e o movimento dos personagens antes da geração. | Demo |
| [Previs de emboscada além de um simples movimento de câmera](#case-21) | Um caso de emboscada que mostra como a previs no Blender pode resolver encenação, timing e movimento de câmera antes de o Seedance gerar a tomada. | Demo |
| [Perseguição de parkour no telhado com obstáculos](#case-32) | Monte uma previs de parkour no Blender com interações com obstáculos e batidas de evasão quando o Seedance tende a reduzir a ação a uma corrida reta. | Demo |


<a id="agentic-blender-mcp"></a>
### 🤖 Blender MCP com agentes

| Caso | O que mostra | Tipo |
|---|---|---|
| [Fluxo de vídeo de referência com Codex + Blender MCP](#case-10) | Um caso de Blender MCP com agentes em que o Codex cria um mercado 3D simples, o movimento de um gato, o enquadramento e uma referência MP4 para o Seedance. | Integration |
| [Arquitetura e trabalho de câmera criados pelo Codex](#case-11) | Um caso para iniciantes assistido pelo Codex em que a arquitetura e o trabalho de câmera são gerados no Blender e depois testados como referência de movimento para o Seedance. | Integration |
| [Previs no Blender MCP criada pelo Claude em minutos](#case-22) | Um caso rápido de previs com agentes em que o Claude usa o Blender MCP para criar uma referência de tomada em dois ou três minutos. | Integration |
| [Skill do Fable portada para o Codex](#case-34) | Peça para um agente construir a skill de vídeo de referência no Blender, portar para o Codex e testar se o Seedance consegue limpar o movimento sem usar prompt algum. | Integration |


<a id="reference-prompt-multi-input-mapping"></a>
### 🧩 Referências, prompts e mapeamento de múltiplas entradas

| Caso | O que mostra | Tipo |
|---|---|---|
| [Prompt reproduzível do Seedance com referência do Blender](#case-13) | Um caso combinado de reprodutibilidade e diagnóstico: a configuração detalha as condições do vídeo de referência, enquanto o teste pareado registra onde o controle de câmera e ritmo funcionou e onde o movimento dos pés falhou. | Tutorial |
| [Movimento do Mixamo como referência do Blender para iniciantes](#case-14) | Um caso de fonte de movimento acessível a iniciantes: use o movimento do Mixamo no Blender como base controlável antes de enviar a referência ao Seedance. | Tutorial |
| [Controle de referência apenas por posição para uma cena mais rápida](#case-23) | Um caso de ponderação da referência: mantenha a referência útil para posições e deixe o prompt recuperar velocidade e dinamismo. | Tutorial |
| [Brinquedo físico como referência em vez de software 3D](#case-24) | Um caso de referência física: use brinquedos como referências rápidas de movimento e encenação quando abrir o Blender der trabalho demais. | Demo |
| [Controle por referência para uma cena específica em que o prompt falhou](#case-26) | Uma alternativa de controle: quando a geração somente por prompt falhar, use uma referência para forçar a cena, mesmo com alguma redução de dinamismo. | Demo |
| [Dicas de proporção de personagens e fundos simples](#case-27) | Um caso em formato de checklist de estabilidade: alinhe as proporções do personagem além da altura e simplifique qualquer fundo que não precise de correspondência precisa. | Tutorial |
| [Mocap de manequim com quadro estilizado](#case-35) | Use uma fonte rígida de movimento do Blender ou de manequim para travar o timing e depois guie o estilo final e o comportamento do tecido no Seedance por meio do quadro de entrada. | Demo |


<a id="production-pipelines-toolchains"></a>
### 🛠️ Pipelines e cadeias de ferramentas de produção

| Caso | O que mostra | Tipo |
|---|---|---|
| [Stack com Hermes, Krea, ComfyUI e Blender MCP](#case-15) | Um pipeline de agentes com várias ferramentas em que o Hermes instala e conecta Krea, ComfyUI, Blender MCP e Seedance para produzir referências visuais e físicas. | Integration |
| [Do viewport do Blender MCP à transferência de estilo no Seedance](#case-16) | Um caso do viewport à transferência de estilo: o Blender MCP controla a câmera e os elementos; depois, Seedance e Magnific adicionam textura e iluminação. | Integration |
| [Da previs do Blender à renderização anime no Seedance](#case-17) | Um caso de previs 3D para anime que mostra como preservar os movimentos de câmera e a ação enquanto o Seedance altera o estilo de renderização. | Integration |
| [Clay pass FBX com câmera keyframed pelo Claude](#case-18) | Um fluxo de clay pass FBX em que o Blender importa o movimento, o Claude ajuda a criar keyframes de câmera e o passe renderizado se torna o vídeo de referência do Seedance. | Integration |
| [Pipeline de referência de dança orquestrado com Fable](#case-30) | Deixe um agente desenhar o personagem, gerar o código de coreografia no Blender e passar a referência de dança de 15 segundos ao Seedance quando o movimento por prompt for vago demais. | Integration |


<a id="limits-tests-troubleshooting"></a>
### 🧪 Limites, testes e solução de problemas

| Caso | O que mostra | Tipo |
|---|---|---|
| [Blockout do Blender somente com referência e sem quadro inicial](#case-20) | Uma variante sem quadro inicial que mostra que o blockout do Blender e referências detalhadas do ambiente podem funcionar quando o fluxo não pode depender de uma imagem inicial. | Limit |
| [Reforço de prompt com brinquedo de referência e exemplo malsucedido](#case-25) | Um caso de diagnóstico que mostra por que vídeos de referência frequentemente precisam de reforço no prompt em vez de imitação direta. | Limit |
| [Teste de estresse de física de tecidos com Blender e Seedance](#case-28) | Um teste de estresse de física de tecidos que mostra onde o Seedance guiado pelo Blender funciona, mas ainda exige iteração em movimentos difíceis. | Limit |
| [Correção de timing com quadros pretos entre keyframes](#case-31) | Quando uma referência bruta do Blender faz o Seedance copiar movimentos robóticos entre poses, mantenha as poses-chave e escureça os quadros intermediários. | Tutorial |
| [Teste de desencontro de movimento em cena complexa](#case-33) | Trate renders MCP de cena bruta como um teste de limite: cenas complexas no Blender ainda podem se desviar do movimento pretendido mesmo após várias tomadas no Seedance. | Limit |



<a id="camera-control-previs-cases"></a>
## 🎥 Controle de câmera e previsualização

<a id="case-1"></a>
### Case 1: [Blockout do Blender como referência de movimento para o Seedance](https://x.com/noman23761/status/2071534020014563328) (by [@noman23761](https://x.com/noman23761))

**Um fluxo de direção combinado: use todo o método de gray box do caso original e leve-o ao timing, à velocidade, ao tremor e à coreografia espacial da previs de ação antes da geração no Seedance.**

- Notas da fonte: Mesclado com o antigo caso 7: juntas, essas fontes mostram todo o fluxo de gray box e a variante de previs de ação com timing aproximado, velocidade, tremor e coreografia espacial.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case1.mp4)

Tipo: Demo | Data: 2026-06-29

---

<a id="case-2"></a>
### Case 2: [Bloqueio de câmera com quadro inicial do Midjourney](https://x.com/reidhannaford/status/2069074506849685773) (by [@reidhannaford](https://x.com/reidhannaford))

**Uma receita compacta de câmera precisa: o Blender fornece o movimento de câmera, o Midjourney fornece o quadro inicial e o Seedance segue a referência de movimento.**

- Notas da fonte: A fonte apresenta um fluxo claro de três etapas e relata que o vídeo gerado acompanha de perto o movimento de câmera do Blender.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case2.mp4)

Tipo: Demo | Data: 2026-06-22

---

<a id="case-3"></a>
### Case 3: [Controle de câmera no ComfyUI com previs do Blender](https://x.com/JMSvid/status/2070258132840796579) (by [@JMSvid](https://x.com/JMSvid))

**Um caso de controle no ComfyUI em que a previs do Blender é combinada com quadros de referência separados, um normal e outro invertido, para testar a fidelidade ao movimento.**

- Notas da fonte: O caso é útil porque combina a previs do Blender com várias referências estáticas em uma configuração de controle ao estilo do ComfyUI.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case3.mp4)

Tipo: Demo | Data: 2026-06-25

---

<a id="case-4"></a>
### Case 4: [Da prévia do viewport a um quadro inicial realista](https://x.com/DiabloNemesis/status/2070441923706503380) (by [@DiabloNemesis](https://x.com/DiabloNemesis))

**Um tutorial curto de prévia no viewport: faça o blockout da cena, exporte a prévia, torne o primeiro quadro realista e forneça as duas referências ao Seedance.**

- Notas da fonte: A publicação apresenta um fluxo conciso com artefatos concretos: prévia do viewport, imagem do primeiro quadro e vídeo de referência do Seedance. A mídia duplicada do caso 29 foi removida para que o caso público mostre apenas uma cópia do mesmo vídeo.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case4.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case4.mp4)

Tipo: Demo | Data: 2026-06-26

---

<a id="case-5"></a>
### Case 5: [Um vídeo de referência, vários mundos](https://x.com/koldo2k/status/2071307945002815967) (by [@koldo2k](https://x.com/koldo2k))

**Um caso de variação de estilo e mundo em que o mesmo vídeo de referência do Blender conduz diferentes mundos gerados no Seedance.**

- Notas da fonte: A fonte é útil porque separa o controle de movimento da variação de mundo e estilo usando o mesmo vídeo de referência.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 5](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case5.mp4)

Tipo: Demo | Data: 2026-06-28

---


<a id="case-29"></a>
### Case 29: [Previs de câmera com iPhone sincronizada ao diálogo](https://x.com/CoffeeVectors/status/2076397975853551924) (por [@CoffeeVectors](https://x.com/CoffeeVectors))

**Use um passe de câmera do Blender guiado por iPhone e sincronizado com o diálogo, depois envie essa previs com áudio e duas imagens para o Seedance planejar a tomada.**

- Notas da fonte: A fonte usa um passe de câmera do Blender guiado por iPhone e sincronizado com o diálogo, depois envia essa previs com áudio ao Seedance 2 junto com duas imagens fixas.
- Prévia de vídeo:

[![Prévia de vídeo — Case 29](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case29.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case29.mp4)

Tipo: Integration | Data: 2026-07-12

---
<a id="character-action-blocking-cases"></a>
## 🎬 Bloqueio de personagens e ação

<a id="case-6"></a>
### Case 6: [Diálogo com vários personagens e poses correspondentes](https://x.com/reidhannaford/status/2069420552394043625) (by [@reidhannaford](https://x.com/reidhannaford))

**Um fluxo para cenas de diálogo em que o Blender é usado para alinhar as poses dos personagens e o movimento da câmera antes de o Seedance gerar a cena encenada.**

- Notas da fonte: A fonte acrescenta diálogo com vários personagens e correspondência de poses, distinguindo-se das demos de controle de câmera com um único personagem.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 6](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case6.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case6.mp4)

Tipo: Demo | Data: 2026-06-23

---

<a id="case-8"></a>
### Case 8: [Câmera de acompanhamento portátil através do espaço](https://x.com/reidhannaford/status/2070507963429671062) (by [@reidhannaford](https://x.com/reidhannaford))

**Um caso de acompanhamento com câmera na mão em que o Blender controla o deslocamento do personagem e o Seedance leva o movimento de câmera áspero ao vídeo final.**

- Notas da fonte: A fonte move o personagem pela cena enquanto a câmera o acompanha, o que a torna útil para tomadas em movimento com câmera na mão.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

Prévia indisponível: o anexo original do GitHub não está mais acessível publicamente.

Tipo: Demo | Data: 2026-06-26

---

<a id="case-9"></a>
### Case 9: [Bloqueio de câmera e personagens para ação tática](https://x.com/SamJWasserman/status/2070742850095230991) (by [@SamJWasserman](https://x.com/SamJWasserman))

**Um caso de bloqueio tático em que o Blender dirige a órbita da câmera, a escolha da lente, as posições de cobertura, os momentos de disparo e o movimento dos personagens antes da geração.**

- Notas da fonte: A fonte mostra bloqueio simultâneo de câmera e personagens, uma referência mais forte do que um simples movimento de câmera.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 9](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case9.mp4)

Tipo: Demo | Data: 2026-06-27

---

<a id="case-21"></a>
### Case 21: [Previs de emboscada além de um simples movimento de câmera](https://x.com/reidhannaford/status/2071595581508563168) (by [@reidhannaford](https://x.com/reidhannaford))

**Um caso de emboscada que mostra como a previs no Blender pode resolver encenação, timing e movimento de câmera antes de o Seedance gerar a tomada.**

- Notas da fonte: Solicitado como caso 21. Mantido como exemplo distinto de Reid Hannaford porque leva o fluxo além de um simples movimento de câmera até a encenação.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 21](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case21.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case21.mp4)

Tipo: Demo | Data: 2026-06-29

---


<a id="case-32"></a>
### Case 32: [Perseguição de parkour no telhado com obstáculos](https://x.com/moframe2026/status/2075203485604470965) (por [@moframe2026](https://x.com/moframe2026))

**Monte uma previs de parkour no Blender com interações com obstáculos e batidas de evasão quando o Seedance tende a reduzir a ação a uma corrida reta.**

- Notas da fonte: O autor usa uma previs de parkour do Blender como referência de vídeo e diz que o Blender foi necessário para acrescentar obstáculos e fluxo de desvio além de uma corrida simples.
- Prévia de vídeo:

[![Prévia de vídeo — Case 32](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case32.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case32.mp4)

Tipo: Demo | Data: 2026-07-09

---
<a id="agentic-blender-mcp-cases"></a>
## 🤖 Blender MCP com agentes

<a id="case-10"></a>
### Case 10: [Fluxo de vídeo de referência com Codex + Blender MCP](https://x.com/akiyoshisan/status/2071081230108660199) (by [@akiyoshisan](https://x.com/akiyoshisan))

**Um caso de Blender MCP com agentes em que o Codex cria um mercado 3D simples, o movimento de um gato, o enquadramento e uma referência MP4 para o Seedance.**

- Notas da fonte: O autor diz que o teste foi inspirado por outro criador, mas a cena, o movimento, a câmera e o processo de exportação descritos são de seu próprio experimento.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 10](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case10.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case10.mp4)

Tipo: Integration | Data: 2026-06-28

---

<a id="case-11"></a>
### Case 11: [Arquitetura e trabalho de câmera criados pelo Codex](https://x.com/6_KAKUU/status/2071051063663452374) (by [@6_KAKUU](https://x.com/6_KAKUU))

**Um caso para iniciantes assistido pelo Codex em que a arquitetura e o trabalho de câmera são gerados no Blender e depois testados como referência de movimento para o Seedance.**

- Notas da fonte: A publicação é valiosa como fluxo de Codex para iniciantes: o usuário delega ao Codex a arquitetura e o trabalho de câmera antes do Seedance.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 11](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case11.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case11.mp4)

Tipo: Integration | Data: 2026-06-28

---

<a id="case-22"></a>
### Case 22: [Previs no Blender MCP criada pelo Claude em minutos](https://x.com/JoshDaws/status/2071401550845481090) (by [@JoshDaws](https://x.com/JoshDaws))

**Um caso rápido de previs com agentes em que o Claude usa o Blender MCP para criar uma referência de tomada em dois ou três minutos.**

- Notas da fonte: Solicitado como caso 22. Mantido porque demonstra velocidade e controle por agente, em vez de trabalho manual no Blender.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 22](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case22.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case22.mp4)

Tipo: Integration | Data: 2026-06-29

---


<a id="case-34"></a>
### Case 34: [Skill do Fable portada para o Codex](https://x.com/mugi_AI_Art/status/2074259600342163846) (por [@mugi_AI_Art](https://x.com/mugi_AI_Art))

**Peça para um agente construir a skill de vídeo de referência no Blender, portar para o Codex e testar se o Seedance consegue limpar o movimento sem usar prompt algum.**

- Notas da fonte: O autor fez o Fable construir uma skill de vídeo de referência no Blender, portou essa skill para o Codex e então executou uma geração no Seedance sem prompt a partir de referências modeladas de forma bruta.
- Prévia de vídeo:

[![Prévia de vídeo — Case 34](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case34.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case34.mp4)

Tipo: Integration | Data: 2026-07-06

---
<a id="reference-prompt-multi-input-mapping-cases"></a>
## 🧩 Referências, prompts e mapeamento de múltiplas entradas

<a id="case-13"></a>
### Case 13: [Prompt reproduzível do Seedance com referência do Blender](https://x.com/aidoga_lab/status/2070864815275585913) (by [@aidoga_lab](https://x.com/aidoga_lab))

**Um caso combinado de reprodutibilidade e diagnóstico: a configuração detalha as condições do vídeo de referência, enquanto o teste pareado registra onde o controle de câmera e ritmo funcionou e onde o movimento dos pés falhou.**

- Notas da fonte: Mesclado com o antigo caso 19: o par preserva tanto a configuração reproduzível quanto a observação de limitação sobre o deslizamento dos pés.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case13.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.mp4)

![Imagem de referência — Caso 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.jpg)

Tipo: Tutorial | Data: 2026-06-27

---

<a id="case-14"></a>
### Case 14: [Movimento do Mixamo como referência do Blender para iniciantes](https://x.com/tanabe_fragm/status/2070685291183243459) (by [@tanabe_fragm](https://x.com/tanabe_fragm))

**Um caso de fonte de movimento acessível a iniciantes: use o movimento do Mixamo no Blender como base controlável antes de enviar a referência ao Seedance.**

- Notas da fonte: A fonte é útil para iniciantes porque apresenta o Mixamo como uma fonte prática de movimento para vídeos de referência do Blender.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 14](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case14.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case14.mp4)

Tipo: Tutorial | Data: 2026-06-27

---

<a id="case-23"></a>
### Case 23: [Controle de referência apenas por posição para uma cena mais rápida](https://x.com/kan_mi_no9/status/2071380621214224403) (by [@kan_mi_no9](https://x.com/kan_mi_no9))

**Um caso de ponderação da referência: mantenha a referência útil para posições e deixe o prompt recuperar velocidade e dinamismo.**

- Notas da fonte: Solicitado como caso 23. Mantido com o teste pareado de kan_mi_no9 como uma variante distinta de controle por referência.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 23](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case23.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case23.mp4)

Tipo: Tutorial | Data: 2026-06-28

---

<a id="case-24"></a>
### Case 24: [Brinquedo físico como referência em vez de software 3D](https://x.com/gcduncombe/status/2070617538745229546) (by [@gcduncombe](https://x.com/gcduncombe))

**Um caso de referência física: use brinquedos como referências rápidas de movimento e encenação quando abrir o Blender der trabalho demais.**

- Notas da fonte: Solicitado como caso 24. Mantido porque amplia a ideia de vídeo de referência para além da previs feita apenas com software.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 24](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case24.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case24.mp4)

Tipo: Demo | Data: 2026-06-26

---

<a id="case-26"></a>
### Case 26: [Controle por referência para uma cena específica em que o prompt falhou](https://x.com/kan_mi_no9/status/2071168235022827587) (by [@kan_mi_no9](https://x.com/kan_mi_no9))

**Uma alternativa de controle: quando a geração somente por prompt falhar, use uma referência para forçar a cena, mesmo com alguma redução de dinamismo.**

- Notas da fonte: Solicitado como caso 26. Mantido como contraparte prática do caso posterior de variação de kan_mi_no9.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 26](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case26.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case26.mp4)

Tipo: Demo | Data: 2026-06-28

---

<a id="case-27"></a>
### Case 27: [Dicas de proporção de personagens e fundos simples](https://x.com/craftcapitallab/status/2070512271391068287) (by [@craftcapitallab](https://x.com/craftcapitallab))

**Um caso em formato de checklist de estabilidade: alinhe as proporções do personagem além da altura e simplifique qualquer fundo que não precise de correspondência precisa.**

- Notas da fonte: Solicitado como caso 27. Mantido porque oferece orientações de configuração específicas e reutilizáveis.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 27](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case27.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case27.mp4)

Tipo: Tutorial | Data: 2026-06-26

---


<a id="case-35"></a>
### Case 35: [Mocap de manequim com quadro estilizado](https://x.com/fatboypink/status/2074087401887039740) (por [@fatboypink](https://x.com/fatboypink))

**Use uma fonte rígida de movimento do Blender ou de manequim para travar o timing e depois guie o estilo final e o comportamento do tecido no Seedance por meio do quadro de entrada.**

- Notas da fonte: O autor diz que um mocap rígido de manequim guiou o timing do movimento, enquanto o quadro desenhado à mão ainda empurrou o Seedance para o estilo e o movimento do tecido desejados.
- Prévia de vídeo:

[![Prévia de vídeo — Case 35](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case35.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case35.mp4)

Tipo: Demo | Data: 2026-07-06

---
<a id="production-pipelines-toolchains-cases"></a>
## 🛠️ Pipelines e cadeias de ferramentas de produção

<a id="case-15"></a>
### Case 15: [Stack com Hermes, Krea, ComfyUI e Blender MCP](https://x.com/SamJWasserman/status/2069656428437225826) (by [@SamJWasserman](https://x.com/SamJWasserman))

**Um pipeline de agentes com várias ferramentas em que o Hermes instala e conecta Krea, ComfyUI, Blender MCP e Seedance para produzir referências visuais e físicas.**

- Notas da fonte: O caso demonstra um stack criativo mais amplo construído por agentes, e não apenas previs manual no Blender.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 15](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case15.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case15.mp4)

Tipo: Integration | Data: 2026-06-24

---

<a id="case-16"></a>
### Case 16: [Do viewport do Blender MCP à transferência de estilo no Seedance](https://x.com/techhalla/status/2070814203435274715) (by [@techhalla](https://x.com/techhalla))

**Um caso do viewport à transferência de estilo: o Blender MCP controla a câmera e os elementos; depois, Seedance e Magnific adicionam textura e iluminação.**

- Notas da fonte: Esta é a fonte mais forte de techhalla porque explica a animação no viewport e a etapa posterior de estilo e iluminação.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 16](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case16.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case16.mp4)

Tipo: Integration | Data: 2026-06-27

---

<a id="case-17"></a>
### Case 17: [Da previs do Blender à renderização anime no Seedance](https://x.com/restofart/status/2070086939756159368) (by [@restofart](https://x.com/restofart))

**Um caso de previs 3D para anime que mostra como preservar os movimentos de câmera e a ação enquanto o Seedance altera o estilo de renderização.**

- Notas da fonte: A fonte enquadra diretamente o fluxo como uma previs 3D do Blender transformada em renderização anime, preservando o movimento de câmera.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 17](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case17.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case17.mp4)

Tipo: Integration | Data: 2026-06-25

---

<a id="case-18"></a>
### Case 18: [Clay pass FBX com câmera keyframed pelo Claude](https://x.com/Viggle_PINOC/status/2070183934265012392) (by [@Viggle_PINOC](https://x.com/Viggle_PINOC))

**Um fluxo de clay pass FBX em que o Blender importa o movimento, o Claude ajuda a criar keyframes de câmera e o passe renderizado se torna o vídeo de referência do Seedance.**

- Notas da fonte: A fonte apresenta um processo específico de FBX para clay pass e inclui keyframes de câmera antes da exportação da referência.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 18](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case18.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case18.mp4)

Tipo: Integration | Data: 2026-06-25

---


<a id="case-30"></a>
### Case 30: [Pipeline de referência de dança orquestrado com Fable](https://x.com/ryo05m/status/2076284841457521043) (por [@ryo05m](https://x.com/ryo05m))

**Deixe um agente desenhar o personagem, gerar o código de coreografia no Blender e passar a referência de dança de 15 segundos ao Seedance quando o movimento por prompt for vago demais.**

- Notas da fonte: O autor descreve três passos: Seedream 5 Pro para o personagem, Blender para uma dança de manequim de 15 segundos e Seedance 2.0 para a passagem final de referência de movimento e câmera.
- Prévia de vídeo:

[![Prévia de vídeo — Case 30](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case30.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case30.mp4)

Tipo: Integration | Data: 2026-07-12

---
<a id="limits-tests-troubleshooting-cases"></a>
## 🧪 Limites, testes e solução de problemas

<a id="case-20"></a>
### Case 20: [Blockout do Blender somente com referência e sem quadro inicial](https://x.com/magneticskiff/status/2070711034793361559) (by [@magneticskiff](https://x.com/magneticskiff))

**Uma variante sem quadro inicial que mostra que o blockout do Blender e referências detalhadas do ambiente podem funcionar quando o fluxo não pode depender de uma imagem inicial.**

- Notas da fonte: Este caso cobre uma variante importante em que imagens de referência substituem a dependência usual de um quadro inicial.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 20](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case20.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case20.mp4)

Tipo: Limit | Data: 2026-06-27

---

<a id="case-25"></a>
### Case 25: [Reforço de prompt com brinquedo de referência e exemplo malsucedido](https://x.com/tea_story_hoshi/status/2071002538703479089) (by [@tea_story_hoshi](https://x.com/tea_story_hoshi))

**Um caso de diagnóstico que mostra por que vídeos de referência frequentemente precisam de reforço no prompt em vez de imitação direta.**

- Notas da fonte: Solicitado como caso 25. Mantido porque inclui exemplos funcionais e uma comparação malsucedida.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 25](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case25.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case25.mp4)

Tipo: Limit | Data: 2026-06-27

---

<a id="case-28"></a>
### Case 28: [Teste de estresse de física de tecidos com Blender e Seedance](https://x.com/fatboypink/status/2070577334701473800) (by [@fatboypink](https://x.com/fatboypink))

**Um teste de estresse de física de tecidos que mostra onde o Seedance guiado pelo Blender funciona, mas ainda exige iteração em movimentos difíceis.**

- Notas da fonte: Solicitado como caso 28. Mantido como um caso concreto de limitação e teste de estresse.
- Status da auditoria: mantido após revisão manual de duplicidade e originalidade.
- Prévia do vídeo:

[![Reproduzir vídeo de demonstração — Caso 28](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case28.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case28.mp4)

Tipo: Limit | Data: 2026-06-26

---

<a id="related-repositories"></a>
## 🔗 Repositórios relacionados

- [Explore prompts do Seedance 2.0](https://github.com/Evolink-AI/awesome-seedance-2.0-prompts)
- [Instale a skill de agente Seedance 2](https://github.com/Evolink-AI/seedance2-video-gen-skill-for-openclaw)
- [Explore o fluxo GPT Image 2 para Seedance 2](https://github.com/Evolink-AI/GPT-Image-2-Seedance2-Workflow)


<a id="case-31"></a>
### Case 31: [Correção de timing com quadros pretos entre keyframes](https://x.com/thechriscooper/status/2076092824102240411) (por [@thechriscooper](https://x.com/thechriscooper))

**Quando uma referência bruta do Blender faz o Seedance copiar movimentos robóticos entre poses, mantenha as poses-chave e escureça os quadros intermediários.**

- Notas da fonte: O autor diz que o Seedance copiava a animação bruta do Blender de forma literal demais, enquanto o padrão keyframe-preto-keyframe-preto manteve o blocking e suavizou o movimento.
- Prévia de vídeo:

[![Prévia de vídeo — Case 31](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case31.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case31.mp4)

Tipo: Tutorial | Data: 2026-07-11

---

<a id="case-33"></a>
### Case 33: [Teste de desencontro de movimento em cena complexa](https://x.com/sonicpower1970/status/2074322339391824012) (por [@sonicpower1970](https://x.com/sonicpower1970))

**Trate renders MCP de cena bruta como um teste de limite: cenas complexas no Blender ainda podem se desviar do movimento pretendido mesmo após várias tomadas no Seedance.**

- Notas da fonte: Este acompanhamento relata que, mesmo depois de cerca de quatro tomadas, cenas complexas ainda não correspondiam ao movimento pretendido no teste Claude→Blender→Seedance do autor.
- Prévia de vídeo:

[![Prévia de vídeo — Case 33](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case33.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case33.mp4)

Tipo: Limit | Data: 2026-07-07

---
<a id="acknowledge"></a>
## 🙏 Agradecimentos

Este repositório foi inspirado por criadores que compartilharam publicamente fluxos de Blender + Seedance, testes, prompts, vídeos de referência e notas de produção.

[@noman23761](https://x.com/noman23761), [@reidhannaford](https://x.com/reidhannaford), [@JMSvid](https://x.com/JMSvid), [@DiabloNemesis](https://x.com/DiabloNemesis), [@koldo2k](https://x.com/koldo2k), [@SamJWasserman](https://x.com/SamJWasserman), [@akiyoshisan](https://x.com/akiyoshisan), [@6_KAKUU](https://x.com/6_KAKUU), [@aidoga_lab](https://x.com/aidoga_lab), [@tanabe_fragm](https://x.com/tanabe_fragm), [@techhalla](https://x.com/techhalla), [@restofart](https://x.com/restofart), [@Viggle_PINOC](https://x.com/Viggle_PINOC), [@magneticskiff](https://x.com/magneticskiff), [@JoshDaws](https://x.com/JoshDaws), [@kan_mi_no9](https://x.com/kan_mi_no9), [@gcduncombe](https://x.com/gcduncombe), [@tea_story_hoshi](https://x.com/tea_story_hoshi), [@craftcapitallab](https://x.com/craftcapitallab), [@fatboypink](https://x.com/fatboypink)

*Não podemos garantir que todos os casos estejam atribuídos ao criador original. Se algo precisar de correção, entre em contato e nós o atualizaremos.*

Tem um fluxo de Blender + Seedance para adicionar? [Abra uma issue de caso de uso](https://github.com/Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases/issues/new?template=use-case.yml) com o [arquivo de template da issue](.github/ISSUE_TEMPLATE/use-case.yml), ou abra um pull request com o [template de PR](.github/PULL_REQUEST_TEMPLATE.md).

[![Gráfico do histórico de estrelas](https://api.star-history.com/svg?repos=Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&type=Date)](https://www.star-history.com/#Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&Date)
