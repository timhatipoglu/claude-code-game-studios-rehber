# Model matrisi: hangi iş hangi modele

SKILL.md'deki üçlü ayrımın ayrıntısı. Yalnız model seçerken emin olamadığında oku.

Model adları takma ad olarak yazıldı (`haiku`, `sonnet`, `opus`). Hangi sürüme çözüldüklerini ve fiyatları Anthropic'in güncel model/fiyat sayfasından kontrol et; bu dosyada rakam yok, çünkü rakamlar değişir. Sıralama sabit: **Haiku en ucuz ve hızlı, Opus en güçlü ve en pahalı, Sonnet ikisinin arası.**

## Önce işi ölç: üç soru

| Soru | Evet ise |
|---|---|
| Cevap dosyada ya da komut çıktısında zaten var mı, benden karar beklenmiyor mu? | **Basit** |
| Birkaç dosya, bilinen bir kalıp, net bir kabul ölçütü ve bir test var mı? | **Orta** |
| Gereksinim belirsiz, kök neden bilinmiyor, birçok sistem birbirine değiyor ya da geri dönüşü pahalı mı? | **Zor** |

Birden fazla "evet" çıkarsa **yüksek olanı** seç. İki sorudan emin değilsen **Sonnet** ile başla, kötü giderse yükselt (aşağıda).

## 1. Kod

| Düzey | İş | Model |
|---|---|---|
| Basit | Dosya/sembol arama, "bu fonksiyon nerede çağrılıyor", import düzeltme, yeniden adlandırma, biçimlendirme, yorum satırı, commit mesajı taslağı, tek satırlık sabit değer değişikliği | `haiku` |
| Basit | Test/derleme çalıştır, yalnız **hatalı satırları** özetle | `haiku` |
| Orta | Tek dosyalık özellik, bilinen kalıpla yeni bileşen, 1–3 dosyalık hata düzeltme (yeniden üretilebilir), test yazma, küçük yeniden düzenleme, rutin kod incelemesi | `sonnet` |
| Zor | Mimari karar, çok dosyalı/çok sistemli değişiklik, kök nedeni bilinmeyen hata, eşzamanlılık, performans darboğazı, güvenlik incelemesi, "hangi yaklaşım" tartışması | `opus` |
| Zor | Oyun motoru seçimi, kayıt/oyun durumu mimarisi, ağ/eşitleme tasarımı | `opus` |

Oyun örnekleri: "karakter hızını 5'ten 6'ya çıkar" basit; "zıplamaya koyote süresi ekle ve test yaz" orta; "kayıt sistemini sürüm geçişli hâle getir, eski kayıtlar bozulmasın" zor.

## 2. Araştırma

| Düzey | İş | Model |
|---|---|---|
| Basit | Bir kütüphanenin sürümü/lisansı/komutu, tek sayfa belge okuyup özetle, depoda şu ayarı bul | `haiku` |
| Orta | 3–5 kaynağı karşılaştır (motor seçenekleri, eklentiler), bir hatanın bilinen çözümlerini tara, rakip oyunların bir mekaniğini özetle | `sonnet` |
| Zor | Birçok kaynağı **çelişkileriyle** birlikte sentezle, karar önerisi yaz, tarafsız karşılaştırma tablosu ve kaynak doğrulaması | `opus` |

Geniş araştırma deseni: **tarama ucuz, sentez pahalı.** Kaynakları alt ajanlarla `haiku`/`sonnet`'le tara (her biri kendi bağlamında okur, ana bağlama kısa özet döner), sonunda yalnız özetleri `opus`'a ver. Ham sayfaları ana bağlama yığma.

Araştırma sonuçlarında rakamı kaynağında doğrula; "model dedi" kaynak değildir.

## 3. Oyun tasarımı ve belge

| Düzey | İş | Model |
|---|---|---|
| Basit | Şablonu doldur, bölüm başlıklarını denetle, belge arasında tutarlı isim/sayı kontrolü, sürüm notu ve değişiklik günlüğü taslağı | `haiku` |
| Orta | Tek sistem tasarım belgesi, görev/hikâye yazımı, sprint planı, hata raporu sınıflama, test planı | `sonnet` |
| Zor | Oyunun çekirdek döngüsü ve hissi, ekonomi/denge, sistemler arası çelişkiyi çözme, kapsam kesme kararı, "bu oyun eğlenceli mi" yargısı | `opus` |

Denge ve his işi **ölçümle** desteklenmediği sürece model fikrinden ibarettir. Karar vermeden önce oynayıp ekran görüntüsü/sayı topla; hangi model olursa olsun tahmin değil kanıt iste.

## 4. QA ve test

| Düzey | İş | Model |
|---|---|---|
| Basit | Testleri koştur, geçti/kaldı say, ekran görüntüsünün klasörde olup olmadığını denetle | `haiku` |
| Orta | Test senaryosu ve regresyon listesi yazma, hata ayıklama, tekrarlanabilirlik adımları çıkarma | `sonnet` |
| Zor | Aralıklı (flaky) testin kök nedeni, çok oyunculu/zamanlama hataları, "test geçiyor ama oyun bozuk" durumları | `opus` |

## 5. Metin, ses, sanat yönergesi

| Düzey | İş | Model |
|---|---|---|
| Basit | Metin düzeltme, yerelleştirme tablosu doldurma, ad listesi, kısa diyalog varyasyonu | `haiku` |
| Orta | Karakter/diyalog yazımı, görev metni, mağaza sayfası metni, ses efekti listesi | `sonnet` |
| Zor | Anlatı yapısı, sanat yönergesi (bir bütün olarak tutarlı görünüm), ton kararı | `opus` |

## 6. Üretim ve yönetim

| Düzey | İş | Model |
|---|---|---|
| Basit | Durum raporu, açık iş sayımı, kontrol listesi işaretleme | `haiku` |
| Orta | Sprint planı, tahmin, retrospektif özeti, risk listesi | `sonnet` |
| Zor | Kapsam/tarih çatışması, yayın kararı, birden çok ekibin önceliği çatıştığında karar | `opus` |

## Yükseltme ve düşürme kuralları

1. **Yükselt:** Aynı iş `haiku`/`sonnet`'te **iki denemede** düzelmediyse bir üst modele geç. Üçüncü denemeyi aynı modelde yapma.
2. **Önce işi parçala:** Başarısızlık çoğu zaman modelden değil, işin büyüklüğünden gelir. Yükseltmeden önce görevi ikiye böl ve kabul ölçütünü yaz.
3. **Plan pahalı, uygulama ucuz:** Zor işte `opus` ile planı ve kök nedeni **yazdır**, uygulamayı `sonnet`'e ver. Plan yazılı olmazsa devir kayıp verir.
4. **Düşür:** Bir `opus` oturumu rutine döndüyse (biçimlendirme, tekrar eden düzenleme, test çalıştırma) oturumu `sonnet`'e al ya da işi alt ajana ver.
5. **Yanlışı pahalıya alma:** Veri silme, kayıt formatı, güvenlik ve yayın gibi geri dönüşü pahalı işlerde model tasarrufu yapma, `opus`'ta kal ve sonucu insan gözüyle doğrula.
6. **`haiku` sınırı:** Birden çok dosyayı tutarlı düzenleme, belirsiz gereksinim ve yargı gerektiren iş `haiku`'ya verilmez; sonuç hızlı ama yanlış olur ve düzeltmek daha pahalıya çıkar.

## Alt ajan ne zaman kazandırır, ne zaman kaybettirir

Alt ajanın **ayrı bağlamı ve ayrı faturası** var. Kazandırdığı iki şey: ana bağlamı temiz tutar (ham çıktı ona girmez, yalnız özet döner) ve görevi ucuz modele taşır. Kaybettirdiği: her alt ajan kendi başlangıç bağlamını yükler, bu yüzden küçük bir iş için alt ajan açmak **toplamda daha pahalıdır**.

| Durum | Karar |
|---|---|
| Çok dosyada arama/okuma, yalnız sonuç gerekli | Alt ajan (`haiku`) |
| Uzun test/derleme çıktısı, yalnız hatalar gerekli | Alt ajan (`haiku`) |
| Birbirinden bağımsız 3+ kaynak taraması | Paralel alt ajanlar (`haiku`/`sonnet`), sentez ana oturumda |
| Taze gözle inceleme (yazanın körlüğü olmasın) | Alt ajan (`sonnet`) |
| Tek dosyada küçük düzenleme | Alt ajan **açma**, doğrudan yap |
| Birbirine bağımlı adımlar (çıktı sonrakinin girdisi) | Alt ajan **açma**, aynı bağlamda ilerle |

Alt ajana görevi **tam** yaz: amaç, bakacağı yer, ne döndüreceği ("en fazla 15 satır, dosya yolu + satır no"). Kısa ve net bir görev hem ucuz hem doğru sonuç verir.
