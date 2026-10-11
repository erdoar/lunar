# Generates overview.svg: the current design (rev 20 baseline) at a glance + base cutaway showing what attaches to what.
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
A('<text x="20" y="30" class="t">Current design (rev 20 baseline): the whole rig</text>')
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
lab(X(-17), Z(85), X(-22), Z(90), ['Solar wings, 70–100 m', '(2 x 17 x 30 m, ~350 kW)'], 'end')
lab(X(-10), Z(100), X(-22), Z(104), ['Top yard, 100 m'], 'end')
lab(X(0), Z(107), X(8), Z(112), ['Mast, 108 m'])
lab(X(0) + 10, Z(62), X(14), Z(64), ['Upper collar 62 m + stay cables'])
lab(X(0) + 10, Z(35), X(14), Z(38), ['Strut collar 35 m + A-frame struts'])
lab(X(30), gy - 4, X(31), gy - 110, ["Foot pad, 30 m out"])
lab(X(0.8), gy - 8, X(10), gy - 70, ['Single base bearing +', 'rotating base frame (see right)'])
A(f'<text x="30" y="{gy+58}" font-size="12">Turns (once per lunar day): <tspan fill="{ROT}" font-weight="bold">orange</tspan> + <tspan fill="{ROT2}" font-weight="bold">blue</tspan>.  Fixed: <tspan fill="{FIX}" font-weight="bold">grey</tspan>, <tspan fill="{FIX2}" font-weight="bold">green</tspan> collars, purple cables.</text>')

# ================= RIGHT: base cutaway =================
x0 = 620
k, cx, gy2 = 150, 860, 520
BX = lambda m: cx + m * k
BZ = lambda m: gy2 - m * k
A(f'<text x="{x0-60}" y="30" class="t">Base close-up: what attaches to what</text>')
A(f'<text x="{x0-60}" y="48" font-size="11.5">Section through the mast foot (full detail in base.svg)</text>')
A(f'<rect x="{BX(-2)}" y="{gy2}" width="{4*k}" height="40" fill="url(#g)"/><line x1="{BX(-2)}" y1="{gy2}" x2="{BX(2)}" y2="{gy2}" stroke="#222"/>')
A(f'<path d="M{BX(-1)} {BZ(0)} L{BX(-0.45)} {BZ(0.55)} H{BX(0.45)} L{BX(1)} {BZ(0)} Z" fill="{FIX}" class="s"/>')
A(f'<path d="M{BX(-0.42)} {BZ(0.55)} A{0.6*k} {0.25*k} 0 0 0 {BX(0.42)} {BZ(0.55)}" fill="#bbb" class="s"/>')
A(f'<rect x="{BX(-0.42)}" y="{BZ(0.95)}" width="{0.84*k}" height="{0.4*k}" fill="{FIX}" class="s"/>')
A(f'<rect x="{BX(-0.33)}" y="{BZ(0.8)}" width="{0.66*k}" height="{0.08*k}" fill="{ROT}" stroke="#222"/>')
A(f'<rect x="{BX(-0.07)}" y="{BZ(1.2)}" width="{0.14*k}" height="{0.75*k}" fill="#bfa6d9" class="s"/>')
for sx in (-1, 1):
    A(f'<rect x="{BX(sx*0.75)-22}" y="{BZ(0.95)}" width="44" height="34" fill="#7fa3d6" class="s"/>')
    A(f'<line x1="{BX(sx*0.9)}" y1="{BZ(0.06)}" x2="{BX(sx*2)}" y2="{BZ(0.06)}" stroke="#c87f0a" stroke-width="2" stroke-dasharray="6 3"/>')
A(f'<rect x="{BX(-0.45)}" y="{BZ(1.02)}" width="{0.9*k}" height="{0.07*k}" fill="{ROT}" class="s"/>')
A(f'<rect x="{BX(-0.7)}" y="{BZ(2.6)}" width="{1.4*k}" height="{1.5*k}" fill="none" stroke="{ROT}" stroke-width="4"/>')
A(f'<rect x="{BX(-1.5)}" y="{BZ(1.5)}" width="{3*k}" height="8" fill="{ROT}" opacity="0.7"/>')
A(f'<rect x="{BX(0.8)}" y="{BZ(1.5)-36}" width="60" height="36" fill="#7fa3d6" class="s"/>')
A(f'<rect x="{BX(-1.25)}" y="{BZ(2.3)}" width="{2.5*k}" height="{1.75*k}" fill="none" stroke="#2e7d32" stroke-width="2" stroke-dasharray="7 4"/>')


def call(n, x, y, dx, dy):
    A(f'<path d="M{x:.0f} {y:.0f}L{x+dx:.0f} {y+dy:.0f}" class="l"/><circle cx="{x+dx:.0f}" cy="{y+dy:.0f}" r="10" fill="#fff" stroke="#222"/>'
      f'<text x="{x+dx:.0f}" y="{y+dy+4:.0f}" text-anchor="middle" font-size="11" font-weight="bold" style="stroke:none">{n}</text>')


call(1, BX(0.3), BZ(1.05), 160, -30)
call(2, BX(0.33), BZ(0.78), 175, 25)
call(3, BX(0.3), BZ(0.5), 170, 40)
call(4, BX(0.75), BZ(0.9), 110, -45)
call(5, BX(1.2), BZ(1.48), 60, -30)
call(6, BX(0), BZ(1.15), -170, -40)
call(7, BX(-0.9), BZ(0.06), -110, 40)
call(8, BX(-1.25), BZ(1.9), -60, -20)
items = [
    ('Mast → bearing', 'The mast foot plate (where the 3 legs meet) bolts to the turning race of the base bearing.'),
    ('Base bearing', 'Ø0.6 m crossed-roller slewing ring in a swappable cartridge; carries ~9.9 kN.'),
    ('Bearing → foundation', 'The cartridge sits on a spherical seat (±1°) in the foundation frame on a ~2 x 2 m pad.'),
    ('Drive → bearing', '2 self-locking worm motors on the foundation frame drive the ring\'s internal gear.'),
    ('Base frame → mast', 'The Ø3 m rotating base frame clamps to the bottom mast section ~1.5 m up (winch, power).'),
    ('Slip ring', 'Through the bearing\'s hollow centre: rotor on the mast side, stator in the foundation.'),
    ('Ties → foundation', 'The 3 ground ties from the strut feet end on lugs on the foundation frame and cancel out.'),
    ('Jack frame', 'Bolted to the foundation frame: used for erection, then left for bearing swaps.'),
]
ly = 600
for i, (a_, b_) in enumerate(items):
    y = ly + i * 32
    A(f'<circle cx="{x0-48}" cy="{y-4}" r="9" fill="#fff" stroke="#222"/><text x="{x0-48}" y="{y}" text-anchor="middle" font-size="10.5" font-weight="bold" style="stroke:none">{i+1}</text>')
    A(f'<text x="{x0-34}" y="{y}" font-weight="bold">{a_}</text><text x="{x0-34}" y="{y+14}" font-size="11.5">{b_}</text>')
A(f'<text x="{x0-60}" y="78" font-size="12"><tspan fill="{ROT}" font-weight="bold">Turns:</tspan> mast, bearing inner race, base frame.   <tspan fill="{FIX}" font-weight="bold">Fixed:</tspan> foundation, seat, bearing housing, drives, ties.</text>')
A(f'<text x="{x0-60}" y="96" font-size="12">Weight path: mast → foot plate → base bearing → spherical seat → foundation frame → pad → regolith.</text>')
A('</svg>')
open('overview.svg', 'w').write('\n'.join(o))
