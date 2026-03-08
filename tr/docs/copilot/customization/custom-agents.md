---
ContentId: 276ecd8f-2a76-467e-bf82-846d49c13ab5
DateApproved: 3/4/2026
MetaDescription: VS Code'da belirli iş akışlarınız ve geliştirme senaryolarınız için AI sohbet davranışını özelleştirmek üzere özel ajanlar (eski adıyla özel sohbet modları) oluşturmayı öğrenin.
MetaSocialImage: ../images/shared/github-copilot-social.png
Keywords:
- custom agents
- chat modes
- agent personas
- handoffs
- subagents
- copilot
- ai
- customize
- code review
---
# VS Code'da özel ajanlar

Özel ajanlar, AI'nın belirli geliştirme rolleri ve görevleri için özelleştirilmiş farklı kişilikler benimsemesini yapılandırmanızı sağlar. Örneğin, güvenlik inceleyicisi, planlayıcı, çözüm mimarı veya diğer uzman roller için ajanlar oluşturabilirsiniz. Her kişiliğin kendi davranışı, kullanılabilir araçları ve talimatları olabilir.

Ayrıca ajanlar arasında yönlendirilen iş akışları oluşturmak için handoff'ları kullanabilirsiniz. Tek bir seçimle planlama ajanından uygulama ajanına veya ilgili bağlamla kod inceleyicisine sorunsuz geçiş yapın.

Bu makale VS Code'da özel ajanların nasıl oluşturulacağını ve yönetileceğini açıklar.

> [!TIP]
> Tüm sohbet özelleştirmelerinizi tek bir yerde keşfetmek, oluşturmak ve yönetmek için [Sohbet Özelleştirmeleri editörünü](/docs/copilot/customization/overview.md#chat-customizations-editor) (Önizleme) kullanın. Komut Paleti'nden **Chat: Open Chat Customizations** komutunu çalıştırın.

> [!NOTE]
> Özel ajanlar VS Code 1.106 sürümünden itibarən kullanılabilir. Özel ajanlar önceden özel sohbet modları olarak biliniyordu.

## Özel ajanlar nedir?

[Yerleşik ajanlar](/docs/copilot/agents/local-agents.md) VS Code'da sohbet için genel amaçlı yapılandırmalar sağlar. Daha özelleştirilmiş bir sohbet deneyimi için kendi özel ajanlarınızı oluşturabilirsiniz.

Özel ajanlar, o ajana geçtiğinizde uygulanan bir talimat ve araç setinden oluşur. Örneğin "Plan" ajanı bir uygulama planı oluşturmak için talimatlar içerebilir ve yalnızca salt okunur araçlar kullanabilir. Özel ajan oluşturarak her seferinde ilgili araçları ve talimatları manuel seçmek zorunda kalmadan o yapılandırmaya hızlıca geçebilirsiniz.

Özel ajanlar `.agent.md` Markdown dosyasında tanımlanır ve başkalarının kullanması için çalışma alanınızda veya farklı çalışma alanlarında yeniden kullanmak için kullanıcı profilinizde saklanabilir.

Özel ajanlarınızı [arka plan ajanlarında](/docs/copilot/agents/background-agents.md) ve [bulut ajanlarında](/docs/copilot/agents/cloud-agents.md) yeniden kullanabilirsiniz; aynı özelleştirilmiş yapılandırmalarla özerk görevler çalıştırmanızı sağlar.

## Neden özel ajan kullanılır?

Farklı görevler farklı yetenekler gerektirir. Planlama ajanı yanlışlıkla kod değişikliklerini önlemek için yalnızca araştırma ve analiz için salt okunur araçlara ihtiyaç duyabilir, oysa uygulama ajanı tam düzenleme yeteneklerine ihtiyaç duyar. Özel ajanlar her görev için tam olarak hangi araçların kullanılabilir olduğunu belirtmenizi sağlar; AI'nın iş için doğru yeteneklere sahip olmasını sağlar.

Özel ajanlar ayrıca AI'nın nasıl çalışması gerektiğini tanımlayan özelleştirilmiş talimatlar sağlamanıza izin verir. Örneğin planlama ajanı proje bağlamını toplaması ve detaylı bir uygulama planı oluşturması talimatını verebilir, oysa kod incelemesi ajanı güvenlik açıklarını belirlemeye ve iyileştirme önermeye odaklanabilir. Bu özelleştirilmiş talimatlar o ajana her geçişte tutarlı, göreve uygun yanıtlar sağlar.

> [!NOTE]
> Alt ajanlar özel ajanla çalışabilir. [Özel ajanı alt ajan olarak çalıştırma](/docs/copilot/agents/subagents.md#run-a-custom-agent-as-a-subagent-experimental) (deneysel) hakkında daha fazla bilgi edinin.

## Handoff'lar

Handoff'lar ajanlar arasında önerilen sonraki adımlarla geçiş yapan yönlendirilmiş sıralı iş akışları oluşturmanızı sağlar. Sohbet yanıtı tamamlandıktan sonra kullanıcıların ilgili bağlam ve önceden doldurulmuş istemle sonraki ajana geçmesini sağlayan handoff düğmeleri görünür.

Geliştiricilere sonraki adıma geçmeden önce her adımı inceleme ve onaylama kontrolü veren çok adımlı iş akışlarını orkestra etmek için handoff'lar kullanışlıdır. Örneğin:

* **Planlama → Uygulama**: Planlama ajanında plan oluşturun, ardından kodlamaya başlamak için uygulama ajanına devredin.
* **Uygulama → İnceleme**: Uygulamayı tamamlayın, ardından kalite ve güvenlik sorunlarını kontrol etmek için kod incelemesi ajanına geçin.
* **Başarısız Testler Yaz → Başarılı Testler Yaz**: Büyük uygulamalardan daha kolay incelebilen başarısız testler oluşturun, ardından gerekli kod değişikliklerini uygulayarak bu testlerin geçmesini sağlamak için devredin.

Ajan dosyanızda handoff'ları tanımlamak için bunları frontmatter'a ekleyin. Her handoff hedef ajanı, düğme etiketini ve gönderilecek isteğe bağlı istemi belirtir:

```markdown
---
description: Generate an implementation plan
tools: ['search', 'fetch']
handoffs:
  - label: Start Implementation
    agent: implementation
    prompt: Now implement the plan outlined above.
    send: false
    model: GPT-5.2 (copilot)
---
```

Kullanıcılar handoff düğmesini görüp seçtiğinde istem önceden doldurulmuş olarak hedef ajana geçerler. `send: true` ise istem sonraki iş akışı adımını başlatmak için otomatik olarak gönderilir.

## Özel ajan dosya yapısı

Özel ajan dosyaları Markdown dosyalarıdır, `.agent.md` uzantısını kullanır ve aşağıdaki yapıya sahiptir.

> [!NOTE]
> VS Code çalışma alanınızın `.github/agents` klasöründeki `.md` dosyalarını özel ajanlar olarak algılar.

### Başlık (isteğe bağlı)

Başlık aşağıdaki alanlarla YAML frontmatter olarak biçimlendirilir:

| Alan | Açıklama |
| --- | --- |
| `description`     | Özel ajanın kısa açıklaması, sohbet giriş alanında yer tutucu metin olarak gösterilir. |
| `name`            | Özel ajanın adı. Belirtilmezse dosya adı kullanılır. |
| `argument-hint`   | Kullanıcıların özel ajanla nasıl etkileşime gireceğine rehberlik etmek için sohbet giriş alanında gösterilen isteğe bağlı ipucu metni. |
| `tools`           | Bu özel ajan için kullanılabilir araç veya araç seti adları listesi. Yerleşik araçlar, araç setleri, MCP araçları veya uzantılar tarafından katkıda bulunulan araçları dahil edebilir. Bir MCP sunucusunun tüm araçlarını dahil etmek için `<server name>/*` formatını kullanın.<br/>[Sohbette araçlar](/docs/copilot/agents/agent-tools.md) hakkında daha fazla bilgi edinin. |
| `agents`          | Bu ajanda [alt ajan](/docs/copilot/agents/subagents.md) olarak kullanılabilir ajan adları listesi. Tüm ajanlara izin vermek için `*` veya herhangi bir alt ajan kullanımını engellemek için boş dizi `[]` kullanın. `agents` belirtirseniz `tools` özelliğine `agent` aracının dahil edildiğinden emin olun. |
| `model`           | İstemi çalıştırırken kullanılacak AI modeli. Tek model adı (dize) veya öncelikli model listesi (dizi) belirtin. Dizi belirttiğinizde sistem kullanılabilir bir tane bulunana kadar sırayla her modeli dener. Belirtilmezse model seçicide şu an seçili model kullanılır. |
| `user-invocable`  | Ajanın sohbetteki ajanlar açılır menüsünde görünüp görünmeyeceğini kontrol eden isteğe bağlı boolean bayrak (varsayılan `true`). Yalnızca [alt ajanlar](/docs/copilot/agents/subagents.md) veya programatik olarak erişilebilir ajanlar oluşturmak için `false` yapın. |
| `disable-model-invocation` | Özel ajanın diğer ajanlar tarafından alt ajan olarak çağrılmasını engelleyen isteğe bağlı boolean bayrak (varsayılan `false`). |
| `infer`           | **Kullanımdan kaldırıldı.** Bunun yerine `user-invocable` ve `disable-model-invocation` kullanın. Önceden `infer: true` (varsayılan) ajanı hem seçicide görünür hem de alt ajan olarak kullanılabilir yapardı. `infer: false` her ikisinden de gizlerdi. Yeni alanlar bağımsız kontrol sağlar: seçiciden gizlerken alt ajan çağrısına izin vermek için `user-invocable: false` kullanın veya alt ajan çağrısını engellerken seçicide tutmak için `disable-model-invocation: true` kullanın. |
| `target`          | Özel ajanın hedef ortamı veya bağlamı (`vscode` veya `github-copilot`). |
| `mcp-servers`     | [GitHub Copilot'ta özel ajanlarla](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents) kullanılacak Model Context Protocol (MCP) sunucu yapılandırması json listesi (target: `github-copilot`). |
| `handoffs`        | Özel ajanlar arasında geçiş için önerilen sonraki eylemler veya istemler listesi. Handoff düğmeleri sohbet yanıtı tamamlandıktan sonra etkileşimli öneriler olarak görünür. |
| `handoffs.label`  | Handoff düğmesinde gösterilen görüntü metni. |
| `handoffs.agent`  | Geçilecek hedef ajan tanımlayıcısı. |
| `handoffs.prompt` | Hedef ajana gönderilecek istem metni. |
| `handoffs.send`   | İstemi otomatik gönderme isteğe bağlı boolean bayrağı (varsayılan `false`) |
| `handoffs.model`  | Handoff çalıştırıldığında kullanılacak isteğe bağlı dil modeli. Nitelikli model adını `Model Name (vendor)` formatında kullanın, örneğin `GPT-5 (copilot)` veya `Claude Sonnet 4.5 (copilot)`. |

> [!NOTE]
> Özel ajan kullanılırken belirli bir araç kullanılamıyorsa yoksayılır.

### Gövde

Özel ajan dosyası gövdesi Markdown olarak biçimlendirilmiş özel ajan uygulamasını içerir. Bu ajanla çalışırken AI'nın takip etmesini istediğiniz belirli istemleri, yönergeleri veya diğer ilgili bilgileri burada sağlarsınız.

Örneğin talimat dosyalarını yeniden kullanmak için Markdown bağlantıları kullanarak diğer dosyalara atıfta bulunabilirsiniz.

Gövde metninde ajan araçlarına atıfta bulunmak için `#tool:<tool-name>` sözdizimini kullanın. Örneğin `githubRepo` aracına atıfta bulunmak için `#tool:githubRepo` kullanın.

Chat görünümünde özel ajanı seçtiğinizde özel ajan dosyası gövdesindeki yönergeler kullanıcı sohbet isteminin başına eklenir.

### Örnekler

<details>
<summary>Planlama ajanı örneği</summary>

Aşağıdaki kod parçası kod düzenlemesi yapmayan bir uygulama planı oluşturan "Plan" özel ajan dosyası örneğini gösterir. Topluluk tarafından katkıda bulunulan daha fazla örnek için [Awesome Copilot deposuna](https://github.com/github/awesome-copilot/tree/main) bakın.

```markdown
---
description: Generate an implementation plan for new features or refactoring existing code.
name: Planner
tools: ['fetch', 'githubRepo', 'search', 'usages']
model: ['Claude Opus 4.5', 'GPT-5.2']  # Tries models in order
handoffs:
  - label: Implement Plan
    agent: agent
    prompt: Implement the plan outlined above.
    send: false
---
# Planning instructions
You are in planning mode. Your task is to generate an implementation plan for a new feature or for refactoring existing code.
Don't make any code edits, just generate a plan.

The plan consists of a Markdown document that describes the implementation plan, including the following sections:

* Overview: A brief description of the feature or refactoring task.
* Requirements: A list of requirements for the feature or refactoring task.
* Implementation Steps: A detailed list of steps to implement the feature or refactoring task.
* Testing: A list of tests that need to be implemented to verify the feature or refactoring task.
```

</details>

<details>
<summary>Ajan orkestrasyonu örneği</summary>

Aşağıdaki örnek araştırma-önce-uygulama iş akışı için uzmanlaşmış alt ajanları koordine eden "Feature Builder" ajanını gösterir. Ana ajan hangi ajanların alt ajan olarak çağrılabileceğini kısıtlamak için `agents` özelliğini kullanır.

**feature-builder.agent.md** - Koordine eden ajan:

```markdown
---
name: Feature Builder
description: Build features by researching first, then implementing
tools: ['agent']
agents: ['Researcher', 'Implementer']
---
You are a feature builder. For each task:
1. Use the Researcher agent to gather context and find relevant patterns in the codebase
2. Use the Implementer agent to make the actual code changes based on research findings
```

**researcher.agent.md** - Salt okunur araştırma ajanı:

```markdown
---
name: Researcher
description: Research codebase patterns and gather context
tools: ['codebase', 'fetch', 'usages']
---
Research thoroughly using read-only tools. Return a summary of findings.
```

**implementer.agent.md** - Kod düzenleme ajanı:

```markdown
---
name: Implementer
description: Implement code changes based on provided context
tools: ['editFiles', 'terminalLastCommand']
---
Implement changes following existing code patterns. Make minimal, focused edits.
```

</details>

### Claude ajan formatı

`.claude/agents` klasöründeki ajan dosyaları düz `.md` dosyaları kullanır ve Claude özel frontmatter özelliklerini destekler:

| Alan | Açıklama |
|-------|-------------|
| `name` | Ajan adı (gerekli) |
| `description` | Ajanın ne yaptığı |
| `tools` | İzin verilen araçların virgülle ayrılmış dizesi (örneğin `"Read, Grep, Glob, Bash"`) |
| `disallowedTools` | Engellenecek araçların virgülle ayrılmış dizesi |

VS Code Claude özel araç adlarını karşılık gelen VS Code araçlarına eşler. Hem VS Code `.agent.md` formatı (araçlar için YAML dizileri) hem de Claude formatı (virgülle ayrılmış dizeler) desteklenir.

> [!NOTE]
> VS Code ayrıca [Claude alt ajan formatını](https://code.claude.com/docs/en/sub-agents) takip ederek `.claude/agents` klasöründeki `.md` dosyalarını algılar. VS Code ve Claude Code arasında aynı ajan tanımlarını kullanmanızı sağlar.

## Özel ajan oluşturma

Özel ajan dosyasını çalışma alanınızda veya kullanıcı profilinizde oluşturabilirsiniz.

> [!TIP]
> **Configure Custom Agents** menüsünü hızlıca açmak için sohbet girişinde `/agents` yazın.

1. Ajanlar açılır menüsünden **Configure Custom Agents** seçin, ardından **Create new custom agent** seçin veya Komut Paleti'nde (`kb(workbench.action.showCommands)`) **Chat: New Custom Agent** komutunu çalıştırın.

1. Özel ajan dosyasının oluşturulacağı konumu seçin.

    * **Çalışma alanı**: Yalnızca o çalışma alanında kullanmak için özel ajan tanım dosyasını çalışma alanının `.github/agents` klasöründe oluşturun.

    * **Kullanıcı profili**: Tüm çalışma alanlarınızda kullanmak için özel ajan tanım dosyasını [mevcut profil klasöründe](/docs/configure/profiles.md) oluşturun.

    * **Çalışma alanı (Claude formatı)**: Claude Code ve diğer Claude tabanlı araçlarla uyumluluk için `.claude/agents` klasöründe ajan dosyaları oluşturun.

    > [!TIP]
    > VS Code'un özel ajan dosyalarını aradığı ek konumları `setting(chat.agentFilesLocations)` ayarıyla yapılandırabilirsiniz. Projeler arasında ajan paylaşmak veya bunları çalışma alanınızın dışında merkezi bir konumda tutmak için faydalıdır.

1. Özel ajan için bir dosya adı girin. Ajanlar açılır menüsünde görünen varsayılan addır.

1. Yeni oluşturulan `.agent.md` dosyasında özel ajan için ayrıntıları sağlayın.

    * Özel ajanın adını, açıklamasını, araçlarını ve diğer ayarlarını yapılandırmak için dosyanın üst kısmındaki YAML frontmatter'ı doldurun.
    * Dosyanın gövdesine özel ajan için talimatlar ekleyin.

Özel ajan tanım dosyasını güncellemek için ajanlar açılır menüsünden **Configure Custom Agents** seçin, ardından listeden değiştirmek istediğiniz özel ajanı seçin.

### AI ile özel ajan oluşturma

Rol açıklamasına dayalı olarak AI ile özel ajan oluşturabilirsiniz. Ajan modu sohbette `/create-agent` yazın ve istediğiniz kişiliği açıklayın (örneğin, "güvenlik incelemesi ajanı"). Ajan açıklayıcı sorular sorar ve uygun araçlar, talimatlar ve frontmatter ile bir `.agent.md` dosyası oluşturur.

Devam eden bir sohbetteki özel ajanı da çıkarabilirsiniz. Örneğin çok turlu bir hata ayıklama oturumundan sonra "bu tür görev için ajan yap" deyin; iş akışını yeniden kullanılabilir özel ajan olarak yakalar.

## Ajanlar açılır listesini özelleştirme

Birden fazla özel ajanınız varsa ajanlar açılır menüsünde hangilerinin görüneceğini özelleştirebilirsiniz. Belirli özel ajanları göstermek veya gizlemek için:

1. Ajanlar açılır menüsünden **Configure Custom Agents** seçin.

1. Listede bir özel ajanın üzerine gelin, ardından ajanlar açılır menüsünden göstermek veya gizlemek için göz simgesini seçin.

## Araç listesi önceliği

Özel ajan ve prompt dosyası için `tools` meta veri alanını kullanarak kullanılabilir araç listesini belirtebilirsiniz. Prompt dosyaları ayrıca `agent` meta veri alanını kullanarak özel bir ajana atıfta bulunabilir.

Sohbette kullanılabilir araç listesi şu öncelik sırasına göre belirlenir:

1. Prompt dosyasında belirtilen araçlar (varsa)
2. Prompt dosyasındaki referans verilen özel ajandan araçlar (varsa)
3. Seçilen ajan için varsayılan araçlar (varsa)

## Ekipler arasında özel ajanları paylaşın

Ekibinizle özel ajanları paylaşmak için çalışma alanı düzeyinde özel ajan (`.github/agents` klasörü) oluşturabilirsiniz. Kuruluşunuz genelinde birden fazla çalışma alanında özel ajanları paylaşmak istiyorsanız bunları GitHub kuruluşu düzeyinde tanımlayabilirsiniz.

VS Code, erişiminiz olan kuruluş düzeyinde tanımlanan özel ajanları otomatik olarak algılar. Bu ajanlar yerleşik ajanlarla birlikte sohbetteki Agents açılır menüsünde, kişisel ve çalışma alanı özel ajanlarınızla birlikte görünür.

Kuruluş düzeyinde özel ajanların keşfini etkinleştirmek için `setting(github.copilot.chat.organizationCustomAgents.enabled)` ayarını `true` yapın.

GitHub dokümantasyonunda [kuruluşunuz için özel ajanlar oluşturma](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/create-custom-agents) hakkında bilgi edinin.

## Sık sorulan sorular

### Özel ajanlar sohbet modlarından farklı mı?

Özel ajanlar önceden özel sohbet modları olarak biliniyordu. İşlevsellik aynı kalır, ancak terminoloji belirli görevler için AI davranışını özelleştirmedeki amaçlarını daha iyi yansıtmak üzere güncellendi.

Mevcut `.chatmode.md` dosyalarınız varsa bunları yeni özel ajan formatına dönüştürmek için `.agent.md` olarak yeniden adlandırın ve kullanmaya devam etmek için uygun konuma (`setting(chat.agentFilesLocations)`) yerleştirin.

### Özel ajanı nasıl kaldırırım?

VS Code'dan özel ajanı tamamen kaldırmak için:

* Karşılık gelen `.agent.md` dosyasını çalışma alanınızdan veya kullanıcı profilinizden silin.
* Ajanlar açılır menüsünden **Configure Custom Agents** seçin, listede özel ajanın üzerine gelin ve çöp kutusu simgesini seçin.

Uzantı tarafından katkıda bulunulan bir özel ajanı kaldırmak için onu sağlayan uzantıyı kaldırmanız gerekir. Uzantıyı kaldırmak istemiyorsanız özel ajanı ajanlar açılır menüsünden gizleyebilirsiniz. [Ajanlar açılır listesini özelleştirme](#customize-the-agents-dropdown-list) adımlarını izleyin.

### Özel ajanın nereden geldiğini nasıl anlarım?

Özel ajanlar farklı kaynaklardan gelebilir: yerleşik ajanlar, profilinizde kullanıcı tanımlı, mevcut çalışma alanınızda çalışma alanı tanımlı, kuruluş tanımlı veya uzantı tarafından katkıda bulunulan.

Özel ajanın kaynağını belirlemek için:

1. Ajanlar açılır menüsünden **Configure Custom Agents** seçin.
1. Listede özel ajanın üzerine gelin. Kaynak konum bir ipucunda gösterilir.

> [!TIP]
> Yüklenen tüm özel ajanları, prompt dosyalarını, talimat dosyalarını ve becerileri hatalarla birlikte görmek için sohbet özelleştirme tanılamaları görünümünü kullanın. Chat görünümünde sağ tıklayın ve **Diagnostics** seçin. [VS Code'da AI sorun giderme](/docs/copilot/troubleshooting.md) hakkında daha fazla bilgi edinin.

## İlgili kaynaklar

* [Özel talimatlarla AI'yı özelleştirin](/docs/copilot/customization/custom-instructions.md)
* [Yeniden kullanılabilir prompt dosyaları oluşturun](/docs/copilot/customization/prompt-files.md)
* [Sohbette araçları kullanın](/docs/copilot/agents/agent-tools.md)
