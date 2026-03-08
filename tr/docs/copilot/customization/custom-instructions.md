---
ContentId: 8b4f3c21-4e02-4a89-9f15-7a8d6b5c2e91
DateApproved: 3/4/2026
MetaDescription: AI yanıtlarının kodlama uygulamalarınız, proje gereksinimleriniz ve geliştirme standartlarınızla eşleşmesini sağlamak için VS Code'da GitHub Copilot Chat için özel talimatlar oluşturmayı öğrenin.
MetaSocialImage: ../images/shared/github-copilot-social.png
Keywords:
- customize
- rules
- instructions
- copilot-instructions.md
- AGENTS.md
- CLAUDE.md
- coding standards
- ai
- copilot
---
# VS Code'da özel talimatları kullanın

Özel talimatlar, AI'nın kod üretimini ve diğer geliştirme görevlerini nasıl yönettiğini otomatik olarak etkileyen ortak yönergeler ve kurallar tanımlamanızı sağlar. Her sohbet isteminde manuel olarak bağlam eklemek yerine, Markdown dosyasında özel talimatlar belirleyerek kodlama uygulamalarınız ve proje gereksinimlerinizle uyumlu tutarlı AI yanıtları sağlayın.

Özel talimatları tüm sohbet isteklerine otomatik olarak uygulayacak, yalnızca belirli dosyalara uygulayacak veya belirli bir sohbet istemine manuel olarak ekleyecek şekilde yapılandırabilirsiniz.

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="Generate instructions">
`/init` ile projenize özel özel talimatlar oluşturmak için projenizi AI için ayarlayın.

* [Open in VS Code](vscode://GitHub.Copilot-Chat/chat?prompt=%2Finit)

</div>

> [!TIP]
> Tüm sohbet özelleştirmelerinizi tek bir yerde keşfetmek, oluşturmak ve yönetmek için [Sohbet Özelleştirmeleri editörünü](/docs/copilot/customization/overview.md#chat-customizations-editor) (Önizleme) kullanın. Komut Paleti'nden **Chat: Open Chat Customizations** komutunu çalıştırın.

> [!NOTE]
> Özel talimatlar, editörde yazarken [satır içi öneriler](/docs/copilot/ai-powered-suggestions.md) için dikkate alınmaz.

## Talimat dosyası türleri

VS Code iki kategori özel talimatı destekler. Projenizde birden fazla talimat dosyanız varsa, VS Code bunları birleştirir ve sohbet bağlamına ekler; belirli bir sıra garanti edilmez.

### Her zaman açık talimatlar

Her zaman açık talimatlar her sohbet isteğine otomatik olarak dahil edilir. Proje genelinde kodlama standartları, mimari kararlar ve tüm koda uygulanan sözleşmeler için kullanın.

* Tek bir [`.github/copilot-instructions.md`](#use-a-githubcopilot-instructionsmd-file) dosyası
    * Çalışma alanındaki tüm sohbet isteklerine otomatik uygulanır
    * Çalışma alanı içinde saklanır

* Bir veya daha fazla [`AGENTS.md`](#use-an-agentsmd-file) dosyası
    * Çalışma alanınızda birden fazla AI ajanıyla çalışıyorsanız faydalıdır
    * Çalışma alanındaki tüm sohbet isteklerine veya belirli alt klasörlere otomatik uygulanır (deneysel)
    * Çalışma alanının kökünde veya alt klasörlerde saklanır (deneysel)

* [Kuruluş düzeyinde talimatlar](#share-custom-instructions-across-teams)
    * GitHub kuruluşu genelinde birden fazla çalışma alanı ve depo arasında talimat paylaşın
    * GitHub kuruluşu düzeyinde tanımlanır

* [`CLAUDE.md`](#use-a-claudemd-file) dosyası
    * Claude Code ve diğer Claude tabanlı araçlarla uyumluluk için
    * Çalışma alanı kökünde, `.claude` klasöründe veya kullanıcı ana dizininde saklanır

### Dosya tabanlı talimatlar

Dosya tabanlı talimatlar, ajanın üzerinde çalıştığı dosyalar belirtilen bir desenle eşleştiğinde veya açıklama mevcut görevle eşleştiğinde uygulanır. Dil özel sözleşmeleri, framework kalıpları veya yalnızca kod tabanınızın belirli bölümlerine uygulanan kurallar için dosya tabanlı talimatları kullanın.

* Bir veya daha fazla [`.instructions.md`](#use-instructionsmd-files) dosyası
    * Glob desenleri kullanarak dosya türü veya konuma göre koşullu talimat uygulayın
    * Çalışma alanında veya kullanıcı profilinde saklanır

Dosyalar veya URL'ler gibi belirli bağlama atıfta bulunmak için Markdown bağlantılarını kullanabilirsiniz.

> [!TIP]
> **Hangi yaklaşımı kullanmalısınız?** Proje genelinde kodlama standartları için tek bir `.github/copilot-instructions.md` dosyasıyla başlayın. Farklı dosya türleri veya framework'ler için farklı kurallara ihtiyacınız olduğunda `.instructions.md` dosyaları ekleyin. Çalışma alanınızda birden fazla AI ajanıyla çalışıyorsanız `AGENTS.md` kullanın.

## `.github/copilot-instructions.md` dosyası kullanın

VS Code, çalışma alanınızın kökündeki `.github/copilot-instructions.md` Markdown dosyasını otomatik olarak algılar ve bu dosyadaki talimatları bu çalışma alanındaki tüm sohbet isteklerine uygular.

`copilot-instructions.md` şunlar için kullanın:

* Proje genelinde uygulanan kod stili ve adlandırma sözleşmeleri
* Teknoloji yığını bildirimleri ve tercih edilen kütüphaneler
* Uyulacak veya kaçınılacak mimari kalıplar
* Güvenlik gereksinimleri ve hata işleme yaklaşımları
* Dokümantasyon standartları

Çalışma alanınızda `.github/copilot-instructions.md` dosyası oluşturmak için şu adımları izleyin:

1. Çalışma alanınızın kökünde `.github/copilot-instructions.md` dosyası oluşturun. Gerekirse önce `.github` dizinini oluşturun.

1. Talimatlarınızı Markdown formatında açıklayın. En iyi sonuçlar için kısa ve odaklı tutun.

> [!NOTE]
> VS Code ayrıca her zaman açık talimatlar için [`AGENTS.md`](#use-an-agentsmd-file) dosyası kullanımını destekler.

<details>
<summary>Örnek: Genel kodlama yönergeleri</summary>

```markdown
---
applyTo: "**"
---
# Proje genel kodlama standartları

## Adlandırma Sözleşmeleri
- Bileşen adları, arayüzler ve tür diğer adları için PascalCase kullanın
- Değişkenler, fonksiyonlar ve yöntemler için camelCase kullanın
- Özel sınıf üyelerini alt çizgi (_) ile önekilendirin
- Sabitler için ALL_CAPS kullanın

## Hata İşleme
- Eşzamansız işlemler için try/catch blokları kullanın
- React bileşenlerinde uygun hata sınırları uygulayın
- Hataları her zaman bağlamsal bilgilerle günlükleyin
```

</details>

## `.instructions.md` dosyaları kullanın

Ajanın üzerinde çalıştığı dosyalara veya görevlere göre dinamik olarak uygulanan `*.instructions.md` Markdown dosyalarıyla dosya tabanlı talimatlar oluşturabilirsiniz.

Ajan, talimat dosyası başlığındaki `applyTo` özelliğinde belirtilen dosya desenlerine veya talimat açıklamasının mevcut görevle anlamsal eşleşmesine dayanarak hangi talimat dosyalarının uygulanacağını belirler.

`.instructions.md` dosyalarını şunlar için kullanın:

* Ön uç ve arka uç kodu için farklı sözleşmeler
* Monorepo'da dil özel yönergeleri
* Belirli modüller için framework özel kalıpları
* Test dosyaları veya dokümantasyon için özelleştirilmiş kurallar

### Talimat dosyası konumları

Belirli bir çalışma alanı için veya tüm çalışma alanlarınıza uygulanan kullanıcı düzeyinde talimatları tanımlayabilirsiniz.

| Kapsam | Varsayılan dosya konumu |
|-------|-----------------------|
| Çalışma alanı | `.github/instructions` klasörü |
| Kullanıcı profili | Geçerli [VS Code profili](/docs/configure/profiles.md) `prompts` klasörü |

Çalışma alanı talimat dosyaları için ek dosya konumlarını `setting(chat.instructionsFilesLocations)` ayarıyla yapılandırabilirsiniz. Talimat dosyalarını farklı bir klasörde tutmak veya daha iyi düzen için birden fazla klasör kullanmak istiyorsanız bu faydalıdır.

Claude Code ve diğer Claude tabanlı araçlarla uyumluluk için VS Code ayrıca `.claude/rules` çalışma alanı klasöründe ve `~/.claude/rules` kullanıcı klasöründe talimat dosyalarını algılar.

Aşağıdaki kod parçası, yalnızca çalışma alanı düzeyinde talimatların etkinleştirildiği ve kullanıcı düzeyinde talimatların devre dışı bırakıldığı talimat dosyası konumlarını nasıl yapılandıracağınızı gösterir:

```json
"chat.instructionsFilesLocations": {
  ".github/instructions": true,
  ".claude/rules": true,
  "~/.copilot/instructions": false,
  "~/.claude/rules": false
}
```

### Talimat dosyası formatı

Talimat dosyaları `.instructions.md` uzantılı Markdown dosyalarıdır. İsteğe bağlı YAML frontmatter başlığı talimatların ne zaman uygulanacağını kontrol eder:

| Alan | Gerekli | Açıklama |
|-------|----------|-------------|
| `name` | Hayır | UI'da gösterilen görünen ad. Varsayılan: dosya adı. |
| `description` | Hayır | Chat görünümünde fare ile üzerine gelindiğinde gösterilen kısa açıklama. |
| `applyTo` | Hayır | Talimatların otomatik uygulandığı dosyaları çalışma alanı köküne göre tanımlayan glob deseni. Tüm dosyalara uygulamak için `**` kullanın. Belirtilmezse talimatlar otomatik uygulanmaz—bunları bir sohbet isteğine manuel olarak ekleyebilirsiniz. |

Gövde Markdown formatında talimatları içerir. Ajan araçlarına atıfta bulunmak için `#tool:<tool-name>` sözdizimini kullanın (örneğin, `#tool:githubRepo`).

```markdown
---
name: 'Python Standards'
description: 'Coding conventions for Python files'
applyTo: '**/*.py'
---
# Python kodlama standartları
- PEP 8 stil rehberini takip edin.
- Tüm fonksiyon imzaları için tür ipuçları kullanın.
- Genel fonksiyonlar için docstring yazın.
- Girinti için 4 boşluk kullanın.
```

### Talimat dosyası oluşturma

Talimat dosyası oluşturduğunuzda çalışma alanınızda mı yoksa kullanıcı profilinizde mi saklayacağınızı seçin. Çalışma alanı talimat dosyaları yalnızca o çalışma alanına uygulanır; kullanıcı talimat dosyaları birden fazla çalışma alanında kullanılabilir.

Talimat dosyası oluşturmak için:

> [!TIP]
> **Talimat ve Kurallar Yapılandırması** menüsünü hızlıca açmak için sohbet girişinde `/instructions` yazın.

1. Chat görünümünde **Configure Chat** (dişli simgesi) > **Chat Instructions** seçin, ardından **New instruction file** seçin.

    ![Screenshot showing the Chat view, and Configure Chat menu, highlighting the Configure Chat button.](../images/customization/configure-chat-instructions.png)

    Alternatif olarak Komut Paleti'nden (`kb(workbench.action.showCommands)`) **Chat: New Instructions File** komutunu kullanın.

1. Talimat dosyasının oluşturulacağı konumu seçin.

    * **Çalışma alanı**: yalnızca o çalışma alanında kullanmak için talimat dosyasını çalışma alanının `.github/instructions` klasöründe oluşturun. Çalışma alanınız için daha fazla talimat klasörü eklemek için `setting(chat.instructionsFilesLocations)` ayarını kullanın.

    * **Kullanıcı profili**: tüm çalışma alanlarınızda kullanmak için talimat dosyalarını [mevcut profil klasöründe](/docs/configure/profiles.md) oluşturun.

1. Talimat dosyanız için bir dosya adı girin. Bu, UI'da kullanılan varsayılan addır.

1. Markdown biçimlendirmesi kullanarak özel talimatları yazın.

    * Talimatların açıklamasını, adını ve ne zaman uygulandığını yapılandırmak için dosyanın üst kısmındaki YAML frontmatter'ı doldurun.
    * Dosyanın gövdesine talimatlar ekleyin.

Mevcut bir talimat dosyasını değiştirmek için Chat görünümünde **Configure Chat** (dişli simgesi) > **Chat Instructions** seçin, ardından listeden bir talimat dosyası seçin. Alternatif olarak Komut Paleti'nden (`kb(workbench.action.showCommands)`) **Chat: Configure Instructions** komutunu kullanın ve Quick Pick'ten talimat dosyasını seçin.

### AI ile talimat dosyası oluşturma

Hedefli bir talimat dosyası oluşturmak için AI kullanabilirsiniz. Sohbette `/create-instruction` yazın ve uygulamak istediğiniz sözleşmeyi veya yönergeyi açıklayın (örneğin, "bu projede her zaman sekmeler ve tek tırnak kullanın"). Ajan açıklayıcı sorular sorar ve uygun `applyTo` deseni ve içerikle bir `.instructions.md` dosyası oluşturur.

Devam eden bir sohbetteki talimatları da çıkarabilirsiniz. Örneğin, ajanın import stilini bir sohbet oturumunda düzelttiyseniz, bu düzeltmeyi proje sözleşmesi olarak yakalamak için "extract an instruction from this" deyin.

> [!NOTE]
> `/create-instruction` hedefli, isteğe bağlı talimat dosyaları oluşturur. Çalışma alanı genelinde her zaman açık talimatlar oluşturmak için [`/init` komutu](#generate-custom-instructions-for-your-workspace) kullanın.

<details>
<summary>Örnek: Dil özel kodlama yönergeleri</summary>

Bu talimatların genel kodlama yönergeleri dosyasına nasıl atıfta bulunduğuna dikkat edin. Talimatları düzenli ve belirli konulara odaklı tutmak için birden fazla dosyaya ayırabilirsiniz.

```markdown
---
applyTo: "**/*.ts,**/*.tsx"
---
# TypeScript ve React için proje kodlama standartları

Tüm kod için [genel kodlama yönergelerini](./general-coding.instructions.md) uygulayın.

## TypeScript Yönergeleri
- Tüm yeni kod için TypeScript kullanın
- Mümkün olduğunca fonksiyonel programlama ilkelerini takip edin
- Veri yapıları ve tür tanımları için arayüzler kullanın
- Değişmez veriyi tercih edin (const, readonly)
- Opsiyonel zincirleme (?.) ve nullish birleştirme (??) operatörlerini kullanın

## React Yönergeleri
- Hook'larla fonksiyonel bileşenler kullanın
- React hook kurallarını takip edin (koşullu hook yok)
- Alt öğeleri olan bileşenler için React.FC türünü kullanın
- Bileşenleri küçük ve odaklı tutun
- Bileşen stillendirme için CSS modüllerini kullanın
```

</details>

<details>
<summary>Örnek: Dokümantasyon yazma yönergeleri</summary>

Dokümantasyon yazma dahil geliştirme dışı faaliyetler için farklı görev türleri için talimat dosyaları oluşturabilirsiniz.

```markdown
---
applyTo: "docs/**/*.md"
---
# Proje dokümantasyon yazma yönergeleri

## Genel Yönergeler
- Net ve öz dokümantasyon yazın.
- Tutarlı terim ve stil kullanın.
- Uygulanabilir yerlerde kod örnekleri ekleyin.

## Dil Bilgisi
* Geniş zaman fiilleri kullanın (is, open) geçmiş zaman yerine (was, opened).
* Gerçek ifadeler ve doğrudan komutlar yazın. "could" veya "would" gibi varsayımsal ifadelerden kaçının.
* Öznenin eylemi gerçekleştirdiği yerde aktif ses kullanın.
* Okuyuculara doğrudan hitap etmek için ikinci tekil şahıs (you) ile yazın.

## Markdown Yönergeleri
- İçeriği düzenlemek için başlıklar kullanın.
- Listeler için madde işaretleri kullanın.
- İlgili kaynaklara bağlantılar ekleyin.
- Kod parçaları için kod blokları kullanın.
```

</details>

Topluluk tarafından katkıda bulunulan daha fazla örnek için [Awesome Copilot deposuna](https://github.com/github/awesome-copilot/tree/main) bakın.

## `AGENTS.md` dosyası kullanın

VS Code, çalışma alanınızın kökündeki `AGENTS.md` Markdown dosyasını otomatik olarak algılar ve bu dosyadaki talimatları bu çalışma alanındaki tüm sohbet isteklerine uygular. Çalışma alanınızda birden fazla AI ajanıyla çalışıyorsanız ve hepsi tarafından tanınan tek bir talimat seti istiyorsanız veya monorepo'nun belirli bölümlerine uygulanan alt klasör düzeyinde talimatlar istiyorsanız bu faydalıdır.

`AGENTS.md` şu durumlarda kullanın:

* Birden fazla AI kodlama ajanıyla çalışıyorsunuz ve hepsi tarafından tanınan tek bir talimat seti istiyorsunuz
* Monorepo'nun belirli bölümlerine uygulanan alt klasör düzeyinde talimatlar istiyorsunuz

`AGENTS.md` dosya desteğini etkinleştirmek veya devre dışı bırakmak için `setting(chat.useAgentsMdFile)` ayarını yapılandırın.

### Birden fazla `AGENTS.md` dosyası kullanın (deneysel)

Projenizin farklı bölümlerine farklı talimatlar uygulamak istiyorsanız alt klasörlerde birden fazla `AGENTS.md` dosyası kullanmak faydalıdır. Örneğin, ön uç kodu için bir `AGENTS.md` dosyası ve arka uç kodu için başka bir dosyanız olabilir.

Çalışma alanınızda iç içe `AGENTS.md` dosyaları desteğini etkinleştirmek veya devre dışı bırakmak için deneysel `setting(chat.useNestedAgentsMdFiles)` ayarını kullanın.

Etkinleştirildiğinde VS Code, çalışma alanınızın tüm alt klasörlerinde `AGENTS.md` dosyalarını özyinelemeli olarak arar ve göreli yolunu sohbet bağlamına ekler. Ajan düzenlenen dosyalara göre hangi talimatları kullanacağına karar verebilir.

> [!TIP]
> Klasör özel talimatlar için farklı `applyTo` desenleriyle eşleşen birden fazla [`.instructions.md`](#use-instructionsmd-files) dosyası da kullanabilirsiniz.

## `CLAUDE.md` dosyası kullanın

VS Code `CLAUDE.md` dosyasını algılar ve `AGENTS.md` gibi her zaman açık talimatlar olarak uygular. Claude Code veya diğer Claude tabanlı araçları VS Code ile birlikte kullanıyorsanız ve hepsi tarafından tanınan tek bir talimat seti istiyorsanız bu faydalıdır.

VS Code `CLAUDE.md` dosyalarını şu konumlarda arar:

| Konum | Açıklama |
|----------|-------------|
| Çalışma alanı kökü | Çalışma alanınızın kökündeki `CLAUDE.md` |
| `.claude` klasörü | Çalışma alanınızdaki `.claude/CLAUDE.md` |
| Kullanıcı ana dizini | Tüm projelerde kişisel talimatlar için `~/.claude/CLAUDE.md` |
| Yerel varyant | Sürüm kontrolüne işlenmeyen yalnızca yerel talimatlar için `CLAUDE.local.md` |

`CLAUDE.md` dosya desteğini etkinleştirmek veya devre dışı bırakmak için `setting(chat.useClaudeMdFile)` ayarını yapılandırın.

> [!NOTE]
> `.claude/rules` talimat dosyaları için VS Code glob desenleri için `applyTo` yerine [Claude Rules formatını](https://code.claude.com/docs/en/memory#basic-structure) takip ederek `paths` özelliği kullanır. `paths` özelliği bir glob desenleri dizisi kabul eder ve atlandığında varsayılan olarak `**` (tüm dosyalar) kullanır.

## Çalışma alanınız için özel talimatlar oluşturun

VS Code çalışma alanınızı analiz edebilir ve kodlama uygulamalarınız ve proje yapınızla eşleşen her zaman açık özel talimatlar oluşturabilir. Bu talimatlar ardından çalışma alanındaki tüm sohbet isteklerine otomatik olarak uygulanır.

Talimat oluşturduğunuzda VS Code şu adımları gerçekleştirir:

1. Çalışma alanınızda `copilot-instructions.md` veya `AGENTS.md` dosyaları gibi mevcut AI sözleşmelerini keşfeder.
1. Proje yapınızı ve kodlama kalıplarınızı analiz eder.
1. Projenize özel kapsamlı çalışma alanı talimatları oluşturur.

### `/init` eğik çizgi komutunu kullanın

Çalışma alanınızı özel talimatlarla hazırlamanın en hızlı yolu sohbet giriş kutusuna `/init` eğik çizgi komutunu yazmaktır.

`/init` komutu katkıda bulunulan bir [prompt dosyası](/docs/copilot/customization/prompt-files.md) olarak uygulanır, dolayısıyla temel prompt'u değiştirerek davranışını özelleştirebilirsiniz.

### Komutla talimat oluşturma

Çalışma alanınız için özel talimatlar oluşturmak üzere bir komut kullanmak için:

1. Chat görünümünde **Configure Chat** (dişli simgesi) > **Generate Chat Instructions** seçin.

1. Oluşturulan talimat dosyasını inceleyin ve gerekli düzenlemeleri yapın.

## Ekipler arasında özel talimatları paylaşın

GitHub kuruluşunuz genelinde birden fazla çalışma alanı ve depo arasında özel talimatları paylaşmak için bunları GitHub kuruluşu düzeyinde tanımlayabilirsiniz.

VS Code, erişiminiz olan kuruluş düzeyinde tanımlanan özel talimatları otomatik olarak algılar. Bu talimatlar **Chat Instructions** menüsünde kişisel ve çalışma alanı talimatlarınızla birlikte gösterilir ve tüm sohbet isteklerine otomatik olarak uygulanır.

Kuruluş düzeyinde özel talimatların keşfini etkinleştirmek için `setting(github.copilot.chat.organizationInstructions.enabled)` ayarını `true` yapın.

GitHub dokümantasyonunda [kuruluşunuz için özel talimatlar ekleme](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-organization-instructions) hakkında bilgi edinin.

## Kullanıcı talimat dosyalarını cihazlar arasında senkronize edin

VS Code, [Ayarlar Senkronizasyonu](/docs/configure/settings-sync.md) kullanarak kullanıcı talimat dosyalarınızı birden fazla cihazda senkronize edebilir.

Kullanıcı talimat dosyalarınızı senkronize etmek için prompt ve talimat dosyaları için Ayarlar Senkronizasyonu etkinleştirin:

1. [Ayarlar Senkronizasyonu](/docs/configure/settings-sync.md) etkin olduğundan emin olun.

1. Komut Paleti'nden (`kb(workbench.action.showCommands)`) **Settings Sync: Configure** komutunu çalıştırın.

1. Senkronize edilecek ayarlar listesinden **Prompts and Instructions** seçin.

## Ayarlarda özel talimatlar belirtin

> [!NOTE]
> Ayarlar tabanlı talimat desteği gelecekte kaldırılabilir. Bunun yerine dosya tabanlı talimatları kullanmanızı öneriyoruz.

Kod incelemesi veya commit mesajı oluşturma gibi özel senaryolar için özel talimatları tanımlamak üzere VS Code ayarlarını kullanabilirsiniz. Genel kodlama talimatları için [dosya tabanlı talimatları](#types-of-instruction-files) kullanın.

<details>
<summary>Ayar referansı</summary>

| Talimat türü | Ayar adı |
|---------------------|--------------|
| Kod incelemesi | `setting(github.copilot.chat.reviewSelection.instructions)` |
| Commit mesajı oluşturma | `setting(github.copilot.chat.commitMessageGeneration.instructions)` |
| Pull request başlığı ve açıklaması oluşturma | `setting(github.copilot.chat.pullRequestDescriptionGeneration.instructions)` |
| Kod oluşturma (kullanımdan kaldırıldı)* | `setting(github.copilot.chat.codeGeneration.instructions)` |
| Test oluşturma (kullanımdan kaldırıldı)* | `setting(github.copilot.chat.testGeneration.instructions)` |

_\* VS Code 1.102 itibarıyla `codeGeneration` ve `testGeneration` ayarları kullanımdan kaldırıldı. Bunun yerine talimat dosyalarını (`.github/copilot-instructions.md` veya `*.instructions.md`) kullanın._

Özel talimatları ayar değerinde (`text` özelliği) metin olarak tanımlayabilir veya çalışma alanınızdaki harici bir dosyaya (`file` özelliği) atıfta bulunabilirsiniz.

Aşağıdaki kod parçası `settings.json` dosyasında bir talimat setinin nasıl tanımlanacağını gösterir.

```json
{
    "github.copilot.chat.pullRequestDescriptionGeneration.instructions": [
        { "text": "Always include a list of key changes." }
    ],
    "github.copilot.chat.reviewSelection.instructions": [
        { "file": "guidance/backend-review-guidelines.md" },
        { "file": "guidance/frontend-review-guidelines.md" }
    ]
}
```

</details>

## Talimat önceliği

Birden fazla tür özel talimat bulunduğunda hepsi AI'ya sağlanır. Çakışmalarda daha yüksek öncelikli talimatlar öncelik alır:

1. Kişisel talimatlar (kullanıcı düzeyi, en yüksek öncelik)
1. Depo talimatları (`.github/copilot-instructions.md` veya `AGENTS.md`)
1. Kuruluş talimatları (en düşük öncelik)

## Etkili talimat yazma ipuçları

* Talimatlarınızı kısa ve kendi kendine yeterli tutun. Her talimat tek, basit bir ifade olmalıdır. Birden fazla bilgi sağlamanız gerekiyorsa birden fazla talimat kullanın.

* Kuralların arkasındaki mantığı ekleyin. Talimatlar bir sözleşmenin _neden_ var olduğunu açıkladığında, AI sınır durumlarda daha iyi kararlar verir. Örneğin: "`moment.js` yerine `date-fns` kullanın — moment.js kullanımdan kaldırıldı ve paket boyutunu artırır."

* Tercih edilen ve kaçınılacak kalıpları somut kod örnekleriyle gösterin. AI, soyut kurallardan çok örneklere daha etkili yanıt verir.

* Açık olmayan kurallara odaklanın. Standart linter'lar veya biçimlendiricilerin zaten zorunlu kıldığı sözleşmeleri atlayın.

* Görev veya dil özel talimatlar için her konu için birden fazla `*.instructions.md` dosyası kullanın ve `applyTo` özelliğiyle bunları seçici olarak uygulayın.

* Proje özel talimatları ekip üyeleriyle paylaşmak ve sürüm kontrolüne dahil etmek için çalışma alanınızda saklayın.

* Talimat dosyalarınızı temiz ve odaklı tutmak ve talimat tekrarını önlemek için [prompt dosyalarınızda](/docs/copilot/customization/prompt-files.md) ve [özel ajanlarınızda](/docs/copilot/customization/custom-agents.md) yeniden kullanın ve bunlara atıfta bulunun.

* Talimatlar arasındaki boşluk yoksayılır; dolayısıyla talimatları okunabilirlik için tek paragraf, ayrı satırlar veya boş satırlarla ayrılmış olarak biçimlendirebilirsiniz.

## Sık sorulan sorular

### Talimat dosyam neden uygulanmıyor?

> [!TIP]
> Yüklenen tüm talimat dosyalarını ve hataları görmek için sohbet özelleştirme tanılamaları görünümünü kullanın. Chat görünümünde sağ tıklayın ve **Diagnostics** seçin. [VS Code'da AI sorun giderme](/docs/copilot/troubleshooting.md) hakkında daha fazla bilgi edinin.

Talimat dosyanız uygulanmıyorsa şunları kontrol edin:

* Talimat dosyanızın doğru konumda olduğunu doğrulayın. `.github/copilot-instructions.md` dosyası çalışma alanınızın kökündeki `.github` klasöründe olmalıdır. `*.instructions.md` dosyası `setting(chat.instructionsFilesLocations)` ayarında belirtilen klasörlerden birinde (varsayılan: `.github/instructions`) veya kullanıcı profilinizde olmalıdır.

* `*.instructions.md` dosyaları için `applyTo` glob deseninin üzerinde çalıştığınız dosyayla eşleştiğini kontrol edin. `applyTo` özelliği belirtilmezse talimat dosyası otomatik uygulanmaz. Hangi talimat dosyalarının kullanıldığını görmek için sohbet yanıtındaki **References** bölümünü doğrulayın.

* İlgili ayarların etkin olduğunu kontrol edin: desen tabanlı talimatlar için `setting(chat.includeApplyingInstructions)`, Markdown bağlantılarıyla referans verilen talimatlar için `setting(chat.includeReferencedInstructions)`, `AGENTS.md` dosyaları için `setting(chat.useAgentsMdFile)`.

Gelişmiş tanılamalar için [Chat Debug görünümünde dil modeli isteklerini kontrol edin](https://github.com/microsoft/vscode/wiki/Copilot-Issues#language-model-requests-and-responses) veya [`applyTo` eşleştirme mantığını hata ayıklayın](https://github.com/microsoft/vscode/wiki/Copilot-Issues#custom-instructions-logs).

### Özel talimat dosyasının nereden geldiğini nasıl anlarım?

Özel talimat dosyaları farklı kaynaklardan gelebilir: yerleşik, profilinizde kullanıcı tanımlı, mevcut çalışma alanınızda çalışma alanı tanımlı, kuruluş düzeyinde veya uzantı tarafından katkıda bulunulan.

Özel talimat dosyasının kaynağını belirlemek için:

1. Komut Paleti'nden (`kb(workbench.action.showCommands)`) **Chat: Configure Instructions** seçin.
1. Listede talimat dosyasının üzerine gelin. Kaynak konum bir ipucunda gösterilir.

Yüklenen tüm talimat dosyalarını ve hataları görmek için sohbet özelleştirme tanılamaları görünümünü kullanın. Chat görünümünde sağ tıklayın ve **Diagnostics** seçin. [VS Code'da AI sorun giderme](/docs/copilot/troubleshooting.md) hakkında daha fazla bilgi edinin.

## İlgili kaynaklar

* [Ajan Becerilerini kullanın](/docs/copilot/customization/agent-skills.md)
* [Özel ajanlar oluşturun](/docs/copilot/customization/custom-agents.md)
* [Topluluk tarafından katkıda bulunulan talimatlar, prompt'lar ve özel ajanlar](https://github.com/github/awesome-copilot)
