---
name: calisma-kagidi
description: Her bölüm ve alandan ders slaytlarından/notlarından (pptx, pdf, docx, fotoğraf, el yazısı tarama) sınav odaklı çalışma kağıdı PDF'i hazırlar; test, klasik, matematik, programlama ve sınav öncesi hızlı tekrar biçimleri var. Kullanıcı ya da arkadaşları için "çalışma kağıdı", "vize/final notu", "bu dersin özetini çıkar", "hızlı tekrar" dendiğinde kullan.
---

# Çalışma kağıdı hazırlama

## Amaç
Slaytları **öğretmek**: sade, öz, net ve akılda kalıcı. Kağıt bir kalıptan değil, konunun kendisinden çıkar. Her bölümde şu sorulur: *"Bu konu en iyi nasıl öğrenilir?"* Cevap tanımsa düz anlatım, süreçse adımlar, işlemse çözüm, karşılaştırmaysa yan yana tablo, keyfi bir listeyse ezber aracı olur.

Araçlar ve süzgeç **yardımcıdır, kural değildir**. Kağıt bir kurala uyduğu için doğru sayılmaz; öğretiyorsa doğrudur. Kullanıcı 12 Kasım 2026'da ince kuralların (kod uzunluğu, kutu sayısı gibi sayısal sınırlar) kaldırılmasını istedi: karar her seferinde içeriğe bakılarak verilir.

## İlkeler
1. **Öğret, listeleme.** Slayttaki her şey anlatımla verilir. Ezber araçları anlatımın yerine geçmez, onu destekler.
2. **Görünüm: orijinal kutulu format (varsayılan).** Kullanıcı 12 Kas'ta kutusuz sade görünümü (`SADE_CSS`) denedi: "çok ayrık oldu, karmaşık duruyor, kutular olsun; önceki versiyonlar iyiydi". MTH201'de kutuların çoğalması kullanıcının kendi yönlendirmelerinden kaynaklandı; orijinal formatlar beğeniliyor. `SADE_CSS` sadece istenirse kullanılır.
3. **Öz.** Her fikir önce tek net cümleyle söylenir, ayrıntı ve örnek altında gelir. MTH201'de kullanıcının öğrenmesini belirgin şekilde iyileştiren yapı buydu.
4. **Anlam, ezberden önce.** Bir şeyin nedeni biliniyorsa yazılır. Sıra mantıkla ilerliyorsa mantığı gösterilir; ancak gerçekten keyfi olanlar ezber aracıyla verilir.
5. **Konuya göre biçim.** Aynı kağıtta farklı bölümler farklı anlatılabilir. Numara sadece gerçekten sıralı şeylerde kullanılır.
6. **Sınava dönük.** Kağıt sınav biçimine göre kurulur. Biçim bilinmiyorsa kullanıcıya sorulur.

## Kullanıcının beğendikleri / beğenmedikleri (somut örnekler, kural değil)
- **Beğendi:**
  - MTH201'in son hali: başta "Başlangıçta elimizde", sonra her adımda tek cümle ve altında bütün ara işlemler.
  - "Bu bölümde" girişi, öz cümle + girintili ayrıntı akışı.
  - Altı çizili önemli yerler.
  - İngilizce terimin yanında parantez içinde Türkçesi.
  - A2/A1 kısa İngilizce cevaplar.
  - Kodlama, katla-test, ezber kartları, aralıklı tekrar çizelgesi.
  - Sıralı listelerde mantık zinciri.
  - "**An**·ası **mez**·ar **dik**·ecek·miş" gibi kısa ve anlamlı kodlar, "Ön Kabin" gibi.
- **Beğenmedi:**
  - kutusuz sade görünüm: "çok ayrık, karmaşık" (12 Kas)
  - adım adım ayrı "Elimizde / Neden?" blokları
  - her fikri 1-2-3 diye numaralamak
  - sadece ezbere dönük kağıt
  - uzun cümle kodlar
  - anlamsız harf ya da hece kodları (KPBİ, ŞİÜS, PaKU: "ilk harflerden aklıma gelmiyor")
  - bütün slaytları tek düz kalıba dökmek

## Çalışma şekli
1. **Kaynağı oku ve tanı.** Yardımcı olarak süzgeç çalıştırılabilir:
   ```
   python3 -I ~/.claude/skills/calisma-kagidi/scripts/analiz.py "<ders klasörü>" --out <scratch>/<ders>
   ```
   Rapor (`analiz.md`) şunları ön bilgi olarak verir:
   - konuların ağırlığı
   - her bölümün baskın içeriği (tanım, süreç, işlem, kod, karşılaştırma, ezber yükü)
   - tanımından önce kullanılan terimler
   - lab, izlence ya da çıkmış sorulardan sınav biçimi ipucu

   Rapor sezgiseldir; kararı slaytı okuyarak sen verirsin. Her dosya okunur (`kaynak.txt`). Resimli ve taranmış sayfalar Read ya da `montaj.py` ile görüntüden okunur.
2. **Her bölüm için öğretim kararı ver:** bu konu en iyi nasıl öğrenilir? Ağır konuya daha çok yer ve soru, hafif konuya kısa anlatım düşer.
3. **Yaz.** İstenirse `yeni.py` boş bir çatı kurar (`--plan plan.json` ya da `--alan/--dil/--sinav/--ezber/--hizli`). Çatı sadece başlangıçtır; yer tutucular konuya göre değiştirilir ya da silinir.
4. **Teslim öncesi denetim (her kağıtta, ATLANMAZ).** Kullanıcı kağıtların çoğunu okumadan arkadaşlarına gönderecek; gözüne batanı söyleme şansı olmayacak (12 Kas). Kalite kontrolü bu yüzden teslimden önce burada yapılır:
   - **Otomatik:**
     ```
     python3 -I scripts/denetim.py --kagit <build'in yazdığı .html> --kaynak <kaynak.txt | transkript.md | dosyalar> --out <scratch>/denetim.md
     ```
     Şunları listeler: kaynakta olup kağıtta olmayan sayı/yıl/madde/birimli değer; karşılığı zayıf başlık (atlanmış konu); cevabı anlatımda geçmeyen soru; uzun paragraf; kutu yoğun bölüm. Her maddeyi değerlendir: gerçek eksikse düzelt, önemsizse geç.
   - **Öğrenci gözüyle okuma:** `preview.py` ile bütün sayfaları, konuyu ilk kez gören biri gibi oku:
     - tanımsız terim
     - "bu konu ne?" sorusunu cevaplamayan bölüm girişi
     - yük olan ezber aracı
     - kağıttan cevaplanamayan soru
     - yazım ya da özel ad hatası
   - Düzeltip yeniden derle; denetimi temiz bitir. Kullanıcıya sadece kısa sonucu söyle (ör. "denetim: 2 eksik sayı eklendi, 1 soru değişti").
5. **Kullanıcı yönlendirirse** her zaman ilkelerden önce gelir. Yönlendirme yoksa karar ilkeler ve onaylı örneklere göre verilir; denetim bunun güvencesidir.

## Araç kutusu (`scripts/`)
- **Okuma:**
  - `extract.py`: pptx/pdf/docx metni
  - `montaj.py`: taranmış ve el yazısı sayfalar
  - `render_pages.py`
- **Ölçme, çatı, denetim:** `analiz.py` (süzgeç), `yeni.py` (iskelet), `denetim.py` (teslim öncesi kapsam, soru ve okunabilirlik kontrolü)
- **Kağıt:** `kagit.py` (`Kagit`, `cover`, `h2/h3`, `KAV`, `TRAP`, `TIP`, `TABLE`, `EXAM`, `SLIDE/Q`, `summary`, `build(pdf, copy_to=…, open_pdf=True)`). `copy_to` Preview'daki eski dosyayı kapatıp üstüne yazar ve doğrular.
- **`eklentiler.py`:**
  - **Anlatım:**
    - `SADE_CSS`: kutusuz görünüm, SADECE istenirse (varsayılan değil)
    - `bu_bolumde(...)`, `akis([(öz, [ayrıntı, 'Örnek: …'])], sirali=False)`, `anlat(...)`
    - `mantik_zinciri(baslik, [(adım, 'neden sonrakine geçilir')], ozet)`
  - **İşlem:**
    - `MAT_CSS` + `cozum(baslik, denklem, yontem, [(cümle, [ara işlemler])], sonuc)`
    - `fr()`, `kesir.py` (a/b'leri kesir çizgili yapar)
  - **Kod:** `kod(src, cikti)`
  - **Kronoloji:** `zaman_cizelgesi`
  - **Ezber:**
    - `kodlama(baslik, maddeler, kod='[Ön] [Ka][B][İn]', hikaye, sira_onemli)`; yardımcısı `parca_onerileri()` (ilk heceler)
    - `katla_test`, `ezber_kartlari` (çift taraflı, aynalı), `tekrar_cizelgesi` (öğren/+1/+3/+7)
  - **Sınav:**
    - `EXAM` (test, cevap hemen altında), `testsiz(k)`
    - `klasik_tr`, `klasik_kutu` (İngilizce soru + 🔑 terimler + A2 cevap + Türkçesi)
    - `dogru_yanlis`, `bosluk_doldurma`, `eslestirme`
  - **İngilizce ders:** `T(en, tr)`, `cift_dil_kav`, `vurgu(k, {'1': [...]})` (altı çizili; build'den hemen önce)
- **Şema:** `diyagram.py` (DFD, ağaç, Venn, `fig` + "nasıl çizilir"). Görsel varsayılan değildir, gerekince kullanılır.

## Token tasarrufu (kullanıcının kotası sınırlı, 13 Kas 2026: "şemayla çok uğraşıyorsun, token'ım yok")
- **Şema/çizim varsayılan olarak YOK.** Sadece gerçekten öğretmeyi değiştirecekse ve ucuzsa (`CHAIN` gibi hazır kutular). SVG çizip tekrar tekrar düzeltme. Slayttaki görselleri kopyalamak zorunlu değil.
- **Önce metin katmanı:** `extract.py` / `analiz.py` çıktısı yeterliyse görüntü okuma. Sadece metni olmayan (görsel slayt) dosyalarda görüntüye bak: 4'lü montaj, ~85 dpi, dosya başına bir kez; okurken notları hemen `notlar_*.md`'ye yaz.
- **Önizleme az:** yeni bir öğe tipi için bir kez, kırpılmış küçük görüntüyle. Bütün kağıdı tekrar tekrar render etme.
- **Büyük kaynakları parça parça okuma yerine** sıkıştırılmış metni (boşlukları silinmiş) bir kerede oku.
- Denetim (`denetim.py`) İngilizce soru + Türkçe anlatımda "öğretilmemiş soru" için yanlış alarm verir (acidic ↔ asidik). Listeyi hızlıca gözden geçir, kağıdı yeniden üretme.

## Örnek proje
- `ornekler/tibbi_biyoloji/`: kullanıcının arkadaşı için (İngilizce okuyan tıp 1. sınıf, İngilizcesi zayıf) Tıbbi Biyoloji kağıdı. Türkçe anlatım + İngilizce terim (Türkçesi parantezde), İngilizce test soruları + Türkçe açıklama + yeşil kelime çipleri, 28 bölüm, 203 soru, 122 sayfa. Modüler yapı: `build_tb.py` + bölüm başına `s_*.py` + `ortak.py` (E/T yardımcıları) + `gl.py` (sözlük). Yeni bir İngilizce tıp/fen dersi için şablon olarak kullan.

## Değişmeyen pratik notlar
- Sayıları, yılları, madde numaralarını ve birimleri silme; sadece slayt ya da sayfa numarasını at.
- Cevaplar her soru bölümünün hemen altında olur, en sonda değil. Sorular slayt örneğinin birebir kopyası olmaz.
- Kaynakta olmayan bilgi "genel bilgi" diye işaretlenir.
- Arkadaş kağıtları şahıssız dille yazılır ve kullanıcının "arkadaş kağıtları" klasörüne (hafızada) gider. Defterdeki ⭐ ve "X Hoca" notları belirtilir.
- Kullanıcının İngilizce derslerinde terimler İngilizce, yanında Türkçesi olur; cevaplar basit İngilizce ve tam Türkçe çeviriyle verilir.
- Matematikte:
  - hazır formül yerine yöntemin kendisiyle çözülür, formül en sonda not olur
  - o derste zorlanılan temel işlemlere (ör. integral kalıpları) ayrı bölüm konabilir
  - çözümler sayfada bölünmez
- Kısa tablolar (≤10 satır) `TABLE` içinde otomatik olarak sayfada bölünmez (12 Kas: "tablo arka sayfaya akmış"); uzun tablolar boş sayfa bırakmasın diye bölünebilir. Önizlemede bölünen kısa blok görürsen düzelt.
- Keynote/PowerPoint gibi pencere açan uygulama kullanılmaz.
- Besmele, hayrat ve Fatiha satırı (`hayrat()`) sadece kullanıcı isterse eklenir.
- Kullanıcıya gündelik Türkçe ("kanki") ve kısa cevap verilir; PDF yolu ve sayfa sayısı söylenir.
