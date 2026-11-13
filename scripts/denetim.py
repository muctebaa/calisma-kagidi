"""Teslim öncesi denetim: kullanıcı kağıdı okumadan (ör. arkadaşlara) gönderebileceği için kalite kontrolü burada yapılır.
Kağıdı kaynakla karşılaştırır; KURAL koymaz, düzeltilecek şeyleri listeler. Her maddeyi okuyup karar ver.

    python3 -I denetim.py --kagit <build'in yazdığı .html> --kaynak <kaynak.txt | transkript.md | klasör> [--out denetim.md]

Bakılanlar:
  1. Kapsam: kaynaktaki sayılar (yıl, madde no, yaş aralığı, doz, yüzde) ve slayt başlıkları kağıtta var mı?
  2. Sorular: her test sorusunun doğru cevabı kağıdın anlatım kısmında geçiyor mu? (geçmiyorsa soru, öğretilmeyen bir şeyi soruyor)
  3. Okunabilirlik: çok uzun paragraflar (duvar gibi metin), bölüm başına kutu yoğunluğu.
"""
import sys, re, argparse, pathlib, subprocess, html as _html
from html.parser import HTMLParser

ap = argparse.ArgumentParser(); ap.add_argument('--kagit', required=True); ap.add_argument('--kaynak', required=True, nargs='+'); ap.add_argument('--out')
a = ap.parse_args()
HERE = pathlib.Path(__file__).parent

# ---------- kaynak metni ----------
kaynak = ''
for k in a.kaynak:
    p = pathlib.Path(k).expanduser()
    if p.is_dir() or p.suffix.lower() in ('.pptx', '.pdf', '.docx'):
        kaynak += subprocess.run([sys.executable, '-I', str(HERE / 'extract.py'), str(p)], capture_output=True, text=True).stdout
    else:
        kaynak += p.read_text(errors='ignore')
KAYNAKCA = re.compile(r'\(s\.\s*\d|\bdergisi\b|\d+\(\d+\),\s*\d+|^\s*\[\d+\]|^\s*===|,\s*(19|20)\d\d\s*[-–]\s*(19|20)\d\d\.?\s*$|et al\.|isbn|doi|https?://|press|publisher|university|lecture notes|edition|yayınları|yayınevi|\(\d{4}[a-z]?\)|,\s*(19|20)\d\d\.?\s*$|^\s*•?\s*[A-Z][a-z]+,\s*[A-Z]', re.I)
kaynak_satir, _dosya = [], ''
for l in kaynak.splitlines():
    if l.startswith('##### '): _dosya = l[6:].split('  (')[0]; continue
    if l.strip() and not l.startswith(('--- ', '[RESİM]', '[metin yok')) and not KAYNAKCA.search(l) and not re.match(r'^\s*kaynak\s*:', l, re.I):
        kaynak_satir.append((_dosya, l))

# ---------- kağıt: anlatım metni / soru-cevaplar / paragraflar ----------
class P(HTMLParser):
    def __init__(s):
        super().__init__(); s.yigin = []; s.anlatim = []; s.soru = []; s.paragraf = []; s.cur_p = None; s.bolum = None; s.bolum_kutu = {}
        s.cevaplar = []; s._an = None
    def handle_starttag(s, tag, attrs):
        c = dict(attrs).get('class', '') or ''
        sinav = 'exam' in c or ('tip' in c and 'brk' in c) or 'an' == c.strip()
        ust = s.yigin[-1][1] if s.yigin else False
        if tag in ('div', 'p', 'li', 'td', 'dd', 'dt', 'h2', 'h3', 'span', 'b', 'i', 'ol', 'ul', 'table', 'tr', 'dl', 'section'):
            s.yigin.append((tag, ust or sinav))
        if c.strip() == 'an': s._an = []
        if tag == 'h2': s.bolum = ''
        if tag == 'div' and any(x in c.split() for x in ('box', 'kav', 'trap', 'kd', 'zc2', 'ks', 'kt')) and s.bolum is not None:
            s.bolum_kutu[s.bolum_ad if hasattr(s, 'bolum_ad') else '?'] = s.bolum_kutu.get(getattr(s, 'bolum_ad', '?'), 0) + 1
        if tag == 'p' and not (ust or sinav): s.cur_p = []
    def handle_endtag(s, tag):
        if tag == 'p' and s.cur_p is not None:
            t = ' '.join(s.cur_p).strip()
            if t: s.paragraf.append(t)
            s.cur_p = None
        if tag == 'h2' and s.bolum is not None: s.bolum_ad = s.bolum.strip()[:60]; s.bolum = None
        if s.yigin and s.yigin[-1][0] == tag: s.yigin.pop()
        if tag == 'div' and s._an is not None and not any(t == 'div' for t, _ in s.yigin[-1:]):
            pass
    def handle_data(s, d):
        if s.bolum is not None and s.yigin and s.yigin[-1][0] == 'h2': s.bolum += d
        sinav = s.yigin[-1][1] if s.yigin else False
        (s.soru if sinav else s.anlatim).append(d)
        if s.cur_p is not None: s.cur_p.append(d)
        if s._an is not None: s._an.append(d)

h = pathlib.Path(a.kagit).read_text()
h = re.sub(r'<style.*?</style>', ' ', h, flags=re.S)
pr = P(); pr.feed(h)
anlatim = _html.unescape(' '.join(pr.anlatim)); anlatim_l = anlatim.lower()
tum = _html.unescape(re.sub(r'<[^>]+>', ' ', h)).lower()

# ---------- 1. kapsam: sayılar ----------
SAYI = re.compile(r'(?<![\w.,])(\d{1,2}\.\d{1,2}\.\d{4}|\d{1,6}(?:[.,]\d+)?(?:\s?[–-]\s?\d{1,6})?)\s?(%|yaş|yıl|madde|sayılı|mg|g/dl|mg/dl|mmhg|meq|ml|kg|°c|saat|gün|ay)?', re.I)
eksik_sayi = []
for dosya, l in kaynak_satir:
    if len(l.split()) < 3: continue
    for m in SAYI.finditer(l):
        n = m.group(1).replace(' ', '')
        if len(re.sub(r'\D', '', n)) < 2 and not m.group(2): continue           # tek haneli çıplak sayılar (madde no vb.) atlanır
        if l[max(0, m.start() - 1):m.start()] == '%': n = '%' + n                   # %15 gibi
        n_ = n.lstrip('%')
        varyant = {n_, n_.replace('-', '–'), n_.replace('–', '-'), n_.replace(',', '.'), n_.replace('.', ',')}
        birim = (m.group(2) or ('%' if n.startswith('%') else '')).lower()
        if birim in ('yıl', 'yaş') and re.fullmatch(r'(1[5-9]|20)\d\d', n_): birim = ''      # "1900 yılında" → kağıtta "1900" yeterli
        if birim:   # birimli sayı: sayı + birim birlikte geçmeli (%15, 15 mg, 0–8 yaş)
            kalip = lambda v: r'(?<![\d.,])(' + re.escape(v) + r'\s*' + re.escape(birim) + (r'|%\s?' + re.escape(v) if birim == '%' else '') + r')'
        else:
            kalip = lambda v: r'(?<![\d.,])' + re.escape(v) + r'(?![\d])'
        if not any(re.search(kalip(v), tum) for v in varyant):
            tarih = re.match(r'(\d{1,2})\.(\d{1,2})\.(\d{4})$', n)
            if tarih and re.search(r'(?<!\d)' + tarih.group(3) + r'(?!\d)', tum): n = n + ' (yılı var)'
            eksik_sayi.append((n + (' ' + m.group(2) if m.group(2) else ''), l.strip(), dosya))
eksik_sayi = list(dict.fromkeys(eksik_sayi))
# öncelik: hoca notu ([NOT]), ders akışı süreleri ve kişilerin yaşam yılları (1775–1838) düşük; kanun/madde/%/yaş/tek yıl yüksek
def oncelik(n, s_, d_=''):
    if s_.startswith('[NOT]') or re.search(r'ders akışı|dakika|≈\s*\d|grup(lar)? (oluştur|kur)|tartışın|kişilik grup|\bvaka\b|kararları \(\d', s_, re.I): return 2
    if re.fullmatch(r'\s*\d{4}\s*[–-]\s*\d{4}\s*', s_): return 2                     # zaman çizelgesi ara başlığı (1784 – 1990)
    if re.search(r'\d+\.\s*hükümet|\bH\.\s*\d', s_, re.I): return 1                  # hükümet görev tarihleri
    if '(yılı var)' in n or re.search(r'\bRG\s*\d|sayılı resm[iî] gazete|tebliğler dergisi|karar no', s_, re.I): return 1
    if re.match(r'^\d{4}\s?[–-]\s?\d{4}$', n) and re.search(r'\(\s*' + re.escape(n[:4]), s_): return 1
    return 0
eksik_sayi = sorted(eksik_sayi, key=lambda x: oncelik(*x))
dusuk = [x for x in eksik_sayi if oncelik(*x) > 0]; eksik_sayi = [x for x in eksik_sayi if oncelik(*x) == 0]

# ---------- 1b. kapsam: slayt başlıkları / defter başlıkları ----------
STOP = set('ve ile bir bu için olarak da de the of and to in a an is are for on with'.split())
BOS_BASLIK = re.compile(r'^(recommended|sources?|references?|kaynaklar|kaynakça|outline|contents?|agenda|içindekiler|thank you|teşekkürler|questions\??|sorular\??|summary|özet)\b', re.I)
basliklar = []
for blok in re.split(r'\n--- (?:slayt|sayfa) \d+\n', kaynak):
    ilk = next((l.strip() for l in blok.splitlines() if l.strip() and not l.startswith(('#', '[', '---'))), '')
    if 2 <= len(ilk.split()) <= 8 and not re.match(r'^\d', ilk): basliklar.append(ilk)
for _d, l in kaynak_satir:                               # transkript/defter: "Başlık:" satırları
    m = re.match(r'^\s*\**\s*([A-ZÇĞİÖŞÜ][^:]{3,60}):\s*$', l)
    if m: basliklar.append(m.group(1))
eksik_baslik = []
for b_ in dict.fromkeys(basliklar):
    if BOS_BASLIK.match(b_.strip()): continue
    kel = [w for w in re.findall(r'[\wçğıöşü]{4,}', b_.lower()) if w not in STOP]
    if not kel: continue
    bulunan = sum(1 for w in kel if w[:6] in tum)
    if bulunan / len(kel) < 0.6: eksik_baslik.append(b_)

# ---------- 2. sorular: cevap anlatımda var mı ----------
ogretilmemis = []
for m in re.finditer(r'<b>([SQ]\d+) → ([A-E])\)</b>\s*<i>(.*?)</i>', h, re.S):
    no, harf, cevap = m.group(1), m.group(2), _html.unescape(re.sub(r'<[^>]+>', '', m.group(3)))
    kel = [w for w in re.findall(r'[\wçğıöşüÇĞİÖŞÜ]{4,}', cevap.lower()) if w not in STOP]
    if not kel: continue
    bulunan = sum(1 for w in kel if w[:5] in anlatim_l)
    if bulunan / len(kel) < 0.5: ogretilmemis.append((no, cevap[:80]))

# ---------- 3. okunabilirlik ----------
uzun = [p_ for p_ in pr.paragraf if len(p_.split()) > 90]
kalabalik = {b_: n for b_, n in pr.bolum_kutu.items() if n > 6}

# ---------- rapor ----------
L = ['# Teslim öncesi denetim', '', f'Kağıt: {a.kagit}', '',
     '_Bu liste kural değil, bakılacak yerlerdir. Her maddeyi kaynağa ve öğretme amacına göre değerlendir: gerçekten eksikse ekle, önemsizse geç._', '']
L += [f'## 1. Kaynakta olup kağıtta olmayan sayılar ({len(eksik_sayi)} önemli olabilir · {len(dusuk)} düşük öncelik)', '',
      '_Önemli olabilir: yıl, kanun/madde no, yüzde, yaş, miktar. Sınavda “hangi yıl / kaç” diye sorulabilecekleri ekle._', '']
L += [f'- **{n}** · {d_[:38]} · “{s[:120]}”' for n, s, d_ in eksik_sayi[:120]] or ['- yok']
if dusuk: L += ['', f'<details>Düşük öncelik ({len(dusuk)}): hoca notları, ders akışı, kişilerin yaşam yılları — genelde gerekmez.</details>']
L += ['', f'## 2. Kağıtta karşılığı zayıf başlıklar ({len(eksik_baslik)})', '', '_Başlık kelimelerinin yarısından azı kağıtta geçiyor: konu atlanmış olabilir (ya da farklı adla anlatılmış)._', '']
L += [f'- {b_}' for b_ in eksik_baslik[:40]] or ['- yok']
L += ['', f'## 3. Cevabı anlatımda geçmeyen sorular ({len(ogretilmemis)})', '', '_Soru, kağıtta öğretilmeyen bir şeyi soruyor olabilir: ya anlatıma ekle ya soruyu değiştir._', '']
L += [f'- {no}: “{c}”' for no, c in ogretilmemis] or ['- yok']
L += ['', f'## 4. Okunabilirlik', '']
L += [f'- Uzun paragraf ({len(p_.split())} kelime): “{p_[:90]}…” → öz cümle + ayrıntıya böl' for p_ in uzun[:10]] or ['- uzun paragraf yok']
L += [f'- Kutu yoğun bölüm: {b_} ({n} kutu) → bir kısmını düz anlatıma çevir' for b_, n in kalabalik.items()]
L += ['', '## 5. Öğrenci gözüyle okuma (elle, her kağıtta)', '',
      '- [ ] Kağıdı baştan sona, konuyu ilk kez gören biri gibi oku (preview ile sayfalara bak).',
      '- [ ] Tanımı verilmeden kullanılan terim var mı?',
      '- [ ] Her bölümün ilk cümleleri “bu konu ne?” sorusunu cevaplıyor mu?',
      '- [ ] Ezber aracı (kod, zincir) gerçekten kolaylaştırıyor mu, yoksa yük mü?',
      '- [ ] Sorular, kağıdı okuyan birinin cevaplayabileceği şeyleri mi soruyor?',
      '- [ ] Yazım/ad hataları (özel adlar, terimler) var mı?']
rapor = '\n'.join(L) + '\n'
out = pathlib.Path(a.out) if a.out else pathlib.Path(a.kagit).with_name('denetim.md')
out.write_text(rapor)
print(f'sayı eksik {len(eksik_sayi)} (+{len(dusuk)} düşük) · başlık zayıf {len(eksik_baslik)} · öğretilmemiş soru {len(ogretilmemis)} · uzun paragraf {len(uzun)} → {out}')
