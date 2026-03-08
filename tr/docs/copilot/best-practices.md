---
ContentId: 58ea6755-9bfa-42c2-a4c8-ff0510f9c031
DateApproved: 3/4/2026
MetaDescription: VS Code'da GitHub Copilot'tan en iyi şekilde yararlanmak için istem yazmaktan projenizi AI için yapılandırmaya kadar kanıtlanmış uygulamalar.
MetaSocialImage: images/shared/github-copilot-social.png
---
# VS Code'da AI kullanımı için en iyi uygulamalar

Bu makale Visual Studio Code'da AI kullanımından en iyi şekilde yararlanmak için kanıtlanmış uygulamaları kapsar. Her bölüm daha derin dokümantasyona bağlantılarla uygulanabilir rehberlik sunar.

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="How AI works in VS Code">
Ajan döngüsü, bağlam penceresi, araçlar ve diğer temel kavramlar hakkında bilgi edinin.

* [Temel kavramları okuyun](/docs/copilot/core-concepts.md)

</div>

## Projenizi AI için optimize edin

Projenizi ve kod tabanınızı AI'ı göz önünde bulundurarak yapılandırarak AI yanıtlarının doğruluğunu artırabilir ve AI'ın ekibinizin kodlama standartlarına ve uygulamalarına uymasını sağlayabilirsiniz.

VS Code projeniz için AI davranışını yapılandırmak üzere birkaç mekanizma destekler. Başlangıç yapılandırması oluşturmak için sohbete `/init` yazın.

| Mekanizma | En iyi kullanım | Başlarken |
|-----------|-----------------|------------|
| [Özel talimatlar](/docs/copilot/customization/custom-instructions.md) | Proje genelinde kodlama standartları ve mimari bağlam | Temel dosya oluşturmak için `/init` yazın |
| [Prompt dosyaları](/docs/copilot/customization/prompt-files.md) | Tekrarlayan görevler için yeniden kullanılabilir istemler (incelemeler, iskele) | Yönetmek için `/prompts` yazın |
| [Özel ajanlar](/docs/copilot/customization/custom-agents.md) | Özelleştirilmiş iş akışları veya kişilikler (TDD, güvenlik denetimi) | Yönetmek için `/agents` yazın |
| [Ajan becerileri](/docs/copilot/customization/agent-skills.md) | Etki alanına özgü yetenekler (test, dağıtım) | Yönetmek için `/skills` yazın |
| [Araçlar ve MCP sunucuları](/docs/copilot/agents/agent-tools.md) | Harici sistemlere bağlanma (veritabanları, API'ler, CLI'lar) | `mcp.json` içinde yapılandırın |

Etkili proje yapılandırması ipuçları:

* **Talimat dosyalarını kısa tutun.** Her sohbet etkileşiminde yüklenirler. AI'ın koddan çıkaramayacağı bilgilere odaklanın: varsayılan olmayan sözleşmeler, mimari kararlar veya ortam kurulumu gibi.
* **`applyTo` desenleriyle talimatları kapsamlayın.** Her şeyi tek dosyaya koymak yerine dil özelinde veya klasör özelinde talimat dosyaları oluşturmak için `/instructions` yazın.
* **Etkin araçları sınırlayın.** Daha az etkin araç daha hızlı, daha ilgili yanıtlar anlamına gelir. Görev gerektirdiğinde yalnızca araçları etkinleştirin.

Tam kurulum detayları için [özelleştirme genel bakışı](/docs/copilot/customization/overview.md)'na bakın.

## Görev için doğru aracı seçin

VS Code'da AI birkaç etkileşim modu sunar. Elinizdeki görev için doğru olanı seçmek zaman kazandırır ve daha iyi sonuçlar üretir.

| Araç | En iyi kullanım | Örnek |
|------|-----------------|-------|
| [Satır içi öneriler](/docs/copilot/ai-powered-suggestions.md) | Kod yazarken akışta kalmak | Kod tamamlamaları, değişken adları, şablon |
| [Ask (chat)](/docs/copilot/chat/copilot-chat.md) | Sorular, beyin fırtınası, fikirleri keşfetme | "Bu projede kimlik doğrulama nasıl çalışır?" |
| [Inline chat](/docs/copilot/chat/inline-chat.md) | Bağlam değiştirmeden hedefli, yerinde düzenlemeler | Bir fonksiyonu yeniden düzenleme, hata işleme ekleme |
| [Ajanlar](/docs/copilot/agents/overview.md) | Otonom planlama ve araç kullanımı gerektiren çok dosyalı değişiklikler | Bir özelliği uçtan uca uygulama |
| [Plan](/docs/copilot/agents/planning.md) | Uygulamadan önce yapılandırılmış planlama | Mimari veya geçiş stratejisi tasarlama |
| [Akıllı eylemler](/docs/copilot/copilot-smart-actions.md) | Yerleşik, özelleştirilmiş tek adımlı görevler | Commit mesajı oluşturma, hataları düzeltme, sembolleri yeniden adlandırma |

## Etkili istemler yazın

AI yanıtlarının kalitesi isteminizin netliğine ve özgüllüğüne bağlıdır. Bu teknikler daha iyi sonuçlar almanıza yardımcı olur.

* **Girişler, çıkışlar ve kısıtlamalar konusunda belirli olun.** Kullanmak istediğiniz programlama dilini, framework'leri ve kütüphaneleri belirtin. Beklenen davranışı tanımlayın veya örnek giriş ve çıkış ekleyin.

    ```prompt
    Write a TypeScript function that validates email addresses.
    Return true for valid addresses, false otherwise. Don't use regex.
    Example: validateEmail("user@example.com") returns true
    Example: validateEmail("invalid") returns false
    ```

* **Karmaşık görevleri parçalayın.** Tüm bir özelliği bir seferde istemek yerine, daha küçük, iyi kapsamlı adımlara ayırın. Bu yaklaşım daha güvenilir sonuçlar üretir ve sorunları erken yakalamayı kolaylaştırır.

* **Doğrulama için beklenen çıktı ekleyin.** AI'ın kendi işini doğrulayabilmesi için test senaryoları, beklenen sonuçlar veya kabul kriterleri sağlayın. Bu adım yapabileceğiniz en yüksek kaldıraçlı şeylerden biridir.

    ```prompt
    Implement a rate limiter using the token bucket algorithm.
    Write unit tests that verify: 10 requests/second allowed,
    11th request rejected, bucket refills after 1 second.
    Run the tests after implementing.
    ```

* **Belirsiz istemlerden kaçının.** "Make this better" gibi bir istem AI'a yön vermez. Bunun yerine "better"ın ne anlama geldiğini belirtin: "reduce the time complexity" veya "add input validation for null values."

* **Takip istemleriyle yineleyin.** Tüm istemi yeniden yazmak yerine takip mesajlarında kısıtlamalar veya düzeltmeler ekleyerek yanıtları iyileştirin.

* **Erken yön düzeltin.** AI yanlış yöne gidiyorsa, mevcut isteği yönlendirmek, takip isteğini sıraya almak veya durdurup yeni istem göndermek için [takip mesajıyla yönlendirin](/docs/copilot/chat/chat-sessions.md#send-messages-while-a-request-is-running).

* **AI'a netleştirme soruları sormasını söyleyin.** Görev belirsizse, devam etmeden önce size sorular sormasını talep edin. Bu, gereksinimlerde tahmin yürütmekten daha doğru sonuçlara yol açar.

* **Paralel görevler.** Birden fazla bağımsız göreviniz varsa zaman kazanmak için AI'dan bunları paralel çalıştırmasını isteyin. Örneğin, "X ve Y hakkında izole araştırma paralel yapın ve bulguları özetleyin."

Daha fazla bilgi için [istem mühendisliği](/docs/copilot/guides/prompt-engineering-guide.md) bölümüne bakın ve GitHub Copilot dokümantasyonunda pratik [istem örnekleri](https://docs.github.com/en/copilot/copilot-chat-cookbook) bulun.

## Doğru bağlamı sağlayın

AI ilgili bağlama sahip olduğunda daha doğru yanıt verir. AI'ı doğru bilgiye yönlendirmek için bu teknikleri kullanın:

* AI ilgili bağlamı toplamak için otomatik olarak kod araması yapar. İsteminiz belirsiz olduğunda istemde `#<file>`, `#<folder>` veya `#<symbol>` ile belirli dosyalara, klasörlere veya sembollere referans vererek AI'ı yönlendirebilirsiniz.

* Web sayfalarından veya GitHub depolarından bilgi çekmek için kod tabanınızın ötesinde güncel bilgi sağlamak üzere AI için `#fetch` veya `#githubRepo` kullanın.

* Kaynak kontrol değişiklikleri, terminal çıktısı veya test hataları gibi VS Code ortam bağlamına referans vererek AI'ın projenizin mevcut durumunu anlamasına ve daha ilgili yanıtlar vermesine yardımcı olun.

* AI'ın görsel içeriği analiz etmesi için görüntü veya ekran görüntüleri ekleyin.

* Uygulamanızı önizlemek ve bağlam olarak kullanılacak sayfa öğelerini seçmek için [entegre tarayıcıyı](/docs/debugtest/integrated-browser.md) kullanın.

Daha fazla bilgi için [sohbet istemlerine bağlam ekleme](/docs/copilot/chat/copilot-chat-context.md) ve [araçları yapılandırma](/docs/copilot/agents/agent-tools.md) bölümlerine bakın.

## Doğru modeli seçin

Her AI modelinin farklı güçlü yönleri vardır. Bazıları akıl yürütmede daha iyi, diğerleri kod üretimi veya daha hızlı yanıtlar sunuyor. Göreviniz için doğru modeli seçmek sonuçları iyileştirir.

* **Görev karmaşıklığına model eşleştirin.** Basit tamamlamalar ve şablon için hızlı modeller kullanın. Planlama, hata ayıklama veya mimari kararlar için akıl yürütme optimize modellere geçin.

* **En son modelleri kullanın.** Yeni modeller genellikle geliştirilmiş yeteneklere sahiptir. VS Code sürekli yeni modellere ve model sürümlerine destek ekler. [Mevcut modelleri](/docs/copilot/customization/language-models.md) kontrol edin ve en son modelleri kullanın.

* **İstem dosyalarında ve ajanlarda modelleri sabitleyin.** Belirli görevler için tutarlı doğru model kullanımını sağlamak için prompt dosyanızda veya özel ajan tanımlarınızda tercih edilen modelleri belirtin.

* **Deneyin ve karşılaştırın.** Bir yanıttan memnun değilseniz farklı bir model deneyin. Farklı modeller aynı istem için önemli ölçüde farklı sonuçlar üretebilir.

* **Ek kontrol için BYOK kullanın.** Daha fazla model seçeneği ve barındırma seçeneği için kendi API anahtarınızı getirin.

Daha fazla bilgi için [AI modelleri seçme](/docs/copilot/customization/language-models.md) ve [Copilot Chat için mevcut modeller](https://docs.github.com/en/copilot/using-github-copilot/ai-models/changing-the-ai-model-for-copilot-chat) bölümlerine bakın.

## Önce planlayın, sonra uygulayın

Birden fazla dosyayı kapsayan karmaşık değişiklikler için planlamayı uygulamadan ayırın. Bu yaklaşım AI'ın yanlış sorunu çözmesini önler.

1. **Keşfedin.** Değişiklik yapmadan önce ilgili kodu okumak ve nasıl çalıştığını anlamak için ask modu veya alt ajan kullanın.
1. **Planlayın.** Yapılandırılmış uygulama planı oluşturmak için [Plan ajanını](/docs/copilot/agents/planning.md) kullanın. Yürütmeden önce planı inceleyin ve iyileştirin.
1. **Uygulayın.** Ajan moduna geçin ve plandan uygulayın. Ajanın kendi işini doğrulayabilmesi için testler veya beklenen çıktılar ekleyin. Daha uzun görevler için [arka plan ajanına](/docs/copilot/agents/background-agents.md) veya [bulut ajanına](/docs/copilot/agents/cloud-agents.md) devredin.
1. **İnceleyin.** İlerlemeyi incelemek, ajan sapırsa geri sarmak veya ortaya çıkan pull request üzerinde [Copilot kod incelemesi istemek](https://docs.github.com/en/copilot/concepts/agents/code-review) için [kontrol noktalarını](/docs/copilot/chat/chat-checkpoints.md) kullanın.

Daha fazla bilgi için [bağlam mühendisliği iş akışı](/docs/copilot/guides/context-engineering-guide.md)'na bakın.

## AI çıktısını inceleyin ve doğrulayın

AI ile üretilen kod hata, güvenlik sorunu veya ince mantık hataları içerebilir. AI çıktısını her zaman inceleme gerektiren bir başlangıç noktası olarak görün.

* **Kabul etmeden önce inceleyin.** Üretilen kodu kabul etmeden önce okuyun. Kenar durumlarına, hata işlemeye ve AI'ın yapmış olabileceği varsayımlara dikkat edin.

* **AI değişikliklerinden sonra testleri çalıştırın.** AI'ın kendi işini doğrulayabilmesi için isteminizde test senaryoları ekleyin. AI otomatik test çalıştırmıyorsa devam etmeden önce kendiniz çalıştırın.

* **Geri sarmak için kontrol noktaları kullanın.** Ajan sapırsa zincirleme hataları düzeltmeye çalışmak yerine bilinen iyi bir duruma geri dönmek için [kontrol noktalarını](/docs/copilot/chat/chat-checkpoints.md) kullanın.

* **Güvenlik sorunlarını kontrol edin.** AI ile üretilen kodu enjeksiyon açıkları, sabitlenmiş gizliler veya eksik giriş doğrulaması gibi yaygın güvenlik açıkları için inceleyin. İstemlere kimlik bilgisi veya hassas veri yapıştırmaktan kaçının.

Daha fazla bilgi için [GitHub Copilot güvenliği](/docs/copilot/security.md) ve [GitHub Copilot Güven Merkezi](https://copilot.github.trust.page/faq)'ne bakın.

## Bağlamı ve oturumları yönetin

Sohbet ilgisiz bağlamla doldukça AI yanıtları bozulabilir. Oturumlarınızı proaktif yönetin.

* **İlgisiz görevler için yeni oturumlar başlatın.** İlgisiz soruları tek sohbette biriktirmeyin. Bağlam kirlenmesi yanıt kalitesini düşürür.

* **İlgisiz geçmişi kaldırın.** Artık ilgili olmayan geçmiş soru ve yanıtları silin veya yeni bir oturum başlatın.

* **Araştırma için alt ajanları kullanın.** Ana bağlamınızı kirletmemesi için [alt ajanları](/docs/copilot/agents/subagents.md) kullanarak AI'a araştırma ve keşfi izole yapmasını ima edin.

* **Doğru oturum türünü seçin.** Mevcut kodunuzda hemen dikkatinizi gerektiren hızlı görevler için yerel oturumlar, ana bağlamınızdan izole yerel çalışabilecek görevler için arka plan görevleri veya ekip işbirliğinden yararlanabilecek bulut oturumları kullanın.

* **Paralel oturumlarla ölçeklendirin.** Bağımsız görevler için zaman kazanmak ve bağlamları ayırmak için paralel oturumlar çalıştırın. Yerel, arka plan ve bulut ortamlarında aynı anda birden fazla oturum çalıştırabilir ve VS Code'daki [Agent Sessions görünümü](/docs/copilot/agents/overview.md#agent-sessions-list) üzerinden aralarında geçiş yapabilirsiniz.

Daha fazla bilgi için [oturum yönetimi](/docs/copilot/chat/chat-sessions.md) ve [çalışma alanı indekslemesi](/docs/copilot/reference/workspace-context.md)'na bakın.

## Büyük kod tabanlarıyla çalışın

Copilot büyük, karmaşık ve çok köklü çalışma alanlarıyla etkili çalışacak şekilde tasarlanmıştır. Ölçekte en iyi sonuçlar için bu uygulamaları kullanın.

* **Çalışma alanı indekslemesini kullanın.** VS Code semantik arama, dil zekası ve GitHub kod araması kullanarak projenizi otomatik indeksler; derin dosyalar arası akıl yürütme için. Bu hem küçük projeler hem de büyük kurumsal kod tabanları için çalışır. Büyük depolar için GitHub'daki deponuz ve ilgili depolar genelinde hızlı, kapsamlı sonuçlar için [uzak indeksleme](/docs/copilot/reference/workspace-context.md#remote-index) kullanın.

* **Çok köklü çalışma alanlarıyla işi kapsamlayın.** Monorepo'lar veya birden fazla hizmetli projeler için AI'a net sınırlar ve odaklı bağlam vermek üzere [çok köklü çalışma alanlarını](/docs/editing/workspaces/multi-root-workspaces.md) kullanın.

* **Proje düzeyinde talimatlar sağlayın.** AI'ın koddan tek başına çıkaramayacağı projenizin mimarisini, modül sınırlarını ve sözleşmeleri tanımlamak için [özel talimatları](/docs/copilot/customization/custom-instructions.md) kullanın. Bu AI'a mimari düzeyinde değişiklikler için ihtiyaç duyduğu bağlamı verir.

* **Bağımsız değişiklikler için paralel oturumlar çalıştırın.** Büyük görevleri bağımsız alt görevlere bölün ve her biri kod tabanının farklı bir alanına odaklanan [paralel ajan oturumlarında](/docs/copilot/agents/overview.md#agent-sessions-list) çalıştırın.

* **Kesişen değişiklikler için Plan ajanını kullanın.** Birçok dosyayı veya modülü kapsayan değişiklikler için yürütmeden önce yapılandırılmış uygulama planı oluşturmak üzere [Plan ajanıyla](/docs/copilot/agents/planning.md) başlayın.

Daha fazla bilgi için [çalışma alanı bağlamı](/docs/copilot/reference/workspace-context.md) ve [ajanlar](/docs/copilot/agents/overview.md) bölümlerine bakın.

## İlgili kaynaklar

* [İstem mühendisliği rehberi](/docs/copilot/guides/prompt-engineering-guide.md)
* [Bağlam mühendisliği rehberi](/docs/copilot/guides/context-engineering-guide.md)
* [Özelleştirme genel bakışı](/docs/copilot/customization/overview.md)
* [Kopya kağıdı](/docs/copilot/reference/copilot-vscode-features.md)
* [GitHub Copilot güvenliği](/docs/copilot/security.md)
* GitHub Copilot dokümantasyonunda [GitHub Copilot kullanımı için En İyi Uygulamalar](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)
