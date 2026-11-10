---
name: token-ekonomisi
description: Claude Code'da token ve maliyeti düşürür. İşi basit/orta/zor diye sınıflar, haiku/sonnet/opus seçer, alt ajanı ne zaman açacağını ve bağlamı nasıl temiz tutacağını söyler. "token", "maliyet", "hangi model", "ucuz çalış", "alt ajan", "Game Studios pahalı" denince kullan.
argument-hint: "[yapılacak iş]"
---

# Token ekonomisi

Amaç: **aynı kaliteyi daha az token ile almak.** Önce işi sınıfla, sonra modeli ve yöntemi seç, sonra tek satırla söyle. Bu dosyayı kısa tuttum; ayrıntılı tablo için `model-matrisi.md`'yi yalnız emin olamadığında oku.

## 1. İşi sınıfla

| Sınıf | Ölçüt |
|---|---|
| **Basit** | Cevap dosyada/komut çıktısında zaten var, karar gerekmiyor, yanlışı hemen fark edilir |
| **Orta** | Birkaç dosya, bilinen kalıp, net kabul ölçütü ve doğrulayan bir test var |
| **Zor** | Gereksinim belirsiz, kök neden bilinmiyor, çok sistem birbirine değiyor ya da geri dönüşü pahalı |

Birden fazla sınıfa uyuyorsa **yükseğini** al. Emin değilsen `sonnet`'le başla.

## 2. Modeli seç

| Sınıf | Model | Örnek |
|---|---|---|
| Basit | `haiku` | arama, listeleme, test çalıştırıp hataları özetleme, biçimlendirme, değişiklik günlüğü taslağı |
| Orta | `sonnet` | tek özellik, 1–3 dosyalık hata düzeltme, test yazma, tasarım belgesi, rutin kod incelemesi |
| Zor | `opus` | mimari karar, kök nedeni bilinmeyen hata, güvenlik, denge/ekonomi tasarımı, kapsam kesme |

Zor işte **plan `opus`, uygulama `sonnet`**: `/model opusplan` plan modunda Opus'u, uygulamada Sonnet'i kullanır. Plan yazılı olmazsa devir kayıp verir; kök nedeni ve adımları dosyaya yazdır.

## 3. Modeli nasıl değiştirirsin

Oturum modelini **sen değiştiremezsin**; kullanıcı `/model` ile değiştirir. Yapabileceğin üç şey var:

1. Kullanıcıya söyle: "Bu iş orta, `/model sonnet` yeter."
2. İşi **alt ajana** ver ve Agent aracını çağırırken `model` parametresine takma adı yaz (`haiku`, `sonnet`, `opus`). Bu parametre ajan tanımındaki `model:` alanından ve ortam değişkenlerinden önce gelir.
3. Sık yapılan iş için `.claude/agents/<ad>.md` içine `model:` yazdır. `ajanlar/` klasöründe iki hazır örnek var (`tarayici`, `test-kosucu`). Ucuz tarama için kendi ajanını tanımla: yerleşik **Explore alt ajanı Haiku değildir**, ana oturumun modelini kullanır.

Bir skill'in frontmatter'ındaki `model:` yalnız **o turu** etkiler ve ayara kaydedilmez.

## 4. Alt ajan: ne zaman aç, ne zaman açma

Alt ajanın **ayrı bağlamı ve ayrı faturası** var. Ana bağlamı temiz tutar (ham çıktı girmez, özet döner) ve işi ucuz modele taşır. Ama her biri kendi başlangıcını yükler: küçük iş için açmak toplamda pahalıdır.

- **Aç:** çok dosyada arama, uzun test/derleme çıktısı, bağımsız 3+ kaynak taraması, taze gözle inceleme.
- **Açma:** tek dosyalık küçük düzenleme, çıktısı sonrakinin girdisi olan adımlar.
- Alt ajana görevi **tam yaz**: amaç, nereye bakacağı, ne döndüreceği ("en fazla 15 satır, `dosya:satır`").
- Paralel alt ajan **hız** içindir, tasarruf için değil. Üç alt ajan üç ayrı bağlamdır.

## 5. Bağlamı temiz tut

- Görev bitince `/clear` (bedava, sayaç sıfırlanır). Aynı oturumda ilgisiz ikinci işe geçme.
- Uzun görevde `/compact <ne korunsun>`; `/context` ile neyin yer kapladığına bak.
- Dosyayı baştan sona okutma: önce `Grep`, sonra satır aralığı. Uzun çıktıyı dosyaya yazdırıp `tail`/`grep` ile oku.
- Aynı dosyayı tekrar okutma; öğrendiğini bir satırla not al.
- `CLAUDE.md` 200 satırın altında kalsın; uzun iş akışlarını skill'e taşı.
- Basit işte `/effort low`, zor işte `high` dene; çoğu 5.x modelde varsayılan `medium`.

## 6. Claude Code Game Studios'a özel

Deponun kendi README'sine göre:

- 3 direktör `opus`, `lead-programmer` ve 15 uzman `sonnet` ister; **kalan 30 ajan oturumun modelini devralır** (`inherit`). Oturumu `opus`'ta tutarsan o 30 ajan da `opus`'ta çalışır. Günlük oturumu `sonnet`'te tut.
- `project.yaml` içinde `modes.rigor` varsayılan `minimal`. Yükseltmeden önce gerçekten gerekli mi bak: deponun kendi ölçümünde 30 belge yazan `standard` sürüm kör değerlendirmede son çıktı.
- Direktör incelemesi pahalıdır (Opus). Kişisel olarak azalt: `/project-settings --local modes.review_mode=solo`.
- `team-*` komutları (`/team-combat`, `/team-ui`, `/team-release`…) birkaç ajanı birden çalıştırır. Bunları bilinçli kullan; küçük işte tek ajanlı komutlar yeter.
- `/prototype` hafif yoldur. Stüdyo modunu oyun büyüyünce aç.

## 7. Yükseltme kuralları

1. Aynı iş bir modelde **iki denemede** düzelmediyse bir üst modele geç; üçüncü denemeyi aynı modelde yapma.
2. Yükseltmeden önce işi **ikiye böl** ve kabul ölçütünü yaz; sorun çoğu zaman modelden değil işin büyüklüğünden gelir.
3. Veri silme, kayıt formatı, güvenlik, yayın gibi geri dönüşü pahalı işlerde tasarruf yapma: `opus` kullan, sonucu insan gözüyle doğrula.
4. `haiku`'ya birden çok dosyayı tutarlı düzenleme, belirsiz gereksinim ve yargı işi verme.

## 8. Cevabın biçimi

Bir iş alırken **tek satır** yaz, uzatma:

`Sınıf: orta → sonnet, alt ajan yok (tek dosya). Sonra testleri haiku ajanıyla koştururum.`

Kullanıcı itiraz etmezse devam et. İş bittiğinde `/clear` öner.
