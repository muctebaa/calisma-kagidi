"""Süzgeç: ders materyalini ölçer, analiz eder ve çalışma kağıdı planı çıkarır.

    python3 -I analiz.py <klasör veya dosyalar>... --out <scratch>/<ders>

Çıktı:
  analiz.md  : okunacak rapor (ağırlıklar, içerik tipleri, sıralama uyarıları, sınav biçimi ipuçları, öneriler)
  plan.json  : yeni.py --plan ile iskelete dönüşen plan (alan/dil/sınav, bölüm sırası, sayfa/soru bütçesi, kutu önerileri)
  kaynak.txt : extract.py çıktısı (bölüm yazarken buradan okunur)

Ölçülenler (birim = dosya; tek büyük dosyada "Chapter/Week/Bölüm/Hafta N" başlıklarından bölünür):
  hacim (slayt, kelime) · tanım · karşılaştırma · süreç/adım · örnek · formül · kod · tarih/sayı/madde · resimli slayt ·
  vurgu (önemli/exam/dikkat) · örnek soru tipleri (test, klasik, D/Y, boşluk, eşleştirme, hesaplama) · anahtar terimler ve
  hangi birimde tanımlanıp hangilerinde kullanıldığı (ileri referans = sıralama uyarısı).
"""
import sys, re, json, math, pathlib, subprocess, argparse, collections

HERE = pathlib.Path(__file__).parent
ap = argparse.ArgumentParser(); ap.add_argument('src', nargs='+'); ap.add_argument('--out', required=True)
a = ap.parse_args()
OUT = pathlib.Path(a.out); OUT.mkdir(parents=True, exist_ok=True)

URETIM = re.compile(r'Calisma_Kagidi|Hizli_Tekrar|Yonlendirmeli|Aciklamali|_Kagidi\.pdf$', re.I)   # bizim ürettiğimiz PDF'ler kaynak sayılmaz
girdi = []
for s_ in a.src:
    p_ = pathlib.Path(s_).expanduser()
    girdi += sorted(x for x in p_.iterdir() if x.is_file() and not x.name.startswith('.')) if p_.is_dir() else [p_]
atlanan = [x.name for x in girdi if URETIM.search(x.name)]
girdi = [str(x) for x in girdi if not URETIM.search(x.name)]
ham = subprocess.run([sys.executable, '-I', str(HERE / 'extract.py'), *girdi, '--img', str(OUT / 'img')], capture_output=True, text=True).stdout
(OUT / 'kaynak.txt').write_text(ham)

# ---------------- birimlere ve slaytlara böl ----------------
def nat(s): return [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', s)]
dosyalar, cur = [], None
for line in ham.splitlines():
    if line.startswith('##### '):
        cur = {'ad': line[6:].split('  (')[0], 'slaytlar': [], 'diger': '  (' in line}; dosyalar.append(cur); continue
    if cur is None: continue
    if re.match(r'--- (slayt|sayfa) \d+', line): cur['slaytlar'].append([]); continue
    if not cur['slaytlar']: cur['slaytlar'].append([])
    cur['slaytlar'][-1].append(line)
dosyalar = [d for d in dosyalar if not d['diger']]
# aynı adlı docx/pdf kopyalarından birini tut (pptx > docx > txt > pdf; pdf'te bitişik harf bozulması olur)
TERCIH = {'.pptx': 0, '.docx': 1, '.txt': 2, '.pdf': 3}
gruplar = collections.OrderedDict()
for d in dosyalar:
    st, ext = re.sub(r'\.[^.]+$', '', d['ad']).strip().lower(), (re.search(r'\.[^.]+$', d['ad']) or [''])[0].lower()
    gruplar.setdefault(st, []).append((TERCIH.get(ext, 9), d))
cift = [d['ad'] for g in gruplar.values() if len(g) > 1 for _, d in sorted(g, key=lambda x: x[0])[1:]]
dosyalar = [sorted(g, key=lambda x: x[0])[0][1] for g in gruplar.values()]
SINAV_D = re.compile(r"sınav|sinav|exam|midterm|vize|final|quiz|çıkmış|cikmis|past.?paper|sample.?question|soru", re.I)
LAB_D = re.compile(r"\blab|worksheet|ödev|odev|assignment|tutorial|uygulama|practice", re.I)
IZL_D = re.compile(r"syllabus|izlence|course outline|course information|ders bilgi|ders tanıtım", re.I)
TRS_D = re.compile(r"transcript|transkript|ders kaydı|kayıt|recording|deşifre", re.I)
for d in dosyalar:
    d['rol'] = ('izlence' if IZL_D.search(d['ad']) else 'sinav' if SINAV_D.search(d['ad']) else 'lab' if LAB_D.search(d['ad'])
                else 'transkript' if TRS_D.search(d['ad']) else 'ders')
ROMA = {'i': 1, 'ii': 2, 'iii': 3, 'iv': 4, 'v': 5, 'vi': 6, 'vii': 7, 'viii': 8, 'ix': 9, 'x': 10, 'xi': 11, 'xii': 12}
def sira(d):
    ad = re.sub(r'\b(i{1,3}|iv|v|vi{0,3}|ix|x|xi{0,2})\b', lambda m: str(ROMA[m.group(1).lower()]), d['ad'], flags=re.I)
    m = re.search(r'(?:week|hafta|lecture|lab|chapter|bölüm|unit|ders|ch)\s*[-_ ]*(\d+)', ad, re.I)
    return ({'izlence': -1, 'ders': 0, 'transkript': 1, 'lab': 2, 'sinav': 3}[d['rol']], int(m.group(1)) if m else 999, nat(ad))
dosyalar.sort(key=sira)

BOLUM = re.compile(r'^\s*(chapter|week|lecture|unit|part|module|bölüm|hafta|ünite|konu|ders)\s*[-:]?\s*\d+', re.I)
birimler = []
for d in dosyalar:
    parcalar, simdiki = [], None
    for i, s in enumerate(d['slaytlar']):
        ilk = next((l for l in s if l.strip() and not l.startswith('[')), '')
        if simdiki is None or (len(dosyalar) <= 2 and len(d['slaytlar']) > 30 and BOLUM.match(ilk) and len(simdiki['slaytlar']) > 3):
            simdiki = {'ad': d['ad'] + (f' · {ilk.strip()[:40]}' if parcalar or BOLUM.match(ilk) else ''), 'slaytlar': [], 'rol': d['rol']}; parcalar.append(simdiki)
        simdiki['slaytlar'].append(s)
    birimler += parcalar

# ---------------- ölçüm ----------------
TIP_DEGIL = set('analysis analyses emphasis synthesis hypothesis thesis basis oasis diploma diplomas aroma academia sympathy empathy telepathy apathy genesis catalysis'.split())
EN_SW = set('the is are of and to in that for with this be as on by it an or from which can'.split())
TR_SW = set('ve bir bu ile için olarak da de olan gibi daha çok en ise ya veya ki ne'.split())
P = {
 'tanim': re.compile(r"\b(is defined as|refers to|is called|is a|is an|are the|means)\b|(?:dır|dir|dur|dür|tır|tir|tur|tür)\.|\bdenir\b|\btanım|\bdefinition", re.I),
 'karsilastirma': re.compile(r"\bvs\.?\b|versus|difference|compare|comparison|advantages?|disadvantages?|\bfark|karşılaştır|avantaj|dezavantaj|benzerlik|whereas|on the other hand", re.I),
 'surec': re.compile(r"\bstep|stages?\b|phases?\b|process|procedure|algorithm|\badım|aşama|evre|süreç|basamak|→|->|\bfirst\b.*\bthen\b", re.I),
 'ornek': re.compile(r"\bexample|e\.g\.|for instance|\börnek|\bör\.|case study|vaka|scenario|senaryo", re.I),
 'vurgu': re.compile(r"important|önemli|exam|sınav|\bnote\b|dikkat|remember|unutma|key point|!{1,}", re.I),
 'tarih': re.compile(r"\b(1[5-9]\d\d|20[0-4]\d)\b|\bmadde\s*\d+|\bkanun|law no|article \d+|\b\d+\s*sayılı", re.I),
}
MATH = re.compile(r"[=∫∑√×÷∂]|d[xy]/d[xy]|\^|\b[a-z]\s*\(\s*[a-z]\s*\)|\b(solve|equation|derivative|integral|denklem|türev|integral|çöz)", re.I)
CODE = re.compile(r"[;{}]\s*$|^\s*(def |class |public |private |static |int |void |#include|import |print\(|console\.|for\s*\(|if\s*\(|return )")
SORU = {
 'test': re.compile(r"^\s*\(?[A-Ea-e][\).]\s+\S"),
 'dy': re.compile(r"true\s*/\s*false|doğru\s*/\s*yanlış|\bD\s*/\s*Y\b|\(\s*[TF]\s*\)", re.I),
 'bosluk': re.compile(r"\w[^\n]{0,60}?(_{4,}|\.{6,}|…{2,})[^\n]{0,60}?\w"),
 'eslestirme': re.compile(r"\bmatch (the|each|following)|eşleştiriniz|eşleştirin", re.I),
 'klasik': re.compile(r"^\s*(\d+[\).]\s*)?(explain|describe|discuss|compare|identify|why|what is|define|justify|differentiate|açıklayınız|tartışınız|karşılaştırınız|tanımlayınız|nedir|neden)\b", re.I),
 'hesap': re.compile(r"\b(solve|calculate|compute|find|hesaplayınız|çözünüz|bulunuz)\b", re.I),
}
SORU_DOSYA = re.compile(r"sınav|sinav|exam|midterm|final|quiz|çıkmış|cikmis|soru|question|sample|lab|worksheet|ödev|odev|assignment", re.I)

KALIP = set('''answer answers objective objectives general lab precautions precaution figure table note notes what who why how where when which there these this those
it they we you he she consider instructions instruction question questions example examples recommended source sources reference references
summary introduction conclusion outline contents agenda task tasks exercise exercises date name student cevap soru şekil tablo not örnek amaç amaçlar
giriş özet kaynaklar kaynak'''.split())
def terimler_tanim(text):
    out = []
    pat = r"(?m)^\s*[•\-–]?\s*([A-ZÇĞİÖŞÜ][\w’'\- ]{2,40}?)\s*(?::\s+\S+\s+\S+\s+\S+|\s(?:is|are|refers to|is defined as|means)\s+(?:a|an|the|used|defined|called)?\b)"
    for m in re.finditer(pat, text):
        t = m.group(1).strip(' -–•')
        ws = t.lower().split()
        if 1 <= len(ws) <= 5 and ws[0] not in EN_SW | TR_SW | KALIP and not re.search(r'\d', t): out.append(t)
    for m in re.finditer(r"(?:bu|buna|bunlara)?\s*([\wçğıöşü’'\- ]{3,40}?)\s+denir", text, re.I):
        t = m.group(1).strip(); out.append(t.split(' ', 3)[-1] if len(t.split()) > 4 else t)
    return out

veri, tum_terim = [], collections.OrderedDict()
for bi, b in enumerate(birimler):
    metin = '\n'.join(l for s in b['slaytlar'] for l in s if not l.startswith('[RESİM]') and not l.startswith('[metin yok'))
    metin = '\n'.join(l for l in metin.splitlines() if not re.search(r'et al\.|\(\d{4}\)|isbn|doi|https?://|recommended sources|references', l, re.I))
    satir = [l for l in metin.splitlines() if l.strip()]
    kel = re.findall(r"[\wçğıöşüÇĞİÖŞÜ’']+", metin)
    en = sum(w.lower() in EN_SW for w in kel); tr = sum(w.lower() in TR_SW for w in kel) + len(re.findall(r'[çğışöüÇĞİŞÖÜ]', metin)) / 6
    m = {k: len(p.findall(metin)) for k, p in P.items()}
    m['formul'] = sum(1 for l in satir if len(MATH.findall(l)) >= 2)
    m['kod'] = sum(1 for l in satir if CODE.search(l))
    m['tarih_farkli'] = len(set(re.findall(r'\b(1[5-9]\d\d|20[0-4]\d)\b', metin))) + len(set(re.findall(r'madde\s*\d+|\d+\s*sayılı|article \d+', metin, re.I)))   # altbilgide tekrar eden yıl sayılmaz
    # ezber yükü: kısa liste maddeleri, birimli sayılar, tıbbi/latince terim ekleri
    m['liste'] = sum(1 for l in satir if len(l.split()) <= 7 and re.match(r'^\s*([•\-–▪○●]|\d+[\).]|[a-z][\).])\s', l))
    m['birimli'] = len(re.findall(r'\d+(?:[.,]\d+)?\s?(?:mg|mcg|µg|g/dl|g/dL|mg/dl|mg/dL|mmol|mEq|IU|ml|mL|mmHg|bpm|/dk|/min|°C|kg)\b', metin))
    m['tip_terim'] = len([x for x in re.findall(r'\b\w{3,}(?:itis|itit|oma|emia|emi|algia|alji|ektomi|ectomy|ozis|osis|patia|pati|plazi|plasia|genez|genesis|lizis|lysis|stenoz|stenosis|trofi|trophy)\b', metin, re.I) if x.lower() not in TIP_DEGIL])
    m['resim'] = sum(1 for s in b['slaytlar'] if any(l.startswith('[RESİM]') for l in s))
    m['bos_slayt'] = sum(1 for s in b['slaytlar'] if len(' '.join(s).split()) < 6)
    m['soru'] = {k: sum(1 for l in satir if p.search(l)) for k, p in SORU.items()}
    m['soru_dosyasi'] = b['rol'] == 'sinav'; m['rol'] = b['rol']
    basliklar = [next((l.strip() for l in s if l.strip() and not l.startswith('[')), '') for s in b['slaytlar']]
    tt = terimler_tanim(metin)
    for t in tt: tum_terim.setdefault(t.lower(), {'ad': t, 'tanim': bi})
    veri.append({'ad': b['ad'], 'slayt': len(b['slaytlar']), 'kelime': len(kel), 'dil_en': en, 'dil_tr': tr, 'olcum': m,
                 'basliklar': [x for x in basliklar if 2 <= len(x.split()) <= 9][:40], 'terimler': list(dict.fromkeys(tt))[:40], 'metin': metin.lower()})

# terim kullanımı → ileri referans
ileri = []
for key, t in tum_terim.items():
    if len(key) < 4: continue
    kullan = [i for i, v in enumerate(veri) if len(re.findall(r'\b' + re.escape(key) + r'\b', v['metin'])) > 0]
    t['kullanim'] = kullan
    once = [i for i in kullan if i < t['tanim']]
    if once: ileri.append((t['ad'], once, t['tanim']))

# ---------------- karar ----------------
icerik = [v for v in veri if v['olcum']['rol'] not in ('sinav', 'izlence')] or veri
CARPAN = {'ders': 1.0, 'lab': 0.6, 'transkript': 0.35, 'sinav': 0, 'izlence': 0}
for v in veri: v['etkin'] = v['kelime'] * CARPAN[v['olcum']['rol']]
# izlence: sınav biçimi ve ağırlıkları, haftalık konu sırası
izl_satir = []
for v in veri:
    if v['olcum']['rol'] == 'izlence':
        izl_satir += [l.strip() for l in v['metin'].splitlines() if re.search(r'midterm|final|quiz|vize|ara sınav|exam|assessment|değerlendirme|%|percent|multiple choice|çoktan|written|yazılı|essay|klasik|project|proje|presentation|sunum|week\s*\d+|hafta\s*\d+', l, re.I)]
izl_bicim = []
izl_txt = ' '.join(izl_satir).lower()
if re.search(r'multiple.choice|çoktan seçmeli|\btest\b', izl_txt): izl_bicim.append('test')
if re.search(r'written|essay|open.ended|yazılı|klasik|short answer|kısa cevap', izl_txt): izl_bicim.append('klasik')
if re.search(r'true.?false|doğru.?yanlış', izl_txt): izl_bicim.append('dy')
TOP = lambda k: sum(v['olcum'][k] for v in icerik)
kelime = sum(v['kelime'] for v in icerik) or 1
satir_say = sum(len(v['metin'].splitlines()) for v in icerik) or 1
dil = 'en' if sum(v['dil_en'] for v in veri) > 1.3 * sum(v['dil_tr'] for v in veri) else 'tr'
oran_mat, oran_kod = TOP('formul') / satir_say, TOP('kod') / satir_say
adlar = ' '.join([str(x) for x in a.src] + [v['ad'] for v in veri])
IP_SAY = re.compile(r"\bmth|math|matemat|diferansiyel|differential|calculus|kalkülüs|fizik|physics|istatistik|statistic|olasılık|probability|muhasebe|accounting|cebir|algebra|sayısal|numerical|mekanik|mechanics|devre|circuit", re.I)
IP_KOD = re.compile(r"programming|programlama|object.oriented|\boop\b|java|python|c#|csharp|c\+\+|javascript|algorithm|algoritma|data structure|veri yapı|yazılım geliştirme|web dev|database|veritaban|sql", re.I)
ipucu = 'kod' if IP_KOD.search(adlar) else 'sayisal' if IP_SAY.search(adlar) else None
alan_metin = 'kod' if oran_kod > 0.06 else 'sayisal' if oran_mat > 0.10 else 'sozel'
alan = alan_metin if alan_metin != 'sozel' else (ipucu or 'sozel')
alan_neden = f'metinden {alan_metin}' + (f', ders adından {ipucu}' if ipucu else '')
IP_EZB = re.compile(r"\btıp\b|medicine|medical|anatom|fizyoloji|physiology|farmako|pharmac|patoloji|patholog|histoloji|histolog|biyokimya|biochem|hemşire|nursing|eczac|pharmacy|diş hek|dentist|mikrobiyo|microbio|hukuk|\blaw\b|kanun|mevzuat|legislation|\bisg\b|occupational", re.I)
taranmis = [v['ad'] for v in veri if v['slayt'] and v['kelime'] / v['slayt'] < 12]

soru_tip = collections.Counter()
for v in veri:
    rol = v['olcum']['rol']
    for k, n in v['olcum']['soru'].items():
        if rol in ('sinav', 'lab'): soru_tip[k] += n * (3 if rol == 'sinav' else 2)
        elif rol == 'ders' and k == 'test': soru_tip[k] += n          # slaytta quiz sorusu olabilir; anlatım cümleleri soru sayılmaz
sinav, sinav_neden = [], ''
kanit = {k: n for k, n in soru_tip.items() if n >= 3}
if kanit:
    if kanit.get('test', 0) >= 12: sinav.append('test')
    if kanit.get('klasik', 0) >= 3: sinav.append('klasik')
    if kanit.get('hesap', 0) >= 3 and alan == 'sayisal' and 'klasik' not in sinav: sinav.append('klasik')
    for k in ('dy', 'bosluk', 'eslestirme'):
        if kanit.get(k, 0) >= 3: sinav.append(k)
    sinav_neden = ('kaynaktaki soru kalıplarından (TAHMİN: lab/çalışma soruları sınavla aynı biçimde olmayabilir, kullanıcıya teyit ettir): '
                   + ', '.join(f'{k} {n}' for k, n in soru_tip.most_common() if n))
if izl_bicim:
    sinav = list(dict.fromkeys(izl_bicim + sinav)); sinav_neden = 'izlenceden: ' + ', '.join(izl_bicim) + ('; ' + sinav_neden if sinav_neden else '')
if not sinav:
    sinav = ['klasik'] if alan == 'sayisal' else ['test', 'klasik']
    sinav_neden = 'kaynakta soru örneği yok → BİLİNMİYOR; kullanıcıya sor (varsayılan: ' + '+'.join(sinav) + ')'

def norm(x, mx): return x / mx if mx else 0
mx = {k: max((v[k] for v in icerik), default=1) or 1 for k in ('etkin', 'slayt')}
mt = max((len(v['terimler']) for v in icerik), default=1) or 1
mv = max((v['olcum']['vurgu'] for v in icerik), default=1) or 1
for v in veri:
    v['agirlik'] = 0 if v['olcum']['rol'] in ('sinav', 'izlence') else round((0.5 * norm(v['etkin'], mx['etkin']) + 0.2 * norm(v['slayt'], mx['slayt'])
                         + 0.2 * norm(len(v['terimler']), mt) + 0.1 * norm(v['olcum']['vurgu'], mv)) * {'transkript': 0.6, 'lab': 0.8}.get(v['olcum']['rol'], 1), 3)
toplam_ag = sum(v['agirlik'] for v in icerik) or 1
sayfa_toplam = max(8, min(60, round(kelime / 220)))
for v in veri:
    r = v['agirlik'] / toplam_ag; o = v['olcum']
    if o['rol'] in ('sinav', 'izlence'): v['butce'] = {'sayfa': 0, 'test': 0, 'klasik': 0}
    else: v['butce'] = {'sayfa': 0, 'test': max(3, min(10, round(3 + 25 * r))) if 'test' in sinav else 0,
                        'klasik': max(1, min(4, round(1 + 8 * r))) if 'klasik' in sinav else 0}
    k = []
    if o['tanim'] >= 3 or len(v['terimler']) >= 3: k.append('tanım ağırlıklı: akışta her tanım bir öz cümle, bölüm sonunda tek kavram listesi')
    if o['karsilastirma'] >= 2: k.append('karşılaştırma: akıştan sonra yan yana sade tablo (+ gerçekten karışıyorsa tek dikkat notu)')
    if o['surec'] >= 2: k.append('süreç: akışı numaralı adımlar olarak yaz')
    if o['tarih_farkli'] >= 4: k.append('kronoloji: tarih/madde sırasıyla liste (zaman_cizelgesi; sayıları silme)')
    if o['formul'] >= 3 and o['formul'] / max(1, len(v['metin'].splitlines())) > 0.05: k.append('işlem: MTH201 adım formatı (cozum) + 💡 fikir')
    if o['kod'] >= 3: k.append('kod: kod + çıktısı, "ne yazdırır?" soruları')
    if o['ornek'] >= 2: k.append('örnekleri farklı değerlerle soruya çevir')
    if v['slayt'] and o['resim'] / v['slayt'] > 0.3: k.append('resimli slayt çok: resimleri Read ile oku / gerekirse diyagram.py')
    if o['vurgu'] >= 2: k.append('hocanın vurguları: altı çizili (vurgu)')
    satir_n = max(1, len(v['metin'].splitlines()))
    v['ezber_yuk'] = round((0.3 * o['liste'] + 3 * o['birimli'] + 3 * o['tip_terim']) / satir_n, 2)
    if v['ezber_yuk'] >= 0.35 or o['birimli'] >= 5 or o['tip_terim'] >= 5:
        k.append('ezber: ölçülü serpiştir (kodlama / katla-test / kart; normal değer, doz, sınıflama)')
    # baskın içerik → anlatım biçimi
    sat = max(1, len(v['metin'].splitlines()))
    puan = {'işlem': 3 * o['formul'] / sat, 'kod': 3 * o['kod'] / sat, 'karşılaştırma': o['karsilastirma'] / sat,
            'süreç': o['surec'] / sat, 'kronoloji': (o['tarih_farkli'] / sat) if o['tarih_farkli'] >= 4 else 0,
            'ezber': (3 * o['birimli'] + 3 * o['tip_terim']) / sat, 'tanım': (o['tanim'] + len(v['terimler'])) / sat}
    bas_tip = max(puan, key=puan.get) if max(puan.values()) > 0.02 else 'tanım'
    if bas_tip == 'işlem' and (oran_kod > 0.03 or ipucu == 'kod'): bas_tip = 'kod'      # kod dersinde ifade/atama satırları işlem sayılmaz
    if o['rol'] in ('izlence', 'sinav'): bas_tip = '-'
    v['baskin'] = bas_tip
    v['anlatim'] = {'işlem': 'adım (MTH201 düzeni: başta elimizde, tek cümle + bütün ara işlemler)', 'kod': 'kod + çıktı, satır satır açıklama',
                    'karşılaştırma': 'akış + yan yana sade tablo', 'süreç': 'numaralı adımlar (akış)', 'kronoloji': 'tarih sırasıyla akış',
                    'ezber': 'akış + ölçülü ezber araçları', 'tanım': 'akış (öz cümle + girintili ayrıntı/örnek)',
                    '-': 'anlatılmaz: biçim/kapsam bilgisi için okunur'}[bas_tip]
    v['kutular'] = k

ezber_ort = sum(v.get('ezber_yuk', 0) for v in icerik) / max(1, len(icerik))
ezber = bool(IP_EZB.search(adlar)) or ezber_ort >= 0.3 or sum(1 for v in icerik if any(x.startswith('EZBER') for x in v['kutular'])) >= max(1, len(icerik) // 3)
# sayfa tahmini: metin + sorular (+ İngilizce kaynakta kelime anlamları yer kaplar)
# anlatım kısmı kaynak hacmiyle karekök oranında büyür (çok uzun kaynak = daha çok süzme)
etkin_top = sum(v['etkin'] for v in icerik) or 1
metin_sayfa = max(6, min(45, 2.5 * math.sqrt(etkin_top / 100) * (1.3 if dil == 'en' else 1)))
for v in veri:
    if v['olcum']['rol'] in ('sinav', 'izlence'): continue
    b_ = v['butce']; b_['sayfa'] = max(1, round(metin_sayfa * v['agirlik'] / toplam_ag + b_['test'] * 0.28 + b_['klasik'] * 0.4))
sayfa_toplam = min(80, sum(v['butce']['sayfa'] for v in veri) + 3)
# ---------------- rapor ----------------
L = [f'# Kaynak analizi ({len(veri)} birim, {kelime} kelime)', '',
     f'**Öneri:** `--alan {alan} --dil {dil} --sinav {",".join(sinav)}` · tahmini {sayfa_toplam} sayfa', '',
     f'- Dil: İngilizce işaret {sum(v["dil_en"] for v in veri)} · Türkçe işaret {round(sum(v["dil_tr"] for v in veri))} → **{dil}**',
     f'- Alan: formül satırı oranı {oran_mat:.2f} · kod satırı oranı {oran_kod:.2f} · {alan_neden} → **{alan}**',
     f'- Sınav biçimi: {sinav_neden}',
     f'- Ezber yükü: ortalama {ezber_ort:.2f}' + (' → **ezber modu öner** (`--ezber`: kodlama, katla-test, kartlar, aralıklı tekrar)' if ezber else ' → normal')]
if cift: L.append(f'- Aynı dosyanın ikinci kopyası atlandı: {", ".join(cift)}')
if atlanan: L.append(f'- Atlanan (bizim ürettiğimiz kağıtlar): {", ".join(atlanan)}')
if taranmis: L.append(f'- ⚠️ Sayfa başına çok az metin (taranmış, formül görseli ya da resim ağırlıklı): {", ".join(taranmis)} → `montaj.py` ile görüntü olarak oku; ölçümler bu birimlerde eksik kalır')
L += ['', '## Birimler (kaynaktaki sırayla)', '', '| # | birim | slayt | kelime | ağırlık | sayfa | test | klasik | tanım | karş. | süreç | örnek | formül | kod | tarih | resim | vurgu |', '|' + '---|' * 17]
for i, v in enumerate(veri):
    o, bt = v['olcum'], v['butce']
    L.append(f"| {i + 1} | {v['ad'][:45]}{'' if o['rol'] == 'ders' else ' (' + o['rol'] + ')'} | {v['slayt']} | {v['kelime']} | {v['agirlik']} | {bt['sayfa']} | {bt['test']} | {bt['klasik']} | "
             f"{o['tanim']} | {o['karsilastirma']} | {o['surec']} | {o['ornek']} | {o['formul']} | {o['kod']} | {o['tarih']} | {o['resim']} | {o['vurgu']} |")
if izl_satir:
    L += ['', '## İzlenceden (sınav biçimi, ağırlıklar, haftalık sıra)', '', '_Tablo satırları bölünmüş olabilir: izlenceyi kaynak.txt’den ayrıca oku; haftalık konu sırası ve sınav kapsamı buradan alınır._', ''] + [f'- {x[:160]}' for x in dict.fromkeys(izl_satir[:30])]
L += ['', '## Birim bazında anlatım önerileri (sade format: kutu değil anlatım)', '']
for i, v in enumerate(veri):
    L.append(f"- **{i + 1}. {v['ad'][:50]}** · baskın: **{v.get('baskin', '-')}** → anlatım: **{v.get('anlatim', 'akış')}**")
    if v['kutular']: L.append('  - ' + '; '.join(v['kutular']))
    if v['terimler']: L.append(f"  - tanımlanan terimler: {', '.join(v['terimler'][:15])}")
L += ['', '## Sıralama (öğrenme sırası)', '']
if ileri:
    L.append('Aşağıdaki terimler **tanımlandıkları birimden önce** kullanılıyor. Ya tanımlayan birimi öne al ya da kağıdın başına '
             '"Önce bunu bil: temel kavramlar" bölümü koy:')
    for ad, once, td in ileri[:25]: L.append(f'- **{ad}**: tanım {td + 1}. birimde, önce kullanıldığı: {", ".join(str(x + 1) for x in once)}')
else:
    L.append('İleri referans bulunmadı → kaynak sırası korunabilir.')
L += ['', '## Karar listesi (kağıda başlamadan)', '',
      '1. Sınav biçimi kaynaktan çıkmadıysa kullanıcıya sor; çıktıysa ona göre kur.',
      '2. Ağırlığı düşük birimleri birleştir (pb=False), yüksekleri ayrı h2 + daha çok soru.',
      '3. Sınav/çıkmış soru dosyalarını birim olarak değil, soru biçimi ve konu dağılımı için kullan. Lablar hem içerik hem soru biçimi kaynağıdır: ilgili haftanın bölümüne bağla.',
      '4. Bu rapor bir ön bilgidir: her bölümü slaytı okuyarak, en iyi nasıl öğretileceğine göre kur.']
(OUT / 'analiz.md').write_text('\n'.join(L) + '\n')

plan = {'alan': alan, 'dil': dil, 'sinav': sinav, 'ezber': ezber, 'sayfa': sayfa_toplam, 'sinav_neden': sinav_neden,
        'temel_kavramlar': [x[0] for x in ileri[:15]],
        'birimler': [{'ad': v['ad'], 'slayt': v['slayt'], 'agirlik': v['agirlik'], 'butce': v['butce'], 'kutular': v['kutular'],
                      'terimler': v['terimler'][:15], 'baskin': v.get('baskin'), 'anlatim': v.get('anlatim'), 'basliklar': v['basliklar'][:12], 'soru_dosyasi': v['olcum']['soru_dosyasi']} for v in veri]}
(OUT / 'plan.json').write_text(json.dumps(plan, ensure_ascii=False, indent=1))
print('\n'.join(L[:L.index('## Birimler (kaynaktaki sırayla)') - 1]))
print(f'\nrapor → {OUT / "analiz.md"}\nplan  → {OUT / "plan.json"}')
