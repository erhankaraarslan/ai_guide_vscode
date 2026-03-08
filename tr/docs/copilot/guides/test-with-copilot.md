---
ContentId: 9f84b21e-5b76-4c3a-a5dd-2021ab343f1f
DateApproved: 3/4/2026
MetaDescription: Visual Studio Code'da GitHub Copilot ile test yazmayı, hata ayıklamayı ve düzeltmeyi öğrenin.
MetaSocialImage: ../images/shared/github-copilot-social.png
---
# GitHub Copilot ile test etme

Test yazmak ve sürdürmek yazılım geliştirmenin kritik ancak genellikle zaman alan bir parçasıdır. GitHub Copilot bu süreci kolaylaştırarak Visual Studio Code'da testleri daha verimli yazmanıza, hata ayıklamanıza ve düzeltmenize yardımcı olur. Bu makale Copilot'un test yeteneklerinden yararlanarak test iş akışınızı iyileştirmeyi ve projelerinizdeki test kapsamını artırmayı gösterir.

Copilot şu test görevlerinde yardımcı olabilir:

* **Test çerçevelerini kurma**: Projeniz ve diliniz için doğru test çerçevesini ve VS Code uzantılarını yapılandırmada yardım alın.
* **Test kodu oluşturma**: Uygulama kodunuzu kapsayan birim testleri, entegrasyon testleri ve uçtan uca testler oluşturun.
* **Kenar durumlarını ele alma**: Kenar durumları ve hata koşullarını kapsayan kapsamlı test paketleri oluşturun.
* **Başarısız testleri düzeltme**: Test hataları için öneriler alın.
* **Tutarlılığı koruma**: Copilot'u projenizin kodlama uygulamalarına uyan testler oluşturacak şekilde kişiselleştirin.

> [!TIP]
> Henüz Copilot aboneliğiniz yoksa [Copilot Free planına](https://github.com/github-copilot/signup) kaydolarak satır içi öneriler ve sohbet etkileşimleri için aylık limite sahip olarak ücretsiz kullanabilirsiniz.

## Test çerçevenizi kurun

Test iş akışınızı hızlandırmak için Copilot proje türüne göre uygun test çerçevelerini önerebilir.

1. Sohbet görünümünü (`kb(workbench.action.chat.open)`) açın.
1. Sohbet giriş alanına `/setupTests` komutunu girin.
1. Projenizi yapılandırmak için Copilot'un rehberliğini izleyin.

## Copilot ile test yazın

Copilot uygulama kodunuzu kapsayan test kodu oluşturarak test yazmanıza yardımcı olabilir. Bu birim testleri, uçtan uca testler ve kenar durumları için testleri içerir.

### Sohbet promptları kullanın

1. Uygulama kod dosyanızı açın.

1. Şu görünümlerden birini açın:
    * Sohbet görünümü (`kb(workbench.action.chat.open)`)
    * Satır İçi Sohbet (`kb(inlineChat.start)`)

1. Şu gibi bir prompt girin:
    * "Generate tests for this code"
    * "Write unit tests including edge cases"
    * "Create integration tests for this module"

GitHub belgelerinde [GitHub Copilot ile test yazma](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/writing-tests-with-github-copilot) hakkında daha fazla rehberlik edinin.

### Editör akıllı eylemlerini kullanın

Prompt yazmadan uygulama kodunuz için test oluşturmak üzere editör akıllı eylemlerini kullanabilirsiniz.

1. Uygulama kod dosyanızı açın.
1. İsteğe bağlı olarak test etmek istediğiniz kodu seçin.
1. Sağ tıklayıp **Generate Code** > **Generate Tests** seçin.

    Copilot mevcut test dosyasında test kodu oluşturur veya yoksa yeni test dosyası oluşturur.

1. İsteğe bağlı olarak Satır İçi Sohbet promptunda ek bağlam sağlayarak oluşturulan testleri iyileştirin.

## Başarısız testleri düzeltme

Copilot VS Code'daki Test Explorer ile entegre olur ve başarısız testleri düzeltmede yardımcı olabilir.

1. Test Explorer'da başarısız bir testin üzerine gelin
1. **Fix Test Failure** düğmesini (parıltı simgesi) seçin
1. Copilot'un önerilen düzeltmesini inceleyin ve uygulayın

Alternatif olarak:

1. Sohbet görünümünü açın
1. `/fixTestFailure` komutunu girin
1. Testi düzeltmek için Copilot'un önerilerini izleyin

> [!TIP]
> [Ajanları](/docs/copilot/agents/local-agents.md) kullanırken ajan testleri çalıştırırken test çıktısını izler ve başarısız testleri otomatik düzeltip yeniden çalıştırmaya çalışır.

## Test oluşturmayı kişiselleştirme

Kuruluşunuzun belirli test gereksinimleri varsa Copilot'un testleri oluşturma şeklini, standartlarınıza uymasını sağlayacak şekilde özelleştirebilirsiniz. Özel talimatlar sağlayarak Copilot'un testleri nasıl oluşturacağını kişiselleştirebilirsiniz. Örneğin:

* Tercih edilen test çerçevelerini belirtin
* Testler için adlandırma sözleşmelerini tanımlayın
* Kod yapısı tercihlerini ayarlayın
* Belirli test desenleri veya metodolojiler isteyin

[Test oluşturma için Copilot'u kişiselleştirme](/docs/copilot/customization/overview.md) hakkında daha fazla bilgi edinin.

## Daha iyi test oluşturma ipuçları

Copilot ile test oluştururken en iyi sonuçlar için şu ipuçlarını izleyin:

* Tercih ettiğiniz test çerçevesi hakkında promptlarınızda bağlam sağlayın
* İstediğiniz test türlerini (birim, entegrasyon, uçtan uca) belirtin
* Belirli test durumları veya kenar durumları isteyin
* Projenizin kodlama standartlarına uyan testler isteyin

## Sonraki adımlar

* [Tarayıcı ajan araçlarıyla web uygulamalarını test etmeyi](/docs/copilot/guides/browser-agent-testing-guide.md) deneyin.
* [VS Code'da Copilot](/docs/copilot/overview.md) hakkında daha fazla bilgi edinin.
* [VS Code'da genel test özelliklerini](/docs/debugtest/testing.md) keşfedin.
* [Birim testleri oluşturma](https://docs.github.com/en/copilot/example-prompts-for-github-copilot-chat/testing-code/generate-unit-tests) için örnek promptlara bakın
