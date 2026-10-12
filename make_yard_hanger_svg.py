# Generates yard-hanger.svg (rev 33): yard cross-section, pack hanger elevation, root joint, CFRP rod end fitting and numbers.
# Run: python3 make_yard_hanger_svg.py
o = []
A = o.append
W, H = 1240, 1000
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker>'
  '<pattern id="gr" width="5" height="5" patternUnits="userSpaceOnUse"><path d="M0 0H5M0 0V5" stroke="#888" stroke-width="0.7"/></pattern></defs>')
A('<style>.s{stroke:#222;stroke-width:1.2}.l{stroke:#555;stroke-width:1;fill:none}.rope{stroke:#c0392b;stroke-width:1.6;fill:none;stroke-dasharray:6 3}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}.n{font-size:11px;font-weight:bold}</style>')
YD, YDS, TI, HNG, PACK, BOT, CONE, BUS = '#e0a040', '#8a5a00', '#9fb3c8', '#4a9', '#2c4a7a', '#6c3483', '#c9a227', '#2e86c1'


def lab(x1, y1, x2, y2, lines, anchor='start', fs=11.5):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*14:.0f}" text-anchor="{anchor}" font-size="{fs}">{t}</text>')


def call(n, x, y, tx, ty):
    A(f'<path d="M{x:.0f} {y:.0f}L{tx:.0f} {ty:.0f}" class="l"/>')
    A(f'<circle cx="{tx:.0f}" cy="{ty:.0f}" r="9" fill="#fff" stroke="#222"/><text x="{tx:.0f}" y="{ty+4:.0f}" text-anchor="middle" class="n" style="stroke:none">{n}</text>')


def key(x, y, items, w=330):
    for j, (n, t) in enumerate(items):
        A(f'<circle cx="{x+9}" cy="{y+j*17}" r="8" fill="#fff" stroke="#222"/><text x="{x+9}" y="{y+j*17+4}" text-anchor="middle" class="n" style="stroke:none">{n}</text>')
        A(f'<text x="{x+24}" y="{y+j*17+4}" font-size="11.5">{t}</text>')


def chord(x, y, r):
    A(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{YD}" stroke="{YDS}" stroke-width="1.4"/><circle cx="{x:.1f}" cy="{y:.1f}" r="{r-2:.1f}" fill="#fff" stroke="none"/>')


# ================= 1. Yard cross-section =================
A('<text x="20" y="30" class="t">1. Yard section (looking along the arm)</text>')
s1, c1 = 170, 215
Y1 = lambda z: 410 - z * s1
X1 = lambda y: c1 + y * s1
r = 0.03 * s1
# web: verticals and the lateral X between the chords (dashed: in the panel behind)
for yy in (-0.25, 0.25):
    A(f'<line x1="{X1(yy)}" y1="{Y1(0)}" x2="{X1(yy)}" y2="{Y1(0.8)}" stroke="{YDS}" stroke-width="1.2"/>')
A(f'<line x1="{X1(-0.25)}" y1="{Y1(0)}" x2="{X1(0.25)}" y2="{Y1(0.8)}" stroke="{YDS}" stroke-dasharray="4 3"/>')
A(f'<line x1="{X1(-0.25)}" y1="{Y1(0.8)}" x2="{X1(0.25)}" y2="{Y1(0)}" stroke="{YDS}" stroke-dasharray="4 3"/>')
for z in (0, 0.8):
    A(f'<line x1="{X1(-0.25)}" y1="{Y1(z)}" x2="{X1(0.25)}" y2="{Y1(z)}" stroke="{YDS}" stroke-width="1.2"/>')
# bus trunks in a tray on the inside of the bottom chords
A(f'<rect x="{X1(-0.20)}" y="{Y1(0.13)}" width="{0.14*s1}" height="{0.07*s1}" fill="#fff" stroke="{BUS}" stroke-width="1.4"/>')
for yy in (-0.17, -0.13, -0.09):
    A(f'<circle cx="{X1(yy):.1f}" cy="{Y1(0.095):.1f}" r="3" fill="{BUS}"/>')
for yy in (-0.25, 0.25):
    for z in (0, 0.8):
        chord(X1(yy), Y1(z), r)
# walkway grating, toe boards, stanchion + fall-arrest T-rail on the outer edge
A(f'<rect x="{X1(-0.27)}" y="{Y1(0.86)}" width="{0.54*s1}" height="{0.03*s1}" fill="url(#gr)" stroke="#555"/>')
for yy in (-0.27, 0.26):
    A(f'<rect x="{X1(yy)}" y="{Y1(0.97)}" width="{0.01*s1+1}" height="{0.11*s1}" fill="#777"/>')
A(f'<line x1="{X1(0.30)}" y1="{Y1(0.83)}" x2="{X1(0.30)}" y2="{Y1(1.95)}" stroke="{BOT}" stroke-width="3"/>')
A(f'<line x1="{X1(0.25)}" y1="{Y1(0.83)}" x2="{X1(0.30)}" y2="{Y1(0.83)}" stroke="{BOT}" stroke-width="3"/>')
A(f'<rect x="{X1(0.26)}" y="{Y1(1.97)}" width="{0.10*s1}" height="4" fill="{BOT}"/><rect x="{X1(0.30)-1.5}" y="{Y1(1.97)}" width="3" height="10" fill="{BOT}"/>')
A(f'<rect x="{X1(0.28)}" y="{Y1(1.93)}" width="{0.06*s1}" height="{0.05*s1}" fill="#fff" stroke="{BOT}"/>')   # captive trolley
A(f'<path d="M{X1(0.28)} {Y1(1.90)} Q{X1(0.05)} {Y1(1.75)} {X1(0.0)} {Y1(1.45)}" stroke="{BOT}" fill="none" stroke-dasharray="3 2"/>')
A(f'<text x="{X1(-0.02)}" y="{Y1(1.40)}" text-anchor="end" font-size="10.5" fill="{BOT}">tether to bot</text>')
# reel socket on the walkway, latch lever + flag + push rod
A(f'<rect x="{X1(-0.15)}" y="{Y1(1.0)}" width="{0.24*s1}" height="{0.11*s1}" fill="#d5d8dc" class="s"/>')
A(f'<line x1="{X1(0.18)}" y1="{Y1(-0.04)}" x2="{X1(0.18)}" y2="{Y1(0.95)}" stroke="#555" stroke-width="2"/>')
A(f'<line x1="{X1(0.18)}" y1="{Y1(0.95)}" x2="{X1(0.10)}" y2="{Y1(1.22)}" stroke="#222" stroke-width="3.5" stroke-linecap="round"/>')
A(f'<path d="M{X1(0.10)} {Y1(1.22)} l14 -5 l-3 9 z" fill="#e74c3c" stroke="#222" stroke-width="0.8"/>')
A(f'<circle cx="{X1(0.18)}" cy="{Y1(0.95)}" r="3" fill="#fff" stroke="#222"/>')
# hanger: saddle seat across both bottom chords, Ti box beam, cone sockets and hook
A(f'<rect x="{X1(-0.29)}" y="{Y1(-0.03)}" width="{0.58*s1}" height="{0.025*s1}" fill="{TI}" class="s"/>')
A(f'<rect x="{X1(-0.29)}" y="{Y1(-0.045)}" width="{0.58*s1}" height="{0.012*s1+1}" fill="#bbb"/>')
A(f'<rect x="{X1(-0.04)}" y="{Y1(-0.06)}" width="{0.08*s1}" height="{0.12*s1}" fill="{HNG}" class="s"/>')
for yy in (-0.09, 0.09):
    A(f'<path d="M{X1(yy)-9} {Y1(-0.12)} h18 v{0.06*s1} l-5 3 h-8 l-5 -3 z" fill="{HNG}" class="s"/>')
# pack head below: cones up into the sockets, latch bar under the hook
ph = -0.24
A(f'<rect x="{X1(-0.13)}" y="{Y1(ph)}" width="{0.26*s1}" height="{0.10*s1}" fill="{YD}" class="s"/>')
for yy in (-0.09, 0.09):
    A(f'<path d="M{X1(yy)-6} {Y1(ph)} L{X1(yy)} {Y1(ph+0.07)} L{X1(yy)+6} {Y1(ph)} z" fill="{CONE}" class="s"/>')
A(f'<path d="M{X1(0.0)} {Y1(-0.18)} v8 q0 6 6 6 h6" stroke="#222" stroke-width="2.4" fill="none"/>')
A(f'<rect x="{X1(-0.03)}" y="{Y1(ph+0.035)}" width="{0.06*s1}" height="4" fill="#555"/>')
A(f'<rect x="{X1(-0.02)}" y="{Y1(ph-0.10)}" width="{0.04*s1}" height="{0.24*s1}" fill="{PACK}"/>')
A(f'<path d="M{X1(-0.06)} {Y1(ph-0.34)} l8 -6 l8 6 l8 -6 l8 6" stroke="#555" fill="none"/>')
lab(X1(-0.25) - r, Y1(0.8), 150, Y1(0.62), ['4 chords Ø60 x 2 mm', 'CFRP, 0.8 x 0.5 m box'], 'end')
lab(X1(-0.27), Y1(0.88), 150, Y1(1.12), ['Grating 0.5 m', '+ toe boards'], 'end')
lab(X1(-0.10), Y1(1.0), 150, Y1(1.45), ['Reel socket'], 'end')
lab(X1(0.30), Y1(1.70), X1(0.62), Y1(1.85), ['T-section fall-arrest', 'rail, 1.1 m up'])
lab(X1(0.13), Y1(1.18), X1(0.62), Y1(1.35), ['Latch lever + flag,', 'lock pin, pilot switch'])
lab(X1(0.18), Y1(0.45), X1(0.62), Y1(0.60), ['Push rod to the', 'hook cross rod'])
lab(X1(-0.20), Y1(0.12), 150, Y1(0.22), ['Bus trunks in', 'a chord tray'], 'end')
lab(X1(0.29), Y1(-0.02), X1(0.62), Y1(0.12), ['Saddle seat on both', 'bottom chords, shimmed'])
lab(X1(0.04), Y1(-0.08), X1(0.62), Y1(-0.18), ['Ti box hanger', '0.12 x 0.08 m'])
lab(X1(0.13), Y1(ph - 0.03), X1(0.62), Y1(-0.42), ['Pack head: cones up into', 'the sockets, latch bar', 'under the hook'])
lab(X1(-0.09) - 9, Y1(-0.09), 150, Y1(-0.14), ['Cone sockets', 'front and back'], 'end')
A(f'<text x="{X1(0)}" y="{Y1(ph-0.48)}" text-anchor="middle" font-size="11" fill="#555">pack hangs 30 m below</text>')

# ================= 3. Hanger elevation =================
A('<text x="560" y="30" class="t">3. Pack hanger elevation (wing plane), rope run shown for a swap</text>')
s3, c3 = 250, 860
X3 = lambda x: c3 + x * s3
Y3 = lambda z: 330 - z * s3
# yard: bottom + top chords, Warren web in 0.7 m panels, break lines
A(f'<rect x="{X3(-1.25)}" y="{Y3(0.015)}" width="{2.5*s3}" height="{0.03*s3}" fill="{YD}" stroke="{YDS}"/>')
A(f'<rect x="{X3(-1.25)}" y="{Y3(0.815)}" width="{2.5*s3}" height="{0.03*s3}" fill="{YD}" stroke="{YDS}"/>')
for i in range(-2, 2):
    x0, x1 = i * 0.7, (i + 1) * 0.7
    z0, z1 = (0, 0.8) if i % 2 == 0 else (0.8, 0)
    xa, xb = max(x0, -1.25), min(x1, 1.25)
    za = z0 + (z1 - z0) * (xa - x0) / 0.7
    zb = z0 + (z1 - z0) * (xb - x0) / 0.7
    A(f'<line x1="{X3(xa):.1f}" y1="{Y3(za):.1f}" x2="{X3(xb):.1f}" y2="{Y3(zb):.1f}" stroke="{YDS}" stroke-width="2.5"/>')
for xn in (-0.7, 0, 0.7):
    for z in (0, 0.8):
        A(f'<rect x="{X3(xn)-6}" y="{Y3(z)-6}" width="12" height="12" fill="{TI}" stroke="#555"/>')
for xb in (-1.25, 1.25):
    A(f'<path d="M{X3(xb)} {Y3(0.92)} V{Y3(0.45)} l-6 8 l12 8 l-6 8 V{Y3(-0.04)}" stroke="#888" fill="none"/>')
# walkway, stanchions, reel socket, anchor eyes, lever
A(f'<rect x="{X3(-1.25)}" y="{Y3(0.86)}" width="{2.5*s3}" height="{0.03*s3}" fill="url(#gr)" stroke="#555"/>')
for xs in (-1.0, 1.0):
    A(f'<line x1="{X3(xs)}" y1="{Y3(0.86)}" x2="{X3(xs)}" y2="{Y3(1.12)}" stroke="{BOT}" stroke-width="2"/>')
A(f'<line x1="{X3(-1.25)}" y1="{Y3(1.12)}" x2="{X3(1.25)}" y2="{Y3(1.12)}" stroke="{BOT}" stroke-width="2" stroke-dasharray="8 4"/>')
A(f'<rect x="{X3(-0.15)}" y="{Y3(0.98)}" width="{0.30*s3}" height="{0.12*s3}" fill="#d5d8dc" class="s"/>')
A(f'<text x="{X3(0)}" y="{Y3(0.98)+0.07*s3}" text-anchor="middle" font-size="10" style="stroke:none">socket</text>')
for xe in (-0.25, 0.25):
    A(f'<circle cx="{X3(xe)}" cy="{Y3(0.92)}" r="5" fill="none" stroke="#222" stroke-width="2"/>')
A(f'<line x1="{X3(0.5)}" y1="{Y3(0.88)}" x2="{X3(0.42)}" y2="{Y3(1.10)}" stroke="#222" stroke-width="4" stroke-linecap="round"/>')
A(f'<path d="M{X3(0.42)} {Y3(1.10)} l16 -6 l-4 11 z" fill="#e74c3c" stroke="#222" stroke-width="0.8"/>')
A(f'<line x1="{X3(0.5)}" y1="{Y3(0.88)}" x2="{X3(0.5)}" y2="{Y3(-0.08)}" stroke="#555" stroke-width="2"/>')
# hanger beam and fittings
hz0, hz1 = -0.03, -0.15
A(f'<rect x="{X3(-1.0)}" y="{Y3(hz0)}" width="{2.0*s3}" height="{0.12*s3}" fill="{HNG}" class="s"/>')
for xn in (-0.7, 0.7):
    A(f'<rect x="{X3(xn)-10}" y="{Y3(0)-1}" width="20" height="{0.03*s3+1}" fill="{TI}" class="s"/>')
A(f'<rect x="{X3(-0.42)}" y="{Y3(0.12)}" width="{0.24*s3}" height="{0.12*s3-2}" fill="#fdebd0" class="s"/>')   # e-fuse box (above the bottom chord, beside the hanger top)
A(f'<text x="{X3(-0.30)}" y="{Y3(0.12)+0.08*s3}" text-anchor="middle" font-size="10" style="stroke:none">e-fuse</text>')
A(f'<line x1="{X3(-0.30)}" y1="{Y3(0.12)}" x2="{X3(-0.30)}" y2="{Y3(0.36)}" stroke="{BUS}" stroke-width="2"/>')
A(f'<line x1="{X3(-1.25)}" y1="{Y3(0.36)}" x2="{X3(1.25)}" y2="{Y3(0.36)}" stroke="{BUS}" stroke-width="3"/>')
A(f'<line x1="{X3(-0.30)}" y1="{Y3(0.0)}" x2="{X3(-0.30)}" y2="{Y3(hz0)}" stroke="{BUS}" stroke-width="2"/>')
A(f'<path d="M{X3(-0.30)} {Y3(hz0+0.01)} H{X3(0.25)} V{Y3(hz1)}" stroke="{BUS}" stroke-width="1.6" fill="none" stroke-dasharray="4 2"/>')
# forks
for sx in (-1, 1):
    xf = X3(sx * 1.02)
    A(f'<path d="M{xf} {Y3(hz0)} V{Y3(-0.22)} L{xf+sx*14} {Y3(-0.36)}" stroke="#222" stroke-width="3" fill="none"/>')
    A(f'<path d="M{X3(sx*1.0)} {Y3(hz0)} H{xf}" stroke="#222" stroke-width="3"/>')
# sheaves: centre (±0.05) and end (±0.8)
for xs in (-0.05, 0.05, -0.8, 0.8):
    A(f'<circle cx="{X3(xs)}" cy="{Y3(-0.09)}" r="7" fill="#fff" stroke="#222" stroke-width="1.4"/><circle cx="{X3(xs)}" cy="{Y3(-0.09)}" r="1.6" fill="#222"/>')
# cone sockets (±0.5) and hooks beside them (inboard, ±0.42)
for sx in (-1, 1):
    xc = X3(sx * 0.5)
    A(f'<path d="M{xc-11} {Y3(hz1)} L{xc-5} {Y3(hz1+0.07)} H{xc+5} L{xc+11} {Y3(hz1)}" fill="#fff" stroke="#222" stroke-width="1.2"/>')
    xh = X3(sx * 0.42)
    A(f'<path d="M{xh} {Y3(-0.125)} V{Y3(-0.215)} h{-sx*12} v-5" stroke="#222" stroke-width="2.6" fill="none"/>')
    A(f'<circle cx="{xh}" cy="{Y3(-0.125)}" r="3" fill="#fff" stroke="#222"/>')
A(f'<line x1="{X3(-0.42)}" y1="{Y3(-0.125)}" x2="{X3(0.42)}" y2="{Y3(-0.125)}" stroke="#555" stroke-width="1.4" stroke-dasharray="2 2"/>')
# connector receptacle on float mount at +0.25
A(f'<rect x="{X3(0.25)-11}" y="{Y3(hz1)}" width="22" height="{0.05*s3}" fill="#f5b041" class="s"/>')
A(f'<path d="M{X3(0.25)-14} {Y3(hz1)+2} h-4 M{X3(0.25)+14} {Y3(hz1)+2} h4" stroke="#222"/>')
# pack head and the top of the pack
pz0, pz1 = -0.235, -0.335
A(f'<rect x="{X3(-0.98)}" y="{Y3(pz0)}" width="{1.96*s3}" height="{0.10*s3}" fill="{YD}" class="s"/>')
A(f'<rect x="{X3(-0.98)}" y="{Y3(pz1)}" width="{1.96*s3}" height="{0.2*s3}" fill="{PACK}"/>')
for i in range(1, 14):
    A(f'<line x1="{X3(-0.98+i*0.14)}" y1="{Y3(pz1)}" x2="{X3(-0.98+i*0.14)}" y2="{Y3(pz1-0.2)}" stroke="#4a6a9a"/>')
A(f'<path d="M{X3(-0.98)} {Y3(pz1-0.2)} l20 6 l20 -6 l20 6" stroke="#fff" fill="none" stroke-width="3"/>')
for sx in (-1, 1):
    xc = X3(sx * 0.5)
    A(f'<path d="M{xc-9} {Y3(pz0)} L{xc-3} {Y3(hz1+0.06)} H{xc+3} L{xc+9} {Y3(pz0)} z" fill="{CONE}" class="s"/>')
    xb = X3(sx * 0.42)
    xbar = xb - sx * 12
    A(f'<rect x="{xbar-2}" y="{Y3(-0.205)}" width="4" height="{Y3(pz0)-Y3(-0.205)}" fill="#555"/>')
    A(f'<rect x="{min(xbar, xbar-sx*14)}" y="{Y3(-0.205)}" width="14" height="4" fill="#555"/>')
    A(f'<circle cx="{X3(sx*0.8)}" cy="{Y3(pz0)-5}" r="5" fill="none" stroke="#222" stroke-width="2.2"/>')
    A(f'<circle cx="{X3(sx*0.66)}" cy="{Y3(pz0)-5}" r="4.5" fill="none" stroke="#c0392b" stroke-width="2.2"/>')
A(f'<rect x="{X3(0.25)-8}" y="{Y3(pz0)-9}" width="16" height="9" fill="#f5b041" class="s"/>')
# rope run during a swap: socket -> centre sheaves -> end sheaves -> lifting eyes
for sx in (-1, 1):
    A(f'<path d="M{X3(sx*0.05)} {Y3(0.98)} V{Y3(-0.09)-7} M{X3(sx*0.05)+sx*7} {Y3(-0.09)} H{X3(sx*0.8)-sx*7} '
      f'M{X3(sx*0.8)+sx*7} {Y3(-0.09)} V{Y3(pz0)-10}" class="rope"/>')
# callouts
cy = 75
call(1, X3(0.0), Y3(1.04), X3(-0.15), cy)
call(2, X3(-0.25), Y3(0.92), X3(-0.55), cy)
call(3, X3(0.44), Y3(1.07), X3(0.45), cy)
call(4, X3(-0.30), Y3(0.06), X3(-1.18), Y3(0.20))
call(5, X3(0.7), Y3(0.0), X3(1.18), Y3(0.20))
call(6, X3(1.02), Y3(-0.30), X3(1.18), Y3(-0.22))
call(7, X3(-0.8), Y3(-0.09) + 7, X3(-1.18), Y3(-0.50))
call(8, X3(-0.05), Y3(-0.09) + 7, X3(-0.12), Y3(-0.62))
call(9, X3(0.5), Y3(hz1 + 0.03), X3(0.62), Y3(-0.62))
call(10, X3(-0.42) + 10, Y3(-0.205), X3(-0.48), Y3(-0.62))
call(11, X3(0.25), Y3(hz1 - 0.03), X3(0.28), Y3(-0.62))
call(12, X3(-0.66), Y3(pz0) - 5, X3(-0.82), Y3(-0.62))
call(13, X3(0.8), Y3(pz0) - 5, X3(0.96), Y3(-0.62))
A(f'<text x="{X3(-1.22)}" y="{Y3(1.12)+14}" font-size="10.5" fill="{BOT}">fall-arrest rail, 1.1 m up</text>')
A(f'<text x="{X3(-1.22)}" y="{Y3(0.36)-6}" font-size="10.5" fill="{BUS}">±500 V yard bus</text>')
# dims
A(f'<path d="M{X3(-1.0)} 498H{X3(1.0)}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{X3(0)}" y="512" text-anchor="middle" font-size="11">hanger 2.0 m; pack 1.96 m; hanger pitch 2.1 m</text>')

# ================= 2. Root joint =================
A('<text x="20" y="568" class="t">2. Root joint: yard to mast, core kept open</text>')
s2, c2, zb = 70, 190, 757
X2 = lambda x: c2 + x * s2
Y2 = lambda z: zb - z * s2
# stiffened yard-mast section (1.4 m face), 3 m tall: z -1.1 ... +1.9 about the bottom chord
A(f'<rect x="{X2(-0.7)}" y="{Y2(1.9)}" width="{1.4*s2}" height="{3.0*s2}" fill="#f2f3f4" stroke="#555" stroke-width="2.4"/>')
for z0 in (-1.1, -0.35, 0.4, 1.15):
    A(f'<path d="M{X2(-0.7)} {Y2(z0)} L{X2(0.7)} {Y2(z0+0.75)} M{X2(0.7)} {Y2(z0)} L{X2(-0.7)} {Y2(z0+0.75)}" stroke="#bbb"/>')
A(f'<line x1="{X2(0)}" y1="{Y2(-1.35)}" x2="{X2(0)}" y2="{Y2(1.05)}" stroke="#888" stroke-width="2"/>')
A(f'<line x1="{X2(-0.7)}" y1="{Y2(-1.35)}" x2="{X2(-0.7)}" y2="{Y2(-1.1)}" stroke="#888" stroke-width="2"/><line x1="{X2(0.7)}" y1="{Y2(-1.35)}" x2="{X2(0.7)}" y2="{Y2(-1.1)}" stroke="#888" stroke-width="2"/>')
# climb rail inside the core, up to the hatch
A(f'<line x1="{X2(0.1)}" y1="{Y2(-1.35)}" x2="{X2(0.1)}" y2="{Y2(1.3)}" stroke="{BOT}" stroke-width="2.5" stroke-dasharray="6 3"/>')
# hatch in the face above the walkway
A(f'<rect x="{X2(0.15)}" y="{Y2(1.85)}" width="{0.5*s2}" height="{0.98*s2}" fill="#fff" stroke="#222" stroke-width="1.6" stroke-dasharray="5 2"/>')
A(f'<path d="M{X2(0.1)} {Y2(1.3)} Q{X2(0.4)} {Y2(1.55)} {X2(0.75)} {Y2(1.7)} H{X2(2.3)}" stroke="{BOT}" stroke-width="2.5" fill="none"/>')
A(f'<line x1="{X2(-0.75)}" y1="{Y2(1.7)}" x2="{X2(-2.3)}" y2="{Y2(1.7)}" stroke="{BOT}" stroke-width="2.5"/>')
# ring frames at the two chord levels, arms bolted on
for z in (0, 0.8):
    A(f'<rect x="{X2(-0.9)}" y="{Y2(z)-5}" width="{1.8*s2}" height="10" fill="{TI}" class="s"/>')
for sx in (-1, 1):
    xa, xb = sorted((X2(sx * 0.9), X2(sx * 2.3)))
    for z in (0, 0.8):
        A(f'<rect x="{xa}" y="{Y2(z)-4}" width="{xb-xa}" height="8" fill="{YD}" stroke="{YDS}"/>')
        A(f'<rect x="{X2(sx*0.9)-(8 if sx>0 else 0)}" y="{Y2(z)-7}" width="8" height="14" fill="#555"/>')
    for i in range(2):
        p, q = sx * (0.9 + i * 0.7), sx * (0.9 + (i + 1) * 0.7)
        q = sx * min(abs(q), 2.3)
        A(f'<line x1="{X2(p)}" y1="{Y2(0 if i==0 else 0.8)}" x2="{X2(q)}" y2="{Y2(0.8 if i==0 else 0)}" stroke="{YDS}" stroke-width="2"/>')
    A(f'<rect x="{xa}" y="{Y2(0.86)}" width="{xb-xa}" height="4" fill="url(#gr)" stroke="#555" stroke-width="0.6"/>')
    A(f'<path d="M{X2(sx*2.3)} {Y2(1.9)} l-4 10 l8 10 l-4 10 V{Y2(-0.1)}" stroke="#888" fill="none"/>')
A(f'<rect x="{X2(-0.9)}" y="{Y2(0.86)}" width="{1.8*s2}" height="4" fill="url(#gr)" stroke="#555" stroke-width="0.6"/>')
# reel garage on the port walkway
A(f'<rect x="{X2(-2.1)}" y="{Y2(1.45)}" width="{1.1*s2}" height="{0.55*s2}" fill="#d5d8dc" class="s"/>')
A(f'<text x="{X2(-1.55)}" y="{Y2(1.1)}" text-anchor="middle" font-size="10" style="stroke:none">reel garage</text>')
# bus trunks out through the lower ring frame
A(f'<path d="M{X2(-0.45)} {Y2(-1.35)} V{Y2(0.25)} H{X2(-2.3)} M{X2(0.45)} {Y2(-1.35)} V{Y2(0.25)} H{X2(2.3)}" stroke="{BUS}" stroke-width="2.4" fill="none"/>')
# masthead rail outside, above
A(f'<line x1="{X2(-0.6)}" y1="{Y2(1.9)}" x2="{X2(-0.6)}" y2="{Y2(2.25)}" stroke="{BOT}" stroke-width="2.5"/>')
A(f'<line x1="{X2(-0.7)}" y1="{Y2(1.9)}" x2="{X2(-0.7)}" y2="{Y2(2.25)}" stroke="#888" stroke-width="2"/><line x1="{X2(0.7)}" y1="{Y2(1.9)}" x2="{X2(0.7)}" y2="{Y2(2.25)}" stroke="#888" stroke-width="2"/>')
call('A', X2(0.85), Y2(0.8), X2(1.3), Y2(2.2))
call('B', X2(0.4), Y2(1.55), X2(0.5), Y2(2.2))
call('C', X2(0.1), Y2(-0.6), X2(-1.0), Y2(-0.9))
call('D', X2(-1.6), Y2(1.45), X2(-1.6), Y2(2.2))
call('E', X2(-1.4), Y2(0.25), X2(-1.6), Y2(-0.9))
call('F', X2(-0.6), Y2(2.1), X2(-0.15), Y2(2.2))
call('G', X2(1.6), Y2(0.4), X2(1.6), Y2(-0.9))
# plan of the ring frame
pc, pr = (480, 700), 64
A(f'<text x="{pc[0]}" y="{pc[1]-pr-28}" text-anchor="middle" font-size="12" font-weight="bold">Plan at a ring frame</text>')
tri = [(pc[0] + 0.808 * pr / 0.9 * __import__('math').cos(__import__('math').radians(a)), pc[1] + 0.808 * pr / 0.9 * __import__('math').sin(__import__('math').radians(a))) for a in (90, 210, 330)]
A(f'<circle cx="{pc[0]}" cy="{pc[1]}" r="{pr}" fill="none" stroke="{TI}" stroke-width="7"/>')
A(f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in tri)}" fill="#f2f3f4" stroke="#555" stroke-width="2"/>')
for x, y in tri:
    A(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="5" fill="#888"/>')
A(f'<circle cx="{pc[0]}" cy="{pc[1]}" r="{0.345*pr/0.9:.1f}" fill="none" stroke="{BOT}" stroke-dasharray="4 3"/>')
q = 0.25 * pr / 0.9
for sx in (-1, 1):
    for sy in (-1, 1):
        xin = pc[0] + sx * (pr ** 2 - q ** 2) ** 0.5
        A(f'<line x1="{xin:.1f}" y1="{pc[1]+sy*q:.1f}" x2="{pc[0]+sx*(pr+32):.1f}" y2="{pc[1]+sy*q:.1f}" stroke="{YDS}" stroke-width="4"/>')
A(f'<text x="{pc[0]}" y="{pc[1]+4}" text-anchor="middle" font-size="9.5" fill="{BOT}" style="stroke:none">core Ø0.69</text>')
A(f'<text x="{pc[0]}" y="{pc[1]+pr+22}" text-anchor="middle" font-size="10.5">ring R 0.9 m round the 1.4 m face;</text>')
A(f'<text x="{pc[0]}" y="{pc[1]+pr+36}" text-anchor="middle" font-size="10.5">chord pairs 0.5 m apart</text>')
key(20, 876, [('A', 'Ti ring frames at both chord levels take the chord forces round the mast'),
              ('B', 'Hatch in the face: the climb rail meets the walkway rail'),
              ('C', 'Climb rail in the open core (~Ø0.69 m)'),
              ('D', 'Reel garage on the port walkway (2 reels)'),
              ('E', 'Bus trunks leave the core trays under the lower ring'),
              ('F', 'Masthead rail outside, above the hatch'),
              ('G', 'Arms: 14 sections of ~2.7 m, ~0.45 t for both')])

# ================= 4. CFRP rod end fitting (rev 33: one bundle per outrigger) =================
A('<text x="610" y="568" class="t">4. Topping lift rod end (yard tip)</text>')
s4, x4, y4 = 400, 618, 690
X4 = lambda m: x4 + m * s4
A(f'<rect x="{X4(0)}" y="{y4-0.0055*s4:.1f}" width="{0.17*s4}" height="{0.011*s4:.1f}" fill="#fdfefe" stroke="#555" stroke-width="0.8"/>')
A(f'<path d="M{X4(0.17)} {y4-3:.1f} L{X4(0.29)} {y4-0.012*s4:.1f} V{y4+0.012*s4:.1f} L{X4(0.17)} {y4+3:.1f} z" fill="{TI}" class="s"/>')
A(f'<rect x="{X4(0.29)}" y="{y4-5}" width="{0.11*s4}" height="10" fill="#d5d8dc" class="s"/>')
for i in range(8):
    A(f'<line x1="{X4(0.30+i*0.012)}" y1="{y4-5}" x2="{X4(0.305+i*0.012)}" y2="{y4+5}" stroke="#555" stroke-width="0.7"/>')
A(f'<rect x="{X4(0.345)}" y="{y4-7}" width="8" height="14" fill="#555"/>')
A(f'<path d="M{X4(0.40)} {y4-8} H{X4(0.45)} V{y4+8} H{X4(0.40)} z" fill="{TI}" class="s"/><circle cx="{X4(0.435)}" cy="{y4}" r="3" fill="#222"/>')
A(f'<path d="M{X4(0.425)} {y4-4} H{X4(0.49)} V{y4+40} H{X4(0.425)} z" fill="{TI}" stroke="#222"/>')
A(f'<rect x="{X4(0.40)}" y="{y4+40}" width="{0.13*s4}" height="26" fill="{TI}" class="s"/>')
A(f'<circle cx="{X4(0.465)}" cy="{y4+53}" r="9" fill="{YD}" stroke="{YDS}" stroke-width="1.4"/>')
A(f'<text x="{X4(0.465)}" y="{y4+82}" text-anchor="middle" font-size="10.5">outrigger, ±0.55 m</text>')
lab(X4(0.07), y4 - 0.0055 * s4, X4(-0.01), y4 - 60, ['Rod bundle 7 x Ø3 mm,', 'white jacket (~Ø11 mm)'])
lab(X4(0.23), y4 + 0.012 * s4, X4(0.10), y4 + 50, ['Potted Ti', 'cone socket'])
lab(X4(0.35), y4 - 7, X4(0.36), y4 - 60, ['M16 barrel adjuster,', 'locknut + lock wire'])
A(f'<text x="610" y="{y4+112}" font-size="11">One per rod: the 2 rods of a lift splay to</text>')
A(f'<text x="610" y="{y4+126}" font-size="11">outriggers either side of the walkway, and</text>')
A(f'<text x="610" y="{y4+140}" font-size="11">are trimmed against the crown load pins</text>')
A(f'<text x="610" y="{y4+154}" font-size="11">(masthead.svg; 1/8 turn = 64 N).</text>')
A(f'<text x="610" y="{y4+176}" font-size="11">Steel rope would swing ~38 mm on the lift</text>')
A(f'<text x="610" y="{y4+190}" font-size="11">(±1.3 kN if held); CFRP ~1 mm (±0.4 kN).</text>')
A(f'<text x="610" y="{y4+212}" font-size="11">One bundle breaks at ~89 kN: factor ~24 alone.</text>')

# ================= 5. Key + numbers =================
A('<text x="905" y="568" class="t">Hanger key (panel 3)</text>')
key(905, 592, [(1, 'Reel socket: clamp, power + data'), (2, '2 anchor eyes for rope grabs'),
               (3, 'Latch lever, flag, lock pin, pilot sw.'), (4, 'E-fuse box tapped off the yard bus'),
               (5, 'Shimmed seat at a chord node (±0.7)'), (6, 'Flared guide fork (±1.02)'),
               (7, 'End sheave (±0.80) to the lifting eye'), (8, 'Centre sheaves (±0.05) from the socket'),
               (9, 'Cone socket (±0.5), 4 in all'), (10, 'Spring-closed hook + latch bar, 5 kN'),
               (11, 'Connector receptacle, float mount'), (12, 'Rescue eyes (±0.66), red'),
               (13, 'Lifting eyes (±0.80)')])
A('<text x="905" y="838" class="t">Numbers (one arm)</text>')
for j, t in enumerate(['8 packs of 2.0 m at 2.1 m pitch: 1.8–18.5 m', 'Load ~2.6 kN; lift ~3.4 kN at 23°',
                       'Yard compression ~3.1 kN; buckling 320 kN', 'Midspan 5.7 kN·m: 3.6 kN/chord, 11 MPa',
                       'Deflection ~7 mm; a pack swap 0.24 kN', 'Worst imbalance ~7 kN·m (quake ~12)',
                       'Hanger ~8 kg; 16 per rig']):
    A(f'<text x="905" y="{860+j*16}" font-size="11.5">{t}</text>')
A('</svg>')
open('yard-hanger.svg', 'w').write('\n'.join(o))
print('wrote yard-hanger.svg')
