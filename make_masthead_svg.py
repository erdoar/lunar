# Generates masthead.svg (rev 33): masthead elevation, crown plan + lift tang, yard tip end view, lift profile/plan, rod bundle and numbers.
# Run: python3 make_masthead_svg.py
from math import radians, sin, cos, tan, pi

o = []
A = o.append
W, H = 1300, 1000
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker>'
  '<pattern id="gr" width="5" height="5" patternUnits="userSpaceOnUse"><path d="M0 0H5M0 0V5" stroke="#888" stroke-width="0.7"/></pattern>'
  '<pattern id="hz" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M0 6L6 0" stroke="#e6b0aa" stroke-width="1.2"/></pattern></defs>')
A('<style>.s{stroke:#222;stroke-width:1.2}.l{stroke:#555;stroke-width:1;fill:none}.rod{stroke:#7f8c8d;stroke-width:2.2;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}.n{font-size:11px;font-weight:bold}</style>')
YD, YDS, TI, BOT, BUS, ROD, MAST = '#e0a040', '#8a5a00', '#9fb3c8', '#6c3483', '#2e86c1', '#7f8c8d', '#888'
ANG = 23.4
TA = tan(radians(ANG))


def lab(x1, y1, x2, y2, lines, anchor='start', fs=11.5):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*14:.0f}" text-anchor="{anchor}" font-size="{fs}">{t}</text>')


def call(n, x, y, tx, ty):
    A(f'<path d="M{x:.0f} {y:.0f}L{tx:.0f} {ty:.0f}" class="l"/>')
    A(f'<circle cx="{tx:.0f}" cy="{ty:.0f}" r="9" fill="#fff" stroke="#222"/><text x="{tx:.0f}" y="{ty+4:.0f}" text-anchor="middle" class="n" style="stroke:none">{n}</text>')


def key(x, y, items, dy=17):
    for j, (n, t) in enumerate(items):
        A(f'<circle cx="{x+9}" cy="{y+j*dy}" r="8" fill="#fff" stroke="#222"/><text x="{x+9}" y="{y+j*dy+4}" text-anchor="middle" class="n" style="stroke:none">{n}</text>')
        A(f'<text x="{x+24}" y="{y+j*dy+4}" font-size="11.5">{t}</text>')


def bot(x, y, h):
    """Humanoid icon standing, feet at (x, y), h px tall."""
    u = h / 26
    A(f'<g stroke="{BOT}" stroke-width="{2.4*u:.1f}" stroke-linecap="round" fill="none">'
      f'<line x1="{x}" y1="{y-8*u}" x2="{x-4*u}" y2="{y}"/><line x1="{x}" y1="{y-8*u}" x2="{x+4*u}" y2="{y}"/>'
      f'<line x1="{x}" y1="{y-8*u}" x2="{x}" y2="{y-19*u}"/><line x1="{x}" y1="{y-17*u}" x2="{x-6*u}" y2="{y-10*u}"/>'
      f'<line x1="{x}" y1="{y-17*u}" x2="{x+6*u}" y2="{y-24*u}"/></g><circle cx="{x}" cy="{y-22.5*u}" r="{3.4*u:.1f}" fill="{BOT}"/>')


# ================= 1. Masthead elevation (wing plane) =================
A('<text x="20" y="30" class="t">1. Masthead, wing-plane elevation</text>')
k1, c1 = 50, 235
X1 = lambda x: c1 + x * k1
Z1 = lambda z: 615 - (z - 99) * k1
# mast lattice 99..108
A(f'<rect x="{X1(-0.7)}" y="{Z1(108)}" width="{1.4*k1}" height="{9*k1}" fill="#f7f7f7" stroke="{MAST}" stroke-width="2.4"/>')
z = 99.0
while z < 108:
    A(f'<path d="M{X1(-0.7)} {Z1(z)} L{X1(0.7)} {Z1(z+0.75)} M{X1(0.7)} {Z1(z)} L{X1(-0.7)} {Z1(z+0.75)}" stroke="#ccc"/>')
    z += 0.75
A(f'<line x1="{X1(0)}" y1="{Z1(99)}" x2="{X1(0)}" y2="{Z1(108)}" stroke="{MAST}" stroke-width="1.6"/>')
for zj in (102, 105):
    A(f'<line x1="{X1(-0.78)}" y1="{Z1(zj)}" x2="{X1(0.78)}" y2="{Z1(zj)}" stroke="#555" stroke-width="2"/>')
# yard arms, ring frames, walkway, rail
for sx in (-1, 1):
    xa, xb = sorted((X1(sx * 0.9), X1(sx * 4.0)))
    for zc in (100.0, 100.8):
        A(f'<rect x="{xa}" y="{Z1(zc)-3}" width="{xb-xa}" height="6" fill="{YD}" stroke="{YDS}"/>')
    for i in range(5):
        p = sx * (0.9 + i * 0.7)
        q = sx * min(0.9 + (i + 1) * 0.7, 4.0)
        z0, z1 = (100.0, 100.8) if i % 2 == 0 else (100.8, 100.0)
        if abs(q) - abs(p) < 0.69:
            z1 = z0 + (z1 - z0) * (abs(q) - abs(p)) / 0.7
        A(f'<line x1="{X1(p)}" y1="{Z1(z0)}" x2="{X1(q)}" y2="{Z1(z1)}" stroke="{YDS}" stroke-width="1.6"/>')
    A(f'<rect x="{xa}" y="{Z1(100.86)}" width="{xb-xa}" height="3" fill="url(#gr)" stroke="#555" stroke-width="0.6"/>')
    A(f'<line x1="{xa}" y1="{Z1(101.94)}" x2="{xb}" y2="{Z1(101.94)}" stroke="{BOT}" stroke-width="2"/>')
    A(f'<path d="M{X1(sx*4.0)} {Z1(102.2)} l-4 8 l8 8 l-4 8 V{Z1(99.8)}" stroke="#888" fill="none"/>')
for zc in (100.0, 100.8):
    A(f'<rect x="{X1(-0.9)}" y="{Z1(zc)-4}" width="{1.8*k1}" height="8" fill="{TI}" class="s"/>')
# hatch, climb rail inside, masthead rail outside, platform
A(f'<rect x="{X1(0.12)}" y="{Z1(101.85)}" width="{0.5*k1}" height="{0.95*k1}" fill="#fff" stroke="#222" stroke-dasharray="4 2"/>')
A(f'<line x1="{X1(0.05)}" y1="{Z1(99)}" x2="{X1(0.05)}" y2="{Z1(101.2)}" stroke="{BOT}" stroke-width="2.4" stroke-dasharray="6 3"/>')
A(f'<line x1="{X1(0.55)}" y1="{Z1(101.9)}" x2="{X1(0.55)}" y2="{Z1(107.7)}" stroke="{BOT}" stroke-width="2.6"/>')
A(f'<rect x="{X1(-0.35)}" y="{Z1(106.6)}" width="{1.1*k1}" height="4" fill="url(#gr)" stroke="#555"/>')
for xs in (-0.3, 0.7):
    A(f'<line x1="{X1(xs)}" y1="{Z1(106.6)}" x2="{X1(xs)}" y2="{Z1(107.6)}" stroke="#777" stroke-width="1.4"/>')
A('<g opacity="0.55">')
bot(X1(0.15), Z1(106.6), 1.6 * k1 * 0.95)
A('</g>')
# service + data cable up the aft face to the post
A(f'<path d="M{X1(0.68)} {Z1(101.6)} V{Z1(108.0)+3} H{X1(0.06)}" stroke="{BUS}" stroke-width="1.6" fill="none"/>')
# crown, boss, lift arms + twin tangs, lifts
A(f'<rect x="{X1(-0.78)}" y="{Z1(108.05)}" width="{1.56*k1}" height="{0.05*k1+1}" fill="{TI}" class="s"/>')
A(f'<rect x="{X1(-0.12)}" y="{Z1(108.22)}" width="{0.24*k1}" height="{0.17*k1}" fill="{TI}" class="s"/>')
for sx in (-1, 1):
    A(f'<path d="M{X1(sx*0.12)} {Z1(108.18)} L{X1(sx*0.26)} {Z1(108.1)} L{X1(sx*0.26)} {Z1(107.86)} L{X1(sx*0.12)} {Z1(108.05)}" fill="{TI}" class="s"/>')
    A(f'<circle cx="{X1(sx*0.2)}" cy="{Z1(107.92)}" r="3" fill="#c0392b"/>')
    x_end = 4.1
    A(f'<line x1="{X1(sx*0.2)}" y1="{Z1(107.92)}" x2="{X1(sx*x_end)}" y2="{Z1(108-x_end*TA)}" class="rod"/>')
    A(f'<line x1="{X1(sx*0.2)}" y1="{Z1(107.92)+2}" x2="{X1(sx*x_end)}" y2="{Z1(108-x_end*TA)+2.5}" class="rod" stroke-width="1.4"/>')
# stay arms point at the viewer: show their ends as discs
A(f'<circle cx="{X1(0)}" cy="{Z1(108.1)}" r="5" fill="#fff" stroke="#222" stroke-width="1.4"/>')
# instrument post
A(f'<rect x="{X1(-0.04)}" y="{Z1(109.5)}" width="{0.08*k1}" height="{1.28*k1}" fill="#d5d8dc" class="s"/>')
A(f'<rect x="{X1(-0.13)}" y="{Z1(109.62)}" width="{0.26*k1}" height="{0.14*k1}" fill="#5d6d7e" class="s"/>')    # camera
A(f'<circle cx="{X1(0.06)}" cy="{Z1(109.55)}" r="3" fill="#aed6f1" stroke="#222"/>')
A(f'<line x1="{X1(0)}" y1="{Z1(109.62)}" x2="{X1(0)}" y2="{Z1(110.25)}" stroke="#222" stroke-width="2.2"/>')       # antenna
A(f'<circle cx="{X1(0)}" cy="{Z1(110.3)}" r="4" fill="#e74c3c" stroke="#222"/>')                                    # obstacle light
for sx in (-1, 1):
    A(f'<line x1="{X1(0)}" y1="{Z1(109.1)}" x2="{X1(sx*0.25)}" y2="{Z1(109.1)}" stroke="#222" stroke-width="1.6"/>')
    A(f'<rect x="{X1(sx*0.25)-5}" y="{Z1(109.1)-5}" width="10" height="10" fill="#f9e79f" class="s"/>')           # Sun sensors
A(f'<path d="M{X1(0.04)} {Z1(108.75)} l10 -6 v12 z" fill="#d5d8dc" class="s"/>')                                       # corner reflector
A(f'<rect x="{X1(-0.1)}" y="{Z1(108.32)}" width="{0.2*k1}" height="{0.07*k1}" fill="#a9cce3" class="s"/>')           # accelerometer + hub
# labels
A(f'<text x="{X1(-4.1)}" y="{Z1(108-4.1*TA)+18}" font-size="11">lift to the port tip</text>')
A(f'<text x="{X1(4.1)}" y="{Z1(108-4.1*TA)+18}" text-anchor="end" font-size="11">to the starboard tip, 18.5 m</text>')
lab(X1(-0.78), Z1(105), X1(-1.4), Z1(104.4), ['Section joints', '(102, 105 m)'], 'end')
call(1, X1(-0.7), Z1(108.08), X1(-1.6), Z1(108.6))
call(2, X1(-0.22), Z1(107.95), X1(-1.6), Z1(107.6))
call(3, X1(0), Z1(108.1), X1(-1.0), Z1(109.6))
call(4, X1(-0.13), Z1(109.69), X1(-1.0), Z1(110.2))
call(5, X1(0.25) + 5, Z1(109.1), X1(1.0), Z1(110.2))
call(6, X1(0), Z1(110.3), X1(0.45), Z1(110.55))
call(7, X1(0.1), Z1(108.35), X1(1.6), Z1(109.3))
call(8, X1(0.07), Z1(108.75), X1(1.6), Z1(108.75))
call(9, X1(0.55), Z1(107.2), X1(1.6), Z1(107.4))
call(10, X1(0.6), Z1(106.6), X1(1.6), Z1(106.4))
call(11, X1(0.68), Z1(104.0), X1(1.6), Z1(104.2))
call(12, X1(0.62), Z1(101.4), X1(1.6), Z1(102.5))
call(13, X1(-0.9), Z1(100.0), X1(-1.6), Z1(99.4))
key(20, 655, [(1, 'Ti crown plate on the 3 chord ends (~18 kg)'), (2, 'Lift arm + twin tang, a load pin per rod'),
              (3, 'Stay arms fore and aft, 0.95 m (see plan)'), (4, 'Pan-tilt inspection camera'),
              (5, 'Sun sensors (tracking check)'), (6, 'Radio relay + obstacle light'),
              (7, 'Sensor hub + 3-axis accelerometer'), (8, 'Corner reflector for landers'),
              (9, 'Masthead rail (outside, aft face)'), (10, 'Grating at 106.6 m: crown at chest height'),
              (11, '~60 W feed up from the yard junction'), (12, 'Hatch: climb rail to walkway rail'),
              (13, 'Ti ring frames, yard chords bolted on')])
A(f'<text x="20" y="{655+13*17+6}" font-size="11" fill="#555">Top 2 standard sections (102 to 108 m), 1.4 m face; post 1.5 m, on the axis.</text>')

# ================= 2. Crown plan + lift tang =================
A('<text x="470" y="30" class="t">2. Crown, plan from above</text>')
k2, px, py = 140, 680, 225
P = lambda x, y: (px + x * k2, py + y * k2)
R = 1.4 / 3 ** 0.5
tri = [P(R * cos(radians(a)), R * sin(radians(a))) for a in (-90, 30, 150)]       # vertex fore (up), face aft (down)
A(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in tri)}" fill="none" stroke="{MAST}" stroke-width="2" stroke-dasharray="6 3"/>')
cr = [P(0.95 * R * cos(radians(a)), 0.95 * R * sin(radians(a))) for a in (-90, 30, 150)]
A(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in cr)}" fill="{TI}" fill-opacity="0.55" stroke="#222" stroke-width="1.4"/>')
for x, y in tri:
    A(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="7" fill="#888" stroke="#222"/>')
# platform (below, dashed) and masthead rail on the aft face
x0, y0 = P(-0.35, 0.47)
A(f'<rect x="{x0}" y="{y0}" width="{1.1*k2}" height="{0.42*k2}" fill="none" stroke="#777" stroke-dasharray="4 3"/>')
xr, yr = P(0.55, 0.43)
A(f'<rect x="{xr-4}" y="{yr-4}" width="8" height="8" fill="{BOT}"/>')
# stay arms fore/aft with stays leaving
for sy in (-1, 1):
    x1, y1 = P(-0.05, sy * 0.12)
    A(f'<rect x="{x1:.1f}" y="{min(y1, P(0, sy*0.95)[1]):.1f}" width="{0.1*k2:.1f}" height="{abs(P(0, sy*0.95)[1]-y1):.1f}" fill="{TI}" class="s"/>')
    xe, ye = P(0, sy * 0.95)
    A(f'<circle cx="{xe}" cy="{ye}" r="6" fill="#fff" stroke="#222" stroke-width="1.6"/><circle cx="{xe}" cy="{ye}" r="2" fill="#222"/>')
    xs, ys = P(0, sy * 1.32)
    A(f'<line x1="{xe}" y1="{ye}" x2="{xs}" y2="{ys}" stroke="#8e44ad" stroke-width="2.4"/>')
# lift arms port/starboard with twin rods
for sx in (-1, 1):
    x1, y1 = P(sx * 0.12, -0.05)
    A(f'<rect x="{min(x1, P(sx*0.26, 0)[0]):.1f}" y="{y1:.1f}" width="{0.14*k2:.1f}" height="{0.1*k2:.1f}" fill="{TI}" class="s"/>')
    for dy in (-0.03, 0.03):
        xa, ya = P(sx * 0.22, dy)
        xb, yb = P(sx * 1.2, dy * (1 + 0.98 / 18.5 * 17))
        A(f'<line x1="{xa}" y1="{ya}" x2="{xb:.1f}" y2="{yb:.1f}" stroke="{ROD}" stroke-width="2.4"/>')
        A(f'<circle cx="{xa}" cy="{ya}" r="3.2" fill="#c0392b"/>')
A(f'<circle cx="{px}" cy="{py}" r="{0.12*k2}" fill="{TI}" stroke="#222" stroke-width="1.4"/><circle cx="{px}" cy="{py}" r="{0.05*k2}" fill="#d5d8dc" stroke="#222"/>')
A(f'<text x="{P(1.2,0)[0]}" y="{py-14}" text-anchor="end" font-size="11">to the starboard tip →</text>')
A(f'<text x="{P(-1.2,0)[0]}" y="{py-14}" font-size="11">← to the port tip</text>')
A(f'<text x="{px+10}" y="{P(0,-1.32)[1]+4}" font-size="11" fill="#8e44ad">fore diamond stay</text>')
A(f'<text x="{px+10}" y="{P(0,1.32)[1]+4}" font-size="11" fill="#8e44ad">aft diamond stay</text>')
lab(*P(0.05, -0.6), *P(0.5, -0.9), ['Stay arm 0.95 m, clear of', 'the 0.81 m lattice vertex'])
lab(*P(0.85 * R * cos(radians(30)), 0.2), *P(0.75, 0.5), ['Crown plate'])
lab(*P(-0.22, 0.03), *P(-0.75, 0.45), ['Twin tang: 2 load pins,', 'rods 60 mm apart'], 'end')
lab(*P(-0.45, -0.25), *P(-0.75, -0.85), ['Mast top (1.4 m face)'], 'end')
lab(*P(-0.2, 0.89), *P(-0.75, 0.95), ['Grating 1.4 m below'], 'end')
lab(*P(0.06, 0.03), *P(0.75, 0.2), ['Boss + post (on the axis)'])
# lift tang, side view
A('<text x="470" y="452" font-size="12" font-weight="bold">Lift tang, side view (one rod shown)</text>')
k5, bx, by = 380, 525, 500
A(f'<rect x="{bx-0.12*k5}" y="{by-0.06*k5}" width="{0.12*k5}" height="{0.15*k5}" fill="{TI}" class="s"/>')        # boss
A(f'<path d="M{bx} {by-0.03*k5} L{bx+0.2*k5} {by} L{bx+0.2*k5} {by+0.06*k5} L{bx} {by+0.08*k5} z" fill="{TI}" class="s"/>')
A(f'<rect x="{bx-0.12*k5}" y="{by+0.09*k5}" width="{0.4*k5}" height="6" fill="{TI}" class="s"/>')
pxn, pyn = bx + 0.2 * k5, by + 0.03 * k5
A(f'<g transform="rotate({ANG} {pxn} {pyn})">'
  f'<rect x="{pxn-8}" y="{pyn-9}" width="34" height="18" rx="4" fill="{TI}" class="s"/>'
  f'<path d="M{pxn+26} {pyn-8} L{pxn+26+0.12*k5} {pyn-3} V{pyn+3} L{pxn+26} {pyn+8} z" fill="{TI}" class="s"/>'
  f'<rect x="{pxn+26+0.12*k5}" y="{pyn-3}" width="{0.10*k5}" height="6" fill="#fdfefe" stroke="#555"/></g>')
A(f'<circle cx="{pxn}" cy="{pyn}" r="6" fill="#c0392b" stroke="#222"/>')
A(f'<path d="M{pxn} {pyn-6} q-10 -22 -60 -20" stroke="{BUS}" fill="none" stroke-width="1.4"/>')
lab(pxn + 4, pyn - 5, bx + 0.45 * k5, by - 0.08 * k5, ['Load pin Ø16 mm, 10 kN, wired'])
lab(pxn + 50, pyn + 22, bx + 0.45 * k5, by + 0.10 * k5, ['Potted Ti cone socket + clevis, 23.4°'])
A(f'<text x="{bx-0.06*k5}" y="{by+0.02*k5}" text-anchor="middle" font-size="10.5" style="stroke:none">boss</text>')

# ================= 3. Yard tip, looking in along the arm =================
A('<text x="905" y="30" class="t">3. Yard tip, looking in along the arm</text>')
A('<text x="905" y="47" font-size="11" fill="#555">Each rod\'s line here is its true height vs offset,</text>')
A('<text x="905" y="61" font-size="11" fill="#555">so this view shows the clearance at every station.</text>')
k3, c3 = 140, 1060
X3 = lambda y: c3 + y * k3
Z3 = lambda z: 555 - (z - 99.6) * k3
# bot envelope band (above the walkway, 1.8 m)
A(f'<rect x="{X3(-0.30)}" y="{Z3(102.64)}" width="{0.6*k3}" height="{1.8*k3}" fill="url(#hz)" stroke="#c0392b" stroke-dasharray="5 3"/>')
A(f'<text x="{X3(0)}" y="{Z3(101.9)}" text-anchor="middle" font-size="11" fill="#c0392b">bot</text><text x="{X3(0)}" y="{Z3(101.9)+14}" text-anchor="middle" font-size="11" fill="#c0392b">1.8 x 0.6 m</text>')
# yard box at the tip, tip frame, outriggers
for yy in (-0.25, 0.25):
    A(f'<line x1="{X3(yy)}" y1="{Z3(100.0)}" x2="{X3(yy)}" y2="{Z3(100.8)}" stroke="{YDS}" stroke-width="1.6"/>')
for zz in (100.0, 100.8):
    A(f'<line x1="{X3(-0.25)}" y1="{Z3(zz)}" x2="{X3(0.25)}" y2="{Z3(zz)}" stroke="{YDS}" stroke-width="1.6"/>')
A(f'<line x1="{X3(-0.25)}" y1="{Z3(100)}" x2="{X3(0.25)}" y2="{Z3(100.8)}" stroke="{YDS}" stroke-dasharray="4 3"/>')
A(f'<rect x="{X3(-0.62)}" y="{Z3(100.0)-6}" width="{1.24*k3}" height="12" fill="{TI}" class="s"/>')
for yy in (-0.25, 0.25):
    for zz in (100.0, 100.8):
        A(f'<circle cx="{X3(yy)}" cy="{Z3(zz)}" r="{0.03*k3}" fill="{YD}" stroke="{YDS}" stroke-width="1.4"/>')
A(f'<rect x="{X3(-0.27)}" y="{Z3(100.86)}" width="{0.54*k3}" height="{0.04*k3}" fill="url(#gr)" stroke="#555"/>')
A(f'<line x1="{X3(0.30)}" y1="{Z3(100.84)}" x2="{X3(0.30)}" y2="{Z3(101.94)}" stroke="{BOT}" stroke-width="3"/>')
A(f'<rect x="{X3(0.26)}" y="{Z3(101.97)}" width="{0.10*k3}" height="5" fill="{BOT}"/>')
# rods: from outriggers (±0.55, 100.0) towards the crown (±0.03, 108.0), clipped at the panel top
ztop = 102.95
for sy in (-1, 1):
    yt = 0.55 - (0.55 - 0.03) * (ztop - 100.0) / 8.0
    A(f'<line x1="{X3(sy*0.55)}" y1="{Z3(100.0)}" x2="{X3(sy*yt):.1f}" y2="{Z3(ztop):.1f}" stroke="{ROD}" stroke-width="3"/>')
    # barrel adjuster + clevis on the outrigger lug
    A(f'<rect x="{X3(sy*0.55)-5}" y="{Z3(100.0)-30}" width="10" height="22" fill="#d5d8dc" class="s"/>')
    A(f'<rect x="{X3(sy*0.55)-7}" y="{Z3(100.0)-9}" width="14" height="9" fill="{TI}" class="s"/>')
    # brace lug below the bottom chord, brace leaving down and out
    A(f'<line x1="{X3(sy*0.25)}" y1="{Z3(99.95)}" x2="{X3(sy*(0.25+0.3*0.32)):.1f}" y2="{Z3(99.65)}" stroke="#7d3c98" stroke-width="2"/>')
yh = 0.55 - 0.52 * (102.64 - 100.0) / 8.0
A(f'<path d="M{X3(0.30)} {Z3(102.64)} H{X3(yh):.1f}" stroke="#222" stroke-width="1.2"/>')
lab(X3(yh), Z3(102.64), X3(0.62), Z3(102.85), ['≥78 mm at head height'])
lab(X3(0.55) + 5, Z3(100.0) - 20, X3(0.62), Z3(100.6), ['M16 barrel adjuster,', 'locknut + lock wire'])
lab(X3(0.60), Z3(100.0), X3(0.62), Z3(99.9), ['Outrigger ±0.55 m'])
lab(X3(0.40), Z3(102.3), X3(0.62), Z3(102.35), ['Lift rod (bundle)'])
lab(X3(0.30), Z3(101.5), X3(0.62), Z3(101.35), ['Rail + trolley', '(rod 0.12 m out)'])
lab(X3(-0.27), Z3(100.88), X3(-0.72), Z3(100.95), ['Walkway'], 'end')
lab(X3(-0.25), Z3(100.4), X3(-0.72), Z3(100.3), ['Yard box', '0.8 x 0.5 m'], 'end')
lab(X3(-0.30), Z3(99.7), X3(-0.72), Z3(99.68), ['Brace to the', 'spreader tip'], 'end')

# ================= 4. Lift profile and plan =================
A('<text x="470" y="590" class="t">4. Topping lift, crown to yard tip: elevation and plan (plan across-yard x5)</text>')
k4, x4 = 22, 520
X4 = lambda x: x4 + x * k4
Z4 = lambda z: 612 + (108.3 - z) * k4
A(f'<rect x="{X4(-0.7)}" y="{Z4(108)}" width="{1.4*k4}" height="{(108-99.6)*k4}" fill="#f7f7f7" stroke="{MAST}"/>')
A(f'<rect x="{X4(0.7)}" y="{Z4(100.8)}" width="{18.0*k4}" height="{0.8*k4}" fill="none" stroke="{YDS}" stroke-width="1.4"/>')
A(f'<line x1="{X4(0.7)}" y1="{Z4(100.86)}" x2="{X4(18.7)}" y2="{Z4(100.86)}" stroke="#555" stroke-width="2"/>')
A(f'<line x1="{X4(0)}" y1="{Z4(108)}" x2="{X4(18.5)}" y2="{Z4(100.0)}" stroke="{ROD}" stroke-width="2.4"/>')
for i in range(8):
    c = 2.8 + 2.1 * i
    hit = 108 - 8 * c / 18.5 < 100.84 + 1.8
    A(f'<rect x="{X4(c-0.3)}" y="{Z4(102.64)}" width="{0.6*k4}" height="{1.8*k4}" fill="{"url(#hz)" if hit else "none"}" stroke="{"#c0392b" if hit else "#bbb"}" stroke-dasharray="3 2"/>')
x_h, x_w = (108 - 102.64) * 18.5 / 8, (108 - 100.84) * 18.5 / 8
for xx in (x_h, x_w):
    A(f'<circle cx="{X4(xx):.1f}" cy="{Z4(108-8*xx/18.5):.1f}" r="3.5" fill="#c0392b"/>')
lab(X4(x_h), Z4(108 - 8 * x_h / 18.5), X4(9.0), Z4(105.9), [f'1.8 m above the walkway at {x_h:.1f} m'], 'end')
lab(X4(x_w), Z4(108 - 8 * x_w / 18.5), X4(15.0), Z4(104.2), [f'at walkway level at {x_w:.1f} m'], 'end')
A(f'<text x="{X4(18.7)}" y="{Z4(99.6)+14}" text-anchor="end" font-size="11">On the centreline it would cross the bot envelopes at the outer stations (red)</text>')
A(f'<text x="{X4(1.0)}" y="{Z4(108)+4}" font-size="11">crown, 108 m</text>')
# plan, y exaggerated x5
yc, ky = 905, 22 * 5
Y4 = lambda y: yc + y * ky
A(f'<rect x="{X4(0.7)}" y="{Y4(-0.25)}" width="{18.0*k4}" height="{0.5*ky}" fill="#fbeee0" stroke="{YDS}"/>')
A(f'<line x1="{X4(0.7)}" y1="{Y4(0.30)}" x2="{X4(18.7)}" y2="{Y4(0.30)}" stroke="{BOT}" stroke-width="2"/>')
A(f'<rect x="{X4(x_h)}" y="{Y4(-0.30)}" width="{(18.7-x_h)*k4}" height="{0.6*ky}" fill="url(#hz)" stroke="#c0392b" stroke-dasharray="4 3"/>')
A(f'<rect x="{X4(-0.7)}" y="{Y4(-0.40)}" width="{1.4*k4}" height="{0.81*ky}" fill="#f7f7f7" stroke="{MAST}"/>')
for sy in (-1, 1):
    A(f'<line x1="{X4(0.2)}" y1="{Y4(sy*0.03)}" x2="{X4(18.5)}" y2="{Y4(sy*0.55)}" stroke="{ROD}" stroke-width="2.4"/>')
    A(f'<rect x="{X4(18.5)-3}" y="{min(Y4(sy*0.25), Y4(sy*0.58))}" width="6" height="{abs(Y4(sy*0.58)-Y4(sy*0.25))}" fill="{TI}" class="s"/>')
lab(X4(16.0), Y4(-0.48), X4(13.3), Y4(-0.58), ['Rods splay 0.06 → 1.1 m apart'], 'end')
lab(X4(18.5), Y4(0.58), X4(17.2), Y4(0.62), ['Tip outriggers'], 'end')
lab(X4(10.0), Y4(0.30), X4(7.5), Y4(0.55), ['Walkway rail (+0.30 m)'], 'end')
lab(X4(x_h + 0.5), Y4(0.0), X4(11.5), Y4(0.05), ['Bot band where the lift is', 'below head height'], 'end')

# ================= 5. Rod bundle + numbers =================
A('<text x="20" y="905" class="t">5. Rod bundle section</text>')
bc, bk = (85, 955), 4.0 * 1.5
A(f'<circle cx="{bc[0]}" cy="{bc[1]}" r="{5.6*bk:.1f}" fill="#fdfefe" stroke="#555" stroke-width="1.4"/>')
for j in range(7):
    if j == 0:
        x, y = bc
    else:
        a = radians(60 * j)
        x, y = bc[0] + 3.0 * bk * cos(a), bc[1] + 3.0 * bk * sin(a)
    A(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{1.5*bk:.1f}" fill="#2c3e50"/>')
for j, t in enumerate(['7 x Ø3 mm pultruded rods, ~50 mm²',
                       'White static-dissipative jacket, ~Ø11 mm',
                       'Breaks ~89 kN; ~0.1 kg/m',
                       'Coils to Ø1.4 m at 0.21% (Ø8 solid: 0.57%)']):
    A(f'<text x="140" y="{932+j*15}" font-size="11.5">{t}</text>')
nx = 1010
A(f'<text x="{nx}" y="612" class="t">Numbers</text>')
for j, t in enumerate(['Lift 20.2 m at 23.4°', 'Static 3.36 kN (1.68 per rod)', 'Bot at the outer station: 3.69 kN',
                       'Factor 48 per rod; 24 on one rod', 'Outer pack off: −0.58 kN in a lift',
                       'Crown sideways ≤0.83 kN, sway 1.4 mm', 'Masthead compression ~4.7 kN',
                       'Stay arm root ~0.9 kN·m', 'Rod mode 3.2 Hz, sag 5 mm', '1/8 adjuster turn = 64 N',
                       'Broken rod: 0.73 kN·m arm torsion', 'Horizon ~19 km (22 km to a rover)']):
    A(f'<text x="{nx}" y="{632+j*15}" font-size="11.5">{t}</text>')
A('</svg>')
open('masthead.svg', 'w').write('\n'.join(o))
print('wrote masthead.svg')
