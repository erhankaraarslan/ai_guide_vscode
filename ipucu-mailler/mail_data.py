# -*- coding: utf-8 -*-
"""
40 günlük mail, temel seviyeden ileri seviyeye progresif sıra.
Her mail 3 ipucu içerir. Toplam 120 ipucu.
Sıra: 1-10 Başlangıç | 11-20 Temel | 21-30 Orta | 31-40 İleri

Kaynaklar: VS Code Copilot resmi dokümantasyonu, GitHub Blog, GitHub Docs.
"""

# Ortak görsel ve CTA için kısayollar
_IMG = "https://raw.githubusercontent.com/erhankaraarslan/ai_guide_vscode/main/tr/docs/copilot/images"
_BASE = "https://code.visualstudio.com"

# Ek kaynak referansları (isim, URL)
_GITHUB_BLOG_IDE = {"name": "GitHub Blog", "url": "https://github.blog/2024-03-25-how-to-use-github-copilot-in-your-ide-tips-tricks-and-best-practices/"}
_GITHUB_BLOG_INSTRUCTIONS = {"name": "GitHub Blog", "url": "https://github.blog/ai-and-ml/github-copilot/5-tips-for-writing-better-custom-instructions-for-copilot/"}
_GITHUB_BLOG_EXAMPLES = {"name": "GitHub Blog", "url": "https://github.blog/ai-and-ml/github-copilot/what-can-github-copilot-do-examples/"}
_GITHUB_BLOG_UNIT_TEST = {"name": "GitHub Blog", "url": "https://github.blog/ai-and-ml/github-copilot/how-to-generate-unit-tests-with-github-copilot-tips-and-examples/"}
_GITHUB_BLOG_TDD = {"name": "GitHub Blog", "url": "https://github.blog/ai-and-ml/github-copilot/github-for-beginners-test-driven-development-tdd-with-github-copilot/"}
_GITHUB_BLOG_CLI = {"name": "GitHub Blog", "url": "https://github.blog/ai-and-ml/github-copilot-cli-101-how-to-use-github-copilot-from-the-command-line/"}
_GITHUB_BLOG_ACCESSIBILITY = {"name": "GitHub Blog", "url": "https://github.blog/developer-skills/github/prompting-github-copilot-chat-to-become-your-personal-ai-assistant-for-accessibility/"}
_GITHUB_DOCS = {"name": "GitHub Docs", "url": "https://docs.github.com/en/copilot"}
_GITHUB_DOCS_BEST_PRACTICES = {"name": "GitHub Docs", "url": "https://docs.github.com/en/copilot/get-started/best-practices"}
_GITHUB_DOCS_PROMPT_ENG = {"name": "GitHub Docs", "url": "https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot"}
_GITHUB_DOCS_CHEAT_SHEET = {"name": "GitHub Docs", "url": "https://docs.github.com/en/copilot/using-github-copilot/github-copilot-chat-cheat-sheet"}
_GITHUB_DOCS_COOKBOOK = {"name": "GitHub Docs", "url": "https://docs.github.com/en/copilot/example-prompts-for-github-copilot-chat"}
_GITHUB_DOCS_RESPONSIBLE = {"name": "GitHub Docs", "url": "https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot"}
_GITHUB_DOCS_CLI = {"name": "GitHub Docs", "url": "https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli"}
_GITHUB_TRUST = {"name": "GitHub Trust Center", "url": "https://resources.github.com/copilot-trust-center/"}
_VS_CODE_CONTEXT_ENG = {"name": "VS Code Context Guide", "url": "https://code.visualstudio.com/docs/copilot/guides/context-engineering-guide"}
_VS_CODE_CHAT_CONTEXT = {"name": "VS Code Docs", "url": "https://code.visualstudio.com/docs/copilot/copilot-chat-context"}
_VS_CODE_QUICKSTART = {"name": "VS Code Quickstart", "url": "https://code.visualstudio.com/docs/getstarted/copilot-quickstart"}
_VS_CODE_BEST_PRACTICES = {"name": "VS Code Docs", "url": "https://code.visualstudio.com/docs/copilot/best-practices"}
_VS_CODE_TDD = {"name": "VS Code TDD Guide", "url": "https://code.visualstudio.com/docs/copilot/guides/test-driven-development-guide"}
_VS_CODE_TEST = {"name": "VS Code Docs", "url": "https://code.visualstudio.com/docs/copilot/guides/test-with-copilot"}
_GITHUB_ACCESSIBILITY = {"name": "GitHub Accessibility", "url": "https://accessibility.github.com/documentation/guide/copilot-instructions/"}

def _tip(title, content, how, example, source=None):
    t = {"title": title, "content": content, "how": how, "example": example}
    if source:
        t["source"] = source
    return t

MAILS = [
    # ========== 1-10 BAŞLANGIÇ ==========
    {
        "id": 1, "title": "Copilot'a ilk temas", "subtitle": "Başlangıç · Kurulum",
        "theme": "blue", "img": "setup/setup-copilot-status-bar.png",
        "cta": "Copilot kurulumu", "cta_url": "/docs/copilot/setup",
        "tips": [
            _tip(
                "Status bar'daki Copilot simgesini bulun",
                "VS Code penceresinin en altında (status bar) Copilot simgesi görünür. Üzerine gelince durumu ve hızlı erişim menüsünü görürsünüz. Copilot Free ile aylık limitli inline öneri ve sohbet; abonelikle sınırsız. İlk kurulumdaysa 'Copilot'u Ayarla' seçeneği çıkar.",
                ["Status bar (alt çubuk) sağ tarafında Copilot/Sparkle simgesine tıklayın", "Menüden 'Sign in' veya 'Copilot\'u Ayarla' seçin", "GitHub hesabınızla giriş yapın"],
                "İlk kez kullanıyorsanız: Simge → Sign in to GitHub",
                source=_VS_CODE_QUICKSTART,
            ),
            _tip(
                "Chat panelini açın",
                "Sol kenar çubuğunda mesaj balonu (Chat) simgesi veya Ctrl+Cmd+I (Mac) / Ctrl+Alt+I (Windows) ile Chat panelini açabilirsiniz. Inline suggestions, inline chat ve Chat view farklı etkileşim modları sunar; karmaşık görevler için Agent seçin. AI ile sohbet buradan yapılır.",
                ["Sol kenarda Activity Bar'da Chat (balon) simgesine tıklayın", "Veya Ctrl+Cmd+I (Mac) / Ctrl+Alt+I (Windows) kısayolunu kullanın", "Panel açıldığında giriş kutusu en altta olacak"],
                "Ctrl+Cmd+I ile Chat'i açın, ilk sohbetiniz hazır",
                source=_VS_CODE_QUICKSTART,
            ),
            _tip(
                "İlk sorunuzu yazın",
                "Chat giriş kutusuna (en altta) doğal dilde bir soru yazıp Enter'a basın. Örn: 'Bu dosya ne yapıyor?' veya 'Bu fonksiyona açıklama ekle'. Ask modunda aktif dosya otomatik bağlama eklenir; Agent ise ihtiyaca göre karar verir. AI yanıt verir.",
                ["Giriş kutusuna tıklayın", "Sorunuzu Türkçe veya İngilizce yazın", "Enter'a basın"],
                "«Bu projenin yapısı nedir?» — ilk deneme için uygun",
                source=_VS_CODE_CHAT_CONTEXT,
            ),
        ],
    },
    {
        "id": 2, "title": "Satır içi öneriler", "subtitle": "Başlangıç · Kod tamamlama",
        "theme": "sky", "img": "getting-started/html-completion.png",
        "cta": "Satır içi öneriler", "cta_url": "/docs/copilot/ai-powered-suggestions",
        "tips": [
            _tip(
                "Hayalet metin (ghost text) nedir?",
                "Yazarken AI, gri/şeffaf metin olarak bir sonraki satırı veya ifadeyi önerir. Bu 'hayalet metin' gerçek kod değildir; Tab ile kabul ederseniz koda dönüşür. Inline suggestions boilerplate kod, tekrarlayan desenler ve değişken adları için otomatik çalışır.",
                ["Kod yazmaya başlayın — birkaç karakter sonra gri öneri görünür", "Öneriyi kabul etmek için Tab tuşuna basın", "Reddetmek için öneriyi yok sayıp yazmaya devam edin"],
                "function yazdıktan sonra AI parantez ve süslü parantez önerebilir",
                source=_VS_CODE_QUICKSTART,
            ),
            _tip(
                "Birden fazla öneri varsa",
                "Bazen birkaç alternatif öneri olur. Alt+] / Alt+[ (Mac: Option+]) ile öneriler arasında geçiş yapın; beğendiğinizi Tab ile kabul edin. Thumbs up/down ile geri bildirim vererek gelecek önerileri iyileştirebilirsiniz.",
                ["Öneri göründüğünde hayalet metnin üzerine gelin", "Alternatif öneriler için sağ/sol ok veya kısayol kullanın", "Beğendiğinizi Tab ile kabul edin"],
                "Alt+] sonraki öneri, Alt+[ önceki öneri",
                source=_GITHUB_DOCS_BEST_PRACTICES,
            ),
            _tip(
                "Ne zaman kullanılır?",
                "Şablon kod, HTML yapısı, tekrarlayan desenler, değişken adları, regex, unit test, dokümantasyon için çok faydalı. Uzun mantık veya karmaşık mimari için Chat kullanın. Copilot bu tür tekrarlayan işlerde parlar.",
                ["Boilerplate ve tekrar için satır içi önerilere güvenin", "Karmaşık mantık için Chat'e geçin", "Yazarken akışınızı bozmamak için Tab kabul edin"],
                "for döngüsü, try-catch, HTML form, regex — satır içi öneri ideal",
                source=_GITHUB_BLOG_IDE,
            ),
        ],
    },
    {
        "id": 3, "title": "Ask vs Agent modu", "subtitle": "Başlangıç · Chat modları",
        "theme": "indigo", "img": "getting-started/agent-mode-selection.png",
        "cta": "Ajan modları", "cta_url": "/docs/copilot/agents/overview",
        "tips": [
            _tip(
                "Ask (Chat) modu",
                "Sorular sorar, açıklama ister, fikir alırsınız. Kod değişikliği yapmaz; sadece yanıt verir. Beyin fırtınası, kod açıklama, doğal dil soruları, belirli persona (örn. Senior C++ Developer kod incelemesi) için ideal. Slash komutları ve skills ile hızlanır.",
                ["Chat girişinin üstündeki mod seçicisini tıklayın", "'Ask' veya 'Chat' seçin", "Soru sorun — AI yanıt verir, dosya değiştirmez"],
                "«Bu algoritmanın zaman karmaşıklığı nedir?» → Ask modu",
                source=_GITHUB_DOCS_BEST_PRACTICES,
            ),
            _tip(
                "Agent modu",
                "Birden fazla dosyada değişiklik yapar, terminal çalıştırır, araç kullanır. Büyük kod blokları üretir, sonra iterasyonla ihtiyaca göre düzenler. Özellik uygulama, refaktör, hata düzeltme için. Tam yetkili AI; değişiklikleri siz inceleyip onaylarsınız.",
                ["Mod seçiciden 'Agent' seçin", "Görevinizi net yazın (örn. 'Login formu ekle')", "AI dosyaları düzenler, siz değişiklikleri inceleyip onaylarsınız"],
                "«Bu API endpoint'ini ekle» → Agent modu",
                source=_GITHUB_DOCS_BEST_PRACTICES,
            ),
            _tip(
                "Ne zaman hangisi?",
                "Sadece bilgi mi istiyorsunuz? → Ask. Kod değişikliği mi? → Agent. Kararsız kalmayın; yanlış mod verimsiz sonuç verir. Doğru aracı seçmek hız, maliyet ve kaliteyi doğrudan etkiler.",
                ["Bilgi/soru → Ask", "Kod yazma/değiştirme → Agent", "Plan yapma → Plan ajanı (sonraki mailler)"],
                "Açıklama: Ask. Uygulama: Agent.",
                source=_VS_CODE_BEST_PRACTICES,
            ),
        ],
    },
    {
        "id": 4, "title": "# ile bağlam ekleme", "subtitle": "Başlangıç · Bağlam",
        "theme": "teal", "img": "prompt-engineering-guide/copilot-chat-view-attach-context.png",
        "cta": "Bağlam ekleme", "cta_url": "/docs/copilot/chat/copilot-chat-context",
        "tips": [
            _tip(
                "#'nin işlevi",
                "İsteminizin sonuna # yazdığınızda VS Code size dosya, klasör veya #codebase gibi bağlam seçenekleri sunar. #-mentions ile dosya, klasör, sembol, araç ve terminal çıktısı ekleyebilirsiniz. AI yanıt verirken bu bağlamı kullanır.",
                ["Chat giriş kutusuna sorunuzu yazın", "Sorunun sonuna boşluk + # yazın", "Açılan listeden dosya, klasör veya #codebase seçin"],
                "«Bu fonksiyon ne yapıyor?» yazdıktan sonra # yazın",
                source=_VS_CODE_CHAT_CONTEXT,
            ),
            _tip(
                "Belirli dosya ekleme",
                "Hangi dosyayla ilgili sorduğunuzu biliyorsanız # yazıp dosya adını seçin. AI sadece o dosyaya bakar; daha odaklı yanıt alırsınız. Ayrıca ilgili dosyaları editörde açık tutun — Copilot açık dosyalardan bağlam çıkarır.",
                ["# yazın", "Dosya adı yazarak filtreleyin (örn. auth)", "İlgili dosyaları editörde açık tutun", "Listeden ilgili dosyayı seçin"],
                "#src/utils/auth.ts — sadece bu dosya bağlama eklenir",
                source=_GITHUB_BLOG_IDE,
            ),
            _tip(
                "#codebase nedir?",
                "Hangi dosyaların ilgili olduğunu bilmiyorsanız #codebase seçin. VS Code projede semantik arama yapıp ilgili dosyaları bulur. Basic, local veya remote indeks kullanılır; büyük depolarda remote indeks daha hızlıdır.",
                ["Sorunuzun sonuna # yazın", "Listeden #codebase seçin", "AI projede arama yapıp ilgili kodları getirir"],
                "«Kimlik doğrulama nasıl çalışıyor? #codebase»",
                source=_VS_CODE_CHAT_CONTEXT,
            ),
        ],
    },
    {
        "id": 5, "title": "Inline Chat", "subtitle": "Başlangıç · Yerinde düzenleme",
        "theme": "sky", "img": "getting-started/inline-chat-start.png",
        "cta": "Inline Chat", "cta_url": "/docs/copilot/chat/inline-chat",
        "tips": [
            _tip(
                "Inline Chat nasıl açılır?",
                "Editörde kodu seçin, Cmd+I (Mac) veya Ctrl+I (Windows) basın. Chat paneline geçmeden, tam o kod üzerinde AI ile konuşursunuz. Inline comments ile doğal dilde kod üretebilirsiniz. Sadece seçili blok değişir.",
                ["Editörde düzenlemek istediğiniz kodu seçin", "Cmd+I veya Ctrl+I tuşlarına basın", "Açılan kutuya isteğinizi yazın"],
                "Bir fonksiyonu seçip Cmd+I → «try-catch ekle»",
                source=_GITHUB_DOCS_BEST_PRACTICES,
            ),
            _tip(
                "Ne zaman kullanılır?",
                "Tek fonksiyon düzeltmesi, açıklama ekleme, null kontrolü, küçük refaktör için idealdir. İş akışınızı bozmadan hızlı, odaklı düzenlemeler. Birden fazla dosya değişecekse Agent kullanın.",
                ["Tek dosyada küçük değişiklik → Inline Chat", "Çok dosyalı değişiklik → Agent", "Hızlı düzeltme, typo, yorum → Inline Chat"],
                "«Bu değişkene JSDoc ekle» — Inline Chat ideal",
                source=_VS_CODE_QUICKSTART,
            ),
            _tip(
                "Diff inceleme",
                "AI öneriyi yeşil (eklenen) ve kırmızı (silinen) satırlarla gösterir. Kabul (✓) veya reddet (✗) düğmesiyle karar verin. Kabul etmeden önce mutlaka okuyun; fonksiyonellik, güvenlik ve okunabilirliği kontrol edin.",
                ["AI yanıt verince diff editörde görünür", "✓ ile kabul, ✗ ile reddedin", "Yanlışsa reddedip «Sadece X'i değiştir» diye netleştirin"],
                "Öneri yanlışsa reddedin, yeni talimat yazın",
                source=_GITHUB_DOCS_BEST_PRACTICES,
            ),
        ],
    },
    {
        "id": 6, "title": "İlk soruyu doğru sorma", "subtitle": "Başlangıç · Prompt",
        "theme": "lime", "img": "prompt-engineering-guide/fibonacci-first.png",
        "cta": "Prompt mühendisliği", "cta_url": "/docs/copilot/guides/prompt-engineering-guide",
        "tips": [
            _tip(
                "Belirsiz istemler işe yaramaz",
                "'Bunu iyileştir' veya 'düzelt' AI'a yeterli bilgi vermez. Ne tür iyileştirme? 'Bunu', 'şu' belirsiz — spesifik referans verin: 'createUser fonksiyonu', 'son yanıttaki kod'. Somut hedef ve ölçülebilir kriter yazın.",
                ["İsteminizde ne istediğinizi net belirtin", "'İyileştir', 'düzelt' yerine 'O(n) yap', 'null kontrolü ekle' gibi somut ifade kullanın", "Mümkünse kısıtlama ekleyin (dil, kütüphane)"],
                "Bunun yerine: «Bu fonksiyona null kontrolü ekle, boş string için [] dönsün»",
                source=_GITHUB_DOCS_PROMPT_ENG,
            ),
            _tip(
                "Örnek giriş/çıkış verin",
                "AI'ın ne beklediğinizi anlaması için örnek verin. Örn: validateEmail('a@b.com') → true, validateEmail('x') → false. Özellikle veri işleme veya string manipülasyonunda örnekler büyük fark yaratır. Unit testler de bir tür örnek kodu sağlar.",
                ["İlk cümlede ne yapılacağını yazın", "Örnek giriş/çıkış ekleyin", "Kısıtlama: 'regex kullanma', 'TypeScript' vb."],
                "«Email doğrula: user@x.com→true, invalid→false. Regex kullanma.»",
                source=_GITHUB_BLOG_IDE,
            ),
            _tip(
                "Takip mesajıyla düzeltin",
                "İlk yanıt tam istediğiniz gibi değilse tüm istemi yeniden yazmayın. '2. maddeyi genişlet' veya 'Sadece X'i değiştir' gibi takip mesajı gönderin. Deneyin, yineleyin — farklı formülasyon denemek genelde sonucu iyileştirir.",
                ["İlk yanıttan memnun değilseniz giriş kutusuna takip yazın", "Spesifik düzeltme isteyin", "Yeni sohbet açmaya gerek yok"],
                "«Sadece hata mesajını Türkçe yap»",
                source=_GITHUB_DOCS_PROMPT_ENG,
            ),
        ],
    },
    {
        "id": 7, "title": "#codebase ile otomatik arama", "subtitle": "Temel · Bağlam",
        "theme": "teal", "img": "workspace-context/workspace-index-status.png",
        "cta": "Bağlam yönetimi", "cta_url": "/docs/copilot/chat/copilot-chat-context",
        "tips": [
            _tip(
                "Ne zaman #codebase?",
                "Hangi dosyaların sorunuzla ilgili olduğunu bilmiyorsanız #codebase kullanın. VS Code projede semantik arama yapıp ilgili kodları otomatik bulur. Agent modunda AI gerektiğinde otomatik codebase araması yapar; netleştirmek için #codebase ekleyebilirsiniz.",
                ["Chat'te sorunuzu yazın, sonuna # yazın", "#codebase seçin", "AI projede arama yapar, ilgili dosyaları bağlama ekler"],
                "«OAuth bu projede nasıl kullanılıyor? #codebase»",
                source=_VS_CODE_CHAT_CONTEXT,
            ),
            _tip(
                "#fetch ve #githubRepo",
                "#fetch bir URL'den web sayfası içeriği çeker (API docs, migration guide). #githubRepo bir GitHub depoda kod arar. Güncel dokümantasyona ihtiyaç varsa kullanın. VS Code harici URL için onay ister; güvenlik için.",
                ["Sorunuzun sonuna #fetch https://... veya #githubRepo owner/repo yazın", "Harici URL için VS Code onay isteyebilir", "AI bu içeriği bağlam olarak kullanır"],
                "«React 19 migration? #fetch https://react.dev/blog»",
                source=_VS_CODE_CHAT_CONTEXT,
            ),
            _tip(
                "Dosya, klasör, sembol",
                "# ile dosya, klasör veya kod sembolü (fonksiyon, sınıf) seçebilirsiniz. Sembol için ilgili dosyayı editörde açık tutun. Explorer'dan sürükleyip Chat'e bırakarak da bağlam ekleyebilirsiniz.",
                ["# yazıp dosya/klasör adıyla filtreleyin", "Sembol için dosyayı açın, sonra # ile sembolü seçin", "Spesifik bağlam = daha iyi yanıt"],
                "#AuthService veya #src/api/",
                source=_VS_CODE_CHAT_CONTEXT,
            ),
        ],
    },
    {
        "id": 8, "title": "Farklı işler için ayrı sohbet", "subtitle": "Temel · Context isolation",
        "theme": "indigo", "img": "agents-overview/chat-view-compact2.png",
        "cta": "Bağlam mühendisliği", "cta_url": "/docs/copilot/guides/context-engineering-guide",
        "tips": [
            _tip(
                "Neden ayrı sohbet?",
                "AI sohbet geçmişindeki her şeyi kullanır. Planlama, kodlama ve hata ayıklamayı aynı sohbette yaparsanız bağlam karışır; hem kalite düşer hem maliyet artar. Artık ilgili olmayan soruları silerek de sohbeti temiz tutabilirsiniz.",
                ["Her iş türü için yeni sohbet açın", "Artık ilgili olmayan mesajları silin (bağlamı sadeleştirir)", "Chat panelinde + veya 'New Chat' butonuna tıklayın", "Örn: Plan bittikten sonra yeni sohbet açıp 'Bu plana göre uygula' yazın"],
                "Planlama sohbeti bitti → New Chat → «Plandaki 1. adımı uygula»",
                source=_GITHUB_BLOG_IDE,
            ),
            _tip(
                "Bağlam penceresi nedir?",
                "AI'ın okuyabildiği bilgi miktarı sınırlıdır (bağlam penceresi). Her eklediğiniz dosya ve mesaj bu alanı doldurur. Chat giriş kutusundaki göstergede token kullanımını takip edin; dolunca otomatik sıkıştırma olur. Gereksiz bilgi eklemeyin; önce az başlayın.",
                ["İlk mesajda sadece soru + 1–2 dosya referansı verin", "AI yeterli bulamazsa sonraki mesajda ekleyin", "Tüm projeyi değil ilgili klasörü (# ile) verin"],
                "Önce «#src/auth/ bu klasör ne yapıyor?» — yetmezse ekleyin",
                source=_VS_CODE_CHAT_CONTEXT,
            ),
            _tip(
                "Konu değişince",
                "Farklı proje veya konuya geçtiğinizde mutlaka yeni sohbet açın. İlgisiz sorular aynı sohbette hem AI'ı karıştırır hem token israfına yol açar. /new veya + ile yeni konuşma; geçmişi temiz tutun.",
                ["Konu değişti mi? → New Chat", "Farklı dosya grubu mu? → New Chat", "Uzun sohbet 10+ mesaj oldu mu? → /compact veya New Chat"],
                "Login bitti, şimdi veritabanı → yeni sohbet",
                source=_GITHUB_DOCS_CHEAT_SHEET,
            ),
        ],
    },
    {
        "id": 9, "title": "Bağlam anti-patterns", "subtitle": "Temel · Kaçınılması gerekenler",
        "theme": "red", "img": "core-concepts/context-assembly.png",
        "cta": "Bağlam mühendisliği", "cta_url": "/docs/copilot/guides/context-engineering-guide",
        "tips": [
            _tip(
                "Bağlam dökümü yapmayın",
                "İlgisiz veya çok fazla dosya eklemek AI'ı karıştırır. Önemli bilgi kaybolur, maliyet artar. Context dumping anti-pattern'den kaçının: odaklanmamış, karar vermeye yardımcı olmayan bilgi yığını eklemeyin.",
                ["İlk mesajda 1–2 dosya veya #codebase yeterli olabilir", "Tüm src/ yerine #src/auth/ gibi odaklı referans verin", "AI 'daha fazla lazım' derse ekleyin"],
                "Tüm projeyi değil: #src/auth/ veya #config.ts",
                source=_VS_CODE_CONTEXT_ENG,
            ),
            _tip(
                "Küçük başlayın",
                "Talimat dosyalarında önce en kritik 5–10 kuralı yazın. Üst düzey mimariye odaklanın. AI sürekli aynı hatayı yapıyorsa o zaman yeni kural ekleyin. Bağlam mühendisliğinde 'start small and iterate' prensibi — context overload'dan kaçının.",
                ["copilot-instructions.md'de 1–2 sayfa yeterli", "Genel bilgileri (AI'ın bildiği) yazmayın", "Zamanla ihtiyaca göre ekleyin"],
                "«API prefix /api/v1. Hata formatı { code, message }»",
                source=_VS_CODE_CONTEXT_ENG,
            ),
            _tip(
                "Belirsiz istemlerden kaçının",
                "'İyileştir', 'düzelt', 'better' yeterli değil. Ne tür iyileştirme? Ölçülebilir kriter veya örnek giriş/çıkış ekleyin. Belirsiz kütüphane referansları da sorun — spesifik import veya kütüphane adı yazın.",
                ["Hedefi net yazın", "Ölçülebilir kriter: hız, format, kısıtlama", "Örnek: 'O(n) yap' veya 'Null için [] dönsün'"],
                "«Bu fonksiyonu O(n) yap» — somut hedef",
                source=_GITHUB_DOCS_PROMPT_ENG,
            ),
        ],
    },
    {
        "id": 10, "title": "/init ile proje kurulumu", "subtitle": "Temel · Proje setup",
        "theme": "blue", "img": "getting-started/agent-mode-selection.png",
        "cta": "Başlarken", "cta_url": "/docs/copilot/getting-started",
        "tips": [
            _tip(
                "/init ne yapar?",
                "Chat'e /init yazınca VS Code projenizi analiz edip .github/copilot-instructions.md ve temel kuralları oluşturur. Mevcut kod tabanı varsa AI PRODUCT.md, ARCHITECTURE.md, CONTRIBUTING.md gibi dökümanlar da üretebilir. Yeni proje veya henüz yapılandırmadıysanız kullanın.",
                ["VS Code'da projeyi açın", "Chat panelini açın", "Giriş kutusuna /init yazıp Enter'a basın"],
                "Yeni klonladığınız depoda Chat'e «/init» yazın",
                source=_VS_CODE_CONTEXT_ENG,
            ),
            _tip(
                "Oluşan talimatları düzenleyin",
                "/init genel kurallar üretir. Ekibinizin kod stili, mimari, kısıtlamaları ekleyin. Oluşan dökümanları gözden geçirip güncelleyin. Dosyayı kısa tutun; her sohbette yüklenir.",
                ["Explorer'da .github/copilot-instructions.md açın", "AI'ın eklediklerini okuyun", "Projeye özel kurallar ekleyin, gereksizleri silin"],
                "«API route'lar /api/v1», «Hata mesajları Türkçe»",
                source=_VS_CODE_BEST_PRACTICES,
            ),
            _tip(
                "Özelleştirme komutları",
                "/instructions (talimatlar), /prompts (prompt dosyaları), /agents (ajanlar), /skills (yetenekler) ile yönetim. /fix aktif dosyadaki hataları düzeltir, /tests test yazar. Slash komutları iş akışını hızlandırır.",
                ["/instructions → talimat dosyaları", "/prompts → kayıtlı istemler", "/agents, /skills → ajan ve yetenek yönetimi"],
                "/prompts → 'code-review' oluştur → /code-review ile çağır",
                source=_GITHUB_DOCS_CHEAT_SHEET,
            ),
        ],
    },
    # ========== 11-20 TEMEL ==========
    {
        "id": 11, "title": "Token ve maliyet farkındalığı", "subtitle": "Temel · Token",
        "theme": "amber", "img": "agents-overview/chat-view-compact2.png",
        "cta": "Bağlam sıkıştırma", "cta_url": "/docs/copilot/chat/copilot-chat-context#context-compaction",
        "tips": [
            _tip("Token nedir?", "AI metni 'token' adlı birimlerle işler. Her kelime, noktalama birkaç token. Bağlam penceresi token sayısıyla sınırlı; her mesaj ve eklenen dosya token tüketir. Model seçimine göre (örn. 15K/128K) toplam bağlam değişir.", ["Uzun sohbet = çok token = daha yüksek maliyet", "Gereksiz bilgi eklemeyin", "Konu değişince yeni sohbet açın"], "10+ mesajlık sohbet → /compact veya New Chat", source=_VS_CODE_CHAT_CONTEXT),
            _tip("/compact kullanımı", "Uzun sohbetlerde geçmiş her mesajda tekrar işlenir. /compact yazınca VS Code konuşmayı özetler; yer açar, maliyet düşer. İsteğe bağlı: '/compact odaklan: veritabanı şeması kararları' ile özeti yönlendirebilirsiniz.", ["Chat giriş kutusuna /compact yazın", "Enter'a basın", "Konuşma özetlenir, devam edebilirsiniz"], "Sohbet 10+ mesaj olduğunda «/compact»", source=_VS_CODE_CHAT_CONTEXT),
            _tip("Talimat dosyalarını kısa tutun", "copilot-instructions.md her sohbette yüklenir. Uzunsa gereksiz token harcanır. Karar vermeye yardımcı olan bilgiye odaklanın — AI'ın koddan çıkaramayacağı mimari, sözleşmeler, proje kuralları.", [".github/copilot-instructions.md'de kısa maddeler", "Mimari, sözleşmeler, projeye özel kurallar", "Genel bilgileri yazmayın"], "Mimari kararlar, API prefix, hata formatı", source=_VS_CODE_CONTEXT_ENG),
        ],
    },
    {
        "id": 12, "title": "Belirli ve net istemler", "subtitle": "Temel · Prompt",
        "theme": "lime", "img": "prompt-engineering-guide/fibonacci-first.png",
        "cta": "Prompt mühendisliği", "cta_url": "/docs/copilot/guides/prompt-engineering-guide",
        "tips": [
            _tip("'Make better' yeterli değil", "Ne tür iyileştirme? Performans mı, okunabilirlik mi, hata kontrolü mü? Önce genel hedef verin, sonra spesifik kriterler ekleyin. Somut hedef yazın.", ["Hedefi net belirtin: 'O(n) yap', 'null kontrolü ekle'", "Ölçülebilir kriter verin", "Kısıtlama: dil, kütüphane, format"], "«Zaman karmaşıklığını azalt» veya «Null için boş dizi dön»", source=_GITHUB_DOCS_PROMPT_ENG),
            _tip("Giriş + çıkış + kısıtlama", "Örnek giriş/çıkış AI'ın ne beklediğinizi anlamasını sağlar. Unit testler de örnek olarak kullanılabilir — önce test yazdırıp sonra fonksiyonu o testlere göre yazdırabilirsiniz. Hangi dili, framework'ü kullanacağını belirtin.", ["Ne yapılacağını yazın", "Örnek: validateEmail('a@b.com')→true", "Kısıtlama: 'regex kullanma', 'TypeScript'"], "«Email doğrula: a@b.com→true, x→false. Regex kullanma.»", source=_GITHUB_DOCS_PROMPT_ENG),
            _tip("Beklenen çıktı ekleyin", "Test senaryosu veya kabul kriteri verirseniz AI ürettiğini doğrulayabilir. Cookbook'da debug, rate limit, JSON validation gibi 30+ örnek var. En yüksek kaldıraçlı adımlardan biri.", ["İstemin sonuna 'X yapmalı, Y yapmamalı' ekleyin", "'Testleri çalıştır' deyin", "Sayısal kriter: '10 req/sn, 11. reddedilmeli'"], "«Rate limiter: 10 req/sn. Test yaz ve çalıştır.»", source=_GITHUB_DOCS_COOKBOOK),
        ],
    },
    {
        "id": 13, "title": "Görev için doğru mod", "subtitle": "Temel · Araç seçimi",
        "theme": "fuchsia", "img": "chat-tools/agent-mode-select-tools.png",
        "cta": "En iyi uygulamalar", "cta_url": "/docs/copilot/best-practices",
        "tips": [
            _tip("Inline Chat vs Agent vs Plan", "Inline: Tek dosyada küçük düzenleme, test üretimi, tekrarlayan kod. Agent: Çok dosyalı değişiklik, büyük kod blokları, iterasyon. Plan: Mimari, adım listesi. Basit düzeltme için Agent gereksiz maliyet.", ["1 fonksiyon/küçük blok? → Inline (Cmd/Ctrl+I)", "Birden fazla dosya? → Agent", "Önce strateji? → Plan"], "Değişken adı: Inline. Yeni API+frontend: Agent.", source=_GITHUB_DOCS_BEST_PRACTICES),
            _tip("Ask ne zaman?", "Sadece soru, açıklama, fikir istiyorsanız Ask yeterli. @workspace ile projeye özel soru sorabilirsiniz. Kod değiştirmeyecekseniz Agent açmayın — token tasarrufu.", ["Bilgi/soru → Ask", "Kod değişikliği → Agent", "Planlama → Plan ajanı"], "«Bu kod ne yapıyor?» → Ask", source=_GITHUB_DOCS_CHEAT_SHEET),
            _tip("Yanlış araç = israf", "Basit düzenleme için Agent açmak token ve zaman israfı. Proje optimizasyonu için /init kullanın; doğru araç seçimi hız ve kaliteyi artırır.", ["Önce görevin kapsamını düşünün", "Tek dosya, küçük? Inline", "Çok dosya, büyük? Agent"], "JSDoc ekleme: Inline. Yeni özellik: Agent.", source=_VS_CODE_BEST_PRACTICES),
        ],
    },
    {
        "id": 14, "title": "Plan ajanı ile ilk plan", "subtitle": "Temel · Planning",
        "theme": "blue", "img": "chat-planning/plan-agent-sample.png",
        "cta": "Plan ajanı", "cta_url": "/docs/copilot/agents/planning",
        "tips": [
            _tip("Plan ajanı ne yapar?", "Büyük görevi adım adım uygulama planına çevirir. Kod yazmadan önce strateji oluşturur; plan-template.md ile tutarlı format. Belirsiz noktaları size sorar. GitHub issue referansı ile bağlam ekleyebilirsiniz.", ["Mod seçiciden 'Plan' seçin", "Görevinizi yazın (örn. 'Kullanıcı kayıt akışı')", "AI sorular sorar, siz cevaplayın, plan oluşur"], "«Sepet özelliği: ürün ekleme, miktar, silme, toplam»", source=_VS_CODE_CONTEXT_ENG),
            _tip("Planı inceleyip onaylayın", "Plan oluşunca baştan sona okuyun. Eksik/yanlış varsa düzeltme isteyin. Doğru görünüyorsa 'Start Implementation' ile Agent'a geçin.", ["Planı okuyun", "Eksikse «2. adımda migration detayı ekle» deyin", "Memnunsanız handoff düğmesine basın"], "Plan 5 adım gösteriyorsa Agent'a geçince bu 5 adım bağlamda olur"),
            _tip("Büyük özelliği parçalayın", "Tek mesajda 'tüm özelliği yap' demek yerine adım adım isteyin. Karmaşık görevleri küçük, yönetilebilir parçalara bölün. Her adımı onaylayıp sonrakine geçin.", ["1) «Önce veritabanı şemasını tasarla»", "Onayla", "2) «API endpoint'lerini yaz»", "Onayla", "3) «Frontend ekle»"], "Şema → onayla → API → onayla → Frontend", source=_GITHUB_DOCS_PROMPT_ENG),
        ],
    },
    {
        "id": 15, "title": "Handoff ile Agent'a geçiş", "subtitle": "Temel · İş akışı",
        "theme": "cyan", "img": "agents-overview/hand-off-agent-session.png",
        "cta": "Handoff", "cta_url": "/docs/copilot/customization/custom-agents#handoffs",
        "tips": [
            _tip("Handoff nedir?", "Plan ajanı planı bitirince 'Start Implementation' düğmesi çıkar. Tıklayınca uygulama ajana geçersiniz; plan ve istem otomatik aktarılır. Handoff'lar ajanlar arasında yönlendirilmiş geçiş sağlar — planlama, uygulama, inceleme zinciri.", ["Plan ajanında plan oluşturun", "Yanıttaki 'Start Implementation' düğmesini görün", "Tıklayın — Agent açılır, plan bağlamda gelir"], "Plan bitti → Start Implementation → Agent plana göre kod yazar", source=_VS_CODE_CONTEXT_ENG),
            _tip("Her adımı onaylayın", "Handoff önce planı/uygulamayı kontrol etmenizi sağlar. Yanlışsa düzeltme isteyin, doğruysa devam edin. AI tam otomatik değil; siz yönlendirirsiniz. Feedback loop ile yanlış anlamaları erkenden düzeltin.", ["Yanıtı okuyun", "Eksik/yanlış varsa mesajla düzeltin", "Memnunsanız handoff'a basın"], "Plan eksikse «2. adımda DB migration detayı ekle»", source=_VS_CODE_CONTEXT_ENG),
            _tip("Plan → Uygulama → İnceleme", "Bu zincir: Plan ajanı plan yapar, handoff ile Agent uygular, yine handoff ile inceleme ajana geçebilirsiniz. TDD ajanı için test-first, implement, refactor fazları da ayrı ajanlara bölünebilir. Adım adım kontrol.", ["Plan → Start Implementation", "Agent bitince → Review/Inceleme (tanımlıysa)", "Her adımda siz onaylarsınız"], "Planlama → Uygulama → İnceleme sırası", source=_VS_CODE_TDD),
        ],
    },
    {
        "id": 16, "title": "copilot-instructions.md", "subtitle": "Temel · Proje talimatları",
        "theme": "orange", "img": "customization/configure-chat-instructions.png",
        "cta": "Özel talimatlar", "cta_url": "/docs/copilot/customization/custom-instructions",
        "tips": [
            _tip("Proje kökünde .github/copilot-instructions.md", "Bu dosya her sohbette AI'a otomatik gönderilir. Kod stili, mimari, hata işleme kuralları burada. PRODUCT.md, ARCHITECTURE.md, CONTRIBUTING.md'e Markdown link ile referans verin. Önerilenler: proje özeti, tech stack, proje yapısı. AI her yanıtta bunlara uyar.", [".github/ oluşturun", "copilot-instructions.md ekleyin", "PRODUCT.md, ARCHITECTURE.md referansları", "Proje özeti ve tech stack ekleyin", "Markdown ile kurallar yazın"], "## Kod: 2 boşluk indent. ## Hata: try-catch, kullanıcıya anlaşılır mesaj.", source=_VS_CODE_CONTEXT_ENG),
            _tip("applyTo ile kapsamlayın", "Her şeyi tek dosyaya koymayın. Dil veya klasör özelinde .instructions.md kullanıp applyTo ile hedefleyin. Proje geneli, modül, özellik seviyesinde hiyerarşi kurun. Sadece .instructions.md'de geçerli; Skill'lerde applyTo yoktur.", ["Farklı .instructions.md dosyaları oluşturun", "applyTo: '**/*.ts' veya 'src/api/**'", "/instructions ile yönetin"], "applyTo: '**/*.ts' — sadece TypeScript için (.instructions.md üstünde)", source=_VS_CODE_CONTEXT_ENG),
            _tip("Kısa ve odaklı", "Her kural 1–2 cümle. AI'ın koddan çıkaramayacağı bilgi: mimari kararlar, özel sözleşmeler, proje kuralları. Dış referanslar: ilgili API, standart dokümantasyonuna link verin. Tutarlı pattern ve naming kullanın.", ["Uzun paragraflardan kaçının", "Genel bilgileri (AI bildiği) yazmayın", "Kritik 5–10 kurala odaklanın"], "«API /api/v1. Hata RFC 7807.»", source=_VS_CODE_CONTEXT_ENG),
        ],
    },
    {
        "id": 17, "title": "Prompt dosyaları", "subtitle": "Temel · Tekrarlayan görevler",
        "theme": "cyan", "img": "customization/prompt-file-recommendations.png",
        "cta": "Prompt dosyaları", "cta_url": "/docs/copilot/customization/prompt-files",
        "tips": [
            _tip(".github/prompts/*.prompt.md", "Sık yaptığınız görevler için .prompt.md oluşturun. /komut-adı ile çağırırsınız; önceden tanımlı istem, ajan ve model yüklenir. Kod incelemesi, güvenlik taraması, refaktör için ayrı prompt dosyaları.", [".github/prompts/ oluşturun", "code-review.prompt.md gibi dosya", "İçine prompt: ve agent: tanımlayın"], "/code-review yazınca inceleme ajana geçer", source=_VS_CODE_CONTEXT_ENG),
            _tip("/code-review örneği", "Kod incelemesi için: agent: inceleme ajanı, prompt: standart sorular. Cookbook'daki güvenlik, performans, okunabilirlik sorularını özelleştirin. /code-review yazınca hepsi hazır gelir.", ["code-review.prompt.md oluşturun", "prompt: «Güvenlik, performans, okunabilirlik incele»", "agent: inceleme ajanı adı"], "prompt: «Bu değişiklikleri incele: güvenlik, performans»", source=_GITHUB_DOCS_COOKBOOK),
            _tip("/prompts ile yönetin", "Chat'te /prompts yazarak mevcut prompt dosyalarını listeleyebilir, yenisini ekleyebilirsiniz. /rename ile sohbeti adlandırın, /delete ile silin. Slash komutları iş akışını hızlandırır.", ["Chat'e /prompts yazın", "Mevcut prompt'ları görün", "Configure Prompts ile ekleyin/düzenleyin"], "/prompts → code-review, security-check ekleyin", source=_GITHUB_DOCS_CHEAT_SHEET),
        ],
    },
    {
        "id": 18, "title": "Model seçimi", "subtitle": "Temel · Model",
        "theme": "purple", "img": "language-models/model-dropdown-change-model.png",
        "cta": "Dil modelleri", "cta_url": "/docs/copilot/customization/language-models",
        "tips": [
            _tip("Görev karmaşıklığına model eşleştirin", "Planlama, hata ayıklama, mimari için 'akıl yürütme' ağırlıklı büyük modeller. Basit tamamlama için hızlı küçük modeller yeterli. Auto model seçimi gerektiğinde otomatik geçiş yapar.", ["Chat'te model adına tıklayın", "Listeden görevinize uygun modeli seçin", "Karmaşık iş → büyük model"], "Planlama: Claude Sonnet. Basit düzeltme: daha küçük model.", source=_VS_CODE_BEST_PRACTICES),
            _tip("Uygulama için küçük model", "Açık talimatlarla kod yazdırırken küçük modeller hem hızlı hem ucuz olabilir. Context engineering'de implement agent için model: küçük model önerilir. Deneyerek karar verin.", [".agent.md'de model: ['Model Adı']", "Veya Chat'te elle seçin", "Aynı istemle farklı modeller deneyin"], "model: ['Claude Haiku'] — uygulama ajanı için", source=_VS_CODE_CONTEXT_ENG),
            _tip("Prompt/ajanda model sabitleyin", "Belirli görevler için .prompt.md veya .agent.md içinde model tanımlayın. Her seferinde seçmek zorunda kalmazsınız.", ["Dosya üstünde model: ['Tercih edilen']", "O görev için her zaman bu model kullanılır", "Tutarlı sonuç alırsınız"], "code-review.prompt.md: model: ['Claude Sonnet']"),
        ],
    },
    {
        "id": 19, "title": "Test-driven prompts", "subtitle": "Temel · Doğrulama",
        "theme": "green", "img": "test-driven-development-guide/tdd-implementation-diagram.png",
        "cta": "En iyi uygulamalar", "cta_url": "/docs/copilot/best-practices",
        "tips": [
            _tip("Unit test + uygulama", "İsteminizde kabul kriterlerini sayısal verin. '10 istek/sn, 11. reddedilsin'. Önce test yazdırıp sonra fonksiyonu o testlere göre yazdırabilirsiniz — TDD döngüsü. AI hem kodu yazar hem testleri çalıştırıp doğrulayabilir.", ["İstemin sonuna kabul kriteri ekleyin", "'Unit test yaz ve çalıştır' deyin", "Beklenen davranışı sayısal yazın"], "«Rate limiter: 10 req/sn. 11. reddedilmeli. Test yaz ve çalıştır.»", source=_GITHUB_BLOG_TDD),
            _tip("AI kendi işini doğrulasın", "Test senaryosu veya örnek giriş/çıkış verirseniz AI ürettiğini bu kriterlere göre kontrol edebilir. Given-When-Then test isimleri Copilot'a daha iyi kod üretir. LLM hâlâ hata yapabilir — TDD geri bildirimi kritik.", ["Test senaryosu veya örnek ekleyin", "'Çalıştır' veya 'Doğrula' deyin", "AI test çalıştırıp sonucu bildirir"], "«validateEmail('a@b.com') true dönmeli. Test et.»", source=_GITHUB_BLOG_UNIT_TEST),
            _tip("Takip ile yineleyin", "Yanıt tam değilse tüm istemi yeniden yazmayın. '2. maddeyi genişlet' veya 'Sadece X'i değiştir' gibi takip gönderin. Önceki yanıta referans vererek («son yanıttaki 3. madde») netleştirin.", ["Giriş kutusuna takip yazın", "Spesifik düzeltme isteyin", "Aynı sohbette devam edin"], "«Sadece hata mesajını Türkçe yap»", source=_GITHUB_DOCS_PROMPT_ENG),
        ],
    },
    {
        "id": 20, "title": "Oturum yönetimi", "subtitle": "Temel · Session",
        "theme": "slate", "img": "agents-overview/chat-view-expanded.png",
        "cta": "Sohbet oturumları", "cta_url": "/docs/copilot/chat/chat-sessions",
        "tips": [
            _tip("İlgisiz geçmişi kaldırın", "Konu değiştiyse veya eski sorular geçersizse sohbet geçmişini temizleyin. İlgisiz mesajları silin; Copilot sadece alakalı geçmişi kullansın. Yeni görev için thread ile yeni konuşma açın. New Chat ile yeni oturum en temizi.", ["Mesaja sağ tık → Remove veya New Chat (+) ile yeni sohbet", "Bağlam kirlenmişse yeni sohbet açın"], "10 mesaj sonra konu değiştiyse → New Chat", source=_GITHUB_DOCS_PROMPT_ENG),
            _tip("Paralel oturumlar", "Bağımsız iki göreviniz varsa iki ayrı sohbette ilerleyin. Agent Sessions görünümünden geçiş yapın. Her oturum kendi thread'inde; bağlam karışmaz. /new ile hızlı yeni sohbet.", ["Farklı oturumlar açın", "Sol tarafta oturum listesinden geçiş yapın", "Her oturum kendi bağlamında çalışır"], "Bir sohbet: login. Diğeri: veritabanı. Paralel ilerleyin.", source=_GITHUB_DOCS_CHEAT_SHEET),
            _tip("Kontrol noktaları", "Ajan yanlış yöne gidiyorsa zincirleme düzeltmek zor olabilir. Checkpoint'e dönerek bilinen iyi duruma geri alın. Incremental complexity: her adımı doğrulayın, karmaşıklık eklemeden önce.", ["Sohbet geçmişinde checkpoint varsa kullanın", "O noktaya dönün", "Farklı talimatla devam edin"], "Ajan 5 dosyayı yanlış değiştirdiyse → checkpoint'a dön", source=_VS_CODE_CONTEXT_ENG),
        ],
    },
    # ========== 21-30 ORTA ==========
    {
        "id": 21, "title": "AI çıktısını doğrulama", "subtitle": "Orta · Kalite",
        "theme": "red", "img": "review-code-edits/copilot-edits-file-review-controls.png",
        "cta": "Copilot güvenliği", "cta_url": "/docs/copilot/security",
        "tips": [
            _tip("Kabul etmeden önce inceleyin", "AI ürettiği kodu kabul etmeden önce okuyun. Fonksiyonellik, güvenlik, okunabilirlik ve sürdürülebilirliği düşünün. Gerekirse Copilot Chat'ten kodu açıklamasını isteyin. Kenar durumları, null kontrolü, hata mesajlarını kontrol edin.", ["Önerilen değişikliği diff olarak görün", "Her satırı gözden geçirin", "Şüphe varsa reddedin"], "Boş liste, null, çok uzun string — bu girdilerde ne oluyor?", source=_GITHUB_DOCS_BEST_PRACTICES),
            _tip("Test çalıştırın", "AI değişiklik yaptıktan sonra ilgili testleri çalıştırın. Linting, code scanning, IP scanning gibi araçlarla ek doğrulama katmanı ekleyin. AI 'test et' demiş olsanız bile sonucu siz kontrol edin.", ["npm test veya proje test komutu", "AI çalıştırmışsa çıktıyı kontrol edin", "Test yoksa manuel senaryo deneyin", "Linting ve tarama araçları kullanın"], "Kod değişikliği sonrası: npm test", source=_GITHUB_DOCS_BEST_PRACTICES),
            _tip("Güvenlik kontrolü", "Enjeksiyon, hardcoded API key, eksik input validasyonu. Responsible use: şifre, token, PII sohbetine göndermeyin. Trust Center'da gizlilik ve IP politikalarını inceleyin.", ["Üretilen kodu güvenlik açısından tarayın", "Env variable, secret manager kullanılmalı", "User input için validasyon kontrol edin"], "API key kodda görünüyorsa → env variable", source=_GITHUB_DOCS_RESPONSIBLE),
        ],
    },
    {
        "id": 22, "title": "Büyük kod tabanları", "subtitle": "Orta · Scale",
        "theme": "indigo", "img": "context-engineering-guide/context-engineering-workflow.png",
        "cta": "Çalışma alanı bağlamı", "cta_url": "/docs/copilot/reference/workspace-context",
        "tips": [
            _tip("Çalışma alanı indekslemesi", "VS Code projeyi indeksler; #codebase ile hızlı semantik arama. Basic (daha basit algoritma), local (yerel semantik) veya remote (GitHub depo) indeks seçenekleri. Büyük depolarda remote daha hızlı.", ["Proje açıkken arka planda indekslenir", "Status bar'da durumu kontrol edin", "Büyük depo için remote index açın"], "1000+ dosyada #codebase ile 'auth nerede?'", source=_VS_CODE_CHAT_CONTEXT),
            _tip("Proje düzeyinde talimatlar", "Mimari, modül sınırları, API sözleşmeleri gibi AI'ın koddan çıkaramayacağı bilgileri copilot-instructions.md'de verin. PRODUCT.md (ürün vizyonu), ARCHITECTURE.md (mimari), CONTRIBUTING.md (katkı rehberi) ile karar verme bağlamını zenginleştirin.", ["ARCHITECTURE.md, CONTRIBUTING.md referansları", "Modül sınırları: 'X Y'yi import etmemeli'", "Kısa ve odaklı"], "«API layer sadece services/ ile konuşur»", source=_VS_CODE_CONTEXT_ENG),
            _tip("Monorepo'da odaklı bağlam", "Multi-root workspace'te AI'a hangi köke odaklanacağını net verin. #packages/auth gibi spesifik referans. Bağlam mühendisliği ölçeklendirmede proje geneli, modül ve özellik katmanları düşünün.", ["File > Add Folder ile multi-root", "#packages/api gibi belirli kök", "Tüm monorepo'yu eklemeyin"], "#packages/api veya #apps/web", source=_VS_CODE_CONTEXT_ENG),
        ],
    },
    {
        "id": 23, "title": "Özel ajan kavramı", "subtitle": "Orta · Custom agents",
        "theme": "violet", "img": "background-agents/custom-agent-selection.png",
        "cta": "Özel ajanlar", "cta_url": "/docs/copilot/customization/custom-agents",
        "tips": [
            _tip("Özel ajan nedir?", "Belirli bir işe odaklanmış AI kişiliğidir. Planlama, güvenlik incelemesi, kod yazımı için farklı ajanlar. Persona örneği: Senior C++ Developer kod kalitesi odaklı. Her biri kendi talimat ve araç setiyle daha iyi sonuç verir.", ["Mod seçiciden hazır ajanları seçin (Plan, Agent vb.)", "İleride .agent.md ile kendi ajanlarınızı tanımlayın", "Görev tipine göre ajan seçin"], "Mimari plan → Plan. Kod yaz → Agent.", source=_GITHUB_DOCS_BEST_PRACTICES),
            _tip(".agent.md ile tanımlama", "Projede .github/agents/ klasörüne .agent.md ekleyerek özel ajan tanımlayın. description, tools, talimatlar, handoffs yazın. Chat: New Custom Agent komutu ile başlayın. Canlı belge — hatalara göre güncelleyin.", [".github/agents/ oluşturun", "plan.agent.md gibi dosya", "description, tools: ['search','read'] ve talimatlar"], "Planlama: tools: ['search', 'read', 'fetch'] — edit eklemeyin", source=_VS_CODE_CONTEXT_ENG),
            _tip("tools: sadece gereken araçlar", "Planlama ajanı dosya düzenlemesin; tools: ['search','read'] yeterli. Uygulama ajanı edit, read, search gerektirir. Güvenlik: gereksiz araç data exfiltration riskini artırır. Minimum araç prensibi.", ["Planlama/inceleme: edit, write eklemeyin", "Uygulama: edit, read, search", "Daha az araç = daha hızlı, odaklı yanıt"], "Planlama: salt okunur. Uygulama: tam yetki.", source=_VS_CODE_CONTEXT_ENG),
        ],
    },
    {
        "id": 24, "title": "tools: sınırlama", "subtitle": "Orta · Araç verimliliği",
        "theme": "teal", "img": "chat-tools/chat-tools-picker.png",
        "cta": "Ajan araçları", "cta_url": "/docs/copilot/agents/agent-tools",
        "tips": [
            _tip("Salt okunur araçlar", "Sadece okuma/analiz istiyorsanız tools: ['search','fetch','read']. AI yanlışlıkla dosya değiştiremez.", [".agent.md'de tools listesine edit, write eklemeyin", "Codebase arama, dosya okuma, web fetch yeterli", "Değişiklik istediğinizde siz uygularsınız"], "Güvenlik incelemesi: tools: ['read','search']"),
            _tip("Planlama ajanı araçları", "Planlama ajanı düzenleme aracı gerektirmez. search, read, fetch ile araştırma yapar.", ["plan.agent.md: tools: ['search','read','fetch']", "edit aracı eklemeyin", "Yanlışlıkla kod değişikliği önlenir"], "Planlama: search, read, fetch — edit yok"),
            _tip("Daha az araç = daha hızlı", "Görev için gereksiz araç eklemek hem yavaşlatır hem yanıtı dağıtır. Sadece o iş için gereken araçları verin.", ["Her ajan için minimal tools listesi", "Planlama: read, search", "Uygulama: edit, read, search, run vb."], "Görev için minimum araç kullanın"),
        ],
    },
    {
        "id": 25, "title": "model: ile ajana özel model", "subtitle": "Orta · Model özelleştirme",
        "theme": "purple", "img": "language-models/model-dropdown-change-model.png",
        "cta": "Dil modelleri", "cta_url": "/docs/copilot/customization/language-models",
        "tips": [
            _tip("Her ajana uygun model", "Planlama gibi karmaşık işler için büyük model, basit kod yazımı için küçük model. .agent.md'de model: alanı ile atayın.", [".agent.md üstünde model: ['Model Adı']", "Chat'te mevcut modelleri kontrol edin", "Başlangıçta varsayılan, ileride özelleştirin"], "Planlama: model: ['Claude Sonnet']. Uygulama: daha küçük model."),
            _tip("Maliyet ve hız dengesi", "Büyük modeller pahalı ve yavaş; küçük modeller hızlı ve ucuz. Görev karmaşıklığına göre seçin.", ["Planlama → büyük model", "Uygulama (açık talimatlar) → küçük model", "Deneyerek karar verin"], "Uygulama ajanı: Claude Haiku deneyin"),
            _tip("Prompt dosyasında model", ".prompt.md içinde de model: tanımlayabilirsiniz. O prompt çağrıldığında her zaman bu model kullanılır.", ["code-review.prompt.md: model: ['Claude Sonnet']", "İnceleme için tutarlı büyük model", "Her seferinde seçmeye gerek kalmaz"], "İnceleme prompt'u: model sabitleyin"),
        ],
    },
    {
        "id": 26, "title": "Handoff yapılandırma", "subtitle": "Orta · handoffs",
        "theme": "cyan", "img": "agents-overview/hand-off-agent-session.png",
        "cta": "Handoff", "cta_url": "/docs/copilot/customization/custom-agents#handoffs",
        "tips": [
            _tip("handoffs frontmatter", ".agent.md üstünde handoffs: bölümü ile geçiş düğmeleri tanımlanır. label: düğme metni, agent: hedef, prompt: gönderilecek mesaj.", ["plan.agent.md'de handoffs: ekleyin", "label, agent, prompt alanlarını doldurun", "send: true ile otomatik gönderim (isteğe bağlı)"], "handoffs: - label: Uygulamaya Geç | agent: impl | prompt: Yukarıdaki plana göre kod yaz"),
            _tip("Planlama → Uygulama handoff", "Plan ajanı planı bitirince 'Start Implementation' düğmesi çıkar. Tıklayınca Agent'a plan ve prompt gider.", ["Plan ajanında handoffs tanımlayın", "agent: uygulama ajanı adı", "prompt: «Plandaki adımları uygula»"], "Plan → Start Implementation → Agent"),
            _tip("Uygulama → İnceleme", "Uygulama ajanı kodu bitirince 'Start Review' gibi handoff ile inceleme ajana geçebilirsiniz.", ["Uygulama ajanında handoffs", "agent: inceleme ajanı", "prompt: «Bu değişiklikleri incele»"], "Uygulama → Review handoff"),
        ],
    },
    {
        "id": 27, "title": "Agent Skills giriş", "subtitle": "Orta · SKILL.md",
        "theme": "emerald", "img": "agent-plugins/extensions-view.png",
        "cta": "Agent Skills", "cta_url": "/docs/copilot/customization/agent-skills",
        "tips": [
            _tip("Skill nedir?", "Talimatlar, scriptler, örnekler içeren klasörler. Özel talimatlardan farkı: sadece ilgili olduğunda yüklenir; her sohbette değil. Token tasarrufu.", [".github/skills/ klasörü oluşturun", "Alt klasör (örn. kod-incelemesi)", "SKILL.md ve description ile ne zaman yükleneceğini yazın"], "Kod incelemesi skill: 'Kullanıcı code review istediğinde yüklenir'"),
            _tip(".github/skills/ altında SKILL.md", "Test, dağıtım, kod incelemesi gibi iş akışları için skill tanımlayın. /skills ile yönetin.", ["Chat'e /skills yazın", "Configure Skills ile yeni skill ekleyin", "Her skill için alt klasör + SKILL.md"], "/skills → Configure Skills → test yazma skill"),
            _tip("Skill'ler taşınabilir", "agentskills.io standardında. VS Code, Copilot CLI, GitHub Copilot'ta çalışır. Ekipçe paylaşabilirsiniz.", ["Skill klasörünü projeler arası kopyalayın", ".github/skills/ veya ~/.copilot/skills/", "Aynı SKILL.md yapısı her yerde geçerli"], "Ortak 'güvenlik incelemesi' skill'ini depoda tutun"),
        ],
    },
    {
        "id": 28, "title": "Alt ajanlar (subagents)", "subtitle": "Orta · Subagents",
        "theme": "rose", "img": "subagents/subagent-execution-flow.png",
        "cta": "Alt ajanlar", "cta_url": "/docs/copilot/agents/subagents",
        "tips": [
            _tip("Alt ajan nedir?", "Ana görevin bir parçasını (araştırma, analiz) ayrı 'oda'da yapan geçici AI. Ana sohbet sadece özet alır; ara adımlar gelmez. Token tasarrufu.", ["Agent modunda karmaşık görev verin", "AI gerekirse otomatik alt ajan başlatır", "Sohbette 'Subagent çalışıyor...' görünür"], "«Bu API'yi analiz et ve en iyi kullanım öner»"),
            _tip("Paralel analiz", "Birden fazla yönü aynı anda inceletmek için (güvenlik, performans, erişilebilirlik) AI birden fazla alt ajanı paralel çalıştırır. Erişilebilirlik için WCAG, w3.org referansı isteyebilirsiniz.", ["İsteminizde 'paralel' veya 'aynı anda' kullanın", "«Güvenlik, performans, erişilebilirliği aynı anda analiz et»", "Tüm sonuçlar birleştirilir"], "«Bu PR'ı güvenlik, performans, okunabilirlik açısından paralel incele»", source=_GITHUB_BLOG_ACCESSIBILITY),
            _tip("Araştırma için alt ajan", "Ana konunuzu dağıtmadan keşif yapın. Alt ajan sadece nihai özeti getirir.", ["İsteminizde 'araştır', 'incele', 'karşılaştır' kullanın", "Beklenen çıktıyı net yazın", "Alt ajan otomatik başlar"], "«Redis vs Memcached bu proje için? Araştır, artı/eksileri listele.»"),
        ],
    },
    {
        "id": 29, "title": "Paralel subagents", "subtitle": "Orta · Paralel çalışma",
        "theme": "sky", "img": "agents-overview/agent-types-diagram-v3.png",
        "cta": "Alt ajan senaryoları", "cta_url": "/docs/copilot/agents/subagents#usage-scenarios",
        "tips": [
            _tip("Paralel ne zaman?", "Birden fazla bağımsız araştırma/analiz gerekiyorsa AI alt ajanları paralel başlatır. Hepsi bitene kadar bekler, sonuçları birleştirir.", ["İsteminizde paralel analiz ima edin", "Örn: 'X ve Y'yi paralel incele, karşılaştır'", "Seri yerine paralel = zaman kazanımı"], "«3 farklı caching yaklaşımını paralel araştır, karşılaştır»"),
            _tip("runSubagent aracı", "Özel ajanlarda tools: listesinde runSubagent varsa AI alt ajan başlatabilir. Varsayılan davranışta zaten etkindir.", [".agent.md'de tools: ['runSubagent', ...] veya agent aracı", "AI karmaşık görevde alt ajan kullanır", "Siz manuel başlatmanıza gerek yok"], "Agent otomatik alt ajan kullanır"),
            _tip("Alt ajan özeti", "Alt ajan tüm ara adımları ana sohbete göndermez; sadece nihai özet. Ana bağlam temiz kalır, token tasarrufu sağlanır.", ["Alt ajan daraltılmış görünür", "Tıklayınca detayları görürsünüz", "Ana sohbet sadece özet alır"], "Araştırma 20 adım yaptıysa ana sohbete sadece özet gelir"),
        ],
    },
    {
        "id": 30, "title": "Tam iş akışı: Plan → Uygulama → İnceleme", "subtitle": "Orta · Orchestration",
        "theme": "blue", "img": "chat-planning/plan-agent-sample.png",
        "cta": "Bağlam mühendisliği", "cta_url": "/docs/copilot/guides/context-engineering-guide",
        "tips": [
            _tip("Üç aşamalı akış", "1) Plan ajanı plan oluşturur. 2) Handoff ile Agent uygular. 3) İnceleme (handoff veya manuel) ile doğrular. Farklı iş türlerini (planlama, kodlama, test) ayrı sohbetlerde tutun; context isolation kaliteyi artırır. Her adımda siz onaylarsınız.", ["Plan ajanı seç → plan oluştur", "Start Implementation → Agent", "İnceleme ajanı varsa oraya handoff"], "Plan → Agent → Review zinciri", source=_VS_CODE_CONTEXT_ENG),
            _tip("Özel ajanlarla orkestrasyon", "Plan, implementation, review için ayrı .agent.md tanımlayın. Handoff'larla birbirine bağlayın.", ["plan.agent.md, impl.agent.md, review.agent.md", "Her birinde handoffs ile sonrakine geçiş", "Koordinatör gibi çalışır"], "Plan → handoff → Impl → handoff → Review"),
            _tip("Kontrol sizde", "Her handoff öncesi çıktıyı inceleyin. Yanlışsa düzeltme isteyin. Doğruysa devam edin. AI tam otomatik değil; siz yönlendirirsiniz.", ["Planı okuyun, eksikse düzeltin", "Agent'ın kodunu inceleyin", "İnceleme bulgularını değerlendirin"], "Her adımda onay vermeden handoff'a basmayın"),
        ],
    },
    # ========== 31-40 İLERİ ==========
    {
        "id": 31, "title": "Skill SKILL.md yapısı", "subtitle": "İleri · Skill içeriği",
        "theme": "emerald", "img": "agent-plugins/extensions-view.png",
        "cta": "Agent Skills", "cta_url": "/docs/copilot/customization/agent-skills",
        "tips": [
            _tip("SKILL.md zorunlu alanlar", "description: ne zaman yükleneceği. Talimatlar: AI'ın izleyeceği adımlar. Örnekler, scriptler, dosya referansları ekleyebilirsiniz.", ["SKILL.md üstünde description: yazın", "Örn: 'Kullanıcı test yazma istediğinde'", "Talimatları maddeler halinde ekleyin"], "description: Kullanıcı unit test istediğinde bu skill yüklenir"),
            _tip("Skill description ile kapsam", "Skill'ler applyTo desteklemez. Ne zaman yükleneceğini description: ile yazın: 'Kullanıcı test yazma istediğinde', 'TypeScript dosyasında çalışırken' gibi. AI sohbet bağlamına göre ilgili skill'i seçer.", ["description: 'Kullanıcı X istediğinde bu skill yüklenir'", "Örn: test, refactor, güvenlik incelemesi", "Belirsiz description = gereksiz yükleme"], "description: Unit test yazma veya test ekleme istendiğinde"),
            _tip("Skill paylaşımı", "Skill'leri depo, npm paketi veya ortak klasörde tutun. Ekip üyeleri .github/skills/'e symlink veya kopya ile ekler.", ["Skill klasörünü repo'da tutun", "README'de kurulum adımları", "Aynı standardı tüm projelerde kullanın"], "github.com/ekip/ai-skills repo'sundan skill çek"),
        ],
    },
    {
        "id": 32, "title": "Çok aşamalı handoff zinciri", "subtitle": "İleri · Orchestration",
        "theme": "cyan", "img": "agents-overview/hand-off-agent-session.png",
        "cta": "Custom agents", "cta_url": "/docs/copilot/customization/custom-agents",
        "tips": [
            _tip("3+ ajan zinciri", "Plan → Uygulama → İnceleme → Dağıtım gibi uzun zincirler. Her ajan sonunda handoff ile sonrakine geçiş. Karmaşık iş akışları için.", ["plan.agent.md → impl → review → deploy", "Her handoff'ta prompt: ile ne yapılacağını yazın", "Zincir uzadıkça kontrol noktaları önemli"], "Plan → Impl → Review → Deploy handoff zinciri"),
            _tip("Koşullu handoff", "handoffs: bölümünde birden fazla düğme. Kullanıcı duruma göre 'Düzelt' veya 'Devam' seçebilir. Aynı ajanda farklı hedefler.", ["handoffs: altında 2+ giriş", "label, agent, prompt her biri farklı", "Örn: Düzelt → Plan. Devam → Impl."], "Plan eksikse: Düzelt düğmesi. Tamamlaysa: Devam."),
            _tip("Handoff bağlam iletimi", "Handoff'ta prompt: yazarken «Yukarıdaki plan», «Bu değişiklikler» gibi referanslarla önceki çıktıyı iletin. AI otomatik bağlam alır.", ["prompt: «Yukarıdaki plana göre 1. adımı uygula»", "Önceki mesajda zaten plan var", "Ek dosya eklemenize gerek kalmaz"], "Handoff prompt: Plandaki adımları sırayla uygula"),
        ],
    },
    {
        "id": 33, "title": "Özel ajan derinlemesine", "subtitle": "İleri · .agent.md",
        "theme": "violet", "img": "background-agents/custom-agent-selection.png",
        "cta": "Özel ajanlar", "cta_url": "/docs/copilot/customization/custom-agents",
        "tips": [
            _tip("description ve talimatlar", "description: AI'a bu ajanın ne yaptığını anlatır. Altındaki talimatlar her görevde uygulanır. Kısa, net cümleler.", ["description: 1-2 cümle", "Talimatlar: maddeler halinde", "Örn: 'Planlama ajanı. Kod yazmaz, sadece adım listesi üretir.'"], "description: Bu ajan sadece plan üretir. Kod yazmaz."),
            _tip("tools: tam listesi", "search, read, fetch, edit, write, run, runSubagent vb. Her aracın amacı farklı. Görev için minimum araç seçin; güvenlik ve hız için.", ["Dokümantasyonda tools listesini inceleyin", "Planlama: search, read, fetch", "Uygulama: edit, read, search, run"], "İnceleme: read, search. Değişiklik yok."),
            _tip("Özel ajan test etme", "Yeni ajan tanımladıktan sonra basit görevle dene. Yanıt yanlış yöne gidiyorsa description veya talimatları güncelleyin. tools: fazlaysa kısıtlayın.", ["Mod seçiciden yeni ajanı seçin", "Basit test: 'Bu projenin yapısını özetle'", "Beklenenden farklıysa talimatları netleştirin"], "Plan ajanı kod yazıyorsa tools: edit çıkarın"),
        ],
    },
    {
        "id": 34, "title": "Bağlam optimizasyonu", "subtitle": "İleri · Token verimliliği",
        "theme": "amber", "img": "chat-tools/chat-tools-picker.png",
        "cta": "Bağlam mühendisliği", "cta_url": "/docs/copilot/guides/context-engineering-guide",
        "tips": [
            _tip("Önce #codebase, gerekirse dosya", "Bilinmeyen sorularda önce #codebase deneyin. AI ilgili dosyaları bulur. Yetmezse manuel #dosya ekleyin. Tüm projeyi eklemeyin.", ["İlk mesaj: soru + #codebase", "Yanıt yetersizse: «#src/auth/ ekle»", "Gereksiz dosya = token israfı"], "«Auth nasıl çalışıyor? #codebase» — yetmezse #src/auth/"),
            _tip("/compact stratejisi", "Uzun sohbetlerde konu özetlenince bazı detay kaybolur. Kritik bilgi varsa /compact öncesi not alın veya checkpoint oluşturun.", ["10+ mesajda /compact düşünün", "Önemli kararları ayrı tutun", "Checkpoint varsa ona göre ilerleyin"], "Plan 5 adım vardı → /compact öncesi kopyala"),
            _tip("Talimat + Skill ayrımı", "Her sohbette gelen: copilot-instructions. Sadece ilgili olduğunda: Skill. Uzun rehberleri Skill'e koyun; talimatlarda kısa kurallar.", ["copilot-instructions: 1 sayfa civarı", "Detaylı rehber: Skill", "Skill description ile ne zaman yükleneceğini yazın"], "Test yazma rehberi: Skill. Genel kod stili: talimat."),
        ],
    },
    {
        "id": 35, "title": "Güvenlik ve gizlilik", "subtitle": "İleri · Güvenli kullanım",
        "theme": "red", "img": "review-code-edits/copilot-edits-file-review-controls.png",
        "cta": "Copilot güvenliği", "cta_url": "/docs/copilot/security",
        "tips": [
            _tip("Hassas veri yapıştırmayın", "Şifre, API key, token, PII (kişisel bilgi) AI sohbetine göndermeyin. Responsible use: VS Code hassas bilgi taraması yapar. Kod örneği verecekseniz placeholder kullanın. Trust Center'da veri işleme politikalarını inceleyin.", ["Gerçek değer yerine PLACEHOLDER", "API key → process.env.API_KEY", "Şifre → '***' veya env ref"], "apiKey: 'sk-...' yerine apiKey: process.env.API_KEY", source=_GITHUB_DOCS_RESPONSIBLE),
            _tip("Üretilen kodu güvenlik taraması", "AI kodu SQL injection, XSS, path traversal açığı içerebilir. Özellikle user input kullanan kodda manuel veya otomatik tarama yapın. Responsible use: önerilen kodu her zaman doğrulayın; AI hataya açıktır.", ["User input → sanitize/validate", "SQL → parametreli sorgu", "AI'dan gelen kodu güvenlik gözüyle inceleyin"], "req.body.email direkt SQL'e gitmemeli", source=_GITHUB_DOCS_RESPONSIBLE),
            _tip("Kurumsal ayarlar", "GitHub Copilot Business/Enterprise ile veri eğitim politikaları, filtreleme, audit log. Business planında kodunuz eğitime gitmez. Şirket politikasına uyun; IP, uyumluluk soruları için Trust Center.", ["Yönetici ayarlarını kontrol edin", "Eğitimden hariç tutma (opt-out)", "SSO, IP kısıtlaması varsa uygulayın"], "Şirket verisi eğitime gitmemeli → ayarlardan kapat", source=_GITHUB_TRUST),
        ],
    },
    {
        "id": 36, "title": "Prompt dosyası ileri düzey", "subtitle": "İleri · .prompt.md",
        "theme": "lime", "img": "customization/prompt-file-recommendations.png",
        "cta": "Prompt dosyaları", "cta_url": "/docs/copilot/customization/prompt-files",
        "tips": [
            _tip("agent: + prompt: + model:", ".prompt.md'de agent: hangi ajana geçileceği, prompt: varsayılan istem, model: sabit model. Tek komutla tam kurulum.", ["agent: inceleme-ajani", "prompt: «Bu değişiklikleri incele...»", "model: ['Claude Sonnet']"], "/code-review → inceleme ajana geç, prompt hazır, model sabit"),
            _tip("Placeholder ve değişkenler", "VS Code prompt dosyalarında ${fileBasename}, ${relativeFile} gibi placeholder'lar desteklenir. Örn. ${fileBasename} ile seçili dosya adı enjekte edilir. Dokümantasyonda tam listeyi kontrol edin.", ["Placeholder varsa kullanın", "Örn: ${fileBasename}, ${relativeFile}", "Desteklenmiyorsa sabit metin"], "prompt: «${fileBasename} dosyasını incele»"),
            _tip("Prompt kategorileri", "Farklı iş türleri için: /code-review, /security-check, /refactor, /explain. Her biri ayrı .prompt.md. /prompts ile hepsini yönetin.", [".github/prompts/ altında kategorize edin", "security-check.prompt.md, refactor.prompt.md", "Kısa isimler: /sec, /refactor"], "/sec → güvenlik. /refactor → refaktör."),
        ],
    },
    {
        "id": 37, "title": "Hata ayıklama AI ile", "subtitle": "İleri · Debug",
        "theme": "rose", "img": "test-driven-development-guide/tdd-implementation-diagram.png",
        "cta": "En iyi uygulamalar", "cta_url": "/docs/copilot/best-practices",
        "tips": [
            _tip("Hata mesajı + stack trace", "AI'a hata ayıklarken tam hata mesajı ve stack trace verin. Dosya:satır bilgisi AI'ın doğru yere bakmasını sağlar. Cookbook'da invalid JSON, rate limit gibi debug örnekleri var. /fix ile aktif dosyadaki hataları düzeltebilirsiniz.", ["Hata çıktısını kopyalayın", "İlgili dosyayı # ile ekleyin", "«Bu hata neden oluyor? #src/foo.ts»"], "TypeError: Cannot read 'x' of undefined at foo.ts:42", source=_GITHUB_DOCS_COOKBOOK),
            _tip("Reproducible adımlar", "«X yaptığımda Y oluyor» şeklinde adımları yazın. AI bazen çevresel sorunları (env, cache) önerebilir. Minimal reproducible case oluşturmak hem AI hem sizin için hızlandırır.", ["1. Ne yaptınız", "2. Ne beklediniz", "3. Ne oldu", "İlgili kodu # ile ekleyin"], "Login butonuna basınca → 500 alıyorum. #LoginForm.tsx", source=_VS_CODE_TEST),
            _tip("Parçalı debug", "Büyük hatayı tek seferde çözdürmeye çalışmayın. Önce «Bu fonksiyon doğru mu?» sonra «Bu satır neden fail ediyor?» diye daraltın. Hata ayıklamada Copilot Chat ile başlamak genelde daha hızlıdır.", ["Önce genel: «Bu modül ne yapıyor?»", "Sonra spesifik: «42. satırda neden null?»", "Minimal reproducible case oluşturun"], "Genel soru → daralt → en küçük failing case", source=_GITHUB_BLOG_IDE),
        ],
    },
    {
        "id": 38, "title": "Ekip için standartlar", "subtitle": "İleri · Organizasyon",
        "theme": "indigo", "img": "customization/configure-chat-instructions.png",
        "cta": "Özel talimatlar", "cta_url": "/docs/copilot/customization/custom-instructions",
        "tips": [
            _tip("copilot-instructions.md ekip sözleşmesi", "Tüm ekip aynı talimatlara uyar. Kod stili, commit mesajı formatı, PR şablonu, test kuralları. Organizasyon seviyesinde accessibility (WCAG) gibi standartlar da tanımlanabilir. Tek kaynak.", [".github/copilot-instructions.md'de ekip kuralları", "CONTRIBUTING.md referansı", "Yeni üye /init + düzenleme"], "## Commit: feat/fix/refactor prefix. ## Test: her public fn test.", source=_GITHUB_ACCESSIBILITY),
            _tip("Ortak Skill deposu", "Şirket veya ekip için skill'leri ortak depoda tutun. Her proje .github/skills/'e submodule veya script ile çeker.", ["Ortak repo: org/ai-copilot-skills", "Projede git submodule add", "Veya setup script ile kopyala"], "git submodule add …/ai-skills .github/skills/shared"),
            _tip("Prompt şablonları", "code-review, security-check, release-notes gibi standart prompt'ları paylaşın. Yeni projede aynı .prompt.md'ler kullanılır.", [".github/prompts/ şablonları repo'da", "Template repo ile yeni proje", "Kurulumda prompts/ kopyalanır"], "Tüm projelerde /code-review aynı sorularla"),
        ],
    },
    {
        "id": 39, "title": "Performans ve ölçeklenebilirlik", "subtitle": "İleri · Best practices",
        "theme": "teal", "img": "context-engineering-guide/context-engineering-workflow.png",
        "cta": "Bağlam mühendisliği", "cta_url": "/docs/copilot/guides/context-engineering-guide",
        "tips": [
            _tip("Büyük dosya vermeyin", "1000+ satır dosyayı bütün halde eklemeyin. İlgili fonksiyon veya sınıfı seçip # ile verin. Bağlam penceresi dolunca eski mesajlar kesilir.", ["Sadece ilgili kısmı referans verin", "# ile fonksiyon/sınıf seçin", "Gerekirse dosyayı parçalara bölün"], "#AuthService.login metodu — tüm auth.ts değil"),
            _tip("Monorepo stratejisi", "packages/auth, packages/api gibi her paketi ayrı referans edin. Workspace root'u eklemeyin; ilgili package'a odaklanın.", ["#packages/auth veya #apps/web", "Paket sınırlarını net tutun", "AI'ın hangi köke baktığını belirtin"], "«API'de rate limit ekle» → #packages/api"),
            _tip("Yinelenen sohbetler", "Aynı tip soruyu sık soruyorsanız prompt dosyası yapın. Her seferinde aynı uzun istemi yazmak yerine /komut ile hazır başlayın.", ["Sık soru → .prompt.md", "/soru-adı ile çağır", "Zaman ve token tasarrufu"], "Sürekli «Bu PR'ı incele» → /pr-review"),
        ],
    },
    {
        "id": 40, "title": "40. gün: Tam döngü özeti", "subtitle": "İleri · Kapanış",
        "theme": "blue", "img": "chat-planning/plan-agent-sample.png",
        "cta": "Copilot dokümantasyonu", "cta_url": "/docs/copilot",
        "tips": [
            _tip("Başlangıçtan ileriye yolculuk", "1–10: Kurulum, Ask/Agent, #, Inline Chat. 11–20: Token, talimatlar, Plan, handoff. 21–30: Doğrulama, özel ajanlar, Skill, subagent. 31–40: Derinlemesine ajan, güvenlik, ekip. Quickstart ile task app; TDD guide ile test-first akış.", ["Geçmiş mailleri gözden geçirin", "Eksik kaldığınız konuları tekrar edin", "Kendi .agent.md, .prompt.md, Skill'lerinizi oluşturun"], "1. gün: Chat aç. 40. gün: Plan→Impl→Review zinciri.", source=_VS_CODE_QUICKSTART),
            _tip("Kendi playbook'unuzu yazın", "En sık yaptığınız işler için .prompt.md ve Skill oluşturun. Cookbook ve örnek promptlardan ilham alın. Zamanla genişletin; canlı belge gibi güncelleyin. Ekipçe paylaşın.", ["En çok 5 görevinizi listeleyin", "Her biri için prompt veya skill", "CONTRIBUTING'a 'AI kullanımı' ekleyin"], "code-review, security-check, refactor — 3 prompt ile başlayın", source=_GITHUB_DOCS_COOKBOOK),
            _tip("Sürekli öğrenme", "Copilot ve AI araçları hızla gelişiyor. Resmi dokümantasyonu, GitHub changelog, blog'u takip edin. Copilot CLI, VS Code dışı kullanım için terminal'de copilot komutu. Yeni özellikler çıktıkça deneyin.", ["code.visualstudio.com/docs/copilot", "github.blog/changelog (label: copilot)", "Topluluk örnekleri"], "Her çeyrekte 'Yeni neler var?' kontrol edin", source=_GITHUB_BLOG_CLI),
        ],
    },
]
