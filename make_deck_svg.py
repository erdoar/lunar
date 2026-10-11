# Generates deck.svg (rev 18): deck plan and section. Run: python3 make_deck_svg.py
import math
o = []
A = o.append
W, H = 1240, 680
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern>'
  '<pattern id="gr" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M0 0H6M0 0V6" stroke="#9aa" stroke-width="0.8"/></pattern></defs>')
A('<style>.s{stroke:#222;stroke-width:1.5}.l{stroke:#555;stroke-width:1;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*14:.0f}" text-anchor="{anchor}">{t}</text>')


def pol(cx, cy, r, deg):
    a = math.radians(deg - 90)
    return cx + r * math.cos(a), cy + r * math.sin(a)


# ---------- plan
cx, cy, k = 300, 300, 36
A('<text x="20" y="30" class="t">Plan</text>')
A(f'<circle cx="{cx}" cy="{cy}" r="{6*k}" fill="none" stroke="#c0392b" stroke-width="5"/>')          # rail under
A(f'<circle cx="{cx}" cy="{cy}" r="{6*k}" fill="none" stroke="#9fb4c7" stroke-width="14" opacity="0.8"/>')  # ring girder
A(f'<circle cx="{cx}" cy="{cy}" r="{5.0*k}" fill="none" stroke="url(#gr)" stroke-width="{1.0*k}"/>')     # walkway ring grating
for i in range(12):
    d = i * 30
    x, y = pol(cx, cy, 6 * k, d)
    main = d % 120 == 0
    A(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{"#c87f0a" if main else "#888"}" stroke-width="{9 if main else 3}"/>')
    if main:
        A(f'<rect x="{x-12:.1f}" y="{y-12:.1f}" width="24" height="24" fill="#e0a040" class="s"/>')
    x1, y1 = pol(cx, cy, 6 * k - 10, d + 15); x2, y2 = pol(cx, cy, 6 * k + 10, d + 15)
    A(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#222" stroke-width="1.2"/>')
# maintenance azimuth tray strip (30/210)
for d in (30, 210):
    x1, y1 = pol(cx, cy, 2 * k, d); x2, y2 = pol(cx, cy, 6 * k, d)
    A(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#7d8790" stroke-width="12" opacity="0.7"/>')
A(f'<circle cx="{cx}" cy="{cy}" r="{0.8*k}" fill="#cfd8e3" class="s"/>')                                 # hub
pts = [pol(cx, cy, 0.81 * k, d) for d in (0, 120, 240)]
A('<polygon points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '" fill="none" stroke="#555" stroke-width="3"/>')
A(f'<rect x="{cx+1.2*k}" y="{cy+0.5*k}" width="{1.6*k}" height="{0.9*k}" fill="#7fa3d6" class="s"/>')    # winch
A(f'<rect x="{cx-2.8*k}" y="{cy+0.6*k}" width="{1.2*k}" height="{0.8*k}" fill="#bfa6d9" class="s"/>')    # power conditioning
A(f'<rect x="{cx-1.25*k}" y="{cy-1.25*k}" width="{2.5*k}" height="{2.5*k}" fill="none" stroke="#2e7d32" stroke-width="2" stroke-dasharray="6 3"/>')  # jack frame
def call(n, x, y, dx, dy):
    A(f'<path d="M{x:.0f} {y:.0f}L{x+dx:.0f} {y+dy:.0f}" class="l"/><circle cx="{x+dx:.0f}" cy="{y+dy:.0f}" r="10" fill="#fff" stroke="#222"/>'
      f'<text x="{x+dx:.0f}" y="{y+dy+4:.0f}" text-anchor="middle" font-size="11" font-weight="bold" style="stroke:none">{n}</text>')


x, y = pol(cx, cy, 6 * k, 0); call(1, x + 12, y, 30, -10)
x, y = pol(cx, cy, 4 * k, 120); call(2, x, y, 30, 25)
x, y = pol(cx, cy, 4.5 * k, 60); call(3, x, y, 30, -20)
x, y = pol(cx, cy, 6 * k, 300); call(4, x - 7, y, -25, -20)
x, y = pol(cx, cy, 5 * k, 165); call(5, x, y, 20, 30)
x, y = pol(cx, cy, 4 * k, 210); call(6, x, y, -30, 25)
call(7, cx + 2.8 * k, cy + 0.95 * k, 30, 30)
call(8, cx - 2.8 * k, cy + 1.0 * k, -30, 30)
call(9, cx + 0.5 * k, cy - 0.6 * k, 40, -50)
call(10, cx - 1.25 * k, cy - 1.25 * k, -30, -30)
items = ['Bogie under each main spoke (x3)', 'Main spoke: ~1 m deep truss (x3)', 'Light spoke (x9)', 'Ring girder over the rail (12 segments) + dust skirt',
         'Walkway grating ring', 'Inboard landing-tray strip (maintenance azimuth)', 'Panel elevation winch + 4 trim sheaves', 'Power conditioning (to the slip ring)',
         'Hub: mast-foot seat on top, kingpin + slip ring below', 'Jack frame (erection) / base maintenance frame']
for i, t in enumerate(items):
    col, row = divmod(i, 5)
    x0, y0 = 30 + col * 300, 560 + row * 19
    A(f'<circle cx="{x0}" cy="{y0-4}" r="8" fill="#fff" stroke="#222" stroke-width="1.2"/><text x="{x0}" y="{y0}" text-anchor="middle" font-size="10" font-weight="bold" style="stroke:none">{i+1}</text>')
    A(f'<text x="{x0+13}" y="{y0}" font-size="11.5">{t}</text>')

# ---------- section through hub and one main spoke
sx, sy, e = 780, 470, 60
X = lambda m: sx + m * e
Y = lambda m: sy - m * e
A(f'<text x="{sx-80}" y="30" class="t">Section through the hub and a main spoke</text>')
A(f'<rect x="{X(-0.7)}" y="{Y(0)+60}" width="{7*e}" height="40" fill="url(#g)"/><line x1="{X(-0.7)}" y1="{Y(0)+60}" x2="{X(6.3)}" y2="{Y(0)+60}" stroke="#222"/>')
# rail at r=6 on pier
A(f'<rect x="{X(6)-12}" y="{Y(0)+30}" width="24" height="30" fill="#ccc" class="s"/><rect x="{X(6)-16}" y="{Y(0)+18}" width="32" height="12" fill="#7d8790" class="s"/><rect x="{X(6)-16}" y="{Y(0)+14}" width="32" height="5" fill="#c0392b"/>')
A(f'<circle cx="{X(6)}" cy="{Y(0)+2}" r="12" fill="#bbb" class="s"/>')                           # tyre
A(f'<rect x="{X(6)-22}" y="{Y(0.3)-6}" width="44" height="16" fill="#e0a040" class="s"/>')          # bogie
# kingpin foundation + slewing ring + hub
A(f'<rect x="{X(-0.5)}" y="{Y(0)+30}" width="{1.0*e}" height="30" fill="#ccc" class="s"/>')
A(f'<rect x="{X(-0.6)}" y="{Y(0.3)}" width="{1.2*e}" height="12" fill="#4a9" class="s"/>')
A(f'<rect x="{X(-0.8)}" y="{Y(1.3)}" width="{1.6*e}" height="{1.0*e-12}" fill="#cfd8e3" class="s"/>')
A(f'<path d="M{X(-0.35)} {Y(1.3)} A{0.35*e} {0.2*e} 0 0 1 {X(0.35)} {Y(1.3)}" fill="#e0a040" class="s"/>')   # spherical seat
# main spoke truss from hub (r 0.8) to bogie (r 6)
A(f'<line x1="{X(0.8)}" y1="{Y(1.3)}" x2="{X(6)}" y2="{Y(1.3)}" stroke="#c87f0a" stroke-width="5"/>')
A(f'<line x1="{X(0.8)}" y1="{Y(0.3)}" x2="{X(6)}" y2="{Y(0.3)}" stroke="#c87f0a" stroke-width="5"/>')
for i in range(6):
    x0 = 0.8 + i * 0.87
    A(f'<line x1="{X(x0)}" y1="{Y(1.3)}" x2="{X(x0+0.43)}" y2="{Y(0.3)}" stroke="#c87f0a" stroke-width="2"/>')
A(f'<rect x="{X(0.8)}" y="{Y(1.3)-6}" width="{5.2*e}" height="6" fill="url(#gr)" stroke="#999"/>')       # grating
# mast foot
A(f'<rect x="{X(-0.7)}" y="{Y(4)}" width="{1.4*e}" height="{2.6*e}" fill="none" stroke="#888" stroke-width="3"/>')
A(f'<path d="M{X(-0.7)} {Y(1.4)} L{X(0)} {Y(1.42)+4} L{X(0.7)} {Y(1.4)}" fill="none" stroke="#555" stroke-width="3"/>')
A(f'<rect x="{X(0.7)-2}" y="{Y(2.1)}" width="6" height="{0.5*e}" fill="#fff" stroke="#c0392b" stroke-width="2"/>')  # side window
A(f'<path d="M{X(1.6)} {Y(1.4)} L{X(0.75)} {Y(2.0)} L{X(0)} {Y(2.3)} V{Y(4)}" fill="none" stroke="#c0392b" stroke-width="2"/>')
A(f'<circle cx="{X(0.75)}" cy="{Y(2.0)}" r="5" fill="#fff" class="s"/>')
A(f'<rect x="{X(1.3)}" y="{Y(1.75)}" width="{0.9*e}" height="{0.42*e}" fill="#7fa3d6" class="s"/>')
lab(X(0), Y(1.33), X(-1.0), Y(2.6), ['Mast-foot spherical', 'seat, ~9 kN'], 'end')
lab(X(-0.6), Y(0.25), X(-1.0), Y(0.6), ['Kingpin slewing ring', '+ slip ring (centring only)'], 'end')
lab(X(3.3), Y(0.8), X(2.4), Y(-0.8), ['Main spoke truss, ~1 m deep', '(~18 kN chord force)'])
lab(X(1.75), Y(1.55), X(2.6), Y(2.6), ['Winch'])
lab(X(0.75), Y(2.0), X(2.6), Y(3.1), ['Halyards enter via a side', 'window + deflection sheave'])
lab(X(6), Y(0.3), X(5.9), Y(2.3), ['Bogie pivot (~6 kN)'], 'end')
lab(X(4), Y(1.3) - 3, X(4.6), Y(2.1), ['Grating, deck top ~1.4 m'])
A(f'<text x="20" y="{H-14}" font-size="12">Deck ~2.5 t: hub 0.30, main spokes 0.72, light spokes 0.54, ring girder 0.57, gratings 0.24, skirt/trays/mounts 0.15 t. All parts fit the 3.2 x 1.5 x 1.5 m freight module.</text>')
A('</svg>')
open('deck.svg', 'w').write('\n'.join(o))
