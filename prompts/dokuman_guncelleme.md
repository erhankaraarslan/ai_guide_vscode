# dokuman_guncelleme.md

## Amaç
Bu dokümanın amacı, bir yapay zeka asistanının Visual Studio Code GitHub Copilot resmi dokümantasyonunu kaynak alarak:

1. İlk çalıştırmada `docs/copilot` altındaki tüm resmi dokümanları toplayıp Türkçeye çevirmesi,
2. Sonraki çalıştırmalarda yalnızca yeni eklenen veya değişen dokümanları işlemesi,
3. Yeni gelen dokümanların Türkçe sürümlerini eklemesi,
4. Değişen mevcut dokümanların Türkçe sürümlerini güncellemesi,
5. Her çalıştırmada tüm yenilikleri ve değişiklikleri tek bir bülten dosyasında özetlemesi,
6. Tüm süreci tekrarlanabilir, denetlenebilir ve bozulmaya dayanıklı şekilde yürütmesidir.

Bu dosya, yapay zekanın her seferinde aynı talimatları tekrar istemeden aynı kurallarla çalışmasını sağlayan kalıcı çalışma spesidir.

---

## Resmi kaynak
Birincil kaynak depo:
- `https://github.com/microsoft/vscode-docs`

İzlenecek ana klasör:
- `docs/copilot/`

Yayın görünümü / doğrulama kaynağı:
- `https://code.visualstudio.com/docs/copilot/...`

Temel ilke:
- Kaynak olarak **site HTML'i değil, GitHub repo içindeki Markdown dosyaları** kullanılacaktır.
- Yayındaki görünüm kontrolü gerekiyorsa ikinci kaynak olarak `code.visualstudio.com` kullanılabilir.

---

## Kapsam
Yapay zeka aşağıdaki içerikleri kapsamalıdır:

- `docs/copilot/` altındaki tüm `.md` dosyaları
- Alt klasörlerdeki tüm Copilot belgeleri
- Yeni eklenen tüm klasörler ve sayfalar
- Silinen veya taşınan dosyalar
- İlişkili görseller, iç linkler, referans yapıları ve başlık hiyerarşileri

Not:
Başlangıç fazında kapsam yalnızca `docs/copilot/` ile sınırlıdır. İleride ihtiyaç olursa kapsam ayrı bir kararla genişletilebilir.

---

## Hedef çıktı yapısı
Aşağıdaki klasör yapısı korunmalıdır:

```text
project-root/
  upstream/
    docs/
      copilot/
        ... İngilizce kaynakların senkron kopyası ...

  tr/
    docs/
      copilot/
        ... Türkçe çeviri dosyaları ...

  bulten/
    2026-03-08-bulten.md
    latest-bulten.md

  metadata/
    source_manifest.json
    translation_manifest.json
    last_sync.json
    term_dictionary.json
    processing_rules.json

  logs/
    sync.log
    translate.log
    qa.log

  prompts/
    dokuman_guncelleme.md
```

---

## İlk çalıştırma kuralları
İlk çalıştırmada yapay zeka aşağıdaki adımları eksiksiz uygulamalıdır:

### 1. Kaynakları çek
- Resmi `microsoft/vscode-docs` deposundan `docs/copilot/` altını al.
- Kaynak dosyaların birebir İngilizce kopyasını `upstream/docs/copilot/` altına yerleştir.
- Her dosya için aşağıdaki metadata'yı çıkar:
  - relative path
  - dosya adı
  - son commit SHA
  - içerik hash'i
  - ilk görülme tarihi
  - son senkron tarihi

### 2. Tüm dokümanları tara
- `docs/copilot/` altındaki tüm Markdown dosyalarını recursive olarak bul.
- Her dosyayı işlem listesine ekle.
- Dosya yok sayma yapılmayacak; yalnızca açıkça tanımlanmış istisnalar uygulanabilir.

### 3. Çeviri üret
- Her İngilizce dosya için `tr/docs/copilot/...` altında birebir karşılık Türkçe dosya üret.
- Klasör yapısı korunmalıdır.
- Dosya adı mümkün olduğunca korunmalı; istenirse yalnızca içerik Türkçeleştirilmelidir.
- İç linkler bozulmamalıdır.
- Başlık yapısı korunmalıdır.
- Kod blokları aynen bırakılmalıdır.
- Ayar anahtarları, komutlar, komut paleti ifadeleri, kısayollar, JSON anahtarları, CLI komutları ve dosya yolları çevrilmemelidir.

### 4. Manifest üret
Aşağıdaki kayıtlar oluşturulmalıdır:

#### `metadata/source_manifest.json`
Her İngilizce kaynak için:
- `path`
- `sha`
- `hash`
- `last_seen_at`
- `status`

#### `metadata/translation_manifest.json`
Her Türkçe çıktı için:
- `source_path`
- `translated_path`
- `source_sha`
- `source_hash`
- `translated_at`
- `translation_status`
- `needs_review`

### 5. İlk bülteni üret
İlk çalıştırmada ayrı bir bülten dosyası oluştur:
- `bulten/YYYY-MM-DD-bulten.md`
- `bulten/latest-bulten.md`

Bu ilk bültende şunlar yazmalıdır:
- ilk senkron yapıldığı
- toplam kaç kaynak dosya bulunduğu
- kaç dosyanın Türkçeye çevrildiği
- ana kategori dağılımı
- dikkat çeken yeni başlıklar
- çevrilemeyen / manuel kontrol gereken dosyalar

---

## Sonraki çalıştırma kuralları
(İçerik talimat.md ile aynı - tam metin proje kökündeki talimat.md dosyasında bulunur)

---

## Tek komutluk kullanım amacı
Bu dosya, başka açıklama gerekmeden yapay zekaya şu şekilde verilebilmelidir:

> `prompts/dokuman_guncelleme.md` dosyasındaki kurallara göre VS Code Copilot resmi dokümanlarını senkronize et, Türkçeye çevir, değişiklikleri işle ve güncel bülteni üret.

Yapay zeka bu komutu gördüğünde ek açıklama istemeden bu dokümandaki tüm kuralları uygulamalıdır.
