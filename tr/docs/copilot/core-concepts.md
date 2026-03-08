---
ContentId: d8b3c7f1-2e4a-5b6d-9c0e-1f3a5b7d9e2c
DateApproved: 3/4/2026
MetaDescription: VS Code'da GitHub Copilot'un dil modelleri ve bağlamdan ajanlara ve ajantik döngüye kadar nasıl çalıştığını öğrenin.
MetaSocialImage: images/shared/github-copilot-social.png
Keywords:
- copilot
- ai
- concepts
- language model
- context window
- agents
- agentic loop
- autonomous
- multi-file editing
- deep context
- architecture
- semantic search
---

# VS Code'da AI nasıl çalışır

Visual Studio Code'un yerleşik AI özellikleri GitHub Copilot ve büyük dil modelleri (LLM) tarafından desteklenir. Bu özellikler yazarken görünen satır içi önerilerden tüm özellikleri uygulayan otonom ajanlara kadar birden fazla arayüzü kapsar. Bu makale temel mimariyi, anahtar kavramları ve tüm AI özelliklerinin nasıl bağlandığını açıklar. Uygulamalı bir öğretici için [Hızlı başlangıç](/docs/copilot/getting-started.md) sayfasına bakın. Pratik ipuçları için [En iyi uygulamalar](/docs/copilot/best-practices.md) bölümüne bakın.

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="Get started with agents">
VS Code'da yerel, arka plan ve bulut ajanlarını deneyimlemek için uygulamalı öğreticiyi takip edin.

* [Öğreticiyi başlat](/docs/copilot/agents/agents-tutorial.md)

</div>

## AI özelliklerine genel bakış

VS Code, farklı görevlere uygun geniş bir etkileşim yelpazesi sunar:

* **[Ajanlar](/docs/copilot/agents/overview.md)**: tam [ajan döngüsünü](#agent-loop) takip eden otonom oturumlar; dosyaları okur, birden fazla dosyada koordineli değişiklikler yapar, komutları çalıştırır ve görev tamamlanana kadar yineleyerek ilerler. Ajanlar özellik uygulamaktan mimari düzeyinde yeniden düzenlemeye ve framework geçişlerine kadar çok adımlı görevleri uçtan uca ele alır.
* **[Chat](/docs/copilot/chat/copilot-chat.md)**: soru sorduğunuz, fikirleri keşfettiğiniz veya açıklamalar aldığınız sohbet arayüzü. Ask modunda model kodunuzu değiştirmeden soruları yanıtlamak için salt okunur araçlar kullanır.
* **[Inline chat](/docs/copilot/chat/inline-chat.md)**: hızlı, odaklı düzenlemeler için doğrudan editörde açılan hafif bir sohbet arayüzü.
* **[Satır içi öneriler](/docs/copilot/ai-powered-suggestions.md)**: yazarken hayalet metin olarak görünen kod önerileri. Bunlar özelleştirilmiş tamamlama modelleri kullanır ve ajan döngüsü veya araç gerektirmez. [Sonraki Düzenleme Önerileri (NES)](/docs/copilot/ai-powered-suggestions.md#next-edit-suggestions) bir sonraki düzenlemenizin *nereye* yapılması gerektiğini tahmin ederek daha ileri gider.
* **[Akıllı eylemler](/docs/copilot/copilot-smart-actions.md)**: iş akışınıza entegre tek tıklamalı AI eylemleri; commit mesajı oluşturma veya tanı teşhis hatalarını düzeltme gibi.

## Dil modelleri

VS Code, AI özelliklerini desteklemek için büyük dil modelleri (LLM) kullanır. GitHub Copilot planınız üzerinden birden fazla model arasından seçim yapabilir veya kendi modellerinizi getirebilirsiniz.

Her modelin farklı güçlü ve zayıf yönleri vardır. Bazıları hız için optimize edilmiş olup basit tamamlamalar için uygundur. Diğerleri daha geniş bağlam penceresine veya daha iyi akıl yürütme yeteneklerine sahiptir ve karmaşık görevler için idealdir. Belirli bir görevin ihtiyaçlarına göre istediğiniz zaman model değiştirebilirsiniz.

LLM'lerin temel özellikleri:

* **Belirleyici olmayan**: aynı istem her seferinde farklı sonuçlar üretebilir. Bu tasarım gereğidir ve modelin olasılık dağılımlarından nasıl örneklediğini yansıtır.
* **Bağlama bağımlı**: yanıtın kalitesi, istemde sağlanan bağlamın kalitesine ve ilgiselliğine bağlıdır.
* **Bilgi sınırları**: modeller belirli bir tarihe kadar verilerle eğitilmiştir; eğitim verilerinin ötesindeki konularda güncel olmayan veya hatalı bilgi üretebilirler. Copilot bunu web araması ve çalışma alanı indekslemesi gibi araçlarla hafifletir.

[Dil modelleri seçme ve yapılandırma](/docs/copilot/customization/language-models.md) hakkında daha fazla bilgi edinin.

## Ajan döngüsü

Bir AI kodlama asistanına bir görev verdiğinizde, genellikle ajantik döngüyü takip eder. Bu model modern AI asistanlarında yaygındır. VS Code içinde bir ajan, plan yapan ve eylemler gerçekleştiren sistemdir; [dil modeli](#language-models) ise bu eylemleri bilgilendiren yanıtlar üretir.

Her adımda ajan ilerlemesini değerlendirir ve bir sonraki eylemi seçer. Bir API'yi anlamak için bir dosya açabilir, bir düzenleme yapabilir, sonra değişikliğin çalıştığını doğrulamak için bir komut çalıştırabilir. Her eylemin çıktısı, bir sonraki karar için girdi olur.

![Ajantik döngü diyagramı: Kullanıcı istemi -> Ajan akıl yürütmesi -> Araç çağrıları (dosya okuma, kod düzenleme, test çalıştırma) -> Araç sonuçlarına göre ajan güncellemesi -> Kullanıcı incelemesi için nihai çıktı](images/core-concepts/agent-loop.png)

Ajan döngüsü tipik olarak üç üst düzey aşamadan oluşur:

1. **Anlama.** Ajan değişiklik gerekenleri anlamak için dosyaları okur, kod tabanını arar ve dokümantasyona bakar.
1. **Eyleme geçme.** Ajan kodu düzenler, terminal komutları çalıştırır, bağımlılıkları yükler veya araçlar aracılığıyla harici hizmetleri çağırır.
1. **Doğrulama.** Ajan testleri çalıştırır, derleyici hatalarını kontrol eder ve kendi değişikliklerini inceler. Bir sorun varsa yinelemeye devam eder.

Ajan, en iyi eylem yolunu düşünmek için [dil modelini](#language-models) kullanır. Ancak kodunuz veya VS Code ortamı gibi ortamla etkileşim kurma yeteneği olmadan model yalnızca genel yanıtlar verebilir. [Ajan araçları](#tools) ile ajan her adımda dosya okuma, kod değişikliği yapma, terminal komutları çalıştırma ve harici hizmetlere ulaşma gibi bilgi toplamak ve eylem gerçekleştirmek için araç çağrıları yapar.

Ajan görevi tamamlayana kadar bu eylemleri gerektiği gibi zincirler. Kod tabanınız hakkında bir soruyu yanıtlamak yalnızca birkaç dosya okuması gerektirebilir. Yeni bir özellik uygulamak tipik olarak düzenleme, test çalıştırma, hata teşhisi ve testler geçene kadar tekrar düzenleme döngüsünden geçer.

Süreç boyunca kontrol sizdedir. Ajanı yönlendirmek, bağlam eklemek veya farklı bir yaklaşım önermek için yeni bir mesaj gönderin. Değişiklikleri inceleme ve ajan davranışını yönetme hakkında daha fazla bilgi için [Kontrol sizde](#stay-in-control) bölümüne bakın.

Perde arkasında, [VS Code mevcut bağlamı](#how-vs-code-assembles-context) bir istemde bir araya getirir ve dil modeline gönderir. Model metin, kod düzenlemesi veya araç talebi ile yanıt verir. Bir araç çalıştığında çıktısı bir sonraki yineleme için bağlama eklenir ve bu döngü görev tamamlanana kadar tekrarlanır.

## Ajan döngüsünü özelleştirin

Ajan döngüsü her proje için tek tip değildir ve projeden projeye farklılık gösterebilir. Ajanın davranışını kişiselleştirmek için özel ajanlar, ajan becerileri, talimatlar veya kancalar gibi farklı seçenekler vardır; bunlarla projeniz veya ekibiniz için ajan döngüsünü optimize edebilirsiniz.

[**Özel ajan**](/docs/copilot/customization/custom-agents) ajan için farklı kişilikler tanımlamanızı sağlar; her birinin kendi talimatları, kullanılabilir araçları, dil modeli ve isteğe bağlı olarak başka bir ajana devretme özelliği vardır. Yerleşik Plan ajanı özellik uygulama planları oluşturmada uzmanlaşmıştır. Derin araştırma ve analiz yapmak için yalnızca salt okunur araçlara erişimi vardır ve kod tabanında değişiklik yapmadan ayrıntılı bir uygulama yaklaşımı özetler.

[**Ajan becerileri**](/docs/copilot/customization/agent-skills.md) ile ajanı belirli bir etki alanı veya görev için yeni yeteneklerle donatabilirsiniz; ajan elindeki görevle ilgili olduğunda bu becerilere dinamik olarak başvurabilir. Örneğin, güvenlik açıkları analiz talimatlarını ve bilinen savunmasızlık veritabanlarına karşı kontrol araçlarını içeren bir güvenlik denetimi becerisi oluşturabilirsiniz.

[AI özelleştirme seçenekleri](/docs/copilot/customization/overview.md) hakkında daha fazla bilgi edinin.

## Bağlam

Bağlam, model bir yanıt üretirken görebildiği her şeydir. Sohbet geçmişini, çalışma alanınızdaki dosya içeriklerini, araç çıktılarını, özel talimatları ve açıkça eklediğiniz referansları içerir.

Bağlam önemlidir çünkü model yalnızca görebildiği hakkında akıl yürütebilir. İlgili dosyalar, net talimatlar ve odaklı geçmiş içeren bir istem, bağlamı olmayan belirsiz bir istemden daha iyi sonuçlar üretir.

VS Code bağlamı otomatik olarak toplar ve ne ekleyeceğiniz konusunda size kontrol verir:

* **Otomatik bağlam**: düzenlediğiniz dosya, çalışma alanı indeksiniz, git durumu ve sohbet geçmişi.
* **Açık bağlam**: modeli belirli bilgilere yönlendirmek için `#file`, `#codebase`, `#web` ve diğer [#-bahsetmeler](/docs/copilot/chat/copilot-chat-context.md) kullanın.
* **Kalıcı bağlam**: [özel talimatlar](/docs/copilot/customization/custom-instructions.md) kendinizi tekrarlamadan sohbet isteklerine proje özelinde bağlam eklemenizi sağlar.

### Bağlam penceresi

Bağlam penceresi, modelin tek bir istekte işleyebileceği toplam bilgi miktarıdır. Her şeyi içerir: sistem istemi, özel talimatlar, sohbet geçmişi, dosya içerikleri, araç çıktıları ve mevcut mesajınız. Farklı modellerin farklı bağlam penceresi boyutları vardır.

Bağlam penceresi dolduğunda VS Code yer açmak için otomatik olarak sohbetin eski bölümlerini özetler. Bu, uzun bir sohbetteki erken önemli detayların sıkıştırılabileceği veya kaybolabileceği anlamına gelir. Bağlam penceresi dolmasını beklemeden herhangi bir anda manuel olarak sıkıştırmayı tetiklemek için sohbet girişine `/compact` yazabilirsiniz. İsteğe bağlı olarak özet için rehberlik etmesi amacıyla komuttan sonra özel talimatlar ekleyebilirsiniz, örneğin `/compact focus on the API design decisions`.

Bağlam penceresi sınırlarıyla etkili çalışmak için:

* **Yeni görevler için yeni oturumlar başlatın.** Bir [oturum](/docs/copilot/chat/chat-sessions.md) kendi bağlam penceresi ve geçmişi olan bağımsız bir sohbettir. Her oturum sıfırdan başlar, bu yüzden ilgisiz görevler için tek bir sohbeti yeniden kullanmayın.
* **Bağlam konusunda seçici olun.** Tüm kod tabanınızı eklemek her zaman yardımcı olmaz. Görevle ilgili belirli dosyalara referans verin.
* **Kalıcı kurallar için özel talimatları kullanın.** [Özel talimatlar](/docs/copilot/customization/custom-instructions.md)'da eklediğiniz kurallar her istekte dahil edilir, bu yüzden sohbet özetlendiğinde kaybolmazlar.

### VS Code bağlamı nasıl bir araya getirir

Bir mesaj gönderdiğinizde VS Code birden fazla kaynaktan bir dil modeli istemi oluşturur:

![Bağlam penceresini yedi katmanlı bir konteyner olarak gösteren diyagram: sistem talimatları, özelleştirmeler, kullanıcı mesajı, sohbet geçmişi, örtülü bağlam, açık referanslar ve araç çıktıları, birleştirilmiş istemi dil modeline gönderen ok ile](images/core-concepts/context-assembly.png)

* **Sistem talimatları**: ajanın davranışını tanımlayan yerleşik yönergeler.
* **Özelleştirmeler**: özel ajanlar, beceriler ve özel talimatlar dahil ayarladığınız AI özelleştirmeleri.
* **Kullanıcı mesajı**: ajana gönderdiğiniz mevcut mesaj.
* **Sohbet geçmişi**: mevcut oturumda şimdiye kadar alışveriş yapılan mesajlar.
* **Örtülü bağlam**: düzenlediğiniz dosya, mevcut seçiminiz, görünür hatalar ve git durumu.
* **Açık referanslar**: `#`-bahsetmelerle referans verdiğiniz dosyalar, editör bağlamı, web içeriği ve diğer kaynaklar.
* **Araç çıktıları**: ajan oturumları sırasında dosya okumaları, terminal komutları, kod tabanı arama sonuçları ve diğer araç çağrılarından gelen sonuçlar.

Bu birleştirilmiş istem modelin gördüğü şeydir. Dışındaki her şey modele görünmezdir. Bu nedenle `#file` ile belirli dosyalara referans vermek, modelin görmediği kod hakkında sormaktan daha iyi sonuçlar üretir.

[Sohbete bağlam ekleme](/docs/copilot/chat/copilot-chat-context.md) ve [çalışma alanı indekslemesi](/docs/copilot/reference/workspace-context.md) hakkında daha fazla bilgi edinin.

## Araçlar

Araçlar, modelin geliştirme ortamınızda işlem yapmasını sağlayan mekanizmadır. VS Code dosya okuma ve yazma, terminal komutları çalıştırma, kod tabanınızı arama ve editörde gezinme için yerleşik araçlar içerir.

Yerleşik araçların ötesinde ajanın yapabileceklerini genişletebilirsiniz:

* **[MCP sunucuları](/docs/copilot/customization/mcp-servers.md)**: Model Bağlam Protokolü (MCP) aracılığıyla harici hizmetlere bağlanın; AI modellerine harici araç ve veri kaynaklarına erişim sağlayan açık bir standart.
* **[Ajan becerileri](/docs/copilot/customization/agent-skills.md)**: API dokümantasyonu oluşturma veya bileşen iskelesi kurma gibi etki alanına özgü görevleri ajanı öğretin.
* **[Kancalar](/docs/copilot/customization/hooks.md)**: her düzenlemeden sonra kodu biçimlendirme gibi ajan döngüsündeki belirli noktalarda komutları otomatik olarak çalıştırın.

[Ajanlar için mevcut araçlar](/docs/copilot/agents/agent-tools.md) hakkında daha fazla bilgi edinin.

## Ajan türleri

Ajanlar sonuçlara ne zaman ihtiyacınız olduğuna ve ne kadar denetim istediğinize bağlı olarak farklı ortamlarda çalışır:

* **Yerel ajanlar** VS Code'da etkileşimli olarak çalışır. Her adımı görürsünüz ve ajanı gerçek zamanlı yönlendirebilirsiniz. Elinizi hiç çekmek istemediğiniz görevler için idealdir.
* **Arka plan ajanları** makinenizde otonom çalışır. Bir görevi devredin ve ajan tamamlayana kadar diğer işlere devam edin.
* **Bulut ajanları** GitHub'ın altyapısında çalışır. Dallar oluşturur, değişiklikleri uygular ve ekibinizin incelemesi için pull request açar.
* **Üçüncü taraf ajanlar** Anthropic ve OpenAI gibi harici AI sağlayıcılarına bağlanır. Ajan türleri arasında oturumları istediğiniz anda devredebilirsiniz.

![Farklı ajan türlerini gösteren diyagram: Yerel ajanlar (VS Code'da etkileşimli), Arka plan ajanları (makinenizde otonom), Bulut ajanları (GitHub altyapısında çalışır) ve Üçüncü taraf ajanlar (harici AI sağlayıcılarına bağlanır)](images/agents-overview/agent-types-diagram-v3.png)

[Ajanlar ve ajan oturumları](/docs/copilot/agents/overview.md) hakkında daha fazla bilgi edinin.

## Kontrol sizde

AI ile üretilen çıktı inceleme gerektirir. VS Code, kod tabanınıza ulaşan değişikliklerin kontrolünde kalmanız için birden fazla mekanizma içerir.

* **Uygulamadan önce düzenlemeleri inceleyin.** Ajanlar dosya değişikliklerini diff görünümünde gösterir. Her değişikliği inceleyebilir, tek tek düzenlemeleri kabul edebilir veya reddedebilir ve kaydetmeden önce kodu değiştirebilirsiniz. [Kod düzenlemelerini inceleme](/docs/copilot/chat/review-code-edits.md) hakkında daha fazla bilgi edinin.

* **Geri almak için kontrol noktaları kullanın.** Ajan oturumları ilerleme kaydettikçe kontrol noktaları oluşturur. Ajan yanlış yola saparsa önceki bir kontrol noktasına dönün ve farklı bir yaklaşım deneyin. [Kontrol noktaları](/docs/copilot/chat/chat-checkpoints.md) hakkında daha fazla bilgi edinin.

* **Araç çağrılarını onaylayın.** VS Code terminal komutları çalıştırmadan veya yan etkili araçları kullanmadan önce onayınızı ister. Hangi araçların otomatik çalışabileceğini ve hangilerinin onay gerektirdiğini siz kontrol edersiniz.

* **Güven sınırları.** VS Code dosya erişimi, URL erişimi, terminal sandboxing ve MCP sunucu etkileşimleri için güvenlik sınırları uygular. [AI güvenliği](/docs/copilot/security.md) hakkında daha fazla bilgi edinin.

Taahhüt etmeden önce her zaman AI ile üretilen kodu inceleyin. Kenar durumlarını ele aldığını, projenizin sözleşmelerine uyduğunu ve güvenlik sorunları getirmediğini doğrulayın.

## AI sınırlamaları

AI güçlü bir araçtır ancak anlamanız gereken önemli sınırlamaları vardır.

**Belirleyici olmama.** Aynı istem her seferinde farklı sonuçlar üretebilir. Bu, aynı soruyu iki kez sorduğunuzda farklı bir kod önerisi, açıklama veya yaklaşım alabileceğiniz anlamına gelir. Bu normaldir ve modellerin olasılık dağılımlarından nasıl örneklediğini yansıtır.

**Hatalı çıktı.** Modeller doğru görünen ancak hata içeren, kullanımdan kaldırılmış API'leri kullanan veya kenar durumlarını ele almayan kod üretebilir. Özellikle güvenlik, veri bütünlüğü veya kritik akışları etkileyen mantık için her zaman AI ile üretilen kodu test edin.

**Bilgi sınırları.** Modeller belirli bir tarihe kadar verilerle eğitilmiştir. Yeni framework sürümleri, yeni çıkan API'ler veya projenizdeki değişiklikler hakkında bilgileri olmayabilir. Copilot'a güncel bilgiye erişim vermek için `#web` kullanın ve yanıtları gerçek kodunuzda temellendirmek için `#file` ile belirli dosyalara referans verin.

**Bağlam sınırları.** Sohbet uzadıkça model önceki bağlama erişimini kaybeder. Yanıtlar bozulmaya başlarsa yeni bir oturum başlatın ve elindeki görev için taze bağlam sağlayın.

**İstem enjeksiyonu.** Dosyalardaki, araç çıktılarındaki veya web sayfalarındaki kötü niyetli içerik ajanın davranışını yönlendirmeye çalışabilir. Bu nedenle VS Code [araç onay kapıları ve güven sınırları](#stay-in-control) içerir. [AI güvenliği](/docs/copilot/security.md) hakkında daha fazla bilgi edinin.

AI ile etkili çalışmanın en iyi yolu çıktısını ilk taslak olarak görmektir: başlangıç noktası olarak faydalı ancak her zaman incelemeniz ve yargınız gerekiyor.

## İlgili kaynaklar

* [VS Code'da AI ile başlayın](/docs/copilot/getting-started.md)
* [VS Code'da AI kullanımı için en iyi uygulamalar](/docs/copilot/best-practices.md)
* [VS Code'da ajanları kullanma](/docs/copilot/agents/overview.md)
