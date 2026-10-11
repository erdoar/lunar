# Generates torque-arm.svg (upper collar anti-wind-up torque arm: plan + elevation). Run: python3 make_torque_arm_svg.py
import math
o = []
A = o.append
W, H = 1240, 760
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
A('<text x="20" y="30" class="t">Plan: one torque arm (of three) and its two wires</text>')
# mast + collar
A(f'<circle cx="{cx}" cy="{cy}" r="{1.45*k}" fill="none" stroke="#4a9" stroke-width="7"/><circle cx="{cx}" cy="{cy}" r="{0.95*k}" fill="none" stroke="#7d8790" stroke-width="5"/>')
pts = [(cx + 0.81 * k * math.cos(math.radians(a)), cy + 0.81 * k * math.sin(math.radians(a))) for a in (0, 120, 240)]
A('<polygon points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '" fill="none" stroke="#888" stroke-width="3"/>')
# array line (parked) and stub arms of the other two planes
for ang, w, op in ((30, 4, 0.35),):
    a = math.radians(ang)
    A(f'<line x1="{cx}" y1="{cy}" x2="{cx+17*k*math.cos(a):.0f}" y2="{cy-17*k*math.sin(a):.0f}" stroke="#2c4a7a" stroke-width="{w}" opacity="{op}"/>')
# wires to foot
fx, fy = P(30, 0)
for t in (3, -3):
    x, y = P(8, t)
    A(f'<line x1="{x}" y1="{y}" x2="{fx}" y2="{fy}" class="guy"/>')
A(f'<rect x="{fx-10}" y="{fy-10}" width="20" height="20" fill="#555"/>')
# arm (stem + crossbar) and the twisted position (ghost)
th = math.radians(8)  # exaggerated twist
def rotp(x, y):
    dx, dy = x - cx, y - cy
    return cx + dx * math.cos(th) + dy * math.sin(th), cy - dx * math.sin(th) + dy * math.cos(th)
for ghost in (True, False):
    f = (lambda p: rotp(*p)) if ghost else (lambda p: p)
    sty = 'stroke="#c87f0a" stroke-width="2" stroke-dasharray="6 4" opacity="0.9"' if ghost else 'stroke="#c87f0a" stroke-width="7"'
    a0, a1, c0, c1 = f(P(1.45, 0)), f(P(8, 0)), f(P(8, 3)), f(P(8, -3))
    A(f'<line x1="{a0[0]:.1f}" y1="{a0[1]:.1f}" x2="{a1[0]:.1f}" y2="{a1[1]:.1f}" {sty}/>')
    A(f'<line x1="{c0[0]:.1f}" y1="{c0[1]:.1f}" x2="{c1[0]:.1f}" y2="{c1[1]:.1f}" {sty}/>')
    if not ghost:
        for d in ((1.45, 0.5, 8, 3), (1.45, -0.5, 8, -3)):
            q0, q1 = P(d[0], d[1]), P(d[2], d[3])
            A(f'<line x1="{q0[0]}" y1="{q0[1]}" x2="{q1[0]}" y2="{q1[1]}" stroke="#c87f0a" stroke-width="2.5"/>')
# rotation arrow on collar
r = 2.3 * k
A(f'<path d="M{cx+r*math.cos(math.radians(-60)):.0f} {cy+r*math.sin(math.radians(-60)):.0f} A{r} {r} 0 0 0 {cx+r*math.cos(math.radians(-110)):.0f} {cy+r*math.sin(math.radians(-110)):.0f}" fill="none" stroke="#222" stroke-width="1.6" marker-end="url(#ar)"/>')
A(f'<text x="{cx-30}" y="{cy-48}" font-size="12">friction drag</text>')
# tension change labels
x, y = P(14, 2.3); A(f'<text x="{x}" y="{y-6}" font-size="13" fill="#8e44ad" font-weight="bold">+ΔT (stretches)</text>')
x, y = P(14, -2.3); A(f'<text x="{x}" y="{y+18}" font-size="13" fill="#8e44ad" font-weight="bold">−ΔT (slackens)</text>')
lab(fx, fy + 10, fx - 10, fy + 50, ['Foot pad, 30 m out'], 'end')
x, y = P(8, 3); lab(x, y, x + 20, y - 40, ['Crossbar ±3 m (6 m across)'])
x, y = P(5, 0); lab(x, y + 4, x + 10, y + 75, ['Arm, 8 m (CFRP truss)'])
x, y = P(5, 1.9); lab(x, y, x - 10, y - 70, ['Diagonal braces'], 'end')
x, y = P(1.45, 1.0); lab(x, y, x - 20, y + 110, ['Upper collar (stationary),', 'mast turns inside'], 'start')
a = math.radians(30); x, y = cx + 15 * k * math.cos(a), cy - 15 * k * math.sin(a)
lab(x, y, x + 30, y - 18, ['Curtain-lowering plane (30°): tips stay', '≥1.4 m clear (tip azimuth 20.6°)'])
A(f'<text x="20" y="{cy+150}" font-size="12">Dashed: arm after a small twist (exaggerated). One wire is stretched and the other slackened;</text>')
A(f'<text x="20" y="{cy+166}" font-size="12">their tension difference × 3 m lever resists the twist. Stiffness ~320 kN·m/rad (all 3 arms);</text>')
A(f'<text x="20" y="{cy+182}" font-size="12">~0.09° twist at 500 N·m (partly seized roller). Without arms: ~10°.</text>')

# ---------------- elevation: hinge, knee brace, latch, folded position
e, mx, hy = 26, 720, 370   # px/m, mast x, hinge height (62 m level)
Xe = lambda r: mx + r * e
Ye = lambda z: hy - z * e   # z relative to 62 m
A(f'<text x="{mx-60}" y="30" class="t">Elevation: hinge, knee brace, latch</text>')
A(f'<rect x="{mx-18}" y="60" width="36" height="{H-260}" class="mast s"/>')
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
# knee brace from collar lower flange to arm at r=5
kb0, kb1 = (Xe(1.6), Ye(-2.6)), (Xe(5), Ye(-0.6))
A(f'<rect x="{mx+18}" y="{Ye(-2.4)}" width="{0.9*e}" height="14" class="collar s"/>')
A(f'<line x1="{kb0[0]}" y1="{kb0[1]}" x2="{kb1[0]}" y2="{kb1[1]}" stroke="#c87f0a" stroke-width="4"/>')
A(f'<circle cx="{kb0[0]}" cy="{kb0[1]}" r="5" fill="#fff" class="s"/>')
# stop + latch at the knee-brace head
A(f'<rect x="{kb1[0]-12}" y="{kb1[1]-2}" width="24" height="12" fill="#c0392b" class="s"/>')
A(f'<circle cx="{kb1[0]+20}" cy="{kb1[1]+14}" r="5" fill="#f5b700" stroke="#222"/>')
# folded (jack-up) position, dashed, and swing arc
A(f'<line x1="{hx}" y1="{Ye(0)}" x2="{hx}" y2="{Ye(6.6)}" stroke="#c87f0a" stroke-width="4" stroke-dasharray="7 5"/>')
A(f'<line x1="{hx+0.6*e}" y1="{Ye(0.3)}" x2="{hx+0.6*e}" y2="{Ye(6.6)}" stroke="#c87f0a" stroke-width="2" stroke-dasharray="7 5"/>')
A(f'<path d="M{hx+20} {Ye(6.2)} A{6.4*e} {6.4*e} 0 0 1 {Xe(7.3)} {Ye(0.9)}" fill="none" stroke="#222" stroke-width="1.5" stroke-dasharray="4 3" marker-end="url(#ar)"/>')
# wire from tip down to foot
A(f'<line x1="{Xe(8)}" y1="{Ye(-0.4)}" x2="{Xe(8)+(H-120-Ye(-0.4))/math.tan(math.radians(64))}" y2="{H-120}" class="guy"/>')
# labels
lab(hx - 8, Ye(0), mx - 60, Ye(0) - 40, ['Hinge pin', '(horizontal axis)'], 'end')
lab(hx, Ye(4), Xe(2.2), Ye(6.5), ['Folded upright for jack-up'])
lab(Xe(5.5), Ye(3.5), Xe(6.4), Ye(4.3), ['Wire tension swings it down'])
lab(kb1[0] + 12, kb1[1] + 6, Xe(8.6), Ye(-2.2), ['Stop + spring latch', '(camera target, yellow)'])
lab((kb0[0] + kb1[0]) / 2, (kb0[1] + kb1[1]) / 2, Xe(2.4), Ye(-5.4), ['Knee brace (pinned), carries', 'the arm bending'])
lab(mx + 18 + 0.45 * e, Ye(-2.4) + 14, mx - 40, Ye(-4.2), ['Collar lower flange'], 'end')
lab(mx + 30, Ye(0.1), mx - 40, Ye(-1.6), ['Upper collar, 62 m'], 'end')
lab(Xe(8), Ye(0) - 8, Xe(8.6), Ye(1.2), ['Crossbar (end-on)'])
lab(Xe(9.6), Ye(-4.4), Xe(10.4), Ye(-5.6), ['Wire to foot (64° slope);', 'one from each crossbar end'])
A(f'<text x="{mx-60}" y="{H-36}" font-size="12">Arm ~70 kg (CFRP truss, Ti hinge and latch). Upward-folded arms ride up with the collar during</text>')
A(f'<text x="{mx-60}" y="{H-20}" font-size="12">jack-up; the 3 arms balance each other, so the collar ring is not tilted.</text>')
A('</svg>')
open('torque-arm.svg', 'w').write('\n'.join(o))
