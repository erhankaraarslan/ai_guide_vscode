---
ContentId: 9d8f3a2b-5c6e-4f7a-8b9c-1d2e3f4a5b6c
DateApproved: 3/4/2026
MetaDescription: Kod oluşturma, hata ayıklama, test ve notebook'larla çalışma dahil farklı senaryolarda VS Code chat için etkili istem örneklerini keşfedin.
MetaSocialImage: ../images/shared/github-copilot-social.png
---
# İstem örnekleri

Bu makale farklı senaryolar ve ajanlar genelinde Visual Studio Code chat için örnek istemler sunar. Kendi geliştirme görevleriniz için etkili istemler oluşturmak üzere bu örnekleri ilham olarak kullanın.

VS Code'da chat kullanmaya yeni başlıyorsanız [chat ile başlarken](/docs/copilot/chat/copilot-chat.md) veya [istem oluşturma için en iyi uygulamalar](/docs/copilot/guides/prompt-engineering-guide.md) hakkında daha fazla bilgi edinin.

<div class="docs-action" data-show-in-doc="false" data-show-in-sidebar="true" title="Get started with agents">
VS Code'da yerel, arka plan ve bulut ajanlarını deneyimlemek için uygulamalı öğreticiyi takip edin.

* [Öğreticiyi başlat](/docs/copilot/agents/agents-tutorial.md)

</div>

## Genel kodlama ve teknoloji soruları

Kodlama kavramları, teknoloji konuları ve genel programlama soruları hakkında hızlı yanıtlar almak için **Ask** ajanını kullanın.

```prompt-ask
What is a linked list?
```

```prompt-ask
Provide 3 ways to implement a search feature in React.
```

```prompt-ask
Explain the difference between async/await and promises.
```

## Kod tabanınızı anlama ve keşfetme

Projenizin nasıl çalıştığını anlamak, belirli işlevselliği bulmak veya kod ilişkilerini keşfetmek için `#codebase` ile **Ask** ajanını kullanın.

```prompt-ask
Explain how authentication works in #codebase
```

```prompt-ask
Where is the database connection string configured? #codebase
```

```prompt-ask
How do I build this #codebase?
```

```prompt-ask
Which testing framework is used for #calculator.test.js?
```

## Kod oluşturma ve düzenleme

Çok dosyalı oluşturma için **Agent** ve hedefli, yerinde düzenlemeler için **inline chat** (`kb(inlinechat.start)`) kullanın.

```prompt
Add a login button and style it based on #styles.css
```

```prompt
Create a meal-planning web app using React and Node.js
```

```prompt
Refactor this code to use async/await
```

## Test ve kalite güvencesi

Test oluşturmak veya başarısız testleri düzeltmek için **Agent** kullanın.

```prompt
Add unit tests for the user service.
```

```prompt
Fix the failing tests #testFailure
```

## Hata ayıklama ve sorunları düzeltme

Dosyalar genelinde sorunları düzeltmek için **Agent** veya önce kök nedeni anlamak için **Ask** kullanın.

```prompt
Fix the issues in #problems
```

```prompt
Why is this function returning undefined?
```

## Kaynak kontrolüyle çalışma

Bekleyen değişikliklerinizle çalışmak ve sürüm dokümantasyonu oluşturmak için chat kullanın.

```prompt
Summarize the #changes
```

```prompt
Generate release notes based on the #changes
```

## Harici kaynaklarla çalışma

Web veya GitHub depolarından içeriğe referans vermek için `#fetch` ve `#githubRepo` kullanın.

```prompt
How do I use the 'useState' hook in react 18? #fetch https://18.react.dev/reference/react/useState#usage
```

```prompt
Build an API endpoint to fetch address info, use the template from #githubRepo contoso/api-templates
```

```prompt
What are the top #extensions for this workspace?
```

## Terminal ve komut satırı görevleri

Kabuk komutları ve terminal işlemleri konusunda yardım için [terminal inline chat](/docs/copilot/chat/inline-chat.md#use-terminal-inline-chat) kullanın.

```prompt
How do I install npm packages?
```

```prompt
List the top 5 largest files in the src directory
```

```prompt
undo the last git commit
```

## Jupyter notebook'larla çalışma

Jupyter notebook'ları oluşturmak, düzenlemek ve bunlarla çalışmak için **Agent** kullanın.

```prompt
/newNotebook use pandas and seaborn to read and visualize the titanic dataset. Show key information from the dataset.
```

```prompt
Create a notebook to read data from #housing.csv and plot the distribution of prices
```

```prompt
Make sure the data is cleaned before visualizing and processing it
```

```prompt
Show the correlation between different features in the dataset
```

## Çok turlu konuşma örnekleri

Chat aynı oturumda takip istemlerini destekler. Sonuçlar üzerinde yinelemek ve AI çıktısını iyileştirmek için çok turlu konuşmaları kullanın.

**İlk istem:**

```prompt
Create a REST API with Express.js that has endpoints for users and products
```

**Takip istemleri:**

```prompt
Add input validation and error handling to both endpoints
```

```prompt
Now add unit tests for the validation logic
```

Önceki yanıtlar üzerine inşa ederek AI önceki adımlardan bağlamı korur ve daha tutarlı kod üretir.

## Etkili istemler oluşturma ipuçları

* **Belirli olun**: Ne yapmak istediğiniz, kullanılacak teknolojiler ve beklenen çıktı biçimi hakkında detaylar ekleyin.
* **Bağlam ekleyin**: Dosyalara, sembollere veya `#codebase`, `#changes` veya `#problems` gibi bağlam değişkenlerine referans vermek için #-bahsetmeler kullanın.
* **Yineleyin**: Basit bir istemle başlayın ve yanıta göre iyileştirin. Sonuçları iyileştirmek için takip soruları sorun.
* **Karmaşık görevleri parçalayın**: Her şeyi bir seferde istemek yerine büyük görevleri daha küçük, yönetilebilir adımlara bölün.

[İstem oluşturma için en iyi uygulamalar](/docs/copilot/guides/prompt-engineering-guide.md) ve [istemlerinize bağlam ekleme](/docs/copilot/chat/copilot-chat-context.md) hakkında daha fazla bilgi edinin.

## İlgili kaynaklar

* [Chat genel bakış](/docs/copilot/chat/copilot-chat.md)
* [Sohbet isteminize bağlam ekleyin](/docs/copilot/chat/copilot-chat-context.md)
* [Inline chat](/docs/copilot/chat/inline-chat.md)
* GitHub dokümantasyonunda [Copilot Chat Cookbook](https://docs.github.com/en/copilot/example-prompts-for-github-copilot-chat)
