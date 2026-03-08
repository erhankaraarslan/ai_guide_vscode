---
ContentId: 3a6e8c1d-5f2b-4d9a-b7e1-9c4f2a8d6b3e
DateApproved: 3/4/2026
MetaDescription: Çalışma alanınıza, araçlarınıza ve modellerinize tam erişimle etkileşimli kodlama görevleri için VS Code'da yerel ajanları nasıl kullanacağınızı öğrenin.
MetaSocialImage: ../images/shared/github-copilot-social.png
Keywords:
- ai
- agents
- local agent
- chat
- copilot
---

# Visual Studio Code'da yerel ajanlar

Yerel ajanlar doğrudan VS Code içinde makinenizde çalışır. Promptlarınıza anında sonuç almak için sohbet üzerinden yerel ajanlarla etkileşim kurarsınız. Yerel ajanlar çalışma alanınızda çalışır ve VS Code'da mevcut araçların ve modellerin tam yelpazesine erişir. [Özel ajanlar oluşturarak](/docs/copilot/customization/custom-agents.md) ajanın kod inceleyicisi, testçi veya belge yazarı gibi görev için belirli bir rol veya kişilik üstlenmesini sağlayabilirsiniz.

Yerel ajanlar VS Code'daki sohbet arayüzünde çalışır. Bir sohbet oturumunu kapattığınızda yerel ajan etkin kalır ve oturumlar görünümünde takip edebilirsiniz.

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="Get started with agents">
VS Code'da yerel, arka plan ve bulut ajanlarını deneyimlemek için uygulamalı öğreticiyi izleyin.

* [Start tutorial](/docs/copilot/agents/agents-tutorial.md)

</div>

## Yerel ajanları neden kullanmalı?

* Beyin fırtınası, planlama veya henüz tam tanımlanmamış görevler gibi anında geri bildirim gerektiren etkileşimli görüşmeler
* Linter hataları, yığın izleri, birim test sonuçları gibi geliştirici ortamınızdan bağlam gerektiren görevler
* VS Code uzantılarından veya MCP sunucularından belirli araçlara erişim gerektiren veya BYOK modelleri gibi belirli modelleri kullanması gereken görevler
* Diğer ekip üyelerinden iş birliği gerektirmeyen görevler

## Temel özellikler

* Makinenizde VS Code içinde çalışır ve mevcut çalışma alanınızda çalışır
* Gerçek zamanlı geri bildirim ve yineleme için etkileşimli sohbet tabanlı arayüz
* Çalışma alanınıza, dosyalarınıza ve bağlama tam erişim
* Yerleşik araçlar, MCP araçları ve uzantı tarafından sağlanan araçlar dahil VS Code'da yapılandırılmış tüm ajan araçlarına erişebilir
* BYOK modelleri ve diğer sağlayıcılardan modeller dahil sizin için mevcut tüm modelleri kullanabilir

## Yerleşik ajanlar

Yerel ajan oturumları farklı görev türleri için optimize edilmiş üç yerleşik ajandan birini kullanır. Sohbet oturumu sırasında Sohbet görünümündeki ajan seçiciden farklı bir ajan seçerek istediğiniz zaman geçiş yapabilirsiniz. Daha uzmanlaşmış iş akışları için kendi [özel ajanlarınızı](/docs/copilot/customization/custom-agents.md) oluşturabilirsiniz.

### Agent

Agent karmaşık kodlama görevleri için optimize edilmiştir; terminal komutları ve araçlar çalıştırma gerektirebilecek üst düzey gereksinimlere dayalıdır. Yapay zeka özerk çalışır, ilgili bağlamı ve düzenlenecek dosyaları belirler, gereken işi planlar ve sorunları çözmek için yineler.

VS Code kod değişikliklerini doğrudan editörde uygular ve editör yer paylaşımı kontrolleri önerilen düzenlemeler arasında gezinmenize ve incelemenize olanak tanır. Ajan farklı görevleri tamamlamak için birden fazla [araç](/docs/copilot/agents/agent-tools.md) çağırabilir.

MCP sunucuları ekleyerek veya araç katkıda bulunan uzantılar yükleyerek [sohbeti ek araçlarla özelleştirebilirsiniz](/docs/copilot/agents/agent-tools.md).

Agent ile sohbet açın: [Stable](vscode://GitHub.Copilot-Chat/chat?mode=agent) | [Insiders](vscode-insiders://GitHub.Copilot-Chat/chat?mode=agent)

> [!IMPORTANT]
> Ajan seçeneğini görmüyorsanız VS Code ayarlarınızda ajanların etkin olduğundan emin olun (`setting(chat.agent.enabled)`). Kuruluşunuz ajanları devre dışı bırakmış olabilir. Bu işlevi etkinleştirmek için yöneticinizle iletişime geçin.

### Plan

Plan ajanı kodlama görevinde yapılandırılmış bir uygulama planı oluşturmak için optimize edilmiştir. Karmaşık bir özelliği veya değişikliği uygulamadan önce daha küçük, yönetilebilir adımlara bölmek istediğinizde plan ajanını kullanın.

Plan ajanı gereken adımların bir dökümünü içeren ayrıntılı bir plan oluşturur ve kapsamlı anlayış sağlamak için açıklayıcı sorular sorar. Ardından planı bir uygulama ajanına devredebilir veya rehber olarak kullanabilirsiniz.

Plan ile sohbet açın: [Stable](vscode://GitHub.Copilot-Chat/chat?mode=plan) | [Insiders](vscode-insiders://GitHub.Copilot-Chat/chat?mode=plan)

[Ajanlarla planlama](/docs/copilot/agents/planning.md) hakkında daha fazla bilgi edinin.

### Ask

Ask özelliği kod tabanınız, kodlama ve genel teknoloji kavramları hakkındaki soruları yanıtlamak için en uygundur. Bir şeyin nasıl çalıştığını anlamak, fikirleri keşfetmek veya kodlama görevlerinde yardım almak istediğinizde Ask kullanın.

Ask kod tabanınızı araştırmak ve ilgili bağlamı toplamak için ajanik yetenekler kullanır. Yanıtlar kod tabanınıza tek tek uygulayabileceğiniz kod blokları içerebilir. Kod bloğu uygulamak için kod bloğunun üzerine gelin ve **Apply in Editor** düğmesini seçin.

Ask ile sohbet açın: [Stable](vscode://GitHub.Copilot-Chat/chat?mode=ask) | [Insiders](vscode-insiders://GitHub.Copilot-Chat/chat?mode=ask)

### Edit modu (gizli)

Edit _modu_ çoklu dosya kod düzenlemesi için optimize edilmiştir. VS Code kod değişikliklerini doğrudan editörde uygular ve değişiklikleri inceleyip kabul etmenize olanak tanır.

Edit modu kuruluşunuz Agent modunu devre dışı bırakmadıkça varsayılan olarak ajan seçicide gizlidir. Edit modunu geri yüklemek için `setting(chat.editMode.hidden)` ayarını devre dışı bırakabilirsiniz.

## Başlarken

> [!TIP]
> Arka plan ve bulut ajanları dahil farklı ajan türleriyle çalışmayı gösteren uygulamalı öğretici için [ajanlar öğreticisine](/docs/copilot/agents/agents-tutorial.md) bakın.

Yerel ajan oturumu başlatmak için:

1. Sohbet görünümündeki ajan seçiciden **Agent** seçin.

1. Sohbet giriş alanına üst düzey bir prompt yazın. Örneğin şunları sorabilirsiniz:

    ```prompt-agent
    Implement a user authentication system with OAuth2 and JWT.
    ```

    veya

    ```prompt-agent
    Set up a CI/CD pipeline for this project.
    ```

1. Ajana daha fazla yetenek vermek için araç seçiciden [araçları etkinleştirin](/docs/copilot/agents/agent-tools.md).

1. Promptunuzu göndermek için **Send** seçin veya `kb(workbench.action.chat.submit)` tuşuna basın.

1. Ajan isteğiniz üzerinde çalışırken kod değişikliklerini ve araç çağrılarını inceleyin ve onaylayın.

    Ajan çalışırken takip promptları gönderebilirsiniz. Sıraya almak, ajanı yeni yöne yönlendirmek veya durdurup hemen göndermek için mesajları sıraya alın. [İstek çalışırken mesaj gönderme](/docs/copilot/chat/chat-sessions.md#send-messages-while-a-request-is-running) hakkında daha fazla bilgi edinin.

    > [!TIP]
    > VS Code çalışma alanı yapılandırma ayarları veya ortam ayarları gibi hassas dosyalara yanlışlıkla düzenlemelere karşı koruma sağlar. [Hassas dosyaları düzenleme](/docs/copilot/chat/review-code-edits.md#edit-sensitive-files) hakkında daha fazla bilgi edinin.

Ask ile başlamak için:

1. Sohbet giriş alanına promptunuzu yazın. Örneğin şunları sorabilirsiniz:

    ```prompt-ask
    Provide 3 ways to implement a search feature in React.
    ```

    veya

    ```prompt-ask
    Where is the db connection configured in this project? #codebase
    ```

1. Sohbet görünümündeki ajan seçiciden **Ask** seçin.

1. İsteğe bağlı olarak daha doğru yanıtlar almak için [promptunuza bağlam ekleyin](/docs/copilot/chat/copilot-chat-context.md).

1. Promptunuzu göndermek için **Send** seçin veya `kb(workbench.action.chat.submit)` tuşuna basın.

## İlgili kaynaklar

* [Ajanlara genel bakış](/docs/copilot/agents/overview.md): Ajan türleri ve oturum yönetimine genel bakış.
* [Ajanlar öğreticisi](/docs/copilot/agents/agents-tutorial.md): Farklı ajan türleriyle çalışma için uygulamalı öğretici.
* [Araçlar](/docs/copilot/agents/agent-tools.md): Ajanları yerleşik, MCP ve uzantı araçlarıyla genişletin.
* [Özel ajanlar](/docs/copilot/customization/custom-agents.md): Kendi yapay zeka ajanlarınızı ve uzantılarınızı oluşturun.
* [Sohbet](/docs/copilot/chat/copilot-chat.md): Sohbet arayüzü ve etkileşim özellikleri hakkında bilgi edinin.
