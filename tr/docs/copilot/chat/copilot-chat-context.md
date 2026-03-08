---
ContentId: 5d8a707d-a239-4cc7-92ee-ccc763e8eb9c
DateApproved: 3/4/2026
MetaDescription: VS Code'da AI kullanırken çalışma alanı indekslemesi, dosya ve semboller için #-bahsetmeler, web içerik referansları ve özel talimatlar dahil bağlam yönetimini öğrenin.
MetaSocialImage: ../images/shared/github-copilot-social.png
---
# AI için bağlam yönetimi

Doğru bağlamı sağlayarak VS Code'daki AI'dan daha ilgili ve doğru yanıtlar alabilirsiniz. Bu makalede sohbette bağlam yönetimini, dosya, klasör ve sembollere referans vermek için #-bahsetmelerin nasıl kullanılacağını, web içeriğine nasıl referans verileceğini veya AI yanıtlarını yönlendirmek için özel talimatların nasıl kullanılacağını öğreneceksiniz.

## Çalışma alanı indekslemesi

VS Code ilgili kod parçalarını hızlı ve doğru aramak için kod tabanınızı indeks kullanır. Bu indeks GitHub tarafından tutulabilir veya makinenizde yerel olarak saklanabilir.

Aşağıdaki çalışma alanı indeksleme seçenekleri mevcuttur:

* **Uzak indeks**: Kodunuz bir GitHub deposunda barındırılıyorsa büyük kod tabanları için bile kod tabanınızı hızlı aramak üzere uzak indeks oluşturabilirsiniz.
* **Yerel indeks**: Kod tabanınız için hızlı ve doğru arama sonuçları sağlamak üzere makinenizde saklanan gelişmiş semantik indeks kullanın.
* **Temel indeks**: Yerel indeksleme mevcut değilse daha büyük kod tabanları için yerel çalışacak şekilde optimize edilmiş daha basit algoritmalar kullanabilirsiniz.

[Çalışma alanı indekslemesi](/docs/copilot/reference/workspace-context.md) hakkında daha fazla bilgi edinin.

## Örtülü bağlam

VS Code mevcut etkinliğinize dayalı olarak chat istemine otomatik bağlam sağlar. Aşağıdaki bilgiler chat bağlamına örtülü olarak dahil edilir:

* Etkin editörde şu anda seçili metin.
* Etkin editörün dosya adı veya notebook adı.
* **Ask** ajanını kullanıyorsanız etkin dosya otomatik olarak bağlam olarak dahil edilir.
* **Agent** kullanırken isteminize göre etkin dosyanın chat bağlamına eklenip eklenmeyeceğini otonom karar verir.

![Chat giriş kutusunda etkin dosyayı önerilen bağlam öğesi olarak gösteren Chat görünümü ekran görüntüsü.](./images/copilot-chat/chat-context-current-file.png)

## #-bahsetmeler

Bahsetmek istediğiniz bağlam öğesinin ardından `#` yazarak isteminize açıkça bağlam ekleyebilirsiniz. VS Code farklı bağlam öğesi türlerini destekler: dosyalar, klasörler, kod sembolleri, araçlar, terminal çıktısı, kaynak kontrol değişiklikleri ve daha fazlası.

Mevcut bağlam öğelerinin listesini görmek için chat giriş alanına `#` sembolünü yazın veya bağlam seçicisini açmak için Chat görünümünde **Add Context** seçin.

![VS Code Chat görünümünü, chat değişken seçicisini göstererek.](./images/copilot-chat/copilot-chat-view-chat-variables.png)

[Desteklenen bağlam öğelerinin](/docs/copilot/reference/copilot-vscode-features.md#chat-tools) tam listesini görüntüleyin.

### Dosyaları bağlam olarak ekleyin

Belirli dosyaları, klasörleri veya sembolleri bağlam olarak sağlamak için şu yöntemlerle bunları sohbete ekleyin:

* Chat mesajınızda dosyayı, klasörü veya sembolü #-bahsetmeyle `#` ardından dosya, klasör veya sembol adı yazarak referans verin.
    Bir sembole referans vermek için önce sembolü içeren dosyayı editörde açın.

* Explorer görünümünden, Search görünümünden veya editör sekmelerinden dosya veya klasörleri sürükleyip Chat görünümüne bırakarak bağlam olarak ekleyin.

* Chat görünümünde **Add Context** seçin ve Hızlı Seçim'den **Files & Folders** veya **Symbols** seçin.

> [!NOTE]
> Mümkünse dosya eklendiğinde dosyanın tam içeriği dahil edilir. Bağlam penceresine sığmayacak kadar büyükse uygulamaları olmadan fonksiyonlar ve açıklamaları içeren dosya özeti dahil edilir. Özet de çok büyükse dosya istemin parçası olmaz.

### Kod tabanı araması yapın

Dosyaları tek tek manuel eklemek yerine VS Code'un kod tabanınızdan doğru dosyaları otomatik bulmasını sağlayabilirsiniz. Hangi dosyaların sorunuzla ilgili olduğunu bilmediğinizde kullanışlıdır.

Çalışma alanınız için kod aramasını etkinleştirmek üzere isteminize `#codebase` ekleyin veya **Add Context** > **Tools** > **codebase** seçin.

Aşağıdaki istem örnekleri kod tabanı aramasının nasıl kullanılacağını gösterir:

* `"Explain how authentication works in #codebase"`
* `"Where is the database connection string configured? #codebase"`
* `"Add a new API route for updating the address #codebase"`

[Ajanları](/docs/copilot/agents/local-agents.md) kullanıyorsanız ajan sorunuzu yanıtlamak için ek bağlam gerektiğini belirlediğinde otomatik olarak kod tabanı araması kullanır. Sorunuzun farklı yorumlanabileceğinden eminseniz ve ajanın kod tabanı araması kullandığından emin olmak istiyorsanız yine de `#codebase` ekleyebilirsiniz.

### Web'den içerik referans verin

Sohbet istemlerinizde web'den içerik referans verebilirsiniz; örneğin en son API referansı veya kod örnekleri almak için.

* `#fetch <URL>`

    Belirli bir web sayfasından içerik almak için `fetch` aracını kullanın. Bu aracı kullanmak için `#fetch` ardından referans vermek istediğiniz sayfanın URL'sini yazın.

    `fetch` aracı performansı artırmak için web sayfasının içeriğini sınırlı süre önbelleğe alır. Sayfa içeriği değişirse VS Code'u yeniden başlatarak yenilemeyi zorlayabilirsiniz. Sayfaya ulaşılamazsa önbellek kısa süre sonra (yaklaşık beş dakika) sona erer.

    VS Code gizliliğinizi ve güvenliğinizi korumak için harici URL'lere erişmeden önce onay ister. [URL otomatik onayını yapılandırma](/docs/copilot/agents/agent-tools.md#url-approval) hakkında daha fazla bilgi edinin.

    `fetch` aracını kullanan örnek istemler:

    * `"What are the highlights of VS Code 1.100 #fetch https://code.visualstudio.com/updates/v1_100"`
    * `"Update the asp.net app to .net 9 #fetch https://learn.microsoft.com/en-us/aspnet/core/migration/80-90"`

* `#githubRepo <repo adı>`

    GitHub deposunda kod araması yapmak için `githubRepo` aracını kullanın. Depo adının ardından `#githubRepo` yazın.

    `githubRepo` aracını kullanan örnek istemler:

    * `"How does routing work in next.js #githubRepo vercel/next.js"`
    * `"Perform a code review to validate it's consistent with #githubRepo microsoft/typescript"`

### Araçlara referans verin

Ajanları kullanırken ajan belirli görevleri gerçekleştirmek için araçları kullanmaya otonom karar verir. Sohbet isteminizde bir araca açıkça referans vermek istiyorsanız #-bahsetmeleri kullanabilirsiniz. Araç adı ve isteğe bağlı parametrelerin ardından `#` yazın:

* `"Summarize #fetch https://code.visualstudio.com/updates"`
* `"How does routing work? #githubRepo vercel/next.js"`
* `"what are my open issues #github-mcp"` (GitHub MCP sunucusundan araçları kullanın)

Bir araç setine veya MCP sunucusuna adıyla referans verirseniz, o set veya sunucudaki tüm araçlar mevcut istem için ajana kullanılabilir hale gelir.

[Chat'te araç ekleme ve kullanma](/docs/copilot/agents/agent-tools.md) hakkında daha fazla bilgi edinin.

## @-bahsetmeler

Chat katılımcıları sohbette etki alanına özgü sorular sormanızı sağlayan özelleştirilmiş asistanlardır. Bir chat katılımcısını, chat isteğinizi devrettiğiniz ve geri kalanı halleden bir etki alanı uzmanı olarak düşünün.

Chat katılımcıları, ajan akışının parçası olarak çağrılan ve belirli görevlere katkıda bulunup gerçekleştiren [araçlardan](#reference-tools) farklıdır.

Chat katılımcısını @-bahsetmeyle çağırabilirsiniz: katılımcı adının ardından `@` yazın. VS Code'da `@vscode`, `@terminal` veya `@workspace` gibi birkaç yerleşik chat katılımcısı vardır. Kendi alanlarıyla ilgili soruları yanıtlamak için optimize edilmişlerdir.

Aşağıdaki örnekler chat istemlerinizde @-bahsetmelerin nasıl kullanılacağını gösterir:

* `"@vscode how to enable word wrapping"`
* `"@terminal what are the top 5 largest files in the current directory"`

Mevcut chat katılımcılarının listesini görmek için chat giriş alanına `@` yazın.

Uzantılar kendi [chat katılımcılarını](/api/extension-guides/ai/chat.md) da katkıda bulunabilir.

## Vision (Önizleme)

Chat görüntü yeteneklerini destekler; bu da chat isteminize bağlam olarak bir görüntü ekleyip bunun hakkında sorular sorabileceğiniz anlamına gelir. Örneğin bir kod bloğunun ekran görüntüsünü ekleyip açıklamasını isteyin veya bir UI taslağı ekleyip ajanın uygulamasını isteyin.

> [!TIP]
> Bağlam olarak eklemek için bir görüntüyü web tarayıcısından Chat görünümüne sürükleyip bırakabilirsiniz.

## Tarayıcı öğeleri ekleyin (Deneysel)

VS Code'da web sayfalarını VS Code içinde önizlemek ve etkileşim kurmak için kullanabileceğiniz yerleşik [entegre tarayıcı](/docs/debugtest/integrated-browser.md) vardır; örneğin web uygulamanızın hızlı test ve hata ayıklaması için.

Tarayıcı penceresindeki öğeleri chat isteminize bağlam olarak ekleyebilirsiniz. Belirli web sayfası bölümleri konusunda yardım almak istediğinizde kullanışlıdır; HTML öğeleri, CSS stilleri veya JavaScript kodu gibi.

Entegre tarayıcıdan chat isteminize öğe eklemek için:

1. Web uygulamanızı başlatın.
1. Komut Paleti'nden **Browser: Open Integrated Browser** komutunu çalıştırarak entegre tarayıcıyı açın.
1. Etkileşim kurmak istediğiniz web sayfasının URL'sini girin.
1. **Add Element to Chat** düğmesini seçin. Artık web sayfasının öğelerinin üzerine gelip bunları chat isteminize bağlam olarak eklemek için seçebilirsiniz.

    <video src="images/copilot-chat/integrated-browser-select-element.mp4" title="Video showing how to select and add elements from the integrated browser to the chat prompt." loop controls muted></video>

Bağlama hangi bilginin dahil edileceğini yapılandırabilirsiniz:

* CSS ekle: `setting(chat.sendElementsToChat.attachCSS)` ayarı
* Görüntüler ekle: `setting(chat.sendElementsToChat.attachImages)` ayarı

## Tarayıcı sayfalarıyla etkileşim kurun

> [!NOTE]
> Ajanlar için tarayıcı araçları şu anda deneyseldir.

Ajanlar yerleşik tarayıcı araçlarını kullanarak [entegre tarayıcıdaki](/docs/debugtest/integrated-browser.md) sayfaları doğrudan okuyup etkileşime girebilir. Bu, harici MCP sunucusu gerektirmeden URL'lere gidebilmeyi, sayfa içeriği ve konsol hatalarını okumayı, ekran görüntüsü almayı, öğelere tıklamayı, metin yazmayı ve daha fazlasını sağlar.

Tarayıcı araçlarını etkinleştirmek için `setting(workbench.browser.enableChatTools)` ayarını `true` olarak ayarlayın.

Ayrıca zaten açık olan bir tarayıcı sayfasını ajana paylaşabilirsiniz. Mevcut oturumunuz ve giriş durumunuz dahil sayfanıza ajana erişim vermek için tarayıcı araç çubuğundaki **Share with Agent** düğmesini seçin.

Örneğin bir ajana web uygulamanızı açmasını, düzen sorunlarını kontrol etmesini veya bir özelliğin doğru çalıştığını doğrulamasını isteyebilirsiniz. Ajan tarayıcıyı açar, sayfayla etkileşime girer ve bulgularıyla geri bildirir.

[Ajanlar için tarayıcı araçları](/docs/debugtest/integrated-browser.md#browser-tools-for-agents) hakkında daha fazla bilgi edinin.

## Bağlam penceresi kullanımını izleyin

Chat giriş kutusu modelin bağlam penceresinin ne kadarının kullanıldığını gösteren bir bağlam penceresi kontrolü gösterir. Bu görsel gösterge chat özetlemesinin ne zaman gerçekleşebileceğini veya yeni oturum başlatmanız gerektiğini anlamanıza yardımcı olur.

![Chat giriş kutusundaki bağlam penceresi kullanım kontrolünü gösteren VS Code Chat görünümü ekran görüntüsü.](./images/copilot-chat/chat-context-window-control.png)

Bağlam penceresi kontrolü şu bilgileri sağlar:

* **Görsel doluluk göstergesi**: gölgeli bir çubuk şu anda kullanılan bağlam penceresi oranını gösterir
* **Hover'da toplam kullanım ve dağılım**: hover ile tam token sayısını toplam mevcut bağlamın kesri olarak (örneğin 15K/128K) ve kategoriye göre kullanım dağılımını görün

Sohbette daha fazla istek gönderdikçe kontrol artan bağlam kullanımını yansıtacak şekilde güncellenir. Toplam mevcut bağlam (payda) seçtiğiniz AI modeline göre değişir; farklı modellerin farklı bağlam penceresi boyutları vardır.

> [!TIP]
> Bağlam penceresi dolduğunda VS Code [konuşma geçmişini otomatik olarak sıkıştırır](#context-compaction) ve yer açar.

## Bağlam sıkıştırma

Konuşma büyüdükçe biriken mesajlar ve bağlam modelin bağlam penceresini doldurabilir. Bağlam sıkıştırma konuşma geçmişini özetleyerek yer açar; böylece önemli detayları kaybetmeden aynı oturumda çalışmaya devam edebilirsiniz.

### Otomatik sıkıştırma

Bağlam penceresi dolduğunda VS Code erken mesajları özetleyerek konuşmayı otomatik sıkıştırır. Bu arka planda şeffaf gerçekleşir; kesintisiz sohbet etmeye devam edebilirsiniz.

### Manuel sıkıştırma

Konuşmayı yeniden odaklamak veya erken alışverişlerden gürültüyü azaltmak için örneğin herhangi bir anda manuel olarak sıkıştırmayı tetikleyebilirsiniz. Manuel sıkıştırma yerel, arka plan ve Claude ajan oturumları için mevcuttur.

Konuşmayı manuel sıkıştırmak için şu yöntemlerden birini kullanın:

* Chat giriş alanına `/compact` yazın. İsteğe bağlı olarak özetin nasıl oluşturulacağına rehberlik etmek için komuttan sonra özel talimatlar ekleyin, örneğin `/compact focus on the database schema decisions`.

* Chat giriş kutusundaki bağlam penceresi kontrolünü seçin ve ardından **Compact Conversation** seçin.

Bağlamı tamamen sıfırlamak istiyorsanız [yeni chat oturumu](/docs/copilot/chat/chat-sessions.md) başlatın.

## İlgili kaynaklar

* [Chat genel bakış](/docs/copilot/chat/copilot-chat.md)
* [İstem örnekleri](/docs/copilot/chat/prompt-examples.md)
* [İstem mühendisliği rehberi](/docs/copilot/guides/prompt-engineering-guide.md)
* [Chat etkileşimlerinde hata ayıklama](/docs/copilot/chat/chat-debug-view.md)
