# Generates bogie-rail.svg (rev 5: 3 bogies x 4 replaceable tyres). Run: python3 make_bogie_svg.py
import math
o = []
A = o.append
W, H = 1240, 820
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="13">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker>'
  '<pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern></defs>')
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
cx, cy, k = 200, 250, 26   # px per metre
R = 6
A('<text x="20" y="30" class="t">Plan: 3 bogies at 120°</text>')
A(f'<circle cx="{cx}" cy="{cy}" r="{R*k}" fill="none" stroke="#c0392b" stroke-width="6"/>')
for i in range(12):
    x1, y1 = pol(cx, cy, R * k - 8, i * 30 + 15); x2, y2 = pol(cx, cy, R * k + 8, i * 30 + 15)
    A(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#222" stroke-width="1.5"/>')
half = math.degrees(1.2 / R)  # half bogie length as angle
for d in (0, 120, 240):
    a0, a1 = d - half, d + half
    p0, p1 = pol(cx, cy, R * k, a0), pol(cx, cy, R * k, a1)
    A(f'<path d="M{p0[0]:.1f} {p0[1]:.1f} A{R*k} {R*k} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#e0a040" stroke-width="16"/>')
    for j in range(4):
        x, y = pol(cx, cy, R * k + 12, a0 + (j + 0.5) * (a1 - a0) / 4)
        A(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4" fill="#bbb" stroke="#222"/>')
    if d != 0:
        dl = 60 if d == 120 else 180
    x, y = pol(cx, cy, R * k + 30, d)
A(f'<circle cx="{cx}" cy="{cy}" r="8" fill="#fff" class="s"/>')
# free-rail arc between bogies 120 and 240 (bottom)
r2 = R * k + 34
p0, p1 = pol(cx, cy, r2, 120 + half + 2), pol(cx, cy, r2, 240 - half - 2)
A(f'<path d="M{p0[0]:.1f} {p0[1]:.1f} A{r2} {r2} 0 0 1 {p1[0]:.1f} {p1[1]:.1f}" fill="none" stroke="#222" stroke-width="1.3" marker-start="url(#ar)" marker-end="url(#ar)"/>')
A(f'<text x="{cx}" y="{cy+R*k+58}" text-anchor="middle">~10 m clear rail between bogies</text>')
A(f'<text x="{cx}" y="{cy+R*k+74}" text-anchor="middle">(3 full segments free)</text>')
x, y = pol(cx, cy, R * k, 0); lab(x + 30, y, x + 60, y - 20, ['Bogie, 2.4 m,', '4 tyres'])
A(f'<text x="{cx}" y="{cy+48}" text-anchor="middle" font-size="12">Ø12 m rail,</text><text x="{cx}" y="{cy+63}" text-anchor="middle" font-size="12">12 segments of π m</text>')
A(f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="11" dy="22">kingpin</text>')

# ---------- side view of one bogie (developed along the rail)
ox, oy = 560, 70
A(f'<text x="{ox}" y="30" class="t">Side view: one bogie (one tyre lifted out)</text>')
s = 210  # px per metre
X = lambda m: ox + 40 + (m + 1.2) * s
deck_y, frame_y, axle_y, rail_y = oy + 20, oy + 120, oy + 205, oy + 245
A(f'<rect x="{X(-1.35)}" y="{deck_y}" width="{2.7*s}" height="34" class="deck s"/><text x="{X(-1.3)}" y="{deck_y+22}">Rotating deck</text>')
A(f'<rect x="{X(0)-26}" y="{deck_y+34}" width="52" height="30" fill="#fff" class="s"/><circle cx="{X(0)}" cy="{deck_y+79}" r="15" class="frame s"/>')
A(f'<rect x="{X(-1.2)}" y="{frame_y-12}" width="{2.4*s}" height="26" rx="5" class="frame s"/>')
tx = (-0.9, -0.3, 0.3, 0.9)
r_t = 0.15 * s
for i, m in enumerate(tx):
    pivot = (X(m) + (0.22 * s if m < 0 else -0.22 * s), frame_y + 14)
    lifted = (i == 2)
    ay = axle_y - (14 if lifted else 0)
    A(f'<line x1="{pivot[0]:.0f}" y1="{pivot[1]}" x2="{X(m):.0f}" y2="{ay}" stroke="#555" stroke-width="9" stroke-linecap="round"/>')
    A(f'<circle cx="{pivot[0]:.0f}" cy="{pivot[1]}" r="6" fill="#fff" class="s"/>')
    # spring + retract screw between frame and arm
    sx = X(m) + (0.06 * s if m < 0 else -0.06 * s)
    zz = ' '.join(f'l{(-8 if j % 2 else 8)} 7' for j in range(6))
    A(f'<path d="M{sx:.0f} {frame_y+14} {zz}" fill="none" stroke="#222" stroke-width="2"/>')
    A(f'<rect x="{sx-4:.0f}" y="{frame_y-34}" width="8" height="22" fill="#333"/><rect x="{sx-10:.0f}" y="{frame_y-40}" width="20" height="7" fill="#333"/>')
    if lifted:
        A(f'<circle cx="{X(m):.0f}" cy="{ay}" r="{r_t}" fill="none" stroke="#555" stroke-width="2" stroke-dasharray="6 4"/>')
        A(f'<circle cx="{X(m):.0f}" cy="{ay}" r="7" fill="#333"/>')
    else:
        A(f'<circle cx="{X(m):.0f}" cy="{ay}" r="{r_t}" class="tyre s"/><circle cx="{X(m):.0f}" cy="{ay}" r="{r_t*0.55}" fill="#ddd" stroke="#222"/><circle cx="{X(m):.0f}" cy="{ay}" r="7" fill="#333"/>')
# uplift rollers + scrapers
for m in (-1.12, 1.12):
    A(f'<line x1="{X(m)}" y1="{frame_y+14}" x2="{X(m)}" y2="{rail_y+30}" stroke="#555" stroke-width="5"/><circle cx="{X(m)}" cy="{rail_y+34}" r="9" class="cart s"/>')
    A(f'<path d="M{X(m)+(-14 if m<0 else 14)} {frame_y+14} L{X(m)+(-30 if m<0 else 30)} {rail_y-2}" stroke="#222" stroke-width="2.5"/>')
# rail
A(f'<rect x="{X(-1.45)}" y="{rail_y}" width="{2.9*s}" height="14" class="head s"/><rect x="{X(-1.45)}" y="{rail_y+14}" width="{2.9*s}" height="12" class="rail s"/>')
A(f'<rect x="{X(-1.45)}" y="{rail_y+46}" width="{2.9*s}" height="40" class="rail s"/><rect x="{X(-1.45)}" y="{rail_y+26}" width="{2.9*s}" height="20" fill="#fff" stroke="none"/>')
A(f'<rect x="{X(-0.15)}" y="{rail_y+26}" width="{0.3*s}" height="20" class="rail s"/>')
A(f'<line x1="{X(0.62)}" y1="{rail_y}" x2="{X(0.7)}" y2="{rail_y+14}" stroke="#fff" stroke-width="3"/>')
# labels side view
lab(X(0) + 15, deck_y + 79, X(0) + 120, deck_y + 52, ['Spherical pivot,', '±20 mm radial float'])
lab(X(-0.9) + 6, frame_y - 38, X(-0.95), oy + 4, ['Retract screw (lifts tyre ~20 mm)'], 'end')
lab(X(-0.9) + 22, frame_y + 30, X(-1.45), frame_y + 40, ['Preload spring'], 'end')
lab(X(-0.62), frame_y + 40, X(-1.45), frame_y + 70, ['Swing arm'], 'end')
lab(X(0.3) + 20, axle_y + 20, X(0.2), rail_y + 104, ['Tyre lifted clear and slid off'])
lab(X(0.9) + 32, axle_y + 10, X(1.45), axle_y + 10, ['Tyre Ø300'])
lab(X(1.12) + 9, rail_y + 34, X(1.45), rail_y + 48, ['Uplift roller'])
lab(X(-1.12) - 22, rail_y - 10, X(-1.45), rail_y - 26, ['Scraper'], 'end')
lab(X(0.66), rail_y + 7, X(0.95), rail_y + 122, ['Wear strip joint'])
lab(X(-0.6), rail_y + 7, X(-0.5), rail_y + 104, ['Rail head wear strip (red), π m long'], 'end')

# ---------- cross-section through a tyre
sx0, sy0 = 470, 510
A(f'<text x="{sx0}" y="{sy0-20}" class="t">Section through a tyre (ring centre to the left)</text>')
q = 1.0
A(f'<rect x="{sx0+10}" y="{sy0}" width="420" height="30" class="deck s"/>')
A(f'<rect x="{sx0+120}" y="{sy0+30}" width="60" height="70" class="frame s"/>')                   # bogie frame (inboard)
A(f'<rect x="{sx0+180}" y="{sy0+70}" width="26" height="40" fill="#555" class="s"/>')             # arm end
A(f'<rect x="{sx0+206}" y="{sy0+82}" width="120" height="14" fill="#555" class="s"/>')             # stub axle (outboard)
A(f'<polygon points="{sx0+226},{sy0+42} {sx0+290},{sy0+48} {sx0+290},{sy0+132} {sx0+226},{sy0+138}" class="tyre s"/>')  # conical tyre
A(f'<rect x="{sx0+236}" y="{sy0+70}" width="44" height="38" fill="#ddd" stroke="#222"/>')         # hub/bearing
A(f'<polygon points="{sx0+296},{sy0+80} {sx0+322},{sy0+80} {sx0+326},{sy0+89} {sx0+322},{sy0+98} {sx0+296},{sy0+98}" fill="#333"/>')  # captive nut
# rail section (conical head) + uplift roller
A(f'<polygon points="{sx0+210},{sy0+141} {sx0+306},{sy0+132} {sx0+306},{sy0+148} {sx0+210},{sy0+157}" class="head s"/>')
A(f'<rect x="{sx0+246}" y="{sy0+150}" width="24" height="26" class="rail s"/><rect x="{sx0+214}" y="{sy0+176}" width="90" height="70" class="rail s"/>')
A(f'<rect x="{sx0+246}" y="{sy0+246}" width="26" height="40" class="pier s"/>')
A(f'<rect x="{sx0+150}" y="{sy0+100}" width="12" height="62" class="frame s"/><circle cx="{sx0+214}" cy="{sy0+164}" r="8" class="cart s"/><line x1="{sx0+162}" y1="{sy0+160}" x2="{sx0+206}" y2="{sy0+164}" stroke="#555" stroke-width="4"/>')
A(f'<path d="M{sx0+340} {sy0+60} H{sx0+400}" stroke="#222" stroke-width="2" marker-end="url(#ar)"/><text x="{sx0+342}" y="{sy0+52}" font-size="12">slides off</text>')
lab(sx0 + 150, sy0 + 50, sx0 + 60, sy0 + 70, ['Bogie frame', '(inboard)'], 'end')
lab(sx0 + 216, sy0 + 89, sx0 + 140, sy0 + 230, ['Cantilevered stub axle,', 'points at ring centre'], 'end')
lab(sx0 + 258, sy0 + 46, sx0 + 330, sy0 + 20, ['Flangeless conical tread (apex at ring centre)'])
lab(sx0 + 322, sy0 + 92, sx0 + 380, sy0 + 110, ['Captive hub nut'])
lab(sx0 + 272, sy0 + 100, sx0 + 380, sy0 + 135, ['Wheel cartridge: hub, sealed', 'hybrid bearing, MoS₂, steel tread'])
lab(sx0 + 300, sy0 + 140, sx0 + 380, sy0 + 175, ['Conical rail head wear strip,', 'ceramic/DLC coated'])
lab(sx0 + 214, sy0 + 170, sx0 + 140, sy0 + 190, ['Uplift roller'], 'end')
lab(sx0 + 300, sy0 + 220, sx0 + 380, sy0 + 225, ['Box beam rail on pier'])

# ---------- tyre swap steps (under the plan)
ty = 520
A(f'<text x="20" y="{ty}" class="t">Swapping a tyre</text>')
for j, t in enumerate(['1. Stop and lock the drive.', '2. Wind the retract screw: tyre lifts', '    ~20 mm, its load goes to the other 3.',
                      '3. Undo the captive hub nut; slide the', '    wheel cartridge off outward.', '4. Slide the spare on, tighten, wind the',
                      '    screw back to the spring-load mark.', 'Wheel cartridge ~10 kg (under 2 kg-weight', 'on the Moon). No deck jacking.']):
    A(f'<text x="20" y="{ty+26+j*19}" font-size="13">{t}</text>')
A('</svg>')
open('bogie-rail.svg', 'w').write('\n'.join(o))
