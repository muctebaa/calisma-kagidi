"""Taranmış / el yazısı PDF notlarını okumak için: sayfaları PNG'ye çevirir ve 2'li montaj yapar.

    python3 -I montaj.py <notlar.pdf> <çıkış_klasörü> [--dpi 110]

Çıkış: p01.png… (tek sayfa) ve m01.png… (2 sayfa yan yana). İlk 2 sayfayı tek tek, kalanları m*.png ile Read et;
okurken transkripti hemen bir .md dosyasına yaz (bağlam sıkışırsa kaybolmasın).
Metin katmanı olan PDF'lerde önce extract.py dene; bu araç metni olmayan taramalar içindir.
"""
import sys, pathlib, argparse
import pymupdf
from PIL import Image

ap = argparse.ArgumentParser(); ap.add_argument('pdf'); ap.add_argument('out'); ap.add_argument('--dpi', type=int, default=110)
a = ap.parse_args()
out = pathlib.Path(a.out); out.mkdir(parents=True, exist_ok=True)
d = pymupdf.open(a.pdf)
metin = sum(len(p.get_text()) for p in d)
fs = []
for i, p in enumerate(d):
    f = out / f'p{i + 1:02d}.png'; p.get_pixmap(dpi=a.dpi).save(f); fs.append(f)
for i in range(0, len(fs), 2):
    ims = [Image.open(f).convert('RGB') for f in fs[i:i + 2]]
    h = 1500; ims = [im.resize((int(im.width * h / im.height), h)) for im in ims]
    m = Image.new('RGB', (sum(im.width for im in ims) + 20, h), 'white'); x = 0
    for im in ims: m.paste(im, (x, 0)); x += im.width + 20
    m.save(out / f'm{i // 2 + 1:02d}.png')
print(f'{len(fs)} sayfa · metin katmanı {metin} karakter · montaj {(len(fs) + 1) // 2} → {out}')
