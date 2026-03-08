---
ContentId: e6b33fcb-8240-49dd-b6ca-5412d6fa669a
DateApproved: 3/4/2026
MetaDescription: Visual Studio Code'da Inline Chat ile editörde doğrudan düzenleme yapın veya terminalde komut önerileri alın.
MetaSocialImage: ../images/shared/github-copilot-social.png
---
# Inline chat

Visual Studio Code'da inline chat ile editörde doğrudan kod oluşturma veya düzenleme isteyebilir veya entegre terminal içinde kabuk komutları konusunda yardım alabilirsiniz. Inline chat ayrı bir Chat görünümüne geçmeden iş akışınızda kalmanızı sağlar.

Görünür kod bağlamı içinde hızlı, hedefli düzenlemeler yapmak istediğinizde inline chat kullanın. Çok adımlı görevler, çok dosyalı değişiklikler veya daha geniş kod tabanı keşfi için bunun yerine [Chat görünümünü](/docs/copilot/chat/copilot-chat.md) kullanın.

## Editör inline chat kullanın

Editör inline chat kullandığınızda isteminiz etkin editördeki kodla kapsamlanır. Inline chat isteminiz için çalışma alanınızdaki diğer dosyalardaki içeriği bağlam olarak kullanabilir.

Editör inline chat kullanmak için:

1. Editörde bir dosya açın.

1. `kb(inlinechat.start)` klavye kısayolunu kullanarak veya başlık çubuğundaki Chat menüsünden **Open Inline Chat** seçerek editör inline chat'i açın.

1. Chat giriş alanına isteminizi yazın ve `kbstyle(Enter)` tuşuna basın.

    > [!TIP]
    > İstemi o kodla kapsamlamak için editörde bir kod bloğu seçin.

1. VS Code editörde satır içi kod önerisiyle bir diff gösterir. Değişiklikleri kabul edin veya reddedin.

    ![Özyinelemesiz factorial uygulaması öneren editör inline chat ekran görüntüsü.](images/copilot-chat/inline-chat-no-recursion.png)

1. İsteğe bağlı olarak diğer öneriler almak veya sonuçları iyileştirmek için takip sorusu sorun.

> [!TIP]
> İlgili dosyaları, kod sembollerini veya diğer bağlamı dahil etmek için inline chat isteminize bağlam ekleyin. [Sohbet isteminize bağlam ekleme](/docs/copilot/chat/copilot-chat-context.md) hakkında daha fazla bilgi edinin.

### Metin seçiminde görsel ipucu göster (Deneysel)

Editörde metin seçtiğinizde VS Code seçilen kod için inline chat başlatmanıza yardımcı olacak görsel bir ipucu gösterebilir. Bu ipucunun nasıl göründüğünü kontrol etmek için `setting(inlineChat.affordance)` ayarını kullanın:

* `off`: metin seçtiğinizde ipucu gösterilmez
* `gutter`: ipucu seçiminizin yanındaki satır numarası alanında görünür
* `editor`: ipucu seçiminiz içindeki imleç konumunda görünür; kod eylemleri için ampulle entegre

![Editörde metin seçildiğinde kenar boşluğundaki inline chat ipucusunu gösteren ekran görüntüsü.](images/copilot-chat/inline-chat-hint-gutter.png)

İpucu inline chat giriş kutusunu ve seçimi sohbete ekleme, kodu açıklama ve seçimin kod incelemesini başlatma eylemlerini gösterir.

> [!NOTE]
> Bu özellik deneyseldir ve `setting(inlineChat.renderMode)` ayarı `hover` olarak ayarlandığında çalışır.

## Terminal inline chat kullanın

Kabuk komutları konusunda yardım almak veya terminalle ilgili sorular sormak için [entegre terminalde](/docs/terminal/basics.md) terminal inline chat'i açabilirsiniz.

Terminal inline chat kullanmak için:

1. VS Code'da **View** > **Terminal** menü öğesini seçerek veya `kb(workbench.action.terminal.toggleTerminal)` klavye kısayolunu kullanarak terminali açın.

1. `kb(workbench.action.terminal.chat.start)` klavye kısayolunu kullanarak veya Komut Paleti'nde **Terminal Inline Chat** komutunu çalıştırarak terminal inline chat'i başlatın.

1. Chat giriş alanına isteminizi yazın ve `kbstyle(Enter)` tuşuna basın.

    !["src klasöründeki en büyük 5 dosyayı listele" gibi karmaşık sorular sorabileceğinizi gösteren ekran görüntüsü](images/copilot-chat/terminal-chat-2.png)

1. Yanıtı inceleyin ve komutu terminalde çalıştırmak için **Run** (`kb(workbench.action.terminal.chat.runCommand)`) seçin

    Alternatif olarak komutu terminale ekleyip çalıştırmadan önce değiştirmek için **Insert** (`kb(workbench.action.terminal.chat.insertCommand)`) seçin.

## Inline chat için modeli değiştirin

Editör inline chat için kullanılan dil modelini değiştirebilirsiniz. Varsayılan olarak inline chat Chat görünümüyle aynı modeli kullanır ancak inline chat için belirli bir varsayılan model yapılandırabilirsiniz.

Inline chat için varsayılan modeli yapılandırmak üzere `setting(inlineChat.defaultModel)` ayarını kullanın. Ayar model seçiciden tüm mevcut modelleri listeler.

Bir inline chat oturumu sırasında modeli değiştirirseniz seçim oturumun geri kalanında kalır. VS Code'u yeniden yükledikten sonra model `setting(inlineChat.defaultModel)` ayarında belirtilen değere sıfırlanır.

[Göreviniz için doğru modeli seçme](/docs/copilot/customization/language-models.md#choose-the-right-model-for-your-task) hakkında daha fazla bilgi edinin.

## Quick Chat kullanın

Quick Chat editörün üstünde açılan hafif bir chat paneli sunar. Tam Chat görünümünü açmadan veya mevcut iş akışınızdan ayrılmadan hızlı sorular ve kısa etkileşimler için kullanın.

Quick Chat'i açmak için `kb(workbench.action.quickchat.toggle)` tuşuna basın veya başlık çubuğundaki **Chat** menüsünden **Quick Chat** seçin.

Yanıt almak için isteminizi yazın ve `kbstyle(Enter)` tuşuna basın. Quick Chat bağlam eklemek için Chat görünümüyle aynı `#`-bahsetmeleri ve `@`-bahsetmeleri destekler. Konuşmaya tam Chat görünümünde devam etmek için **Open in Chat View** düğmesini seçin.

## İlgili kaynaklar

* [Chat genel bakış](/docs/copilot/chat/copilot-chat.md)
* [Sohbet isteminize bağlam ekleyin](/docs/copilot/chat/copilot-chat-context.md)
* [AI ile üretilen kod düzenlemelerini inceleyin](/docs/copilot/chat/review-code-edits.md)
* [VS Code'da AI dil modelleri](/docs/copilot/customization/language-models.md)
