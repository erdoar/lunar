# Generates cartridge.svg (rev 29): collar roller cartridge section, roller detail, collar plan, numbers and swap.
# Run: python3 make_cartridge_svg.py
from math import sin, cos, radians, sqrt

o = []
A = o.append
W, H = 1300, 980
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><pattern id="hc" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M0 6L6 0" stroke="#bbb"/></pattern></defs>')
A('<style>.s{stroke:#222;stroke-width:1.3}.l{stroke:#555;stroke-width:1;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')
TI, ST, CER, MAST, COL, SPR, SEN = '#9fb3c8', '#6b7280', '#e8e0c8', '#e67e22', '#4a9', '#c0392b', '#2c4a7a'


def num(n, x, y, px=None, py=None):
    if px is not None:
        A(f'<path d="M{px:.0f} {py:.0f}L{x:.0f} {y:.0f}" class="l"/><circle cx="{px:.0f}" cy="{py:.0f}" r="2" fill="#222"/>')
    A(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="#fff" stroke="#222"/><text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" '
      f'font-size="10.5" font-weight="bold" style="stroke:none">{n}</text>')


def spring(x0, y0, x1, y1, n=6, w=6):
    pts = [(x0, y0)]
    for i in range(1, 2 * n):
        t = i / (2 * n)
        dx, dy = x1 - x0, y1 - y0
        L = sqrt(dx * dx + dy * dy)
        ox, oy = -dy / L * w * (1 if i % 2 else -1), dx / L * w * (1 if i % 2 else -1)
        pts.append((x0 + dx * t + ox, y0 + dy * t + oy))
    pts.append((x1, y1))
    A('<polyline points="' + ' '.join(f'{x:.0f},{y:.0f}' for x, y in pts) + f'" fill="none" stroke="{SPR}" stroke-width="2"/>')


# ================= A. section through band and cartridge (radial-vertical plane) =================
s = 1.45                                     # px per mm
R0, Z0 = 860, 0                              # mm: radius at the drawing's left edge, height datum = band mid-height
X = lambda r_mm: 40 + (r_mm - R0) * s
Y = lambda z_mm: 400 - z_mm * s
A('<text x="20" y="30" class="t">A. Section through the band and one cartridge (mast axis to the left)</text>')
# mast leg + band bracket (turns), band box, strips
A(f'<rect x="{X(860)}" y="{Y(150)}" width="{25*s}" height="{300*s}" fill="{MAST}" opacity="0.85" class="s"/>')
A(f'<rect x="{X(885)}" y="{Y(30)}" width="{12*s}" height="{60*s}" fill="{MAST}" class="s"/>')
A(f'<rect x="{X(897)}" y="{Y(60)}" width="{78*s}" height="{120*s}" fill="{TI}" class="s"/>')
A(f'<rect x="{X(905)}" y="{Y(52)}" width="{62*s}" height="{104*s}" fill="#fff" stroke="#888" stroke-dasharray="3 2"/>')
for (x0, y0, w, h) in ((915, 62, 50, 2), (915, -60, 50, 2), (975, 40, 2, 80)):
    A(f'<rect x="{X(x0)}" y="{Y(y0)}" width="{w*s}" height="{h*s+1}" fill="{ST}"/>')
# upper thrust roller (axis radial): tapered rectangle in section, on the top strip
def thrust(zc, up=True):
    rl, rr = 920, 950
    h_l, h_r = 49.2, 50.8                    # half-heights at inner/outer edge (taper exaggerated x1 in mm)
    A(f'<polygon points="{X(rl)},{Y(zc-h_l)} {X(rr)},{Y(zc-h_r)} {X(rr)},{Y(zc+h_r)} {X(rl)},{Y(zc+h_l)}" fill="{CER}" class="s"/>')
    A(f'<rect x="{X(rl+8)}" y="{Y(zc+21)}" width="{14*s}" height="{42*s}" fill="#ddd" stroke="#555"/>')
    A(f'<line x1="{X(890)}" y1="{Y(zc)}" x2="{X(1010)}" y2="{Y(zc)}" stroke="#333" stroke-width="4"/>')
    # axle block, Belleville stack and hard stop in the jaw
    A(f'<rect x="{X(990)}" y="{Y(zc+14)}" width="{30*s}" height="{28*s}" fill="{TI}" class="s"/>')
    yb = zc + (14 if up else -14)
    for k in range(4):
        dy = (k * 5 + 2) * (1 if up else -1)
        A(f'<path d="M{X(992)} {Y(yb+dy)} L{X(1005)} {Y(yb+dy+(3 if up else -3))} L{X(1018)} {Y(yb+dy)}" stroke="{SPR}" stroke-width="2" fill="none"/>')
thrust(60 + 2 + 50, up=True)
thrust(-60 - 2 - 50, up=False)
# radial roller (axis vertical) on a swing arm
A(f'<rect x="{X(977)}" y="{Y(15)}" width="{100*s}" height="{30*s}" fill="{CER}" class="s"/>')
A(f'<rect x="{X(1006)}" y="{Y(6)}" width="{42*s}" height="{12*s}" fill="#ddd" stroke="#555"/>')
A(f'<line x1="{X(1027)}" y1="{Y(40)}" x2="{X(1027)}" y2="{Y(-40)}" stroke="#333" stroke-width="4"/>')
A(f'<path d="M{X(1027)} {Y(-40)} L{X(1110)} {Y(-55)}" stroke="#555" stroke-width="6"/><circle cx="{X(1110)}" cy="{Y(-55)}" r="6" fill="#fff" class="s"/>')
spring(X(1060), Y(-48), X(1110), Y(-100), n=5)
# C-frame (Ti): body outside, two jaws
A(f'<path d="M{X(895)} {Y(168)} H{X(1130)} V{Y(-168)} H{X(895)} V{Y(-185)} H{X(1150)} V{Y(185)} H{X(895)} Z" fill="{TI}" opacity="0.55" class="s"/>')
A(f'<rect x="{X(1130)}" y="{Y(150)}" width="{20*s}" height="{300*s}" fill="{TI}" class="s"/>')
# collar ring with window, dovetail rails, captive bolts, grapple, cam, connector, cover, brush, shelf, transport pin
A(f'<rect x="{X(1150)}" y="{Y(200)}" width="{70*s}" height="{400*s}" fill="{COL}" opacity="0.35" class="s"/>')
for z in (160, -160):
    A(f'<rect x="{X(1150)}" y="{Y(z+6)}" width="{70*s}" height="{12*s}" fill="#888"/>')
for z in (100, -100):
    A(f'<line x1="{X(1135)}" y1="{Y(z)}" x2="{X(1220)}" y2="{Y(z)}" stroke="#222" stroke-width="4"/><rect x="{X(1220)}" y="{Y(z+8)}" width="{10*s}" height="{16*s}" fill="#555"/>')
A(f'<path d="M{X(1230)} {Y(40)} H{X(1265)} V{Y(-40)} H{X(1230)}" fill="none" stroke="#222" stroke-width="5"/>')
A(f'<circle cx="{X(1100)}" cy="{Y(190)}" r="11" fill="#f2c94c" class="s"/><path d="M{X(1100)-5} {Y(190)} h10 M{X(1100)} {Y(190)-5} v10" stroke="#222"/>')
A(f'<rect x="{X(1136)}" y="{Y(-20)}" width="{14*s}" height="{40*s}" fill="{SEN}"/>')
A(f'<path d="M{X(895)} {Y(196)} L{X(1150)} {Y(206)}" stroke="#777" stroke-width="4"/>')
A(f'<path d="M{X(905)} {Y(-182)} H{X(1000)} V{Y(-192)}" fill="none" stroke="#8a5a2b" stroke-width="3"/>')
A(f'<line x1="{X(960)}" y1="{Y(185)}" x2="{X(960)}" y2="{Y(40)}" stroke="#2e7d32" stroke-width="5" stroke-dasharray="6 3"/>')
for (rx, zz) in ((935, 112), (935, -112), (1027, 0)):
    A(f'<rect x="{X(rx)+(24 if rx < 1000 else -6)}" y="{Y(zz)-4}" width="8" height="8" fill="{SEN}"/>')
calls = [(X(872), Y(140), 60, 92), (X(936), Y(0), 60, 470), (X(940), Y(62), 140, 92), (X(935), Y(140), 235, 92),
         (X(1005), Y(112), 330, 92), (X(1010), Y(126), 425, 92), (X(1050), Y(5), 790, 330), (X(1080), Y(-75), 790, 470),
         (X(935), Y(-150), 150, 690), (X(960), Y(150), 520, 92), (X(1100), Y(190), 620, 92), (X(1160), Y(100), 790, 200),
         (X(1250), Y(0), 790, 400), (X(1143), Y(0), 790, 265), (X(1020), Y(201), 720, 92), (X(950), Y(-186), 300, 690),
         (X(1185), Y(-170), 790, 600)]
for n, (px, py, qx, qy) in enumerate(calls, 1):
    num(n, qx, qy, px, py)
key = ['Mast leg + band bracket (turns)', 'Ti box band (turns)', '440C running strips, DLC, 6 segments', 'Upper thrust roller, tapered',
       'Axle block on Belleville stack', 'Hard stop (loaded roller rests here)', 'Radial roller, axis vertical', 'Swing arm + 10 N/mm spring',
       'Lower thrust roller, tapered', 'Transport clamp pin (pulled at height)', 'Release cam: 90° unloads all rollers',
       'Dovetail rail in the collar window', 'Grapple handle', 'Blind-mate 8-pin connector', 'Hinged cover / sunshade',
       'Debris catch shelf', 'Collar ring (stationary)']
ky = 720
for j, t in enumerate(key):
    col, row = divmod(j, 9)
    num(j + 1, 40 + col * 300, ky + row * 22)
    A(f'<text x="{54+col*300}" y="{ky+row*22+4}" font-size="11.5">{t}</text>')
A(f'<text x="40" y="{ky+9*22+10}" font-size="11" fill="#555">Blue squares: tyre and sleeve rotation sensors. Taper of the thrust rollers (3.1°) drawn to scale.</text>')

# ================= B. roller detail =================
A('<text x="860" y="30" class="t">B. One roller: two rotation paths</text>')
bk, bx, by = 2.6, 1040, 200
Bx = lambda mm: bx + mm * bk
By = lambda mm: by - mm * bk
A(f'<rect x="{Bx(-15)}" y="{By(50)}" width="{30*bk}" height="{100*bk}" fill="{CER}" class="s"/>')                 # tyre
A(f'<rect x="{Bx(-15)}" y="{By(30)}" width="{30*bk}" height="{60*bk}" fill="{TI}" class="s"/>')                   # hub
A(f'<rect x="{Bx(-6)}" y="{By(21)}" width="{12*bk}" height="{42*bk}" fill="#ddd" stroke="#222"/>')               # bearing
for yy in (15.5, -15.5):
    A(f'<circle cx="{Bx(0)}" cy="{By(yy)}" r="{3.5*bk}" fill="#333"/>')
A(f'<rect x="{Bx(-8)}" y="{By(10)}" width="{16*bk}" height="{20*bk}" fill="#c9a227" stroke="#222"/>')            # sleeve
A(f'<rect x="{Bx(-40)}" y="{By(8)}" width="{80*bk}" height="{16*bk}" fill="#555"/>')                            # axle
A(f'<rect x="{Bx(-40)}" y="{By(30)}" width="{8*bk}" height="{60*bk}" fill="{TI}" opacity="0.6" class="s"/><rect x="{Bx(32)}" y="{By(30)}" width="{8*bk}" height="{60*bk}" fill="{TI}" opacity="0.6" class="s"/>')
A(f'<rect x="{Bx(12)}" y="{By(44)}" width="{4*bk}" height="{6*bk}" fill="{SEN}"/><rect x="{Bx(12)}" y="{By(6)}" width="{4*bk}" height="{4*bk}" fill="{SEN}"/>')
for j, (px, py, t) in enumerate(((Bx(15), By(45), 'Si₃N₄ tyre, Ø100 x 30 mm, crown R200'),
                                 (Bx(15), By(25), 'Ti hub'),
                                 (Bx(6), By(15), 'Path 1: hybrid 6004 bearing, MoS₂ film'),
                                 (Bx(8), By(0), 'Path 2: MoS₂-polyimide sleeve journal'),
                                 (Bx(40), By(-4), 'DLC-coated axle in the fork'),
                                 (Bx(16), By(-44), 'Magnets on tyre and sleeve → which path turns'))):
    ly = 75 + j * 40
    A(f'<path d="M{px:.0f} {py:.0f}L1135 {ly}" class="l"/><text x="1138" y="{ly+4}" font-size="11">{t if len(t) < 24 else ""}</text>')
    if len(t) >= 24:
        w = t.split(' ')
        h = len(w) // 2
        A(f'<text x="1138" y="{ly+4}" font-size="11">{" ".join(w[:h])}</text><text x="1138" y="{ly+17}" font-size="11">{" ".join(w[h:])}</text>')

# ================= C. collar plan =================
A('<text x="860" y="365" class="t">C. Collar plan: 6 cartridges</text>')
pk, pcx, pcy = 95, 1010, 520
for ac in range(0, 360, 60):
    a = radians(ac + 30)
    x, y = pcx + 1.15 * pk * cos(a), pcy - 1.15 * pk * sin(a)
    A(f'<rect x="{x-14:.0f}" y="{y-10:.0f}" width="28" height="20" fill="{TI}" class="s" transform="rotate({-(ac+30)} {x:.0f} {y:.0f})"/>')
A(f'<circle cx="{pcx}" cy="{pcy}" r="{1.25*pk}" fill="none" stroke="{COL}" stroke-width="10" opacity="0.5"/>')
A(f'<circle cx="{pcx}" cy="{pcy}" r="{0.935*pk}" fill="none" stroke="{TI}" stroke-width="8"/>')
Rm = 1.4 / sqrt(3)
v = [(pcx + Rm * pk * cos(radians(a)), pcy - Rm * pk * sin(radians(a))) for a in (90, 210, 330)]
A('<polygon points="' + ' '.join(f'{x:.0f},{y:.0f}' for x, y in v) + f'" fill="none" stroke="{MAST}" stroke-width="3"/>')
a = radians(30)
x1, y1 = pcx + 0.935 * pk * cos(a), pcy - 0.935 * pk * sin(a)
A(f'<line x1="{pcx}" y1="{pcy}" x2="{x1+20*cos(a):.0f}" y2="{y1-20*sin(a):.0f}" stroke="#555" stroke-dasharray="4 3"/>')
A(f'<text x="{pcx+12}" y="{pcy+22}" font-size="10.5">cone apex on the axis</text>')
for ac in (0, 120, 240):
    a = radians(ac)
    x, y = pcx + 1.38 * pk * cos(a), pcy - 1.38 * pk * sin(a)
    A(f'<rect x="{x-6:.0f}" y="{y-6:.0f}" width="12" height="12" fill="#c87f0a"/>')
A(f'<rect x="{pcx+1.3*pk:.0f}" y="{pcy+60}" width="40" height="22" fill="#f2c94c" class="s"/><text x="{pcx+1.3*pk+46:.0f}" y="{pcy+75}" font-size="10.5">sensor hub, cells,</text><text x="{pcx+1.3*pk+46:.0f}" y="{pcy+88}" font-size="10.5">radio (fails safe)</text>')
A(f'<text x="{pcx-1.6*pk:.0f}" y="{pcy+1.55*pk:.0f}" font-size="10.5">orange squares: V-link lugs · band Ø1.95 m · any one cartridge may be out</text>')

# ================= D. numbers and swap =================
dx, dy = 860, 700
A(f'<text x="{dx}" y="{dy}" class="t">D. Numbers (collar_cartridge_check.py)</text>')
for j, t in enumerate(['Thrust per roller 0.72 kN (upper), 0.95 kN (strut); ≤1.15 kN, one out',
                       'Peak contact ~0.73 GPa · ~20 turns per lunar day',
                       'Collar torque: ~8 N·m normal · ~42 on a sleeve · ~345 skidding',
                       '→ a skidding roller trips the 200 N·m interlock',
                       '~5.9 kg each; 12 fitted + 2 spares',
                       '',
                       'Swap (~30 min, mast parked): bot clips to the collar,',
                       'cam 90°, 2 bolts, draw out, spare in, cam to "run".']):
    A(f'<text x="{dx}" y="{dy+22+j*18}" font-size="11.5"{" font-weight=\"bold\"" if j == 6 else ""}>{t}</text>')
A('</svg>')
open('cartridge.svg', 'w').write('\n'.join(o))
