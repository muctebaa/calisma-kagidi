import sys, pathlib
sys.path.insert(0, str(pathlib.Path.home() / '.claude/skills/calisma-kagidi/scripts'))
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from kagit import Kagit
from gl import gloss, GL
import ortak
D = pathlib.Path(__file__).parent  # kaynak metinler (k_*.txt) scratchpad'deydi; yeniden üretmek için analiz.py/extract.py çalıştır
DERS = D / 'cikti'; DERS.mkdir(exist_ok=True)   # PDF'in kopyalanacağı klasör
k = Kagit('Tıbbi Biyoloji Çalışma Kağıdı', mode='en', gloss=gloss)
k.qprefix = 'Q'
k.add(ortak.CSS)

BOLUMLER = [('1', 'Hücre ve yaşam, hücre kuramı, hücrenin işleri', 'Intro (S. Yılmaz)'),
            ('2', 'Hücre biyolojisinin tarihi: kim, ne zaman, ne buldu', 'Intro'),
            ('3', 'Hücrenin kökeni ve evrimi, endosimbiyoz', 'Intro'),
            ('4', 'Sınıflandırma: 3 domain, 6 kingdom', 'Intro'),
            ('5', 'Prokaryot, ökaryot, arkeler', 'Intro'),
            ('6', 'Virüsler', 'Intro'),
            ('7', 'Zigot, kök hücre, organizasyon düzeyleri', 'Intro'),
            ('8', 'Enerji: ototrof, heterotrof, ATP', 'Intro'),
            ('9', 'Hücrenin molekülleri, genom, mutasyon', 'Intro')]

import s_intro
MODULLER = [s_intro]
for ad in ['s_c1', 's_c2', 's_mito', 's_mt', 's_c3', 's_adh', 's_ecm']:
    try:
        m = __import__(ad); MODULLER.append(m); BOLUMLER += getattr(m, 'BOLUMLER', [])
    except ModuleNotFoundError:
        pass

k.cover('Medical Biology – Tıbbi Biyoloji', 'Çalışma Kağıdı · Türkçe anlatım, İngilizce terimler · test sınavına göre',
        basliklar=('Bölüm', 'Konu', 'Kaynak'), bolumler=BOLUMLER,
        oneri='Konular <b>Türkçe</b> anlatıldı; sınavda karşına çıkacak <b>terimler İngilizce</b>, yanında parantez içinde Türkçesi. '
              'Her bölümün sonunda sınav gibi <b>İngilizce test soruları</b> var; cevap ve <b>Türkçe açıklama</b> hemen altında, sorudaki İngilizce kelimelerin anlamı yeşil kutucuklarda. '
              'Slaytta olmayıp açıklama için eklenen bilgiler <b>"genel bilgi"</b> diye işaretlendi. En sonda bütün kavramların özeti ve İngilizce–Türkçe terim sözlüğü var.')
for m in MODULLER:
    m.yaz(k)

k.summary()
k.h2('İngilizce – Türkçe terim sözlüğü (A–Z)')
items = sorted(((a, b) for a, b in GL.items() if len(a.split()) <= 3 and a not in ('which of the following', 'is not', 'all of the above', 'none of the above')), key=lambda x: x[0].lower())
h = (len(items) + 2) // 3
cols = [items[i * h:(i + 1) * h] for i in range(3)]
rows = ''.join('<tr>' + ''.join((f'<td><b>{c[r][0]}</b></td><td>{c[r][1]}</td>' if r < len(c) else '<td></td><td></td>') for c in cols) + '</tr>' for r in range(h))
k.add('<style>table.gl td{font-size:8pt;padding:1.5px 5px} table.gl td:nth-child(2n){color:#17652f;border-right:2px solid #bbb}</style>')
k.add(f'<table class="gl">{rows}</table>')
k.build(D / 'tb.pdf', copy_to=DERS / 'Tibbi_Biyoloji_Calisma_Kagidi.pdf', open_pdf=False)
