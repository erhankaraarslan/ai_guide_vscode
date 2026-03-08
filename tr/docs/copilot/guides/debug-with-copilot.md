---
ContentId: 2f21c45a-8931-4da2-a921-af23a3b92949
DateApproved: 3/4/2026
MetaDescription: Visual Studio Code'da GitHub Copilot ile hata ayıklama yapılandırması kurmayı ve hata ayıklama sırasında keşfedilen sorunları düzeltmeyi öğrenin.
MetaSocialImage: ../images/shared/github-copilot-social.png
---
# GitHub Copilot ile hata ayıklama

GitHub Copilot Visual Studio Code'daki hata ayıklama iş akışınızı iyileştirmenize yardımcı olabilir. Copilot projeniz için hata ayıklama yapılandırması oluşturma ve hata ayıklama sırasında keşfedilen sorunları düzeltme önerileri sunma konusunda size yardımcı olabilir. Bu makale VS Code'da uygulamaları hata ayıklamak için Copilot kullanımına genel bakış sağlar.

Copilot şu hata ayıklama görevlerinde yardımcı olabilir:

* **Hata ayıklama ayarlarını yapılandırma**: Projeniz için launch yapılandırmaları oluşturma ve özelleştirme.
* **Hata ayıklama oturumu başlatma**: Terminalden `copilot-debug` kullanarak hata ayıklama oturumu başlatma.
* **Sorunları düzeltme**: Hata ayıklama sırasında keşfedilen sorunlar için düzeltme önerileri alma.

> [!TIP]
> Henüz Copilot aboneliğiniz yoksa [Copilot Free planına](https://github.com/github-copilot/signup) kaydolarak satır içi öneriler ve sohbet etkileşimleri için aylık limite sahip olarak ücretsiz kullanabilirsiniz.

## Copilot ile hata ayıklama yapılandırması kurma

VS Code [hata ayıklama yapılandırması](/docs/debugtest/debugging-configuration.md) için `launch.json` dosyasını kullanır. Copilot projeniz için hata ayıklama kurulumunda bu dosyayı oluşturmanıza ve özelleştirmenize yardımcı olabilir.

1. Sohbet görünümünü (`kb(workbench.action.chat.open)`) açın.
1. `/startDebugging` komutunu girin.
1. Projeniz için hata ayıklama kurulumunda Copilot'un rehberliğini izleyin.

Alternatif olarak şu gibi doğal dil promptu kullanabilirsiniz:

* "Create a debug configuration for a Django app"
* "Set up debugging for a React Native app"
* "Configure debugging for a Flask application"

## Copilot ile hata ayıklamayı başlatma

`copilot-debug` terminal komutu hata ayıklama oturumunu yapılandırma ve başlatma sürecini basitleştirir. Uygulamanızı başlatmak için kullanacağınız komutun önüne `copilot-debug` ekleyin; Copilot otomatik olarak hata ayıklama oturumunu yapılandırır ve başlatır.

1. Entegre terminali (`kb(workbench.action.terminal.toggleTerminal)`) açın.

1. Uygulamanızın başlangıç komutunun önüne `copilot-debug` yazın. Örneğin:

    ```bash
    copilot-debug node app.js
    ```

    veya

    ```bash
    copilot-debug python manage.py
    ```

1. Copilot uygulamanız için hata ayıklama oturumu başlatır. Artık VS Code'daki yerleşik hata ayıklama özelliklerini kullanabilirsiniz.

[VS Code'da hata ayıklama](/docs/debugtest/debugging.md) hakkında daha fazla bilgi edinin.

## Copilot ile kodlama sorunlarını düzeltme

Kodlama sorunlarını düzeltmek veya kodunuzu iyileştirmek için Copilot Sohbet'i kullanabilirsiniz.

### Sohbet promptları kullanın

1. Uygulama kod dosyanızı açın.

1. Şu görünümlerden birini açın:
    * Sohbet görünümü (`kb(workbench.action.chat.open)`)
    * Satır İçi Sohbet (`kb(inlineChat.start)`)

1. Şu gibi bir prompt girin:
    * "/fix"
    * "Fix this #selection"
    * "Validate input for this function"
    * "Refactor this code"
    * "Improve the performance of this code"

VS Code'da [Copilot Sohbet](/docs/copilot/chat/copilot-chat.md) kullanımı hakkında daha fazla bilgi edinin.

### Editör akıllı eylemlerini kullanın

Prompt yazmadan uygulama kodunuzdaki kodlama sorunlarını düzeltmek için editör akıllı eylemlerini kullanabilirsiniz.

1. Uygulama kod dosyanızı açın.
1. Düzeltmek istediğiniz kodu seçin.
1. Sağ tıklayıp **Generate Code** > **Fix** seçin.

    VS Code kodu düzeltmek için bir kod önerisi sağlar.

1. İsteğe bağlı olarak sohbet promptunda ek bağlam sağlayarak oluşturulan kodu iyileştirin.

## Sonraki adımlar

* [VS Code'da genel hata ayıklama özelliklerini](/docs/debugtest/debugging.md) keşfedin.
* [VS Code'da Copilot](/docs/copilot/overview.md) hakkında daha fazla bilgi edinin.
