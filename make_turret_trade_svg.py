# Generates turret-trade.svg: option A (ground turntable) vs option B (top turret). Rotating parts in orange.
o = []
A = o.append
W, H = 1240, 760
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12.5">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern>'
  '<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:1.5}.l{stroke:#555;stroke-width:1;fill:none}.cab{stroke:#8e44ad;stroke-width:1.3}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:16px;font-weight:bold}</style>')
ROT, FIX = '#e67e22', '#888'
e, gy = 5.2, 660


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*14:.0f}" text-anchor="{anchor}">{t}</text>')


def rig(mid, turret):
    X = lambda m: mid + m * e
    Z = lambda m: gy - m * e
    A(f'<rect x="{mid-260}" y="{gy}" width="520" height="30" fill="url(#g)"/><line x1="{mid-260}" y1="{gy}" x2="{mid+260}" y2="{gy}" stroke="#222"/>')
    # bracing (fixed in both)
    for fx in (30, -15):
        A(f'<line x1="{X(fx)}" y1="{gy-2}" x2="{X(0)}" y2="{Z(62)}" class="cab"/>')
        A(f'<line x1="{X(fx)}" y1="{gy-2}" x2="{X(0)}" y2="{Z(35)}" stroke="#555" stroke-width="4"/>')
        A(f'<rect x="{X(fx)-7}" y="{gy-5}" width="14" height="5" fill="#555"/>')
    split = 64 if turret else 0
    # mast: fixed part grey, rotating part orange
    A(f'<rect x="{X(0)-3}" y="{Z(split)}" width="6" height="{split*e}" fill="{FIX}"/>' if split else '')
    A(f'<rect x="{X(0)-3}" y="{Z(105)}" width="6" height="{(105-split)*e}" fill="{ROT}"/>')
    # top yard + wings (rotating)
    A(f'<rect x="{X(-17.5)}" y="{Z(100)-2}" width="{35*e}" height="4" fill="{ROT}" class="s"/>')
    for sx in (-1, 1):
        xl, xr = sorted((X(sx * 2), X(sx * 17)))
        A(f'<rect x="{xl}" y="{Z(100)}" width="{xr-xl}" height="{30*e}" fill="#2c4a7a" stroke="{ROT}" stroke-width="3"/>')
    if turret:
        A(f'<rect x="{X(0)-14}" y="{Z(64)-6}" width="28" height="12" fill="{ROT}" class="s"/>')
        A(f'<rect x="{X(0)-8}" y="{Z(62)-3}" width="16" height="6" fill="{FIX}" class="s"/><rect x="{X(0)-8}" y="{Z(35)-3}" width="16" height="6" fill="{FIX}" class="s"/>')
        A(f'<rect x="{X(-4)}" y="{gy-10}" width="{8*e}" height="10" fill="{FIX}" class="s"/>')                 # foundation pad
        A(f'<line x1="{X(0)+5}" y1="{Z(2)}" x2="{X(0)+5}" y2="{Z(63)}" stroke="#2e7d32" stroke-width="2" stroke-dasharray="6 3"/>')  # service lift rail
    else:
        A(f'<rect x="{X(-1.5)}" y="{gy-12}" width="{3*e}" height="4" fill="{ROT}"/>')                 # rotating base frame
        A(f'<rect x="{X(-1.2)}" y="{gy-7}" width="{2.4*e}" height="7" fill="{FIX}"/>')                  # foundation + base pivot
        for c in (35, 62):
            A(f'<rect x="{X(0)-8}" y="{Z(c)-4}" width="16" height="8" fill="#4a9" class="s"/>')
    return X, Z


# ---------- A
X, Z = rig(310, False)
A('<text x="60" y="34" class="t">A. Whole mast turns (baseline)</text>')
lab(X(0) + 8, Z(62), X(10), Z(56), ['Roller collar (mast turns inside)'])
lab(X(0) + 8, Z(35), X(10), Z(29), ['Roller collar'])
lab(X(1.5), gy - 10, X(16), gy - 40, ['Single base pivot +', 'rotating base frame (ground level)'])
lab(X(0), Z(80), X(-24), Z(56), ['Whole mast turns'], 'end')
A(f'<text x="60" y="{gy+55}" font-size="12.5">Turns: ~7.1 t. Rotating bearings: 1 base pivot +</text>')
A(f'<text x="60" y="{gy+71}" font-size="12.5">2 collars (12 cartridges). All drives reachable from the ground.</text>')

# ---------- B
X, Z = rig(930, True)
A('<text x="680" y="34" class="t">B. Top turret (set aside)</text>')
lab(X(0) + 14, Z(64), X(10), Z(70), ['Turret bearing ~Ø2 m at 64 m', '+ drive, slip ring, wing winch'])
lab(X(0) + 8, Z(62), X(10), Z(56), ['Stay head (fixed lugs, no rollers)'])
lab(X(0) + 8, Z(35), X(10), Z(29), ['Strut head (fixed lugs)'])
lab(X(0) + 5, Z(20), X(-24), Z(26), ['Service lift on the', 'fixed mast'], 'end')
lab(X(2), gy - 8, X(10), gy - 30, ['Mast foundation pad (no rail)'])
lab(X(0), Z(52), X(-24), Z(46), ['Fixed lower mast'], 'end')
A(f'<text x="680" y="{gy+55}" font-size="12.5">Turns: ~5 t. Rotating bearings: 1 turret; no collars;</text>')
A(f'<text x="680" y="{gy+71}" font-size="12.5">no moving parts in the dust; all moving parts at 64 m.</text>')
# legend
A(f'<rect x="560" y="60" width="16" height="10" fill="{ROT}"/><text x="582" y="70">turns</text><rect x="560" y="78" width="16" height="10" fill="{FIX}"/><text x="582" y="88">fixed</text>')
A('</svg>')
open('turret-trade.svg', 'w').write('\n'.join(o))
