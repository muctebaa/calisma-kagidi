"""HTML gövdesindeki a/b bölmelerini kesir çizgili gösterime çevirir."""
import re
SUP = '²³⁴⁵⁶⁷⁸⁹⁰¹ⁿˣʸ⁻'
SUBC = '₀₁₂₃₄₅₆₇₈₉ₓᵧ'
ATOM = re.compile(r"[A-Za-z0-9.,∂μλπθ½√" + SUP + SUBC + r"']")
FUNCS = ('sin', 'cos', 'tan', 'sec', 'csc', 'cot', 'ln', 'arctan', 'arcsin')
LOG = []

def fr(a, b):
    return f'<span class="fr"><span class="nu">{a}</span><span class="de">{b}</span></span>'

def strip_tags(s): return re.sub(r'<[^>]+>', '', s)

def mathy(s):
    t = strip_tags(s)
    for w in re.findall(r'[A-Za-zçğıöşüÇĞİÖŞÜ]{3,}', t):
        if w not in FUNCS: return False
    return bool(t.strip())

def is_prime(h, i):
    return h[i] == "'" and not (i + 1 < len(h) and h[i + 1].isalpha() and h[i + 1].islower())

def left(h, j):
    """h[:j] sonundaki operandın başlangıç indeksi (yoksa None)."""
    i = j
    def grab_supers(i):
        while True:
            if i > 0 and h[i - 1] in SUP: i -= 1; continue
            for t in ('</sup>', '</sub>'):
                if h[i - len(t):i] == t:
                    k = h.rfind('<' + t[2:], 0, i - len(t))
                    if k >= 0: i = k; break
            else: return i
    i = grab_supers(i)
    if i > 0 and h[i - 1] == ')':
        d = 0; k = i - 1
        while k >= 0:
            if h[k] == ')': d += 1
            elif h[k] == '(':
                d -= 1
                if d == 0: break
            k -= 1
        if k < 0: return None
        i = k
    # atom karakterleri (ve içlerindeki sup/sub)
    while i > 0:
        c = h[i - 1]
        if c == "'" or (ATOM.match(c) and c != "'"):
            i -= 1; continue
        n = grab_supers(i)
        if n != i: i = n; continue
        break
    return i if i < j else None

def right(h, j):
    """h[j:] başındaki operandın bitiş indeksi."""
    i = j
    def grab_supers(i):
        while True:
            if i < len(h) and h[i] in SUP: i += 1; continue
            for t in ('<sup>', '<sub>'):
                if h.startswith(t, i):
                    k = h.find('</' + t[1:], i)
                    if k >= 0: i = k + len(t) + 1; break
            else: return i
    def paren(i):
        d = 0; k = i
        while k < len(h):
            if h[k] == '(': d += 1
            elif h[k] == ')':
                d -= 1
                if d == 0: return k + 1
            k += 1
        return None
    if i < len(h) and h[i] == '−': i += 1
    if i < len(h) and h[i] == '(':
        e = paren(i)
        if e is None: return None
        return grab_supers(e)
    st = i
    while i < len(h):
        if ATOM.match(h[i]) and (h[i] != "'" or is_prime(h, i)): i += 1; continue
        n = grab_supers(i)
        if n != i: i = n; continue
        break
    if i == st: return None
    word = strip_tags(h[st:i])
    if word in FUNCS and i < len(h) and h[i] == ' ':
        r = right(h, i + 1)
        if r: return r
    if i < len(h) and h[i] == '(':
        e = paren(i)
        if e: i = grab_supers(e)
    return i

def unwrap(s):
    if s.startswith('(') and s.endswith(')'):
        d = 0
        for k, c in enumerate(s):
            d += c == '('; d -= c == ')'
            if d == 0 and k < len(s) - 1: return s
        return s[1:-1]
    return s

def convert(html):
    head, sep, body = html.partition('<body>')
    out = []; i = 0; h = body
    intag = False; sup_depth = 0
    k = 0
    while k < len(h):
        c = h[k]
        if c == '<':
            e = h.find('>', k); tag = h[k:e + 1]
            if tag.startswith('<sup'): sup_depth += 1
            elif tag.startswith('</sup'): sup_depth -= 1
            k = e + 1; continue
        if c == '/' and sup_depth == 0:
            sp_l = h[k - 1] == ' ' and k >= 2 and h[k - 2] != ' '
            sp_r = k + 1 < len(h) and h[k + 1] == ' '
            if sp_l != sp_r: k += 1; continue
            lj = k - 1 if sp_l else k
            rj = k + 2 if sp_r else k + 1
            L = left(h, lj); R = right(h, rj)
            while R is not None and R > rj and h[R - 1] in '.,': R -= 1
            while L is not None and L < lj and h[L] in '.,': L += 1
            if L is not None and R is not None and L >= i:
                a, b = h[L:lj], h[rj:R]
                if mathy(a) and mathy(b):
                    LOG.append(f'{strip_tags(a)}  /  {strip_tags(b)}')
                    out.append(h[i:L]); out.append(fr(unwrap(a), unwrap(b)))
                    i = k = R; continue
        k += 1
    out.append(h[i:])
    return head + sep + ''.join(out)
