#!/usr/bin/env python3
"""40 günlük mail, her birinde 3 ipucu. Toplam 120 ipucu. Temel→ileri progresif sıra."""
import os

from mail_data import MAILS

IMG_BASE = "https://raw.githubusercontent.com/erhankaraarslan/ai_guide_vscode/main/tr/docs/copilot/images"
BASE = "https://code.visualstudio.com"

# MAILS mail_data.py'den import ediliyor (40 mail, 1-10 Başlangıç, 11-20 Temel, 21-30 Orta, 31-40 İleri)



THEMES = {
    "indigo": ("#4f46e5", "#4338ca", "#3730a3", "#c7d2fe", "#f5f3ff"),
    "amber": ("#f59e0b", "#d97706", "#b45309", "#fde68a", "#fffbeb"),
    "violet": ("#7c3aed", "#6d28d9", "#5b21b6", "#c4b5fd", "#f5f3ff"),
    "cyan": ("#06b6d4", "#0891b2", "#0e7490", "#67e8f9", "#ecfeff"),
    "emerald": ("#10b981", "#059669", "#047857", "#6ee7b7", "#ecfdf5"),
    "rose": ("#f43f5e", "#e11d48", "#be123c", "#fda4af", "#fff1f2"),
    "sky": ("#0ea5e9", "#0284c7", "#0369a1", "#7dd3fc", "#f0f9ff"),
    "orange": ("#f97316", "#ea580c", "#c2410c", "#fdba74", "#fff7ed"),
    "lime": ("#84cc16", "#65a30d", "#4d7c0f", "#bef264", "#f7fee7"),
    "fuchsia": ("#d946ef", "#c026d3", "#a21caf", "#f0abfc", "#fdf4ff"),
    "blue": ("#3b82f6", "#2563eb", "#1d4ed8", "#93c5fd", "#eff6ff"),
    "slate": ("#64748b", "#475569", "#334155", "#cbd5e1", "#f8fafc"),
    "red": ("#ef4444", "#dc2626", "#b91c1c", "#fca5a5", "#fef2f2"),
    "green": ("#22c55e", "#16a34a", "#15803d", "#86efac", "#f0fdf4"),
    "purple": ("#a855f7", "#9333ea", "#7e22ce", "#d8b4fe", "#faf5ff"),
    "teal": ("#14b8a6", "#0d9488", "#0f766e", "#5eead4", "#f0fdfa"),
}


def gen_mail(mail_data, theme_colors):
    c1, c2, c3, clight, cbglt = theme_colors
    img_url = f"{IMG_BASE}/{mail_data['img']}"
    cta_full = BASE + mail_data["cta_url"] if mail_data["cta_url"].startswith("/") else mail_data["cta_url"]

    tips_html = ""
    for i, tip in enumerate(mail_data["tips"], 1):
        how_html = ""
        if tip.get("how"):
            steps = "\n".join(f'<li style="margin: 4px 0;">{s}</li>' for s in tip["how"])
            how_html = f'''
                    <p style="margin: 12px 0 6px; font-size: 12px; font-weight: 600; color: #64748b; text-transform: uppercase;">Nasıl yapılır:</p>
                    <ol style="margin: 0; padding-left: 20px; font-size: 13px; line-height: 1.7; color: #475569;">{steps}</ol>'''
        example_html = ""
        if tip.get("example"):
            example_html = f'''
                    <div style="margin-top: 12px; padding: 12px; background: #f8fafc; border-radius: 6px; border-left: 3px solid {c1};">
                      <p style="margin: 0 0 4px; font-size: 12px; font-weight: 600; color: #64748b;">Deneyebileceğiniz örnek:</p>
                      <p style="margin: 0; font-size: 13px; line-height: 1.6; color: #334155; font-style: italic;">{tip["example"]}</p>
                    </div>'''
        source_html = ""
        if tip.get("source"):
            s = tip["source"]
            source_html = f'''
                    <p style="margin-top: 10px; font-size: 12px; color: #64748b;">Kaynak: <a href="{s['url']}" style="color: {c1}; text-decoration: none;">{s['name']}</a></p>'''
        tips_html += f'''
              <table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="margin: 20px 0 0; border: 1px solid #e2e8f0; border-radius: 8px; overflow: hidden;">
                <tr>
                  <td style="padding: 16px 20px; background: #fafafa; border-bottom: 1px solid #e2e8f0;">
                    <strong style="font-size: 14px; color: {c1};">İpucu {i}</strong>
                  </td>
                </tr>
                <tr>
                  <td style="padding: 16px 20px;">
                    <p style="margin: 0 0 8px; font-size: 15px; font-weight: 600; color: #1e293b;">{tip["title"]}</p>
                    <p style="margin: 0; font-size: 14px; line-height: 1.6; color: #475569;">{tip["content"]}</p>{how_html}{example_html}{source_html}
                  </td>
                </tr>
              </table>'''

    return f'''<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Copilot Günlük İpucu #{mail_data["id"]}</title>
</head>
<body style="margin: 0; padding: 0; background-color: {cbglt}; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="background-color: {cbglt};">
    <tr>
      <td align="center" style="padding: 32px 16px;">
        <table role="presentation" cellpadding="0" cellspacing="0" width="600" style="max-width: 600px; background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 24px rgba(0,0,0,0.06); overflow: hidden;">
          <tr>
            <td style="padding: 32px 32px 24px; background: linear-gradient(135deg, {c1} 0%, {c2} 50%, {c3} 100%);">
              <span style="font-size: 12px; color: {clight}; text-transform: uppercase; letter-spacing: 1.5px; font-weight: 600;">GitHub Copilot</span>
              <h1 style="margin: 8px 0 0; font-size: 24px; font-weight: 700; color: #ffffff;">Günlük İpucu #{mail_data["id"]}</h1>
              <p style="margin: 4px 0 0; font-size: 14px; color: {clight};">{mail_data["subtitle"]}</p>
            </td>
          </tr>
          <tr>
            <td style="padding: 32px;">
              <h2 style="margin: 0 0 16px; font-size: 18px; font-weight: 600; color: #1e293b;">{mail_data["title"]}</h2>
              <table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="margin: 24px 0;">
                <tr>
                  <td style="border-radius: 8px; overflow: hidden; border: 1px solid #e2e8f0;">
                    <img src="{img_url}" alt="{mail_data["title"]}" width="536" style="display: block; max-width: 100%; height: auto; width: 100%;" />
                  </td>
                </tr>
              </table>
{tips_html}
              <table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="margin-top: 28px;">
                <tr>
                  <td>
                    <a href="{cta_full}" style="display: inline-block; padding: 12px 24px; background: {c1}; color: #ffffff !important; text-decoration: none; font-size: 14px; font-weight: 600; border-radius: 8px;">{mail_data["cta"]} →</a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>
          <tr>
            <td style="padding: 24px 32px; background: #f8fafc; border-top: 1px solid #e2e8f0;">
              <p style="margin: 0; font-size: 12px; color: #64748b;">VS Code Copilot, GitHub Docs, GitHub Blog ve GitHub Trust Center içeriklerinden derlenmiştir.</p>
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>
</body>
</html>'''


def main():
    os.makedirs("ipucu-mailler", exist_ok=True)
    for mail in MAILS:
        theme = THEMES.get(mail["theme"], THEMES["blue"])
        html = gen_mail(mail, theme)
        safe_sub = "-".join(s for s in "".join(c if c.isalnum() else "-" for c in mail["subtitle"].lower()).split("-") if s)[:35]
        path = f"ipucu-mailler/ipucu-{mail['id']:02d}-{safe_sub}.html"
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created {path}")
    print(f"\nToplam {len(MAILS)} günlük mail oluşturuldu. Her mailde 3 ipucu.")

if __name__ == "__main__":
    main()
