# Generates erection.svg: freight module packing, flat-pack mast section, and jack-up stages. Run: python3 make_erection_svg.py
o = []
A = o.append
W, H = 1240, 700
A(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Helvetica, Arial, sans-serif" font-size="12.5">')
A(f'<rect width="{W}" height="{H}" fill="#fff"/>')
A('<defs><pattern id="g" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 8L8 0" stroke="#a08c6c"/></pattern>'
  '<marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#222"/></marker></defs>')
A('<style>.s{stroke:#222;stroke-width:1.5}.l{stroke:#555;stroke-width:1;fill:none}.cab{stroke:#8e44ad;stroke-width:1.3}'
  'text{paint-order:stroke;stroke:#fff;stroke-width:4px;stroke-linejoin:round}.t{font-size:15px;font-weight:bold}</style>')

# ---------- 1. freight module with flat-packed mast sections
A('<text x="20" y="32" class="t">1. Freight module (≤3.2 x 1.5 x 1.5 m)</text>')
ox, oy, k = 40, 90, 70
A(f'<rect x="{ox}" y="{oy}" width="{3.2*k}" height="{1.5*k}" fill="none" stroke="#222" stroke-width="2" stroke-dasharray="6 4"/>')
for i in range(12):
    A(f'<rect x="{ox+6}" y="{oy+6+i*8.2}" width="{3.0*k}" height="6" fill="#c87f0a" stroke="#222" stroke-width="0.8"/>')
A(f'<text x="{ox}" y="{oy+1.5*k+20}">~12 flat-packed 3 m mast sections per module;</text>')
A(f'<text x="{ox}" y="{oy+1.5*k+36}">35 sections = 3 modules (vs ~10 rigid).</text>')
A(f'<text x="{ox}" y="{oy+1.5*k+60}">Whole rig ≈ 25 modules: tent-pole struts,</text>')
A(f'<text x="{ox}" y="{oy+1.5*k+76}">base pivot + base frame, packs, reels.</text>')

# ---------- 2. flat-pack section unfolding
A('<text x="20" y="330" class="t">2. Flat-pack section unfolds at the jack frame</text>')
bx, by = 60, 400
A(f'<line x1="{bx}" y1="{by+60}" x2="{bx+150}" y2="{by+60}" stroke="#c87f0a" stroke-width="5"/><text x="{bx+75}" y="{by+84}" text-anchor="middle" font-size="11.5">folded (end view, ~0.12 m)</text>')
A(f'<path d="M{bx+200} {by+60} H{bx+260}" class="l" marker-end="url(#ar)"/>')
tx = bx + 330
A(f'<polygon points="{tx-48},{by+60} {tx+48},{by+60} {tx},{by-23}" fill="none" stroke="#c87f0a" stroke-width="5"/>')
for (x, y) in ((tx - 48, by + 60), (tx + 48, by + 60)):
    A(f'<circle cx="{x}" cy="{y}" r="5" fill="#fff" class="s"/>')
A(f'<circle cx="{tx}" cy="{by-23}" r="6" fill="#f5b700" stroke="#222"/>')
A(f'<text x="{tx}" y="{by+84}" text-anchor="middle" font-size="11.5">unfolded triangle, 1.4 m face</text>')
A(f'<path d="M{tx+8} {by-26} L{tx+70} {by-50}" class="l"/><text x="{tx+72}" y="{by-46}" font-size="11.5">pin the open edge</text><text x="{tx+72}" y="{by-32}" font-size="11.5">(captive pin, one tool)</text>')
A(f'<text x="{bx}" y="{by+120}" font-size="11.5">Faces hinged on two chords; the third chord is pinned on site.</text>')
A(f'<text x="{bx}" y="{by+136}" font-size="11.5">Then the section is pushed into the bottom of the mast.</text>')

# ---------- 3. jack-up stages
gy, e = 640, 5.2
A('<text x="560" y="32" class="t">3. Jack-up: top yard fitted first, rigged, rides up</text>')
stages = [(25, 'Free-standing', False, False), (55, 'Upper collar + stays', True, False), (105, 'Struts scissor up', True, True)]
for i, (top, title, collar, struts) in enumerate(stages):
    mid = 640 + i * 220
    X = lambda m: mid + m * e * 0.8
    Z = lambda m: gy - m * e
    A(f'<text x="{mid}" y="70" text-anchor="middle" font-size="12.5" font-weight="bold">{title}</text>')
    A(f'<rect x="{mid-100}" y="{gy}" width="200" height="22" fill="url(#g)"/><line x1="{mid-100}" y1="{gy}" x2="{mid+100}" y2="{gy}" stroke="#222"/>')
    A(f'<rect x="{mid-16}" y="{gy-16}" width="32" height="16" fill="#9fb4c7" class="s"/>')       # jack frame
    A(f'<rect x="{mid-3}" y="{Z(top)}" width="6" height="{top*e}" fill="#888"/>')
    A(f'<rect x="{mid-17*e*0.8}" y="{Z(top)-3}" width="{34*e*0.8}" height="5" fill="#e0a040" class="s"/>')    # top yard, fitted first: unfolded and rigged
    A(f'<line x1="{mid}" y1="{Z(top)-14}" x2="{mid-17*e*0.8}" y2="{Z(top)-1}" stroke="#555"/><line x1="{mid}" y1="{Z(top)-14}" x2="{mid+17*e*0.8}" y2="{Z(top)-1}" stroke="#555"/><rect x="{mid-3}" y="{Z(top)-14}" width="6" height="14" fill="#888"/>')
    for fx in (-1, 1):
        A(f'<rect x="{X(fx*30)-6}" y="{gy-5}" width="12" height="5" fill="#555"/>')
    if collar:
        cz = top - 43
        A(f'<rect x="{mid-7}" y="{Z(cz)-3}" width="14" height="6" fill="#4a9" class="s"/>')
        for fx in (-1, 1):
            A(f'<line x1="{mid}" y1="{Z(cz)}" x2="{X(fx*30)}" y2="{gy-3}" class="cab"/>')
    if struts:
        A(f'<rect x="{mid-7}" y="{Z(35)-3}" width="14" height="6" fill="#4a9" class="s"/>')
        for fx in (-1, 1):
            A(f'<line x1="{mid}" y1="{Z(35)}" x2="{X(fx*30)}" y2="{gy-3}" stroke="#555" stroke-width="3"/>')
    A(f'<text x="{mid}" y="{gy+40}" text-anchor="middle" font-size="11.5">top at {top} m</text>')
A(f'<path d="M{640+30} {gy-20} V{gy-100}" stroke="#222" stroke-width="1.5" marker-end="url(#ar)"/>')
A(f'<text x="{640+36}" y="{gy-60}" font-size="11">jack</text>')
A(f'<text x="560" y="{gy+48+20}" font-size="12">0–43 m free-standing: 31x buckling margin. Peak jack force ~10 kN. ~1 h per 3 m section (~35 h).</text>')
A('</svg>')
open('erection.svg', 'w').write('\n'.join(o))
