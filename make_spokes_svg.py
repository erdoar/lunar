# Generates spokes.svg (rev 19): main and light deck spokes, elevation + section + moment diagram.
o = []
A = o.append
W, H = 1240, 760
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:1.5}.l{stroke:#555;stroke-width:1;fill:none}.ch{stroke:#c87f0a;stroke-width:4}.dg{stroke:#c87f0a;stroke-width:1.6}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*14:.0f}" text-anchor="{anchor}">{t}</text>')


def truss(x0, ytop, L, d0, d1, panel, k):
    """Elevation of a truss: top chord flat at ytop, bottom chord tapering from d0 (left) to d1 (right)."""
    yb = lambda x: ytop + (d0 + (d1 - d0) * x / L) * k
    A(f'<line x1="{x0}" y1="{ytop}" x2="{x0+L*k}" y2="{ytop}" class="ch"/>')
    A(f'<line x1="{x0}" y1="{yb(0)}" x2="{x0+L*k}" y2="{yb(L)}" class="ch"/>')
    n = round(L / panel)
    for i in range(n):
        xa, xb = i * L / n, (i + 1) * L / n
        A(f'<line x1="{x0+xa*k}" y1="{ytop}" x2="{x0+(xa+xb)/2*k}" y2="{yb((xa+xb)/2)}" class="dg"/>')
        A(f'<line x1="{x0+(xa+xb)/2*k}" y1="{yb((xa+xb)/2)}" x2="{x0+xb*k}" y2="{ytop}" class="dg"/>')
    return yb


# ---------- main spoke
k = 150
x0, yt = 120, 110
A('<text x="20" y="30" class="t">Main spoke (x3): tapered triangular truss, hub → bogie</text>')
A(f'<rect x="{x0-60}" y="{yt-20}" width="60" height="{1.0*k+40}" fill="#cfd8e3" class="s"/><text x="{x0-30}" y="{yt+1.0*k+40}" text-anchor="middle" font-size="11">hub</text>')
yb = truss(x0, yt, 5.2, 1.0, 0.4, 0.8, k)
A(f'<rect x="{x0+5.2*k-14}" y="{yb(5.2)+2}" width="28" height="18" fill="#e0a040" class="s"/><circle cx="{x0+5.2*k}" cy="{yb(5.2)+32}" r="10" fill="#bbb" class="s"/>')
A(f'<line x1="{x0+2.6*k}" y1="{yt-14}" x2="{x0+2.6*k}" y2="{yb(2.6)+14}" stroke="#2e7d32" stroke-width="2" stroke-dasharray="5 3"/>')
A(f'<path d="M{x0-14} {yt} V{yb(0)}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{x0-18}" y="{(yt+yb(0))/2+4}" text-anchor="end">1.0 m</text>')
A(f'<path d="M{x0+5.2*k+40} {yt} V{yb(5.2)}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{x0+5.2*k+46}" y="{(yt+yb(5.2))/2+4}">0.4 m</text>')
A(f'<path d="M{x0} {yt-34} H{x0+5.2*k}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{x0+2.6*k}" y="{yt-40}" text-anchor="middle">5.2 m (r 0.8 → 6.0 m)</text>')
lab(x0 + 2.6 * k, yt - 14, x0 + 2.6 * k + 40, yt - 60, ['Mid-span splice: ships as 2 x ~2.6 m'])
lab(x0 + 5.2 * k, yb(5.2) + 32, x0 + 5.2 * k - 60, yb(5.2) + 60, ['Bogie pivot (spherical: no moment)'], 'end')
lab(x0 + 1.2 * k, yt, x0 + 1.4 * k, yt + 1.25 * k, ['Top chords x2, Ø50 x 2 CFRP: ~9 kN compression each'])
lab(x0 + 0.8 * k, yb(0.8), x0 + 1.4 * k, yt + 1.25 * k + 30, ['Bottom chord Ø50 x 2: ~17 kN tension at the root'])
A(f'<path d="M{x0+5.2*k} {yb(5.2)+70} v-28" stroke="#c0392b" stroke-width="2.5" marker-end="url(#ar)"/><text x="{x0+5.2*k+6}" y="{yb(5.2)+72}" font-size="11" fill="#c0392b">~3.3 kN reaction</text>')
# moment diagram
my = 400
A(f'<text x="{x0}" y="{my-12}" font-size="12" font-weight="bold">Bending moment</text>')
A(f'<polygon points="{x0},{my} {x0+5.2*k},{my} {x0},{my+70}" fill="#f5cba7" stroke="#c0392b"/>')
A(f'<text x="{x0+6}" y="{my+60}" font-size="11.5">~17 kN·m at the hub</text><text x="{x0+5.2*k-6}" y="{my+16}" font-size="11.5" text-anchor="end">0 at the bogie</text>')
# section A-A
sx, sy, sk = 1050, 160, 160
A(f'<text x="{sx-60}" y="{sy-50}" font-weight="bold">Section at the hub</text>')
A(f'<polygon points="{sx-0.25*sk},{sy} {sx+0.25*sk},{sy} {sx},{sy+1.0*sk}" fill="none" stroke="#c87f0a" stroke-width="2"/>')
for x, y in ((sx - 0.25 * sk, sy), (sx + 0.25 * sk, sy), (sx, sy + 1.0 * sk)):
    A(f'<circle cx="{x}" cy="{y}" r="7" fill="#c87f0a" class="s"/>')
A(f'<rect x="{sx-0.35*sk}" y="{sy-10}" width="{0.7*sk}" height="6" fill="#bbb" stroke="#888"/><text x="{sx}" y="{sy-16}" text-anchor="middle" font-size="11">grating</text>')
A(f'<path d="M{sx-0.25*sk} {sy+18} H{sx+0.25*sk}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{sx}" y="{sy+32}" text-anchor="middle" font-size="11">0.5 m</text>')
A(f'<text x="{sx}" y="{sy+1.0*sk+24}" text-anchor="middle" font-size="11">1.0 m deep (0.4 m at the rim)</text>')

# ---------- light spoke
ly = 580
A(f'<text x="20" y="{ly-40}" class="t">Light spoke (x9): constant 0.45 m triangular truss, cantilever from the hub</text>')
A(f'<rect x="{x0-60}" y="{ly-20}" width="60" height="{0.45*k+40}" fill="#cfd8e3" class="s"/>')
truss(x0, ly, 5.2, 0.45, 0.45, 0.6, k)
A(f'<rect x="{x0+5.2*k}" y="{ly-10}" width="22" height="{0.45*k+20}" fill="#9fb4c7" class="s"/><text x="{x0+5.2*k+26}" y="{ly+40}">ring girder</text>')
A(f'<path d="M{x0+5.2*k-20} {ly-50} v40" stroke="#c0392b" stroke-width="2.5" marker-end="url(#ar)"/><text x="{x0+5.2*k-26}" y="{ly-40}" font-size="11" fill="#c0392b" text-anchor="end">~1 kN: ring + grating + astronaut/robot + landed packs</text>')
A(f'<text x="{x0}" y="{ly+0.45*k+34}" font-size="12">Chords Ø35 x 1.5, diagonals Ø25 x 1.2 CFRP; ~5 kN·m root moment, ~11 kN chord force; ~17 mm free-tip deflection (less when tied to the ring).</text>')
A(f'<text x="20" y="{H-16}" font-size="12">All CFRP tubes with Ti-6Al-4V nodes; bolted moment joints at the hub (upper/lower rings), bolted to the ring girder. Stresses &lt; 60 MPa: sized by buckling, joints and handling.</text>')
A('</svg>')
open('spokes.svg', 'w').write('\n'.join(o))
