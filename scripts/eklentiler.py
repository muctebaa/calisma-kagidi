"""Kagit için eklentiler (Kasım 2026'da kullanıcının onayladığı biçimler).

    from eklentiler import T, cift_dil_kav, vurgu, klasik_kutu, testsiz, CSS_HEPSI
    k.add(CSS_HEPSI)                       # bir kez, kapaktan önce

- T(en, tr)                 → 'English (Türkçe)'  : Türkçe gri ve parantez içinde
- cift_dil_kav(k, MAP)      → k.KAV'ı sarar: KAV(('Term', ...)) çağrılarında MAP[term] = (T(...), T(...)) kullanılır
- klasik_kutu(...)          → klasik (yazılı) soru: İng. soru + 🇹🇷 soru + 🔑 mutlaka geçsin + A2 cevap + tam Türkçe + kelime çipleri
- testsiz(k)                → sınav klasikse: EXAM bloklarını boşaltır, kapaktaki "Kırmızı kutu" satırını soru kutusuyla değiştirir
- vurgu(k, {'1': [...]})    → bölüm bazında ifadelerin İLK geçtiği yeri sarı fosfor + kırmızı alt çizgi yapar
                              (build'den hemen önce çağır; soru kutuları ve kelime çipleri atlanır)
"""
import re

CSS_HEPSI = '''<style>
 .tp{color:#5a6b80;font-weight:400;font-size:92%}
 .hl{background:linear-gradient(transparent 52%,#ffe866 52%);text-decoration:underline;text-decoration-color:#d0342c;
     text-decoration-thickness:1.5px;text-underline-offset:2px;-webkit-print-color-adjust:exact;print-color-adjust:exact}
 .ma{background:#f6f9ff;border-left:5px solid #3b6fd8;page-break-inside:avoid;break-inside:avoid}
 .ma .title{color:#12305e}.ma .en{font-weight:400;color:#111;font-family:Georgia,serif;font-size:10.6pt;line-height:1.65;margin:4px 0}
 .ma .trc{font-weight:400;font-size:9.5pt;color:#444;border-top:1px dashed #b7c3d6;padding-top:3px;margin-top:3px}
 .ks .qtr{font-size:9.5pt;color:#4a5568;margin:1px 0 3px}
 .ks .key{font-size:9.5pt;background:#fff6dd;border-left:3px solid #e0a800;padding:2px 8px;margin:3px 0}
 .ks .lvl{display:inline-block;font-size:8pt;font-weight:700;color:#fff;background:#3b6fd8;border-radius:8px;padding:0 7px;margin-top:3px}
 .ks .words{font-size:8pt;line-height:1.35;margin-top:4px}.ks .words .w{padding:0 5px;margin:1px 2px}
</style>'''


def T(en, tr):
    return f'{en} <span class="tp">({tr})</span>'


def cift_dil_kav(k, MAP):
    """MAP: {'Term': (T('Term','terim'), T('explanation','açıklama'))}. Eksik terimde hata verir."""
    eski = k.KAV
    def KAV(*pairs, **kw):
        pairs = [(a.split(' <span class="tp">')[0], b) for a, b in pairs]
        eksik = [a for a, _ in pairs if a not in MAP]
        assert not eksik, f'cift_dil MAP eksik: {eksik}'
        return eski(*[MAP[a] for a, _ in pairs], **kw)
    k.KAV = KAV
    return KAV


def klasik_kutu(q, qtr, key, en, tr, gloss=None, seviye='A2'):
    g = ''.join(f'<span class="w"><b>{a}</b> = {b}</span>' for a, b in gloss(q + ' ' + en)) if gloss else ''
    return (f'<div class="box ma ks"><div class="title">✍️ {q}</div><div class="qtr">🇹🇷 {qtr}</div>'
            f'<div class="key">🔑 <b>Cevapta mutlaka geçsin:</b> {key}</div><span class="lvl">{seviye} cevap</span>'
            f'<div class="en">{en}</div><div class="trc">🇹🇷 {tr}</div>'
            + (f'<div class="words tm">📘 {g}</div>' if g else '') + '</div>')


def testsiz(k):
    k.EXAM = lambda *a, **kw: ''
    eski = '<tr><td><div class="box exam" style="margin:0;padding:3px 8px">Kırmızı kutu</div></td><td>Örnek sorular. Cevaplar hemen altındaki kutuda.</td></tr>'
    yeni = '<tr><td><div class="box ma" style="margin:0;padding:3px 8px">✍️ Soru kutusu</div></td><td>Klasik soru: cevap, Türkçesi ve 🔑 mutlaka geçecek terimler</td></tr>'
    k._testsiz_satir = (eski, yeni)
    return k.EXAM


_ATLA = re.compile(r'(<p class="gl">.*?</p>|<div class="words[^"]*">.*?</div>)', re.S)


def vurgu(k, P):
    """P: {'1': ['ifade', ...], '2': [...]} — anahtar, h2 başlığındaki 'N ·' numarası. Dönüş: (sayı, bulunamayanlar)."""
    if getattr(k, '_testsiz_satir', None):
        e, y = k._testsiz_satir; k.H = [h.replace(e, y) for h in k.H if h]
    sec, done, out = None, set(), []
    def metin(seg):
        parts = re.split(r'(<[^>]+>)', seg)
        for i, t in enumerate(parts):
            if not t or t.startswith('<'): continue
            for ph in P.get(sec, []):
                if (sec, ph) in done: continue
                j = t.find(ph)
                if j >= 0:
                    t = t[:j] + f'<span class="hl">{ph}</span>' + t[j + len(ph):]; done.add((sec, ph))
            parts[i] = t
        return ''.join(parts)
    for ch in k.H:
        m = re.search(r'<h2>(\d+) ·', ch)
        if m: sec = m.group(1)
        elif '<h2>' in ch: sec = None
        if sec and 'class="box exam' not in ch:
            ch = ''.join(s if _ATLA.fullmatch(s) else metin(s) for s in _ATLA.split(ch))
        out.append(ch)
    k.H = out
    eksik = [(s, p) for s, ps in P.items() for p in ps if (s, p) not in done]
    return len(done), eksik


# ---------- Matematik: onaylanan tek format (MTH201, 10 Kasım 2026) ----------
MAT_CSS = '''<style>
 .fr{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;font-size:92%;margin:0 2px}
 .fr .nu{border-bottom:1px solid #222;padding:0 2px}.fr .de{padding:0 2px}
 .sol{background:#f7f9fc;border-left:5px solid #2e9b55;page-break-inside:avoid;break-inside:avoid}.sol.long{page-break-inside:auto;break-inside:auto}
 .bas{background:#eef3fb;border:1px solid #c9d6ea;border-radius:6px;padding:5px 10px;margin:4px 0 8px;line-height:1.6}.bas .bt{font-weight:700;color:#1f4fa8;margin-bottom:2px}
 ol.yn{list-style:none;counter-reset:yn;padding-left:0;margin:4px 0}
 ol.yn>li{counter-increment:yn;margin:6px 0 4px;page-break-inside:avoid}
 ol.yn>li>.stxt:before{content:counter(yn);display:inline-block;width:18px;height:18px;line-height:18px;border-radius:50%;background:#2e9b55;color:#fff;font-size:9pt;font-weight:700;text-align:center;margin-right:7px}
 ol.yn .ml{border-left:2px solid #cfd6df;margin:4px 0 6px 24px;padding:1px 0 1px 14px;font-family:"Times New Roman","STIX Two Math",serif;font-size:11.5pt;line-height:1.9}
 .ans{background:#e6f6ea;border:1px solid #9fd5ab;border-radius:6px;padding:4px 8px;margin-top:4px;font-weight:700}
</style>'''


def fr(a, b):
    """Kesir çizgili kesir (kesir.py '/' yazımını da otomatik çevirir)."""
    return f'<span class="fr"><span class="nu">{a}</span><span class="de">{b}</span></span>'


def cozum(baslik, denklem, yontem, adimlar, sonuc=None, aday=None):
    """adimlar: [('Tek cümle ne yapıldığı', ['ara işlem 1', 'ara işlem 2', ...]), ...]
    Kural: adım başına TEK cümle + altında BÜTÜN ara işlemler. Adım adım 'Elimizde/Neden' blokları YOK."""
    bas = f'<div><b>Denklem:</b> {denklem}</div>' + (f'<div><b>Aday çözüm:</b> {aday}</div>' if aday else '') + f'<div><b>Yöntem:</b> {yontem}</div>'
    body = ''.join(f'<li><div class="stxt">{t}</div><div class="ml">' + ''.join(f'<div>{l}</div>' for l in ls) + '</div></li>' for t, ls in adimlar)
    n = sum(1 + sum(1.5 if 'fr' in x or '/' in x else 1 for x in ls) for _, ls in adimlar)
    cls = 'box sol long' if n > 27 else 'box sol'
    a = f'<div class="ans">✅ Sonuç: {sonuc}</div>' if sonuc else ''
    return (f'<div class="{cls}"><div class="title">✏️ {baslik}</div><div class="bas"><div class="bt">📋 Başlangıçta elimizde</div>{bas}</div>'
            f'<ol class="yn">{body}</ol>{a}</div>')


# ---------- Alanlara göre ek kutular ----------
ALAN_CSS = '''<style>
 .kod{background:#1e2430;color:#e6edf3;font-family:Menlo,Consolas,monospace;font-size:9.5pt;line-height:1.5;border-radius:6px;padding:8px 12px;margin:6px 0;white-space:pre;page-break-inside:avoid;overflow:hidden}
 .kod .c{color:#8b949e}.kod .k{color:#ff7b72}.kod .s{color:#a5d6ff}
 .cikti{background:#f3f6f9;border-left:4px solid #6b7a90;font-family:Menlo,Consolas,monospace;font-size:9.5pt;padding:4px 10px;white-space:pre;margin:2px 0 8px}
 .kt{border:1.5px solid #c9d6ea;border-radius:8px;padding:6px 12px;margin:8px 0;background:#fbfcfe;page-break-inside:avoid;break-inside:avoid}
 .kt .s{font-weight:700;color:#12305e}.kt .key{font-size:9.5pt;background:#fff6dd;border-left:3px solid #e0a800;padding:2px 8px;margin:4px 0}
 .kt .c{border-top:1px dashed #b7c3d6;margin-top:4px;padding-top:4px}
 .zc{border-left:3px solid #7a4fd0;margin:4px 0 4px 6px;padding-left:12px}.zc div{margin:3px 0}.zc b{color:#4b2a9a}
</style>'''


def kod(src, cikti=None, dil=''):
    """Programlama dersleri: kod bloğu (+ istenirse çıktısı). src düz metin; HTML kaçışı burada yapılır."""
    import html
    out = f'<div class="kod">{html.escape(src.strip(chr(10)))}</div>'
    return out + (f'<div class="cikti">▶ Çıktı:\n{html.escape(cikti)}</div>' if cikti is not None else '')


def klasik_tr(soru, anahtar, cevap):
    """Türkçe derslerde klasik (yazılı) soru: soru + 🔑 mutlaka geçecek kavramlar + örnek cevap."""
    return (f'<div class="kt"><div class="s">✍️ {soru}</div><div class="key">🔑 <b>Cevapta mutlaka geçsin:</b> {anahtar}</div>'
            f'<div class="c"><b>Örnek cevap:</b> {cevap}</div></div>')


def zaman_cizelgesi(olaylar):
    """Tarih / hukuk / kronoloji ağırlıklı dersler: [(yıl, olay), ...]"""
    return '<div class="zc">' + ''.join(f'<div><b>{y}</b> · {o}</div>' for y, o in olaylar) + '</div>'


# ---------- Diğer sınav biçimleri (cevaplar hemen altında) ----------
def dogru_yanlis(maddeler, baslik='✔️ Doğru / Yanlış'):
    """maddeler: [(ifade, True/False, 'yanlışsa doğrusu / kısa açıklama'), ...]"""
    s = ''.join(f'<li>( &nbsp; ) {m}</li>' for m, _, _ in maddeler)
    c = ''.join(f'<li><b>{"D" if d else "Y"}</b>{" — " + n if n else ""}</li>' for _, d, n in maddeler)
    return (f'<div class="box exam"><div class="title">{baslik}</div><ol>{s}</ol></div>'
            f'<div class="box tip"><div class="title">✅ Cevaplar</div><ol>{c}</ol></div>')


def bosluk_doldurma(maddeler, baslik='✏️ Boşluk doldurma'):
    """maddeler: [('… cümle ____ devam', 'cevap'), ...]"""
    s = ''.join(f'<li>{m}</li>' for m, _ in maddeler)
    c = ''.join(f'<li><b>{c_}</b></li>' for _, c_ in maddeler)
    return (f'<div class="box exam"><div class="title">{baslik}</div><ol>{s}</ol></div>'
            f'<div class="box tip"><div class="title">✅ Cevaplar</div><ol>{c}</ol></div>')


def eslestirme(ciftler, baslik='🔗 Eşleştirme', karistir=True):
    """ciftler: [(sol, sağ), ...] — sağ sütun karıştırılır, cevap anahtarı altta."""
    import random
    sag = [r for _, r in ciftler]; sira = list(range(len(sag)))
    if karistir: random.Random(len(sag) * 31 + 7).shuffle(sira)
    harf = 'abcdefghijklmnopqrstuvwxyz'
    rows = ''.join(f'<tr><td>{i + 1}. {l}</td><td>{harf[j]}) {sag[sira[j]]}</td></tr>' for i, ((l, _), j) in enumerate(zip(ciftler, range(len(sira)))))
    ters = {sira[j]: harf[j] for j in range(len(sira))}
    c = ' · '.join(f'{i + 1}→{ters[i]}' for i in range(len(ciftler)))
    return (f'<div class="box exam"><div class="title">{baslik}</div><table>{rows}</table></div>'
            f'<div class="box tip"><div class="title">✅ Cevaplar</div><p>{c}</p></div>')


# ---------- Ezber modu (tıp, hukuk, anatomi, farmakoloji… liste ve sayı ağırlıklı alanlar) ----------
EZBER_CSS = '''<style>
 .kd{border:1.5px solid #e0a800;border-left:6px solid #e0a800;border-radius:8px;background:#fffaf0;padding:6px 12px;margin:8px 0;page-break-inside:avoid;break-inside:avoid}
 .kd .t{font-weight:700;color:#7a5200}.kd .kdk{font-size:19pt;font-weight:800;letter-spacing:1px;margin:2px 0}.kd .kdk .dolgu{color:#9aa3ad;font-weight:500}
 .kd .cm{font-style:italic;margin:2px 0 4px}.kd .cm b,.kd li b.h{color:#b00020;font-size:115%}
 .kd ol{margin:2px 0 2px 20px;padding:0}.kd li{margin:1px 0}
 table.kt2{width:100%;border-collapse:collapse;page-break-inside:auto}
 table.kt2 td{border-bottom:1px solid #dde3ea;padding:5px 8px;vertical-align:top}
 table.kt2 td.cv{border-left:2px dashed #888;color:#123;background:#f6f9fc}
 table.kt2 tr{page-break-inside:avoid}
 .ktb{font-size:9.5pt;color:#555;margin:2px 0 4px}
 .kartlar{display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:6cm;page-break-inside:avoid}
 .kart{border:1px dashed #999;display:flex;align-items:center;justify-content:center;text-align:center;padding:12px;font-size:13pt;line-height:1.4;position:relative}
 .kart .no{position:absolute;top:4px;left:8px;font-size:8pt;color:#999}
 .kart.arka{background:#f6f9fc;font-size:11.5pt}
 table.tc td,table.tc th{text-align:center;font-size:9.5pt;padding:3px 5px}table.tc td:first-child{text-align:left}
</style>'''


def _ilk(s):
    import re as _re
    m = _re.search(r'[A-Za-zÇĞİÖŞÜçğıöşü0-9]', _re.sub(r'<[^>]+>', '', s))
    if not m: return '?'
    c = m.group(0)
    return 'İ' if c == 'i' else 'I' if c == 'ı' else c.upper()


def kodlama(baslik, maddeler, kod=None, hikaye=None, sira_onemli=True, cumle=None):
    """ANLAMLI kodlama. kod: anlamlı bir söz öbeği; maddelere karşılık gelen parçalar [köşeli parantez] içinde,
    aradaki dolgu harfleri parantez dışında. Parçalar maddelerle AYNI SIRADA olmalı (sıra önemsizse maddeleri koda göre diz).
      kodlama('Sıfat-fiil ekleri', ['-an (gelen)', '-ası (görülesi)', '-mez (bitmez)', '-ar (akar)', '-dik (bildik)', '-ecek (gelecek)', '-miş (olmuş)'],
              kod='[An][ası] [mez][ar] [dik][ecek][miş]')
      kodlama('OBS’nin dört özelliği', ['Bireyselleştirilmiş', 'İnsan onuruna yakışır', 'Kanıt temelli', 'Proaktif'],
              kod='[B][İ]r [K]a[P]', hikaye='OBS çocuğu bir kap gibi sarar.', sira_onemli=False)
    Kod kısa ve anlamlı olmalı, parçalar maddeyi çağrıştırmalı; sırası mantıklı listede kod yerine mantik_zinciri daha iyi."""
    import re as _re
    renk = ['#c0392b', '#1f5fa8', '#1e8449', '#a04000', '#7d3c98', '#117a65', '#b7950b']
    if cumle and not kod: kod = cumle            # eski çağrılarla uyum
    if not kod or '[' not in kod:                # parça işaretlenmemişse: baş harfleri işaretle (yalnızca son çare)
        kod = kod or ''.join(_ilk(m) for m in maddeler)
        parcalar = [_ilk(m) for m in maddeler]
    else:
        parcalar = _re.findall(r'\[([^\]]+)\]', kod)
    assert len(parcalar) == len(maddeler), f'kodlama: {len(parcalar)} parça ↔ {len(maddeler)} madde ({baslik})'
    sayac = iter(range(len(parcalar)))
    kod_html = _re.sub(r'\[([^\]]+)\]', lambda m: (lambda i: f'<b style="color:{renk[i % len(renk)]}">{m.group(1)}</b>')(next(sayac)),
                       _re.sub(r'([^\[\]]+)(?![^\[]*\])', r'<span class="dolgu">\1</span>', kod)) if '[' in kod else f'<b style="color:{renk[0]}">{kod}</b>'
    def isaretle(m, parca, i):
        duz = _re.sub(r'<[^>]+>', '', m)
        j = duz.lower().find(parca.lower().strip('-'))
        if j < 0: return f'<b style="color:{renk[i % len(renk)]}">[{parca}]</b> {m}'
        p = parca.strip('-'); return duz[:j] + f'<b style="color:{renk[i % len(renk)]}">{duz[j:j + len(p)]}</b>' + duz[j + len(p):]
    li = ''.join(f'<li>{isaretle(m, p, i)}</li>' for i, (m, p) in enumerate(zip(maddeler, parcalar)))
    not_ = '' if sira_onemli else '<div class="small">Sıra önemli değil; maddeler koda göre dizildi.</div>'
    hk = f'<div class="cm">💬 {hikaye}</div>' if hikaye else ''
    liste = f'<ol>{li}</ol>' if sira_onemli else f'<ul style="margin:2px 0 2px 20px;padding:0">{li}</ul>'   # sırasız listede numara yok
    return f'<div class="kd"><div class="t">🔤 Kodlama: {baslik}</div><div class="kdk">{kod_html}</div>{hk}{liste}{not_}</div>'


def katla_test(baslik, satirlar, sol='Gördüğün', sag='Söyleyeceğin'):
    """Kendini sınama tablosu: sağ sütunu katla/kapat, soldakine bakıp cevabı söyle. satirlar: [(sol, sağ), ...]"""
    rows = ''.join(f'<tr><td>{a}</td><td class="cv">{b}</td></tr>' for a, b in satirlar)
    return (f'<div class="box tip" style="page-break-inside:auto"><div class="title">🙈 Katla-test: {baslik}</div>'
            f'<div class="ktb">Kesikli çizgiden katla ya da sağ sütunu kapat; soldakini görünce cevabı yüksek sesle söyle, sonra aç ve kontrol et.</div>'
            f'<table class="kt2"><tr><th>{sol}</th><th>{sag}</th></tr>{rows}</table></div>')


def ezber_kartlari(kartlar, baslik='✂️ Ezber kartları'):
    """Kesilebilir kartlar: önce ön yüzler, sonra arka yüzler. Çift taraflı (uzun kenardan) basınca arka yüz tam denk gelir.
    kartlar: [(ön, arka), ...] · sayfa başına 8 kart (2×4)."""
    out = [f'<h3>{baslik}</h3><p class="small">Çift taraflı yazdır (uzun kenardan çevir), kesikli çizgilerden kes. Önde soru, arkada cevap.</p>']
    for s in range(0, len(kartlar), 8):
        grup = kartlar[s:s + 8]
        on = ''.join(f'<div class="kart"><span class="no">{s + i + 1}</span>{a}</div>' for i, (a, _) in enumerate(grup))
        arka_sira = []
        for r in range(0, 8, 2):                       # her satırda sol-sağ yer değiştirir (ayna)
            ikili = list(range(r, min(r + 2, len(grup))))
            arka_sira += ([ikili[1], ikili[0]] if len(ikili) == 2 else [None, ikili[0]]) if ikili else []
        arka = ''.join('<div class="kart arka"></div>' if j is None else f'<div class="kart arka"><span class="no">{s + j + 1}</span>{grup[j][1]}</div>' for j in arka_sira)
        out.append(f'<div class="kartlar" style="page-break-before:always">{on}</div>')
        out.append(f'<div class="kartlar" style="page-break-before:always">{arka}</div>')
    return ''.join(out)


def tekrar_cizelgesi(konular, sinav_tarihi, baslangic=None, araliklar=(0, 1, 3, 7)):
    """Aralıklı tekrar: her konu ilk öğrenildiği günden +1, +3, +7 gün sonra tekrar edilir (sınavdan sonraya düşen atlanır).
    konular sırayla başlangıç ile sınavın 1 gün öncesi arasına yayılır. Tarihler 'YYYY-MM-DD'."""
    import datetime as dt
    son = dt.date.fromisoformat(sinav_tarihi) - dt.timedelta(days=1)
    bas = dt.date.fromisoformat(baslangic) if baslangic else dt.date.today()
    gun = max(1, (son - bas).days + 1)
    AY = 'Oca Şub Mar Nis May Haz Tem Ağu Eyl Eki Kas Ara'.split()
    f = lambda d: f'{d.day} {AY[d.month - 1]}'
    rows = ''
    for i, k in enumerate(konular):
        ilk = bas + dt.timedelta(days=min(gun - 1, i * gun // max(1, len(konular))))
        hucre = []
        for a in araliklar:
            d = ilk + dt.timedelta(days=a)
            hucre.append(f'☐ {f(d)}' if d <= son else '—')
        rows += f'<tr><td>{k}</td>' + ''.join(f'<td>{h}</td>' for h in hucre) + '</tr>'
    bas_h = ''.join(f'<th>{"öğren" if a == 0 else f"+{a} gün"}</th>' for a in araliklar)
    return (f'<div class="box tip"><div class="title">📅 Aralıklı tekrar çizelgesi (sınav: {f(son + dt.timedelta(days=1))})</div>'
            f'<p class="small">Her konuyu öğrendiğin gün, ertesi gün, 3 gün ve 7 gün sonra kısa tekrar et (katla-test/kartlarla). Yaptıkça kutuyu işaretle. Son gün sadece işaretsiz kalanlar.</p>'
            f'<table class="tc"><tr><th>Konu</th>{bas_h}</tr>{rows}</table></div>')


# ---------- Sade format (varsayılan, 12 Kasım 2026: kullanıcı "kutularla yormayalım" dedi) ----------
# Bütün kutuları düz anlatıma çevirir: dolgu ve çerçeve yok, sadece ince sol çizgi + küçük başlık etiketi.
# Diğer CSS'lerden SONRA eklenmeli (sonraki kural öncekini ezer).
SADE_CSS = '''<style>
 body{font-size:10.8pt;line-height:1.62;color:#222}
 p{margin:6px 0 8px}
 h2{font-size:15pt;color:#14335f;border-bottom:1px solid #c9d2df;padding-bottom:4px;margin:24px 0 10px}
 h3{font-size:12pt;color:#14335f;margin:16px 0 4px}
 .box,.kav,.trap,.tip,.exam,.slide,.ezber,.vocab,.warn,.ma,.kt,.kd,.ik,.fig,.sol,.bas,.kod+.cikti{
   background:none!important;border:none!important;border-radius:0!important;box-shadow:none!important;
   border-left:2px solid #d5dbe5!important;padding:2px 0 2px 14px!important;margin:12px 0!important}
 .kav{border-left-color:#7da2d6!important}.trap,.warn{border-left-color:#e3a0a0!important}
 .exam{border-left-color:#e3a0a0!important}.ezber,.kd{border-left-color:#e7c66a!important}
 .sol{border-left-color:#8fcca2!important}.bas{border-left:none!important;padding-left:0!important}
 .title,.kav .title,.trap .title,.slide .lbl,.kd .t,.ik .it,.fig .t{font-size:9pt!important;font-weight:700!important;letter-spacing:.4px;
   text-transform:uppercase;color:#5d6b80!important;margin:0 0 3px!important}
 .trap .title{color:#a33!important}.kav .title{color:#3d6aa8!important}
 .kav dl{margin:0}.kav dt{display:inline;font-weight:700;color:#14335f}.kav dt:after{content:" — ";font-weight:400;color:#888}
 .kav dd{display:inline;margin:0}.kav dd:after{content:"";display:block;margin-bottom:3px}
 .slide p.q{font-style:normal}.q b,b.k{background:none;border-bottom:1.5px solid #e7c66a;border-radius:0;padding:0}
 .sq{border-bottom:none;margin:4px 0 8px}
 .w,.tm .w,.ks .words .w{background:none!important;border:none!important;padding:0!important;margin:0 8px 0 0!important;
   color:#2f6b45!important;font-size:8.8pt!important;display:inline}
 .gl{color:#2f6b45}.words{line-height:1.6}
 table{font-size:10pt}th,td{border:none;border-bottom:1px solid #e3e7ee;padding:5px 8px}th{background:none;color:#14335f;border-bottom:1.5px solid #c9d2df}
 .exam .qn{color:#a33}.an{border-top:none}.box.tip .an{font-size:9.8pt;color:#444}
 .cover{border:1px solid #c9d2df;border-radius:6px}
 .ks .key,.kt .key,.ma .trc{background:none!important;border:none!important;padding:0!important}
 .ks .lvl{background:none;color:#3d6aa8;padding:0;font-size:8.5pt}
 .kd .kdk{font-size:17pt;letter-spacing:1px}
 .ans{background:none;border:none;border-top:1px solid #cfe6d5;border-radius:0;padding:4px 0 0}
</style>'''


def anlat(*paragraflar):
    """Slaytın anlattığını düz metinle anlatmak için: her argüman bir paragraf (kalın anahtar kelimeler serbest)."""
    return ''.join(f'<p>{p}</p>' for p in paragraflar)


# ---------- Akış formatı: MTH201'deki çözüm yapısının sözel derslere uyarlanması ----------
# MTH'de işe yarayan: başta "elimizde ne var" + numaralı adımlar; her adımda TEK cümle öz + altında girintili ayrıntı.
# Sözel derste adım = fikir: slaytın akışı sırasıyla, her fikir bir öz cümle + ayrıntı/örnek satırları.
AKIS_CSS = '''<style>
 .bubl{margin:6px 0 10px;padding:0 0 0 14px;border-left:2px solid #c9d6ea}
 .bubl .bt{font-size:9pt;font-weight:700;letter-spacing:.4px;text-transform:uppercase;color:#3d6aa8;margin-bottom:2px}
 .bubl ul{margin:0;padding-left:18px}
 ol.ak{list-style:none;counter-reset:ak;padding-left:0;margin:6px 0}
 ol.ak>li{counter-increment:ak;margin:9px 0 6px;page-break-inside:avoid;break-inside:avoid}
 ol.ak>li>.oz:before{content:counter(ak);display:inline-block;width:19px;height:19px;line-height:19px;border-radius:50%;background:#3d6aa8;color:#fff;
   font-size:9pt;font-weight:700;text-align:center;margin-right:8px}
 ol.ak .oz{font-weight:600;color:#14335f}
 ol.ak.sz>li{margin:11px 0 6px}
 ol.ak.sz>li>.oz:before{content:"";width:7px;height:7px;line-height:0;border-radius:50%;background:#9db4d6;margin:0 9px 2px 2px;vertical-align:middle}
 ol.ak.sz .ay{margin-left:18px}
 ol.ak .ay{border-left:2px solid #d5dbe5;margin:3px 0 4px 26px;padding:1px 0 1px 14px;line-height:1.6}
 ol.ak .ay div{margin:2px 0}
 ol.ak .ay .orn{color:#3f5a3f}ol.ak .ay .orn:before{content:"Örnek: ";font-weight:700}
</style>'''
SADE_CSS = SADE_CSS + AKIS_CSS


def bu_bolumde(*maddeler, baslik='Bu bölümde'):
    """MTH'deki 'Başlangıçta elimizde' karşılığı: bölümün başında ne öğrenileceği (2–5 kısa madde)."""
    return f'<div class="bubl"><div class="bt">📋 {baslik}</div><ul>' + ''.join(f'<li>{m}</li>' for m in maddeler) + '</ul></div>'


def akis(maddeler, sirali=False):
    """maddeler: [(öz cümle, [ayrıntı satırları]), ...]. Ayrıntı 'Örnek: …' ile başlarsa örnek olarak işaretlenir.
    Slaytın sırasını izle; her öz cümle tek başına okununca konuyu özetlemeli.
    sirali=True SADECE içerik gerçekten sıralıysa (süreç, adım, evre, aşama, kronoloji): o zaman numaralı daire çıkar.
    Yan yana fikirlerde numara kullanma (kullanıcı 12 Kas: "her başlığı 1-2-3 diye ayırmak çok düz mantık")."""
    out = []
    for oz, ay in maddeler:
        satir = ''.join(f'<div class="orn">{x[7:].strip()}</div>' if x.startswith('Örnek:') else f'<div>{x}</div>' for x in ay)
        out.append(f'<li><div class="oz">{oz}</div>' + (f'<div class="ay">{satir}</div>' if ay else '') + '</li>')
    return f'<ol class="ak{"" if sirali else " sz"}">' + ''.join(out) + '</ol>'


# ---------- Kodlama yardımcısı: hece / 2–3 harf parçaları ----------
_UNLU = set('aeıioöuüAEIİOÖUÜâîûÂÎÛ')


def heceler(kelime):
    """Türkçe heceleme (basit kural: iki ünlü arasındaki son ünsüz sonraki heceye geçer). 'Pazarlık' → ['Pa', 'zar', 'lık']"""
    k = kelime; idx = [i for i, c in enumerate(k) if c in _UNLU]
    if len(idx) <= 1: return [k]
    out, bas = [], 0
    for a_, b_ in zip(idx, idx[1:]):
        unsuz = b_ - a_ - 1
        kes = b_ - 1 if unsuz >= 1 else b_
        out.append(k[bas:kes]); bas = kes
    out.append(k[bas:]); return out


def parca_onerileri(maddeler):
    """Kod kurmadan önce bak: her madde için ilk hece ve 2–3 harflik baş parçalar. Anahtar kelime ilk kelime değilse elle seç."""
    import re as _re
    for m in maddeler:
        w = _re.sub(r'<[^>]+>|^[-–\\s]+', '', m).split()[0]
        h = heceler(w)
        print(f'{m[:40]:40} → ilk hece: {h[0]:6} · 2 harf: {w[:2]:4} · 3 harf: {w[:3]:5} · iki hece: {"".join(h[:2])}')


# ---------- Mantık zinciri: sırası mantıklı listeler için (kod yerine) ----------
# Kullanıcı 12 Kas: "ŞİÜS / PaKU mantıksız, ilk harflerden aklıma gelmiyor". Sıra bir mantıkla ilerliyorsa
# (evreler, süreçler, gelişim basamakları) kod zorlanmaz: her adım + bir sonrakine NEDEN geçildiği tek cümle.
ZINCIR_CSS = '''<style>
 .zc2{margin:10px 0;padding:2px 0 2px 14px;border-left:2px solid #e7c66a;page-break-inside:avoid;break-inside:avoid}
 .zc2 .t{font-size:9pt;font-weight:700;letter-spacing:.4px;text-transform:uppercase;color:#8a6400;margin-bottom:4px}
 .zc2 .ad{font-weight:700;color:#14335f;font-size:11pt}
 .zc2 .gc{color:#6b7a90;font-size:9.6pt;margin:1px 0 3px 10px}
 .zc2 .gc:before{content:"↓ ";color:#c08a00;font-weight:700}
 .zc2 .oz{margin-top:6px;font-size:9.8pt;color:#333}
</style>'''
SADE_CSS = SADE_CSS + ZINCIR_CSS


def mantik_zinciri(baslik, adimlar, ozet=None):
    """adimlar: [(adım, 'bir sonrakine neden geçilir'), ..., (son adım, '')]. Geçiş cümlesi kısa ve sebep bildiren olsun.
      mantik_zinciri('Ailenin evreleri', [('Şok', 'haberi kaldıramaz, gerçeği reddeder'), ('İnkâr', 'gerçek oturunca acı gelir'), …, ('Uyum', '')])"""
    s = ''
    for i, (ad, gecis) in enumerate(adimlar):
        s += f'<div class="ad">{ad}</div>'
        if gecis and i < len(adimlar) - 1: s += f'<div class="gc">{gecis}</div>'
    oz = f'<div class="oz">💬 {ozet}</div>' if ozet else ''
    return f'<div class="zc2"><div class="t">🔗 Mantık zinciri: {baslik}</div>{s}{oz}</div>'
