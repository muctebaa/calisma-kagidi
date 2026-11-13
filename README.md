# Çalışma Kağıdı

Ders slaytlarından ve notlarından (pptx, pdf, docx, el yazısı tarama) **sınav odaklı çalışma kağıdı PDF'i** üreten bir Claude Code skill'i ve Python araçları.

- Kağıt kalıptan değil kaynaktan kurulur: önce slaytlar ölçülür (`analiz.py`), sonra her bölüm en iyi nasıl öğretilecekse öyle yazılır.
- Test, klasik, doğru-yanlış, boşluk doldurma, eşleştirme; matematik için adım adım çözüm; programlama için kod + çıktı.
- İngilizce dersler için: Türkçe anlatım, İngilizce terim (Türkçesi parantezde), sorulardaki kelimelerin anlamı.
- Ezber araçları: kısa ve anlamlı kodlama, mantık zinciri, katla-test, kesilebilir ezber kartları, aralıklı tekrar çizelgesi.
- Teslim öncesi denetim (`denetim.py`): kaynakta olup kağıtta olmayan sayı ve başlıkları, kağıtta anlatılmayan bir şeyi soran soruları bulur.

## Yapı
| Yol | Ne? |
|---|---|
| `SKILL.md` | Claude için kurallar: amaç, ilkeler, çalışma şekli, araç kutusu |
| `scripts/kagit.py` | `Kagit` sınıfı: kutular, sorular, kapak, özet, HTML → PDF (headless Chrome) |
| `scripts/eklentiler.py` | anlatım akışı, matematik çözüm formatı, klasik soru, ezber araçları, sade görünüm |
| `scripts/analiz.py` | süzgeç: kaynağı ölçer, plan çıkarır |
| `scripts/yeni.py` | plana ya da ayarlara göre kağıt iskeleti |
| `scripts/denetim.py` | teslim öncesi kapsam ve soru kontrolü |
| `scripts/extract.py`, `montaj.py`, `preview.py` | metin çıkarma, taranmış sayfa okuma, önizleme |
| `ornekler/tibbi_biyoloji/` | örnek: İngilizce okutulan Tıbbi Biyoloji dersi (28 bölüm, 203 soru) |

## Kullanım
Skill'i `~/.claude/skills/calisma-kagidi/` altına koy; Claude Code'da "şu ders için çalışma kağıdı hazırla, klasör şu" demek yeterli.
Elle: `python3 scripts/analiz.py <ders klasörü> --out <iş klasörü>` → `python3 scripts/yeni.py <iş klasörü>/kagit --ders "Ders" --cikti <pdf klasörü> --plan <iş klasörü>/plan.json`

Gereksinimler: Python 3, Google Chrome, `pypdf`, `pymupdf`, `Pillow`.
