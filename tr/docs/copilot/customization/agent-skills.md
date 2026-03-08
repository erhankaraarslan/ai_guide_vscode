---
ContentId: a7d3e5f8-2c4b-4d9a-b8e1-3f6c9a2d7e41
DateApproved: 3/4/2026
MetaDescription: VS Code'da Agent Skills kullanarak GitHub Copilot'a VS Code, GitHub Copilot CLI ve GitHub Copilot kodlama ajanında çalışan özelleştirilmiş yetenekler öğretmeyi öğrenin.
MetaSocialImage: ../images/shared/github-copilot-social.png
Keywords:
- copilot
- agents
- skills
- instructions
- customization
- ai
- claude
---
# VS Code'da Agent Skills kullanın

Agent Skills, GitHub Copilot'un ilgili olduğunda özelleştirilmiş görevleri gerçekleştirmek üzere yükleyebildiği talimatlar, scriptler ve kaynaklar içeren klasörlerdir. Agent Skills, VS Code'da GitHub Copilot, GitHub Copilot CLI ve GitHub Copilot kodlama ajanı dahil birden çok AI ajanında çalışan [açık bir standarddır](https://agentskills.io).

Öncelikle kodlama yönergeleri tanımlayan [özel talimatlardan](/docs/copilot/customization/custom-instructions.md) farklı olarak beceriler, scriptler, örnekler ve diğer kaynakları içerebilen özelleştirilmiş yetenekler ve iş akışları sağlar. Oluşturduğunuz beceriler taşınabilir ve beceri uyumlu herhangi bir ajanda çalışır.

Agent Skills'ın temel faydaları:

* **Copilot'u uzmanlaştırın**: Bağlamı tekrarlamadan alan özel görevler için yetenekleri uyarlayın
* **Tekrarları azaltın**: Bir kez oluşturun, tüm konuşmalarda otomatik kullanın
* **Yetenekleri birleştirin**: Karmaşık iş akışları oluşturmak için birden fazla beceriyi birleştirin
* **Verimli yükleme**: Yalnızca ilgili içerik gerektiğinde bağlama yüklenir

> [!TIP]
> Tüm sohbet özelleştirmelerinizi tek bir yerde keşfetmek, oluşturmak ve yönetmek için [Sohbet Özelleştirmeleri editörünü](/docs/copilot/customization/overview.md#chat-customizations-editor) (Önizleme) kullanın. Komut Paleti'nden **Chat: Open Chat Customizations** komutunu çalıştırın.

## Agent Skills vs özel talimatlar

Hem Agent Skills hem de özel talimatlar Copilot'un davranışını özelleştirmeye yardımcı olsa da farklı amaçlara hizmet eder:

| Özellik | Agent Skills | Özel Talimatlar |
| ------- | ------------ | ------------------- |
| **Amaç** | Özelleştirilmiş yetenekleri ve iş akışlarını öğretin | Kodlama standartları ve yönergeleri tanımlayın |
| **Taşınabilirlik** | VS Code, Copilot CLI ve Copilot kodlama ajanında çalışır | Yalnızca VS Code ve GitHub.com |
| **İçerik** | Talimatlar, scriptler, örnekler ve kaynaklar | Yalnızca talimatlar |
| **Kapsam** | Görev özel, isteğe bağlı yüklenir | Her zaman uygulanır (veya glob desenleriyle) |
| **Standart** | Açık standart ([agentskills.io](https://agentskills.io)) | VS Code özel |

Agent Skills'ı şu durumlarda kullanın:

* Farklı AI araçları arasında çalışan yeniden kullanılabilir yetenekler oluşturmak
* Talimatlarla birlikte scriptler, örnekler veya diğer kaynakları dahil etmek
* Yetenekleri daha geniş AI topluluğuyla paylaşmak
* Test, hata ayıklama veya dağıtım süreçleri gibi özelleştirilmiş iş akışları tanımlamak

Özel talimatları şu durumlarda kullanın:

* Proje özel kodlama standartları tanımlamak
* Dil veya framework sözleşmeleri belirlemek
* Kod incelemesi veya commit mesajı yönergeleri belirtmek
* Glob desenleri kullanarak dosya türlerine göre kurallar uygulamak

## Beceri oluşturma

> [!TIP]
> **Configure Skills** menüsünü hızlıca açmak için sohbet girişinde `/skills` yazın.

Beceriler beceri davranışını tanımlayan `SKILL.md` dosyası içeren dizinlerde saklanır. VS Code iki tür beceriyi destekler:

| Beceri türü | Konum |
| ---------- | -------- |
| Deponuzda saklanan proje becerileri | `.github/skills/`, `.claude/skills/`, `.agents/skills/` |
| Kullanıcı profilinizde saklanan kişisel beceriler | `~/.copilot/skills/`, `~/.claude/skills/`, `~/.agents/skills/` |

> [!TIP]
> VS Code'un beceri aradığı ek konumları `setting(chat.agentSkillsLocations)` ayarıyla yapılandırabilirsiniz. Projeler arasında beceri paylaşmak veya bunları merkezi bir konumda tutmak için faydalıdır.

Beceri oluşturmak için:

1. Çalışma alanınızda `.github/skills` dizini oluşturun.

1. Beceriniz için bir alt dizin oluşturun. Her becerinin kendi dizini olmalıdır (örneğin `.github/skills/webapp-testing`).

1. Beceri dizininde aşağıdaki yapıda `SKILL.md` dosyası oluşturun:

    ```markdown
    ---
    name: skill-name
    description: Description of what the skill does and when to use it
    ---

    # Skill Instructions

    Your detailed instructions, guidelines, and examples go here...
    ```

1. İsteğe bağlı olarak beceri dizinine scriptler, örnekler veya diğer kaynaklar ekleyin.

    Örneğin web uygulamalarını test etmek için bir beceri şunları içerebilir:

    * `SKILL.md` - Testleri çalıştırma talimatları
    * `test-template.js` - Şablon test dosyası
    * `examples/` - Örnek test senaryoları

### AI ile beceri oluşturma

Yetenek açıklamasına dayalı olarak AI ile beceri oluşturabilirsiniz. Sohbette `/create-skill` yazın ve istediğiniz beceriyi açıklayın (örneğin, "entegrasyon testlerini çalıştırma ve hata ayıklama becerisi"). Ajan açıklayıcı sorular sorar ve dizin yapısı, talimatlar ve frontmatter ile bir `SKILL.md` dosyası oluşturur.

Devam eden bir sohbetteki yeniden kullanılabilir beceriyi de çıkarabilirsiniz. Örneğin karmaşık bir sorunu hata ayıkladığınız çok turlu bir oturumdan sonra "bunu az önce nasıl hata ayıkladığımızdan bir beceri oluştur" deyin; çok adımlı prosedürü yeniden kullanılabilir beceri olarak yakalar.

## SKILL.md dosya formatı

`SKILL.md` dosyası becerinin meta verilerini ve davranışını tanımlayan YAML frontmatter içeren bir Markdown dosyasıdır.

### Başlık (gerekli)

Başlık aşağıdaki alanlarla YAML frontmatter olarak biçimlendirilir:

| Alan | Gerekli | Açıklama |
|-------|----------|-------------|
| `name` | Evet | Beceri için benzersiz tanımlayıcı. Küçük harf olmalı, boşluklar için tire kullanın (örneğin `webapp-testing`). Üst dizin adıyla eşleşmeli. Maksimum 64 karakter. |
| `description` | Evet | Becerinin ne yaptığının **ve ne zaman kullanılacağının** açıklaması. Hem yetenekleri hem de kullanım senaryolarını belirterek Copilot'un beceriyi ne zaman yükleyeceğine karar vermesine yardımcı olun. Maksimum 1024 karakter. |
| `argument-hint` | Hayır | Beceri eğik çizgi komutu olarak çağrıldığında sohbet giriş alanında gösterilen ipucu metni. Kullanıcıların ne tür ek bilgi sağlaması gerektiğini anlamalarına yardımcı olur (örneğin `[test file] [options]`). |
| `user-invocable` | Hayır | Becerinin sohbet menüsünde eğik çizgi komutu olarak görünüp görünmeyeceğini kontrol eder. Varsayılan `true`. Ajanın hala otomatik yüklemesine izin verirken beceriyi `/` menüsünden gizlemek için `false` yapın. |
| `disable-model-invocation` | Hayır | Ajanın ilgiliye göre beceriyi otomatik yükleyip yükleyemeyeceğini kontrol eder. Varsayılan `false`. Yalnızca `/` eğik çizgi komutu üzerinden manuel çağrı gerektirmek için `true` yapın. |

### Gövde

Beceri gövdesi Copilot bu beceriyi kullanırken takip etmesi gereken talimatları, yönergeleri ve örnekleri içerir. Şunları açıklayan net, spesifik talimatlar yazın:

* Becerinin ne başarmaya yardımcı olduğu
* Beceriyi ne zaman kullanacağı
* Takip edilecek adım adım prosedürler
* Beklenen giriş ve çıktı örnekleri
* Dahil edilen scriptlere veya kaynaklara referanslar

Beceri dizinindeki dosyalara göreli yollarla atıfta bulunabilirsiniz. Örneğin beceri dizininizdeki bir scripte referans vermek için `[test script](./test-template.js)` kullanın.

## Örnek beceriler

Aşağıdaki örnekler oluşturabileceğiniz farklı beceri türlerini gösterir.

<details>
<summary>Örnek: Web uygulaması test becerisi</summary>

````markdown
---
name: webapp-testing
description: Guide for testing web applications using Playwright. Use this when asked to create or run browser-based tests.
---

# Web Uygulaması Testi Playwright ile

Bu beceri Playwright kullanarak web uygulamaları için tarayıcı tabanlı testler oluşturmanıza ve çalıştırmanıza yardımcı olur.

## Bu beceriyi ne zaman kullanın

Şu durumlarda bu beceriyi kullanın:
- Web uygulamaları için yeni Playwright testleri oluşturma
- Başarısız tarayıcı testlerini hata ayıklama
- Yeni proje için test altyapısı kurma

## Test oluşturma

1. Standart test yapısı için [test şablonuna](./test-template.js) bakın
2. Test edilecek kullanıcı akışını belirleyin
3. `tests/` dizininde yeni test dosyası oluşturun
4. Öğeleri bulmak için Playwright lokatörlerini kullanın (rol tabanlı seçicileri tercih edin)
5. Beklenen davranışı doğrulamak için onaylar ekleyin

## Testleri çalıştırma

Yerel olarak testleri çalıştırmak için:
```bash
npx playwright test
```

Testleri hata ayıklamak için:
```bash
npx playwright test --debug
```

## En iyi uygulamalar

- Dinamik içerik için data-testid nitelikleri kullanın
- Testleri bağımsız ve atomik tutun
- Karmaşık sayfalar için Page Object Model kullanın
- Başarısızlıkta ekran görüntüsü alın
````

</details>

<details>
<summary>Örnek: GitHub Actions hata ayıklama becerisi</summary>

````markdown
---
name: github-actions-debugging
description: Guide for debugging failing GitHub Actions workflows. Use this when asked to debug failing GitHub Actions workflows.
---

# GitHub Actions Hata Ayıklama

Bu beceri pull request'lerdeki başarısız GitHub Actions iş akışlarını hata ayıklamanıza yardımcı olur.

## Süreç

1. Pull request için son iş akışı çalıştırmalarına ve durumlarına bakmak için `list_workflow_runs` aracını kullanın
2. Başarısız işlerin logları için AI özeti almak için `summarize_job_log_failures` aracını kullanın
3. Daha fazla bilgi gerekiyorsa tam hata loglarını almak için `get_job_logs` veya `get_workflow_run_logs` aracını kullanın
4. Başarısızlığı ortamınızda yerel olarak yeniden oluşturmayı deneyin
5. Başarısız derlemeyi düzeltin ve değişiklikleri işlemeden önce düzeltmeyi doğrulayın

## Yaygın sorunlar

- **Eksik ortam değişkenleri**: Tüm gerekli gizli bilgilerin yapılandırıldığından emin olun
- **Sürüm uyumsuzlukları**: Action sürümleri ve bağımlılıkların uyumlu olduğunu doğrulayın
- **İzin sorunları**: İş akışının gerekli izinlere sahip olduğundan emin olun
- **Zaman aşımı sorunları**: Uzun süren işleri bölmeyi veya zaman aşımı değerlerini artırmayı düşünün
````

</details>

## Becerileri eğik çizgi komutları olarak kullanın

Beceriler sohbette [prompt dosyaları](/docs/copilot/customization/prompt-files.md) ile birlikte eğik çizgi komutları olarak kullanılabilir. Sohbet giriş alanında `/` yazın, mevcut beceri ve prompt listesini görün, bir beceriyi seçip çağırın.

Eğik çizgi komutundan sonra ek bağlam ekleyebilirsiniz. Örneğin `/webapp-testing for the login page` veya `/github-actions-debugging PR #42`.

Varsayılan olarak tüm beceriler `/` menüsünde görünür. Her becerinin nasıl erişileceğini kontrol etmek için `user-invocable` ve `disable-model-invocation` frontmatter özelliklerini kullanın:

| Yapılandırma | Eğik çizgi komutu | Copilot tarafından otomatik yüklenir | Kullanım senaryosu |
|---|---|---|---|
| Varsayılan (her iki özellik atlanmış) | Evet | Evet | Genel amaçlı beceriler |
| `user-invocable: false` | Hayır | Evet | Model ilgili olduğunda yüklenen arka plan bilgi becerileri |
| `disable-model-invocation: true` | Evet | Hayır | Yalnızca talep üzerine çalıştırmak istediğiniz beceriler |
| İkisi de ayarlı | Hayır | Hayır | Devre dışı beceriler |

## Copilot becerileri nasıl kullanır

Beceriler verimli yükleme için yalnızca gerektiğinde içerik yükleyen aşamalı açıklama kullanır. Bu üç seviyeli yükleme sistemi bağlamı tüketmeden birçok beceri yüklemenizi sağlar:

**Seviye 1: Beceri keşfi**

Copilot YAML frontmatter'dan `name` ve `description` okuyarak hangi becerilerin mevcut olduğunu her zaman bilir. Bu meta veri hafiftir ve Copilot'un isteminize hangi becerilerin ilgili olduğuna karar vermesine yardımcı olur.

**Seviye 2: Talimat yükleme**

İsteminiz bir becerinin açıklamasıyla eşleştiğinde Copilot `SKILL.md` dosya gövdesini bağlamına yükler. Yalnızca o zaman detaylı talimatlar kullanılabilir olur. Beceriyi sohbette `/` eğik çizgi komutunu kullanarak doğrudan da çağırabilirsiniz.

**Seviye 3: Kaynak erişimi**

Copilot beceri dizinindeki ek dosyalara (scriptler, örnekler, dokümantasyon) yalnızca gerektiğinde erişebilir. Copilot bunlara referans verene kadar bu kaynaklar yüklenmez; bağlamınız verimli kalır.

Bu mimari becerilerin hem isteminize göre otomatik etkinleştirildiği hem de eğik çizgi komutları aracılığıyla manuel çağrılabildiği anlamına gelir. Birçok beceri yükleyebilirsiniz ve Copilot her görev için yalnızca ilgili olanı yükler.

## Paylaşılan becerileri kullanın

Başkalarının oluşturduğu becerileri Copilot'un yeteneklerini geliştirmek için kullanabilirsiniz. [github/awesome-copilot](https://github.com/github/awesome-copilot) deposu beceriler, özel ajanlar, talimatlar ve prompt'lardan oluşan büyüyen topluluk koleksiyonu içerir. [anthropics/skills](https://github.com/anthropics/skills) deposu ek referans becerileri içerir.

[Ajan eklentilerinde](/docs/copilot/customization/agent-plugins.md) paketlenmiş becerileri de keşfedebilir ve yükleyebilirsiniz. Yüklenen eklentilerden gelen beceriler **Configure Skills** menüsünde yerel olarak tanımladığınız becerilerle birlikte görünür.

Paylaşılan beceri kullanmak için:

1. Depodaki mevcut becerilere göz atın
1. Beceri dizinini `.github/skills/` klasörünüze kopyalayın
1. İhtiyaçlarınıza göre `SKILL.md` dosyasını inceleyin ve özelleştirin
1. İsteğe bağlı olarak gerektiğinde kaynakları değiştirin veya ekleyin

> [!TIP]
> Kullanmadan önce paylaşılan becerileri her zaman gereksinimlerinize ve güvenlik standartlarınıza uyduğundan emin olmak için inceleyin. VS Code'un [terminal aracı](/docs/copilot/agents/agent-tools.md#terminal-commands) script yürütme için [otomatik onay seçenekleri](/docs/copilot/agents/agent-tools.md#automatically-approve-terminal-commands) dahil kontroller sağlar. Otomatik onay özellikleri için [güvenlik değerlendirmeleri](/docs/copilot/security.md#automated-approval) hakkında daha fazla bilgi edinin.

## Uzantılardan beceri katkısı

Uzantılar `package.json` dosyalarındaki `chatSkills` katkı noktasını kullanarak beceri katkısında bulunabilir. Yol [Agent Skills belirtimini](https://agentskills.io/specification) takip ederek `SKILL.md` dosyası içeren bir dizine işaret etmelidir.

### Gerekli klasör yapısı

Beceri dizini bu yapıyı takip etmelidir:

```text
extension-root/
└── skills/
    └── my-skill/           # Dizin adı SKILL.md'deki `name` alanıyla eşleşmeli
        └── SKILL.md         # Gerekli
```

### package.json'da beceriyi kaydedin

Uzantınızın `package.json` dosyasına `chatSkills` katkı noktasını ekleyin. `path` özelliği karşılık gelen `SKILL.md` dosyasına işaret etmelidir:

```json
{
  "contributes": {
    "chatSkills": [
      {
        "path": "./skills/my-skill/SKILL.md"
      }
    ]
  }
}
```

> [!IMPORTANT]
> `SKILL.md` frontmatter'daki `name` alanı üst dizin adıyla eşleşmelidir. Örneğin dizin `skills/my-skill/` ise `name` alanı `my-skill` olmalıdır. Ad eşleşmezse beceri yüklenmez.

`SKILL.md` dosyası [proje ve kişisel becerilerle](#create-a-skill) aynı formatı takip eder. Örneğin:

```markdown
---
name: my-skill
description: Description of what the skill does and when to use it.
---

# My Skill

Detailed instructions for the skill...
```

## Agent Skills standardı

Agent Skills farklı AI ajanları arasında taşınabilirlik sağlayan açık bir standarddır. VS Code'da oluşturduğunuz beceriler birden çok ajanda çalışır, dahil:

* **VS Code'da GitHub Copilot**: Sohbette ve ajan modunda kullanılabilir
* **GitHub Copilot CLI**: Terminalde çalışırken erişilebilir
* **GitHub Copilot kodlama ajanı**: Otomatik kodlama görevleri sırasında kullanılır

Agent Skills standardı hakkında [agentskills.io](https://agentskills.io) adresinde daha fazla bilgi edinin.

## İlgili kaynaklar

* [AI yanıtlarını özelleştirme genel bakış](/docs/copilot/customization/overview.md)
* [Özel talimatlar oluşturun](/docs/copilot/customization/custom-instructions.md)
* [Yeniden kullanılabilir prompt dosyaları oluşturun](/docs/copilot/customization/prompt-files.md)
* [Özel ajanlar oluşturun](/docs/copilot/customization/custom-agents.md)
* [Agent Skills belirtimi](https://agentskills.io)
* [Referans beceriler deposu](https://github.com/anthropics/skills)
* [Ajan eklentilerini keşfedin ve yönetin](/docs/copilot/customization/agent-plugins.md)
