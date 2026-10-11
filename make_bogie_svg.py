# Generates bogie-rail.svg (rev 6: 3 bogies x 2 replaceable tyres). Run: python3 make_bogie_svg.py
import math
o = []
A = o.append
W, H = 1240, 820
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="13">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:2}.l{stroke:#555;stroke-width:1;fill:none}.deck{fill:#9fb4c7}.frame{fill:#e0a040}'
  '.tyre{fill:#bbb}.rail{fill:#7d8790}.head{fill:#c0392b}.pier{fill:#cfcfcf}.cart{fill:#4a9}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:17px;font-weight:bold}</style>')


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*15:.0f}" text-anchor="{anchor}">{t}</text>')


def pol(cx, cy, r, deg):
    a = math.radians(deg - 90)
    return cx + r * math.cos(a), cy + r * math.sin(a)


# ---------- plan of the ring
cx, cy, k, R = 230, 250, 26, 6
A('<text x="20" y="30" class="t">Plan: 3 bogies x 2 tyres</text>')
A(f'<circle cx="{cx}" cy="{cy}" r="{R*k}" fill="none" stroke="#c0392b" stroke-width="6"/>')
for i in range(12):
    x1, y1 = pol(cx, cy, R * k - 8, i * 30 + 15); x2, y2 = pol(cx, cy, R * k + 8, i * 30 + 15)
    A(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#222" stroke-width="1.5"/>')
half = math.degrees(0.65 / R)
tang = math.degrees(0.45 / R)
for d in (0, 120, 240):
    p0, p1 = pol(cx, cy, R * k, d - half), pol(cx, cy, R * k, d + half)
    A(f'<path d="M{p0[0]:.1f} {p0[1]:.1f} A{R*k} {R*k} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#e0a040" stroke-width="16"/>')
    for t in (-tang, tang):
        x, y = pol(cx, cy, R * k + 14, d + t)
        A(f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#888" stroke-width="0.8" stroke-dasharray="3 4"/>')
        A(f'<rect x="-6" y="-4" width="12" height="8" fill="#bbb" stroke="#222" transform="translate({x:.1f},{y:.1f}) rotate({d+t})"/>')
A(f'<circle cx="{cx}" cy="{cy}" r="8" fill="#fff" class="s"/>')
r2 = R * k + 34
p0, p1 = pol(cx, cy, r2, 120 + half + 2), pol(cx, cy, r2, 240 - half - 2)
A(f'<path d="M{p0[0]:.1f} {p0[1]:.1f} A{r2} {r2} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#222" stroke-width="1.3" marker-start="url(#ar)" marker-end="url(#ar)"/>')
A(f'<text x="{cx}" y="{cy+R*k+58}" text-anchor="middle">~11 m clear rail between bogies</text>')
A(f'<text x="{cx}" y="{cy+R*k+74}" text-anchor="middle">(3 full segments free)</text>')
x, y = pol(cx, cy, R * k, 0); lab(x + 22, y, x + 60, y - 22, ['Bogie 1.3 m, 2 tyres;', 'axles point at centre', '(fan ~8.6°)'])
A(f'<text x="{cx}" y="{cy+28}" text-anchor="middle" font-size="11">kingpin</text>')
A(f'<text x="{cx}" y="{cy+48}" text-anchor="middle" font-size="12">Ø12 m rail,</text><text x="{cx}" y="{cy+63}" text-anchor="middle" font-size="12">12 segments of π m</text>')

# ---------- side view of one bogie
ox, oy = 560, 70
A(f'<text x="{ox}" y="30" class="t">Side view: one bogie (right tyre out, shoe down)</text>')
s = 300
X = lambda m: ox + 230 + m * s
deck_y, frame_y, axle_y, rail_y = oy + 20, oy + 130, oy + 200, oy + 245
r_t = 0.15 * s
A(f'<rect x="{X(-0.85)}" y="{deck_y}" width="{1.7*s}" height="34" class="deck s"/><text x="{X(-0.8)}" y="{deck_y+22}">Rotating deck</text>')
A(f'<rect x="{X(0)-26}" y="{deck_y+34}" width="52" height="34" fill="#fff" class="s"/><circle cx="{X(0)}" cy="{frame_y-16}" r="16" class="frame s"/>')
A(f'<path d="M{X(-0.65)} {frame_y} H{X(0.65)} V{frame_y+40} H{X(0.56)} V{frame_y+22} H{X(-0.56)} V{frame_y+40} H{X(-0.65)} Z" class="frame s"/>')
for i, m in enumerate((-0.45, 0.45)):
    out = (i == 1)
    A(f'<line x1="{X(m)}" y1="{frame_y+22}" x2="{X(m)}" y2="{axle_y}" stroke="#555" stroke-width="10"/>')
    if out:
        A(f'<circle cx="{X(m)}" cy="{axle_y-5}" r="{r_t}" fill="none" stroke="#555" stroke-width="2" stroke-dasharray="6 4"/><circle cx="{X(m)}" cy="{axle_y-5}" r="7" fill="#333"/>')
    else:
        A(f'<circle cx="{X(m)}" cy="{axle_y}" r="{r_t}" class="tyre s"/><circle cx="{X(m)}" cy="{axle_y}" r="{r_t*0.55}" fill="#ddd" stroke="#222"/><circle cx="{X(m)}" cy="{axle_y}" r="7" fill="#333"/>')
    # support shoe on a screw, outboard of each tyre
    sx = X(m + (0.24 if m > 0 else -0.24))
    shoe_bot = rail_y if out else rail_y - 6
    A(f'<rect x="{sx-4}" y="{frame_y+10}" width="8" height="{shoe_bot-frame_y-24}" fill="#333"/>')
    A(f'<rect x="{sx-20}" y="{shoe_bot-14}" width="40" height="14" rx="2" fill="#4a9" class="s"/>')
for m in (-0.6, 0.6):
    A(f'<path d="M{X(m)} {frame_y+40} L{X(m+(-0.12 if m<0 else 0.12))} {rail_y-2}" stroke="#222" stroke-width="2.5"/>')
A(f'<line x1="{X(-0.05)}" y1="{frame_y+40}" x2="{X(-0.05)}" y2="{rail_y+30}" stroke="#555" stroke-width="5"/><circle cx="{X(-0.05)}" cy="{rail_y+34}" r="9" class="cart s"/>')
A(f'<line x1="{X(0.05)}" y1="{frame_y+40}" x2="{X(0.05)}" y2="{rail_y+30}" stroke="#555" stroke-width="5"/><circle cx="{X(0.05)}" cy="{rail_y+34}" r="9" class="cart s"/>')
A(f'<rect x="{X(-0.9)}" y="{rail_y}" width="{1.8*s}" height="14" class="head s"/><rect x="{X(-0.9)}" y="{rail_y+14}" width="{1.8*s}" height="12" class="rail s"/>')
A(f'<rect x="{X(-0.12)}" y="{rail_y+26}" width="{0.24*s}" height="20" class="rail s"/><rect x="{X(-0.9)}" y="{rail_y+46}" width="{1.8*s}" height="40" class="rail s"/>')
A(f'<line x1="{X(0.75)}" y1="{rail_y}" x2="{X(0.8)}" y2="{rail_y+14}" stroke="#fff" stroke-width="3"/>')
lab(X(0) + 16, frame_y - 16, X(0.4), deck_y + 50, ['Spherical centre pivot', '= load equaliser, ±20 mm radial float'])
lab(X(-0.69), frame_y + 60, X(-0.95), frame_y + 18, ['Support shoe on screw,', '3 mm above rail'], 'end')
lab(X(0.69) + 20, rail_y - 7, X(0.95), rail_y - 40, ['Shoe down: carries', 'the load for a swap'])
lab(X(0.45) + 20, axle_y - 30, X(0.95), frame_y - 10, ['Tyre slid off', 'outward'])
lab(X(-0.45) - 44, axle_y - 10, X(-0.95), axle_y - 12, ['Tyre Ø300'], 'end')
lab(X(-0.05) - 9, rail_y + 34, X(-0.95), rail_y + 52, ['Uplift rollers (2)'], 'end')
lab(X(-0.68), rail_y - 8, X(-0.95), rail_y + 14, ['Scraper'], 'end')
lab(X(0.77), rail_y + 7, X(0.95), rail_y + 60, ['Wear strip joint'])
lab(X(-0.5), rail_y + 7, X(-0.3), rail_y + 104, ['Flat rail head wear strip (red), π m long'], 'end')

# ---------- section through a tyre
sx0, sy0 = 470, 510
A(f'<text x="{sx0}" y="{sy0-20}" class="t">Section through a tyre (ring centre to the left)</text>')
A(f'<rect x="{sx0+10}" y="{sy0}" width="420" height="30" class="deck s"/>')
A(f'<rect x="{sx0+120}" y="{sy0+30}" width="60" height="70" class="frame s"/>')
tilt = -5.7  # exaggerated from 1.4 deg; negative = inner end down
cxa, cya = sx0 + 262, sy0 + 92
A(f'<g transform="rotate({tilt} {cxa} {cya})">')
A(f'<rect x="{sx0+180}" y="{sy0+80}" width="26" height="30" fill="#555" class="s"/>')
A(f'<rect x="{sx0+206}" y="{sy0+86}" width="122" height="13" fill="#555" class="s"/>')
A(f'<polygon points="{sx0+222},{sy0+48} {sx0+302},{sy0+40} {sx0+302},{sy0+144} {sx0+222},{sy0+136}" class="tyre s"/>')
A(f'<rect x="{sx0+238}" y="{sy0+72}" width="48" height="40" fill="#ddd" stroke="#222"/>')
A(f'<polygon points="{sx0+302},{sy0+83} {sx0+326},{sy0+83} {sx0+330},{sy0+92} {sx0+326},{sy0+101} {sx0+302},{sy0+101}" fill="#333"/>')
A('</g>')
ry = sy0 + 140
A(f'<rect x="{sx0+206}" y="{ry}" width="104" height="16" class="head s"/>')
A(f'<rect x="{sx0+246}" y="{ry+16}" width="24" height="24" class="rail s"/><rect x="{sx0+214}" y="{ry+40}" width="90" height="70" class="rail s"/>')
A(f'<rect x="{sx0+246}" y="{ry+110}" width="26" height="40" class="pier s"/>')
A(f'<rect x="{sx0+150}" y="{sy0+100}" width="12" height="76" class="frame s"/><circle cx="{sx0+212}" cy="{ry+28}" r="8" class="cart s"/><line x1="{sx0+162}" y1="{ry+26}" x2="{sx0+204}" y2="{ry+28}" stroke="#555" stroke-width="4"/>')
A(f'<line x1="{sx0+10}" y1="{ry}" x2="{sx0+206}" y2="{ry}" stroke="#888" stroke-dasharray="4 4"/>')
A(f'<path d="M{sx0+345} {sy0+60} H{sx0+405}" stroke="#222" stroke-width="2" marker-end="url(#ar)"/><text x="{sx0+347}" y="{sy0+52}" font-size="12">slides off</text>')
lab(sx0 + 150, sy0 + 50, sx0 + 60, sy0 + 70, ['Bogie frame', '(inboard)'], 'end')
lab(sx0 + 214, sy0 + 92, sx0 + 140, sy0 + 236, ['Stub axle tipped ~1.4° down', 'toward the centre (drawn ~6°)'], 'end')
lab(sx0 + 30, ry, sx0 + 30, ry + 40, ['Rail-top plane runs to the', 'ring centre = cone apex'], 'end')
lab(sx0 + 262, sy0 + 46, sx0 + 340, sy0 + 20, ['Conical tread, half-angle ~1.4°'])
lab(sx0 + 324, sy0 + 98, sx0 + 380, sy0 + 112, ['Captive hub nut'])
lab(sx0 + 280, sy0 + 110, sx0 + 380, sy0 + 140, ['Wheel cartridge: hub, sealed', 'hybrid bearing, MoS₂, steel tread'])
lab(sx0 + 305, ry + 8, sx0 + 380, ry + 44, ['Flat rail head wear strip,', 'ceramic/DLC coated'])
lab(sx0 + 212, ry + 36, sx0 + 150, ry + 66, ['Uplift roller'], 'end')
lab(sx0 + 300, ry + 90, sx0 + 380, ry + 95, ['Box beam rail on pier'])
A(f'<text x="{sx0+10}" y="{H-22}" font-size="12">Load on each tyre is vertical (tripod + kingpin take all side loads), so tyres are not tilted outward.</text>')

# ---------- swap steps
ty = 520
A(f'<text x="20" y="{ty}" class="t">Swapping a tyre</text>')
for j, t in enumerate(['1. Stop and lock the drive.', '2. Wind the support shoe down until it', '    takes the load; tyre lifts ~5 mm.',
                      '3. Undo the captive hub nut; slide the', '    wheel cartridge off outward.', '4. Slide the spare on, tighten, wind the',
                      '    shoe back to its 3 mm standoff.', 'Wheel cartridge ~12 kg (~2 kg-weight', 'on the Moon). No deck jacking.',
                      'If a tyre fails in service, its shoe', 'lands on the rail: the bogie never drops.']):
    A(f'<text x="20" y="{ty+26+j*19}" font-size="13">{t}</text>')
A('</svg>')
open('bogie-rail.svg', 'w').write('\n'.join(o))
