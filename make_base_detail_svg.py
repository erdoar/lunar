# Generates base-detail.svg (rev 26): drive cartridge, plan inside the enclosure, enclosure half-section with labyrinth.
# Run: python3 make_base_detail_svg.py
from math import sin, cos, radians, pi

o = []
A = o.append
W, H = 1300, 1080
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker>'
  '<pattern id="hc" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M0 6L6 0" stroke="#bbb"/></pattern></defs>')
A('<style>.s{stroke:#222;stroke-width:1.4}.l{stroke:#555;stroke-width:1;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}.k{font-size:11.5px}</style>')
ROT, FIX, DRV, SR, ENC, MLI, RAD = '#e67e22', '#7d8790', '#7fa3d6', '#bfa6d9', '#3a7d6b', '#c9a227', '#9ec9e8'


def num(n, x, y, px=None, py=None):
    if px is not None:
        A(f'<path d="M{px:.0f} {py:.0f}L{x:.0f} {y:.0f}" class="l"/><circle cx="{px:.0f}" cy="{py:.0f}" r="2" fill="#222"/>')
    A(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="#fff" stroke="#222"/><text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" '
      f'font-size="10.5" font-weight="bold" style="stroke:none">{n}</text>')


def key(x, y, items, dy=18):
    for j, t in enumerate(items):
        num(j + 1, x, y + j * dy)
        A(f'<text x="{x+14}" y="{y+j*dy+4}" class="k">{t}</text>')


# ================= A. drive cartridge, seen from outside (looking toward the mast axis) =================
s = 560
U = lambda u: 300 + u * s
Zp = lambda z: 70 + (1.17 - z) * s
A('<text x="20" y="30" class="t">A. Drive cartridge (one of two), seen from outside</text>')
A('<text x="20" y="48" fill="#555">Worm and motor run tangentially; the pin wheel meshes the pin ring from outside.</text>')
# foot plate + pin ring (rotating, behind)
A(f'<rect x="{U(-0.48)}" y="{Zp(1.14)}" width="{0.90*s}" height="{0.06*s}" fill="{ROT}" class="s"/>')
for z0 in (1.06, 0.94):
    A(f'<rect x="{U(-0.48)}" y="{Zp(z0+0.02)}" width="{0.90*s}" height="{0.02*s}" fill="{ROT}" opacity="0.85" class="s"/>')
u = -0.47
while u < 0.42:
    A(f'<rect x="{U(u)-5.6}" y="{Zp(1.06)}" width="11.2" height="{0.10*s}" fill="#ccc" stroke="#555"/>')
    u += 0.0393
A(f'<rect x="{U(-0.48)}" y="{Zp(0.94)}" width="{0.90*s}" height="5" fill="#2c4a7a"/>')            # magnetic scale
# pin wheel, limiter, output housing, worm-wheel box
A(f'<rect x="{U(-0.075)}" y="{Zp(1.035)}" width="{0.15*s}" height="{0.05*s}" fill="#9aa" class="s"/>')
for j in range(7):
    A(f'<line x1="{U(-0.065+j*0.0217)}" y1="{Zp(1.035)}" x2="{U(-0.065+j*0.0217)}" y2="{Zp(0.985)}" stroke="#555"/>')
A(f'<rect x="{U(-0.05)}" y="{Zp(0.985)}" width="{0.10*s}" height="{0.05*s}" fill="#f2c94c" class="s"/>')
A(f'<rect x="{U(-0.04)}" y="{Zp(0.935)}" width="{0.08*s}" height="{0.13*s}" fill="{DRV}" class="s"/>')
A(f'<rect x="{U(-0.13)}" y="{Zp(0.805)}" width="{0.26*s}" height="{0.18*s}" fill="{DRV}" class="s"/>')
A(f'<line x1="{U(-0.26)}" y1="{Zp(0.70)}" x2="{U(0.17)}" y2="{Zp(0.70)}" stroke="#333" stroke-width="5"/>')       # worm shaft
for j in range(9):
    A(f'<line x1="{U(-0.09+j*0.02)}" y1="{Zp(0.72)}" x2="{U(-0.08+j*0.02)}" y2="{Zp(0.68)}" stroke="#222" stroke-width="1.5"/>')
A(f'<rect x="{U(-0.27)}" y="{Zp(0.755)}" width="{0.13*s}" height="{0.11*s}" fill="{DRV}" class="s"/><text x="{U(-0.205)}" y="{Zp(0.70)+4}" text-anchor="middle" font-size="10" style="stroke:none">50:1</text>')
A(f'<rect x="{U(-0.43)}" y="{Zp(0.765)}" width="{0.16*s}" height="{0.13*s}" fill="#5d7fb8" class="s"/><text x="{U(-0.35)}" y="{Zp(0.70)+4}" text-anchor="middle" font-size="10.5" fill="#fff" style="stroke:none">motor</text>')
A(f'<rect x="{U(-0.47)}" y="{Zp(0.74)}" width="{0.04*s}" height="{0.08*s}" fill="#ddd" class="s"/>')                 # resolver
A(f'<polygon points="{U(0.17)},{Zp(0.72)} {U(0.20)},{Zp(0.72)} {U(0.21)},{Zp(0.70)} {U(0.20)},{Zp(0.68)} {U(0.17)},{Zp(0.68)}" fill="#ddd" stroke="#222"/>')  # hex
# swing plate, pivot pin, preload spring, mesh release, dovetail, connector
A(f'<rect x="{U(-0.48)}" y="{Zp(0.47)}" width="{0.72*s}" height="{0.03*s}" fill="#aab" class="s"/>')
A(f'<rect x="{U(-0.48)}" y="{Zp(0.44)}" width="{0.72*s}" height="{0.03*s}" fill="url(#hc)" stroke="#555"/>')
A(f'<line x1="{U(-0.13)}" y1="{Zp(0.62)}" x2="{U(-0.13)}" y2="{Zp(0.47)}" stroke="#555" stroke-width="6"/><line x1="{U(0.13)}" y1="{Zp(0.62)}" x2="{U(0.13)}" y2="{Zp(0.47)}" stroke="#555" stroke-width="6"/>')
A(f'<line x1="{U(-0.35)}" y1="{Zp(0.635)}" x2="{U(-0.35)}" y2="{Zp(0.47)}" stroke="#555" stroke-width="6"/>')
A(f'<circle cx="{U(0.21)}" cy="{Zp(0.485)}" r="9" fill="#fff" stroke="#222" stroke-width="2"/><line x1="{U(0.21)}" y1="{Zp(0.50)+9}" x2="{U(0.21)}" y2="{Zp(0.44)}" stroke="#222" stroke-width="3"/>')
A('<path d="M' + ' '.join(f'{U(0.0)+((-1)**j)*7:.0f},{Zp(0.47)+6+j*5:.0f}' for j in range(8)) + '" fill="none" stroke="#c0392b" stroke-width="2"/>')
A(f'<rect x="{U(0.05)}" y="{Zp(0.50)-6}" width="22" height="16" fill="#f2c94c" class="s"/>')
A(f'<rect x="{U(-0.46)}" y="{Zp(0.47)+2}" width="22" height="12" fill="#555"/>')
A(f'<rect x="{U(0.32)}" y="{Zp(0.94)+8}" width="24" height="14" fill="#2c4a7a" class="s"/><line x1="{U(0.32)+12}" y1="{Zp(0.94)+22}" x2="{U(0.32)+12}" y2="{Zp(0.47)}" stroke="#555" stroke-width="3"/>')
A(f'<rect x="{U(-0.48)}" y="{Zp(0.42)}" width="{0.90*s}" height="{0.02*s}" fill="{FIX}" class="s"/>')                # deck
pts = [(U(0.33), Zp(1.12), U(0.25), Zp(1.10)), (U(0.42), Zp(1.03), U(0.30), Zp(1.03)), (U(0.15), Zp(1.05), U(0.06), Zp(1.03)),
       (U(0.15), Zp(0.97), U(0.05), Zp(0.97)), (U(0.20), Zp(0.88), U(0.13), Zp(0.84)), (U(0.17), Zp(0.62), U(0.0), Zp(0.70)),
       (U(-0.20), Zp(0.84), U(-0.205), Zp(0.755)), (U(-0.35), Zp(0.84), U(-0.35), Zp(0.765)), (U(0.27), Zp(0.62), U(0.20), Zp(0.70)),
       (U(0.27), Zp(0.535), U(0.21), Zp(0.50)), (U(0.06), Zp(0.565), U(0.01), Zp(0.47)+10), (U(0.12), Zp(0.535), U(0.08), Zp(0.50)),
       (U(-0.43), Zp(0.55), U(-0.44), Zp(0.47)+8), (U(0.42), Zp(0.94), U(0.36), Zp(0.94)+14), (U(0.42), Zp(0.405), U(0.30), Zp(0.43))]
for n, (x, y, px, py) in enumerate(pts, 1):
    num(n, x, y, px, py)
key(560, 80, ['Foot plate (turns)', 'Pin ring: 96 pins Ø20 mm, sleeved', 'Pin wheel, 12 teeth, DLC', 'Ball-detent torque limiter',
              'Output shaft + bearings', 'Self-locking 60:1 worm', '50:1 planetary', '~20 W brushless motor + resolver',
              'Hex socket: hand drive by bot', 'Swing-plate pivot pin', 'Preload spring ~400 N into mesh',
              'Mesh release cam (pin-puller)', 'Blind-mate connector', 'Magnetic scale + read head', 'Dovetail slide, 2 captive bolts'])
A(f'<text x="560" y="{80+15*18+12}" class="k" fill="#555">~14 kg; 24,000:1; 0.07 N·m at the motor</text>')
A(f'<text x="560" y="{80+15*18+28}" class="k" fill="#555">for 500 N·m at the ring</text>')

# ================= B. plan inside the enclosure =================
pk, pcx, pcy = 205, 1035, 300
P = lambda r, a: (pcx + r * pk * cos(radians(a)), pcy - r * pk * sin(radians(a)))
A(f'<text x="830" y="30" class="t">B. Plan inside the enclosure</text>')
A(f'<rect x="{pcx-1.0*pk}" y="{pcy-1.0*pk}" width="{2*pk}" height="{2*pk}" fill="none" stroke="{FIX}" stroke-dasharray="6 4"/>')
A(f'<circle cx="{pcx}" cy="{pcy}" r="{1.06*pk}" fill="none" stroke="{ROT}" stroke-width="1.5" stroke-dasharray="8 4"/>')
panels = {30: ('C', '#eee'), 90: ('D', '#eee'), 150: ('R', RAD), 210: ('R', RAD), 270: ('D', '#eee'), 330: ('R', RAD)}
for ac, (lab_, col) in panels.items():
    a0, a1 = ac - 29, ac + 29
    x0, y0 = P(0.98, a0); x1, y1 = P(0.98, a1); x2, y2 = P(0.93, a1); x3, y3 = P(0.93, a0)
    A(f'<path d="M{x0:.1f} {y0:.1f} A{0.98*pk} {0.98*pk} 0 0 0 {x1:.1f} {y1:.1f} L{x2:.1f} {y2:.1f} A{0.93*pk} {0.93*pk} 0 0 1 {x3:.1f} {y3:.1f} Z" fill="{col}" stroke="{ENC}" stroke-width="2"/>')
    tx, ty = P(1.12, ac)
    A(f'<text x="{tx:.0f}" y="{ty+4:.0f}" text-anchor="middle" font-weight="bold" fill="{ENC}">{lab_}</text>')
for ac in range(0, 360, 60):
    x0, y0 = P(0.91, ac); x1, y1 = P(1.0, ac)
    A(f'<line x1="{x0:.0f}" y1="{y0:.0f}" x2="{x1:.0f}" y2="{y1:.0f}" stroke="#222" stroke-width="2"/>')
# pin ring, slip ring, flange, ball, cup rim, keeper hooks, opening
A(f'<circle cx="{pcx}" cy="{pcy}" r="{0.6*pk}" fill="none" stroke="{ROT}" stroke-width="7" opacity="0.35"/>')
for j in range(96):
    x, y = P(0.6, j * 3.75)
    A(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.6" fill="#555"/>')
A(f'<circle cx="{pcx}" cy="{pcy}" r="{0.465*pk}" fill="none" stroke="{SR}" stroke-width="{0.07*pk}"/>')
A(f'<circle cx="{pcx}" cy="{pcy}" r="{0.31*pk}" fill="#d0d4d8" stroke="#222"/>')
A(f'<circle cx="{pcx}" cy="{pcy}" r="{0.245*pk}" fill="#9fb3c8" stroke="#222"/>')
A(f'<circle cx="{pcx}" cy="{pcy}" r="{0.15*pk}" fill="none" stroke="{ROT}" stroke-width="2" stroke-dasharray="4 3"/>')
A(f'<circle cx="{pcx}" cy="{pcy}" r="{0.275*pk}" fill="none" stroke="{ROT}" stroke-width="1.2" stroke-dasharray="2 3"/>')
for ac in (90, 210, 330):
    x, y = P(0.345, ac)
    A(f'<rect x="{x-6:.0f}" y="{y-6:.0f}" width="12" height="12" fill="{ROT}" class="s"/>')
# drive cartridges (tangential) at 90 and 270, with scale heads
for ac in (90, 270):
    x, y = P(0.675, ac)
    A(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{0.075*pk:.0f}" fill="#9aa" class="s"/>')
    yy = y + (-1 if ac == 90 else 1) * 0.11 * pk
    A(f'<rect x="{x-0.47*pk:.0f}" y="{yy-0.06*pk:.0f}" width="{0.66*pk:.0f}" height="{0.12*pk:.0f}" fill="{DRV}" opacity="0.85" class="s"/>')
    hx, hy = P(0.6, ac + 25)
    A(f'<rect x="{hx-5:.0f}" y="{hy-5:.0f}" width="10" height="10" fill="#2c4a7a"/>')
# debris drawer, radiator straps
dx, dy = P(0.5, 200)
A(f'<rect x="{dx-0.12*pk:.0f}" y="{dy-0.08*pk:.0f}" width="{0.24*pk:.0f}" height="{0.16*pk:.0f}" fill="none" stroke="#8a5a2b" stroke-width="2" stroke-dasharray="4 2"/>')
for ac in (150, 210, 330):
    x0, y0 = P(0.5, ac); x1, y1 = P(0.93, ac)
    A(f'<path d="M{x0:.0f} {y0:.0f} L{x1:.0f} {y1:.0f}" stroke="#b87333" stroke-width="3" stroke-dasharray="2 2"/>')
cx_, cy_ = P(0.9, 30)
A(f'<path d="M{pcx} {pcy} L{cx_:.0f} {cy_:.0f}" stroke="{ROT}" stroke-width="1.5" stroke-dasharray="1 0" marker-end="url(#ar)" opacity="0"/>')
labs = [((0.98, 120), (1.2, 118), 'Fixed tub, 6 panels'), ((1.06, 60), (1.25, 62), 'Rotating lid edge'),
        ((0.6, 160), (1.2, 172), 'Pin ring'), ((0.465, 125), (1.25, 140), 'Slip ring')]
for (r0, a0), (r1, a1), t in labs:
    x0, y0 = P(r0, a0); x1, y1 = P(r1, a1)
    anchor = 'end' if x1 < pcx else 'start'
    A(f'<path d="M{x0:.0f} {y0:.0f}L{x1:.0f} {y1:.0f}" class="l"/><text x="{x1+(-4 if anchor=="end" else 4):.0f}" y="{y1+4:.0f}" text-anchor="{anchor}" font-size="11">{t}</text>')
ky = pcy + 1.215 * pk
for j, t in enumerate(['C cup side · D drive door · R radiator (louvred, strapped to the slip ring)',
                       'Blue: drive cartridges · orange: keeper hooks · dotted: foot-plate opening',
                       'Brown: debris drawer under the deck · dark blue: azimuth scale heads']):
    A(f'<text x="790" y="{ky+j*15:.0f}" font-size="11">{t}</text>')

# ================= C. enclosure half-section =================
cs = 330
R_ = lambda r: 60 + r * cs
Zc = lambda z: 610 + (1.32 - z) * cs
def PC(deg, r):
    return R_(r * sin(radians(deg))), Zc(0.75 + r * cos(radians(deg)))
A('<text x="20" y="580" class="t">C. Enclosure half-section (axis at left)</text>')
A(f'<line x1="{R_(0)}" y1="{Zc(1.32)}" x2="{R_(0)}" y2="{Zc(0.30)}" stroke="#999" stroke-dasharray="10 4 2 4"/>')
A(f'<rect x="{R_(0)}" y="{Zc(0.40)}" width="{1.05*cs}" height="{0.03*cs}" fill="{FIX}" class="s"/>')                     # deck
A(f'<rect x="{R_(0.22)}" y="{Zc(0.37)}" width="{0.22*cs}" height="{0.05*cs}" fill="none" stroke="#8a5a2b" stroke-width="2" stroke-dasharray="4 2"/>')
A(f'<rect x="{R_(0)}" y="{Zc(0.79)}" width="{0.17*cs}" height="{0.39*cs}" fill="{FIX}" class="s"/>')                      # pedestal
A(f'<path d="M{R_(0.17)} {Zc(0.63)} L{R_(0.31)} {Zc(0.578)} V{Zc(0.555)} H{R_(0)} V{Zc(0.63)} Z" fill="{FIX}" class="s"/>')
x80, y80 = PC(80, 0.25)
A(f'<path d="M{R_(0)} {Zc(1.0)} A{0.25*cs} {0.25*cs} 0 0 1 {x80:.1f} {y80:.1f} V{Zc(0.79)} H{R_(0)} Z" fill="#9fb3c8" class="s"/>')
c1 = PC(35, 0.25); c2 = PC(35, 0.264)
A(f'<path d="M{R_(0)} {Zc(1.014)} A{0.264*cs} {0.264*cs} 0 0 1 {c2[0]:.1f} {c2[1]:.1f} V{Zc(1.08)} H{R_(0.27)} V{Zc(1.14)} H{R_(0.32)} V{Zc(1.17)} H{R_(0)} Z" fill="{ROT}" class="s"/>')  # holder ring
A(f'<path d="M{R_(0)} {Zc(1.0)} A{0.25*cs} {0.25*cs} 0 0 1 {c1[0]:.1f} {c1[1]:.1f} L{c2[0]:.1f} {c2[1]:.1f} A{0.264*cs} {0.264*cs} 0 0 0 {R_(0)} {Zc(1.014)} Z" fill="#e3d08e" stroke="#222"/>')  # cup
A(f'<rect x="{R_(0.275)}" y="{Zc(1.14)}" width="{0.445*cs}" height="{0.06*cs}" fill="{ROT}" class="s"/>')                 # foot plate
A(f'<line x1="{R_(0.68)}" y1="{Zc(1.14)}" x2="{R_(0.68)}" y2="{Zc(1.32)}" stroke="{ROT}" stroke-width="6"/>')
A(f'<path d="M{R_(0.36)} {Zc(1.08)} V{Zc(0.52)} H{R_(0.26)} V{Zc(0.545)} H{R_(0.335)} V{Zc(1.08)} Z" fill="{ROT}" class="s"/>')
A(f'<line x1="{R_(0.465)}" y1="{Zc(0.40)}" x2="{R_(0.465)}" y2="{Zc(0.80)}" stroke="{FIX}" stroke-width="5"/>')
A(f'<rect x="{R_(0.43)}" y="{Zc(0.905)}" width="{0.07*cs}" height="{0.105*cs}" fill="{SR}" class="s"/>')
A(f'<rect x="{R_(0.43)}" y="{Zc(1.08)}" width="{0.07*cs}" height="{0.165*cs}" fill="{SR}" stroke="{ROT}" stroke-width="2.5"/>')
A('<path d="M' + ' '.join(f'{R_(0.50)+j*((0.98-0.50)*cs/12):.0f},{Zc(0.86)+(4 if j % 2 else -4):.0f}' for j in range(13)) + f'" fill="none" stroke="#b87333" stroke-width="2.5"/>')
for z0 in (1.06, 0.94):
    A(f'<rect x="{R_(0.555)}" y="{Zc(z0+0.02)}" width="{0.11*cs}" height="{0.02*cs}" fill="{ROT}" class="s"/>')
A(f'<rect x="{R_(0.59)}" y="{Zc(1.06)}" width="{0.02*cs}" height="{0.10*cs}" fill="#ccc" stroke="#555"/>')
A(f'<rect x="{R_(0.61)}" y="{Zc(1.035)}" width="{0.13*cs}" height="{0.05*cs}" fill="#9aa" class="s"/>')
A(f'<rect x="{R_(0.64)}" y="{Zc(0.985)}" width="{0.07*cs}" height="{0.49*cs}" fill="{DRV}" class="s"/>')
A(f'<circle cx="{R_(0.80)}" cy="{Zc(0.70)}" r="{0.065*cs}" fill="#5d7fb8" class="s"/>')
A(f'<rect x="{R_(0.60)}" y="{Zc(0.495)}" width="{0.32*cs}" height="{0.03*cs}" fill="#aab" class="s"/>')
for (rr, zz) in ((0.675, 0.62), (0.465, 0.86), (0.20, 1.04)):
    A(f'<rect x="{R_(rr)-5}" y="{Zc(zz)-4}" width="10" height="8" fill="#c0392b"/>')
A(f'<rect x="{R_(0.98)}" y="{Zc(1.02)}" width="{0.02*cs}" height="{0.62*cs}" fill="{ENC}"/>')
A(f'<line x1="{R_(0.972)}" y1="{Zc(1.0)}" x2="{R_(0.972)}" y2="{Zc(0.72)}" stroke="{MLI}" stroke-width="3" stroke-dasharray="5 3"/>')
A(f'<rect x="{R_(1.0)}" y="{Zc(0.95)}" width="5" height="{0.33*cs}" fill="{RAD}" stroke="#222" stroke-width="0.8"/>')
A(f'<path d="M{R_(0.96)} {Zc(0.43)} V{Zc(0.40)} M{R_(1.02)} {Zc(0.43)} V{Zc(0.40)}" stroke="{ENC}" stroke-width="3"/>')
A(f'<path d="M{R_(0.72)} {Zc(1.11)} H{R_(1.05)} V{Zc(0.95)} M{R_(0.955)} {Zc(1.11)} V{Zc(0.97)}" fill="none" stroke="{ROT}" stroke-width="4"/>')
A(f'<line x1="{R_(1.12)}" y1="{Zc(0.40)}" x2="{R_(1.12)}" y2="{Zc(1.32)}" stroke="#2e7d32" stroke-width="3" stroke-dasharray="8 4"/>')
cpts = {1: ((0.08, 0.88), (0.08, 0.88)), 2: ((0.10, 1.005), (0.13, 1.27)), 3: ((0.05, 1.10), (0.04, 1.27)), 4: ((0.50, 1.11), (0.40, 1.27)),
        5: ((0.30, 0.53), (0.24, 0.47)), 6: ((0.465, 0.75), (0.53, 0.66)), 7: ((0.61, 1.06), (0.56, 1.27)), 8: ((0.80, 0.70), (0.86, 0.60)),
        9: ((0.74, 0.86), (0.86, 0.92)), 10: ((0.98, 0.65), (1.30, 0.65)), 11: ((1.005, 0.85), (1.30, 0.85)),
        12: ((0.88, 1.11), (0.86, 1.27)), 13: ((1.03, 1.02), (1.10, 1.24)), 14: ((0.33, 0.37), (0.55, 0.33)), 15: ((1.12, 0.47), (1.30, 0.47))}
for n, ((pr, pz), (qr, qz)) in cpts.items():
    if (pr, pz) == (qr, qz):
        num(n, R_(qr), Zc(qz))
    else:
        num(n, R_(qr), Zc(qz), R_(pr), Zc(pz))
key(560, 640, ['Pivot ball dome (fixed)', 'Wear cup (turns)', 'Holder ring: bolts on top, lifts out upward', 'Foot plate, Ø0.55 m opening',
               'Keeper hook (pinned from above)', 'Slip ring: stator + rotor', 'Pin ring + pin wheel', 'Drive cartridge',
               'Copper strap to the radiator', 'Tub panel: CFRP + inner MLI', 'Radiator face (OSR, louvred)',
               'Rotating lid (dropped-tool shield)', 'Double labyrinth + brush ring', 'Debris drawer', 'Jack-frame post (outside)'], dy=19)
A(f'<text x="560" y="{640+15*19+8}" class="k" fill="#555">Red: thermostatic heaters (~90 W in all)</text>')
# labyrinth zoom under the section
zx, zy = 60, 965
A(f'<rect x="{zx}" y="{zy}" width="440" height="100" fill="#fff" stroke="#999" stroke-dasharray="3 3"/>')
A(f'<text x="{zx+8}" y="{zy+18}" font-size="11" font-weight="bold">Labyrinth at the tub top (x4)</text>')
ox, oz = zx + 300, zy + 22
A(f'<rect x="{ox-8}" y="{oz+26}" width="16" height="52" fill="{ENC}"/>')
A(f'<path d="M{ox-90} {oz} H{ox+60} V{oz+60} M{ox-28} {oz} V{oz+48}" fill="none" stroke="{ROT}" stroke-width="6"/>')
for xx in (ox - 14, ox + 14):
    A(f'<line x1="{xx}" y1="{oz+26}" x2="{xx}" y2="{oz+8}" stroke="#555" stroke-width="1" stroke-dasharray="1 2"/>')
A(f'<text x="{zx+8}" y="{zy+40}" font-size="11">Lid lips (orange) straddle the</text>')
A(f'<text x="{zx+8}" y="{zy+55}" font-size="11">tub top (green): ~10 mm gaps,</text>')
A(f'<text x="{zx+8}" y="{zy+70}" font-size="11">70 mm overlap, a bristle ring;</text>')
A(f'<text x="{zx+8}" y="{zy+85}" font-size="11">still closed at a 10 mm jack lift.</text>')

# ================= D. numbers and procedures =================
dx0, dy0 = 830, 680
A(f'<text x="{dx0}" y="{dy0-60}" class="t">D. Numbers and access</text>')
lines = ['Drive (base_drive_check.py)',
         '· 24,000:1; tracking steps 0.1° every ~12 min',
         '· slew ≤5°/min, 180° in 36 min, ~5 s ramps',
         '· mesh force 83–275 N running, 833 N design',
         '· limiter 37.5 N·m at the pin wheel = 300 N·m at the ring',
         '· both units always driven, with a torque bias',
         '',
         'Enclosure',
         '· tub Ø1.96 m x 0.62 m, 6 panels ~5 kg; lid 3 segments',
         '· slip ring ~0.45 kW → 1.9 m² radiators run ~2 °C',
         '· array dark: louvres shut, ~90 W heaters (base battery)',
         '',
         'Drive cartridge swap (~1 h; the other worm holds)',
         '1. Fire its mesh release; open its door (D)',
         '2. Undo 2 captive bolts, slide out on the dovetail',
         '3. Slide the spare in, re-engage, re-sync the pair',
         '',
         'Cup swap: unpin hooks, jack ~10 mm, lift the holder',
         'ring and cup up into the mast core; enclosure stays shut']
for j, t in enumerate(lines):
    bold = t and not t.startswith(('·', '1', '2', '3', 'ring')) and t != ''
    A(f'<text x="{dx0}" y="{dy0-36+j*17}" font-size="12"{" font-weight=\"bold\"" if bold else ""}>{t}</text>')
A('</svg>')
open('base-detail.svg', 'w').write('\n'.join(o))
