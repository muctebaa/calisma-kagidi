"""PDF sayfalarını tek tek PNG yapar (PDFKit, pencere açmaz). Kağıda FIG ile koymak için.
python3 render_pages.py <pdf> <çıkış_klasörü> 3,7,10-12 [ölçek=2]"""
import sys, subprocess, pathlib, tempfile
from preview import SWIFT, pages_arg
import pypdf
pdf, out, spec = sys.argv[1], pathlib.Path(sys.argv[2]), sys.argv[3]
scale = sys.argv[4] if len(sys.argv) > 4 else '2'
out.mkdir(parents=True, exist_ok=True)
n = len(pypdf.PdfReader(pdf).pages); pages = pages_arg(spec, n)
sw = pathlib.Path(tempfile.mkdtemp()) / 'r.swift'; sw.write_text(SWIFT.replace('let s: CGFloat = 1.3', f'let s: CGFloat = {scale}'))
subprocess.run(['swift', str(sw), pdf, str(out)] + [str(p) for p in pages], check=True)
print('→', out, pages)
