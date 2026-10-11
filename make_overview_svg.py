# Generates overview.svg: the current design (rev 21 baseline) at a glance + base cutaway showing what attaches to what.
import math
o = []
A = o.append
W, H = 1240, 930
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern>'
  '<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:1.5}.l{stroke:#555;stroke-width:1;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:16px;font-weight:bold}</style>')
ROT, ROT2, FIX, FIX2 = '#e67e22', '#2c4a7a', '#7d8790', '#4a9'


def lab(x1, y1, x2, y2, lines, anchor='start', bold=False):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        w = ' font-weight="bold"' if (bold and j == 0) else ''
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*14:.0f}" text-anchor="{anchor}"{w}>{t}</text>')


# ================= LEFT: whole rig =================
A('<text x="20" y="30" class="t">Current design (rev 21 baseline): the whole rig</text>')
e, mid, gy = 6.2, 250, 790
X = lambda m: mid + m * e
Z = lambda m: gy - m * e
A(f'<rect x="20" y="{gy}" width="480" height="40" fill="url(#g)"/><line x1="20" y1="{gy}" x2="500" y2="{gy}" stroke="#222"/>')
# fixed bracing
for fx in (30, -15):
    A(f'<line x1="{X(fx)}" y1="{gy-2}" x2="{X(1.9*(1 if fx>0 else -0.5))}" y2="{Z(62)}" stroke="#8e44ad" stroke-width="1.4"/>')
    A(f'<line x1="{X(fx)}" y1="{gy-2}" x2="{X(4*(1 if fx>0 else -0.5))}" y2="{Z(35)}" stroke="{FIX}" stroke-width="4"/>')
    A(f'<line x1="{X(fx)}" y1="{gy-1}" x2="{X(0)}" y2="{gy-1}" stroke="#c87f0a" stroke-width="1.5" stroke-dasharray="6 3"/>')
    A(f'<rect x="{X(fx)-8}" y="{gy-6}" width="16" height="6" fill="{FIX}"/>')
for c in (35, 62):
    A(f'<rect x="{X(0)-10}" y="{Z(c)-4}" width="20" height="8" fill="{FIX2}" class="s"/>')
# rotating: mast, yard, wings, deck
A(f'<rect x="{X(0)-3}" y="{Z(108)}" width="6" height="{108*e-8}" fill="{ROT}"/>')
A(f'<rect x="{X(-17.5)}" y="{Z(100)-2}" width="{35*e}" height="5" fill="{ROT}" class="s"/>')
for sx in (-1, 1):
    A(f'<line x1="{X(0)}" y1="{Z(108)}" x2="{X(sx*17)}" y2="{Z(100)}" stroke="#555"/>')
    xl, xr = sorted((X(sx * 2), X(sx * 17)))
    A(f'<rect x="{xl}" y="{Z(100)+3}" width="{xr-xl}" height="{30*e-3}" fill="{ROT2}"/>')
A(f'<rect x="{X(-1.5)}" y="{gy-11}" width="{3*e}" height="3" fill="{ROT}"/>')
A(f'<rect x="{X(-1.2)}" y="{gy-6}" width="{2.4*e}" height="6" fill="{FIX}"/>')
for sx in (-1, 1):
    A(f'<rect x="{X(sx*9.5)-8*e}" y="{gy-10}" width="{15*e}" height="3" fill="#999"/>')
lab(X(17), Z(85), X(20), Z(88), ['Solar wings, 70–100 m', '(2 x 17 x 30 m, ~350 kW)'])
lab(X(-10), Z(100), X(-22), Z(104), ['Top yard, 100 m'], 'end')
lab(X(0), Z(107), X(8), Z(112), ['Mast, 108 m'])
lab(X(0) + 10, Z(62), X(14), Z(64), ['Upper collar 62 m + stay cables'])
lab(X(0) + 10, Z(35), X(14), Z(38), ['Strut collar 35 m + A-frame struts'])
lab(X(30), gy - 4, X(31), gy - 110, ["Foot pad, 30 m out"])
lab(X(0.8), gy - 8, X(10), gy - 70, ['Single base pivot +', 'rotating base frame (see right)'])
A(f'<text x="30" y="{gy+58}" font-size="12">Turns (once per lunar day): <tspan fill="{ROT}" font-weight="bold">orange</tspan> + <tspan fill="{ROT2}" font-weight="bold">blue</tspan>.  Fixed: <tspan fill="{FIX}" font-weight="bold">grey</tspan>, <tspan fill="{FIX2}" font-weight="bold">green</tspan> collars, purple cables.</text>')

# ================= RIGHT: base cutaway =================
from math import sin, cos, radians
x0 = 620
k, cx, gy2 = 190, 860, 540
BX = lambda m: cx + m * k
BZ = lambda m: gy2 - m * k
R, ZC = 0.25, 0.75


def BP(deg, r):
    return BX(r * sin(radians(deg))), BZ(ZC + r * cos(radians(deg)))


def barc(d1, d2, r):
    x, y = BP(d2, r)
    return f'A{r*k:.1f} {r*k:.1f} 0 0 {1 if d2 > d1 else 0} {x:.1f} {y:.1f}'


A(f'<text x="{x0-60}" y="30" class="t">Base close-up: what attaches to what</text>')
A(f'<text x="{x0-60}" y="48" font-size="11.5">Section through the mast foot (full detail in base.svg)</text>')
A(f'<rect x="{BX(-1.6)}" y="{gy2}" width="{3.2*k}" height="30" fill="url(#g)"/><line x1="{BX(-1.6)}" y1="{gy2}" x2="{BX(1.6)}" y2="{gy2}" stroke="#222"/>')
A(f'<rect x="{BX(-0.95)}" y="{BZ(0.40)}" width="{1.9*k}" height="{0.40*k}" fill="{FIX}" opacity="0.85" class="s"/>')
A(f'<rect x="{BX(-0.17)}" y="{BZ(0.80)}" width="{0.34*k}" height="{0.40*k}" fill="{FIX}" class="s"/>')
A(f'<path d="M{BX(-0.17)} {BZ(0.63)} L{BX(-0.31)} {BZ(0.578)} V{BZ(0.555)} H{BX(0.31)} V{BZ(0.578)} L{BX(0.17)} {BZ(0.63)} Z" fill="{FIX}" class="s"/>')
p0 = BP(-80, R)
A(f'<path d="M{p0[0]:.1f} {p0[1]:.1f} {barc(-80, 80, R)} L{BX(0.17):.1f} {BZ(0.80):.1f} H{BX(-0.17):.1f} Z" fill="#9fb3c8" class="s"/>')
h0 = BP(-42, 0.262)
h1 = BP(42, 0.262)
A(f'<path d="M{h0[0]:.1f} {h0[1]:.1f} V{BZ(1.08):.1f} H{h1[0]:.1f} V{h1[1]:.1f} {barc(42, -42, 0.262)} Z" fill="{ROT}" class="s"/>')
c0 = BP(-35, R)
c1 = BP(35, 0.285)
A(f'<path d="M{c0[0]:.1f} {c0[1]:.1f} {barc(-35, 35, R)} L{c1[0]:.1f} {c1[1]:.1f} {barc(35, -35, 0.285)} Z" fill="#e3d08e" class="s"/>')
for rl in (0.258, 0.268):
    q = BP(-32, rl)
    A(f'<path d="M{q[0]:.1f} {q[1]:.1f} {barc(-32, 32, rl)}" stroke="#b87333" stroke-width="1.5" fill="none"/>')
A(f'<path d="M{BX(0.36)} {BZ(1.08)} V{BZ(0.52)} H{BX(0.26)} V{BZ(0.545)} H{BX(0.335)} V{BZ(1.08)} Z" fill="{ROT}" class="s"/>')
for sx in (-1, 1):
    a_, b_ = sorted((BX(sx*0.43), BX(sx*0.50)))
    A(f'<line x1="{(a_+b_)/2}" y1="{BZ(0.40)}" x2="{(a_+b_)/2}" y2="{BZ(0.80)}" stroke="{FIX}" stroke-width="4"/>')
    A(f'<rect x="{a_}" y="{BZ(0.905)}" width="{b_-a_}" height="{0.105*k}" fill="#bfa6d9" class="s"/>')
    A(f'<rect x="{a_}" y="{BZ(1.08)}" width="{b_-a_}" height="{0.165*k}" fill="#bfa6d9" stroke="{ROT}" stroke-width="2"/>')
    a_, b_ = sorted((BX(sx*0.555), BX(sx*0.665)))
    A(f'<rect x="{a_}" y="{BZ(1.08)}" width="{b_-a_}" height="{0.12*k}" fill="none" stroke="{ROT}" stroke-width="2.5"/>')
    A(f'<circle cx="{BX(sx*0.61)}" cy="{BZ(0.915)}" r="8" fill="#7fa3d6" class="s"/>')
    A(f'<rect x="{BX(sx*0.61)-7}" y="{BZ(0.875)}" width="14" height="{0.465*k}" fill="#7fa3d6" class="s"/>')
    m0, m1 = sorted((BX(sx*0.70), BX(sx*0.93)))
    A(f'<rect x="{m0}" y="{BZ(0.58)}" width="{m1-m0}" height="{0.17*k}" fill="#7fa3d6" class="s"/>')
    A(f'<line x1="{BX(sx*0.95)}" y1="{BZ(0.06)}" x2="{BX(sx*1.6)}" y2="{BZ(0.06)}" stroke="#c87f0a" stroke-width="2" stroke-dasharray="6 3"/>')
    A(f'<line x1="{BX(sx*0.68)}" y1="{BZ(1.14)}" x2="{BX(sx*0.68)}" y2="{BZ(2.2)}" stroke="{ROT}" stroke-width="4"/>')
    A(f'<path d="M{BX(sx*1.06)} {BZ(0.40)} V{BZ(2.0)} H{BX(sx*0.68)}" fill="none" stroke="#2e7d32" stroke-width="2" stroke-dasharray="7 4"/>')
A(f'<rect x="{BX(-0.72)}" y="{BZ(1.14)}" width="{1.44*k}" height="{0.06*k}" fill="{ROT}" class="s"/>')
A(f'<rect x="{BX(-1.4)}" y="{BZ(1.53)}" width="{2.8*k}" height="7" fill="{ROT}" opacity="0.7"/>')
A(f'<rect x="{BX(0.80)}" y="{BZ(1.72)}" width="{0.36*k}" height="{0.19*k}" fill="#7fa3d6" class="s"/>')
A(f'<path d="M{BP(-38, R+0.02)[0]:.0f} {BP(-38, R+0.02)[1]:.0f} {barc(-38, -78, R+0.02)} L{BX(-0.27)} {BZ(0.61)} L{BX(-0.33)} {BZ(0.575)} V{BZ(0.43)}" fill="none" stroke="#8a5a2b" stroke-width="1.5" stroke-dasharray="2 3"/>')


def call(n, x, y, dx, dy):
    A(f'<path d="M{x:.0f} {y:.0f}L{x+dx:.0f} {y+dy:.0f}" class="l"/><circle cx="{x+dx:.0f}" cy="{y+dy:.0f}" r="10" fill="#fff" stroke="#222"/>'
      f'<text x="{x+dx:.0f}" y="{y+dy+4:.0f}" text-anchor="middle" font-size="11" font-weight="bold" style="stroke:none">{n}</text>')


for n, (px, pz, cy) in {1: (0.2, 1.11, 250), 2: (0.12, 1.01, 285), 6: (0.665, 1.03, 320), 3: (0.05, 0.88, 365),
                        4: (0.30, 0.53, 410), 5: (0.93, 0.50, 455)}.items():
    call(n, BX(px), BZ(pz), BX(1.55) - BX(px), cy - BZ(pz))
call(7, BX(-0.50), BZ(1.0), -170, -40)
call(8, BX(-1.2), BZ(1.53), -40, -50)
call(9, BX(-0.95), BZ(0.06), -110, 30)
call(10, BX(-1.06), BZ(1.1), -60, 40)
items = [
    ('Mast → cup', 'The mast foot plate (where the 3 legs meet) holds the concave wear cup, facing down.'),
    ('Wear cup', 'Dry-lubricated, replaceable; conductive layers inside read wear depth electrically.'),
    ('Pivot ball', 'Hard convex ball R 0.25 m, fixed, facing up: carries ~9.9 kN; dust and debris fall off it.'),
    ('Ball → foundation', 'Pedestal with drip flange on the foundation frame (~2 x 2 m pad); 3 keeper hooks.'),
    ('Drive', '2 self-locking worm motors (slip clutch ~300 N·m) on the frame drive a pin-ring gear.'),
    ('Pin-ring gear', 'Ø1.2 m lantern gear under the foot plate; tolerates dust and the ±1° pivot tilt.'),
    ('Slip ring', 'Annular, Ø0.9 m, around the pivot: rotor under the foot plate, stator on the frame.'),
    ('Base frame → mast', 'The Ø3 m rotating base frame clamps to the bottom mast section ~1.5 m up (battery, bot dock, power).'),
    ('Ties → foundation', 'The 3 ground ties from the strut feet end on lugs on the foundation frame and cancel out.'),
    ('Jack frame', 'Bolted to the foundation frame: erection, then lifts the mast ~60 mm for a cup swap.'),
]
ly = 600
for i, (a_, b_) in enumerate(items):
    y = ly + i * 31
    A(f'<circle cx="{x0-48}" cy="{y-4}" r="9" fill="#fff" stroke="#222"/><text x="{x0-48}" y="{y}" text-anchor="middle" font-size="10.5" font-weight="bold" style="stroke:none">{i+1}</text>')
    A(f'<text x="{x0-34}" y="{y}" font-weight="bold">{a_}</text><text x="{x0-34}" y="{y+14}" font-size="11.5">{b_}</text>')
A(f'<text x="{x0-60}" y="78" font-size="12"><tspan fill="{ROT}" font-weight="bold">Turns:</tspan> mast, foot plate, wear cup, pin ring, base frame.   <tspan fill="{FIX}" font-weight="bold">Fixed:</tspan> ball, foundation, drives, ties.</text>')
A(f'<text x="{x0-60}" y="96" font-size="12">Weight path: mast → foot plate → wear cup → pivot ball → foundation frame → pad → regolith.</text>')
A('</svg>')
open('overview.svg', 'w').write('\n'.join(o))
