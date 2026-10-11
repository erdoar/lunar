# Generates platform-layout.svg (rev 3: tall guyed rig). Run: python3 make_layout_svg.py
import math
o = []
A = o.append
W, H = 1180, 820
MAST, YT, YB, HALF = 105, 100, 70, 17          # m: mast top, yard heights, half array width
COLLARS, ANCH, RING = (22, 42, 62), 40, 6       # m: collar heights, anchor radius, ring radius
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="13">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker>'
  '<pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern></defs>')
A('<style>.s{stroke:#222;stroke-width:2}.l{stroke:#555;stroke-width:1;fill:none}.guy{stroke:#8e44ad;stroke-width:1.4}.c{stroke:#555;stroke-width:1.3}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:17px;font-weight:bold}</style>')


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*15:.0f}" text-anchor="{anchor}">{t}</text>')


# ---------- elevation (view along a line perpendicular to the 0° guy plane)
e, mid, gy = 6.2, 250, 760
X = lambda m: mid + m * e
Z = lambda m: gy - 6 - m * e
A('<text x="20" y="30" class="t">Elevation (guys shown in projection)</text>')
A(f'<rect x="10" y="{gy}" width="580" height="40" fill="url(#g)"/><line x1="10" y1="{gy}" x2="590" y2="{gy}" class="s"/>')
# base
A(f'<rect x="{X(-RING)}" y="{gy-12}" width="{2*RING*e}" height="8" fill="#9fb4c7" class="s"/>')
for R in (-RING, RING):
    A(f'<rect x="{X(R)-3}" y="{gy-5}" width="6" height="5" fill="#c0392b"/>')
# guys: plane at 0 deg projects to +40 m, the two at 120/240 deg overlap at -20 m
for c in COLLARS:
    for ax in (ANCH, -ANCH / 2):
        A(f'<line x1="{X(0)}" y1="{Z(c)}" x2="{X(ax)}" y2="{gy}" class="guy"/>')
    A(f'<rect x="{X(0)-9}" y="{Z(c)-4}" width="18" height="8" fill="#4a9" class="s"/>')
for ax in (ANCH, -ANCH / 2):
    A(f'<rect x="{X(ax)-7}" y="{gy-6}" width="14" height="6" fill="#555"/>')
# mast
A(f'<rect x="{X(0)-3}" y="{Z(MAST)}" width="6" height="{MAST*e}" fill="#888" stroke="#222"/>')
# diamond stays
A(f'<polyline points="{X(0)},{Z(MAST)} {X(-6)},{Z(81)} {X(0)},{Z(62)}" fill="none" class="c"/>')
A(f'<polyline points="{X(0)},{Z(MAST)} {X(6)},{Z(81)} {X(0)},{Z(62)}" fill="none" class="c"/>')
A(f'<line x1="{X(-6)}" y1="{Z(81)}" x2="{X(6)}" y2="{Z(81)}" stroke="#e0a040" stroke-width="3"/>')
# curtains
for i in range(8):
    x0 = -HALF + i * 4.25
    A(f'<rect x="{X(x0)+1}" y="{Z(YT)}" width="{4.25*e-2}" height="{(YT-YB)*e}" fill="#2c4a7a" opacity="0.92"/>')
for m in (YT, YB):
    A(f'<rect x="{X(-HALF)-3}" y="{Z(m)-3}" width="{2*HALF*e+6}" height="6" fill="#e0a040" class="s"/>')
for sx in (-1, 1):
    A(f'<line x1="{X(0)}" y1="{Z(MAST)}" x2="{X(sx*HALF)}" y2="{Z(YT)}" class="c"/>')
# one curtain being lowered (ghost)
A(f'<rect x="{X(-HALF)+1}" y="{Z(40)}" width="{4.25*e-2}" height="{30*e}" fill="none" stroke="#2c4a7a" stroke-dasharray="5 4"/>')
A(f'<path d="M{X(-HALF+2.1)} {Z(YB)+8}V{Z(42)}" class="l" marker-end="url(#ar)"/>')
# dims + labels
A(f'<path d="M{X(23)} {Z(YT)}V{gy}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{X(23)+5}" y="{Z(55)}">100 m</text>')
A(f'<path d="M{X(-HALF)} {Z(MAST)-10}H{X(HALF)}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{X(0)}" y="{Z(MAST)-16}" text-anchor="middle">34 m</text>')
lab(X(HALF), Z(85), X(26), Z(88), ['8 curtains, 34 x 30 m', '≈1,000 m², ~350 kWe'])
lab(X(6), Z(81), X(26), Z(76), ['Diamond stays (rotate)'])
for c in COLLARS:
    lab(X(0) + 9, Z(c), X(8), Z(c) - 14, [f'Collar {c} m'])
lab(X(30), Z(18), X(31), Z(30), ['Stationary guys', '(6 mm steel rope)'])
lab(X(ANCH), gy - 3, X(33), gy - 40, ['Anchor, 40 m'])
lab(X(-HALF + 2), Z(30), X(-24), Z(24), ['Curtain lowered', 'for repair'], 'end')
lab(X(RING), gy - 8, X(14), gy - 28, ['Ø12 m ring: bogies,', 'drive, slip ring'])
hx = X(-9)
A(f'<line x1="{hx}" y1="{gy-12}" x2="{hx}" y2="{gy}" stroke="#222" stroke-width="2"/><text x="{hx-4}" y="{gy-4}" font-size="11" text-anchor="end">2 m person</text>')
A(f'<line x1="{X(-26)}" y1="{Z(52)}" x2="{X(-3)}" y2="{Z(52)}" stroke="#f5b700" stroke-width="3" stroke-dasharray="7 4" marker-end="url(#ar)"/>'
  f'<circle cx="{X(-30)}" cy="{Z(52)}" r="11" fill="#f5b700" class="s"/><text x="{X(-36)}" y="{Z(52)-18}" font-size="12">Sun ~0–1.5°</text>')

# ---------- plan
k, cx, cy = 5.2, 880, 360
A(f'<text x="{cx-280}" y="30" class="t">Plan (from above)</text>')
A(f'<circle cx="{cx}" cy="{cy}" r="{HALF*k}" fill="#eef3fa" stroke="#2c4a7a" stroke-dasharray="6 4"/>')
for d in (0, 120, 240):
    a = math.radians(d - 90)
    ax, ay = cx + ANCH * k * math.cos(a), cy + ANCH * k * math.sin(a)
    A(f'<line x1="{cx}" y1="{cy}" x2="{ax:.1f}" y2="{ay:.1f}" class="guy"/>')
    A(f'<rect x="{ax-8:.1f}" y="{ay-8:.1f}" width="16" height="16" fill="#555"/>')
    A(f'<text x="{ax+(14 if d!=240 else -14):.1f}" y="{ay+(-8 if d==0 else 22):.1f}" text-anchor="{"start" if d!=240 else "end"}">Anchor {d}°</text>')
A(f'<circle cx="{cx}" cy="{cy}" r="{RING*k}" fill="none" stroke="#c0392b" stroke-width="3"/>')
# array at maintenance azimuth 30/210 (measured like the guys, clockwise from up)
for d, style in ((30, 'stroke="#2c4a7a" stroke-width="6"'), (75, 'stroke="#2c4a7a" stroke-width="3" opacity="0.35"')):
    a = math.radians(d - 90)
    A(f'<line x1="{cx-HALF*k*math.cos(a):.1f}" y1="{cy-HALF*k*math.sin(a):.1f}" x2="{cx+HALF*k*math.cos(a):.1f}" y2="{cy+HALF*k*math.sin(a):.1f}" {style}/>')
A(f'<circle cx="{cx}" cy="{cy}" r="5" fill="#fff" class="s"/>')
a = math.radians(30 - 90)
lab(cx + HALF * k * math.cos(a), cy + HALF * k * math.sin(a), cx + 120, cy - 150, ['Array parked at maintenance', 'azimuth (30°/210°): curtains', 'drop between guy planes'])
a = math.radians(75 - 90)
lab(cx + 0.8 * HALF * k * math.cos(a), cy + 0.8 * HALF * k * math.sin(a), cx + 140, cy + 60, ['Array while tracking', '(any angle above 67 m:', 'clears all guys)'])
lab(cx - HALF * k * 0.7, cy + HALF * k * 0.7, cx - 150, cy + 150, ['Array sweep, r = 17 m', '(only at 67–100 m)'], 'end')
lab(cx, cy + RING * k, cx + 10, cy + 110, ['Ø12 m ring'])
A(f'<path d="M{cx} {cy+ANCH*k*0.5+40}H{cx+ANCH*k}" class="l" marker-start="url(#ar)" marker-end="url(#ar)" visibility="hidden"/>')
# legend + shading note
L = 640
A(f'<line x1="{cx-270}" y1="{L}" x2="{cx-245}" y2="{L}" class="guy"/><text x="{cx-238}" y="{L+4}">Stationary guy</text>')
A(f'<rect x="{cx-270}" y="{L+14}" width="22" height="8" fill="#4a9" class="s"/><text x="{cx-238}" y="{L+23}">Roller collar (mast turns inside)</text>')
A(f'<line x1="{cx-270}" y1="{L+38}" x2="{cx-245}" y2="{L+38}" stroke="#2c4a7a" stroke-width="5"/><text x="{cx-238}" y="{L+42}">Solar curtains</text>')
A(f'<text x="{cx-270}" y="{L+72}" font-size="12">Neighbouring rigs: ≥10x array width apart, in a line along the</text>')
A(f'<text x="{cx-270}" y="{L+88}" font-size="12">ridge, heights staggered (≈1–2% loss per neighbour).</text>')
A('</svg>')
open('platform-layout.svg', 'w').write('\n'.join(o))
