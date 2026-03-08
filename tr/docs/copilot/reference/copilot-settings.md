---
ContentId: 7b232695-cbbe-4f3f-a625-abc7a5e6496c
DateApproved: 3/4/2026
MetaDescription: Visual Studio Code'da GitHub Copilot için yapılandırma ayarlarına genel bakış.
MetaSocialImage: ../images/shared/github-copilot-social.png
---
# VS Code'da GitHub Copilot ayarları referansı

Bu makale Visual Studio Code'da GitHub Copilot için yapılandırma ayarlarını listeler. VS Code'da ayarlarla çalışma hakkında genel bilgi için [Kullanıcı ve çalışma alanı ayarları](/docs/configure/settings.md) bölümüne bakın.

Ekip VS Code'da Copilot'u iyileştirmeye ve yeni özellikler eklemeye sürekli çalışıyor. Bazı özellikler hala deneyseldir. Bunları deneyin ve [sorunlarımızda](https://github.com/microsoft/vscode/issues) geri bildiriminizi paylaşın. [VS Code'da özellik yaşam döngüsü](/docs/configure/settings.md#feature-lifecycle) hakkında daha fazla bilgi edinin.

> [!TIP]
> Henüz Copilot aboneliğiniz yoksa [Copilot Free planına](https://github.com/github-copilot/signup) kaydolarak satır içi öneriler ve sohbet etkileşimleri için aylık limite sahip olarak ücretsiz kullanabilirsiniz.

## Genel ayarlar

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(chat.commandCenter.enabled)`<br/>VS Code başlık çubuğunda Sohbet menüsünün gösterilip gösterilmeyeceğini kontrol eder. | `true` |
| `setting(workbench.settings.showAISearchToggle)`<br/>Ayarlar editöründe yapay zeka ile ayar aramayı etkinleştirir. | `true` |
| `setting(workbench.commandPalette.experimental.askChatLocation)` _(Deneysel)_<br/>Komut Paleti'nin sohbet sorularını nerede sorması gerektiğini kontrol eder. | `"chatView"` |
| `setting(search.searchView.semanticSearchBehavior)` _(Önizleme)_<br/>Arama görünümünde anlamsal aramanın ne zaman çalışacağını yapılandırır: manuel (varsayılan), metin arama sonucu bulunamadığında veya her zaman. | `"manual"` |
| `setting(search.searchView.keywordSuggestions)` _(Önizleme)_<br/>Arama görünümünde anahtar kelime önerilerinin gösterilip gösterilmeyeceğini kontrol eder. | `false` |

## Kod düzenleme ayarları

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(github.copilot.editor.enableCodeActions)`<br/>Copilot komutlarının mevcut olduğunda Kod Eylemleri olarak gösterilip gösterilmeyeceğini kontrol eder. | `true` |
| `setting(github.copilot.renameSuggestions.triggerAutomatically)`<br/>Sembol yeniden adlandırma önerileri oluşturur. | `true` |
| `setting(github.copilot.enable)`<br/>Belirtilen [diller](/docs/languages/identifiers.md) için satır içi önerileri etkinleştirir veya devre dışı bırakır. | `{ "*": true, "plaintext": false, "markdown": false, "scminput": false }` |
| `setting(github.copilot.nextEditSuggestions.enabled)`<br/>[Sonraki düzenleme önerilerini](/docs/copilot/ai-powered-suggestions.md#next-edit-suggestions) (NES) etkinleştirir. | `true` |
| `setting(editor.inlineSuggest.edits.allowCodeShifting)`<br/>NES'in öneri göstermek için kodunuzu kaydırıp kaydıramayacağını yapılandırır. | `"always"` |
| `setting(editor.inlineSuggest.edits.renderSideBySide)`<br/>NES'in mümkünse daha büyük önerileri yan yana gösterebilmesini veya Copilot NES'in daha büyük önerileri her zaman ilgili kodun altında göstermesini yapılandırır. | `"auto"` |
| `setting(github.copilot.nextEditSuggestions.fixes)`<br/>Tanılara (dalgalı çizgiler) dayalı sonraki düzenleme önerilerini etkinleştirir. Örneğin eksik import'lar. | `true` |
| `setting(editor.inlineSuggest.minShowDelay)`<br/>Satır içi önerileri göstermeden önce beklenen süre (milisaniye). | `0` |

## Sohbet ayarları

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(github.copilot.chat.localeOverride)`<br/>Sohbet yanıtları için `en` veya `fr` gibi yerel ayar belirtir. | `"auto"` |
| `setting(github.copilot.chat.useProjectTemplates)`<br/>`/new` kullanırken ilgili GitHub projelerini başlangıç projeleri olarak kullanır. | `true` |
| `setting(github.copilot.chat.scopeSelection)`<br/>`/explain` kullanıp etkin editörde seçim olmadığında belirli sembol kapsamı isteyip istemeyeceğini kontrol eder. | `false` |
| `setting(github.copilot.chat.terminalChatLocation)`<br/>Terminalden sohbet sorgularının nerede açılacağını kontrol eder. | `"chatView"` |
| `setting(chat.detectParticipant.enabled)`<br/>Sohbet görünümünde sohbet katılımcısı algılamayı etkinleştirir. | `true` |
| `setting(chat.checkpoints.enabled)` <br/>Sohbette [denetim noktalarını](/docs/copilot/chat/chat-checkpoints.md) etkinleştirir veya devre dışı bırakır. | `true` |
| `setting(chat.checkpoints.showFileChanges)` <br/>Her sohbet isteğinin sonunda dosya değişikliklerinin özetini gösterir. | `false` |
| `setting(chat.editRequests)`<br/>[Önceki sohbet isteklerini düzenlemeyi](/docs/copilot/chat/chat-checkpoints.md#edit-a-previous-chat-request) etkinleştirir veya devre dışı bırakır. | `"inline"` |
| `setting(chat.editor.fontFamily)`<br/>Sohbet kod bloklarında yazı tipi ailesi. | `"default"` |
| `setting(chat.editor.fontSize)`<br/>Sohbet kod bloklarında piksel cinsinden yazı tipi boyutu. | `14` |
| `setting(chat.editor.fontWeight)`<br/>Sohbet kod bloklarında yazı tipi ağırlığı. | `"default"` |
| `setting(chat.editor.lineHeight)`<br/>Sohbet kod bloklarında piksel cinsinden satır yüksekliği. | `0` |
| `setting(chat.editor.wordWrap)`<br/>Sohbet kod bloklarında satır kaydırmayı açıp kapatır. | `"off"` |
| `setting(chat.editing.confirmEditRequestRemoval)`<br/>Düzenlemeyi geri almadan önce onay ister. | `true` |
| `setting(chat.editing.confirmEditRequestRetry)`<br/>Son düzenlemenin yeniden yapılmasından önce onay ister. | `true` |
| `setting(chat.editing.autoAcceptDelay)`<br/>Önerilen düzenlemelerin otomatik kabul edileceği gecikmeyi yapılandırır; otomatik kabulü devre dışı bırakmak için sıfır kullanın. | `0` |
| `setting(chat.fontFamily)`<br/>Sohbette Markdown içeriği için yazı tipi ailesi. | `"default"` |
| `setting(chat.fontSize)`<br/>Sohbette Markdown içeriği için piksel cinsinden yazı tipi boyutu. | `13` |
| `setting(chat.notifyWindowOnConfirmation)`<br/>Sohbet oturumunda kullanıcı girdisi gerektiğinde OS bildirimi gösterilme zamanını yapılandırır: `off` hiç bildirim göstermez, `windowNotFocused` (varsayılan) yalnızca VS Code penceresi odakta değilken, `always` her zaman. | `"windowNotFocused"` |
| `setting(chat.notifyWindowOnResponseReceived)`<br/>Sohbet yanıtı alındığında OS bildirimi gösterilme zamanını yapılandırır: `off` hiç bildirim göstermez, `windowNotFocused` (varsayılan) yalnızca VS Code penceresi odakta değilken, `always` her zaman. | `"windowNotFocused"` |
| `setting(chat.requestQueuing.defaultAction)`<br/>İstek devam ederken **Send** düğmesi için varsayılan eylemi yapılandırır: `queue` mesajı sıraya ekler, `steer` mevcut isteğe teslim olması için sinyal verir. | `"queue"` |
| `setting(chat.tools.terminal.autoReplyToPrompts)` <br/>Terminal istemlerine varsayılan yanıtla otomatik yanıt verir. | `false` |
| `setting(chat.tools.terminal.terminalProfile.<platform>)`<br/>Her platformda sohbet terminal komutları için hangi terminal profilinin kullanılacağını yapılandırır. | `""` |
| `setting(chat.hookFilesLocations)` _(Önizleme)_ <br/>Ek [hook dosya konumlarını](/docs/copilot/customization/hooks.md#hook-file-locations) yapılandırır. Klasörlere yollar (tüm `*.json` dosyalarını yükler) veya `.json` dosyalarına doğrudan yollar belirtin. Yalnızca göreli yollar ve tilde yolları desteklenir. | `{}` |
| `setting(chat.useAgentsMdFile)` <br/>Sohbet istekleri için bağlam olarak `AGENTS.md` dosyalarının kullanılmasını etkinleştirir veya devre dışı bırakır. | `true` |
| `setting(chat.math.enabled)` <br/>Sohbette [KaTeX](https://katex.org) ile matematik işlemeyi etkinleştirir veya devre dışı bırakır. | `false` |
| `setting(chat.viewTitle.enabled)` _(Önizleme)_<br/>Sohbet üstbilgisinde mevcut sohbet oturumunun başlığını gösterir. | `true` |
| `setting(github.copilot.chat.codesearch.enabled)` _(Önizleme)_<br/>Prompt'ta `#codebase` kullanıldığında Copilot'un düzenlenecek ilgili dosyaları otomatik keşfetmesini sağlar. | `false` |
| `setting(chat.emptyState.history.enabled)` _(Deneysel)_<br/>Sohbet görünümünün boş durumunda son sohbet geçmişini gösterir. | `false` |
| `setting(chat.sendElementsToChat.enabled)` _(Deneysel)_<br/>[Entegre tarayıcıdan](/docs/debugtest/integrated-browser.md) öğelerin sohbet görünümüne bağlam olarak gönderilmesini etkinleştirir. | `true` |
| `setting(workbench.browser.enableChatTools)` _(Deneysel)_<br/>Ajanların entegre tarayıcıdaki sayfalarla etkileşim kurmasını sağlayan [tarayıcı araçlarını](/docs/debugtest/integrated-browser.md#browser-tools-for-agents) etkinleştirir. | `false` |
| `setting(chat.useNestedAgentsMdFiles)` _(Deneysel)_<br/>Sohbet istekleri için bağlam olarak çalışma alanınızın alt klasörlerindeki `AGENTS.md` dosyalarının kullanılmasını etkinleştirir veya devre dışı bırakır. | `false` |
| `setting(github.copilot.chat.customOAIModels)` _(Deneysel)_<br/>Sohbet için özel OpenAI uyumlu modelleri yapılandırır. | `[]` |
| `setting(github.copilot.chat.edits.suggestRelatedFilesFromGitHistory)` _(Deneysel)_<br/>Sohbet bağlamında git geçmişinden ilgili dosyalar önerir. | `true` |

## Ajan ayarları

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(chat.agent.enabled:true)`<br/>Ajanların kullanımını etkinleştirir veya devre dışı bırakır (VS Code 1.99 veya üzeri gerekir). | `true` |
| `setting(chat.agent.maxRequests)`<br/>Copilot'un ajanlar kullanarak yapabileceği maksimum istek sayısı. | `25` |
| `setting(github.copilot.chat.agent.autoFix)`<br/>Oluşturulan kod değişikliklerindeki sorunları otomatik teşhis eder ve düzeltir. | `true` |
| `setting(chat.mcp.access)`<br/>VS Code'da hangi Model Context Protocol (MCP) sunucularının kullanılabileceğini yönetir. | `true` |
| `setting(chat.mcp.discovery.enabled)`<br/>Diğer uygulamalardan MCP sunucu yapılandırmasının otomatik keşfini yapılandırır. | `false` |
| `setting(chat.mcp.serverSampling)`<br/>MCP sunucularına örnekleme için hangi modellerin sunulduğunu yapılandırır. | `{}` |
| `setting(chat.mcp.apps.enabled)` _(Deneysel)_<br/>MCP sunucuları tarafından sağlanan zengin kullanıcı arayüzleri olan MCP Apps'i etkinleştirir veya devre dışı bırakır. | `true` |
| `setting(chat.tools.terminal.autoApprove)` <br/>[Ajanlar kullanırken hangi terminal komutlarının otomatik onaylanacağını](/docs/copilot/agents/agent-tools.md#automatically-approve-terminal-commands) kontrol eder. Komutlar `true` (otomatik onay) veya `false` (onay gerekli) olarak ayarlanabilir. Desenleri `/` karakterleri içine alarak normal ifadeler kullanılabilir. | `{ "rm": false, "rmdir": false, "del": false, "kill": false, "curl": false, "wget": false, "eval": false, "chmod": false, "chown": false, "/^Remove-Item\\b/i": false }` |
| `setting(chat.tools.terminal.enableAutoApprove)` <br/>Terminal komutlarının otomatik onayını etkinleştirir veya devre dışı bırakır. | `true` |
| `setting(chat.tools.terminal.enforceTimeoutFromModel)` _(Deneysel)_<br/>Ajanın terminal komutları için belirttiği zaman aşımı değerinin uygulanıp uygulanmayacağını kontrol eder. Etkinleştirildiğinde ajan belirtilen süre sonunda komutu izlemeyi durdurur ve o ana kadar toplanan çıktıyı döndürür. | `true` |
| `setting(chat.tools.terminal.ignoreDefaultAutoApproveRules)` <br/>Terminal komutları için varsayılan otomatik onay kurallarını yok sayar. | `false` |
| `setting(chat.tools.global.autoApprove)`<br/>Tüm araçları otomatik onaylar - bu ayar [kritik güvenlik korumalarını devre dışı bırakır](/docs/copilot/security.md). | `false` |
| `setting(chat.tools.urls.autoApprove)` <br/>[Hangi URL istekleri ve yanıtlarının otomatik onaylanacağını](/docs/copilot/agents/agent-tools.md#url-approval) kontrol eder. | `[]` |
| `setting(chat.agent.thinking.collapsedTools)` _(Deneysel)_<br/>Sohbet görüşmesinde araç çağrısı ayrıntılarının varsayılan olarak daraltılıp genişletileceğini yapılandırır. | `always` |
| `setting(chat.agent.thinkingStyle)` _(Deneysel)_<br/>Sohbette düşünme token'larının nasıl sunulduğunu yapılandırır. | `fixedScrolling` |
| `setting(chat.mcp.autoStart)` _(Deneysel)_<br/>MCP yapılandırma değişiklikleri algılandığında MCP sunucularını otomatik başlatır. | `newAndOutdated` |
| `setting(chat.tools.eligibleForAutoApproval)` _(Deneysel)_<br/>Ajanlar tarafından kullanılmadan önce manuel onay gerektiren araçları yapılandırır. | `[]` |
| `setting(chat.tools.terminal.blockDetectedFileWrites)` _(Deneysel)_<br/>Dosya yazma gerçekleştiren terminal komutları için kullanıcı onayı gerektirir. | `outsideWorkspace` |
| `setting(chat.tools.terminal.sandbox.enabled)` _(Deneysel)_<br/>Ajan tarafından çalıştırılan [terminal komutları için sandbox](/docs/copilot/agents/agent-tools.md#sandbox-terminal-commands-experimental) etkinleştirir (yalnızca macOS ve Linux). Etkinleştirildiğinde komutlar otomatik onaylanır ve kısıtlı dosya sistemi ve ağ erişimine sahiptir. | `false` |
| `setting(chat.tools.terminal.sandbox.linuxFileSystem)` _(Deneysel)_<br/>Linux'ta sandbox terminal komutları için dosya sistemi erişim kurallarını yapılandırır. `allowWrite`, `denyWrite` ve `denyRead` özelliklerini destekler. | `{}` |
| `setting(chat.tools.terminal.sandbox.macFileSystem)` _(Deneysel)_<br/>macOS'ta sandbox terminal komutları için dosya sistemi erişim kurallarını yapılandırır. `allowWrite`, `denyWrite` ve `denyRead` özelliklerini destekler. | `{}` |
| `setting(chat.tools.terminal.sandbox.network)` _(Deneysel)_<br/>Sandbox terminal komutları için ağ erişim kurallarını yapılandırır. İzin verilen etki alanlarını belirtmek için `allowedDomains` ve [Trusted Domains](/docs/editing/editingevolved.md#outgoing-link-protection) listesindeki etki alanlarını dahil etmek için `allowTrustedDomains` destekler. | `{}` |
| `setting(github.copilot.chat.newWorkspaceCreation.enabled)` _(Deneysel)_<br/>Sohbette yeni çalışma alanı iskeleti için aracı etkinleştirir. | `true` |
| `setting(github.copilot.chat.agent.thinkingTool:true)` _(Deneysel)_<br/>Ajanlar kullanılırken düşünme aracını etkinleştirir. | `false` |
| `setting(github.copilot.chat.summarizeAgentConversationHistory.enabled)` _(Deneysel)_<br/>Bağlam penceresi dolu olduğunda ajan sohbet geçmişini otomatik özetler. | `true` |
| `setting(github.copilot.chat.virtualTools.threshold)` _(Deneysel)_<br/>Sanal araçların kullanılması gereken araç sayısı eşiği. Sanal araçlar benzer araç setlerini gruplar ve modelin bunları isteğe bağlı etkinleştirmesini sağlar. Sohbet isteği için 128 araç limitinin ötesine geçmenizi sağlar. | `128` |

## Ajan oturumları

[Ajanlar görünümü](/docs/copilot/agents/overview.md) hem yerel sohbet görüşmelerini hem de uzak kodlama ajan oturumlarını yönetmek için merkezi bir konum sağlar. Bu görünüm birden fazla yapay zeka oturumuyla eşzamanlı çalışmanıza, ilerlemelerini takip etmenize ve uzun süren görevleri verimli yönetmenize olanak tanır.

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(workbench.startupEditor)` <br/>VS Code karşılama sayfasını ajan oturumları giriş noktanız olarak yapılandırır. Son oturumlar, gömülü sohbet ve hızlı eylemlerle [VS Code karşılama sayfasını](/docs/copilot/chat/chat-sessions.md#vs-code-welcome-page) göstermek için `agentSessionsWelcomePage` olarak ayarlayın. | N/A |
| `setting(chat.viewSessions.enabled)` <br/>Sohbet görünümünde ajan oturumları listesini gösterir. | `true` |
| `setting(chat.agentsControl.enabled)` _(Deneysel)_<br/>Komut merkezinde [ajan durum göstergesini](/docs/copilot/agents/overview.md#agent-status-indicator-experimental) etkinleştirir. Okunmamış ve devam eden oturum rozetlerini gösterir. | `true` |
| `setting(chat.agentsControl.clickBehavior)` _(Deneysel)_<br/>Ajan durum göstergesinde sohbet simgesi seçildiğinde davranışı yapılandırır. | `"cycle"` (Insiders)<br/>`"default"` (Stable) |
| `setting(chat.unifiedAgentsBar.enabled)` _(Deneysel)_<br/>Komut merkezi arama kutusunu birleşik sohbet ve arama kontrolüyle değiştirir. | `false` |

## Satır içi sohbet ayarları

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(inlineChat.defaultModel)`<br/>Editör satır içi sohbeti için varsayılan dil modelini yapılandırır. Seçtiğiniz model oturum sırasında korunur ancak VS Code yeniden yüklendikten sonra bu yapılandırılmış varsayılana sıfırlanır. | N/A |
| `setting(inlineChat.renderMode)` _(Deneysel)_<br/>Satır içi sohbetin nasıl görüntüleneceğini yapılandırır. `hover`: satır içi sohbeti yüzen katmanda gösterir, `zone`: editörde ayrılmış bölgede gösterir. | `"hover"` |
| `setting(inlineChat.finishOnType)`<br/>Değiştirilen bölgelerin dışında yazarken editör satır içi sohbet oturumunu sonlandırır. | `false` |
| `setting(inlineChat.holdToSpeech)`<br/>Editör satır içi sohbet klavye kısayoluna (`kb(inlineChat.start)`) basılı tutmak konuşma tanımayı otomatik etkinleştirir. | `true` |
| `setting(editor.inlineSuggest.syntaxHighlightingEnabled)`<br/>Satır içi öneriler için sözdizimi vurgulama gösterir. | `true` |
| `setting(inlineChat.affordance)` _(Deneysel)_<br/>Metin seçtiğinizde satır içi sohbeti başlatmaya yardımcı olmak için görsel ipucu gösterir. `off`: ipucu yok, `gutter`: satır numarası alanında, `editor`: ampul ile imleç konumunda. | `"off"` |
| `setting(inlineChat.lineEmptyHint)` _(Deneysel)_<br/>Boş satırda editör satır içi sohbet için ipucu gösterir. | `false` |
| `setting(inlineChat.lineNaturalLanguageHint)` _(Deneysel)_<br/>Satır çoğunlukla kelimelerden oluşur oluşmaz editör satır içi sohbeti tetikler. | `true` |
| `setting(github.copilot.chat.editor.temporalContext.enabled)` _(Deneysel)_<br/>Editör satır içi sohbet için bağlama son görüntülenen ve düzenlenen dosyaları dahil eder. | `false` |

## Kod inceleme ayarları

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(github.copilot.chat.reviewSelection.enabled)` _(Önizleme)_<br/>Editör metin seçimi için yapay zeka ile kod incelemesini etkinleştirir. | `true` |
| `setting(github.copilot.chat.reviewSelection.instructions)` _(Önizleme)_<br/>Mevcut editör seçimini yapay zeka ile inceleme isteklerine eklenen özel talimatlar. | `[]` |

## Özel talimatlar ayarları

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(chat.instructionsFilesLocations)` <br/>Özel talimat dosyalarını aramak için konumlar. Göreli yollar çalışma alanınızın kök klasör(ler)inden çözülür. Dosya yolları için glob desenlerini destekler. | `{ ".github/instructions": true, "~/.claude/rules": false }` |
| `setting(chat.includeApplyingInstructions)`<br/>Eşleşen `applyTo` deseni olan talimat dosyalarını sohbet isteklerine otomatik ekler. | `true` |
| `setting(chat.includeReferencedInstructions)`<br/>Markdown bağlantıları aracılığıyla referans verilen talimat dosyalarını sohbet isteklerine otomatik ekler. | `false` |
| `setting(github.copilot.chat.codeGeneration.useInstructionFiles)`<br/>Sohbet isteklerine `.github/copilot-instructions.md` dosyasından özel talimatları otomatik ekler. | `true` |
| `setting(github.copilot.chat.commitMessageGeneration.instructions)` _(Deneysel)_<br/>Yapay zeka ile commit mesajları oluşturma için özel talimatlar. | `[]` |
| `setting(github.copilot.chat.pullRequestDescriptionGeneration.instructions)` _(Deneysel)_<br/>Yapay zeka ile pull request başlıkları ve açıklamaları oluşturma için özel talimatlar. | `[]` |

## Yeniden kullanılabilir prompt dosyası ayarları

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(chat.promptFilesLocations)` <br/>Prompt dosyalarını aramak için konumlar. Göreli yollar çalışma alanınızın kök klasör(ler)inden çözülür. Dosya yolları için glob desenlerini destekler. | `{ ".github/prompts": true }` |
| `setting(chat.promptFilesRecommendations)` <br/>Yeni sohbet oturumu açılırken prompt dosyası önerilerini etkinleştirir veya devre dışı bırakır. Prompt dosyası adı ve boolean veya when koşulu anahtar-değer çiftleri listesi. | `[]` |

## Özel ajan ayarları

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(chat.agentFilesLocations)` <br/>Özel ajan dosyalarını aramak için konumlar. Göreli yollar çalışma alanınızın kök klasör(ler)inden çözülür. Kullanıcı özelinde yollar için ev dizini genişlemesini (`~`) destekler. | `{ ".github/agents": true }` |
| `setting(chat.customAgentInSubagent.enabled)` _(Deneysel)_<br/>[Alt ajanlarla](/docs/copilot/agents/subagents.md) özel ajan kullanımını etkinleştirir. | `false` |
| `setting(github.copilot.chat.cli.customAgents.enabled)` _(Deneysel)_<br/>GitHub arka plan ajan oturumlarından özel ajan kullanımını etkinleştirir. | `false` |

## Ajan becerileri ayarları

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(chat.useAgentSkills)` <br/>VS Code'da [ajan becerileri](/docs/copilot/customization/agent-skills.md) desteğini etkinleştirir. | `true` |
| `setting(chat.agentSkillsLocations)` <br/>Ajan becerilerini aramak için konumlar. Göreli yollar çalışma alanınızın kök klasör(ler)inden çözülür. Kullanıcı özelinde yollar için ev dizini genişlemesini (`~`) destekler. | `"chat.agentSkillsLocations": { ".github/skills": true,".claude/skills": true,"~/.copilot/skills": true,"~/.claude/skills": true}` |

## Hata ayıklama ayarları

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(github.copilot.chat.startDebugging.enabled)` _(Önizleme)_<br/>Hata ayıklama yapılandırması oluşturmak için Sohbet görünümünde deneysel `/startDebugging` niyetini etkinleştirir. | `true` |
| `setting(github.copilot.chat.copilotDebugCommand.enabled)` _(Önizleme)_<br/>`copilot-debug` terminal komutunu etkinleştirir. | `true` |

## Test ayarları

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(github.copilot.chat.generateTests.codeLens)` _(Deneysel)_<br/>Mevcut test kapsam bilgisi tarafından kapsanmayan semboller için **Generate tests** kod merceği gösterir. | `false` |
| `setting(github.copilot.chat.setupTests.enabled)` _(Deneysel)_<br/>`/tests` oluşturmada deneysel `/setupTests` niyetini ve istemeyi etkinleştirir. | `true` |

## Notebook ayarları

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(notebook.experimental.generate)` _(Deneysel)_<br/>Notebook satır içi sohbetle kod hücreleri oluşturmak için **Generate** eylemini etkinleştirir. | `true` |
| `setting(github.copilot.chat.edits.newNotebook.enabled)` _(Deneysel)_<br/>Düzenleme modunda yeni notebook dosyası oluşturmak için notebook aracını etkinleştirir. | `true` |
| `setting(github.copilot.chat.notebook.followCellExecution.enabled)` _(Deneysel)_<br/>Editörde şu anda çalışan hücreyi gösterir. | `false` |

## Erişilebilirlik ayarları

| Ayar ve Açıklama | Varsayılan |
|------------------------|---------------|
| `setting(inlineChat.accessibleDiffView)`<br/>Satır İçi Sohbet'in değişiklikleri için erişilebilir diff görüntüleyici oluşturup oluşturmayacağı. | `"auto"` |
| `setting(accessibility.signals.chatRequestSent)`<br/>Sohbet isteği yapıldığında sinyal çalar - ses (ses ipucu) ve/veya duyuru (uyarı). | `{ "sound": "auto", "announcement": "auto" }` |
| `setting(accessibility.signals.chatResponseReceived)`<br/>Yanıt alındığında ses/ ses ipucu çalar. | `{ "sound": "auto" }` |
| `setting(accessibility.signals.chatEditModifiedFile)`<br/>Dosya sohbet düzenlemeleriyle değiştirildiğinde ses/ses ipucu çalar. | `{ "sound": "auto" }` |
| `setting(accessibility.signals.chatUserActionRequired)`<br/>Kullanıcının sohbette eylem yapması gerektiğinde ses/ses ipucu çalar. | `{ "sound": "auto", "announcement": "auto" }` |
| `setting(accessibility.signals.lineHasInlineSuggestion)`<br/>İmleç satır içi önerisi olan satırdayken ses/ses ipucu çalar. | `{ "sound": "auto" }` |
| `setting(accessibility.signals.nextEditSuggestion)`<br/>Sonraki düzenleme önerisi mevcut olduğunda ses/ses ipucu çalar. | `{ "sound": "auto", "announcement": "auto" }` |
| `setting(accessibility.verboseChatProgressUpdates)`<br/>Sohbet etkinliği hakkında ayrıntılı güncellemeler sağlar. | `true` |
| `setting(accessibility.verbosity.inlineChat)`<br/>Girdi odakta olduğunda özelliğin nasıl kullanılacağını açıklayan ipuçlarıyla satır içi editör sohbet erişilebilirlik yardım menüsüne ve uyarıya nasıl erişileceği bilgisini sağlar. | `true` |
| `setting(accessibility.verbosity.inlineCompletions)`<br/>Satır içi öneriler hover ve Erişilebilir Görünüm'e nasıl erişileceği bilgisini sağlar. | `true` |
| `setting(accessibility.verbosity.panelChat)`<br/>Sohbet girdisi odakta olduğunda sohbet yardım menüsüne nasıl erişileceği bilgisini sağlar. | `true` |
| `setting(accessibility.voice.keywordActivation)`<br/>Sesli sohbet oturumu başlatmak için 'Hey Code' anahtar kelime ifadesinin tanınıp tanınmayacağını kontrol eder. | `"off"` |
| `setting(accessibility.voice.autoSynthesize)`<br/>Konuşma girdi olarak kullanıldığında metinsel yanıtın otomatik sesli okunup okunmayacağını kontrol eder. | `"off"` |
| `setting(accessibility.voice.speechTimeout)`<br/>Konuşmayı bıraktıktan sonra sesli konuşma tanımanın aktif kaldığı süre (milisaniye). | `1200` |

## İlgili kaynaklar

* [VS Code'da Copilot özelliklerine hızlı genel bakış](/docs/copilot/reference/copilot-vscode-features.md)
