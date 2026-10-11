# Generates torque-arm.svg (rev 9: V torque arms with a Y-bridle; plan + elevation). Run: python3 make_torque_arm_svg.py
import math
o = []
A = o.append
W, H = 1240, 920
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
A(f'<text x="{mx-60}" y="30" class="t">Elevation: fold hinge + hanging A-bracket knee</text>')
A(f'<rect x="{mx-18}" y="60" width="36" height="420" class="mast s"/>')
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
# hanging A-bracket knee: pins on the arm bottom chord 3 m out, apex seated in a funnel cup 1.5 m below the hinge
A(f'<rect x="{mx+18}" y="{Ye(0.4)}" width="{0.9*e}" height="{0.95*e+14}" class="collar s"/>')
A(f'<rect x="{hx-4}" y="{Ye(-0.5)}" width="8" height="{1.0*e}" fill="#555" class="s"/>')                   # seat post
A(f'<path d="M{hx-2} {Ye(-1.5)} l14 -10 M{hx-2} {Ye(-1.5)} l-6 -10" stroke="#222" stroke-width="2" fill="none"/>')
A(f'<line x1="{Xe(4.45)}" y1="{Ye(-0.6)}" x2="{hx+3}" y2="{Ye(-1.5)}" stroke="#c87f0a" stroke-width="4"/>')  # knee
A(f'<circle cx="{Xe(4.45)}" cy="{Ye(-0.6)}" r="4" fill="#fff" class="s"/>')
A(f'<circle cx="{hx+3}" cy="{Ye(-1.5)}" r="4" fill="#f5b700" stroke="#222"/>')
# folded (jack-up) position, dashed, and swing arc
A(f'<line x1="{hx}" y1="{Ye(0)}" x2="{hx}" y2="{Ye(6.6)}" stroke="#c87f0a" stroke-width="4" stroke-dasharray="7 5"/>')
A(f'<line x1="{hx+0.6*e}" y1="{Ye(0.3)}" x2="{hx+0.6*e}" y2="{Ye(6.6)}" stroke="#c87f0a" stroke-width="2" stroke-dasharray="7 5"/>')
A(f'<line x1="{hx+0.6*e}" y1="{Ye(3)}" x2="{hx+0.6*e}" y2="{Ye(3-3.35)}" stroke="#c87f0a" stroke-width="2" stroke-dasharray="3 3"/>')
A(f'<path d="M{hx+20} {Ye(6.2)} A{6.4*e} {6.4*e} 0 0 1 {Xe(7.3)} {Ye(0.9)}" fill="none" stroke="#222" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#ar)"/>')
# wire from tip down to foot
A(f'<line x1="{Xe(8)}" y1="{Ye(-0.4)}" x2="{Xe(8)+(Ye(-4.5)-Ye(-0.4))/math.tan(math.radians(64))}" y2="{Ye(-4.5)}" class="guy"/>')
# labels
lab(hx - 8, Ye(0), mx - 60, Ye(0) - 40, ['Fold hinge', '(horizontal pin)'], 'end')
lab(hx, Ye(4), Xe(2.2), Ye(6.5), ['Folded upright for jack-up'])
lab(Xe(5.5), Ye(3.5), Xe(6.4), Ye(4.3), ['Wire tension swings it down'])
lab(Xe(3), Ye(-1.1), Xe(5.5), Ye(-2.2), ['Hanging A-bracket knee: see detail'])
lab(hx - 4, Ye(-1.2), mx - 40, Ye(-2.4), ['Seat post under the collar', '(stationary), cup 1.5 m down'], 'end')
lab(mx + 30, Ye(0.1), mx - 40, Ye(-1.6), ['Upper collar, 62 m'], 'end')
lab(Xe(8), Ye(0) - 8, Xe(8.6), Ye(1.2), ['Tip tie bar (end-on)'])
lab(Xe(8.9), Ye(-2.4), Xe(11.0), Ye(-0.9), ['Bridle leg, down to the', 'split plate 12 m up'])

# ---------------- detail: hanging A-bracket knee (enlarged)
d, ox, oy = 100, 780, 610          # px per metre, origin = fold hinge
A(f'<rect x="{ox-190}" y="{oy-85}" width="625" height="340" fill="none" stroke="#999" stroke-dasharray="4 3"/>')
A(f'<text x="{ox-180}" y="{oy-66}" font-weight="bold">Detail: hanging A-bracket knee</text>')
A(f'<rect x="{ox-120}" y="{oy-30}" width="26" height="240" class="mast s"/>')
A(f'<rect x="{ox-94}" y="{oy-0.4*d}" width="{0.8*d}" height="{0.5*d+14}" class="collar s"/>')               # collar ring
A(f'<rect x="{ox-10}" y="{oy+0.1*d}" width="10" height="{1.4*d}" fill="#555" class="s"/>')                  # seat post
cx_, cy_ = ox + 6, oy + 1.5 * d
A(f'<path d="M{cx_-10} {cy_+6} Q{cx_} {cy_+14} {cx_+10} {cy_+6} L{cx_+34} {cy_-22}" fill="none" stroke="#222" stroke-width="3"/>')  # cup + funnel ramp
A(f'<line x1="{ox}" y1="{oy}" x2="{ox+3.6*d}" y2="{oy}" stroke="#c87f0a" stroke-width="7"/>')                # arm top chord
A(f'<line x1="{ox+0.15*d}" y1="{oy+0.6*d}" x2="{ox+3.6*d}" y2="{oy+0.6*d}" stroke="#c87f0a" stroke-width="4"/>')  # bottom chord
for i in range(6):
    x0 = ox + 0.15 * d + i * 0.55 * d
    A(f'<line x1="{x0}" y1="{oy}" x2="{x0+0.27*d}" y2="{oy+0.6*d}" stroke="#c87f0a" stroke-width="1.5"/>')
A(f'<circle cx="{ox}" cy="{oy}" r="8" fill="#fff" class="s"/><circle cx="{ox}" cy="{oy}" r="3" fill="#222"/>')   # fold hinge
kx, ky = ox + 3.0 * d, oy + 0.6 * d
A(f'<line x1="{kx}" y1="{ky}" x2="{cx_}" y2="{cy_+4}" stroke="#c87f0a" stroke-width="5"/>')                 # knee (seated)
A(f'<circle cx="{kx}" cy="{ky}" r="6" fill="#fff" class="s"/><circle cx="{cx_}" cy="{cy_+4}" r="5" fill="#f5b700" stroke="#222"/>')
A(f'<line x1="{kx}" y1="{ky}" x2="{kx}" y2="{ky+1.45*d}" stroke="#c87f0a" stroke-width="2" stroke-dasharray="5 4"/>')  # unloaded: hangs vertical
# front view of the A (small)
fx0, fy0 = ox + 3.95 * d, oy + 0.75 * d
A(f'<line x1="{fx0-26}" y1="{fy0}" x2="{fx0+26}" y2="{fy0}" stroke="#c87f0a" stroke-width="4"/>')
A(f'<path d="M{fx0-22} {fy0} L{fx0} {fy0+1.1*d} L{fx0+22} {fy0}" fill="none" stroke="#c87f0a" stroke-width="3"/>')
A(f'<circle cx="{fx0-22}" cy="{fy0}" r="4" fill="#fff" class="s"/><circle cx="{fx0+22}" cy="{fy0}" r="4" fill="#fff" class="s"/><circle cx="{fx0}" cy="{fy0+1.1*d}" r="4" fill="#f5b700" stroke="#222"/>')
A(f'<text x="{fx0}" y="{fy0-12}" text-anchor="middle" font-size="11">A, seen end-on:</text><text x="{fx0}" y="{fy0+1.1*d+18}" text-anchor="middle" font-size="11">2 pins ~0.5 m apart</text>')
# labels and forces
lab(ox + 1.8 * d, oy + 1.05 * d, ox + 0.9 * d, oy + 2.2 * d, ['Knee (A-bracket), ~3.35 m: compression only,', '~3.4 kN (6.9 kN at 3 kN bridle tension)'], 'start')
lab(kx - 2, ky + 1.3 * d, kx - 30, ky + 1.3 * d, ['Unloaded:', 'hangs vertically'], 'end')
lab(cx_ - 8, cy_ + 8, ox - 60, cy_ + 30, ['Funnel ramp + cup seat'], 'end')
lab(ox - 5, oy + 0.9 * d, ox - 60, oy + 0.9 * d, ['Seat post', '(stationary)'], 'end')
lab(ox + 6, oy - 6, ox + 0.5 * d, oy - 0.45 * d, ['Fold hinge (~3 kN)'])
A(f'<path d="M{ox+3.6*d} {oy+0.05*d} v40" stroke="#8e44ad" stroke-width="2.5" marker-end="url(#ar)"/><text x="{ox+3.6*d-6}" y="{oy-12}" font-size="11.5" fill="#8e44ad" text-anchor="middle">bridle pull</text>')
A(f'<text x="{mx-60}" y="{H-36}" font-size="12">Each arm ~30 kg; the V pair folds as one frame on a common hinge axis.</text>')
A(f'<text x="{mx-60}" y="{H-20}" font-size="12">Folded arms ride up with the collar; the 3 pairs balance, so the collar is not tilted.</text>')
A('</svg>')
open('torque-arm.svg', 'w').write('\n'.join(o))
