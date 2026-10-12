# Generates wings.svg (rev 23): service bots swap one pack at a time on two ropes from a twin-drum reel; no halyards.
# Run: python3 make_wings_svg.py
from math import sqrt

o = []
A = o.append
W, H = 1240, 820
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker>'
  '<pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern></defs>')
A('<style>.s{stroke:#222;stroke-width:1.5}.l{stroke:#555;stroke-width:1;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')
BOT, ROPE, PACK, YARD = '#6c3483', '#c0392b', '#2c4a7a', '#e0a040'


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*14:.0f}" text-anchor="{anchor}">{t}</text>')


def bot(x, y, h=26, reel=True):
    """Humanoid icon standing with its feet at (x, y), h px tall (drawn enlarged)."""
    u = h / 26
    A(f'<g stroke="{BOT}" stroke-width="{2.4*u:.1f}" stroke-linecap="round" fill="none">'
      f'<line x1="{x}" y1="{y-8*u}" x2="{x-4*u}" y2="{y}"/><line x1="{x}" y1="{y-8*u}" x2="{x+4*u}" y2="{y}"/>'
      f'<line x1="{x}" y1="{y-8*u}" x2="{x}" y2="{y-19*u}"/><line x1="{x}" y1="{y-17*u}" x2="{x-6*u}" y2="{y-10*u}"/>'
      f'<line x1="{x}" y1="{y-17*u}" x2="{x+6*u}" y2="{y-11*u}"/></g>'
      f'<circle cx="{x}" cy="{y-22.5*u}" r="{3.4*u:.1f}" fill="{BOT}"/>')
    if reel:
        A(f'<rect x="{x+5*u:.1f}" y="{y-6*u:.1f}" width="{7*u:.1f}" height="{6*u:.1f}" fill="#7fa3d6" stroke="#222" stroke-width="1"/>')


# ================= LEFT: elevation at the maintenance azimuth =================
e, cx, gy = 6.4, 330, 780
X = lambda m: cx + m * e
Z = lambda m: gy - m * e
A('<text x="20" y="30" class="t">Swapping one pack (rev 23): elevation at the maintenance azimuth</text>')
A('<text x="20" y="48" fill="#555">Bots drawn enlarged. Struts and stays lie 30° out of the wing plane (drawn faint), so a lowered pack passes them.</text>')
A(f'<rect x="{X(-40)}" y="{gy}" width="{80*e}" height="24" fill="url(#g)"/><line x1="{X(-40)}" y1="{gy}" x2="{X(40)}" y2="{gy}" stroke="#222"/>')
# faint bracing (out of plane)
for fx in (-26, 26):
    A(f'<line x1="{X(fx)}" y1="{gy}" x2="{X(0)}" y2="{Z(35)}" stroke="#bbb" stroke-width="3"/>')
    A(f'<line x1="{X(fx)}" y1="{gy}" x2="{X(fx*0.06)}" y2="{Z(62)}" stroke="#d7c0e6" stroke-width="1.2"/>')
# mast, collars, base frame, foundation
A(f'<rect x="{X(-0.7)}" y="{Z(108)}" width="{1.4*e}" height="{108*e}" fill="#e8e8e8" stroke="#888"/>')
A(f'<line x1="{X(0)}" y1="{Z(1.6)}" x2="{X(0)}" y2="{Z(100.6)}" stroke="{BOT}" stroke-width="1.6" stroke-dasharray="5 3"/>')
for c in (35, 62):
    A(f'<rect x="{X(-1.4)}" y="{Z(c)-3}" width="{2.8*e}" height="6" fill="#4a9" class="s"/>')
A(f'<rect x="{X(-1.5)}" y="{Z(1.5)-2}" width="{3*e}" height="4" fill="#e67e22"/><rect x="{X(-1)}" y="{gy-4}" width="{2*e}" height="4" fill="#7d8790"/>')
# yard, walkway rail, topping lifts
A(f'<rect x="{X(-18.7)}" y="{Z(100.4)}" width="{37.4*e}" height="{0.8*e}" fill="{YARD}" class="s"/>')
A(f'<line x1="{X(-18.7)}" y1="{Z(101.6)}" x2="{X(18.7)}" y2="{Z(101.6)}" stroke="{BOT}" stroke-width="1.2"/>')
for i in range(-18, 19, 2):
    A(f'<line x1="{X(i)}" y1="{Z(100.4)}" x2="{X(i)}" y2="{Z(101.6)}" stroke="{BOT}" stroke-width="0.8"/>')
for sx in (-1, 1):
    A(f'<line x1="{X(0)}" y1="{Z(108)}" x2="{X(sx*18.5)}" y2="{Z(100.4)}" stroke="#555"/>')
# packs: 8 per wing between 1.8 and 18.5 m; one port pack lowered
pitch, pw = 2.1, 2.0
LOW = 5                       # index of the port pack being swapped
top_now = 48                  # m, current height of its pack head
trays = []
for sx in (-1, 1):
    xl, xr = sorted((X(sx * 1.8), X(sx * 18.5)))
    A(f'<rect x="{xl-2}" y="{Z(1.5)}" width="{xr-xl+4}" height="4" fill="#7d8790"/>')
    for leg in (2.4, 10.2, 18.0):
        A(f'<line x1="{X(sx*leg)}" y1="{Z(1.5)}" x2="{X(sx*leg)}" y2="{gy}" stroke="#7d8790" stroke-width="2"/>')
    for i in range(8):
        c = sx * (2.8 + pitch * i)
        x0 = X(c - pw / 2)
        A(f'<rect x="{X(c)-3}" y="{Z(100.4)}" width="6" height="4" fill="#4a9" stroke="#222" stroke-width="0.8"/>')   # hanger
        if sx == -1 and i == LOW:
            A(f'<rect x="{x0}" y="{Z(100)}" width="{pw*e}" height="{30*e}" fill="none" stroke="{PACK}" stroke-dasharray="4 3"/>')
            for dx in (-0.8, 0.8):
                A(f'<line x1="{X(c+dx)}" y1="{Z(100.4)}" x2="{X(c+dx)}" y2="{Z(top_now)}" stroke="{ROPE}" stroke-width="1.3"/>')
            A(f'<rect x="{x0}" y="{Z(top_now)}" width="{pw*e}" height="{30*e}" fill="{PACK}"/>')
            A(f'<rect x="{x0-1}" y="{Z(top_now)-2}" width="{pw*e+2}" height="3" fill="{YARD}"/>')
            A(f'<path d="M{X(c)+16} {Z(top_now)+30} V{Z(top_now)+90}" stroke="#222" stroke-width="1.5" marker-end="url(#ar)"/>')
            low_x = X(c)
        else:
            A(f'<rect x="{x0}" y="{Z(100)}" width="{pw*e}" height="{30*e}" fill="{PACK}" opacity="0.92"/>')
# new folded pack waiting next to the port tray
A(f'<rect x="{X(-21)}" y="{Z(1.5)-6}" width="{pw*e}" height="6" fill="{PACK}" opacity="0.7" class="s"/>')
# bots: one at the station on the yard with its reel, one climbing inside the mast
bot(low_x + 2, Z(101.6), 28)
bot(X(0), Z(55), 26, reel=False)
# labels, left
lab(low_x + 6, Z(103.6), X(-24), Z(107), ['Bot at the station: reel hoist', 'clipped into the socket'], 'end')
lab(X(-12.3), Z(78), X(-24), Z(82), ['Two ropes, 0.1 m/s'], 'end')
lab(X(-13), Z(33), X(-24), Z(40), ['One pack lowered,', '~16 min each way'], 'end')
lab(X(0) - 6, Z(53), X(-24), Z(58), ['Second bot climbing unladen', 'inside the mast core'], 'end')
lab(X(-12.3), Z(1.8), X(-24), Z(12), ['Lands in its tray slot,', 'then folds itself up'], 'end')
lab(X(-20), Z(1.5) - 6, X(-30), Z(5.5), ['New folded pack', 'waits by the tray'], 'end')
# labels, right
lab(X(10), Z(101.6), X(20), Z(106), ['Walkway + fall-arrest rail on the yard'])
lab(X(14), Z(100.4) + 4, X(20), Z(97), ['16 fixed pack hangers under the yard'])
lab(X(12), Z(85), X(20), Z(85), ['Starboard wing: 8 packs,', 'still working'])
lab(X(1.4), Z(62), X(20), Z(64), ['Upper collar 62 m'])
lab(X(1.4), Z(35), X(20), Z(37), ['Strut collar 35 m'])
lab(X(15), Z(1.5), X(20), Z(14), ['Landing trays (8 slots each)'])
lab(X(1.5), Z(1.5), X(20), Z(-1.2), ['Base frame: bot dock + hatch'])

# ================= RIGHT TOP: plan section of the mast with a bot in the core =================
pk, pcx, pcy = 165, 945, 205
A(f'<text x="800" y="30" class="t">Inside the mast: plan section</text>')
face = 1.4
R = face / sqrt(3)
verts = [(pcx + R * pk * sx, pcy + R * pk * sy) for sx, sy in ((0, -1), (sqrt(3) / 2, 0.5), (-sqrt(3) / 2, 0.5))]
A('<polygon points="' + ' '.join(f'{x:.0f},{y:.0f}' for x, y in verts) + '" fill="#f4f4f4" stroke="#888" stroke-width="2"/>')
for x, y in verts:
    A(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{0.06*pk:.0f}" fill="#888" stroke="#222"/>')
rin = face / (2 * sqrt(3)) - 0.06
A(f'<circle cx="{pcx}" cy="{pcy}" r="{rin*pk:.0f}" fill="none" stroke="#2e7d32" stroke-width="1.5" stroke-dasharray="6 4"/>')
# climb rail on the bottom face, trolley, bot from above
ry = pcy + 0.5 * R * pk - 6
A(f'<rect x="{pcx-12}" y="{ry-4}" width="24" height="10" fill="#555"/><rect x="{pcx-8}" y="{ry-14}" width="16" height="10" fill="{BOT}" opacity="0.6" stroke="#222"/>')
A(f'<ellipse cx="{pcx}" cy="{pcy+6}" rx="{0.225*pk:.0f}" ry="{0.15*pk:.0f}" fill="{BOT}" opacity="0.35" stroke="{BOT}" stroke-width="2"/>')
A(f'<circle cx="{pcx}" cy="{pcy+2}" r="{0.1*pk:.0f}" fill="{BOT}" opacity="0.8"/>')
A(f'<path d="M{verts[2][0]:.0f} {verts[2][1]+22:.0f} H{verts[1][0]:.0f}" class="l" marker-start="url(#ar)" marker-end="url(#ar)"/><text x="{pcx}" y="{verts[2][1]+36:.0f}" text-anchor="middle">1.4 m face</text>')
lab(pcx + rin * pk * 0.7, pcy - rin * pk * 0.7, pcx + 110, pcy - 110, ['Clear core ~Ø0.69 m', '(members on faces only)'])
lab(pcx + 0.225 * pk, pcy + 6, pcx + 110, pcy - 40, ['Bot ~0.45 x 0.3 m; a reel', 'rides as a chest pack'])
lab(pcx + 12, ry, pcx + 110, pcy + 50, ['Climb rail + captive', 'fall-arrest trolley'])
A(f'<text x="800" y="{pcy+150}" font-size="11.5">Collars, V-links, stays and spreaders are all outside the</text>')
A(f'<text x="800" y="{pcy+165}" font-size="11.5">mast, so the climb inside never has to pass them.</text>')

# ================= RIGHT BOTTOM: sequence and balance =================
sx0, sy0 = 800, 420
A(f'<text x="{sx0}" y="{sy0}" class="t">Pack swap, ~1.2 h with one bot</text>')
steps = ['1. Park at the maintenance azimuth; new pack to the tray.',
         '2. Bot climbs inside the mast unladen (~11 min), clips to the',
         '    yard rail, takes a reel from the garage, walks out.',
         '3. Reel into the socket, 2 ropes to the pack head; take the',
         '    load, open the hanger latch.',
         '4. Lower ~16 min: past its neighbours, clear of the collars;',
         '    it lands in its slot and folds itself up.',
         '5. Rover or crew swaps the folded pack in the tray.',
         '6. Hoist ~16 min: it unfolds as it lifts; guide forks square',
         '    it, cones seat, bot latches, parks the reel, climbs down.',
         'Two ropes 1.6 m apart hold it square (≤1.3° at 100 m): no spin.']
for j, t in enumerate(steps):
    A(f'<text x="{sx0+(14 if t.startswith(" ") else 0)}" y="{sy0+22+j*17}">{t.strip()}</text>')
by = sy0 + 22 + len(steps) * 17 + 20
A(f'<text x="{sx0}" y="{by}" class="t">Balance</text>')
for j, t in enumerate(['A pack on its ropes still hangs from the yard: no change.',
                       'Pack landed: ≤3.6 kN·m; with the bot at the far tip ≤6 kN·m,',
                       'half the ~12 kN·m quake case. First fit alternates sides.',
                       '',
                       'Deleted: halyards, wing winch, trim sheaves, wing top bars,',
                       'docks and ballast pallet. The rest of the array keeps working.']):
    A(f'<text x="{sx0}" y="{by+20+j*17}"{" fill=\"#555\"" if j > 3 else ""}>{t}</text>')
A('</svg>')
open('wings.svg', 'w').write('\n'.join(o))
