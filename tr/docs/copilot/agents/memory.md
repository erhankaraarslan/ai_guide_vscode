---
ContentId: 3a7e9c4f-5d1b-4e8f-a2c6-8b0d3f5e7a9c
DateApproved: 3/4/2026
MetaDescription: VS Code'daki ajanların bağlamı korumak, tercihleri öğrenmek ve görüşmeler arasında zamanla iyileştirmek için bellek aracını ve Copilot Memory'yi nasıl kullandığını öğrenin.
MetaSocialImage: ../images/shared/github-copilot-social.png
---

# VS Code ajanlarında bellek

Visual Studio Code'daki ajanlar bağlamı görüşmeler arasında korumak için bellek kullanır. Her oturumda sıfırdan başlamak yerine ajanlar tercihlerinizi hatırlar, önceki görevlerden dersler uygular ve zamanla kod tabanınız hakkında bilgi oluşturur.

VS Code iki tamamlayıcı bellek sistemi destekler:

* **Bellek aracı**: Makinenizde yerel olarak notları depolayan, üç kapsamda (kullanıcı, depo ve oturum) düzenlenen yerleşik bir araç. Ajanlar çalışırken hem belleğe okur hem de yazar.
* **Copilot Memory**: Kodlama ajanı, kod inceleme ve CLI gibi Copilot ajanları arasında depo özelinde içgörüleri yakalayan GitHub barındırmalı bir bellek sistemi. Copilot Memory VS Code'un ötesinde GitHub Copilot yüzeylerinde paylaşılır.

Bu makale VS Code'da bellek aracının nasıl kullanılacağını, bellek dosyalarının nasıl yönetileceğini ve Copilot Memory'nin geliştirme iş akışınız genelinde belleği nasıl genişlettiğini açıklar.

## Bellek aracı

> [!NOTE]
> Bellek aracı şu anda önizlemededir. `setting(github.copilot.chat.tools.memory.enabled)` ayarıyla etkinleştirip devre dışı bırakabilirsiniz.

Bellek aracı, ajanların çalışırken not kaydetmesine ve hatırlamasına olanak tanıyan yerleşik bir ajan aracıdır. Ayrıca ajana bir şeyi açıkça hatırlatmanızı da isteyebilirsiniz. Tüm veriler makinenizde yerel olarak depolanır. Bellek aracı varsayılan olarak etkindir.

### Bellek kapsamları

Her kapsam bilginin ne kadar süre kalması ve nerede geçerli olması gerektiğine bağlı olarak farklı bir amaca hizmet eder.

| Kapsam | Yol | Oturumlar arasında kalır | Çalışma alanları arasında kalır | Kullanım amacı |
|--------|-----|--------------------------|----------------------------------|-----------------|
| **Kullanıcı** | `/memories/` | Evet | Evet | Tercihler, desenler, sık kullanılan komutlar |
| **Depo** | `/memories/repo/` | Evet | Hayır (çalışma alanı kapsamlı) | Kod tabanı sözleşmeleri, proje yapısı, derleme komutları |
| **Oturum** | `/memories/session/` | Hayır (sohbet bitince temizlenir) | Hayır | Görev özelinde bağlam, devam eden planlar |

#### Kullanıcı belleği

Kullanıcı belleği tüm çalışma alanlarında ve görüşmelerde kalır. İlk 200 satır her oturumun başında otomatik olarak ajanın bağlamına yüklenir. Hangi projede çalışırsanız çalışın geçerli olan genel tercihler ve içgörüler için kullanıcı belleği kullanın.

Örneğin ajanın bir kodlama tercihini hatırlamasını isteyin:

```prompt
Remember that I prefer tabs over spaces and always use single quotes in JavaScript
```

Daha sonraki bir görüşmede, hatta farklı bir çalışma alanında bile ajan bu tercihi hatırlar ve oluşturulan koda uygular.

#### Depo belleği

Depo belleği mevcut çalışma alanına kapsamlıdır ve o çalışma alanındaki görüşmelerde kalır. Mimari kararlar, adlandırma sözleşmeleri veya derleme komutları gibi belirli bir kod tabanı hakkındaki gerçekler için depo belleği kullanın.

Örneğin:

```prompt
Remember that this project uses the repository pattern for data access and all API endpoints require authentication
```

#### Oturum belleği

Oturum belleği mevcut görüşmeye kapsamlıdır ve görüşme bittiğinde temizlenir. Plan ajanı uygulama planlarını bir `plan.md` dosyasında kalıcı hale getirmek için oturum belleği kullanır. Ajan çok adımlı bir görev üzerinde çalışırken takip ettiği geçici çalışma notları veya görev özelinde bağlam için oturum belleği kullanın.

Bu plan oturum sırasında kullanılabilir ve **Chat: Show Memory Files** komutuyla görüntülenebilir ancak sonraki oturumlarda mevcut değildir. [Ajanlarla planlama](/docs/copilot/agents/planning.md) hakkında daha fazla bilgi edinin.

### Bellekleri depolama ve alma

Bellek depolamak için ajana doğal dilde bir şeyi hatırlamasını isteyin. Ajan uygun kapsamı belirler ve ilgili bellek dosyasını oluşturur veya günceller.

```prompt
Remember that our team uses conventional commits for all commit messages
```

Belleği almak için yeni bir görüşmede sorun. Ajan bellek dosyalarını kontrol eder ve ilgili bilgiyi hatırlar.

```prompt
What are our commit message conventions?
```

Ajanın sohbet yanıtlarındaki bellek dosyası referansları tıklanabilir, böylece bellek dosyasının içeriğini doğrudan görüntüleyebilirsiniz.

### Bellek dosyalarını yönetme

VS Code bellek dosyalarınızı görüntülemek ve yönetmek için komutlar sağlar:

* **Chat: Show Memory Files**: Tüm kapsamlardaki tüm bellek dosyalarının listesini açar. İçeriğini görüntülemek için bir dosya seçin.
* **Chat: Clear All Memory Files**: Tüm kapsamlardaki tüm bellek dosyalarını kaldırır.

> [!NOTE]
> Tek tek bellek dosyalarını silmek henüz desteklenmiyor. Tüm bellekleri kaldırmak için **Chat: Clear All Memory Files** kullanın veya güncel olmayan bilgileri kaldırmak için ajana belirli bir bellek dosyasını güncellemesini isteyin.

## Copilot Memory

> [!NOTE]
> Copilot Memory önizlemededir ve yukarıda açıklanan yerel bellek aracından ayrıdır.

[Copilot Memory](https://docs.github.com/copilot/how-tos/use-copilot-agents/copilot-memory), Copilot'un çalışırken öğrenmesine ve depo özelinde içgörüleri korumasına olanak tanıyan GitHub barındırmalı bir bellek sistemidir. Yerel bellek aracının aksine Copilot Memory, Copilot kodlama ajanı, Copilot kod inceleme ve Copilot CLI dahil birden fazla GitHub Copilot yüzeyinde paylaşılır.

### Copilot Memory nasıl çalışır

Copilot ajanları depolarınızda çalışırken "bellekler" adı verilen dar kapsamlı içgörüleri otomatik olarak yakalar. Bu bellekler:

* **Depo kapsamlı**: Bellekler belirli bir depoya bağlıdır ve yalnızca yazma erişimine sahip katkıda bulunanlar tarafından oluşturulabilir.
* **Ajanlar arası**: Bir Copilot ajanının öğrendiği diğer ajanlara kullanılabilir. Örneğin Copilot kod inceleme tarafından keşfedilen bir desen daha sonra Copilot kodlama ajanına rehberlik edebilir.
* **Kullanımdan önce doğrulanır**: Ajanlar güncel olmayan veya yanlış bilgilerin sonuçları etkilemesini önlemek için belleği uygulamadan önce mevcut kod tabanına karşı doğrular.
* **Otomatik süre dolar**: Bellekler güncel olmayan bilgileri önlemek için 28 gün sonra silinir.

### Copilot Memory'yi etkinleştirme

Copilot Memory varsayılan olarak kapalıdır ve GitHub ayarlarınızda etkinleştirilmesi gerekir:

* **Bireysel kullanıcılar** (Copilot Pro veya Pro+): GitHub'da [kişisel Copilot ayarlarınızda](https://github.com/settings/copilot) Copilot Memory'yi etkinleştirin.
* **Kuruluşlar ve kuruluşlar**: Kuruluş veya kuruluş ayarlarında politika ayarları üzerinden etkinleştirin.

Ayrıca VS Code'da `setting(github.copilot.chat.copilotMemory.enabled)` ayarıyla Copilot Memory entegrasyonunu etkinleştirmeniz gerekir.

Depo sahipleri **Repository Settings** > **Copilot** > **Memory** bölümünde depolanan belleği inceleyebilir ve silebilir.

Ayrıntılı kurulum talimatları için GitHub belgelerinde [Copilot Memory'yi etkinleştirme ve düzenleme](https://docs.github.com/copilot/how-tos/use-copilot-agents/copilot-memory) bölümüne bakın.

### Bellek aracı ve Copilot Memory karşılaştırması

| | Bellek aracı | Copilot Memory |
|--|-------------|----------------|
| **Depolama** | Yerel (makinenizde) | GitHub barındırmalı (uzak) |
| **Kapsamlar** | Kullanıcı, depo, oturum | Yalnızca depo |
| **Copilot yüzeylerinde paylaşılır** | Hayır (yalnızca VS Code) | Evet (kodlama ajanı, kod inceleme, CLI) |
| **Oluşturan** | Siz veya sohbet sırasında ajan | Copilot ajanları otomatik olarak |
| **Varsayılan olarak etkin** | Evet | Hayır (katılım gerekli) |
| **Süre sonu** | Manuel yönetim | Otomatik (28 gün) |

İki sistem tamamlayıcıdır. VS Code'da kişisel tercihler ve oturum özelinde bağlam için yerel bellek aracını kullanın. Geliştirme iş akışınız genelinde tüm Copilot ajanlarından faydalanacak depo bilgisi için Copilot Memory kullanın.

## İlgili kaynaklar

* [Ajanlarla planlama](/docs/copilot/agents/planning.md)
* [Ajan araçları](/docs/copilot/agents/agent-tools.md)
* [Copilot Memory'yi etkinleştirme ve düzenleme](https://docs.github.com/copilot/how-tos/use-copilot-agents/copilot-memory) (GitHub belgeleri)
* [GitHub Copilot için ajanik bellek sistemi oluşturma](https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot/) (GitHub blog)
