# Generates vlink-tensioner.svg (rev 30): V-plate part, load-pin section, apex termination, foot node and thermal comparison.
# Run: python3 make_vlink_tensioner_svg.py
from math import sin, cos, radians, atan

o = []
A = o.append
W, H = 1300, 960
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern>'
  '<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:1.3}.l{stroke:#555;stroke-width:1;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')
TI, COL, ST, PIN, STAY, SPR, SEN = '#9fb3c8', '#4a9', '#6b7280', '#c9a227', '#8e44ad', '#c0392b', '#2c4a7a'


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*14:.0f}" text-anchor="{anchor}" font-size="11.5">{t}</text>')


# ================= A. V-plate in its own plane =================
A('<text x="20" y="30" class="t">A. V-link (in its own plane)</text>')
k, cx, top = 300, 190, 120
A(f'<rect x="{cx-0.32*k}" y="{top-48}" width="{0.64*k}" height="26" fill="{COL}" opacity="0.6" class="s"/><text x="{cx}" y="{top-30}" text-anchor="middle" font-size="11" style="stroke:none">collar ring lugs</text>')
pins = [(cx - 0.2 * k, top), (cx + 0.2 * k, top)]
apex = (cx, top + 1.0 * k)
for (px, py) in pins:
    A(f'<polygon points="{px-10},{py} {px+10},{py} {apex[0]+7},{apex[1]} {apex[0]-7},{apex[1]}" fill="{TI}" class="s"/>')
for (px, py) in pins:
    A(f'<circle cx="{px}" cy="{py}" r="18" fill="{TI}" class="s"/><circle cx="{px}" cy="{py}" r="11" fill="#fff" stroke="#222"/><circle cx="{px}" cy="{py}" r="6" fill="{PIN}" stroke="#222"/>')
    A(f'<rect x="{px-6}" y="{top-48}" width="12" height="40" fill="{PIN}" opacity="0.7"/>')
A(f'<circle cx="{apex[0]}" cy="{apex[1]}" r="20" fill="{TI}" class="s"/><circle cx="{apex[0]}" cy="{apex[1]}" r="11" fill="#fff" stroke="#222"/>')
A(f'<path d="M{apex[0]-9} {apex[1]+8} L{apex[0]-9} {apex[1]+40} L{apex[0]+9} {apex[1]+40} L{apex[0]+9} {apex[1]+8}" fill="#ddd" stroke="#222"/>')
A(f'<rect x="{apex[0]-6}" y="{apex[1]+40}" width="12" height="34" fill="#bbb" stroke="#222"/>')
A(f'<line x1="{apex[0]}" y1="{apex[1]+74}" x2="{apex[0]}" y2="{apex[1]+160}" stroke="{STAY}" stroke-width="3"/>')
A(f'<path d="M{pins[0][0]} {top+12} V{apex[1]} M{pins[0][0]-4} {apex[1]} h8" class="l"/>')
A(f'<path d="M{pins[0][0]-30} {top} V{apex[1]}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{pins[0][0]-34}" y="{(top+apex[1])/2}" text-anchor="end" font-size="11">1.0 m</text>')
A(f'<path d="M{pins[0][0]} {top-58} H{pins[1][0]}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{cx}" y="{top-62}" text-anchor="middle" font-size="11">0.4 m</text>')
lab(pins[1][0] + 18, top, 330, top + 20, ['2-axis load pins Ø20,', 'spherical bushings'])
lab(cx + 0.11 * k, top + 0.5 * k, 330, top + 0.45 * k, ['Ti-6Al-4V, 8 mm,', '30 mm legs, ~2.5 kg'])
lab(apex[0] + 20, apex[1], 330, apex[1] - 10, ['apex boss +', 'spherical bushing'])
lab(apex[0] + 9, apex[1] + 30, 330, apex[1] + 40, ['swaged fork terminal,', 'captive clevis pin'])
lab(apex[0], apex[1] + 130, 330, apex[1] + 120, ['stay: 6 mm 7x19', 'Nitronic 50, white'])
A(f'<text x="30" y="{apex[1]+190}" font-size="11">Hangs straight down when slack; under tension</text><text x="30" y="{apex[1]+204}" font-size="11">it lines up with the stay. No other bracing.</text>')

# ================= B. load pin section =================
A('<text x="470" y="30" class="t">B. Load pin (section)</text>')
bx, by = 560, 150
A(f'<rect x="{bx-80}" y="{by-50}" width="40" height="100" fill="{COL}" opacity="0.6" class="s"/><rect x="{bx+40}" y="{by-50}" width="40" height="100" fill="{COL}" opacity="0.6" class="s"/>')
A(f'<rect x="{bx-30}" y="{by-34}" width="60" height="68" fill="{TI}" class="s"/>')
A(f'<ellipse cx="{bx}" cy="{by}" rx="22" ry="22" fill="#ddd" stroke="#222"/>')
A(f'<rect x="{bx-100}" y="{by-10}" width="200" height="20" fill="{PIN}" class="s"/>')
for gx in (bx - 36, bx + 32):
    A(f'<rect x="{gx}" y="{by-10}" width="4" height="20" fill="{SEN}"/>')
A(f'<rect x="{bx+100}" y="{by-14}" width="10" height="28" fill="#555"/><rect x="{bx+110}" y="{by-6}" width="22" height="12" fill="{SEN}"/>')
A(f'<rect x="{bx-112}" y="{by-14}" width="12" height="28" fill="#555"/>')
lab(bx - 60, by - 50, bx - 60, by - 80, ['collar lug (clevis)'])
lab(bx, by - 22, bx + 50, by - 78, ['spherical bushing (MoS₂ ball,', 'polyimide-lined Ti housing)'])
lab(bx + 34, by + 10, bx + 60, by + 80, ['strain-gauge grooves at the', 'two shear planes, 17-4PH + DLC'])
lab(bx + 121, by + 6, bx + 140, by + 40, ['connector to the', 'collar sensor hub'])
lab(bx - 106, by + 14, bx - 140, by + 74, ['retaining collar'], 'end')

# ================= C. what the pins read =================
A('<text x="470" y="290" class="t">C. What the pins read</text>')
rows = [('Collar torque', 'Pull at apex', 'Pin couple'), ('10 N·m (normal)', '~1.8 N', '±4.5 N'),
        ('200 N·m (interlock)', '~36 N', '±89 N'), ('500 N·m', '~89 N', '±223 N')]
for i, r in enumerate(rows):
    y = 318 + i * 24
    if i == 0:
        A(f'<rect x="465" y="{y-16}" width="330" height="22" fill="#eee"/>')
    for j, c in enumerate(r):
        A(f'<text x="{470+[0,150,250][j]}" y="{y}" font-size="11.5"{" font-weight=\"bold\"" if i == 0 else ""}>{c}</text>')
A('<text x="470" y="420" font-size="11">0.1% pins resolve ~3 N ≈ 7 N·m of collar torque.</text>')
A('<text x="470" y="436" font-size="11">Corrects the earlier "±0.2 kN at 200 N·m".</text>')

# ================= D. foot node =================
A('<text x="820" y="30" class="t">D. Foot node (elevation; mast to the left)</text>')
fx, fy = 1080, 420
A(f'<rect x="{fx-260}" y="{fy}" width="470" height="50" fill="url(#g)"/><line x1="{fx-260}" y1="{fy}" x2="{fx+210}" y2="{fy}" stroke="#222"/>')
A(f'<rect x="{fx-70}" y="{fy}" width="160" height="14" fill="#c9b79c" stroke="#222"/>')
A(f'<path d="M{fx-60} {fy} L{fx-40} {fy-60} H{fx+70} L{fx+80} {fy} Z" fill="{TI}" opacity="0.6" class="s"/>')
# strut ball joint and strut going up-left at 53 deg
bxj, byj = fx - 30, fy - 64
A(f'<circle cx="{bxj}" cy="{byj}" r="12" fill="#ddd" class="s"/>')
a = radians(53)
A(f'<line x1="{bxj}" y1="{byj}" x2="{bxj-260*cos(a):.0f}" y2="{byj-260*sin(a):.0f}" stroke="#7d8790" stroke-width="9"/>')
# stay tensioner: drum, worm box, motor, buffer, load cell, stay up-left at 65 deg
dx, dy = fx + 30, fy - 92
A(f'<circle cx="{dx}" cy="{dy}" r="26" fill="#bbb" class="s"/>')
for r_ in (8, 14, 20):
    A(f'<circle cx="{dx}" cy="{dy}" r="{r_}" fill="none" stroke="{STAY}" stroke-width="1"/>')
A(f'<rect x="{dx+30}" y="{dy-14}" width="40" height="28" fill="#7fa3d6" class="s"/><rect x="{dx+70}" y="{dy-10}" width="34" height="20" fill="#5d7fb8" class="s"/>')
A(f'<text x="{dx+50}" y="{dy+28}" font-size="9.5" text-anchor="middle">worm</text><text x="{dx+87}" y="{dy+28}" font-size="9.5" text-anchor="middle">motor</text>')
a = radians(65)
sx0, sy0 = dx - 22, dy - 14
A(f'<rect x="{sx0-14}" y="{sy0-34}" width="16" height="22" fill="{SEN}" transform="rotate(-25 {sx0-6} {sy0-23})"/>')
for i in range(4):
    A(f'<path d="M{sx0-28+i*-5} {sy0-46-i*11} l12 -5 l12 5" stroke="{SPR}" stroke-width="2" fill="none" transform="rotate(-25 {sx0-16} {sy0-56})"/>')
A(f'<line x1="{sx0}" y1="{sy0}" x2="{sx0-310*cos(a):.0f}" y2="{sy0-310*sin(a):.0f}" stroke="{STAY}" stroke-width="3"/>')
A(f'<path d="M{dx+12} {dy+26} l8 10 l8 -10" stroke="#222" stroke-width="2" fill="none"/>')
# tie tensioner and tie going left at ground level, power/data cable along it
tx, ty = fx - 50, fy - 20
A(f'<rect x="{tx-30}" y="{ty-14}" width="30" height="28" fill="#bbb" class="s"/>')
A(f'<line x1="{tx-30}" y1="{ty}" x2="{fx-260}" y2="{ty}" stroke="#c87f0a" stroke-width="3"/>')
A(f'<line x1="{tx-30}" y1="{ty+8}" x2="{fx-260}" y2="{ty+8}" stroke="#2e7d32" stroke-width="2" stroke-dasharray="6 3"/>')
lab(bxj - 150, byj - 200, fx - 230, fy - 300, ['A-frame strut (CFRP), 53°'], 'start')
lab(sx0 - 120, sy0 - 257, fx - 60, fy - 370, ['stay to the V-link, 65°'], 'start')
lab(sx0 - 30, sy0 - 60, fx + 20, fy - 250, ['Belleville buffer 40 kN/m ±15 mm', '+ in-line load cell'], 'start')
lab(dx + 20, dy - 20, fx + 60, fy - 190, ['drum Ø0.3 m (spare stay)', 'self-locking 50:1 worm', '+ 30:1 planetary', '~1 N·m motor'], 'start')
lab(dx + 20, dy + 34, fx + 120, fy - 40, ['ratchet pawl +', 'hand-drive socket'], 'start')
lab(bxj, byj + 10, fx - 150, fy + 75, ['strut ball joint on the Ti foot frame'], 'start')
lab(tx - 60, ty, fx - 250, fy - 60, ['tie tensioner (same unit, 1 kN)'], 'start')
lab(fx - 200, ty + 8, fx - 240, fy + 95, ['power + data cable along the tie to the base'], 'start')
A(f'<text x="{fx-250}" y="{fy+130}" font-size="11">Net on the pad at 1.5 kN stay / 1 kN tie / 2.5 kN strut: −0.14 kN sideways, 0.64 kN down</text>')

# ================= E. thermal: why the tensioner is active =================
ex, ey = 20, 680
A(f'<text x="{ex}" y="{ey}" class="t">E. Stay tension swing over a sun/shade cycle (67 m of 6 mm stainless)</text>')
bars = [('Bare, held rigid', 2.6, '#c0392b', '±2.6 kN (~220 K, ~250 mm)'),
        ('White-coated, held rigid (power off)', 1.3, '#e67e22', '±1.3 kN (~110 K, ~120 mm): 0.2–2.8 kN, never slack'),
        ('White-coated, servo tensioner on', 0.1, '#2e7d32', '±0.1 kN deadband (buffer drift ~7 mm)')]
z0 = 700
sc = 100
A(f'<line x1="{z0}" y1="{ey+18}" x2="{z0}" y2="{ey+150}" stroke="#222"/>')
for i, (name, v, c, t) in enumerate(bars):
    y = ey + 30 + i * 40
    A(f'<text x="420" y="{y+16}" text-anchor="end" font-size="12">{name}</text>')
    A(f'<rect x="{z0-v*sc:.0f}" y="{y}" width="{2*v*sc:.0f}" height="22" fill="{c}" opacity="0.85"/>')
    A(f'<text x="{z0+v*sc+10:.0f}" y="{y+16}" font-size="11.5">{t}</text>')
A(f'<text x="{z0}" y="{ey+170}" text-anchor="middle" font-size="11">set point 1.5 kN</text>')
A(f'<text x="{ex}" y="{ey+200}" font-size="11.5">The CFRP mast and struts barely change length; the steel stays and ties do. A soft spring would absorb it but make the bracing soft against quakes,</text>')
A(f'<text x="{ex}" y="{ey+216}" font-size="11.5">so the foot winch stays on as a slow servo (0.5 mm/s; the stay\'s thermal time constant is ~20 min). Alternative for later: a coated CFRP rod stay (α ≈ 0).</text>')
A('</svg>')
open('vlink-tensioner.svg', 'w').write('\n'.join(o))
