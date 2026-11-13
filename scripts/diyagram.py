"""Hızlı tekrar kağıtları için inline SVG çizim yardımcıları (DFD, ağaç, Venn).

    from diyagram import svg, txt, ent, proc, store, arr, agac, venn3, FIG_CSS
    k.add(FIG_CSS)
    k.add(fig('Context diagram', svg(720, 300, proc(360,140,70,'0','RHMS') + ent(20,117,140,46,'Device') + arr(160,140,290,140,'data')),
              adimlar=['Ortaya tek daire', 'Etrafına kareler', 'Oklar + veri adı'], cumle='The whole system is one process.'))
"""

FIG_CSS = '''<style>
 svg{display:block;margin:6px auto;max-width:100%} svg text{font-family:Helvetica,Arial,sans-serif}
 .fig{border:1.5px solid #c9d6ea;border-radius:8px;padding:6px 10px;margin:8px 0;page-break-inside:avoid;break-inside:avoid;background:#fff;text-align:left}
 .fig .t{font-weight:700;color:#12305e;font-size:12pt}
 .steps{background:#eef4ff;border-left:4px solid #3b6fd8;padding:4px 10px;font-size:10pt;margin:4px 0}.steps ol{margin:2px 0 2px 18px;padding:0}
</style>'''

_DEFS = ('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
         '<path d="M0,0 L10,5 L0,10 z" fill="#222"/></marker></defs>')


def svg(w, h, body): return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}">{_DEFS}{body}</svg>'


def txt(x, y, s, size=11, w='400', c='#111', anchor='middle'):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{c}" text-anchor="{anchor}">{s}</text>'


def ent(x, y, w, h, s):
    """DFD external entity: kare/dikdörtgen."""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#fff6dd" stroke="#222" stroke-width="1.6"/>' + txt(x + w / 2, y + h / 2 + 4, s, 11, '700')


def proc(cx, cy, r, *lines):
    """DFD process: daire; ilk satır numara (kalın)."""
    out = f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#e6f6ea" stroke="#222" stroke-width="1.6"/>'
    y0 = cy - (len(lines) - 1) * 6.5 + 4
    for i, l in enumerate(lines): out += txt(cx, y0 + i * 13, l, 10.5, '700' if i == 0 else '400')
    return out


def store(x, y, w, s):
    """DFD data store: açık uçlu dikdörtgen. s = 'D1 Ad'."""
    a, b = s.split(' ', 1)
    return (f'<path d="M{x + w},{y} L{x},{y} L{x},{y + 28} L{x + w},{y + 28}" fill="#eef4ff" stroke="#222" stroke-width="1.6"/>'
            f'<line x1="{x + 30}" y1="{y}" x2="{x + 30}" y2="{y + 28}" stroke="#222" stroke-width="1.2"/>'
            + txt(x + 15, y + 18, a, 10.5, '700') + txt(x + 34, y + 18, b, 10.5, '400', anchor='start'))


def arr(x1, y1, x2, y2, s='', dx=0, dy=-5, anchor='middle'):
    out = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#222" stroke-width="1.4" marker-end="url(#ar)"/>'
    if s: out += txt((x1 + x2) / 2 + dx, (y1 + y2) / 2 + dy, s, 9.5, '400', '#b00020', anchor)
    return out


def agac(kok, dallar, w=780):
    """Top-down ağacı: dallar = [('Ana parça', 'alt1', 'alt2'), ...] (en çok 4–5 dal)."""
    n = len(dallar); step = w / n
    b = f'<rect x="{w / 2 - 90}" y="10" width="180" height="36" rx="4" fill="#12305e"/>' + txt(w / 2, 33, kok, 12, '700', '#fff')
    for i, (ad, *alt) in enumerate(dallar):
        cx = step * (i + 0.5)
        b += f'<line x1="{w / 2}" y1="46" x2="{cx}" y2="86" stroke="#222" stroke-width="1.4"/>'
        b += f'<rect x="{cx - 80}" y="86" width="160" height="32" rx="4" fill="#e6f6ea" stroke="#222"/>' + txt(cx, 107, ad, 11, '700')
        for j, s in enumerate(alt):
            x = cx - 45 * (len(alt) - 1) + j * 90
            b += f'<line x1="{cx}" y1="118" x2="{x}" y2="150" stroke="#222" stroke-width="1.2"/>'
            b += f'<rect x="{x - 44}" y="150" width="88" height="30" rx="3" fill="#fff" stroke="#888"/>' + txt(x, 169, s, 8.6)
    return svg(w, 190, b)


def venn3(a, b, c, sadece_a=(), sadece_b=(), sadece_c=(), ab=(), bc=(), ac=(), abc=()):
    """Üç kesişen daire: a sol üst, b sağ üst, c alt."""
    def blok(x, y, items, w='400', col='#111', size=10.5):
        return ''.join(txt(x, y + i * 14, s, size, w, col) for i, s in enumerate(items))
    body = ('<circle cx="260" cy="150" r="125" fill="#3b6fd8" fill-opacity="0.13" stroke="#3b6fd8" stroke-width="2"/>'
            '<circle cx="420" cy="150" r="125" fill="#2e9b55" fill-opacity="0.13" stroke="#2e9b55" stroke-width="2"/>'
            '<circle cx="340" cy="275" r="125" fill="#e0a800" fill-opacity="0.15" stroke="#c08a00" stroke-width="2"/>'
            + txt(170, 22, a, 13, '700', '#1f4fa8') + txt(510, 22, b, 13, '700', '#17652f') + txt(340, 396, c, 13, '700', '#8a6400')
            + blok(195, 105, sadece_a) + blok(490, 105, sadece_b) + blok(340, 330, sadece_c)
            + blok(340, 95, ab, '700') + blok(440, 245, bc, '700') + blok(240, 245, ac, '700') + blok(340, 190, abc, '700', '#b00020', 12))
    return svg(680, 400, body)


def fig(baslik, cizim, adimlar=(), cumle=None):
    s = '' if not adimlar else '<b>Nasıl çizilir?</b><ol>' + ''.join(f'<li>{a}</li>' for a in adimlar) + '</ol>'
    if cumle: s += f'<b>Kısa cümle:</b> {cumle}'
    return f'<div class="fig"><div class="t">{baslik}</div>{cizim}' + (f'<div class="steps">{s}</div>' if s else '') + '</div>'
