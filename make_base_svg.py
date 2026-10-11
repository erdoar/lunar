# Generates base.svg (rev 21): spherical base pivot (hard ball, wear cup with sensing layers), drive, foundation, base frame.
# Run: python3 make_base_svg.py
from math import sin, cos, radians

o = []
A = o.append
W, H = 1400, 900
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern>'
  '<pattern id="gr" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M0 0H6M0 0V6" stroke="#9aa" stroke-width="0.8"/></pattern>'
  '<pattern id="cm" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#e3d08e"/><circle cx="3" cy="3" r="0.6" fill="#8d7a45"/></pattern>'
  '<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker>'
  '<marker id="ad" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10z" fill="#8a5a2b"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:1.5}.l{stroke:#444;stroke-width:1;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}'
  '.n{font-size:11px;font-weight:bold}</style>')
ROT, FIX, DRV, SR, CU = '#e67e22', '#7d8790', '#7fa3d6', '#bfa6d9', '#b87333'
k, cx, gy = 300, 470, 790
X = lambda m: cx + m * k
Z = lambda m: gy - m * k
R, ZC = 0.25, 0.75          # ball radius and centre height (m); top of ball 1.0 m above regolith


def P(deg, r):              # point on a circle about the ball centre, deg from vertical (+ = right)
    return X(r * sin(radians(deg))), Z(ZC + r * cos(radians(deg)))


def arc(d1, d2, r):         # svg arc command from current point at d1 to d2 (both on radius r)
    x, y = P(d2, r)
    return f'A{r*k:.1f} {r*k:.1f} 0 0 {1 if d2 > d1 else 0} {x:.1f} {y:.1f}'


def call(n, px, py, qx, qy):   # numbered callout: part point (m) -> circle (m)
    if (px, py) != (qx, qy):
        A(f'<path d="M{X(px):.0f} {Z(py):.0f}L{X(qx):.0f} {Z(qy):.0f}" class="l"/><circle cx="{X(px):.0f}" cy="{Z(py):.0f}" r="2" fill="#222"/>')
    A(f'<circle cx="{X(qx):.0f}" cy="{Z(qy):.0f}" r="11" fill="#fff" stroke="#222"/>'
      f'<text x="{X(qx):.0f}" y="{Z(qy)+4:.0f}" text-anchor="middle" class="n" style="stroke:none">{n}</text>')


A('<text x="20" y="30" class="t">Section through the base pivot (rev 21): fixed parts grey, turning parts orange</text>')
A('<text x="20" y="50" fill="#555">Hard convex ball below, replaceable dry-lubricated wear cup above. Cup and gaps drawn thicker than true scale.</text>')
# ground, pad, ties
A(f'<rect x="{X(-1.45)}" y="{gy}" width="{2.9*k}" height="60" fill="url(#g)"/><line x1="{X(-1.45)}" y1="{gy}" x2="{X(1.45)}" y2="{gy}" stroke="#222"/>')
A(f'<rect x="{X(-1.0)}" y="{gy}" width="{2.0*k}" height="16" fill="#c9b79c" stroke="#222"/>')
# foundation frame (box truss)
A(f'<rect x="{X(-0.95)}" y="{Z(0.40)}" width="{1.9*k}" height="{0.40*k}" fill="none" stroke="{FIX}" stroke-width="5"/>')
for a_, b_ in ((-0.95, -0.45), (-0.45, 0.0), (0.0, 0.45), (0.45, 0.95)):
    A(f'<line x1="{X(a_)}" y1="{Z(0)}" x2="{X(b_)}" y2="{Z(0.40)}" stroke="{FIX}" stroke-width="3"/>')
A(f'<rect x="{X(-0.95)}" y="{Z(0.40)}" width="{1.9*k}" height="10" fill="{FIX}" class="s"/>')
for sx in (-1, 1):
    A(f'<circle cx="{X(sx*0.95)}" cy="{Z(0.06)}" r="7" fill="#fff" class="s"/>')
    A(f'<line x1="{X(sx*0.98)}" y1="{Z(0.06)}" x2="{X(sx*1.45)}" y2="{Z(0.06)}" stroke="#c87f0a" stroke-width="2" stroke-dasharray="6 3" marker-end="url(#ar)"/>')
# pedestal + conical drip flange (fixed)
A(f'<rect x="{X(-0.17)}" y="{Z(0.80)}" width="{0.34*k}" height="{0.40*k}" fill="{FIX}" class="s"/>')
A(f'<path d="M{X(-0.17)} {Z(0.63)} L{X(-0.31)} {Z(0.578)} V{Z(0.555)} H{X(0.31)} V{Z(0.578)} L{X(0.17)} {Z(0.63)} Z" fill="{FIX}" class="s"/>')
# pivot ball (fixed): sphere cap from -80 to +80 deg on its pedestal
x0, y0 = P(-80, R)
x1, y1 = P(80, R)
A(f'<path d="M{x0:.1f} {y0:.1f} {arc(-80, 80, R)} L{X(0.17):.1f} {Z(0.80):.1f} H{X(-0.17):.1f} Z" fill="#9fb3c8" class="s"/>')
A(f'<path d="M{P(-60,R*0.8)[0]:.1f} {P(-60,R*0.8)[1]:.1f} {arc(-60,-20,R*0.8)}" stroke="#fff" stroke-width="3" fill="none" opacity="0.7"/>')
# cup holder (turning): recess around the cup, up to the foot plate
RH = 0.262
hx0, hy0 = P(-42, RH)
hx1, hy1 = P(42, RH)
A(f'<path d="M{hx0:.1f} {hy0:.1f} V{Z(1.08):.1f} H{hx1:.1f} V{hy1:.1f} {arc(42, -42, RH)} Z" fill="{ROT}" opacity="0.9" class="s"/>')
# wear cup (turning), exaggerated thickness, with embedded conductive layers and a small apex relief
RC = 0.282
c0 = P(-35, R)
A(f'<path d="M{c0[0]:.1f} {c0[1]:.1f} {arc(-35, -5, R)} L{P(-5, R+0.008)[0]:.1f} {P(-5, R+0.008)[1]:.1f} {arc(-5, 5, R+0.008)} '
  f'L{P(5, R)[0]:.1f} {P(5, R)[1]:.1f} {arc(5, 35, R)} L{P(35, RC)[0]:.1f} {P(35, RC)[1]:.1f} {arc(35, -35, RC)} Z" fill="url(#cm)" class="s"/>')
for rl in (0.256, 0.262, 0.270):
    s0 = P(-33, rl)
    A(f'<path d="M{s0[0]:.1f} {s0[1]:.1f} {arc(-33, 33, rl)}" stroke="{CU}" stroke-width="1.6" fill="none"/>')
# foot plate + bottom mast section (turning)
A(f'<rect x="{X(-0.72)}" y="{Z(1.14)}" width="{1.44*k}" height="{0.06*k}" fill="{ROT}" class="s"/>')
for sx in (-1, 1):
    A(f'<line x1="{X(sx*0.68)}" y1="{Z(1.14)}" x2="{X(sx*0.68)}" y2="{Z(2.3)}" stroke="{ROT}" stroke-width="5"/>')
for z in (1.14, 1.72):
    A(f'<line x1="{X(-0.68)}" y1="{Z(z)}" x2="{X(0.68)}" y2="{Z(z+0.58)}" stroke="{ROT}" stroke-width="1.5"/>')
    A(f'<line x1="{X(0.68)}" y1="{Z(z)}" x2="{X(-0.68)}" y2="{Z(z+0.58)}" stroke="{ROT}" stroke-width="1.5"/>')
# keeper hook (right side; the section on the left passes through a gap between the 3 hooks)
A(f'<path d="M{X(0.36)} {Z(1.08)} V{Z(0.52)} H{X(0.26)} V{Z(0.545)} H{X(0.335)} V{Z(1.08)} Z" fill="{ROT}" class="s"/>')
A(f'<circle cx="{X(0.3475)}" cy="{Z(1.0)}" r="3" fill="#fff" stroke="#222"/>')
# annular slip ring: stator on posts (fixed), rotor under the foot plate (turning)
for sx in (-1, 1):
    a_, b_ = sorted((X(sx*0.43), X(sx*0.50)))
    A(f'<line x1="{(a_+b_)/2}" y1="{Z(0.40)}" x2="{(a_+b_)/2}" y2="{Z(0.80)}" stroke="{FIX}" stroke-width="5"/>')
    A(f'<rect x="{a_}" y="{Z(0.905)}" width="{b_-a_}" height="{0.105*k}" fill="{SR}" class="s"/>')
    A(f'<rect x="{a_}" y="{Z(1.08)}" width="{b_-a_}" height="{0.165*k}" fill="{SR}" stroke="{ROT}" stroke-width="2.5"/>')
    for d in (0.45, 0.48):
        A(f'<line x1="{X(sx*d)}" y1="{Z(0.905)}" x2="{X(sx*d)}" y2="{Z(0.915)}" stroke="#222" stroke-width="2"/>')
# pin-ring gear (turning) + worm gearmotors with slip clutch (fixed)
for sx in (-1, 1):
    a_, b_ = sorted((X(sx*0.555), X(sx*0.665)))
    A(f'<rect x="{a_}" y="{Z(1.08)}" width="{b_-a_}" height="{0.12*k}" fill="none" stroke="{ROT}" stroke-width="3"/>')
    A(f'<circle cx="{X(sx*0.61)}" cy="{Z(0.985)}" r="7" fill="#ddd" class="s"/>')
    A(f'<circle cx="{X(sx*0.61)}" cy="{Z(0.915)}" r="11" fill="{DRV}" class="s"/>')
    A(f'<path d="M{X(sx*0.61)-8} {Z(0.915)-4}H{X(sx*0.61)+8}M{X(sx*0.61)-8} {Z(0.915)+4}H{X(sx*0.61)+8}" stroke="#222"/>')
    A(f'<rect x="{X(sx*0.61)-10}" y="{Z(0.875)}" width="20" height="{0.465*k}" fill="{DRV}" class="s"/>')
    m0, m1 = sorted((X(sx*0.70), X(sx*0.93)))
    A(f'<rect x="{m0}" y="{Z(0.58)}" width="{m1-m0}" height="{0.17*k}" fill="{DRV}" class="s"/>')
    A(f'<rect x="{X(sx*0.675)-6}" y="{Z(0.54)}" width="12" height="{0.09*k}" fill="#f2c94c" class="s"/>')
    A(f'<text x="{(m0+m1)/2}" y="{Z(0.48)}" text-anchor="middle" font-size="11" style="stroke:none">motor</text>')
# debris path (left, through a gap between keeper hooks)
dp = P(-30, R)
A(f'<path d="M{dp[0]:.0f} {dp[1]-6:.0f} {arc(-30,-78,R+0.02)} L{X(-0.27)} {Z(0.61)} L{X(-0.33)} {Z(0.575)} L{X(-0.33)} {Z(0.43)}" '
  f'fill="none" stroke="#8a5a2b" stroke-width="1.5" stroke-dasharray="2 3" marker-end="url(#ad)"/>')
for (xx, zz) in ((-0.33, 0.47), (-0.335, 0.52), (-0.30, 0.596), (-0.31, 0.43)):
    A(f'<circle cx="{X(xx)}" cy="{Z(zz)}" r="2.2" fill="#8a5a2b"/>')
# rotating base frame at 1.5 m (shown cut), winch, readout, brush skirt
A(f'<rect x="{X(-1.35)}" y="{Z(1.53)}" width="{2.7*k}" height="9" fill="url(#gr)" stroke="{ROT}" stroke-width="2"/>')
for sx in (-1, 1):
    xb = X(sx*1.35)
    A(f'<path d="M{xb} {Z(1.53)-6} l{sx*6} 6 l{-sx*6} 6 l{sx*6} 6" fill="none" stroke="#222"/>')
    A(f'<line x1="{X(sx*0.68)}" y1="{Z(1.53)}" x2="{X(sx*1.0)}" y2="{Z(1.30)}" stroke="{ROT}" stroke-width="2"/>')
    A(f'<line x1="{X(sx*1.2)}" y1="{Z(1.50)}" x2="{X(sx*1.2)}" y2="{Z(0.15)}" stroke="#999" stroke-width="4" stroke-dasharray="3 2"/>')
A(f'<rect x="{X(0.80)}" y="{Z(1.72)}" width="{0.36*k}" height="{0.19*k}" fill="{DRV}" class="s"/><text x="{X(0.98)}" y="{Z(1.60)}" text-anchor="middle" font-size="11" style="stroke:none">winch</text>')
A(f'<rect x="{X(-1.16)}" y="{Z(1.70)}" width="{0.36*k}" height="{0.17*k}" fill="{SR}" class="s"/><text x="{X(-0.98)}" y="{Z(1.585)}" text-anchor="middle" font-size="10" style="stroke:none">readout</text>')
A(f'<path d="M{X(-0.98)} {Z(1.53)} V{Z(1.20)} H{X(-0.20)} V{Z(1.06)}" fill="none" stroke="{CU}" stroke-width="1.5" stroke-dasharray="4 2"/>')
# jack frame (fixed, stays bolted): posts + jack heads under the mast lugs
for sx in (-1, 1):
    A(f'<path d="M{X(sx*1.06)} {Z(0.40)} V{Z(2.05)} H{X(sx*0.68)}" fill="none" stroke="#2e7d32" stroke-width="3" stroke-dasharray="8 4"/>')
    A(f'<rect x="{min(X(sx*0.68), X(sx*0.78))}" y="{Z(2.0)}" width="{0.10*k}" height="{0.05*k}" fill="{ROT}" class="s"/>')
# halyards: winch -> side window sheave -> up the mast centre
A(f'<path d="M{X(0.86)} {Z(1.72)} L{X(0.68)} {Z(2.16)} L{X(0.02)} {Z(2.22)} V{Z(2.32)}" fill="none" stroke="#c0392b" stroke-width="2"/>')
A(f'<circle cx="{X(0.68)}" cy="{Z(2.16)}" r="6" fill="#fff" class="s"/>')
# callouts
call(1, 0.0, 0.86, 0.0, 0.86)
call(2, 0.16, 1.0, 0.24, 1.30)
call(3, -0.16, 1.05, -0.24, 1.30)
call(4, 0.0, 1.11, 0.0, 1.30)
call(5, 0.30, 0.53, 0.24, 0.47)
call(6, 0.0, 0.64, 0.0, 0.66)
call(7, 0.665, 1.03, 0.84, 1.15)
call(8, 0.93, 0.50, 1.38, 0.62)
call(9, 0.50, 1.00, 0.84, 0.86)
call(10, -0.70, 0.10, -1.33, 0.25)
call(11, -1.30, 1.53, -1.33, 1.85)
call(12, -1.20, 0.90, -1.38, 1.0)
call(13, -1.06, 1.20, -1.38, 1.40)
call(14, -0.33, 0.47, -1.38, 0.62)
call(15, 0.68, 2.16, 1.0, 2.25)
A(f'<text x="{X(0.37)}" y="{Z(0.53)+4}" font-size="10" fill="#555">5 mm</text>')
# ---- right column: wear-cup detail
ix, iy, iw = 930, 70, 310
A(f'<text x="{ix}" y="{iy}" class="t">Wear cup detail (about 30x)</text>')
s = 30                       # px per mm
yb = iy + 40                 # top of Ti backing
A(f'<rect x="{ix}" y="{yb}" width="{iw}" height="40" fill="{ROT}" opacity="0.9" class="s"/>')
A(f'<text x="{ix+8}" y="{yb+24}" style="stroke:none" fill="#fff" font-weight="bold">Ti backing, in the holder (turns)</text>')
y0 = yb + 40                 # top of composite liner
yr = y0 + 6 * s              # running surface (6 mm liner)
A(f'<rect x="{ix}" y="{y0}" width="{iw}" height="{6*s}" fill="url(#cm)" class="s"/>')
for j, (d, nm) in enumerate(((2.0, 'L4  2 mm'), (1.0, 'L3  1 mm'), (0.5, 'L2  0.5 mm'), (0.25, 'L1  0.25 mm'))):
    yy = yr - d * s
    for sec in range(3):
        xa = ix + 6 + sec * (iw - 12) / 3
        A(f'<line x1="{xa+4:.0f}" y1="{yy:.0f}" x2="{xa+(iw-12)/3-4:.0f}" y2="{yy:.0f}" stroke="{CU}" stroke-width="3"/>')
    ly = y0 + 70 + j * 26
    A(f'<path d="M{ix+iw-6} {yy:.0f}L{ix+iw+14} {ly}H{ix+iw+20}" class="l"/><text x="{ix+iw+24}" y="{ly+4}" font-size="12">{nm}</text>')
A(f'<text x="{ix+8}" y="{y0+18}" font-size="11">MoS₂/WS₂ metal-matrix composite, 6 mm</text>')
A(f'<text x="{ix+8}" y="{y0+34}" font-size="11">Insulated copper foil layers, 3 sectors each</text>')
A(f'<rect x="{ix}" y="{yr}" width="{iw}" height="34" fill="#9fb3c8" class="s"/>')
A(f'<text x="{ix+8}" y="{yr+22}" style="stroke:none">Hard ball surface (fixed, grounded)</text>')
A(f'<path d="M{ix+iw} {yr}H{ix+iw+20}" class="l"/><text x="{ix+iw+24}" y="{yr+4}" font-size="12" fill="#8a5a2b">running surface</text>')
A(f'<text x="{ix+iw+24}" y="{yr+20}" font-size="11" fill="#8a5a2b">10-yr wear ~0.001 mm</text>')
ty = yr + 58
for j, t in enumerate(['When wear reaches a layer it touches the ball: a metal ball shorts',
                       'it to ground; with a ceramic ball each layer is a loop that breaks.',
                       'Normal wear never reaches L1, so ANY trip flags an anomaly',
                       '(galling, contamination, overload). Sector differences show',
                       'uneven wear. Readout on the rotating base frame (11).']):
    A(f'<text x="{ix}" y="{ty+j*16}" font-size="12">{t}</text>')
# ---- right column: key and numbers
ky = ty + 100
A(f'<text x="{ix}" y="{ky}" class="t">Key</text>')
key = ['Pivot ball R 0.25 m, ~60 HRC steel + DLC or Si₃N₄ (fixed)',
       'Wear cup with sensing layers (turns); slides out on rails',
       'Cup holder + Ti backing, under the foot plate',
       'Mast foot plate: ~9.9 kN down',
       'Keeper hooks (3), pinned; ~5 mm under the flange',
       'Pedestal with conical drip flange',
       'Pin-ring (lantern) gear Ø1.2 m (turns)',
       'Worm gearmotors (2), self-locking; slip clutch ~300 N·m',
       'Annular slip ring Ø0.9 m: rotor turns, stator fixed',
       'Foundation frame, ~2 x 2 m pad, 3 ground-tie lugs',
       'Rotating base frame Ø3 m: winch, power, wear readout',
       'Brush skirt',
       'Jack frame: erection, then ~60 mm lift for a cup swap',
       'Debris falls off the ball, between the hooks',
       'Halyards enter via a side window and sheave']
for j, t in enumerate(key):
    yy = ky + 22 + j * 21
    A(f'<circle cx="{ix+10}" cy="{yy-4}" r="9" fill="#fff" stroke="#222"/><text x="{ix+10}" y="{yy}" text-anchor="middle" class="n" style="stroke:none">{j+1}</text>')
    A(f'<text x="{ix+26}" y="{yy}">{t}</text>')
ny = ky + 22 + len(key) * 21 + 12
A(f'<text x="{ix}" y="{ny}" font-weight="bold">Numbers (pivot_check.py)</text>')
for j, t in enumerate(['Contact ~630 cm², ~0.16 MPa; friction ~30 to 145 N·m',
                       'Running torque ~50 to 165 N·m (with collars)',
                       'Cup 45 mm deep; jack lift ~60 mm; ~1 shift to swap']):
    A(f'<text x="{ix}" y="{ny+18+j*16}">{t}</text>')
A('</svg>')
open('base.svg', 'w').write('\n'.join(o))
