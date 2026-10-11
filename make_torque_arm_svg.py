# Generates torque-arm.svg (rev 9: V torque arms with a Y-bridle; plan + elevation). Run: python3 make_torque_arm_svg.py
import math
o = []
A = o.append
W, H = 1240, 850
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="13">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:2}.l{stroke:#555;stroke-width:1;fill:none}.guy{stroke:#8e44ad;stroke-width:2}'
  '.arm{stroke:#c87f0a}.collar{fill:#4a9}.mast{fill:#888}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:17px;font-weight:bold}</style>')


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*15:.0f}" text-anchor="{anchor}">{t}</text>')


# ---------------- plan: one of the three arms
k, cx, cy = 16, 70, 300
P = lambda r, t: (cx + r * k, cy - t * k)          # r: radial (m), t: tangential (m)
A('<text x="20" y="30" class="t">Plan: one V pair of arms (of three) and its Y-bridle</text>')
# mast + collar
A(f'<circle cx="{cx}" cy="{cy}" r="{1.45*k}" fill="none" stroke="#4a9" stroke-width="7"/><circle cx="{cx}" cy="{cy}" r="{0.95*k}" fill="none" stroke="#7d8790" stroke-width="5"/>')
pts = [(cx + 0.81 * k * math.cos(math.radians(a)), cy + 0.81 * k * math.sin(math.radians(a))) for a in (0, 120, 240)]
A('<polygon points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '" fill="none" stroke="#888" stroke-width="3"/>')
# array line (parked) and stub arms of the other two planes
for ang, w, op in ((30, 4, 0.35),):
    a = math.radians(ang)
    A(f'<line x1="{cx}" y1="{cy}" x2="{cx+17*k*math.cos(a):.0f}" y2="{cy-17*k*math.sin(a):.0f}" stroke="#2c4a7a" stroke-width="{w}" opacity="{op}"/>')
# Y-bridle: legs from the arm tips to the split plate, single main cable to the foot
fx, fy = P(30, 0)
jx, jy = P(25.6, 0)
for t in (3, -3):
    x, y = P(8, t)
    A(f'<line x1="{x}" y1="{y}" x2="{jx}" y2="{jy}" class="guy"/>')
A(f'<line x1="{jx}" y1="{jy}" x2="{fx}" y2="{fy}" stroke="#8e44ad" stroke-width="4"/>')
A(f'<polygon points="{jx-9},{jy-9} {jx+7},{jy} {jx-9},{jy+9}" fill="#8e44ad" stroke="#222"/>')
A(f'<rect x="{fx-10}" y="{fy-10}" width="20" height="20" fill="#555"/>')
# arm (stem + crossbar) and the twisted position (ghost)
th = math.radians(8)  # exaggerated twist
def rotp(x, y):
    dx, dy = x - cx, y - cy
    return cx + dx * math.cos(th) + dy * math.sin(th), cy - dx * math.sin(th) + dy * math.cos(th)
for ghost in (True, False):
    f = (lambda p: rotp(*p)) if ghost else (lambda p: p)
    sty = 'stroke="#c87f0a" stroke-width="2" stroke-dasharray="6 4" opacity="0.9"' if ghost else 'stroke="#c87f0a" stroke-width="7"'
    for t in (0.6, -0.6):                                   # the two hinged arms of the V
        a0, a1 = f(P(1.45, t)), f(P(8, 3 if t > 0 else -3))
        A(f'<line x1="{a0[0]:.1f}" y1="{a0[1]:.1f}" x2="{a1[0]:.1f}" y2="{a1[1]:.1f}" {sty}/>')
    c0, c1 = f(P(8, 3)), f(P(8, -3))                       # light tip tie bar
    tie = sty.replace('stroke-width="7"', 'stroke-width="2.5"')
    A(f'<line x1="{c0[0]:.1f}" y1="{c0[1]:.1f}" x2="{c1[0]:.1f}" y2="{c1[1]:.1f}" {tie}/>')
# rotation arrow on collar
r = 2.3 * k
A(f'<path d="M{cx+r*math.cos(math.radians(-60)):.0f} {cy+r*math.sin(math.radians(-60)):.0f} A{r} {r} 0 0 0 {cx+r*math.cos(math.radians(-110)):.0f} {cy+r*math.sin(math.radians(-110)):.0f}" fill="none" stroke="#222" stroke-width="1.6" marker-end="url(#ar)"/>')
A(f'<text x="{cx-30}" y="{cy-48}" font-size="12">friction drag</text>')
# tension change labels
x, y = P(13, 2.2); A(f'<text x="{x}" y="{y-6}" font-size="13" fill="#8e44ad" font-weight="bold">+ΔT (leg tightens)</text>')
x, y = P(13, -2.2); A(f'<text x="{x}" y="{y+18}" font-size="13" fill="#8e44ad" font-weight="bold">−ΔT (leg slackens)</text>')
lab(fx, fy + 10, fx + 5, fy + 60, ['Foot: tensioner +', 'load cell, 30 m out'], 'end')
lab(jx, jy + 9, jx - 60, jy + 128, ['Split plate (fixed, NOT a pulley),', '~12 m up; load pins read ΔT'], 'end')
lab((jx+fx)/2, jy, (jx+fx)/2, jy + 30, ['Single main cable'], 'end')
x, y = P(8, 3); lab(x, y, x + 20, y - 40, ['Arm tips ±3 m, light tie bar'])
x, y = P(5, -1.9); lab(x, y, x + 10, y + 48, ['Two hinged arms in a V (CFRP), 8 m'])
x, y = P(1.45, 1.0); lab(x, y, x - 20, y + 128, ['Upper collar (stationary),', 'mast turns inside'], 'start')
a = math.radians(30); x, y = cx + 15 * k * math.cos(a), cy - 15 * k * math.sin(a)
lab(x, y, x + 30, y - 18, ['Wing-lowering plane (30°): tips stay', '≥1.4 m clear (tip azimuth 20.6°)'])
A(f'<text x="20" y="{cy+195}" font-size="12">Dashed: arms after a small twist (exaggerated). One leg tightens and the other slackens, and the split plate</text>')
A(f'<text x="20" y="{cy+211}" font-size="12">is pulled sideways against the main cable tension. ~170 kN·m/rad at 1.5 kN, ~250 at 3 kN (all 3 planes):</text>')
A(f'<text x="20" y="{cy+227}" font-size="12">~0.17° twist at 500 N·m (partly seized roller). Without arms: ~10°. Raise tension to stiffen.</text>')

# ---------------- elevation: hinge, knee brace, latch, folded position
e, mx, hy = 26, 720, 370   # px/m, mast x, hinge height (62 m level)
Xe = lambda r: mx + r * e
Ye = lambda z: hy - z * e   # z relative to 62 m
A(f'<text x="{mx-60}" y="30" class="t">Elevation: two-point root (500 mm couple)</text>')
A(f'<rect x="{mx-18}" y="60" width="36" height="440" class="mast s"/>')
A(f'<text x="{mx}" y="76" text-anchor="middle" font-size="11" style="stroke:none" fill="#fff">mast</text>')
# collar (stationary) with band
A(f'<rect x="{mx+18}" y="{Ye(0.4)}" width="{0.9*e}" height="{0.8*e+12}" class="collar s"/>')
A(f'<rect x="{mx-18-0.9*e}" y="{Ye(0.4)}" width="{0.9*e}" height="{0.8*e+12}" class="collar s"/>')
hx = Xe(1.45)
# array sweep bottom at 67 m
A(f'<line x1="{mx-40}" y1="{Ye(5)}" x2="{Xe(17)}" y2="{Ye(5)}" stroke="#2c4a7a" stroke-dasharray="8 5"/><text x="{Xe(9)}" y="{Ye(5)-8}" font-size="12">Bottom of array sweep, 67 m (5 m above)</text>')
# deployed arm truss (top chord, bottom chord, verticals)
A(f'<line x1="{hx}" y1="{Ye(0)}" x2="{Xe(8)}" y2="{Ye(0)}" stroke="#c87f0a" stroke-width="5"/>')
A(f'<line x1="{hx+10}" y1="{Ye(-0.6)}" x2="{Xe(8)}" y2="{Ye(-0.6)}" stroke="#c87f0a" stroke-width="3"/>')
for i in range(6):
    r0 = 1.45 + 0.3 + i * 1.1
    A(f'<line x1="{Xe(r0)}" y1="{Ye(0)}" x2="{Xe(r0+0.55)}" y2="{Ye(-0.6)}" stroke="#c87f0a" stroke-width="1.5"/>')
A(f'<rect x="{Xe(8)-6}" y="{Ye(0)-8}" width="12" height="{0.6*e+16}" fill="#c87f0a" class="s"/>')   # crossbar end-on
# hinge
A(f'<circle cx="{hx}" cy="{Ye(0)}" r="8" fill="#fff" class="s"/><circle cx="{hx}" cy="{Ye(0)}" r="3" fill="#222"/>')
# two-point root: fold hinge (top pin) + seat with keeper pin 500 mm below
A(f'<rect x="{mx+18}" y="{Ye(0.4)}" width="{0.9*e}" height="{0.95*e+14}" class="collar s"/>')            # 0.5 m deep collar box at the arm station
A(f'<rect x="{hx-5}" y="{Ye(0)}" width="12" height="{0.5*e}" fill="#c87f0a" class="s"/>')                # root post
A(f'<circle cx="{hx}" cy="{Ye(-0.5)}" r="6" fill="#4a9" class="s"/><circle cx="{hx}" cy="{Ye(-0.5)}" r="2.5" fill="#f5b700" stroke="#222"/>')
# folded (jack-up) position, dashed, and swing arc
A(f'<line x1="{hx}" y1="{Ye(0)}" x2="{hx}" y2="{Ye(6.6)}" stroke="#c87f0a" stroke-width="4" stroke-dasharray="7 5"/>')
A(f'<line x1="{hx+0.6*e}" y1="{Ye(0.3)}" x2="{hx+0.6*e}" y2="{Ye(6.6)}" stroke="#c87f0a" stroke-width="2" stroke-dasharray="7 5"/>')
A(f'<path d="M{hx+20} {Ye(6.2)} A{6.4*e} {6.4*e} 0 0 1 {Xe(7.3)} {Ye(0.9)}" fill="none" stroke="#222" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#ar)"/>')
# wire from tip down to foot
A(f'<line x1="{Xe(8)}" y1="{Ye(-0.4)}" x2="{Xe(8)+(Ye(-4.5)-Ye(-0.4))/math.tan(math.radians(64))}" y2="{Ye(-4.5)}" class="guy"/>')
# labels
lab(hx - 8, Ye(0), mx - 60, Ye(0) - 40, ['Top pin = fold hinge', '(horizontal axis)'], 'end')
lab(hx, Ye(4), Xe(2.2), Ye(6.5), ['Folded upright for jack-up'])
lab(Xe(5.5), Ye(3.5), Xe(6.4), Ye(4.3), ['Wire tension swings it down'])
lab(hx + 6, Ye(-0.5), Xe(5.5), Ye(-2.2), ['Two-point root: see detail below'])
lab(mx + 18 + 0.45 * e, Ye(-0.6) + 10, mx - 40, Ye(-2.4), ['Collar box, 0.5 m deep', 'at each arm station'], 'end')
lab(mx + 30, Ye(0.1), mx - 40, Ye(-1.6), ['Upper collar, 62 m'], 'end')
lab(Xe(8), Ye(0) - 8, Xe(8.6), Ye(1.2), ['Tip tie bar (end-on)'])
lab(Xe(8.9), Ye(-2.4), Xe(11.0), Ye(-0.9), ['Bridle leg, down to the', 'split plate 12 m up'])

# ---------------- detail: two-point root (enlarged)
d, ox, oy = 210, 840, 610          # px per metre, origin = top pin
A(f'<rect x="{ox-200}" y="{oy-60}" width="590" height="190" fill="none" stroke="#999" stroke-dasharray="4 3"/>')
A(f'<text x="{ox-190}" y="{oy-42}" font-weight="bold">Detail: two-point root (no knee brace)</text>')
A(f'<rect x="{ox-130}" y="{oy-30}" width="30" height="160" class="mast s"/>')                                   # mast edge
A(f'<rect x="{ox-100}" y="{oy-22}" width="{0.45*d}" height="{0.5*d+44}" class="collar s"/>')                  # collar box
A(f'<rect x="{ox-8}" y="{oy}" width="16" height="{0.5*d}" fill="#c87f0a" class="s"/>')                         # root post
A(f'<rect x="{ox+8}" y="{oy-6}" width="{1.5*d}" height="12" fill="#c87f0a" class="s"/>')                       # arm top chord
A(f'<rect x="{ox+8}" y="{oy+0.3*d}" width="{1.5*d}" height="8" fill="#c87f0a" class="s"/>')                    # arm bottom chord
for i in range(5):
    x0 = ox + 14 + i * 0.3 * d
    A(f'<line x1="{x0}" y1="{oy+6}" x2="{x0+0.15*d}" y2="{oy+0.3*d}" stroke="#c87f0a" stroke-width="2"/>')
A(f'<circle cx="{ox}" cy="{oy}" r="10" fill="#fff" class="s"/><circle cx="{ox}" cy="{oy}" r="4" fill="#222"/>')   # top pin
A(f'<rect x="{ox-26}" y="{oy+0.5*d-8}" width="18" height="22" fill="#555" class="s"/>')                        # seat
A(f'<circle cx="{ox}" cy="{oy+0.5*d+4}" r="6" fill="#f5b700" stroke="#222"/>')                                   # keeper pin
A(f'<path d="M{ox+28} {oy-30} H{ox+80}" stroke="#c0392b" stroke-width="2.5" marker-end="url(#ar)"/>')
A(f'<text x="{ox+84}" y="{oy-26}" font-size="12" fill="#c0392b">top pin: ~9 kN tension (fold hinge)</text>')
A(f'<path d="M{ox+80} {oy+0.5*d+24} H{ox+16}" stroke="#2e7d32" stroke-width="2.5" marker-end="url(#ar)"/>')
A(f'<text x="{ox+84}" y="{oy+0.5*d+28}" font-size="12" fill="#2e7d32">seat: ~9 kN compression; keeper pin ~0</text>')
A(f'<path d="M{ox+1.5*d} {oy+0.15*d} v40" stroke="#8e44ad" stroke-width="2.5" marker-end="url(#ar)"/>')
A(f'<text x="{ox+1.5*d+6}" y="{oy+0.15*d+30}" font-size="12" fill="#8e44ad">bridle pull</text>')
A(f'<path d="M{ox-145} {oy} V{oy+0.5*d}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><line x1="{ox-150}" y1="{oy}" x2="{ox-10}" y2="{oy}" stroke="#999" stroke-dasharray="2 3"/><line x1="{ox-150}" y1="{oy+0.5*d}" x2="{ox-10}" y2="{oy+0.5*d}" stroke="#999" stroke-dasharray="2 3"/>')
A(f'<text x="{ox-150}" y="{oy+0.25*d+4}" text-anchor="end" font-size="12" font-weight="bold">500</text><text x="{ox-150}" y="{oy+0.25*d+18}" text-anchor="end" font-size="12" font-weight="bold">mm</text>')
A(f'<text x="{ox-190}" y="{oy+150}" font-size="11.5">Root moment ~4.6 kN·m per arm at 1.5 kN bridle tension (~19 kN pin loads at 3 kN): 20–25 mm Ti pins.</text>')
A(f'<text x="{mx-60}" y="{H-36}" font-size="12">Each arm ~30 kg; the V pair folds as one frame on a common hinge axis.</text>')
A(f'<text x="{mx-60}" y="{H-20}" font-size="12">Folded arms ride up with the collar; the 3 pairs balance, so the collar is not tilted.</text>')
A('</svg>')
open('torque-arm.svg', 'w').write('\n'.join(o))
