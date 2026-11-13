"""PDF sayfalarını PNG montajına çevirir (görsel kontrol için). sips tablo hücrelerini siyah gösterdiği için PDFKit kullanır.

python3 preview.py <pdf> <çıkış.png> [sayfalar: 1,2,5-8 | son4] [sütun=4]
"""
import sys, subprocess, pathlib, tempfile

SWIFT = r'''
import PDFKit; import AppKit
let d = PDFDocument(url: URL(fileURLWithPath: CommandLine.arguments[1]))!
let out = CommandLine.arguments[2]
for a in CommandLine.arguments.dropFirst(3) {
  let i = Int(a)! - 1; let p = d.page(at: i)!; let b = p.bounds(for: .mediaBox); let s: CGFloat = 1.3
  let img = NSImage(size: NSSize(width: b.width*s, height: b.height*s))
  img.lockFocus(); NSColor.white.set(); NSRect(x:0,y:0,width:b.width*s,height:b.height*s).fill()
  let ctx = NSGraphicsContext.current!.cgContext; ctx.scaleBy(x: s, y: s); p.draw(with: .mediaBox, to: ctx); img.unlockFocus()
  let rep = NSBitmapImageRep(data: img.tiffRepresentation!)!
  try! rep.representation(using: .png, properties: [:])!.write(to: URL(fileURLWithPath: "\(out)/p\(a).png"))
}
'''

def pages_arg(spec, n):
    out = []
    for part in spec.split(','):
        if part.startswith('son'): k = int(part[3:]); out += range(n - k + 1, n + 1)
        elif '-' in part: a, b = map(int, part.split('-')); out += range(a, b + 1)
        else: out.append(int(part))
    return [p for p in out if 1 <= p <= n]

def main(pdf, png, spec='1-4', cols=4):
    import pypdf
    from PIL import Image
    n = len(pypdf.PdfReader(pdf).pages); pages = pages_arg(spec, n)
    tmp = pathlib.Path(tempfile.mkdtemp()); sw = tmp / 'r.swift'; sw.write_text(SWIFT)
    subprocess.run(['swift', str(sw), pdf, str(tmp)] + [str(p) for p in pages], check=True)
    ims = [Image.open(tmp / f'p{p}.png') for p in pages]
    w, h = ims[0].size; cols = min(int(cols), len(ims)); rows = (len(ims) + cols - 1) // cols
    m = Image.new('RGB', (w * cols, h * rows), 'white')
    for i, im in enumerate(ims): m.paste(im, ((i % cols) * w, (i // cols) * h))
    m.save(png); print(f'{n} sayfa, gösterilen: {pages} → {png}')

if __name__ == '__main__':
    main(*sys.argv[1:])
