# Generates collar.svg (roller collar: plan + section). Run: python3 make_collar_svg.py
import math
o = []
A = o.append
W, H = 1240, 730
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="13">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:2}.l{stroke:#555;stroke-width:1;fill:none}.guy{stroke:#8e44ad;stroke-width:2}'
  '.band{fill:#7d8790}.collar{fill:#4a9}.cart{fill:#e0a040}.roll{fill:#bbb}.mast{fill:#888}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:17px;font-weight:bold}</style>')


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*15:.0f}" text-anchor="{anchor}">{t}</text>')


def pol(cx, cy, r, deg):  # 0 deg = up, clockwise
    a = math.radians(deg - 90)
    return cx + r * math.cos(a), cy + r * math.sin(a)


# ---------------- plan view
cx, cy, k = 330, 350, 135  # px per metre
A('<text x="20" y="30" class="t">Plan (looking down the mast)</text>')
RB, RI, RO = 0.95, 1.25, 1.45   # band centre, ring inner, ring outer radii (m)
for d in (0, 120, 240):
    x1, y1 = pol(cx, cy, RO * k, d)
    x2, y2 = pol(cx, cy, 2.2 * k, d)
    A(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="guy"/>')
ri, ro = RI * k, RO * k
A(f'<circle cx="{cx}" cy="{cy}" r="{(ri+ro)/2}" fill="none" stroke="#4a9" stroke-width="{ro-ri}"/>')
A(f'<circle cx="{cx}" cy="{cy}" r="{ri}" fill="none" stroke="#222" stroke-width="2"/><circle cx="{cx}" cy="{cy}" r="{ro}" fill="none" stroke="#222" stroke-width="2"/>')
for d in (60, 180, 300):
    x1, y1 = pol(cx, cy, ri - 4, d)
    x2, y2 = pol(cx, cy, ro + 4, d)
    A(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#fff" stroke-width="5"/><line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#222" stroke-width="1.5" stroke-dasharray="3 3"/>')
for d in (0, 120, 240):
    x, y = pol(cx, cy, ro + 10, d)
    A(f'<rect x="-9" y="-12" width="18" height="24" fill="#555" transform="translate({x:.1f},{y:.1f}) rotate({d})"/>')
rb = RB * k
A(f'<circle cx="{cx}" cy="{cy}" r="{rb}" fill="none" stroke="#7d8790" stroke-width="13"/>')
A(f'<circle cx="{cx}" cy="{cy}" r="{rb+6.5}" fill="none" stroke="#c0392b" stroke-width="2.5"/>')
rl = 0.81 * k
pts = [pol(cx, cy, rl, d) for d in (0, 120, 240)]
A('<polygon points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '" fill="none" stroke="#888" stroke-width="4"/>')
for (x, y), d in zip(pts, (0, 120, 240)):
    bx, by = pol(cx, cy, rb - 6, d)
    A(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{bx:.1f}" y2="{by:.1f}" stroke="#555" stroke-width="7"/>')
    A(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" class="mast s"/>')
for i in range(6):
    d = 30 + 60 * i
    x, y = pol(cx, cy, (rb + 7 + ri + 10) / 2, d)
    A(f'<rect x="-16" y="-{(ri+10-rb-7)/2:.0f}" width="32" height="{ri+10-rb-7:.0f}" rx="3" class="cart s" transform="translate({x:.1f},{y:.1f}) rotate({d})"/>')
    rx, ry = pol(cx, cy, rb + 14, d)
    A(f'<rect x="-9" y="-6" width="18" height="12" rx="3" class="roll s" transform="translate({rx:.1f},{ry:.1f}) rotate({d})"/>')
r = 0.55 * k
x1, y1 = pol(cx, cy, r, 200); x2, y2 = pol(cx, cy, r, 250)
A(f'<path d="M{x1:.0f} {y1:.0f} A{r} {r} 0 0 1 {x2:.0f} {y2:.0f}" fill="none" stroke="#222" stroke-width="1.6" marker-end="url(#ar)"/>')
A(f'<text x="{cx}" y="{cy+4}" text-anchor="middle" font-size="12">Mast turns</text><text x="{cx}" y="{cy+19}" text-anchor="middle" font-size="12">0.51°/h</text>')
x, y = pol(cx, cy, 2.1 * k, 0); lab(x, y, x + 25, y + 5, ['Strut or wire (stationary)'])
x, y = pol(cx, cy, (ri + ro) / 2, 60); lab(x, y, cx + 150, cy - 200, ['Collar ring: 3 x 120° segments', '(stationary, ~50 kg each)'])
x, y = pol(cx, cy, ro, 300); lab(x, y, cx - 160, cy - 215, ['Segment joint,', 'captive bolts'], 'end')
x, y = pol(cx, cy, ro + 16, 120); lab(x, y, cx + 215, cy + 160, ['Lug + load pin'])
x, y = pol(cx, cy, (rb + ri) / 2, 150); lab(x, y, cx + 120, cy + 235, ['6 roller cartridges', '(any one removable)'])
x, y = pol(cx, cy, rb + 6, 210); lab(x, y, cx - 120, cy + 250, ['Collar band on the mast (rotates;', 'red = running face)'], 'end')
x, y = pts[2]; lab(x - 6, y, 150, cy - 60, ['CFRP mast leg', '+ band bracket'], 'end')
A(f'<text x="20" y="{H-38}" font-size="12">Mast face 1.4 m. Band Ø1.9 m. Collar ring Ø2.5–2.9 m.</text>')
A(f'<text x="20" y="{H-22}" font-size="12">Struts/wires at 0°/120°/240°; segment joints between them.</text>')

# ---------------- section through one cartridge (numbered callouts)
A('<g transform="translate(40,0)">')
A('<text x="640" y="30" class="t">Section through a cartridge</text>')
A('<rect x="650" y="150" width="26" height="320" class="mast s"/>')
A('<rect x="676" y="306" width="40" height="28" fill="#555" class="s"/>')
A('<rect x="716" y="290" width="90" height="60" class="band s"/>')
for x1, y1, x2, y2 in ((716, 290, 806, 290), (806, 290, 806, 350), (716, 350, 806, 350)):
    A(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#c0392b" stroke-width="4"/>')
A('<rect x="718" y="262" width="6" height="28" class="band s"/>')
A('<path d="M736 222 H950 V242 H866 V398 H950 V418 H736 V398 H846 V242 H736 Z" class="cart s"/>')
A('<line x1="770" y1="242" x2="770" y2="252" stroke="#222" stroke-width="3"/><circle cx="770" cy="270" r="19" class="roll s"/><circle cx="770" cy="270" r="4" fill="#222"/>')
A('<rect x="808" y="300" width="34" height="40" rx="5" class="roll s"/><line x1="825" y1="242" x2="825" y2="300" stroke="#222" stroke-width="3"/><line x1="825" y1="340" x2="825" y2="398" stroke="#222" stroke-width="3"/>')
A('<line x1="770" y1="398" x2="770" y2="386" stroke="#222" stroke-width="3"/><circle cx="770" cy="369" r="17" class="roll s"/><circle cx="770" cy="369" r="4" fill="#222"/>')
A('<rect x="796" y="196" width="10" height="110" fill="#c0392b" stroke="#222" stroke-width="1.5"/>')
A('<rect x="900" y="196" width="120" height="26" class="collar s"/><rect x="900" y="418" width="120" height="26" class="collar s"/>')
A('<rect x="1000" y="222" width="20" height="196" class="collar s"/>')
A('<line x1="900" y1="232" x2="1000" y2="232" stroke="#222" stroke-width="2" stroke-dasharray="6 3"/><line x1="900" y1="408" x2="1000" y2="408" stroke="#222" stroke-width="2" stroke-dasharray="6 3"/>')
A('<path d="M950 320 l6 -10 6 20 6 -20 6 20 6 -20 6 20 6 -10 h6" fill="none" stroke="#222" stroke-width="2"/>')
A('<rect x="1020" y="306" width="30" height="28" fill="#e0a040" class="s"/><circle cx="1058" cy="320" r="9" fill="#fff" class="s"/>')
A('<rect x="955" y="186" width="8" height="40" fill="#333"/><rect x="955" y="414" width="8" height="40" fill="#333"/>')
A('<rect x="1000" y="444" width="22" height="34" fill="#555" class="s"/><circle cx="1011" cy="468" r="5" fill="#fff"/>')
A('<line x1="1011" y1="468" x2="1100" y2="530" class="guy"/>')
A('<path d="M1080 230 V280" stroke="#8e44ad" stroke-width="2" marker-end="url(#ar)"/><path d="M1080 230 H1125" stroke="#8e44ad" stroke-width="2" marker-end="url(#ar)"/><text x="1078" y="214" font-size="11">Wire pull</text>')


def call(n, tx, ty, x, y):
    A(f'<path d="M{tx} {ty}L{x} {y}" class="l"/><circle cx="{x}" cy="{y}" r="10" fill="#fff" stroke="#222" stroke-width="1.5"/>'
      f'<text x="{x}" y="{y+4}" text-anchor="middle" font-size="11" font-weight="bold" style="stroke:none">{n}</text>')


C = [(1, 663, 180, 640, 120, 'CFRP mast leg'),
     (2, 696, 334, 690, 400, 'Band bracket'),
     (3, 760, 340, 735, 470, 'Collar band (turns with mast), Ti ring'),
     (4, 721, 265, 700, 230, 'Dust lip'),
     (5, 760, 258, 740, 160, 'Upper thrust roller: downward pull'),
     (6, 842, 325, 880, 470, 'Radial roller: holds mast sideways'),
     (7, 780, 380, 805, 470, 'Lower thrust roller: upward push'),
     (8, 801, 200, 801, 140, 'Clamp pin: locks collar for jack-up'),
     (9, 920, 232, 880, 175, 'Slide rails'),
     (10, 980, 315, 975, 275, 'Preload spring: ±10 mm thermal float'),
     (11, 1015, 200, 1010, 140, 'Collar ring (stationary)'),
     (12, 959, 190, 940, 140, 'Captive bolts (2 per cartridge)'),
     (13, 1058, 330, 1075, 375, 'Grapple for the climber robot'),
     (14, 1011, 478, 1050, 500, 'Strut/wire lug with load pin')]
for n, tx, ty, x, y, _ in C:
    call(n, tx, ty, x, y)
A('</g>')
ky = 568
for i, (n, *_r, t) in enumerate(C):
    col, row = divmod(i, 7)
    x = 680 + col * 270
    y = ky + row * 19
    A(f'<circle cx="{x}" cy="{y-4}" r="8" fill="#fff" stroke="#222" stroke-width="1.2"/><text x="{x}" y="{y}" text-anchor="middle" font-size="10" font-weight="bold" style="stroke:none">{n}</text>')
    A(f'<text x="{x+13}" y="{y}" font-size="11.5">{t}</text>')
A(f'<text x="680" y="{ky+7*19+4}" font-size="11.5">Red = ceramic/DLC running faces. Upper collar is pulled down, mid collar pushed up: same cartridge.</text>')
A('</svg>')
open('collar.svg', 'w').write('\n'.join(o))
