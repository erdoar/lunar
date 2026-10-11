# Generates torque-arm.svg (rev 14: V-link torque lever on the upper collar). Run: python3 make_torque_arm_svg.py
import math
o = []
A = o.append
W, H = 1240, 640
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="13">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:2}.l{stroke:#555;stroke-width:1;fill:none}.cab{stroke:#8e44ad;stroke-width:2.5}'
  '.collar{fill:#4a9}.mast{fill:#888}.v{fill:#c87f0a;stroke:#222;stroke-width:1.5}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:16px;font-weight:bold}</style>')


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*15:.0f}" text-anchor="{anchor}">{t}</text>')


# ---------------- 1. plan: collar, V-link, cable; twisted state
k, cx, cy = 70, 140, 300          # px per metre
A('<text x="20" y="32" class="t">1. Plan: how the V-link resists twist</text>')
A(f'<circle cx="{cx}" cy="{cy}" r="{1.45*k}" fill="none" stroke="#4a9" stroke-width="12"/>')
A(f'<circle cx="{cx}" cy="{cy}" r="{0.95*k}" fill="none" stroke="#7d8790" stroke-width="7"/>')
pts = [(cx + 0.81 * k * math.cos(math.radians(a)), cy + 0.81 * k * math.sin(math.radians(a))) for a in (0, 120, 240)]
A('<polygon points="' + ' '.join(f'{x:.1f},{y:.1f}' for x, y in pts) + '" fill="none" stroke="#888" stroke-width="4"/>')
P = lambda r, t: (cx + r * k, cy - t * k)
foot = (560, cy)
for twist, sty in ((0, 'class="cab"'), (6, 'stroke="#8e44ad" stroke-width="1.5" stroke-dasharray="6 4"')):
    th = math.radians(twist)
    R = lambda r, t: (cx + (r * math.cos(th) + t * math.sin(th)) * k, cy - (-r * math.sin(th) + t * math.cos(th)) * k)
    p1, p2, ap = R(1.45, 0.2), R(1.45, -0.2), R(1.45 + 0.42, 0)   # V seen from above: ~0.42 m horizontal reach when aligned
    if twist == 0:
        A(f'<polygon points="{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} {ap[0]:.1f},{ap[1]:.1f}" class="v"/>')
    else:
        A(f'<polygon points="{p1[0]:.1f},{p1[1]:.1f} {p2[0]:.1f},{p2[1]:.1f} {ap[0]:.1f},{ap[1]:.1f}" fill="none" stroke="#c87f0a" stroke-width="1.5" stroke-dasharray="4 3"/>')
    A(f'<line x1="{ap[0]:.1f}" y1="{ap[1]:.1f}" x2="{foot[0]}" y2="{foot[1]}" {sty}/>')
A(f'<rect x="{foot[0]-10}" y="{foot[1]-10}" width="20" height="20" fill="#555"/>')
r = 1.9 * k
A(f'<path d="M{cx+r*math.cos(math.radians(-40)):.0f} {cy+r*math.sin(math.radians(-40)):.0f} A{r} {r} 0 0 0 {cx+r*math.cos(math.radians(-80)):.0f} {cy+r*math.sin(math.radians(-80)):.0f}" fill="none" stroke="#222" stroke-width="1.6" marker-end="url(#ar)"/>')
A(f'<text x="{cx+20}" y="{cy-140}" font-size="12">friction drag</text>')
A(f'<path d="M{P(1.87,0.45)[0]:.0f} {P(1.87,0.45)[1]:.0f} v34" stroke="#c0392b" stroke-width="2.5" marker-end="url(#ar)"/>')
A(f'<text x="{P(1.87,0.45)[0]+8:.0f}" y="{P(1.87,0.45)[1]+8:.0f}" font-size="12" fill="#c0392b">cable pulls it back</text>')
lab(foot[0], foot[1] + 10, foot[0] - 10, foot[1] + 60, ['To foot, 30 m out:', 'one stay cable'], 'end')
lab(P(1.6, 0.15)[0], P(1.6, 0.15)[1], cx + 40, cy + 150, ['V-link on 2 close pins', '(load pins = torque sensor)'])
lab(cx, cy + 1.45 * k, cx - 10, cy + 200, ['Upper collar (stationary)'])
A(f'<text x="20" y="{H-90}" font-size="12">Dashed: collar after a small twist (exaggerated). The tensioned cable pulls the</text>')
A(f'<text x="20" y="{H-74}" font-size="12">apex back; the V turns that sideways pull into a couple on its two pins.</text>')
A(f'<text x="20" y="{H-58}" font-size="12">~3.8 kN·m/rad at 1.5 kN (0.15° at normal friction); interlock stops the drive at</text>')
A(f'<text x="20" y="{H-42}" font-size="12">~200 N·m collar torque (≤3° twist).</text>')

# ---------------- 2. elevation: hinged V aligned with the cable; slack = hangs straight down
e, mx, hy = 120, 690, 210          # px per metre, mast centre x, pin height (62 m)
A(f'<text x="{mx-110}" y="32" class="t">2. Elevation</text>')
A(f'<rect x="{mx-30}" y="60" width="60" height="420" class="mast s"/>')
A(f'<rect x="{mx+30}" y="{hy-0.3*e}" width="{0.45*e}" height="{0.55*e}" class="collar s"/>')
A(f'<rect x="{mx-30-0.45*e}" y="{hy-0.3*e}" width="{0.45*e}" height="{0.55*e}" class="collar s"/>')
px_ = mx + 30 + 0.45 * e + 6
beta = math.atan2(62, 30 - 1.45)
ax_, ay_ = px_ + 1.0 * e * math.cos(beta), hy + 1.0 * e * math.sin(beta)
A(f'<line x1="{px_}" y1="{hy}" x2="{ax_:.0f}" y2="{ay_:.0f}" stroke="#c87f0a" stroke-width="9" stroke-linecap="round"/>')
A(f'<circle cx="{px_}" cy="{hy}" r="7" fill="#fff" class="s"/><circle cx="{ax_:.0f}" cy="{ay_:.0f}" r="7" fill="none" stroke="#222" stroke-width="2.5"/>')
A(f'<line x1="{ax_:.0f}" y1="{ay_:.0f}" x2="{ax_+ (480-ay_)/math.tan(beta):.0f}" y2="480" class="cab"/>')
A(f'<line x1="{px_}" y1="{hy}" x2="{px_}" y2="{hy+1.0*e}" stroke="#c87f0a" stroke-width="4" stroke-dasharray="6 4"/>')
A(f'<circle cx="{px_}" cy="{hy+1.0*e}" r="6" fill="none" stroke="#222" stroke-dasharray="3 2"/>')
lab(px_ + 6, hy - 4, px_ + 40, hy - 60, ['2 close pins (end-on),', 'free to hinge'])
lab((px_ + ax_) / 2 + 6, (hy + ay_) / 2, px_ + 90, hy + 30, ['Tensioned: lines up', 'with the cable'])
lab(px_ - 4, hy + 0.7 * e, px_ - 70, hy + 1.6 * e, ['Slack: hangs straight', 'down under gravity'], 'end')
lab(ax_ + 6, ay_, ax_ + 40, ay_ + 20, ['Shackle, 1 m', 'from the pins'])
lab(ax_ + 50, ay_ + 100, ax_ + 80, 440, ['Stay cable to', 'foot (~64°)'])
lab(mx + 30, hy - 0.3 * e + 4, mx + 60, 80, ['Upper collar, 62 m'])
A(f'<text x="{mx}" y="76" text-anchor="middle" font-size="11" style="stroke:none" fill="#fff">mast</text>')

# ---------------- 3. the part
fx, fy = 1140, 120
A(f'<text x="{fx-110}" y="32" class="t">3. The part</text>')
A(f'<path d="M{fx-48} {fy} L{fx+48} {fy} L{fx+10} {fy+190} L{fx-10} {fy+190} Z" class="v"/>')
A(f'<path d="M{fx-28} {fy+14} L{fx+28} {fy+14} L{fx} {fy+150} Z" fill="#fff" stroke="#222" stroke-width="1"/>')
for x in (fx - 40, fx + 40):
    A(f'<circle cx="{x}" cy="{fy+8}" r="6" fill="#fff" stroke="#222" stroke-width="1.5"/>')
A(f'<circle cx="{fx}" cy="{fy+175}" r="8" fill="#fff" stroke="#222" stroke-width="1.5"/>')
A(f'<path d="M{fx-40} {fy-18} H{fx+40}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{fx}" y="{fy-24}" text-anchor="middle" font-size="12">0.4 m</text>')
A(f'<path d="M{fx+70} {fy+8} V{fy+175}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{fx+76}" y="{fy+95}" font-size="12">1 m</text>')
lab(fx - 46, fy + 8, fx - 90, fy + 50, ['2 pin holes', '(collar lugs)'], 'end')
lab(fx - 8, fy + 175, fx - 70, fy + 215, ['1 shackle hole', '(stay cable)'], 'end')
A(f'<text x="{fx-90}" y="{fy+260}" font-size="12">Flat Ti plate, ~8 mm, ~2 kg.</text>')
A(f'<text x="{fx-90}" y="{fy+276}" font-size="12">Tension only (1.5–3 kN).</text>')
A(f'<text x="{fx-90}" y="{fy+292}" font-size="12">Fitted and shackled at deck</text>')
A(f'<text x="{fx-90}" y="{fy+308}" font-size="12">level before jack-up.</text>')
A('</svg>')
open('torque-arm.svg', 'w').write('\n'.join(o))
