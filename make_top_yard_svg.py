# Generates top-yard.svg (rev 22): front elevation, side view, pack hanger station and portable reel hoist.
# Run: python3 make_top_yard_svg.py
o = []
A = o.append
W, H = 1240, 900
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker>'
  '<pattern id="gr" width="6" height="6" patternUnits="userSpaceOnUse"><path d="M0 0H6M0 0V6" stroke="#999" stroke-width="0.8"/></pattern></defs>')
A('<style>.s{stroke:#222;stroke-width:1.5}.l{stroke:#555;stroke-width:1;fill:none}.w{stroke:#555;stroke-width:1.4}'
  '.rope{stroke:#c0392b;stroke-width:1.8;fill:none}.yard{stroke:#c87f0a;stroke-width:3}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')
BOT, PACK, HNG = '#6c3483', '#2c4a7a', '#4a9'


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*14:.0f}" text-anchor="{anchor}">{t}</text>')


def bot(x, y, h, kneel=False):
    """Humanoid icon, feet at (x, y), h px tall."""
    u = h / 26
    legs = (f'<polyline points="{x},{y-8*u} {x-6*u},{y-3*u} {x-2*u},{y}"/><polyline points="{x},{y-8*u} {x+6*u},{y-2*u} {x+9*u},{y}"/>'
            if kneel else f'<line x1="{x}" y1="{y-8*u}" x2="{x-4*u}" y2="{y}"/><line x1="{x}" y1="{y-8*u}" x2="{x+4*u}" y2="{y}"/>')
    A(f'<g stroke="{BOT}" stroke-width="{2.4*u:.1f}" stroke-linecap="round" fill="none">{legs}'
      f'<line x1="{x}" y1="{y-8*u}" x2="{x}" y2="{y-19*u}"/><line x1="{x}" y1="{y-17*u}" x2="{x-6*u}" y2="{y-10*u}"/>'
      f'<line x1="{x}" y1="{y-17*u}" x2="{x+7*u}" y2="{y-9*u}"/></g><circle cx="{x}" cy="{y-22.5*u}" r="{3.4*u:.1f}" fill="{BOT}"/>')


# ---------------- 1. front elevation (wing plane)
k, cx, Zb = 16.5, 330, 92
X = lambda m: cx + m * k
Z = lambda m: 410 - (m - Zb) * k
A('<text x="20" y="30" class="t">1. Front elevation (wing plane), 92–108 m</text>')
A(f'<rect x="{X(-0.7)}" y="{Z(108)}" width="{1.4*k}" height="{(108-Zb)*k}" fill="none" stroke="#888" stroke-width="2"/>')
for z in range(Zb, 108, 1):
    A(f'<line x1="{X(-0.7)}" y1="{Z(z)}" x2="{X(0.7)}" y2="{Z(z+1)}" stroke="#ccc"/>')
A(f'<line x1="{X(0)}" y1="{Z(Zb)}" x2="{X(0)}" y2="{Z(101.6)}" stroke="{BOT}" stroke-width="2" stroke-dasharray="6 3"/>')
for zc in (100.4, 99.6):
    A(f'<line x1="{X(-17)}" y1="{Z(zc)}" x2="{X(17)}" y2="{Z(zc)}" class="yard"/>')
for i in range(-17, 17):
    A(f'<line x1="{X(i)}" y1="{Z(100.4)}" x2="{X(i+1)}" y2="{Z(99.6)}" stroke="#c87f0a" stroke-width="1"/>')
# walkway + rail on top
A(f'<rect x="{X(-17)}" y="{Z(100.4)-3}" width="{34*k}" height="3" fill="url(#gr)" stroke="#777" stroke-width="0.6"/>')
A(f'<line x1="{X(-17)}" y1="{Z(101.5)}" x2="{X(17)}" y2="{Z(101.5)}" stroke="{BOT}" stroke-width="1.6"/>')
for i in range(-17, 18, 2):
    A(f'<line x1="{X(i)}" y1="{Z(100.4)-3}" x2="{X(i)}" y2="{Z(101.5)}" stroke="{BOT}" stroke-width="0.8"/>')
for sx in (-1, 1):
    A(f'<line x1="{X(0)}" y1="{Z(108)}" x2="{X(sx*17)}" y2="{Z(100.4)}" class="w"/>')
A(f'<circle cx="{X(0)}" cy="{Z(108)}" r="4" fill="#555"/>')
# hangers and packs; one port pack being lowered
pitch, pw, LOW = 15 / 8, 1.75, 5
for sx in (-1, 1):
    for i in range(8):
        c = sx * (2 + pitch * (i + 0.5))
        A(f'<path d="M{X(c)-9} {Z(99.6)} h18 l-4 7 h-10 z" fill="{HNG}" stroke="#222"/>')
        A(f'<rect x="{X(c)-4}" y="{Z(100.4)-9}" width="8" height="6" fill="#ddd" stroke="#222" stroke-width="0.8"/>')   # reel socket
        if sx == -1 and i == LOW:
            A(f'<line x1="{X(c)}" y1="{Z(100.4)-5}" x2="{X(c)}" y2="{Z(Zb)}" class="rope"/>')
            A(f'<rect x="{X(c-pw/2)}" y="{Z(99.6)+7}" width="{pw*k}" height="{(99.6-Zb)*k-7}" fill="none" stroke="{PACK}" stroke-dasharray="4 3"/>')
            lx = X(c)
        else:
            A(f'<rect x="{X(c-pw/2)}" y="{Z(99.6)+7}" width="{pw*k}" height="4" fill="#e0a040" class="s"/>')
            A(f'<rect x="{X(c-pw/2)}" y="{Z(99.6)+11}" width="{pw*k}" height="{(99.6-Zb)*k-11}" fill="{PACK}" opacity="0.88"/>')
bot(lx + 4, Z(100.4) - 3, 34, kneel=True)
A(f'<rect x="{lx-12}" y="{Z(100.4)-15}" width="12" height="11" fill="#7fa3d6" class="s"/>')
lab(X(0) + 4, Z(108), X(3), Z(108.6), ['Masthead, 108 m (8 m above yard)'])
lab(X(9), Z(103.9), X(10), Z(106.3), ['Topping lift ~3.0 kN'])
lab(X(6), Z(101.5), X(7.5), Z(104.3), ['Walkway + fall-arrest rail'])
lab(X(8), Z(100.4), X(8.5), Z(102.6), ['Yard truss 34 m, 0.8 m deep'])
lab(lx + 4, Z(102.6), X(-15.5), Z(107.6), ['Bot with its reel at the station'])
lab(X(-2.9), Z(99.6) + 5, X(-6), Z(89.2), ['Fixed hanger (16)'])
lab(lx, Z(93), X(-16.5), Z(89.2), ['Rope to the pack', 'being lowered'])
lab(X(0), Z(93), X(2), Z(89.2), ['Climb rail inside', 'the mast'])
lab(X(12), Z(92.5), X(9), Z(89.2), ['Packs hang 30 m below'])

# ---------------- 2. side view (fore-aft)
sx0, sk = 760, 7.5
SX = lambda m: sx0 + m * sk
SZ = lambda m: 420 - (m - 60) * sk
A(f'<text x="{sx0-90}" y="30" class="t">2. Side view</text>')
A(f'<line x1="{SX(0)}" y1="{SZ(108)}" x2="{SX(0)}" y2="{SZ(60)}" stroke="#888" stroke-width="5"/>')
A(f'<line x1="{SX(-6)}" y1="{SZ(81)}" x2="{SX(6)}" y2="{SZ(81)}" stroke="#e0a040" stroke-width="4"/>')
for s_ in (-1, 1):
    A(f'<polyline points="{SX(0)},{SZ(64)} {SX(s_*6)},{SZ(81)} {SX(0)},{SZ(108)}" fill="none" class="w"/>')
    A(f'<line x1="{SX(0)}" y1="{SZ(100)}" x2="{SX(s_*6)}" y2="{SZ(81)}" stroke="#2e7d32" stroke-width="1.6"/>')
A(f'<rect x="{SX(-0.4)}" y="{SZ(100.4)}" width="{0.8*sk}" height="{0.8*sk}" fill="#c87f0a" class="s"/>')
A(f'<rect x="{SX(-0.15)}" y="{SZ(100)}" width="{0.3*sk}" height="{30*sk*0.33}" fill="{PACK}"/>')
A(f'<rect x="{SX(-1.2)}" y="{SZ(62)-4}" width="{2.4*sk}" height="8" fill="#4a9" class="s"/>')
lab(SX(0) + 4, SZ(100), SX(2.5), SZ(104), ['Yard (end-on)'])
lab(SX(4), SZ(87), SX(6.5), SZ(95), ['Braces: yard tips', 'to spreader tips'])
lab(SX(6), SZ(81), SX(7.5), SZ(79), ['Spreaders ±6 m, 81 m'])
lab(SX(3), SZ(72.5), SX(5), SZ(68), ['Diamond stays', '64 → 81 → 108 m'])
lab(SX(1.2), SZ(62), SX(3), SZ(61), ['Upper collar, 62 m'])
lab(SX(0), SZ(78), SX(-2), SZ(74), ['Wings', '(edge-on)'], 'end')

# ---------------- 3. hanger station, section across the yard
hk, hx, hy = 95, 1010, 175          # px/m; yard top-chord centre
A(f'<text x="{hx-80}" y="30" class="t">3. Hanger station (section)</text>')
YW, YD = 0.5, 0.8
A(f'<rect x="{hx-YW/2*hk}" y="{hy}" width="{YW*hk}" height="{YD*hk}" fill="none" stroke="#c87f0a" stroke-width="3"/>')
A(f'<line x1="{hx-YW/2*hk}" y1="{hy}" x2="{hx+YW/2*hk}" y2="{hy+YD*hk}" stroke="#c87f0a"/>')
A(f'<rect x="{hx-YW/2*hk-4}" y="{hy-7}" width="{YW*hk+8}" height="7" fill="url(#gr)" stroke="#777"/>')        # grating
A(f'<line x1="{hx+YW/2*hk}" y1="{hy-7}" x2="{hx+YW/2*hk}" y2="{hy-0.9*hk}" stroke="{BOT}" stroke-width="2.5"/>')  # rail post
A(f'<rect x="{hx+YW/2*hk-5}" y="{hy-0.9*hk-6}" width="12" height="8" fill="{BOT}"/>')                           # rail head
A(f'<rect x="{hx+YW/2*hk-7}" y="{hy-0.9*hk+3}" width="14" height="10" fill="#555"/>')                           # trolley
# reel socket and reel, rope through the yard to the hanger and pack head
A(f'<rect x="{hx-18}" y="{hy-13}" width="36" height="6" fill="#ddd" class="s"/>')
A(f'<rect x="{hx-17}" y="{hy-40}" width="34" height="27" rx="4" fill="#7fa3d6" class="s"/><circle cx="{hx}" cy="{hy-27}" r="8" fill="#fff" stroke="#222"/>')
A(f'<line x1="{hx}" y1="{hy-19}" x2="{hx}" y2="{hy+YD*hk+46}" class="rope"/>')
# hanger: cone sockets + latch, pack head with cones and eye
hb = hy + YD * hk
A(f'<path d="M{hx-0.45*hk} {hb} h{0.9*hk} v14 h-{0.9*hk} z" fill="{HNG}" stroke="#222"/>')
for dx in (-0.32, 0.32):
    A(f'<path d="M{hx+dx*hk-9} {hb+14} l9 -12 l9 12 z" fill="#fff" stroke="#222"/>')
    A(f'<path d="M{hx+dx*hk-8} {hb+28} l8 -12 l8 12 z" fill="#e0a040" stroke="#222"/>')
A(f'<rect x="{hx-0.5*hk}" y="{hb+28}" width="{hk}" height="10" fill="#e0a040" class="s"/>')
A(f'<circle cx="{hx}" cy="{hb+46}" r="6" fill="#fff" stroke="#222" stroke-width="2"/>')
A(f'<path d="M{hx-0.45*hk} {hb+6} h-14 v26" stroke="#c0392b" stroke-width="4" fill="none"/>')                      # latch hook
A(f'<line x1="{hx-0.45*hk-14}" y1="{hb+6}" x2="{hx-0.45*hk-14}" y2="{hy-30}" stroke="#555" stroke-width="2.5"/>')   # lever rod up
A(f'<rect x="{hx-0.45*hk-24}" y="{hy-44}" width="20" height="14" fill="#f2c94c" class="s"/>')                    # flag / handle
for j in range(4):
    A(f'<line x1="{hx}" y1="{hb+52+j*34}" x2="{hx}" y2="{hb+82+j*34}" stroke="{PACK}" stroke-width="6" stroke-linecap="round"/>')
    A(f'<circle cx="{hx}" cy="{hb+84+j*34}" r="2.5" fill="#222"/>')
bot(hx - 0.36 * hk, hy - 7, 62, kneel=True)
A(f'<path d="M{hx-0.36*hk} {hy-45} Q{hx} {hy-110} {hx+YW/2*hk} {hy-0.9*hk+8}" stroke="#555" stroke-width="1.2" fill="none" stroke-dasharray="3 2"/>')
RX = hx + 80
for (px, py, ly, lines) in ((hx + YW / 2 * hk + 6, hy - 0.9 * hk, hy - 125, ['Fall-arrest rail', '+ captive trolley']),
                            (hx - 0.36 * hk, hy - 52, hy - 88, ['Bot, tethered', 'to the trolley']),
                            (hx - 0.45 * hk - 4, hy - 38, hy - 52, ['Latch handle', 'with position flag']),
                            (hx + 17, hy - 22, hy - 16, ['Reel hoist in', 'its socket']),
                            (hx + YW / 2 * hk, hy + 40, hy + 30, ['Yard truss', '0.5 x 0.8 m']),
                            (hx + 0.45 * hk, hb + 8, hb - 2, ['Hanger: 4 cone', 'sockets + latch']),
                            (hx + 0.5 * hk, hb + 33, hb + 36, ['Pack head: cones', '+ lifting eye']),
                            (hx + 3, hb + 100, hb + 96, ['Pack: 30 x 1 m', 'hinged panels'])):
    lab(px, py, RX, ly, lines)

# ---------------- 4. portable reel hoist
ry = 610
A(f'<text x="20" y="{ry-20}" class="t">4. Portable reel hoist (~12 kg; 2 + 1 spare)</text>')
A(f'<rect x="40" y="{ry}" width="1160" height="270" fill="none" stroke="#999" stroke-dasharray="4 3"/>')
by = ry + 130
A(f'<rect x="90" y="{by-70}" width="520" height="150" rx="10" fill="#eef3f8" stroke="#222"/>')
A(f'<rect x="130" y="{by-50}" width="150" height="100" rx="6" fill="#bbb" class="s"/>')
for j in range(7):
    A(f'<line x1="{140+j*20}" y1="{by-48}" x2="{140+j*20}" y2="{by+48}" stroke="#c0392b" stroke-width="2"/>')
A(f'<text x="290" y="{by-56}" font-size="11">drum Ø0.12 m, ~105 m rope</text>')
A(f'<rect x="300" y="{by-30}" width="80" height="60" fill="#7fa3d6" class="s"/><text x="340" y="{by+4}" text-anchor="middle" font-size="11">worm</text>')
A(f'<rect x="395" y="{by-30}" width="80" height="60" fill="#7fa3d6" class="s"/><text x="435" y="{by+4}" text-anchor="middle" font-size="11">motor</text>')
A(f'<rect x="490" y="{by-25}" width="40" height="50" fill="#c0392b" class="s"/><text x="510" y="{by+42}" text-anchor="middle" font-size="11">brake</text>')
A(f'<rect x="545" y="{by-25}" width="50" height="50" fill="#ddd" class="s"/><text x="570" y="{by+4}" text-anchor="middle" font-size="10">enc.</text>')
A(f'<line x1="280" y1="{by}" x2="300" y2="{by}" stroke="#555" stroke-width="4"/><line x1="380" y1="{by}" x2="395" y2="{by}" stroke="#555" stroke-width="4"/><line x1="475" y1="{by}" x2="490" y2="{by}" stroke="#555" stroke-width="4"/>')
A(f'<rect x="150" y="{by-90}" width="110" height="16" fill="#ddd" class="s"/><text x="205" y="{by-78}" text-anchor="middle" font-size="10">level wind</text>')
A(f'<rect x="90" y="{by+80}" width="520" height="18" fill="#888" class="s"/><text x="350" y="{by+93}" text-anchor="middle" font-size="11" fill="#fff" style="stroke:none">clamp + power/data plug into the reel socket</text>')
A(f'<rect x="190" y="{by+56}" width="30" height="16" fill="#f2c94c" class="s"/><text x="226" y="{by+68}" font-size="10">load-cell guide</text>')
A(f'<path d="M205 {by+50} V{by+125}" class="rope" marker-end="url(#ar)"/><text x="214" y="{by+120}" font-size="11">rope down through the socket to the pack head</text>')
specs = ['2.5 mm stainless wire rope, breaks at ~3.5 kN:',
         '   factor ~15 on the 0.23 kN pack (stainless for UV)',
         '~14 N·m at the drum, 16 rpm for 0.1 m/s; ~40 W;',
         '   ~6 Wh per 100 m; ~16 min to lower or hoist',
         'Self-locking worm + spring brake hold the pack',
         '   if power fails',
         'Load cell + encoder: slow, automatic approach',
         '   to the tray and to the hanger cones',
         'Powered from the socket (array harness):',
         '   the bot carries no extra battery']
for j, t in enumerate(specs):
    A(f'<text x="{740+(14 if t.startswith(" ") else 0)}" y="{ry+40+j*20}" font-size="12">{t.strip()}</text>')
A('</svg>')
open('top-yard.svg', 'w').write('\n'.join(o))
