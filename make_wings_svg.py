# Generates wings.svg (rev 15: both wings lowered together; packs self-fold into landing trays). Run: python3 make_wings_svg.py
o = []
A = o.append
W, H = 1240, 760
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12.5">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker>'
  '<pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern></defs>')
A('<style>.s{stroke:#222;stroke-width:1.5}.hal{stroke:#555;stroke-width:1}.l{stroke:#555;stroke-width:1;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')
e, gy = 4.3, 600
TRAY = 1.5   # m, tray height


def panel(i, title, top):
    """top: height of the wing top bars (m)."""
    mid = 160 + i * 300
    X = lambda m: mid + m * e
    Z = lambda m: gy - m * e
    A(f'<text x="{mid}" y="40" text-anchor="middle" class="t">{title}</text>')
    A(f'<rect x="{mid-140}" y="{gy}" width="280" height="30" fill="url(#g)"/><line x1="{mid-140}" y1="{gy}" x2="{mid+140}" y2="{gy}" stroke="#222"/>')
    A(f'<rect x="{X(-6)}" y="{Z(1.3)}" width="{12*e}" height="{1.3*e}" fill="#9fb4c7" class="s"/>')
    A(f'<rect x="{X(0)-2}" y="{Z(105)}" width="4" height="{105*e}" fill="#888"/>')
    for c in (35, 62):
        A(f'<rect x="{X(0)-5}" y="{Z(c)-3}" width="10" height="6" fill="#4a9" class="s"/>')
    A(f'<rect x="{X(-17.5)}" y="{Z(100)-2}" width="{35*e}" height="4" fill="#e0a040" class="s"/>')
    for sx in (-1, 1):
        A(f'<line x1="{X(0)}" y1="{Z(105)}" x2="{X(sx*17)}" y2="{Z(100)}" stroke="#555"/>')
        xl, xr = sorted((X(sx * 2), X(sx * 17)))
        # landing tray
        A(f'<rect x="{xl-2}" y="{Z(TRAY)}" width="{xr-xl+4}" height="3" fill="#7d8790"/>')
        if top < 100:
            for xh in (X(sx * 2), X(sx * 17)):
                A(f'<line x1="{xh}" y1="{Z(100)}" x2="{xh}" y2="{Z(top)}" class="hal"/>')
        hang = min(30, top - TRAY - 1)                 # deployed length still hanging free
        folded = 30 - hang
        A(f'<rect x="{xl}" y="{Z(top)}" width="{xr-xl}" height="{hang*e}" fill="#2c4a7a"/>')
        for j in range(1, 8):
            xx = xl + j * (xr - xl) / 8
            A(f'<line x1="{xx}" y1="{Z(top)}" x2="{xx}" y2="{Z(top-hang)}" stroke="#7fa3d6"/>')
        if folded > 0:
            fh = max(3, folded / 30 * 0.7 * e * 4)     # stack height (drawn, exaggerated)
            A(f'<rect x="{xl}" y="{Z(TRAY)-fh}" width="{xr-xl}" height="{fh}" fill="#2c4a7a" opacity="0.6"/>')
        A(f'<rect x="{xl}" y="{Z(top)-2}" width="{xr-xl}" height="4" fill="#e0a040" class="s"/>')
    A(f'<text x="{mid}" y="{gy+50}" text-anchor="middle" font-size="12" fill="#2e7d32" font-weight="bold">Balanced (both wings together)</text>')


panel(0, '1. Operating', 100)
panel(1, '2. Lowering both wings', 22)
panel(2, '3. Down: swap packs', 3.2)
mid = 160
A(f'<path d="M{mid+17*e} {gy-100*e-6}L{mid+17*e+30} {gy-100*e-36}" class="l"/><text x="{mid+17*e+10}" y="{gy-100*e-40}" font-size="11">Permanent top yard</text>')
mid = 460
A(f'<path d="M{mid+12*e} {gy-12*e}L{mid+100} {gy-40*e}" class="l"/><text x="{mid+60}" y="{gy-40*e-6}" font-size="11">Packs land and fold</text><text x="{mid+60}" y="{gy-40*e+8}" font-size="11">themselves in the trays</text>')
A(f'<path d="M{mid-17*e} {gy-60*e}L{mid-100} {gy-70*e}" class="l"/><text x="{mid-100}" y="{gy-70*e-6}" font-size="11" text-anchor="end">Halyards</text>')
A(f'<path d="M{mid+8} {gy-90*e} V{gy-60*e}" stroke="#222" stroke-width="1.5" marker-end="url(#ar)"/>')
mid = 760
A(f'<path d="M{mid+10*e} {gy-3.2*e}L{mid+80} {gy-20*e}" class="l"/><text x="{mid+60}" y="{gy-20*e-6}" font-size="11">Hangers at working</text><text x="{mid+60}" y="{gy-20*e+8}" font-size="11">height (~1 m above tray)</text>')
A(f'<path d="M{mid-14*e} {gy-1.5*e}L{mid-90} {gy-14*e}" class="l"/><text x="{mid-92}" y="{gy-14*e}" font-size="11" text-anchor="end">Landing tray</text><text x="{mid-92}" y="{gy-14*e+13}" font-size="11" text-anchor="end">(deck height)</text>')

# ---------- 4. detail: one pack folding into its tray (side view)
dx, dy = 1080, 120
A(f'<text x="{dx}" y="40" text-anchor="middle" class="t">4. One pack, side view</text>')
A(f'<rect x="{dx-70}" y="{dy}" width="140" height="10" fill="#e0a040" class="s"/><text x="{dx}" y="{dy-8}" text-anchor="middle" font-size="11">top bar (lowering)</text>')
A(f'<rect x="{dx-12}" y="{dy+10}" width="24" height="10" fill="#4a9" class="s"/>')
y = dy + 20
for i in range(5):                                   # still hanging flat
    A(f'<line x1="{dx}" y1="{y+i*40+2}" x2="{dx}" y2="{y+(i+1)*40-2}" stroke="#2c4a7a" stroke-width="5" stroke-linecap="round"/>')
    A(f'<circle cx="{dx}" cy="{y+(i+1)*40}" r="2.5" fill="#222"/>')
yt = dy + 20 + 5 * 40
ytray = yt + 140
pts = []
n = 12
for i in range(n):                                   # folding zig-zag into the tray
    pts.append((dx + (0 if i % 2 == 0 else 46) - 23, yt + i * (ytray - yt - 8) / (n - 1)))
A(f'<polyline points="{dx},{yt} ' + ' '.join(f'{x:.0f},{yv:.0f}' for x, yv in pts) + '" fill="none" stroke="#2c4a7a" stroke-width="4" stroke-linejoin="round"/>')
A(f'<rect x="{dx-60}" y="{ytray}" width="120" height="8" fill="#7d8790" class="s"/><line x1="{dx-60}" y1="{ytray-24}" x2="{dx-60}" y2="{ytray}" stroke="#7d8790" stroke-width="3"/><line x1="{dx+60}" y1="{ytray-24}" x2="{dx+60}" y2="{ytray}" stroke="#7d8790" stroke-width="3"/>')
A(f'<path d="M{dx+90} {dy+40} V{dy+140}" stroke="#222" stroke-width="1.5" marker-end="url(#ar)"/>')
A(f'<text x="{dx+96}" y="{dy+95}" font-size="11">lowering</text>')
A(f'<path d="M{dx-34} {yt+20} L{dx-80} {yt-10}" class="l"/><text x="{dx-82}" y="{yt-14}" font-size="11" text-anchor="end">Alternate hinges sprung</text><text x="{dx-82}" y="{yt}" font-size="11" text-anchor="end">to fold the same way</text>')
A(f'<path d="M{dx+60} {ytray+4} L{dx+90} {ytray+30}" class="l"/><text x="{dx+20}" y="{ytray+44}" font-size="11">Tray with low side walls</text>')
A(f'<text x="{dx-110}" y="{ytray+80}" font-size="11.5">Raising reverses it: each panel</text>')
A(f'<text x="{dx-110}" y="{ytray+95}" font-size="11.5">unfolds as it lifts off the tray.</text>')
A(f'<text x="20" y="{H-38}" font-size="12.5">One winch drives all 4 halyards through linked drums, so both wings always lower, fold, lift and unfold together and the rig stays balanced.</text>')
A(f'<text x="20" y="{H-20}" font-size="12.5">No Roman-blind cords, carriers or per-pack hoists: the packs fold by landing. Down ~20 min, swap, up ~20 min.</text>')
A('</svg>')
open('wings.svg', 'w').write('\n'.join(o))
