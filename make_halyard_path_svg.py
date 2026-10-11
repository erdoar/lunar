# Generates halyard-path.svg (superseded, Appendix B): one halyard from the base-frame winch, up the mast, along the yard, down to the wing.
o = []
A = o.append
W, H = 1000, 640
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12.5">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#c0392b"/></marker>'
  '<pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern></defs>')
A('<style>.s{stroke:#222;stroke-width:1.5}.l{stroke:#555;stroke-width:1;fill:none}.hal{stroke:#c0392b;stroke-width:2.5;fill:none}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')
mx, top, deck = 300, 90, 560        # mast centre x, yard y, deck y
A('<text x="20" y="30" class="t">Halyard path: the rope is the transmission (one of 4 shown)</text>')
A(f'<rect x="{mx-30}" y="{top-40}" width="60" height="{deck-top+40}" fill="none" stroke="#888" stroke-width="2"/>')
for y in range(top - 40, deck, 30):
    A(f'<line x1="{mx-30}" y1="{y}" x2="{mx+30}" y2="{y+30}" stroke="#ccc"/>')
    A(f'<ellipse cx="{mx}" cy="{y+15}" rx="9" ry="3" fill="none" stroke="#4a9" stroke-width="2"/>')
A(f'<rect x="{mx}" y="{top-6}" width="600" height="14" fill="none" stroke="#c87f0a" stroke-width="3"/>')
A(f'<circle cx="{mx}" cy="{top}" r="9" fill="#fff" class="s"/>')
A(f'<circle cx="{mx+560}" cy="{top+8}" r="9" fill="#fff" class="s"/>')
for xr in (mx + 200, mx + 380):
    A(f'<circle cx="{xr}" cy="{top+5}" r="4" fill="#fff" stroke="#222"/>')
A(f'<rect x="{mx+430}" y="{top+150}" width="250" height="10" fill="#e0a040" class="s"/><path d="M{mx+560} {top+150} l-8 -14 h16 z" fill="#e0a040" stroke="#222"/>')
A(f'<rect x="{mx+430}" y="{top+160}" width="250" height="140" fill="#2c4a7a" opacity="0.85"/>')
A(f'<rect x="{mx-60}" y="{deck}" width="300" height="20" fill="#9fb4c7" class="s"/><rect x="{mx-120}" y="{deck+20}" width="560" height="40" fill="url(#g)"/>')
A(f'<ellipse cx="{mx}" cy="{deck-14}" rx="26" ry="14" fill="#bbb" class="s"/><rect x="{mx+40}" y="{deck-30}" width="44" height="30" fill="#9fb4c7" class="s"/><rect x="{mx+90}" y="{deck-28}" width="36" height="26" fill="#7fa3d6" class="s"/>')
A(f'<path d="M{mx} {deck-28} V{top} H{mx+560} V{top+136}" class="hal" marker-end="url(#ar)"/>')
def lab(x1, y1, x2, y2, lines, anchor='start'):
    A(f'<path d="M{x1:.0f} {y1:.0f}L{x2:.0f} {y2:.0f}" class="l"/>')
    for j, t in enumerate(lines):
        A(f'<text x="{x2+(4 if anchor=="start" else -4):.0f}" y="{y2+4+j*15:.0f}" text-anchor="{anchor}">{t}</text>')
lab(mx - 26, deck - 14, mx - 80, deck - 50, ['1. Traction sheave on the', 'rotating base frame'], 'end')
lab(mx - 9, 330, mx - 80, 330, ['2. Up the clear centre of the', 'lattice, ceramic guide ring', 'every 3 m (~23 N rope weight)'], 'end')
lab(mx - 9, top, mx - 80, top - 20, ['3. Turning block at', 'the yard-mast, 100 m'], 'end')
lab(mx + 200, top + 5, mx + 200, top + 50, ['4. Inside the yard on guide rollers'])
lab(mx + 569, top + 8, mx + 610, top + 50, ['5. End sheave', '(2 m or 17 m out),', 'turns down'])
lab(mx + 560, top + 140, mx + 610, top + 120, ['Cone on the wing', 'top bar (docks', 'under the yard)'])
A(f'<text x="{mx+120}" y="{deck-40}" font-size="11.5">gearbox + motors</text>')
A(f'<text x="20" y="{H-20}" font-size="12">Base frame, mast and yard turn together: no rope crosses a rotating joint. Flat-pack sections unfold around the 4-rope bundle during jack-up.</text>')
A('</svg>')
open('halyard-path.svg', 'w').write('\n'.join(o))
