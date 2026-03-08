---
ContentId: de6f9f68-7dd5-4de3-a210-3db57882384b
DateApproved: 3/4/2026
MetaDescription: VS Code'da GitHub Copilot hızlı referansı: özerk ajanlar, çok dosyalı düzenleme, satır içi öneriler ve kurumsal kontroller dahil.
MetaSocialImage: ../images/shared/github-copilot-social.png
---
# VS Code'da GitHub Copilot kopya kağıdı

Visual Studio Code'daki GitHub Copilot özerk ajanlar, satır içi öneriler, sohbet ve akıllı eylemler sunar. Ajanlar birden fazla dosyada plan yapar, uygular ve değişiklikleri doğrular; yerel olarak, arka planda veya bulutta paralel çalışır. Birden fazla yapay zeka modelinden seçim yapın, MCP ile harici araçlara bağlanın ve ajanları ekibinizin iş akışlarına göre özelleştirin. Bu kopya kağıdı tüm özelliklere hızlı bir genel bakış sunar.

> [!TIP]
> Henüz Copilot aboneliğiniz yoksa [Copilot Free planına](https://github.com/github-copilot/signup) kaydolarak ücretsiz kullanabilir ve aylık satır içi öneri ile sohbet etkileşimi limitine sahip olabilirsiniz.

## Temel klavye kısayolları

* `kb(workbench.panel.chat)` - Sohbet görünümünü aç
* `kb(workbench.action.chat.startVoiceChat)` - Sohbet görünümünde sesli sohbet istemini gir
* `kb(workbench.action.chat.newChat)` - Sohbet görünümünde yeni sohbet oturumu başlat
* `kb(workbench.action.chat.openAgent)` - Sohbet görünümünde ajan kullanımına geç
* `kb(inlineChat.start)` - Editörde veya terminalde satır içi sohbeti başlat
* `kb(workbench.action.chat.startVoiceChat)` (basılı tut) - Satır içi sesli sohbeti başlat
* `kb(editor.action.inlineSuggest.commit)` - Satır içi öneriyi kabul et veya sonraki düzenleme önerisine geç
* `kb(editor.action.inlineSuggest.hide)` - Satır içi öneriyi kapat

## VS Code'da yapay zekaya erişin

* Doğal dille sohbet başlatın
    * Sohbet görünümü (`kb(workbench.action.chat.open)`): İkincil Kenar Çubuğunda sürekli bir sohbet görüşmesi tutun
    * Editör veya terminalde satır içi sohbet (`kb(inlineChat.start)`): İşinizin akışındayken sorular sorun
    * Hızlı Sohbet (`kb(workbench.action.quickchat.toggle)`): Mevcut görevinizden ayrılmadan hızlı sorular sorun

* [Editörde](/docs/copilot/ai-powered-suggestions.md) yapay zeka
    * Satır içi öneriler: yazarken öneriler alın, `kb(editor.action.inlineSuggest.commit)` ile bir öneriyi kabul edin
    * Düzenleme bağlam menüsü eylemleri: Kodu açıklama veya düzeltme, test oluşturma veya metin seçimini inceleme gibi yaygın yapay zeka eylemlerine erişin
    * Kod eylemleri: Editörde lint ve derleyici hatalarını düzeltmek için kod eylemlerine (ampul) erişin

* VS Code genelinde görev odaklı [akıllı eylemler](/docs/copilot/copilot-smart-actions.md)
    * Commit mesajları ile pull request başlıkları ve açıklamaları oluşturma
    * Test hatalarını düzeltme
    * Anlamsal dosya arama önerileri

## VS Code'da sohbet deneyimi

Kodlama görevlerinde yardım almak için doğal dille sohbet başlatın. Örneğin bir kod bloğunu veya programlama kavramını açıklatın, bir kodu yeniden düzenletin veya yeni bir özellik uygulatın. [Copilot Sohbet](/docs/copilot/chat/copilot-chat.md) kullanımı hakkında daha fazla bilgi edinin.

| Eylem | Açıklama |
|--------|-------------|
| `kb(workbench.action.chat.open)` | [Sohbet görünümünü](/docs/copilot/chat/copilot-chat.md) İkincil Kenar Çubuğunda açın. |
| `kb(inlinechat.start)` | Editörde veya terminalde sohbet açmak için [satır içi sohbeti](/docs/copilot/chat/inline-chat.md) başlatın. |
| `kb(workbench.action.quickchat.toggle)` | İş akışınızı kesmeden [Hızlı Sohbet](/docs/copilot/chat/copilot-chat.md) açın. |
| `kb(workbench.action.chat.newChat)` | Sohbet görünümünde yeni sohbet oturumu başlatın. |
| `kb(workbench.action.chat.toggleAgentMode)` | Sohbet görünümünde farklı [ajanlar](/docs/copilot/customization/custom-agents.md) arasında geçiş yapın. |
| `kb(workbench.action.chat.openModelPicker)` | Sohbet için [farklı yapay zeka modeli seçmek](/docs/copilot/customization/language-models.md) üzere model seçiciyi gösterin. |
| Bağlam penceresi kontrolü | Sohbet girdi kutusunda [bağlam penceresi kullanımını](/docs/copilot/chat/copilot-chat-context.md#monitor-context-window-usage) gösteren görsel gösterge. Toplam token sayısı ve kategorilere göre dağılım için üzerine gelin. |
| `Add Context...` | Sohbet isteminize [farklı bağlam türleri ekleyin](/docs/copilot/chat/copilot-chat-context.md). |
| `/`-komutu | Yaygın görevler için [slash komutlarını](#slash-commands) kullanın veya [yeniden kullanılabilir sohbet promptu](/docs/copilot/customization/overview.md) çağırın. |
| `#`-mention | İsteminize [bağlam sağlamak](/docs/copilot/chat/copilot-chat-context.md) için yaygın araçları veya sohbet değişkenlerini referans alın. |
| `@`-mention | Alan odaklı istekleri ele almak için [sohbet katılımcılarını](#chat-participants) referans alın. |
| Düzenle (<i class="codicon codicon-pencil"></i>) | [Önceki bir sohbet istemini düzenleyin](/docs/copilot/chat/chat-checkpoints.md#edit-a-previous-chat-request) ve değişiklikleri geri alın. |
| Geçmiş (<i class="codicon codicon-history"></i>) | Sohbet oturumlarınızın geçmişine erişin. |
| Kuyrukla veya yönlendir | İstek çalışırken [takip mesajı gönderin](/docs/copilot/chat/chat-sessions.md#send-messages-while-a-request-is-running). Mesajı kuyruğa ekleyin, mevcut isteği yönlendirin veya durdurun ve hemen gönderin. |
| Ses (<i class="codicon codicon-mic"></i>) | Konuşma kullanarak sohbet istemi girin (sesli sohbet). Sohbet yanıtı sesli okunur. |
| [KaTeX](https://katex.org) | Sohbet yanıtlarında matematik denklemlerini render edin. `setting(chat.math.enabled)` ile etkinleştirin. Kaynak ifadeyi kopyalamak için bir matematik ifadesine sağ tıklayın. |
| [Mermaid](https://mermaid.js.org) | Sohbet yanıtlarında Mermaid diyagramlarını render edin. `setting(mermaid-chat.enabled)` ile etkinleştirin. Kaynak kodu kopyalamak için diyagrama sağ tıklayın. |

> **İpuçları**
>
> * Sohbet isteminize daha fazla bağlam eklemek için `#`-mention kullanın.
> * Daha doğru ve ilgili yanıtlar almak için `/` komutları ve `@` katılımcılarını kullanın.
> * En iyi sonuçlar için net olun, basit tutun ve takip soruları sorun.
> * İhtiyacınıza uyan bir ajan seçin: Sor, Düzenle, Ajan veya özel ajan oluşturun.

## İsteminize bağlam ekleyin

[Sohbet isteminize bağlam sağlayarak](/docs/copilot/chat/copilot-chat-context.md) daha ilgili yanıtlar alın. Dosyalar, semboller, editör seçimleri, kaynak kontrol commit'leri, test hataları ve daha fazlası gibi farklı bağlam türlerinden seçin.

| Eylem | Açıklama |
|--------|-------------|
| **Bağlam Ekle** | Sohbet isteminiz için ilgili bağlam seçmek üzere Hızlı Seçim açın. Çalışma alanı dosyaları, semboller, mevcut editör seçimi, terminal seçimi ve daha fazlası gibi farklı bağlam türlerinden seçin. |
| Dosya sürükle ve bırak | Gezginden veya Arama görünümünden bir dosyayı sürükleyip bırakın veya bir editör sekmesini Sohbet görünümüne sürükleyin. |
| Klasör sürükle ve bırak | İçindeki dosyaları eklemek için bir klasörü Sohbet görünümüne sürükleyip bırakın. |
| Sorun sürükle ve bırak | Sorunlar panelinden bir öğeyi sürükleyip bırakın. |
| `#<dosya\|klasör\|sembol>` | Sohbet bağlamı olarak eklemek için `#` ardından dosya, klasör veya sembol adı yazın. |
| `#`-mention | Belirli bir bağlam türü veya aracı eklemek için [sohbet aracını](#chat-tools) `#` ardından yazın. |

## Sohbet araçları

Kullanıcı isteğini işlerken uzmanlaşmış görevleri tamamlamak için [araçları](/docs/copilot/agents/agent-tools.md) sohbette kullanın. Bu tür görevlere örnekler: bir dizindeki dosyaları listeleme, çalışma alanınızda bir dosyayı düzenleme, terminal komutu çalıştırma, terminalden çıktı alma ve daha fazlası.

VS Code yerleşik araçlar sunar; [MCP sunucuları](/docs/copilot/customization/mcp-servers.md) ve [uzantılardan](/api/extension-guides/ai/tools.md) gelen araçlarla sohbeti genişletebilirsiniz. [Araç türleri](/docs/copilot/agents/agent-tools.md#types-of-tools) hakkında daha fazla bilgi edinin.

Aşağıdaki tablo VS Code yerleşik araçlarını listeler:

| Sohbet değişkeni/Araç | Açıklama |
|--------|-------------|
| `#changes` | Kaynak kontrol değişiklikleri listesi. |
| `#codebase` | Sohbet istemi için ilgili bağlamı otomatik bulmak üzere mevcut çalışma alanında kod araması yapar. |
| `#createAndRunTask` | Çalışma alanında yeni bir [görev](/docs/debugtest/tasks.md) oluşturur ve çalıştırır. |
| `#createDirectory` | Çalışma alanında yeni bir dizin oluşturur. |
| `#createFile` | Çalışma alanında yeni bir dosya oluşturur. |
| `#edit` (araç seti) | Çalışma alanında değişiklikleri etkinleştirir. |
| `#editFiles` | Çalışma alanındaki dosyalara düzenleme uygular. |
| `#editNotebook` | Bir notebook'a düzenleme yapar. |
| `#extensions` | VS Code uzantılarında arama yapar ve hakkında sorular sorar. Örn: "Python ile nasıl başlanır #extensions?" |
| `#fetch` | Verilen bir web sayfasının içeriğini getirir. Örn: "Özetle #fetch code.visualstudio.com/updates." |
| `#fileSearch` | Glob desenleri kullanarak çalışma alanında dosya arar ve yollarını döndürür. |
| `#getNotebookSummary` | Notebook hücrelerinin listesini ve ayrıntılarını alır. |
| `#getProjectSetupInfo` | Farklı proje türleri için iskele kurulum talimatları ve yapılandırma sağlar. |
| `#getTaskOutput` | Çalışma alanında bir [görev](/docs/debugtest/tasks.md) çalıştırmanın çıktısını alır. |
| `#getTerminalOutput` | Çalışma alanında terminal komutu çalıştırmanın çıktısını alır. |
| `#githubRepo` | GitHub deposunda kod araması yapar. Örn: "global snippet nedir #githubRepo microsoft/vscode." |
| `#installExtension` | VS Code uzantısı yükler. |
| `#listDirectory` | Çalışma alanındaki bir dizindeki dosyaları listeler. |
| `#new` | Hata ayıklama ve çalıştırma yapılandırmaları önceden yapılandırılmış yeni bir VS Code çalışma alanı oluşturur. |
| `#newJupyterNotebook` | Verilen bir açıklamaya göre yeni bir Jupyter notebook oluşturur. |
| `#newWorkspace` | Yeni bir çalışma alanı oluşturur. |
| `#openSimpleBrowser` | [Entegre tarayıcıyı](/docs/debugtest/integrated-browser.md) açar ve yerel olarak dağıtılmış bir web uygulamasını önizler. |
| `#browser` (araç seti) | _(Deneysel)_ [Entegre tarayıcıdaki](/docs/debugtest/integrated-browser.md) sayfalarla etkileşim kurar: gezin, sayfa içeriğini oku, ekran görüntüsü al, tıkla, yaz, üzerine gel, sürükle ve iletişim kutularını yönet. `setting(workbench.browser.enableChatTools)` ile etkinleştirin. |
| `#problems` | **Sorunlar** panelinden çalışma alanı sorunlarını ve problemlerini bağlam olarak ekler. Kod düzeltirken veya hata ayıklarken faydalıdır. |
| `#readFile` | Çalışma alanındaki bir dosyanın içeriğini okur. |
| `#readNotebookCellOutput` | Notebook hücre çalıştırmasından çıktıyı okur. |
| `#runCell` | Bir notebook hücresini çalıştırır. |
| `#runCommands` (araç seti) | Terminalde komut çalıştırmayı ve çıktıyı okumayı etkinleştirir. |
| `#runInTerminal` | Entegre terminalde bir kabuk komutu çalıştırır. |
| `#runNotebooks` (araç seti) | Notebook hücrelerini çalıştırmayı etkinleştirir. |
| `#runTask` | Çalışma alanında mevcut bir [görevi](/docs/debugtest/tasks.md) çalıştırır. |
| `#runTasks` (araç seti) | Çalışma alanında [görevleri](/docs/debugtest/tasks.md) çalıştırmayı ve çıktıyı okumayı etkinleştirir. |
| `#runSubagent` | Görevi izole bir [alt ajan bağlamında](/docs/copilot/agents/subagents.md) çalıştırır. Ana ajan iş parçacığının bağlam yönetimini iyileştirmeye yardımcı olur. |
| `#runTests` | Çalışma alanında [birim testlerini](/docs/debugtest/testing.md) çalıştırır. |
| `#runVscodeCommand` | VS Code komutu çalıştırır. Örn: "Zen modunu etkinleştir #runVscodeCommand." |
| `#search` (araç seti) | Mevcut çalışma alanında dosya aramasını etkinleştirir. |
| `#searchResults` | Arama görünümünden arama sonuçlarını alır. |
| `#selection` | Mevcut editör seçimini alır (yalnızca metin seçildiğinde kullanılabilir). |
| `#terminalLastCommand` | Son çalıştırılan terminal komutunu ve çıktısını alır. |
| `#terminalSelection` | Mevcut terminal seçimini alır. |
| `#testFailure` | Birim test başarısızlık bilgisini alır. [Testleri](/docs/debugtest/testing.md) çalıştırırken ve tanılarken faydalıdır. |
| `#textSearch` | Dosyalarda metin arar. |
| `#todos` | Sohbet isteğinin uygulamasını ve ilerlemesini todo listesi ile takip edin. |
| `#usages` | "Tüm Referansları Bul", "Uygulamayı Bul" ve "Tanıma Git" kombinasyonu. |
| `#VSCodeAPI` | VS Code işlevselliği ve uzantı geliştirme hakkında sorular sorun. |

## Slash komutları

Slash komutları sohbet içinde belirli işlevlere kısayollardır. Hata düzeltme, test oluşturma veya kodu açıklama gibi eylemleri hızlıca gerçekleştirmek için kullanabilirsiniz.

| Slash komutu | Açıklama |
|---------------|-------------|
| `/doc` | Editör satır içi sohbetinden kod dokümantasyon yorumları oluşturun. |
| `/explain` | Bir kod bloğunu, dosyayı veya programlama kavramını açıklatın. |
| `/fix` | Bir kod bloğunu düzeltmesini veya derleyici veya lint hatalarını çözmesini isteyin. |
| `/tests` | Editördeki tüm veya yalnızca seçili metot ve fonksiyonlar için test oluşturun. |
| `/setupTests` | Kodunuz için bir test çerçevesi kurulumunda yardım alın. İlgili test çerçevesi için öneri, kurulum ve yapılandırma adımları ile VS Code test uzantıları önerileri alın. |
| `/clear` | Sohbet görünümünde yeni sohbet oturumu başlatın. |
| `/compact` | Görüşme bağlamını özetleyerek sıkıştırın. Görüşme modelin bağlam penceresi için çok uzadığında faydalıdır. |
| `/fork` | Mevcut sohbet oturumunu tam görüşme geçmişini devralan yeni bağımsız bir oturuma çatallayın. [Sohbet oturumlarını çatallama](/docs/copilot/chat/chat-sessions.md#fork-a-chat-session) hakkında daha fazla bilgi edinin. |
| `/debug` | [Sorun giderme için sohbet günlüklerini incelemek](/docs/copilot/troubleshooting.md) üzere Sohbet Hata Ayıklama görünümünü gösterin. |
| `/new` | Yeni bir VS Code çalışma alanı veya dosyası oluşturun. İhtiyacınız olan proje/dosya türünü doğal dille tanımlayın ve oluşturmadan önce içeriği önizleyin. |
| `/newNotebook` | Gereksinimlerinize göre yeni bir Jupyter notebook oluşturun. Notebook'un ne içermesi gerektiğini doğal dille tanımlayın. |
| `/init` | Proje yapınız ve kodlama desenlerinize göre çalışma alanı talimatları (`copilot-instructions.md` veya `AGENTS.md`) oluşturun veya güncelleyin. |
| `/plan` | Karmaşık bir kodlama görevi için ayrıntılı uygulama planı oluşturun. Gereksinimleri araştırın, açıklayıcı sorular sorun ve adımlar, doğrulama ve kararlarla yapılandırılmış bir plan oluşturun. |
| `/search` | Arama görünümü için arama sorgusu oluşturun. Neyi aramak istediğinizi doğal dille tanımlayın. |
| `/startDebugging` | Sohbet görünümünden `launch.json` hata ayıklama yapılandırma dosyası oluşturun ve hata ayıklama oturumu başlatın. |
| `/agents` | [Özel ajanlarınızı](/docs/copilot/customization/custom-agents.md) yapılandırın. |
| `/hooks` | [Hook'larınızı](/docs/copilot/customization/hooks.md) yapılandırın. |
| `/instructions` | [Özel talimatlarınızı](/docs/copilot/customization/custom-instructions.md) yapılandırın. |
| `/prompts` | [Yeniden kullanılabilir prompt dosyalarınızı](/docs/copilot/customization/prompt-files.md) yapılandırın. |
| `/skills` | [Ajan becerilerinizi](/docs/copilot/customization/agent-skills.md) yapılandırın. |
| `/create-prompt` | Ajan modunda yapay zeka yardımıyla [prompt dosyası](/docs/copilot/customization/prompt-files.md) oluşturun. |
| `/create-instruction` | Ajan modunda yapay zeka yardımıyla [talimat dosyası](/docs/copilot/customization/custom-instructions.md) oluşturun. |
| `/create-skill` | Ajan modunda yapay zeka yardımıyla [ajan becerisi](/docs/copilot/customization/agent-skills.md) oluşturun. |
| `/create-agent` | Ajan modunda yapay zeka yardımıyla [özel ajan](/docs/copilot/customization/custom-agents.md) oluşturun. |
| `/create-hook` | Ajan modunda yapay zeka yardımıyla [hook](/docs/copilot/customization/hooks.md) yapılandırması oluşturun. |
| `/yolo`<br/>`/autoApprove` | Tüm araç çağrılarının [genel otomatik onayını](/docs/copilot/agents/agent-tools.md#can-i-automatically-approve-all-tools-and-terminal-commands) etkinleştirin (`setting(chat.tools.global.autoApprove)`). İlk seferde uyarı iletişim kutusu gösterir. |
| `/disableYolo`<br/>`/disableAutoApprove` | Tüm araç çağrılarının [genel otomatik onayını](/docs/copilot/agents/agent-tools.md#can-i-automatically-approve-all-tools-and-terminal-commands) devre dışı bırakın. |
| `/<beceri adı>` | Sohbette [ajan becerisi](/docs/copilot/customization/agent-skills.md) çalıştırın. Örn: `webapp-testing.md` adında bir beceri dosyanız varsa `/webapp-testing` yazarak çalıştırabilirsiniz. |
| `/<prompt adı>` | Sohbette [yeniden kullanılabilir prompt](/docs/copilot/customization/prompt-files.md) çalıştırın. |

## Sohbet katılımcıları

Alan odaklı istekleri sohbette ele almak için sohbet katılımcılarını kullanın. Sohbet katılımcıları `@` ile başlar ve belirli konularda sorular sormak için kullanılabilir. VS Code `@github`, `@terminal` ve `@vscode` gibi yerleşik sohbet katılımcıları sunar; uzantılar ek katılımcılar sağlayabilir.

| Sohbet katılımcısı | Açıklama |
|------------------|-------------|
| `@github` | GitHub depoları, sorunlar, pull request'ler ve daha fazlası hakkında sorular sormak için `@github` katılımcısını kullanın. [Mevcut GitHub becerileri](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide#currently-available-skills) hakkında daha fazla bilgi edinin.<br/>Örnek: `@github Bana atanmış tüm açık PR'lar neler?`, `@github @dancing-mona'dan son birleştirilen PR'ları göster` |
| `@terminal` | Entegre terminal veya kabuk komutları hakkında sorular sormak için `@terminal` katılımcısını kullanın.<br/>Örnek: `@terminal bu çalışma alanındaki en büyük 5 dosyayı listele` |
| `@vscode` | VS Code özellikleri, ayarları ve VS Code uzantı API'leri hakkında sorular sormak için `@vscode` katılımcısını kullanın.<br/>Örnek: `@vscode satır kaydırmayı nasıl etkinleştiririm?` |
| `@workspace` | Mevcut çalışma alanı hakkında sorular sormak için `@workspace` katılımcısını kullanın.<br/>Örnek: `@workspace kimlik doğrulama nasıl uygulanıyor?` |

## Ajanları kullanın

[Ajanları](/docs/copilot/agents/local-agents.md) kullanırken üst düzey bir görevi doğal dille belirtebilir ve yapay zekanın isteği özerk değerlendirmesine, gereken işi planlamasına ve değişiklikleri kod tabanınıza uygulamasına izin verebilirsiniz. Ajanlar belirttiğiniz görevi tamamlamak için kod düzenleme ve araç çağrısı kombinasyonu kullanır. İsteğinizi işlerken düzenleme ve araç sonuçlarını izler ve ortaya çıkan sorunları çözmek için yinelemeler yapar.

| Eylem | Açıklama |
|--------|-------------|
| `kb(workbench.action.chat.openAgent)` | Sohbet görünümünde ajan kullanımına geçin |
| Araçlar (<i class="codicon codicon-tools"></i>) | Ajan kullanırken hangi araçların mevcut olduğunu yapılandırın. Yerleşik araçlar, MCP sunucuları ve uzantı tarafından sağlanan araçlardan seçin. |
| Araçları otomatik onayla | Ajan kullanırken [tüm araçların otomatik onayını](/docs/copilot/agents/agent-tools.md#auto-approve-all-tools) etkinleştirin (`setting(chat.tools.autoApprove)`). |
| Terminal komutlarını otomatik onayla | Ajan kullanırken [terminal komutlarının otomatik onayını](/docs/copilot/agents/agent-tools.md#automatically-approve-terminal-commands) etkinleştirin (`setting(chat.tools.terminal.autoApprove)`). |
| MCP | Ajan yeteneklerini ve araçlarını genişletmek için [MCP sunucularını](/docs/copilot/customization/mcp-servers.md) yapılandırın. |
| [Üçüncü taraf ajanlar](/docs/copilot/agents/third-party-agents.md) | Claude Agent (Önizleme) ve OpenAI Codex gibi harici sağlayıcıların ajanlarını Copilot aboneliğinizle kullanın. |
| Claude Agent _(Önizleme)_ | Anthropic'nin Claude Agent SDK'sı tarafından desteklenen bir Claude Agent oturumu başlatın. Gelişmiş iş akışları için `/agents`, `/hooks` ve `/memory` slash komutlarını kullanın. |

> **İpuçları**
>
> * Yeteneklerini genişletmek için ajan kullanırken ek araçlar ekleyin.
> * Ajanın nasıl çalışması gerektiğini tanımlamak için (ör. salt okunur planlama modu) özel ajanlar yapılandırın.
> * Ajanlara kodu nasıl oluşturup yapılandıracağını yönlendirmek için özel talimatlar tanımlayın.
> * Alternatif ajanik kodlama deneyimleri için Claude Code veya OpenAI Codex gibi üçüncü taraf ajanları deneyin.

## Planlama

VS Code sohbetinde karmaşık kodlama görevlerine başlamadan önce ayrıntılı uygulama planları oluşturmak için [plan ajanı](/docs/copilot/agents/planning.md) kullanın. Onaylanan planı bir uygulama ajanına devrederek kodlamaya başlayın.

| Eylem | Açıklama |
|--------|-------------|
| Plan ajanı | Karmaşık kodlama görevleri için ayrıntılı uygulama planı oluşturmak üzere ajanlar açılır menüsünden **Plan** ajanını seçin veya `/plan` slash komutunu kullanın. |
| Todo listesi | Karmaşık görevlerde ilerlemeyi takip etmek için todo listesi görüntüleyin. Bunu `setting(chat.tools.todos.showWidget` ayarıyla etkinleştirin. |
| [Bellek](/docs/copilot/agents/memory.md) | Ajanlar görüşmeler arasında kalıcı notlar kaydeder ve geri çağırır. `setting(github.copilot.chat.tools.memory.enabled)` ayarıyla etkinleştirin veya devre dışı bırakın. Kaydedilen anıları görüntülemek için **Chat: Show Memory Files** komutunu kullanın. |

## Sohbet deneyiminizi özelleştirin

Kodlama tarzınız, araçlarınız ve geliştirici iş akışınızla eşleşen yanıtlar oluşturmak için sohbet deneyiminizi özelleştirin. VS Code'da sohbet deneyiminizi özelleştirmenin birkaç yolu vardır:

* [Özel talimatlar](/docs/copilot/customization/custom-instructions.md): Kod oluşturma, kod incelemesi veya commit mesajı oluşturma gibi görevler için yaygın yönergeler veya kurallar tanımlayın. Özel talimatlar yapay zekanın hangi koşullarda çalışması gerektiğini açıklar (_nasıl_ yapılmalı).

* [Yeniden kullanılabilir prompt dosyaları](/docs/copilot/customization/prompt-files.md): Kod oluşturma veya kod incelemesi gibi yaygın görevler için yeniden kullanılabilir promptlar tanımlayın. Prompt dosyaları sohbette doğrudan çalıştırabileceğiniz bağımsız promptlardır. Yapılacak görevi tanımlarlar (_ne_ yapılmalı).

* [Özel ajanlar](/docs/copilot/customization/custom-agents.md): Sohbetin nasıl çalıştığını, hangi araçları kullanabileceğini ve kod tabanıyla nasıl etkileşim kuracağını tanımlayın. Her sohbet istemi ajan sınırları içinde çalışır; her istek için araç ve talimatları yapılandırmanız gerekmez.

> **İpuçları**
>
> * Her dil için daha doğru oluşturulan kod almak için dile özgü talimatlar tanımlayın.
> * Talimatlarınızı ekibinizle kolayca paylaşmak için çalışma alanınızda saklayın.
> * Zaman kazanmak ve ekip üyelerinin hızlı başlamasına yardımcı olmak için yaygın görevler için yeniden kullanılabilir prompt dosyaları tanımlayın.

## Editör yapay zeka özellikleri

Editörde kod yazarken yazdıkça satır içi öneriler oluşturmak için Copilot'u kullanabilirsiniz. Sorular sormak ve kodlama akışında kalırken Copilot'tan yardım almak için Satır İçi Sohbeti çağırın. Örneğin bir fonksiyon veya metot için birim testleri oluşturmasını isteyin. [Satır içi öneriler](/docs/copilot/ai-powered-suggestions.md) ve [Satır İçi Sohbet](/docs/copilot/chat/inline-chat.md) hakkında daha fazla bilgi edinin.

| Eylem | Açıklama |
|--------|-------------|
| Satır içi öneriler | Editörde yazmaya başlayın ve kodlama tarzınıza uyan ve mevcut kodunuzu dikkate alan [satır içi öneriler](/docs/copilot/ai-powered-suggestions.md) alın. |
| Kod yorumları | Kod yorumunda talimatlar yazarak satır içi öneri istemi sağlayın.<br/>Örnek: `# add, subtract ve multiply için metotları olan bir hesaplayıcı sınıfı yaz. Statik metotlar kullan.` |
| `kb(inlinechat.start)` | Editör satır içi sohbetini başlatarak doğrudan editörden sohbet isteği gönderin. Bağlam sağlamak için doğal dil, sohbet değişkenleri ve slash komutlarını kullanın. |
| `kb(editor.action.rename)` | Kodunuzdaki sembolleri yeniden adlandırırken yapay zeka destekli öneriler alın. |
| Bağlam menüsü eylemleri | Kodu açıklama, test oluşturma, kod incelemesi ve daha fazlası gibi yaygın yapay zeka eylemlerine erişmek için editör bağlam menüsünü kullanın. Editörde sağ tıklayarak bağlam menüsünü açın ve **Kod Oluştur** seçin. |
| Kod Eylemleri (ampul) | Kodunuzdaki lint veya derleyici hatalarını düzeltmek için editörde Kod Eylemini (ampul) seçin. |

> **İpuçları**
>
> * Daha iyi satır içi önerileri daha hızlı almak için anlamlı metot veya fonksiyon adları kullanın.
> * Satır İçi Sohbet isteminizi kapsamlandırmak için bir kod bloğu seçin veya dosya veya sembol ekleyerek ilgili bağlamı ekleyin.
> * Editörden doğrudan yaygın yapay zeka destekli eylemlere erişmek için editör bağlam menüsü seçeneklerini kullanın.

## Kaynak kontrol ve sorunlar

Commit'lerinizdeki ve pull request'lerinizdeki değişiklikleri analiz etmek ve commit mesajları ile pull request açıklamaları için öneriler sunmak üzere yapay zekayı kullanın.

| Eylem | Açıklama |
|--------|-------------|
| `#changes` | Sohbet isteminize mevcut kaynak kontrol değişikliklerini bağlam olarak ekleyin. |
| Bağlam olarak commit | Sohbet isteminize kaynak kontrol geçmişinden bir commit'i bağlam olarak ekleyin. |
| Commit mesajı | Kaynak kontrol commit'indeki mevcut değişiklikler için commit mesajı oluşturun. |
| Birleştirme çakışmaları (Deneysel) | [Yapay zeka ile Git birleştirme çakışmalarını çözmek](/docs/sourcecontrol/overview#resolve-merge-conflicts-with-ai-experimental) konusunda yardım alın. |
| Pull request açıklaması | Pull request'inizdeki değişikliklerle uyumlu pull request başlığı ve açıklaması oluşturun. |
| `@github` | Depolarınızdaki sorunlar, pull request'ler ve daha fazlası hakkında sormak için sohbette `@github` katılımcısını kullanın. [Mevcut GitHub becerileri](https://docs.github.com/en/copilot/using-github-copilot/asking-github-copilot-questions-in-your-ide#currently-available-skills) hakkında daha fazla bilgi edinin.<br/>Örnek: `@github Bana atanmış tüm açık PR'lar neler?`, `@github @dancing-mona'dan son birleştirilen PR'ları göster` |

## Kod incelemesi (deneysel)

Bir kod bloğunun hızlı incelemesini yapmak veya çalışma alanınızdaki commit edilmemiş değişikliklerin incelemesini gerçekleştirmek için yapay zekayı kullanın. İnceleme geri bildirimi önerileri uygulayabileceğiniz editörde yorum olarak görünür.

| Eylem | Açıklama |
|--------|-------------|
| **Seçimi İncele** _(Önizleme)_ | Bir kod bloğu seçin ve hızlı inceleme için editör bağlam menüsünden **Kod Oluştur** > **İncele** seçin. |
| **Kod İncelemesi** | Tüm commit edilmemiş değişikliklerin daha derin incelemesi için Kaynak Kontrol görünümünde **Kod İncelemesi** düğmesini seçin. |

## Arama ve ayarlar

Arama görünümünde anlamsal olarak ilgili arama sonuçları alın veya Ayarlar editöründe ayar aramada yardım alın.

| Eylem | Açıklama |
|--------|-------------|
| Ayar araması | Ayarlar editöründe anlamsal arama sonuçlarını dahil edin (`setting(workbench.settings.showAISearchToggle)`). |
| Anlamsal arama _(Önizleme)_ | Arama görünümünde anlamsal arama sonuçlarını dahil edin (`setting(search.searchView.semanticSearchBehavior)`). |

## Test oluşturma

VS Code sohbette slash komutlarını kullanarak kod tabanınızdaki fonksiyon ve metotlar için test oluşturabilir. Slash komutları sohbet istemlerinde kullanabileceğiniz yaygın görevler için kısa notasyonlardır. Slash komutu kullanmak için `/` ardından komut adını yazın.

| Eylem | Açıklama |
|--------|-------------|
| `/tests` | Editördeki tüm veya yalnızca seçili metot ve fonksiyonlar için test oluşturun. Oluşturulan testler mevcut bir test dosyasına eklenir veya yeni bir test dosyası oluşturulur. |
| `/setupTests` | Kodunuz için bir test çerçevesi kurulumunda yardım alın. İlgili test çerçevesi için öneri, kurulum ve yapılandırma adımları ile VS Code test uzantıları önerileri alın. |
| `/fixTestFailure` | Başarısız testleri nasıl düzelteceğiniz konusunda Copilot'tan öneriler isteyin. |
| Test kapsamı _(Deneysel)_ | Henüz testlerle kapsanmamış fonksiyon ve metotlar için test oluşturun. [Daha fazla bilgi](https://code.visualstudio.com/updates/v1_93#_generate-tests-based-on-test-coverage-experimental). |

> **İpuçları**
>
> * Kullanılacak test çerçeveleri veya kütüphaneler hakkında ayrıntı verin.

## Hata ayıklama ve sorunları düzeltme

Kodlama sorunlarını düzeltmek ve VS Code'da hata ayıklama oturumlarını yapılandırıp başlatmak konusunda yardım almak için Copilot'u kullanın.

| Eylem | Açıklama |
|--------|-------------|
| `/fix` | Bir kod bloğunu nasıl düzelteceğiniz veya kodunuzdaki derleyici veya lint hatalarını nasıl çözeceğiniz konusunda Copilot'tan öneriler isteyin. Örn: çözümlenmemiş Node.js paket adlarını düzeltmek için. |
| `/fixTestFailure` | Başarısız testleri nasıl düzelteceğiniz konusunda Copilot'tan öneriler isteyin. |
| `/startDebugging` _(Deneysel)_ | Sohbet görünümünden `launch.json` hata ayıklama yapılandırma dosyası oluşturun ve [hata ayıklama oturumu](/docs/copilot/guides/debug-with-copilot.md) başlatın. |
| `copilot-debug` komutu | [Programlarınızda hata ayıklamaya](/docs/copilot/guides/debug-with-copilot.md) yardımcı olan terminal komutu. Bunun için bir hata ayıklama oturumu başlatmak üzere bir çalıştırma komutunun önüne ekleyin (örn: `copilot-debug python foo.py`). |

> **İpuçları**
>
> * Bellek tüketimini veya performansı optimize etme gibi ihtiyacınız olan düzeltme türü hakkında ek bilgi verin.
> * Kodunuzdaki sorunları düzeltmek için önerileri gösteren editördeki Copilot Kod Eylemlerini izleyin.

## Yeni proje oluşturma

Copilot proje yapısının iskeletini oluşturarak veya gereksinimlerinize göre notebook oluşturarak yeni proje oluşturmanıza yardımcı olabilir.

| Eylem | Açıklama |
|--------|-------------|
| Ajan | [Ajanları](/docs/copilot/agents/local-agents.md) kullanın ve yeni proje veya dosya oluşturmak için doğal dil istemi kullanın. Örn: `Görevlerimi takip etmek için bir Svelte web uygulaması oluştur` |
| `/new` | Yeni proje veya dosya oluşturmak için Sohbet görünümünde `/new` komutunu kullanın. İhtiyacınız olan proje/dosya türünü doğal dille tanımlayın ve oluşturmadan önce içeriği önizleyin.<br/>Örnek: `/new typescript ve svelte kullanan Express uygulaması` |
| `/newNotebook` | Gereksinimlerinize göre yeni Jupyter notebook oluşturmak için Sohbet görünümünde `/newNotebook` komutunu kullanın. Notebook'un ne içermesi gerektiğini doğal dille tanımlayın.<br/>Örnek: `/newNotebook nüfus sayımı verisi al ve Seaborn ile temel içgörüleri önizle` |

## Terminal

Terminalde komut çalıştırırken kabuk komutları ve hata çözümü konusunda yardım alın.

| Eylem | Açıklama |
|--------|-------------|
| `kb(inlinechat.start)` | Kabuk komutları ve terminal hakkında doğal dille sormak için terminal satır içi sohbetini başlatın.<br/>Örnek: `bu makinede kaç çekirdek var?` |
| `@terminal` | Entegre terminal veya kabuk komutları hakkında sorular sormak için Sohbet görünümünde `@terminal` katılımcısını kullanın.<br/>Örnek: `@terminal bu çalışma alanındaki en büyük 5 dosyayı listele` |
| `@terminal /explain` | Terminalden bir şey açıklatmak için Sohbet görünümünde `/explain` komutunu kullanın.<br/>Örnek: `@terminal /explain top kabuk komutu` |

## Python ve notebook desteği

Yerel Python REPL'de ve Jupyter notebook'larda Python programlama görevlerinde size yardımcı olmak için sohbeti kullanabilirsiniz.

| Eylem | Açıklama |
|--------|-------------|
| <i class="codicon codicon-sparkle"></i> Oluştur<br/>`kb(inlinechat.start)` | Kod bloğu veya Markdown bloğu oluşturmak için notebook'ta Satır İçi Sohbet başlatın. |
| `#` | Daha ilgili yanıtlar almak için Jupyter çekirdeğinden değişkenleri sohbet isteminize ekleyin. |
| Yerel REPL + `kb(inlinechat.start)` | Yerel Python REPL'de Satır İçi Sohbet başlatın ve oluşturulan komutları çalıştırın. |
| `kb(workbench.action.chat.open)` | **Sohbet görünümünü** açın ve notebook düzenlemeleri için ajanları kullanın. |
| `/newNotebook` | Gereksinimlerinize göre yeni Jupyter notebook oluşturmak için Sohbet görünümünde `/newNotebook` komutunu kullanın. Notebook'un ne içermesi gerektiğini doğal dille tanımlayın.<br/>Örnek: `/newNotebook nüfus sayımı verisi al ve Seaborn ile temel içgörüleri önizle` |

## Sonraki adımlar

* [Öğretici: VS Code'da yapay zeka özelliklerine başlama](/docs/copilot/getting-started.md)
