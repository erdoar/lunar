# Generates wings.svg (rev 8: port/starboard wings on halyards, lowering stages and balance). Run: python3 make_wings_svg.py
o = []
A = o.append
W, H = 1240, 740
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="13">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker>'
  '<marker id="rr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10z" fill="#c0392b"/></marker>'
  '<pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern></defs>')
A('<style>.s{stroke:#222;stroke-width:1.5}.hal{stroke:#555;stroke-width:1}.l{stroke:#555;stroke-width:1;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')
e, gy = 4.3, 600
STAGES = [
    ('1. Both wings up (operating)', 'up', 'up', None),
    ('2. Port packs retracted', 'rolled', 'up', None),
    ('3. Port lowered to 3 m', 'low', 'up', None),
    ('4a. Port off: ballast on', 'ballast', 'up', None),
]


def panel(i, title, port, stbd):
    mid = 160 + i * 300
    X = lambda m: mid + m * e
    Z = lambda m: gy - m * e
    A(f'<text x="{mid}" y="40" text-anchor="middle" class="t">{title}</text>')
    A(f'<rect x="{mid-140}" y="{gy}" width="280" height="30" fill="url(#g)"/><line x1="{mid-140}" y1="{gy}" x2="{mid+140}" y2="{gy}" stroke="#222"/>')
    A(f'<rect x="{X(-6)}" y="{Z(1.3)}" width="{12*e}" height="{1.3*e}" fill="#9fb4c7" class="s"/>')
    A(f'<rect x="{X(0)-2}" y="{Z(105)}" width="4" height="{105*e}" fill="#888"/>')
    for c in (35, 62):
        A(f'<rect x="{X(0)-5}" y="{Z(c)-3}" width="10" height="6" fill="#4a9" class="s"/>')
    A(f'<line x1="{X(0)}" y1="{Z(62)}" x2="{X(8)}" y2="{Z(62)}" stroke="#c87f0a" stroke-width="2.5"/>')
    # permanent top yard + topping lifts
    A(f'<rect x="{X(-17.5)}" y="{Z(100)-2}" width="{35*e}" height="4" fill="#e0a040" class="s"/>')
    for sx in (-1, 1):
        A(f'<line x1="{X(0)}" y1="{Z(105)}" x2="{X(sx*17)}" y2="{Z(100)}" stroke="#555"/>')
    for side, state in ((-1, port), (1, stbd)):
        x_in, x_out = X(side * 2), X(side * 17)
        xl, xr = min(x_in, x_out), max(x_in, x_out)
        if state == 'up':
            A(f'<rect x="{xl}" y="{Z(100)}" width="{xr-xl}" height="{30*e}" fill="#2c4a7a"/>')
            for j in range(1, 4):
                xx = xl + j * (xr - xl) / 4
                A(f'<line x1="{xx}" y1="{Z(100)}" x2="{xx}" y2="{Z(70)}" stroke="#7fa3d6"/>')
            A(f'<rect x="{xl}" y="{Z(70)-2}" width="{xr-xl}" height="4" fill="#e0a040"/>')
        elif state == 'rolled':
            A(f'<rect x="{xl}" y="{Z(100)}" width="{xr-xl}" height="7" fill="#2c4a7a" class="s"/>')
        else:
            zb = 3
            for xh in (x_in, x_out):
                A(f'<line x1="{xh}" y1="{Z(100)}" x2="{xh}" y2="{Z(zb)}" class="hal"/>')
            if state == 'low':
                A(f'<rect x="{xl}" y="{Z(zb)}" width="{xr-xl}" height="7" fill="#2c4a7a" class="s"/>')
            else:
                A(f'<rect x="{xl+8}" y="{Z(zb)}" width="{xr-xl-16}" height="{2*e}" fill="#8d6e4a" class="s"/>')
                A(f'<text x="{(xl+xr)/2}" y="{Z(zb)-6}" text-anchor="middle" font-size="11">ballast 0.75 t</text>')
        # equal sheave loads
        for xh in (x_in, x_out):
            A(f'<path d="M{xh} {Z(100)-26}V{Z(100)-4}" stroke="#c0392b" stroke-width="2.5" marker-end="url(#rr)"/>')
    A(f'<text x="{mid}" y="{gy+50}" text-anchor="middle" font-size="12" fill="#2e7d32" font-weight="bold">Balanced</text>')


for i, (t, p, s_, _) in enumerate(STAGES):
    panel(i, t, p, s_)
# annotations on panel 1 and 3
mid = 160
A(f'<path d="M{mid+17*e} {gy-100*e-20}L{mid+17*e+30} {gy-100*e-50}" class="l"/><text x="{mid+17*e+10}" y="{gy-100*e-54}" font-size="11">Permanent top yard</text>')
A(f'<text x="{mid-80}" y="{gy-85*e}" font-size="12" text-anchor="end">Port</text><text x="{mid+80}" y="{gy-85*e}" font-size="12" text-anchor="start">Stbd</text>')
mid3 = 160 + 2 * 300
A(f'<path d="M{mid3-2*e} {gy-50*e}L{mid3-55} {gy-45*e}" class="l"/><text x="{mid3-57}" y="{gy-45*e+4}" font-size="11" text-anchor="end">Halyards</text>')
A(f'<path d="M{mid3-60} {gy-3*e}L{mid3-110} {gy-14*e}" class="l"/><text x="{mid3-112}" y="{gy-14*e}" font-size="11" text-anchor="end">Bundle 3 m up:</text><text x="{mid3-112}" y="{gy-14*e+13}" font-size="11" text-anchor="end">work at ground</text>')
A(f'<text x="20" y="{H-38}" font-size="12.5">Red arrows: the load on the 4 top-yard sheaves. It stays the same in every stage, so the rig stays balanced whichever height a wing is at.</text>')
A(f'<text x="20" y="{H-20}" font-size="12.5">4b (alternative): engage the winch cross-connect clutch and land or hoist both wings together. One wing landed with no ballast would put ~11 kN·m on the mast top.</text>')
A('</svg>')
open('wings.svg', 'w').write('\n'.join(o))
