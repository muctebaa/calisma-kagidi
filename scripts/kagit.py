"""Çalışma kağıdı kütüphanesi: HTML yardımcıları + PDF üretimi + kontrol.

Kullanım (build script içinde):
    import sys; sys.path.insert(0, '<skill>/scripts'); from kagit import Kagit
    k = Kagit('Ders Adı Çalışma Kağıdı', mode='tr')   # 'tr' = sadece Türkçe, 'en' = İngilizce alıntı + yeşil kelime
    k.cover('AEF411 – Özel Eğitim', 'Çalışma Kağıdı', hoca='...', bolumler=[('1', 'Konu', 'Sunum')])
    k.h2('1. Bölüm'); k.add(k.KAV(('Terim', 'Tanım'))); k.add(k.EXAM((soru, [A,B,C,D], 'B', 'neden')))
    k.summary(); k.build('/çıktı/yolu.pdf')
"""
import pathlib, re, subprocess, shutil, random, html as _html
from collections import Counter

HERE = pathlib.Path(__file__).parent
CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
LETTERS = 'ABCDE'
UNSAFE_OPT = re.compile(r'hepsi|hiçbiri|yukarıdaki|all of the above|none of the above|both|[IV]+\s*ve\s*[IV]+|^[IV]+(,|$)', re.I)


class Kagit:
    def __init__(self, title, mode='tr', balance=True, gloss=None):
        self.title, self.mode, self.balance = title, mode, balance
        self.H, self.KEY, self.KAVLIST, self._pend = [], [], [], []
        self.gloss = gloss          # mode='en': metin -> [(terim, anlam)] döndüren fonksiyon (sorulardaki kelimeler)
        self.qprefix = 'S' if mode == 'tr' else 'Q'

    # ---------- temel ----------
    def add(self, *parts):
        # Başlıklar bir sonraki parçayla birlikte tutulur: sayfa sonunda başlık yalnız kalmaz.
        for p in parts:
            if self._pend:
                heads = ''.join(self._pend); self._pend = []
                if p.lstrip().startswith('<table'):
                    p = p.replace('>', f'><caption class="hcap">{heads}</caption>', 1)
                elif len(re.sub(r'<[^>]+>', '', p)) < 1800:
                    p = f'<div class="keep">{heads}{p}</div>'
                else:
                    p = heads + p
            self.H.append(p)
    def _head(self, html):
        self._pend.append(html)
    def h2(self, t, pb=True):
        if pb and self.H: self.H.append('<div class="pb"></div>')
        self._head(f'<h2>{t}</h2>')
    def h3(self, t): self._head(f'<h3>{t}</h3>')
    def p(self, t): self.add(f'<p>{t}</p>')
    def ul(self, *items): self.add('<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>')

    # ---------- kutular ----------
    def KAV(self, *pairs, title='🧠 Ezberlenecek kavramlar'):
        self.KAVLIST.extend(pairs)
        return f'<div class="kav"><div class="title">{title}</div><dl>' + ''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a, b in pairs) + '</dl></div>'
    @staticmethod
    def TIP(title, body, cls='tip'): return f'<div class="box {cls}"><div class="title">{title}</div>{body}</div>'
    @staticmethod
    def TRAP(title, body): return f'<div class="trap"><div class="title">⚠️ Dikkat: {title}</div>{body}</div>'
    @staticmethod
    def EZBER(*lines): return '<div class="box ezber"><div class="title">⭐ Ezberle</div><ul>' + ''.join(f'<li><b>{l}</b></li>' for l in lines) + '</ul></div>'
    @staticmethod
    def FLOW(t): return f'<div class="flow">{t}</div>'
    @staticmethod
    def TABLE(hdr, rows, cls='cmp'):
        # kısa tablo (≤10 satır, kısa metin) sayfada BÖLÜNMEZ; sığmazsa bütün olarak sonraki sayfaya geçer (12 Kas: "tablo arka sayfaya akmış")
        kisa = len(rows) <= 10 and sum(len(re.sub(r'<[^>]+>', '', str(c))) for r in rows for c in r) < 1400
        st = ' style="page-break-inside:avoid;break-inside:avoid"' if kisa else ''
        return f'<table class="{cls}"{st}><tr>' + ''.join(f'<th>{h}</th>' for h in hdr) + '</tr>' + ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows) + '</table>'
    # ---------- şemalar ve görseller ----------
    @staticmethod
    def _fig(body, title=None, note=None):
        t = f'<div class="ftitle">📊 {title}</div>' if title else ''
        n = f'<div class="fnote">{note}</div>' if note else ''
        return f'<div class="fig">{t}{body}{n}</div>'
    @classmethod
    def CHAIN(cls, items, title=None, note=None):
        """Kutu → kutu → kutu (süreç/zaman çizelgesi). items: str ya da (başlık, alt yazı)"""
        boxes = []
        for it in items:
            a, b = (it, '') if isinstance(it, str) else it
            boxes.append(f'<div class="cbox"><b>{a}</b>{f"<span>{b}</span>" if b else ""}</div>')
        return cls._fig('<div class="chain">' + '<div class="carr">➜</div>'.join(boxes) + '</div>', title, note)
    @classmethod
    def HUB(cls, center, items, title=None, note=None):
        """Merkez kavram + çevresindeki öğeler (SmartArt tarzı)."""
        cells = ''.join(f'<div class="hitem">{i}</div>' for i in items)
        return cls._fig(f'<div class="hub"><div class="hcenter">{center}</div><div class="hitems">{cells}</div></div>', title, note)
    @classmethod
    def PYRAMID(cls, levels, top='', bottom='', title=None, note=None):
        """Yukarıdan aşağı daralan ters piramit (en az → en çok kısıtlayıcı gibi)."""
        n = len(levels); rows = []
        for i, l in enumerate(levels):
            w = 100 - i * (55 / max(n - 1, 1))
            rows.append(f'<div class="plev" style="width:{w:.0f}%;background:hsl(215,55%,{38 + i * 5}%)">{l}</div>')
        lab = lambda x: f'<div class="plab">{x}</div>' if x else ''
        return cls._fig(lab(top) + '<div class="pyr2">' + ''.join(rows) + '</div>' + lab(bottom), title, note)
    @classmethod
    def BARS(cls, data, title=None, note=None, unit=''):
        """Yatay çubuk grafik. data: [(etiket, değer)]"""
        mx = max(v for _, v in data) or 1
        def fmt(v): return f'{v:,}'.replace(',', '.') if isinstance(v, int) else str(v).replace('.', ',')
        rows = ''.join(f'<div class="brow"><div class="blab">{a}</div><div class="btrack"><div class="bbar" style="width:{max(v / mx * 100, 1.5):.1f}%"></div></div><div class="bval">{fmt(v)}{unit}</div></div>' for a, v in data)
        return cls._fig(f'<div class="bars">{rows}</div>', title, note)
    @classmethod
    def FIG(cls, path, title=None, note=None, width=80):
        """Slayttaki resmi/şemayı gömer (base64 JPEG, PDF tek dosya kalır)."""
        import base64, io
        from PIL import Image
        im = Image.open(path).convert('RGB'); im.thumbnail((1600, 1600))
        buf = io.BytesIO(); im.save(buf, 'JPEG', quality=82)
        src = 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
        return cls._fig(f'<img src="{src}" style="width:{width}%">', title, note)

    # İngilizce mod: slayt alıntısı + kelime çipleri
    @staticmethod
    def W(*pairs): return '<div class="words">🟢 ' + ''.join(f'<span class="w"><b>{a}</b> = {b}</span>' for a, b in pairs) + '</div>'
    @staticmethod
    def Q(en, gl, tr=None):
        s = f'<div class="sq"><p class="q">"{en}"</p><p class="gl">📖 {gl}</p>'
        return s + (f'<p class="tr">→ {tr}</p>' if tr else '') + '</div>'
    @staticmethod
    def SLIDE(*qs, lbl='SLAYTTA YAZAN'): return f'<div class="box slide"><div class="lbl">{lbl}</div>{"".join(qs)}</div>'

    # ---------- sorular (cevaplar hemen altında) ----------
    def _target(self):
        c = Counter(a for _, a, _ in self.KEY); m = min(c[L] for L in 'ABCD')
        cand = [L for L in 'ABCD' if c[L] == m]
        last = self.KEY[-1][1] if self.KEY else None
        if len(cand) > 1 and last in cand: cand.remove(last)
        return random.Random(len(self.KEY) * 7919 + 17).choice(cand)

    def EXAM(self, *qs, title='🎯 Sınavda böyle çıkabilir'):
        out = f'<div class="box exam brk"><div class="title">{title}</div>'
        answers = []
        for q, opts, ans, why in qs:
            opts = list(opts); n = len(self.KEY) + 1
            if self.balance and len(opts) == 4 and not any(UNSAFE_OPT.search(o) for o in opts) \
                    and not re.search(r'(^|[\s(])[A-Ea-e]\)', why) and 'şık' not in why:
                t = self._target(); i, j = LETTERS.index(ans), LETTERS.index(t)
                opts[i], opts[j] = opts[j], opts[i]; ans = t
            self.KEY.append((n, ans, why))
            o = ''.join(f'<li>{L}) {t}</li>' for L, t in zip(LETTERS, opts))
            out += f'<div class="qq"><p><span class="qn">{self.qprefix}{n}.</span> {q}</p><ol class="opts">{o}</ol></div>'
            terms = ''
            if self.gloss:
                tm = self.gloss(' '.join([q] + [x + ' ;' for x in opts]))
                if tm: terms = '<div class="words tm">📘 ' + ''.join(f'<span class="w"><b>{a}</b> = {b}</span>' for a, b in tm) + '</div>'
            answers.append(f'<div class="an"><p><b>{self.qprefix}{n} → {ans})</b> <i>{opts[LETTERS.index(ans)]}</i><br>{why}</p>{terms}</div>')
        out += '</div>'
        return out + f'<div class="box tip brk"><div class="title">✅ Cevaplar ve açıklamalar (önce kendin çöz!)</div>{"".join(answers)}</div>'

    # ---------- kapak / özet / hayrat ----------
    def cover(self, ders, alt='Çalışma Kağıdı', hoca=None, bolumler=None, oneri=None, legend=True, basliklar=('Bölüm', 'Konu', 'Kaynak')):
        s = f'<div class="cover"><h1>{ders}</h1><div style="font-size:14pt;font-weight:700;color:#1f4fa8">{alt}</div>'
        if hoca: s += f'<div style="margin:8px 0 0"><span class="pill">{hoca}</span></div>'
        if legend:
            s += '<table class="legend" style="margin-top:12px">'
            s += '<tr><td><div class="kav" style="margin:0;padding:3px 8px"><b style="color:#1f4fa8">Mavi kutu</b></div></td><td>Ezberlenecek kavramlar. Hepsi en sonda tek listede.</td></tr>'
            s += '<tr><td><div class="trap" style="margin:0;padding:3px 8px"><b style="color:#b00020">⚠️ Dikkat</b></div></td><td>Sınavda karıştırılabilecek noktalar</td></tr>'
            s += '<tr><td><div class="box exam" style="margin:0;padding:3px 8px">Kırmızı kutu</div></td><td>Örnek sorular. Cevaplar hemen altındaki kutuda.</td></tr>'
            if self.mode == 'en':
                s += '<tr><td><span class="w"><b>word</b> = kelime</span></td><td>İngilizce kelimeler ve Türkçe anlamları</td></tr>'
            s += '</table>'
        s += '</div>'
        self.add(s)
        if bolumler:
            hdr = ''.join(f'<th>{h}</th>' for h in list(basliklar)[:len(bolumler[0])])
            rows = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in bolumler)
            self.add(self.TIP('📌 Dersin haritası', f'<table><tr>{hdr}</tr>{rows}</table>' + (f'<p>{oneri}</p>' if oneri else '')))

    def summary(self, title='Tek sayfa özet: Ezberlenecek kavramların tamamı'):
        self.h2(title)
        self.add('<table><tr><th>Kavram</th><th>Kısa açıklama</th></tr>' + ''.join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a, b in self.KAVLIST) + '</table>')

    def hayrat(self, isim):   # isim zorunlu (kullanıcıya sor / hafızadan al)
        """Paylaşılan kağıtlar için: Mushaf hattıyla besmele + hayrat satırı + sayfa filigranı (sadece istenirse)."""
        self.H.insert(0, '<div style="position:fixed;top:50%;left:50%;transform:translate(-50%,-50%);font-family:\'Mishafi Gold\',\'Mishafi\',serif;font-size:260pt;line-height:1;color:#0f5a2a;opacity:.045;z-index:9999;pointer-events:none;direction:rtl">ٱللَّه</div>'
                      f'<div style="text-align:center;margin:0 0 10px"><div style="font-family:\'Mishafi Gold\',\'Mishafi\',serif;font-size:40pt;line-height:1.5;color:#0f5a2a;direction:rtl">بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ</div><div style="width:220px;margin:2px auto 6px;border-top:1.5px solid #b8975a"></div><div style="font-size:12.5pt;font-style:italic;font-weight:600;color:#6b5a2e">{isim} hayratıdır</div></div>')
        self.add(f'<div style="text-align:center;margin:22px 0 4px;padding:12px;border-top:2px solid #9fd5ab;page-break-inside:avoid"><div style="font-size:12pt;font-weight:700;color:#17652f">{isim}\'nın geçmişlerinin ruhuna bir Fatiha 🤲</div><div style="font-size:10pt;color:#555;margin-top:4px">Hata görülürse bildirilmesi rica olunur. Herkese kolay gelsin.</div></div>')

    # ---------- üretim ----------
    def html(self):
        if self._pend: self.H.extend(self._pend); self._pend = []
        css = (HERE / 'style.css').read_text()
        return f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>{_html.escape(self.title)}</title><style>{css}</style></head><body>\n' + '\n'.join(self.H) + '\n</body></html>'

    def build(self, pdf, copy_to=None, open_pdf=False):
        pdf = pathlib.Path(pdf); hp = pdf.with_suffix('.html')
        hp.write_text(self.html())
        subprocess.run([CHROME, '--headless=new', '--disable-gpu', '--no-pdf-header-footer', f'--print-to-pdf={pdf}', hp.resolve().as_uri()],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        try:
            import pypdf; pages = len(pypdf.PdfReader(str(pdf)).pages)
        except Exception: pages = '?'
        dist = sorted(Counter(a for _, a, _ in self.KEY).items())
        print(f'sayfa {pages} · soru {len(self.KEY)} {dist} · kavram {len(self.KAVLIST)}')
        print(' '.join(f'{n}{a}' for n, a, _ in self.KEY))
        if copy_to:
            dst = pathlib.Path(copy_to)
            subprocess.run(['osascript', '-e', f'tell application "Preview" to close (every document whose name is "{dst.name}")'], capture_output=True)
            shutil.copyfile(pdf, dst)
            assert dst.read_bytes() == pdf.read_bytes(), 'kopya doğrulanamadı'
            print('kopyalandı →', dst)
            if open_pdf: subprocess.run(['open', str(dst)])
        return pages
