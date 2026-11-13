"""Ders materyalinden metin çıkarır: .pptx (slayt + SmartArt + not + resim listesi), .pdf, .docx, .txt.

python3 -I extract.py <dosya veya klasör>... [--img <çıkış klasörü>]
--img verilirse slaytlara bağlı resimler <çıkış>/<dosya>/slideN_*.ext olarak kaydedilir (resimli slaytları okumak için).
"""
import zipfile, re, sys, html, pathlib

def _paras(xml):
    out = []
    for p in re.findall(r'<a:p>.*?</a:p>', xml, re.S):
        t = ''.join(re.findall(r'<a:t>([^<]*)</a:t>', p))
        if t.strip(): out.append(html.unescape(t))
    return out

def pptx(path, imgdir=None):
    z = zipfile.ZipFile(path); names = z.namelist()
    slides = sorted([n for n in names if re.match(r'ppt/slides/slide\d+\.xml$', n)], key=lambda n: int(re.findall(r'\d+', n)[0]))
    for n in slides:
        no = int(re.findall(r'\d+', n)[0]); print(f'--- slayt {no}')
        for t in _paras(z.read(n).decode('utf8')): print(t)
        rel = n.replace('slides/', 'slides/_rels/') + '.rels'
        if rel in names:
            r = z.read(rel).decode()
            for tgt in re.findall(r'Target="\.\./diagrams/(data\d+\.xml)"', r):
                for t in _paras(z.read('ppt/diagrams/' + tgt).decode('utf8')): print('[SmartArt]', t)
            imgs = [m for m in re.findall(r'Target="\.\./media/([^"]+)"', r)]
            big = [m for m in imgs if z.getinfo('ppt/media/' + m).file_size > 5000]
            if big:
                print('[RESİM]', ', '.join(big))
                if imgdir:
                    d = pathlib.Path(imgdir) / pathlib.Path(path).stem; d.mkdir(parents=True, exist_ok=True)
                    for m in big: (d / f'slide{no}_{m}').write_bytes(z.read('ppt/media/' + m))
        nt = n.replace('slides/slide', 'notesSlides/notesSlide')
        if nt in names:
            t = ' '.join(_paras(z.read(nt).decode('utf8')))
            if len(t.strip()) > 5 and not t.strip().isdigit(): print('[NOT]', t)

def docx(path):
    x = zipfile.ZipFile(path).read('word/document.xml').decode('utf8')
    for p in re.findall(r'<w:p[ >].*?</w:p>', x, re.S):
        t = ''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>', p))
        if t.strip(): print(html.unescape(t))

def pdf(path):
    import pypdf
    for i, pg in enumerate(pypdf.PdfReader(path).pages, 1):
        print(f'--- sayfa {i}'); print(pg.extract_text() or '[metin yok: taranmış sayfa, görüntü olarak oku]')

def main(args):
    imgdir = None
    if '--img' in args: i = args.index('--img'); imgdir = args[i + 1]; args = args[:i] + args[i + 2:]
    files = []
    for a in args:
        p = pathlib.Path(a)
        files += sorted(x for x in p.iterdir() if x.is_file()) if p.is_dir() else [p]
    for f in files:
        ext = f.suffix.lower()
        if ext not in ('.pptx', '.pdf', '.docx', '.txt'):
            print(f'##### {f.name}  ({ext}: resim/diğer, ayrıca bak)'); continue
        print(f'##### {f.name}')
        {'.pptx': lambda: pptx(f, imgdir), '.pdf': lambda: pdf(f), '.docx': lambda: docx(f), '.txt': lambda: print(f.read_text())}[ext]()

if __name__ == '__main__':
    main(sys.argv[1:])
