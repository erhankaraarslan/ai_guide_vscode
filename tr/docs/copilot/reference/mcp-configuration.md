---
ContentId: a3e1f7c2-8d4b-4f9a-b6e5-2c8d3f1a9b7e
DateApproved: 3/4/2026
MetaDescription: Visual Studio Code'da MCP sunucu yapılandırma formatı, komutları ve ayarları için referans.
MetaSocialImage: ../images/shared/github-copilot-social.png
Keywords:
- mcp
- model context protocol
- mcp.json
- configuration
- sandbox
- tools
- copilot
- reference
- ai
---
# MCP yapılandırma referansı

Bu makale VS Code'da MCP sunucu yapılandırma dosyası formatı, ilgili komutlar ve ayarlar için bir referans sağlar. MCP sunucuları ekleme ve yönetme hakkında bilgi için [MCP sunucularını ekleme ve yönetme](/docs/copilot/customization/mcp-servers.md) bölümüne bakın.

## Yapılandırma dosyası

MCP sunucu yapılandırması `mcp.json` JSON dosyasında depolanır. Bu dosya çalışma alanınızda (`.vscode/mcp.json`) veya [kullanıcı profilinizde](/docs/configure/profiles.md) olabilir. VS Code yapılandırma dosyası için IntelliSense sağlar.

### Yapılandırma yapısı

Yapılandırma dosyasının iki ana bölümü vardır:

* **`"servers": {}`**: sunucu adlarını yapılandırmalarına eşleyen bir nesne. Her anahtar sunucu adıdır ve değer sunucu yapılandırma nesnesidir. Sunucu türüne bağlı olarak farklı alanlar gereklidir.

* **`"inputs": []`**: API anahtarları gibi hassas bilgiler için girdi değişken tanımlarının isteğe bağlı dizisi.

Sunucu yapılandırmasında çalışma alanı klasörüne (`${workspaceFolder}`) referans vermek gibi [önceden tanımlanmış değişkenleri](/docs/reference/variables-reference.md) kullanabilirsiniz.

### Standart Girdi/Çıktı (stdio) sunucuları

Standart girdi ve çıktı akışları üzerinden iletişim kuran sunucular için bu yapılandırmayı kullanın. Bu yerel olarak çalışan MCP sunucuları için en yaygın türdür.

| Alan | Gerekli | Açıklama | Örnekler |
|------|---------|----------|----------|
| `type` | Evet | Sunucu bağlantı türü | `"stdio"` |
| `command` | Evet | Sunucu yürütülebilirini başlatacak komut. Sistem yolunuzda mevcut olmalı veya tam yolunu içermelidir. | `"npx"`, `"node"`, `"python"`, `"docker"` |
| `args` | Hayır | Komuta geçirilen bağımsız değişkenler dizisi | `["server.py", "--port", "3000"]` |
| `env` | Hayır | Sunucu için ortam değişkenleri | `{"API_KEY": "${input:api-key}"}` |
| `envFile` | Hayır | Daha fazla değişken yüklemek için ortam dosyası yolu | `"${workspaceFolder}/.env"` |
| `sandboxEnabled` | Hayır | Sunucuyu sandbox ortamında çalıştır. Yalnızca macOS ve Linux'ta desteklenir. | `true` |
| `sandbox` | Hayır | Sandbox sunucu için dosya sistemi ve ağ erişim kuralları. Yalnızca `sandboxEnabled` `true` olduğunda geçerlidir. [Sandbox yapılandırması](#sandbox-configuration) bölümüne bakın. | `{"filesystem": {...}, "network": {...}}` |

> [!NOTE]
> stdio sunucularında Docker kullanırken detach seçeneğini (`-d`) kullanmayın. Sunucu VS Code ile iletişim kurmak için ön planda çalışmalıdır.

<details>
<summary>Örnek yerel sunucu yapılandırması</summary>

Bu örnek `npx` kullanan temel, yerel MCP sunucu için minimal yapılandırmayı gösterir:

```json
{
    "servers": {
        "memory": {
            "command": "npx",
            "args": [
            "-y",
            "@modelcontextprotocol/server-memory"
            ]
        }
    }
}
```

</details>

### Sandbox yapılandırması

Dosya sistemi ve ağ erişimini kısıtlamak için yerel olarak çalışan stdio MCP sunucuları için sandbox'ı etkinleştirebilirsiniz. Sandbox sunucuları yalnızca açıkça izin verdiğiniz dosya sistemi yollarına ve ağ etki alanlarına erişebilir. Sandbox yalnızca macOS ve Linux'ta kullanılabilir.

Sunucu için sandbox'ı etkinleştirmek için yapılandırmasında `"sandboxEnabled": true` ayarlayın. Ardından dosya sistemi ve ağ erişim kurallarını tanımlamak için `sandbox` nesnesini kullanın. Sandbox sunucu mevcut kuralların izin vermediği erişime ihtiyaç duyduğunda sunucu çıktısında hata iletilerini kontrol edin ve `sandbox` yapılandırmasını buna göre güncelleyin.

> [!NOTE]
> Sandbox etkinleştirildiğinde araç onayları sunucu kontrollü ortamda çalıştığından otomatik onaylanır.

`sandbox` nesnesi şu özellikleri destekler:

| Özellik | Tür | Açıklama |
|---------|-----|----------|
| `filesystem.allowWrite` | string[] | Sunucunun yazmasına izin verilen dosya yolları. |
| `filesystem.denyRead` | string[] | Sunucunun okumasına izin verilmeyen dosya yolları. |
| `filesystem.denyWrite` | string[] | Sunucunun yazmasına izin verilmeyen dosya yolları. |
| `network.allowedDomains` | string[] | Sunucunun erişmesine izin verilen etki alanları. Joker karakterler desteklenir, örneğin `*.example.com`. |
| `network.deniedDomains` | string[] | Sunucunun erişmesine izin verilmeyen etki alanları. |

Dosya sistemi yol değerlerinde `${workspaceFolder}` gibi [önceden tanımlanmış değişkenleri](/docs/reference/variables-reference.md) kullanabilirsiniz.

<details>
<summary>Örnek sandbox yapılandırması</summary>

Bu örnek sandbox'ı etkinleştirir, çalışma alanına yazma erişimi verir, `.ssh` dizinine okuma erişimini reddeder ve belirli etki alanlarına ağ erişimine izin verir:

```json
{
    "servers": {
        "myServer": {
            "type": "stdio",
            "command": "npx",
            "args": ["-y", "@example/mcp-server"],
            "sandboxEnabled": true,
            "sandbox": {
                "filesystem": {
                    "allowWrite": ["${workspaceFolder}"],
                    "denyRead": ["${userHome}/.ssh"]
                },
                "network": {
                    "allowedDomains": ["api.example.com", "*.cdn.example.com"]
                }
            }
        }
    }
}
```

</details>

### HTTP ve Server-Sent Events (SSE) sunucuları

HTTP üzerinden iletişim kuran sunucular için bu yapılandırmayı kullanın. VS Code önce HTTP Stream aktarımını dener, HTTP desteklenmiyorsa SSE'ye geri döner.

| Alan | Gerekli | Açıklama | Örnekler |
|------|---------|----------|----------|
| `type` | Evet | Sunucu bağlantı türü | `"http"`, `"sse"` |
| `url` | Evet | Sunucu URL'si | `"http://localhost:3000"`, `"https://api.example.com/mcp"` |
| `headers` | Hayır | Kimlik doğrulama veya yapılandırma için HTTP başlıkları | `{"Authorization": "Bearer ${input:api-token}"}` |

Ağ üzerinden mevcut sunuculara ek olarak VS Code, Unix soketleri veya Windows'ta adlandırılmış kanallar üzerinde HTTP trafiği dinleyen MCP sunucularına `unix:///path/to/server.sock` veya Windows'ta `pipe:///pipe/named-pipe` biçiminde soket veya kanal yolu belirleyerek bağlanabilir. `unix:///tmp/server.sock#/mcp/subpath` gibi URL parçası kullanarak alt yollar belirtebilirsiniz.

<details>
<summary>Örnek uzak sunucu yapılandırması</summary>

Bu örnek kimlik doğrulaması olmayan uzak MCP sunucu için minimal yapılandırmayı gösterir:

```json
{
    "servers": {
        "context7": {
            "type": "http",
            "url": "https://mcp.context7.com/mcp"
        }
    }
}
```

</details>

### Hassas veriler için girdi değişkenleri

Girdi değişkenleri yapılandırma değerleri için yer tutucular tanımlamanızı sağlar; API anahtarları veya parolalar gibi hassas bilgileri sunucu yapılandırmasında doğrudan sabit kodlamaktan kaçınır.

`${input:variable-id}` kullanarak girdi değişkenine referans verdiğinizde VS Code sunucu ilk kez başladığında değeri sizden ister. Değer sonraki kullanım için güvenli şekilde depolanır. VS Code'da [girdi değişkenleri](/docs/reference/variables-reference.md#input-variables) hakkında daha fazla bilgi edinin.

**Girdi değişken özellikleri:**

| Alan | Gerekli | Açıklama | Örnek |
|------|---------|----------|-------|
| `type` | Evet | Girdi istemi türü | `"promptString"` |
| `id` | Evet | Sunucu yapılandırmasında referans için benzersiz tanımlayıcı | `"api-key"`, `"database-url"` |
| `description` | Evet | Kullanıcı dostu istem metni | `"GitHub Personal Access Token"` |
| `password` | Hayır | Yazılan girdiyi gizle (varsayılan: false) | API anahtarları ve parolalar için `true` |

<details>
<summary>Girdi değişkenleriyle örnek sunucu yapılandırması</summary>

Bu örnek API anahtarı gerektiren yerel sunucuyu yapılandırır:

```json
{
    "inputs": [
        {
            "type": "promptString",
            "id": "perplexity-key",
            "description": "Perplexity API Key",
            "password": true
        }
    ],
    "servers": {
        "perplexity": {
            "type": "stdio",
            "command": "npx",
            "args": [
                "-y",
                "server-perplexity-ask"
            ],
            "env": {
                "PERPLEXITY_API_KEY": "${input:perplexity-key}"
            }
        }
    }
}
```

</details>

### Geliştirme modu

Sunucu yapılandırmasına `dev` anahtarı ekleyerek MCP sunucuları için _geliştirme modunu_ etkinleştirebilirsiniz. Bu iki özelliğe sahip bir nesnedir:

* `watch`: MCP sunucuyu yeniden başlatan dosya değişiklikleri için izlenecek dosya glob deseni.
* `debug`: MCP sunucu ile hata ayıklayıcı kurmanızı sağlar. Şu anda VS Code Node.js ve Python MCP sunucularının hata ayıklamasını destekler.

MCP Dev Kılavuzunda [MCP geliştirme modu](/api/extension-guides/ai/mcp.md#mcp-development-mode-in-vs-code) hakkında daha fazla bilgi edinin.

### Sunucu adlandırma sözleşmeleri

MCP sunucularını tanımlarken sunucu adı için şu adlandırma sözleşmelerine uyun:

* Sunucu adı için camelCase kullanın, örneğin "uiTesting" veya "githubIntegration"
* Boşluk veya özel karakterler kullanmaktan kaçının
* Çakışmaları önlemek için her sunucu için benzersiz ad kullanın
* "github" veya "database" gibi sunucunun işlevselliğini veya markasını yansıtan açıklayıcı ad kullanın

## Komutlar

Aşağıdaki tablo Komut Paleti'nde (`kb(workbench.action.showCommands)`) mevcut MCP ile ilgili komutları listeler.

| Komut | Açıklama |
|-------|----------|
| **MCP: Add Server** | Çalışma alanınıza veya kullanıcı profilinize yeni MCP sunucusu ekleyin. |
| **MCP: Browse MCP Servers** | Uzantılar görünümünde MCP sunucu galerisini açın. |
| **MCP: Browse Resources** | MCP sunucuları tarafından sağlanan kaynaklara göz atın. |
| **MCP: Install Server from Manifest** | MCP manifest dosyasından MCP sunucusu yükleyin. |
| **MCP: List Servers** | Yapılandırılmış tüm MCP sunucularını listeleyin ve başlat, durdur, yeniden başlat veya çıktıyı göster gibi eylemler gerçekleştirin. |
| **MCP: Open Remote User Configuration** | Uzak ortam için `mcp.json` dosyasını açın. |
| **MCP: Open User Configuration** | Kullanıcı profilinizdeki `mcp.json` dosyasını açın. |
| **MCP: Open Workspace Folder MCP Configuration** | Çalışma alanınızdaki `.vscode/mcp.json` dosyasını açın. |
| **MCP: Reset Cached Tools** | MCP sunucuları için önbelleğe alınmış araç listesini temizleyin. Sunucunun araçları değiştiğinde kullanın. |
| **MCP: Reset Trust** | MCP sunucuları için güven kararlarını sıfırlayın; bir sonraki başlatmada yeniden onay gerektirir. |
| **MCP: Show Installed Servers** | Yüklü tüm MCP sunucularının listesini gösterin. |

## Ayarlar

VS Code yapay zeka ayarlarının tam listesi için [Yapay Zeka Ayarları Referansına](/docs/copilot/reference/copilot-settings.md) bakın. Aşağıdaki ayarlar MCP sunucularına özgüdür.

| Ayar | Açıklama |
|------|----------|
| `setting(chat.mcp.access)` | VS Code'da hangi MCP sunucularının kullanılabileceğini yönetin. |
| `setting(chat.mcp.discovery.enabled)` | Diğer uygulamalardan MCP sunucu yapılandırmasının otomatik keşfini yapılandırın. |
| `setting(chat.mcp.autostart)` (Deneysel) | Yapılandırma değişiklikleri algılandığında MCP sunucularını otomatik başlatın. |
| `setting(chat.mcp.serverSampling)` | MCP sunucularına arka planda istek yapmak için örnekleme (sampling) için hangi modellerin sunulduğunu yapılandırın. |
| `setting(chat.mcp.apps.enabled)` (Deneysel) | MCP sunucuları tarafından sağlanan zengin kullanıcı arayüzleri olan MCP Apps'i etkinleştirin veya devre dışı bırakın. |

## İlgili kaynaklar

* [MCP sunucularını ekleme ve yönetme](/docs/copilot/customization/mcp-servers.md)
* [Model Context Protocol Belgeleri](https://modelcontextprotocol.io/)
* [MCP Dev Kılavuzu](/docs/copilot/guides/mcp-developer-guide.md)
