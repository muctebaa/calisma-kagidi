"""Her bölüm/alan için çalışma kağıdı iskeleti üretir (örnek içerikle, doğrudan derlenir).

    python3 yeni.py <iş_klasörü> --ders "Ders Adı" --cikti "<PDF klasörü>" \\
        [--alan sozel|sayisal|kod] [--dil tr|en] [--sinav test|klasik|karisik] [--hizli] [--dosya Ad]

Üç ayar her dersi kapsar:
  --alan   sozel   : tanım/kavram/madde ağırlıklı (eğitim, hukuk, tıp, tarih, işletme, sosyal bilimler…)
           sayisal : işlem/çözüm ağırlıklı (matematik, fizik, muhasebe, istatistik, mühendislik hesapları…)
           kod     : programlama (kod bloğu + çıktı, "bu kod ne yazdırır?" soruları)
  --dil    tr      : kaynak Türkçe, kağıt tamamen Türkçe
           en      : kaynak İngilizce → slayt cümlesi + kelime anlamları, kavramlar 'English (Türkçe)', A2 klasik cevaplar
  --sinav  virgülle birleştirilebilir: test · klasik · dy (doğru-yanlış) · bosluk · eslestirme · karisik (= test,klasik)
           test yoksa test kutuları hiç çıkmaz
  --plan   analiz.py'nin plan.json'u: bölüm sırası, her bölümün kaynağı, sayfa/soru bütçesi ve kutu önerileri yorum olarak gelir
  --hizli  sınava saatler kala A1/kısa hızlı tekrar: diyagram çizimi + kısa tanım tablosu (diğer ayarlar yok sayılır)

Kısayollar: --tur arkadas (sozel/tr/test) · ingilizce (sozel/en/karisik) · matematik (sayisal/tr/klasik) · hizli
"""
import argparse, pathlib, re

ap = argparse.ArgumentParser()
ap.add_argument('klasor'); ap.add_argument('--ders', required=True); ap.add_argument('--cikti', required=True)
ap.add_argument('--alan', choices=['sozel', 'sayisal', 'kod']); ap.add_argument('--dil', choices=['tr', 'en'])
ap.add_argument('--sinav', help='virgülle: test,klasik,dy,bosluk,eslestirme ya da karisik'); ap.add_argument('--hizli', action='store_true')
ap.add_argument('--ezber', action='store_true', help='ezber modu: kodlama, katla-test, kartlar, aralıklı tekrar (tıp, hukuk…)')
ap.add_argument('--sinav-tarihi', help='YYYY-MM-DD (aralıklı tekrar çizelgesi için)')
ap.add_argument('--plan', help='analiz.py çıktısı plan.json: sıra, bütçe, kutu önerileri ve alan/dil/sınav buradan gelir')
ap.add_argument('--tur', choices=['arkadas', 'ingilizce', 'matematik', 'hizli']); ap.add_argument('--dosya')
a = ap.parse_args()
KIS = {'arkadas': ('sozel', 'tr', 'test'), 'ingilizce': ('sozel', 'en', 'karisik'), 'matematik': ('sayisal', 'tr', 'klasik')}
if a.tur == 'hizli': a.hizli = True
if a.tur in KIS:
    for k_, v in zip(('alan', 'dil', 'sinav'), KIS[a.tur]):
        if getattr(a, k_) is None: setattr(a, k_, v)
import json
PLAN = json.loads(pathlib.Path(a.plan).read_text()) if a.plan else None
if PLAN:
    a.alan = a.alan or PLAN['alan']; a.dil = a.dil or PLAN['dil']; a.sinav = a.sinav or ','.join(PLAN['sinav'])
alan, dil, sinav = a.alan or 'sozel', a.dil or 'tr', a.sinav or 'karisik'
SN = set(sinav.split(','))
EZB = a.ezber or bool(PLAN and PLAN.get('ezber'))
if 'karisik' in SN: SN |= {'test', 'klasik'}

TRM = str.maketrans('çğıöşüÇĞİÖŞÜ', 'cgiosuCGIOSU')
dosya = a.dosya or re.sub(r'[^A-Za-z0-9]+', '_', a.ders.translate(TRM)).strip('_') + ('_Hizli_Tekrar' if a.hizli else '_Calisma_Kagidi')
d = pathlib.Path(a.klasor); d.mkdir(parents=True, exist_ok=True)
hedef = d / 'build.py'
assert not hedef.exists(), f'{hedef} zaten var; üzerine yazılmadı'
L = []   # üretilecek satırlar
w = L.append
DERS, CIKIS = repr(a.ders), repr(dosya + '.pdf')

w('import sys, pathlib, re')
w("sys.path.insert(0, str(pathlib.Path.home() / '.claude/skills/calisma-kagidi/scripts'))")
w('from kagit import Kagit')
w('from eklentiler import *')
w('D = pathlib.Path(__file__).parent')
w(f'CIKTI = pathlib.Path({a.cikti!r}).expanduser(); CIKTI.mkdir(parents=True, exist_ok=True)')

# ---------------- hızlı tekrar ----------------
if a.hizli:
    w('from diyagram import FIG_CSS, fig, svg, txt, ent, proc, store, arr, agac, venn3')
    w(f"k = Kagit({DERS} + ' Hızlı Tekrar', mode='tr')")
    w('TIP, TABLE, add = k.TIP, k.TABLE, k.add')
    w('add(CSS_HEPSI); add(FIG_CSS)')
    w("add('<style>table.d td{font-size:9.6pt;padding:3px 6px;vertical-align:top} table.d td:first-child{font-weight:700;color:#12305e} table.d td:nth-child(2){font-family:Georgia,serif;font-size:10pt}</style>')")
    w("k.h2('1 · Çizilebilecek şemalar', pb=False)")
    w("add(fig('ÖRNEK akış / bağlam şeması', svg(720, 300, proc(360, 140, 70, '0', 'SİSTEM') + ent(20, 117, 140, 46, 'Kullanıcı') + arr(160, 140, 290, 140, 'istek', 0, -7)),")
    w("        adimlar=['Ortaya ana kutuyu çiz.', 'Etrafına dış öğeleri yerleştir.', 'Okların üstüne ne gittiğini yaz.'], cumle='ÖRNEK tek cümlelik açıklama.'))")
    w("add(fig('ÖRNEK sınıflandırma ağacı', agac('KONU', [('Alt başlık 1', 'örnek a', 'örnek b'), ('Alt başlık 2', 'örnek c', 'örnek d')])))")
    w("k.h2('2 · Tanım soruları: kısa cevaplar')")
    w("R = [('Kavram', 'Bir iki kısa cümlelik cevap (İngilizce derste A1).', 'Türkçesi / açıklama')]")
    w("add('<table class=\"d\"><tr><th>Kavram</th><th>Kısa cevap (bunu yaz)</th><th>Not</th></tr>' + ''.join(f'<tr><td>{x}</td><td>{y}</td><td class=\"tp\">{z}</td></tr>' for x, y, z in R) + '</table>')")
    w("add(TIP('✍️ Uzun soru iskeleti', '<p>1) Tanım · 2) Örnek · 3) Neden önemli</p>'))")
    w(f"k.build(D / 'kagit.pdf', copy_to=CIKTI / {CIKIS}, open_pdf=True)")
    hedef.write_text('\n'.join(L) + '\n')
    print(f'iskelet (hızlı tekrar) → {hedef}'); raise SystemExit

# ---------------- normal kağıt ----------------
if dil == 'en':
    w("# Kelime sözlüğü: slayt cümlesindeki BÜTÜN anlamlı kelimeler (a/the/is/of hariç). Uzun ifadeler önce eşleşir.")
    w("GL = {'design': 'tasarım', 'system': 'sistem', 'requirement': 'gereksinim'}")
    w("def gloss(text):")
    w("    low = re.sub(r'<[^>]+>', ' ', text).lower()")
    w("    return [(x, GL[x]) for x in sorted(GL, key=len, reverse=True) if re.search(r'\\b' + re.escape(x) + r'\\b', low)]")
    w(f"k = Kagit({DERS} + ' Çalışma Kağıdı', mode='en', gloss=gloss)")
else:
    w(f"k = Kagit({DERS} + ' Çalışma Kağıdı', mode='tr')")
w('TIP, TRAP, TABLE, EXAM, add, EZBER, SLIDE = k.TIP, k.TRAP, k.TABLE, k.EXAM, k.add, k.EZBER, k.SLIDE')
w('add(EZBER_CSS)' if EZB else '# ezber modu kapalı')
w('add(CSS_HEPSI); add(ALAN_CSS)' + ('; add(MAT_CSS)' if alan == 'sayisal' else '') + '   # görünüm: orijinal kutulu format (kutusuz SADE_CSS sadece istenirse)')
if alan == 'sayisal': w('import kesir')
if 'test' not in SN: w('testsiz(k); EXAM = k.EXAM   # test sorusu yok')
if dil == 'en':
    w("def S(en, tr): return k.Q(en, ' · '.join(f'<b>{x}</b> = {y}' for x, y in gloss(en)), tr)")
    w("# Kavramlar İngilizce + (Türkçe): KAV'da kullanılan her terim burada olmalı")
    w("KAVMAP = {'Design': (T('Design', 'tasarım'), T('HOW the system works', 'sistem nasıl çalışır'))}")
    w('KAV = cift_dil_kav(k, KAVMAP)')
else:
    w('KAV = k.KAV')

ADLAR = {'test': 'çoktan seçmeli', 'klasik': 'klasik (🔑 anahtar kavramlı yazılı)', 'dy': 'doğru-yanlış', 'bosluk': 'boşluk doldurma', 'eslestirme': 'eşleştirme'}
bicim = ' + '.join(ADLAR[x] for x in ('test', 'klasik', 'dy', 'bosluk', 'eslestirme') if x in SN)
birimler = [b for b in PLAN['birimler'] if not b.get('soru_dosyasi') and b.get('butce', {}).get('sayfa', 1)] if PLAN else []
w(f"k.cover({DERS}, 'Çalışma Kağıdı', basliklar=('Bölüm', 'Konu', 'Kaynak'),")
if birimler:
    w('        bolumler=[' + ', '.join(repr((str(i + 1), 'KONU ADI', b['ad'][:60])) for i, b in enumerate(birimler)) + '],')
else:
    w("        bolumler=[('1', 'ÖRNEK konu', 'hafta 1 / s.1–5')],")
w(f"        oneri='Sınav: {bicim}. <span class=\"hl\">Sarı ve altı çizili</span> yerler en önemli ifadeler. Kaynakta olmayan bilgiler <b>“genel bilgi”</b> diye işaretlendi.')")

if PLAN and PLAN.get('temel_kavramlar'):
    w('')
    w('# Analiz: bu terimler tanımlandıkları birimden ÖNCE kullanılıyor → önce burada kısaca tanımla')
    w("k.h2('Önce bunu bil: temel kavramlar')")
    if dil == 'tr':
        w('add(KAV(' + ', '.join(repr((t, 'kısa tanım')) for t in PLAN['temel_kavramlar'][:10]) + '))')
    else:
        w("# KAVMAP'e ekleyip KAV ile ver: " + ', '.join(PLAN['temel_kavramlar'][:10]))
        w("add(TIP('📘 Temel kavramlar', '<p>ÖRNEK</p>'))")


def bolum(no, ad, b=None):
    w('')
    w(f'# ================= {no} =================')
    if b:
        bt = b['butce']
        w(f"# KAYNAK: {b['ad']} · {b['slayt']} slayt · ağırlık {b['agirlik']} → BÜTÇE ≈ {bt['sayfa']} sayfa, {bt['test']} test, {bt['klasik']} klasik")
        if b.get('anlatim'): w(f"# BASKIN İÇERİK: {b.get('baskin')} → ANLATIM: {b['anlatim']}")
        if b.get('kutular'): w('# ÖNERİ: ' + '; '.join(b['kutular']))
        if b.get('terimler'): w('# TANIMLANAN TERİMLER: ' + ', '.join(b['terimler']))
        if b.get('basliklar'): w('# SLAYT BAŞLIKLARI: ' + ' | '.join(b['basliklar'][:12]))
        w('# ANLATIM SIRASI: tanım → neden/fikir → süreç/örnek → karşılaştırma/tuzak → kavram kutusu → sorular')
    w(f"k.h2({no + ' · ' + ad!r})")
    bas = (b or {}).get('basliklar') or ['Slayttaki 1. fikir', 'Slayttaki 2. fikir']
    w("add(bu_bolumde('Bu bölümde öğrenilecek 1', 'Bu bölümde öğrenilecek 2'))   # MTH'deki 'Başlangıçta elimizde' karşılığı")
    w('# BU ÇATI SADECE BAŞLANGIÇ: konuya göre değiştir/sil. Öz cümle + ayrıntı akışı çoğu konuda iyi çalışır ama tek yol değil.')
    sirali = (b or {}).get('baskin') in ('süreç', 'kronoloji')
    w('add(akis([' + ('   # baskın içerik sıralı → numaralı' if sirali else '   # yan yana fikirler → numarasız (sadece gerçekten sıralıysa sirali=True)'))
    for x in bas[:6]:
        w(f"    ({('ÖZ: ' + x)!r}, ['ayrıntı: slaytta anlatılanı kendi cümlelerinle anlat', 'Örnek: …']),")
    w(f']], sirali={sirali}))'.replace(']],', '],'))
    if dil == 'en':
        w("add(SLIDE(S('Design is about HOW the system will do it.', 'Tasarım, sistemin bunu NASIL yapacağıyla ilgilidir.')))")
        w("add(TABLE(['', T('Column', 'sütun')], [['Satır', T('English cell', 'Türkçe karşılığı')]]))   # her İngilizce hücreye T()")
    else:
        w("add(anlat('Gerekirse akışa sığmayan kısa açıklama: <b>anahtar kelime</b> kalın.'))")
    if alan == 'sayisal':
        w("add(TIP('💡 Fikir: bu yöntem neden işe yarıyor?', '<p>ÖRNEK yöntem fikri.</p>'))")
        w("add(cozum('Örnek: y\\' = xy', 'y\\' = xy', 'ÖRNEK yöntem', [")
        w("    ('Değişkenleri ayır.', ['dy/dx = xy', 'dy/y = x dx']),")
        w("    ('İki tarafın integralini al.', ['∫ dy/y = ∫ x dx', 'ln|y| = x²/2 + c'])], sonuc='y = C e<sup>x²/2</sup>'))")
    if alan == 'kod':
        w('add(kod("x = [1, 2, 3]\\nfor i in x:\\n    print(i * 2)", cikti="2\\n4\\n6"))')
    w("# add(TRAP('Karıştırılan', '<p>X = … · Y = …</p>'))   # sadece gerçekten karıştırılan çift varsa")
    if EZB:
        w('# EZBER: sadece işe yarayacaksa (keyfi liste → kısa anlamlı kod; mantıklı sıra → mantik_zinciri; sayı/doz → katla_test)')
        w("add(kodlama('ÖRNEK sıralı liste', ['Birinci madde', 'İkinci madde', 'Üçüncü madde'], cumle='Bugün İyi Üç'))   # baş harfler; akılda kalan cümle uydur")
        w("add(katla_test('ÖRNEK normal değerler / dozlar / sınıflama', [('Kavram ya da soru', 'cevap, sayı ve birimiyle')]))   # sayıları ASLA silme")
    w("add(KAV(('Design', 'kısa tanım')))" if dil == 'en' else "add(KAV(('Kavram', 'Kısa tanım')))")
    if 'test' in SN:
        if alan == 'kod':
            w("add(EXAM(('Yukarıdaki kod ne yazdırır?', ['2 4 6 (alt alta)', '1 2 3', '6', 'Hata verir'], 'A', 'Her eleman 2 ile çarpılıp yazdırılır.')))")
        else:
            w("add(EXAM(('ÖRNEK soru (kaynaktaki örneğin birebir kopyası olmasın)?', ['şık A', 'şık B', 'şık C', 'şık D'], 'B', 'Neden B.')))")
    if 'dy' in SN: w("add(dogru_yanlis([('ÖRNEK ifade.', True, ''), ('ÖRNEK yanlış ifade.', False, 'doğrusu: …')]))")
    if 'bosluk' in SN: w("add(bosluk_doldurma([('ÖRNEK cümle ____ devamı.', 'cevap')]))")
    if 'eslestirme' in SN: w("add(eslestirme([('Kavram 1', 'tanım 1'), ('Kavram 2', 'tanım 2'), ('Kavram 3', 'tanım 3')]))")
    if 'klasik' in SN:
        if dil == 'en':
            w("k.h3('✍️ Klasik sorular (A2 İngilizce cevap + Türkçesi)')")
            w("add(klasik_kutu('What is software design?', 'Yazılım tasarımı nedir?', 'HOW · structure', 'Software design shows <b>HOW</b> the system works. For example, …', 'Yazılım tasarımı sistemin NASIL çalıştığını gösterir. Örneğin …', gloss))")
        elif alan == 'sayisal':
            w("k.h3('Sınav tipi sorular: önce kendin çöz, sonra çözüme bak')")
        else:
            w("k.h3('✍️ Klasik sorular')")
            w("add(klasik_tr('ÖRNEK: X’i tanımlayıp bir örnek veriniz.', 'kavram 1 · kavram 2', 'X, … dir. Örneğin …'))")


if birimler:
    for i, b in enumerate(birimler): bolum(str(i + 1), 'KONU ADI', b)
else:
    bolum('1', 'ÖRNEK bölüm')
w('')
w('k.summary()')
if EZB:
    w("k.h2('Ezber kartları ve tekrar planı')")
    w("KARTLAR = [('ÖRNEK ön yüz: soru', 'arka yüz: cevap')]   # her bölümün katla-test satırlarından üret")
    tarih = a.sinav_tarihi or 'YYYY-MM-DD'
    w(f"add(tekrar_cizelgesi([" + ', '.join(repr(f'{i + 1}. bölüm') for i in range(max(1, len(birimler)))) + f"], {tarih!r}))" if a.sinav_tarihi else
      "# add(tekrar_cizelgesi(['1. bölüm', '2. bölüm'], 'YYYY-MM-DD'))   # sınav tarihi verilince aç")
    w('add(ezber_kartlari(KARTLAR))')
ifade = "'about HOW the system will do it'" if dil == 'en' else "'anahtar kelime'"
w("n, eksik = vurgu(k, {" + ', '.join(f"'{i + 1}': [{ifade}]" for i in range(max(1, len(birimler)))) + "})   # her bölüm için en önemli ifadeler")
w("print('altı çizili:', n, 'bulunamayan:', eksik)")
if alan == 'sayisal':
    w('_h = k.html; k.html = lambda: kesir.convert(kesir.convert(_h()))   # a/b → kesir çizgisi')
w(f"k.build(D / 'kagit.pdf', copy_to=CIKTI / {CIKIS}, open_pdf=True)")
w("# TESLİMDEN ÖNCE: python3 -I ~/.claude/skills/calisma-kagidi/scripts/denetim.py --kagit " + str(d / 'kagit.html') + " --kaynak <kaynak> ; sonra preview ile öğrenci gözüyle oku")
hedef.write_text('\n'.join(L) + '\n')
etiket = f'{alan} / {dil} / {",".join(sorted(SN))}' + (f' · plan: {len(birimler)} bölüm' if birimler else '')
print(f'iskelet ({etiket}) → {hedef}\nçalıştır: python3 {hedef}\nPDF → {pathlib.Path(a.cikti).expanduser() / (dosya + ".pdf")}')
