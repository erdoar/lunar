# Generates overview.svg: the current design (rev 19 baseline) at a glance + base cutaway showing what attaches to what.
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
A('<text x="20" y="30" class="t">Current design (rev 19 baseline): the whole rig</text>')
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
A(f'<rect x="{X(-6)}" y="{gy-9}" width="{12*e}" height="6" fill="{ROT}" class="s"/>')
A(f'<rect x="{X(-6)-3}" y="{gy-3}" width="{12*e+6}" height="3" fill="{FIX}"/>')
lab(X(-17), Z(85), X(-22), Z(90), ['Solar wings, 70–100 m', '(2 x 17 x 30 m, ~350 kW)'], 'end')
lab(X(-10), Z(100), X(-22), Z(104), ['Top yard, 100 m'], 'end')
lab(X(0), Z(107), X(8), Z(112), ['Mast, 108 m'])
lab(X(0) + 10, Z(62), X(14), Z(64), ['Upper collar 62 m + stay cables'])
lab(X(0) + 10, Z(35), X(14), Z(38), ['Strut collar 35 m + A-frame struts'])
lab(X(30), gy - 4, X(31), gy - 110, ["Foot pad, 30 m out"])
lab(X(6), gy - 6, X(12), gy - 70, ['Deck + bogies on the', 'Ø12 m rail (see right)'])
A(f'<text x="30" y="{gy+58}" font-size="12">Turns (once per lunar day): <tspan fill="{ROT}" font-weight="bold">orange</tspan> + <tspan fill="{ROT2}" font-weight="bold">blue</tspan>.  Fixed: <tspan fill="{FIX}" font-weight="bold">grey</tspan>, <tspan fill="{FIX2}" font-weight="bold">green</tspan> collars, purple cables.</text>')

# ================= RIGHT: base cutaway =================
x0, gy2 = 620, 560
kx, kz = 95, 190                         # px per metre: horizontal, vertical (x2)
BX = lambda r: x0 + r * kx               # r = radius from the mast centre
BZ = lambda z: gy2 - z * kz
A(f'<text x="{x0-60}" y="30" class="t">Base close-up: what attaches to what</text>')
A(f'<text x="{x0-60}" y="48" font-size="11.5">Radial section through one bogie, mast centre on the left (vertical scale x2)</text>')
A(f'<rect x="{x0-60}" y="{gy2}" width="{8*kx}" height="50" fill="url(#g)"/><line x1="{x0-60}" y1="{gy2}" x2="{x0+7.4*kx}" y2="{gy2}" stroke="#222"/>')
# kingpin foundation + kingpin (fixed)
A(f'<rect x="{BX(-0.5)}" y="{BZ(0.05)}" width="{1.0*kx}" height="{0.25*kz}" fill="{FIX}" class="s"/>')
A(f'<rect x="{BX(-0.15)}" y="{BZ(0.6)}" width="{0.3*kx}" height="{0.55*kz}" fill="{FIX}" class="s"/>')
# hub (rotating) with slewing ring around the kingpin top
A(f'<rect x="{BX(-0.8)}" y="{BZ(1.5)}" width="{1.6*kx}" height="{1.0*kz}" fill="#f6c9a0" class="s"/>')
A(f'<rect x="{BX(-0.3)}" y="{BZ(0.62)}" width="{0.6*kx}" height="{0.12*kz}" fill="{FIX2}" class="s"/>')
# mast foot + mast stub
A(f'<path d="M{BX(-0.25)} {BZ(1.5)} A{0.25*kx} {0.08*kz} 0 0 1 {BX(0.25)} {BZ(1.5)}" fill="{ROT}" class="s"/>')
A(f'<rect x="{BX(-0.7)}" y="{BZ(2.2)}" width="{1.4*kx}" height="{0.65*kz}" fill="none" stroke="{ROT}" stroke-width="4"/>')
# main spoke (rotating): top chord at 1.5, bottom from 0.5 at hub to 1.1 at the ring
A(f'<line x1="{BX(0.8)}" y1="{BZ(1.5)}" x2="{BX(5.85)}" y2="{BZ(1.5)}" stroke="{ROT}" stroke-width="5"/>')
A(f'<line x1="{BX(0.8)}" y1="{BZ(0.5)}" x2="{BX(5.85)}" y2="{BZ(1.1)}" stroke="{ROT}" stroke-width="5"/>')
for i in range(6):
    ra = 0.8 + i * 0.84
    zb = lambda r: 0.5 + 0.6 * (r - 0.8) / 5.05
    A(f'<line x1="{BX(ra)}" y1="{BZ(1.5)}" x2="{BX(ra+0.42)}" y2="{BZ(zb(ra+0.42))}" stroke="{ROT}" stroke-width="2"/>')
    A(f'<line x1="{BX(ra+0.42)}" y1="{BZ(zb(ra+0.42))}" x2="{BX(ra+0.84)}" y2="{BZ(1.5)}" stroke="{ROT}" stroke-width="2"/>')
# ring girder (rotating) over the rail
A(f'<rect x="{BX(5.8)}" y="{BZ(1.55)}" width="{0.4*kx}" height="{0.35*kz}" fill="{ROT}" class="s"/>')
# dust skirt
A(f'<line x1="{BX(6.25)}" y1="{BZ(1.4)}" x2="{BX(6.25)}" y2="{BZ(0.82)}" stroke="#999" stroke-width="3" stroke-dasharray="3 2"/>')
# bogie pivot + bogie frame + tyre (rotating)
A(f'<circle cx="{BX(6)}" cy="{BZ(1.13)}" r="8" fill="#fff" class="s"/>')
A(f'<rect x="{BX(5.55)}" y="{BZ(1.08)}" width="{0.9*kx}" height="{0.13*kz}" fill="#e0a040" class="s"/>')
A(f'<circle cx="{BX(6)}" cy="{BZ(0.93)}" r="{0.15*kz*0.6}" fill="#bbb" class="s"/><circle cx="{BX(6)}" cy="{BZ(0.93)}" r="3" fill="#222"/>')
A(f'<line x1="{BX(5.62)}" y1="{BZ(0.95)}" x2="{BX(5.62)}" y2="{BZ(0.62)}" stroke="#555" stroke-width="3"/><circle cx="{BX(5.7)}" cy="{BZ(0.62)}" r="5" fill="{FIX2}" class="s"/>')
# rail + pier (fixed)
A(f'<rect x="{BX(5.75)}" y="{BZ(0.8)}" width="{0.5*kx}" height="{0.05*kz}" fill="#c0392b"/>')
A(f'<rect x="{BX(5.8)}" y="{BZ(0.75)}" width="{0.4*kx}" height="{0.25*kz}" fill="{FIX}" class="s"/>')
A(f'<rect x="{BX(5.9)}" y="{BZ(0.5)}" width="{0.2*kx}" height="{0.45*kz}" fill="#ccc" class="s"/>')
A(f'<rect x="{BX(5.7)}" y="{BZ(0.05)}" width="{0.6*kx}" height="{0.05*kz}" fill="#999"/>')
# tie cable at ground level to the strut foot (fixed)
A(f'<line x1="{BX(0.5)}" y1="{BZ(0.05)}" x2="{BX(7.3)}" y2="{BZ(0.05)}" stroke="#c87f0a" stroke-width="2" stroke-dasharray="6 3" marker-end="url(#ar)"/>')
A(f'<text x="{BX(6.6)}" y="{BZ(0.05)+18}" font-size="11">tie → strut foot, 30 m</text>')

# numbered attachments
def call(n, x, y, dx, dy):
    A(f'<path d="M{x:.0f} {y:.0f}L{x+dx:.0f} {y+dy:.0f}" class="l"/><circle cx="{x+dx:.0f}" cy="{y+dy:.0f}" r="10" fill="#fff" stroke="#222"/>'
      f'<text x="{x+dx:.0f}" y="{y+dy+4:.0f}" text-anchor="middle" font-size="11" font-weight="bold" style="stroke:none">{n}</text>')

call(1, BX(6.25), BZ(0.78), 40, 30)        # tyre on rail
call(2, BX(5.7), BZ(0.62), -30, 40)        # uplift roller
call(3, BX(6), BZ(1.13), 45, -10)          # bogie pivot -> ring girder
call(4, BX(5.85), BZ(1.4), -10, -60)       # spoke -> ring girder
call(5, BX(0.8), BZ(1.0), 30, -70)         # spoke -> hub
call(6, BX(0), BZ(1.52), -40, -40)         # mast foot on hub
call(7, BX(0.3), BZ(0.66), 40, 30)         # hub slewing ring on kingpin
call(8, BX(6), BZ(0.5), 40, 20)            # rail on pier
call(9, BX(0), BZ(0.05), -45, 30)          # kingpin foundation + ties
items = [
    ('Tyres → rail head', 'The 2 tyres of each bogie roll on the rail\'s wear strip (red).'),
    ('Uplift rollers → under the rail head', 'Captive hooks against quake bounce; normally unloaded.'),
    ('Bogie → ring girder', 'Spherical pivot on top of the bogie bolts under the ring girder, exactly where a main spoke meets it.'),
    ('Spokes → ring girder', 'All 12 spokes bolt to the ring girder at their outer ends (main spokes over the 3 bogies).'),
    ('Spokes → hub', 'Inner ends bolt to the hub\'s upper and lower rings (moment joints).'),
    ('Mast → hub', 'The mast foot sits on a spherical seat on top of the hub.'),
    ('Hub → kingpin', 'A slewing ring on the hub underside fits round the fixed kingpin: centring only, no weight.'),
    ('Rail → piers → ground', 'The fixed rail (12 segments) sits on 12 levelling piers on sintered pads.'),
    ('Kingpin foundation ← ties', 'The 3 ground ties from the strut feet end here and cancel out.'),
]
ly = 640
for i, (a, b) in enumerate(items):
    y = ly + i * 30
    A(f'<circle cx="{x0-48}" cy="{y-4}" r="9" fill="#fff" stroke="#222"/><text x="{x0-48}" y="{y}" text-anchor="middle" font-size="10.5" font-weight="bold" style="stroke:none">{i+1}</text>')
    A(f'<text x="{x0-34}" y="{y}" font-weight="bold">{a}</text><text x="{x0-34}" y="{y+14}" font-size="11.5">{b}</text>')
A(f'<text x="{x0-60}" y="90" font-size="12"><tspan fill="{ROT}" font-weight="bold">Turns:</tspan> mast, hub, spokes, ring girder, bogies.   <tspan fill="{FIX}" font-weight="bold">Fixed:</tspan> rail, piers, kingpin, ties.</text>')
A(f'<text x="{x0-60}" y="108" font-size="12">Weight path: mast → hub → 3 main spokes → ring girder → 3 bogie pivots → 6 tyres → rail → piers → ground.</text>')
A('</svg>')
open('overview.svg', 'w').write('\n'.join(o))
