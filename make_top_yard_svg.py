# Generates top-yard.svg (rev 17): front elevation, side view, docking latch, panel elevation winch.
# Run: python3 make_top_yard_svg.py
o = []
A = o.append
W, H = 1240, 920
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:1.5}.l{stroke:#555;stroke-width:1;fill:none}.w{stroke:#555;stroke-width:1.4}'
  '.hal{stroke:#c0392b;stroke-width:1.6;fill:none}.yard{stroke:#c87f0a;stroke-width:3}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')


def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*14:.0f}" text-anchor="{anchor}">{t}</text>')


# ---------------- 1. front elevation (wing plane)
k, cx = 16.5, 330
Zb = 92
X = lambda m: cx + m * k
Z = lambda m: 400 - (m - Zb) * k
A('<text x="20" y="30" class="t">1. Front elevation (wing plane), 92–108 m</text>')
A(f'<rect x="{X(-0.7)}" y="{Z(108)}" width="{1.4*k}" height="{(108-Zb)*k}" fill="none" stroke="#888" stroke-width="2"/>')
for z in range(Zb, 108, 1):
    A(f'<line x1="{X(-0.7)}" y1="{Z(z)}" x2="{X(0.7)}" y2="{Z(z+1)}" stroke="#aaa"/>')
# yard truss
for zc in (100.4, 99.6):
    A(f'<line x1="{X(-17)}" y1="{Z(zc)}" x2="{X(17)}" y2="{Z(zc)}" class="yard"/>')
for i in range(-17, 17):
    A(f'<line x1="{X(i)}" y1="{Z(100.4)}" x2="{X(i+1)}" y2="{Z(99.6)}" stroke="#c87f0a" stroke-width="1"/>')
# topping lifts
for sx in (-1, 1):
    A(f'<line x1="{X(0)}" y1="{Z(108)}" x2="{X(sx*17)}" y2="{Z(100.4)}" class="w"/>')
A(f'<circle cx="{X(0)}" cy="{Z(108)}" r="4" fill="#555"/>')
# sheaves, docks, docked top bars, halyards inside the yard and down the mast
for sx in (-1, 1):
    for r in (2, 17):
        x = X(sx * r)
        A(f'<circle cx="{x}" cy="{Z(99.6)+6}" r="5" fill="#fff" class="s"/>')                    # sheave
        A(f'<path d="M{x-8} {Z(99.6)+12} h16 l-4 8 h-8 z" fill="#4a9" stroke="#222"/>')           # dock
    xl, xr = sorted((X(sx * 2), X(sx * 17)))
    A(f'<rect x="{xl-4}" y="{Z(99.6)+20}" width="{xr-xl+8}" height="7" fill="#e0a040" class="s"/>')   # wing top bar (docked)
    A(f'<rect x="{xl}" y="{Z(99.6)+27}" width="{xr-xl}" height="{(99.0-Zb)*k-27}" fill="#2c4a7a" opacity="0.85"/>')
    for j in range(1, 8):
        xx = xl + j * (xr - xl) / 8
        A(f'<line x1="{xx}" y1="{Z(99.6)+27}" x2="{xx}" y2="{Z(Zb)}" stroke="#7fa3d6"/>')
    A(f'<path d="M{X(sx*17)} {Z(99.6)+6} H{X(sx*0.4)}" class="hal"/>')
    A(f'<path d="M{X(sx*2)} {Z(99.6)+6} H{X(sx*0.4)}" class="hal" stroke-dasharray="1 0"/>')
A(f'<path d="M{X(-0.3)} {Z(99.6)+6} V{Z(Zb)}" class="hal" stroke-dasharray="6 3"/><path d="M{X(0.3)} {Z(99.6)+6} V{Z(Zb)}" class="hal" stroke-dasharray="6 3"/>')
A(f'<circle cx="{X(0)}" cy="{Z(99.6)+6}" r="6" fill="#fff" class="s"/>')
lab(X(0) + 4, Z(108), X(3), Z(108.6), ['Masthead, 108 m (8 m above yard)'])
lab(X(-9), Z(104.2), X(-12), Z(107), ['Topping lift ~3.0 kN'], 'end')
lab(X(7), Z(100.4), X(7.5), Z(103.6), ['Yard truss 34 m, 0.8 m deep,', '~2.7 kN compression'])
lab(X(17), Z(99.6) + 6, X(15), Z(97.6), ['Sheave + dock'], 'end')
lab(X(-10), Z(99.6) + 6, X(-12), Z(97.4), ['Halyards run inside the yard'], 'end')
lab(X(0.3), Z(95), X(3), Z(95.5), ['…then down inside the mast', 'to the base-frame winch'])
lab(X(-9), Z(99.6) + 24, X(-12), Z(94.2), ['Wing top bar, docked', '(weight on the yard)'], 'end')
A(f'<text x="{X(-17)}" y="{Z(Zb)+18}" font-size="11.5">Wing packs hang below (30 m, shortened here)</text>')

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
A(f'<rect x="{SX(-0.15)}" y="{SZ(100)}" width="{0.3*sk}" height="{30*sk*0.33}" fill="#2c4a7a"/>')
A(f'<rect x="{SX(-1.2)}" y="{SZ(62)-4}" width="{2.4*sk}" height="8" fill="#4a9" class="s"/>')
lab(SX(0) + 4, SZ(100), SX(2.5), SZ(104), ['Yard (end-on)'])
lab(SX(4), SZ(87), SX(6.5), SZ(95), ['Braces: yard tips', 'to spreader tips'])
lab(SX(6), SZ(81), SX(7.5), SZ(79), ['Spreaders ±6 m, 81 m'])
lab(SX(3), SZ(72.5), SX(5), SZ(68), ['Diamond stays', '64 → 81 → 108 m'])
lab(SX(1.2), SZ(62), SX(3), SZ(61), ['Upper collar, 62 m'])
lab(SX(0), SZ(78), SX(-2), SZ(74), ['Wings', '(edge-on)'], 'end')

# ---------------- 3. docking latch
dx, dy = 1080, 80
A(f'<text x="{dx-120}" y="30" class="t">3. Docking latch (no power)</text>')
for i, (title, latched) in enumerate((('Docked', True), ('Push to release', False))):
    x = dx - 60 + i * 120
    A(f'<text x="{x}" y="{dy}" text-anchor="middle" font-size="11.5" font-weight="bold">{title}</text>')
    A(f'<rect x="{x-35}" y="{dy+10}" width="70" height="26" fill="#c87f0a" class="s"/>')                   # yard chord
    A(f'<path d="M{x-24} {dy+36} h48 l-10 22 h-28 z" fill="#4a9" stroke="#222"/>')                          # dock
    cy_ = dy + 40 if latched else dy + 80
    A(f'<path d="M{x} {cy_} l-12 18 h24 z" fill="#e0a040" stroke="#222"/>')                                  # cone
    A(f'<rect x="{x-30}" y="{cy_+18}" width="60" height="9" fill="#e0a040" class="s"/>')                    # top bar
    jaw = 'M{0} {1} l10 0'.format(x - 22, dy + 54) if latched else 'M{0} {1} l4 -10'.format(x - 22, dy + 54)
    A(f'<path d="{jaw}" stroke="#c0392b" stroke-width="4"/>')
    A(f'<line x1="{x+12}" y1="{cy_+27}" x2="{x+12}" y2="{dy+190}" class="hal"/>')
A(f'<text x="{dx-120}" y="{dy+215}" font-size="11.5">Hoist ~50 mm past the dock: the latch</text>')
A(f'<text x="{dx-120}" y="{dy+230}" font-size="11.5">toggles (shut, then open next time).</text>')
A(f'<text x="{dx-120}" y="{dy+245}" font-size="11.5">Like a ballpoint pen; limit switch</text>')
A(f'<text x="{dx-120}" y="{dy+260}" font-size="11.5">confirms the state.</text>')

# ---------------- 4. panel elevation winch (deck)
wy = 520
A(f'<text x="20" y="{wy-20}" class="t">4. Panel elevation winch (on the rotating base frame at the mast base)</text>')
A(f'<rect x="40" y="{wy}" width="1160" height="380" fill="none" stroke="#999" stroke-dasharray="4 3"/>')
shaft_y = wy + 170
A(f'<line x1="200" y1="{shaft_y}" x2="1020" y2="{shaft_y}" stroke="#555" stroke-width="8"/>')
labels = ('Port outer', 'Port inner', 'Stbd inner', 'Stbd outer')
for i, name in enumerate(labels):
    x = 300 + i * 190
    A(f'<ellipse cx="{x}" cy="{shaft_y}" rx="28" ry="60" fill="#bbb" class="s"/>')                         # traction sheave
    for g_ in range(3):
        A(f'<line x1="{x-22+g_*22}" y1="{shaft_y-58}" x2="{x-22+g_*22}" y2="{shaft_y+58}" stroke="#777"/>')
    A(f'<line x1="{x}" y1="{shaft_y-60}" x2="{x}" y2="{wy+15}" class="hal"/>')                              # up the mast
    A(f'<rect x="{x+40}" y="{shaft_y+75}" width="60" height="40" rx="18" fill="#ddd" class="s"/>')        # storage reel
    A(f'<path d="M{x+10} {shaft_y+58} Q{x+30} {shaft_y+95} {x+40} {shaft_y+95}" class="hal"/>')
    A(f'<text x="{x}" y="{wy+12}" text-anchor="middle" font-size="11">{name}</text>')
    A(f'<text x="{x+70}" y="{shaft_y+132}" text-anchor="middle" font-size="10.5">storage reel</text>')
A(f'<rect x="1030" y="{shaft_y-40}" width="70" height="80" fill="#9fb4c7" class="s"/><text x="1065" y="{shaft_y+4}" text-anchor="middle" font-size="11">gearbox</text><text x="1065" y="{shaft_y+18}" text-anchor="middle" font-size="11">~600:1</text>')
A(f'<rect x="1110" y="{shaft_y-55}" width="60" height="45" fill="#7fa3d6" class="s"/><text x="1140" y="{shaft_y-28}" text-anchor="middle" font-size="11">motor 1</text>')
A(f'<rect x="1110" y="{shaft_y+10}" width="60" height="45" fill="#7fa3d6" class="s"/><text x="1140" y="{shaft_y+37}" text-anchor="middle" font-size="11">motor 2</text>')
A(f'<rect x="150" y="{shaft_y-30}" width="40" height="60" fill="#c0392b" class="s"/><text x="170" y="{shaft_y+48}" text-anchor="middle" font-size="11">brake</text>')
A(f'<circle cx="110" cy="{shaft_y}" r="12" fill="#fff" class="s"/><text x="110" y="{shaft_y+30}" text-anchor="middle" font-size="11">hand crank</text><line x1="122" y1="{shaft_y}" x2="150" y2="{shaft_y}" stroke="#555" stroke-width="4"/>')
A(f'<text x="60" y="{wy+345}" font-size="12">One shaft, 4 grooved traction sheaves (Ø0.4 m, 3 wraps): exactly equal stroke on all 4 halyards, so both wings move together and stay level.</text>')
A(f'<text x="60" y="{wy+363}" font-size="12">0.1 m/s = 4.8 rpm, ~890 N·m; 2 x 0.5 kW motors (either suffices), spring-applied brake, load cells and encoders on every halyard.</text>')
A('</svg>')
open('top-yard.svg', 'w').write('\n'.join(o))
