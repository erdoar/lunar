# Generates pack-converter.svg (rev 28): converter block diagram, pack-head layout, hanger connector section and interlock timeline.
# Run: python3 make_pack_converter_svg.py
o = []
A = o.append
W, H = 1300, 1000
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:1.3}.l{stroke:#555;stroke-width:1;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')
HV, PE, PIL, PACK, HD, HNG = '#c0392b', '#2e7d32', '#555', '#2c4a7a', '#e0a040', '#4a9'


def box(x, y, w, h, lines, fill='#f4f6f8', fs=10.5, bold=False):
    A(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}" class="s"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x+w/2}" y="{y+15+j*13}" text-anchor="middle" font-size="{fs}"{" font-weight=\"bold\"" if bold and j == 0 else ""} style="stroke:none">{t}</text>')


def wire(pts, col=HV, w=2.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    A('<polyline points="' + ' '.join(f'{x},{y}' for x, y in pts) + f'" fill="none" stroke="{col}" stroke-width="{w}"{d}/>')


# ================= A. block diagram =================
A('<text x="20" y="28" class="t">A. Pack converter (in the pack head): 4 MPPT bands → 450 V link → dual active bridge → ±500 V</text>')
bands = [('Band 1', '8 panels, 18 A'), ('Band 2', '8 panels, 18 A'), ('Band 3', '7 panels, 16 A'), ('Band 4', '7 panels, 16 A')]
for j, (b, d) in enumerate(bands):
    y = 52 + j * 62
    box(20, y, 120, 46, [b + ' (top→bottom)' if j == 0 else b, d, '315 V, 2 strings/panel'], fill='#dfe8f5', fs=10)
    A(f'<path d="M150 {y+17} l10 6 l-10 6 z" fill="#222"/><line x1="160" y1="{y+17}" x2="160" y2="{y+29}" stroke="#222" stroke-width="2"/>')
    wire([(140, y + 23), (175, y + 23)])
    box(175, y + 6, 110, 34, ['MPPT boost', '315 → 450 V'], fs=10)
    wire([(285, y + 23), (320, y + 23)])
wire([(320, 75), (320, 263)], w=5)
A('<text x="326" y="290" font-size="10.5">450 V link</text>')
wire([(320, 170), (360, 170)])
box(360, 140, 100, 60, ['Primary bridge', 'SiC 1200 V', '(38% of rating)'], fs=10)
wire([(460, 170), (490, 170)])
A('<rect x="490" y="120" width="70" height="100" rx="6" fill="#fff" class="s"/>')
for yy in (135, 185):
    A('<path d="M500 ' + str(yy) + ' ' + ' '.join(f'q6 -8 12 0' for _ in range(4)) + '" fill="none" stroke="#b87333" stroke-width="2"/>')
A('<text x="525" y="232" text-anchor="middle" font-size="10">planar transformer</text><text x="525" y="245" text-anchor="middle" font-size="10">~100 kHz, 2 secondaries</text>')
for j, (y, lab) in enumerate(((100, 'Sec. bridge +'), (190, 'Sec. bridge −'))):
    wire([(560, y + 40 if j == 0 else y + 5), (590, y + 40 if j == 0 else y + 5)])
    box(590, y, 100, 60, [lab, 'SiC 1200 V', '500 V (42%)'], fs=10)
wire([(690, 130), (740, 130)]); wire([(690, 220), (740, 220)])
wire([(690, 160), (715, 160), (715, 190), (690, 190)], col='#555', w=2)
A('<text x="745" y="126" font-size="11" font-weight="bold" fill="#c0392b">+500</text><text x="745" y="178" font-size="11">mid</text><text x="745" y="226" font-size="11" font-weight="bold" fill="#c0392b">−500</text>')
wire([(715, 175), (740, 175)], col='#555', w=2)
box(790, 120, 120, 110, ['Output stage', 'ideal diode (no', 'backfeed), filter,', 'current limit 25 A,', 'droop sharing', 'soft start'], fs=10)
wire([(910, 175), (950, 175)], w=4)
box(950, 140, 80, 70, ['Plug', '5 pins', '(pack head)'], fill='#fdebd0', fs=10)
wire([(1030, 175), (1060, 175)], w=4)
box(1060, 140, 90, 70, ['Receptacle', '+ e-fuse', '(hanger)'], fill='#d5f5e3', fs=10)
wire([(1150, 175), (1270, 175)], w=5)
A('<text x="1160" y="168" font-size="10.5">yard bus ±500 V</text>')
box(360, 290, 560, 92, ['Controller (rad-tolerant MCU + FPGA watchdog)',
                       'MPPT x 4 bands · droop + current limit · soft start · power-line modem on the bus pins (telemetry, commands)',
                       'insulation monitor on the cell strings · series-arc detector · overvoltage clamps · temperatures',
                       'enable only when the pilot loop is closed · keep-warm ~5 W from the bus when the array is dark'], fill='#fff', fs=10.5, bold=True)
A('<path d="M640 290 V230" class="l" stroke-dasharray="3 3"/>')
box(950, 290, 200, 92, ['Cold plate → heat pipes', '→ hinged radiator fin', '2.0 x 0.45 m, both faces', '~0.42 kW at ~60 °C'], fill='#eaf2f8', fs=10.5)
A('<text x="20" y="320" font-size="11">Cells ~30 °C (radiating both faces)</text><text x="20" y="335" font-size="11">8 x 8 cm triple junction, 136 per string</text>'
  '<text x="20" y="350" font-size="11">bypass diode per 17 cells, blocking</text><text x="20" y="365" font-size="11">diode per string; ~21.3 kW per pack</text>'
  '<text x="20" y="380" font-size="11" font-weight="bold">Overall ~98%, ~21 A out</text>')

# ================= B. pack head layout =================
A('<text x="20" y="430" class="t">B. Pack head: front view and side section</text>')
s, cx, ty = 210, 300, 530                  # px/m, head centre x, head top y
X = lambda m: cx + m * s
A(f'<rect x="{X(-1.05)}" y="{ty-40}" width="{2.1*s}" height="14" fill="{HNG}" class="s"/>')
A(f'<rect x="{X(0.25)-18}" y="{ty-26}" width="36" height="14" fill="#d5f5e3" class="s"/>')
A(f'<rect x="{X(-1.0)}" y="{ty}" width="{2.0*s}" height="34" fill="{HD}" class="s"/>')
for m in (-0.5, 0.5):
    A(f'<path d="M{X(m)-9} {ty} l9 -14 l9 14 z" fill="{HD}" stroke="#222"/>')
for m in (-1.02, 1.02):
    A(f'<rect x="{X(m)-5}" y="{ty-18}" width="10" height="18" fill="{HD}" stroke="#222"/>')
for m in (-0.8, 0.8):
    A(f'<circle cx="{X(m)}" cy="{ty-6}" r="6" fill="#fff" stroke="#222" stroke-width="2"/>')
for m in (-0.66, 0.66):
    A(f'<circle cx="{X(m)}" cy="{ty-5}" r="4.5" fill="#fff" stroke="{HV}" stroke-width="2"/>')
A(f'<rect x="{X(0.25)-14}" y="{ty-12}" width="28" height="12" fill="#fdebd0" class="s"/>')
A(f'<rect x="{X(-0.3)}" y="{ty+4}" width="{0.45*s}" height="26" fill="#7fa3d6" class="s"/>')
A(f'<rect x="{X(-1.0)}" y="{ty+34}" width="{2.0*s}" height="120" fill="{PACK}" opacity="0.9"/>')
for j in range(1, 4):
    A(f'<line x1="{X(-1.0)}" y1="{ty+34+j*30}" x2="{X(1.0)}" y2="{ty+34+j*30}" stroke="#7fa3d6"/>')
A(f'<path d="M{X(-0.97)} {ty+150} V{ty+36} M{X(0.97)} {ty+150} V{ty+36}" stroke="#f2c94c" stroke-width="3" stroke-dasharray="6 3"/>')
calls = [(X(-1.02), ty - 18), (X(-0.8), ty - 6), (X(-0.66), ty - 5), (X(-0.5), ty - 14), (X(0.25), ty - 12), (X(0.97), ty + 90), (X(-0.075), ty + 17)]
cxs = [60, 100, 140, 180, 350, 520, 260]
for n, ((px, py), qx) in enumerate(zip(calls, cxs), 1):
    qy = 462 if n < 6 else (ty + 110 if n == 6 else 462)
    if n == 6:
        qx, qy = X(1.0) + 30, ty + 90
    A(f'<path d="M{px:.0f} {py:.0f}L{qx:.0f} {qy:.0f}" class="l"/><circle cx="{qx:.0f}" cy="{qy:.0f}" r="9" fill="#fff" stroke="#222"/>'
      f'<text x="{qx:.0f}" y="{qy+4:.0f}" text-anchor="middle" font-size="10.5" font-weight="bold" style="stroke:none">{n}</text>')
A(f'<text x="20" y="{ty+190}" font-size="10.5">1 end tab (into the guide fork) · 2 lifting eye · 3 rescue eye · 4 cone (2) · 5 plug, facing up under the receptacle</text>')
A(f'<text x="20" y="{ty+205}" font-size="10.5">6 band harnesses down both edges · 7 converter (~8 kg) on the cold plate</text>')
A(f'<text x="{X(-1.0)}" y="{ty+172}" font-size="10.5">2.0 m wide; panels hang below (30 x 1 m)</text>')
# side section
sx, sy = 690, 520
A(f'<text x="{sx-40}" y="458" font-size="12" font-weight="bold">Side section</text>')
A(f'<rect x="{sx-40}" y="{sy-40}" width="80" height="14" fill="{HNG}" class="s"/>')
A(f'<rect x="{sx-20}" y="{sy}" width="40" height="34" fill="{HD}" class="s"/>')
A(f'<rect x="{sx-14}" y="{sy+5}" width="22" height="24" fill="#7fa3d6" class="s"/>')
A(f'<rect x="{sx-6}" y="{sy+34}" width="12" height="120" fill="{PACK}"/>')
A(f'<line x1="{sx+20}" y1="{sy+8}" x2="{sx+20+0.45*s*0.87}" y2="{sy+8+0.45*s*0.5}" stroke="#9ec9e8" stroke-width="6"/>')
A(f'<circle cx="{sx+20}" cy="{sy+8}" r="4" fill="#fff" stroke="#222"/>')
A(f'<line x1="{sx+20}" y1="{sy+8}" x2="{sx+24}" y2="{sy-30}" stroke="#9ec9e8" stroke-width="3" stroke-dasharray="3 3"/>')
A(f'<path d="M{sx-80} {sy+20} H{sx-30}" stroke="#f5b700" stroke-width="2" marker-end="url(#ar)"/><text x="{sx-82}" y="{sy+16}" font-size="10" text-anchor="end">Sun</text>')
A(f'<text x="{sx+50}" y="{sy+75}" font-size="10.5">radiator fin, hinged,</text><text x="{sx+50}" y="{sy+89}" font-size="10.5">30° down-back (anti-Sun);</text>'
  f'<text x="{sx+50}" y="{sy+103}" font-size="10.5">folds flat (dashed) for</text><text x="{sx+50}" y="{sy+117}" font-size="10.5">transport and the tray</text>')

# ================= C. connector section =================
A('<text x="860" y="430" class="t">C. Hanger connector (section)</text>')
cx0, cy0 = 980, 470
A(f'<rect x="{cx0-110}" y="{cy0}" width="220" height="16" fill="{HNG}" class="s"/><text x="{cx0}" y="{cy0+12}" text-anchor="middle" font-size="10" style="stroke:none">hanger plate</text>')
for dx in (-95, 95):
    A('<path d="M' + ' '.join(f'{cx0+dx+(4 if i % 2 else -4)},{cy0+16+i*4}' for i in range(6)) + '" fill="none" stroke="#555" stroke-width="1.5"/>')
A(f'<rect x="{cx0-100}" y="{cy0+36}" width="200" height="50" fill="#d5f5e3" class="s"/><text x="{cx0+104}" y="{cy0+50}" font-size="10">receptacle on</text><text x="{cx0+104}" y="{cy0+63}" font-size="10">float (±3 mm, ±1°)</text>')
A(f'<rect x="{cx0-100}" y="{cy0+86}" width="120" height="6" fill="#888"/><text x="{cx0+104}" y="{cy0+90}" font-size="10">sliding shutter (open)</text>')
pins = [(-70, HV, 'power +', 30), (-35, HV, 'power −', 30), (0, PE, 'PE', 38), (35, PIL, 'pilot', 26), (70, PIL, 'pilot', 26)]
for dx, col, lab, L in pins:
    A(f'<rect x="{cx0+dx-7}" y="{cy0+44}" width="14" height="36" fill="#fff" stroke="#222"/>')       # socket
    A(f'<rect x="{cx0+dx-4}" y="{cy0+150-L-40}" width="8" height="{L+40}" fill="{col}"/>')
    A(f'<text x="{cx0+dx}" y="{cy0+200}" text-anchor="middle" font-size="9.5">{lab}</text>')
A(f'<rect x="{cx0-100}" y="{cy0+150}" width="200" height="34" fill="#fdebd0" class="s"/><text x="{cx0}" y="{cy0+172}" text-anchor="middle" font-size="10" style="stroke:none">plug on the pack head</text>')
A(f'<path d="M{cx0+100} {cy0+150} l20 -16" stroke="#888" stroke-width="4"/><text x="{cx0+124}" y="{cy0+136}" font-size="10">flip cover (cammed aside)</text>')
A(f'<text x="{cx0+104}" y="{cy0+110}" font-size="10">PE longest; pilots</text><text x="{cx0+104}" y="{cy0+123}" font-size="10">4 mm shorter</text>')
A(f'<text x="870" y="{cy0+225}" font-size="10.5">Ø8 mm rhodium pins in gold multi-lam sockets: 30 A rated, ~21 A used,</text>'
  f'<text x="870" y="{cy0+239}" font-size="10.5">~0.2 mΩ; 40 mm pitch, ribbed PEEK/alumina, ≥25 mm creepage; ~60 N to mate</text>')

# ================= D. interlock timeline =================
A('<text x="20" y="760" class="t">D. Interlock: the hanger e-fuse is the switch</text>')
cols = ['Step', 'PE', '± pins', 'Pilots', 'Latch', 'E-fuse', 'Converter']
rows = [('1 Hoisting: cones enter', 'made', 'made (dead)', 'made', 'open', 'OPEN', 'off'),
        ('2 Bot closes the latch', 'made', 'made', 'made', 'closed', 'pre-charge → ON', 'MPPT'),
        ('3 Lever first ~10°', 'made', 'made', 'loop open', 'closing...', 'OPEN &lt;1 ms', 'stops'),
        ('4 Lever on: hook frees', 'made', 'made (dead)', 'loop open', 'open', 'OPEN', 'off'),
        ('5 Lift 50 mm, lower', 'breaks last', 'part, no current', 'break first', 'open', 'OPEN', 'off')]
xs = [20, 230, 330, 450, 560, 660, 800]
for j, c in enumerate(cols):
    A(f'<text x="{xs[j]}" y="785" font-weight="bold" font-size="11.5">{c}</text>')
for i, r in enumerate(rows):
    y = 808 + i * 24
    A(f'<rect x="15" y="{y-15}" width="890" height="22" fill="{"#f7f9fb" if i % 2 else "#fff"}"/>')
    for j, c in enumerate(r):
        col = HV if c.startswith('ON') or 'pre-charge' in c else ('#2e7d32' if c.startswith('OPEN') else '#222')
        A(f'<text x="{xs[j]}" y="{y}" font-size="11" fill="{col}">{c}</text>')
A('<text x="20" y="948" font-size="11">The bot also commands "pack off" and checks the e-fuse state before touching the lever. Contacts only ever move dead,</text>'
  '<text x="20" y="963" font-size="11">so no DC arc can strike in vacuum. Pilot lead 4 mm at the 10 mm/s final creep = 0.4 s of margin.</text>')
A('<text x="930" y="800" font-size="12" font-weight="bold">Numbers (pack_converter_check.py)</text>')
for j, t in enumerate(['~21.3 kW in, ~98%, ~0.42 kW of heat', 'SiC at 38–42% of 1,200 V (SEB derating)', 'radiator 1.1 m² effective (0.82 needed)',
                       'keep-warm 5 W/pack, 80 W total', 'connector loss ~0.2 W; mate ~60 N', '16 packs ≈ 335 kW at the bus (margin item)']):
    A(f'<text x="930" y="{820+j*17}" font-size="11">{t}</text>')
A('</svg>')
open('pack-converter.svg', 'w').write('\n'.join(o))
