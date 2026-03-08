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
- Kaynak olarak **site HTML’i değil, GitHub repo içindeki Markdown dosyaları** kullanılacaktır.
- Yayındaki görünüm kontrolü gerekiyorsa ikinci kaynak olarak `code.visualstudio.com` kullanılabilir.

### Ön gereksinimler
- Git kurulu olmalı
- GitHub'a ağ erişimi olmalı
- **project-root**: Bu talimat dosyasının bulunduğu dizin veya işlemin başlatıldığı ana klasör

---

## Kapsam
Yapay zeka aşağıdaki içerikleri kapsamalıdır:

- `docs/copilot/` altındaki tüm `.md` dosyaları
- Alt klasörlerdeki tüm Copilot belgeleri
- Yeni eklenen tüm klasörler ve sayfalar
- Silinen veya taşınan dosyalar
- İlişkili görseller, iç linkler, referans yapıları ve başlık hiyerarşileri

Görseller:
- Görseller (`images/`, `chat/images/` vb.) `upstream/docs/copilot/` altından `tr/docs/copilot/` altına aynı klasör yapısıyla kopyalanmalıdır. Sadece `.md` dosyaları çevrilir; görsel dosyalar olduğu gibi kopyalanır.

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
- Her dosya için aşağıdaki metadata’yı çıkar:
  - relative path (proje köküne göre, örn. `docs/copilot/overview.md`)
  - dosya adı
  - son commit SHA
  - içerik hash’i (SHA-256 ile hesaplanır)
  - ilk görülme tarihi
  - son senkron tarihi

### 2. Tüm dokümanları tara
- `docs/copilot/` altındaki tüm Markdown dosyalarını recursive olarak bul.
- Her dosyayı işlem listesine ekle.
- Dosya yok sayma yapılmayacak. Şu an tanımlı istisna dosyası yoktur; ileride `processing_rules.json` ile istisna listesi eklenebilir.

### 3. Çeviri üret
- Her İngilizce dosya için `tr/docs/copilot/...` altında birebir karşılık Türkçe dosya üret.
- Görselleri `upstream/docs/copilot/` altından `tr/docs/copilot/` altına (images/, chat/images/ vb.) aynı yapıyla kopyala.
- Klasör yapısı korunmalıdır.
- Dosya adı mümkün olduğunca korunmalı; istenirse yalnızca içerik Türkçeleştirilmelidir.
- İç linkler: `/docs/copilot/...` formatı korunmalıdır. Türkçe yayın farklı URL kullanıyorsa (örn. `/tr/docs/copilot/...`), bu mapping `processing_rules.json` içinde tanımlanabilir; varsayılan olarak path değiştirilmez.
- Başlık yapısı korunmalıdır.
- Kod blokları aynen bırakılmalıdır.
- Ayar anahtarları, komutlar, komut paleti ifadeleri, kısayollar, JSON anahtarları, CLI komutları ve dosya yolları çevrilmemelidir.

### 4. Manifest üret
Aşağıdaki kayıtlar oluşturulmalıdır:

#### `metadata/source_manifest.json`
Her İngilizce kaynak için (path'ler proje köküne göre relative):
- `path` (örn. `docs/copilot/overview.md`)
- `sha`
- `hash`
- `last_seen_at`
- `status`

#### `metadata/translation_manifest.json`
Her Türkçe çıktı için (tüm çevrilen dosyalar tek tek kaydedilmeli):
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
İlk çalıştırmadan sonraki her çalıştırmada yapay zeka **tam baştan çeviri yapmayacaktır**. Bunun yerine fark analizi yapacaktır.

### 1. Kaynağı yeniden senkronize et
- Resmi repo’dan son durumu çek.
- `docs/copilot/` altındaki mevcut dosya listesini çıkar.
- Önceki `source_manifest.json` ile karşılaştır.

### 2. Dosya durumlarını sınıflandır
Her dosya aşağıdaki kategorilerden birine düşmelidir:

- `new`: daha önce yoktu, yeni geldi
- `updated`: dosya vardı ama içerik değişti
- `unchanged`: dosya aynı kaldı
- `deleted`: daha önce vardı, artık yok
- `moved_or_renamed`: path değişti; tespit: yeni path'teki dosyanın içerik hash'i, eski manifest'teki başka bir dosyanın hash'iyle örtüşüyorsa veya benzerlik yüksekse (içerik %90+ aynı) eşleştir

### 3. Yeni dosyaları işle
Durumu `new` olan dosyalar için:
- İngilizce dosyayı `upstream/` altına ekle
- Türkçe karşılığını `tr/` altına üret
- Metadata kayıtlarını oluştur
- Bültene “Yeni Dokümanlar” bölümü olarak ekle

### 4. Değişen dosyaları işle
Durumu `updated` olan dosyalar için:
- Eski hash ve yeni hash’i karşılaştır
- Mümkünse bölüm bazlı diff çıkar
- Yalnızca değişen bölümleri yeniden çevir
- Gerekirse tüm dosyayı yeniden üret ama bunu bültende belirt
- Türkçe dokümanda eski çeviri ile yeni resmi içerik arasında tutarlılık sağla
- Çeviri sonrası metadata güncelle

### 5. Silinen dosyaları işle
Durumu `deleted` olan dosyalar için:
- İlgili Türkçe dosyayı doğrudan silme
- `metadata/translation_manifest.json` içinde ilgili kaydın `status` alanını `archived` yap
- Bültene “Kaldırılan / Yayından Çıkan Dokümanlar” olarak ekle
- Fiziksel taşıma: Türkçe dosyayı `tr/archive/YYYY-MM-DD/` altına taşı (aynı relative path korunarak)

### 6. Taşınan veya yeniden adlandırılan dosyaları işle
Durumu `moved_or_renamed` olan dosyalar için:
- Mümkünse eski Türkçe dosyayı yeniden kullan
- Yeni path’e taşı
- İç linkleri kontrol et
- Bültene “Taşınan veya Yeniden Adlandırılan Dokümanlar” bölümü ekle

### 7. Değişmeyen dosyalara dokunma
Durumu `unchanged` olan dosyalar:
- yeniden çevrilmeyecek
- tarihleri gereksiz güncellenmeyecek
- bültende toplu sayı olarak raporlanabilir

---

## Bülten üretim kuralları
Her çalıştırmada mutlaka bir bülten oluşturulacaktır.

### Dosya adları
- tarihli çıktı: `bulten/YYYY-MM-DD-bulten.md` (aynı gün tekrar çalıştırılırsa üzerine yazılır)
- son sürüm: `bulten/latest-bulten.md` (her çalıştırmada güncellenir)

### Bülten içeriği
Bültende şu bölümler bulunmalıdır:

```md
# VS Code Copilot Doküman Güncelleme Bülteni - YYYY-MM-DD

## Özet
- Toplam taranan dosya sayısı:
- Yeni doküman sayısı:
- Güncellenen doküman sayısı:
- Silinen / taşınan doküman sayısı:
- Değişmeyen doküman sayısı:

## Yeni Dokümanlar
- path
- kısa açıklama
- Türkçe çıktı yolu

## Güncellenen Dokümanlar
- path
- ne değişti (kısa özet)
- hangi başlıklar etkilendi
- Türkçe dosyada yapılan işlem

## Kaldırılan / Arşivlenen Dokümanlar
- eski path
- durum

## Taşınan / Yeniden Adlandırılan Dokümanlar
- eski path -> yeni path

## Dikkat Çeken Yenilikler
- yeni özellikler
- ayar değişiklikleri
- deprecated ifadeler
- preview / experimental notları

## Manuel İnceleme Gereken Noktalar
- çeviri belirsizlikleri
- kırık link riski
- tablo / özel blok riski
```

### Bülten yazım ilkeleri
- Bülten kısa ama bilgi yoğun olmalı
- Teknik değişiklikler net yazılmalı
- Kullanıcıyı ilgilendiren yenilikler öne çıkarılmalı
- Gereksiz tekrar olmamalı
- `deprecated`, `preview`, `experimental`, `important`, `warning` gibi ibareler özellikle özetlenmeli

---

## Çeviri kuralları
Yapay zeka aşağıdaki çeviri kurallarına uymak zorundadır.

### Asla çevrilmeyecek öğeler
- `GitHub Copilot`
- `Visual Studio Code`
- ürün adı, özellik adı, marka adı
- ayar anahtarları (`github.copilot.*` gibi)
- komutlar ve komut paleti komutları
- JSON key’leri
- CLI komutları
- dosya yolları
- kod blokları
- kısayollar
- API adları
- sabit terimler (gerekirse glossary’ye göre)

### Frontmatter (YAML) kuralları
- `ContentId`, `DateApproved`, `MetaSocialImage`, `Keywords`: değiştirilmez
- `MetaDescription`: Türkçeye çevrilir

### Kontrollü çevrilecek öğeler
- açıklayıcı paragraflar
- kullanım adımları
- notlar, ipuçları, uyarılar
- örnek senaryo açıklamaları
- başlıklar
- tablo açıklamaları

### Terminoloji yönetimi
`metadata/term_dictionary.json` dosyası tutulmalıdır.

Örnek:

```json
{
  "inline suggestions": "satır içi öneriler",
  "smart actions": "akıllı eylemler",
  "agent sessions": "ajan oturumları",
  "settings reference": "ayarlar başvurusu",
  "custom instructions": "özel talimatlar",
  "prompt files": "prompt dosyaları"
}
```

Kurallar:
- Aynı İngilizce terim her yerde mümkün olduğunca aynı Türkçe karşılıkla çevrilmelidir.
- Gerekirse ilk kullanımda şu format kullanılabilir:
  - `Ajan oturumları (agent sessions)`
- Teknik anlamı bozacak serbest çeviriden kaçınılmalıdır.

---

## Markdown koruma kuralları
Yapay zeka çeviri sırasında Markdown yapısını bozmamalıdır.

Korunacak öğeler:
- başlık seviyeleri
- madde listeleri
- numaralı listeler
- tablo yapısı
- link hedefleri
- relatif yollar
- görsel referansları
- admonition blokları (`[!NOTE]`, `[!TIP]`, `[!WARNING]`, `[!IMPORTANT]` vb.; etiket korunur, içerik çevrilir)
- kod blokları
- frontmatter / metadata alanları varsa onların gerekli teknik bölümleri

Yapılmaması gerekenler:
- kod bloklarını çevirmek
- link URL’lerini bozmak
- anchor yapısını kırmak
- tablo kolon sayısını değiştirmek
- key-value yapılarını serbest çevirmek

---

## Kalite kontrol kuralları
Her güncelleme sonunda QA yapılmalıdır.

### Zorunlu kontroller
1. Kaynak ve çeviri dosyasında başlık sayısı uyumlu mu?
2. Kod blok sayısı aynı mı?
3. Link sayısı aynı mı?
4. Ayar anahtarları bozulmuş mu?
5. JSON örnekleri geçerli görünüyor mu?
6. Tablo yapısı korunmuş mu?
7. Türkçe dosya path’i doğru mu?
8. İç linkler mevcut dosyalara gidiyor mu?

### QA sonucu
Her dosya için şu statülerden biri atanmalıdır:
- `ok`
- `ok_with_warnings`
- `manual_review_required`
- `failed`

QA sonuçları:
- `logs/qa.log`
- `metadata/translation_manifest.json`

---

## Karar alma kuralları
Yapay zeka belirsizlik durumlarında aşağıdaki karar sırasını izleyecektir:

1. Resmi kaynak metni koru
2. Teknik doğruluğu koru
3. Terminoloji tutarlılığını koru
4. Markdown yapısını koru
5. Türkçe akıcılığı iyileştir

Yani önce teknik doğruluk, sonra dil akıcılığı gelir.

---

## Çalıştırma modu
Yapay zeka her çalıştırmada aşağıdaki mantığı uygulamalıdır:

### Mod 1: İlk kurulum
Şart:
- `metadata/source_manifest.json` yoksa veya okunamıyorsa (bozuk/geçersiz JSON)

Yapılacaklar:
- full scan
- full translate
- manifest oluştur
- ilk bülteni yaz

### Mod 2: Güncelleme
Şart:
- manifest varsa

Yapılacaklar:
- upstream sync
- diff analizi
- new / updated / deleted / moved tespiti
- seçici çeviri güncellemesi
- yeni bülten üretimi

---

## AI için net görev tanımı
Yapay zekanın görevi şudur:

> Resmi VS Code Copilot dokümantasyon kaynağını takip et. İlk çalıştırmada `docs/copilot` altındaki tüm İngilizce Markdown dokümanlarını Türkçeye çevir ve aynı klasör yapısıyla çıktı üret. Sonraki çalıştırmalarda yalnızca yeni eklenen, değişen, silinen, taşınan veya yeniden adlandırılan dokümanları tespit et. Yeni dokümanların Türkçe kopyalarını ekle, güncellenen dokümanların Türkçe sürümlerini uyumlu biçimde güncelle, silinenleri arşivle. Her çalıştırmada tüm değişiklikleri ve dikkat çeken yenilikleri ayrı bir bülten dosyasında özetle. Markdown yapısını, teknik terimleri, kod bloklarını, ayar anahtarlarını ve bağlantıları koru. Tutarlılık için terminoloji sözlüğünü ve manifest dosyalarını kullan.

---

## Yapay zekanın asla atlamaması gereken maddeler
- Sadece site HTML’ini parse ederek çalışmamalı
- Önce manifest kontrol etmeli
- Değişmeyen dosyaları yeniden çevirmemeli
- Yeni dosyaları mutlaka Türkçeye eklemeli
- Tüm değişiklikleri bültene mutlaka yazmalı
- Çevirilerde teknik anahtarları bozmamalı
- QA yapmadan çıktıyı tamamlanmış saymamalı
- Hata veya belirsizlik varsa bültende belirtmeli

---

## Bülten için örnek özet formatı

```md
## Dikkat Çeken Yenilikler
- `customization/prompt-files.md` dosyasında prompt dosyalarıyla ilgili açıklamalar güncellendi.
- `reference/copilot-settings.md` içinde yeni veya güncellenmiş ayar açıklamaları var.
- Bazı özelliklerde `deprecated` uyarısı eklendi veya değişti.
- Bazı sayfalarda `preview` / `experimental` notları öne çıktı.
```

---

## Çeviri tonu
- Türkçe doğal olmalı
- Teknik olarak net olmalı
- Gereksiz süslü çeviri yapılmamalı
- Dokümantasyon tonu korunmalı
- Gerektiğinde sadeleştir ama anlamı genişletme
- Resmi metinde olmayan yorum ekleme

---

## Hata yönetimi
Aşağıdaki durumlar olduğunda yapay zeka bunu log ve bültende belirtmelidir:
- dosya okunamadı
- dosya parse edilemedi
- Markdown yapısı bozuldu
- çeviri belirsiz
- link doğrulaması başarısız
- taşınan dosya eşleşmesi belirsiz
- büyük çaplı dosya değişimi nedeniyle tam yeniden çeviri yapıldı

---

## Önerilen işlem sırası
Her çalıştırmada şu sıra izlenmelidir:

1. Kaynak repo’yu senkronize et
2. `docs/copilot/` ağacını tara
3. Manifest ile karşılaştır
4. Dosyaları sınıflandır
5. Yeni dosyaları çevir
6. Güncellenen dosyaları diff bazlı güncelle
7. Silinen / taşınan dosyaları işle
8. QA yap
9. Manifestleri güncelle
10. Bülteni üret
11. `latest-bulten.md` dosyasını yenile

---

## Tek komutluk kullanım amacı
Bu dosya, başka açıklama gerekmeden yapay zekaya şu şekilde verilebilmelidir:

> `prompts/dokuman_guncelleme.md` dosyasındaki kurallara göre VS Code Copilot resmi dokümanlarını senkronize et, Türkçeye çevir, değişiklikleri işle ve güncel bülteni üret.

Yapay zeka bu komutu gördüğünde ek açıklama istemeden bu dokümandaki tüm kuralları uygulamalıdır.

---

## İsteğe bağlı gelişmiş iyileştirmeler
İleride eklenebilir:
- bölüm bazlı daha hassas diff
- translation memory
- otomatik PR üretimi
- kırık link raporu
- değişiklik önem puanı
- sadece son 7 gündeki güncellemeler için kısa bülten
- tam bülten + yönetici özeti olmak üzere iki ayrı çıktı

---

## Son söz
Bu doküman bir "çalışma anayasası" gibi kullanılmalıdır. Yapay zeka her senkronizasyonda aynı kuralları uygulamalı, teknik doğruluğu ve Markdown bütünlüğünü korumalı, tüm yeni ve değişen Copilot belgelerini Türkçe kaynaklara yansıtmalı ve her çalıştırmada denetlenebilir bir bülten üretmelidir.