# Generates power-cabling.svg (rev 28): one-line diagram, slip-ring section, mast cable trays, hanger connector interlock.
# Run: python3 make_power_cabling_svg.py
from math import sqrt

o = []
A = o.append
W, H = 1300, 1010
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:1.3}.l{stroke:#555;stroke-width:1;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}.k{font-size:11px}</style>')
ROT, FIX, HV, FEED, FIB, SR = '#e67e22', '#7d8790', '#c0392b', '#2e7d32', '#1f6fb2', '#bfa6d9'


def box(x, y, w, h, lines, fill='#f4f6f8', bold=False, fs=11):
    A(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" class="s"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x+w/2}" y="{y+16+j*14}" text-anchor="middle" font-size="{fs}"'
          f'{" font-weight=\"bold\"" if bold and j == 0 else ""} style="stroke:none">{t}</text>')


def hv(x1, y1, x2, y2, w=4, dash=None, col=HV, arrow=False):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    m = ' marker-end="url(#ar)"' if arrow else ''
    A(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" stroke-width="{w}"{d}{m}/>')


# ================= A. one-line diagram =================
A('<text x="20" y="28" class="t">A. One-line diagram (±500 V DC bipolar; both wings shown, 8 packs each)</text>')
bands = [(20, 210, 'Pack head (x16)', '#fdf2e9'), (210, 420, 'Top yard, 100 m', '#fef9e7'), (420, 585, 'Mast, 105 m', '#f4f6f6'),
         (585, 870, 'Rotating base frame', '#fdf2e9'), (870, 1010, 'Slip ring', '#f5eef8'), (1010, 1280, 'Fixed foundation', '#eaf2f8')]
for x0, x1, t, c in bands:
    A(f'<rect x="{x0}" y="42" width="{x1-x0}" height="380" fill="{c}" stroke="#ddd"/>')
    A(f'<text x="{(x0+x1)/2}" y="60" text-anchor="middle" font-weight="bold" font-size="12">{t}</text>')
for row, (y, wing) in enumerate(((110, 'Port'), (250, 'Starboard'))):
    box(30, y, 120, 58, [f'{wing} pack', 'cells → MPPT', '+ isolated boost'], fill='#fff')
    A(f'<text x="155" y="{y+12}" font-size="10" fill="#555">x8</text>')
    hv(150, y + 29, 230, y + 29)
    A(f'<rect x="168" y="{y+19}" width="18" height="20" fill="#fff" class="s"/><text x="177" y="{y+33}" text-anchor="middle" font-size="9" style="stroke:none">P</text>')
    box(230, y + 12, 60, 34, ['e-fuse', '40 A'], fill='#fff', fs=10)
    hv(290, y + 29, 330, y + 29, w=6)
    box(330, y + 4, 80, 50, ['Root box', 'SSB + surge'], fill='#fff', fs=10)
    hv(410, y + 29, 600, y + 29, w=6)
    A(f'<text x="500" y="{y+22}" text-anchor="middle" font-size="10.5">trunk {wing[0]}: 95 mm² Al ±</text>')
    A(f'<text x="500" y="{y+48}" text-anchor="middle" font-size="10.5">105 m, 175 A, ~1.9 kW loss</text>')
A('<text x="240" y="196" font-size="10.5">yard bus: 50 mm² Al ±, ≤182 A</text>')
box(600, 92, 255, 230, ['Base power cabinet'], fill='#fff', bold=True)
box(612, 118, 110, 40, ['Trunk breakers', '+ insulation mon.'], fs=10)
box(612, 260, 110, 40, ['Trunk breakers', '+ insulation mon.'], fs=10)
hv(722, 138, 740, 138, w=6); hv(722, 280, 740, 280, w=6)
hv(740, 138, 740, 280, w=6)
hv(740, 209, 870, 209, w=8)
box(760, 118, 90, 30, ['Bot chargers'], fs=10)
hv(740, 133, 760, 133, w=2, col='#555')
box(760, 232, 90, 34, ['Battery DC/DC', '10 kW, 2-way'], fs=10)
hv(740, 249, 760, 249, w=2, col='#555')
box(612, 175, 110, 34, ['Feeder conv.', '120 V'], fs=10)
hv(722, 192, 740, 192, w=2, col='#555')
box(760, 340, 90, 40, ['Battery', '~20 kWh'], fill='#fff', fs=10)
hv(805, 266, 805, 340, w=2, col='#555')
A(f'<path d="M612 192 H440 V96 H372 V110" stroke="{FEED}" stroke-width="2" fill="none" stroke-dasharray="6 3" marker-end="url(#ar)"/>')
A(f'<text x="445" y="90" font-size="10.5" fill="{FEED}">service feeder 120 V → reel sockets, garage</text>')
A(f'<path d="M590 400 H300 V400" stroke="{FIB}" stroke-width="2" stroke-dasharray="2 3" fill="none"/><text x="300" y="414" font-size="10.5" fill="{FIB}">2 fibres (data), same trays</text>')
for j, (t, c) in enumerate((('+500', HV), ('−500', HV), ('PE', '#2e7d32'), ('spare', '#999'))):
    A(f'<rect x="900" y="{150+j*24}" width="80" height="14" fill="{c}" opacity="0.8" class="s"/><text x="940" y="{161+j*24}" text-anchor="middle" font-size="10" fill="#fff" style="stroke:none">{t}</text>')
A('<text x="940" y="262" text-anchor="middle" font-size="10">+ 2 signal rings</text>')
A('<text x="940" y="276" text-anchor="middle" font-size="10">+ 60 GHz data coupler</text>')
A('<text x="940" y="300" text-anchor="middle" font-size="10">~0.25 kW loss</text>')
hv(985, 209, 1025, 209, w=8)
box(1025, 92, 245, 230, ['Base switchgear'], fill='#fff', bold=True)
box(1037, 118, 100, 34, ['Solid-state', 'breaker'], fs=10)
box(1037, 162, 100, 34, ['Isolator', '(zero current)'], fs=10)
box(1150, 118, 108, 34, ['Surge arrester', '+ metering'], fs=10)
box(1150, 162, 108, 34, ['Fixed DC/DC'], fs=10)
A('<text x="1204" y="214" text-anchor="middle" font-size="10">→ drives, heaters,</text><text x="1204" y="227" text-anchor="middle" font-size="10">cameras (fixed side)</text>')
hv(1147, 260, 1262, 260, w=8)
A('<polygon points="1262,250 1280,260 1262,270" fill="#c0392b"/>')
A('<text x="1150" y="288" font-size="10.5" font-weight="bold">EXPORT ±500 V DC</text><text x="1150" y="302" font-size="10.5">350 kW to the site</text>')
A('<text x="30" y="345" font-size="10.5">P: hanger connector with pilot pins.</text><text x="30" y="359" font-size="10.5">Latch lever breaks the pilot first;</text>'
  '<text x="30" y="373" font-size="10.5">the converter stops before the</text><text x="30" y="387" font-size="10.5">contacts move.</text>')

# ================= B. slip ring half-section =================
A('<text x="20" y="460" class="t">B. Slip ring, half-section (rotor left, stator right)</text>')
k = 1.25                      # px per mm
x0, y0 = 120, 500             # rotor drum outer face at x0; top of stack at y0
A(f'<rect x="{x0-120}" y="{y0-34}" width="{360}" height="22" fill="{ROT}" class="s"/><text x="{x0-110}" y="{y0-19}" font-size="10.5" fill="#fff" style="stroke:none">foot plate (turns)</text>')
A(f'<rect x="{x0-40}" y="{y0-12}" width="40" height="{290*k}" fill="#d9d2c3" class="s"/>')
A(f'<text x="{x0-20}" y="{y0+180}" text-anchor="middle" font-size="10" transform="rotate(-90 {x0-20} {y0+180})" style="stroke:none">insulating drum</text>')
rings = [('+500 V', 40, HV), ('−500 V', 40, HV), ('PE', 40, '#2e7d32'), ('spare', 40, '#999'), ('sig', 12, '#c9a227'), ('sig', 12, '#c9a227')]
y = y0
for j, (t, w, c) in enumerate(rings):
    pitch = 60 if w == 40 else 20
    yc = y + pitch / 2 * k
    A(f'<rect x="{x0}" y="{yc-w/2*k:.0f}" width="{6*k:.0f}" height="{w*k:.0f}" fill="{c}" class="s"/>')
    if j < len(rings) - 1:
        yb = y + pitch * k
        A(f'<rect x="{x0}" y="{yb-2:.0f}" width="{30*k:.0f}" height="4" fill="#8e7cc3"/>')               # rotor barrier fin
    if w == 40:
        for dy in (-9, 9):
            A(f'<rect x="{x0+6*k:.0f}" y="{yc+dy*k-7.5*k/2:.0f}" width="{22*k:.0f}" height="{7.5*k:.0f}" fill="#333"/>')    # brushes
            A('<path d="M' + ' '.join(f'{x0+28*k+i*4:.0f},{yc+dy*k+(3 if i % 2 else -3):.0f}' for i in range(7)) + '" fill="none" stroke="#555" stroke-width="1.5"/>')
        A(f'<text x="{x0-48}" y="{yc+4:.0f}" text-anchor="end" font-size="10.5">{t}</text>')
    else:
        A(f'<rect x="{x0+6*k:.0f}" y="{yc-3:.0f}" width="{18*k:.0f}" height="6" fill="#c9a227"/>')
    y += pitch * k
# stator cartridge
cx = x0 + 60 * k
A(f'<rect x="{cx}" y="{y0-4}" width="{45*k}" height="{290*k}" fill="none" stroke="{FIX}" stroke-width="3"/>')
for j in range(4):
    yf = y0 + (60 * (j + 1) - 30 + 30) * k
for j in range(5):
    yb = y0 + [60, 120, 180, 240, 260][j] * k
    A(f'<rect x="{x0+16*k:.0f}" y="{yb+3:.0f}" width="{44*k:.0f}" height="3" fill="{FIX}"/>')                 # stator fin
A(f'<rect x="{cx+45*k}" y="{y0+20}" width="12" height="{250*k}" fill="{FIX}"/>')                              # post
A(f'<rect x="{cx+10}" y="{y0+290*k+6}" width="{80}" height="8" fill="#8a5a2b"/>')                               # gutter
for yy in (y0 + 20, y0 + 290 * k - 30):
    A(f'<circle cx="{cx+20*k}" cy="{yy}" r="6" fill="#fff" stroke="#222"/>')
labs = [(x0 + 3, y0 + 30 * k, 'Silver-plated Cu rings, 40 mm wide'),
        (x0 + 16 * k, y0 + 51 * k, 'Brushes Ag-MoS₂-graphite, 2 per ring per cartridge'),
        (x0 + 31 * k, y0 + 60 * k, 'Rotor barrier fins (labyrinth with stator fins)'),
        (x0 + 40 * k, y0 + 79 * k, 'Brush springs ±6 mm radial float'),
        (cx + 20 * k, y0 + 20, 'Captive screws (2): cartridge slides out radially'),
        (cx + 50 * k, y0 + 150 * k, 'Stator post on the foundation deck'),
        (cx + 50, y0 + 290 * k + 10, 'Debris gutter under the stack')]
for j, (px, py, t) in enumerate(labs):
    ly = 500 + j * 46
    A(f'<path d="M{px:.0f} {py:.0f}L370 {ly}" class="l"/><circle cx="{px:.0f}" cy="{py:.0f}" r="2" fill="#222"/><text x="374" y="{ly+4}" font-size="11">{t}</text>')
A(f'<text x="20" y="{y0+300*k+40}" font-size="11">Drum Ø0.93 m · 8 cartridges round the stator · 16 brushes per power ring, ~4.4 cm² each, 5 A/cm²</text>')
A(f'<text x="20" y="{y0+300*k+56}" font-size="11">40 mm rings vs 15 mm brushes: ±8 mm axial tilt + 10 mm jack lift; ≥20 mm creepage, ≥10 mm clearance</text>')

# ================= C. mast trays, joint S-loop, connector =================
mx, my, mk = 960, 600, 150
A('<text x="760" y="460" class="t">C. Mast core: trays, climb rail and cables</text>')
R = 1.4 / sqrt(3)
v = [(mx, my - R * mk), (mx + 0.7 * mk, my + R / 2 * mk), (mx - 0.7 * mk, my + R / 2 * mk)]
A('<polygon points="' + ' '.join(f'{x:.0f},{y:.0f}' for x, y in v) + '" fill="#f7f7f7" stroke="#888" stroke-width="2"/>')
A(f'<circle cx="{mx}" cy="{my}" r="{0.345*mk:.0f}" fill="none" stroke="#2e7d32" stroke-dasharray="5 4"/>')
A(f'<rect x="{mx-10}" y="{my+R/2*mk-14:.0f}" width="20" height="10" fill="#555"/>')
for (vx, vy), lab in ((v[0], 'trunk P + fibre'), (v[1], 'trunk S + feeder')):
    tx = vx + (mx - vx) * 0.36
    ty = vy + (my - vy) * 0.36
    A(f'<rect x="{tx-13:.0f}" y="{ty-9:.0f}" width="26" height="18" fill="#ddd" stroke="#222"/>')
    A(f'<circle cx="{tx-6:.0f}" cy="{ty:.0f}" r="4" fill="{HV}"/><circle cx="{tx+6:.0f}" cy="{ty:.0f}" r="4" fill="{HV}"/>')
    A(f'<text x="{tx+18:.0f}" y="{ty+4:.0f}" font-size="10.5">{lab}</text>')
A(f'<text x="{mx}" y="{my+R/2*mk+20:.0f}" text-anchor="middle" font-size="10.5">climb rail (third face)</text>')
A(f'<text x="{mx+60}" y="{my-10}" font-size="10.5" fill="#2e7d32">bots\' clear circle</text>')
# S-loop at a section joint
sx, sy = 780, 720
A(f'<text x="{sx}" y="{sy}" font-size="12" font-weight="bold">Section joint (side view)</text>')
A(f'<line x1="{sx}" y1="{sy+60}" x2="{sx+180}" y2="{sy+60}" stroke="#888" stroke-dasharray="5 3"/><text x="{sx+185}" y="{sy+64}" font-size="10">joint</text>')
A(f'<path d="M{sx+60} {sy+15} V{sy+45} C{sx+60} {sy+60} {sx+90} {sy+52} {sx+90} {sy+60} S{sx+60} {sy+75} {sx+60} {sy+90} V{sy+110}" stroke="{HV}" stroke-width="4" fill="none"/>')
for yy in (sy + 30, sy + 100):
    A(f'<rect x="{sx+52}" y="{yy}" width="16" height="6" fill="#555"/>')
A(f'<text x="{sx+100}" y="{sy+35}" font-size="10.5">clamps every 1.5 m</text><text x="{sx+100}" y="{sy+90}" font-size="10.5">S-loop takes ~7 mm</text><text x="{sx+100}" y="{sy+104}" font-size="10.5">(0.24 m over 105 m)</text>')
# hanger connector interlock
hx, hy = 1040, 720
A(f'<text x="{hx}" y="{hy}" font-size="12" font-weight="bold">Hanger connector</text>')
A(f'<rect x="{hx}" y="{hy+12}" width="210" height="34" fill="#4a9" class="s"/><text x="{hx+105}" y="{hy+33}" text-anchor="middle" font-size="10.5" style="stroke:none">hanger socket (shutter)</text>')
for j, (dx, col, h) in enumerate(((30, HV, 26), (70, HV, 26), (105, '#2e7d32', 32), (140, '#555', 18), (175, '#555', 18))):
    A(f'<rect x="{hx+dx-4}" y="{hy+46}" width="8" height="{h}" fill="{col}"/>')
A(f'<rect x="{hx}" y="{hy+80}" width="210" height="26" fill="#e0a040" class="s"/><text x="{hx+105}" y="{hy+98}" text-anchor="middle" font-size="10.5" style="stroke:none">pack head plug</text>')
A(f'<text x="{hx}" y="{hy+125}" font-size="10.5">PE longest · 2 power pins (30 A) · 2 short pilots:</text>')
A(f'<text x="{hx}" y="{hy+139}" font-size="10.5">pilots make last, break first; the hanger</text>')
A(f'<text x="{hx}" y="{hy+153}" font-size="10.5">e-fuse stays open until the latch closes</text>')
A(f'<text x="{hx}" y="{hy+167}" font-size="10.5">the pilot loop, so no contact ever moves</text>')
A(f'<text x="{hx}" y="{hy+181}" font-size="10.5">under load (DC arcs persist in vacuum).</text>')
A(f'<text x="780" y="{hy+215}" font-size="11.5" font-weight="bold">Totals (power_cabling_check.py)</text>')
for j, t in enumerate(['~95.7% of the cells\' DC reaches the fixed side', 'cables ~0.22 t with insulation, trays, feeder, fibre',
                       'trunks are continuous 115 m cables laid in during jack-up']):
    A(f'<text x="780" y="{hy+233+j*16}" font-size="11">{t}</text>')
A('</svg>')
open('power-cabling.svg', 'w').write('\n'.join(o))
