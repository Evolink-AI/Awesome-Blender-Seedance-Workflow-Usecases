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

## 🍌 Giriş

Blender + Seedance kullanım senaryosu deposuna hoş geldiniz.

**Gerçek dünyadaki Blender, Blender MCP, viewport, previs, FBX, Mixamo, ComfyUI ve yaratıcıların Seedance video oluşturmayı kontrol etmek için kullandıkları aracı destekli iş akışlarını topluyoruz.**

Mevcut koleksiyon, kullanıcı tarafından sağlanan X/Twitter kaynak verilerinden seçilmiştir. Her vaka orijinal gönderiye ve yaratıcı profiline bağlantı verir.

EvoLink Blender-video yemek kitabından başlayın, ardından depo-yerel iş akışı referansı olarak aşağıdaki Hızlı Başlangıç'ı kullanın.

## 📊 Genel Bakış

- **Sahibinin sağladığı kaynak veri kümesindeki herkese açık içerik oluşturucu gönderilerinden seçilen 25 Blender + Seedance vaka**.
- Kamera kontrolü, Blender ön izleme, çoklu karakter engelleme, aksiyon koreografisi, Blender MCP, Codex/Claude destekli engellemeler, FBX/Mixamo referansları, ComfyUI/stil aktarımı ve bilinen sınırlamaları kapsar.
- Her vaka orijinal kaynağı, yaratıcının atıfını, kısa bir çıkarımı, kanıt türünü ve yayın tarihini içerir.
- Herkese açık liste, 35 adaylık denetimden ve talep edilen yeni bağlantılardan 25 ana vakaya yeniden oluşturuldu.
- Pratik iş akışlarını incelemek için bu repoyu kullanın, ardından kurulum ve yürütme için kullanıcıları EvoLink Blender-video yemek kitabına gönderin.

> [!NOTE]
> Koleksiyon, abartı yerine somut iş akışı kanıtlarını tercih ediyor: kaynak destekli adımlar, referans video yöntemleri, aracı/MCP kullanımı, tekrarlanabilir kısıtlamalar ve açıkça belirtilmiş sınırlar.

<a id="quick-start"></a>
## ⚡ Hızlı Başlangıç

Önce yerel Blender kontrol yolunu ayarlayın, ardından temsilcinizin arayacağı EvoLink becerilerini yükleyin.

### 1. Blender MCP'yi yükleyin

Resmi Blender MCP kurulum kılavuzunu takip edin, Blender'yi açın ve referansları oluşturmadan önce aracınızın Blender MCP sunucusuna bağlanabildiğinden emin olun.

- Resmi kurulum: [Blender MCP kurulum](https://projects.blender.org/lab/blender_mcp/wiki/Setup)

İlk çalıştırılabilir istekten önce EvoLink anahtarınızı [API anahtarı alın](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key) bağlantısından alın.

### 2. EvoLink becerilerini yükleyin

Aracı çalışma alanına Seedance oluşturma becerisini ve Topaz yükseltme becerisini yükleyin.

```bash
npm i evolink-seedance
npm i evolink-topaz-video-upscale
```

### 3. [API anahtarı alın](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key)

Hesabınızdan bir EvoLink API anahtarı oluşturun ve ardından bunu aracı çalışma zamanına gösterin.

```bash
export EVOLINK_API_KEY="<your-evolink-api-key>"
```

### 4. Aracınızın içinde çalıştırın

MCP, beceriler ve API anahtarı hazır olduktan sonra temsilcinizden bir Blender blokajı oluşturmasını, referans videoyu dışa aktarmasını, Seedance ile oluşturmasını ve gerektiğinde son klibi yükseltmesini isteyin.

Doğrudan istek göndermeden önce anahtarınızı [API anahtarı alın](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key) bağlantısından doğrulayın. Doğrudan API fallback gerekirse Blender referans iş akışını `POST https://api.evolink.ai/v1/videos/generations` adresine gönderin:

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

Bu iş akışını şimdi bir aracıya devredecekseniz aynı anahtarı önce [API anahtarı alın](https://evolink.ai/dashboard/keys?utm_source=github&utm_medium=quickstart&utm_campaign=awesome-blender-seedance-workflow-usecases&utm_content=api_key) bağlantısında doğrulayın.

```text
Use Blender MCP to create a rough 5-second camera blockout for this shot, export it as a reference video, generate the final video with Seedance, then upscale the output with Topaz if the result is approved.
```

> [!NOTE]
> Blender MCP kurulum sayfası, Blender tarafı kurulum detayları için gerçeklerin kaynağıdır.

## 📑 Menü

| Bölüm | Vakalar |
|---|---|
| [🎥 Kamera Kontrolü ve Ön İzleme](#camera-control-previs) | Case 1, 2, 3, 4, 5, 29 |
| [🎬 Karakter ve Eylem Engelleme](#character-action-blocking) | Case 6, 8, 9, 21, 32 |
| [🤖 Ajan Blender MCP](#agentic-blender-mcp) | Case 10, 11, 22, 34 |
| [🧩 Referans, Bilgi İstemi ve Çoklu Giriş Eşlemesi](#reference-prompt-multi-input-mapping) | Case 13, 14, 23, 24, 26, 27, 35 |
| [🛠️ Üretim Boru Hatları ve Takım Zincirleri](#production-pipelines-toolchains) | Case 15, 16, 17, 18, 30 |
| [🧪 Sınırlar, Testler ve Sorun Giderme](#limits-tests-troubleshooting) | Case 20, 25, 28, 31, 33 |
| [🙏 Teşekkür](#acknowledge) | Katkılar ve düzeltme politikası |

<a id="camera-control-previs"></a>
### 🎥 Kamera Kontrolü ve Ön İzleme

| Case | Ne gösterir | Tür |
|---|---|---|
| [Blender Seedance Hareket Referansı Olarak Engelleme](#case-1) | Birleştirilmiş yön iş akışı: Orijinal durumdaki tam gri kutu yöntemini kullanın, ardından Seedance oluşturmadan önce zamanlama, hız, sarsıntı ve mekansal koreografiyi önceden aksiyona aktarın. | Demo |
| [Midjourney Başlangıç Çerçevesi ile Kamera Engelleme](#case-2) | Kompakt bir hassas kamera tarifi: Blender kamera hareketini sağlar, Midjourney başlangıç karesini sağlar ve Seedance hareket referansını takip eder. | Demo |
| [ComfyUI Blender Ön İzleme ile Kamera Kontrolü](#case-3) | Hareket uyumunu test etmek için Blender previz'in ayrı dik ve baş aşağı referans çerçeveleriyle birleştirildiği bir ComfyUI kontrol durumu. | Demo |
| [Gerçekçi Başlangıç Çerçevesine Görüntüleme Önizlemesi](#case-4) | Kısa bir görüntü alanı önizleme eğitimi: sahneyi kapatın, önizlemeyi dışa aktarın, ilk kareyi gerçekçi hale getirin, ardından Seedance'ye her iki referansı da sağlayın. | Demo |
| [Tek Referans Videosu, Çoklu Dünya](#case-5) | Aynı Blender referans videosunun Seedance'de farklı oluşturulmuş dünyaları yönlendirdiği bir stil/dünya varyasyonu durumu. | Demo |
| [Diyaloğa senkron iPhone kamera previsuali](#case-29) | iPhone ile sürülen ve diyaloğa senkronlanan bir Blender kamera geçişi kullanın; ardından bu sesli previsuali ve iki görseli çekim planı için Seedance'a verin. | Integration |


<a id="character-action-blocking"></a>
### 🎬 Karakter ve Aksiyon Engelleme

| Case | Ne gösterir | Tür |
|---|---|---|
| [Eşleşen Pozlarla Çok Karakterli Diyalog](#case-6) | Seedance gerçekleştirilen sahneyi oluşturmadan önce karakter pozlarını ve kamera hareketini eşleştirmek için Blender'nin kullanıldığı bir diyalog çekimi iş akışı. | Demo |
| [Uzayda Elde Taşınabilir Takip Kamerası](#case-8) | Blender'nin bir karakterin uzayda nasıl seyahat ettiğini kontrol ettiği ve Seedance'nin cesur kamera hareketini son videoya taşıdığı, elde taşınır takip vakası. | Demo |
| [Taktik Eylem için Kamera ve Karakter Engelleme](#case-9) | Blender'nin kamera yörüngesini, lens seçimini, siper pozisyonlarını, silah sesi vuruşlarını ve karakter hareketini nesilden önce yönlendirdiği taktiksel bir engelleme durumu. | Demo |
| [Basit Kamera Hareketinin Ötesinde Pusu Sahnesi Öngörülüyor](#case-21) | Blender previs'in, Seedance çekimi oluşturmadan önce sahnelemeyi, zamanlamayı ve kamera hareketini nasıl çözebildiğini gösteren bir pusu sahnesi vakası. | Demo |
| [Engelli çatı parkur kovalamacası](#case-32) | Seedance eylemi düz bir koşuya indirgediğinde, engel etkileşimleri ve kaçınma vuruşları içeren bir Blender parkur previsuali kurun. | Demo |


<a id="agentic-blender-mcp"></a>
### 🤖 Ajan Blender MCP

| Case | Ne gösterir | Tür |
|---|---|---|
| [Codex + Blender MCP Referans Video İş Akışı](#case-10) | Codex'nin basit bir 3D pazar, kedi hareketi, kamera çerçevelemesi ve Seedance için bir MP4 referansı oluşturduğu etkili bir Blender MCP durumu. | Integration |
| [Codex-Yapı Mimarisi ve Kamera Çalışması](#case-11) | Mimarinin ve kamera çalışmasının Blender'de oluşturulduğu ve ardından Seedance referans hareketi olarak test edildiği, Codex destekli başlangıç seviyesi vakası. | Integration |
| [Claude-Dahili Blender MCP Dakikalar İçinde Ön Görünüm](#case-22) | Claude'nin iki ila üç dakika içinde bir atış referansı oluşturmak için Blender MCP'yi kullandığı hızlı bir ajansal ön izleme durumu. | Integration |
| [Fable skill'inin Codex'e taşınması](#case-34) | Bir agente Blender referans-video skill'ini kurdurun, bunu Codex'e taşıyın ve Seedance'ın hiç prompt olmadan hareketi temizleyip temizleyemediğini test edin. | Integration |


<a id="reference-prompt-multi-input-mapping"></a>
### 🧩 Referans, Bilgi İstemi ve Çoklu Giriş Eşleme

| Case | Ne gösterir | Tür |
|---|---|---|
| [Blender Referanslı Tekrarlanabilir Seedance İstemi](#case-13) | Birleştirilmiş bir tekrarlanabilirlik ve sorun giderme durumu: kurulum, referans video koşullarını açıklarken eşleştirilmiş test, kamera/ritim kontrolünün çalıştığı ve ayak hareketinin başarısız olduğu yerleri kaydeder. | Tutorial |
| [Mixamo Başlangıç Olarak Hareket Blender Referans](#case-14) | Yeni başlayanlar için uygun bir hareket kaynağı durumu: Referansı Seedance'ye göndermeden önce, kontrol edilebilir hareket tabanı olarak Blender'deki Mixamo hareketini kullanın. | Tutorial |
| [Daha Hızlı Bir Sahne için Yalnızca Konum Referans Kontrolü](#case-23) | Referans ağırlıklandırma durumu: İstemin hız ve dinamizmi geri kazanmasına izin verirken referansı pozisyonlar için yararlı tutun. | Tutorial |
| [3D Yazılımı Yerine Fiziksel Oyuncak Referansı](#case-24) | Fiziksel referans durumu: Blender'yi açmak çok fazla yük getirdiğinde oyuncakları hızlı hareket ve sahneleme referansları olarak kullanın. | Demo |
| [Belirli Başarısız Bir İstem Sahnesi için Referans Kontrolü](#case-26) | Bir kontrol geri dönüş durumu: Yalnızca bilgi istemi oluşturma başarısız olduğunda, bir miktar dinamizm azalmış olsa bile sahneyi zorlamak için bir referans kullanın. | Demo |
| [Karakter Oranı ve Basit Arka Plan İpuçları](#case-27) | Bir stabilite kontrol listesi örneği: karakter oranlarını yüksekliğin ötesinde eşleştirin ve hassas hizalama gerektirmeyen tüm arka planları basitleştirin. | Tutorial |
| [Stilize kare ile manken mocap](#case-35) | Zamanlamayı kilitlemek için sert bir Blender ya da manken hareket kaynağı kullanın; ardından giriş karesi tasarımıyla Seedance'ın nihai stilini ve kumaş davranışını yönlendirin. | Demo |


<a id="production-pipelines-toolchains"></a>
### 🛠️ Üretim Boru Hatları ve Takım Zincirleri

| Case | Ne gösterir | Tür |
|---|---|---|
| [Hermes, Krea, ComfyUI ve Blender MCP Yığın](#case-15) | Hermes'nin hem görüntü hem de fiziksel referanslar üretmek için Krea, ComfyUI, Blender MCP ve Seedance'yi kurup bağladığı çok araçlı bir aracı hattı. | Integration |
| [Blender MCP Seedance Stil Aktarımına Görünüm](#case-16) | Görüntü alanından stile aktarım durumu: Blender MCP kamera ve öğe kontrolü sağlar, ardından Seedance/Magnific doku ve aydınlatma ekler. | Integration |
| [Blender Anime Önizleme Seedance Oluşturma](#case-17) | Seedance oluşturma stilini değiştirirken kamera hareketlerinin ve hareketin nasıl korunabileceğini gösteren bir 3D anime öncesi durumu. | Integration |
| [FBX Claude-Anahtar Çerçeveli Kamerayla Kil Geçişi](#case-18) | Blender'nin hareketi içe aktardığı, Claude'nin ana kare kamera hareketlerine yardımcı olduğu ve oluşturulan geçişin Seedance referans videosu haline geldiği FBX kil geçiş iş akışı. | Integration |
| [Fable ile kurgulanmış dans referans hattı](#case-30) | Hareket yalnızca prompt ile kaba kalıyorsa, karakter tasarımını ve Blender koreografi kodunu bir agente bırakın ve 15 saniyelik dans referansını Seedance'a taşıyın. | Integration |


<a id="limits-tests-troubleshooting"></a>
### 🧪 Sınırlar, Testler ve Sorun Giderme

| Case | Ne gösterir | Tür |
|---|---|---|
| [Yalnızca Referans Blender Başlangıç Çerçevesi Olmadan Bloklama](#case-20) | Blender engellemenin yanı sıra ayrıntılı ortam referanslarının olduğunu gösteren, başlangıç çerçevesi olmayan bir varyant, iş akışı bir başlangıç çerçevesine dayanamadığında işe yarayabilir. | Limit |
| [Oyuncak Referans İstemi Takviyesi ve NG Örneği](#case-25) | Referans videolarının neden genellikle ham taklit yerine anında pekiştirmeye ihtiyaç duyduğunu gösteren bir sorun giderme örneği. | Limit |
| [Blender ve Seedance](#case-28) ile Kumaş Fiziği Stres Testi | Blender kılavuzlu Seedance'nin nerede çalışabileceğini ancak yine de zor hareketler için yinelenmesi gerektiğini gösteren bir kumaş fiziği stres testi. | Limit |
| [Siyah kareli keyframe zamanlama düzeltmesi](#case-31) | Kaba Blender referansı Seedance'ın robotik ara hareketleri kopyalamasına yol açıyorsa, ana pozları koruyun ve aradaki kareleri siyaha çevirin. | Tutorial |
| [Karmaşık sahnede hareket sapması testi](#case-33) | Kaba sahne MCP renderlarını bir limit testi olarak görün; karmaşık Blender sahneleri birden çok Seedance denemesinden sonra bile hedeflenen hareketten sapabilir. | Limit |



<a id="camera-control-previs-cases"></a>
## 🎥 Kamera Kontrolü ve Ön İzleme

<a id="case-1"></a>
### Case 1: [Blender Seedance Hareket Referansı Olarak Engelleme](https://x.com/noman23761/status/2071534020014563328) ([@noman23761](https://x.com/noman23761) ile)

**Birleştirilmiş yön iş akışı: Orijinal durumdaki tam gri kutu yöntemini kullanın, ardından Seedance oluşturmadan önce zamanlama, hız, sarsıntı ve mekansal koreografiyi önceden aksiyona aktarın.**

- Kaynak notları: Önceki durum 7 ile birleştirilmiştir: bu kaynaklar birlikte tam gri kutu iş akışını ve kaba zamanlama, hız, sarsıntı ve uzamsal koreografi ile aksiyon öncesi varyantını gösterir.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case1.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case1.mp4)

Tür: Demo | Tarih: 2026-06-29

---

<a id="case-2"></a>
### Case 2: [Midjourney Başlangıç Çerçevesi ile Kamera Engelleme](https://x.com/reidhannaford/status/2069074506849685773) (tarafından [@reidhannaford](https://x.com/reidhannaford))

**Kompakt, hassas bir kamera tarifi: Blender kamera hareketini sağlar, Midjourney başlangıç karesini sağlar ve Seedance hareket referansını takip eder.**

- Kaynak notları: Kaynak, üç adımlı net bir iş akışı sağlar ve oluşturulan videonun Blender kamera hareketini yakından takip ettiğini bildirir.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case2.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case2.mp4)

Tür: Demo | Tarih: 2026-06-22

---

<a id="case-3"></a>
### Case 3: [ComfyUI Blender Ön İzleme ile Kamera Kontrolü](https://x.com/JMSvid/status/2070258132840796579) (tarafından [@JMSvid](https://x.com/JMSvid))

**Hareket uyumunu test etmek için Blender previz'in ayrı dikey ve baş aşağı referans çerçeveleriyle birleştirildiği bir ComfyUI kontrol durumu.**

- Kaynak notları: Bu durum kullanışlıdır çünkü Blender ön izlemesini ComfyUI tarzı bir kontrol kurulumunda çoklu hareketsiz referanslarla birleştirir.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case3.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case3.mp4)

Tür: Demo | Tarih: 2026-06-25

---

<a id="case-4"></a>
### Case 4: [Gerçekçi Başlangıç Çerçevesine Görüntü Alanı Önizlemesi](https://x.com/DiabloNemesis/status/2070441923706503380) (tarafından [@DiabloNemesis](https://x.com/DiabloNemesis))

**Kısa bir görüntü alanı önizleme eğitimi: sahneyi kapatın, önizlemeyi dışa aktarın, ilk kareyi gerçekçi hale getirin ve ardından Seedance'ye her iki referansı da sağlayın.**

- Kaynak notları: Gönderi, somut eserler içeren kısa bir iş akışı sağlar: görünüm önizlemesi, ilk kare görüntüsü ve Seedance referans videosu. Yinelenen vaka 29 medyası kaldırıldı, böylece genel vaka aynı videonun yalnızca bir kopyasını gösteriyor.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case4.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case4.mp4)

Tür: Demo | Tarih: 2026-06-26

---

<a id="case-5"></a>
### Case 5: [Tek Referans Video, Çoklu Dünya](https://x.com/koldo2k/status/2071307945002815967) (tarafından: [@koldo2k](https://x.com/koldo2k))

**Aynı Blender referans videosunun Seedance'de farklı oluşturulmuş dünyaları yönlendirdiği bir stil/dünya varyasyonu durumu.**

- Kaynak notları: Kaynak, aynı referans videoyu kullanarak hareket kontrolünü dünya/tarz varyasyonundan ayırdığı için faydalıdır.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 5](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case5.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case5.mp4)

Tür: Demo | Tarih: 2026-06-28

---


<a id="case-29"></a>
### Case 29: [Diyaloğa senkron iPhone kamera previsuali](https://x.com/CoffeeVectors/status/2076397975853551924) (tarafından [@CoffeeVectors](https://x.com/CoffeeVectors))

**iPhone ile sürülen ve diyaloğa senkronlanan bir Blender kamera geçişi kullanın; ardından bu sesli previsuali ve iki görseli çekim planı için Seedance'a verin.**

- Kaynak notları: Kaynak, iPhone ile sürülen ve diyaloğa senkronlanan bir Blender kamerayı kullanıyor; ardından bu sesli previsuali iki durağan görselle birlikte Seedance 2'ye gönderiyor.
- Video önizlemesi:

[![Video önizlemesi — Case 29](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case29.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case29.mp4)

Tür: Integration | Tarih: 2026-07-12

---
<a id="character-action-blocking-cases"></a>
## 🎬 Karakter ve Aksiyon Engelleme

<a id="case-6"></a>
### Case 6: [Eşleşen Pozlarla Çok Karakterli Diyalog](https://x.com/reidhannaford/status/2069420552394043625) (tarafından: [@reidhannaford](https://x.com/reidhannaford))

** Seedance gerçekleştirilen sahneyi oluşturmadan önce karakter pozlarını ve kamera hareketini eşleştirmek için Blender'nin kullanıldığı bir diyalog çekimi iş akışı.**

- Kaynak notları: Kaynak, çok karakterli diyalog ve poz eşleştirmeyi ekleyerek onu tek karakterli kamera kontrolü demolarından farklı kılıyor.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 6](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case6.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case6.mp4)

Tür: Demo | Tarih: 2026-06-23

---

<a id="case-8"></a>
### Case 8: [Uzayda Elde Taşınabilir Takip Kamerası](https://x.com/reidhannaford/status/2070507963429671062) (tarafından: [@reidhannaford](https://x.com/reidhannaford))

**Blender'nin bir karakterin uzayda nasıl seyahat ettiğini kontrol ettiği ve Seedance'nin cesur kamera hareketini son videoya taşıdığı elde taşınan bir takip durumu.**

- Kaynak notları: Kamera takip ederken kaynak, karakteri sahnede hareket ettirir, bu da onu elde taşınır hareketli çekimler için faydalı kılar.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

Önizleme kullanılamıyor: Orijinal GitHub ekine artık herkes erişemez.

Tür: Demo | Tarih: 2026-06-26

---

<a id="case-9"></a>
### Case 9: [Taktik Eylem için Kamera ve Karakter Engelleme](https://x.com/SamJWasserman/status/2070742850095230991) (tarafından: [@SamJWasserman](https://x.com/SamJWasserman))

**Blender'nin kamera yörüngesini, lens seçimini, korunma konumlarını, silah sesleri ve karakter hareketlerini nesilden önce yönlendirdiği taktiksel bir engelleme durumu.**

- Kaynak notları: Kaynak, yalnızca kameraya yönelik basit bir referanstan daha güçlü olan eşzamanlı kamera ve karakter engellemeyi gösterir.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 9](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case9.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case9.mp4)

Tür: Demo | Tarih: 2026-06-27

---

<a id="case-21"></a>
### Case 21: [Basit Bir Kamera Hareketinin Ötesinde Pusu Sahnesi Ön Gösterimi](https://x.com/reidhannaford/status/2071595581508563168) (tarafından: [@reidhannaford](https://x.com/reidhannaford))

**Blender previs'in, Seedance çekimi oluşturmadan önce sahnelemeyi, zamanlamayı ve kamera hareketini nasıl çözebildiğini gösteren bir pusu sahnesi vakası.**

- Kaynak notları: Durum 21 olarak talep edildi. İş akışını basit bir kamera hareketinin ötesine, sahne hazırlamaya taşıdığı için ayrı bir Reid Hannaford örneği olarak tutuldu.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 21](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case21.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case21.mp4)

Tür: Demo | Tarih: 2026-06-29

---


<a id="case-32"></a>
### Case 32: [Engelli çatı parkur kovalamacası](https://x.com/moframe2026/status/2075203485604470965) (tarafından [@moframe2026](https://x.com/moframe2026))

**Seedance eylemi düz bir koşuya indirgediğinde, engel etkileşimleri ve kaçınma vuruşları içeren bir Blender parkur previsuali kurun.**

- Kaynak notları: Yazar, Blender parkur previsualini video referansı olarak kullandığını ve Blender'ın basit koşunun ötesine geçen engel kullanımı ile kaçınma akışını eklemek için gerekli olduğunu söylüyor.
- Video önizlemesi:

[![Video önizlemesi — Case 32](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case32.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case32.mp4)

Tür: Demo | Tarih: 2026-07-09

---
<a id="agentic-blender-mcp-cases"></a>
## 🤖 Ajan Blender MCP

<a id="case-10"></a>
### Case 10: [Codex + Blender MCP Referans Video İş Akışı](https://x.com/akiyoshisan/status/2071081230108660199) (tarafından [@akiyoshisan](https://x.com/akiyoshisan))

**Codex'nin basit bir 3D pazar, kedi hareketi, kamera çerçevelemesi ve Seedance için bir MP4 referansı oluşturduğu etkili bir Blender MCP durumu.**

- Kaynak notları: Yazar, testin başka bir yaratıcıdan ilham aldığını ancak açıklanan sahne, hareket, kamera ve dışa aktarma sürecinin kendi deneyleri olduğunu söylüyor.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 10](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case10.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case10.mp4)

Tür: Integration | Tarih: 2026-06-28

---

<a id="case-11"></a>
### Case 11: [Codex-Yapı Mimarisi ve Kamera Çalışması](https://x.com/6_KAKUU/status/2071051063663452374) (tarafından: [@6_KAKUU](https://x.com/6_KAKUU))

**Mimari ve kamera çalışmasının Blender'de oluşturulduğu ve ardından Seedance referans hareketi olarak test edildiği, Codex destekli başlangıç seviyesi vakası.**

- Kaynak notları: Gönderi, yeni başlayan bir Codex iş akışı olarak değerlidir: kullanıcı, mimariyi ve kamera çalışmasını Seedance'den önce Codex'ye devreder.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 11](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case11.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case11.mp4)

Tür: Integration | Tarih: 2026-06-28

---

<a id="case-22"></a>
### Case 22: [Claude-Built Blender MCP Dakikalar İçinde Ön Görünüm](https://x.com/JoshDaws/status/2071401550845481090) (tarafından: [@JoshDaws](https://x.com/JoshDaws))

**Claude'nin iki ila üç dakika içinde bir atış referansı oluşturmak için Blender MCP'yi kullandığı hızlı bir ajansal ön izleme durumu.**

- Kaynak notları: Durum 22 olarak talep edildi. Manuel Blender çalışması yerine hız ve aracı kontrolünü gösterdiği için tutuldu.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 22](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case22.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case22.mp4)

Tür: Integration | Tarih: 2026-06-29

---


<a id="case-34"></a>
### Case 34: [Fable skill'inin Codex'e taşınması](https://x.com/mugi_AI_Art/status/2074259600342163846) (tarafından [@mugi_AI_Art](https://x.com/mugi_AI_Art))

**Bir agente Blender referans-video skill'ini kurdurun, bunu Codex'e taşıyın ve Seedance'ın hiç prompt olmadan hareketi temizleyip temizleyemediğini test edin.**

- Kaynak notları: Yazar, Fable'ın Blender referans-video skill'i oluşturmasını sağladı, bunu Codex'e taşıdı ve kaba modellenmiş referanslardan prompt kullanmadan Seedance üretimi yaptı.
- Video önizlemesi:

[![Video önizlemesi — Case 34](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case34.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case34.mp4)

Tür: Integration | Tarih: 2026-07-06

---
<a id="reference-prompt-multi-input-mapping-cases"></a>
## 🧩 Referans, Bilgi İstemi ve Çoklu Giriş Eşleme

<a id="case-13"></a>
### Case 13: [Blender Referanslı Tekrarlanabilir Seedance İstemi](https://x.com/aidoga_lab/status/2070864815275585913) (tarafından [@aidoga_lab](https://x.com/aidoga_lab))

**Birleşik bir tekrarlanabilirlik ve sorun giderme durumu: kurulum, referans video koşullarını açıklarken eşleştirilmiş test, kamera/ritim kontrolünün çalıştığı ve ayak hareketinin başarısız olduğu yerleri kaydeder.**

- Kaynak notları: Önceki durum 19 ile birleştirilmiştir: çift hem tekrarlanabilir kurulumu hem de ayak kaymasıyla ilgili sınırlama notunu korur.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case13.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.mp4)

![Referans görseli — Case 13](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case13.jpg)

Tür: Tutorial | Tarih: 2026-06-27

---

<a id="case-14"></a>
### Case 14: [Mixamo Başlangıç Olarak Hareket Blender Referans](https://x.com/tanabe_fragm/status/2070685291183243459) (tarafından [@tanabe_fragm](https://x.com/tanabe_fragm))

**Yeni başlayanlar için uygun bir hareket kaynağı örneği: Referansı Seedance'ye göndermeden önce kontrol edilebilir hareket tabanı olarak Blender'deki Mixamo hareketini kullanın.**

- Kaynak notları: Kaynak, yeni başlayanlar için faydalıdır çünkü Mixamo'yi Blender referans videoları için pratik bir hareket kaynağı olarak adlandırır.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 14](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case14.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case14.mp4)

Tür: Tutorial | Tarih: 2026-06-27

---

<a id="case-23"></a>
### Case 23: [Daha Hızlı Bir Sahne için Yalnızca Konum Referans Kontrolü](https://x.com/kan_mi_no9/status/2071380621214224403) (tarafından [@kan_mi_no9](https://x.com/kan_mi_no9))

**Referans ağırlıklandırma durumu: Referansın konumlar için yararlı olmasını sağlarken, istemin hız ve dinamizmi geri kazanmasına izin verin.**

- Kaynak notları: Durum 23 olarak talep edildi. Ayrı bir referans-kontrol değişkeni olarak eşleştirilmiş kan_mi_no9 testiyle tutuldu.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 23](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case23.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case23.mp4)

Tür: Tutorial | Tarih: 2026-06-28

---

<a id="case-24"></a>
### Case 24: [3D Yazılımı Yerine Fiziksel Oyuncak Referansı](https://x.com/gcduncombe/status/2070617538745229546) (tarafından [@gcduncombe](https://x.com/gcduncombe))

**Fiziksel referans durumu: Blender'yi açmak çok fazla yük getirdiğinde oyuncakları hızlı hareket ve sahneleme referansları olarak kullanın.**

- Kaynak notları: Durum 24 olarak talep edildi. Referans video fikrini yalnızca yazılım ön incelemesinin ötesine genişlettiği için tutuldu.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 24](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case24.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case24.mp4)

Tür: Demo | Tarih: 2026-06-26

---

<a id="case-26"></a>
### Case 26: [Belirli Başarısız Bir İstem Sahnesi için Referans Kontrolü](https://x.com/kan_mi_no9/status/2071168235022827587) (tarafından [@kan_mi_no9](https://x.com/kan_mi_no9))

**Kontrol için geri dönüş durumu: Yalnızca bilgi istemi oluşturma başarısız olduğunda, bir miktar dinamizm azalsa bile sahneyi zorlamak için bir referans kullanın.**

- Kaynak notları: Durum 26 olarak talep edildi. Daha sonraki kan_mi_no9 varyasyon durumunun pratik karşılığı olarak tutuldu.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 26](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case26.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case26.mp4)

Tür: Demo | Tarih: 2026-06-28

---

<a id="case-27"></a>
### Case 27: [Karakter Oranı ve Basit Arka Plan İpuçları](https://x.com/craftcapitallab/status/2070512271391068287) (tarafından [@craftcapitallab](https://x.com/craftcapitallab))

**Bir stabilite kontrol listesi örneği: karakter oranlarını yüksekliğin ötesinde eşleştirin ve hassas hizalama gerektirmeyen tüm arka planları basitleştirin.**

- Kaynak notları: Durum 27 olarak talep edildi. Özel, yeniden kullanılabilir kurulum önerileri sunduğu için tutuldu.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 27](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case27.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case27.mp4)

Tür: Tutorial | Tarih: 2026-06-26

---


<a id="case-35"></a>
### Case 35: [Stilize kare ile manken mocap](https://x.com/fatboypink/status/2074087401887039740) (tarafından [@fatboypink](https://x.com/fatboypink))

**Zamanlamayı kilitlemek için sert bir Blender ya da manken hareket kaynağı kullanın; ardından giriş karesi tasarımıyla Seedance'ın nihai stilini ve kumaş davranışını yönlendirin.**

- Kaynak notları: Yazar, sert manken mocap'inin hareket zamanlamasını verdiğini; elde çizilmiş giriş karesinin ise Seedance'ı istenen stil ve kumaş hareketine doğru ittiğini söylüyor.
- Video önizlemesi:

[![Video önizlemesi — Case 35](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case35.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case35.mp4)

Tür: Demo | Tarih: 2026-07-06

---
<a id="production-pipelines-toolchains-cases"></a>
## 🛠️ Üretim Boru Hatları ve Takım Zincirleri

<a id="case-15"></a>
### Case 15: [Hermes, Krea, ComfyUI ve Blender MCP Stack](https://x.com/SamJWasserman/status/2069656428437225826) (tarafından [@SamJWasserman](https://x.com/SamJWasserman))

**Hermes'nin hem görüntü hem de fiziksel referanslar üretmek için Krea, ComfyUI, Blender MCP ve Seedance'yi yükleyip bağladığı çok araçlı bir aracı hattı.**

- Kaynak notları: Vaka, yalnızca manuel Blender previs'i değil, aracı tarafından oluşturulmuş daha geniş bir yaratıcı yığını göstermektedir.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 15](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case15.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case15.mp4)

Tür: Integration | Tarih: 2026-06-24

---

<a id="case-16"></a>
### Case 16: [Blender MCP Seedance Stil Aktarımına Görünüm](https://x.com/techhalla/status/2070814203435274715) (tarafından [@techhalla](https://x.com/techhalla))

**Görüntü alanından stile aktarım durumu: Blender MCP kamera ve öğe kontrolü sağlar, ardından Seedance/Magnific doku ve aydınlatma ekler.**

- Kaynak notları: Bu daha güçlü bir techhalla kaynağıdır çünkü görüntü alanı animasyonunu ve aşağı akış stili/ışıklandırma adımını açıklar.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 16](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case16.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case16.mp4)

Tür: Integration | Tarih: 2026-06-27

---

<a id="case-17"></a>
### Case 17: [Blender Anime Önizleme Seedance Oluşturma](https://x.com/restofart/status/2070086939756159368) (tarafından: [@restofart](https://x.com/restofart))

** Seedance oluşturma stilini değiştirirken kamera hareketlerinin ve hareketin nasıl korunabileceğini gösteren 3D anime öncesi durumu.**

- Kaynak notları: Kaynak, iş akışını doğrudan Blender 3D previz'in kamera hareketini korurken bir anime render'a dönüştürülmesiyle çerçeveliyor.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 17](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case17.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case17.mp4)

Tür: Integration | Tarih: 2026-06-25

---

<a id="case-18"></a>
### Case 18: [FBX Claude-Anahtar Çerçeveli Kamera ile Kil Geçişi](https://x.com/Viggle_PINOC/status/2070183934265012392) (tarafından: [@Viggle_PINOC](https://x.com/Viggle_PINOC))

**Blender'nin hareketi içe aktardığı, Claude'nin ana kare kamera hareketlerine yardımcı olduğu ve oluşturulan geçişin Seedance referans videoya dönüştüğü FBX kil geçiş iş akışı.**

- Kaynak notları: Kaynak, belirli bir FBX-kilden geçiş sürecini verir ve referans dışa aktarımından önce kamera anahtar karesini içerir.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 18](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case18.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case18.mp4)

Tür: Integration | Tarih: 2026-06-25

---


<a id="case-30"></a>
### Case 30: [Fable ile kurgulanmış dans referans hattı](https://x.com/ryo05m/status/2076284841457521043) (tarafından [@ryo05m](https://x.com/ryo05m))

**Hareket yalnızca prompt ile kaba kalıyorsa, karakter tasarımını ve Blender koreografi kodunu bir agente bırakın ve 15 saniyelik dans referansını Seedance'a taşıyın.**

- Kaynak notları: Yazar üç adımı açıkça veriyor: karakter için Seedream 5 Pro, 15 saniyelik manken dansı için Blender ve hareket ile kamera referansı için Seedance 2.0.
- Video önizlemesi:

[![Video önizlemesi — Case 30](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case30.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case30.mp4)

Tür: Integration | Tarih: 2026-07-12

---
<a id="limits-tests-troubleshooting-cases"></a>
## 🧪 Sınırlar, Testler ve Sorun Giderme

<a id="case-20"></a>
### Case 20: [Yalnızca Referans Blender Başlangıç Çerçevesi Olmadan Bloklama](https://x.com/magneticskiff/status/2070711034793361559) (tarafından [@magneticskiff](https://x.com/magneticskiff))

**İş akışının bir başlangıç çerçevesine dayanamadığı durumlarda Blender engellemenin yanı sıra ayrıntılı ortam referanslarının işe yarayabileceğini gösteren başlangıç çerçevesi olmayan bir değişken.**

- Kaynak notları: Bu durum, referans görüntülerinin olağan başlangıç karesi bağımlılığının yerini aldığı önemli bir değişkeni kapsamaktadır.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 20](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case20.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case20.mp4)

Tür: Limit | Tarih: 2026-06-27

---

<a id="case-25"></a>
### Case 25: [Oyuncak Referans İstemi Takviyesi ve NG Örneği](https://x.com/tea_story_hoshi/status/2071002538703479089) (tarafından [@tea_story_hoshi](https://x.com/tea_story_hoshi))

**Referans videoların neden genellikle ham taklit yerine anında pekiştirmeye ihtiyaç duyduğunu gösteren bir sorun giderme örneği.**

- Kaynak notları: Durum 25 olarak talep edildi. Hem çalışma örneklerini hem de başarısız bir karşılaştırmayı içerdiği için tutuldu.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 25](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case25.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case25.mp4)

Tür: Limit | Tarih: 2026-06-27

---

<a id="case-28"></a>
### Case 28: [Blender ve Seedance ile Kumaş Fiziği Stres Testi](https://x.com/fatboypink/status/2070577334701473800) (tarafından [@fatboypink](https://x.com/fatboypink))

**Blender kılavuzlu Seedance'nin nerede çalışabileceğini ancak yine de zor hareketler için yinelenmesi gerektiğini gösteren kumaş fiziği stres testi.**

- Kaynak notları: Durum 28 olarak talep edildi. Somut bir sınırlama/stres testi durumu olarak tutuldu.
- Denetim durumu: manuel kopya ve özgünlük incelemesinden sonra tutulur.
- Video önizlemesi:

[![Demo videosunu oynat — Case 28](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case28.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case28.mp4)

Tür: Limit | Tarih: 2026-06-26

---

<a id="related-repositories"></a>
## 🔗 İlgili Depolar

- [Seedance 2.0 promptlarını inceleyin](https://github.com/Evolink-AI/awesome-seedance-2.0-prompts)
- [Seedance 2 ajan skill'ini yükleyin](https://github.com/Evolink-AI/seedance2-video-gen-skill-for-openclaw)
- [GPT Image 2'den Seedance 2'ye iş akışını keşfedin](https://github.com/Evolink-AI/GPT-Image-2-Seedance2-Workflow)


<a id="case-31"></a>
### Case 31: [Siyah kareli keyframe zamanlama düzeltmesi](https://x.com/thechriscooper/status/2076092824102240411) (tarafından [@thechriscooper](https://x.com/thechriscooper))

**Kaba Blender referansı Seedance'ın robotik ara hareketleri kopyalamasına yol açıyorsa, ana pozları koruyun ve aradaki kareleri siyaha çevirin.**

- Kaynak notları: Yazar, Seedance'ın kaba Blender animasyonunu fazla kelimesi kelimesine kopyaladığını; keyframe-siyah-keyframe düzeninin ise blocking'i koruyup hareketi yumuşattığını söylüyor.
- Video önizlemesi:

[![Video önizlemesi — Case 31](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case31.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case31.mp4)

Tür: Tutorial | Tarih: 2026-07-11

---

<a id="case-33"></a>
### Case 33: [Karmaşık sahnede hareket sapması testi](https://x.com/sonicpower1970/status/2074322339391824012) (tarafından [@sonicpower1970](https://x.com/sonicpower1970))

**Kaba sahne MCP renderlarını bir limit testi olarak görün; karmaşık Blender sahneleri birden çok Seedance denemesinden sonra bile hedeflenen hareketten sapabilir.**

- Kaynak notları: Bu devam gönderisi, yazarın Claude→Blender→Seedance testinde yaklaşık dört denemeden sonra bile karmaşık sahnelerin hedeflenen hareketi yakalayamadığını bildiriyor.
- Video önizlemesi:

[![Video önizlemesi — Case 33](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/posters/case33.jpg)](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/github-repo-media/Awesome-Blender-Seedance-Workflow-Usecases/media/case33.mp4)

Tür: Limit | Tarih: 2026-07-07

---
<a id="acknowledge"></a>
## 🙏 Teşekkür

Bu depo, Blender + Seedance iş akışlarını, testleri, istemleri, referans videolarını ve üretim notlarını herkese açık olarak paylaşan yaratıcılardan ilham almıştır.

[@noman23761](https://x.com/noman23761), [@reidhannaford](https://x.com/reidhannaford), [@JMSvid](https://x.com/JMSvid), [@DiabloNemesis](https://x.com/DiabloNemesis), [@koldo2k](https://x.com/koldo2k), [@SamJWasserman](https://x.com/SamJWasserman), [@akiyoshisan](https://x.com/akiyoshisan), [@6_KAKUU](https://x.com/6_KAKUU), [@aidoga_lab](https://x.com/aidoga_lab), [@tanabe_fragm](https://x.com/tanabe_fragm), [@techhalla](https://x.com/techhalla), [@restofart](https://x.com/restofart), [@Viggle_PINOC](https://x.com/Viggle_PINOC), [@magneticskiff](https://x.com/magneticskiff), [@JoshDaws](https://x.com/JoshDaws), [@kan_mi_no9](https://x.com/kan_mi_no9), [@gcduncombe](https://x.com/gcduncombe), [@tea_story_hoshi](https://x.com/tea_story_hoshi), [@craftcapitallab](https://x.com/craftcapitallab), [@fatboypink](https://x.com/fatboypink)

*Her vakanın orijinal yaratıcıya atfedildiğini garanti edemeyiz. Düzeltilmesi gereken bir şey varsa lütfen bizimle iletişime geçin, biz de güncelleyeceğiz.*

Eklemeniz gereken bir Blender + Seedance iş akışınız mı var? [Sorun şablon dosyası](.github/ISSUE_TEMPLATE/use-case.yml) ile [bir kullanım senaryosu sorunu açın](https://github.com/Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases/issues/new?template=use-case.yml) veya [PR şablonu](.github/PULL_REQUEST_TEMPLATE.md) ile bir çekme isteği açın.

[![Yıldız Geçmişi Tablosu](https://api.star-history.com/svg?repos=Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&type=Date)](https://www.star-history.com/#Evolink-AI/Awesome-Blender-Seedance-Workflow-Usecases&Date)
