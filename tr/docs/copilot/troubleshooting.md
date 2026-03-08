---
ContentId: f8e4b2c1-9d3a-4e5f-b6c7-8a9d0e1f2b3c
DateApproved: 3/4/2026
MetaDescription: Günlükler, tanı teşhis araçları ve hata ayıklama araçlarıyla Visual Studio Code'da GitHub Copilot sorunlarında sorun giderme.
MetaSocialImage: images/shared/github-copilot-social.png
Keywords:
- ai
- copilot
- troubleshooting
- diagnostics
- logs
- debugging
---
# Visual Studio Code'da AI sorun giderme

Bu makale VS Code'da AI ile ilgili sorunları gidermek için tanı teşhis araçlarını ve teknikleri kapsar. Bu araçları ağ bağlantısı, özelleştirme dosyaları ve AI yanıtlarındaki sorunları belirlemek için kullanın.

## GitHub Copilot için günlükleri görüntüleyin

GitHub Copilot uzantısı için günlük dosyaları Visual Studio Code uzantıları için standart günlük konumunda saklanır. Bağlantı sorunlarını, uzantı hatalarını ve beklenmeyen davranışları teşhis etmek için bu günlükleri kullanın.

Ayrıntılı günlükleri görüntülemek için:

1. Komut Paleti'ni açın (`kb(workbench.action.showCommands)`).
1. **Developer: Set Log Level** çalıştırın ve GitHub Copilot ile GitHub Copilot Chat uzantıları için değeri **Trace** olarak ayarlayın.
1. **Output: Show Output Channels** çalıştırın ve listeden **GitHub Copilot** veya **GitHub Copilot Chat** seçin.
1. Output panelinde seçilen uzantı için günlükleri görüntüleyin.

Çıktı kanalları arasında geçiş yapmak için Output panelinin sağ tarafındaki açılır menüden **GitHub Copilot** veya **GitHub Copilot Chat** seçin.

## Ağ tanı teşhislerini toplayın

GitHub Copilot'a bağlanırken sorunlarla karşılaşırsanız güvenlik duvarı, proxy veya VPN sorunlarını belirlemek için ağ bağlantısı tanı teşhislerini toplayın.

1. Komut Paleti'ni açın (`kb(workbench.action.showCommands)`).
1. **GitHub Copilot: Collect Diagnostics** çalıştırın.
1. Sorun bildirirken paylaşabileceğiniz tanı teşhis bilgilerini inceleyebileceğiniz bir editör sekmesi açılır.

Ağ yapılandırması hakkında daha fazla bilgi için [Copilot için ağ ve güvenlik duvarı yapılandırması](/docs/copilot/faq.md#network-and-firewall-configuration-for-copilot) sayfasına bakın.

## Chat etkileşimlerinde hata ayıklama

VS Code AI'ya bir istem gönderdiğinizde ne olduğunu incelemek için araçlar sağlar.

**Agent Debug paneli** birincil hata ayıklama aracıdır. Ajan etkileşimlerinin kronolojik olay günlüğünü gösterir; araç çağrı dizileri, LLM istekleri, token kullanımı, prompt dosyası keşfi ve hatalar dahil.

Agent Debug panelini açmak için:

1. Chat görünümünde dişli simgesini seçin.
1. **Show Agent Logs** seçin.

Alternatif olarak Komut Paleti'nden **Developer: Open Agent Debug Panel** çalıştırın.

**Chat Debug görünümü** her LLM isteğinin ve yanıtının ham detaylarını gösterir; tam sistem istemi, bağlam ve araç yükleri dahil.

Chat Debug görünümünü açmak için:

1. Chat görünümünde taşma menüsünü (`...`) seçin.
1. **Show Chat Debug View** seçin.

Alternatif olarak Komut Paleti'nden **Developer: Show Chat Debug View** çalıştırın.

[Chat etkileşimlerinde hata ayıklama](/docs/copilot/chat/chat-debug-view.md) hakkında daha fazla bilgi edinin.

## Chat özelleştirme tanı teşhisleri

Chat özelleştirme tanı teşhis görünümü yüklenen tüm özel ajanları, prompt dosyalarını, talimat dosyalarını ve becerileri gösterir. Uygulanmayan veya hata veren özelleştirme dosyalarındaki sorunları gidermek için bu görünümü kullanın.

Tanı teşhis görünümünü açmak için:

1. Chat görünümünde sağ tıklayın.
1. **Diagnostics** seçin.

Bu aşağıdakileri listeleyen bir markdown belgesi açar:

* Tüm etkin özelleştirme dosyaları ve konumları
* Her dosya için yükleme durumu (yüklendi, başarısız veya atlandı)
* Yüklenemeyen dosyalar için hata mesajları
* Talimatların uygulanma sırası

> [!TIP]
> Bir özelleştirme dosyası uygulanmıyorsa başarıyla yüklendiğini doğrulamak ve hata mesajlarını incelemek için tanı teşhis görünümünü kontrol edin.

## MCP sunucularında sorun giderme

MCP sunucuları harici hizmetlere bağlanarak chat yeteneklerini genişletir. Bir MCP sunucusu düzgün çalışmıyorsa günlüklerini görüntüleyebilir ve yeniden başlatabilirsiniz.

MCP sunucularında sorun gidermek için:

1. Komut Paleti'ni açın ve **MCP: List Servers** çalıştırın.
1. Durumunu ve mevcut eylemleri görüntülemek için bir sunucu seçin.
1. Sunucunun günlüklerini görüntülemek için **Show Output** seçin.
1. Sorunlu bir sunucuyu yeniden başlatmak için **Restart Server** seçin.

[MCP sunucularını yapılandırma ve hata ayıklama](/docs/copilot/customization/mcp-servers.md) hakkında daha fazla bilgi edinin.

## Geri bildirim sağlayın

Çözemediğiniz sorunlarla karşılaşırsanız GitHub Copilot'un iyileştirilmesine yardımcı olmak için bildirin:

* **Hayalet metin önerileri**: Editörde hayalet metin önerisinin üzerine gelin ve **Send Copilot Completion Feedback** seçin.
* **Sonraki düzenleme önerileri**: Editör kenar boşluğundaki sonraki düzenleme önerileri menüsünde **Feedback** eylemini seçin.
* **Genel sorunlar**: **Help** > **Report Issue** açın, **VS Code Extension** seçin ve **GitHub Copilot Chat** seçin.

Sorun bildirirken sorunu teşhis etmeye yardımcı olması için [Copilot günlüklerinden](#view-logs-for-github-copilot) ilgili bilgiyi ekleyin.

## İlgili kaynaklar

* [Chat etkileşimlerinde hata ayıklama](/docs/copilot/chat/chat-debug-view.md)
* [Özel talimatlar](/docs/copilot/customization/custom-instructions.md)
* [MCP sunucuları](/docs/copilot/customization/mcp-servers.md)
* [GitHub Copilot SSS](/docs/copilot/faq.md)
