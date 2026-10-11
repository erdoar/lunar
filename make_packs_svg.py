# Generates packs.svg (rev 10: concertina pack deploy / retract / stack / exchange). Run: python3 make_packs_svg.py
o = []
A = o.append
W, H = 1240, 760
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12.5">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker>'
  '<pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern></defs>')
A('<style>.s{stroke:#222;stroke-width:1.5}.l{stroke:#555;stroke-width:1;fill:none}.panel{stroke:#2c4a7a;stroke-width:5;stroke-linecap:round}'
  '.cord{stroke:#c0392b;stroke-width:1.5;fill:none}.hoist{stroke:#555;stroke-width:1.2}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*14:.0f}" text-anchor="{anchor}">{t}</text>')


def topbar(x, y, w=90):
    A(f'<rect x="{x-w/2}" y="{y}" width="{w}" height="22" fill="#e0a040" class="s"/>')
    A(f'<circle cx="{x-16}" cy="{y+11}" r="7" fill="#fff" class="s"/><circle cx="{x+16}" cy="{y+11}" r="7" fill="#fff" class="s"/>')
    A(f'<rect x="{x-32}" y="{y+22}" width="64" height="12" fill="#4a9" class="s"/>')       # carrier
    return y + 34


TOP = 80
# ---------- (a) deployed: side + front
x0 = 70
A(f'<text x="20" y="34" class="t">1. Deployed (side view and front)</text>')
yb = topbar(x0, TOP)
n, ph = 8, 46
for i in range(n):
    y1, y2 = yb + i * ph, yb + (i + 1) * ph
    if i == 4:
        A(f'<path d="M{x0-14} {y1+18} l28 -8 M{x0-14} {y1+26} l28 -8" stroke="#222" stroke-width="1.5"/>')
        continue
    A(f'<line x1="{x0}" y1="{y1+2}" x2="{x0}" y2="{y2-2}" class="panel"/>')
    A(f'<circle cx="{x0}" cy="{y2}" r="3" fill="#222"/><circle cx="{x0+9}" cy="{y2}" r="4" fill="#fff" stroke="#c0392b" stroke-width="1.5"/>')
ybot = yb + n * ph
A(f'<rect x="{x0-10}" y="{ybot}" width="26" height="10" fill="#e0a040" class="s"/>')
A(f'<path d="M{x0+16} {yb-23} V{yb} L{x0+9} {yb+8} V{ybot}" class="cord"/>')
lab(x0 - 30, TOP + 11, x0 - 40, TOP - 18, ['Top bar (station)'], 'start')
lab(x0 + 16, TOP + 11, x0 + 60, TOP + 2, ['Lift-cord drum'])
lab(x0 + 32, yb - 6, x0 + 60, yb + 16, ['Carrier (latched)'])
lab(x0 + 13, yb + 3 * ph, x0 + 40, yb + 3 * ph + 30, ['Ceramic guide', 'ring at fold'])
lab(x0, yb + ph, x0 + 40, yb + ph + 22, ['Hinge (180° stop)'])
lab(x0 + 16, ybot + 5, x0 + 40, ybot + 30, ['Bottom bar'])
A(f'<text x="{x0-50}" y="{ybot+60}" font-size="11.5">30 panels x 1 m = 30 m (shortened)</text>')
# front view
fx, fw = 255, 70
A(f'<rect x="{fx}" y="{yb}" width="{fw}" height="{n*ph}" fill="#2c4a7a"/>')
for i in range(1, n):
    A(f'<line x1="{fx}" y1="{yb+i*ph}" x2="{fx+fw}" y2="{yb+i*ph}" stroke="#9cc0ea"/>')
for cx_ in (fx + 8, fx + fw - 8):
    A(f'<line x1="{cx_}" y1="{yb-10}" x2="{cx_}" y2="{ybot}" stroke="#c0392b" stroke-width="1.2" stroke-dasharray="4 3"/>')
A(f'<rect x="{fx-4}" y="{yb-12}" width="{fw+8}" height="12" fill="#4a9" class="s"/><rect x="{fx-2}" y="{ybot}" width="{fw+4}" height="8" fill="#e0a040" class="s"/>')
A(f'<path d="M{fx} {ybot+24} H{fx+fw}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{fx+fw/2}" y="{ybot+40}" text-anchor="middle">1–3 m (2 m)</text>')
A(f'<text x="{fx+fw/2}" y="{yb-20}" text-anchor="middle" font-size="11.5">front</text>')

# ---------- (b) retracting
x1 = 420
A(f'<text x="{x1-90}" y="34" class="t">2. Retracting (cords wind in)</text>')
yb = topbar(x1, TOP)
for i in range(3):
    y1, y2 = yb + i * ph, yb + (i + 1) * ph
    A(f'<line x1="{x1}" y1="{y1+2}" x2="{x1}" y2="{y2-2}" class="panel"/>')
    A(f'<circle cx="{x1+9}" cy="{y2}" r="4" fill="#fff" stroke="#c0392b" stroke-width="1.5"/>')
yz = yb + 3 * ph
pts = []
for i in range(9):
    pts.append((x1 + (0 if i % 2 == 0 else 34), yz + i * 11))
A('<polyline points="' + ' '.join(f'{x},{y}' for x, y in pts) + '" fill="none" stroke="#2c4a7a" stroke-width="5" stroke-linejoin="round"/>')
ybar = pts[-1][1] + 4
A(f'<rect x="{x1-10}" y="{ybar}" width="56" height="10" fill="#e0a040" class="s"/>')
A(f'<path d="M{x1+16} {yb-23} V{yb} L{x1+9} {yb+8} V{ybar}" class="cord"/>')
A(f'<path d="M{x1+70} {ybar+10} V{yz}" stroke="#222" stroke-width="1.5" marker-end="url(#ar)"/>')
lab(x1 + 34, yz + 11, x1 + 85, yz + 40, ['Folds gather from', 'the bottom up'])
lab(x1 + 30, yz + 7 * 11, x1 + 85, yz + 92, ['Alternate hinges sprung', 'toward their fold'])
lab(x1 + 16, yb - 23, x1 + 60, yb - 50, ['Drums wind in'])
A(f'<text x="{x1-60}" y="{ybar+60}" font-size="11.5">Deploy is the reverse: pay out, gravity</text>')
A(f'<text x="{x1-60}" y="{ybar+75}" font-size="11.5">unfolds it (~0.1 m/s, ~5 min per pack)</text>')

# ---------- (c) folded stack
x2 = 690
A(f'<text x="{x2-70}" y="34" class="t">3. Stowed stack</text>')
yb = topbar(x2, TOP)
pts = [(x2 - 30 + (0 if i % 2 == 0 else 60), yb + 2 + i * 5) for i in range(16)]
A('<polyline points="' + ' '.join(f'{x},{y}' for x, y in pts) + '" fill="none" stroke="#2c4a7a" stroke-width="3" stroke-linejoin="round"/>')
A(f'<rect x="{x2-34}" y="{pts[-1][1]+3}" width="68" height="8" fill="#e0a040" class="s"/>')
lab(x2 + 30, yb + 40, x2 + 55, yb + 80, ['~2 x 1 x 0.7 m,', '~140 kg (0.23 kN', 'on the Moon)'])
A(f'<text x="{x2-60}" y="{yb+250}" font-size="11.5">Stays latched while other</text><text x="{x2-60}" y="{yb+265}" font-size="11.5">packs keep producing.</text>')

# ---------- (d) exchange: carrier + stack lowered on hoist lines
x3, gy = 1010, 640
A(f'<text x="{x3-110}" y="34" class="t">4. Exchange: lowered alone</text>')
A(f'<rect x="{x3-45}" y="{TOP}" width="90" height="22" fill="#e0a040" class="s"/>')
for sx in (-26, 26):
    A(f'<circle cx="{x3+sx}" cy="{TOP+11}" r="6" fill="#fff" class="s"/>')
    A(f'<line x1="{x3+sx}" y1="{TOP+17}" x2="{x3+sx}" y2="{gy-70}" class="hoist"/>')
A(f'<rect x="{x3-32}" y="{gy-70}" width="64" height="12" fill="#4a9" class="s"/>')
pts = [(x3 - 30 + (0 if i % 2 == 0 else 60), gy - 56 + i * 3.4) for i in range(14)]
A('<polyline points="' + ' '.join(f'{x:.0f},{y:.0f}' for x, y in pts) + '" fill="none" stroke="#2c4a7a" stroke-width="3" stroke-linejoin="round"/>')
A(f'<rect x="{x3-50}" y="{gy-10}" width="100" height="10" fill="#9fb4c7" class="s"/><circle cx="{x3-36}" cy="{gy}" r="5" fill="#555"/><circle cx="{x3+36}" cy="{gy}" r="5" fill="#555"/>')
A(f'<rect x="{x3-150}" y="{gy+5}" width="300" height="30" fill="url(#g)"/><line x1="{x3-150}" y1="{gy+5}" x2="{x3+150}" y2="{gy+5}" stroke="#222"/>')
A(f'<path d="M{x3+70} {TOP+60} V{gy-80}" stroke="#222" stroke-width="1.5" marker-end="url(#ar)" marker-start="url(#ar)"/>')
lab(x3 + 26, TOP + 140, x3 + 80, TOP + 160, ['Hoist lines (2)', 'from station drums'])
lab(x3 - 32, gy - 64, x3 - 90, gy - 110, ['Carrier + folded', 'pack, 4 cones +', 'captive latches'], 'end')
lab(x3 + 50, gy - 5, x3 + 80, gy - 40, ['Ground cart (or the', 'deck, for inner packs)'])
lab(x3 - 45, TOP + 11, x3 - 100, TOP + 50, ['Wing top bar'], 'end')
A(f'<text x="{x3-140}" y="{gy+60}" font-size="11.5">Mast parked at the maintenance azimuth. The pack weight stays on</text>')
A(f'<text x="{x3-140}" y="{gy+75}" font-size="11.5">the top bar until it lands; swap packs in port/starboard pairs.</text>')
A('</svg>')
open('packs.svg', 'w').write('\n'.join(o))
