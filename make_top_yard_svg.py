# Generates top-yard.svg (rev 25): front elevation, side view, two-rope hanger station and twin-drum reel hoist.
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
            for dx in (-0.8, 0.8):
                A(f'<line x1="{X(c+dx)}" y1="{Z(99.6)+4}" x2="{X(c+dx)}" y2="{Z(Zb)}" class="rope"/>')
            A(f'<line x1="{X(c-0.8)}" y1="{Z(99.6)+4}" x2="{X(c+0.8)}" y2="{Z(99.6)+4}" class="rope"/>')
            A(f'<rect x="{X(c-pw/2)}" y="{Z(99.6)+7}" width="{pw*k}" height="{(99.6-Zb)*k-7}" fill="none" stroke="{PACK}" stroke-dasharray="4 3"/>')
            lx = X(c)
        else:
            A(f'<rect x="{X(c-pw/2)}" y="{Z(99.6)+7}" width="{pw*k}" height="4" fill="#e0a040" class="s"/>')
            A(f'<rect x="{X(c-pw/2)}" y="{Z(99.6)+11}" width="{pw*k}" height="{(99.6-Zb)*k-11}" fill="{PACK}" opacity="0.88"/>')
bot(lx + 4, Z(100.4) - 3, 34, kneel=True)
A(f'<rect x="{X(-2.6)}" y="{Z(100.4)-16}" width="{1.6*k}" height="13" fill="#d5d8dc" class="s"/>')
lab(X(-1.8), Z(100.4) - 16, X(-3.5), Z(104.2), ['Reel garage (2 reels)'])
A(f'<rect x="{lx-12}" y="{Z(100.4)-15}" width="12" height="11" fill="#7fa3d6" class="s"/>')
lab(X(0) + 4, Z(108), X(3), Z(108.6), ['Masthead, 108 m (8 m above yard)'])
lab(X(9), Z(103.9), X(10), Z(106.3), ['Topping lift ~3.0 kN'])
lab(X(6), Z(101.5), X(7.5), Z(104.3), ['Walkway + fall-arrest rail'])
lab(X(8), Z(100.4), X(8.5), Z(102.6), ['Yard truss 34 m, 0.8 m deep'])
lab(lx + 4, Z(102.6), X(-15.5), Z(107.6), ['Bot with a reel at the station'])
lab(X(-2.9), Z(99.6) + 5, X(-6), Z(89.2), ['Fixed hanger (16)'])
lab(lx, Z(93), X(-16.5), Z(89.2), ['Two ropes to the', 'pack being lowered'])
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

# ---------------- 3. hanger station, front view along the yard (two ropes)
hk, hx, hy = 105, 1075, 150
A(f'<text x="{hx-150}" y="30" class="t">3. Hanger station (front view)</text>')
L2 = 1.2
A(f'<rect x="{hx-L2*hk}" y="{hy-7}" width="{2*L2*hk}" height="7" fill="url(#gr)" stroke="#777"/>')            # walkway
A(f'<line x1="{hx-L2*hk}" y1="{hy-0.9*hk}" x2="{hx+L2*hk}" y2="{hy-0.9*hk}" stroke="{BOT}" stroke-width="3"/>')  # rail
hb = hy + 0.8 * hk
for yy in (hy, hb):
    A(f'<line x1="{hx-L2*hk}" y1="{yy}" x2="{hx+L2*hk}" y2="{yy}" class="yard"/>')
for j in range(-3, 3):
    A(f'<line x1="{hx+j*0.4*hk}" y1="{hy}" x2="{hx+(j+1)*0.4*hk}" y2="{hb}" stroke="#c87f0a"/>')
# reel in its socket, bot kneeling beside it
A(f'<rect x="{hx-20}" y="{hy-13}" width="40" height="6" fill="#ddd" class="s"/>')
A(f'<rect x="{hx-20}" y="{hy-38}" width="40" height="25" rx="4" fill="#7fa3d6" class="s"/>')
for dx in (-9, 9):
    A(f'<circle cx="{hx+dx}" cy="{hy-26}" r="7" fill="#fff" stroke="#222"/>')
bot(hx - 0.55 * hk, hy - 7, 66, kneel=True)
A(f'<path d="M{hx-0.55*hk} {hy-50} Q{hx-0.7*hk} {hy-0.9*hk-20} {hx-0.85*hk} {hy-0.9*hk}" stroke="#555" stroke-width="1.2" fill="none" stroke-dasharray="3 2"/>')
A(f'<rect x="{hx-0.85*hk-7}" y="{hy-0.9*hk-4}" width="14" height="9" fill="#555"/>')
# hanger plate, 4 sheaves, guide forks
A(f'<rect x="{hx-1.05*hk}" y="{hb}" width="{2.1*hk}" height="12" fill="{HNG}" stroke="#222"/>')
ys = hb + 20
A(f'<path d="M{hx-9} {hy-19} V{ys} H{hx-0.8*hk} V{hb+86} M{hx+9} {hy-19} V{ys} H{hx+0.8*hk} V{hb+86}" class="rope"/>')
for x_ in (hx - 9, hx + 9, hx - 0.8 * hk, hx + 0.8 * hk):
    A(f'<circle cx="{x_}" cy="{ys}" r="6" fill="#fff" stroke="#222" stroke-width="1.3"/>')
for sx in (-1, 1):
    xf = hx + sx * 1.02 * hk
    A(f'<path d="M{xf-5} {hb+12} V{hb+40} L{xf-16} {hb+58} M{xf+5} {hb+12} V{hb+40} L{xf+16} {hb+58}" stroke="#2e7d32" stroke-width="3" fill="none"/>')
# pack head (hanging a little below, arriving): cones, end tabs, 2 eyes; pack below
yh = hb + 86
A(f'<rect x="{hx-1.0*hk}" y="{yh}" width="{2.0*hk}" height="10" fill="#e0a040" class="s"/>')
for sx in (-1, 1):
    A(f'<rect x="{hx+sx*1.02*hk-4}" y="{yh-14}" width="8" height="14" fill="#e0a040" stroke="#222"/>')
    A(f'<path d="M{hx+sx*0.5*hk-8} {yh} l8 -12 l8 12 z" fill="#e0a040" stroke="#222"/>')
    A(f'<path d="M{hx+sx*0.5*hk-9} {hb+12} l9 12 l9 -12 z" fill="#fff" stroke="#222"/>')
    A(f'<circle cx="{hx+sx*0.8*hk}" cy="{yh-5}" r="5" fill="#fff" stroke="#222" stroke-width="2"/>')
    A(f'<circle cx="{hx+sx*0.66*hk}" cy="{yh-4}" r="4" fill="#fff" stroke="#c0392b" stroke-width="2"/>')   # rescue eye
A(f'<rect x="{hx-1.0*hk}" y="{yh+10}" width="{2.0*hk}" height="64" fill="{PACK}" opacity="0.9"/>')
for j in range(1, 3):
    A(f'<line x1="{hx-1.0*hk}" y1="{yh+10+j*30}" x2="{hx+1.0*hk}" y2="{yh+10+j*30}" stroke="#7fa3d6"/>')
A(f'<path d="M{hx-1.2*hk} {yh+40} V{yh-6}" stroke="#222" stroke-width="1.5" marker-end="url(#ar)"/>')
A(f'<text x="{hx-1.2*hk-4}" y="{yh+56}" text-anchor="end" font-size="11">hoisting</text>')
# numbered key
def num(n, x, y):
    A(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="9" fill="#fff" stroke="#222"/><text x="{x:.0f}" y="{y+4:.0f}" text-anchor="middle" font-size="10.5" font-weight="bold" style="stroke:none">{n}</text>')
pts = [(hx + 26, hy - 34), (hx - 0.55 * hk - 16, hy - 66), (hx - 0.85 * hk, hy - 0.9 * hk - 14), (hx + 0.8 * hk + 14, ys - 12),
       (hx + 1.02 * hk + 22, hb + 40), (hx + 0.5 * hk + 14, yh - 14), (hx + 0.8 * hk + 14, yh + 4), (hx + 0.6 * hk, yh + 44)]
for n, (x_, y_) in enumerate(pts, 1):
    num(n, x_, y_)
keys = ['Twin-drum reel in its socket', 'Bot, tethered to the rail trolley', 'Yard fall-arrest rail', '4 passive sheaves in the hanger',
        'Flared guide forks (squares the head)', 'Cones into the hanger sockets', '2 lifting eyes (+2 red rescue eyes)', 'Pack hangs square on 2 ropes']
ky = yh + 96
for j, t in enumerate(keys):
    num(j + 1, hx - 140, ky + j * 20)
    A(f'<text x="{hx-124}" y="{ky+j*20+4}" font-size="11.5">{t}</text>')

# ---------------- 4. twin-drum reel hoist + chest-pack carry
ry = 610
A(f'<text x="20" y="{ry-20}" class="t">4. Twin-drum reel hoist (~14 kg; 2 parked at the top, 1 spare on the ground)</text>')
A(f'<rect x="40" y="{ry}" width="1160" height="270" fill="none" stroke="#999" stroke-dasharray="4 3"/>')
by = ry + 130
A(f'<rect x="70" y="{by-75}" width="560" height="160" rx="10" fill="#eef3f8" stroke="#222"/>')
for x0 in (100, 220):
    A(f'<rect x="{x0}" y="{by-50}" width="100" height="100" rx="6" fill="#bbb" class="s"/>')
    for j in range(5):
        A(f'<line x1="{x0+10+j*20}" y1="{by-48}" x2="{x0+10+j*20}" y2="{by+48}" stroke="#c0392b" stroke-width="2"/>')
    A(f'<rect x="{x0+15}" y="{by-72}" width="70" height="14" fill="#ddd" class="s"/><text x="{x0+50}" y="{by-61}" text-anchor="middle" font-size="9.5">level wind</text>')
    A(f'<rect x="{x0+35}" y="{by+54}" width="30" height="14" fill="#f2c94c" class="s"/>')
    A(f'<path d="M{x0+50} {by+50} V{by+120}" class="rope" marker-end="url(#ar)"/>')
A(f'<line x1="90" y1="{by}" x2="330" y2="{by}" stroke="#555" stroke-width="5"/>')
A(f'<text x="210" y="{by+138}" text-anchor="middle" font-size="11">2 ropes down through the socket to the hanger sheaves</text>')
A(f'<text x="345" y="{by-54}" font-size="11">2 drums Ø0.1 m on one shaft</text>')
A(f'<rect x="340" y="{by-30}" width="75" height="60" fill="#7fa3d6" class="s"/><text x="377" y="{by+4}" text-anchor="middle" font-size="11">worm</text>')
A(f'<rect x="425" y="{by-30}" width="75" height="60" fill="#7fa3d6" class="s"/><text x="462" y="{by+4}" text-anchor="middle" font-size="11">motor</text>')
A(f'<rect x="510" y="{by-25}" width="40" height="50" fill="#c0392b" class="s"/><text x="530" y="{by+42}" text-anchor="middle" font-size="11">brake</text>')
A(f'<rect x="560" y="{by-25}" width="50" height="50" fill="#ddd" class="s"/><text x="585" y="{by+4}" text-anchor="middle" font-size="10">enc.</text>')
A(f'<line x1="330" y1="{by}" x2="340" y2="{by}" stroke="#555" stroke-width="4"/><line x1="415" y1="{by}" x2="425" y2="{by}" stroke="#555" stroke-width="4"/><line x1="500" y1="{by}" x2="510" y2="{by}" stroke="#555" stroke-width="4"/>')
A(f'<text x="420" y="{by+72}" font-size="10.5">load cell on each rope (yellow)</text>')
specs = ['2 x ~108 m of 2 mm stainless rope, opposite lay:',
         '   ~0.11 kN each, factor ~21; lay torques cancel',
         'One shaft, a dog clutch per drum: equal payout,',
         '   and each rope can be re-equalised in a recovery',
         '~11 N·m, 19 rpm for 0.1 m/s; ~40 W; ~6 Wh per 100 m',
         'Self-locking worm + spring brake hold the pack',
         'Load cells + encoder: slow, automatic approach;',
         '   unequal loads flag a snag or a tilted head',
         'Powered from the socket; parked in the garage',
         '   at the yard root, so the bots climb unladen']
for j, t in enumerate(specs):
    A(f'<text x="{660+(14 if t.startswith(" ") else 0)}" y="{ry+40+j*20}" font-size="12">{t.strip()}</text>')
# chest-pack carry on the ladder (side view)
cx_, cy_ = 1120, ry + 235
A(f'<text x="{cx_-55}" y="{ry+24}" font-size="12" font-weight="bold">Carrying a reel</text>')
A(f'<line x1="{cx_+40}" y1="{ry+35}" x2="{cx_+40}" y2="{ry+262}" stroke="#555" stroke-width="5"/>')
for j in range(6):
    A(f'<line x1="{cx_+40}" y1="{ry+50+j*38}" x2="{cx_+26}" y2="{ry+50+j*38}" stroke="#555" stroke-width="3"/>')
u = 7
A(f'<g stroke="{BOT}" stroke-width="5" stroke-linecap="round" fill="none">'
  f'<polyline points="{cx_+30},{cy_-6} {cx_+8},{cy_-30} {cx_-4},{cy_-70}"/><polyline points="{cx_+30},{cy_-60} {cx_+2},{cy_-80} {cx_-4},{cy_-70}"/>'
  f'<line x1="{cx_-4}" y1="{cy_-70}" x2="{cx_-4}" y2="{cy_-150}"/><polyline points="{cx_-4},{cy_-140} {cx_+18},{cy_-158} {cx_+30},{cy_-180}"/></g>'
  f'<circle cx="{cx_-4}" cy="{cy_-166}" r="12" fill="{BOT}"/>')
A(f'<rect x="{cx_+2}" y="{cy_-138}" width="22" height="40" rx="4" fill="#7fa3d6" class="s"/>')
A(f'<text x="{cx_-60}" y="{cy_+18}" font-size="11">chest pack between</text><text x="{cx_-60}" y="{cy_+31}" font-size="11">the bot and the rungs</text>')
A('</svg>')
open('top-yard.svg', 'w').write('\n'.join(o))
