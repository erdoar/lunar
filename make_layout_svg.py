# Generates platform-layout.svg (rev 2: compact ring, cable-stayed rig). Run: python3 make_layout_svg.py
import math
o = []
A = o.append
W, H = 1245, 760
RING, MAST, YT, YB, SPAN, SPR = 6, 45, 40, 15, 40, 8  # metres
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="13">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker>'
  '<pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern></defs>')
A('<style>.s{stroke:#222;stroke-width:2}.l{stroke:#555;stroke-width:1;fill:none}.c{stroke:#555;stroke-width:1.3}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:17px;font-weight:bold}</style>')
gy = 680


def ground(x0, x1):
    A(f'<rect x="{x0}" y="{gy}" width="{x1-x0}" height="40" fill="url(#g)"/><line x1="{x0}" y1="{gy}" x2="{x1}" y2="{gy}" class="s"/>')


def base(mid, e):
    for R in (-RING, RING):
        x = mid + R * e
        A(f'<rect x="{x-3}" y="{gy-9}" width="6" height="9" fill="#ccc" class="s"/><rect x="{x-5}" y="{gy-13}" width="10" height="4" fill="#c0392b"/>'
          f'<rect x="{x-6}" y="{gy-22}" width="12" height="9" fill="#e0a040" class="s"/>')
    A(f'<rect x="{mid-RING*e}" y="{gy-34}" width="{2*RING*e}" height="12" fill="#9fb4c7" class="s"/>')
    A(f'<rect x="{mid-5}" y="{gy-22}" width="10" height="22" fill="#fff" class="s"/>')
    return gy - 34


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*15:.0f}" text-anchor="{anchor}">{t}</text>')


# ---- front elevation (facing the blanket)
e, mid = 12.4, 320
A('<text x="30" y="30" class="t">Front elevation (facing the Sun)</text>')
ground(20, 590)
dt = base(mid, e)
z = lambda m: dt - m * e
A(f'<rect x="{mid-4}" y="{z(MAST)}" width="8" height="{MAST*e}" fill="#888" class="s"/>')
A(f'<rect x="{mid-SPAN/2*e}" y="{z(YT)}" width="{SPAN*e}" height="{(YT-YB)*e}" fill="#2c4a7a" stroke="#222"/>')
for i in range(1, 10):
    x = mid - SPAN / 2 * e + i * SPAN * e / 10
    A(f'<line x1="{x}" y1="{z(YT)}" x2="{x}" y2="{z(YB)}" stroke="#7fa3d6"/>')
for m in (YT, YB):
    A(f'<rect x="{mid-SPAN/2*e-4}" y="{z(m)-4}" width="{SPAN*e+8}" height="8" fill="#e0a040" class="s"/>')
for sx in (-1, 1):
    for f in (0.5, 1):
        A(f'<line x1="{mid}" y1="{z(MAST)}" x2="{mid+sx*SPAN/2*e*f}" y2="{z(YT)}" class="c"/>')
A(f'<path d="M{mid-SPAN/2*e} {z(MAST)-14}H{mid+SPAN/2*e}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{mid}" y="{z(MAST)-20}" text-anchor="middle">40 m blanket span</text>')
A(f'<path d="M{mid+SPAN/2*e+12} {z(YT)}V{z(YB)}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{mid+SPAN/2*e+16}" y="{z((YT+YB)/2)}" text-anchor="start">25 m</text>')
A(f'<path d="M{mid-SPAN/2*e-12} {z(MAST)}V{dt}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{mid-SPAN/2*e-16}" y="{z(MAST/2)+50}" text-anchor="end">45 m</text>')
lab(mid + 120, z(MAST) + 15, mid + 165, z(MAST) + 38, ['Topping lifts'])
lab(mid + 200, z(YT), mid + 215, z(YT) + 30, ['Top yard'])
A(f'<text x="{mid-150}" y="{z(30)}" fill="#fff" style="stroke:none" font-size="15">Solar blanket, 1,000 m²</text>')
lab(mid - 200, z(YB), mid - 185, z(YB) + 30, ['Bottom yard (tension)'])
lab(mid + 4, z(8), mid + 60, z(8) - 10, ['Mast, built by jack-up'])
lab(mid + RING * e, dt + 5, mid + 120, dt - 40, ['Ø12 m ring'])
A(f'<path d="M{mid-RING*e} {gy+20}H{mid+RING*e}" stroke="#222" marker-start="url(#ar)" marker-end="url(#ar)"/>')
hx = mid + 170
A(f'<circle cx="{hx}" cy="{gy-21}" r="2.6" fill="#222"/><line x1="{hx}" y1="{gy-18}" x2="{hx}" y2="{gy-8}" stroke="#222" stroke-width="1.6"/><path d="M{hx-4} {gy}L{hx} {gy-8}L{hx+4} {gy}" stroke="#222" fill="none" stroke-width="1.6"/>')
A(f'<text x="{hx+8}" y="{gy-6}" font-size="11">2 m person</text>')

# ---- side elevation (edge-on to blanket): spreaders + stays
e2, mid2 = 12.4, 760
A(f'<text x="{mid2-110}" y="30" class="t">Side elevation</text>')
ground(mid2 - 125, mid2 + 125)
dt2 = base(mid2, e2)
z2 = lambda m: dt2 - m * e2
A(f'<rect x="{mid2-4}" y="{z2(MAST)}" width="8" height="{MAST*e2}" fill="#888" class="s"/>')
A(f'<rect x="{mid2-2}" y="{z2(YT)}" width="4" height="{(YT-YB)*e2}" fill="#2c4a7a"/>')
for h in (15, 30):
    A(f'<line x1="{mid2-SPR*e2}" y1="{z2(h)}" x2="{mid2+SPR*e2}" y2="{z2(h)}" stroke="#e0a040" stroke-width="5"/>')
for sx in (-1, 1):
    A(f'<polyline points="{mid2},{z2(MAST)} {mid2+sx*SPR*e2},{z2(30)} {mid2+sx*SPR*e2},{z2(15)} {mid2+sx*RING*e2},{dt2}" fill="none" class="c"/>')
    A(f'<line x1="{mid2}" y1="{z2(MAST)}" x2="{mid2+sx*SPR*e2}" y2="{z2(30)}" class="c"/>')
lab(mid2 + SPR * e2, z2(30), mid2 + 60, z2(36), ['Spreader ±8 m'])
lab(mid2 + 50, z2(37), mid2 + 40, z2(42), ['Stays'])
lab(mid2 + RING * e2 - 4, dt2 - 4, mid2 + 95, z2(6), ['Spring tensioner', '+ load cell'])
A(f'<circle cx="{mid2-110}" cy="{z2(27)}" r="12" fill="#f5b700" class="s"/><path d="M{mid2-95} {z2(27)}H{mid2-20}" stroke="#f5b700" stroke-width="3" stroke-dasharray="7 4" marker-end="url(#ar)"/>')
A(f'<text x="{mid2-118}" y="{z2(27)+30}" font-size="12">Sun ~0–1.5°</text>')

# ---- plan
k, cx, cy = 8.5, 1040, 300
A(f'<text x="{cx-150}" y="30" class="t">Plan (from above)</text>')
r = RING * k
A(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#c0392b" stroke-width="4"/>')
for i in range(12):
    a = 2 * math.pi * i / 12
    A(f'<line x1="{cx+(r-5)*math.cos(a):.1f}" y1="{cy+(r-5)*math.sin(a):.1f}" x2="{cx+(r+5)*math.cos(a):.1f}" y2="{cy+(r+5)*math.sin(a):.1f}" stroke="#222"/>')
for i in range(8):
    d = i * 45 + 22.5
    col = '#4a9' if i in (0, 4) else '#e0a040'
    A(f'<rect x="-5" y="-8" width="10" height="16" rx="2" fill="{col}" class="s" transform="translate({cx+r*math.cos(math.radians(d)):.1f},{cy+r*math.sin(math.radians(d)):.1f}) rotate({d})"/>')
A(f'<rect x="{cx-SPAN/2*k}" y="{cy-3}" width="{SPAN*k}" height="6" fill="#2c4a7a" class="s"/>')
A(f'<line x1="{cx}" y1="{cy-SPR*k}" x2="{cx}" y2="{cy+SPR*k}" stroke="#e0a040" stroke-width="4"/>')
A(f'<circle cx="{cx}" cy="{cy}" r="6" fill="#fff" class="s"/>')
A(f'<circle cx="{cx}" cy="{cy+150}" r="11" fill="#f5b700" class="s"/><path d="M{cx} {cy+136}V{cy+SPR*k+6}" stroke="#f5b700" stroke-width="3" stroke-dasharray="7 4" marker-end="url(#ar)"/>')
rr = 95
A(f'<path d="M{cx+rr*math.cos(math.radians(-70)):.0f} {cy+rr*math.sin(math.radians(-70)):.0f} A{rr} {rr} 0 0 1 {cx+rr*math.cos(math.radians(-25)):.0f} {cy+rr*math.sin(math.radians(-25)):.0f}" fill="none" stroke="#222" stroke-width="1.6" marker-end="url(#ar)"/>')
A(f'<text x="{cx+30}" y="{cy-100}" font-size="12">1 rev / 29.5 days</text>')
lab(cx + 150, cy + 3, cx + 165, cy + 30, ['Blanket plane'], 'end')
lab(cx + r * 0.7, cy + r * 0.7, cx + 70, cy + 75, ['Ø12 m rail', '12 x π m segments'])
lab(cx + 3, cy + SPR * k, cx - 60, cy + 95, ['Spreaders'], 'end')
L = H - 22
A(f'<rect x="{cx-160}" y="{cy+190}" width="12" height="12" fill="#e0a040" class="s"/><text x="{cx-142}" y="{cy+201}">Load bogie (6)</text>')
A(f'<rect x="{cx-160}" y="{cy+212}" width="12" height="12" fill="#4a9" class="s"/><text x="{cx-142}" y="{cy+223}">Drive bogie (2)</text>')
A(f'<text x="{cx-150}" y="{cy+345}" font-size="12">No wind + 1/6 g: a 40 m wide</text>')
A(f'<text x="{cx-150}" y="{cy+361}" font-size="12">tension rig on a 12 m ring.</text>')
A(f'<text x="{cx-150}" y="{cy+377}" font-size="12">Balanced: CoM on the axis.</text>')
A('</svg>')
open('platform-layout.svg', 'w').write('\n'.join(o))
