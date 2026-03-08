---
ContentId: 9c4d5e6f-7a8b-9c0d-1e2f-3a4b5c6d7e8f
DateApproved: 3/4/2026
MetaDescription: Otomasyon, doğrulama ve politika uygulaması için ajan oturumları sırasında kritik yaşam döngüsü noktalarında özel kabuk komutları çalıştırmak üzere VS Code'da hook'ların nasıl kullanılacağını öğrenin.
MetaSocialImage: ../images/shared/github-copilot-social.png
Keywords:
- copilot
- ai
- agents
- hooks
- automation
- lifecycle
- preToolUse
- postToolUse
---

# Visual Studio Code'da ajan hook'ları (Önizleme)

Hook'lar, ajan oturumları sırasında kritik yaşam döngüsü noktalarında özel kabuk komutları çalıştırmanızı sağlar. Hook'ları iş akışlarını otomatikleştirmek, güvenlik politikalarını uygulamak, işlemleri doğrulamak ve harici araçlarla entegre olmak için kullanın. Hook'lar deterministik şekilde çalışır ve aracın yürütülmesini engelleme veya sohbete bağlam enjekte etme dahil olmak üzere ajan davranışını kontrol edebilir.

> [!NOTE]
> Ajan hook'ları şu anda Önizleme aşamasındadır. Yapılandırma formatı ve davranışı gelecek sürümlerde değişebilir.

> [!IMPORTANT]
> Kuruluşunuz hook kullanımını VS Code'da devre dışı bırakmış olabilir. Daha fazla bilgi için yöneticinizle iletişime geçin. Ayrıntılar için [kurumsal politikalar](/docs/enterprise/policies.md) bölümüne bakın.

> [!TIP]
> Tüm sohbet özelleştirmelerinizi tek bir yerde keşfetmek, oluşturmak ve yönetmek için [Sohbet Özelleştirmeleri editörünü](/docs/copilot/customization/overview.md#chat-customizations-editor) (Önizleme) kullanın. Komut Paleti'nden **Chat: Open Chat Customizations** çalıştırın.

Hook'lar yerel ajanlar, arka plan ajanları ve bulut ajanları dahil olmak üzere tüm ajan türlerinde çalışacak şekilde tasarlanmıştır. Her hook yapılandırılmış JSON girdisi alır ve ajan davranışını etkilemek için JSON çıktısı döndürebilir.

## Hook'ları neden kullanmalı?

Hook'lar deterministik, kod tabanlı otomasyon sağlar. Ajan davranışını yönlendiren talimatlardan veya özel promptlardan farklı olarak, hook'lar kodunuzu belirli yaşam döngüsü noktalarında garantili sonuçlarla çalıştırır:

* **Güvenlik politikalarını uygulayın**: Ajan ne şekilde yönlendirilirse yönlendirilsin `rm -rf` veya `DROP TABLE` gibi tehlikeli komutları yürütülmeden önce engelleyin.

* **Kod kalitesini otomatikleştirin**: Dosya değişikliklerinden sonra otomatik olarak biçimlendiriciler, linter'lar veya testler çalıştırın.

* **Denetim izleri oluşturun**: Uyumluluk ve hata ayıklama için her araç çağrısını, komut yürütmesini veya dosya değişikliğini günlüğe kaydedin.

* **Bağlam enjekte edin**: Ajanın daha iyi kararlar vermesine yardımcı olmak için proje özelinde bilgiler, API anahtarları veya ortam ayrıntıları ekleyin.

* **Onaylamaları kontrol edin**: Güvenli işlemleri otomatik olarak onaylarken hassas olanlar için onay gerektirin.

## Hook yaşam döngüsü olayları

VS Code, bir ajan oturumu sırasında belirli noktalarda tetiklenen sekiz hook olayını destekler:

| Hook Olayı | Ne Zaman Tetiklenir | Yaygın Kullanım Senaryoları |
|------------|---------------------|------------------------------|
| `SessionStart` | Kullanıcı yeni bir oturumun ilk promptunu gönderir | Kaynakları başlat, oturum başlangıcını günlüğe kaydet, proje durumunu doğrula |
| `UserPromptSubmit` | Kullanıcı bir prompt gönderir | Kullanıcı isteklerini denetle, sistem bağlamı enjekte et |
| `PreToolUse` | Ajan herhangi bir aracı çağırmadan önce | Tehlikeli işlemleri engelle, onay iste, araç girdisini değiştir |
| `PostToolUse` | Araç başarıyla tamamlandıktan sonra | Biçimlendiricileri çalıştır, sonuçları günlüğe kaydet, takip eylemlerini tetikle |
| `PreCompact` | Sohbet bağlamı sıkıştırılmadan önce | Önemli bağlamı dışa aktar, kesmeden önce durumu kaydet |
| `SubagentStart` | Alt ajan başlatıldığında | İç içe ajan kullanımını izle, alt ajan kaynaklarını başlat |
| `SubagentStop` | Alt ajan tamamlandığında | Sonuçları topla, alt ajan kaynaklarını temizle |
| `Stop` | Ajan oturumu sona erdiğinde | Raporlar oluştur, kaynakları temizle, bildirimler gönder |

## Hook'ları yapılandırma

Hook'lar çalışma alanınızda veya kullanıcı dizininizde depolanan JSON dosyalarında yapılandırılır.

### Hook dosya konumları

VS Code hook yapılandırma dosyalarını şu konumlarda arar:

* **Çalışma alanı**: `.github/hooks/*.json` - Ekibinizle paylaşılan proje özelinde hook'lar
* **Çalışma alanı**: `.claude/settings.local.json` - Yerel çalışma alanı hook'ları (işlenmez)
* **Çalışma alanı**: `.claude/settings.json` - Çalışma alanı düzeyinde hook'lar
* **Kullanıcı**: `~/.claude/settings.json` - Tüm çalışma alanlarına uygulanan kişisel hook'lar

Aynı olay türü için çalışma alanı hook'ları kullanıcı hook'larına göre önceliklidir.

Hangi hook dosyalarının yükleneceğini özelleştirmek için `setting(chat.hookFilesLocations)` ayarını kullanın. Klasörlere yollar belirtebilirsiniz (VS Code klasördeki tüm `*.json` dosyalarını yükler) veya tek tek `.json` dosyalarına doğrudan yollar belirtebilirsiniz. Yalnızca göreli yollar ve tilde (`~`) yolları desteklenir.

Varsayılan değer şu konumları içerir:

```json
"chat.hookFilesLocations": {
  ".github/hooks": true,
  ".claude/settings.local.json": true,
  ".claude/settings.json": true,
  "~/.claude/settings.json": true
}
```

Özel konumlar eklemek için bu ayara girdiler ekleyin:

```json
"chat.hookFilesLocations": {
  "custom/hooks": true,
  "~/my-hooks/security.json": true
}
```

Claude Code yapılandırma dosyalarından hook yüklemeyi durdurmak dahil, bir konumdan hook yüklemeyi devre dışı bırakmak için yolu `false` olarak ayarlayın:

```json
"chat.hookFilesLocations": {
  ".claude/settings.json": false,
  ".claude/settings.local.json": false,
  "~/.claude/settings.json": false
}
```

### Hook yapılandırma formatı

Her olay türü için hook komut dizileri içeren bir `hooks` nesnesi olan bir JSON dosyası oluşturun. VS Code uyumluluk için Claude Code ve Copilot CLI ile aynı hook formatını kullanır:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "./scripts/validate-tool.sh",
        "timeout": 15
      }
    ],
    "PostToolUse": [
      {
        "type": "command",
        "command": "npx prettier --write \"$TOOL_INPUT_FILE_PATH\""
      }
    ]
  }
}
```

### Hook komut özellikleri

Her hook girişinde `type: "command"` ve en az bir komut özelliği olmalıdır:

| Özellik | Tür | Açıklama |
|---------|-----|----------|
| `type` | string | `"command"` olmalı |
| `command` | string | Çalıştırılacak varsayılan komut (platformlar arası) |
| `windows` | string | Windows'a özel komut geçersiz kılma |
| `linux` | string | Linux'a özel komut geçersiz kılma |
| `osx` | string | macOS'a özel komut geçersiz kılma |
| `cwd` | string | Çalışma dizini (depo köküne göre) |
| `env` | object | Ek ortam değişkenleri |
| `timeout` | number | Saniye cinsinden zaman aşımı (varsayılan: 30) |

> [!NOTE]
> İşletim sistemi özelinde komutlar uzantı ana bilgisayar platformuna göre seçilir. Uzak geliştirme senaryolarında (SSH, Containers, WSL) bu, yerel işletim sisteminizden farklı olabilir.

### İşletim sistemi özelinde komutlar

Her işletim sistemi için farklı komutlar belirtin:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "type": "command",
        "command": "./scripts/format.sh",
        "windows": "powershell -File scripts\\format.ps1",
        "linux": "./scripts/format-linux.sh",
        "osx": "./scripts/format-mac.sh"
      }
    ]
  }
}
```

Yürütme hizmeti işletim sisteminize göre uygun komutu seçer. İşletim sistemi özelinde komut tanımlanmamışsa, `command` özelliğine geri döner.

## Hook girdisi ve çıktısı

Hook'lar VS Code ile stdin (girdi) ve stdout (çıktı) üzerinden JSON kullanarak iletişim kurar.

### Ortak girdi alanları

Her hook stdin üzerinden şu ortak alanlara sahip bir JSON nesnesi alır:

```json
{
  "timestamp": "2026-02-09T10:30:00.000Z",
  "cwd": "/path/to/workspace",
  "sessionId": "session-identifier",
  "hookEventName": "PreToolUse",
  "transcript_path": "/path/to/transcript.json"
}
```

### Ortak çıktı formatı

Hook'lar ajan davranışını etkilemek için stdout üzerinden JSON döndürebilir. Tüm hook'lar şu çıktı alanlarını destekler:

```json
{
  "continue": true,
  "stopReason": "Security policy violation",
  "systemMessage": "Unit tests failed"
}
```

| Alan | Tür | Açıklama |
|------|-----|----------|
| `continue` | boolean | İşlemeyi durdurmak için `false` yapın (varsayılan: `true`) |
| `stopReason` | string | `continue` `false` olduğunda durdurma nedeni (kullanıcıya gösterilir) |
| `systemMessage` | string | Kullanıcıya gösterilen uyarı mesajı |

### Çıkış kodları

Hook'un çıkış kodu VS Code'un sonucu nasıl işleyeceğini belirler:

| Çıkış Kodu | Davranış |
|------------|----------|
| `0` | Başarı: stdout'u JSON olarak ayrıştır |
| `2` | Engelleme hatası: işlemeyi durdur ve modele hatayı göster |
| Diğer | Engellemeyen uyarı: kullanıcıya uyarı göster, işlemeye devam et |

### Veri döndürme şeklini seçme

Hook'ların ajan davranışını kontrol etmek için birden fazla yolu vardır: çıkış kodları, üst düzey çıktı alanları (`continue`, `stopReason`) ve hook'a özel çıktı alanları (`hookSpecificOutput`). Bunları şu şekilde birlikte kullanın:

* **Çıkış kodu 2** bir işlemi engellemenin en basit yoludur. Hook'un stderr'i modele bağlam olarak gösterilir. JSON çıktısı gerekmez.
* **JSON çıktısında `continue: false`** tüm ajan oturumunu durdurur. Kullanıcıya nedenini söylemek için `stopReason` kullanın. Bu tek bir araç çağrısını engellemekten daha radikaldir.
* **`hookSpecificOutput`** her hook olayına özel ince ayarlı kontrol sağlar. Örneğin, `PreToolUse` hook'ları oturumu durdurmadan tek bir araç çağrısı için izin vermek, reddetmek veya onay istemek için `permissionDecision` kullanır.
* **`systemMessage`** diğer kararlardan bağımsız olarak kullanıcıya sohbette bir uyarı gösterir.

Birden fazla kontrol mekanizması birlikte kullanıldığında en kısıtlayıcı olan kazanır. Örneğin, bir hook `continue: false` ve `permissionDecision: "allow"` döndürse bile oturum yine de durur.

## PreToolUse

`PreToolUse` hook'u ajan bir aracı çağırmadan önce tetiklenir.

### PreToolUse girdisi

Ortak alanlara ek olarak, `PreToolUse` hook'ları şunları alır:

```json
{
  "tool_name": "editFiles",
  "tool_input": { "files": ["src/main.ts"] },
  "tool_use_id": "tool-123"
}
```

### PreToolUse çıktısı

`PreToolUse` hook'u, `hookSpecificOutput` nesnesi aracılığıyla araç yürütmesini kontrol edebilir:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "Destructive command blocked by policy",
    "updatedInput": { "files": ["src/safe.ts"] },
    "additionalContext": "User has read-only access to production files"
  }
}
```

| Alan | Değerler | Açıklama |
|------|----------|----------|
| `permissionDecision` | `"allow"`, `"deny"`, `"ask"` | Araç onayını kontrol eder |
| `permissionDecisionReason` | string | Kullanıcıya gösterilen neden |
| `updatedInput` | object | Değiştirilmiş araç girdisi (isteğe bağlı) |
| `additionalContext` | string | Model için ek bağlam |

**İzin kararı önceliği**: Aynı araç çağrısı için birden fazla hook çalıştığında, en kısıtlayıcı karar geçerlidir:
1. `deny` (en kısıtlayıcı): araç yürütmesini engeller
2. `ask`: kullanıcı onayı gerektirir
3. `allow` (en az kısıtlayıcı): yürütmeyi otomatik onaylar

**`updatedInput` formatı**: `updatedInput` formatını belirlemek için [ajan günlüklerini](/docs/copilot/chat/chat-debug-view.md#agent-logs) açın ve günlüğe kaydedilen araç şemasını bulun. `updatedInput` beklenen şemayla eşleşmezse yok sayılır.

## PostToolUse

`PostToolUse` hook'u bir araç başarıyla tamamlandıktan sonra tetiklenir.

### PostToolUse girdisi

Ortak alanlara ek olarak, `PostToolUse` hook'ları şunları alır:

```json
{
  "tool_name": "editFiles",
  "tool_input": { "files": ["src/main.ts"] },
  "tool_use_id": "tool-123",
  "tool_response": "File edited successfully"
}
```

### PostToolUse çıktısı

`PostToolUse` hook'u modele ek bağlam sağlayabilir veya sonraki işlemeyi engelleyebilir:

```json
{
  "decision": "block",
  "reason": "Post-processing validation failed",
  "hookSpecificOutput": {
    "hookEventName": "PostToolUse",
    "additionalContext": "The edited file has lint errors that need to be fixed"
  }
}
```

| Alan | Değerler | Açıklama |
|------|----------|----------|
| `decision` | `"block"` | Sonraki işlemeyi engelle (isteğe bağlı) |
| `reason` | string | Engelleme nedeni (modele gösterilir) |
| `hookSpecificOutput.additionalContext` | string | Sohbete enjekte edilen ek bağlam |

## UserPromptSubmit

`UserPromptSubmit` hook'u kullanıcı bir prompt gönderdiğinde tetiklenir.

### UserPromptSubmit girdisi

Ortak alanlara ek olarak, `UserPromptSubmit` hook'ları kullanıcının gönderdiği metni içeren bir `prompt` alanı alır.

`UserPromptSubmit` hook'u yalnızca ortak çıktı formatını kullanır.

## SessionStart

`SessionStart` hook'u yeni bir ajan oturumu başladığında tetiklenir.

### SessionStart girdisi

Ortak alanlara ek olarak, `SessionStart` hook'ları şunları alır:

```json
{
  "source": "new"
}
```

| Alan | Tür | Açıklama |
|------|-----|----------|
| `source` | string | Oturumun nasıl başlatıldığı. Şu anda her zaman `"new"`. |

### SessionStart çıktısı

`SessionStart` hook'u ajanın sohbetine ek bağlam enjekte edebilir:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Project: my-app v2.1.0 | Branch: main | Node: v20.11.0"
  }
}
```

| Alan | Tür | Açıklama |
|------|-----|----------|
| `additionalContext` | string | Ajanın sohbetine eklenen bağlam |

## Stop

`Stop` hook'u ajan oturumu sona erdiğinde tetiklenir.

### Stop girdisi

Ortak alanlara ek olarak, `Stop` hook'ları şunları alır:

```json
{
  "stop_hook_active": false
}
```

| Alan | Tür | Açıklama |
|------|-----|----------|
| `stop_hook_active` | boolean | Ajan önceki bir stop hook'u sonucunda zaten devam ediyorsa `true`. Ajanın süresiz çalışmasını önlemek için bu değeri kontrol edin. |

### Stop çıktısı

`Stop` hook'u ajanın durmasını engelleyebilir:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "Stop",
    "decision": "block",
    "reason": "Run the test suite before finishing"
  }
}
```

| Alan | Değerler | Açıklama |
|------|----------|----------|
| `decision` | `"block"` | Ajanın durmasını engelle |
| `reason` | string | Karar `"block"` olduğunda gerekli. Ajana neden devam etmesi gerektiğini söyler. |

> [!IMPORTANT]
> `Stop` hook'u ajanın durmasını engellediğinde ajan çalışmaya devam eder ve ek turlar [premium isteklerini](https://docs.github.com/en/copilot/managing-copilot/monitoring-usage-and-entitlements/about-premium-requests) tüketir. Ajanın süresiz çalışmasını önlemek için her zaman `stop_hook_active` alanını kontrol edin.

## SubagentStart

`SubagentStart` hook'u bir alt ajan başlatıldığında tetiklenir.

### SubagentStart girdisi

Ortak alanlara ek olarak, `SubagentStart` hook'ları şunları alır:

```json
{
  "agent_id": "subagent-456",
  "agent_type": "Plan"
}
```

| Alan | Tür | Açıklama |
|------|-----|----------|
| `agent_id` | string | Alt ajan için benzersiz tanımlayıcı |
| `agent_type` | string | Ajan adı (örneğin yerleşik ajanlar için `"Plan"` veya özel ajan adları) |

### SubagentStart çıktısı

`SubagentStart` hook'u alt ajanın sohbetine ek bağlam enjekte edebilir:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "SubagentStart",
    "additionalContext": "This subagent should follow the project coding guidelines"
  }
}
```

| Alan | Tür | Açıklama |
|------|-----|----------|
| `additionalContext` | string | Alt ajanın sohbetine eklenen bağlam |

## SubagentStop

`SubagentStop` hook'u bir alt ajan tamamlandığında tetiklenir.

### SubagentStop girdisi

Ortak alanlara ek olarak, `SubagentStop` hook'ları şunları alır:

```json
{
  "agent_id": "subagent-456",
  "agent_type": "Plan",
  "stop_hook_active": false
}
```

| Alan | Tür | Açıklama |
|------|-----|----------|
| `agent_id` | string | Alt ajan için benzersiz tanımlayıcı |
| `agent_type` | string | Ajan adı (örneğin yerleşik ajanlar için `"Plan"` veya özel ajan adları) |
| `stop_hook_active` | boolean | Alt ajan önceki bir stop hook'u sonucunda zaten devam ediyorsa `true`. Alt ajanın süresiz çalışmasını önlemek için bu değeri kontrol edin. |

### SubagentStop çıktısı

`SubagentStop` hook'u alt ajanın durmasını engelleyebilir:

```json
{
  "decision": "block",
  "reason": "Verify subagent results before completing"
}
```

| Alan | Değerler | Açıklama |
|------|----------|----------|
| `decision` | `"block"` | Alt ajanın durmasını engelle |
| `reason` | string | Karar `"block"` olduğunda gerekli. Alt ajana neden devam etmesi gerektiğini söyler. |

## PreCompact

`PreCompact` hook'u sohbet bağlamı sıkıştırılmadan önce tetiklenir.

### PreCompact girdisi

Ortak alanlara ek olarak, `PreCompact` hook'ları şunları alır:

```json
{
  "trigger": "auto"
}
```

| Alan | Tür | Açıklama |
|------|-----|----------|
| `trigger` | string | Sıkıştırmanın nasıl tetiklendiği. Sohbet prompt bütçesi için çok uzun olduğunda `"auto"`. |

`PreCompact` hook'u yalnızca ortak çıktı formatını kullanır.

## UI ile hook'ları yapılandırma

Hook'ları birkaç yolla etkileşimli bir UI üzerinden yapılandırabilirsiniz:

* Sohbet girişine `/hooks` yazın ve `kbstyle(Enter)` tuşuna basın.
* Komut Paleti'ni (`kb(workbench.action.showCommands)`) açın ve **Chat: Configure Hooks** çalıştırın.
* Sohbet görünümünün üst kısmındaki **Settings** simgesini (<i class="codicon codicon-gear"></i>) seçin, ardından **Hooks** seçin.

Hook yapılandırma menüsünde:

1. Listeden bir hook olay türü seçin.

1. Düzenlemek için mevcut bir hook seçin veya yeni bir tane oluşturmak için **Add new hook** seçin.

1. Bir hook yapılandırma dosyası seçin veya oluşturun.

Komut, düzenlemeye hazır imleciniz komut alanında konumlandığı halde hook dosyasını editörde açar.

### AI ile hook oluşturma

AI kullanarak hook yapılandırması oluşturabilirsiniz. Sohbete `/create-hook` yazın ve istediğiniz otomasyonu açıklayın (örneğin, "her dosya düzenlemesinden sonra ESLint çalıştır"). Ajan açıklayıcı sorular sorar ve uygun olay türü, komut ve ayarlarla bir hook yapılandırma dosyası oluşturur.

## Kullanım senaryoları

Aşağıdaki örnekler yaygın hook desenlerini gösterir.

<details>
<summary>Tehlikeli terminal komutlarını engelle</summary>

Yıkıcı komutları önleyen bir `PreToolUse` hook'u oluşturun:

**.github/hooks/security.json**:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "./scripts/block-dangerous.sh",
        "timeoutSec": 5
      }
    ]
  }
}
```

**scripts/block-dangerous.sh**:
```bash
#!/bin/bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')
TOOL_INPUT=$(echo "$INPUT" | jq -r '.tool_input')

if [ "$TOOL_NAME" = "runTerminalCommand" ]; then
  COMMAND=$(echo "$TOOL_INPUT" | jq -r '.command // empty')

  if echo "$COMMAND" | grep -qE '(rm\s+-rf|DROP\s+TABLE|DELETE\s+FROM)'; then
    echo '{"hookSpecificOutput":{"permissionDecision":"deny","permissionDecisionReason":"Destructive command blocked by security policy"}}'
    exit 0
  fi
fi

echo '{"continue":true}'
```

</details>

<details>
<summary>Düzenlemelerden sonra kodu otomatik biçimlendir</summary>

Herhangi bir dosya değişikliğinden sonra Prettier'ı otomatik çalıştırın:

**.github/hooks/formatting.json**:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "type": "command",
        "command": "./scripts/format-changed-files.sh",
        "windows": "powershell -File scripts\\format-changed-files.ps1",
        "timeout": 30
      }
    ]
  }
}
```

**scripts/format-changed-files.sh**:
```bash
#!/bin/bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')

if [ "$TOOL_NAME" = "editFiles" ] || [ "$TOOL_NAME" = "createFile" ]; then
  FILES=$(echo "$INPUT" | jq -r '.tool_input.files[]? // .tool_input.path // empty')

  for FILE in $FILES; do
    if [ -f "$FILE" ]; then
      npx prettier --write "$FILE" 2>/dev/null
    fi
  done
fi

echo '{"continue":true}'
```

</details>

<details>
<summary>Denetim için araç kullanımını günlüğe kaydet</summary>

Tüm araç çağrılarının denetim izi oluşturun:

**.github/hooks/audit.json**:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "./scripts/log-tool-use.sh",
        "env": {
          "AUDIT_LOG": ".github/hooks/audit.log"
        }
      }
    ]
  }
}
```

**scripts/log-tool-use.sh**:
```bash
#!/bin/bash
INPUT=$(cat)
TIMESTAMP=$(echo "$INPUT" | jq -r '.timestamp')
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')
SESSION_ID=$(echo "$INPUT" | jq -r '.sessionId')

echo "[$TIMESTAMP] Session: $SESSION_ID, Tool: $TOOL_NAME" >> "${AUDIT_LOG:-audit.log}"
echo '{"continue":true}'
```

</details>

<details>
<summary>Belirli araçlar için onay gerektir</summary>

Altyapıyı değiştiren araçlar için manuel onay zorunlu kılın:

**.github/hooks/approval.json**:
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "command",
        "command": "./scripts/require-approval.sh"
      }
    ]
  }
}
```

**scripts/require-approval.sh**:
```bash
#!/bin/bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')

# Tools that should always require approval
SENSITIVE_TOOLS="runTerminalCommand|deleteFile|pushToGitHub"

if echo "$TOOL_NAME" | grep -qE "^($SENSITIVE_TOOLS)$"; then
  echo '{"hookSpecificOutput":{"permissionDecision":"ask","permissionDecisionReason":"This operation requires manual approval"}}'
else
  echo '{"hookSpecificOutput":{"permissionDecision":"allow"}}'
fi
```

</details>

<details>
<summary>Oturum başında proje bağlamı enjekte et</summary>

Oturum başladığında proje özelinde bilgi sağlayın:

**.github/hooks/context.json**:
```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "command",
        "command": "./scripts/inject-context.sh"
      }
    ]
  }
}
```

**scripts/inject-context.sh**:
```bash
#!/bin/bash
PROJECT_INFO=$(cat package.json 2>/dev/null | jq -r '.name + " v" + .version' || echo "Unknown project")
BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")

cat <<EOF
{
  "hookSpecificOutput": {
    "hookEventName": "SessionStart",
    "additionalContext": "Project: $PROJECT_INFO | Branch: $BRANCH | Node: $(node -v 2>/dev/null || echo 'not installed')"
  }
}
EOF
```

</details>

## Güvenlik

Ajanın hook'lar tarafından çalıştırılan betikleri düzenleme erişimi varsa, kendi çalışması sırasında bu betikleri değiştirme ve yazdığı kodu yürütme yeteneğine sahiptir. Ajanın manuel onay olmadan hook betiklerini düzenlemesini engellemek için `chat.tools.edits.autoApprove` kullanmanızı öneririz.

## Sorun giderme

### Hook tanılamalarını görüntüleme

Hangi hook'ların yüklendiğini görmek ve yapılandırma hatalarını kontrol etmek için:

1. Tüm günlükleri görüntülemek için **View Logs** seçin.

1. Yüklenen hook'ları ve hangi konumlardan yüklendiklerini görmek için "Load Hooks" arayın.

### Hook çıktısını görüntüleme

Hook çıktısını ve hatalarını incelemek için:

1. **Output** panelini açın.

1. Kanal listesinden **GitHub Copilot Chat Hooks** seçin.

### Yaygın sorunlar

**Hook çalışmıyor**: Hook dosyasının `.github/hooks/` içinde olduğunu ve `.json` uzantısına sahip olduğunu doğrulayın. `type` özelliğinin `"command"` olarak ayarlandığını kontrol edin.

**İzin reddedildi hataları**: Hook betiklerinizin yürütme izinlerine sahip olduğundan emin olun (`chmod +x script.sh`).

**Zaman aşımı hataları**: `timeout` değerini artırın veya hook betiğinizi optimize edin. Varsayılan 30 saniyedir.

**JSON ayrıştırma hataları**: Hook betiğinizin stdout'a geçerli JSON çıktıladığını doğrulayın. Çıktı oluşturmak için `jq` veya bir JSON kitaplığı kullanın.

## Sık sorulan sorular

### VS Code Claude Code hook yapılandırmalarını nasıl işler?

VS Code varsayılan olarak `.claude/settings.json`, `.claude/settings.local.json` ve `~/.claude/settings.json` dosyalarından hook yapılandırmalarını okur. VS Code, eşleştirici sözdizimi dahil Claude Code'un hook yapılandırma formatını ayrıştırır. Şu anda VS Code eşleştirici değerlerini yok sayar, bu nedenle hook'lar eşleştiriciden bağımsız olarak tüm araç çağrılarında çalışır.

Claude Code hook'unu VS Code için uyarlıyorsanız, aşağıdaki farkların farkında olun:

* **Araç girdisi özellik adları**: Claude Code araç girdisi özellikleri için snake_case kullanır (örneğin `tool_input.file_path`), oysa VS Code araçları camelCase kullanır (örneğin `tool_input.filePath`). Hook betiklerinizi doğru özellik adlarını okuyacak şekilde güncelleyin.
* **Araç adları**: Claude Code ve VS Code farklı araç adları kullanır. Örneğin Claude Code dosya işlemleri için `Write` ve `Edit` kullanır, oysa VS Code `create_file` ve `replace_string_in_file` gibi araç adları kullanır. `tool_name` girdi alanındaki araç adını kontrol edin ve hook mantığınızı buna göre güncelleyin.
* **Eşleştiriciler yok sayılır**: `"Edit|Write"` gibi hook eşleştiricileri ayrıştırılır ancak uygulanmaz. Tüm hook'lar eşleştiricideki araç adından bağımsız olarak her eşleşen olayda çalışır.

### VS Code Copilot CLI hook yapılandırmalarını nasıl işler?

VS Code Copilot CLI hook yapılandırmalarını ayrıştırır ve altCamelCase hook olay adlarını (örneğin `preToolUse`) VS Code tarafından kullanılan PascalCase formatına (`PreToolUse`) dönüştürür. `bash` ve `powershell` komut özellikleri işletim sistemi özelinde komutlara eşlenir: `powershell` `windows` ile, `bash` `osx` ve `linux` ile eşlenir.

## Güvenlik hususları

> [!CAUTION]
> Hook'lar VS Code ile aynı izinlerle kabuk komutları çalıştırır. Özellikle güvenilmeyen kaynaklardan hook kullanırken hook yapılandırmalarını dikkatle inceleyin.

* **Hook betiklerini inceleyin**: Özellikle paylaşılan depolarında etkinleştirmeden önce tüm hook betiklerini inceleyin.

* **Hook izinlerini sınırlayın**: En az ayrıcalık ilkesini uygulayın. Hook'ların yalnızca ihtiyaç duydukları erişime sahip olmalıdır.

* **Girdiyi doğrulayın**: Hook betikleri ajandan girdi alır. Enjeksiyon saldırılarını önlemek için tüm girdiyi doğrulayın ve temizleyin.

* **Kimlik bilgilerini güvence altına alın**: Asla gizli bilgileri hook betiklerinde sabit olarak kodlamayın. Ortam değişkenleri veya güvenli kimlik bilgisi depolaması kullanın.

## İlgili kaynaklar

* [Ajanlarla araçları kullanma](/docs/copilot/agents/agent-tools.md) - Araç onayı ve yürütmeyi öğrenin
* [Özel ajanlar](/docs/copilot/customization/custom-agents.md) - Uzmanlaşmış ajan yapılandırmaları oluşturun
* [Alt ajanlar](/docs/copilot/agents/subagents.md) - Görevleri bağlam izole alt ajanlara devredin
* [Güvenlik hususları](/docs/copilot/security.md) - VS Code'da AI güvenliği için en iyi uygulamalar
