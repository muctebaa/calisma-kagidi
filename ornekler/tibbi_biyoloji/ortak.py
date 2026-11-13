"""Tıbbi biyoloji kağıdı: ortak yardımcılar. Anlatım Türkçe, terimler İngilizce + (Türkçe)."""
import re


def E(en, tr=None):
    """Metin içinde terim: **English** (Türkçe)"""
    return f'<b>{en}</b>' + (f' <span class="tp">({tr})</span>' if tr else '')


def T(en, tr):
    return f'{en} <span class="tp">({tr})</span>'


CSS = '''<style>
 .tp{color:#5a6b80;font-weight:400;font-size:92%}
 .kisi td:first-child{white-space:nowrap}
 .ipucu{background:#f3f8ef;border-left:5px solid #5aa05a}
</style>'''


def _t(x, y, s, size=10, w='400', c='#222', a='middle'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{c}" text-anchor="{a}" font-family="Helvetica,Arial">{s}</text>'


def zar_svg():
    """Akışkan mozaik zar: fosfolipit çift katmanı + kolesterol + integral / periferal / lipide bağlı protein + glikokaliks (+ altında açıklama)."""
    W, y1, y2, X0 = 760, 110, 190, 150
    s = ''
    for i in range(30):
        x = X0 + i * 20
        if X0 + 220 <= x <= X0 + 300: continue
        for yy, d in ((y1, 1), (y2, -1)):
            s += f'<circle cx="{x}" cy="{yy}" r="7" fill="#7fb3e6" stroke="#3a6ea5"/>'
            s += f'<line x1="{x - 3}" y1="{yy + 7 * d}" x2="{x - 3}" y2="{yy + 34 * d}" stroke="#d9a441" stroke-width="2"/>'
            s += f'<line x1="{x + 3}" y1="{yy + 7 * d}" x2="{x + 3}" y2="{yy + 34 * d}" stroke="#d9a441" stroke-width="2"/>'
    ix = X0 + 225
    s += f'<rect x="{ix}" y="88" width="70" height="125" rx="22" fill="#9ccc8b" stroke="#4f8a3c"/>' + _t(ix + 35, 155, 'integral', 10, '700')
    s += f'<path d="M{ix+35} 88 L{ix+35} 60 M{ix+35} 72 L{ix+20} 52 M{ix+35} 72 L{ix+50} 52" stroke="#b05aa8" stroke-width="3" fill="none"/>' + _t(ix + 80, 50, 'glycoprotein', 9, '400', '#b05aa8')
    s += f'<ellipse cx="{X0+400}" cy="212" rx="34" ry="16" fill="#f2c27b" stroke="#b5832e"/>' + _t(X0 + 400, 216, 'peripheral', 9, '700')
    s += f'<ellipse cx="{X0+520}" cy="226" rx="32" ry="15" fill="#e8a0a0" stroke="#a05050"/><line x1="{X0+520}" y1="211" x2="{X0+520}" y2="168" stroke="#a05050" stroke-width="3"/>' + _t(X0 + 520, 230, 'lipid-anchored', 8, '700')
    s += f'<path d="M{X0+80} 103 L{X0+80} 70 M{X0+80} 82 L{X0+68} 62 M{X0+80} 82 L{X0+92} 62" stroke="#b05aa8" stroke-width="3" fill="none"/>' + _t(X0 + 80, 56, 'glycolipid', 9, '400', '#b05aa8')
    s += f'<rect x="{X0+337}" y="124" width="12" height="26" rx="3" fill="#e05a5a" stroke="#fff" stroke-width="1"/>'
    s += f'<line x1="{X0+343}" y1="124" x2="{X0+343}" y2="70" stroke="#c03030" stroke-width="1" stroke-dasharray="3,2"/>' + _t(X0 + 343, 66, 'cholesterol', 9, '700', '#c03030')
    s += _t(8, 104, 'hydrophilic head', 9, '700', '#3a6ea5', 'start') + _t(8, 116, '(suyu seven baş)', 8, '400', '#3a6ea5', 'start')
    s += f'<line x1="104" y1="110" x2="{X0-8}" y2="110" stroke="#3a6ea5" stroke-width="1"/>'
    s += _t(8, 146, 'hydrophobic tails', 9, '700', '#a07020', 'start') + _t(8, 158, '(sudan kaçan kuyruk)', 8, '400', '#a07020', 'start')
    s += f'<line x1="112" y1="150" x2="{X0-6}" y2="132" stroke="#a07020" stroke-width="1"/>'
    s += _t(W / 2 + 40, 22, 'EXTRACELLULAR (exoplasmic face) · dış yüz: şeker zincirleri burada (glycocalyx)', 10, '700', '#555')
    s += _t(W / 2 + 40, 262, 'CYTOSOL (cytosolic face) · iç yüz', 10, '700', '#555')
    svg = f'<svg width="{W}" height="270" viewBox="0 0 {W} 270" style="display:block;margin:6px auto;max-width:100%">{s}</svg>'
    return ('<div style="page-break-inside:avoid;break-inside:avoid">' + svg +
            '<p class="small" style="text-align:center">Şekil (bu kağıt için çizildi): akışkan mozaik zar. Şeker zincirleri (glikoprotein, glikolipit) yalnız <b>dış yüzde</b>; kolesterol iki tabakada da.</p></div>')


def mito_svg():
    """Mitokondrinin 4 bölmesi: dış zar, zarlar arası boşluk, iç zar (kristalar), matriks."""
    s = '<ellipse cx="300" cy="140" rx="250" ry="105" fill="#fde8c8" stroke="#c07a1e" stroke-width="4"/>'
    s += '<ellipse cx="300" cy="140" rx="232" ry="88" fill="#fff7ea" stroke="#d98b2b" stroke-width="3"/>'
    import math
    for i, x in enumerate([120, 170, 220, 380, 430, 480]):
        up = i % 2 == 0
        h = 88 * math.sqrt(max(0, 1 - ((x - 300) / 232) ** 2))
        y0 = 140 - h + 2 if up else 140 + h - 2
        y1 = y0 + (h * 1.25) if up else y0 - (h * 1.25)
        s += f'<path d="M{x-10} {y0} L{x-10} {y1} Q{x} {y1 + (14 if up else -14)} {x+10} {y1} L{x+10} {y0}" fill="#fde8c8" stroke="#d98b2b" stroke-width="3"/>'
    s += '<circle cx="262" cy="190" r="7" fill="none" stroke="#7a3fb0" stroke-width="2"/><circle cx="345" cy="92" r="6" fill="none" stroke="#7a3fb0" stroke-width="2"/>'
    s += '<circle cx="330" cy="188" r="4" fill="#3a6ea5"/><circle cx="342" cy="194" r="4" fill="#3a6ea5"/><circle cx="255" cy="92" r="4" fill="#3a6ea5"/>'
    L = lambda x1, y1, x2, y2: f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#444" stroke-width="1"/>'
    s += L(560, 60, 520, 85) + _t(565, 58, 'Outer membrane', 10, '700', '#c07a1e', 'start') + _t(565, 71, '(dış zar)', 9, '400', '#c07a1e', 'start')
    s += L(560, 110, 538, 120) + _t(565, 108, 'Intermembrane space', 10, '700', '#a0601a', 'start') + _t(565, 121, '(zarlar arası boşluk: H⁺, sitokrom c)', 9, '400', '#a0601a', 'start')
    s += L(560, 165, 520, 170) + _t(565, 163, 'Inner membrane', 10, '700', '#d98b2b', 'start') + _t(565, 176, '(iç zar: ETZ + ATP sentaz)', 9, '400', '#d98b2b', 'start')
    s += L(560, 215, 482, 205) + _t(565, 213, 'Cristae', 10, '700', '#d98b2b', 'start') + _t(565, 226, '(kristalar: yüzey ↑)', 9, '400', '#d98b2b', 'start')
    s += _t(300, 140, 'MATRIX', 12, '700', '#7a3fb0') + _t(300, 154, '(Krebs, mtDNA ●, ribozom)', 9, '400', '#7a3fb0')
    svg = f'<svg width="760" height="270" viewBox="0 0 760 270" style="display:block;margin:6px auto;max-width:100%">{s}</svg>'
    return '<div style="page-break-inside:avoid;break-inside:avoid">' + svg + '<p class="small" style="text-align:center">Şekil (bu kağıt için çizildi): mitokondrinin 4 bölmesi. Mor halka = mtDNA (halkasal, histonsuz), mavi noktalar = mitokondri ribozomları.</p></div>'


def gecirgenlik_svg():
    """Lipit çift katmanı neyi geçirir? 4 grup molekül + oklar."""
    s = ''
    for y in range(30, 250, 14):
        s += f'<circle cx="430" cy="{y}" r="6" fill="#7fb3e6" stroke="#3a6ea5"/><circle cx="500" cy="{y}" r="6" fill="#7fb3e6" stroke="#3a6ea5"/>'
        s += f'<line x1="436" y1="{y}" x2="462" y2="{y}" stroke="#d9a441" stroke-width="2"/><line x1="468" y1="{y}" x2="494" y2="{y}" stroke="#d9a441" stroke-width="2"/>'
    rows = [('Hydrophobic molecules', 'hidrofobik', 'O₂, CO₂, N₂', '#5aa02c', True, 'kolay geçer'),
            ('Small uncharged polar', 'küçük yüksüz polar', 'H₂O, glycerol, ethanol', '#8fc46a', True, 'geçer (yavaş)'),
            ('Large uncharged polar', 'büyük yüksüz polar', 'glucose, sucrose', '#4a8aa8', False, 'geçemez → taşıyıcı'),
            ('Ions', 'iyonlar', 'Na⁺, K⁺, Cl⁻, Ca²⁺', '#3a5fb0', False, 'geçemez → kanal / pompa')]
    for i, (a, b, c, col, ok, d) in enumerate(rows):
        y = 40 + i * 58
        s += f'<rect x="10" y="{y-16}" width="190" height="40" rx="5" fill="{col}"/>' + _t(105, y, a, 10, '700', '#fff') + _t(105, y + 14, f'({b})', 9, '400', '#fff')
        s += _t(300, y + 4, c, 11, '700', '#222')
        if ok:
            s += f'<line x1="375" y1="{y}" x2="560" y2="{y}" stroke="{col}" stroke-width="5" marker-end="url(#ok)"/>' + _t(620, y + 4, d, 10, '700', '#2e7d32')
        else:
            s += f'<path d="M375 {y} L420 {y} Q426 {y+12} 410 {y+20} L385 {y+22}" stroke="{col}" stroke-width="5" fill="none" marker-end="url(#ok)"/>' + _t(620, y + 4, d, 10, '700', '#b00020')
    s += _t(465, 268, 'lipid bilayer (lipit çift katmanı)', 10, '700', '#555')
    defs = '<defs><marker id="ok" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#444"/></marker></defs>'
    svg = f'<svg width="720" height="280" viewBox="0 0 720 280" style="display:block;margin:6px auto;max-width:100%">{defs}{s}</svg>'
    return ('<div style="page-break-inside:avoid;break-inside:avoid">' + svg +
            '<p class="small" style="text-align:center">Şekil (bu kağıt için çizildi): boyut ve yük difüzyon hızını belirler. Polar ve yüklü maddeler çift katmandan geçemez; taşıyıcı, kanal ve pompalara ihtiyaç duyar.</p></div>')
